# Source: https://docs.mage.ai/integrations/compute/spark-pro.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# PySpark in Mage Pro

> This guide explains how to use PySpark in Mage Pro, including how to run PySpark blocks in batch pipelines, connect to Spark on Kubernetes, manage dependencies like Apache Iceberg, and access cloud storage securely.


export const ProOnly = ({button = 'Get started for free', description = 'Try our fully managed solution to access this advanced feature.', source = 'documentation', title = 'Only in Mage Pro.'}) => <a href={`https://cloud.mage.ai/sign-up?source=${source}`} className="block my-4 px-5 py-4 overflow-hidden rounded-xl flex gap-3 border border-emerald-500/20 bg-emerald-50/50 dark:border-emerald-500/30 dark:bg-emerald-500/10" target="_blank">
    <div style={{
  display: 'flex',
  alignItems: 'center',
  width: '100%'
}}>
      <div className="text-sm prose min-w-0 text-emerald-900 dark:text-emerald-200" style={{
  flex: 1
}}>
        {title}
        <p className="normal">{description}</p>
      </div>

      <div> </div>

      <div>
        <ProButton label={button} href={`https://cloud.mage.ai/sign-up?source=${source}`} />
      </div>
    </div>
  </a>;

export const ProButton = ({href, label = 'Get started with Mage Pro for free', source = 'documentation'}) => <div style={{
  height: 32,
  position: 'relative'
}}>
    <a target="_blank" className="group px-4 py-1.5 relative inline-flex items-center text-sm font-medium rounded-full" href={href ?? `https://cloud.mage.ai/sign-up?source=${source}`}>
      <span className="absolute inset-0 bg-primary-dark dark:bg-primary-light/10 border-primary-light/30 rounded-full dark:border group-hover:opacity-[0.9] dark:group-hover:border-primary-light/60">
      </span>

      <div className="mr-0.5 space-x-2.5 flex items-center">
        <span class="z-10 text-white dark:text-primary-light">
          {label}
        </span>

        <svg width="3" height="24" viewBox="0 -9 3 24" class="h-5 rotate-0 overflow-visible text-white/90 dark:text-primary-light">
          <path d="M0 0L3 3L0 6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path>
        </svg>
      </div>
    </a>
  </div>;

<ProOnly source="spark" />

Mage Pro provides built-in support for running PySpark code inside your pipelines. You can run distributed Spark jobs directly within a Mage Pro batch pipeline, with automatic resource management, cloud integration, and observability.

Use PySpark in Mage to transform large datasets, connect to cloud object storage like **GCS or S3**, and integrate with modern data lake formats like **Apache Iceberg**.

## How to Use PySpark in Mage Pro

Follow these steps to run PySpark code in Mage Pro:

1. Create a **batch pipeline** in the Mage UI.
2. Add a **block** of type: `Data Loader`, `Transformer`, `Data Exporter`, or `Custom`.
3. In your block, write PySpark code using the provided `SparkSession`.
4. Install or mount any required Spark JARs, such as those for Iceberg or cloud storage access.

## Example Pipeline

Create a standard **batch pipeline** and configure the following settings in the pipeline's `metadata.yaml` file to ensure PySpark works properly:

```yaml  theme={"system"}
cache_block_output_in_memory: true
run_pipeline_in_one_process: true
```

These settings ensure data is passed in-memory between PySpark blocks and the pipeline runs in a single JVM process for Spark compatibility.

### Data Loader Block (PySpark)

```python  theme={"system"}
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
from pyspark.sql import Row, SparkSession

@data_loader
def load_data(*args, **kwargs):
    spark = SparkSession.builder.getOrCreate()
    data = [
        Row(id=1, name="Alice", age=29, salary=50000),
        Row(id=2, name="Bob", age=35, salary=60000),
        Row(id=3, name="Charlie", age=40, salary=70000),
        Row(id=4, name="David", age=45, salary=None)  # Null value example
    ]

    df = spark.createDataFrame(data)
    df.show()
    return df
```

### Data Exporter Block

```python  theme={"system"}
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_data(df, *args, **kwargs):
    df.write.csv("spark_output", header=True, mode="overwrite")
```

This example pipeline loads structured data into a Spark DataFrame and writes it to disk in CSV format.

## Connecting to Spark on Kubernetes

Mage Pro can connect to an external Spark cluster running on Kubernetes. This allows you to leverage existing Spark infrastructure or run Spark jobs on a dedicated Kubernetes cluster.

### Option 1: Configure via metadata.yaml (Recommended)

Configure Spark connection settings in your project's `metadata.yaml` file:

```yaml  theme={"system"}
spark_config:
  # Application name
  app_name: 'my spark app'
  # Master URL to connect to Spark on Kubernetes
  # For Kubernetes native mode:
  spark_master: 'k8s://https://kubernetes.default.svc:443'
  # Or for standalone Spark cluster in Kubernetes:
  # spark_master: 'spark://spark-master-service:7077'
  
  # Executor environment variables
  executor_env: {}
  
  # Jar files to be uploaded to the cluster and added to the classpath
  spark_jars: []
  
  # Path where Spark is installed on worker nodes (if applicable)
  spark_home: null
  
  # Additional Spark configuration options
  others:
    spark.executor.memory: '4g'
    spark.executor.cores: '2'
    spark.kubernetes.namespace: 'default'
    spark.kubernetes.container.image: 'your-spark-image:tag'
```

### Option 2: Configure via Environment Variable

Alternatively, you can set the `SPARK_MASTER_HOST` environment variable in your Mage Pro workspace configuration:

* For Kubernetes native mode: `SPARK_MASTER_HOST=k8s://https://kubernetes.default.svc:443`
* For standalone Spark cluster: `SPARK_MASTER_HOST=spark://spark-master-service:7077`

### Setting Up Spark on Kubernetes

If you need to deploy Spark on Kubernetes first, you can use Helm:

```bash  theme={"system"}
# Add the Bitnami Helm repository
helm repo add bitnami https://charts.bitnami.com/bitnami

# Install Spark cluster
helm install my-spark bitnami/spark

# Get the Spark master service URL
kubectl get svc my-spark-spark-master-svc
```

Then use the service URL in your `spark_master` configuration. For example:

* Service name: `my-spark-spark-master-svc`
* Port: `7077`
* Configuration: `spark_master: 'spark://my-spark-spark-master-svc:7077'`

### Using Spark in Your Code

Once configured, you can use Spark in your pipeline blocks:

```python  theme={"system"}
from pyspark.sql import SparkSession

# SparkSession will automatically use the configuration from metadata.yaml
spark = SparkSession.builder.getOrCreate()

# Your Spark operations here
df = spark.read.csv("your-data.csv")
```

The Spark session will automatically connect to your configured Kubernetes Spark cluster.

## Benefits of Running PySpark in Mage Pro

Mage Pro handles all the infrastructure so you can focus on your PySpark code:

* ⚙️ Distributed execution with automatic pod scheduling and resource allocation
* ☁️ Seamless cloud integration with GCS, S3, and service account/IAM-based authentication
* 🧩 Support for Spark JARs and connectors like Apache Iceberg, GCS connectors, Delta Lake, and more
* 📈 Built-in observability, with access to logs, resource usage, and block-level monitoring in the Mage UI

## Notes

* You can customize the `SparkSession` in any block using `.builder.config(...)` to tune performance or integrate external tools.
* Cloud storage credentials (e.g., a GCP service account key or AWS credentials) must be mounted and accessible inside the Mage Pro cluster.
* For advanced use cases (e.g., Apache Iceberg), see the [Iceberg + PySpark guide](/integrations/databases/Iceberg#using-iceberg-with-pyspark).


Built with [Mintlify](https://mintlify.com).