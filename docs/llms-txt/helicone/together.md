# Source: https://docs.helicone.ai/getting-started/integration-method/together.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Together AI Integration

> Connect Helicone with Together AI, a platform for running open-source language models. Monitor and optimize your AI applications using Together AI's powerful models through a simple base_url configuration.

<Warning>
  This integration method is maintained but no longer actively developed. For the best experience and latest features, use our new [AI Gateway](/gateway/overview) with unified API access to 100+ models.
</Warning>

You can seamlessly integrate Helicone with your OpenAI compatible models that are deployed on Together AI.

The integration process closely mirrors the [proxy approach](/integrations/openai/javascript). The only distinction lies in the modification of the base\_url to point to the dedicated TogetherAI endpoint `https://together.helicone.ai/v1`.

```bash  theme={null}
base_url="https://together.helicone.ai/v1"
```

Please ensure that the base\_url is correctly set to ensure successful integration.

## Streaming with Together AI

Helicone now provides enhanced support for streaming with Together AI through our improved asynchronous stream parser. This allows for more efficient and reliable handling of streamed responses.

### Example: Manual Logging with Streaming

Here's an example of how to use Helicone's manual logging with Together AI's streaming functionality:

```typescript  theme={null}
import Together from "together-ai";
import { HeliconeManualLogger } from "@helicone/helpers";

export async function main() {
  // Initialize the Helicone logger
  const heliconeLogger = new HeliconeManualLogger({
    apiKey: process.env.HELICONE_API_KEY!,
    headers: {}, // You can add custom headers here
  });

  // Initialize the Together client
  const together = new Together();

  // Create your request body
  const body = {
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages: [{ role: "user", content: "Your question here" }],
    stream: true,
  } as Together.Chat.CompletionCreateParamsStreaming & { stream: true };

  // Make the request
  const response = await together.chat.completions.create(body);

  // Split the stream into two for logging and processing
  const [stream1, stream2] = response.tee();

  // Log the stream to Helicone using the async stream parser
  heliconeLogger.logStream(body, async (resultRecorder) => {
    resultRecorder.attachStream(stream1.toReadableStream());
  });

  // Process the stream for your application
  const textDecoder = new TextDecoder();
  for await (const chunk of stream2.toReadableStream()) {
    console.log(textDecoder.decode(chunk));
  }

  return stream2;
}
```

This approach allows you to:

1. Log all your Together AI streaming requests to Helicone
2. Process the stream in your application simultaneously
3. Benefit from Helicone's improved async stream parser for better performance

For more information on streaming with Helicone, see our [streaming documentation](/features/streaming).
