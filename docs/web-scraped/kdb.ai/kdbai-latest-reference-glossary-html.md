# Source: https://code.kx.com/kdbai/latest/reference/glossary.html

Title: KDB.AI Glossary - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/reference/glossary.html

Markdown Content:
_This page contains descriptions of commonly used terminology with vector databases._

Cosine similarity
-----------------

Cosine similarity is a measure of the cosine of the angle between two vectors. In document embeddings, each dimension can represent a word's frequency or TF-IDF weight. However, two documents of different lengths can have drastically different word frequencies yet the same word distribution. Since this places them in similar directions in vector space but not similar distances, cosine similarity is a great choice.

Database
--------

A database is collection of related data stored and accessed electronically using a Database Management System (DBMS). Databases are likely to be hosted on computer clusters or cloud storage.

Database Management System (DBMS)
---------------------------------

The DBMS provides various functions that allow entry, storage and retrieval of large quantities of information and provides ways to manage how that information is organized.

Because of the close relationship between them, the term "database" is often used casually to refer to both a database and the DBMS used to manipulate it.

Dense vector
------------

A dense vector is a type of vector where most of the elements are non-zero. Dense vectors are information-rich, with densely-packed data in every dimension. By providing a compact yet expressive way to represent data, **dense vectors are valuable for various tasks in machine learning.

Dot product
-----------

The Dot product measures the similarity or alignment between two vectors. It quantifies how much the vectors point in the same direction. For two vectors A and B in n-dimensional space, the Dot product is calculated as the sum of the products of their corresponding elements.

The Dot product can be positive (if vectors are aligned in the same direction), negative (if vectors are aligned in opposite directions), or zero (if vectors are orthogonal). With this metric, both magnitude and direction of vectors are used.

Euclidean vector
----------------

A Euclidean vector is a geometric object that has magnitude, or length, and direction.

Euclidean distance
------------------

Euclidean distance is a measure of the straight-line distance between two points in Euclidean space. In the context of vectors, Euclidean distance is calculated as the square root of the sum of squared differences between corresponding elements of two vectors. With this metric, both magnitude and direction of vectors are used.

Facebook AI Similarity Search (FAISS)
-------------------------------------

Facebook AI Similarity Search (FAISS) is a library that enables efficient similarity searches, especially in high-dimensional spaces. It’s particularly useful when you have a set of vectors and need to find the most similar vectors within that set based on a query.

FAISS indexes are primarily stored in RAM (Random Access Memory). The library supports distance metrics like L2 (Euclidean) distances, Dot products for vector comparison, Cosine similarity, as well as HNSW (Hierarchical Navigable Small World), the search algorithm for Approximate Nearest Neighbor (ANN).

Filter
------

Filter parameters are used for applying custom filtering to your database query. This allows you to include or exclude certain data from your query and can improve the search response time.

Flat search
-----------

A flat search performs an exhaustive search against all vectors in the search space it can be configured with a number of distance metrics. As the search is exhaustive it finds the exact nearest neighbors without approximations.

Flat Inverted File (IVF) search
-------------------------------

When using a Flat Inverted File (IVF) search, you firstly train the index on a set of points that are used to generate cluster centroids using a k-means algorithm. The data is not partitioned into a cluster based on centroid distance. The search is performed by running a flat search against the most relevant clusters. As only a subset of the data is searched, the results are returned much quicker, but as a consequence can be less accurate.

Hierarchical Navigable Small Worlds (HNSW)
------------------------------------------

At a fundamental level, a HNSW incrementally generates a hierarchical, multi-level graph structure which allows searches to navigate through the layers of the graph to find increasingly similar data in the graph to the data being searched greedily. This approach is extremely efficient with search performance a measure of the complexity of the graph.

Hybrid search
-------------

Hybrid search is a specialized vector search that increases the relevancy of search results by combining two search methods: the precision of keyword-based sparse vector search, and the contextual understanding of semantic dense vector search.

Index
-----

Vector databases utilize a crucial element known as the index to process data. The creation of this index involves applying an algorithm to the vector embeddings stored within the database.

This algorithm functions to map these vectors to a specialized data structure, facilitating rapid searches. Searches are more efficient this way due to the index's condensed representation of the original vector data. This compactness reduces memory requirements and enhances accessibility when contrasted with processing searches via raw embeddings.

Inverted File with Product Quantization (IVFPQ)
-----------------------------------------------

The IVFPQ (Inverted File with Product Quantization)** is a data structure and algorithm used in the Faiss library for efficient approximate nearest neighbor search in high-dimensional spaces. It's leveraging the **IVFPQ** techniques to accelerate the search process.

The IVFPQ algorithm divides the vector space into a set of Voronoi cells (partitions of a vector space) using the Product Quantization method. Then each cell is associated with an inverted list that stores the identifiers of the vectors falling into that cell in an inverted file structure. This ivf structure provides a mapping between each Voronoi cell and the vectors associated with it.

During the search, a query vector is assigned to a specific Voronoi cell, only the vectors in that cell are considered for the nearest neighbor search. This significantly reduces the search space and improves the efficiency of the search process.

To find the nearest neighbors, the algorithm computes the distances between the query vector and the vectors in the assigned Voronoi cell using a distance metric (e.g., Euclidean distance or cosine similarity).

The search algorithm efficiently traverses the inverted file and retrieves the vectors with the closest distances to the query vector.

LangChain
---------

Langchain is an open-source framework that facilitates the creation of large language model (LLM) based applications and chatbots. It provides a standard interface for interacting with LLMs, as well as a number of features that make it easier to build complex applications.

Large Language Models (LLMs)
----------------------------

Large language models are algorithmic predictors for text, which are able to process enormous amounts of text data. These models come in various forms including: Autoencoder-Based, Sequence-to-Sequence, Recursive Neural Network, and the most well-known, Transformer-Based Models.

List type
---------

List type is a fundamental data type in programming and data management, providing the building blocks for more complex data structures and operations. A list type represents a collection of values, all of which are of the same type. Lists can store multiple values in an ordered sequence. List types are used when you need to store multiple values of the same type together, allowing for operations on the entire collection.

Examples:

*   List of integers: `[1, 2, 3, 4]`
*   List of floats: `[1.1, 2.2, 3.3]`
*   List of characters: `['a', 'b', 'c']`
*   List of booleans: `[true, false, true]`

Machine learning (ML)
---------------------

Machine learning (ML) is a computational method that enables computers to learn and perform tasks by analysing large datasets without being explicitly programmed.

Machine learning model
----------------------

A machine learning model is a program trained to identify specific patterns. You train the model using a dataset, equipping it with an algorithm to interpret and learn from that data. After the model has been trained, it generalizes patterns it learned to make predictions for new datasets.

Metadata is the additional information associated with the vector embeddings stored in a vector database. It enriches the vector entries by providing context, labels, and other relevant attributes. For example, for image vectors, metadata could include labels like "sky," "sunset," or "clouds."

Query
-----

A query is used to extract data from a database and present it in a readable form. In the case of a vector database, you first need to process the queries into the same vector space as the database. For text-based search, this means that plain human text needs to be converted into the same format as the embeddings themselves.

The process involves creating a **query vector**. This is generated from the input text, processing it through your embedding model (and any other feature engineering steps also applied to your other embeddings), and finally creating a query vector that lands in the appropriate part of the vector space. Other than text as an input, code, images, video, audio and other formats can be used, but all will still generate a numerical arrayed query vector.

The query vector should be generated using the same embedding model that was used to generate your content embeddings stored in the database. This is important because you need to map existing content in the same embedding format as your query, in the same vector space, to perform similarity calculations.

q Inter-Process Communication (qIPC)
------------------------------------

[qIPC](https://code.kx.com/q/basics/ipc/) is a q/kdb+ communication method used for exchanging data between processes running on the same machine or within a network. It's designed to be highly efficient, minimizing latency and maximizing throughput. Ideal for high-performance computing environments, real-time data processing, and applications requiring fast, low-latency communication between processes.

Retrieval Augmented Generation (RAG)
------------------------------------

Retrieval Augmented Generation, known as RAG, is a framework that optimizes the way LLMs operate. They currently operate within the static knowledge snapshot captured during their training, so face significant challenges staying up-to-date with recent world events. RAG enables these language models to access relevant data from external knowledge bases, enriching their responses with current and contextually accurate information.

Scalar type
-----------

Scalar type is a fundamental data type in programming and data management, providing the building blocks for more complex data structures and operations. A scalar type represents a single value. It is the most basic type of data, such as an integer, float, character, or boolean. Scalar types are used when you need to store individual values that are not collections or sequences.

Examples:

*   Integer: `42`
*   Float: `3.14`
*   Character: `a`
*   Boolean: `true` or `false`

Schema
------

In a vector database, a schema defines how data is stored, organized, and retrieved. Unlike traditional databases that establish relationships between elements based on explicit links or hierarchy, vector databases associate records algorithmically based on the similarity of their data attributes.

Sparse vector
-------------

Given a fixed vector space basis, a vector is sparse if it can be represented by a linear combination of a small subset of the basis vectors. Typically, the size of the subset is a small fraction of the dimension of the vector space, but no absolute threshold is imposed.

Time series data
----------------

Time series data is a collection of data points that are indexed or listed in chronological order based on time. Time series data allows us to observe how variables change over time. In other words, time serves as a crucial variable, revealing both the adjustments within the data points and the final outcomes.

Training
--------

In the context of vector databases, training is the process of creating vector embeddings for the data that you want to index. During training, a machine learning model learns to describe your data (whether it’s text, images, or other types) as vector embeddings.

The model assigns values to each dimension of the vector, capturing the essential features of the data. These embeddings are closely related to the original data and are stored in the vector database. Training allows efficient similarity search and retrieval.

In KDB.AI, you can train your IVF or IVFPQ indexes. In this case, training is a process that starts with creating an empty index. Next, you load the data and train the IVF index. This initiates training of K-means clustering, which results in the formation of k centroids (k = the number of inverted lists that you want in the IVF). Once it's trained you need to add the vectors to the index.

Vector database
---------------

A vector database is a specialized type of database designed to store, manage and index massive quantities of high-dimensional vector data. Unlike relational databases that organize information in tables, rows, and columns, vector databases are based on vectors. They support AI tasks and enable applications that rely on similarity and context.

In a vector database, data is automatically arranged spatially by content similarity, and that similarity is on content meaning rather than just keywords. With advances in Machine Learning, machines are now able to understand the content we provide to them.

Vector databases allow a high degree of granularity on the similarities, so books in a library, for example, could be searched by author's writing style, or story plots, all within the same storage structure, without having to manually label or tag the content itself for exact lookups that have no contextual grounding.

Vector embeddings
-----------------

Vector embeddings are a powerful way to convert various types of data (such as words, sentences, or images) into numerical representations (vectors) that capture their meaning and relationships. Embeddings map data points into a multidimensional space, where similar data points cluster closer together. Vector embeddings allow to represent complex data in a structured and meaningful way using numerical vectors.
