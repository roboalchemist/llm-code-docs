# Source: https://docs.anyscale.com/runtime.md

# What is the Anyscale Runtime?

[View Markdown](/runtime.md)

# What is the Anyscale Runtime?

The Anyscale Runtime describes the proprietary version of Ray used for running workloads on Anyscale.

Anyscale improves Ray performance using a combination of fine-tuned infrastructure, advanced checkpointing, and engine optimizations.

The Anyscale Runtime uses the same APIs and libraries as Ray, meaning you have full portability for your Ray code without fear of vendor lock-in.

## Data[​](#data "Direct link to Data")

Ray Data in the Anyscale Runtime provides enhanced data processing capabilities for machine learning workloads, particularly for unstructured data such as images, video, and audio. The Anyscale Runtime improves Ray Data performance through intelligent autoscaling, accelerated I/O operations, and production-grade fault tolerance.

Key improvements include the following:

* **Intelligent autoscaling**: Responsive cluster and actor pool scaling that enables jobs to start immediately without waiting for full cluster launch.
* **Job-level checkpointing**: Recover from driver, head node, or cluster failures without restarting from the beginning.
* **Data dashboard**: Purpose-built observability for debugging data pipelines with operator metrics and dataset-aware logs. See [Ray Data dashboard](/monitoring/workload-debugging/data-dashboard.md).

The Anyscale Runtime also includes automatic optimizations for file chunking, vectorized operations, advanced query planning, and enhanced I/O performance that work without configuration.

For detailed information, see [Ray Data](/runtime/data.md)

## Train[​](#train "Direct link to Train")

Ray Train in the Anyscale Runtime provides enhanced distributed training capabilities beyond open source Ray Train. Anyscale recommends using Ray version 2.51.0 or later for all Ray Train workloads to access the following improvements:

* **Mid-epoch training resumption**: Resume training from the exact data sample where it stopped, ensuring the dataset iterator processes each row exactly once per epoch. See [Mid-epoch training resumption](/runtime/mid-epoch-resumption.md).
* **Elastic training**: Dynamically scale worker groups in response to resource availability, ensuring continuous execution despite hardware failures or node preemptions. See [Elastic training](/runtime/train.md#elastic-training).
* **Train dashboard with profiling**: Purpose-built observability dashboard with integrated CPU and GPU profiling tools for identifying bottlenecks and debugging failures. See [Train dashboard](/monitoring/workload-debugging/train-dashboard.md).

When you enable log ingestion, Anyscale automatically persists Ray Train logs for 30 days, enabling post-mortem analysis without keeping expensive clusters running. See [Accessing logs](/monitoring/accessing-logs.md)

## Serve[​](#serve "Direct link to Serve")

The Anyscale Runtime optimizes your Ray Serve optimizations for high-throughput and reduced latency, while Anyscale services provide production serving endpoints with enhancements for high availability, high reliability, and zero-downtime updates.

See [Ray Serve on the Anyscale Runtime](/runtime/serve.md).

## RLlib[​](#rllib "Direct link to RLlib")

The Anyscale Runtime includes the InfiniteAPPO algorithm for use with RLlib as a beta release.

InfiniteAPPO is a decentralized Asynchronous Proximal Policy Optimization algorithm tuned to avoid scaling bottlenecks in traditional APPO. By moving communication and computation to the edges, the Anyscale Runtime is able to decentralize data and control and achieve high training throughput with reduced scaling issues.

To get started with InfiniteAPPO, contact [Anyscale Support](mailto:support@anyscale.com).
