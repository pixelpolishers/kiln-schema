# Usage: python validate.py <schema-dir> <schema-file>=<json-file> ...
# Requires: pip install jsonschema referencing
import json, sys, pathlib
import jsonschema
from referencing import Registry, Resource

root = pathlib.Path(sys.argv[1])
reg = Registry()
schemas = {}
for p in sorted(root.glob('*.schema.json')):
    s = json.loads(p.read_text())
    jsonschema.Draft202012Validator.check_schema(s)
    schemas[p.name] = s
    reg = reg.with_resource(p.name, Resource.from_contents(s))
print("schemas valid:", ", ".join(schemas))

def check(schema, path):
    v = jsonschema.Draft202012Validator(schemas[schema], registry=reg)
    errs = list(v.iter_errors(json.loads(pathlib.Path(path).read_text())))
    print(("OK   " if not errs else "FAIL ") + f"{path} against {schema}")
    for e in errs:
        print("   -", "/".join(map(str, e.absolute_path)), ":", e.message[:200])
    return not errs

ok = True
for spec in sys.argv[2:]:
    schema, path = spec.split("=", 1)
    ok &= check(schema, path)
sys.exit(0 if ok else 1)
