# Source: https://docs.anyscale.com/get-started/what-is-ray.md

# What is Ray?

[View Markdown](/get-started/what-is-ray.md)

# What is Ray?

Ray is an open source framework for building, deploying, and serving AI and ML applications using distributed compute resources.

Ray excels when applications need to scale to many machines and optimizes resource utilization for workloads that require both CPUs and GPUs.

Anyscale, founded by the original creators of Ray, provides a unified platform that simplifies the deployment, scaling, and management of Ray workloads in production environments.

Anyscale provides an optimized version of Ray known as the Anyscale Runtime. See [What is the Anyscale Runtime?](/runtime.md).

## What are common workloads for Ray?[​](#common-workloads "Direct link to What are common workloads for Ray?")

The Ray AI libraries provide high-level APIs for completing most common data, AI, and ML tasks. The following are examples of common workloads:

* Batch inference.
* LLMs and gen AI.
* Model serving.
* Feature engineering and data preprocessing.
* Hyperparameter tuning.
* Distributing training.
* Reinforcement learning.

## What are the core features of Ray?[​](#core-features "Direct link to What are the core features of Ray?")

Ray provides a set of specialized libraries built on top of Ray Core. These libraries work together seamlessly to help you build end-to-end ML applications. Each library focuses on a specific part of the ML workflow, from data processing to model deployment.

Ray Core is the underlying common code base for the Ray AI libraries. Advanced Ray users extend the logic in Ray AI libraries by writing custom methods using lower-level Ray Core primitives. See [What is Ray Core?](#core).

All Ray apps deploy as Ray clusters. Anyscale supports deploying Ray clusters using virtual machines or Kubernetes. See [Define a Ray cluster](/configuration.md).

## What is Ray Data?[​](#ray-data "Direct link to What is Ray Data?")

Ray Data is a scalable data processing library built on Ray, designed for machine learning and AI workloads. It provides flexible and high-performance APIs for data loading, transformation, and consumption. In the Ray ecosystem, it is the primary tool for preprocessing, feature engineering, batch inference, and data ingestion for ML training.

Ray Data specializes in processing multimodal data, including video, audio, unstructured text, and images. It has support for structured and semi-structured data formats such as Parquet, CSV, and JSON.

To maximize utilization of CPU and GPU resources, Ray Data parallelizes all steps in data processing pipelines. Instead of distributing the entire dataset, Ray passes batches of data through pipeline logic with tasks distributed to the compute resources best suited for that computation.

For more details on Ray Data, see the [Ray Data overview](https://docs.ray.io/en/latest/data/data.html).

## What is Ray Train?[​](#ray-train "Direct link to What is Ray Train?")

Ray Train is the Ray AI library for distributed training and fine-tuning. Ray Train handles resource allocation for GPUs and CPUs and provides simple configurations for managing parallelism.

Ray Train provides specialized libraries for distributing and scaling code for ML and AI frameworks such as PyTorch, Hugging Face, and XGBoost. You migrate your existing training code to Ray Train by adding a few lines and decorator functions to configure the distribution of your training logic. You can continue to develop and test your training function on a small cluster, and then scale to hundreds or thousands of machines by updating only a few configurations.

Ray Train integrates with Ray Data to enable high-throughput streaming of large datasets for training. This allows you to design unified workloads that ingest raw data, apply preprocessing and feature engineering steps, and train or fine-tune models. See the Ray docs for [data loading and preprocessing](https://docs.ray.io/en/latest/train/user-guides/data-loading-preprocessing.html).

For more details on Ray Train, see the [Ray Train overview](https://docs.ray.io/en/latest/train/train.html).

## What is Ray Serve?[​](#ray-serve "Direct link to What is Ray Serve?")

Ray Serve is the Ray AI library for serving models and Python services to power online inference at scale. It supports popular ML frameworks and is performant for serving large and complex AI applications, including the following:

* Large language models (LLMs).
* ML pipelines with multiple models.
* Applications that combine ML and business logic.

Ray Serve supports dynamic scaling and resource sharing, with optimizations for multi-GPU deployments, including GPU fractional allocation.

Ray Serve automatically and dynamically batches and queues requests, and supports response streaming.

It has built-in support for FastAPI for HTTP handling.

For more details on Ray Serve, see the [Ray Serve overview](https://docs.ray.io/en/latest/serve/index.html).

## What is Ray Tune?[​](#ray-tune "Direct link to What is Ray Tune?")

Ray Tune is the Ray AI library for experiment execution and hyperparameter tuning. Ray Tune works with all major ML frameworks, with built-in support for framework-specific features and distributed training. Key benefits of Ray Tune include the following:

* Efficient CPU and GPU utilization across parallel execution of training runs and concurrent trials.
* Integration with optimization algorithms such as random search, Bayesian optimization, and population-based methods.
* Early stopping of non-promising configurations and automated trial prioritization.
* Built-in support for logging, experiment tracking, and checkpoint management and fault tolerance for long-running experiments.

For more details on Ray Tune, see the [Ray Tune overview](https://docs.ray.io/en/latest/tune/index.html).

## What is Ray RLlib?[​](#ray-rllib "Direct link to What is Ray RLlib?")

Ray RLlib is the Ray AI library for reinforcement learning (RL). RLlib provides production-level implementation of popular RL algorithms. Consider RLlib if you are looking to do any of the following:

* Scale RL training to large clusters.
* Deploy production RL systems.
* Experiment with custom algorithms or environments.
* Handle complex multi-agent scenarios.
* Combine multiple RL approaches.

For more details on Ray RLlib, see the [Ray RLlib overview](https://docs.ray.io/en/latest/rllib/index.html).

## What is Ray Core?[​](#core "Direct link to What is Ray Core?")

Ray Core is the underlying framework for all the Ray AI libraries. Anyscale recommends you use the Ray AI libraries for most applications and use cases. Use Ray Core when functionality you need isn't available in a Ray AI library.

Ray Core uses a set of primitives called tasks, actors, and objects to provide highly customizable, low-level tooling for building and scaling distributed applications. You can use Ray Core as a universal distributed compute platform for any Python code.

With Ray Core, you can implement nearly any application or pattern as a distributed Python program, but need to reason about low-level implementation details in order to get optimized performance.

For more details on Ray Core, see the [Ray Core overview](https://docs.ray.io/en/latest/ray-core/walkthrough.html).

## How does Anyscale contribute to Ray?[​](#how-does-anyscale-contribute-to-ray "Direct link to How does Anyscale contribute to Ray?")

All Ray AI libraries are open source. The Anyscale team works with the open source community and Anyscale customers to collaboratively set the roadmap for Ray and develop new functionality to meet user needs.

If you're an Anyscale customer, reach out to your account representative with suggestions for new Ray features, or open an issue or pull request on the [Ray project repo](https://github.com/ray-project/ray).

## What is KubeRay?[​](#what-is-kuberay "Direct link to What is KubeRay?")

[KubeRay](https://github.com/ray-project/kuberay) is an open source Kubernetes operator. Anyscale provides a proprietary operator for Kubernetes that allows you to deploy an Anyscale platform on top of your Kubernetes cluster. See [Deploy Anyscale on Kubernetes](/admin/cloud/kubernetes.md).

## What is RayTurbo?[​](#rayturbo "Direct link to What is RayTurbo?")

RayTurbo is the legacy name for the Anyscale Runtime, which is the proprietary version of Ray deployed on Anyscale. See [What is the Anyscale Runtime?](/runtime.md).
