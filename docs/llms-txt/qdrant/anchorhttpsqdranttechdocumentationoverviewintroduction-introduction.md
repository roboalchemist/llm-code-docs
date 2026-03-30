# [Anchor](https://qdrant.tech/documentation/overview/\#introduction) Introduction

Vector databases are a relatively new way for interacting with abstract data representations
derived from opaque machine learning models such as deep learning architectures. These
representations are often called vectors or embeddings and they are a compressed version of
the data used to train a machine learning model to accomplish a task like sentiment analysis,
speech recognition, object detection, and many others.

These new databases shine in many applications like [semantic search](https://en.wikipedia.org/wiki/Semantic_search)
and [recommendation systems](https://en.wikipedia.org/wiki/Recommender_system), and here, we’ll
learn about one of the most popular and fastest growing vector databases in the market, [Qdrant](https://github.com/qdrant/qdrant).

## [Anchor](https://qdrant.tech/documentation/overview/\#what-is-qdrant) What is Qdrant?

[Qdrant](https://github.com/qdrant/qdrant) “is a vector similarity search engine that provides a production-ready
service with a convenient API to store, search, and manage points (i.e. vectors) with an additional
payload.” You can think of the payloads as additional pieces of information that can help you
hone in on your search and also receive useful information that you can give to your users.

You can get started using Qdrant with the Python `qdrant-client`, by pulling the latest docker
image of `qdrant` and connecting to it locally, or by trying out [Qdrant’s Cloud](https://cloud.qdrant.io/)
free tier option until you are ready to make the full switch.

With that out of the way, let’s talk about what are vector databases.

## [Anchor](https://qdrant.tech/documentation/overview/\#what-are-vector-databases) What Are Vector Databases?

![dbs](https://raw.githubusercontent.com/ramonpzg/mlops-sydney-2023/main/images/databases.png)

Vector databases are a type of database designed to store and query high-dimensional vectors
efficiently. In traditional [OLTP](https://www.ibm.com/topics/oltp) and [OLAP](https://www.ibm.com/topics/olap)
databases (as seen in the image above), data is organized in rows and columns (and these are
called **Tables**), and queries are performed based on the values in those columns. However,
in certain applications including image recognition, natural language processing, and recommendation
systems, data is often represented as vectors in a high-dimensional space, and these vectors, plus
an id and a payload, are the elements we store in something called a **Collection** within a vector
database like Qdrant.

A vector in this context is a mathematical representation of an object or data point, where elements of
the vector implicitly or explicitly correspond to specific features or attributes of the object. For example,
in an image recognition system, a vector could represent an image, with each element of the vector
representing a pixel value or a descriptor/characteristic of that pixel. In a music recommendation
system, each vector could represent a song, and elements of the vector would capture song characteristics
such as tempo, genre, lyrics, and so on.

Vector databases are optimized for **storing** and **querying** these high-dimensional vectors
efficiently, and they often use specialized data structures and indexing techniques such as
Hierarchical Navigable Small World (HNSW) – which is used to implement Approximate Nearest
Neighbors – and Product Quantization, among others. These databases enable fast similarity
and semantic search while allowing users to find vectors that are the closest to a given query
vector based on some distance metric. The most commonly used distance metrics are Euclidean
Distance, Cosine Similarity, and Dot Product, and these three are fully supported Qdrant.

Here’s a quick overview of the three:

- [**Cosine Similarity**](https://en.wikipedia.org/wiki/Cosine_similarity) \- Cosine similarity
is a way to measure how similar two vectors are. To simplify, it reflects whether the vectors
have the same direction (similar) or are poles apart. Cosine similarity is often used with text representations
to compare how similar two documents or sentences are to each other. The output of cosine similarity ranges
from -1 to 1, where -1 means the two vectors are completely dissimilar, and 1 indicates maximum similarity.
- [**Dot Product**](https://en.wikipedia.org/wiki/Dot_product) \- The dot product similarity metric is another way
of measuring how similar two vectors are. Unlike cosine similarity, it also considers the length of the vectors.
This might be important when, for example, vector representations of your documents are built
based on the term (word) frequencies. The dot product similarity is calculated by multiplying the respective values
in the two vectors and then summing those products. The higher the sum, the more similar the two vectors are.
If you normalize the vectors (so the numbers in them sum up to 1), the dot product similarity will become
the cosine similarity.
- [**Euclidean Distance**](https://en.wikipedia.org/wiki/Euclidean_distance) \- Euclidean
distance is a way to measure the distance between two points in space, similar to how we
measure the distance between two places on a map. It’s calculated by finding the square root
of the sum of the squared differences between the two points’ coordinates. This distance metric
is also commonly used in machine learning to measure how similar or dissimilar two vectors are.

Now that we know what vector databases are and how they are structurally different than other
databases, let’s go over why they are important.

## [Anchor](https://qdrant.tech/documentation/overview/\#why-do-we-need-vector-databases) Why do we need Vector Databases?

Vector databases play a crucial role in various applications that require similarity search, such
as recommendation systems, content-based image retrieval, and personalized search. By taking
advantage of their efficient indexing and searching techniques, vector databases enable faster
and more accurate retrieval of unstructured data already represented as vectors, which can
help put in front of users the most relevant results to their queries.

In addition, other benefits of using vector databases include:

1. Efficient storage and indexing of high-dimensional data.
2. Ability to handle large-scale datasets with billions of data points.
3. Support for real-time analytics and queries.
4. Ability to handle vectors derived from complex data types such as images, videos, and natural language text.
5. Improved performance and reduced latency in machine learning and AI applications.
6. Reduced development and deployment time and cost compared to building a custom solution.

Keep in mind that the specific benefits of using a vector database may vary depending on the
use case of your organization and the features of the database you ultimately choose.

Let’s now evaluate, at a high-level, the way Qdrant is architected.

## [Anchor](https://qdrant.tech/documentation/overview/\#high-level-overview-of-qdrants-architecture) High-Level Overview of Qdrant’s Architecture

![qdrant](https://raw.githubusercontent.com/ramonpzg/mlops-sydney-2023/main/images/qdrant_overview_high_level.png)

The diagram above represents a high-level overview of some of the main components of Qdrant. Here
are the terminologies you should get familiar with.

- [Collections](https://qdrant.tech/documentation/concepts/collections/): A collection is a named set of points (vectors with a payload) among which you can search. The vector of each point within the same collection must have the same dimensionality and be compared by a single metric. [Named vectors](https://qdrant.tech/documentation/concepts/collections/#collection-with-multiple-vectors) can be used to have multiple vectors in a single point, each of which can have their own dimensionality and metric requirements.
- [Distance Metrics](https://en.wikipedia.org/wiki/Metric_space): These are used to measure
similarities among vectors and they must be selected at the same time you are creating a
collection. The choice of metric depends on the way the vectors were obtained and, in particular,
on the neural network that will be used to encode new queries.
- [Points](https://qdrant.tech/documentation/concepts/points/): The points are the central entity that
Qdrant operates with and they consist of a vector and an optional id and payload.
  - id: a unique identifier for your vectors.
  - Vector: a high-dimensional representation of data, for example, an image, a sound, a document, a video, etc.
  - [Payload](https://qdrant.tech/documentation/concepts/payload/): A payload is a JSON object with additional data you can add to a vector.
- [Storage](https://qdrant.tech/documentation/concepts/storage/): Qdrant can use one of two options for
storage, **In-memory** storage (Stores all vectors in RAM, has the highest speed since disk
access is required only for persistence), or **Memmap** storage, (creates a virtual address
space associated with the file on disk).
- Clients: the programming languages you can use to connect to Qdrant.

## [Anchor](https://qdrant.tech/documentation/overview/\#next-steps) Next Steps

Now that you know more about vector databases and Qdrant, you are ready to get started with one
of our tutorials. If you’ve never used a vector database, go ahead and jump straight into
the **Getting Started** section. Conversely, if you are a seasoned developer in these
technology, jump to the section most relevant to your use case.

As you go through the tutorials, please let us know if any questions come up in our
[Discord channel here](https://qdrant.to/discord). 😎

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/overview/_index.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/overview/_index.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-148-lllmstxt|>
## practicle-examples
- [Articles](https://qdrant.tech/articles/)
- Practical Examples

#### Practical Examples

Building blocks and reference implementations to help you get started with Qdrant. Learn how to use Qdrant to solve real-world problems and build the next generation of AI applications.

[![Preview](https://qdrant.tech/articles_data/binary-quantization-openai/preview/preview.jpg)\\
**Optimizing OpenAI Embeddings: Enhance Efficiency with Qdrant's Binary Quantization** \\
Explore how Qdrant's Binary Quantization can significantly improve the efficiency and performance of OpenAI's Ada-003 embeddings. Learn best practices for real-time search applications.\\
\\
Nirant Kasliwal\\
\\
February 21, 2024](https://qdrant.tech/articles/binary-quantization-openai/)[![Preview](https://qdrant.tech/articles_data/food-discovery-demo/preview/preview.jpg)\\
**Food Discovery Demo** \\
Feeling hungry? Find the perfect meal with Qdrant's multimodal semantic search.\\
\\
Kacper Łukawski\\
\\
September 05, 2023](https://qdrant.tech/articles/food-discovery-demo/)[![Preview](https://qdrant.tech/articles_data/search-as-you-type/preview/preview.jpg)\\
**Semantic Search As You Type** \\
To show off Qdrant's performance, we show how to do a quick search-as-you-type that will come back within a few milliseconds.\\
\\
Andre Bogus\\
\\
August 14, 2023](https://qdrant.tech/articles/search-as-you-type/)[![Preview](https://qdrant.tech/articles_data/serverless/preview/preview.jpg)\\
**Serverless Semantic Search** \\
Create a serverless semantic search engine using nothing but Qdrant and free cloud services.\\
\\
Andre Bogus\\
\\
July 12, 2023](https://qdrant.tech/articles/serverless/)[![Preview](https://qdrant.tech/articles_data/chatgpt-plugin/preview/preview.jpg)\\
**Extending ChatGPT with a Qdrant-based knowledge base** \\
ChatGPT factuality might be improved with semantic search. Here is how.\\
\\
Kacper Łukawski\\
\\
March 23, 2023](https://qdrant.tech/articles/chatgpt-plugin/)[![Preview](https://qdrant.tech/articles_data/langchain-integration/preview/preview.jpg)\\
**Using LangChain for Question Answering with Qdrant** \\
We combined LangChain, a pre-trained LLM from OpenAI, SentenceTransformers & Qdrant to create a question answering system with just a few lines of code. Learn more!\\
\\
Kacper Łukawski\\
\\
January 31, 2023](https://qdrant.tech/articles/langchain-integration/)[![Preview](https://qdrant.tech/articles_data/qa-with-cohere-and-qdrant/preview/preview.jpg)\\
**Question Answering as a Service with Cohere and Qdrant** \\
End-to-end Question Answering system for the biomedical data with SaaS tools: Cohere co.embed API and Qdrant\\
\\
Kacper Łukawski\\
\\
November 29, 2022](https://qdrant.tech/articles/qa-with-cohere-and-qdrant/)[![Preview](https://qdrant.tech/articles_data/faq-question-answering/preview/preview.jpg)\\
**Q&A with Similarity Learning** \\
A complete guide to building a Q&A system using Quaterion and SentenceTransformers.\\
\\
George Panchuk\\
\\
June 28, 2022](https://qdrant.tech/articles/faq-question-answering/)

×

[Powered by](https://qdrant.tech/)

<|page-149-lllmstxt|>
## filtered-search-benchmark
February 13, 2023

Dataset:keyword-100range-100int-2048100-kw-small-vocabkeyword-2048geo-radius-100range-2048geo-radius-2048int-100h-and-m-2048arxiv-titles-384

Plot values:

Regular search

Filter search

_Download raw data: [here](https://qdrant.tech/benchmarks/filter-result-2023-02-03.json)_

## [Anchor](https://qdrant.tech/benchmarks/filtered-search-benchmark/\#filtered-results) Filtered Results

As you can see from the charts, there are three main patterns:

- **Speed boost** \- for some engines/queries, the filtered search is faster than the unfiltered one. It might happen if the filter is restrictive enough, to completely avoid the usage of the vector index.

- **Speed downturn** \- some engines struggle to keep high RPS, it might be related to the requirement of building a filtering mask for the dataset, as described above.

- **Accuracy collapse** \- some engines are loosing accuracy dramatically under some filters. It is related to the fact that the HNSW graph becomes disconnected, and the search becomes unreliable.


Qdrant avoids all these problems and also benefits from the speed boost, as it implements an advanced [query planning strategy](https://qdrant.tech/documentation/search/#query-planning).

Share this article

[x](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Ffiltered-search-benchmark%2F&text= "x")[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Ffiltered-search-benchmark%2F "LinkedIn")

Up!

<|page-150-lllmstxt|>
## database-optimization
- [Documentation](https://qdrant.tech/documentation/)
- [Faq](https://qdrant.tech/documentation/faq/)
- Database Optimization