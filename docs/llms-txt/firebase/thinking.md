# Source: https://firebase.google.com/docs/ai-logic/thinking.md.txt

<br />

Gemini 3andGemini 2.5models can use an internal "thinking process" that significantly improves their reasoning and multi-step planning abilities, making them highly effective for complex tasks such as coding, advanced mathematics, and data analysis.

Thinking models offer the following configurations and options:

- [**Thinking budget**](https://firebase.google.com/docs/ai-logic/thinking#thinking-budget): You can configure how much "thinking" that a model can do using a***thinking budget*** . This configuration is particularly important if reducing latency or cost is a priority. Also, review the[comparison of task difficulties](https://firebase.google.com/docs/ai-logic/thinking#task-complexity)to decide how much a model might need its thinking capability.

- [**Thought summaries**](https://firebase.google.com/docs/ai-logic/thinking#thought-summaries): You can enable***thought summaries***to include with the generated response. These summaries are synthesized versions of the model's raw thoughts and offer insights into the model's internal reasoning process.

- [**Thought signatures**](https://firebase.google.com/docs/ai-logic/thinking#thought-signatures): TheFirebase AI LogicSDKs automatically handle***thought signatures***for you, which ensures that the model has access to the thought context from previous turns specifically when using function calling.

Make sure to review the[best practices and prompting guidance](https://firebase.google.com/docs/ai-logic/thinking#best-practices)for using thinking models.
| **Note:** Firebase AI Logicdoes*not* yet support***thinking levels*** for theGemini 3models, but that feature is coming soon!  
| In the meantime, you set[***thinking budgets***](https://firebase.google.com/docs/ai-logic/thinking#thinking-budget).

## Use a thinking model

**Use a thinking model just like you'd use any otherGeminimodel** (initialize your chosenGemini APIprovider, create a`GenerativeModel`instance, etc.). These models can be used for text or code generation tasks, like[generating structured output](https://firebase.google.com/docs/ai-logic/generate-structured-output)or analyzing multimodal input (like[images](https://firebase.google.com/docs/ai-logic/analyze-images),[video](https://firebase.google.com/docs/ai-logic/analyze-video),[audio](https://firebase.google.com/docs/ai-logic/analyze-audio), or[PDFs](https://firebase.google.com/docs/ai-logic/analyze-documents)). You can even use thinking models when you're streaming the output.

#### Models that support this capability

OnlyGemini 3andGemini 2.5models support this capability.

- `gemini-3-pro-preview`
- `gemini-3-flash-preview`
- `gemini-3-pro-image-preview`(aka "nano banana pro")
- `gemini-2.5-pro`
- `gemini-2.5-flash`
- `gemini-2.5-flash-lite`

| Note the following:
|
| - Gemini 2.5 FlashâLitehas thinking*disabled by default* . To enable thinking for that model, you need to[set the thinking budget](https://firebase.google.com/docs/ai-logic/thinking#set-thinking-budget)to a supported value. For all other supported models, thinking is*enabled by default*.
| - ForGemini Live APImodels,Firebase AI Logicdoes*not yet*support adding a thinking configuration, but that feature is coming soon!

## Best practices \& prompting guidance for using thinking models

We recommend testing your prompt in[Google AI Studio](https://aistudio.google.com)or[Vertex AI Studio](https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart)where you can view the full thinking process. You can identify any areas where the model may have gone astray so that you can refine your prompts to get more consistent and accurate responses.

Begin with a general prompt that describes the desired outcome, and observe the model's initial thoughts on how it determines its response. If the response isn't as expected, help the model generate a better response by using any of the following[prompting techniques](https://cloud.google.com/vertex-ai/generative-ai/docs/thinking#prompting-techniques):

- Provide step-by-step instructions
- Provide several examples of input-output pairs
- Provide guidance for how the output and responses should be phrased and be formatted
- Provide specific verification steps

In addition to prompting, consider using these recommendations:

- Set[system instructions](https://firebase.google.com/docs/ai-logic/system-instructions), which are like a "preamble" that you add before the model gets exposed to any further instructions from the prompt or end user. They let you steer the behavior of the model based on your specific needs and use cases.

- Set a[thinking budget](https://firebase.google.com/docs/ai-logic/thinking#thinking-budget)to configure how much thinking the model can do. If you set a low budget, then the model won't "overthink" its response. If you set a high budget, then the model can think more if needed. Setting a thinking budget also reserves more of the total token output limit for the actual response.

- Enable[AI monitoring in theFirebaseconsole](https://firebase.google.com/docs/ai-logic/monitoring#ai-monitoring-in-console)to monitor the count of thinking tokens and the latency of your requests that have thinking enabled. And if you have[thought summaries](https://firebase.google.com/docs/ai-logic/thinking#thought-summaries)enabled, they will display in the console where you can inspect the model's detailed reasoning to help you debug and refine your prompts.

## Control the thinking budget

To control how much thinking the model can do to generate its response, you can specify the number of***thinking budget***tokens that it's allowed to use.

You can manually set the thinking budget in situations where you might need more or fewer tokens than the default thinking budget. Find more detailed guidance about[task complexity and suggested budgets](https://firebase.google.com/docs/ai-logic/thinking#task-complexity)later in this section. Here's some high-level guidance:

- Set a low thinking budget if latency is important or for less complex tasks
- Set a high thinking budget for more complex tasks

| **Note** :Firebase AI Logicdoes*not yet* support the following:
|
| - Setting***thinking levels*** for theGemini 3models, but it's coming soon! In the meantime, you can set***thinking budgets***.
| - Setting***thinking budgets*** for theGemini Live APImodels, but it's coming soon!

### Set the thinking budget

|----------------------------------------------------------------------------------------------------------------------------------|
| *Click yourGemini APIprovider to view provider-specific content and code on this page.* Gemini Developer APIVertex AI Gemini API |

Set the thinking budget in a`GenerationConfig`as part of creating the`GenerativeModel`instance. The configuration is maintained for the lifetime of the instance. If you want to use different thinking budgets for different requests, then create`GenerativeModel`instances configured with each budget.

Learn about[supported thinking budget values](https://firebase.google.com/docs/ai-logic/thinking#supported-thinking-budget-values)later in this section.  

### Swift

Set the thinking budget in a[`GenerationConfig`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerationConfig)as part of creating a`GenerativeModel`instance.  


    // ...

    // Set the thinking configuration
    // Use a thinking budget value appropriate for your model (example value shown here)
    let generationConfig = GenerationConfig(
      thinkingConfig: ThinkingConfig(thinkingBudget: 1024)
    )

    // Specify the config as part of creating the `GenerativeModel` instance
    let model = FirebaseAI.firebaseAI(backend: .googleAI()).generativeModel(
      modelName: "<var translate="no">GEMINI_MODEL_NAME</var>",
      generationConfig: generationConfig
    )

    // ...

### Kotlin

Set the values of the parameters in a[`GenerationConfig`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig)as part of creating a`GenerativeModel`instance.  


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
      modelName = "<var translate="no">GEMINI_MODEL_NAME</var>",
      generationConfig,
    )

    // ...

### Java

Set the values of the parameters in a[`GenerationConfig`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig)as part of creating a`GenerativeModel`instance.  


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
                      /* modelName */ "<var translate="no">GEMINI_MODEL_NAME</var>",
                      /* generationConfig */ generationConfig
                    );
    );

    // ...

### Web

Set the values of the parameters in a[`GenerationConfig`](https://firebase.google.com/docs/reference/js/ai.generationconfig)as part of creating a`GenerativeModel`instance.  


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
    const model = getGenerativeModel(ai, { model: "<var translate="no">GEMINI_MODEL_NAME</var>", generationConfig });

    // ...

### Dart

Set the values of the parameters in a[`GenerationConfig`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/GenerationConfig-class.html)as part of creating a`GenerativeModel`instance.  


    // ...

    // Set the thinking configuration
    // Use a thinking budget value appropriate for your model (example value shown here)
    final thinkingConfig = ThinkingConfig(thinkingBudget: 1024);

    final generationConfig = GenerationConfig(
      thinkingConfig: thinkingConfig
    );

    // Specify the config as part of creating the `GenerativeModel` instance
    final model = FirebaseAI.googleAI().generativeModel(
      model: '<var translate="no">GEMINI_MODEL_NAME</var>',
      config: generationConfig,
    );

    // ...

### Unity

Set the values of the parameters in a[`GenerationConfig`](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generation-config)as part of creating a`GenerativeModel`instance.  


    // ...

    // Set the thinking configuration
    // Use a thinking budget value appropriate for your model (example value shown here)
    var thinkingConfig = new ThinkingConfig(thinkingBudget: 1024);

    var generationConfig = new GenerationConfig(
      thinkingConfig: thinkingConfig
    );

    // Specify the config as part of creating the `GenerativeModel` instance
    var model = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI()).GetGenerativeModel(
      modelName: "<var translate="no">GEMINI_MODEL_NAME</var>",
      generationConfig: generationConfig
    );

    // ...

### Supported thinking budget values

The following table lists the thinking budget values that you can set for each model by[configuring the model's`thinkingBudget`](https://firebase.google.com/docs/ai-logic/thinking#set-thinking-budget).

|         Model         |              Default value              |                                                                                       Available range for thinking budget                                                                                        || Value to [disable thinking](https://firebase.google.com/docs/ai-logic/thinking#disable-thinking) | Value to [enable dynamic thinking](https://firebase.google.com/docs/ai-logic/thinking#enable-dynamic-thinking) |
|         Model         |              Default value              | Value to [disable thinking](https://firebase.google.com/docs/ai-logic/thinking#disable-thinking) | Value to [enable dynamic thinking](https://firebase.google.com/docs/ai-logic/thinking#enable-dynamic-thinking) |
|-----------------------|-----------------------------------------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
|                                                                || **Minimum value**                                                                                | **Maximum value**                                                                                              |                                                                                                                                                                                                                  ||
| Gemini 2.5 Pro        | `8,192`                                 | `128`                                                                                            | `32,768`                                                                                                       | *cannot be turned off*                                                                           | `-1`                                                                                                           |
| Gemini 2.5 Flash      | `8,192`                                 | `1`                                                                                              | `24,576`                                                                                                       | `0`                                                                                              | `-1`                                                                                                           |
| Gemini 2.5 FlashâLite | `0` *(thinking is disabled by default)* | `512`                                                                                            | `24,576`                                                                                                       | `0` *(or don't configure thinking budget at all)*                                                | `-1`                                                                                                           |

#### Disable thinking

For some[easier tasks](https://firebase.google.com/docs/ai-logic/thinking#task-complexity), the thinking capability isn't necessary, and traditional inference is sufficient. Or if reducing latency is a priority, you may not want the model to take any more time than necessary to generate a response.

In these situations, you can disable (or turn off) thinking:

- **Gemini 2.5 Pro** : thinking*cannot*be disabled
- **Gemini 2.5 Flash** : set`thinkingBudget`to`0`tokens
- **Gemini 2.5 FlashâLite**: thinking is disabled by default

#### Enable dynamic thinking

You can let the model decide when and how much it thinks (called***dynamic thinking*** ) by setting`thinkingBudget`to`-1`. The model can use as many tokens as it decides is appropriate, up to its maximum token value listed above.

### Task complexity

- **Easy tasks --- thinking could be turned off**   
  Straightforward requests where complex reasoning isn't required, such as fact retrieval or classification. Examples:

  - "Where was DeepMind founded?"
  - "Is this email asking for a meeting or just providing information?"
- **Medium tasks --- default budget or some additional thinking budget needed**   
  Common requests that benefit from a degree of step-by-step processing or deeper understanding. Examples:

  - "Create an analogy between photosynthesis and growing up."
  - "Compare and contrast electric cars and hybrid cars."
- **Hard tasks --- maximum thinking budget may be needed**   
  Truly complex challenges, such as solving complex math problems or coding tasks. These types of tasks require the model to engage its full reasoning and planning capabilities, often involving many internal steps before providing an answer. Examples:

  - "Solve problem 1 in AIME 2025: Find the sum of all integer bases b \> 9 for which 17b is a divisor of 97b."
  - "Write Python code for a web application that visualizes real-time stock market data, including user authentication. Make it as efficient as possible."

## Include thought summaries in responses

***Thought summaries***are synthesized versions of the model's raw thoughts and offer insights into the model's internal reasoning process.

Here are some reasons to include thought summaries in responses:

- You can display the thought summary in your app's UI or make them accessible to your users. The thought summary is returned as a separate part in the response so that you have more control over how it's used in your app.

- If you also enable[AI monitoring in theFirebaseconsole](https://firebase.google.com/docs/ai-logic/monitoring#ai-monitoring-in-console), then thought summaries display in the console where you can inspect the model's detailed reasoning to help you debug and refine your prompts.

Here are some key notes about thought summaries:

- Thought summaries are*not* controlled by[thinking budgets](https://firebase.google.com/docs/ai-logic/thinking#thinking-budget)(budgets*only* apply to the model's raw thoughts). However, if[thinking is disabled](https://firebase.google.com/docs/ai-logic/thinking#disable-thinking), then the model won't return a thought summary.

- Thought summaries are considered part of the model's regular generated-text response and count as output tokens.

| **Note** : ForGemini Live APImodels,Firebase AI Logicdoes*not yet*support enabling thought summaries, but that feature is coming soon!

### Enable thought summaries

|----------------------------------------------------------------------------------------------------------------------------------|
| *Click yourGemini APIprovider to view provider-specific content and code on this page.* Gemini Developer APIVertex AI Gemini API |

You can enable thought summaries by setting`includeThoughts`to true in your model configuration. You can then access the summary by checking the`thoughtSummary`field from the response.

Here's an example demonstrating how to enable and retrieve thought summaries with the response:  

### Swift

Enable thought summaries in the[`GenerationConfig`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerationConfig)as part of creating a`GenerativeModel`instance.  


    // ...

    // Set the thinking configuration
    // Optionally enable thought summaries in the generated response (default is false)
    let generationConfig = GenerationConfig(
      thinkingConfig: ThinkingConfig(includeThoughts: true)
    )

    // Specify the config as part of creating the `GenerativeModel` instance
    let model = FirebaseAI.firebaseAI(backend: .googleAI()).generativeModel(
      modelName: "<var translate="no">GEMINI_MODEL_NAME</var>",
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

Enable thought summaries in the[`GenerationConfig`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig)as part of creating a`GenerativeModel`instance.  


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
      modelName = "<var translate="no">GEMINI_MODEL_NAME</var>",
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

Enable thought summaries in the[`GenerationConfig`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig)as part of creating a`GenerativeModel`instance.  


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
                      /* modelName */ "<var translate="no">GEMINI_MODEL_NAME</var>",
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

Enable thought summaries in the[`GenerationConfig`](https://firebase.google.com/docs/reference/js/ai.generationconfig)as part of creating a`GenerativeModel`instance.  


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
    const model = getGenerativeModel(ai, { model: "<var translate="no">GEMINI_MODEL_NAME</var>", generationConfig });

    const result = await model.generateContent("solve x^2 + 4x + 4 = 0");
    const response = result.response;

    // Handle the response that includes thought summaries
    if (response.thoughtSummary()) {
        console.log(`Thought Summary: ${response.thoughtSummary()}`);
    }
    const text = response.text();
    console.log(`Answer: ${text}`);

### Dart

Enable thought summaries in the[`GenerationConfig`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/GenerationConfig-class.html)as part of creating a`GenerativeModel`instance.  


    // ...

    // Set the thinking configuration
    // Optionally enable thought summaries in the generated response (default is false)
    final thinkingConfig = ThinkingConfig(includeThoughts: true);

    final generationConfig = GenerationConfig(
      thinkingConfig: thinkingConfig
    );

    // Specify the config as part of creating the `GenerativeModel` instance
    final model = FirebaseAI.googleAI().generativeModel(
      model: '<var translate="no">GEMINI_MODEL_NAME</var>',
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

Enable thought summaries in the[`GenerationConfig`](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generation-config)as part of creating a`GenerativeModel`instance.  


    // ...

    // Set the thinking configuration
    // Optionally enable thought summaries in the generated response (default is false)
    var thinkingConfig = new ThinkingConfig(includeThoughts: true);

    var generationConfig = new GenerationConfig(
      thinkingConfig: thinkingConfig
    );

    // Specify the config as part of creating the `GenerativeModel` instance
    var model = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI()).GetGenerativeModel(
      modelName: "<var translate="no">GEMINI_MODEL_NAME</var>",
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
    #     Okay, let's solve the quadratic equation xÂ² + 4x + 4 = 0.
    #     ...
    #     **Answer:**
    #     The solution to the equation xÂ² + 4x + 4 = 0 is x = -2. This is a repeated root (or a root with multiplicity 2).

    # Example Thought Summary:
    #     **My Thought Process for Solving the Quadratic Equation**
    #
    #     Alright, let's break down this quadratic, xÂ² + 4x + 4 = 0. First things first:
    #     it's a quadratic; the xÂ² term gives it away, and we know the general form is
    #     axÂ² + bx + c = 0.
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
    #     (x + 2)(x + 2) = 0, or more concisely, (x + 2)Â² = 0. Solving for x is now
    #     trivial: x + 2 = 0, thus x = -2.
    #
    #     Okay, just to be absolutely certain, I'll run the quadratic formula just to
    #     double-check. x = [-b Â± â(bÂ² - 4ac)] / 2a. Plugging in the values, x = [-4 Â±
    #     â(4Â² - 4 * 1 * 4)] / (2 * 1). That simplifies to x = [-4 Â± â0] / 2. So, x =
    #     -2 again - a repeated root. Nice.
    #
    #     Now, let's check via completing the square. Starting from the same equation,
    #     (xÂ² + 4x) = -4. Take half of the b-value (4/2 = 2), square it (2Â² = 4), and
    #     add it to both sides, so xÂ² + 4x + 4 = -4 + 4. Which simplifies into (x + 2)Â²
    #     = 0. The square root on both sides gives us x + 2 = 0, therefore x = -2, as
    #      expected.
    #
    #     Always, *always* confirm! Let's substitute x = -2 back into the original
    #     equation: (-2)Â² + 4(-2) + 4 = 0. That's 4 - 8 + 4 = 0. It checks out.
    #
    #     Conclusion: the solution is x = -2. Confirmed.

<br />

<br />

#### Stream thought summaries

You can also view thought summaries if you choose to stream a response using`generateContentStream`. This will return rolling, incremental summaries during the response generation.  

### Swift

Enable thought summaries in the[`GenerationConfig`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerationConfig)as part of creating a`GenerativeModel`instance.  


    // ...

    // Set the thinking configuration
    // Optionally enable thought summaries in the generated response (default is false)
    let generationConfig = GenerationConfig(
      thinkingConfig: ThinkingConfig(includeThoughts: true)
    )

    // Specify the config as part of creating the `GenerativeModel` instance
    let model = FirebaseAI.firebaseAI(backend: .googleAI()).generativeModel(
      modelName: "<var translate="no">GEMINI_MODEL_NAME</var>",
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

Enable thought summaries in the[`GenerationConfig`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig)as part of creating a`GenerativeModel`instance.  


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
      modelName = "<var translate="no">GEMINI_MODEL_NAME</var>",
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

Enable thought summaries in the[`GenerationConfig`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig)as part of creating a`GenerativeModel`instance.  


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
                      /* modelName */ "<var translate="no">GEMINI_MODEL_NAME</var>",
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

Enable thought summaries in the[`GenerationConfig`](https://firebase.google.com/docs/reference/js/ai.generationconfig)as part of creating a`GenerativeModel`instance.  


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
    const model = getGenerativeModel(ai, { model: "<var translate="no">GEMINI_MODEL_NAME</var>", generationConfig });

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

Enable thought summaries in the[`GenerationConfig`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/GenerationConfig-class.html)as part of creating a`GenerativeModel`instance.  


    // ...

    // Set the thinking configuration
    // Optionally enable thought summaries in the generated response (default is false)
    final thinkingConfig = ThinkingConfig(includeThoughts: true);

    final generationConfig = GenerationConfig(
      thinkingConfig: thinkingConfig
    );

    // Specify the config as part of creating the `GenerativeModel` instance
    final model = FirebaseAI.googleAI().generativeModel(
      model: '<var translate="no">GEMINI_MODEL_NAME</var>',
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

Enable thought summaries in the[`GenerationConfig`](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generation-config)as part of creating a`GenerativeModel`instance.  


    // ...

    // Set the thinking configuration
    // Optionally enable thought summaries in the generated response (default is false)
    var thinkingConfig = new ThinkingConfig(includeThoughts: true);

    var generationConfig = new GenerationConfig(
      thinkingConfig: thinkingConfig
    );

    // Specify the config as part of creating the `GenerativeModel` instance
    var model = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI()).GetGenerativeModel(
      modelName: "<var translate="no">GEMINI_MODEL_NAME</var>",
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

## Understand thought signatures

| **Important:** TheFirebase AI LogicSDKs automatically handle thought signatures for you. Also note that you can't enable or disable thought signatures (this is a limitation from the underlyingGemini APIproviders). Thought signatures are considered input tokens.

When using thinking in multi-turn interactions, the model doesn't have access to thought context from previous turns. However, if you're using[function calling](https://firebase.google.com/docs/ai-logic/function-calling), you can take advantage of***thought signatures*** to maintain thought context across turns. Thought signatures are encrypted representations of the model's internal thought process, and they're available when using thinking*and*function calling. Specifically, thought signatures are generated when:

- Thinking is enabled and thoughts are generated.
- The request includes function declarations.

**To take advantage of thought signatures, use function calling as normal.** TheFirebase AI LogicSDKs simplify the process by managing the state and automatically handling thought signatures for you. The SDKs automatically pass any generated thought signatures between subsequent`sendMessage`or`sendMessageStream`calls in a`Chat`session.

## Pricing and counting thinking tokens

Thinking tokens use the same[pricing](https://firebase.google.com/docs/ai-logic/pricing)as text-output tokens. If you enable[thought summaries](https://firebase.google.com/docs/ai-logic/thinking#thought-summaries), they are considered to be thinking tokens and are priced accordingly.

You can enable[AI monitoring in theFirebaseconsole](https://firebase.google.com/docs/ai-logic/monitoring#ai-monitoring-in-console)to monitor the count of thinking tokens for requests that have thinking enabled.

You can get the total number of thinking tokens from the`thoughtsTokenCount`field in the`usageMetadata`attribute of the response:  

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

Learn more about tokens in the[count tokens guide](https://firebase.google.com/docs/ai-logic/count-tokens).