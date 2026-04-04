# Source: https://docs.together.ai/docs/dedicated-inference.md

# Dedicated Inference

> Deploy models on your own custom endpoints for improved reliability at scale

Dedicated Endpoints allows you to deploy models as dedicated endpoints with custom hardware and scaling configurations. Benefits of dedicated endpoints include:

* Predictable performance unaffected by serverless traffic.
* Reliable capacity to respond to spiky traffic.
* Customization to suit the unique usage of the model.

## Getting Started

Jump straight into the API with these [docs](/reference/listendpoints) or create an endpoint with this guide below.

### 1. Select a model

Explore the list of supported models for dedicated endpoints on our [models list](https://api.together.ai/models?filter=dedicated).

You can also upload your own [model](/docs/custom-models) .

### 2. Create a dedicated endpoint

To create a dedicated endpoint, first identify the hardware options for your specific model.

To do this, run:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints hardware --model <MODEL_ID>
  ```
</CodeGroup>

You will get a response like:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints hardware --model mistralai/Mixtral-8x7B-Instruct-v0.1

  All hardware options:
    2x_nvidia_a100_80gb_sxm
    2x_nvidia_h100_80gb_sxm
    4x_nvidia_a100_80gb_sxm
    4x_nvidia_h100_80gb_sxm
    8x_nvidia_a100_80gb_sxm
    8x_nvidia_h100_80gb_sxm
  ```
</CodeGroup>

From this list, you can identify which of the GPUs can be listed in your command. For example, in this list, the following combinations are possible:

1. `--gpu a100 --gpu-count 2`, `--gpu a100 --gpu-count 4`, `--gpu a100 --gpu-count 8`
2. `--gpu h100 --gpu-count 2`, `--gpu h100 --gpu-count 4`, `--gpu h100 --gpu-count 8`

You can now create a dedicated endpoint by running:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints create \
  --model mistralai/Mixtral-8x7B-Instruct-v0.1 \
  --gpu h100 \
  --gpu-count 2 \
  --no-speculative-decoding \
  --no-prompt-cache \
  --wait
  ```
</CodeGroup>

This command will finish when the endpoint is `READY`. To let it run asynchronously, remove the `--wait`flag.

You can optionally start an endpoint in a specific availability zone (e.g., us-central-4b). To get the list of availability zones, run:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints availability-zones
  ```
</CodeGroup>

Then specify the availability zone when creating your endpoint. Only specify an availability zone if you have specific latency or geographic needs as selecting one can limit hardware availability.

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints create \
  --model mistralai/Mixtral-8x7B-Instruct-v0.1 \
  --gpu h100 \
  --gpu-count 2 \
  --availability-zone us-east-1a
  --no-speculative-decoding \
  --no-prompt-cache \
  --wait
  ```
</CodeGroup>

### 3. Get endpoint status

You can check on the deployment status by running:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints get <ENDPOINT_ID>
  ```
</CodeGroup>

A sample response will look like the following:

<CodeGroup>
  ```shell Shell theme={null}
  ID:		endpoint-e6c6b82f-90f7-45b7-af39-3ca3b51d08xx
  Name:		tester/mistralai/Mixtral-8x7B-Instruct-v0.1-bb04c904
  Display Name:	My Endpoint
  Hardware:	2x_nvidia_h100_80gb_sxm
  Autoscaling:	Min=1, Max=1
  Model:		mistralai/Mixtral-8x7B-Instruct-v0.1
  Type:		dedicated
  Owner:		tester
  State:		READY
  Created:	2025-02-18 11:55:50.686000+00:00
  ```
</CodeGroup>

### 4. Start, stop & delete endpoint

If you added the `--wait`flag on creation or previously stopped the endpoint, you can start it again by running:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints start <ENDPOINT_ID>
  ```
</CodeGroup>

Stopping the endpoint follows the same pattern:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints stop <ENDPOINT_ID>
  ```
</CodeGroup>

To fully delete the endpoint, run:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints delete <ENDPOINT_ID>
  ```
</CodeGroup>

### 5. List your endpoints

You can get a list of all your dedicated endpoints by running:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints list --mine true 
  ```
</CodeGroup>

To filter dedicated endpoints by usage type:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints list --mine true --type dedicated --usage-type on-demand
  ```
</CodeGroup>

## Endpoint options

### Replica count

Replicas provide horizontal scaling, ensuring better handling of high traffic, reduced latency, and resiliency in the event of instance failure. They are set with the `--min-replicas`and `--max-replicas`options. The default min and max replica is set to 1. When the max replica is increased, the endpoint will automatically scale based on server load.

### Auto-shutdown

If an endpoint is inactive for an hour, it will shutdown automatically. This window of inactivity can be customized when configuring a deployment in the web interface or by setting `--inactive-timeout` to the desired value.

### Choosing hardware and GPU count

A hardware configuration for a given model follows this format: \[gpu-count]-\[hardware]-\[gpu-type]-\[gpu-link]

Example:`2x_nvidia_h100_80gb_sxm`

When configuring the hardware on the CLI, you can specify which version of the hardware you would like by listing the `--gpu`(or hardware), `--gpu-count`and `gpu-type`

#### Multiple GPUs

Increasing the `gpu-count` will increase the GPUs per replica. This will result in higher generation speed, lower time-to-first-token and higher max QPS.

#### Availability zone

If you have specific latency or geographic needs, select an availability zone when creating your endpoint. It is important to note that restricting to an availability zone can limit hardware availability.

To get the list of availability zones, run:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints availability-zones
  ```
</CodeGroup>

### Speculative decoding

Speculative decoding is an optimization technique used to improve the efficiency of text generation and decoding processes. Using speculators can improve performance, increase throughput and improve the handling of uncertain or ambiguous input.

Customers who require consistently low tail latencies—such as those running real-time or mission-critical applications—may want to avoid speculative decoding. While this technique can improve average performance, it also introduces the risk of occasional extreme delays, which may be unacceptable in latency-sensitive workloads.

By default, speculative decoding is not enabled. To enable speculative decoding, remove the `--no-speculative-decoding` flag from the create command.

### Prompt caching

Prompt caching stores the results of previously executed prompts, allowing your model to quickly retrieve and return cached responses instead of reprocessing the same input. This significantly improves performance by reducing redundant computations.

By default, caching is not enabled. To turn on prompt caching, remove `--no-prompt-cache` from the create command.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt