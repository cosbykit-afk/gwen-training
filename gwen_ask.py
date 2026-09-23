import json
import sys
import urllib.request

prompt = open(sys.argv[1], encoding="utf-8").read()
payload = json.dumps(
    {"model": "gwen:latest", "prompt": prompt, "stream": False}
).encode("utf-8")
req = urllib.request.Request(
    "http://localhost:11434/api/generate",
    data=payload,
    headers={"Content-Type": "application/json"},
)
with urllib.request.urlopen(req, timeout=900) as resp:
    out = json.loads(resp.read().decode("utf-8"))
print(out.get("response", ""))
sys.stdout.write(
    "\n---META--- "
    + json.dumps(
        {k: out.get(k) for k in ("done", "total_duration", "eval_count", "prompt_eval_count")}
    )
    + "\n"
)
