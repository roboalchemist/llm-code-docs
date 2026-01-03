# Source: https://braintrust.dev/docs/reference/autoevals/index.md

# Source: https://braintrust.dev/docs/index.md

# Source: https://braintrust.dev/docs/guides/traces/index.md

# Source: https://braintrust.dev/docs/guides/self-hosting/index.md

# Source: https://braintrust.dev/docs/guides/automations/index.md

# Source: https://braintrust.dev/docs/core/logs/index.md

# Source: https://braintrust.dev/docs/core/functions/index.md

# Source: https://braintrust.dev/docs/core/experiments/index.md

# Experiments

> How to write, run, and interpret evals

Experiments let you snapshot the performance of your AI application so you can improve it over time. In traditional software, performance usually refers to speed, like for example, how many milliseconds it takes to complete a request. In AI, it often refers to other measurements in addition to speed, including accuracy or quality. These types of metrics are harder to define and measure, especially at scale. Assessing the performance of an LLM application is known as evaluation.

Braintrust supports two types of evaluations:

* Offline evals are structured experiments used to compare and improve your app systematically.
* Online evals run scorers on live requests to monitor performance in real time.

Both types of evals are important for building quality AI applications.

<img src="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/eval-summary.png?fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=3f5daf1ea06a74b983c5b8e15aa3ba82" alt="Eval Screenshot" data-og-width="2634" width="2634" data-og-height="1482" height="1482" data-path="images/core/experiments/eval-summary.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/eval-summary.png?w=280&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=16ac2b3570981b2e43d457e09256dea8 280w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/eval-summary.png?w=560&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=ed03308dddfc4d45c1b241b2f19d09df 560w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/eval-summary.png?w=840&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=e40b0326d0feaeddd89a13977068f8d1 840w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/eval-summary.png?w=1100&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=b7484dfba2eeca38ead23175838f0a9f 1100w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/eval-summary.png?w=1650&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=602aeb9456ed0c7dbb69c53d40867b9b 1650w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/eval-summary.png?w=2500&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=e33c4f3b829b95f2c93580594108a85e 2500w" />

## Why are evals important?

In AI development, it's hard for teams to understand how an update will impact performance. This breaks the typical software development loop, making
iteration feel like guesswork instead of engineering.

Evaluations solve this, helping you distill the non-deterministic outputs of AI applications into an effective feedback loop that enables you
to ship more reliable, higher quality products.

Specifically, great evals help you:

* Understand whether an update is an improvement or a regression
* Quickly drill down into good / bad examples
* Diff specific examples vs. prior runs
* Avoid playing whack-a-mole

## Breaking down evals

Evals consist of 3 parts:

* Data: a set of examples to test your application on
* Task: the AI function you want to test (any function that takes in an `input` and returns an `output`)
* Scores: a set of scoring functions that take an `input`, `output`, and optional `expected` value and compute a score

You can establish an `Eval()` function with these 3 pieces:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
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

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
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
</CodeGroup>

For more details, try the [full tutorial](/evaluation).

## View experiments

Running your `Eval` function will automatically create an experiment in Braintrust,
display a summary in your Terminal, and populate the UI:

<img src="https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/eval-summary.png?fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=41b320a3688ae1c2a640c3aa3cce11cd" alt="Eval in UI" data-og-width="2634" width="2634" data-og-height="1482" height="1482" data-path="core/experiments/eval-summary.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/eval-summary.png?w=280&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=ca0ebbd1ab1fc56e6f3fe44a2d23bc18 280w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/eval-summary.png?w=560&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=f0525427cf8a723617df019c982bd3dd 560w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/eval-summary.png?w=840&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=1683f0385ee928577138470a20e12c6c 840w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/eval-summary.png?w=1100&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=65526716c60bece3761be8abd5f99611 1100w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/eval-summary.png?w=1650&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=153bcc8398970d6c2858e6255e11cc55 1650w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/eval-summary.png?w=2500&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=50663967d9c7924a153f525e10436adf 2500w" />

This gives you great visibility into how your AI application performed. You can:

* Preview each test case and score in a table
* Filter by high or low scores
* Select any individual example and see detailed tracing
* See high level scores
* Sort by improvements or regressions

## Where to go from here

* [Run your first eval with a full tutorial](/evaluation)
* [Writing evals](/core/experiments/write)
* [Running evals locally, in CI, or in production](/core/experiments/run)
* [Interpreting eval results](/core/experiments/interpret)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt