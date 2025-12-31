# Source: https://developer.nvidia.com/topics/ai/data-science/cuda-x-data-science-libraries/cuml.md

1. [AI](/topics/ai)

[Data Science](/topics/ai/data-science)
2. [CUDA-X Data Science Libraries](/topics/ai/data-science/cuda-x-data-science-libraries)

cuML

# NVIDIA cuML: GPU-Accelerated Machine Learning

NVIDIA cuML is an open-source CUDA-X™ Data Science library that accelerates scikit-learn, UMAP, and HDBSCAN on GPUs—supercharging machine learning workflows with no code changes required.

[Demo Notebook](https://colab.research.google.com/github/rapidsai-community/showcase/blob/main/getting_started_tutorials/cuml_sklearn_colab_demo.ipynb)[Documentation](https://docs.rapids.ai/api/cuml/stable/zero-code-change/)

* * *

## Key Features

### Maximizes Performance on NVIDIA GPUs

cuML optimizes fundamental machine learning operations for execution on GPUs. This significantly speeds up model development and training times with quicker testing and parameter-tuning iterations.

### Zero-Code-Change Acceleration

cuML includes an API (cuml.accel) that can run your existing scikit-learn, UMAP, or HDBSCAN code on GPUs with no code modifications.

### CPU Fallback

cuML’s zero-code-change API (cuml.accel) ensures your scikit-learn, UMAP, and HDBSCAN code won’t fail to execute by automatically pushing code to the GPU or CPU based on coverage. Read more in [How It Works](#howitworks).

### Flexibility

cuML includes two interfaces: a zero-code-change API for popular machine learning algorithms and a Python GPU-only machine learning library similar to scikit-learn with comprehensive coverage. [Learn more in the docs](https://docs.rapids.ai/api/cuml/stable/zero-code-change/#faqs).

### Scalability

cuML efficiently utilizes single-GPU systems to process large datasets that overwhelm CPU-based implementations of core machine learning libraries. 

### Distributed Computing

cuML accelerates distributed machine learning applications at scale, with real-world examples of up to 6 TB datasets on multi-node-multi-GPU clusters via the popular Apache Spark MLlib API.

* * *

## Turn cuML On to Accelerate scikit-learn by 50x 

https://www.youtube-nocookie.com/embed/cIJsVq8CPys?&amp;loop=1&amp;playlist=cIJsVq8CPys
 

NVIDIA cuML runs popular machine learning algorithms like scikit-learn Random Forest, UMAP, and HDBSCAN on GPUs with zero code changes.

* * *

## Test Drive cuML

### Intro Blog: cuML Accelerator  

NVIDIA cuML brings zero-code-change GPU acceleration with massive speedups to scikit-learn, UMAP, and HDBSCAN. 

[Read the Blog](https://developer.nvidia.com/blog/nvidia-cuml-brings-zero-code-change-acceleration-to-scikit-learn/)

### Colab Quickstart: Hands-On cuML Tutorial  

cuML comes preinstalled in Google Colab, making it incredibly easy to get started. Simply switch to a GPU runtime and use this notebook to try cuml.accel for scikit-learn, UMAP, and HDBSCAN.

[Launch on Colab](https://colab.research.google.com/github/rapidsai-community/showcase/blob/main/getting_started_tutorials/cuml_sklearn_colab_demo.ipynb)

* * *

## Install cuML

To get started, install cuML using the code snippets below.

### Quick Install With conda

1. If not installed, download and run the install script. This will install the latest miniforge:

    wget &quot;https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh&quot; bash Miniforge3-$(uname)-$(uname -m).sh

2. Then install with:

    conda create -n rapids-25.12 -c rapidsai -c conda-forge \ cuml=25.12 python=3.13 cuda-version=13.0

### Quick Install With pip

    Install via the NVIDIA PyPI index: pip install \ cudf-cu13==25.12.\* \ cuml-cu13==25.12\* \

See the complete install selector for docker, WSL2, and individual libraries.

[Install Selector  
](https://docs.rapids.ai/install?_gl=1*kwbd1w*_ga*MTE4NDAwMTQ1NS4xNzA5NzcwODcw*_ga_RKXFW6CM42*czE3NTIxODk0OTQkbzk1JGcwJHQxNzUyMTg5NDk0JGo2MCRsMCRoMA.. &quot;Download Workflows&quot;)

* * *

## Enable cuML Acceleration of scikit-learn, UMAP, and HDBSCAN With Zero Code Changes

Once cuML is installed, you can access and enable the cuml.accel module to accelerate scikit-learn, UMAP, and HDBSCAN workflows with no code changes. Note that not all cuML estimators are supported in cuml.accel (open beta) today. Read about the [known limitations](https://docs.rapids.ai/api/cuml/stable/zero-code-change-limitations/) to understand what is and what is not covered.  
  
To use cuml.accel, enable it using one of these methods before importing scikit-learn, UMAP, or HDBSCAN:

#### To accelerate IPython or Jupyter notebooks, use the magic command:

    %load\_ext cuml.accel import sklearn ...

### To accelerate a Python script, use the Python module flag on the command line:

    python -m cuml.accel script.py

### If you can&#39;t use command-line flags, explicitly enable cudf.pandas via import:

    import cuml.accel cuml.accel.install() import sklearn ...

#### 50x Faster scikit-learn

Speedup of average training performance for traditional machine learning algorithms running on cuml.accel and scikit-learn code on GPU vs scikit-learn on CPU.

Specs: NVIDIA cuML 25.02 on NVIDIA H100 80GB HBM3, scikit-learn v1.5.2 on Intel Xeon Platinum 8480CL

#### 60x Faster UMAP, 175x Faster HDBSCAN

Speedup of average training performance for traditional machine learning algorithms running on cuml.accel and UMAP/HDBSCAN code on GPU vs UMAP/HDBSCAN on CPU.

Specs: NVIDIA cuML 25.02 on NVIDIA H100 80GB HBM3, umap-learn  v0.5.7, hdbscan v0.8.40  on Intel Xeon Platinum 8480CL

[Run this benchmark.](https://github.com/rapidsai/cuml/tree/branch-25.06/python/cuml/cuml/benchmark)

* * *

## Hands-On Tutorials: Accelerate scikit-learn, UMAP, and HDBSCAN

Dive into these resources to accelerate your machine learning workflows with cuML, including hands-on examples of advanced ML techniques, specialized applications, and deployment optimizations.

#### Starter Kit: Accelerate Portfolio Optimization

This kit demonstrates an end-to-end machine learning and optimization workflow in portfolio use cases.   
It leverages CUDA-X libraries such as cuML for KDE fitting and sampling yields for significant acceleration on GPU compared to CPU, especially as dataset sizes and the scenarios to sample increase.

- 

Blog: [Accelerating Real-Time Financial Decisions with Quantitative Portfolio Optimization](https://developer.nvidia.com/blog/accelerating-real-time-financial-decisions-with-quantitative-portfolio-optimization/)l

- 

Notebook: [Quantitative Portfolio Optimization Developer Example](https://github.com/NVIDIA-AI-Blueprints/quantitative-portfolio-optimization)

#### Starter Kit: Accelerate Single-Cell Genomics 

This kit demonstrates techniques to measure and analyze single-cell data at scale, accelerating analysis cycles and saving significant time by leveraging GPUs for genomics workflows.

- 
[Blog: Driving Toward Billion-Cell Analysis and Biological Breakthroughs With RAPIDS-singlecell](https://developer.nvidia.com/blog/driving-toward-billion-cell-analysis-and-biological-breakthroughs-with-rapids-singlecell/)
- 
[Blueprint: Single-Cell Analysis With RAPIDS-singlecell, Powered by CUDA-X Data Science](https://build.nvidia.com/nvidia/single-cell-analysis)

#### Starter Kit: Accelerate Topic Modeling

This kit demonstrates how to significantly improve performance for topic modeling by minimizing noise clusters and leveraging a rewards-guided, GPU-accelerated method with BERTopic and cuml.accel.

- 
[Video: Minimizing Noise Cluster for Topic Modeling (13:47)](https://www.youtube.com/watch?v=8TBaLWvJBuE&amp;t=12s)
- 
[Notebook: Minimizing Noise Cluster for Topic Modeling](https://github.com/rapidsai-community/showcase/blob/main/blogs_notebooks/video_notebook_for_Minimizing_Noise_Cluster_for_Topic_Modeling.ipynb)
- 
[Blog: Deep dive into UMAP, the technique behind accelerated topic modeling](https://developer.nvidia.com/blog/even-faster-and-more-scalable-umap-on-the-gpu-with-rapids-cuml/)

#### Accelerate Time-Series Forecasting 

This blog demonstrates how cuML accelerates time-series forecasting, enabling you to work with larger datasets and forecast windows using skforecast for faster iteration.

- 
[Blog: Accelerating Time-Series Forecasting With RAPIDS cuML](https://developer.nvidia.com/blog/accelerating-time-series-forecasting-with-rapids-cuml/)

#### Starter Kit: Stacking Using cuML

This kit shows how to achieve high-performance stacking by using the speed of GPUs to efficiently train and combine numerous diverse models, maximizing accuracy in complex tabular data challenges.

- 
[Blog: Winning First Place in a Kaggle Competitions With Stacking Using cuML](https://developer.nvidia.com/blog/grandmaster-pro-tip-winning-first-place-in-a-kaggle-competition-with-stacking-using-cuml/)
- 
[Blog: Stacking Generalization With HPO: Maximize Accuracy in 15 Minutes With cuML](https://developer.nvidia.com/blog/stacking-generalization-with-hpo-maximize-accuracy-in-15-minutes-with-nvidia-cuml/)

#### Supercharge Tree Model Inference With FIL

This blog highlights how Forest Inference Library (FIL) delivers blazing-fast inference for tree models within cuML. Explore new capabilities, performance gains, and features to optimize your model deployment.

- 
[Blog: Supercharge Tree-Based Model Inference with Forest Inference Library in NVIDIA cuML](https://developer.nvidia.com/blog/supercharge-tree-based-model-inference-with-forest-inference-library-in-nvidia-cuml/)

* * *

## How cuML Accelerates scikit-learn, UMAP, and HDBSCAN

cuML introduced zero-code-change acceleration in open beta with the cuml.accel module. When you load this module, importing scikit-learn, umap-learn, or hdbscan allows cuML to &quot;intercept&quot; estimators from these CPU modules. This makes all scikit-learn estimators a proxy to either a GPU or a CPU estimator at any given time.   
  
When you use an estimator, your code will use cuML’s GPU-accelerated implementation under the hood if it can. If it can’t, it will fall back to standard CPU scikit-learn. This works in reverse as well. If you’ve already trained a model on the GPU and a particular method isn’t supported, cuML will reconstruct the trained model on the CPU and use the scikit-learn version.  
  
Read more about the rapidly growing [list of algorithms and parameters](https://docs.rapids.ai/api/cuml/stable/zero-code-change-limitations/) that the zero-code-change interface covers.  
  
cuML also provides an API that mirrors scikit-learn, supports a much wider set of algorithms, and is suitable for users looking to maximize performance for their bespoke applications. Read about it in [cuML&#39;s documentation](https://docs.rapids.ai/api/cuml/stable/).

* * *

## Data Science Training From NVIDIA

 ![Data Science Learning Path From the NVIDIA DLI](https://developer.download.nvidia.com/icons/m48-certification-ribbon-1-256px-blk.png)
### Data Science Learning Path From the NVIDIA Deep Learning Institute

 ![Self-Paced Course: Accelerate Data Science Workflows With Zero Code Changes](https://developer.download.nvidia.com/icons/m48-deep-learning-institute-usd.svg)
### Self-Paced Course: Accelerate Data Science Workflows With Zero Code Changes

 ![Get Certified in Accelerated Data Science](https://developer.download.nvidia.com/icons/m48-certification-ribbon-2.svg)
### Get Certified in Accelerated Data Science

* * *

## Join the Community

 ![Join NVIDIA CUDA-X Data Science Libraries Slack Community](https://developer.download.nvidia.com/icons/m48-people-group.svg)
### Join the CUDA-X Data Science Libraries Slack Community

 ![Sign Up for NVIDIA Data Science Newsletter](https://developer.download.nvidia.com/icons/m48-email-settings.svg)
### Sign Up for the Data Science Newsletter

* * *

## Ethical AI 

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their supporting team to ensure their application meets requirements for the relevant industry and use case and addresses unforeseen product misuse.   
  
  
Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

### Get Started with NVIDIA cuML today.

[Documentation](https://docs.rapids.ai/api/cuml/stable/zero-code-change/)


