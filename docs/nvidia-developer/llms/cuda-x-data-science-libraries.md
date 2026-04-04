# Source: https://developer.nvidia.com/topics/ai/data-science/cuda-x-data-science-libraries.md

1. [Topics](https://developer.nvidia.com/topics/)

[AI](https://developer.nvidia.com/topics/ai)
2. [Data Science](/topics/ai/data-science)

CUDA-X Data Science Libraries

# CUDA-X Data Science

CUDA-X™ Data Science is a collection of open-source libraries that accelerate popular data science libraries and platforms. It is part of the CUDA-X collection of highly optimized, domain-specific libraries built on CUDA®.  
  
CUDA-X Data Science includes zero code change APIs to accelerate popular PyData tools like pandas, scikit-learn, as well as distributed computing frameworks like Apache Spark. With 100+ integrations with open-source libraries and tools in the data science and data processing ecosystem, CUDA-X Data Science democratizes access to accelerated data science.

[Download Now](https://docs.rapids.ai/install?_gl=1*kwbd1w*_ga*MTE4NDAwMTQ1NS4xNzA5NzcwODcw*_ga_RKXFW6CM42*czE3NTIxODk0OTQkbzk1JGcwJHQxNzUyMTg5NDk0JGo2MCRsMCRoMA)[Documentation](https://docs.rapids.ai/)

 ![NVIDIA CUDA-X Data Science open-source libraries](https://developer.download.nvidia.com/images/cuda-x/cuda-diagram-data-science-and-ai-application-stack.png)
* * *

## CUDA-X Data Science Libraries 

Accelerate data analytics, machine learning, graphs as well as data intensive applications such as vector search to get the highest performance possible on single GPUs or scale up to distributed systems using simple zero code change interfaces.

### cuDF: 50x Faster pandas

cuDF is a GPU-accelerated library that optimizes fundamental DataFrame operations. It includes drop-in accelerators for popular DataFrame tools like pandas, Polars, and Apache Spark with no code changes required.

[Learn More About cuDF](/cudf)

[Run the Benchmark](https://github.com/rapidsai/cudf/blob/branch-25.06/docs/cudf/source/user_guide/performance-comparisons/performance-comparisons.ipynb)

[View Docs](https://docs.rapids.ai/api/cudf/stable/)

[Install Now](https://docs.rapids.ai/install?_gl=1*kwbd1w*_ga*MTE4NDAwMTQ1NS4xNzA5NzcwODcw*_ga_RKXFW6CM42*czE3NTIxODk0OTQkbzk1JGcwJHQxNzUyMTg5NDk0JGo2MCRsMCRoMA..)

**TAGS: pandas, dataframe, Python,Cc++**

### cuML: 50x Faster scikit-learn

cuML is a GPU-accelerated machine learning library that optimizes machine learning algorithms for execution on GPUs. It includes accelerators that run machine learning algorithms in scikit-learn, UMAP, and HDBSCAN with no code changes required. 

[Learn More About cuML](/cuml)

[Run the Benchmark](https://github.com/rapidsai/cuml/tree/branch-25.06/python/cuml/cuml/benchmark)

[View Docs](https://docs.rapids.ai/api/cuml/stable/)

[Install Now](https://docs.rapids.ai/install?_gl=1*kwbd1w*_ga*MTE4NDAwMTQ1NS4xNzA5NzcwODcw*_ga_RKXFW6CM42*czE3NTIxODk0OTQkbzk1JGcwJHQxNzUyMTg5NDk0JGo2MCRsMCRoMA..)

**TAGS: scikit-learn, machine learning, Python, C++**

### cuGraph: 48x Faster NetworkX

cuGraph is a GPU-accelerated graph analytics library that optimizes graph algorithms for execution on GPUs to process millions of nodes without specialized software. It includes a zero-code-change accelerator for NetworkX. 

[Run the Benchmark](https://github.com/rapidsai/nx-cugraph/blob/branch-25.06/benchmarks/pytest-based)

[View Docs](https://docs.rapids.ai/api/cugraph/stable/)

[Install Now](https://docs.rapids.ai/install?_gl=1*kwbd1w*_ga*MTE4NDAwMTQ1NS4xNzA5NzcwODcw*_ga_RKXFW6CM42*czE3NTIxODk0OTQkbzk1JGcwJHQxNzUyMTg5NDk0JGo2MCRsMCRoMA..)

**TAGS: NetworkX, graph, Python, C++**

### Apache Spark Accelerated with cuDF

Learn more about our accelerator plug-in for Apache Spark workflows.

[Learn More About GPU-Accelerated Spark](https://www.nvidia.com/en-us/deep-learning-ai/solutions/data-science/apache-spark-3/)

**TAGS: machine learning, data processing, distributed computing, Scala, Python**

### Dask-RAPIDS

Scale out GPU-accelerated data science pipelines to multiple nodes on Dask.

[Get Started on GitHub](https://github.com/rapidsai/cudf/tree/main/python/dask_cudf)

**Tags: distributed computing, Python**

### cuxfilter

Create interactive data visuals with multidimensional filtering of over 100-million-row tabular datasets.

[Get Started With cuxfilter](https://docs.rapids.ai/api/cuxfilter/stable/)

**Tags: dashboards, visualization, Python**

### cuCIM

Mirror scikit-image for image manipulation and OpenSlide for image loading with the cuCIM API.

[Get Started With cuCIM](https://docs.rapids.ai/api/cucim/stable/?_gl=1*w4ryfi*_ga*MTE4NDAwMTQ1NS4xNzA5NzcwODcw*_ga_RKXFW6CM42*czE3NTIxODUyMjUkbzk0JGcwJHQxNzUyMTg1MjI1JGo2MCRsMCRoMA..)

**Tags: computer vision, vision processing, Python**

### cuVS

Apply cuVS algorithms to accelerate vector search, including world-class performance from CAGRA.

[Get Started With cuVS](/cuvs)

**TAGS: vector search, Python, C++, c, rust**

### RAFT

Use RAFT’s CUDA-accelerated primitives to rapidly compose analytics.

[Get Started With RAFT](https://docs.rapids.ai/api/raft/stable?_gl=1*1jr70u0*_ga*MTE4NDAwMTQ1NS4xNzA5NzcwODcw*_ga_RKXFW6CM42*czE3NTIxODUyMjUkbzk0JGcwJHQxNzUyMTg1MjI1JGo2MCRsMCRoMA..)

**Tags: primitives, algorithms, CUDA, Python, C++**

### KvikIO  

Take full advantage of NVIDIA® GPUDirect® Storage (GDS) through powerful bindings to cuFile.

[Get Started With KviKIO](https://docs.rapids.ai/api/kvikio/stable?_gl=1*w4ryfi*_ga*MTE4NDAwMTQ1NS4xNzA5NzcwODcw*_ga_RKXFW6CM42*czE3NTIxODUyMjUkbzk0JGcwJHQxNzUyMTg1MjI1JGo2MCRsMCRoMA..)

**Tags: FILEIO, GPUDirectStorage, Python, C++**

### Other CUDA-X Data Science and Processing Libraries  

See a complete list of libraries and tools.

[Check out GitHub](https://github.com/rapidsai)

* * *

## Get Started

Hands-On Tutorials

Training

### Starter Kit: Accelerated Data Analytics With pandas Code  

This kit demonstrates how to create responsive dashboards on large-scale data using pandas code and PyViz libraries, leveraging cuDF for accelerated exploratory data analytics with zero code changes.

- 

Video: [Accelerated Exploratory Data Analysis With pandas on NVIDIA GPUs](https://www.youtube.com/watch?v=PJpCJsqcfOk) (16:06)

- 

Notebook: [Build an Interactive Dashboard Notebook](https://colab.research.google.com/gist/will-hill/aa24c3ffe1428c005af3793fcacf9bd2/cudf_pandas_opencellid_demo.ipynb)

### Starter Kit: Accelerated Machine Learning on XGBoost  

XGBoost is the most popular Python library for gradient boosted decision trees. It supercharges machine learning models for classification, regression and ranking workflows.

- 

Video: 

# [Accelerated Machine Learning with XGBoost on NVIDIA GPUs](https://www.youtube.com/watch?v=lhraJRaDkOA) (20:10)

- 

Notebook: [Get Started With Accelerating XGBoost Workflows on GPUs](https://colab.research.google.com/gist/will-hill/2edd85e351e62e52fccd43da9b027434/xgboost_rapids_taxi.ipynb)

### Starter kit: Accelerated Machine Learning With cuML Code

cuML accelerates popular machine learning algorithms, including Random Forest, UMAP, and HDBSCAN

- 

Video: [cuML Accelerates Machine Learning by 50x With Zero Code Change](https://www.youtube.com/watch?v=cIJsVq8CPys)(00:55)

- 

Blog: [NVIDIA cuML Brings Zero-Code-Change Acceleration to scikit-learn](https://developer.nvidia.com/blog/nvidia-cuml-brings-zero-code-change-acceleration-to-scikit-learn/)

- 

Notebook: [Get Started With Accelerating Popular Machine Learning Libraries](https://colab.research.google.com/github/rapidsai-community/showcase/blob/main/getting_started_tutorials/cuml_sklearn_colab_demo.ipynb)

#### Starter Kit: Accelerated Data Analytics With Apache Spark

The NVIDIA RAPIDS™ accelerator for Apache Spark accelerates enterprise-level data workloads to drive cost savings.

- 

Video: [Accelerate Data Analytics on GPUa With the RAPIDS Accelerator for Apache Spark](https://www.nvidia.com/en-us/on-demand/session/gtc25-dlit71528/) (1:27:34)

- 

Blog: [Predicting Performance on Apache Spark with GPUs](https://developer.nvidia.com/blog/predicting-performance-on-apache-spark-with-gpus/)

- 

User [Guide: RAPIDS Accelerator for Apache Spark User Guide](https://docs.nvidia.com/spark-rapids/user-guide/latest/index.html)

#### Starter Kit: Accelerated Data Analytics With Polars Code  

Polars is known for its high performance and memory optimizations. Experience even faster execution when you call the GPU engine powered by cuDF.

- 

Video: [Processing 100 Million Rows of Data in Under 2 Seconds With Polars](https://www.youtube.com/watch?v=AoKeit2Fbmw) (00:28)

- 

Blog: [Get Started with Accelerating Polars](https://developer.nvidia.com/blog/polars-gpu-engine-powered-by-rapids-cudf-now-available-in-open-beta/)

- 

Notebook: [Accelerate Polars Data Processing Workflows Notebook](https://colab.research.google.com/github/CUDA-X Data Science Librariesai-community/showcase/blob/main/accelerated_data_processing_examples/polars_gpu_engine_demo.ipynb?utm_source=nvidia+mktg&amp;utm_medium=web&amp;utm_campaign=polars+launch)

#### Starter Kit: Accelerated Graph Analytics With NetworkX Code  

NetworkX accelerates popular graph algorithms, including Louvain, Betweeness Centrality, and PageRank.

- 

Video: [Achieve up to 500x Faster NetworkX With Zero Code Changes Using NVIDIA cuGraph](https://www.youtube.com/watch?v=3EsbU1gcH5c) (00:42)

- 

Blog: [NetworkX Introduces Zero-Code-Change Acceleration Using NVIDIA cuGraph](https://developer.nvidia.com/blog/networkx-introduces-zero-code-change-acceleration-using-nvidia-cugraph/)

- 

Notebook: [Accelerated Graph Analytics Notebook](https://colab.research.google.com/github/rapidsai-community/showcase/blob/main/getting_started_tutorials/accelerated_networkx_demo.ipynb?ncid=so-othe-145635-vt27)

### Data Science Learning Path

Get an overview of everything DLI offers for upskilling in accelerated data science.

[Learn More](https://www.nvidia.com/en-us/learn/learning-path/accelerated-data-science/)

### Accelerated Data Science Workflows With Zero Code Change

Take our free self-paced course to learn how to transform your workflow with zero-code-change acceleration.

[Learn More](https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+T-DS-03+V1)

### Get Certified in Accelerated Data Science

Gain a deeper understanding of accelerated data science in our certification course.

[Learn More](https://www.nvidia.com/en-us/learn/certification/accelerated-data-science-professional/)

 

* * *

## Install and Deploy in Your Environment

Quick Install

Deployment Guides

### Quick Install With conda

1. If not installed, download and run the install script. This will install the latest miniforge:

    wget &quot;https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh&quot; bash Miniforge3-$(uname)-$(uname -m).sh

2. Then install with:

    conda create -n rapids-25.12 -c rapidsai -c conda-forge rapids=25.12 python=3.13 cuda-version=13.0

### Quick Install With pip

    Install via the NVIDIA PyPI index: pip install \ --extra-index-url=https://pypi.nvidia.com \ cudf-cu13==25.12.\* \ dask-cudf-cu13==25.12\* \ cuml-cu13==25.12.\* \ cugraph-cu13==25.12.\*

### Deploy Locally

Use this guide to install and build with conda, pip, Docker, or WSL2 on your local machine.

[Read the Local Deployment Guide](https://docs.rapids.ai/deployment/stable/local/)

### Deploy on Platforms  

Deploy CUDA-X Data Science libraries on your platform of choice, including Kubernetes, Databricks, and Google Colab. 

[Read the Platforms Guide](https://docs.rapids.ai/deployment/stable/platforms/)

### Deploy in the Cloud

Run CUDA-X Data Science libraries in AWS, Azure, GCP, and more.

[Read the Cloud Deployment Guide](https://docs.rapids.ai/deployment/stable/cloud/)

* * *

## The Accelerated Data Science Ecosystem

Data practitioners in open-source libraries, commercial software, and industries are driving innovation with CUDA-X Data Science.

Open-Source Libraries

Platforms

Industry Adoption

 ![Data Science Open-Source Library - Apache Arrow](https://developer.download.nvidia.com/images/logos/apache-arrow-logo.svg)

 ![Data Science Open-Source Library - Apache Spark](https://developer.download.nvidia.com/images/logos/apache-spark-logo.svg)

 ![Data Science Open-Source Library - CuPy](https://developer.download.nvidia.com/images/logos/cupy-logo.svg)

 ![Data Science Open-Source Library - Dask](https://developer.download.nvidia.com/images/logos/dask-logo.svg)

 ![Data Science Open-Source Library - Dmlc XGBoost](https://developer.download.nvidia.com/images/logos/dmlc-xgboost-logo.svg)

 ![Data Science Open-Source Library - HoloViz](https://developer.download.nvidia.com/images/logos/holoviz-logo.svg)

 ![Data Science Open-Source Library - NetworkX](https://developer.download.nvidia.com/images/logos/networkx-logo.svg)

 ![Data Science Open-Source Library - Numba](https://developer.download.nvidia.com/images/logos/numba-logo.svg)

 ![Data Science Open-Source Library - Polars](https://developer.download.nvidia.com/images/logos/polars-logo.svg)

 ![Data Science Open-Source Library - PyG](https://developer.download.nvidia.com/images/logos/pyg-logo.svg)

 ![Data Science Open-Source Library - PyTorch](https://developer.download.nvidia.com/images/logos/pytorch-logo.svg)

 ![Data Science Open-Source Library - Scikit Learn](https://developer.download.nvidia.com/images/logos/scikit-learn-logo.svg)

 ![Data Science Open-Source Library - scverse](https://developer.download.nvidia.com/images/logos/scverse-logo.svg)

 ![Data Science Platform - Amazon SageMaker](https://developer.download.nvidia.com/images/logos/amazon-sagemaker-logo.svg)

 ![Data Science Platform - Anaconda](https://developer.download.nvidia.com/images/logos/anaconda-logo.svg)

 ![Data Science Platform - Azure Machine Learning](https://developer.download.nvidia.com/images/logos/azure-machine-learning-logo.svg)

 ![Data Science Platform - Cloudera](https://developer.download.nvidia.com/images/logos/cloudera-logo.svg)

 ![Data Science Platform - Databricks](https://developer.download.nvidia.com/images/logos/databricks-logo.svg)

 ![Data Science Platform - Google Cloud Dataproc](https://developer.download.nvidia.com/images/logos/dataproc-logo.svg)

 ![Data Science Platform - Determined AI](https://developer.download.nvidia.com/images/logos/determined-ai-logo.svg)

 ![Data Science Platform - Domino](https://developer.download.nvidia.com/images/logos/domino-logo.svg)

 ![Data Science Platform - Google Colab](https://developer.download.nvidia.com/images/logos/google-colab-logo.svg)

 ![Data Science Platform - Iguazio](https://developer.download.nvidia.com/images/logos/iguazio-logo.svg)

 ![Data Science Platform - Snowflake](https://developer.download.nvidia.com/images/logos/snowflake-logo.svg)

 ![Data Science Industry Adoption - AT&amp;T](https://developer.download.nvidia.com/images/logos/att-logo.svg)

AT&amp;T applied the RAPIDS Accelerator for Apache Spark on GPU clusters in their data-to-AI pipeline.

[Read Blog](https://developer.nvidia.com/blog/scaling-data-pipelines-att-optimizes-speed-cost-and-efficiency-with-gpus/)

 ![Data Science Industry Adoption - bunq](https://developer.download.nvidia.com/images/logos/bunq-logo.svg)

bunq improved fraud detection accuracy by accelerating model training 100x and data processing 5x using NVIDIA CUDA-X libraries.

[Read Blog](https://blogs.nvidia.com/blog/europe-financial-services-ai/)

 ![Data Science Industry Adoption - CapitalOne](https://developer.download.nvidia.com/images/logos/capital-one-logo.svg)

Capital One accelerated their financial and credit analysis pipelines, improving model training by 100x.

[Watch On-Demand Session](https://www.nvidia.com/en-us/on-demand/session/gtcsj20-s22136/)

 ![Data Science Industry Adoption - Checkout.com](https://developer.download.nvidia.com/images/logos/checkout-logo.svg)

Checkout.com accelerated their data analysis workflows from minutes to seconds with NVIDIA cuDF.

[Read Blog](https://blogs.nvidia.com/blog/europe-financial-services-ai/)

 ![Data Science Industry Adoption - Cloudera](https://developer.download.nvidia.com/images/logos/cloudera-logo.svg)

The IRS team uncovered fraud with the RAPIDS Accelerator for Apache Spark on the Cloudera Data Platform.

[Read Blog](https://blogs.nvidia.com/blog/2021/09/07/cloudera-spark-irs-gpus/)

 ![Data Science Industry Adoption - Linkedin](https://developer.download.nvidia.com/images/logos/linkedin-logo.svg)

LinkedIn developed DARWIN to enable faster data analysis on NVIDIA cuDF.

[Watch On-Demand Session](https://www.nvidia.com/en-us/on-demand/session/gtcspring23-s51399/)

 ![Data Science Industry Adoption - NASA](https://developer.download.nvidia.com/images/logos/nasa-logo.svg)

NASA used CUDA-X Data Science to detect and quantify air pollution anomalies and build a bias-correction model.

[Read Blog: Part 1](https://developer.nvidia.com/blog/nasa-and-nvidia-collaborate-to-accelerate-scientific-data-science-use-cases-part-1/)[Read Blog: Part 2](https://developer.nvidia.com/blog/nasa-and-nvidia-collaborate-to-accelerate-scientific-data-science-use-cases-part-2/)

 ![Data Science Industry Adoption - PayPal](https://developer.download.nvidia.com/images/logos/paypal-logo.svg)

PayPal reduced cloud costs by up to 70% with the RAPIDS Accelerator for Apache Spark.

[Watch On-Demand Session](https://www.nvidia.com/en-us/on-demand/session/gtc24-s62506/)

 ![Data Science Industry Adoption - Taboola](https://developer.download.nvidia.com/images/logos/taboola-logo.svg)

Taboola, an advertising platform, processes terabytes of hourly data with the RAPIDS Accelerator for Apache Spark.

[Watch On-Demand Session](https://www.nvidia.com/en-us/on-demand/session/gtc24-s62130/)

 ![Data Science Industry Adoption - Tgen](https://developer.download.nvidia.com/images/logos/tgen-logo.svg)

TGen cut analysis time on 4 million-cell datasets from 10 hours to three minutes with RAPIDS-singlecell, built on CUDA-X Data Science.

[Read Customer Story](https://www.nvidia.com/en-us/customer-stories/reduce-single-cell-spatial-analysis-from-hours-to-minutes/)

 ![Data Science Industry Adoption - TCS](https://developer.download.nvidia.com/images/logos/tcs-logo.svg)

TCS Optumera accelerated their demand forecasting pipeline with the RAPIDS Accelerator for Apache Spark.

[Watch On-Demand Session](https://www.nvidia.com/en-us/on-demand/session/gtcspring22-s42508/)

 ![Data Science Industry Adoption - Uber](https://developer.download.nvidia.com/images/logos/uber-logo.svg)

Uber developed Horovod with support for Spark 3.x with GPU scheduling.

[Watch On-Demand Session](https://www.nvidia.com/en-us/on-demand/session/gtcsj20-s21300/)

 ![Data Science Industry Adoption - Walmart](https://developer.download.nvidia.com/images/logos/walmart-logo.svg)

Walmart solved scalability issues with their product-substitution algorithm.

[Watch On-Demand Session](https://www.nvidia.com/en-us/on-demand/session/gtcspring22-s42259/)

* * *

## Join the Community

 ![](https://developer.download.nvidia.com/icons/m48-people-group.svg)
### Join the Accelerated Data Science Community on Slack

 ![](https://developer.download.nvidia.com/icons/m48-email-settings.svg)
### Sign Up for the Data Science Newsletter

* * *

## Ethical AI 

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their supporting team to ensure their application meets requirements for the relevant industry and use case and addresses unforeseen product misuse.   
  
Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

### Download CUDA-X Data Science libraries today.  

[Download](https://docs.rapids.ai/install/?_gl=1*kwbd1w*_ga*MTE4NDAwMTQ1NS4xNzA5NzcwODcw*_ga_RKXFW6CM42*czE3NTIxODk0OTQkbzk1JGcwJHQxNzUyMTg5NDk0JGo2MCRsMCRoMA)


