"""Embed data/gold_typicals.json and data/copper_typicals.json in index.html, in the same shape as LI_TYPICALS.
Run after tools/compile_typicals_au_cu.py: python3 -I tools/embed_typicals_au_cu.py"""
import json, re

P = 'index.html'
s = open(P, encoding='utf-8').read()


def table(path):
    d = json.load(open(path, encoding='utf-8'))
    t = {k: {**{x: v[x] for x in ('label', 'unit', 'median', 'low', 'high', 'n', 'note')}, 'points': [[p['study'], p['value'], p['page'], p['working']] for p in v['points']]} for k, v in d['typicals'].items()}
    return t, d['studies']


gold, gs = table('data/gold_typicals.json')
copper, cs = table('data/copper_typicals.json')
names = {k: {'source': v, 'url': ''} for k, v in {**gs, **cs}.items()}
line = lambda name, obj, note: f"const {name} = {json.dumps(obj, ensure_ascii=False, separators=(',', ':'))};   // {note}"
s, n1 = re.subn(r"^const AU_TYPICALS = .*$", lambda m: line('AU_TYPICALS', gold, 'gold: generated from data/gold_typicals.json'), s, count=1, flags=re.M)
s, n2 = re.subn(r"^const CU_TYPICALS = .*$", lambda m: line('CU_TYPICALS', copper, 'copper: generated from data/copper_typicals.json'), s, count=1, flags=re.M)
s, n3 = re.subn(r"^const STUDY_NAMES = .*$", lambda m: line('STUDY_NAMES', names, 'gold and copper study keys, as LI_STUDIES does for lithium'), s, count=1, flags=re.M)
assert (n1, n2, n3) == (1, 1, 1), (n1, n2, n3)
open(P, 'w', encoding='utf-8').write(s)
print('embedded', len(gold), 'gold and', len(copper), 'copper values')
