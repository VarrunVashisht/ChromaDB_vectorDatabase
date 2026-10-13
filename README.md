# ChromaDB Vector Database

This repository is a simple learning project for working with ChromaDB, a vector database used for semantic search and embedding-based retrieval.

The scripts in this project show how to:
- create a collection
- store text documents
- persist data to disk
- run semantic queries
- inspect embeddings
- compare vector similarity
- add metadata and filter records
- update and delete stored items

This is a beginner-friendly example project, not a production application.

## Why this project exists

Modern AI apps often need to search through large amounts of text using meaning, not just exact keywords. ChromaDB helps with that by storing text as vector embeddings and searching by similarity.

In this project, the database stores example transport-related documents like:
- Car run on land
- Plane flies in the sky
- Boat sails on water
- Bus drives on road

Then the scripts query the database with phrases such as:
- "vehicle that doesn't need fuel."
- "which one contains more than one word?"

## Project structure

- `semanticSearchSetup.py` — creates a persistent ChromaDB collection and runs a semantic search
- `createEmbedding.py` — shows how to add documents and inspect stored embeddings
- `compareEmbeddings.py` — compares embedding vectors using cosine similarity
- `metadata.py` — adds metadata to documents and filters by metadata values
- `query_client.py` — creates a collection using `chromadb.Client()`
- `query_PersistentClient.py` — creates a collection using `chromadb.PersistentClient()`
- `updating_deleting.py` — updates and deletes records in a collection
- `my_database/` — persistent database directory created by ChromaDB
- `chroma/` — additional local ChromaDB storage folder used during experimentation
- `venv/` — project virtual environment

## Setup

This project already includes a local virtual environment in `venv/`, so you can run the scripts without installing anything extra if the environment is already working.

If you want to create a fresh environment manually, run:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install chromadb numpy
```

On Windows PowerShell, use:

```powershell
cd "C:\Users\61424\Desktop\ChromaDB"
.\venv\Scripts\Activate.ps1
```

## Run the examples

You can run any script directly with Python:

```powershell
cd "C:\Users\61424\Desktop\ChromaDB"
.\venv\Scripts\python.exe .\semanticSearchSetup.py
```

Example output:

```text
Collection is ready: vehicle_semantic
Semantic Search Results:
-Car run on land (distance: 1.1657)
-Bus drives on road (distance: 1.5367)
-Boat sails on water (distance: 1.6816)
```

Use the other scripts in the same way:

```powershell
.\venv\Scripts\python.exe .\createEmbedding.py
.\venv\Scripts\python.exe .\compareEmbeddings.py
.\venv\Scripts\python.exe .\metadata.py
.\venv\Scripts\python.exe .\updating_deleting.py
```

## How the basic workflow works

Most scripts in this repository follow the same pattern:

1. Connect to ChromaDB
2. Create or open a collection
3. Add documents with IDs
4. Query the database with a natural-language prompt
5. Inspect the returned results

Example pattern:

```python
import chromadb

client = chromadb.PersistentClient(path="./my_database")
collection = client.get_or_create_collection(name="vehicle_semantic")

collection.add(
    documents=["Car run on land", "Plane flies in the sky"],
    ids=["1", "2"]
)

results = collection.query(
    query_texts=["vehicle that doesn't need fuel."],
    n_results=3
)
```

## Notes

- The collection data is stored locally in the `my_database` folder.
- `PersistentClient` is used when you want the database to keep data across script runs.
- ChromaDB automatically handles embedding generation for text content.
- The semantic search results are based on similarity, not exact keyword matching.

## Learning goals

This project is useful for learning:
- vector databases basics
- semantic search concepts
- embedding storage and retrieval
- metadata filtering in vector databases
- persistent storage with Python

## License

This project does not currently include a formal license file. If you plan to share or publish it, add an appropriate license such as MIT or Apache-2.0.
