# Source: https://www.traceloop.com/docs/openllmetry/getting-started-nextjs.md

# Next.js

> Install OpenLLMetry for Next.js by following these 3 easy steps and get instant monitoring.

You can also check out our full working example with Next.js 13 [here](https://github.com/traceloop/openllmetry-nextjs-demo).

<Steps>
  <Step title="Install the SDK">
    <Tip>
      Want our AI to do it for you? <a href="" target="_blank" id="vibekit-button" data-vibekit-token="k174v9knzdnmt51nf4d76fdnjn7jtmt4" rel="noreferrer">Click here</a>
    </Tip>

    Run the following command in your terminal:

    <CodeGroup>
      ```bash npm theme={null}
      npm install @traceloop/node-server-sdk
      ```

      ```bash pnpm theme={null}
      pnpm add @traceloop/node-server-sdk
      ```

      ```bash yarn theme={null}
      yarn add @traceloop/node-server-sdk
      ```
    </CodeGroup>

    <Tabs>
      <Tab title="With Pages Router">
        Create a file named `instrumentation.ts` in the root of your project (i.e., outside of the `pages` or 'app' directory) and add the following code:

        ```ts  theme={null}
        export async function register() {
          if (process.env.NEXT_RUNTIME === "nodejs") {
            await import("./instrumentation.node.ts");
          }
        }
        ```

        <Warning>
          Please note that you might see the following warning: `An import path can only
            end with a '.ts' extension when 'allowImportingTsExtensions' is enabled` To
          resolve it, simply add `"allowImportingTsExtensions": true` to your
          tsconfig.json
        </Warning>

        Create a file named `instrumentation.node.ts` in the root of your project and add the following code:

        ```ts  theme={null}
        import * as traceloop from "@traceloop/node-server-sdk";
        import OpenAI from "openai";
        // Make sure to import the entire module you want to instrument, like this:
        // import * as LlamaIndex from "llamaindex";

        traceloop.initialize({
          appName: "app",
          disableBatch: true,
          instrumentModules: {
            openAI: OpenAI,
            // Add any other modules you'd like to instrument here
            // for example:
            // llamaIndex: LlamaIndex,
          },
        });
        ```

        <Warning>
          Make sure to explictly pass any LLM modules you want to instrument as
          otherwise auto-instrumentation won't work on Next.js. Also make sure to set
          `disableBatch` to `true`.
        </Warning>

        On Next.js v12 and below, you'll also need to add the following to your `next.config.js`:

        ```js  theme={null}
        /** @type {import('next').NextConfig} */
        const nextConfig = {
          experimental: {
            instrumentationHook: true,
          },
        };

        module.exports = nextConfig;
        ```

        <Tip>
          See Next.js [official OpenTelemetry
          docs](https://nextjs.org/docs/pages/building-your-application/optimizing/open-telemetry)
          for more information.
        </Tip>
      </Tab>

      <Tab title="With App Router">
        Install the following packages by running the following commands in your terminal:

        <CodeGroup>
          ```bash npm theme={null}
          npm install --save-dev node-loader
          npm i supports-color@8.1.1
          ```

          ```bash pnpm theme={null}
          pnpm add -D node-loader
          pnpm add supports-color@8.1.1
          ```

          ```bash yarn theme={null}
          yarn add -D node-loader
          yarn add supports-color@8.1.1
          ```
        </CodeGroup>

        Edit your `next.config.js` file and add the following webpack configuration:

        ```js  theme={null}
        const nextConfig = {
        webpack: (config, { isServer }) => {
          config.module.rules.push({
            test: /\.node$/,
            loader: "node-loader",
          });
          if (isServer) {
            config.ignoreWarnings = [{ module: /opentelemetry/ }];
          }
          return config;
        },
        };
        ```

        On every app API route you want to instrument, add the following code at the top of the file:

        ```ts  theme={null}
        import * as traceloop from "@traceloop/node-server-sdk";
        import OpenAI from "openai";
        // Make sure to import the entire module you want to instrument, like this:
        // import * as LlamaIndex from "llamaindex";

        traceloop.initialize({
          appName: "app",
          disableBatch: true,
          instrumentModules: {
            openAI: OpenAI,
            // Add any other modules you'd like to instrument here
            // for example:
            // llamaIndex: LlamaIndex,
          },
        });
        ```

        <Tip>
          See Next.js [official OpenTelemetry
          docs](https://nextjs.org/docs/app/building-your-application/optimizing/open-telemetry)
          for more information.
        </Tip>
      </Tab>
    </Tabs>
  </Step>

  <Step title="Annotate your workflows">
    <Frame>
      <img className="block dark:hidden" src="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-light.png?fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=4fb338092a5577def9eb9098f02cb196" data-og-width="1328" width="1328" data-og-height="955" height="955" data-path="img/workflow-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-light.png?w=280&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=70baa0606922b2fd3e8e0190191e74bc 280w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-light.png?w=560&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=c928d5b7c0e5831ffa2b8937df89abd9 560w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-light.png?w=840&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=ffe71ed1ab9296db92c537e0a7b552c6 840w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-light.png?w=1100&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=f867d9c2a3693e1ab581962476710beb 1100w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-light.png?w=1650&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=e9ea81c7adb1b6b3f1ed5bead5e56498 1650w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-light.png?w=2500&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=cc52f5b2a5925e7e3e72aee1e7731cff 2500w" />

      <img className="hidden dark:block" src="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-dark.png?fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=1059fe0a327bccf355b00ca598537abc" data-og-width="1328" width="1328" data-og-height="955" height="955" data-path="img/workflow-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-dark.png?w=280&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=80f095a842aa8c3d96aee367b4f0f91a 280w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-dark.png?w=560&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=47021b4cec64e8d65cc85a0c2d75bc70 560w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-dark.png?w=840&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=2ef7c4b86b9af56f624376bffff7aa41 840w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-dark.png?w=1100&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=ba9206af514f391cc75488c79367b1c9 1100w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-dark.png?w=1650&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=6ae49fb7c1039b35ee0ba06463a2db08 1650w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-dark.png?w=2500&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=f1cd87cc3f3944bf8f5ff0936f68fd6b 2500w" />
    </Frame>

    If you have complex workflows or chains, you can annotate them to get a better understanding of what's going on.
    You'll see the complete trace of your workflow on Traceloop or any other dashboard you're using.

    We have a set of [methods and decorators](/openllmetry/tracing/annotations) to make this easier.
    Assume you have a function that renders a prompt and calls an LLM, simply wrap it in a `withWorkflow()` function call.

    We also have compatible Typescript decorators for class methods which are more convenient.

    <Tip>
      If you're using a [supported LLM framework](/openllmetry/tracing/supported#frameworks) -
      we'll do that for you. No need to add any annotations to your code.
    </Tip>

    <CodeGroup>
      ```js Functions (async / sync) theme={null}
      async function suggestAnswers(question: string) {
        return await withWorkflow({ name: "suggestAnswers" }, () => {
          ...
        });
      }
      ```

      ```js Class Methods theme={null}
      class MyLLM {
        @traceloop.workflow({ name: "suggest_answers" })
        async suggestAnswers(question: string) {
          ...
        }
      }
      ```
    </CodeGroup>

    For more information, see the [dedicated section in the docs](/openllmetry/tracing/annotations).
  </Step>

  <Step title="Configure trace exporting">
    Lastly, you'll need to configure where to export your traces.
    The 2 environment variables controlling this are `TRACELOOP_API_KEY` and `TRACELOOP_BASE_URL`.

    For Traceloop, read on. For other options, see [Exporting](/openllmetry/integrations/introduction).

    ### Using Traceloop Cloud

    <Note>
      You need an API key to send traces to Traceloop.
      [Generate one in Settings](https://app.traceloop.com/settings/api-keys) by selecting
      a project and environment, then click **Generate API key**.

      ⚠️ **Important:** Copy the key immediately - it won't be shown again after you close or reload the page.

      [Detailed instructions →](/settings/managing-api-keys)
    </Note>

    Set the API key as an environment variable in your app named `TRACELOOP_API_KEY`:

    ```bash  theme={null}
    export TRACELOOP_API_KEY=your_api_key_here
    ```

    Done! You'll get instant visibility into everything that's happening with your LLM.
    If you're calling a vector DB, or any other external service or database, you'll also see it in the Traceloop dashboard.

    <Tip>
      **Not seeing traces?** Make sure you're viewing the correct project and environment in the
      dashboard that matches your API key. See [Troubleshooting](/settings/managing-api-keys#troubleshooting).
    </Tip>
  </Step>
</Steps>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://www.traceloop.com/docs/llms.txt