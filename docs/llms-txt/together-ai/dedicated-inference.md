# Source: https://docs.together.ai/docs/dedicated-inference.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

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
  together endpoints hardware --model zai-org/GLM-4.7

  Hardware ID              GPU    Memory    Count    Price (per minute)    availability
  -----------------------  -----  --------  -------  --------------------  --------------
  8x_nvidia_h100_80gb_sxm  h100   80GB      8        $0.45                 ✓ available
  ```
</CodeGroup>

From this list, you can specify the GPUs by using `--hardware 8x_nvidia_h100_80gb_sxm`.

You can now create a dedicated endpoint by running:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints create \
  --model zai-org/GLM-4.7 \
  --hardware 8x_nvidia_h100_80gb_sxm \
  --display-name "My Endpoint" \
  --wait
  ```
</CodeGroup>

This command will finish when the endpoint is `READY`. To let it run asynchronously, remove the `--wait` flag.

Upon successful creation, you will receive an **endpoint ID** (e.g., `endpoint-e6c6b82f-90f7-45b7-af39-3ca3b51d08xx`). This ID is required for subsequent operations like get, update, start, stop, and delete. You can also find your endpoint IDs by running `together endpoints list --mine`.

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
  --model zai-org/GLM-4.7 \
  --hardware 8x_nvidia_h100_80gb_sxm \
  --display-name "My Endpoint" \
  --availability-zone us-east-1a \
  --wait
  ```
</CodeGroup>

### 3. Get endpoint status

You can check on the deployment status by running the following command with your endpoint ID (e.g., `endpoint-e6c6b82f-90f7-45b7-af39-3ca3b51d08xx`)

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints get <ENDPOINT_ID>
  ```
</CodeGroup>

A sample response will look like the following:

<CodeGroup>
  ```shell Shell theme={null}
  ID:		endpoint-e6c6b82f-90f7-45b7-af39-3ca3b51d08xx
  Name:		tester/zai-org/GLM-4.7-bb04c904
  Display Name:	My Endpoint
  Hardware:	8x_nvidia_h100_80gb_sxm
  Autoscaling:	Min=1, Max=1
  Model:		zai-org/GLM-4.7
  Type:		dedicated
  Owner:		tester
  State:		READY
  Created:	2025-02-18 11:55:50.686000+00:00
  ```
</CodeGroup>

### 4. Start, stop & delete endpoint

You can start, stop and delete endpoints by running the following commands with your endpoint ID (e.g., `endpoint-e6c6b82f-90f7-45b7-af39-3ca3b51d08xx`).
If you added the `--wait` flag on creation or previously stopped the endpoint, you can start it again by running:

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
  together endpoints list --mine
  ```
</CodeGroup>

To filter dedicated endpoints by usage type:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints list --mine --type dedicated --usage-type on-demand
  ```
</CodeGroup>

### 6. Send traffic to your endpoint

Once your endpoint is in the `READY` state, you can send inference requests to it. Use the **endpoint name** (found in the `Name` field from `together endpoints get`) as the `model` parameter in your API calls.

<Note>
  The endpoint name (e.g., `tester/zai-org/GLM-4.7-bb04c904`) is different from the endpoint ID (e.g., `endpoint-e6c6b82f-90f7-45b7-af39-3ca3b51d08xx`). Use the **endpoint name** for inference requests and the **endpoint ID** for management operations (start, stop, update, delete).
</Note>

<CodeGroup>
  ```shell cURL theme={null}
  curl -X POST https://api.together.xyz/v1/chat/completions \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "tester/zai-org/GLM-4.7-bb04c904",
      "messages": [{"role": "user", "content": "Hello!"}]
    }'
  ```

  ```python Python theme={null}
  from together import Together

  client = Together()

  response = client.chat.completions.create(
      model="tester/zai-org/GLM-4.7-bb04c904",
      messages=[{"role": "user", "content": "Hello!"}],
  )

  print(response.choices[0].message.content)
  ```
</CodeGroup>

## Endpoint options

### Replica count

Replicas provide horizontal scaling, ensuring better handling of high traffic, reduced latency, and resiliency in the event of instance failure. They are set with the `--min-replicas` and `--max-replicas` options. The default min and max replica is set to 1. When the max replica is increased, the endpoint will automatically scale based on server load.

You can configure replicas when creating an endpoint:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints create \
  --model zai-org/GLM-4.7 \
  --hardware 8x_nvidia_h100_80gb_sxm \
  --display-name "My Endpoint" \
  --min-replicas 1 \
  --max-replicas 3 \
  --wait
  ```
</CodeGroup>

To update the replica configuration on an existing endpoint, use the `update` command and pass your endpoint ID (e.g., `endpoint-e6c6b82f-90f7-45b7-af39-3ca3b51d08xx`):

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints update --min-replicas 2 --max-replicas 4 <ENDPOINT_ID>
  ```
</CodeGroup>

<Note>
  Both `--min-replicas` and `--max-replicas` must be specified together when updating an endpoint.
</Note>

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

Prompt caching is **enabled by default** for all Dedicated Endpoints and cannot be disabled.

<Note>
  The `--no-prompt-cache` CLI flag and `disable_prompt_cache` API field are deprecated and will be removed in February 2026. These fields are currently accepted but ignored — prompt caching is always enabled.
</Note>


Built with [Mintlify](https://mintlify.com).