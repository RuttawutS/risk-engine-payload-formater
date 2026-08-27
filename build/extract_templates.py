"""Extract base REQUEST payloads from representative CRA logs -> templates.json"""
import json, re
from pathlib import Path

BASE = Path(r"D:\work\luna\documents\credit_scoring_engine\example_test_data\Ex.Log CRA-20260513T160519Z-3-001\Ex.Log CRA")

# combo key -> representative log file (prefer clean A1 approve cases)
SRC = {
    "MICRO|CA1":      "1 Micro_A1_API2_CA1_CRA.log",
    "MICRO|CA2":      "4 Micro_A1_API6_CA2_CRA.log",
    "SME-LOWER|CA2":  "1 Lower_A1_API6_CRA.log",
    "SME-UPPER1|CA2": "1 Upper1_A1_API6_CRA.log",
    "SME-M|CA2":      "1 Medium_A1_API6_CA2_CRA.log",
    "SME-L|CA2":      "1 Large_A1_API6_CA2_CRA.log",
    "SME-UPPER2|CA2": "1 Upper2_A1_API6_CA2_CRA.log",
}

def parse_request(path: Path):
    text = path.read_text(encoding="utf-8", errors="replace")
    m = re.search(r'\*\*\*REQUEST\*\*\*\s*\n(\{.*)', text, re.DOTALL)
    raw = text[m.start(1):]
    cut = re.search(r'\n\*\*\*RESPONSE\*\*\*', raw)
    raw = raw[:cut.start()] if cut else raw
    return json.loads(raw.strip())

templates = {}
for key, fname in SRC.items():
    req = parse_request(BASE / fname)
    templates[key] = req
    # quick introspection
    names = [i["name"] for i in req["inputs"]]
    has_af = "AF_Quantitative_" in names
    has_5c = "Condition1_" in names
    af = next((i for i in req["inputs"] if i["name"] == "AF_Quantitative_"), None)
    ncols = len(af["value"][0]["metadata"]) if af else 0
    print(f"{key:16} <- {fname:32} inputs={len(names):3} AF={has_af} 5C={has_5c} cols={ncols}")

out = Path(__file__).parent / "templates.json"
out.write_text(json.dumps(templates, ensure_ascii=False), encoding="utf-8")
print("size:", out.stat().st_size, "bytes ->", out)

# also dump the shared AF metadata column order from one template
af = next(i for i in templates["SME-L|CA2"]["inputs"] if i["name"]=="AF_Quantitative_")
cols = [list(m.keys())[0] for m in af["value"][0]["metadata"]]
print("AF cols:", len(cols))
for want in ["ApplNo","Installment","TermYear","ICR","DSCR","ObjCodeDetail","IncomePerYear","Limit","AF_IndustryType"]:
    print(f"  {want} -> idx {cols.index(want) if want in cols else 'MISSING'}")
