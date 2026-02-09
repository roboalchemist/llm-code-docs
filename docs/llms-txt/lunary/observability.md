# Source: https://docs.lunary.ai/docs/features/observability.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Observability

Lunary has powerful observability features that lets you record and analyze your LLM calls.

There are 3 main observability features: analytics, logs and traces.

Analytics and logs are automatically captured as soon as you integrate our SDK.

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="/docs/integrations/python/installation">
    Learn how to install the Python SDK.
  </Card>

  <Card title="JavaScript" icon="js" href="/docs/integrations/javascript/installation">
    Learn how to install the JS SDK.
  </Card>

  <Card title="LangChain" icon="box" href="/docs/integrations/langchain">
    Learn how to integrate with LangChain.
  </Card>
</CardGroup>

## Analytics

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/analytics.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=e2fe9a51b243ebbbc78cb099f6ca374b" alt="Analytics" data-og-width="2054" width="2054" data-og-height="1386" height="1386" data-path="media/docs/features/analytics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/analytics.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=7324ac1ead4d2aa84c4dfb93322927aa 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/analytics.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=85e881f6669fb1e0160f7d3fa5f87ab0 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/analytics.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=c7ac776dd57323254bebfe750cbfb185 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/analytics.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=ce35f69869dca8ad08f6a108b58f2b72 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/analytics.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=c933778159601e587f65523f9239635a 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/analytics.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=87b888fc4865e62b4012febfbe7b3d31 2500w" />

The following metrics are currently automatically captured:

| Metric         | Description                                          |
| -------------- | ---------------------------------------------------- |
| 💰 **Costs**   | Costs incurred by your LLM models                    |
| 📊 **Usage**   | Number of LLM calls made & tokens used               |
| ⏱️ **Latency** | Average latency of LLM calls and agents              |
| ❗ **Errors**   | Number of errors encountered by LLM calls and agents |
| 👥 **Users**   | Usage over time of your top users                    |

## Logs

Lunary allows you to log and inspect your LLM requests and responses.

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/logging.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=efe41ea1e2ea2000c706dc95f66697bb" alt="Logging" data-og-width="2488" width="2488" data-og-height="1498" height="1498" data-path="media/docs/features/logging.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/logging.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=8c04238386813dc1740d108746196e22 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/logging.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=535499789e0fae9eccb55804a05cb509 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/logging.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=10decf25b3b7422830ca7d723d573efb 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/logging.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=1ca894ce736fb0345d36fadf1b1b7cdd 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/logging.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=f832a203689a8eee91d50d24eb8da28c 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/logging.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=a317fc64e1d3d64895fc0d3516aef7a2 2500w" />

Logging is automatic as soon as you integrate our SDK.

## Tracing

Tracing is helpful to debug more complex AI agents and troubleshoot issues.

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/traces.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=3dc5d90a9d39a205179166eafda191de" alt="Feedback tracking" data-og-width="2520" width="2520" data-og-height="1652" height="1652" data-path="media/docs/features/traces.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/traces.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=9b9e1111327b733dc94ce53a45f94aa4 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/traces.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=f7e6437612daabd2d59f65ed21af59f8 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/traces.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=090f8499d49e48e7e0691f4ebfcb9dd8 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/traces.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=4d0fc7de0dbd19e51ba092de97fbce78 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/traces.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=7a23d48481791e272c5b9f028feb5a2c 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/traces.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=2f3df53085c0ac478d0f1dee4392ac17 2500w" />

The easiest way to get started with traces is to use our utility wrappers to automatically track your agents and tools.

### Wrapping Agents

By wrapping an agent, input, outputs and errors are automatically tracked.

Any query ran inside the agent will be tied to the agent.

<Tabs>
  <Tab title="Javascript">
    <Alert title="Agents and tools names" icon={<IconRobot />}>
      Agents & tools are automatically named from the wrapped function's name. You can change the name by passing a 2nd argument `{ name: "custom-name" }` to the `wrapAgent` and `wrapTool` methods.
    </Alert>

    ```js  theme={null}
    // By wrapping your agent's function input, outputs and errors are automatically tracked.
    // Sub tools and logs will be tied to the correct agent.
    const myAgent = lunary.wrapAgent(async function MyAgent(input) {
      // Your agent custom logic
      // ...
    })

    await myAgent("Hello, how are you?")
    ```

    If you prefer to use anonymous functions, make sure to pass a name as a 2nd argument to the `wrapAgent` and `wrapTool` methods.

    ```js  theme={null}
    const myAgent = lunary.wrapAgent(
      (input) => {
        // Your agent custom logic
        // ...
      },
      { name: "MyAgent" }
    )
    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    import lunary

    @lunary.agent()
    def MyAgent(input): # Your agent custom logic # ...
      pass
    ```
  </Tab>
</Tabs>

### Wrapping Chains

Chains are sequences of operations that combine multiple LLM calls, tools, or processing steps into a single workflow. By wrapping chains, you can track the entire sequence of operations as a single unit while still maintaining visibility into each individual step.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    const chain = lunary.wrapChain(async function Chain(input) {
      // Your chain custom logic
      // Call LLM
      // Invoke tool
      // etc...
    })

    await chain('Hello, how are you?')  
    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    @lunary.chain()
    def Chain(input): # Your chain custom logic # ...
      pass
    ```
  </Tab>
</Tabs>

### Wrapping Tools

If your agents use tools, you can wrap them as well to track them.

If a wrapped tool is executed inside a wrapped agent, the tool will be automatically tied to the agent without the need to manually reconcialiate them.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    // By wrapping the tool, input, outputs and errors are automatically tracked.
    // And sub tools / logs will be tied to the correct agent.
    const calculator = lunary.wrapTool(async function Calculator(input) {
      // Your custom logic
      // ...
    })

    await calculator('1 + 2')
    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    import lunary

    @lunary.tool(name='MySuperTool')
    def MyTool(input): # Your tool custom logic # ...
      pass
    ```
  </Tab>
</Tabs>
