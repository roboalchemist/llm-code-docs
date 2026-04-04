# Source: https://braintrust.dev/docs/core/logs/write.md

# Source: https://braintrust.dev/docs/core/experiments/write.md

# Write evals

Use the Braintrust SDKs to write evals, specifying the dataset, task, and scoring functions. Writing an eval in your code creates a new experiment in your project. You can have multiple eval statements in a single file.

## Write evals with the Braintrust SDK

Braintrust provides wrappers for the SDK in [Typescript](/reference/sdks/typescript), [Python](/reference/sdks/python), [Go](https://github.com/braintrustdata/braintrust-sdk-go), [Java](https://github.com/braintrustdata/braintrust-sdk-java), and [Ruby](https://github.com/braintrustdata/braintrust-sdk-ruby).

Every eval function, regardless of language, includes the following properties:

* **Name**:a name for the experiment
* **Data**: a [dataset](#data) to use for the eval containing a list of inputs, expected outputs (optional), and metadata (optional)
* **Task**: a task to run on the dataset that takes a single input and returns an output (usually an LLM call)
* **Scorers**: one or more [scoring functions](#scorers) that take an input, output, and expected output (optional) and return a score
* **Metadata**: (optional) metadata about the experiment, like the model you're using or configuration values

The return value of the eval function includes the full results of the eval as well as a summary that you can use to see the average scores, duration, improvements, regressions, and other metrics.

<CodeGroup dropdown>
  ```typescript wrap theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Eval } from "braintrust";
  import { Factuality } from "autoevals";

  Eval(
    "Say Hi Bot", // Replace with your project name
    {
      data: () => {
        return [
          {
            input: "David",
            expected: "Hi David",
          },
        ];
      }, // Replace with your eval dataset
      task: (input) => {
        return "Hi " + input;
      }, // Replace with your task function
      scores: [Factuality], // Replace with your scoring functions
    },
  );
  ```

  ```python wrap theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from autoevals import Factuality
  from braintrust import Eval

  Eval(
      "Say Hi Bot",  # Replace with your project name
      data=lambda: [
          {
              "input": "David",
              "expected": "Hi David",
          },
      ],  # Replace with your eval dataset
      task=lambda input: "Hi " + input,  # Replace with your task function
      scores=[Factuality], # Replace with your scoring functions
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
  		Experiment: "Say Hi Bot", // Replace with your project name
  		Dataset: eval.NewDataset([]eval.Case[string, string]{
  			{Input: "David", Expected: "Hi David"},
  		}), // Replace with your eval dataset
  		Task: eval.T(func(ctx context.Context, input string) (string, error) {
  			return "Hi " + input, nil
  		}), // Replace with your task function
  		Scorers: []eval.Scorer[string, string]{
  			eval.NewScorer("exact-match", func(ctx context.Context, r eval.TaskResult[string, string]) (eval.Scores, error) {
  				score := 0.0
  				if r.Output == r.Expected {
  					score = 1.0
  				}
  				return eval.S(score), nil
  			}),
  		}, // Replace with your scoring functions
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
    project: "Say Hi Bot",  # Replace with your project name
    cases: [
      {input: "David", expected: "Hi David"},
    ], # Replace with your eval dataset
    task: ->(input) { "Hi #{input}" },  # Replace with your task function
    scorers: [
      Braintrust::Eval.scorer("exact_match") do |input, expected, output, metadata|
        output == expected ? 1.0 : 0.0
      end
    ] # Replace with your scoring functions
  )

  OpenTelemetry.tracer_provider.shutdown
  ```

  ```java wrap theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import dev.braintrust.Braintrust;
  import dev.braintrust.eval.DatasetCase;
  import dev.braintrust.eval.Scorer;

  class Main {
    public static void main(String... args) {
      var braintrust = Braintrust.get();
      var openTelemetry = braintrust.openTelemetryCreate();

      var eval = braintrust.<String, String>evalBuilder()
          .name("Your Experiment Name") // Replace with your project name
          .cases(DatasetCase.of("David", "Hi David")) // Replace with your eval dataset
          .taskFunction(input -> "Hi " + input) // replace with your task function
          .scorers(
              Scorer.of("exact_match", (evalCase, result) -> evalCase.expected().equals(result) ? 1.0 : 0.0)
          ) // Replace with your scoring functions
          .build();

      var result = eval.run();
      System.out.println(result.createReportString());
    }
  }
  ```

  ```csharp wrap theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  using System;
  using Braintrust.Sdk;
  using Braintrust.Sdk.Eval;

  class Program
  {
      static void Main(string[] args)
      {
          var braintrust = Braintrust.Sdk.Braintrust.Get();

          var eval = braintrust
              .EvalBuilder<string, string>()
              .Name("Say Hi Bot") // Replace with your project name
              .Cases(
                  DatasetCase<string, string>.Of("David", "Hi David")
              ) // Replace with your eval dataset
              .TaskFunction(input => "Hi " + input) // Replace with your task function
              .Scorers(
                  Scorer<string, string>.Of("exact_match", (expected, actual) =>
                      actual == expected ? 1.0 : 0.0)
              ) // Replace with your scoring functions
              .Build();

          var result = eval.Run();
          Console.WriteLine(result.CreateReportString());
      }
  }
  ```
</CodeGroup>

## Data

An evaluation dataset is a list of test cases. Each has an input and optional expected output, metadata, and tags:

* **Input**: The arguments that uniquely define a test case (an arbitrary, JSON serializable object). Braintrust uses the `input` to know whether two test cases are the same between evaluation runs, so the cases should not contain run-specific state. A simple rule of thumb is that if you run the same eval twice, the `input` should be identical.
* **Expected**: (optional) the ground truth value (an arbitrary, JSON serializable object) that you'd compare to `output` to determine if your `output` value is correct or not. Braintrust currently does not compare `output` to `expected` for you, since there are many different ways to do that correctly. For example, you may use a subfield in `expected` to compare to a subfield in `output` for a certain scoring function. Instead, these values are just used to help you navigate your evals while debugging and comparing results.
* **Metadata**: (optional) a dictionary with additional data about the test example, model outputs, or just about anything else that's relevant, that you can use to help find and analyze examples later. For example, you could log the `prompt`, example's `id`, model parameters, or anything else that would be useful to slice/dice later.
* **Tags**: (optional) a list of strings that you can use to filter and group records later.

### Get started

To get started with evals, you need some test data. A fine starting point is to write 5-10 examples that you believe are representative. The data must have an input
field (which could be complex JSON, or just a string) and should ideally have an expected output field, (although this is not required).

Once you have an evaluation set up end-to-end, you can always add more test cases. You'll know you need more data if your eval scores and outputs seem fine, but your production app doesn't look right. And once you have [logging](/core/logs) set up, your real application data will provide a rich source of examples to use as test cases.

As you scale, [datasets](/core/datasets) are a great tool for managing your test cases.

<Note>
  It's a common misconception that you need a large volume of perfectly labeled
  evaluation data, but that's not the case. In practice, it's better to assume
  your data is noisy, your AI model is imperfect, and your scoring methods are a little
  bit wrong. The goal of evaluation is to assess each of these components and
  improve them over time.
</Note>

### Specify an existing dataset in evals

In addition to providing inline data examples when you call the `Eval()` function, you can also [pass an existing or newly initialized dataset](/core/datasets#using-a-dataset-in-an-evaluation).

## Scorers

A scoring function allows you to compare the expected output of a task to the actual output and produce a score between 0 and 1. You use a scoring function by referencing it in the `scores` array in your eval.

We recommend starting with the scorers provided by Braintrust's [autoevals library](https://github.com/braintrustdata/autoevals). They work out of the box and will get you up and running quickly. Just like with test cases, once you begin running evaluations, you will find areas that need improvement. This will lead you create your own scorers, customized to your usecases, to get a well-rounded view of your application's performance.

### Define your own scorers

You can define your own scorer in your code and use it in your eval.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Eval } from "braintrust";
  import { Factuality } from "autoevals";

  const exactMatch = (args: {
    input: string;
    output: string;
    expected: string;
  }) => {
    return {
      name: "Exact match",
      score: args.output === args.expected ? 1 : 0,
    };
  };

  Eval(
    "Say Hi Bot", // Replace with your project name
    {
      data: () => {
        return [
          {
            input: "David",
            expected: "Hi David",
          },
        ]; // Replace with your eval dataset
      },
      task: (input) => {
        return "Hi " + input; // Replace with your task function
      },
      scores: [Factuality, exactMatch],
    },
  );
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from autoevals import Factuality
  from braintrust import Eval

  def exact_match(input, expected, output):
      return 1 if output == expected else 0

  Eval(
      "Say Hi Bot",  # Replace with your project name
      data=lambda: [
          {
              "input": "David",
              "expected": "Hi David",
          },
      ],  # Replace with your eval dataset
      task=lambda input: "Hi " + input,  # Replace with your task function
      scores=[Factuality, exact_match],
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

  	exactMatch := eval.NewScorer("exact-match", func(ctx context.Context, r eval.TaskResult[string, string]) (eval.Scores, error) {
  		score := 0.0
  		if r.Output == r.Expected {
  			score = 1.0
  		}
  		return eval.S(score), nil
  	})

  	_, err = evaluator.Run(ctx, eval.Opts[string, string]{
  		Experiment: "Say Hi Bot", // Replace with your project name
  		Dataset: eval.NewDataset([]eval.Case[string, string]{
  			{Input: "David", Expected: "Hi David"},
  		}), // Replace with your eval dataset
  		Task: eval.T(func(ctx context.Context, input string) (string, error) {
  			return "Hi " + input, nil
  		}), // Replace with your task function
  		Scorers: []eval.Scorer[string, string]{exactMatch}, // Replace with your scoring functions
  	})
  	if err != nil {
  		log.Fatal(err)
  	}
  }
  ```

  ```ruby wrap theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  require "braintrust"

  Braintrust.init

  def exact_match(input:, expected:, output:, **kwargs)
    output == expected ? 1.0 : 0.0
  end

  Braintrust::Eval.run(
    project: "Say Hi Bot", # Replace with your project name
    cases: [
      {input: "David", expected: "Hi David"},
    ], # Replace with your eval dataset
    task: ->(input) { "Hi #{input}" }, # Replace with your task function
    scorers: [
      Braintrust::Eval.scorer("exact_match", &method(:exact_match))
    ] # Replace with your scoring functions
  )

  OpenTelemetry.tracer_provider.shutdown
  ```

  ```java wrap theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import dev.braintrust.Braintrust;
  import dev.braintrust.eval.DatasetCase;
  import dev.braintrust.eval.Scorer;

  class Main {
    public static void main(String... args) {
      var braintrust = Braintrust.get();
      var openTelemetry = braintrust.openTelemetryCreate();

      var eval = braintrust.<String, String>evalBuilder()
          .name("Say Hi Bot") // Replace with your project name
          .cases(DatasetCase.of("David", "Hi David")) // Replace with your eval dataset
          .taskFunction(input -> "Hi " + input) // Replace with your task function
          .scorers(
              Scorer.of("exact_match", (evalCase, result) -> evalCase.expected().equals(result) ? 1.0 : 0.0)
          ) // Replace with your scoring functions
          .build();

      var result = eval.run();
      System.out.println(result.createReportString());
    }
  }
  ```

  ```csharp wrap theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  using System;
  using Braintrust.Sdk;
  using Braintrust.Sdk.Eval;

  class Program
  {
      static void Main(string[] args)
      {
          var braintrust = Braintrust.Sdk.Braintrust.Get();

          var eval = braintrust
              .EvalBuilder<string, string>()
              .Name("Say Hi Bot") // Replace with your project name
              .Cases(
                  DatasetCase<string, string>.Of("David", "Hi David")
              ) // Replace with your eval dataset
              .TaskFunction(input => "Hi " + input) // Replace with your task function
              .Scorers(
                  Scorer<string, string>.Of("exact_match", (expected, actual) =>
                      actual == expected ? 1.0 : 0.0)
              ) // Replace with your scoring functions
              .Build();

          var result = eval.Run();
          Console.WriteLine(result.CreateReportString());
      }
  }
  ```
</CodeGroup>

### Score using AI (LLM judges)

You can also define your own prompt-based scoring functions. For example,

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Eval } from "braintrust";
  import { LLMClassifierFromTemplate } from "autoevals";

  const noApology = LLMClassifierFromTemplate({
    name: "No apology",
    promptTemplate: "Does the response contain an apology? (Y/N)\n\n{{output}}",
    choiceScores: {
      Y: 0,
      N: 1,
    },
    useCoT: true,
  });

  Eval(
    "Say Hi Bot", // Replace with your project name
    {
      data: () => {
        return [
          {
            input: "David",
            expected: "Hi David",
          },
        ]; // Replace with your eval dataset
      },
      task: (input) => {
        return "Sorry " + input; // Replace with your task function
      },
      scores: [noApology],
    },
  );
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from autoevals import LLMClassifier
  from braintrust import Eval

  no_apology = LLMClassifier(
      name="No apology",
      prompt_template="Does the response contain an apology? (Y/N)\n\n{{output}}",
      choice_scores={"Y": 0, "N": 1},
      use_cot=True,
  )

  Eval(
      "Say Hi Bot",  # Replace with your project name
      data=lambda: [
          {
              "input": "David",
              "expected": "Hi David",
          },
      ],  # Replace with your eval dataset
      task=lambda input: "Sorry " + input,  # Replace with your task function
      scores=[no_apology],
  )
  ```
</CodeGroup>

### Use conditional scoring

Sometimes, the scoring function(s) you want to use depend on the input data. For example, if you're evaluating a chatbot, you might want to use a scoring function that measures whether calculator-style inputs are correctly answered.

#### Skip scorers

Return `null`/`None` to skip a scorer for a particular test case.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { NumericDiff } from "autoevals";

  interface QueryInput {
    type: string;
    text: string;
  }

  const calculatorAccuracy = ({
    input,
    output,
  }: {
    input: QueryInput;
    output: number;
  }) => {
    if (input.type !== "calculator") {
      return null;
    }
    return NumericDiff({ output, expected: eval(input.text) });
  };
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from autoevals import NumericDiff

  def calculator_accuracy(input, output, **kwargs):
      if input["type"] != "calculator":
          return None

      return NumericDiff()(output=output, expected=eval(input["text"]))
  ```
</CodeGroup>

<Note>
  Scores with null values will be ignored when computing the overall score, improvements/regressions, and summary metrics like standard deviation.
</Note>

##### Handle scorers on errored test cases

By default, eval tasks or scorers that throw an exception will not generate score values. This means you may encounter a computed overall score that shows a higher value than if there were no errored test cases. If you would like to change this behavior, you can pass an unhandled score function to your `Eval` call. We provide a default handler that logs 0% values to any score that doesn't complete successfully.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Eval, defaultErrorScoreHandler } from "braintrust";
  import { Factuality } from "autoevals";

  Eval(
    "Say Hi Bot", // Replace with your project name
    {
      data: () => {
        return [
          {
            input: "foo",
          },
        ];
      },
      task: (input) => {
        throw new Error("Task error");
      },
      scores: [Factuality],
      errorScoreHandler: defaultErrorScoreHandler, // Replace with your own custom function
    },
  );
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from autoevals import Factuality
  from braintrust import Eval, framework

  def error_task(input):
      raise Exception("Task error")

  Eval(
      "Say Hi Bot",  # Replace with your project name
      data=lambda: [
          {
              "input": "foo",
          },
      ],
      task=error_task,
      scores=[Factuality],
      error_score_handler=framework.default_error_score_handler,  # Replace with your own custom function
  )
  ```
</CodeGroup>

#### Return a list of scorers

You can also return a list of scorers from a scorer function. This allows you to dynamically generate scores based on the input data, or even combine scores together into a single score. When you return a list of scores, you must return a `Score` object, which has a `name` and a `score` field.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { NumericDiff } from "autoevals";

  interface QueryInput {
    type: string;
    text: string;
  }

  const calculatorAccuracy = ({
    input,
    output,
  }: {
    input: QueryInput;
    output: number;
  }) => {
    if (input.type !== "calculator") {
      return null;
    }
    return [
      {
        name: "Numeric diff",
        score: NumericDiff({ output, expected: eval(input.text) }),
      },
      {
        name: "Exact match",
        score: output === eval(input.text) ? 1 : 0,
      },
    ];
  };
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from autoevals import NumericDiff, Score

  def calculator_accuracy(input, output, **kwargs):
      if input["type"] != "calculator":
          return None

      return [
          NumericDiff()(output=output, expected=eval(input["text"])),
          Score(
              name="Exact match",
              score=1 if output == eval(input["text"]) else 0,
          ),
      ]
  ```
</CodeGroup>

### Allow additional fields in scorers

Certain scorers, like [ClosedQA](https://github.com/braintrustdata/autoevals/blob/main/templates/closed_q_a.yaml), allow additional fields to be passed in. You can pass them in by initializing them with `.partial(...)`.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Eval, wrapOpenAI } from "braintrust";
  import { ClosedQA } from "autoevals";
  import { OpenAI } from "openai";

  const client = wrapOpenAI(
    new OpenAI({
      apiKey: process.env.OPENAI_API_KEY,
    }),
  );

  Eval("QA bot", {
    data: () => [
      {
        input: "Which insect has the highest population?",
        expected: "ant",
      },
    ],
    task: async (input) => {
      const response = await client.chat.completions.create({
        model: "gpt-4o",
        messages: [
          {
            role: "system",
            content:
              "Answer the following question. Specify how confident you are (or not)",
          },
          { role: "user", content: "Question: " + input },
        ],
      });
      return response.choices[0].message.content || "Unknown";
    },
    scores: [
      ClosedQA.partial({
        criteria:
          "Does the submission specify whether or not it can confidently answer the question?",
      }),
    ],
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  from autoevals import ClosedQA
  from braintrust import Eval, wrap_openai
  from openai import OpenAI

  openai = wrap_openai(OpenAI(api_key=os.environ["OPENAI_API_KEY"]))

  Eval(
      "QA bot",
      data=lambda: [
          {
              "input": "Which insect has the highest population?",
              "expected": "ant",
          },
      ],
      task=lambda input: openai.chat.completions.create(
          model="gpt-4o",
          messages=[
              {"role": "system", "content": "Answer the following question."},
              {"role": "user", "content": "Question: " + input},
          ],
      )
      .choices[0]
      .message.content
      or "Unknown",
      scores=[
          ClosedQA.partial(criteria="Does the submission specify whether or not it can confidently answer the question?")
      ],
  )
  ```
</CodeGroup>

This approach works well if the criteria is static, but if the criteria is dynamic, you can pass them in via a wrapper function, e.g.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Eval, wrapOpenAI } from "braintrust";
  import { ClosedQA } from "autoevals";
  import { OpenAI } from "openai";

  const openai = wrapOpenAI(new OpenAI({ apiKey: process.env.OPENAI_API_KEY }));

  interface Metadata {
    criteria: string;
  }

  const closedQA = (args: {
    input: string;
    output: string;
    metadata: Metadata;
  }) => {
    return ClosedQA({
      input: args.input,
      output: args.output,
      criteria: args.metadata.criteria,
    });
  };

  Eval("QA bot", {
    data: () => [
      {
        input: "Which insect has the highest population?",
        expected: "ant",
        metadata: {
          criteria:
            "Does the submission specify whether or not it can confidently answer the question?",
        },
      },
    ],
    task: async (input) => {
      const response = await openai.chat.completions.create({
        model: "gpt-3.5-turbo",
        messages: [
          {
            role: "system",
            content:
              "Answer the following question. Specify how confident you are (or not)",
          },
          { role: "user", content: "Question: " + input },
        ],
      });
      return response.choices[0].message.content || "Unknown";
    },
    scores: [closedQA],
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from autoevals import ClosedQA
  from braintrust import Eval, wrap_openai
  from openai import OpenAI

  openai = wrap_openai(OpenAI())

  def closed_q_a(input, output, metadata):
      # NOTE: You need to instantiate the scorer class before passing
      # arguments to it directly.
      return ClosedQA()(
          input=input,
          output=output,
          criteria=metadata["criteria"],
      )

  Eval(
      "QA bot",
      data=lambda: [
          {
              "input": "Which insect has the highest population?",
              "expected": "ant",
              "metadata": {
                  "criteria": "Does the submission specify whether or not it can confidently answer the question?",
              },
          },
      ],
      task=lambda input: openai.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
              {
                  "role": "system",
                  "content": "Answer the following question. Specify how confident you are (or not)",
              },
              {"role": "user", "content": "Question: " + input},
          ],
      )
      .choices[0]
      .message.content
      or "Unknown",
      scores=[closed_q_a],
  )
  ```
</CodeGroup>

### Compose scorers

Sometimes, it's useful to build scorers that call other scorers. For example, if you're building a translation app, you could reverse translate the output, and use `EmbeddingSimilarity` to compare it to the original input.

To compose scorers, call one scorer from another.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { EmbeddingSimilarity } from "autoevals";
  import { Eval, wrapOpenAI } from "braintrust";
  import OpenAI from "openai";

  const client = wrapOpenAI(
    new OpenAI({
      apiKey: process.env.OPENAI_API_KEY,
    }),
  );

  async function translationScore({
    input,
    output,
  }: {
    input: string;
    output: string;
  }) {
    const completion = await client.chat.completions.create({
      model: "gpt-4o",
      messages: [
        {
          role: "system",
          content:
            "You are a helpful assistant that translates from French to English.",
        },
        { role: "user", content: output },
      ],
    });
    const reverseTranslated = completion.choices[0].message.content ?? "";
    const similarity = await EmbeddingSimilarity({
      output: reverseTranslated,
      expected: input,
    });
    return {
      name: "TranslationScore",
      score: similarity.score,
      metadata: {
        original: input,
        translated: output,
        reverseTranslated,
      },
    };
  }

  Eval("Translate", {
    data: [
      { input: "May I order a pizza?" },
      { input: "Where is the nearest bank?" },
    ],
    task: async (input) => {
      const completion = await client.chat.completions.create({
        model: "gpt-4o",
        messages: [
          {
            role: "system",
            content:
              "You are a helpful assistant that translates from English to French.",
          },
          { role: "user", content: input },
        ],
      });
      return completion.choices[0].message.content ?? "";
    },
    scores: [translationScore],
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  from autoevals import EmbeddingSimilarity, Score
  from braintrust import Eval, wrap_openai
  from openai import OpenAI

  client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

  def translation_score(input, output):
      completion = client.chat.completions.create(
          model="gpt-4o",
          messages=[
              {"role": "system", "content": "You are a helpful assistant that translates from French to English."},
              {"role": "user", "content": output},
          ],
      )
      reverse_translated = completion.choices[0].message.content
      similarity = EmbeddingSimilarity()(output=reverse_translated, expected=input)
      return Score(
          name="TranslationScore",
          score=similarity.score,
          metadata={"original": input, "translated": output, "reverseTranslated": reverse_translated},
      )

  def task(input):
      completion = client.chat.completions.create(
          model="gpt-4o",
          messages=[
              {"role": "system", "content": "You are a helpful assistant that translates from English to French."},
              {"role": "user", "content": input},
          ],
      )
      return completion.choices[0].message.content

  Eval(
      "Translate",
      data=[
          {"input": "May I order a pizza?"},
          {"input": "Where is the nearest bank?"},
      ],
      task=task,
      scores=[translation_score],
  )
  ```
</CodeGroup>

## Add custom metrics

Sometimes, you need to measure counts or other numbers that cannot be normalized to `[0,1]`. In Braintrust, these are called metrics, and they can be aggregated just like scores, but have less built-in semantic meaning. Braintrust automatically collects several metrics, like token usage, duration, and error counts, but you can also add your own.

For example, to log a metric corresponding to the number of docs retrieved, you can write:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { currentSpan } from "braintrust";

  async function processText(text: string) {
    const words = text.split(/\s+/);
    const sentences = text.split(/[.!?]+/).filter((s) => s.trim().length > 0);

    // Log custom metrics about the text processing
    currentSpan().log({
      metrics: {
        wordCount: words.length,
        sentenceCount: sentences.length,
      },
    });

    return { words, sentences };
  }
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import re

  from braintrust import current_span

  async def process_text(text: str):
      words = text.split()
      sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]

      # Log custom metrics about the text processing
      current_span().log(metrics={"wordCount": len(words), "sentenceCount": len(sentences)})

      return {"words": words, "sentences": sentences}
  ```
</CodeGroup>

### Aggregate metrics

Metrics can be aggregated within a trace (for example, to report in the experiment table) and across traces (for example, to report their performance at the experiment level). For the most part, metrics are aggregated by sum, for example token counts, but there are some exceptions, like `duration` which is the max of `metrics.end-metrics.start` across spans within a trace.

Any custom metrics you log will be summed.

## Add additional metadata

### Add metadata while executing the task function

Although you can provide `metadata` about each test case in the `data` function, it can be helpful to add additional metadata while your `task` is executing. The second argument to `task` is a `hooks` object, which allows you to read and update metadata on the test case.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Eval } from "braintrust";
  import { Factuality } from "autoevals";

  Eval(
    "Say Hi Bot", // Replace with your project name
    {
      data: () => [
        {
          input: "David",
          expected: "Hi David",
        },
      ],
      task: (input, hooks) => {
        hooks.metadata.flavor = "apple";
        return "Hi " + input; // Replace with your LLM call
      },
      scores: [Factuality],
    },
  );
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from autoevals import Factuality
  from braintrust import Eval

  def task(input, hooks):
      hooks.metadata["flavor"] = "apple"
      return "Hi " + input

  Eval(
      "Say Hi Bot",  # Replace with your project name
      data=lambda: [
          {
              "input": "David",
              "expected": "Hi David",
          },
      ],
      task=task,
      scores=[Factuality],
  )
  ```
</CodeGroup>

### Add metadata to a scoring function

To make it easier to debug logs that do not produce a good score, you may want to log additional values in addition to the output of a scoring function. To do this, you can add a `metadata` field to the return value of your function, for example:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { wrapOpenAI } from "braintrust";
  import OpenAI from "openai";

  const client = wrapOpenAI(new OpenAI({ apiKey: process.env.OPENAI_API_KEY }));

  async function precisionRecallScore({
    input,
    output,
    expected,
  }: {
    input: string;
    output: string[];
    expected: string[];
  }) {
    const truePositives = output.filter((item) => expected.includes(item));
    const falsePositives = output.filter((item) => !expected.includes(item));
    const falseNegatives = expected.filter((item) => !output.includes(item));

    const precision = truePositives.length / (output.length || 1);
    const recall = truePositives.length / (expected.length || 1);

    return {
      name: "PrecisionRecallScore",
      score: (precision + recall) / 2, // F1-style simple average
      metadata: {
        truePositives,
        falsePositives,
        falseNegatives,
        precision,
        recall,
      },
    };
  }
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  from braintrust import wrap_openai
  from openai import OpenAI

  client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

  def precision_recall_score(input: str, output: list[str], expected: list[str]):
      true_positives = [item for item in output if item in expected]
      false_positives = [item for item in output if item not in expected]
      false_negatives = [item for item in expected if item not in output]

      precision = len(true_positives) / (len(output) or 1)
      recall = len(true_positives) / (len(expected) or 1)

      return {
          "name": "PrecisionRecallScore",
          "score": (precision + recall) / 2,  # F1-style simple average
          "metadata": {
              "truePositives": true_positives,
              "falsePositives": false_positives,
              "falseNegatives": false_negatives,
              "precision": precision,
              "recall": recall,
          },
      }
  ```
</CodeGroup>

### Add experiment-level metadata

It can be useful to add custom metadata to your experiments, for example, to store information about the model or other parameters that you use.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Eval } from "braintrust";
  import { Factuality } from "autoevals";

  Eval(
    "Say Hi Bot", // Replace with your project name
    {
      data: () => [
        {
          input: "David",
          expected: "Hi David",
        },
      ],
      task: (input) => {
        return "Hi " + input; // Replace with your task function
      },
      scores: [Factuality],
      metadata: {
        model: "gpt-4o",
      }, // Replace with whatever metadata you want to add
    },
  );
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from autoevals import Factuality
  from braintrust import Eval

  Eval(
      "Say Hi Bot",  # Replace with your project name
      data=lambda: [
          {
              "input": "David",
              "expected": "Hi David",
          },
      ],  # Replace with your eval dataset
      task=lambda input: "Hi " + input,  # Replace with your task function
      scores=[Factuality],
      metadata={"model": "gpt-4o"}, # Replace with whatever metadata you want to add
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
  		Experiment: "Say Hi Bot", // Replace with your project name
  		Dataset: eval.NewDataset([]eval.Case[string, string]{
  			{Input: "David", Expected: "Hi David"},
  		}), // Replace with your eval dataset
  		Task: eval.T(func(ctx context.Context, input string) (string, error) {
  			return "Hi " + input, nil
  		}), // Replace with your task function
  		Scorers: []eval.Scorer[string, string]{
  			eval.NewScorer("exact-match", func(ctx context.Context, r eval.TaskResult[string, string]) (eval.Scores, error) {
  				score := 0.0
  				if r.Output == r.Expected {
  					score = 1.0
  				}
  				return eval.S(score), nil
  			}),
  		}, // Replace with your scoring functions
  		Metadata: map[string]any{
  			"model": "gpt-4o",
  		}, // Replace with the metadata you want to add
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
    project: "Say Hi Bot", # Replace with your project name
    cases: [
      {input: "David", expected: "Hi David"},
    ], # Replace with your eval dataset
    task: ->(input) { "Hi #{input}" }, # Replace with your task function
    scorers: [
      Braintrust::Eval.scorer("exact_match") do |input, expected, output, metadata|
        output == expected ? 1.0 : 0.0
      end
    ], # Replace with your scoring functions
    metadata: {model: "gpt-4o"} # Replace with the metadata you want to add
  )

  OpenTelemetry.tracer_provider.shutdown
  ```
</CodeGroup>

Once you set metadata, you can view and filter by it on the Experiments page:

<video className="border rounded-md" src="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/metadata-filter.mov?fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=2a289d5e2c0c9631d605df3a7bc72bd1" loop autoPlay muted poster="/images/core/experiments/metadata-filter-poster.png" data-path="images/core/experiments/metadata-filter.mov" />

You can also construct complex analyses across experiments. See [Analyze across experiments](./interpret#analyze-across-experiments) for more details.

## Use custom prompts/functions from Braintrust

In addition to writing code directly in your evals, you can also use custom prompts and functions that you host in Braintrust in your code. Use cases include:

* Running a code-based eval on a prompt that lives in Braintrust.
* Using a hosted scorer in your evals.
* Using a scorer written in a different language than your eval code (e.g. calling a Python scorer from a TypeScript eval).

You can reference a hosted prompt or scorer by using the `initFunction`/`init_function` function.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Eval, initFunction } from "braintrust";
  import { Factuality } from "autoevals";

  Eval("custom-function", {
    data: [
      {
        input: "Joe",
        expected: "Hi Joe",
      },
      {
        input: "Jane",
        expected: "Hello Jane",
      },
    ],
    task: initFunction({
      projectName: "custom-function",
      slug: "hi-prompt",
    }),
    scores: [
      initFunction({
        projectName: "custom-function",
        slug: "exact-match-scorer",
      }),
    ],
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import Eval, init_function

  Eval(
      "custom-function",
      data=[
          {
              "input": "Joe",
              "expected": "Hi Joe",
          },
          {
              "input": "Jane",
              "expected": "Hello Jane",
          },
      ],
      task=init_function(project_name="custom-function", slug="hi-prompt"),
      scores=[
          init_function(project_name="custom-function", slug="exact-match-scorer"),
      ],
  )
  ```
</CodeGroup>

## Run trials

It is often useful to run each input in an evaluation multiple times, to get a sense of the variance in responses and get a more robust overall score. Braintrust supports *trials* as a first-class concept, allowing you to run each input multiple times. Behind the scenes, Braintrust will intelligently aggregate the results by bucketing test cases with the same `input` value and computing summary statistics for each bucket.

To enable trials, add a `trialCount`/`trial_count` property to your evaluation:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Eval } from "braintrust";
  import { Factuality } from "autoevals";

  Eval(
    "Say Hi Bot", // Replace with your project name
    {
      data: () => {
        return [
          {
            input: "David",
            expected: "Hi David",
          },
        ];
      }, // Replace with your eval dataset
      task: (input) => {
        return "Hi " + input;
      }, // Replace with your LLM call
      scores: [Factuality], // Replace with your scoring functions
      trialCount: 10, // Replace with the number of trials you want to run
    },
  );
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from autoevals import Factuality
  from braintrust import Eval

  Eval(
      "Say Hi Bot",  # Replace with your project name
      data=lambda: [
          {
              "input": "David",
              "expected": "Hi David",
          },
      ],  # Replace with your eval dataset
      task=lambda input: "Hi " + input,  # Replace with your task function
      scores=[Factuality], # Replace with your scoring functions
      trial_count=10, # Replace with the number of trials you want to run
  )
  ```
</CodeGroup>

## Enable hill climbing

Sometimes you do not have expected outputs, and instead want to use a previous experiment as a baseline. Hill climbing is inspired by, but not exactly the same as, the term used in [numerical optimization](https://en.wikipedia.org/wiki/Hill_climbing).

In the context of Braintrust, hill climbing is a way to iteratively improve a model's performance by comparing new experiments to previous ones. This is especially useful when you don't have a pre-existing benchmark to evaluate against.

Braintrust supports hill climbing as a first-class concept, allowing you to use a previous experiment's `output` field as the `expected` field for the current experiment. Autoevals also includes a number of scorers, like `Summary` and `Battle`, that are designed to work well with hill climbing.

To enable hill climbing, use `BaseExperiment()` in the `data` field of an eval:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Battle } from "autoevals";
  import { Eval, BaseExperiment } from "braintrust";

  Eval<string, string, string>(
    "Say Hi Bot", // Replace with your project name
    {
      data: BaseExperiment(),
      task: (input) => {
        return "Hi " + input; // Replace with your task function
      },
      scores: [Battle.partial({ instructions: "Which response said 'Hi'?" })],
    },
  );
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from autoevals import Battle
  from braintrust import BaseExperiment, Eval

  Eval(
      "Say Hi Bot",  # Replace with your project name
      data=BaseExperiment(),
      task=lambda input: "Hi " + input,  # Replace with your task function
      scores=[Battle.partial(instructions="Which response said 'Hi'?")],
  )
  ```
</CodeGroup>

Braintrust will automatically pick the best base experiment, either using git metadata if available or timestamps otherwise, and then populate the `expected` field by merging the `expected` and `output` field of the base experiment. This means that if you set `expected`, e.g. through the UI while reviewing results, it will be used as the `expected` field for the next experiment.

**Using a specific experiment**

If you want to use a specific experiment as the base experiment, you can pass the `name` field to `BaseExperiment()`:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Battle } from "autoevals";
  import { Eval, BaseExperiment } from "braintrust";

  Eval<string, string, string>(
    "Say Hi Bot", // Replace with your project name
    {
      data: BaseExperiment({ name: "main-123" }),
      task: (input) => {
        return "Hi " + input; // Replace with your task function
      },
      scores: [Battle.partial({ instructions: "Which response said 'Hi'?" })],
    },
  );
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from autoevals import Battle
  from braintrust import BaseExperiment, Eval

  Eval(
      "Say Hi Bot",  # Replace with your project name
      data=BaseExperiment(name="main-123"),
      task=lambda input: "Hi " + input,  # Replace with your task function
      scores=[Battle.partial(instructions="Which response said 'Hi'?")],
  )
  ```
</CodeGroup>

### Scoring considerations

Often while hill climbing, you want to use two different types of scoring functions:

* Methods that do not require an expected output, e.g. `ClosedQA`, so that you can judge the quality of the output purely based on the input and output. This measure is useful to track across experiments, and it can be used to compare any two experiments, even if they are not sequentially related.
* Comparative methods, e.g. `Battle` or `Summary`, that accept an `expected` output but do not treat it as a ground truth. Generally speaking, if you score > 50% on a comparative method, it means you're doing better than the base on average. To learn more about how `Battle` and `Summary` work, check out [their prompts](https://github.com/braintrustdata/autoevals/tree/main/templates).

## Create custom reporters

When you run an experiment, Braintrust logs the results to your terminal, and `braintrust eval` returns a non-zero exit code if any eval throws an exception. However, it's often useful to customize this behavior, e.g. in your CI/CD pipeline to precisely define what constitutes a failure, or to report results to a different system.

Braintrust allows you to define custom reporters that can be used to process and log results anywhere you'd like. You can define a reporter by adding a `Reporter(...)` block. A Reporter has two functions:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Reporter } from "braintrust";

  Reporter(
    "My reporter", // Replace with your reporter name
    {
      reportEval(evaluator, result, opts) {
        // Summarizes the results of a single reporter, and return whatever you
        // want (the full results, a piece of text, or both!)
      },

      reportRun(results) {
        // Takes all the results and summarizes them. Return a true or false
        // which tells the process to exit.
        return true;
      },
    },
  );
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import Reporter

  def report_eval(evaluator, result, opts):
      # Summarizes the results of a single reporter, and return whatever you
      # want (the full results, a piece of text, or both!)
      pass

  def report_run(results):
      # Takes all the results and summarizes them. Return a true or false
      # which tells the process to exit.
      return True

  Reporter(
      "My reporter",  # Replace with your reporter name
      report_eval=report_eval,
      report_run=report_run,
  )
  ```
</CodeGroup>

Any `Reporter` included among your evaluated files will be automatically picked up by the `braintrust eval` command.

* If no reporters are defined, the default reporter will be used which logs the results to the console.
* If you define one reporter, it'll be used for all `Eval` blocks.
* If you define multiple `Reporter`s, you have to specify the reporter name as an optional 3rd argument to `Eval()`.

**Example: the default reporter**

As an example, here's the default reporter that Braintrust uses:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Reporter, reportFailures } from "braintrust";

  Reporter("Braintrust default reporter", {
    reportEval: async (evaluator, result, { verbose, jsonl }) => {
      const { results, summary } = result;
      const failingResults = results.filter(
        (r: { error: unknown }) => r.error !== undefined,
      );

      if (failingResults.length > 0) {
        reportFailures(evaluator, failingResults, { verbose, jsonl });
      }

      console.log(jsonl ? JSON.stringify(summary) : summary);
      return failingResults.length === 0;
    },
    reportRun: async (evalReports: boolean[]) => {
      return evalReports.every((r) => r);
    },
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import json

  from braintrust import Reporter
  from braintrust.framework import report_failures

  def report_eval(evaluator, result, verbose, jsonl):
      results = result.results
      summary = result.summary

      failing_results = [x for x in results if x.error]
      if len(failing_results) > 0:
          report_failures(evaluator, failing_results, verbose=verbose, jsonl=jsonl)
      else:
          print(json.dumps(summary.as_dict()) if jsonl else f"{summary}")

      return len(failing_results) == 0

  def report_run(eval_reports, verbose, jsonl):
      return all(x for x in eval_reports)

  Reporter(
      "default",
      report_eval=report_eval,
      report_run=report_run,
  )
  ```
</CodeGroup>

## Include attachments

Braintrust allows you to log arbitrary binary data, like images, audio, and PDFs, as [attachments](/guides/traces/customize#uploading-attachments). The easiest way to use attachments in your evals is to initialize an `Attachment` object in your
data.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Eval, Attachment } from "braintrust";
  import { NumericDiff } from "autoevals";
  import path from "path";

  function loadPdfs() {
    return ["example.pdf"].map((pdf) => ({
      input: {
        file: new Attachment({
          filename: pdf,
          contentType: "application/pdf",
          data: path.join("files", pdf),
        }),
      },
      // This is a toy example where we check that the file size is what we expect.
      expected: 469513,
    }));
  }

  async function getFileSize(input: { file: Attachment }) {
    return (await input.file.data()).size;
  }

  Eval("Project with PDFs", {
    data: loadPdfs,
    task: getFileSize,
    scores: [NumericDiff],
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os
  from typing import Any, Dict, Iterable

  from autoevals import NumericDiff
  from braintrust import Attachment, Eval, EvalCase

  def load_pdfs() -> Iterable[EvalCase[Dict[str, Any], int]]:
      for filename in ["example.pdf"]:
          yield EvalCase(
              input={
                  "file": Attachment(
                      filename=filename,
                      content_type="application/pdf",
                      # The file on your filesystem or the file's bytes.
                      data=os.path.join("files", filename),
                  )
              },
              # This is a toy example where we check that the file size is what we expect.
              expected=469513,
          )

  def get_file_size(input: Dict[str, Any]) -> int:
      return len(input["file"].data)

  # Our evaluation uses a `NumericDiff` scorer to check the file size.
  Eval(
      "Project with PDFs",
      data=load_pdfs(),
      task=get_file_size,
      scores=[NumericDiff],
  )
  ```
</CodeGroup>

You can also [store attachments in a dataset](/core/datasets#multimodal-datasets) for reuse across multiple experiments. After creating the dataset, you can use it by name in an eval. Upon access, the attachment data will be automatically downloaded from Braintrust.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { NumericDiff } from "autoevals";
  import { initDataset, Eval, ReadonlyAttachment } from "braintrust";

  async function getFileSize(input: {
    file: ReadonlyAttachment;
  }): Promise<number> {
    return (await input.file.data()).size;
  }

  Eval("Project with PDFs", {
    data: initDataset({
      project: "Project with PDFs",
      dataset: "My PDF Dataset",
    }),
    task: getFileSize,
    scores: [NumericDiff],
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from autoevals import NumericDiff
  from braintrust import Eval, init_dataset

  def get_file_size(input: Dict[str, Any]) -> int:
      """Download the attachment and get its length."""
      return len(input["file"].data)

  Eval(
      "Project with PDFs",
      data=init_dataset("Project with PDFs", "My PDF Dataset"),
      task=get_file_size,
      scores=[NumericDiff],
  )
  ```
</CodeGroup>

You can also obtain a signed URL for the attachment for forwarding to other services, such as OpenAI.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { initDataset, wrapOpenAI, ReadonlyAttachment } from "braintrust";
  import { OpenAI } from "openai";

  const client = wrapOpenAI(
    new OpenAI({
      apiKey: process.env.OPENAI_API_KEY,
    }),
  );

  async function main() {
    const dataset = initDataset({
      project: "Project with images",
      dataset: "My Image Dataset",
    });
    for await (const row of dataset) {
      const attachment: ReadonlyAttachment = row.input.file;
      const attachmentUrl = (await attachment.metadata()).downloadUrl;
      const response = await client.chat.completions.create({
        model: "gpt-4o",
        messages: [
          {
            role: "system",
            content: "You are a helpful assistant",
          },
          {
            role: "user",
            content: [
              { type: "text", text: "Please summarize the attached image" },
              { type: "image_url", image_url: { url: attachmentUrl } },
            ],
          },
        ],
      });
      const summary = response.choices[0].message.content || "Unknown";
      console.log(
        `Summary for file ${attachment.reference.filename}: ${summary}`,
      );
    }
  }

  main();
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import init_dataset, wrap_openai
  from openai import OpenAI

  openai = wrap_openai(OpenAI(api_key=os.environ["OPENAI_API_KEY"]))

  def main():
      dataset = init_dataset("Project with images", "My Image Dataset")
      for row in dataset:
          attachment = row["input"]["file"]
          attachment_url = attachment.metadata()["downloadUrl"]
          response = openai.chat.completions.create(
              model="gpt-4o",
              messages=[
                  {"role": "system", "content": "You are a helpful assistant"},
                  {
                      "role": "user",
                      "content": [
                          {"type": "text", "text": "Please summarize the attached image"},
                          {"type": "image_url", "image_url": {"url": attachment_url}},
                      ],
                  },
              ],
          )
          summary = response.choices[0].message.content or "Unknown"
          print(f"Summary for file {attachment.reference['filename']}: {summary}")

  main()
  ```
</CodeGroup>

## Trace your evals

Braintrust allows you to trace detailed debug information and metrics about your application that you can use to measure performance and debug issues. The trace is a tree of spans, where each span represents an expensive task, e.g. an LLM call, vector database lookup, or API request.

<Note>
  If you are using the OpenAI API, Braintrust includes a wrapper function that
  automatically logs your requests. To use it, call
  `wrapOpenAI/wrap_openai` on your OpenAI instance. See [Wrapping
  OpenAI](/guides/traces/customize#wrapping-openai)
  for more info.
</Note>

<Note>
  Each call to `experiment.log()` creates its own trace, starting at the time of the previous log statement and ending at the completion of the current. Do not mix `experiment.log()` with tracing. It will result in extra traces that are not correctly parented.
</Note>

For more detailed tracing, you can wrap existing code with the `braintrust.traced` function. Inside the wrapped function, you can log incrementally to `braintrust.currentSpan()`. For example, you can progressively log the input, output, and expected output of a task, and then log a score at the end:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Eval, traced } from "braintrust";

  async function callModel(input: string) {
    return traced(
      async (span) => {
        const messages = { messages: [{ role: "system", text: input }] };
        span.log({ input: messages });

        // Replace this with a model call
        const result = {
          content: "China",
          latency: 1,
          prompt_tokens: 10,
          completion_tokens: 2,
        };

        span.log({
          output: result.content,
          metrics: {
            latency: result.latency,
            prompt_tokens: result.prompt_tokens,
            completion_tokens: result.completion_tokens,
          },
        });
        return result.content;
      },
      {
        name: "My AI model",
      },
    );
  }

  const exactMatch = (args: {
    input: string;
    output: string;
    expected?: string;
  }) => {
    return {
      name: "Exact match",
      score: args.output === args.expected ? 1 : 0,
    };
  };

  Eval("My Evaluation", {
    data: () => [
      { input: "Which country has the highest population?", expected: "China" },
    ],
    task: async (input, { span }) => {
      return await callModel(input);
    },
    scores: [exactMatch],
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import Eval, current_span, traced

  @traced
  async def call_model(input):
      messages = dict(
          messages=[
              dict(role="system", text=input),
          ]
      )
      current_span().log(input=messages)

      # Replace this with a model call
      result = {
          "content": "China",
          "latency": 1,
          "prompt_tokens": 10,
          "completion_tokens": 2,
      }
      current_span().log(
          output=result["content"],
          metrics=dict(
              latency=result["latency"],
              prompt_tokens=result["prompt_tokens"],
              completion_tokens=result["completion_tokens"],
          ),
      )
      return result["content"]

  async def run_input(input):
      return await call_model(input)

  def exact_match(input, expected, output):
      return 1 if output == expected else 0

  Eval(
      "My Evaluation",
      data=[dict(input="Which country has the highest population?", expected="China")],
      task=run_input,
      scores=[exact_match],
  )
  ```
</CodeGroup>

This results in a span tree you can visualize in the UI by clicking on each test case in the experiment:

<img src="https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/trace-anatomy.png?fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=4d5b7695ee4938679a44368b6ec37515" alt="Root Span" data-og-width="1600" width="1600" data-og-height="1160" height="1160" data-path="images/guides/traces/trace-anatomy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/trace-anatomy.png?w=280&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=9089e5674ca417712fe2596505419cb3 280w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/trace-anatomy.png?w=560&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=e7a4bf93ec48a978a823f877add66427 560w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/trace-anatomy.png?w=840&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=f81c08e71c492e490f9e7dea4a6a112d 840w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/trace-anatomy.png?w=1100&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=2f60a9169dd05cabcc37e086986a5197 1100w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/trace-anatomy.png?w=1650&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=a8d6ba63237bca6fd85220e6198381db 1650w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/trace-anatomy.png?w=2500&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=1898034c5e9cff7b1d64aaff6c7f28cc 2500w" />
<img src="https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/span.png?fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=4533b340305efe9ea0131c81ca1e01fa" alt="Subspan" data-og-width="4146" width="4146" data-og-height="3054" height="3054" data-path="images/guides/traces/span.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/span.png?w=280&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=d71101907ac6fbde361f6e3ecd81005b 280w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/span.png?w=560&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=6b8965d81dbdccb77675d251fea05470 560w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/span.png?w=840&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=d2e53b43acee35ffe571b2e5556f98d2 840w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/span.png?w=1100&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=1bd9af4a53656126d1c091acda033dbd 1100w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/span.png?w=1650&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=df752c23d8e619fcbbacf4b9b325b347 1650w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/span.png?w=2500&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=b305df8971d68d67fc476568bf0454ed 2500w" />

## Log evals using the SDK

The SDK allows you to report evaluation results directly from your code, without using the `Eval()` or `.traced()` functions. This is useful if you want to structure your own complex evaluation logic, or integrate Braintrust with an existing testing or evaluation framework.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import * as braintrust from "braintrust";
  import { Factuality } from "autoevals";

  async function runEvaluation() {
    const experiment = braintrust.init("Say Hi Bot"); // Replace with your project name
    const dataset = [{ input: "David", expected: "Hi David" }]; // Replace with your eval dataset

    const promises = [];
    for (const { input, expected } of dataset) {
      // You can await here instead to run these sequentially
      promises.push(
        experiment.traced(async (span) => {
          const output = "Hi David"; // Replace with your LLM call

          const { name, score } = await Factuality({ input, output, expected });

          span.log({
            input,
            output,
            expected,
            scores: {
              [name]: score,
            },
            metadata: { type: "Test" },
          });
        }),
      );
    }
    await Promise.all(promises);

    const summary = await experiment.summarize();
    console.log(summary);
    return summary;
  }

  runEvaluation();
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import braintrust
  from autoevals import Factuality

  def run_evaluation():
      experiment = braintrust.init(project="Say Hi Bot")  # Replace with your project name
      dataset = [
          {"input": "David", "expected": "Hi David"},
      ]  # Replace with your eval dataset

      for data in dataset:
          with experiment.start_span(name="task") as span:
              input = data["input"]
              expected = data["expected"]

              output = "Hi David"  # Replace with your LLM call

              factuality = Factuality()
              factualityScore = factuality(output, expected, input=input)

              span.log(
                  input=input,
                  output=output,
                  expected=expected,
                  scores={
                      factualityScore.name: factualityScore.score,
                  },  # The scores dictionary
                  metadata={"type": "Test"},  # The metadata dictionary
              )

      summary = experiment.summarize(summarize_scores=True)
      print(summary)
      return summary

  run_evaluation()
  ```
</CodeGroup>

Refer to the [tracing](/guides/traces) guide for examples of how to trace evaluations using the low-level SDK. For more details on how to use the low level SDK, see the [Python](/reference/sdks/python) or [Node.js](/reference/sdks/typescript)
documentation.

## Troubleshooting

### Exception when mixing `log` with `traced`

There are two ways to log to Braintrust: `Experiment.log` and
`Experiment.traced`. `Experiment.log` is for non-traced logging, while
`Experiment.traced` is for tracing. This exception is thrown when you mix both
methods on the same object, for instance:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { init, traced } from "braintrust";

  function foo() {
    return traced((span) => {
      const output = 1;
      span.log({ output });
      return output;
    });
  }

  const experiment = init("my-project");
  for (let i = 0; i < 10; ++i) {
    const output = foo();
    // ❌ This will throw an exception, because we have created a trace for `foo`
    // with `traced` but here we are logging to the toplevel object, NOT the
    // trace.
    experiment.log({ input: "foo", output, scores: { rating: 1 } });
  }
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import init, traced

  @traced
  def foo():
      return 1

  experiment = init("my-project")
  for i in range(10):
      output = foo()
      # This will throw an exception, because we have created a trace for `foo`
      # with `@traced` but here we are logging to the toplevel object, NOT the
      # trace.
      experiment.log(input="foo", output=output, scores={"rating": 1})
  ```
</CodeGroup>

Most of the time, you should use either `Experiment.log` or `Experiment.traced`, but not both, so the SDK throws an error to prevent accidentally mixing them together. For the above example, you most likely want to write:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { init, traced } from "braintrust";

  function foo() {
    return traced((span) => {
      const output = 1;
      span.log({ output });
      return output;
    });
  }

  const experiment = init("my-project");
  for (let i = 0; i < 10; ++i) {
    // Create a toplevel trace with `traced`.
    experiment.traced((span) => {
      // The call to `foo` is nested as a subspan under our toplevel trace.
      const output = foo();
      // We log to the toplevel trace with `span.log`.
      span.log({ input: "foo", output: "bar" });
    });
  }
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import init, start_span, traced

  @traced
  def foo():
      return 1

  experiment = init("my-project")
  for i in range(10):
      # Create a toplevel trace with `start_span`.
      with experiment.start_span() as span:
          # The call to `foo` is nested as a subspan under our toplevel trace.
          output = foo()
          # We log to the toplevel trace with `span.log`.
          span.log(input="foo", output="bar")
  ```
</CodeGroup>

In rare cases, if you are certain you want to mix traced and non-traced logging on the same object, you may pass the argument `allowConcurrentWithSpans: true`/`allow_concurrent_with_spans=True` to `Experiment.log`.

## Run local evals without sending logs to Braintrust

You can also run evaluations locally without creating experiments or sending data to Braintrust. In TypeScript, use the `noSendLogs` parameter. In Python, use the `no_send_logs` parameter.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Eval } from "braintrust";
  import { Factuality } from "autoevals";

  Eval(
    "Say Hi Bot", // Replace with your project name
    {
      data: () => {
        return [
          {
            input: "David",
            expected: "Hi David",
          },
        ]; // Replace with your eval dataset
      },
      task: (input) => {
        return "Hi " + input; // Replace with your LLM call
      },
      scores: [Factuality],
    },
    {
      noSendLogs: true, // Run evaluation locally without creating experiment
    },
  );
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from autoevals import Factuality
  from braintrust import Eval

  Eval(
      "Say Hi Bot",  # Replace with your project name
      data=lambda: [
          {
              "input": "David",
              "expected": "Hi David",
          },
      ],  # Replace with your eval dataset
      task=lambda input: "Hi " + input,  # Replace with your LLM call
      scores=[Factuality],
      no_send_logs=True,  # Run evaluation locally without creating experiment
  )
  ```
</CodeGroup>

When you set the parameter to true, the evaluation will:

* Run all tasks and scorers locally
* Generate a local summary of results
* Not create an experiment in Braintrust
* Not send any data to the Braintrust servers

### Access results from local evals

When running locally, you can access the detailed results and summary from the returned object:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Eval } from "braintrust";

  async function runLocalEval() {
    const result = await Eval(
      "Say Hi Bot",
      {
        data: () => [
          { input: "Alice", expected: "Hi Alice" },
          { input: "Bob", expected: "Hi Bob" },
        ],
        task: (input) => "Hi " + input,
        scores: [
          (args) => ({
            name: "exact_match",
            score: args.output === args.expected ? 1 : 0,
          }),
        ],
      },
      { noSendLogs: true },
    );

    // Access individual results
    console.log("Results:", result.results);
    for (const res of result.results) {
      console.log(
        `Input: ${res.input}, Output: ${res.output}, Scores:`,
        res.scores,
      );
    }

    // Access summary statistics
    console.log("Summary:", result.summary);
    console.log(
      "Average exact_match score:",
      result.summary.scores.exact_match?.score,
    );
  }

  runLocalEval();
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import Eval

  def exact_match(input, output, expected):
      return {"name": "exact_match", "score": 1.0 if output == expected else 0.0}

  result = Eval(
      "Say Hi Bot",
      data=[
          {"input": "Alice", "expected": "Hi Alice"},
          {"input": "Bob", "expected": "Hi Bob"},
      ],
      task=lambda input_val: "Hi " + input_val,
      scores=[exact_match],
      no_send_logs=True,
  )

  # Access individual results
  print("Results:", result.results)
  for res in result.results:
      print(f"Input: {res.input}, Output: {res.output}, Scores: {res.scores}")

  # Access summary statistics
  print("Summary:", result.summary)
  print("Average exact_match score:", result.summary.scores["exact_match"].score)
  ```
</CodeGroup>

This is equivalent to passing the `--no-send-logs` flag when using the CLI command `braintrust eval`.

## Run online evals

Although you can log scores from your application, it can be awkward and computationally intensive to run evals code in your production environment. To solve this, Braintrust supports server-side online evaluations that are automatically run asynchronously as you upload logs. You can pick from the pre-built [autoevals](/reference/autoevals) functions or your custom scorers, and define a sampling rate along with more granular filters to control which logs get evaluated.

### Configure online evals

To create an online evaluation, navigate to the **Configuration** tab in a project and create an online scoring rule.

<video className="border rounded-md" src="https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/logs/online-scoring-setup.mov?fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=08b85115044a9ae5319c9598edf440d1" loop autoPlay muted poster="/images/core/logs/Online-Scoring-Setup-Poster.png" data-path="images/core/logs/online-scoring-setup.mov" />

The score will now automatically run at the specified sampling rate for all logs in the project.

<Note>
  Note that online scoring will only be activated once a span has been fully logged. We detect this by checking for the existence of a `metrics.end` timestamp on the span, which is written automatically by the SDK when the span is finished.

  If you are logging through a different means, such as the REST API or any of our [API wrappers](/api-reference/introduction#sdks), you will have to explicitly include `metrics.end` as a Unix timestamp (we also suggest `metrics.start`) in order to activate online scoring.
</Note>

### Define custom scoring logic

In addition to the pre-built autoevals, you can define your own custom scoring logic by creating custom scorers. Currently, you can do that by visiting the [Playground](/core/playground) and creating custom scorers.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt