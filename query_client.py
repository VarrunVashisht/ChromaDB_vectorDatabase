import chromadb
client = chromadb.Client()
collection = client.create_collection("my_collection")
print(collection)

# add data to the collection
collection.add(
    documents=["Car run on land",
               "Plane flies in the sky",
               "Boat sails on water",
               "Bus drives on road"
              ],
    ids=["1", "2", "3", "4"]
)   

# query the collection
results = collection.query(
    query_texts=["which one contains more than one word?"],
    n_results=1
)
print(results)


