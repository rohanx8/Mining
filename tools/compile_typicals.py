"""Compile lithium (spodumene) typical values from the study extractions in data/studies.
Every number below is copied from a study JSON (with its page) or derived from them with the working shown.
FX: each study's own assumption (US$ per local unit). Run: python3 -I tools/compile_typicals.py"""
import json, statistics as st
FX = {"S02": 1.0, "S03": 1.0, "S05": 0.76, "S06": 0.70, "S06b": 0.70, "S07": 1.0, "S11": 0.67, "S11n": 0.69}
NAME = {"S02": "Ewoyaa DFS 2023 (Ghana)", "S03": "Bougouni FS 2020 (Mali)", "S05": "Shaakichiuwaanaan PEA 2024 (Quebec)",
        "S06": "Finniss restart study 2025 (NT)", "S06b": "Finniss DFS 2021 (NT)", "S07": "Rose FS 2023 (Quebec)",
        "S11": "Manna DFS 2025 (WA)", "S11n": "Manna-Nova integration study 2026 (WA)",
        "PLS": "PLS Pilgangoora, Sep Q 2026 actuals (WA)", "LTR": "Liontown Kathleen Valley, Sep Q 2026 actuals (WA)"}
def pt(study, value, page, working):
    return {"study": study, "name": NAME[study], "value": round(value, 3), "page": page, "working": working}
def summarise(label, unit, points, note=""):
    vals = [p["value"] for p in points]
    return {"label": label, "unit": unit, "median": round(st.median(vals), 3), "low": min(vals), "high": max(vals), "n": len(vals), "note": note, "points": points}
T = {}
T["recovery_dms"] = summarise("Lithia recovery, dense-media separation (DMS) only", "%", [
    pt("S02", 62.1, 38, "to SC6 (67.2% to SC5.5)"), pt("S05", 69.5, 11, "LOM average"), pt("S06", 78.0, 4, "global"),
    pt("S06b", 71.7, 2, "DFS"), pt("S11", 72.8, 46, "ore sorting + DMS, LOM"), pt("S11n", 72.85, 16, "ROM to product")],
    "Operating benchmarks: Kathleen Valley 60-63% in ramp-up (Liontown Sep Q 2026, p2).")
T["recovery_flotation"] = summarise("Lithia recovery, with flotation", "%", [
    pt("S03", 71.0, 4, "flotation, no DMS"), pt("S07", 87.4, 3, "conventional flotation"), pt("PLS", 74.7, 2, "Sep Q 2026 actual, DMS + flotation")],
    "PLS last five quarters 74.7-78.2% (p8).")
T["head_grade"] = summarise("Head grade to plant", "% Li2O", [
    pt("S02", 1.22, 22, ""), pt("S03", 1.03, 4, ""), pt("S05", 1.31, 11, ""), pt("S06", 1.27, 4, ""),
    pt("S06b", 1.31, 2, ""), pt("S07", 0.87, 3, ""), pt("S11", 0.88, 68, ""), pt("LTR", 1.3, 2, "Sep Q 2026 actual")])
T["mining_cost_op_per_t_material"] = summarise("Open-pit mining cost per tonne of material moved (ore + waste)", "US$/t", [
    pt("S02", 3.82, 38, "US$3.82/t mined"), pt("S03", 2.63, 3, "US$2.63/t material"),
    pt("S07", 27.05 / (1 + 7.3), 3, "US$27.05/t ore ÷ (1 + strip 7.3)"),
    pt("S11", 73 * 0.67 / (1 + 14.9), 9, "A$73/t ore × 0.67 ÷ (1 + strip 14.9)")])
T["mining_cost_ug_per_t_ore"] = summarise("Underground mining cost per tonne of ore", "US$/t", [
    pt("S06", 67.5 * 0.70, 4, "A$63-72/t mined, mid A$67.5 × 0.70"), pt("S11", 84 * 0.67, 9, "A$84/t ore × 0.67")])
T["processing_cost_dms"] = summarise("Processing cost, DMS route, per tonne of ore", "US$/t", [
    pt("S02", 7.77, 38, ""), pt("S06", 43 * 0.70, 4, "A$40-46/t incl. tailings, mid × 0.70"),
    pt("S11", 30 * 0.67, 9, "A$30/t incl. site G&A × 0.67"), pt("S11n", 28.4 * 0.69, 16, "A$28.4/t crushed × 0.69")])
T["processing_cost_flotation"] = summarise("Processing cost, flotation route, per tonne of ore", "US$/t", [
    pt("S03", 16.33, 3, ""), pt("S07", 20.79, 3, "")])
T["site_ga_per_t_ore"] = summarise("Site G&A per tonne of ore", "US$/t", [
    pt("S02", 47 * 3.58 / 30.6, 38, "US$47/t conc × 3.58 Mt conc ÷ 30.6 Mt ore"), pt("S03", 2.92, 3, ""),
    pt("S06", 9.5 * 0.70, 4, "A$9-10/t, mid × 0.70"), pt("S07", 15.94, 3, "remote James Bay")])
T["capex_per_annual_t_ore"] = summarise("Initial capex per tonne of annual ore capacity", "US$ per t/yr", [
    pt("S02", 185.2e6 / 2.7e6, 41, "US$185.2M ÷ 2.7 Mtpa"), pt("S03", 128.6e6 / 2.0e6, 4, "US$128.6M ÷ 2.0 Mtpa"),
    pt("S06b", 88.9e6 * 0.70 / 1.0e6, 32, "A$88.9M × 0.70 ÷ 1.0 Mtpa"), pt("S06", 187.5e6 * 0.70 / 1.2e6, 4, "A$175-200M mid × 0.70 ÷ 1.2 Mtpa (restart, underground)"),
    pt("S07", 470.6e6 / 1.61e6, 12, "US$470.6M ÷ 1.61 Mtpa (remote Quebec)"), pt("S11", 439.1e6 * 0.67 / 1.8e6, 81, "A$439.1M × 0.67 ÷ 1.8 Mtpa"),
    pt("S11n", 180.1e6 * 0.69 / 2.1e6, 4, "A$180.1M × 0.69 ÷ 2.1 Mtpa (converting an existing plant)")],
    "Greenfield sites need their own power, camp and roads; the integration case shows how much existing infrastructure saves.")
T["contingency_pct"] = summarise("Capex contingency, % of initial capex", "%", [
    pt("S02", 12.2 / 185.2 * 100, 41, "US$12.2M ÷ 185.2M"), pt("S03", 11.7 / 116.9 * 100, 4, "10% on US$116.9M"),
    pt("S05", 162.9 / 761.4 * 100, 12, "C$162.9M ÷ 761.4M (PEA)"), pt("S07", 42.7 / 470.6 * 100, 12, ""),
    pt("S11", 39.93 / 439.1 * 100, 81, "growth + contingency"), pt("S11n", 16.4 / 180.1 * 100, 4, "")],
    "PEA ~21%; feasibility studies 7-10%.")
T["road_haul_per_t_km"] = summarise("Road haulage rate per tonne-kilometre", "US$/t-km", [
    pt("S06b", 8.62 / 88.31 * 0.70, 83, "A$8.62/t ÷ 88.31 km × 0.70 (2021, road only)"),
    pt("S06", 23.5 / 88 * 0.70, 4, "A$22-25/t ÷ 88 km × 0.70 (2025; may include port charges)"),
    pt("S11n", 17.01 / 135 * 0.69, 80, "A$17.01/t ore ÷ 135 km × 0.69 (140 t road trains, dedicated corridor)"),
    pt("S02", 29.81 / 110, 39, "US$29.81/t ÷ ~110 km, site to ship incl. port loading")],
    "Long hauls: Shaakichiuwaanaan pays C$226/t (US$172) for 834 km of road plus a rail leg to Bécancour (PEA p14, p64).")
T["ocean_freight"] = summarise("Ocean freight to Asia, per tonne of concentrate", "US$/t", [
    pt("S06b", 20, 38, "Darwin, 2021"), pt("S11", 30, 84, "Esperance, 2025")])
T["sustaining_capex_per_t_conc"] = summarise("Sustaining capex per tonne of concentrate", "US$/t", [
    pt("S03", 9, 4, ""), pt("S05", 44 * 0.76, 14, "C$44/t × 0.76"), pt("S06b", 41, 34, "incl. underground development"),
    pt("S11", 28.5 * 0.67, 83, "A$28.5/t incl. closure × 0.67"), pt("S02", 112.2e6 / 3.58e6, 42, "US$112.2M ÷ 3.58 Mt conc (incl. US$98.9M resettlement)"),
    pt("S07", 237.8e6 / (203765 * 17), 12, "US$237.8M ÷ (203.8 kt × 17 yr)")])
T["strip_ratio_op"] = summarise("Open-pit strip ratio (waste : ore)", "x", [
    pt("S02", 12.3, 14, ""), pt("S05", 3.7, 1, "open-pit portion"), pt("S07", 7.3, 6, ""), pt("S11", 14.9, 57, ""),
    pt("PLS", 6.7, 2, "(11.5 - 1.5) ÷ 1.5, Sep Q 2026")])
T["discount_rate"] = summarise("Discount rate used by the study (real)", "%", [
    pt("S02", 8, 4, ""), pt("S03", 7, 5, ""), pt("S05", 8, 11, ""), pt("S06b", 8, 2, ""), pt("S07", 8, 3, ""), pt("S11", 8, 84, ""), pt("S11n", 8, 4, "")])
out = {"about": "Typical values for the lithium deposit screener, compiled from data/studies/*.json by tools/compile_typicals.py. Medians across studies; each point keeps its study and page. Converted to US$ at each study's own FX assumption.",
       "fx_used": FX, "typicals": T,
       "fiscal_presets": {
          "Australia (WA)": {"royalty": "5% of revenue on spodumene concentrate (Manna-Nova p83)", "income_tax": "30%", "studies": ["S11", "S11n"]},
          "Australia (NT)": {"royalty": "NT Mineral Royalty Act 1982 hybrid: greater of 20% of net value less A$10,000, or 2.5% of gross (Finniss restart p51)", "income_tax": "30% (Finniss DFS p36)", "studies": ["S06", "S06b"]},
          "Ghana": {"royalty": "5% government + 1% Growth and Sustainability levy (+ 1% and 1% capped third-party royalties)", "income_tax": "35%", "state": "10% free carry", "studies": ["S02"]},
          "Mali (2020, pre-2023 code)": {"royalty": "3% government + 0.5% local partner + 3% ISCP turnover tax", "income_tax": "25%", "note": "Pre-dates Mali's 2023 mining code", "studies": ["S03"]},
          "Canada (Quebec)": {"royalty": "2% (Shaakichiuwaanaan PEA p42); Rose reports royalties of US$28/t and a 41.7% effective tax rate including Quebec mining tax", "studies": ["S05", "S07"]}
       }}
json.dump(out, open("data/lithium_typicals.json", "w"), ensure_ascii=False, indent=1)
for k, t in T.items(): print(f"{t['label'][:62]:62s} median {t['median']:>9} {t['unit']:14s} range {t['low']}-{t['high']} (n={t['n']})")
