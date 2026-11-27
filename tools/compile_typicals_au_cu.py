"""Compile gold and copper typical values from the study research in data/research (gold_studies.json, copper_studies.json,
unit_costs.json). Every value below is copied from those files, which record the page each came from as returned by web search
in November 2026 (not checked page by page against the filings), or derived from them with the working shown.
Only figures stated in US$ (or without currency, such as recoveries and grades) are used: the A$ and C$ figures came without
the study's exchange rate. Costs from studies dated 2024 or earlier are brought to November 2025 prices with US CPI-U,
as the lithium values are. Run: python3 -I tools/compile_typicals_au_cu.py"""
import json, statistics as st

CPI = {2020: 258.811, 2021: 270.970, 2022: 292.655, 2023: 304.702, 2024: 313.689}
CPI_TARGET = 324.122
NAME = {
    "G01": "Montage Gold, Koné Updated FS (Feb 2024), Côte d'Ivoire",
    "G02": "Predictive Discovery, Bankan DFS (Jun 2025), Guinea",
    "G03": "Fortuna Mining, Diamba Sud FS (Jun 2026), Senegal",
    "G04": "Saturn Metals, Apollo Hill PFS (Dec 2025), Western Australia",
    "G05": "Rox Resources, Youanmi DFS (Nov 2025), Western Australia",
    "G06": "Ausgold, Katanning updated DFS (Dec 2025), Western Australia",
    "G07": "Osisko Development, Cariboo optimised FS (Apr 2025), British Columbia",
    "G08": "First Mining Gold, Springpole updated PFS (Nov 2025), Ontario",
    "C01": "Hot Chili, Costa Fuego PFS (Mar 2025), Chile",
    "C02": "Los Andes Copper, Vizcachitas PFS (Feb 2023), Chile",
    "C03": "Highland Copper, Copperwood FS update (Mar 2023), Michigan",
    "C04": "Western Copper and Gold, Casino FS (Jun 2022), Yukon",
    "C05": "New World Resources, Antler PFS (Jul 2024), Arizona",
    "C06": "Caravel Minerals, Caravel PFS (2022-23), Western Australia",
    "C07": "SolGold, Cascabel PFS (Feb 2024), Ecuador",
}
YEAR = {"C02": 2023, "C03": 2023}


def esc(study):
    y = YEAR.get(study)
    return (CPI_TARGET / CPI[y], f"; x CPI {CPI_TARGET / CPI[y]:.3f} ({y} to Nov 2025 prices)") if y else (1.0, "")


def pt(study, value, working="", cost=False):
    f, note = esc(study) if cost else (1.0, "")
    return {"study": study, "name": NAME[study], "value": round(value * f, 3), "page": None, "working": (working + note).strip("; ")}


def summarise(label, unit, points, note=""):
    vals = [p["value"] for p in points]
    return {"label": label, "unit": unit, "median": round(st.median(vals), 3), "low": min(vals), "high": max(vals), "n": len(vals), "note": note, "points": points}


SEARCH = "From the company's announcement as web search returned it; page not checked."
G = {}
G["recovery_cil"] = summarise("Gold recovery, mill (CIL/CIP)", "%", [
    pt("G02", 92.8, "LOM average"), pt("G03", 91.0, "CIL"), pt("G05", 90.8, "plant metallurgical recovery"), pt("G06", 90.4, "")], SEARCH)
G["recovery_heap"] = summarise("Gold recovery, heap leach", "%", [pt("G04", 73.7, "heap leach")], SEARCH)
G["processing_cost_cil"] = summarise("Processing cost, mill (CIL/CIP), per tonne of ore", "US$/t", [
    pt("G03", 16.09, "US$/t processed, 2.26 Mtpa", True), pt("G08", 10.72, "US$/t processed, 30,000 t/d", True)], SEARCH + " Scale matters: the larger plant is cheaper per tonne.")
G["site_ga_per_t_ore"] = summarise("Site G&A per tonne of ore", "US$/t", [
    pt("G03", 8.65, "US$/t processed", True), pt("G08", 2.56, "US$/t (basis not stated; likely per tonne processed)", True)], SEARCH)
G["capex_per_annual_t_ore"] = summarise("Initial capex per tonne of annual ore capacity", "US$ per t/yr", [
    pt("G03", 397.5 / 2.26, "US$397.5M / 2.26 Mtpa", True), pt("G08", 1104 / (30000 * 365 / 1e6), "US$1,104M / 10.95 Mtpa (30,000 t/d)", True)], SEARCH)
G["closure_usd_m"] = summarise("Closure cost", "US$M", [pt("G08", 40, "", True)], SEARCH)
G["strip_ratio_op"] = summarise("Open-pit strip ratio (waste : ore)", "x", [pt("G02", 1.9, ""), pt("G04", 2.4, ""), pt("G08", 3.0, "overall")], SEARCH)
G["discount_rate"] = summarise("Discount rate used by the study", "%", [
    pt("G02", 5, ""), pt("G03", 5, ""), pt("G04", 8, ""), pt("G06", 5, ""), pt("G07", 5, ""), pt("G08", 5, "")], SEARCH)

C = {}
C["recovery_cu"] = summarise("Copper recovery to concentrate", "%", [pt("C01", 86, "sulphide concentrator"), pt("C02", 91.1, ""), pt("C03", 86, "")], SEARCH)
C["conc_grade_cu_pct"] = summarise("Concentrate grade", "% Cu", [pt("C02", 24.5, ""), pt("C03", 25, ""), pt("C06", 25, "approximately 25%")], SEARCH)
C["payability_cu_pct"] = summarise("Copper payability", "%", [pt("C03", 96.5, "")], SEARCH)
C["capex_per_annual_t_ore"] = summarise("Initial capex per tonne of annual ore capacity", "US$ per t/yr", [
    pt("C01", 1270 / 20.7, "US$1,270M / 20.7 Mtpa", True), pt("C02", 2441 / 49.64, "US$2,441M / 49.64 Mtpa (136,000 t/d)", True),
    pt("C03", 391 / 2.482, "US$391M / 2.48 Mtpa (6,800 t/d), underground", True)], SEARCH + " Big open pits sit at the bottom; small underground mines at the top.")
C["mining_cost_ug_per_t_ore"] = summarise("Underground mining cost per tonne of ore", "US$/t", [pt("C03", 24.02, "LOM average", True)], SEARCH)
C["sustaining_capex_per_lb"] = summarise("Sustaining capex per pound of copper", "US$/lb", [
    pt("C02", 1500e6 / (152.883e3 * 26 * 2204.62262), "US$1,500M / (152.9 kt a year x 26 years x 2,204.6 lb/t); copper produced, payable share not stated", True)], SEARCH)
C["strip_ratio_op"] = summarise("Open-pit strip ratio (waste : ore)", "x", [pt("C06", 1.3, "including pre-strip")], SEARCH)
C["discount_rate"] = summarise("Discount rate used by the study", "%", [
    pt("C01", 8, ""), pt("C02", 8, ""), pt("C03", 8, ""), pt("C04", 8, ""), pt("C05", 7, ""), pt("C06", 7, "real"), pt("C07", 8, "")], SEARCH)

for path, data in (("data/gold_typicals.json", G), ("data/copper_typicals.json", C)):
    json.dump({"about": __doc__.strip(), "studies": {k: v for k, v in NAME.items() if k[0] == path[5].upper()}, "typicals": data}, open(path, "w"), indent=1, ensure_ascii=False)
    print(path, len(data), "values")
