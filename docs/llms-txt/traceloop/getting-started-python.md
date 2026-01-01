# Source: https://www.traceloop.com/docs/openllmetry/getting-started-python.md

# Python

> Install OpenLLMetry for Python by following these 3 easy steps and get instant monitoring.

You can also check out our full working example of a RAG pipeline with Pinecone [here](https://github.com/traceloop/pinecone-demo).

<Steps>
  <Step title="Install the SDK">
    <Tip>
      Want our AI to do it for you? <a href="" target="_blank" id="vibekit-button" data-vibekit-token="k171j2wgqrg27p7zsr9kgv93kx7jtdmv" rel="noreferrer">Click here</a>
    </Tip>

    Run the following command in your terminal:

    <CodeGroup>
      ```bash pip theme={null}
      pip install traceloop-sdk
      ```

      ```bash poetry theme={null}
      poetry add traceloop-sdk
      ```
    </CodeGroup>

    In your LLM app, initialize the Traceloop tracer like this:

    ```python  theme={null}
    from traceloop.sdk import Traceloop

    Traceloop.init()
    ```

    If you're running this locally, you may want to disable batch sending, so you can see the traces immediately:

    ```python  theme={null}
    Traceloop.init(disable_batch=True)
    ```
  </Step>

  <Step title="Annotate your workflows">
    <Frame>
      <img className="block dark:hidden" src="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-light.png?fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=4fb338092a5577def9eb9098f02cb196" data-og-width="1328" width="1328" data-og-height="955" height="955" data-path="img/workflow-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-light.png?w=280&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=70baa0606922b2fd3e8e0190191e74bc 280w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-light.png?w=560&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=c928d5b7c0e5831ffa2b8937df89abd9 560w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-light.png?w=840&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=ffe71ed1ab9296db92c537e0a7b552c6 840w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-light.png?w=1100&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=f867d9c2a3693e1ab581962476710beb 1100w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-light.png?w=1650&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=e9ea81c7adb1b6b3f1ed5bead5e56498 1650w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-light.png?w=2500&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=cc52f5b2a5925e7e3e72aee1e7731cff 2500w" />

      <img className="hidden dark:block" src="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-dark.png?fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=1059fe0a327bccf355b00ca598537abc" data-og-width="1328" width="1328" data-og-height="955" height="955" data-path="img/workflow-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-dark.png?w=280&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=80f095a842aa8c3d96aee367b4f0f91a 280w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-dark.png?w=560&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=47021b4cec64e8d65cc85a0c2d75bc70 560w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-dark.png?w=840&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=2ef7c4b86b9af56f624376bffff7aa41 840w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-dark.png?w=1100&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=ba9206af514f391cc75488c79367b1c9 1100w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-dark.png?w=1650&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=6ae49fb7c1039b35ee0ba06463a2db08 1650w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/workflow-dark.png?w=2500&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=f1cd87cc3f3944bf8f5ff0936f68fd6b 2500w" />
    </Frame>

    If you have complex workflows or chains, you can annotate them to get a better understanding of what's going on.
    You'll see the complete trace of your workflow on Traceloop or any other dashboard you're using.

    We have a set of [decorators](/openllmetry/tracing/annotations) to make this easier.
    Assume you have a function that renders a prompt and calls an LLM, simply add `@workflow`.

    <Warning>
      The `@aworkflow` decorator is deprecated and will be removed in a future
      version. Use `@workflow` for both synchronous and asynchronous operations.
    </Warning>

    <Tip>
      If you're using a [supported LLM framework](/openllmetry/tracing/supported#frameworks) -
      we'll do that for you. No need to add any annotations to your code.
    </Tip>

    ```python  theme={null}
    from traceloop.sdk.decorators import workflow

    @workflow(name="suggest_answers")
    def suggest_answers(question: str):
      ...

    # Works seamlessly with async functions too
    @workflow(name="summarize")
    async def summarize(long_text: str):
      ...
    ```

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