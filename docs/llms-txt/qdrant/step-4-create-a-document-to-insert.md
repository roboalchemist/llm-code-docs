# Step 4: Create a Document to Insert

description = "qdrant is a high available vector search engine"
embedding_model = TextEmbedding(model_name=embed_model_name)
vector = next(embedding_model.embed(documents=description)).tolist()
document = {
    "collection_name": collection_name,
    "id": 1,
    "vector": vector,
    "payload": {
        "name": "qdrant",
        "description": description,
        "url": "https://qdrant.tech/documentation"
    }
}