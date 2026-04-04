# Food Discovery Demo

Kacper Łukawski

·

September 05, 2023

![Food Discovery Demo](https://qdrant.tech/articles_data/food-discovery-demo/preview/title.jpg)

Not every search journey begins with a specific destination in mind. Sometimes, you just want to explore and see what’s out there and what you might like.
This is especially true when it comes to food. You might be craving something sweet, but you don’t know what. You might be also looking for a new dish to try,
and you just want to see the options available. In these cases, it’s impossible to express your needs in a textual query, as the thing you are looking for is not
yet defined. Qdrant’s semantic search for images is useful when you have a hard time expressing your tastes in words.

## [Anchor](https://qdrant.tech/articles/food-discovery-demo/\#general-architecture) General architecture

We are happy to announce a refreshed version of our [Food Discovery Demo](https://food-discovery.qdrant.tech/). This time available as an open source project,
so you can easily deploy it on your own and play with it. If you prefer to dive into the source code directly, then feel free to check out the [GitHub repository](https://github.com/qdrant/demo-food-discovery/).
Otherwise, read on to learn more about the demo and how it works!

In general, our application consists of three parts: a [FastAPI](https://fastapi.tiangolo.com/) backend, a [React](https://react.dev/) frontend, and
a [Qdrant](https://qdrant.tech/) instance. The architecture diagram below shows how these components interact with each other:

![Archtecture diagram](https://qdrant.tech/articles_data/food-discovery-demo/architecture-diagram.png)

## [Anchor](https://qdrant.tech/articles/food-discovery-demo/\#why-did-we-use-a-clip-model) Why did we use a CLIP model?

CLIP is a neural network that can be used to encode both images and texts into vectors. And more importantly, both images and texts are vectorized into the same
latent space, so we can compare them directly. This lets you perform semantic search on images using text queries and the other way around. For example, if
you search for “flat bread with toppings”, you will get images of pizza. Or if you search for “pizza”, you will get images of some flat bread with toppings, even
if they were not labeled as “pizza”. This is because CLIP embeddings capture the semantics of the images and texts and can find the similarities between them
no matter the wording.

![CLIP model](https://qdrant.tech/articles_data/food-discovery-demo/clip-model.png)

CLIP is available in many different ways. We used the pretrained `clip-ViT-B-32` model available in the [Sentence-Transformers](https://www.sbert.net/examples/applications/image-search/README.html)
library, as this is the easiest way to get started.

## [Anchor](https://qdrant.tech/articles/food-discovery-demo/\#the-dataset) The dataset

The demo is based on the [Wolt](https://wolt.com/) dataset. It contains over 2M images of dishes from different restaurants along with some additional metadata.
This is how a payload for a single dish looks like:

```json
{
    "cafe": {
        "address": "VGX7+6R2 Vecchia Napoli, Valletta",
        "categories": ["italian", "pasta", "pizza", "burgers", "mediterranean"],
        "location": {"lat": 35.8980154, "lon": 14.5145106},
        "menu_id": "610936a4ee8ea7a56f4a372a",
        "name": "Vecchia Napoli Is-Suq Tal-Belt",
        "rating": 9,
        "slug": "vecchia-napoli-skyparks-suq-tal-belt"
    },
    "description": "Tomato sauce, mozzarella fior di latte, crispy guanciale, Pecorino Romano cheese and a hint of chilli",
    "image": "https://wolt-menu-images-cdn.wolt.com/menu-images/610936a4ee8ea7a56f4a372a/005dfeb2-e734-11ec-b667-ced7a78a5abd_l_amatriciana_pizza_joel_gueller1.jpeg",
    "name": "L'Amatriciana"
}

```

Processing this amount of records takes some time, so we precomputed the CLIP embeddings, stored them in a Qdrant collection and exported the collection as
a snapshot. You may [download it here](https://storage.googleapis.com/common-datasets-snapshots/wolt-clip-ViT-B-32.snapshot).

## [Anchor](https://qdrant.tech/articles/food-discovery-demo/\#different-search-modes) Different search modes

The FastAPI backend [exposes just a single endpoint](https://github.com/qdrant/demo-food-discovery/blob/6b49e11cfbd6412637d527cdd62fe9b9f74ac699/backend/main.py#L37),
however it handles multiple scenarios. Let’s dive into them one by one and understand why they are needed.

### [Anchor](https://qdrant.tech/articles/food-discovery-demo/\#cold-start) Cold start

Recommendation systems struggle with a cold start problem. When a new user joins the system, there is no data about their preferences, so it’s hard to recommend
anything. The same applies to our demo. When you open it, you will see a random selection of dishes, and it changes every time you refresh the page. Internally,
the demo [chooses some random points](https://github.com/qdrant/demo-food-discovery/blob/6b49e11cfbd6412637d527cdd62fe9b9f74ac699/backend/discovery.py#L70) in the
vector space.

![Random points selection](https://qdrant.tech/articles_data/food-discovery-demo/random-results.png)

That procedure should result in returning diverse results, so we have a higher chance of showing something interesting to the user.

### [Anchor](https://qdrant.tech/articles/food-discovery-demo/\#textual-search) Textual search

Since the demo suffers from the cold start problem, we implemented a textual search mode that is useful to start exploring the data. You can type in any text query
by clicking a search icon in the top right corner. The demo will use the CLIP model to encode the query into a vector and then search for the nearest neighbors
in the vector space.

![Random points selection](https://qdrant.tech/articles_data/food-discovery-demo/textual-search.png)

This is implemented as [a group search query to Qdrant](https://github.com/qdrant/demo-food-discovery/blob/6b49e11cfbd6412637d527cdd62fe9b9f74ac699/backend/discovery.py#L44).
We didn’t use a simple search, but performed grouping by the restaurant to get more diverse results. [Search groups](https://qdrant.tech/documentation/concepts/search/#search-groups)
is a mechanism similar to `GROUP BY` clause in SQL, and it’s useful when you want to get a specific number of result per group (in our case just one).

```python
import settings