# Source: https://docs.openpipe.ai/features/request-logs/reporting-anthropic.md

# Logging Anthropic Requests

Anthropic's language models have a different API structure than those of OpenAI.
To record requests made to Anthropic's models, follow the examples below:

<Tabs>
  <Tab title="Python">
    ```python
    import time
    from anthropic import Anthropic
    from openpipe.client import OpenPipe

    anthropic = Anthropic()
    op_client = OpenPipe()

    payload = {
        "model": "claude-3-opus-20240229",
        "messages": [{"role": "user", "content": "Hello, Claude"}],
        "max_tokens": 100,
    }

    message = anthropic.messages.create(**payload)

    op_client.report_anthropic(
        requested_at=int(time.time() * 1000),
        received_at=int(time.time() * 1000),
        req_payload=payload,
        resp_payload=message,
        status_code=200,
        metadata={
            "prompt_id": "My prompt id",
        },
    )
    ```
  </Tab>

  <Tab title="NodeJS">
    ```typescript
    import Anthropic from "@anthropic-ai/sdk";
    import { Message, MessageCreateParams } from "@anthropic-ai/sdk/resources";
    import OpenPipe from "openpipe/client";

    const anthropic = new Anthropic();
    const opClient = new OpenPipe();

    const payload: MessageCreateParams = {
      model: "claude-3-opus-20240229",
      messages: [{ role: "user", content: "Hello, Claude" }],
      max_tokens: 1024,
    };

    const message: Message = await anthropic.messages.create(payload);

    await opClient.reportAnthropic({
      requestedAt: Date.now(),
      receivedAt: Date.now(),
      reqPayload: payload,
      respPayload: message,
      statusCode: 200,
      metadata: {
        prompt_id: "My prompt id",
      },
    });
    ```
  </Tab>
</Tabs>

If you're using a different programming language, you can make a raw http request to the [report-anthropic](/api-reference/post-report-anthropic) enpoint.
