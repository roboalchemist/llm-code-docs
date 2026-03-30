# We'll use the first 100 entries from this dataset and exclude some unused columns.
dataset = dataset.select(range(100)).remove_columns(["gold_label", "genre"])

```

- **Convert the dataset into a Spark dataframe:**

```python
dataset.to_parquet("/dbfs/pq.pq")
dataset_df = spark.read.parquet("file:/dbfs/pq.pq")

```

### [Anchor](https://qdrant.tech/documentation/send-data/databricks/\#vectorizing-the-data) Vectorizing the data

In this section, we’ll be generating both dense and sparse vectors for our rows using [FastEmbed](https://qdrant.github.io/fastembed/). We’ll create a user-defined function (UDF) to handle this step.

#### [Anchor](https://qdrant.tech/documentation/send-data/databricks/\#creating-the-vectorization-function) Creating the vectorization function

```python
from fastembed import TextEmbedding, SparseTextEmbedding

def vectorize(partition_data):
    # Initialize dense and sparse models
    dense_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")
    sparse_model = SparseTextEmbedding(model_name="Qdrant/bm25")

    for row in partition_data:
        # Generate dense and sparse vectors
        dense_vector = next(dense_model.embed(row.sentence1))
        sparse_vector = next(sparse_model.embed(row.sentence2))

        yield [\
            row.sentence1,  # 1st column: original text\
            row.sentence2,  # 2nd column: original text\
            dense_vector.tolist(),  # 3rd column: dense vector\
            sparse_vector.indices.tolist(),  # 4th column: sparse vector indices\
            sparse_vector.values.tolist(),  # 5th column: sparse vector values\
        ]

```

We’re using the [BAAI/bge-small-en-v1.5](https://huggingface.co/BAAI/bge-small-en-v1.5) model for dense embeddings and [BM25](https://huggingface.co/Qdrant/bm25) for sparse embeddings.

#### [Anchor](https://qdrant.tech/documentation/send-data/databricks/\#applying-the-udf-on-our-dataframe) Applying the UDF on our dataframe

Next, let’s apply our `vectorize` UDF on our Spark dataframe to generate embeddings.

```python
embeddings = dataset_df.rdd.mapPartitions(vectorize)

```

The `mapPartitions()` method returns a [Resilient Distributed Dataset (RDD)](https://www.databricks.com/glossary/what-is-rdd) which should then be converted back to a Spark dataframe.

#### [Anchor](https://qdrant.tech/documentation/send-data/databricks/\#building-the-new-spark-dataframe-with-the-vectorized-data) Building the new Spark dataframe with the vectorized data

We’ll now create a new Spark dataframe ( `embeddings_df`) with the vectorized data using the specified schema.

```python
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, FloatType, IntegerType