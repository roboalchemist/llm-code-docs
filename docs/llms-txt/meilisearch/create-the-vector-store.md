# Create the vector store
client = meilisearch.Client(
    url=os.environ.get("MEILI_HTTP_ADDR"),
    api_key=os.environ.get("MEILI_API_KEY"),
)
embeddings = OpenAIEmbeddings()
vector_store = Meilisearch(client=client, embedding=embeddings)