import chromadb
client = chromadb.PersistentClient(path="./my_database")
collection = client.get_or_create_collection("metadata")

collection.add(
    documents=["Car run on land",
               "Plane flies in the sky",
               "Boat sails on water",
               "Bus drives on road"
              ],
    ids=["1", "2", "3", "4"],
    metadatas=[
        {"type":"public_transport","fuel":"diesel"},
        {"type":"air_transport","fuel":"jet"},
        {"type":"water_transport","fuel":"diesel"},
        {"type":"personal_transport","fuel":"manual"}
    ]
)

print("Collection is ready:", collection)

data = collection.get(include=["documents","metadatas"])

print("Current Data")
for i, doc, meta in zip(data['ids'], data['documents'], data['metadatas']):
    print(f"ID: {i}, Document: {doc}, Metadata: {meta}")


diesel_vehicle = collection.get(where={"fuel":"diesel"})
print("\n Diesel Vehicles:")
print(diesel_vehicle)

personal_transport = collection.get(where={"type":"personal_transport"})
print("\n Personal Transport:")
print(personal_transport)                               