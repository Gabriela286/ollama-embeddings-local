import json
import urllib.request

url = "http://localhost:11434/api/embeddings"
payload = {
    "model": "nomic-embed-text",
    "prompt": "Demonstracao de geracao de embeddings com Ollama e Python."
}

req = urllib.request.Request(
    url,
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)

with urllib.request.urlopen(req) as resp:
    dados = json.loads(resp.read().decode("utf-8"))

embedding = dados["embedding"]

print("=== Geracao de Embeddings ===")
print(f"Texto: {payload['prompt']}")
print(f"Dimensao do vetor: {len(embedding)}")
print(f"Primeiros 5 valores: {embedding[:5]}")
