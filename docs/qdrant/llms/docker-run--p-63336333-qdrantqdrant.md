# docker run -p 6333:6333 qdrant/qdrant
client = QdrantClient(url="http://localhost:6333/")

```

2. **Create a new collection for the images with captions**.

```python
COLLECTION_NAME = "llama-multi"

if not client.collection_exists(COLLECTION_NAME):
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config={
            "image": models.VectorParams(size=len(image_embeddings[0]), distance=models.Distance.COSINE),
            "text": models.VectorParams(size=len(text_embeddings[0]), distance=models.Distance.COSINE),
        }
    )

```

3. **Upload our images with captions to the Collection**.

```python
client.upload_points(
    collection_name=COLLECTION_NAME,
    points=[\
        models.PointStruct(\
            id=idx,\
            vector={\
                "text": text_embeddings[idx],\
                "image": image_embeddings[idx],\
            },\
            payload=doc\
        )\
        for idx, doc in enumerate(documents)\
    ]
)

```

## [Anchor](https://qdrant.tech/documentation/multimodal-search/\#search) Search

### [Anchor](https://qdrant.tech/documentation/multimodal-search/\#text-to-image) Text-to-Image

Let’s see what image we will get to the query “ _Adventures on snow hills_”.

```python
from PIL import Image

find_image = model.get_query_embedding("Adventures on snow hills")

Image.open(client.query_points(
    collection_name=COLLECTION_NAME,
    query=find_image,
    using="image",
    with_payload=["image"],
    limit=1
).points[0].payload['image'])

```

Let’s also run the same query in Italian and compare the results.

### [Anchor](https://qdrant.tech/documentation/multimodal-search/\#multilingual-search) Multilingual Search

Now, let’s do a multilingual search using an Italian query:

```python
Image.open(client.query_points(
    collection_name=COLLECTION_NAME,
    query=model.get_query_embedding("Avventure sulle colline innevate"),
    using="image",
    with_payload=["image"],
    limit=1
).points[0].payload['image'])

```

**Response:**

![Snow prints](https://qdrant.tech/documentation/advanced-tutorials/snow-prints.png)

### [Anchor](https://qdrant.tech/documentation/multimodal-search/\#image-to-text) Image-to-Text

Now, let’s do a reverse search with the following image:

![Airplane](https://qdrant.tech/documentation/advanced-tutorials/airplane.png)

```python
client.query_points(
    collection_name=COLLECTION_NAME,
    query=model.get_image_embedding("images/image-2.png"),
    # Now we are searching only among text vectors with our image query
    using="text",
    with_payload=["caption"],
    limit=1
).points[0].payload['caption']

```

**Response:**

```text
'An image about plane emergency safety.'

```

## [Anchor](https://qdrant.tech/documentation/multimodal-search/\#next-steps) Next steps

Use cases of even just Image & Text Multimodal Search are countless: E-Commerce, Media Management, Content Recommendation, Emotion Recognition Systems, Biomedical Image Retrieval, Spoken Sign Language Transcription, etc.

Imagine a scenario: a user wants to find a product similar to a picture they have, but they also have specific textual requirements, like “ _in beige colour_”. You can search using just texts or images and combine their embeddings in a **late fusion manner** (summing and weighting might work surprisingly well).

Moreover, using [Discovery Search](https://qdrant.tech/articles/discovery-search/) with both modalities, you can provide users with information that is impossible to retrieve unimodally!

Join our [Discord community](https://qdrant.to/discord), where we talk about vector search and similarity learning, experiment, and have fun!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/multimodal-search.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/multimodal-search.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-80-lllmstxt|>
## concepts
- [Documentation](https://qdrant.tech/documentation/)
- Concepts