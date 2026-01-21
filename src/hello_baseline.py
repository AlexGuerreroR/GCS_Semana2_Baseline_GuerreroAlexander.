import json, os, argparse

def load_data(path):
    if not os.path.exists(path):
        return {"students": []}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def report(data):
    out = ["REPORTE · Promedios", "-"*22]
    for s in data.get("students", []):
        g = s.get("grades", [])
        avg = sum(g)/len(g) if g else 0.0
        out.append(f"{s['name']}: {avg:.2f}")
    if len(out)==2:
        out.append("Sin datos.")
    return "\n".join(out)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--data", default="data.json")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("report")
    args = p.parse_args()
    data = load_data(args.data)
    print(report(data))

if __name__ == "__main__":
    main()
