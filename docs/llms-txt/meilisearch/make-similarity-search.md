# Make similarity search
embedder_name = "custom"
query = "superhero fighting evil in a city at night"
results = vector_store.similarity_search(
    query=query,
    embedder_name=embedder_name,
    k=3,
)