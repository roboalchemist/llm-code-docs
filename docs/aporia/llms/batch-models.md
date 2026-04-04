# Source: https://docs.aporia.com/storing-your-predictions/batch-models.md

# Source: https://docs.aporia.com/v1/storing-your-predictions/batch-models.md

# Batch Models

If your model runs periodically every X days, we refer to it as a **batch model** (as opposed to a real-time model).

Typically, storing the predictions of batch models is straightforward. The code examples that follow are naive "illustrations" of how to do so.

### Example: Pandas to Parquet on S3

If you use Pandas, you can append any `DataFrame` to a Parquet file on S3 or other cloud storages by using the [fastparquet](https://fastparquet.readthedocs.io/en/latest/) library:

```python
import fastparquet

# Preprocess & predict
X = preprocess(...)
y = model.predict(X_pred)

# Concatenate features, predictions and any other metadata
df = ...

# Store predictions
fastparquet.write(
    filename=f"s3://my-models/{MODEL_ID}/{MODEL_VERSION}/serving.parquet",
    data=df,
    append=True,
)
```

### Example: Pyspark to Delta Lake

This example is especially useful on [Databricks](https://www.databricks.com/), but can you can use it on [Delta Lake](https://delta.io/) + [Spark on K8s operator](https://github.com/GoogleCloudPlatform/spark-on-k8s-operator) for example:

```python
# Predict on SparkML
y = model.transform(X)

# Concatenate features, predictions and any other metadata
df = ...

# Append to a Delta table
df.write.format("delta").mode("append").saveAsTable("my_model_serving")
```
