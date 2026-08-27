"""Inject templates.json into _shell.html -> cra_payload_tool.html (single file)."""
import json
from pathlib import Path

TOOL = Path(r"D:\work\luna\documents\credit_scoring_engine\example_test_data\Ex.Log CRA-20260513T160519Z-3-001\Ex.Log CRA\cra_tool")
SCRATCH = Path(__file__).parent

shell = (TOOL / "_shell.html").read_text(encoding="utf-8")
templates = json.loads((SCRATCH / "templates.json").read_text(encoding="utf-8"))

# Embed as a JS literal. Use json.dumps (valid JS). Escape </script> just in case.
js_literal = json.dumps(templates, ensure_ascii=False).replace("</", "<\\/")
placeholder = "/*__BASE_TEMPLATES__*/ null"
assert placeholder in shell, "placeholder not found in shell"
final = shell.replace(placeholder, js_literal)

out = TOOL / "cra_payload_tool.html"
out.write_text(final, encoding="utf-8")
print("built:", out)
print("size :", f"{out.stat().st_size/1024:.1f} KB")
print("templates embedded:", list(templates.keys()))
