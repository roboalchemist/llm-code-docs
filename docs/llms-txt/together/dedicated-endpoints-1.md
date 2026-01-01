# Source: https://docs.together.ai/docs/dedicated-endpoints-1.md

# Dedicated Endpoints FAQs

## How does the system scale?

Dedicated endpoints support horizontal scaling. This means that it scales linearly with the additional replicas specified during endpoint configuration.

## How does auto-scaling affect my costs?

Billing for dedicated endpoints is proportional to the number of replicas. For example, scaling from 1 to 2 replicas will double your GPU costs.

## Is my endpoint guaranteed to scale to the max replica set?

We will scale to the max possible replica available at the time. This may be short of the max replicas that were set in the configuration if availability is limited.

## When to use vertical vs horizontal scale?

In other words, when to add GPUs per replica or add more replicas?

### Vertical scaling

Multiple GPUs, or vertical scaling, increases the generation speed, time to first token and max QPS. You should increase GPUs if your workload meets the following conditions:

**Compute-bound** If your workload is compute-intensive and bottlenecked by GPU processing power, adding more GPUs to a single endpoint can significantly improve performance.

**Memory-intensive** If your workload requires large amounts of memory, adding more GPUs to a single endpoint can provide more memory and improve performance.

**Single-node scalability** If your workload can scale well within a single node (e.g., using data parallelism or model parallelism), adding more GPUs to a single endpoint can be an effective way to increase throughput.

**Low-latency requirements** If your application requires low latency, increasing the number of GPUs on a single endpoint can help reduce latency by processing requests in parallel.

### Horizontal scaling

The number of replicas (horizontal scaling) increases the max number of QPS. You should increase the number of replicas if your workload meets the following conditions:

**I/O-bound workloads** If your workload is I/O-bound (e.g., waiting for data to be loaded or written), increasing the number of replicas can help spread the I/O load across multiple nodes.

**Request concurrency** If your application receives a high volume of concurrent requests, increasing the number of replicas can help distribute the load and improve responsiveness.

**Fault tolerance**: Increasing the number of replicas can improve fault tolerance by ensuring that if one node fails, others can continue to process requests.

**Scalability across multiple nodes** If your workload can scale well across multiple nodes (e.g., using data parallelism or distributed training), increasing the number of replicas can be an effective way to increase throughput.

## Troubleshooting dedicated endpoints configuration

There are a number of reasons that an endpoint isn't immediately created successfully.

**Lack of availability**: If we are short on available hardware, the endpoint will still be created but rather than automatically starting the endpoint, it will be queued for the next available hardware.

**Low availability**: We may have hardware available but only enough for a small amount of replicas. If this is the case, the endpoint may start but only scale to the amount of replicas available. If the min replica is set higher than we have capacity for, we may queue the endpoint until there is enough availability. To avoid the wait, you can reduce the minimum replica count.

**Hardware unavailable error**: If you see "Hardware for endpoint not available now. please try again later", the required resources are currently unavailable. Try using a different comparable model (see [whichllm.together.ai](https://whichllm.together.ai/)) or attempt deployment at a different time when more resources may be available.

**Model not supported**: Not all models are supported on dedicated endpoints. Check the list of supported models in your [account dashboard](https://api.together.xyz/models?filter=dedicated) under Models > All Models > Dedicated toggle. Your fine-tuned model must be based on a supported base model to deploy on an endpoint.

## Stopping an Endpoint

### Auto-shutdown

When you create an endpoint you can select an auto-shutdown timeframe during the configuration step. We offer various timeframes.

If you need to shut down your endpoint before the auto-shutdown period has elapsed, you can do this in a couple of ways.

### Web Interface

#### Shutdown during deployment

When your model is being deployed, you can click the red stop button to stop the deployment.

#### Shutdown when the endpoint is running

If the dedicated endpoint has started, you can shut down the endpoint by going to your models page. Click on the Model to expand the drop down, click the three dots and then **Stop endpoint**, then confirm in the pop-up prompt.

Once the endpoint has stopped, you will see it is offline on the models page. You can use the same three dots menu to start the endpoint again if you did this by mistake.

### API

You can also use the Together AI CLI to send a stop command, as covered in our documentation. To do this you will need your endpoint ID.

**Minimal availability**: We may have hardware available but only enough for a small amount of replicas. If this is the case, the endpoint may start but only scale to the amount of replicas available. If the min replica is set higher than we have capacity for, we may queue the endpoint until there is enough availability. To avoid the wait, you can reduce the min replica count.

## Will I be billed for the time spent spinning up the endpoint or looking for resources?

Billing events start only when a dedicated endpoint is successfully up and running. If there is a lag in time or a failure to deploy the endpoint, you will not be billed for that time.

## How much will I be charged to deploy a model?

Deployed models incur continuous per-minute hosting charges even when not actively processing requests. This applies to both fine-tuned models and dedicated endpoints. When you deploy a model, you should see a pricing prediction. This will change based on the hardware you select, as dedicated endpoints are charged based on the hardware used rather than the model being hosted.

You can find full details of our hardware pricing on our [pricing page](https://www.together.ai/pricing).

To avoid unexpected charges, make sure to set an auto-shutdown value, and regularly review your active deployments in the [models dashboard](https://api.together.xyz/models) to stop any unused endpoints. Remember that serverless endpoints are only charged based on actual token usage, while dedicated endpoints and fine-tuned models have ongoing hosting costs.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt