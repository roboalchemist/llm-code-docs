# Setup code will go here 👇
```

## Importing documents and embeddings

Now that the project is ready, import some documents in Meilisearch. First, download this small movies dataset:

<Card title="movies-lite.json" icon="file" href="https://gist.githubusercontent.com/Strift/1524ab5e2015e50bbcb215fb4d950a38/raw/movies-lite.json?raw=true">
  Download movies-lite.json
</Card>

Then, update the setup.py file to load the JSON and store it in Meilisearch. You will also use the OpenAI text search models to generate vector embeddings.

To use vector search, we need to set the embedders index setting. In this case, you are using an `userProvided` source which requires to specify the size of the vectors in a `dimensions` field. The default model used by `OpenAIEmbeddings()` is `text-embedding-ada-002`, which has 1,536 dimensions.

```python theme={null}