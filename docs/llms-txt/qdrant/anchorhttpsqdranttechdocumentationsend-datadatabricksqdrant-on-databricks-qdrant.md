# [Anchor](https://qdrant.tech/documentation/send-data/databricks/\#qdrant-on-databricks) Qdrant on Databricks

| Time: 30 min | Level: Intermediate | [Complete Notebook](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/4750876096379825/93425612168199/6949977306828869/latest.html) |
| --- | --- | --- |

[Databricks](https://www.databricks.com/) is a unified analytics platform for working with big data and AI. It’s built around Apache Spark, a powerful open-source distributed computing system well-suited for processing large-scale datasets and performing complex analytics tasks.

Apache Spark is designed to scale horizontally, meaning it can handle expensive operations like generating vector embeddings by distributing computation across a cluster of machines. This scalability is crucial when dealing with large datasets.

In this example, we will demonstrate how to vectorize a dataset with dense and sparse embeddings using Qdrant’s [FastEmbed](https://qdrant.github.io/fastembed/) library. We will then load this vectorized data into a Qdrant cluster using the [Qdrant Spark connector](https://qdrant.tech/documentation/frameworks/spark/) on Databricks.

### [Anchor](https://qdrant.tech/documentation/send-data/databricks/\#setting-up-a-databricks-project) Setting up a Databricks project

- Set up a **[Databricks cluster](https://docs.databricks.com/en/compute/configure.html)** following the official documentation guidelines.

- Install the **[Qdrant Spark connector](https://qdrant.tech/documentation/frameworks/spark/)** as a library:

  - Navigate to the `Libraries` section in your cluster dashboard.

  - Click on `Install New` at the top-right to open the library installation modal.

  - Search for `io.qdrant:spark:VERSION` in the Maven packages and click on `Install`.

    ![Install the library](https://qdrant.tech/documentation/examples/databricks/library-install.png)
- Create a new **[Databricks notebook](https://docs.databricks.com/en/notebooks/index.html)** on your cluster to begin working with your data and libraries.


### [Anchor](https://qdrant.tech/documentation/send-data/databricks/\#download-a-dataset) Download a dataset

- **Install the required dependencies:**

```python
%pip install fastembed datasets

```

- **Download the dataset:**

```python
from datasets import load_dataset

dataset_name = "tasksource/med"
dataset = load_dataset(dataset_name, split="train")