# Source: https://www.traceloop.com/docs/self-host/troubleshooting.md

# Source: https://www.traceloop.com/docs/openllmetry/troubleshooting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting

> Not seeing anything? Here are some things to check.

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/no-traces-light.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=830b02a7eddb112a017f85e30b8e5a86" data-og-width="3021" width="3021" data-og-height="1806" height="1806" data-path="img/no-traces-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/no-traces-light.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=e607c8c019fa95dbc7566db6acc11728 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/no-traces-light.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=ae2147fd7635aa22297b6845fec0018b 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/no-traces-light.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=32bf19fa6c9288666922b885ff78c6b5 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/no-traces-light.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=6272ccfd6ec8d768e94f8de12244a0a6 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/no-traces-light.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=73761266b120b961af22fa968a0a7012 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/no-traces-light.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=f0c4dede37d07aea86c869b33617cd02 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/no-traces-dark.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=64ae1fc5090ab0d3157454e5c70ab5d9" data-og-width="3024" width="3024" data-og-height="1809" height="1809" data-path="img/no-traces-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/no-traces-dark.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=4784cdbe3c1ed0cc7844cf21c9e57431 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/no-traces-dark.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=8dc500b98f1a4b9cc7445d966900d2b8 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/no-traces-dark.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=0e8dec63dd21b7f75732d3300636210c 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/no-traces-dark.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=5d88cecd86d58c5616c6089f8f139041 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/no-traces-dark.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=25ba180f32e5858ee04ad0d16581e727 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/no-traces-dark.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=e39ec4e70cff3286dd907158b3df88cb 2500w" />
</Frame>

We've all been there. You followed all the instructions, but you're not seeing any traces. Let's fix this.

## 1. Disable batch sending

Sending traces in batch is useful in production, but can be confusing if you're working locally.
Make sure you've [disabled batch sending](/openllmetry/configuration#disable-batch).

<CodeGroup>
  ```python Python theme={null}
  Traceloop.init(disable_batch=True)
  ```

  ```js Typescript / Javascript theme={null}
  Traceloop.init({ disableBatch: true });
  ```
</CodeGroup>

## 2. Check the logs

When Traceloop initializes, it logs a message to the console, specifying the endpoint that it uses.
If you don't see that, you might not be initializing the SDK properly.

> **Traceloop exporting traces to `https://api.traceloop.com`**

## 3. (TS/JS only) Fix known instrumentation issues

If you're using Typescript or Javascript, make sure to import traceloop before any other LLM libraries.
This is because traceloop needs to instrument the libraries you're using, and it can only do that if it's imported first.

```js  theme={null}
import * as traceloop from "@traceloop/traceloop";
import OpenAI from "openai";
...
```

If that doesn't work, you may need to manually instrument the libraries you're using.
See the [manual instrumentation guide](/openllmetry/tracing/js-force-instrumentations) for more details.

```js  theme={null}
import OpenAI from "openai";
import * as LlamaIndex from "llamaindex";

traceloop.initialize({
  appName: "app",
  instrumentModules: {
    openAI: OpenAI,
    llamaIndex: LlamaIndex,
    // Add or omit other modules you'd like to instrument
  },
```

## 4. Is your library supported yet?

Check out [OpenLLMetry](https://github.com/traceloop/openllmetry#readme) or [OpenLLMetry-JS](https://github.com/traceloop/openllmetry-js#readme) README files to see which libraries and versions are currently supported.
Contributions are always welcome! If you want to add support for a library, please open a PR.

## 5. Try outputting traces to the console

Use the `ConsoleExporter` and check if you see traces in the console.

<CodeGroup>
  ```python Python theme={null}
  from opentelemetry.sdk.trace.export import ConsoleSpanExporter

  Traceloop.init(exporter=ConsoleSpanExporter())

  ```

  ```js Typescript / Javascript theme={null}
  import { ConsoleSpanExporter } from "@opentelemetry/sdk-trace-node";

  traceloop.initialize({ exporter: new ConsoleSpanExporter() });
  ```
</CodeGroup>

If you see traces in the console, then you probable haven't configured the exporter properly.
Check the [integration guide](/openllmetry/integrations) again, and make sure you're using the right endpoint and API key.

## 6. Talk to us!

We're here to help.
Reach out any time over
[Slack](https://traceloop.com/slack),
[email](mailto:dev@traceloop.com), and we'd love to assist you.
