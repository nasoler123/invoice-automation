from pathlib import Path
import importlib.util
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
def offline(event, args):
    if event.startswith("socket.") or event in {"subprocess.Popen", "os.system", "os.exec", "os.posix_spawn"}:
        raise RuntimeError("Demo offline: conexión o proceso externo rechazado")
sys.addaudithook(offline)
spec = importlib.util.spec_from_file_location("original_sample", HERE / "source" / "invoice_controls.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
checks = []
def check(name, condition):
    assert condition, name
    checks.append({"case": name, "passed": True})
cases = [{'name': 'Factura coherente', 'input': {'base_value': 100, 'tax_value': 21, 'rate_value': 21, 'total_line': 121}, 'result': {'error': False, 'code': ''}, 'passed': True}, {'name': 'IVA incoherente', 'input': {'base_value': 100, 'tax_value': 19, 'rate_value': 21, 'total_line': 119}, 'result': {'error': True, 'code': 'IVANoCuadraConRate'}, 'passed': True}, {'name': 'Total incoherente', 'input': {'base_value': 100, 'tax_value': 21, 'rate_value': 21, 'total_line': 123}, 'result': {'error': True, 'code': 'SumaLineasNoCuadra'}, 'passed': True}, {'name': 'Campo ausente', 'input': {'base_value': None, 'tax_value': 21, 'rate_value': 21, 'total_line': 121}, 'result': {'error': True, 'code': 'DatosLineaIncompletos'}, 'passed': True}, {'name': 'Cero válido', 'input': {'base_value': 0, 'tax_value': 0, 'rate_value': 21, 'total_line': 0}, 'result': {'error': False, 'code': ''}, 'passed': True}]
for item in cases:
    error, code = module.check_line_level(item["input"])
    check(item["name"], {"error": error, "code": code} == item["result"])
print(json.dumps({"checks": checks, "passed": len(checks), "network": "forbidden"}, ensure_ascii=False))
