import chromadb
client = chromadb.PersistentClient(path="./my_database")

collection = client.create_collection("vehicles")

collection.add(
    documents=["Car run on land",
               "Plane flies in the sky",
               "Boat sails on water",
               "Bus drives on road"
              ],
    ids=["1", "2", "3", "4"]
)

print ("Collection created and data added successfully.")

