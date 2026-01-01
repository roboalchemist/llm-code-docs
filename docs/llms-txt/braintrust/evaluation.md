# Source: https://braintrust.dev/docs/evaluation.md

# Evaluation quickstart

> Run evals in Braintrust to measure and improve your AI applications

This quickstart shows you how to set up and run evals in a Braintrust [experiment](/core/experiments) to measure your AI application's effectiveness and iterate continuously using production data. You can create evals with the Braintrust SDK or directly in the Braintrust UI.

<Tabs>
  <Tab title="SDK" icon="terminal">
    Set up your environment and create an eval with the Braintrust SDK. Wrappers are available for [TypeScript](/reference/sdks/typescript), [Python](/reference/sdks/python), and [other languages](/reference/sdks).

    ### 1. Install Braintrust libraries

    Install the Braintrust SDK and autoevals library for your language:

    <CodeGroup>
      ```bash Typescript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      # npm
      npm install braintrust autoevals
      # pnpm
      pnpm add braintrust autoevals
      ```

      ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      pip install braintrust autoevals
      ```

      ```bash Go theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      go get github.com/braintrustdata/braintrust-sdk-go
      ```

      ```bash Ruby theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      gem install braintrust
      ```

      ```bash Java theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      # add to build.gradle dependencies{} block
      implementation 'dev.braintrust:braintrust-sdk-java:<version-goes-here>'
      ```

      ```bash C# theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      # add to .csproj file
      dotnet add package Braintrust.Sdk
      ```
    </CodeGroup>

    ### 2. Configure an API key

    You need a Braintrust API key to authenticate your evaluation.

    Create an API key in the [Braintrust UI](https://www.braintrust.dev/app/settings?subroute=api-keys) and then add the key to your environment:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    export BRAINTRUST_API_KEY="YOUR_API_KEY"
    ```

    ### 3. Run an evaluation

    A Braintrust [evaluation](/core/experiments) is a simple function composed of a dataset of user inputs, a task, and a set of scorers.

    <Note>
      In addition to adding each data point inline when you call the `Eval()` function, you can also [pass an existing or new dataset directly](/core/datasets#use-a-dataset-in-an-evaluation).
    </Note>

    Create an evaluation script:

    <CodeGroup dropdown>
      ```typescript tutorial.eval.ts theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import { Eval } from "braintrust";
      import { Levenshtein } from "autoevals";

      Eval(
        "Say Hi Bot", // Replace with your project name
        {
          data: () => {
            return [
              {
                input: "Foo",
                expected: "Hi Foo",
              },
              {
                input: "Bar",
                expected: "Hello Bar",
              },
            ]; // Replace with your eval dataset
          },
          task: async (input) => {
            return "Hi " + input; // Replace with your LLM call
          },
          scores: [Levenshtein],
        },
      );
      ```

      ```python eval_tutorial.py theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      from autoevals import Levenshtein
      from braintrust import Eval

      Eval(
          "Say Hi Bot",  # Replace with your project name
          data=lambda: [
              {
                  "input": "Foo",
                  "expected": "Hi Foo",
              },
              {
                  "input": "Bar",
                  "expected": "Hello Bar",
              },
          ],  # Replace with your eval dataset
          task=lambda input: "Hi " + input,  # Replace with your LLM call
          scores=[Levenshtein],
      )
      ```

      ```go main.go theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      package main

      import (
      	"context"
      	"fmt"
      	"log"

      	"go.opentelemetry.io/otel"
      	"go.opentelemetry.io/otel/sdk/trace"

      	"github.com/braintrustdata/braintrust-sdk-go"
      	"github.com/braintrustdata/braintrust-sdk-go/eval"
      )

      func main() {
      	ctx := context.Background()

      	// Setup OpenTelemetry
      	tp := trace.NewTracerProvider()
      	defer tp.Shutdown(ctx)
      	otel.SetTracerProvider(tp)

      	// Initialize Braintrust
      	client, err := braintrust.New(tp)
      	if err != nil {
      		log.Fatal(err)
      	}

      	// Create evaluator
      	evaluator := braintrust.NewEvaluator[string, string](client)

      	// Run evaluation
      	_, err = evaluator.Run(ctx, eval.Opts[string, string]{
      		Experiment: "Say Hi Bot", // Replace with your project name
      		Dataset: eval.NewDataset([]eval.Case[string, string]{
      			{Input: "Foo", Expected: "Hi Foo"},
      			{Input: "Bar", Expected: "Hello Bar"},
      		}), // Replace with your eval dataset
      		Task: eval.T(func(ctx context.Context, input string) (string, error) {
      			return "Hi " + input, nil // Replace with your LLM call
      		}),
      		Scorers: []eval.Scorer[string, string]{
      			eval.NewScorer("exact-match", func(ctx context.Context, r eval.TaskResult[string, string]) (eval.Scores, error) {
      				score := 0.0
      				if r.Output == r.Expected {
      					score = 1.0
      				}
      				return eval.S(score), nil
      			}),
      		},
      	})
      	if err != nil {
      		log.Fatal(err)
      	}

      	fmt.Println("Evaluation complete!")
      }
      ```

      ```ruby eval_tutorial.rb theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      require 'braintrust'

      Braintrust.init

      Braintrust::Eval.run(
        project: 'Say Hi Bot', # Replace with your project name
        experiment: 'tutorial-eval',
        cases: [
          { input: 'Foo', expected: 'Hi Foo' },
          { input: 'Bar', expected: 'Hello Bar' }
        ], # Replace with your eval dataset
        task: ->(input) { 'Hi ' + input }, # Replace with your LLM call
        scorers: [
          # Exact match scorer
          Braintrust::Eval.scorer('exact_match') do |_input, expected, output|
            output == expected ? 1.0 : 0.0
          end
        ]
      )
      ```

      ```java Tutorial.java theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      package dev.braintrust.tutorial;

      import dev.braintrust.Braintrust;
      import dev.braintrust.eval.DatasetCase;
      import dev.braintrust.eval.Scorer;
      import java.util.function.Function;

      class Tutorial {
          public static void main(String[] args) throws Exception {
              var braintrust = Braintrust.get();
              var openTelemetry = braintrust.openTelemetryCreate();

              // Define your task function
              Function<String, String> task = (String input) -> {
                  return "Hi " + input; // Replace with your LLM call
              };

              // Run evaluation
              var eval = braintrust.<String, String>evalBuilder()
                  .name("Say Hi Bot") // Replace with your project name
                  .cases(
                      DatasetCase.of("Foo", "Hi Foo"),
                      DatasetCase.of("Bar", "Hello Bar")
                  ) // Replace with your eval dataset
                  .taskFunction(task)
                  .scorers(
                      Scorer.of("exact-match", (evalCase, output) ->
                          output.equals(evalCase.expected()) ? 1.0 : 0.0
                      )
                  )
                  .build();

              var result = eval.run();
              System.out.println("\n\n" + result.createReportString());
          }
      }
      ```

      ```csharp Tutorial.cs theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      using System;
      using Braintrust.Sdk;
      using Braintrust.Sdk.Eval;

      class Tutorial
      {
          static void Main(string[] args)
          {
              var braintrust = Braintrust.Sdk.Braintrust.Get();

              // Define the task function
              string TaskFunction(string input)
              {
                  return "Hi " + input; // Replace with your LLM call
              }

              // Create and run the evaluation
              var eval = braintrust
                  .EvalBuilder<string, string>()
                  .Name("Say Hi Bot") // Replace with your project name
                  .Cases(
                      DatasetCase<string, string>.Of("Foo", "Hi Foo"),
                      DatasetCase<string, string>.Of("Bar", "Hello Bar")
                  ) // Replace with your eval dataset
                  .TaskFunction(TaskFunction)
                  .Scorers(
                      Scorer<string, string>.Of("exact-match", (expected, actual) =>
                          actual == expected ? 1.0 : 0.0)
                  )
                  .Build();

              var result = eval.Run();
              Console.WriteLine(result.CreateReportString());
          }
      }
      ```
    </CodeGroup>

    Run your evaluation:

    <CodeGroup>
      ```bash Typescript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      npx braintrust eval tutorial.eval.ts
      ```

      ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      braintrust eval eval_tutorial.py
      ```

      ```bash Go theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      go run main.go
      ```

      ```bash Ruby theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      ruby eval_tutorial.rb
      ```

      ```bash Java theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      java Tutorial.java
      ```

      ```bash C# theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      dotnet run
      ```
    </CodeGroup>

    This will create an experiment in Braintrust. Once the command runs, you'll see a link to your experiment.

    <Tip>
      To test your evaluation locally without sending results to Braintrust, add the `--no-send-logs` flag.
    </Tip>

    ### 4. View your results

    Congrats, you just ran an eval! You should see a dashboard like this when you load your experiment. This view is called the *experiment view*, and as you use Braintrust, we hope it becomes your trusty companion each time you change your code and want to run an eval.

    The experiment view allows you to look at high level metrics for performance, dig into individual examples, and compare your LLM app's performance over time.

        <img src="https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/first.png?fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=c288b83745e7f6d0bcc8256e7a22a3e4" alt="First eval" data-og-width="2474" width="2474" data-og-height="818" height="818" data-path="images/first.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/first.png?w=280&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=6a202cb8bdb6b5e8d7f61e5903f2928f 280w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/first.png?w=560&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=cb615437ae1dddc202574815b9ca06b3 560w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/first.png?w=840&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=6e595252994da0cec82e282517bc4070 840w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/first.png?w=1100&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=dec917a9f119cf560b890f106a2e237b 1100w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/first.png?w=1650&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=74aa5c3ee2db168d168edb3fbb67aaf8 1650w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/first.png?w=2500&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=28a1a79acbe82c3714feb838432199e9 2500w" />

    ### 5. Run another experiment

    After running your first evaluation, you'll see that we achieved a 77.8% score. Can you adjust the evaluation to improve this score? Make your changes and re-run the evaluation to track your progress.

        <img src="https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/second.png?fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=22656c7185a0dbdc14c6bb7f2cf9b1f7" alt="Second eval" data-og-width="2464" width="2464" data-og-height="798" height="798" data-path="images/second.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/second.png?w=280&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=c8f431414c170bd8aed1df830abc6fe7 280w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/second.png?w=560&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=e74ea7400d828dd1af0623146157333b 560w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/second.png?w=840&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=4eb89c06935cb66d3056023e85b2126a 840w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/second.png?w=1100&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=83af390331feb43ba06c2db6ce6e4f8f 1100w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/second.png?w=1650&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=434c4d6f4d069955e690a97e0d8ace0b 1650w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/second.png?w=2500&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=e5e23dbacc88701f2d609fe167d56e4c 2500w" />
  </Tab>

  <Tab title="UI" icon="mouse-pointer-2">
    Create experiments to run evals directly in the Braintrust UI. This quickstart uses a sample dataset and sample prompts.

    ### 1. Configure your API keys

    Navigate to the [AI providers](https://www.braintrust.dev/app/settings?subroute=secrets) page in your settings and configure at least one API key. For this quickstart, be sure to add your OpenAI API key. After completing this initial setup, you can access models from many providers through a single, unified API.

    ### 2. Create a new project

    For every AI feature your organization is building, the first thing you'll do is create a project.

    ### 3. Create a new prompt

    Navigate to **Prompts**. Create a new prompt in your project called "movie matcher". A prompt is the input you provide to the model to generate a response. Choose `GPT 4o` for your model, and type this for your system prompt:

    ```
    Based on the following description, identify the movie title. In your response, provide the name of the movie.
    ```

    Select the **+ Message** button below the system prompt, and enter a user message

    ```
    {{input}}
    ```

    Prompts can use [mustache](https://mustache.github.io/mustache.5.html) templating syntax to refer to variables. In this case, the input corresponds to the movie description given by the user.

        <img src="https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/movie-matcher-prompt.png?fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=34102d9e1486b470919bf83dc4749b16" alt="First prompt" data-og-width="1520" width="1520" data-og-height="1320" height="1320" data-path="images/movie-matcher-prompt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/movie-matcher-prompt.png?w=280&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=ead21a90455b2f66c4ea2e5efaf8fb56 280w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/movie-matcher-prompt.png?w=560&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=8a400545fb3a1c922b7cd01bf65bc8a6 560w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/movie-matcher-prompt.png?w=840&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=7b5e4c531b0fda7c89d426141e520ffd 840w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/movie-matcher-prompt.png?w=1100&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=1c6f2800b8385feba5bc7dea41c2f095 1100w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/movie-matcher-prompt.png?w=1650&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=36626c8e6527106c059d414787ff277d 1650w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/movie-matcher-prompt.png?w=2500&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=77940beece4a2c3497ea03464457e333 2500w" />

    Select **Save as custom prompt** to save your prompt.

    ### 4. Explore the prompt playground

    Scroll to the bottom of the prompt viewer, and select **Create playground with prompt**. This will open the prompt you just created in the [prompt playground](https://www.braintrust.dev/docs/guides/playground), a tool for exploring, comparing, and evaluating prompts. In the prompt playground, you can evaluate prompts with data from your [datasets](https://www.braintrust.dev/docs/guides/datasets).

        <img src="https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/prompt-playground.png?fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=73bbe5df8b207e1f14b8edf9ee824867" alt="Prompt playground" data-og-width="2326" width="2326" data-og-height="1280" height="1280" data-path="images/prompt-playground.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/prompt-playground.png?w=280&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=61b1da508e2039c7ccdfadf79a56fde0 280w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/prompt-playground.png?w=560&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=ce8257949a792fe72492d6f0f16d1192 560w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/prompt-playground.png?w=840&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=4dd71d18afc006811ff9676e319c5a06 840w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/prompt-playground.png?w=1100&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=fe4bee2e6648629e1923bf6ff1906d3c 1100w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/prompt-playground.png?w=1650&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=1fad0a3b909daeb1c13fc0702c3c9edc 1650w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/prompt-playground.png?w=2500&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=24f7ece02fc18e8e680764406c8ae7d1 2500w" />

    ### 5. Import a dataset

    Open this [sample dataset](https://gist.githubusercontent.com/ornellaaltunyan/28972d2566ddf64bc171922d0f0564e2/raw/838d220eea620a2390427fe1ec35d347f2b798bd/gistfile1.csv), and right-click to select **Save as...** and download it. It is a `.csv` file with two columns, **Movie Title** and **Original Description**. Inside your playground, select **Dataset**, then **Upload dataset**, and upload the CSV file. Using drag and drop, assign the CSV columns to dataset fields. The input column corresponds to Original Description, and the expected column should be Movie Title. Then, select **Import**.

        <img src="https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/upload-dataset.png?fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=3ca01dd9ee718b5e7218121ae0088a60" alt="Upload dataset" data-og-width="1680" width="1680" data-og-height="1598" height="1598" data-path="images/upload-dataset.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/upload-dataset.png?w=280&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=4129f3e6d05a02e2365c8a6bb5cbf7b6 280w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/upload-dataset.png?w=560&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=9ba2969c677371e1ad21d2bafee6a96f 560w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/upload-dataset.png?w=840&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=2d6d2640c3e969a0a9f6aa0e25f533b6 840w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/upload-dataset.png?w=1100&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=10ad67a15835e9ba6df837fe9c81e9b3 1100w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/upload-dataset.png?w=1650&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=3a11d8c85972dd5969aae8a2ff63ca82 1650w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/upload-dataset.png?w=2500&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=9e6c2ddd1b53da2426b97e04c1fe5e5b 2500w" />

    ### 6. Choose a scorer

    A scoring function allows you to compare the expected output of a task to the actual output and produce a score between 0 and 1. Inside your playground, select **Scorers** to choose from several types of scoring functions. There are two main types of scoring functions: heuristics are great for well-defined criteria, while LLM-as-a-judge is better for handling more complex, subjective evaluations. You can also create a custom scorer. For this example, since there is a clear correct answer, we can choose **ExactMatch**.

    ### 7. Run your first evaluation

    From within the playground, select **+ Experiment** to set up your first evaluation. To run an eval, you need three things:

    * **Data**: a set of examples to test your application on
    * **Task**: the AI function you want to test (any function that takes in an input and returns an output)
    * **Scores**: a set of scoring functions that take an input, output, and optional expected value and compute a score

    In this example, the Data is the dataset you uploaded, the Task is the prompt you created, and Scores is the scoring function we selected.

        <img src="https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/create-experiment.png?fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=dccf4fbedb1d2cb4f48ca34525269e2d" alt="Create experiment" data-og-width="2296" width="2296" data-og-height="1406" height="1406" data-path="images/create-experiment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/create-experiment.png?w=280&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=f925fc88dcb4100ddf55070938931829 280w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/create-experiment.png?w=560&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=272c3315424b24c7c7322c87110ed401 560w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/create-experiment.png?w=840&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=e614a00c8377a7d523c4d45a3b4dd5f6 840w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/create-experiment.png?w=1100&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=f32419b63ba2744247de57343f316dfc 1100w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/create-experiment.png?w=1650&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=1de1e120c472b2616a9d110ac316981d 1650w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/create-experiment.png?w=2500&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=4d697b512209cda33baac0e6a9fe6a84 2500w" />

    Creating an experiment from the playground will automatically log your results to Braintrust.

    <Note>
      Experiments run from the UI have a 15-minute timeout, after which the experiment stops executing. For longer-running evaluations, use the [programmatic SDK approach](/core/experiments/run) instead.
    </Note>

    ### 8. Interpret your results

    Navigate to the **Experiments** page to view your evaluation. Examine the exact match scores and other feedback generated by your evals. If you notice that some of your outputs did not match what was expected, you can tweak your prompt directly in the UI until it consistently produces high-quality outputs. If changing the prompt doesn't yield the desired results, consider experimenting with different models.

        <img src="https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/experiment.png?fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=0c280908c845f431993bc1930e417728" alt="Experiment" data-og-width="2942" width="2942" data-og-height="1500" height="1500" data-path="images/experiment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/experiment.png?w=280&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=d5d1dde2ce83a10aa569798c219b3318 280w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/experiment.png?w=560&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=4bd39e4b3a7527dbcc020d78d3b1fc3b 560w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/experiment.png?w=840&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=b0185d0e1555799eb225172086f3bbde 840w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/experiment.png?w=1100&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=7ff0d6f56f223eb31b2ec062bfeb84e5 1100w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/experiment.png?w=1650&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=fa387364536a52289983924976ab8dc1 1650w, https://mintcdn.com/braintrust/psQJ0h1WPc2nKmNr/images/experiment.png?w=2500&fit=max&auto=format&n=psQJ0h1WPc2nKmNr&q=85&s=a51736614fd9be569264c1c7a24b9bf9 2500w" />

    As you iterate on your prompt, you can run more experiments and compare results.
  </Tab>
</Tabs>

## Next steps

* Dig into our [experiments guide](/core/experiments) to learn more about how to run evals.
* Look at our [cookbook](/cookbook) to learn how to evaluate RAG, summarization, text-to-sql, and other popular use cases.
* Learn how to [log traces](/core/logs/write) to Braintrust.
* Read about Braintrust's [platform and architecture](/reference/architecture).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt