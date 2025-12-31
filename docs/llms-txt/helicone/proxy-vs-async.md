# Source: https://docs.helicone.ai/references/proxy-vs-async.md

# Proxy vs Async Integration

> Compare Helicone's Proxy and Async integration methods. Understand the features, benefits, and use cases for each approach to choose the best fit for your LLM application.

## Quick Compare

There are two ways to interface with Helicone - Proxy and Async. We will help you decide which one is right for you, and the pros and cons with each option.

|                                                                     | Proxy | Async |
| ------------------------------------------------------------------- | ----- | ----- |
| **Easy setup**                                                      | ✅     | ❌     |
| [Prompts](/features/prompts/)                                       | ✅     | ✅     |
| [Prompts Auto Formatting (easier)](/features/prompts)               | ✅     | ❌     |
| [Custom Properties](/features/advanced-usage/custom-properties)     | ✅     | ✅     |
| [Bucket Cache](/features/advanced-usage/caching)                    | ✅     | ❌     |
| [User Metrics](/features/advanced-usage/user-metrics)               | ✅     | ✅     |
| [Retries](/features/advanced-usage/retries)                         | ✅     | ❌     |
| [Custom rate limiting](/features/advanced-usage/custom-rate-limits) | ✅     | ❌     |
| Open-source                                                         | ✅     | ✅     |
| Not on critical path                                                | ❌     | ✅     |
| 0 Propagation Delay                                                 | ❌     | ✅     |
| Negligible Logging Delay                                            | ✅     | ✅     |
| Streaming Support                                                   | ✅     | ✅     |

## Proxy

The primary reason Helicone users choose to integrate with Helicone using Proxy is its **simple integration**.

It's as easy as changing the base URL to point to Helicone, and we'll forward the request to the LLM and return the response to you.

<Frame caption="Proxy: flow of data. ">
  <img src="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/example-proxy.png?fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=90db47b04ce80d9bf27166fa6d68ecb3" alt="Helicone Proxy data flow illustrating simple integration by changing the base URL for instant request forwarding and response handling." data-og-width="1440" width="1440" data-og-height="796" height="796" data-path="images/example-proxy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/example-proxy.png?w=280&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=47eb3a50c2b98f6ae808fb364de56a31 280w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/example-proxy.png?w=560&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=2ed6fd395a62f3107f87816348256cd3 560w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/example-proxy.png?w=840&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=ab6159ff57c495b51cb1bc7385a90a1d 840w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/example-proxy.png?w=1100&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=687896e60b0355a3d2a8a30a28270614 1100w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/example-proxy.png?w=1650&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=10ee2a9e6042b57592e4685e8a2734ec 1650w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/example-proxy.png?w=2500&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=2a4eae7d22f68dfebd95edf2cf55f235 2500w" />
</Frame>

Since the proxy sits on the edge and is the gatekeeper of the requests, you get access to a suite of Gateway tools such as caching, rate limiting, API key management, threat detection, moderations and more.

<Accordion title="Here's a simple example">
  Instead of calling the OpenAI API with `api.openai.com`, you will change the URL to a Helicone dedicated domain `oai.helicone.ai`.

  You can also use the general Gateway URL `gateway.helicone.ai` if Helicone doesn't have a dedicated domain for the provider yet.

  <CodeGroup>
    ```python Dedicated domain example theme={null}
    import openai

    # Set the API base URL to Helicone's proxy
    openai.api_base = "https://oai.helicone.ai/v1"

    # Generate a chat completion request
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Say hi!"}],
        headers={
            "Helicone-Auth": "Bearer [HELICONE_API_KEY]"  # Your Helicone API key
        }
    )

    print(response)
    ```

    ```python Other (Gateway example) theme={null}
    import openai

    openai.api_base = "https://gateway.helicone.ai"  # Set the API base URL to Helicone Gateway
    response = openai.ChatCompletion.create(
        model="[DEPLOYMENT]",
        messages=[{"role": "user", "content": "Say hi!"}],
        headers={
            "Helicone-Auth": "Bearer [HELICONE_API_KEY]",  # Your Helicone API key
            "Helicone-Target-Url": "https://api.lemonfox.ai",  # The target API URL
            "Helicone-Target-Provider": "LemonFox",  # The provider name
        }
    )
    print(response)
    ```
  </CodeGroup>

  <Note>For a detailed documentation, check out [Gateway Integration](https://docs.helicone.ai/getting-started/integration-method/gateway). </Note>
</Accordion>

## Async

Helicone Async allows for a more flexible workflow where the actual logging of the event is **not on the critical path**. This gives some users more confidence that if we are going down or if there is a network issue that it will not affect their application.

[Get started with OpenLLMetry](/getting-started/integration-method/openllmetry).

<Frame caption="Async: flow of data. ">
  <img src="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/example-async.png?fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=ce6f840f6525ddc355937a56e9363042" alt="Helicone Async workflow illustrating non-blocking event logging for improved application stability." data-og-width="1440" width="1440" data-og-height="796" height="796" data-path="images/example-async.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/example-async.png?w=280&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=e9f2717b546ccd021f5999e1228dfecc 280w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/example-async.png?w=560&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=2b83b34d37d6466d32f8cec8c3215954 560w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/example-async.png?w=840&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=d508d435a079b9b7360de611356febc7 840w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/example-async.png?w=1100&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=dc433dfc6b4da999912796637049095e 1100w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/example-async.png?w=1650&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=e9052907de2e63d6630e038a8f497196 1650w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/example-async.png?w=2500&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=f8864dba7d10a8b00446e08685880b87 2500w" />
</Frame>

<Warning>
  The downside is that we cannot offer the same suite of tools as we can with
  the proxy.
</Warning>

## Summary

### When to Use Proxy

* When you need a quick and easy setup.
* If you require Gateway features like custom rate limiting, caching, and retries.
* When you want to use tools that can be instrumented directly into the proxy.

### When to Use Async

* If you prefer the logging of events to be off the critical path, ensuring that network issues do not affect your application.
* When you need zero propagation delay.

<Card title="Integrate with Helicone" href="/getting-started/quick-start#quick-start" icon="flag">
  Choose your LLM provider and get started with Helicone.
</Card>

***

<Accordion title="Need more help?">
  Additional questions or feedback? Reach out to
  [help@helicone.ai](mailto:help@helicone.ai) or [schedule a
  call](https://cal.com/team/helicone/helicone-discovery) with us.
</Accordion>
