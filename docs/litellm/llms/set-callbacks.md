# set callbacks
litellm.success_callback = ["lunary", "mlflow", "langfuse", "helicone"] # log input/output to lunary, mlflow, langfuse, helicone

#openai call
response = completion(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hi 👋 - i'm openai"}])

```

### Track Costs, Usage, Latency for streaming [​](https://docs.litellm.ai/\#track-costs-usage-latency-for-streaming "Direct link to Track Costs, Usage, Latency for streaming")

Use a callback function for this - more info on custom callbacks: [https://docs.litellm.ai/docs/observability/custom\_callback](https://docs.litellm.ai/docs/observability/custom_callback)

```codeBlockLines_e6Vv
import litellm