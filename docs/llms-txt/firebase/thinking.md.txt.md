# Source: https://firebase.google.com/docs/ai-logic/thinking.md.txt

Gemini 2.5 and later models can use an internal "thinking process" that
significantly improves their reasoning and multi-step planning abilities, making
them highly effective for complex tasks such as coding, advanced mathematics,
and data analysis.

Thinking models offer the following configurations and options:

- **Control the amount of thinking**   

  You can configure how much "thinking" that a model can do. This configuration
  is particularly important if reducing latency or cost is a priority. Also,
  review the [comparison of task difficulties](https://firebase.google.com/docs/ai-logic/thinking#task-complexity) to decide how
  much a model might need its thinking capability.

  Control this configuration either with
  [***thinking levels***](https://firebase.google.com/docs/ai-logic/thinking#thinking-levels)
  *(Gemini 3 and later models)* or with
  [***thinking budgets***](https://firebase.google.com/docs/ai-logic/thinking#thinking-budget) *(Gemini 2.5 models)*.
- **Get thought summaries**   

  You can enable [***thought summaries***](https://firebase.google.com/docs/ai-logic/thinking#thought-summaries) to include with
  the generated response. These summaries are synthesized versions of the
  model's raw thoughts and offer insights into the model's internal reasoning
  process.

- **Handle thought signatures**   

  The Firebase AI Logic SDKs automatically handle
  [***thought signatures***](https://firebase.google.com/docs/ai-logic/thinking#thought-signatures) for you, which ensures that
  the model has access to the thought context from previous turns specifically
  when using function calling.

Make sure to review the [best practices and prompting guidance](https://firebase.google.com/docs/ai-logic/thinking#best-practices)
for using thinking models.

<br />

*** ** * ** ***

## Use a thinking model

**Use a thinking model just like you'd use any other Gemini model.**

To get the most out of thinking models, review
[Best practices \& prompting guidance for using thinking models](https://firebase.google.com/docs/ai-logic/thinking#best-practices)
later on this page.

#### Models that support this capability

Only Gemini 3 and Gemini 2.5 models support this capability.

- `gemini-3.1-pro-preview`
- `gemini-3-pro-image-preview` (aka "Nano Banana Pro")
- `gemini-3.1-flash-image-preview` (aka "Nano Banana 2")
- `gemini-3-flash-preview`
- `gemini-3.1-flash-lite-preview`
- `gemini-2.5-pro`
- `gemini-2.5-flash`
- `gemini-2.5-flash-lite`

> [!NOTE]
> Note the following:
>
> - Gemini 2.5 Flash‑Lite has thinking *disabled by default* . To enable thinking for that model, you need to [set the thinking budget](https://firebase.google.com/docs/ai-logic/thinking#set-thinking-budget) to a supported value. For all other supported models, thinking is *enabled by default*.
> - For Gemini Live API models, Firebase AI Logic does *not yet* support adding a thinking configuration, but that feature is coming soon!

## Best practices \& prompting guidance for using thinking models

We recommend testing your prompt in
[Google AI Studio](https://aistudio.google.com) or
[Vertex AI Studio](https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart)
where you can view the full thinking process. You can identify any areas where
the model may have gone astray so that you can refine your prompts to get more
consistent and accurate responses.

Begin with a general prompt that describes the desired outcome, and observe the
model's initial thoughts on how it determines its response. If the response
isn't as expected, help the model generate a better response by using any of the
following
[prompting techniques](https://cloud.google.com/vertex-ai/generative-ai/docs/thinking#prompting-techniques):

- Provide step-by-step instructions
- Provide several examples of input-output pairs
- Provide guidance for how the output and responses should be phrased and be formatted
- Provide specific verification steps

In addition to prompting, consider using these recommendations:

- Set [system instructions](https://firebase.google.com/docs/ai-logic/system-instructions),
  which are like a "preamble" that you add before the model gets exposed to
  any further instructions from the prompt or end user. They let you steer
  the behavior of the model based on your specific needs and use cases.

- Set a [thinking level](https://firebase.google.com/docs/ai-logic/thinking#thinking-level)
  (or [thinking budget](https://firebase.google.com/docs/ai-logic/thinking#thinking-budget) for Gemini 2.5 models)
  to control how much thinking the model can do. If you set it high, then the
  model can think more, if needed. If you set it lower, then the model won't
  "overthink" its response, and it also reserves more of the total token
  output limit for the actual response and can help reduce latency and cost.

- Enable
  [AI monitoring in the Firebase console](https://firebase.google.com/docs/ai-logic/monitoring#ai-monitoring-in-console)
  to monitor the count of thinking tokens and the latency of your requests
  that have thinking enabled. And if you have
  [thought summaries](https://firebase.google.com/docs/ai-logic/thinking#thought-summaries) enabled, they will display in the
  console where you can inspect the model's detailed reasoning to help you
  debug and refine your prompts.

<br />

*** ** * ** ***

## Control the amount of thinking

You can configure how much "thinking" and reasoning that a model can do before
it returns a response. This configuration is particularly important if reducing
latency or cost is a priority.

Make sure to review the
[comparison of task difficulties](https://firebase.google.com/docs/ai-logic/thinking#task-complexity) to decide how much a model
might need its thinking capability. Here's some high-level guidance:

- Set a lower thinking value for less complex tasks or if reducing latency or cost is a priority for you.
- Set a higher thinking value for more complex tasks.

Control this configuration either with
[***thinking levels***](https://firebase.google.com/docs/ai-logic/thinking#thinking-levels)
*(Gemini 3 and later models)* or with
[***thinking budgets***](https://firebase.google.com/docs/ai-logic/thinking#thinking-budget) *(Gemini 2.5 models)*.

### Thinking levels *(Gemini 3 and later models)*

To control how much thinking a Gemini 3 and later model can do to
generate its response, you can specify a ***thinking level*** for the amount of
thinking tokens that it's allowed to use.
Note the following:

- Gemini 3 and later models always use thinking; you ***cannot*** disable or turn off thinking for these models.
- Gemini 3 and later models always use *dynamic thinking* (the model decides when and how much it thinks up to the configured amount).
- Gemini 3 and later models support *thinking budgets* for backwards-compatibility, but this configuration is *not* recommended. Also, if you set both `thinkingLevel` and `thinkingBudget` in the same config, the request returns an error.

#### Set the thinking level

|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

Set the thinking level in a `GenerationConfig` as part of creating the
`GenerativeModel` instance. The configuration is maintained for the lifetime of
the instance. If you want to use different thinking levels for different
requests, then create `GenerativeModel` instances configured with each level.

Learn about
[supported values for thinking level](https://firebase.google.com/docs/ai-logic/thinking#supported-thinking-level-values)
later in this section.

### Swift

Set the thinking level in a
[`GenerationConfig`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerationConfig)
as part of creating a `GenerativeModel` instance.


    // ...

    // Set the thinking configuration
    // Use a thinking level value appropriate for your model (example value shown here)
    let generationConfig = GenerationConfig(
      thinkingConfig: ThinkingConfig(thinkingLevel: .low)
    )

    // Specify the config as part of creating the `GenerativeModel` instance
    let model = FirebaseAI.firebaseAI(backend: .googleAI()).generativeModel(
      modelName: "GEMINI_3_MODEL_NAME",
      generationConfig: generationConfig
    )

    // ...

### Kotlin

Set the values of the parameters in a
[`GenerationConfig`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig)
as part of creating a `GenerativeModel` instance.


    // ...

    // Set the thinking configuration
    // Use a thinking level value appropriate for your model (example value shown here)
    val generationConfig = generationConfig {
      thinkingConfig = thinkingConfig {
          thinkingLevel = ThinkingLevel.LOW
      }
    }

    // Specify the config as part of creating the `GenerativeModel` instance
    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).generativeModel(
      modelName = "GEMINI_3_MODEL_NAME",
      generationConfig,
    )

    // ...

### Java

Set the values of the parameters in a
[`GenerationConfig`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig)
as part of creating a `GenerativeModel` instance.


    // ...

    // Set the thinking configuration
    // Use a thinking level value appropriate for your model (example value shown here)
    ThinkingConfig thinkingConfig = new ThinkingConfig.Builder()
        .setThinkingLevel(ThinkingLevel.LOW)
        .build();

    GenerationConfig generationConfig = GenerationConfig.builder()
        .setThinkingConfig(thinkingConfig)
        .build();

    // Specify the config as part of creating the `GenerativeModel` instance
    GenerativeModelFutures model = GenerativeModelFutures.from(
            FirebaseAI.getInstance(GenerativeBackend.googleAI())
                    .generativeModel(
                      /* modelName */ "GEMINI_3_MODEL_NAME",
                      /* generationConfig */ generationConfig
                    );
    );

    // ...

### Web

Set the values of the parameters in a
[`GenerationConfig`](https://firebase.google.com/docs/reference/js/ai.generationconfig)
as part of creating a `GenerativeModel` instance.


    // ...

    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    // Set the thinking configuration
    // Use a thinking level value appropriate for your model (example value shown here)
    const generationConfig = {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW
      }
    };

    // Specify the config as part of creating the `GenerativeModel` instance
    const model = getGenerativeModel(ai, { model: "GEMINI_3_MODEL_NAME", generationConfig });

    // ...

### Dart

Set the values of the parameters in a
[`GenerationConfig`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/GenerationConfig-class.html)
as part of creating a `GenerativeModel` instance.


    // ...

    // Set the thinking configuration
    // Use a thinking level value appropriate for your model (example value shown here)
    final thinkingConfig = ThinkingConfig.withThinkingLevel(ThinkingLevel.low);

    final generationConfig = GenerationConfig(
      thinkingConfig: thinkingConfig
    );

    // Specify the config as part of creating the `GenerativeModel` instance
    final model = FirebaseAI.googleAI().generativeModel(
      model: 'GEMINI_3_MODEL_NAME',
      config: generationConfig,
    );

    // ...

### Unity

Set the values of the parameters in a
[`GenerationConfig`](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generation-config)
as part of creating a `GenerativeModel` instance.


    // ...

    // Set the thinking configuration
    // Use a thinking level value appropriate for your model (example value shown here)
    var thinkingConfig = new ThinkingConfig(thinkingLevel: ThinkingLevel.Low);

    var generationConfig = new GenerationConfig(
      thinkingConfig: thinkingConfig
    );

    // Specify the config as part of creating the `GenerativeModel` instance
    var model = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI()).GetGenerativeModel(
      modelName: "GEMINI_3_MODEL_NAME",
      generationConfig: generationConfig
    );

    // ...

#### Supported thinking level values

The following table lists the thinking level values that you can set for each
model by [configuring the model's `thinkingLevel`](https://firebase.google.com/docs/ai-logic/thinking#set-thinking-level).

|   | `MINIMAL` | `LOW` | `MEDIUM` | `HIGH` |
|---|---|---|---|---|
|   | Model uses as few tokens as possible; close to no thinking Low-complexity tasks | Model uses fewer tokens; minimizes latency \& cost Simple tasks and high-throughput tasks | Model uses a balanced approach Moderate complexity tasks | Model uses tokens up to its maximum level Complex prompts that require deep reasoning |
| `gemini-3.1-pro-preview` | No | Yes | Yes | Yes (default) |
| `gemini-3-flash-preview` | Yes | Yes | Yes | Yes (default) |
| `gemini-3.1-flash-lite-preview` | Yes | Yes | Yes | Yes (default) |
| `gemini-3-pro-image-preview` ("Nano Banana Pro") | No | Yes | No | Yes (default) |
| `gemini-3.1-flash-image-preview` ("Nano Banana 2") | Yes | No | No | Yes (default) |

<br />

*** ** * ** ***

### Thinking budgets *(Gemini 2.5 models)*

To control how much thinking a Gemini 2.5 model can do to generate its
response, you can specify a ***thinking budget*** for the amount of thinking
tokens that it's allowed to use.

> [!NOTE]
> **Note:** For Gemini Live API models, Firebase AI Logic does *not yet* support adding a thinking configuration, but that feature is coming soon!

#### Set the thinking budget

|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

Set the thinking budget in a `GenerationConfig` as part of creating the
`GenerativeModel` instance for a Gemini 2.5 model. The configuration is
maintained for the lifetime of the instance. If you want to use different
thinking budgets for different requests, then create `GenerativeModel` instances
configured with each budget.

Learn about
[supported values for thinking budget](https://firebase.google.com/docs/ai-logic/thinking#supported-thinking-budget-values)
later in this section.

### Swift

Set the thinking budget in a
[`GenerationConfig`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerationConfig)
as part of creating a `GenerativeModel` instance.


    // ...

    // Set the thinking configuration
    // Use a thinking budget value appropriate for your model (example value shown here)
    let generationConfig = GenerationConfig(
      thinkingConfig: ThinkingConfig(thinkingBudget: 1024)
    )

    // Specify the config as part of creating the `GenerativeModel` instance
    let model = FirebaseAI.firebaseAI(backend: .googleAI()).generativeModel(
      modelName: "GEMINI_2.5_MODEL_NAME",
      generationConfig: generationConfig
    )

    // ...

### Kotlin

Set the values of the parameters in a
[`GenerationConfig`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig)
as part of creating a `GenerativeModel` instance.


    // ...

    // Set the thinking configuration
    // Use a thinking budget value appropriate for your model (example value shown here)
    val generationConfig = generationConfig {
      thinkingConfig = thinkingConfig {
          thinkingBudget = 1024
      }
    }

    // Specify the config as part of creating the `GenerativeModel` instance
    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).generativeModel(
      modelName = "GEMINI_2.5_MODEL_NAME",
      generationConfig,
    )

    // ...

### Java

Set the values of the parameters in a
[`GenerationConfig`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig)
as part of creating a `GenerativeModel` instance.


    // ...

    // Set the thinking configuration
    // Use a thinking budget value appropriate for your model (example value shown here)
    ThinkingConfig thinkingConfig = new ThinkingConfig.Builder()
        .setThinkingBudget(1024)
        .build();

    GenerationConfig generationConfig = GenerationConfig.builder()
        .setThinkingConfig(thinkingConfig)
        .build();

    // Specify the config as part of creating the `GenerativeModel` instance
    GenerativeModelFutures model = GenerativeModelFutures.from(
            FirebaseAI.getInstance(GenerativeBackend.googleAI())
                    .generativeModel(
                      /* modelName */ "GEMINI_2.5_MODEL_NAME",
                      /* generationConfig */ generationConfig
                    );
    );

    // ...

### Web

Set the values of the parameters in a
[`GenerationConfig`](https://firebase.google.com/docs/reference/js/ai.generationconfig)
as part of creating a `GenerativeModel` instance.


    // ...

    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    // Set the thinking configuration
    // Use a thinking budget value appropriate for your model (example value shown here)
    const generationConfig = {
      thinkingConfig: {
        thinkingBudget: 1024
      }
    };

    // Specify the config as part of creating the `GenerativeModel` instance
    const model = getGenerativeModel(ai, { model: "GEMINI_2.5_MODEL_NAME", generationConfig });

    // ...

### Dart

Set the values of the parameters in a
[`GenerationConfig`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/GenerationConfig-class.html)
as part of creating a `GenerativeModel` instance.


    // ...

    // Set the thinking configuration
    // Use a thinking budget value appropriate for your model (example value shown here)
    final thinkingConfig = ThinkingConfig.withThinkingBudget(1024);

    final generationConfig = GenerationConfig(
      thinkingConfig: thinkingConfig
    );

    // Specify the config as part of creating the `GenerativeModel` instance
    final model = FirebaseAI.googleAI().generativeModel(
      model: 'GEMINI_2.5_MODEL_NAME',
      config: generationConfig,
    );

    // ...

### Unity

Set the values of the parameters in a
[`GenerationConfig`](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generation-config)
as part of creating a `GenerativeModel` instance.


    // ...

    // Set the thinking configuration
    // Use a thinking budget value appropriate for your model (example value shown here)
    var thinkingConfig = new ThinkingConfig(thinkingBudget: 1024);

    var generationConfig = new GenerationConfig(
      thinkingConfig: thinkingConfig
    );

    // Specify the config as part of creating the `GenerativeModel` instance
    var model = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI()).GetGenerativeModel(
      modelName: "GEMINI_2.5_MODEL_NAME",
      generationConfig: generationConfig
    );

    // ...

#### Supported thinking budget values

The following table lists the thinking budget values that you can set for each
model by [configuring the model's `thinkingBudget`](https://firebase.google.com/docs/ai-logic/thinking#set-thinking-budget).

| Model | Default value | Available range for thinking budget || Value to [disable thinking](https://firebase.google.com/docs/ai-logic/thinking#disable-thinking-2-5-models) | Value to [enable dynamic thinking](https://firebase.google.com/docs/ai-logic/thinking#enable-dynamic-thinking-2-5-models) |
| Model | Default value | Value to [disable thinking](https://firebase.google.com/docs/ai-logic/thinking#disable-thinking-2-5-models) | Value to [enable dynamic thinking](https://firebase.google.com/docs/ai-logic/thinking#enable-dynamic-thinking-2-5-models) |
|---|---|---|---|---|---|
|   || **Minimum value** | **Maximum value** |   ||
| Gemini 2.5 Pro | `8,192` | `128` | `32,768` | *cannot be disabled* | `-1` |
| Gemini 2.5 Flash | `8,192` | `1` | `24,576` | `0` | `-1` |
| Gemini 2.5 Flash‑Lite | `0` *(thinking is disabled by default)* | `512` | `24,576` | `0` *(or don't configure thinking budget at all)* | `-1` |

<br />

##### Disable thinking for Gemini 2.5 models

<br />

For some [easier tasks](https://firebase.google.com/docs/ai-logic/thinking#task-complexity), the thinking capability isn't as
necessary, and traditional inference is sufficient. Also, if reducing latency or
cost is a priority, you may not want the model to take any more time or cost
more than necessary to generate a response.

In these situations, you can disable (or turn off) thinking for some models:

- **Gemini 2.5 Pro** : thinking *cannot* be disabled
- **Gemini 2.5 Flash** : disable thinking by setting `thinkingBudget` to `0` tokens
- **Gemini 2.5 Flash‑Lite** : thinking is disabled by default (so don't set `thinkingBudget` explicitly or just set it to `0`)

Note that for all Gemini 3 models, thinking *cannot* be disabled.

<br />

<br />

<br />

##### Enable dynamic thinking for Gemini 2.5 models

<br />

With ***dynamic thinking***, the model decides when and how much it thinks (up
to a max thinking budget, as described below).

- Enable dynamic thinking by setting the `thinkingBudget` to `-1`.
- When dynamic thinking is enabled, the max thinking tokens will always be 8,192 tokens.

Note that all Gemini 3 models always use dynamic thinking.

<br />

<br />

<br />

*** ** * ** ***

### Task complexity for all thinking models

- **Easy tasks --- thinking isn't as necessary**   

  Straightforward requests where complex reasoning isn't required, such as
  fact retrieval or classification. Examples:

  - "Where was DeepMind founded?"
  - "Is this email asking for a meeting or just providing information?"
- **Moderate tasks --- some thinking is likely necessary**   

  Common requests that benefit from a degree of step-by-step processing or
  deeper understanding. Examples:

  - "Create an analogy between photosynthesis and growing up."
  - "Compare and contrast electric cars and hybrid cars."
- **Hard tasks --- maximum thinking may be necessary**   

  Truly complex challenges, such as solving complex math problems or coding
  tasks. These types of tasks require the model to engage its full reasoning
  and planning capabilities, often involving many internal steps before
  providing an answer. Examples:

  - "Solve problem 1 in AIME 2025: Find the sum of all integer bases b \> 9 for which 17b is a divisor of 97b."
  - "Write Python code for a web application that visualizes real-time stock market data, including user authentication. Make it as efficient as possible."

<br />

*** ** * ** ***

## Thought summaries

***Thought summaries*** are synthesized versions of the model's raw thoughts
and offer insights into the model's internal reasoning process.

Here are some reasons to include thought summaries in responses:

- You can display the thought summary in your app's UI or make them accessible
  to your users. The thought summary is returned as a separate part in the
  response so that you have more control over how it's used in your app.

- If you also enable
  [AI monitoring in the Firebase console](https://firebase.google.com/docs/ai-logic/monitoring#ai-monitoring-in-console),
  then thought summaries display in the console where you can inspect the
  model's detailed reasoning to help you debug and refine your prompts.

Here are some key notes about thought summaries:

- Thought summaries are *not* controlled by
  [thinking budgets](https://firebase.google.com/docs/ai-logic/thinking#thinking-budget) (budgets *only* apply to the model's raw
  thoughts). However, if [thinking is disabled](https://firebase.google.com/docs/ai-logic/thinking#disable-thinking), then the
  model won't return a thought summary.

- Thought summaries are considered part of the model's regular generated-text
  response and count as output tokens.

> [!NOTE]
> **Note** : For Gemini Live API models, Firebase AI Logic does *not yet* support enabling thought summaries, but that feature is coming soon!

### Enable thought summaries

|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

You can enable thought summaries by setting `includeThoughts` to true in your
model configuration. You can then access the summary by checking the
`thoughtSummary` field from the response.

Here's an example demonstrating how to enable and retrieve thought summaries
with the response:

### Swift

Enable thought summaries in the
[`GenerationConfig`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerationConfig)
as part of creating a `GenerativeModel` instance.


    // ...

    // Set the thinking configuration
    // Optionally enable thought summaries in the generated response (default is false)
    let generationConfig = GenerationConfig(
      thinkingConfig: ThinkingConfig(includeThoughts: true)
    )

    // Specify the config as part of creating the `GenerativeModel` instance
    let model = FirebaseAI.firebaseAI(backend: .googleAI()).generativeModel(
      modelName: "GEMINI_MODEL_NAME",
      generationConfig: generationConfig
    )

    let response = try await model.generateContent("solve x^2 + 4x + 4 = 0")

    // Handle the response that includes thought summaries
    if let thoughtSummary = response.thoughtSummary {
      print("Thought Summary: \(thoughtSummary)")
    }
    guard let text = response.text else {
      fatalError("No text in response.")
    }
    print("Answer: \(text)")

### Kotlin

Enable thought summaries in the
[`GenerationConfig`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig)
as part of creating a `GenerativeModel` instance.


    // ...

    // Set the thinking configuration
    // Optionally enable thought summaries in the generated response (default is false)
    val generationConfig = generationConfig {
      thinkingConfig = thinkingConfig {
          includeThoughts = true
      }
    }

    // Specify the config as part of creating the `GenerativeModel` instance
    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).generativeModel(
      modelName = "GEMINI_MODEL_NAME",
      generationConfig,
    )

    val response = model.generateContent("solve x^2 + 4x + 4 = 0")

    // Handle the response that includes thought summaries
    response.thoughtSummary?.let {
        println("Thought Summary: $it")
    }
    response.text?.let {
        println("Answer: $it")
    }

### Java

Enable thought summaries in the
[`GenerationConfig`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig)
as part of creating a `GenerativeModel` instance.


    // ...

    // Set the thinking configuration
    // Optionally enable thought summaries in the generated response (default is false)
    ThinkingConfig thinkingConfig = new ThinkingConfig.Builder()
        .setIncludeThoughts(true)
        .build();

    GenerationConfig generationConfig = GenerationConfig.builder()
        .setThinkingConfig(thinkingConfig)
        .build();

    // Specify the config as part of creating the `GenerativeModel` instance
    GenerativeModelFutures model = GenerativeModelFutures.from(
            FirebaseAI.getInstance(GenerativeBackend.googleAI())
                    .generativeModel(
                      /* modelName */ "GEMINI_MODEL_NAME",
                      /* generationConfig */ generationConfig
                    );
    );

    // Handle the response that includes thought summaries
    ListenableFuture responseFuture = model.generateContent("solve x^2 + 4x + 4 = 0");
    Futures.addCallback(responseFuture, new FutureCallback() {
        @Override
        public void onSuccess(GenerateContentResponse response) {
            if (response.getThoughtSummary() != null) {
                System.out.println("Thought Summary: " + response.getThoughtSummary());
            }
            if (response.getText() != null) {
                System.out.println("Answer: " + response.getText());
            }
        }

        @Override
        public void onFailure(Throwable t) {
            // Handle error
        }
    }, MoreExecutors.directExecutor());

### Web

Enable thought summaries in the
[`GenerationConfig`](https://firebase.google.com/docs/reference/js/ai.generationconfig)
as part of creating a `GenerativeModel` instance.


    // ...

    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    // Set the thinking configuration
    // Optionally enable thought summaries in the generated response (default is false)
    const generationConfig = {
      thinkingConfig: {
        includeThoughts: true
      }
    };

    // Specify the config as part of creating the `GenerativeModel` instance
    const model = getGenerativeModel(ai, { model: "GEMINI_MODEL_NAME", generationConfig });

    const result = await model.generateContent("solve x^2 + 4x + 4 = 0");
    const response = result.response;

    // Handle the response that includes thought summaries
    if (response.thoughtSummary()) {
        console.log(`Thought Summary: ${response.thoughtSummary()}`);
    }
    const text = response.text();
    console.log(`Answer: ${text}`);

### Dart

Enable thought summaries in the
[`GenerationConfig`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/GenerationConfig-class.html)
as part of creating a `GenerativeModel` instance.


    // ...

    // Set the thinking configuration
    // Optionally enable thought summaries in the generated response (default is false)
    final thinkingConfig = ThinkingConfig(includeThoughts: true);

    final generationConfig = GenerationConfig(
      thinkingConfig: thinkingConfig
    );

    // Specify the config as part of creating the `GenerativeModel` instance
    final model = FirebaseAI.googleAI().generativeModel(
      model: 'GEMINI_MODEL_NAME',
      generationConfig: generationConfig,
    );

    final response = await model.generateContent('solve x^2 + 4x + 4 = 0');

    // Handle the response that includes thought summaries
    if (response.thoughtSummary != null) {
      print('Thought Summary: ${response.thoughtSummary}');
    }
    if (response.text != null) {
      print('Answer: ${response.text}');
    }

### Unity

Enable thought summaries in the
[`GenerationConfig`](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generation-config)
as part of creating a `GenerativeModel` instance.


    // ...

    // Set the thinking configuration
    // Optionally enable thought summaries in the generated response (default is false)
    var thinkingConfig = new ThinkingConfig(includeThoughts: true);

    var generationConfig = new GenerationConfig(
      thinkingConfig: thinkingConfig
    );

    // Specify the config as part of creating the `GenerativeModel` instance
    var model = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI()).GetGenerativeModel(
      modelName: "GEMINI_MODEL_NAME",
      generationConfig: generationConfig
    );

    var response = await model.GenerateContentAsync("solve x^2 + 4x + 4 = 0");

    // Handle the response that includes thought summaries
    if (response.ThoughtSummary != null) {
        Debug.Log($"Thought Summary: {response.ThoughtSummary}");
    }
    if (response.Text != null) {
        Debug.Log($"Answer: {response.Text}");
    }

<br />

View the response and thought summary

<br />

    # Example Response:
    #     Okay, let's solve the quadratic equation x² + 4x + 4 = 0.
    #     ...
    #     **Answer:**
    #     The solution to the equation x² + 4x + 4 = 0 is x = -2. This is a repeated root (or a root with multiplicity 2).

    # Example Thought Summary:
    #     **My Thought Process for Solving the Quadratic Equation**
    #
    #     Alright, let's break down this quadratic, x² + 4x + 4 = 0. First things first:
    #     it's a quadratic; the x² term gives it away, and we know the general form is
    #     ax² + bx + c = 0.
    #
    #     So, let's identify the coefficients: a = 1, b = 4, and c = 4. Now, what's the
    #     most efficient path to the solution? My gut tells me to try factoring; it's
    #     often the fastest route if it works. If that fails, I'll default to the quadratic
    #     formula, which is foolproof. Completing the square? It's good for deriving the
    #     formula or when factoring is difficult, but not usually my first choice for
    #     direct solving, but it can't hurt to keep it as an option.
    #
    #     Factoring, then. I need to find two numbers that multiply to 'c' (4) and add
    #     up to 'b' (4). Let's see... 1 and 4 don't work (add up to 5). 2 and 2? Bingo!
    #     They multiply to 4 and add up to 4. This means I can rewrite the equation as
    #     (x + 2)(x + 2) = 0, or more concisely, (x + 2)² = 0. Solving for x is now
    #     trivial: x + 2 = 0, thus x = -2.
    #
    #     Okay, just to be absolutely certain, I'll run the quadratic formula just to
    #     double-check. x = [-b ± √(b² - 4ac)] / 2a. Plugging in the values, x = [-4 ±
    #     √(4² - 4 * 1 * 4)] / (2 * 1). That simplifies to x = [-4 ± √0] / 2. So, x =
    #     -2 again - a repeated root. Nice.
    #
    #     Now, let's check via completing the square. Starting from the same equation,
    #     (x² + 4x) = -4. Take half of the b-value (4/2 = 2), square it (2² = 4), and
    #     add it to both sides, so x² + 4x + 4 = -4 + 4. Which simplifies into (x + 2)²
    #     = 0. The square root on both sides gives us x + 2 = 0, therefore x = -2, as
    #      expected.
    #
    #     Always, *always* confirm! Let's substitute x = -2 back into the original
    #     equation: (-2)² + 4(-2) + 4 = 0. That's 4 - 8 + 4 = 0. It checks out.
    #
    #     Conclusion: the solution is x = -2. Confirmed.

<br />

<br />

#### Stream thought summaries

You can also view thought summaries if you choose to stream a response using
`generateContentStream`. This will return rolling, incremental summaries during
the response generation.

### Swift

Enable thought summaries in the
[`GenerationConfig`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerationConfig)
as part of creating a `GenerativeModel` instance.


    // ...

    // Set the thinking configuration
    // Optionally enable thought summaries in the generated response (default is false)
    let generationConfig = GenerationConfig(
      thinkingConfig: ThinkingConfig(includeThoughts: true)
    )

    // Specify the config as part of creating the `GenerativeModel` instance
    let model = FirebaseAI.firebaseAI(backend: .googleAI()).generativeModel(
      modelName: "GEMINI_MODEL_NAME",
      generationConfig: generationConfig
    )

    let stream = try model.generateContentStream("solve x^2 + 4x + 4 = 0")

    // Handle the streamed response that includes thought summaries
    var thoughts = ""
    var answer = ""
    for try await response in stream {
      if let thought = response.thoughtSummary {
        if thoughts.isEmpty {
          print("--- Thoughts Summary ---")
        }
        print(thought)
        thoughts += thought
      }

      if let text = response.text {
        if answer.isEmpty {
          print("--- Answer ---")
        }
        print(text)
        answer += text
      }
    }

### Kotlin

Enable thought summaries in the
[`GenerationConfig`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig)
as part of creating a `GenerativeModel` instance.


    // ...

    // Set the thinking configuration
    // Optionally enable thought summaries in the generated response (default is false)
    val generationConfig = generationConfig {
      thinkingConfig = thinkingConfig {
          includeThoughts = true
      }
    }

    // Specify the config as part of creating the `GenerativeModel` instance
    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).generativeModel(
      modelName = "GEMINI_MODEL_NAME",
      generationConfig,
    )

    // Handle the streamed response that includes thought summaries
    var thoughts = ""
    var answer = ""
    model.generateContentStream("solve x^2 + 4x + 4 = 0").collect { response ->
        response.thoughtSummary?.let {
            if (thoughts.isEmpty()) {
                println("--- Thoughts Summary ---")
            }
            print(it)
            thoughts += it
        }
        response.text?.let {
            if (answer.isEmpty()) {
                println("--- Answer ---")
            }
            print(it)
            answer += it
        }
    }

### Java

Enable thought summaries in the
[`GenerationConfig`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig)
as part of creating a `GenerativeModel` instance.


    // ...

    // Set the thinking configuration
    // Optionally enable thought summaries in the generated response (default is false)
    ThinkingConfig thinkingConfig = new ThinkingConfig.Builder()
        .setIncludeThoughts(true)
        .build();

    GenerationConfig generationConfig = GenerationConfig.builder()
        .setThinkingConfig(thinkingConfig)
        .build();

    // Specify the config as part of creating the `GenerativeModel` instance
    GenerativeModelFutures model = GenerativeModelFutures.from(
            FirebaseAI.getInstance(GenerativeBackend.googleAI())
                    .generativeModel(
                      /* modelName */ "GEMINI_MODEL_NAME",
                      /* generationConfig */ generationConfig
                    );
    );

    // Streaming with Java is complex and depends on the async library used.
    // This is a conceptual example using a reactive stream.
    Flowable responseStream = model.generateContentStream("solve x^2 + 4x + 4 = 0");

    // Handle the streamed response that includes thought summaries
    StringBuilder thoughts = new StringBuilder();
    StringBuilder answer = new StringBuilder();

    responseStream.subscribe(response -> {
        if (response.getThoughtSummary() != null) {
            if (thoughts.length() == 0) {
                System.out.println("--- Thoughts Summary ---");
            }
            System.out.print(response.getThoughtSummary());
            thoughts.append(response.getThoughtSummary());
        }
        if (response.getText() != null) {
            if (answer.length() == 0) {
                System.out.println("--- Answer ---");
            }
            System.out.print(response.getText());
            answer.append(response.getText());
        }
    }, throwable -> {
        // Handle error
    });

### Web

Enable thought summaries in the
[`GenerationConfig`](https://firebase.google.com/docs/reference/js/ai.generationconfig)
as part of creating a `GenerativeModel` instance.


    // ...

    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    // Set the thinking configuration
    // Optionally enable thought summaries in the generated response (default is false)
    const generationConfig = {
      thinkingConfig: {
        includeThoughts: true
      }
    };

    // Specify the config as part of creating the `GenerativeModel` instance
    const model = getGenerativeModel(ai, { model: "GEMINI_MODEL_NAME", generationConfig });

    const result = await model.generateContentStream("solve x^2 + 4x + 4 = 0");

    // Handle the streamed response that includes thought summaries
    let thoughts = "";
    let answer = "";
    for await (const chunk of result.stream) {
      if (chunk.thoughtSummary()) {
        if (thoughts === "") {
          console.log("--- Thoughts Summary ---");
        }
        // In Node.js, process.stdout.write(chunk.thoughtSummary()) could be used
        // to avoid extra newlines.
        console.log(chunk.thoughtSummary());
        thoughts += chunk.thoughtSummary();
      }

      const text = chunk.text();
      if (text) {
        if (answer === "") {
          console.log("--- Answer ---");
        }
        // In Node.js, process.stdout.write(text) could be used.
        console.log(text);
        answer += text;
      }
    }

### Dart

Enable thought summaries in the
[`GenerationConfig`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/GenerationConfig-class.html)
as part of creating a `GenerativeModel` instance.


    // ...

    // Set the thinking configuration
    // Optionally enable thought summaries in the generated response (default is false)
    final thinkingConfig = ThinkingConfig(includeThoughts: true);

    final generationConfig = GenerationConfig(
      thinkingConfig: thinkingConfig
    );

    // Specify the config as part of creating the `GenerativeModel` instance
    final model = FirebaseAI.googleAI().generativeModel(
      model: 'GEMINI_MODEL_NAME',
      generationConfig: generationConfig,
    );

    final responses = model.generateContentStream('solve x^2 + 4x + 4 = 0');

    // Handle the streamed response that includes thought summaries
    var thoughts = '';
    var answer = '';
    await for (final response in responses) {
      if (response.thoughtSummary != null) {
        if (thoughts.isEmpty) {
          print('--- Thoughts Summary ---');
        }
        thoughts += response.thoughtSummary!;
      }
      if (response.text != null) {
        if (answer.isEmpty) {
          print('--- Answer ---');
        }
        answer += response.text!;
      }
    }

### Unity

Enable thought summaries in the
[`GenerationConfig`](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generation-config)
as part of creating a `GenerativeModel` instance.


    // ...

    // Set the thinking configuration
    // Optionally enable thought summaries in the generated response (default is false)
    var thinkingConfig = new ThinkingConfig(includeThoughts: true);

    var generationConfig = new GenerationConfig(
      thinkingConfig: thinkingConfig
    );

    // Specify the config as part of creating the `GenerativeModel` instance
    var model = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI()).GetGenerativeModel(
      modelName: "GEMINI_MODEL_NAME",
      generationConfig: generationConfig
    );

    var stream = model.GenerateContentStreamAsync("solve x^2 + 4x + 4 = 0");

    // Handle the streamed response that includes thought summaries
    var thoughts = "";
    var answer = "";
    await foreach (var response in stream)
    {
        if (response.ThoughtSummary != null)
        {
            if (string.IsNullOrEmpty(thoughts))
            {
                Debug.Log("--- Thoughts Summary ---");
            }
            Debug.Log(response.ThoughtSummary);
            thoughts += response.ThoughtSummary;
        }
        if (response.Text != null)
        {
            if (string.IsNullOrEmpty(answer))
            {
                Debug.Log("--- Answer ---");
            }
            Debug.Log(response.Text);
            answer += response.Text;
        }
    }

<br />

*** ** * ** ***

## Thought signatures

> [!IMPORTANT]
> **Important:** The Firebase AI Logic SDKs automatically handle thought signatures for you. Also note that you can't enable or disable thought signatures (this is a limitation from the underlying Gemini API providers). Thought signatures are considered input tokens.

When using thinking in multi-turn interactions, the model doesn't have access
to thought context from previous turns. However, if you're using
[function calling](https://firebase.google.com/docs/ai-logic/function-calling), you can take advantage of
***thought signatures*** to maintain thought context across turns. Thought
signatures are encrypted representations of the model's internal thought
process, and they're available when using thinking *and* function calling.
Specifically, thought signatures are generated when:

- Thinking is enabled and thoughts are generated.
- The request includes function declarations.

**To take advantage of thought signatures, use function calling as normal.**
The Firebase AI Logic SDKs simplify the process by managing the state
and automatically handling thought signatures for you. The SDKs automatically
pass any generated thought signatures between subsequent `sendMessage` or
`sendMessageStream` calls in a `Chat` session.

<br />

*** ** * ** ***

## Pricing and counting thinking tokens

Thinking tokens use the same [pricing](https://firebase.google.com/docs/ai-logic/pricing)
as text-output tokens. If you enable [thought summaries](https://firebase.google.com/docs/ai-logic/thinking#thought-summaries),
they are considered to be thinking tokens and are priced accordingly.

You can enable
[AI monitoring in the Firebase console](https://firebase.google.com/docs/ai-logic/monitoring#ai-monitoring-in-console)
to monitor the count of thinking tokens for requests that have thinking enabled.

You can get the total number of thinking tokens from the `thoughtsTokenCount`
field in the `usageMetadata` attribute of the response:

### Swift

    // ...

    let response = try await model.generateContent("Why is the sky blue?")

    if let usageMetadata = response.usageMetadata {
      print("Thoughts Token Count: \(usageMetadata.thoughtsTokenCount)")
    }

### Kotlin

    // ...

    val response = model.generateContent("Why is the sky blue?")

    response.usageMetadata?.let { usageMetadata ->
        println("Thoughts Token Count: ${usageMetadata.thoughtsTokenCount}")
    }

### Java

    // ...

    ListenableFuture<GenerateContentResponse> response =
        model.generateContent("Why is the sky blue?");

    Futures.addCallback(response, new FutureCallback<GenerateContentResponse>() {
        @Override
        public void onSuccess(GenerateContentResponse result) {
            String usageMetadata = result.getUsageMetadata();
            if (usageMetadata != null) {
                System.out.println("Thoughts Token Count: " +
                    usageMetadata.getThoughtsTokenCount());
            }
        }

        @Override
        public void onFailure(Throwable t) {
            t.printStackTrace();
        }
    }, executor);

### Web

    // ...

    const response = await model.generateContent("Why is the sky blue?");

    if (response?.usageMetadata?.thoughtsTokenCount != null) {
        console.log(`Thoughts Token Count: ${response.usageMetadata.thoughtsTokenCount}`);
    }

### Dart

    // ...

    final response = await model.generateContent(
      Content.text("Why is the sky blue?"),
    ]);

    if (response?.usageMetadata case final usageMetadata?) {
      print("Thoughts Token Count: ${usageMetadata.thoughtsTokenCount}");
    }

### Unity

    // ...

    var response = await model.GenerateContentAsync("Why is the sky blue?");

    if (response.UsageMetadata != null)
    {
        UnityEngine.Debug.Log($"Thoughts Token Count: {response.UsageMetadata?.ThoughtsTokenCount}");
    }

Learn more about tokens in the
[count tokens guide](https://firebase.google.com/docs/ai-logic/count-tokens).