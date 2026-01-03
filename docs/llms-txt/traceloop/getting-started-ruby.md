# Source: https://www.traceloop.com/docs/openllmetry/getting-started-ruby.md

# Ruby

> Install OpenLLMetry for Ruby by following these 3 easy steps and get instant monitoring.

<Warning>This is still in beta. Give us feedback at [dev@traceloop.com](mailto:dev@traceloop.com)</Warning>

<Steps>
  <Step title="Install the SDK">
    Run the following command in your terminal:

    <CodeGroup>
      ```bash gem theme={null}
      gem install traceloop-sdk
      ```

      ```bash bundler theme={null}
      bundle add traceloop-sdk
      ```
    </CodeGroup>

    In your LLM app, initialize the Traceloop tracer like this:

    <Tip>
      If you're using Rails, this needs to be in `config/initializers/traceloop.rb`
    </Tip>

    ```ruby  theme={null}
    require "traceloop/sdk"

    traceloop = Traceloop::SDK::Traceloop.new
    ```
  </Step>

  <Step title="Log your prompts">
    <Frame>
      <img className="block dark:hidden" src="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/single-trace-prompt-light.png?fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=1fb91081386699f120ed74946fc07da6" data-og-width="3024" width="3024" data-og-height="1810" height="1810" data-path="img/single-trace-prompt-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/single-trace-prompt-light.png?w=280&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=5a31f519b941d126be8dceb062697f1b 280w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/single-trace-prompt-light.png?w=560&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=4d42e4bf5fc9e2755454a7cee2ccf8dc 560w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/single-trace-prompt-light.png?w=840&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=abf32cc1326044c8b69f08ac26ca723e 840w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/single-trace-prompt-light.png?w=1100&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=e8b1446efb308a1a4cb66c20d98b6a92 1100w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/single-trace-prompt-light.png?w=1650&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=79ffb6db70b7dc34d676bcbd5ff9a307 1650w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/single-trace-prompt-light.png?w=2500&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=3015a00759d9d307248e9541ca491f1d 2500w" />

      <img className="hidden dark:block" src="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/single-trace-prompt-dark.png?fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=7ab70b34bda2c3c95f3a431b86c76c02" data-og-width="3019" width="3019" data-og-height="1806" height="1806" data-path="img/single-trace-prompt-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/single-trace-prompt-dark.png?w=280&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=0cff7999488d911e2117ec0224ff6947 280w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/single-trace-prompt-dark.png?w=560&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=0d17a103e01d0df03112594b25b8e731 560w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/single-trace-prompt-dark.png?w=840&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=b692de6cec06f0117fbf8bae13dd02b8 840w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/single-trace-prompt-dark.png?w=1100&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=65980060063d479150d7b9c6ef1fb46a 1100w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/single-trace-prompt-dark.png?w=1650&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=28f2aed316df14733190811e6881760d 1650w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/single-trace-prompt-dark.png?w=2500&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=eda1d196fab8a7a3011e6d6200b1ae20 2500w" />
    </Frame>

    For now, we don't automatically instrument libraries on Ruby (as opposed to Python and Javascript).
    This will change in later versions.

    This means that you'll need to manually log your prompts and completions.

    ```ruby  theme={null}
    require "openai"

    client = OpenAI::Client.new

    # This tracks the latency of the call and the response
    traceloop.workflow("joke_generator") do
      traceloop.llm_call(provider="openai", model="gpt-3.5-turbo") do |tracer|
        # Log the prompt
        tracer.log_prompt(user_prompt="Tell me a joke about OpenTelemetry")

        # Or use the OpenAI Format
        # tracer.log_messages([{ role: "user", content: "Tell me a joke about OpenTelemetry" }])

        # Call OpenAI like you normally would
        response = client.chat(
          parameters: {
            model: "gpt-3.5-turbo",
            messages: [{ role: "user", content: "Tell me a joke about OpenTelemetry" }]
          })

        # Pass the response form OpenAI as is to log the completion and token usage
        tracer.log_response(response)
      end
    end
    ```
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