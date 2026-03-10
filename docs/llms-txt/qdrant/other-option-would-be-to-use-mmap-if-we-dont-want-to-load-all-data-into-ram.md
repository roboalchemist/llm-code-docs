# Other option would be to use Mmap, if we don't want to load all data into RAM
vectors = np.load('./startup_vectors.npy')

```

And the final step - data uploading

```python
qdrant_client.upload_collection(
    collection_name='startups',
    vectors=vectors,
    payload=payload,
    ids=None,  # Vector ids will be assigned automatically
    batch_size=256  # How many vectors will be uploaded in a single request?
)

```

Now we have vectors uploaded to the vector search engine.
In the next step, we will learn how to actually search for the closest vectors.

The full code for this step can be found [here](https://github.com/qdrant/qdrant_demo/blob/master/qdrant_demo/init_collection_startups.py).

### [Anchor](https://qdrant.tech/articles/neural-search-tutorial/\#step-4-make-a-search-api) Step 4: Make a search API

Now that all the preparations are complete, let’s start building a neural search class.

First, install all the requirements:

```bash
pip install sentence-transformers numpy

```

In order to process incoming requests neural search will need 2 things.
A model to convert the query into a vector and Qdrant client, to perform a search queries.

```python