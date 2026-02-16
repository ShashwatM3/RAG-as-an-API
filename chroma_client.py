import chromadb

# setting up the client
class ChromaDBClient:
    def __init__(self, path = "./db"):
        self.client = chromadb.PersistentClient(path)
        # accessing / making a collection
        self.collection = None
    
    def set_collection(self, collection_name):
        self.collection = self.client.get_or_create_collection(collection_name)

    def ingest_file(self, file_path):
        self.ingest(file_path, type = "file")
        
    def ingest(self, data, type = "text"):
        ingest_text = ""
        if type=="file":
            # data would be the file path
            with open(data, "r") as f:
                text = f.read()
                ingest_text = text
        elif type=="text":
            # data would be raw text string
            ingest_text = data
        self.collection.add(documents=[ingest_text], ids=[f"{self.collection.count()+1}"])

    def query(self, queries):
      results = self.collection.query(query_texts=queries, n_results=1)
      return results