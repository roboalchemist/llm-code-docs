# Source: https://docs.salad.com/container-engine/explanation/job-processing/job-queues.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Salad Job Queues

*Last Updated: February 14, 2025*

Job Queues provide a way to process discrete jobs without worrying about node capacity, load balancing, and retries.
With Job Queues you configure a port on your container, deploy your container group, and then send requests to a static
endpoint. These requests are automatically queued and distributed to healthy nodes, with automatic retries to handle
transient failures.

# Limitations

* Our Job Queues are designed to distribute tasks to an HTTP server, and queue operations are managed with http response
  symantics, e.g. return 200 for a successful job, 500 for a failed job.
* Jobs will be retried up to 3 times (meaning 4 total attempts) before being marked as failed. This limitation in
  combination with interruptible instances means our job queues are not well suited for extremely long running tasks.
* Instance interruptions count as job failures, and those jobs will be retried according to the above policy.
* Jobs are not guaranteed to be processed in order, but they will be processed in a FIFO manner.
* Jobs are not guaranteed to be processed by the same node, but they will be processed by a healthy node.
* The response body from your http server cannot exceed 10MB.
* Job Queues can only be managed and accessed via the [Job Queue API](/reference/saladcloud-api/queues/create-queue)

# Terminology

* **Job:** An individual request to be processed. An example of a job might be a token string sent to an image
  generation service.
* **Job Queue Worker:** A small, multi-architecture go binary program you install in your container which receives jobs
  from the Queue, forwards them to your application running in the container, receives results and returns them to the
  Queue.
* **Job Queue:** Salad-managed queue service that receives requests from your systems, queues them, and distributes them
  FIFO to nodes. Job queues distribute received jobs to one or more container groups. A container group is connected to
  a Job Queue when the container group is first created.

# Architecture

<img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/job-queues-architecture.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=ea76cc54d3c14ddaf5786c46bd589c3e" data-og-width="954" width="954" data-og-height="347" height="347" data-path="container-engine/images/job-queues-architecture.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/job-queues-architecture.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=9c968f37aad7d1cbd4074c7b691e7175 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/job-queues-architecture.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=7b1a336c09c0a4c2aa16c7f30222f2b4 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/job-queues-architecture.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=ee250eed02aed5e40d3ecdb1005a0620 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/job-queues-architecture.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=695e25cb796a6f108bed213dd4bc62ed 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/job-queues-architecture.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=f1a91cb32e705b5a943d175aa7203187 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/job-queues-architecture.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=3a94e9f0d310d25e67e390f51d45a124 2500w" />

# Getting Started with Job Queues

1. **Create a Job Queue** - [How-to Guide](/container-engine/how-to-guides/job-processing/creating-a-job-queue) |
   [API Reference](/reference/saladcloud-api/queues/create-queue)
2. **Configure the Job Queue Worker** - [How-to Guide](/container-engine/how-to-guides/job-processing/queue-worker)
3. **Push your container to a registry** - [Container Registry Guides](/container-engine/how-to-guides/registries)
4. **Configure a Container Group with a Job Queue** -
   [How-to Guide](/container-engine/how-to-guides/job-processing/using-queues) |
   [API Reference](/reference/saladcloud-api/container-groups/create-container-group)
5. **Add Jobs to the Queue** - [API Reference](/reference/saladcloud-api/queues/create-job)
6. **Retrieve Results** - [API Reference](/reference/saladcloud-api/queues/get-job) |
   [List Jobs](/reference/saladcloud-api/queues/list-jobs)
