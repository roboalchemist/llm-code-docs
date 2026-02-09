# Source: https://braintrust.dev/docs/evaluation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Evaluation quickstart

> Run your first eval

[Evaluations](/evaluate) let you systematically measure AI quality. Compare approaches, catch regressions before deployment, and validate improvements with data instead of intuition.

Each evaluation consists of three components:

* **Data** - A dataset of test cases with inputs and expected outputs
* **Task** - An AI function you want to test
* **Scores** - Scoring functions that measure output quality

<Tabs>
  <Tab title="SDK" icon="terminal">
    Set up your environment and [run evals](/evaluate/run-evaluations) with the Braintrust SDK.

    ## 1. Sign up

    If you're new to Braintrust, sign up free at [braintrust.dev](https://www.braintrust.dev).

    ## 2. Get API keys

    Create API keys for:

    * [Braintrust](https://www.braintrust.dev/app/settings?subroute=api-keys)
    * Your AI provider or framework ([OpenAI](https://platform.openai.com/api-keys), [Anthropic](https://console.anthropic.com/settings/keys), [Gemini](https://aistudio.google.com/app/apikey), [etc.](/integrations))

    Set them as environment variables:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    export BRAINTRUST_API_KEY="<your-braintrust-api-key>"
    export OPENAI_API_KEY="<your-openai-api-key>" # or ANTHROPIC_API_KEY, GEMINI_API_KEY, etc.
    ```

    <Tip>
      This quickstart uses OpenAI. For other providers, see [Integrations](/integrations).
    </Tip>

    ## 3. Install SDKs

    Install the Braintrust SDK and required libraries:

    <CodeGroup>
      ```bash TypeScript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      # pnpm
      pnpm add braintrust openai autoevals ts-node
      # npm
      npm install braintrust openai autoevals ts-node
      ```

      ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      pip install braintrust openai autoevals
      ```

      ```bash Go theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      go get github.com/braintrustdata/braintrust-sdk-go
      go get github.com/openai/openai-go
      ```

      ```bash Ruby theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      # Add to your Gemfile
      gem "braintrust"
      gem "ruby-openai"

      # Install:
      bundle install
      ```

      ```bash Java theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      # Add to build.gradle dependencies{} block
      implementation 'dev.braintrust:braintrust-sdk-java:<version-goes-here>'
      implementation 'com.openai:openai-java-sdk:<version-goes-here>'
      ```

      ```bash C# theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      # Add to .csproj file
      dotnet add package Braintrust.Sdk
      dotnet add package OpenAI
      ```
    </CodeGroup>

    ## 4. Run an eval

    Build an evaluation that identifies movies from plot descriptions. You'll define a [dataset](/annotate/datasets) with movie plot descriptions as inputs and expected titles as outputs, write a task function with a [prompt](/evaluate/write-prompts) to identify movies, and use a [scorer](/evaluate/scorers) to measure accuracy.

    <Steps>
      <Step title="Set your project">
        Set your project name as an environment variable:

        ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
        export BRAINTRUST_DEFAULT_PROJECT_NAME="Evaluation quickstart"
        ```
      </Step>

      <Step title="Write your evaluation">
        Create an evaluation that defines your dataset, task, and scorer (built-in `ExactMatch` scorer for Python and TypeScript, equivalent code-based scorer for other languages):

        <CodeGroup dropdown>
          ```typescript movie-matcher.eval.ts theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
          import { Eval } from "braintrust";
          import { ExactMatch } from "autoevals";
          import OpenAI from "openai";

          const client = new OpenAI();

          Eval("Movie matcher", {
            // Data: Test cases with inputs and expected outputs
            data: [
              {
                input: "A detective investigates a series of murders based on the seven deadly sins.",
                expected: "Se7en",
              },
              {
                input: "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
                expected: "Inception",
              },
              {
                input: "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                expected: "The Matrix",
              },
              {
                input: "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                expected: "Toy Story",
              },
              {
                input: "An orphaned boy discovers he's a wizard on his 11th birthday when Hagrid escorts him to magic-teaching Hogwarts School.",
                expected: "Harry Potter and the Sorcerer's Stone",
              },
            ],

            // Task: The function being evaluated
            task: async (input) => {
              const response = await client.responses.create({
                model: "gpt-5-mini",
                input: [
                  {
                    role: "system",
                    content: "Based on the following description, identify the movie."
                  },
                  { role: "user", content: input }
                ],
              });
              return response.output_text;
            },

            // Scores: Metrics to measure quality
            scores: [ExactMatch],
          });
          ```

          ```python movie_matcher.py theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
          from braintrust import Eval
          from autoevals import ExactMatch
          from openai import OpenAI

          client = OpenAI()

          def task(input):
              response = client.responses.create(
                  model="gpt-5-mini",
                  input=[
                      {
                          "role": "system",
                          "content": "Based on the following description, identify the movie."
                      },
                      {"role": "user", "content": input}
                  ],
              )
              return response.output_text

          Eval(
              "Movie matcher",
              # Data: Test cases with inputs and expected outputs
              data=[
                  {
                      "input": "A detective investigates a series of murders based on the seven deadly sins.",
                      "expected": "Se7en",
                  },
                  {
                      "input": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
                      "expected": "Inception",
                  },
                  {
                      "input": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                      "expected": "The Matrix",
                  },
                  {
                      "input": "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                      "expected": "Toy Story",
                  },
                  {
                      "input": "An orphaned boy discovers he's a wizard on his 11th birthday when Hagrid escorts him to magic-teaching Hogwarts School.",
                      "expected": "Harry Potter and the Sorcerer's Stone",
                  },
              ],
              # Task: The function being evaluated
              task=task,
              # Scores: Metrics to measure quality
              scores=[ExactMatch],
          )
          ```

          ```go movie_matcher.go theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
          package main

          import (
          	"context"
          	"log"
          	"os"

          	"github.com/braintrustdata/braintrust-sdk-go"
          	"github.com/braintrustdata/braintrust-sdk-go/eval"
          	traceopenai "github.com/braintrustdata/braintrust-sdk-go/trace/contrib/openai"
          	"github.com/openai/openai-go"
          	"github.com/openai/openai-go/option"
          	"go.opentelemetry.io/otel"
          	"go.opentelemetry.io/otel/sdk/trace"
          )

          func main() {
          	ctx := context.Background()

          	// Setup OpenTelemetry
          	tp := trace.NewTracerProvider()
          	defer tp.Shutdown(ctx)
          	otel.SetTracerProvider(tp)

          	// Initialize Braintrust
          	bt, err := braintrust.New(tp,
          		braintrust.WithAPIKey(os.Getenv("BRAINTRUST_API_KEY")),
          		braintrust.WithProject(os.Getenv("BRAINTRUST_DEFAULT_PROJECT")),
          	)
          	if err != nil {
          		log.Fatal(err)
          	}

          	// Create OpenAI client with tracing
          	openaiClient := openai.NewClient(
          		option.WithMiddleware(traceopenai.NewMiddleware()),
          	)

          	// Create an evaluator
          	evaluator := braintrust.NewEvaluator[string, string](bt)

          	// Run the evaluation
          	_, err = evaluator.Run(ctx, eval.Opts[string, string]{
          		Experiment: "Movie matcher",
          		// Data: Test cases with inputs and expected outputs
          		Dataset: eval.NewDataset([]eval.Case[string, string]{
          			{Input: "A detective investigates a series of murders based on the seven deadly sins.", Expected: "Se7en"},
          			{Input: "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.", Expected: "Inception"},
          			{Input: "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.", Expected: "The Matrix"},
          			{Input: "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.", Expected: "Toy Story"},
          			{Input: "An orphaned boy discovers he's a wizard on his 11th birthday when Hagrid escorts him to magic-teaching Hogwarts School.", Expected: "Harry Potter and the Sorcerer's Stone"},
          		}),
          		// Task: The function being evaluated
          		Task: eval.T(func(ctx context.Context, input string) (string, error) {
          			response, err := openaiClient.Chat.Completions.New(ctx, openai.ChatCompletionNewParams{
          				Messages: []openai.ChatCompletionMessageParamUnion{
          					openai.SystemMessage("Based on the following description, identify the movie."),
          					openai.UserMessage(input),
          				},
          				Model: openai.ChatModelGPT5Mini,
          			})
          			if err != nil {
          				return "", err
          			}
          			return response.Choices[0].Message.Content, nil
          		}),
          		// Scores: Metrics to measure quality
          		Scorers: []eval.Scorer[string, string]{
          			eval.NewScorer("exact_match", func(ctx context.Context, r eval.TaskResult[string, string]) (eval.Scores, error) {
          				score := 0.0
          				if r.Expected == r.Output {
          					score = 1.0
          				}
          				return eval.S(score), nil
          			}),
          		},
          	})
          	if err != nil {
          		log.Fatal(err)
          	}
          }
          ```

          ```ruby movie_matcher.rb theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
          require 'braintrust'
          require 'openai'

          Braintrust.init

          client = OpenAI::Client.new(
              access_token: ENV.fetch('OPENAI_API_KEY', nil)
          )

          Braintrust::Eval.run(
            project: 'Evaluation quickstart',
            experiment: 'Movie matcher',
            # Data: Test cases with inputs and expected outputs
            cases: [
              {input: "A detective investigates a series of murders based on the seven deadly sins.", expected: "Se7en"},
              {input: "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.", expected: "Inception"},
              {input: "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.", expected: "The Matrix"},
              {input: "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.", expected: "Toy Story"},
              {input: "An orphaned boy discovers he's a wizard on his 11th birthday when Hagrid escorts him to magic-teaching Hogwarts School.", expected: "Harry Potter and the Sorcerer's Stone"},
            ],
            # Task: The function being evaluated
            task: lambda do |input|
              response = client.chat(
                parameters: {
                  model: 'gpt-5-mini',
                  messages: [
                    {role: "system", content: "Based on the following description, identify the movie."},
                    {role: "user", content: input}
                  ]
                }
              )
              response.dig("choices", 0, "message", "content")
            end,
            # Scores: Metrics to measure quality
            scorers: [
              Braintrust::Eval.scorer("exact_match") do |input, expected, output, metadata|
                output == expected ? 1.0 : 0.0
              end
            ]
          )

          OpenTelemetry.tracer_provider.force_flush
          ```

          ```java MovieMatcher.java theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
          import com.openai.client.OpenAIClient;
          import com.openai.client.okhttp.OpenAIOkHttpClient;
          import com.openai.models.ChatModel;
          import com.openai.models.chat.completions.ChatCompletionCreateParams;
          import dev.braintrust.Braintrust;
          import dev.braintrust.config.BraintrustConfig;
          import dev.braintrust.eval.DatasetCase;
          import dev.braintrust.eval.Scorer;
          import dev.braintrust.instrumentation.openai.BraintrustOpenAI;
          import java.util.function.Function;

          class MovieMatcher {
            public static void main(String[] args) {
              var braintrust = Braintrust.get();
              var openTelemetry = braintrust.openTelemetryCreate();

              // Wrap the OpenAI client with Braintrust instrumentation
              OpenAIClient client = BraintrustOpenAI.wrapOpenAI(openTelemetry, OpenAIOkHttpClient.fromEnv());

              // Task: The function being evaluated
              Function<String, String> taskFunction = (String input) -> {
                var response = client.chat().completions().create(
                  ChatCompletionCreateParams.builder()
                    .model(ChatModel.GPT_5_MINI)
                    .addSystemMessage("Based on the following description, identify the movie.")
                    .addUserMessage(input)
                    .build()
                );
                return response.choices().get(0).message().content().orElse("");
              };

              // Build and run the evaluation
              var eval = braintrust.<String, String>evalBuilder()
                  .name("Movie matcher")
                  // Data: Test cases with inputs and expected outputs
                  .cases(
                    DatasetCase.of("A detective investigates a series of murders based on the seven deadly sins.", "Se7en"),
                    DatasetCase.of("A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.", "Inception"),
                    DatasetCase.of("A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.", "The Matrix"),
                    DatasetCase.of("A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.", "Toy Story"),
                    DatasetCase.of("An orphaned boy discovers he's a wizard on his 11th birthday when Hagrid escorts him to magic-teaching Hogwarts School.", "Harry Potter and the Sorcerer's Stone")
                  )
                  .taskFunction(taskFunction)
                  // Scores: Metrics to measure quality
                  .scorers(
                    Scorer.of("exact_match", (expected, actual) ->
                      expected.equals(actual) ? 1.0 : 0.0
                    )
                  )
                  .build();

              var result = eval.run();
              System.out.println(result.createReportString());
            }
          }
          ```

          ```csharp MovieMatcher.cs theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
          using System;
          using System.Threading.Tasks;
          using Braintrust.Sdk;
          using Braintrust.Sdk.Eval;
          using Braintrust.Sdk.Instrumentation.OpenAI;
          using OpenAI;
          using OpenAI.Chat;

          class MovieMatcher
          {
              static async Task Main(string[] args)
              {
                  var braintrust = Braintrust.Sdk.Braintrust.Get();
                  var activitySource = braintrust.GetActivitySource();

                  var apiKey = Environment.GetEnvironmentVariable("OPENAI_API_KEY");
                  if (string.IsNullOrEmpty(apiKey))
                  {
                      Console.WriteLine("Error: OPENAI_API_KEY environment variable is not set.");
                      return;
                  }

                  // Wrap the OpenAI client with Braintrust instrumentation
                  var client = BraintrustOpenAI.WrapOpenAI(activitySource, apiKey);

                  // Build and run the evaluation
                  var eval = await braintrust
                      .EvalBuilder<string, string>()
                      .Name("Movie matcher")
                      // Data: Test cases with inputs and expected outputs
                      .Cases(

                          new DatasetCase<string, string>("A detective investigates a series of murders based on the seven deadly sins.", "Se7en"),
                          new DatasetCase<string, string>("A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.", "Inception"),
                          new DatasetCase<string, string>("A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.", "The Matrix"),
                          new DatasetCase<string, string>("A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.", "Toy Story"),
                          new DatasetCase<string, string>("An orphaned boy discovers he's a wizard on his 11th birthday when Hagrid escorts him to magic-teaching Hogwarts School.", "Harry Potter and the Sorcerer's Stone")
                      )
                      // Task: The function being evaluated
                      .TaskFunction((string input) =>
                      {
                          var chatClient = client.GetChatClient("gpt-5-mini");
                          var messages = new ChatMessage[]
                          {
                              new SystemChatMessage("Based on the following description, identify the movie."),
                              new UserChatMessage(input)
                          };
                          var result = chatClient.CompleteChat(messages);
                          return result.Value.Content[0].Text;
                      })
                      // Scores: Metrics to measure quality
                      .Scorers(
                          new FunctionScorer<string, string>("exact_match", (expected, actual) =>
                              actual == expected ? 1.0 : 0.0)
                      )
                      .BuildAsync();

                  var result = await eval.RunAsync();
                  Console.WriteLine(result.CreateReportString());
              }
          }
          ```
        </CodeGroup>
      </Step>

      <Step title="Run the evaluation">
        Run your evaluation:

        <CodeGroup>
          ```bash TypeScript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
          npx braintrust eval movie-matcher.eval.ts
          ```

          ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
          braintrust eval movie_matcher.py
          ```

          ```bash Go theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
          go run movie_matcher.go
          ```

          ```bash Ruby theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
          ruby movie_matcher.rb
          ```

          ```bash Java theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
          javac -cp ".:*" MovieMatcher.java
          java -cp ".:*" MovieMatcher
          ```

          ```bash C# theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
          dotnet run
          ```
        </CodeGroup>

        This creates an **experiment**, a permanent record of how your task performed on the dataset. Each experiment captures inputs, outputs, scores, and metadata, making it easy to compare different versions of your prompts or models.
      </Step>

      <Step title="View results">
        You'll see a link to your experiment in the terminal output.

        Click the link to view your evaluation results, or go to <Icon icon="beaker" /> **Experiments** in the "Evaluation quickstart" project in the Braintrust UI.
      </Step>
    </Steps>

    ## 5. Iterate

    You might notice that some scores are 0%. This is because the scorer requires outputs to exactly match the expected value. For example, if the AI returns "The movie is Se7en" instead of "Se7en", or uses the UK title "Harry Potter and the Philosopher's Stone" instead of the expected US title "Harry Potter and the Sorcerer's Stone", the score will be 0% for that case.

    Let's improve the prompt to return only US-based movie titles and create a second experiment.

    <Steps>
      <Step title="Update your evaluation">
        In your eval code, change the prompt to:

        ```text wrap theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
        Identify the movie from the description. Return only the movie title, with no additional text or explanation. Always use the US-based title.
        ```
      </Step>

      <Step title="Run the evaluation">
        Run the improved evaluation:

        <CodeGroup>
          ```bash TypeScript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
          npx braintrust eval movie-matcher.eval.ts
          ```

          ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
          braintrust eval movie_matcher.py
          ```

          ```bash Go theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
          go run movie_matcher.go
          ```

          ```bash Ruby theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
          ruby movie_matcher.rb
          ```

          ```bash Java theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
          javac -cp ".:*" MovieMatcher.java
          java -cp ".:*" MovieMatcher
          ```

          ```bash C# theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
          dotnet run
          ```
        </CodeGroup>
      </Step>

      <Step title="View results">
        Click the link to your new experiment in the terminal output.

        The improved prompt should have higher scores because it returns just the movie title. In the Braintrust UI, you can [compare this experiment](/evaluate/compare-experiments) with your first one to see the improvement.
      </Step>
    </Steps>

    ## Troubleshoot

    <AccordionGroup>
      <Accordion title="Dataset not found error?">
        Verify your dataset name matches exactly what you see in the Braintrust UI:

        ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
        // Make sure this matches your dataset name
        data: initDataset("Movie matcher", {
          dataset: "Movie matcher dataset"  // Check this name in the UI
        })
        ```

        Go to <Icon icon="database" /> **Datasets** in your Braintrust project and confirm the dataset name.
      </Accordion>

      <Accordion title="Import errors or missing modules?">
        Install all required packages:

        <CodeGroup>
          ```bash TypeScript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
          pnpm add braintrust openai autoevals
          ```

          ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
          pip install braintrust openai autoevals
          ```
        </CodeGroup>
      </Accordion>

      <Accordion title="API key errors?">
        Check your environment variables:

        ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
        echo $BRAINTRUST_API_KEY
        echo $OPENAI_API_KEY
        ```

        Both should return values. If empty, set them:

        ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
        export BRAINTRUST_API_KEY="your-braintrust-key"
        export OPENAI_API_KEY="your-openai-key"
        ```

        Get your Braintrust API key from [Settings > API Keys](https://www.braintrust.dev/app/settings?subroute=api-keys).
      </Accordion>

      <Accordion title="Not seeing experiments in UI?">
        Check your terminal output for the experiment link after running `braintrust eval`. Click it to navigate directly to the experiment.

        If you don't see a link:

        * Check for error messages in terminal output
        * Verify network connectivity
        * Ensure you're viewing the correct project ("Evaluation quickstart")
      </Accordion>

      <Accordion title="Need help?">
        * Join our [Discord](https://discord.gg/6G8s47F44X)
        * Email us at [support@braintrust.dev](mailto:support@braintrust.dev)
        * Use the [Loop](/observe/loop) feature in the Braintrust UI
      </Accordion>
    </AccordionGroup>
  </Tab>

  <Tab title="UI" icon="mouse-pointer-2">
    Build and iterate on evaluations visually in [playgrounds](/evaluate/playgrounds) without writing code.

    ## 1. Sign up

    If you're new to Braintrust, sign up free at [braintrust.dev](https://www.braintrust.dev).

    ## 2. Add an AI provider

    Braintrust lets you call AI providers directly from the UI. For this quickstart, you'll use OpenAI:

    1. Get an OpenAI API key from [platform.openai.com/api-keys](https://platform.openai.com/api-keys).
    2. Go to <Icon icon="settings-2" /> **Settings** > <Icon icon="sparkle" /> [**AI providers**](https://www.braintrust.dev/app/settings?subroute=secrets).
    3. Select **OpenAI** from the provider list.
    4. Enter your OpenAI API key.
    5. Click **Save**.

    <ApiKeyEncryptionNote />

    ## 3. Run an eval

    Build an evaluation that identifies movies from plot descriptions. You'll upload test cases, create prompts, add scoring, and compare results interactively - all in a [playground](/evaluate/playgrounds), a workspace for rapid iteration without writing code. .

    <Steps>
      <Step title="Create a playground">
        1. Go to <Icon icon="shapes" /> **Playgrounds**.
        2. Select **Create empty playground**.
        3. Enter `Movie matcher` as the name and select **Create**.
        4. Select the playground in the list.
      </Step>

      <Step title="Create a prompt">
        A [prompt](/evaluate/write-prompts) is the instruction you give to an AI model to complete a task.

        1. In the playground, choose `GPT-5 mini` as your model.
        2. Enter the following system prompt:

           ```text wrap theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
           Based on the following description, identify the movie.
           ```
        3. Select **+ Message** and enter the following user message:

           ```text  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
           {{input}}
           ```

           Prompts can use [templating syntax](/evaluate/write-prompts#use-templating) to refer to variables. In this case, the input corresponds to the movie description given by the user.
      </Step>

      <Step title="Add a dataset">
        To evaluate how well your prompt works, you need test data. A [dataset](/annotate/datasets) contains inputs and the outputs you expect from your AI.

        1. Download this [sample dataset](/assets/movie-matcher.csv).
        2. In the playground, select <Icon icon="database" /> **Select a dataset** > <Icon icon="upload" /> **Upload new dataset**.
        3. Upload your CSV file.

           Columns automatically map to the input and expected fields. Drag and drop them into different categories as needed:
        4. Click **Import**.
      </Step>

      <Step title="Add a scorer">
        [Scorers](/evaluate/scorers) measure the quality of your AI's outputs using built-in functions, custom code, or LLM judges. For this task, you'll use the **ExactMatch** built-in scorer because movie titles have clear right and wrong answers.

        1. In the playground, select **+ Scorer**.
        2. Select **AutoEvals** > **ExactMatch**.
      </Step>

      <Step title="Run an evaluation">
        Select <Icon icon="play" /> **Run** at the top of the playground to see how well your prompt performs.

        The playground will execute your prompt against all rows in your dataset and score the results. You'll see:

        * The AI's response for each movie description
        * The ExactMatch score (100% for correct, 0% for incorrect)
      </Step>
    </Steps>

    ## 4. Iterate

    You might notice that some ExactMatch scores are 0%. This is because ExactMatch requires outputs to exactly match the expected value. For example, if the AI returns "The movie is Se7en" instead of "Se7en", or uses the UK title "Harry Potter and the Philosopher's Stone" instead of the expected US title "Harry Potter and the Sorcerer's Stone", the score will be 0% for that case.

    Let's create an improved prompt that returns only the US-based movie title:

    1. In the playground, select **+ Task**.
    2. Select <Icon icon="message-circle" /> **Prompt** > **+ Blank prompt**.
    3. Add a more specific system message:

       ```text wrap theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
       Identify the movie from the description. Return only the movie title, with no additional text or explanation. Always use the US-based title.
       ```
    4. Select **+ Message** and enter the following user message:

       ```text  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
       {{input}}
       ```
    5. Select <Icon icon="message-circle" /> **Save prompt**.
    6. Select **Run** to compare both prompts side-by-side.

    You'll now see results for both prompts in the playground. The improved prompt should have higher ExactMatch scores because it returns just the movie title.

    This comparison view helps you quickly see which prompt performs better. You can add multiple prompt variations to test different approaches.

    ## Troubleshoot

    <AccordionGroup>
      <Accordion title="Playground not running?">
        **Check your AI provider:**
        Verify you've added OpenAI in <Icon icon="settings-2" /> **Settings** > <Icon icon="sparkle" /> [**AI providers**](https://www.braintrust.dev/app/settings?subroute=secrets) with a valid API key.

        **Check dataset uploaded:**
        Go to <Icon icon="database" /> **Datasets** and confirm your CSV imported successfully. You should see all 21 movie examples.

        **Browser issues:**
        Try refreshing the page or using a different browser. Clear your browser cache if the playground seems stuck.
      </Accordion>

      <Accordion title="Not seeing results?">
        **Refresh the page:**
        The UI updates in real-time, but try refreshing if results don't appear.

        **Check for errors:**
        Look for error messages in the playground. Common issues:

        * Invalid API key
        * Model not selected
        * Empty dataset
      </Accordion>

      <Accordion title="Need help?">
        * Join our [Discord](https://discord.gg/6G8s47F44X)
        * Email us at [support@braintrust.dev](mailto:support@braintrust.dev)
        * Use the [Loop](/observe/loop) feature in the Braintrust UI
      </Accordion>
    </AccordionGroup>
  </Tab>
</Tabs>

## Next steps

* Explore the full [Braintrust workflow](/workflow)
* Go deeper with evaluation:
  * [Write custom scorers](/evaluate/write-scorers) - Measure what matters for your use case
  * [Compare experiments](/evaluate/compare-experiments) - Systematically test different approaches
  * [Build datasets](/annotate/datasets) - Create representative test cases from production data
  * [Run evaluations in CI/CD](/evaluate/run-evaluations#cicd) - Catch regressions automatically
