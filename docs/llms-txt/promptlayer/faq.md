# Source: https://docs.promptlayer.com/features/faq.md

# FAQ

Frequently Asked Questions

Don't see your question here? Send a message in [Discord](https://discord.gg/DBAhQbW39S) or email us at [hello@promptlayer.com](mailto:hello@promptlayer.com)

## Does PromptLayer support multi-modal image models like `gpt-4-vision`?

Yes, PromptLayer supports multi-modal image models, including `gpt-4-vision-preview`. They are used in a similar way to normal LLMs.

To use `gpt-4-vision-preview` with PromptLayer, follow these steps:

1. Ensure you have the PromptLayer and OpenAI Python libraries installed.
2. Replace the standard OpenAI import with the [PromptLayer SDK client](/languages/python) (or use the REST API).
3. Make your request to `gpt-4-vision-preview` with the necessary image inputs, either through image URLs or base64 encoded images.
4. Check the PromptLayer dashboard to see your request logged!

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/gpt-4-vision-preview.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=8704afa732be26a893b2688c2bb45302" alt="gpt-4-vision request" data-og-width="2030" width="2030" data-og-height="1084" height="1084" data-path="images/gpt-4-vision-preview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/gpt-4-vision-preview.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=dcc8703665c50379444f539a21ae0c8f 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/gpt-4-vision-preview.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=1da9fce1f4e36273162bb6dc14c7de02 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/gpt-4-vision-preview.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=afd4362c1be30b4ee9f0f6d4d9e7c918 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/gpt-4-vision-preview.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=c57cf7aec31aa46c9f77868a136e10d3 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/gpt-4-vision-preview.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=d497a3fcaaa661eadaf7f522fb6bff4d 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/gpt-4-vision-preview.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=bf43da3c605f894319eda710cc1efb5a 2500w" />

Multi-modal models are also supported in the Prompt Registry, Playground, and Evaluations pages.

## Do you support OpenAI function calling?

Yes, we take great pride in staying up to date. PromptLayer is 1-to-1 with OpenAI's library. That means, if you are using PromptLayer+OpenAI through the Python libraries, [function calling](https://platform.openai.com/docs/guides/function-calling) will be implicitly supported.

## Does PromptLayer support streaming?

Yes, streaming requests are supported on the PromptLayer Python and JS SDK. PromptLayer now includes `prompt_blueprint` support in streaming responses, providing both raw streaming data and progressively built structured responses.

When streaming is enabled, each chunk includes:

* `raw_response`: The raw streaming response from the LLM provider
* `prompt_blueprint`: The progressively built prompt blueprint showing the current state of the response
* `request_id`: Only included in the final chunk to indicate completion

Example usage for OpenAI:

```python  theme={null}
for chunk in pl.run(prompt_name="your-prompt", stream=True):
    # Access raw streaming response
    print(chunk["raw_response"])
    
    # Access progressively built prompt blueprint
    if chunk["prompt_blueprint"]:
        current_response = chunk["prompt_blueprint"]["prompt_template"]["messages"][-1]
        if current_response.get("content"):
            print(f"Current response: {current_response['content']}")
```

Example usage for Anthropic:

```python  theme={null}
for chunk in pl.run(prompt_name="your-prompt", stream=True):
    raw_chunk = chunk["raw_response"]
    
    # Handle Anthropic streaming event types
    if raw_chunk.get("type") == "content_block_delta":
        delta = raw_chunk.get("delta", {})
        if delta.get("type") == "text_delta":
            print(f"Streaming content: {delta.get('text', '')}")
    
    # Access progressively built prompt blueprint
    if chunk["prompt_blueprint"]:
        current_response = chunk["prompt_blueprint"]["prompt_template"]["messages"][-1]
        if current_response.get("content") and len(current_response["content"]) > 0:
            text_content = current_response["content"][0].get("text", "")
            if text_content:
                print(f"Current response: {text_content}")
```

If you are using [LangChain](/languages/langchain), streaming is only supported when you use the `PromptLayerCallbackHandler`. Streaming is not supported through the PromptLayer-specific LLMs (the old way to use LangChain).

Finally, if you are interacting with PromptLayer through our [REST API](/languages/rest-api) you will need to store the whole output and log it to PromptLayer (`log-request`) only after it is finished.

## I'm having trouble with the LangChain integration.

Try updating both LangChain and PromptLayer to their most recent versions.

## Can I export my data from PromptLayer?

Yes. You can export your usage data with the button shown below.

Filter your training data export by tags, a search query, or metadata.

<video controls="controls">
  <source src="https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/videos/export.mp4?fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=959826bddc7f1cd9f79243157561df3c" type="video/mp4" data-path="videos/export.mp4" />
</video>

## Do you support on-premises deployment?

Yes, we do support on-premises deployment for a select few of our enterprise customers. However, we are rolling out this option slowly.

If you are interested in onprem, please [contact us](mailto:hello@promptlayer.com) for more information.

## Does AsyncOpenAI work with PromptLayer?

Yes, AsyncOpenAI is compatible with PromptLayer. Use them together as demonstrated in example below.

```python  theme={null}
from promptlayer import PromptLayer 
promptlayer_client = PromptLayer(api_key="pl_*****")

import asyncio
# from openai import AsyncOpenAI
AsyncOpenAI = promptlayer_client.openai.AsyncOpenAI

client = AsyncOpenAI(
    api_key="sk-***",
)


async def main() -> None:
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="gpt-3.5-turbo",
    )
    print(chat_completion)

asyncio.run(main())
```

## Is PromptLayer SOC 2 certified?

Yes, we have achieved SOC 2 Type 2 certification. Please [contact us](mailto:hello@promptlayer.com) for the report.

## Why doesn't my evaluation report use the newest version of my prompt?

To ensure your evaluation report reflects the newest version of your prompt template, you must configure your evaluation pipeline to use the "latest" version of the prompt template in its column step. The template is fetched at runtime, and specifying a frozen version will result in the evaluation report not reflecting your newest prompt template.

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/latest-faq.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=77c26c604e3d055f70f40a9bf7d85992" alt="Latest FAQ Updates" data-og-width="997" width="997" data-og-height="743" height="743" data-path="images/latest-faq.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/latest-faq.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=a4aff32ea7c8b9340f9bb14dc7fedadc 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/latest-faq.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=b2790bcf6d4cdbb7b9af308cc27c534e 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/latest-faq.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=522d206b71429d06bf402314c228bfe0 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/latest-faq.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=c22bb22382b4278674cf7f4530b94961 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/latest-faq.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=52c76e9c02d05cc68eadc5fb5774a0fc 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/latest-faq.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=334f4e89547ee8400243a2867cffcb37 2500w" />

## What model providers do you support on your evaluations page?

While you can log LLM requests from any model and our Prompt Registry is agnostic, our evaluations & playground requests support OpenAI's GPT, Anthropic's Claude, Google's Gemini, Bedrock, Mistral, and Cohere.

## Do you support open source models?

PromptLayer provides out-of-the-box support for Mistral in our logs, playground, Prompt Registry, and evals. You can also connect your own models to the logs & registry.

## What's the difference between tags and metadata?

Both [tags](/features/prompt-history/tagging-requests) and [metadata](/features/prompt-history/metadata) enable the addition of supplementary information to your request logs, yet they serve distinct purposes. Tags are ideal for classifying requests into a limited number of predefined categories, such as "prod" or "dev". Conversely, metadata is tailored for capturing unique, request-specific details like user IDs or session IDs.

## Why do I see extra input variables in my prompt template? Parsing does not seem to be working.

If you see extra input variables in the Prompt Registry or when creating an evaluation, it is likely due to string parsing errors. By default every prompt template uses "f-string" string parsing (`{var}`). If your prompt includes JSON, this will cause issues. We recommend switching to "jinja2" string parsing (`{{var}}`) to avoid such issues.

To switch input variable string parsers, navigate to the prompt template in the Prompt Registry. Then, click "Edit". In the editor, on the top right, you will see a dropdown that allows you to switch between "f-string" and "jinja2". For more details on using template variables effectively, see our [Template Variables](/features/prompt-registry/template-variables) documentation.

## How do I inject multiple messages into my prompt template?

You can use [placeholders](/features/prompt-registry/placeholder-messages), built just for that!

## Does PromptLayer support self-hosted models or custom base URLs?

Yes, PromptLayer supports using your own self-hosted models, those from providers like HuggingFace, or Azure OpenAI. To use a custom base URL:

1. Go to your workspace settings
2. Scroll to "Provider Base URLs"
3. Add the base URL for your model provider

<img src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/quickstart/base-url.png?fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=5a4af21b300518fd889a56be96a1835c" alt="Base URL Configuration" data-og-width="907" width="907" data-og-height="325" height="325" data-path="images/quickstart/base-url.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/quickstart/base-url.png?w=280&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=3428577a44a8e74283f5cc5adb47c474 280w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/quickstart/base-url.png?w=560&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=8e2e0380c2114433aee59bbf38e81267 560w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/quickstart/base-url.png?w=840&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=73248356bebacbaef458c38f89723639 840w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/quickstart/base-url.png?w=1100&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=42f441c951d50813d80503c2bc539634 1100w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/quickstart/base-url.png?w=1650&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=1fe70c53fab859f7b637de16cde7aa2d 1650w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/quickstart/base-url.png?w=2500&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=5aff7ab96e24683a77e3432b2a17755f 2500w" />

### Can I cancel my PromptLayer subscription?

Yes, you can cancel your subscription at any time. Your subscription will remain active until the end of the billing cycle. To cancel your subscription, go to your settings and click on billing portal.

## Does PromptLayer support Grok from xAI?

Yes, PromptLayer supports Grok models through custom providers. For detailed setup instructions and usage guidelines, see our [xAI (Grok) integration guide](/features/xai-integration).

## Does PromptLayer support Deepseek models?

Yes, PromptLayer supports Deepseek models through custom base URLs. Configure it in workspace settings under "Provider Base URLs" using OpenAI as the provider and `https://api.deepseek.com` as the base URL. You can then use models like `deepseek-chat` and `deepseek-reasoner` in the Playground and Prompt Registry.

## Does PromptLayer support MCP?

Yes, PromptLayer supports MCP functions in agents. The MCP Action node allows you to invoke remote functions hosted on your MCP server. To use it, configure the node with your MCP server's base URL and authentication token. Then, select the target function from the available list—PromptLayer will automatically introspect the function schema. Input parameters can be dynamically mapped from outputs of previous nodes, enabling full integration with the rest of your agent workflow. Function calls are executed at runtime, and outputs are passed downstream like any other node result.

<iframe src="https://www.loom.com/embed/92ab94394c6b46fb966f29f16b72cd31?sid=81976fe8-5998-473c-b9ec-4470bab8b0c4" frameBorder="0" allowFullScreen={true} style={{width: "100%", height: "400px"}} />

## How do I use OpenAI's built-in tools (Web Search, File Search)?

PromptLayer supports OpenAI's built-in tools from the Responses API, including Web Search and File Search with Vector Stores. These tools enable your prompts to access real-time web information and search through uploaded documents—all without writing custom function definitions.

Learn how to set up and use these tools in our [Tool Calling documentation](/features/prompt-registry/tool-calling#built-in-tools-openai-responses-api).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt