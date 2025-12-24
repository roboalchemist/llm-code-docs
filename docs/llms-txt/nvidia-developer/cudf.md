# Source: https://developer.nvidia.com/topics/ai/data-science/cuda-x-data-science-libraries/cudf.md

1. [AI](/topics/ai)

[Data Science](/topics/ai/data-science)
2. [CUDA-X Data Science Libraries](/topics/ai/data-science/cuda-x-data-science-libraries)

cuDF

# NVIDIA cuDF: GPU-Accelerated DataFrames

NVIDIA cuDF is an open source CUDA-X™ Data Science library that accelerates popular libraries like pandas, Polars, and Apache Spark on NVIDIA GPUs—delivering massive speedups for DataFrame operations with no code changes required. Built on highly optimized CUDA® primitives, cuDF taps into GPU parallelism and memory bandwidth to accelerate data processing and analytics workflows.   
  
Get Started:

[Accelerate pandas](#accel-pandas)[Accelerate Polars](#accel-polars)[Accelerate Apache Spark](#accel-apache)

* * *

## Key Features

### Maximize Performance With NVIDIA GPUs

cuDF is purpose-built to maximize GPU performance, optimizing core DataFrame operations with low-level CUDA primitives that fully leverage the parallelism and memory bandwidth of NVIDIA GPUs. 

### Accelerate With Zero Code Changes

GPU acceleration can be seamlessly integrated into existing pandas, Polars, or Apache Spark workflows using API-compatible layers like cudf.pandas and the Polars GPU engine—no code changes required.

### Integrate With the Python Data Science Ecosystem  

cuDF interoperates effortlessly with popular Python data science libraries like cuPy, Numba, and scikit-learn, allowing you to build end-to-end GPU-accelerated workflows.

#### Handle Memory Efficiently  

Built on the Apache Arrow format, cuDF utilizes highly efficient columnar data structures, vector processing, and zero-copy interfaces with other accelerated libraries, minimizing data movement overhead.

#### Process Larger Datasets With Unified Virtual Memory (UVM)

UVM allows cuDF to transparently manage data transfers between system RAM and GPU memory, enabling you to process datasets that exceed the VRAM of a single GPU without explicit memory management.

#### Scale to Distributed Architectures

DataFrame workflows can be scaled across multiple GPUs and compute nodes with cuDF—built for distributed processing in environments like Apache Spark.

* * *

## Turn cuDF On for Massive GPU Performance Gains

https://www.youtube-nocookie.com/embed/eThOYTJrbtA?&amp;rel=0

* * *

## Test Drive cuDF

### pandas  

pandas offers a flexible API for data manipulation. cuDF makes pandas more usable for medium to large datasets by accelerating operations on the GPU, with no code changes required.

[Launch on Colab](https://colab.research.google.com/github/rapidsai-community/showcase/blob/main/getting_started_tutorials/cudf_pandas_colab_demo.ipynb)

### Polars  

Polars is known for its performance and memory optimizations. Experience even faster execution when you call the GPU engine powered by cuDF.

[Launch on Colab](https://colab.research.google.com/github/rapidsai-community/showcase/blob/main/accelerated_data_processing_examples/polars_gpu_engine_demo.ipynb?utm_source=nvidia+mktg&amp;utm_medium=web&amp;utm_campaign=polars+launch)

### Apache Spark  

Apache Spark is a powerful engine for large-scale data processing. Learn how to use GPUs to significantly boost performance and cost efficiency.

[View Quick-Start Guide](https://docs.nvidia.com/spark-rapids/user-guide/latest/index.html)

* * *

## pandas Accelerated With cuDF

This section details how cuDF seamlessly integrates with and accelerates your existing pandas workflows.

Get Started

How It Works

Integrate cuDF directly into your environment to accelerate pandas. Follow these steps to get started.

### Install cuDF for pandas

#### **Quick Install With conda**

1. If not installed, download and run the install script. This will install the latest miniforge:

    wget &quot;https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh&quot; bash Miniforge3-$(uname)-$(uname -m).sh

2. Then install with:

    conda create -n rapids-25.12 -c rapidsai -c conda-forge \ cudf=25.12 python=3.13 cuda-version=13.0

#### **Quick Install With pip**

    Install via the NVIDIA PyPI index: pip install \ &quot;cudf-cu13==25.12.\*&quot;

See the complete install selector for docker, WSL2, and individual libraries.

[Install Selector  
](https://docs.rapids.ai/install?_gl=1*kwbd1w*_ga*MTE4NDAwMTQ1NS4xNzA5NzcwODcw*_ga_RKXFW6CM42*czE3NTIxODk0OTQkbzk1JGcwJHQxNzUyMTg5NDk0JGo2MCRsMCRoMA.. &quot;Download Workflows&quot;)

### Enable cuDF Acceleration of pandas With Zero Code Changes

cuDF implements zero-code-change acceleration through the cuDF.pandas module. This module is part of the cuDF package. Load it to seamlessly accelerate your existing pandas code. Enable it using one of these methods before importing or using pandas. For a step-by-step visual guide, watch [this video](https://www.youtube.com/watch?v=jFi60VQVmF4).

#### To accelerate IPython or Jupyter notebooks, use the magic command:

    %load\_ext cudf.pandas import pandas as pd ...

### To accelerate a Python script, use the Python module flag on the command line:

    python -m cudf.pandas script.py import pandas as pd ...

### If you can&#39;t use command-line flags, explicitly enable cudf.pandas via import:

    import cudf.pandas cudf.pandas.install() import pandas as pd ...

#### From Minutes to Seconds: cuDF Accelerates pandas  

Standard DuckDB data benchmark (5 GB) performance comparison between cudf.pandas and traditional pandas v2.2 (lower is better).

 ![A chart showing how cuDF accelerates pandas from minutes to seconds](https://developer.download.nvidia.com/images/cudf/cuda-diagram-data-science-charts-pandas.png)

Specs: HW: NVIDIA L4, CPU: Intel Xeon 8480CL | SW: pandas v2.2.1, NVIDIA RAPIDS™ cuDF 24.02

[Run the benchmark here.](https://github.com/rapidsai/cudf/blob/branch-25.06/docs/cudf/source/user_guide/performance-comparisons/performance-comparisons.ipynb)

### Hands-On Tutorials: Accelerate pandas on Colab

cuDF comes preinstalled in Google Colab, making it incredibly easy to get started. Simply switch to a GPU runtime and enable cudf.pandas at the top of your notebook to instantly accelerate your pandas workflows. Explore these starter kits for hands-on examples:

#### Starter Kit: Build an Interactive Data Analytics Dashboard

This kit demonstrates how to create responsive dashboards using pandas code and PyViz libraries, directly addressing the lag when exploring large-scale data (e.g., 7.3M+ rows of geospatial data). See how GPU acceleration with cuDF makes interactive filters update near instantly with zero code changes.

- 

Video: [Accelerated Exploratory Data Analysis With pandas on NVIDIA GPUs](https://www.youtube.com/watch?v=PJpCJsqcfOk) (16:07)

- 

Notebook: [Build an Interactive Dashboard Notebook](https://colab.research.google.com/gist/will-hill/aa24c3ffe1428c005af3793fcacf9bd2/cudf_pandas_opencellid_demo.ipynb)

#### Starter Kit: Process 18 Million Rows of Stock Data

This kit demonstrates how cuDF handles processing large volumes of time-series data in pandas, tackling bottlenecks like calculating simple moving averages with groupby().rolling(). See how GPU acceleration turns minutes of processing into seconds.

- 

Video: [Processing 18M Rows of Stock Data 20x Faster in cuDF pandas Accelerator Mode](https://www.youtube.com/watch?v=eThOYTJrbtA) (00:29)

- 

Notebook: [Get Started With Accelerating Stock Data](https://colab.research.google.com/github/rapidsai-community/showcase/blob/main/getting_started_tutorials/cudf_pandas_stocks_demo.ipynb?ncid=so-yout-962126#scrollTo=WmOguzNUcw4F)

#### Starter Kit: Process 8 GB of Text Data

This kit addresses the slowdowns pandas experiences from large string fields and memory-intensive operations like reading files, calculating string length, and merging DataFrames, providing massive end-to-end speedups. 

- 

Video: [RAPIDS cuDF Accelerates pandas up to 30x on an 8 GB Text Dataset ](https://youtu.be/AgFVwqDcXCs?si=D1wYmdRUOoPrgvvv)(00:35)

- 

Notebook: [Get Started With Accelerating Stock Data](https://colab.research.google.com/github/rapidsai-community/showcase/blob/main/accelerated_data_processing_examples/cudf_pandas_large_string.ipynb?ncid=so-yout-766280-vt27)

#### How cuDF Accelerates pandas

When cudf.pandas is enabled, it transforms how your pandas operations are executed, acting as a proxy that transparently intercepts your pandas calls. It attempts to execute these operations on the GPU first, utilizing cuDF’s highly optimized, GPU-accelerated functions. If a particular operation isn’t supported on the GPU, it falls back to the CPU, ensuring your code continues to run without errors. This seamless “GPU-first, CPU-fallback” mechanism allows you to continue using familiar pandas syntax and functions while benefiting from significant performance improvements.  
  
This approach ensures that your existing pandas code, including operations within third-party libraries that use pandas, generally works as is, without requiring manual modifications to specifically target the GPU.   
  
For a more granular explanation of the underlying architecture and how cudf.pandas achieves this seamless acceleration, refer to [our documentation](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/how-it-works/).

![A flowchart of how cuDF accelerates pandas](https://developer.download.nvidia.com/images/cudf/cuda-diagram-data-science-flow.png)

* * *

## Polars Accelerated With cuDF

This section details how the Polars GPU engine, powered by cuDF, seamlessly integrates and accelerates your Polars workflows.

Get Started

How It Works

Integrate the Polars GPU engine directly into your environment to accelerate Polars. Follow these steps to get started.

### Install Polars With GPU Support

Simply pip install Polars with the GPU feature flag.

    pip install polars[gpu]

### Configure Polars to Use the GPU Engine

Activate GPU acceleration for your Polars operations by configuring the engine. You can use the default GPU engine or customize it for finer control.

#### Default GPU Engine

Materialize the Polars LazyFrame into a DataFrame with the default GPU engine configuration by calling .collect(engine=&quot;gpu&quot;):

    import polars as pl ldf = pl.LazyFrame({&quot;a&quot;: [1.242, 1.535]}) print( ldf.select( pl.col(&quot;a&quot;).round(1) ).collect(engine=&quot;gpu&quot;) )

#### Custom GPU Engine

For finer control on the engine, you can pass a GPUEngine object with additional configurations like device details and verbosity to the engine=parameter:

    import polars as pl ldf = pl.LazyFrame({&quot;a&quot;: [1.242, 1.535]}) gpu\_engine = pl.GPUEngine( device=0, # This is the default raise\_on\_fail=True, # Fail loudly if can&#39;t execute on the GPU ) print( ldf.select( pl.col(&quot;a&quot;).round(1) ).collect(engine=gpu\_engine) )

#### Accelerate Polars Workflows Up to 13x

Top performing compute heavy queries with complex groupby and join operations  
(PDS-H benchmark | 80 GB dataset)

 ![A chart showing how cuDF accelerate Polars workflows up to 13x](https://developer.download.nvidia.com/images/cudf/cuda-diagram-july-data-science-webpages-chart-charts-polars2.png)

Query Number

#### Performance Improves as Data Size Grows

Query processing time across a range of dataset sizes

 ![A chart showing how cuDF improves Polars performance as data size grows](https://developer.download.nvidia.com/images/cudf/cuda-diagram-july-data-science-webpages-chart-charts-polars1.png)

Specs: [PDS-H benchmark](https://github.com/pola-rs/polars-benchmark) | GPU: NVIDIA H100 | CPU: Intel Xeon W9-3495X (Sapphire Rapids) | Storage: Local NVME  
Note: Note: PDS-H is derived from TPC-H but these results are not comparable to TPC-H results.

[Run the benchmark here.](https://github.com/pola-rs/polars-benchmark)

### Hands-On Tutorials: Accelerate Polars on Colab

The Polars GPU engine is preinstalled in Google Colab, making it incredibly easy to get started. Simply switch to a GPU runtime and enable the GPU engine to instantly accelerate your Polars workflows. Explore these hands-on resources:

#### Starter Kit: Process 100 Million Rows of Transaction Data in Seconds  

This kit demonstrates how the Polars GPU engine can process 100 million rows in under two seconds. Learn how, with it, you can tackle massive transaction datasets that typically cause slowdowns.

- 

Video: [Processing 100M Rows of Data in Under Two Seconds With the Polars GPU Engine](https://www.youtube.com/watch?v=AoKeit2Fbmw) (00:28)

- 

Notebook: [Intro to the Polars GPU Engine](https://colab.research.google.com/github/rapidsai-community/showcase/blob/main/accelerated_data_processing_examples/polars_gpu_engine_demo.ipynb?utm_source=nvidia+mktg&amp;utm_medium=web&amp;utm_campaign=polars+launch#scrollTo=TabS5fiHG0dG)

### How cuDF Accelerates Polars

Polars is already a highly performant DataFrame library, designed with multi-threaded execution, advanced memory optimizations, and lazy evaluation. These features allow Polars to efficiently handle medium- to large-scale data out of the box  
  
The Polars GPU engine takes these strengths further. By adding the speed of cuDF to the efficiency of Polars, you can achieve even faster execution, enabling the processing of hundreds of millions of rows in seconds.  
  
Built directly into the Polars Lazy API, the GPU engine works by attempting to execute operations on the GPU first and falling back to the CPU if necessary. This approach ensures you can continue to use familiar Polars syntax and functions while benefiting from enhanced GPU acceleration.  
  
For a deep dive into the architecture and underlying mechanisms of the Polars GPU Engine, check out the [official Polars blog post](https://pola.rs/posts/gpu-engine-release/).

* * *

## Apache Spark Accelerated With cuDF

This section details how cuDF leverages NVIDIA GPUs to seamlessly integrate and significantly enhance the performance and cost efficiency of your Apache Spark workloads.

Get Started

How It Works

Acceleration of Apache Spark extract, transform, load (ETL) and machine learning workloads is designed to be straightforward, whether you&#39;re deploying on premises or in the cloud.

### Launch Path

Follow our guide [here](https://docs.nvidia.com/spark-rapids/user-guide/latest/getting-started/overview.html). See below for a high-level overview:  
  
Launch Spark with the RAPIDS Accelerator for Apache Spark plug-in jar and enable a configuration setting:

    spark.conf.set(&#39;spark.rapids.sql.enabled&#39;,&#39;true&#39;)

The following is an example of a physical plan with operators running on the GPU:

    == Physical Plan == GpuColumnarToRow false +- GpuProject [cast(c\_customer\_sk#0 as string) AS c\_customer\_sk#40] +- GpuFileGpuScan parquet [c\_customer\_sk#0] Batched: true, DataFilters: [], Format: Parquet, Location: InMemoryFileIndex[file:/tmp/customer], PartitionFilters: [], PushedFilters: [], ReadSchema: struct\&lt;c\_customer\_sk:int\&gt;

#### Lightning Performance at a Fraction of the Cost

[NVIDIA Decision Support Benchmark](https://github.com/NVIDIA/spark-rapids-benchmarks/tree/dev/nds) 3 TB  
AWS EC2, Apache Spark 3.4.1, Spark RAPIDS release 24.04

 ![A chart showing how cuDF leverages NVIDIA GPUs to enhance performance of Apache Spark workloads](https://developer.download.nvidia.com/images/cudf/cuda-diagram-july-data-science-webpages-chart-charts-sparks1-r2.png) ![A chart showing how cuDF leverages NVIDIA GPUs to reduce costs of Apache Spark workloads](https://developer.download.nvidia.com/images/cudf/cuda-diagram-july-data-science-webpages-chart-charts-sparks2.png)

Cluster of 8x nodes in each setup:  
CPU - r6id.8xlarge - 32 vCPU, 256GB, 1x1900 NVMe SSD, 12.5 Gb/s network  
GPU - g6.8xlarge - 32vCPU, 1 L4 GPU, 128GB, NVMe SSD, 25 Gb/s network  
\* included NVAIE at $1/GPU/hr

[Run the benchmark here.](https://github.com/NVIDIA/spark-rapids-benchmarks/tree/dev/nds)

### Getting Started With cuDF Acceleration of Apache Spark

Learn how you can significantly accelerate enterprise-level data workloads, leading to substantial cost savings.

#### Scale Data Analytics With Apache Spark

Learn how GPUs accelerate enterprise-scale Apache Spark workflows to drive cost savings.

- 

On-Demand GTC Session:: [Accelerate Big Data Analytics on GPUs With the RAPIDS Accelerator for Apache Spark](https://www.nvidia.com/en-us/on-demand/session/gtc25-dlit71528/) (01:27:34)

- 

Blog: [Predicting Performance on Apache Spark With GPUs](https://developer.nvidia.com/blog/predicting-performance-on-apache-spark-with-gpus/)

- 

User Guide: [RAPIDS Accelerator for Apache Spark](https://docs.nvidia.com/spark-rapids/user-guide/latest/index.html)

#### How cuDF Accelerates Apache Spark

NVIDIA cuDF enhances your Apache Spark workflows by integrating as a Spark plug-in. Once installed and configured, it automatically detects available GPUs and leverages them for supported operations.  
  
It works by replacing the backend for Spark SQL and DataFrame operations with GPU-accelerated versions. If an operation isn’t supported on GPUs, the accelerator falls back to the standard Spark CPU implementation. This plug-in-based approach makes it easy to integrate with major Spark platforms, including AWS EMR, GCP Dataproc, OCI, and Databricks.  
  
For a deeper-dive explanation of the underlying architecture, supported operations, and integration, refer to the [user guide](https://docs.nvidia.com/spark-rapids/index.html).

![A flowchart of how cuDF accelerates Apache Spark](https://developer.download.nvidia.com/images/cudf/cuda-diagram-data-science-flow.png)

* * *

## Data Science Training From NVIDIA

 ![Data Science Learning Path From the NVIDIA DLI](https://developer.download.nvidia.com/icons/m48-map-search-256px-blk.png)
### Data Science Learning Path From the NVIDIA Deep Learning Institute

 ![Self-Paced Course: Accelerate Data Science Workflows With Zero Code Changes](https://developer.download.nvidia.com/icons/m48-deep-learning-institute-usd.svg)
### Self-Paced Course: Accelerate Data Science Workflows With Zero Code Changes

 ![Get Certified in Accelerated Data Science](https://developer.download.nvidia.com/icons/m48-certification-ribbon-2.svg)
### Get Certified in Accelerated Data Science

## Join the Community

 ![Join NVIDIA CUDA-X Data Science Libraries Slack Community](https://developer.download.nvidia.com/icons/m48-people-group.svg)
### Join the Accelerated Data Science Community on Slack

 ![Sign Up for NVIDIA Data Science Newsletter](https://developer.download.nvidia.com/icons/m48-email-settings.svg)
### Sign Up for the Data Science Newsletter

* * *

## Ethical AI 

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their supporting team to ensure their application meets requirements for the relevant industry and use case and addresses unforeseen product misuse.   
  
Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Get started with NVIDIA cuDF today.

[Documentation](https://docs.rapids.ai/api/cudf/stable/)


