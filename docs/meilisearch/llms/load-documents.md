# Load documents
loader = JSONLoader(
    file_path="./movies-lite.json",
    jq_schema=".[] | {id: .id, overview: .overview, title: .title}",
    text_content=False,
)
documents = loader.load()
print("Loaded {} documents".format(len(documents)))