import requests

API_KEY = "AIzaSyDteFt00AbubJqENDbALTCX3vMAzn7vPm0"  # your AI Studio key

resp = requests.get(
    f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"
)
models = resp.json().get("models", [])

for m in models:
    name = m.get("name")
    methods = m.get("supportedGenerationMethods", [])
    print(f"{name} → {methods}")
