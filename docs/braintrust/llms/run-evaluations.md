# Source: https://braintrust.dev/docs/evaluate/run-evaluations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Run evaluations

> Execute experiments locally, in CI/CD, or on remote environments

Run evaluations directly in your code using the `Eval()` function, use the `braintrust eval` CLI command to run multiple evaluations from files, or create experiments in the Braintrust UI for no-code workflows. Integrate with CI/CD to catch regressions automatically.

<Tip>
  For iterative experimentation, use [playgrounds](/evaluate/playgrounds) to test prompts and models interactively, compare results side-by-side, and then save winning configurations as experiments.
</Tip>

## Run with Eval()

The `Eval()` function runs an evaluation and creates an experiment:

<CodeGroup dropdown>
  ```typescript wrap theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Eval, initDataset } from "braintrust";
  import { Factuality } from "autoevals";

  Eval("My Project", {
    data: initDataset("My Project", { dataset: "My Dataset" }),
    task: async (input) => {
      // Your LLM call here
      return await callModel(input);
    },
    scores: [Factuality],
    metadata: {
      model: "gpt-4o",
      temperature: 0.7,
    },
  });
  ```

  ```python wrap theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import Eval, init_dataset
  from autoevals import Factuality

  Eval(
      "My Project",
      data=init_dataset(project="My Project", name="My Dataset"),
      task=lambda input: call_model(input),  # Your LLM call here
      scores=[Factuality],
      metadata={
          "model": "gpt-4o",
          "temperature": 0.7,
      },
  )
  ```

  ```go wrap theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  package main

  import (
  	"context"
  	"log"

  	"go.opentelemetry.io/otel"
  	"go.opentelemetry.io/otel/sdk/trace"

  	"github.com/braintrustdata/braintrust-sdk-go"
  	"github.com/braintrustdata/braintrust-sdk-go/eval"
  )

  func callModel(input string) string {
  	// Your LLM call implementation here
  	return "model output"
  }

  func main() {
  	ctx := context.Background()

  	tp := trace.NewTracerProvider()
  	defer tp.Shutdown(ctx)
  	otel.SetTracerProvider(tp)

  	client, err := braintrust.New(tp)
  	if err != nil {
  		log.Fatal(err)
  	}

  	evaluator := braintrust.NewEvaluator[string, string](client)

  	_, err = evaluator.Run(ctx, eval.Opts[string, string]{
  		Experiment: "My Project",
  		Dataset: eval.NewDataset([]eval.Case[string, string]{
  			{Input: "example input", Expected: "example expected"},
  		}),
  		Task: eval.T(func(ctx context.Context, input string) (string, error) {
  			return callModel(input), nil // Your LLM call here
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
  		Metadata: map[string]any{
  			"model":       "gpt-4o",
  			"temperature": 0.7,
  		},
  	})
  	if err != nil {
  		log.Fatal(err)
  	}
  }
  ```

  ```ruby wrap theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  require "braintrust"

  Braintrust.init

  Braintrust::Eval.run(
    project: "My Project",
    cases: [
      {input: "example input", expected: "example expected"},
    ],
    task: ->(input) { call_model(input) },  # Your LLM call here
    scorers: [
      Braintrust::Eval.scorer("exact_match") do |input, expected, output, metadata|
        output == expected ? 1.0 : 0.0
      end
    ],
    metadata: {model: "gpt-4o", temperature: 0.7}
  )

  OpenTelemetry.tracer_provider.shutdown
  ```

  ```java wrap theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import dev.braintrust.Braintrust;
  import dev.braintrust.eval.DatasetCase;
  import dev.braintrust.eval.Scorer;

  class Main {
    static String callModel(String input) {
      // Your LLM call implementation here
      return "model output";
    }

    public static void main(String... args) {
      var braintrust = Braintrust.get();
      var openTelemetry = braintrust.openTelemetryCreate();

      var eval = braintrust.<String, String>evalBuilder()
          .name("My Project")
          .cases(DatasetCase.of("example input", "example expected"))
          .taskFunction(input -> callModel(input)) // Your LLM call here
          .scorers(
              Scorer.of("exact_match", (expected, actual) -> expected.equals(actual) ? 1.0 : 0.0)
          )
          .build();

      var result = eval.run();
      System.out.println(result.createReportString());
    }
  }
  ```

  ```csharp wrap theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  using System;
  using System.Collections.Generic;
  using System.Threading.Tasks;
  using Braintrust.Sdk;
  using Braintrust.Sdk.Eval;

  class Program
  {
      static string CallModel(string input)
      {
          // Your LLM call implementation here
          return "model output";
      }

      static async Task Main(string[] args)
      {
          var braintrust = Braintrust.Sdk.Braintrust.Get();

          var eval = await braintrust
              .EvalBuilder<string, string>()
              .Name("My Project")
              .Cases(
                  new DatasetCase<string, string>("example input", "example expected")
              )
              .TaskFunction(input => CallModel(input)) // Your LLM call here
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

Running `Eval()` automatically:

* Creates an experiment in Braintrust
* Displays a summary in your terminal
* Populates the UI with results
* Returns summary metrics

## Run with CLI

Use the `braintrust eval` command to run evaluations from files:

<Tabs>
  <Tab title="TypeScript">
    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    npx braintrust eval basic.eval.ts
    ```

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    npx braintrust eval [file or directory] ...
    ```

    The CLI loads environment variables from:

    * `.env.development.local`
    * `.env.local`
    * `.env.development`
    * `.env`
  </Tab>

  <Tab title="Python">
    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    braintrust eval eval_basic.py
    ```

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    braintrust eval [file or directory] ...
    ```

    The CLI loads environment variables from the same files as the TypeScript version.
  </Tab>
</Tabs>

### Watch mode

Re-run evaluations automatically when files change:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
npx braintrust eval --watch basic.eval.ts
```

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
braintrust eval --watch eval_basic.py
```

### Local testing mode

Run evaluations without sending logs to Braintrust for quick iteration:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
npx braintrust eval --no-send-logs basic.eval.ts
```

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
braintrust eval --no-send-logs eval_basic.py
```

## Run in UI

Create and run experiments directly in the Braintrust UI without writing code:

1. Navigate to **Evaluations** > **Experiments**.
2. Click **+ Experiment** or use the empty state form.
3. Select one or more prompts, workflows, or scorers to evaluate.
4. Choose or create a dataset:
   * **Select existing dataset**: Pick from datasets in your organization
   * **Upload CSV/JSON**: Import test cases from a file
   * **Empty dataset**: Create a blank dataset to populate manually later
5. Add scorers to measure output quality.
6. Click **Create** to execute the experiment.

This workflow is ideal when you have prompts ready and want to quickly run experiments against datasets.

### Use playgrounds for rapid iteration

For iterative experimentation, use [playgrounds](/evaluate/playgrounds) to test prompts and models interactively, compare results side-by-side, and save winning configurations as experiments.

<Note>
  UI experiments timeout after 15 minutes. For longer-running evaluations, use the SDK or CLI approach.
</Note>

## Run in CI/CD

Integrate evaluations into your CI/CD pipeline to catch regressions automatically.

### GitHub Actions

Use the [`braintrustdata/eval-action`](https://github.com/braintrustdata/eval-action) to run evaluations on every pull request:

```yaml  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
- name: Run Evals
  uses: braintrustdata/eval-action@v1
  with:
    api_key: ${{ secrets.BRAINTRUST_API_KEY }}
    runtime: node
```

The action automatically posts a comment with results:

<img src="https://mintcdn.com/braintrust/j7ECWw6iEjI59XB3/evaluate/github-actions-comment.png?fit=max&auto=format&n=j7ECWw6iEjI59XB3&q=85&s=c22158050abd505b3e2c26689c868e51" alt="action comment" data-og-width="1548" width="1548" data-og-height="730" height="730" data-path="evaluate/github-actions-comment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/j7ECWw6iEjI59XB3/evaluate/github-actions-comment.png?w=280&fit=max&auto=format&n=j7ECWw6iEjI59XB3&q=85&s=f6c9b1c5c74b6f40860839577b2a8c22 280w, https://mintcdn.com/braintrust/j7ECWw6iEjI59XB3/evaluate/github-actions-comment.png?w=560&fit=max&auto=format&n=j7ECWw6iEjI59XB3&q=85&s=d4d50fe53eafec48e83d3e6cfb6b6d55 560w, https://mintcdn.com/braintrust/j7ECWw6iEjI59XB3/evaluate/github-actions-comment.png?w=840&fit=max&auto=format&n=j7ECWw6iEjI59XB3&q=85&s=87fe5c9acab33735fad95750eb87dff0 840w, https://mintcdn.com/braintrust/j7ECWw6iEjI59XB3/evaluate/github-actions-comment.png?w=1100&fit=max&auto=format&n=j7ECWw6iEjI59XB3&q=85&s=28b4ec539c70a3594763437409327d69 1100w, https://mintcdn.com/braintrust/j7ECWw6iEjI59XB3/evaluate/github-actions-comment.png?w=1650&fit=max&auto=format&n=j7ECWw6iEjI59XB3&q=85&s=1512d40ca94be2d33cef89c746ced34f 1650w, https://mintcdn.com/braintrust/j7ECWw6iEjI59XB3/evaluate/github-actions-comment.png?w=2500&fit=max&auto=format&n=j7ECWw6iEjI59XB3&q=85&s=ca9bb7de7e94c778fec6baf208e77fa7 2500w" />

Full example workflow:

```yaml  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
name: Run evaluations

on:
  pull_request:
    branches: [main]

jobs:
  evaluate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        run: npm install

      - name: Run Evals
        uses: braintrustdata/eval-action@v1
        with:
          api_key: ${{ secrets.BRAINTRUST_API_KEY }}
          runtime: node
```

### Other CI systems

For other CI systems, run evaluations as a standard command:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
# Install dependencies
npm install

# Run evaluations
npx braintrust eval evals/
```

Ensure your CI environment has the `BRAINTRUST_API_KEY` environment variable set.

## Run remotely

Expose evaluations running on remote servers or local machines using dev mode:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
npx braintrust eval --dev basic.eval.ts
```

This allows you to trigger evaluations from the Braintrust UI or API while the code runs in your environment. See [Run remote evaluations](/evaluate/remote-evals) for details.

## Configure experiments

Customize experiment behavior with options:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  Eval("My Project", {
    data: myDataset,
    task: myTask,
    scores: [Factuality],

    // Experiment name
    experiment: "gpt-4o-experiment",

    // Metadata for filtering/analysis
    metadata: {
      model: "gpt-4o",
      prompt_version: "v2",
    },

    // Maximum concurrency
    maxConcurrency: 10,

    // Trial count for averaging
    trialCount: 3,
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  Eval(
      "My Project",
      data=my_dataset,
      task=my_task,
      scores=[Factuality],

      # Experiment name
      experiment="gpt-4o-experiment",

      # Metadata for filtering/analysis
      metadata={
          "model": "gpt-4o",
          "prompt_version": "v2",
      },

      # Maximum concurrency
      max_concurrency=10,

      # Trial count for averaging
      trial_count=3,
  )
  ```

  ```go  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  package main

  import (
  	"context"
  	"log"

  	"go.opentelemetry.io/otel"
  	"go.opentelemetry.io/otel/sdk/trace"

  	"github.com/braintrustdata/braintrust-sdk-go"
  	"github.com/braintrustdata/braintrust-sdk-go/eval"
  )

  func main() {
  	ctx := context.Background()

  	tp := trace.NewTracerProvider()
  	defer tp.Shutdown(ctx)
  	otel.SetTracerProvider(tp)

  	client, err := braintrust.New(tp)
  	if err != nil {
  		log.Fatal(err)
  	}

  	evaluator := braintrust.NewEvaluator[string, string](client)

  	// Example variables (define your own)
  	myDataset := eval.NewDataset([]eval.Case[string, string]{
  		{Input: "example input", Expected: "example expected"},
  	})
  	myTask := eval.T(func(ctx context.Context, input string) (string, error) {
  		return "model output", nil
  	})
  	myScorers := []eval.Scorer[string, string]{
  		eval.NewScorer("exact-match", func(ctx context.Context, r eval.TaskResult[string, string]) (eval.Scores, error) {
  			score := 0.0
  			if r.Output == r.Expected {
  				score = 1.0
  			}
  			return eval.S(score), nil
  		}),
  	}

  	_, err = evaluator.Run(ctx, eval.Opts[string, string]{
  		Experiment: "gpt-4o-experiment",
  		Dataset:    myDataset,
  		Task:       myTask,
  		Scorers:    myScorers,
  		Metadata: map[string]any{
  			"model":          "gpt-4o",
  			"prompt_version": "v2",
  		},
  	})
  	if err != nil {
  		log.Fatal(err)
  	}
  }
  ```

  ```ruby  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  Braintrust::Eval.run(
    project: "My Project",
    experiment: "gpt-4o-experiment",
    cases: my_dataset,
    task: my_task,
    scorers: my_scorers,
    metadata: {model: "gpt-4o", prompt_version: "v2"},
    max_concurrency: 10,
    trial_count: 3
  )
  ```

  ```java  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import dev.braintrust.Braintrust;
  import dev.braintrust.eval.DatasetCase;
  import dev.braintrust.eval.Scorer;
  import java.util.function.Function;

  class Main {
    public static void main(String... args) {
      var braintrust = Braintrust.get();
      var openTelemetry = braintrust.openTelemetryCreate();

      // Example variables (define your own)
      var myDataset = new DatasetCase[]{
          DatasetCase.of("example input", "example expected")
      };
      Function<String, String> myTask = input -> "model output";
      var myScorers = new Scorer[]{
          Scorer.of("exact_match", (expected, actual) -> expected.equals(actual) ? 1.0 : 0.0)
      };

      var result = braintrust.<String, String>evalBuilder()
          .name("gpt-4o-experiment")
          .cases(myDataset)
          .taskFunction(myTask)
          .scorers(myScorers)
          .build()
          .run();

      System.out.println(result.createReportString());
    }
  }
  ```

  ```csharp  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  using System;
  using System.Collections.Generic;
  using System.Threading.Tasks;
  using Braintrust.Sdk;
  using Braintrust.Sdk.Eval;

  class Program
  {
      static async Task Main(string[] args)
      {
          var braintrust = Braintrust.Sdk.Braintrust.Get();

          // Example variables (define your own)
          var myDataset = new[] {
              new DatasetCase<string, string>("example input", "example expected")
          };
          Func<string, string> myTask = input => "model output";
          var myScorers = new[] {
              new FunctionScorer<string, string>("exact_match", (expected, actual) =>
                  actual == expected ? 1.0 : 0.0)
          };

          var eval = await braintrust
              .EvalBuilder<string, string>()
              .Name("gpt-4o-experiment")
              .Cases(myDataset)
              .TaskFunction(myTask)
              .Scorers(myScorers)
              .BuildAsync();

          var result = await eval.RunAsync();
          Console.WriteLine(result.CreateReportString());
      }
  }
  ```
</CodeGroup>

## Run trials

Run each input multiple times to measure variance and get more robust scores. Braintrust intelligently aggregates results by bucketing test cases with the same `input` value:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  Eval("My Project", {
    data: myDataset,
    task: myTask,
    scores: [Factuality],
    trialCount: 10, // Run each input 10 times
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  Eval(
      "My Project",
      data=my_dataset,
      task=my_task,
      scores=[Factuality],
      trial_count=10,  # Run each input 10 times
  )
  ```

  ```go  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  package main

  import (
  	"context"
  	"log"

  	"go.opentelemetry.io/otel"
  	"go.opentelemetry.io/otel/sdk/trace"

  	"github.com/braintrustdata/braintrust-sdk-go"
  	"github.com/braintrustdata/braintrust-sdk-go/eval"
  )

  func main() {
  	ctx := context.Background()

  	tp := trace.NewTracerProvider()
  	defer tp.Shutdown(ctx)
  	otel.SetTracerProvider(tp)

  	client, err := braintrust.New(tp)
  	if err != nil {
  		log.Fatal(err)
  	}

  	evaluator := braintrust.NewEvaluator[string, string](client)

  	// Example variables (define your own)
  	myDataset := eval.NewDataset([]eval.Case[string, string]{
  		{Input: "example input", Expected: "example expected"},
  	})
  	myTask := eval.T(func(ctx context.Context, input string) (string, error) {
  		return "model output", nil
  	})
  	myScorers := []eval.Scorer[string, string]{
  		eval.NewScorer("exact-match", func(ctx context.Context, r eval.TaskResult[string, string]) (eval.Scores, error) {
  			score := 0.0
  			if r.Output == r.Expected {
  				score = 1.0
  			}
  			return eval.S(score), nil
  		}),
  	}

  	_, err = evaluator.Run(ctx, eval.Opts[string, string]{
  		Experiment: "My Project",
  		Dataset:    myDataset,
  		Task:       myTask,
  		Scorers:    myScorers,
  	})
  	if err != nil {
  		log.Fatal(err)
  	}
  }
  ```

  ```ruby  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  Braintrust::Eval.run(
    project: "My Project",
    cases: my_dataset,
    task: my_task,
    scorers: my_scorers,
    trial_count: 10  # Run each input 10 times
  )
  ```

  ```java  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import dev.braintrust.Braintrust;
  import dev.braintrust.eval.DatasetCase;
  import dev.braintrust.eval.Scorer;
  import java.util.function.Function;

  class Main {
    public static void main(String... args) {
      var braintrust = Braintrust.get();
      var openTelemetry = braintrust.openTelemetryCreate();

      // Example variables (define your own)
      var myDataset = new DatasetCase[]{
          DatasetCase.of("example input", "example expected")
      };
      Function<String, String> myTask = input -> "model output";
      var myScorers = new Scorer[]{
          Scorer.of("exact_match", (expected, actual) -> expected.equals(actual) ? 1.0 : 0.0)
      };

      var result = braintrust.<String, String>evalBuilder()
          .name("My Project")
          .cases(myDataset)
          .taskFunction(myTask)
          .scorers(myScorers)
          .build()
          .run();

      System.out.println(result.createReportString());
    }
  }
  ```

  ```csharp  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  using System;
  using System.Threading.Tasks;
  using Braintrust.Sdk;
  using Braintrust.Sdk.Eval;

  class Program
  {
      static async Task Main(string[] args)
      {
          var braintrust = Braintrust.Sdk.Braintrust.Get();

          // Example variables (define your own)
          var myDataset = new[] {
              new DatasetCase<string, string>("example input", "example expected")
          };
          Func<string, string> myTask = input => "model output";
          var myScorers = new[] {
              new FunctionScorer<string, string>("exact_match", (expected, actual) =>
                  actual == expected ? 1.0 : 0.0)
          };

          var eval = await braintrust
              .EvalBuilder<string, string>()
              .Name("My Project")
              .Cases(myDataset)
              .TaskFunction(myTask)
              .Scorers(myScorers)
              .BuildAsync();

          var result = await eval.RunAsync();
          Console.WriteLine(result.CreateReportString());
      }
  }
  ```
</CodeGroup>

## Run local evals without sending logs

Run evaluations locally without creating experiments or sending data to Braintrust:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  Eval(
    "Say Hi Bot",
    {
      data: () => [{ input: "David", expected: "Hi David" }],
      task: (input) => "Hi " + input,
      scores: [Factuality],
    },
    {
      noSendLogs: true, // Run locally without creating experiment
    },
  );
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  Eval(
      "Say Hi Bot",
      data=lambda: [{"input": "David", "expected": "Hi David"}],
      task=lambda input: "Hi " + input,
      scores=[Factuality],
      no_send_logs=True,  # Run locally without creating experiment
  )
  ```

  ```go  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  package main

  import (
  	"context"
  	"log"

  	"go.opentelemetry.io/otel"
  	"go.opentelemetry.io/otel/sdk/trace"

  	"github.com/braintrustdata/braintrust-sdk-go"
  	"github.com/braintrustdata/braintrust-sdk-go/eval"
  )

  func main() {
  	ctx := context.Background()

  	tp := trace.NewTracerProvider()
  	defer tp.Shutdown(ctx)
  	otel.SetTracerProvider(tp)

  	client, err := braintrust.New(tp)
  	if err != nil {
  		log.Fatal(err)
  	}

  	evaluator := braintrust.NewEvaluator[string, string](client)

  	// Example scorers (define your own)
  	myScorers := []eval.Scorer[string, string]{
  		eval.NewScorer("exact-match", func(ctx context.Context, r eval.TaskResult[string, string]) (eval.Scores, error) {
  			score := 0.0
  			if r.Output == r.Expected {
  				score = 1.0
  			}
  			return eval.S(score), nil
  		}),
  	}

  	_, err = evaluator.Run(ctx, eval.Opts[string, string]{
  		Experiment: "Say Hi Bot",
  		Dataset: eval.NewDataset([]eval.Case[string, string]{
  			{Input: "David", Expected: "Hi David"},
  		}),
  		Task: eval.T(func(ctx context.Context, input string) (string, error) {
  			return "Hi " + input, nil
  		}),
  		Scorers: myScorers,
  	})
  	if err != nil {
  		log.Fatal(err)
  	}
  }
  ```

  ```ruby  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  Braintrust::Eval.run(
    project: "Say Hi Bot",
    cases: [{input: "David", expected: "Hi David"}],
    task: ->(input) { "Hi #{input}" },
    scorers: my_scorers,
    no_send_logs: true  # Run locally without creating experiment
  )
  ```

  ```java  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import dev.braintrust.Braintrust;
  import dev.braintrust.eval.DatasetCase;
  import dev.braintrust.eval.Scorer;

  class Main {
    public static void main(String... args) {
      var braintrust = Braintrust.get();
      var openTelemetry = braintrust.openTelemetryCreate();

      // Example scorers (define your own)
      var myScorers = new Scorer[]{
          Scorer.of("exact_match", (expected, actual) -> expected.equals(actual) ? 1.0 : 0.0)
      };

      var result = braintrust.<String, String>evalBuilder()
          .name("Say Hi Bot")
          .cases(DatasetCase.of("David", "Hi David"))
          .taskFunction(input -> "Hi " + input)
          .scorers(myScorers)
          .build()
          .run();

      System.out.println(result.createReportString());
    }
  }
  ```

  ```csharp  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  using System;
  using System.Threading.Tasks;
  using Braintrust.Sdk;
  using Braintrust.Sdk.Eval;

  class Program
  {
      static async Task Main(string[] args)
      {
          var braintrust = Braintrust.Sdk.Braintrust.Get();

          // Example scorers (define your own)
          var myScorers = new[] {
              new FunctionScorer<string, string>("exact_match", (expected, actual) =>
                  actual == expected ? 1.0 : 0.0)
          };

          var eval = await braintrust
              .EvalBuilder<string, string>()
              .Name("Say Hi Bot")
              .Cases(new DatasetCase<string, string>("David", "Hi David"))
              .TaskFunction(input => "Hi " + input)
              .Scorers(myScorers)
              .BuildAsync();

          var result = await eval.RunAsync();
          Console.WriteLine(result.CreateReportString());
      }
  }
  ```
</CodeGroup>

This is equivalent to passing the `--no-send-logs` flag with the CLI command.

## Next steps

* [Interpret results](/evaluate/interpret-results) from your experiments
* [Compare experiments](/evaluate/compare-experiments) to measure improvements
* [Write scorers](/evaluate/write-scorers) to measure quality
* [Use playgrounds](/evaluate/playgrounds) for no-code experimentation
