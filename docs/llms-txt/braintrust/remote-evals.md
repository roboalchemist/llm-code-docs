# Source: https://braintrust.dev/docs/evaluate/remote-evals.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Run remote evaluations

> Run evaluations on your own infrastructure

Remote evals let you run evaluations on your own infrastructure while using Braintrust's playground for iteration, comparison, and analysis. Your evaluation code runs on your servers or local machine, and the Braintrust playground sends parameters and receives results through a simple HTTP interface.

Use remote evals when your evaluation requires:

* **Agentic workflows**: Multi-step agent flows or complex task logic that goes beyond a single prompt.
* **Custom infrastructure**: Access to internal APIs, databases, or services that can't run in the cloud.
* **Specific runtime environments**: Custom dependencies, system libraries, or environment configurations.
* **Security or compliance requirements**: Data that must remain on your infrastructure.
* **Long-running evaluations**: Complex processing that exceeds typical execution timeouts.

<Note>
  If your evaluation can run in the Braintrust playground, you don't need remote evals.
</Note>

## How it works

1. Write an `Eval()` with parameters that define runtime configuration options.
2. Run your eval locally with the `--dev` flag to expose an HTTP endpoint.
3. Configure the endpoint URL in your Braintrust project settings.
4. Use the remote eval in the playground. Parameters appear as UI controls.
5. When you run the eval, Braintrust sends parameters to your endpoint and displays results.

The playground handles dataset management, scoring, comparison, and visualization while your code handles the task execution.

## Set up a remote eval

A remote eval looks like a standard `Eval()` call with a `parameters` field that defines configurable options. These parameters become UI controls in the playground. See [Remote eval parameters](#remote-eval-parameters) for details on parameter types and syntax.

<CodeGroup dropdown>
  ```typescript remote.eval.ts theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Levenshtein } from "autoevals";
  import { Eval, initDataset, wrapOpenAI } from "braintrust";
  import OpenAI from "openai";
  import { z } from "zod";

  const client = wrapOpenAI(new OpenAI());

  Eval("Simple eval", {
    data: initDataset("local dev", { dataset: "sanity" }),
    task: async (input, { parameters }) => {
      const promptInput = parameters.prefix
        ? `${parameters.prefix}: ${input}`
        : input;

      const completion = await client.chat.completions.create(
        parameters.main.build({
          input: promptInput,
        }),
      );
      return completion.choices[0].message.content ?? "";
    },
    scores: [Levenshtein],
    parameters: {
      main: {
        type: "prompt",
        name: "Main prompt",
        description: "This is the main prompt",
        default: {
          messages: [
            {
              role: "user",
              content: "{{input}}",
            },
          ],
          model: "gpt-4o",
        },
      },
      prefix: z
        .string()
        .describe("Optional prefix to prepend to input")
        .default(""),
    },
  });
  ```

  ```python remote_eval.py theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import openai
  from autoevals import Levenshtein
  from braintrust import Eval, init_dataset, wrap_openai

  client = wrap_openai(openai.AsyncOpenAI())


  async def task(input, hooks):
      parameters = hooks.parameters

      prefix = parameters.get("prefix", "")
      prompt_input = f"{prefix}: {input}" if prefix else input

      completion = await client.chat.completions.create(
          **parameters["main"].build(input=prompt_input)
      )

      return completion.choices[0].message.content or ""


  Eval(
      "Simple eval",
      data=init_dataset("local dev", "sanity"),
      task=task,
      scores=[Levenshtein],
      parameters={
          "main": {
              "type": "prompt",
              "name": "Main prompt",
              "description": "This is the main prompt",
              "default": {
                  "prompt": {
                      "type": "chat",
                      "messages": [{"role": "user", "content": "{{input}}"}],
                  },
                  "options": {"model": "gpt-4o"},
              },
          },
          "prefix": {
              "type": "string",
              "description": "Optional prefix to prepend to input",
              "default": "",
          },
      },
  )
  ```

  ```java SimpleRemoteEval.java theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  // Requires Braintrust Java SDK v0.2.1+
  import com.openai.client.OpenAIClient;
  import com.openai.client.okhttp.OpenAIOkHttpClient;
  import com.openai.models.ChatModel;
  import com.openai.models.chat.completions.ChatCompletionCreateParams;
  import dev.braintrust.Braintrust;
  import dev.braintrust.devserver.Devserver;
  import dev.braintrust.devserver.RemoteEval;
  import dev.braintrust.eval.Scorer;
  import dev.braintrust.instrumentation.openai.BraintrustOpenAI;
  import java.util.List;

  class SimpleRemoteEval {
      public static void main(String[] args) throws Exception {
          var braintrust = Braintrust.get();
          var openTelemetry = braintrust.openTelemetryCreate();
          OpenAIClient client = BraintrustOpenAI.wrapOpenAI(openTelemetry, OpenAIOkHttpClient.fromEnv());

          dev.braintrust.devserver.RemoteEval<String, String> eval =
                  dev.braintrust.devserver.RemoteEval.<String, String>builder()
                          .name("Simple eval")
                          .taskFunction(
                                  input -> {
                                      var request =
                                              ChatCompletionCreateParams.builder()
                                                      .model(ChatModel.GPT_4O)
                                                      .addUserMessage(input)
                                                      .build();

                                      var response = client.chat().completions().create(request);
                                      return response.choices()
                                              .get(0)
                                              .message()
                                              .content()
                                              .orElse("");
                                  })
                          .scorers(
                                  List.of(
                                          Scorer.of(
                                                  "accuracy",
                                                  (expected, output) ->
                                                          output.equals(expected) ? 1.0 : 0.0)))
                          .build();

          Devserver devserver =
                  Devserver.builder()
                          .config(braintrust.config())
                          .registerEval(eval)
                          .host("localhost")
                          .port(8300)
                          .build();

          Runtime.getRuntime()
                  .addShutdownHook(
                          new Thread(
                                  () -> {
                                      System.out.println("Shutting down...");
                                      devserver.stop();
                                      System.out.flush();
                                      System.err.flush();
                                  }));

          System.out.println("Starting Braintrust dev server on http://localhost:8300");
          devserver.start();
      }
  }
  ```
</CodeGroup>

### Remote eval parameters

Parameters define runtime configuration that users can modify in the playground without changing code. They appear as form controls in the UI.

When implementing remote evals, the parameter system works the same way across languages but uses different syntax:

| Feature               | TypeScript                                                                                                                    | Python                                                                                                                 | Java                                                                                                              |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Parameter types**   | `type: "prompt"` for LLM prompts<br />`z.string()`, `z.boolean()`, `z.number()`, `z.array()`, `z.object()` with `.describe()` | `type: "prompt"` for LLM prompts<br />Dictionary with `type: "string"`, `"boolean"`, `"number"`, `"array"`, `"object"` | `type: "prompt"` for LLM prompts<br />`Map` with `type: "string"`, `"boolean"`, `"number"`, `"array"`, `"object"` |
| **Type definition**   | Zod schemas with chained methods                                                                                              | Dictionary with `type`, `description`, `default` fields                                                                | Map with `type`, `description`, `default` fields                                                                  |
| **Parameter access**  | Direct property access: `parameters.prefix`                                                                                   | Dictionary access: `parameters["prefix"]` or `parameters.get("prefix")`                                                | Map access: `parameters.get("prefix")` or `parameters.getOrDefault("prefix", default)`                            |
| **Prompt parameters** | `type: "prompt"` with `messages` array directly in `default`                                                                  | `type: "prompt"` with nested `prompt.messages` and `options` objects                                                   | `type: "prompt"` with nested `prompt.messages` and `options` objects                                              |
| **Prompt usage**      | `parameters.main.build({ input: value })`                                                                                     | `**parameters["main"].build(input=value)`                                                                              | `parameters.get("main").build(Map.of("input", value))`                                                            |
| **Async handling**    | `async`/`await` with promises                                                                                                 | `async`/`await` with coroutines                                                                                        | Synchronous or `CompletableFuture`                                                                                |

When your remote eval runs, Braintrust sends the configured parameter values through the `parameters` object in your task function.

## Expose a remote eval

To make your eval accessible to Braintrust, run it with the `--dev` flag to start a local server:

<Tabs>
  <Tab title="TypeScript">
    Run `npx braintrust eval path/to/eval.ts --dev` to start the dev server at `http://localhost:8300`.
  </Tab>

  <Tab title="Python">
    Run `braintrust eval path/to/eval.py --dev` to start the dev server at `http://localhost:8300`.
  </Tab>

  <Tab title="Java">
    Run `braintrust eval RemoteEval --dev` to start the dev server at `http://localhost:8300`.
  </Tab>
</Tabs>

You can configure the host and port:

* `--dev-host DEV_HOST`: The host to bind the dev server to. Defaults to `localhost`. Set to `0.0.0.0` to bind to all interfaces (be cautious about security when exposing beyond localhost).
* `--dev-port DEV_PORT`: The port to bind the dev server to. Defaults to `8300`.

Once running, your eval exposes an HTTP endpoint that Braintrust can connect to. Keep this process running while using the remote eval in the playground.

## Configure remote eval sources

To add remote eval endpoints beyond localhost, configure them at the project level:

1. In your project, go to **<Icon icon="settings-2" /> Configuration** > **<Icon icon="unplug" /> Remote evals**.
2. Select **<Icon icon="plus" /> Remote eval source**.
3. Enter the name and URL of your remote eval server.
4. Select **Create remote eval source**.

All team members with access to the project can now use this remote eval in their playgrounds.

## Run a remote eval from a playground

After exposing your eval and configuring it in your project, you can use it in any playground:

1. In a playground, select **<Icon icon="plus" /> Task**.
2. Select **<Icon icon="unplug" /> Remote eval** from the task type list.
3. Choose your eval from the available sources (localhost or configured remote URLs).
4. Configure parameters using the UI controls that were defined in your `parameters` object.
5. Run the evaluation.

Braintrust sends your parameters to the remote endpoint and displays results. You can run multiple instances of the same remote eval side-by-side with different parameters to compare results.

## Demo

This video walks through exposing a remote eval to Braintrust and using it in a playground.

<video controls className="w-full aspect-video rounded-xl" poster="/docs/images/guides/remote-evals/remote-evals-tutorial.png" src="https://mintcdn.com/braintrust/ra--46HEM6v2rXpA/images/guides/remote-evals/remote-evals-tutorial.mp4?fit=max&auto=format&n=ra--46HEM6v2rXpA&q=85&s=612eb61cd9634ba9263c5a7b7ffb54e0" data-path="images/guides/remote-evals/remote-evals-tutorial.mp4" />

## Limitations

* The dataset defined in your remote eval is ignored. Datasets are managed through the playground.
* Scorers defined in remote evals are concatenated with playground scorers.

## Next steps

* [Use playgrounds](/evaluate/playgrounds) to compare and analyze results.
* [Write scorers](/evaluate/write-scorers) to evaluate outputs.
* [Run evaluations](/evaluate/run-evaluations) programmatically.
