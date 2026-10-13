import numpy as np
import chromadb


def cosine_similarity(vec1, vec2):
    vec1 = np.asarray(vec1, dtype=float)
    vec2 = np.asarray(vec2, dtype=float)

    if vec1.shape != vec2.shape:
        raise ValueError("Vectors must have the same length.")

    denom = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    if np.isclose(denom, 0.0):
        return 0.0

    return float(np.dot(vec1, vec2) / denom)


# output ranges from -1 to 1 where:
# 1 = very similar
# 0 = unrelated
# -1 = opposite

client = chromadb.PersistentClient(path="./my_database")
collection = client.get_or_create_collection(name="vehicle_embeddings")

data = collection.get(include=["documents", "embeddings"])

# get embeddings from the collection by document name instead of assuming fixed indexes
documents = data.get("documents", [])
embeddings = data.get("embeddings", [])

if len(documents) == 0 or len(embeddings) == 0:
    raise ValueError("No documents or embeddings found in the collection.")

car_index = next((i for i, doc in enumerate(documents) if "car" in doc.lower()), None)
bus_index = next((i for i, doc in enumerate(documents) if "bus" in doc.lower()), None)
bike_index = next((i for i, doc in enumerate(documents) if "bike" in doc.lower()), None)

if car_index is None or bus_index is None:
    raise ValueError("The collection must include at least a 'car' and 'bus' document.")

emb_car = embeddings[car_index]
emb_bus = embeddings[bus_index]

# Compare similarities
sim_car_bus = cosine_similarity(emb_car, emb_bus)
print("Cosine Similarity:")
print(f"Car vs Bus: {sim_car_bus:.4f}")

if bike_index is not None:
    emb_bike = embeddings[bike_index]
    sim_car_bike = cosine_similarity(emb_car, emb_bike)
    print(f"Car vs Bike: {sim_car_bike:.4f}")
else:
    print("No bike document found in the collection.")