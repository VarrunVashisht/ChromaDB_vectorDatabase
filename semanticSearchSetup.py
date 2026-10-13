import chromadb
client = chromadb.PersistentClient(path="./my_database")
collection = client.get_or_create_collection(name="vehicle_semantic")

collection.add(
    documents=["Car run on land",
               "Plane flies in the sky",
               "Boat sails on water",
               "Bus drives on road"
              ],
    ids=["1", "2", "3", "4"]
)
print("Collection is ready:", collection.name)

results = collection.query(
    query_texts=["vehicle that doesn't need fuel."],
    n_results=3
)

print("Semantic Search Results:")
for doc, dist in zip(results["documents"][0], results["distances"][0]):
    print(f"-{doc} (distance: {dist:.4f})")




