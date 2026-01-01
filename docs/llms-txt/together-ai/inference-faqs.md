# Source: https://docs.together.ai/docs/inference-faqs.md

# Inference FAQs

## Model Selection and Availability

### What models are available for inference on Together?

Together hosts a wide range of open-source models and you can view the latest inference models [here](https://docs.together.ai/docs/serverless-models).

### Which model should I use?

The world of AI evolves at a rapid pace, and the often overwhelming flow of new information can make it difficult to find exactly what you need for what you want to do.

Together AI has built Which LLM to help you cut through the confusion. Just tell us what you need/want to do, and we'll tell you which model is the best match.

Visit [whichllm.together.ai](https://whichllm.together.ai/) to find the right model for your use case.

Together AI supports over 200+ open-source models with a wide range of capabilities: Chat, Image, Vision, Audio, Code, Language, Moderation, Embedding, Rerank.

#### Free Models Available

Together AI offers a couple of models that you can use without cost:

##### Chat/Language Models:

* **Apriel 1.5 15B Thinker** - An updated multimodal reasoning model from ServiceNow's Apriel SLM series. With 30% better reasoning token efficiency than its predecessor.

##### Image Generation:

* **FLUX.1 \[schnell] Free** - Free endpoint for the SOTA open-source image generation model by Black Forest Labs

**Note:** Free model endpoints have reduced rate limits and performance compared to paid Turbo endpoints, but provide an excellent way to experiment and test capabilities before committing to paid services.

## Model Parameters and Usage

### What is the maximum context window supported by Together models?

The maximum context window varies significantly by model. Refer to the specific model's documentation or the inference models [page](https://docs.together.ai/docs/serverless-models) for the exact context length supported by each model.

### Where can I find default parameter values for a model?

Default parameter values for a model can be found in the `generation_config.json` file on Hugging Face. For example, the configuration for Llama 3.3 70B Instruct shows defaults like temperature: 0.6 and top\_p: 0.9. If not defined, no value is passed for that parameter.

### How do I send a request to an inference endpoint?

You can use the OpenAI-compatible API. Example using curl:

```bash  theme={null}
curl https://api.together.xyz/v1/chat/completions \
  -H "Authorization: Bearer $TOGETHER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
         "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
         "messages": [{"role": "user", "content": "Hello!"}]
       }'
```

More examples in Python and TypeScript are available [here](https://docs.together.ai/docs/openai-api-compatibility).

### Do you support function calling or tool use?

Function calling is natively supported for some models (see [here](https://docs.together.ai/docs/function-calling#function-calling)) but structured prompting can simulate function-like behavior.

### Function Calls Not Returned in Response "message.content"

Models that support Function Calling return any tool calls in a separate part of the model response, not inside of `message.content`. Some models will return "None" for this if any function calls are made.

Any tool calls instead will be found in:

`message.tool_calls[0].function.name`

For example, when making a function call, `message.content` may be None, but the function name will be in `message.tool_calls[0].function.name`.

### Do you support structured outputs or JSON mode?

Yes, you can use JSON mode to get structured outputs from LLMs like DeepSeek V3 & Llama 3.3. See more [here](https://docs.together.ai/docs/json-mode).

#### Troubleshooting Structured Output Generation

When working with structured outputs, you may encounter issues where your generated JSON gets cut off or contains errors. Here are key considerations:

* **Token Limits**: Check the maximum token limit of your model and ensure you're under it. Model specifications are available in our [serverless models documentation](https://docs.together.ai/docs/serverless-models).
* **Malformed JSON**: Validate your example JSON before using it in prompts. The model follows your example exactly, including syntax errors. Common symptoms include unterminated strings, repeated newlines, incomplete structures, or truncated output with 'stop' finish reason.

## Performance and Optimization

### What kind of latency can I expect for inference requests?

Latency depends on the model and prompt length. Smaller models like Mistral may respond in less than 1 second, while larger MoE models like Mixtral may take several seconds. Prompt caching and streaming can help reduce perceived latency.

### Is Together suitable for high-throughput workloads?

Yes. Together supports production-scale inference. For high-throughput applications (e.g., over 100 RPS), [contact](https://www.together.ai/contact) the Together team for dedicated support and infrastructure.

### Does Together support streaming responses?

Yes. You can receive streamed tokens by setting `"stream": true` in your request. This allows you to begin processing output as soon as it is generated.

### Can I use quantized models for faster inference?

Yes. Together hosts some models with quantized weights (e.g., FP8, FP16, INT4) for faster and more memory-efficient inference. Support varies by model.

### Can I cache prompts or use speculative decoding?

Yes. Together supports optimizations like prompt caching and speculative decoding for models that allow it, reducing latency and improving throughput.

### Can I run batched or parallel inference requests?

Yes. Together supports batching and high-concurrency usage. You can send parallel requests from your client and take advantage of backend batching. See [Batch Inference](https://docs.together.ai/docs/batch-inference#batch-inference) for more details.

## Data Privacy and Security

### Is my data stored or logged?

Together does not store your input or output by default. Temporary caching may be used for performance unless otherwise configured.

### Will my data be used to train other models?

Data sharing for training other models is opt-in and not enabled by default. You can check or modify this setting in your [account profile](https://api.together.ai/settings/profile) under Privacy & Security. See our [privacy policy](https://www.together.ai/privacy) for more details.

### Can I run inference in my own VPC or on-premise?

Yes. Together supports private networking VPC-based deployments for enterprise customers requiring data residency or regulatory compliance. [Contact us](https://www.together.ai/contact) for more information.

## Billing and Limits

### How is inference usage billed?

Inference is billed per input and output token, with rates varying by model. Refer to the pricing [page](https://www.together.ai/pricing) for current pricing details.

### What happens if I exceed my rate limit or quota?

You will receive a 429 Too Many Requests error. You can request higher limits via the Together dashboard or by contacting [support](https://www.together.ai/contact).

## Integrations and Support

### Can I use Together inference with LangChain or LlamaIndex?

Yes. Together is compatible with LangChain via the OpenAI API interface. Set your Together API key and model name in your environment or code.

See more about all available integrations: [Langchain](https://docs.together.ai/docs/integrations#langchain), [LlamaIndex](https://docs.together.ai/docs/integrations#llamaindex), [Hugging Face](https://docs.together.ai/docs/integrations#huggingface), [Vercel AI SDK](https://docs.together.ai/docs/integrations#vercel-ai-sdk).

### How does Together ensure the uptime and reliability of its inference endpoints?

Together aims for high reliability, offering 99.9% SLAs for dedicated endpoints.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt