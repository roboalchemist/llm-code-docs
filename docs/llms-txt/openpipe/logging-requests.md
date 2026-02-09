# Source: https://docs.openpipe.ai/features/request-logs/logging-requests.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openpipe.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Logging Requests

>  Record production data to train and improve your models' performance.

Request logs are a great way to get to know your data. More importantly, you can import recorded logs directly into your training datasets. That means it's really easy to train on data you've collected in production.

We recommend collecting request logs for both base and fine-tuned models. We provide several options for recording your requests.

### SDK

The simplest way to start ingesting request logs into OpenPipe is by installing our Python or TypeScript SDK. Requests to both OpenAI and OpenPipe models will automatically be recorded.
Logging doesn't add any latency to your requests, because our SDK calls the OpenAI server directly and returns your completion before kicking off the request to record it in your project.

We provide a drop-in replacement for the OpenAI SDK, so the only code you need to update is your import statement:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    # from openai import OpenAI
    from openpipe import OpenAI

    # Nothing else changes

    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "count to 10"}],
        # searchable metadata tags are highly recommended
        metadata={"prompt_id": "counting", "any_key": "any_value"},
    )
    ```
  </Tab>

  <Tab title="NodeJS">
    ```typescript  theme={null}
    // import OpenAI from "openai"
    import OpenAI from "openpipe/openai";

    // Nothing else changes

    const client = new OpenAI();

    const completion = await client.chat.completions.create({
      model: "gpt-4o",
      messages: [{ role: "user", content: "Count to 10" }],
      // searchable metadata tags are highly recommended
      metadata: {
        prompt_id: "counting",
        any_key: "any_value",
      },
    });
    ```
  </Tab>
</Tabs>

See [Installing the SDK](/getting-started/openpipe-sdk) for a quick guide on how to get started.

### Proxy

If you're developing in a language other than Python or TypeScript, the best way to ingest data into OpenPipe is through our proxy. We provide a `/chat/completions` endpoint that is fully compatible
with OpenAI, so you can continue using the latest features like tool calls and streaming without a hitch.

Integrating the Proxy and logging requests requires a couple steps.

1. Add an OpenAI key to your project in the [project settings](https://app.openpipe.ai/settings) page.
2. Set the authorization token of your request to be your OpenPipe API key.
3. Set the destination url of your request to be `https://api.openpipe.ai/api/v1/chat/completions`.
4. When making any request that you’d like to record, include the `"store": true` parameter in the request body. We also recommend that you add custom metadata tags to your request to
   distinguish data collected from different prompts.

Here's an example of steps 2-4 put together in both a raw cURL request and with the Python SDK:

<Tabs>
  <Tab title="cURL Request">
    ```bash  theme={null}
    curl --request POST \
      --url https://api.openpipe.ai/api/v1/chat/completions \
      --header "Authorization: Bearer YOUR_OPENPIPE_API_KEY" \
      --header 'Content-Type: application/json' \
      --data '{
      "model": "gpt-4-0613",
      "messages": [
        {
          "role": "system",
          "content": "count to 5"
        }
      ],
      "max_tokens": 100,
      "temperature": 0,
      "store": true,
      "metadata": {
        "prompt_id": "first_prompt"
      }
    }'
    ```
  </Tab>

  <Tab title="Python SDK">
    ```python  theme={null}
    from openai import OpenAI

    # Find your API key in https://app.openpipe.ai/settings
    client = OpenAI(
        base_url="https://api.openpipe.ai/api/v1", api_key="YOUR_OPENPIPE_API_KEY"
    )

    completion = client.chat.completions.create(
        model="gpt-4-0613",
        messages=[{"role": "system", "content": "count to 5"}],
        stream=True,
        store=True,
        metadata={"prompt_id": "first_prompt"},
    )


    ```
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript  theme={null}
    import OpenAI from "openai";

    // Find your API key in https://app.openpipe.ai/settings
    const client = new OpenAI({
      baseURL: "https://api.openpipe.ai/api/v1",
      apiKey: "YOUR_OPENPIPE_API_KEY",
    });

    const completion = await client.chat.completions.create({
      model: "gpt-4-0613",
      messages: [{ role: "system", content: "count to 5" }],
      store: true,
      metadata: { prompt_id: "first_prompt" },
    });
    ```
  </Tab>
</Tabs>

### Reporting

If you need more flexibility in how you log requests, you can use the `report` endpoint. This gives you full control over when and how to create request logs.

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    import time
    from openai import OpenAI
    from openpipe.client import OpenPipe

    client = OpenAI()
    op_client = OpenPipe()

    payload = {
        "model": "gpt-4o",
        "messages": [{"role": "user", "content": "Count to 10"}],
        "metadata": {"prompt_id": "My prompt id"},
    }

    completion = client.chat.completions.create(**payload)

    op_client.report(
        requested_at=int(time.time() * 1000),
        received_at=int(time.time() * 1000),
        req_payload=payload,
        resp_payload=completion,
        status_code=200,
    )
    ```
  </Tab>

  <Tab title="NodeJS">
    ```typescript  theme={null}
    import OpenAI from "openai";
    import { ChatCompletionCreateParams } from "openai/resources";
    import OpenPipe from "openpipe/client";

    const client = new OpenAI();
    const opClient = new OpenPipe();

    const payload: ChatCompletionCreateParams = {
      model: "gpt-4o",
      messages: [{ role: "user", content: "Count to 10" }],
      metadata: { prompt_id: "My prompt id" },
    };

    const completion = await client.chat.completions.create(payload);

    await opClient.report({
      requestedAt: Date.now(),
      receivedAt: Date.now(),
      reqPayload: payload,
      respPayload: completion,
      statusCode: 200,
    });
    ```
  </Tab>
</Tabs>

If you’re developing in a language other than Python or TypeScript, you can also make a raw HTTP request to the [report](/api-reference/post-report) endpoint.

Once you've set up logging, you will see the data on the Request Logs page. From there, you'll be able to search through your requests and train your models. See [Training on Logs](/features/datasets/importing-logs) to learn more.

Each project includes up to 100,000 request logs for free. Need more? Additional storage is available on our [enterprise plan](/pricing/pricing#enterprise-plans) - just reach out to us at [hello@openpipe.ai](mailto:hello@openpipe.ai) to discuss your needs.
