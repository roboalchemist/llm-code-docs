# Source: https://docs.anyscale.com/llm/batch-inference.md

# Run LLM batch inference on Anyscale

[View Markdown](/llm/batch-inference.md)

# Run LLM batch inference on Anyscale

This page explains how to run LLM batch inference workloads on Anyscale for enhanced performance, reliability, and developer experience.

## Why Anyscale[​](#why-anyscale "Direct link to Why Anyscale")

LLM batch inference is the process of running an LLM over a fixed set of inputs, such as summarizing a large batch of articles or extracting structured data from thousands of documents. While powerful, it presents unique challenges in production, including variable workloads, complex CPU/GPU pipeline management, and scaling data processing. See [Understand LLM batch inference basics](/llm/batch-inference/llm-batch-inference-basics.md) to learn about common use cases, challenges, and how batch differs from online inference.

The [`ray.data.llm`](https://docs.ray.io/en/latest/data/working-with-llms.html) module makes it easy to combine distributed data processing with integrated inference engines such as vLLM. Built on Ray, it natively maximizes CPU and GPU utilization, adds fault tolerance through checkpointing, and supports flexible data connections.

Running the same workload on Anyscale takes performance and developer experience to the next level through enhanced tooling, optimizations, and production-grade infrastructure.

## Develop with Workspaces[​](#development "Direct link to Develop with Workspaces")

Anyscale's developer experience centers on making it simple to develop and debug on arbitrarily large clusters without worrying about infrastructure setup, IDE configuration, or autoscaling.

Anyscale Workspaces enable seamless development without infrastructure concerns—just like working on a laptop. See [Workspaces](/platform/workspaces.md). Workspaces provide these key advantages over local Ray cluster setup:

* **Development tools**: Spin up a remote session from your local IDE (Cursor, VS Code, and more) and start coding, using the same tools you love but with the power of Anyscale's compute.
* **Dependencies**: Install dependencies using familiar tools such as pip or uv. Anyscale propagates all dependencies to the cluster's worker nodes.
* **Compute**: Leverage reserved or spot instances from any compute provider by deploying Anyscale into your account. Alternatively, use Anyscale Cloud for a fully serverless experience. Under the hood, clusters automatically spin up and are efficiently managed by Anyscale.
* **Debugging**: Leverage a distributed debugger to get the same VS Code-like debugging experience. See [Distributed debugger](/platform/workspaces/workspaces-debugging.md#distributed-debugger).

![Anyscale compute options](/assets/images/compute-63eff95bc2d0acb22bf29688427bf389.png)

## Deploy to production[​](#production "Direct link to Deploy to production")

For production LLM batch inference workloads, Anyscale jobs enable you to execute discrete workloads such as batch inference, embedding generation, or model fine-tuning. See [What are Anyscale jobs?](/jobs.md). Jobs provide:

* Definition and management through CLI, Python SDK, or YAML configuration. See [Create and manage jobs](/jobs/manage.md).
* Queues and schedules for workflow orchestration. See [Submit jobs to persistent job queues](/jobs/queues.md) and [Job schedules](/jobs/schedules.md).
* Built-in observability, alerting, and monitoring. See [Monitor a job](/jobs/monitor.md).

![Anyscale job results](/assets/images/job_result-40a3ca2de434d8f2071404844eea1701.png)

**Example Job Configuration:**

```
# job.yaml
name: llm-batch-inference
image_uri: anyscale/ray:2.49.0-py312-cu128
compute_config:
  ...
entrypoint: python main.py
max_retries: 0
```

```
# Submit the job
anyscale job submit -f job.yaml
```

## Anyscale Runtime optimizations[​](#anyscale-runtime "Direct link to Anyscale Runtime optimizations")

Ray workloads running on Anyscale automatically leverage the Anyscale Runtime, Anyscale's optimized Ray engine that delivers superior performance, scale, reliability, and efficiency for AI workloads. [RayTurbo Data improvements](https://www.anyscale.com/blog/rayturbo-data-improvements) provide up to **5x faster Parquet schema inference** compared to open-source Ray Data.

For LLM batch inference specifically, Ray Data on the Anyscale Runtime delivers:

* **Accelerated metadata fetching**: Improved performance when reading from large datasets for the first time.
* **Optimized autoscaling**: Jobs can start before waiting for the entire cluster to spin up.
* **High reliability**: Job-level checkpointing allows jobs to resume from the previous state after failures (driver crashes, head node failures, entire cluster failures, or unexpected exceptions). Once configured, checkpointing integrates seamlessly with standard Ray Data operations. By comparison, OSS Ray Data can only recover from worker node failures by retrying individual tasks.

See [Ray Data](/runtime/data.md) for more information.

## Monitor and debug workloads[​](#observability "Direct link to Monitor and debug workloads")

Anyscale provides enhanced debugging and observability capabilities for Ray Data workloads. The Ray Data dashboard allows you to monitor individual operators and key components of your batch workload in real time. Additional views, such as the Tasks dashboard, break down individual tasks by function, error status, and other metrics.

![Ray Data observability dashboard](/assets/images/data_dashboard-3fa5bab3ed4c55b8f5f13ad4f3ca4c5d.png)

These dashboards are invaluable for debugging issues (out-of-memory errors, back pressure, scaling problems) and identifying bottlenecks to improve utilization and throughput performance.
