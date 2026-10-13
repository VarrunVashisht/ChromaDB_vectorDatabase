import chromadb
client = chromadb.PersistentClient(path="./my_database")
collection = client.get_or_create_collection(name="vehicle_embeddings")



collection.add(
    documents=["Car run on land",
               "Plane flies in the sky",
               "Boat sails on water",
               "Bus drives on road"
              ],
    ids=["1", "2", "3", "4"]
)

print("Collection is ready:", collection.name)

data = collection.get(include=["documents","embeddings"])

print("Embeddings data")
for i, doc, emb in zip(data['ids'], data['documents'],data['embeddings']):
    print(f"ID: {i}, Document: {doc}, Embeddings: {emb[:5]}")