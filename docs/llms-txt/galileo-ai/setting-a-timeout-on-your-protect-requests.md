# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-protect/how-to/setting-a-timeout-on-your-protect-requests.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting A Timeout On Your Protect Requests

> Your Protect Rules rely on [Guardrail Metrics](/galileo/gen-ai-studio-products/galileo-protect/how-to/supported-metrics-and-operators). Metrics are calculated using ML models, which can have varying latencies.

### Setting a timeout on your Protect invocations

You can set a timeout on your Protect invocations to ensure that your Protect checks don't add excessive wait times for your users. If a metric exceeds the `timeout` , any Rule and Ruleset that require it also time out and will not trigger.

To configure your timeout setting, set the `timeout` param when calling invoke:

```py  theme={null}
galileo_protect.invoke(payload=...,
                       prioritized_rulesets=...,
                       stage_id=...,
                       timeout=300.0)
```
