# Source: https://docs.fireworks.ai/tools-sdks/python-client/querying-dedicated-deployments.md

# Querying Dedicated Deployments

> Learn how to connect to and query dedicated deployments that were created outside the SDK

<Warning>
  This SDK documentation applies to version [0.19.20](https://pypi.org/project/fireworks-ai/0.19.20/) and earlier. The Build SDK will be deprecated and replaced with version 1.0.0 of the SDK (see our [changelog](/updates/changelog#2025-11-12) for more details). Please migrate to the new SDK when it becomes available.
</Warning>

When you have dedicated deployments that were created via `firectl` or the Fireworks web UI, you can easily connect to them using the Build SDK to run inference. This is particularly useful when you want to leverage existing infrastructure or when deployments are managed by different teams.

## Prerequisites

Before you begin, make sure you have:

* An existing dedicated deployment running on Fireworks
* The deployment ID or name
* Your Fireworks API key configured

<Note>
  You can find your deployment ID in the [Fireworks dashboard](https://app.fireworks.ai/dashboard/deployments) under the deployments section.
</Note>

## Connecting to an existing deployment

To query an existing dedicated deployment, you simply need to create an `LLM` instance with the `deployment_type="on-demand"` and provide the deployment `id`:

```python  theme={null}
from fireworks import LLM

# Connect to your existing dedicated deployment
llm = LLM(
    model="llama-v3p2-3b-instruct",  # The model your deployment is running
    deployment_type="on-demand",
    id="my-custom-deployment",  # Your deployment ID
)

# Start using the deployment immediately - no .apply() needed
response = llm.chat.completions.create(
    messages=[{"role": "user", "content": "Hello from my dedicated deployment!"}]
)

print(response.choices[0].message.content)
```

<Check>
  Since you're connecting to an existing deployment, you don't need to call `.apply()` - the deployment is already running and ready to serve requests.
</Check>

## Important considerations

### No resource creation

When connecting to existing deployments:

* **No new resources are created** - The SDK connects to your existing deployment
* **No `.apply()` call needed** - The deployment is already active
* **Immediate availability** - You can start making inference calls right away

### Deployment ID requirements

The `id` parameter should match exactly with your existing deployment:

* Use the deployment name/ID as shown in the Fireworks dashboard
* The ID is case-sensitive and must match exactly
* If the deployment doesn't exist, you'll receive an error when making requests

### Model specification

While you need to specify the `model` parameter, it should match the model that your deployment is actually running:

```python  theme={null}
# If your deployment is running Llama 3.2 3B Instruct
llm = LLM(
    model="llama-v3p2-3b-instruct",
    deployment_type="on-demand", 
    id="production-llama-deployment"
)

# If your deployment is running Qwen 2.5 72B Instruct
llm = LLM(
    model="qwen2p5-72b-instruct",
    deployment_type="on-demand",
    id="qwen-high-capacity-deployment"
)
```

## Complete example

Here's a complete example that demonstrates connecting to an existing deployment and using it for a conversation:

<CodeGroup>
  ```python Basic usage theme={null}
  from fireworks import LLM

  # Connect to existing deployment
  llm = LLM(
      model="llama-v3p2-3b-instruct",
      deployment_type="on-demand",
      id="my-existing-deployment",
  )

  # Use OpenAI-compatible chat completions
  response = llm.chat.completions.create(
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "Explain quantum computing in simple terms."}
      ],
      max_tokens=150,
      temperature=0.7
  )

  print(response.choices[0].message.content)
  ```

  ```python Streaming responses theme={null}
  from fireworks import LLM

  llm = LLM(
      model="llama-v3p2-3b-instruct",
      deployment_type="on-demand",
      id="my-existing-deployment",
  )

  # Stream the response
  stream = llm.chat.completions.create(
      messages=[{"role": "user", "content": "Write a short poem about AI."}],
      stream=True,
      max_tokens=100
  )

  for chunk in stream:
      if chunk.choices[0].delta.content is not None:
          print(chunk.choices[0].delta.content, end="")
  ```
</CodeGroup>

## Troubleshooting

### Common issues and solutions

<AccordionGroup>
  <Accordion title="Deployment not found error">
    **Problem**: Getting 404 errors when trying to use the deployment.

    **Solutions**:

    * Verify the deployment ID is correct in the [Fireworks dashboard](https://app.fireworks.ai/dashboard/deployments)
    * Ensure the deployment is in "Running" status
    * Check that you're using the correct Fireworks API key
    * Confirm the deployment belongs to your account/organization
  </Accordion>

  <Accordion title="Model mismatch warnings">
    **Problem**: The model parameter doesn't match the actual deployed model.

    **Solutions**:

    * Check what model your deployment is actually running in the dashboard
    * Update the `model` parameter to match the deployed model
    * If unsure, you can often find the model information in the deployment details
  </Accordion>

  <Accordion title="Authentication errors">
    **Problem**: Getting authentication errors when connecting to the deployment.

    **Solutions**:

    * Verify your `FIREWORKS_API_KEY` environment variable is set correctly
    * Ensure your API key has access to the deployment
    * Check that the deployment belongs to your account or organization
  </Accordion>
</AccordionGroup>

## Next steps

Now that you can connect to existing deployments, you might want to:

* Learn about [fine-tuning models](/tools-sdks/python-client/sdk-basics#fine-tuning-a-model) to create custom deployments
* Explore the [complete SDK tutorial](/tools-sdks/python-client/the-tutorial) for more advanced usage
* Check out the [SDK reference documentation](/tools-sdks/python-client/sdk-reference) for all available options
