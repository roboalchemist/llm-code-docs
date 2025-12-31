# Source: https://dev.writer.com/home/models-overview.md

# Choose a model

> Compare Writer's Palmyra models with external provider models to select the best fit for your AI agents

This guide helps you choose between Writer's Palmyra models and external provider models when building agents in AI Studio. Both options are available through the [Models page](https://app.writer.com/aistudio) in AI Studio.

## Palmyra models

Writer's [Palmyra models](/home/models) are pre-configured and immediately available in AI Studio. The Palmyra family includes:

| Model                                             | Best for                                      |
| ------------------------------------------------- | --------------------------------------------- |
| [Palmyra X5](/home/models#palmyra-x5)             | General-purpose tasks with advanced reasoning |
| [Palmyra X4](/home/models#palmyra-x4)             | Complex tasks requiring extended context      |
| [Palmyra Med](/home/models#palmyra-med)           | Healthcare and medical applications           |
| [Palmyra Fin](/home/models#palmyra-fin)           | Financial services and analysis               |
| [Palmyra Creative](/home/models#palmyra-creative) | Marketing content and creative writing        |
| [Palmyra Vision](/home/models#palmyra-vision)     | Image and video understanding                 |

For detailed capabilities, context windows, and use cases, see [Palmyra models](/home/models). For pricing, see [Palmyra pricing](/home/pricing).

## External models

You can also add models from external providers like AWS Bedrock to use alongside Palmyra models. External models require credential configuration but provide access to models like Claude, Llama, and Mistral.

| Provider    | Status      | Setup guide                                     |
| ----------- | ----------- | ----------------------------------------------- |
| AWS Bedrock | Available   | [Configure AWS Bedrock](/providers/aws-bedrock) |
| HuggingFace | Coming soon | —                                               |
| Nvidia      | Coming soon | —                                               |

For information about adding and managing external models, see [Add external models](/home/external-models).

## Compare Palmyra and external models

Consider the following factors when selecting models for your agents:

| Consideration           | Palmyra models                                  | External models                       |
| ----------------------- | ----------------------------------------------- | ------------------------------------- |
| **Setup**               | Pre-configured, immediately available           | Requires credential configuration     |
| **Optimization**        | Optimized for Writer platform                   | Varies by provider                    |
| **Specialized domains** | Palmyra Med (healthcare), Palmyra Fin (finance) | General-purpose models                |
| **Compliance**          | Writer-managed compliance                       | You manage provider compliance        |
| **Billing**             | Unified billing through Writer                  | Billed by provider (for example, AWS) |
| **Cost visibility**     | Included in Writer dashboard                    | Tracked in Writer + provider billing  |

### When to use Palmyra models

Palmyra models are the best choice when you need:

* **Domain-specific capabilities**: Palmyra Med for healthcare, Palmyra Fin for finance, or Palmyra Creative for marketing content
* **Simplified billing**: All usage appears on your Writer invoice
* **Writer platform features**: Optimized integration with Knowledge Graphs and other Writer capabilities
* **Compliance simplicity**: Writer manages model compliance and security

### When to use external models

External models are the best choice when you need:

* **Existing provider agreements**: You have AWS credits or enterprise agreements with cloud providers
* **Specific model access**: You need a particular model not available through Writer (for example, Claude, Llama, or Mistral on Bedrock)
* **Provider-specific compliance**: Your organization mandates specific cloud providers for AI workloads
* **Model comparison**: You want to evaluate performance across different model providers

For information about adding and managing external models, see [Add external models](/home/external-models).

## Use models in your applications

Once models are available in AI Studio, you can use them in Agent Builder, no-code apps, or via the API.

### Agent Builder and no-code agents

In [Agent Builder](/home/agent-builder) and [no-code chat apps](/no-code/introduction), select any available model from the **Model** dropdown. Both Palmyra models and any external models your team has access to appear in the list.

### API usage

Use the [List models](/api-reference/completion-api/list-models) endpoint to see all models available to your organization. You can then pass the model ID in any request that supports the `model` parameter.

<CodeGroup>
  ```bash cURL theme={null}
  curl https://api.writer.com/v1/models \
    -H "Authorization: Bearer $WRITER_API_KEY"
  ```

  ```python Python theme={null}
  from writerai import Writer

  client = Writer()

  models = client.models.list()
  for model in models.models:
      print(model.id)
  ```

  ```javascript JavaScript theme={null}
  import Writer from "writer-sdk";

  const client = new Writer();

  const models = await client.models.list();
  models.models.forEach(model => console.log(model.id));
  ```
</CodeGroup>

To use a model, pass its ID to any completion endpoint. External models use the same API as Palmyra models—just swap the model ID:

<CodeGroup>
  ```bash cURL theme={null}
  curl https://api.writer.com/v1/chat/completions \
    -H "Authorization: Bearer $WRITER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "anthropic.claude-3-sonnet-20240229-v1:0",
      "messages": [{"role": "user", "content": "Hello!"}]
    }'
  ```

  ```python Python theme={null}
  from writerai import Writer

  client = Writer()

  response = client.chat.chat(
      model="anthropic.claude-3-sonnet-20240229-v1:0",
      messages=[{"role": "user", "content": "Hello!"}]
  )
  print(response.choices[0].message.content)
  ```

  ```javascript JavaScript theme={null}
  import Writer from "writer-sdk";

  const client = new Writer();

  const response = await client.chat.chat({
    model: "anthropic.claude-3-sonnet-20240229-v1:0",
    messages: [{ role: "user", content: "Hello!" }]
  });
  console.log(response.choices[0].message.content);
  ```
</CodeGroup>

## Next steps

* [Add external models](/home/external-models): Configure external models from providers like AWS Bedrock
* [Palmyra models](/home/models): Explore Writer's Palmyra model capabilities


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://dev.writer.com/llms.txt