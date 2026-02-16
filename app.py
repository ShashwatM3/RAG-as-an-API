from fastapi import FastAPI
import chromadb
import ollama
from chroma_client import ChromaDBClient

app = FastAPI()

client = ChromaDBClient()
client.set_collection("docs")
ollama_client = ollama.Client(
  host = "http://host.docker.internal:11434"
)

@app.post("/query")
def query(q: str):
    results = client.query([q])
    context = results["documents"][0][0] if results["documents"] and len(results["documents"][0]) > 0 else ""
    
    answer = ollama_client.generate(
        model="tinyllama",
        prompt=f"""
        Context: {context}
        
        Question: {q}
        
        Answer clearly and concisely, with preference to the context
        """
    )
    
    return {"answer": answer['response']}
  
@app.post("/add")
def add(text: str):
  try:
    client.ingest(text)
    return {"state": "success"}
  except Exception as e:
      return {"status": "failed", "error": str(e)}

@app.get("/health")
def health():
  return {"status": "ok"}
