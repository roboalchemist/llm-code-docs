# Source: https://docs.fireworks.ai/faq-new/models-inference/how-to-check-if-a-model-is-available-on-serverless.md

# How to check if a model is available on serverless?

## Web UI

Go to [https://app.fireworks.ai/models?filter=LLM\&serverless=true](https://app.fireworks.ai/models?filter=LLM\&serverless=true)

## Programmatically

You can use the
[`is_available_on_serverless`](/tools-sdks/python-client/sdk-reference#is-available-on-serverless)
method on the [LLM](/tools-sdks/python-client/sdk-reference#llm) object in our
[Build SDK](/tools-sdks/python-client/sdk-introduction) to check if a model is
available on serverless.

```python  theme={null}
llm = LLM(model="llama4-maverick-instruct-basic", deployment_type="auto")
print(llm.is_available_on_serverless()) # True

llm = LLM(model="qwen2p5-7b-instruct", deployment_type="auto")
# Error will be raised saying: "LLM(id=...) must be provided when deployment_strategy is on-demand"
# Which means the model is not available on serverless if the
# deployment_strategy was resolved as "on-demand" when the deployment_type was
# "auto"
```
