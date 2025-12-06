# Nomic Documentation

Source: https://docs.nomic.ai/platform/embeddings-and-retrieval/multimodality

Multimodality refers to the ability to operate with different data types in an application - for example, working with both text and images.

Nomic supports multimodality with embedding models Nomic Embed Text and Nomic Embed Vision that are aligned, meaning each embedding model maps their respective data types into the same unified embedding space.

Below, we show some examples of what this alignment enables for users with a combination of text and image data.

## Text query to image response​

Our Dataset visualization interface Atlas allows you to search & retrieve images using text queries. This capability is available in the Atlas interface as well as with the Nomic API. We demonstrate doing so here in the Atlas interface.

Open the vector search modal by clicking its selection icon or using the hotkey 'V'.
`

### Example: Met Museum​

Searching for animals over the Metropolitan Museum of Art map returns images of artwork that depicts animals.

```
animals
```

### Example: Imagenette​

Searching for a tiny white ball over this map of the Imagenette dataset returns images of golf balls.

```
a tiny white ball
```

## Image query to text response​

The alignment between Nomic Embed Text and Nomic Embed Vision also enables search & retrieval over texts using image queries. This capability is only available programatically using the Nomic Embed models, which we demonstrate here using the Nomic API.

Given an image, we can use embeddings and the cosine similarity metric to find the nearest text from a list of candidates. Here is a function to do so:

```
from nomic import embedimport numpy as npfrom PIL import Imagefrom sklearn.metrics.pairwise import cosine_similaritydef get_nearest_texts(image_path, texts):    """    Sort texts by cosine similarity     to the given image using Nomic Embed    """    text_embeddings = np.array(embed.text(texts)['embeddings'])    image_embedding = np.array(embed.image([Image.open(image_path)])['embeddings'])    similarities = cosine_similarity(text_embeddings, image_embedding).flatten()    return sorted(zip(example_texts, similarities), key=lambda x: x[1], reverse=True)
```

Let's define a list of example texts:

```
example_texts = [    "space",    "office",    "animal",    "furniture",    "mineral",    "transportation",    "fruit",    "vegetable",    "school",    "sports",    "music",    "science"]
```

Here is the result of the get_nearest_texts function on this image of a dog: animal is identified as the closest string.

```
get_nearest_texts
```

```
animal
```

```
get_nearest_texts("test_dog.jpg", example_texts)>>> [('animal', 0.03564013310427372), ('science', 0.031202670580171295), ('school', 0.027342345453057387), ('sports', 0.027165233524738014), ('vegetable', 0.024059498162026658), ('furniture', 0.023418001472089778), ('music', 0.023156718308523366), ('space', 0.022177890839806896), ('office', 0.02213907076336389), ('mineral', 0.016594831073997493), ('transportation', 0.010884708615859745), ('fruit', 0.008455650618822643)]
```

Similarly, here is the result of the get_nearest_texts function on this image of a baseball stadium: sports is identified as the closest string.

```
get_nearest_texts
```

```
sports
```

```
get_nearest_texts("baseball-stadium.png", example_texts)>>> [('sports', 0.037376135866776475), ('transportation', 0.024963588733468628), ('office', 0.021604522797398027), ('music', 0.02136078816567221), ('school', 0.02098362299403069), ('space', 0.020209324940584042), ('mineral', 0.0183532860105191), ('animal', 0.016895717157126414), ('vegetable', 0.01661184792135495), ('science', 0.015450037202627127), ('furniture', 0.009593605615740136), ('fruit', 0.004581729111051765)]
```

- Text query to image responseExample: Met MuseumExample: Imagenette
- Example: Met Museum
- Example: Imagenette
- Image query to text response
