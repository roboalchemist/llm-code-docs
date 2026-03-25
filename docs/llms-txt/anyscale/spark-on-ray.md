# Source: https://docs.anyscale.com/tutorials/spark-on-ray.md

# Run Spark on Ray

[View Markdown](/tutorials/spark-on-ray.md)

# Run Spark on Ray

This example demonstrates how to run a simple data processing example with [RayDP](https://github.com/ray-project/raydp), a library for running Spark on Ray.

## Install the Anyscale CLI[​](#install-the-anyscale-cli "Direct link to Install the Anyscale CLI")

```
pip install -U anyscale
anyscale login
```

## Submit the job.[​](#submit-the-job "Direct link to Submit the job.")

Clone the example from GitHub.

```
git clone https://github.com/anyscale/examples.git
cd examples/spark_on_ray
```

Submit the job.

```
anyscale job submit -f job.yaml
```

## Understanding the example[​](#understanding-the-example "Direct link to Understanding the example")

* This example is extremely simple and just uses basic Spark APIs. More configuration is required to read from blob stores like S3.
