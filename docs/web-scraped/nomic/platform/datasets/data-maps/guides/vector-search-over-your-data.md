# Nomic Documentation

Source: https://docs.nomic.ai/platform/datasets/data-maps/guides/vector-search-over-your-data

Nomic Atlas enables you to search your dataset semantically with vector search.

## Using Vector Search​

Open the vector search modal by clicking its selection icon or using the hotkey 'V'.

After submitting a successful search, a slider will appear for you to adjust. The slider is over similarity values (i.e. dot products) where the larger the value, the more similar the data point is to the search vector. Drag the slider to the left to
include data points that are less similar and right for more similar.
The percentages displayed shows the percentile number of data points captured between the similarity cutoffs.
The Atlas map selection will automatically update based on the slider range.

## Combining Vector Search with Other Selections​

Vector Search is part of the selection paradigm within Atlas.
This means that out-of-the-box, you can combine your vector search filter with other Atlas tools to compose complex
data selections.

Below, we join our vector search results with a search selection and lasso selection to find a subset of
technology stock articles we are interested in.

## Vector Search Over Images​

Nomic Text and Vision embedding models provide compatible, aligned embeddings (See details here). This means you
can run text-to-image and image-to-text vector searches on your data (e.g. Find cat articles by providing a picture
of a cat; find cat images that match the query "What animals are cute to cuddle with?").

## Vector Search API​

Developers can leverage the Nomic API to run a vector search over their dataset. More examples and documentation for the endpoint are found in the API reference.

The API accepts either text queries that will be embedded using Nomic's embedding model, or raw embedding vectors that match the dimensionality of your dataset's embeddings. Read here for more info.

- Text Query
- Vector Query
```
curl -L 'https://api-atlas.nomic.ai/v1/query/topk' \-H 'Content-Type: application/json' \-H 'Authorization: Bearer $NOMIC_API_KEY' \-d '{    "projection_id": "f1e499cd-b5c1-4d31-b38a-fff61e1f8b59",    "k": 3,    "fields": ["title", "average_rating", "price"],    "query": "footwear"}'
```

```
curl -L 'https://api-atlas.nomic.ai/v1/query/topk' \-H 'Content-Type: application/json' \-H 'Authorization: Bearer $NOMIC_API_KEY' \-d '{    "projection_id": "f1e499cd-b5c1-4d31-b38a-fff61e1f8b59",    "k": 3,    "fields": ["title", "average_rating", "price"],    "query": [0.1234, 0.5678, 0.9123, 0.4567, 0.7890, 0.3456, ..., 0.9821]}'
```

The API endpoint returns a list of the closest items to the query from the dataset:

```
{  "data":  [    {      "title":"pediped Unisex-Child Flex Barbara School Uniform Shoe",      "average_rating":4.5,      "price":59.95000076293945,      "_similarity":0.7833542227745056    },    {      "title":"pediped Unisex-Child Flex Eclipse",      "average_rating":3.700000047683716,      "price":32.20000076293945,      "_similarity":0.7810658812522888    },    {      "title":"Cat Footwear Women's Brode St Shoe",      "average_rating":3.799999952316284,      "price":null,      "_similarity":0.7771036028862    }  ]}
```

- Using Vector Search
- Combining Vector Search with Other Selections
- Vector Search Over Images
- Vector Search API
