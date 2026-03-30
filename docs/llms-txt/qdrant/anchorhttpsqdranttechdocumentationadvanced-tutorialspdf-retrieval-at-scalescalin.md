# [Anchor](https://qdrant.tech/documentation/advanced-tutorials/pdf-retrieval-at-scale/\#scaling-pdf-retrieval-with-qdrant) Scaling PDF Retrieval with Qdrant

![scaling-pdf-retrieval-qdrant](https://qdrant.tech/documentation/tutorials/pdf-retrieval-at-scale/image1.png)

| Time: 30 min | Level: Intermediate | Output: [GitHub](https://github.com/qdrant/examples/blob/master/pdf-retrieval-at-scale/ColPali_ColQwen2_Tutorial.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/qdrant/examples/blob/master/pdf-retrieval-at-scale/ColPali_ColQwen2_Tutorial.ipynb) |
| --- | --- | --- | --- |

Efficient PDF documents retrieval is a common requirement in tasks like **(agentic) retrieval-augmented generation (RAG)** and many other search-based applications. At the same time, setting up PDF documents retrieval is rarely possible without additional challenges.

Many traditional PDF retrieval solutions rely on **optical character recognition (OCR)** together with use case-specific heuristics to handle visually complex elements like tables, images and charts. These algorithms are often non-transferable – even within the same domain – with their task-customized parsing and chunking strategies, labor-intensive, prone to errors, and difficult to scale.

Recent advancements in **Vision Large Language Models (VLLMs)**, such as [**ColPali**](https://huggingface.co/blog/manu/colpali) and its successor [**ColQwen**](https://huggingface.co/vidore/colqwen2-v0.1), started the transformation of the PDF retrieval. These multimodal models work directly with PDF pages as inputs, no pre-processing required. Anything that can be converted into an **image** (think of PDFs as screenshots of document pages) can be effectively processed by these models. Being far simpler in use, VLLMs achieve state-of-the-art performance in PDF retrieval benchmarks like the [Visual Document Retrieval (ViDoRe) Benchmark](https://huggingface.co/spaces/vidore/vidore-leaderboard).

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/pdf-retrieval-at-scale/\#how-vllms-work-for-pdf-retrieval) How VLLMs Work for PDF Retrieval

VLLMs like **ColPali** and **ColQwen** generate **multivector representations** for each PDF page; the representations are stored and indexed in a vector database. During the retrieval process, models dynamically create multivector representations for (textual) user queries, and precise retrieval – matching between PDF pages and queries – is achieved through [late-interaction mechanism](https://qdrant.tech/blog/qdrant-colpali/#how-colpali-works-under-the-hood).

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/pdf-retrieval-at-scale/\#challenges-of-scaling-vllms) Challenges of Scaling VLLMs

The heavy multivector representations produced by VLLMs make PDF retrieval at scale computationally intensive. These models are inefficient for large-scale PDF retrieval tasks if used without optimization.

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/pdf-retrieval-at-scale/\#math-behind-the-scaling) Math Behind the Scaling

**ColPali** generates over **1,000 vectors per PDF page**, while its successor, **ColQwen**, generates slightly fewer — up to **768 vectors**, dynamically adjusted based on the image size. Typically, ColQwen produces **~700 vectors per page**.

To understand the impact, consider the construction of an [**HNSW index**](https://qdrant.tech/articles/what-is-a-vector-database/#1-indexing-hnsw-index-and-sending-data-to-qdrant), a common indexing algorithm for vector databases. Let’s roughly estimate the number of comparisons needed to insert a new PDF page into the index.

- **Vectors per page:** ~700 (ColQwen) or ~1,000 (ColPali)
- **[ef\_construct](https://qdrant.tech/documentation/concepts/indexing/#vector-index):** 100 (default)

The lower bound estimation for the number of vector comparisions comparisons would be:

700×700×100=49millions

Now imagine how much it will take to build an index on **20,000 pages**!

For ColPali, this number doubles. The result is **extremely slow index construction time**.

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/pdf-retrieval-at-scale/\#our-solution) Our Solution

We recommend reducing the number of vectors in a PDF page representation for the **first-stage retrieval**. After the first stage retrieval with a reduced amount of vectors, we propose to **rerank** retrieved subset with the original uncompressed representation.

The reduction of vectors can be achieved by applying a **mean pooling operation** to the multivector VLLM-generated outputs. Mean pooling averages the values across all vectors within a selected subgroup, condensing multiple vectors into a single representative vector. If done right, it allows the preservation of important information from the original page while significantly reducing the number of vectors.

VLLMs generate vectors corresponding to patches that represent different portions of a PDF page. These patches can be grouped in columns and rows of a PDF page.

For example:

- ColPali divides PDF page into **1,024 patches**.
- Applying mean pooling by rows (or columns) of this patch matrix reduces the page representation to just **32 vectors**.

![ColPali patching of a PDF page](https://qdrant.tech/documentation/tutorials/pdf-retrieval-at-scale/pooling-by-rows.png)

We tested this approach with the ColPali model, mean pooling its multivectors by PDF page rows. The results showed:

- **Indexing time faster by an order of magnitude**
- **Retrieval quality comparable to the original model**

For details of this experiment refer to our [gitHub repository](https://github.com/qdrant/demo-colpali-optimized), [ColPali optimization blog post](https://qdrant.tech/blog/colpali-qdrant-optimization/) or [webinar “PDF Retrieval at Scale”](https://www.youtube.com/watch?v=_h6SN1WwnLs)

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/pdf-retrieval-at-scale/\#goal-of-this-tutorial) Goal of This Tutorial

In this tutorial, we will demonstrate a scalable approach to PDF retrieval using **Qdrant** and **ColPali** & **ColQwen2** VLLMs.
The presented approach is **highly recommended** to avoid the common pitfalls of long indexing times and slow retrieval speeds.

In the following sections, we will demonstrate an optimized retrieval algorithm born out of our successful experimentation:

**First-Stage Retrieval with Mean-Pooled Vectors:**

- Construct an HNSW index using **only mean-pooled vectors**.
- Use them for the first-stage retrieval.

**Reranking with Original Model Multivectors:**

- Use the original multivectors from ColPali or ColQwen2 **to rerank** the results retrieved in the first stage.

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/pdf-retrieval-at-scale/\#setup) Setup

Install & import required libraries

```python