# Source: https://docs.anyscale.com/runtime/train.md

# Ray Train

[View Markdown](/runtime/train.md)

# Ray Train

[Ray Train](https://docs.ray.io/en/latest/train/train.html) is an open-source library for distributed training and fine-tuning. Ray Train allows you to scale model training code from a single machine to a cluster of machines in the cloud, abstracting away the complexities of distributed computing. It's suitable for handling large models or large datasets.

Ray Train in the Anyscale Runtime simplifies and extends the open source Ray Train experience, making ML developers more productive by improving price-performance, production monitoring, and developer experience. The Anyscale Runtime adds mid-epoch training resumption, elastic training, and purpose-built observability dashboards to help you train models faster, more reliably, and with better visibility into performance and failures.

Anyscale recommends using Ray version 2.51.0 or later for all Ray Train workloads. In Ray 2.51.0 and later, Ray Train V2 is enabled by default, providing improved observability and structured logging.

## Mid-epoch training resumption[​](#mid-epoch-training-resumption "Direct link to Mid-epoch training resumption")

With mid-epoch training resumption, you can resume training from the exact point where it stopped without repeating or skipping data. The dataset iterator yields each row exactly once per epoch, even when failures, preemptions, or manual stops interrupt training.

See [Mid-epoch training resumption](/runtime/mid-epoch-resumption.md).

## Elastic training[​](#elastic-training "Direct link to Elastic training")

Ray Train in the Anyscale Runtime supports elastic training, enabling jobs to seamlessly adapt to changes in resource availability. This behavior ensures continuous execution despite hardware failures or node preemptions, avoiding idle or wasted time. As more nodes become available, the cluster dynamically scales up to speed up training with more worker processes.

To enable elastic training, use `ScalingConfig.num_workers` to specify `(min_workers, max_workers)` as a tuple instead of a fixed worker group size.

```
from ray.train.torch import TorchTrainer, ScalingConfig

def train_func():
    # Your training code here
    ...

# Elastic training with 1-10 workers
scaling_config = ScalingConfig(num_workers=(1, 10), use_gpu=True)

trainer = TorchTrainer(train_func, scaling_config=scaling_config)
trainer.fit()
```

The Anyscale Runtime always requests `max_workers` number of workers, but if it can't get all of them, it starts if `min_workers` is available.

If any failures happen, the Anyscale Runtime restarts with fewer workers. Then it attempts again to bring up to `max_workers` number of workers.

If the cluster gets additional nodes, the Anyscale Runtime restarts with the new workers added to the group.

## Production monitoring and observability[​](#monitoring "Direct link to Production monitoring and observability")

The Anyscale Runtime provides comprehensive monitoring and observability features to help you understand, debug, and optimize distributed training workloads.

### Persistent logs for post-mortem analysis[​](#persistent-logs-for-post-mortem-analysis "Direct link to Persistent logs for post-mortem analysis")

When you enable log ingestion, Anyscale automatically persists Ray Train logs for 30 days, enabling post-mortem analysis even after cluster failures. This feature allows you to debug without keeping expensive clusters running or attempting to reproduce errors. Persistent logs also make it easy to evaluate trends over time and spot slow or inefficient stages across multiple runs.

See [Accessing logs](/monitoring/accessing-logs.md).

### Train dashboard[​](#train-dashboard "Direct link to Train dashboard")

The Train dashboard provides a unified interface for monitoring training progress, debugging failures, and optimizing performance. Key capabilities include the following:

* **Unified log and metric access**: Drill down from high-level job status to individual worker logs and metrics without context-switching between systems.
* **Training progress visualization**: Track resource requests, scheduling behavior, and utilization patterns throughout the job lifecycle.
* **Error attribution**: Get detailed context about failures, including affected workers, error types—application versus hardware—and relevant logs across the stack.
* **Fault tolerance insights**: When using Ray Train fault tolerance or elastic training, easily inspect historical retry attempts and understand recovery behavior.
* **Integrated profiling**: One-click CPU and GPU profiling for live training jobs to identify performance bottlenecks.

See [Train dashboard](/monitoring/workload-debugging/train-dashboard.md).
