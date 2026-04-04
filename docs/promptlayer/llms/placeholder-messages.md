# Source: https://docs.promptlayer.com/features/prompt-registry/placeholder-messages.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Placeholder Messages

Placeholder Messages are a powerful feature that allows you to inject messages into a prompt template. By using the `placeholder` message role, you can define placeholders within your prompt template that can be replaced with full messages at runtime. This complements our standard [template variables](/features/prompt-registry/template-variables) feature, which allows you to insert simple values into your prompts.

This is useful to inject conversation context.

## Creating Placeholder Messages

You can create Placeholder Messages either through the PromptLayer dashboard or programmatically using the `templates.publish` method.

In the dashboard, simply create a new message with the role `placeholder` and provide the desired placeholder content.

<img src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/placeholder.png?fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=014145c927d930f0f7ea33d79427da36" alt="Placeholder Message" data-og-width="1131" width="1131" data-og-height="561" height="561" data-path="images/placeholder.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/placeholder.png?w=280&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=1ce25248a106b34c7ab2aaa3c8455598 280w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/placeholder.png?w=560&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=12e5289f1dc4be046f4c1ad79c9cb56a 560w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/placeholder.png?w=840&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=0143d2211a2d17b549aa4784f47cbc7f 840w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/placeholder.png?w=1100&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=9aaf065d5e5bb9c5cd02cad808f49e15 1100w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/placeholder.png?w=1650&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=2dadd235d371cc2d14952bef9bb88501 1650w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/placeholder.png?w=2500&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=64d9b3aae7900fe9c276daf5696b76f1 2500w" />

## Running a Template with Placeholders

Programmatically, you can include Placeholder Messages when publishing a prompt template:

```python  theme={null}
promptlayer_client.run(
    prompt_name="template-name",
    input_variables={
        "fill_in_message": [
            {
                "role": "user",
                "content": [{"type": "text", "text": "My age is 29"}],
            },
            {
                "role": "assistant",
                "content": [{"type": "text", "text": "What a wonderful age!"}],
            }
        ]
    },
)
```

Passed in messages must confirm to our [prompt blueprint](/quickstart-part-two#prompt-blueprint) format.
