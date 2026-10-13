import chromadb
client = chromadb.PersistentClient(path="./my_database")

collection = client.get_or_create_collection("vehicles")

collection.add(
    documents=["Car run on land",
               "Plane flies in the sky",
               "Boat sails on water",
               "Bus drives on road"
              ],
    ids=["1", "2", "3", "4"]
)

print("Collection is ready:", collection)

data = collection.get()

#Updating the specific record by using unique Id.
collection.update(ids=["1"],
                  documents=["Car run on land on 4 tyres"])
print("Record has been updated.")

#Deleting the record by using unique Id.
collection.delete(ids=["1"])
print("Record has been deleted.")

print("Current Data")
for i, doc in zip(data['ids'], data['documents']):
    print(f"ID: {i}, Document: {doc}")