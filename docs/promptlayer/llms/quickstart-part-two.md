# Source: https://docs.promptlayer.com/quickstart-part-two.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart - Pt 2

<Info>This continues from [Quickstart Part 1](/quickstart), where we built a cake recipe generator prompt.</Info>

In Part 1, you created a prompt, tested it in the playground, and learned about versioning. Now let's evaluate prompt quality, test different models, and connect everything to your code.

## Evaluating a Prompt

Before deploying a prompt, you want to know if it's actually good. PromptLayer lets you build evaluation pipelines that score your prompt's outputs automatically.

### Creating a Dataset

Evaluations run against a dataset - a collection of test cases with inputs and expected outputs. Let's create one for our cake recipe prompt.

Click **New** → **Dataset** and name it "cake-recipes-test".

<Frame>
  <img src="https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/creating-dataset.png?fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=f25ab2f03a4d257e3f08c42e15217fde" alt="Creating a dataset" data-og-width="2634" width="2634" data-og-height="1512" height="1512" data-path="new-quickstart-images/creating-dataset.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/creating-dataset.png?w=280&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=28537ecb6dc5fef354fe05fd94d764ae 280w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/creating-dataset.png?w=560&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=10716f1493b3ff1bd722f83e27222332 560w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/creating-dataset.png?w=840&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=21cdbb1f640b342215627b1ccf2449d5 840w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/creating-dataset.png?w=1100&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=8cd16e797d1d64f58b2d8168a4dbabc8 1100w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/creating-dataset.png?w=1650&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=2fa1bf874bb62490845dca7bd050ca94 1650w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/creating-dataset.png?w=2500&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=8f21f59a720e06319c23613e6a8c1f5b 2500w" />
</Frame>

Add a few test cases. Each row needs the input variables your prompt expects (`cake_type`, `serving_size`) and optionally an expected output to compare against:

<Accordion title="Sample CSV for cake recipe dataset">
  ```csv  theme={null}
  cake_type,serving_size,expected_output
  Chocolate Cake,8,"Should include cocoa or chocolate, have clear measurements"
  Vanilla Birthday Cake,12,"Should be festive, mention frosting options"
  Gluten-Free Lemon Cake,6,"Must not include wheat flour, should use alternatives"
  Vegan Carrot Cake,10,"No eggs or dairy, should suggest substitutes"
  ```

  <a href="/onboarding-guides/example-dataset/cake-recipes.csv" download>Download this CSV</a> or add rows manually in the UI.
</Accordion>

Learn more about [Datasets](/features/evaluations/datasets).

### Creating an Eval Pipeline

Now let's build a pipeline that runs your prompt against each test case and scores the results.

Click **New** → **Evaluation** and select your dataset.

First, add a **Prompt Template** column. This runs your prompt against each row in the dataset, using the column values as input variables. The output appears in a new column.

Next, add an **LLM-as-judge** scoring column. This uses AI to score each output against criteria you define. For our recipe prompt, we might check:

* Does the recipe include all required sections (Overview, Ingredients, Instructions)?
* Are measurements provided in both metric and US units?
* Is the serving size correct?

<Frame>
  <img src="https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/llm_assertion_config.png?fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=bdecef2c970e8dcea390e6e1032ec713" alt="LLM as judge" data-og-width="1656" width="1656" data-og-height="878" height="878" data-path="new-quickstart-images/llm_assertion_config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/llm_assertion_config.png?w=280&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=64bf738eab39f41b4b1d3bc39d03a061 280w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/llm_assertion_config.png?w=560&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=47660daa7fd8b84f4336c60233c99ea1 560w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/llm_assertion_config.png?w=840&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=34acd9ee4abff5853e81730448ae49cc 840w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/llm_assertion_config.png?w=1100&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=0a12f3b2dfd2b9155436ad903ed07607 1100w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/llm_assertion_config.png?w=1650&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=cf4bbec029ff188c75de3975735a428f 1650w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/llm_assertion_config.png?w=2500&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=10cd17a5e9621dc8ccc04bdb406bf600 2500w" />
</Frame>

You can also add an **Equality Comparison** column to compare the prompt output against the `expected_output` column in your dataset.

<Frame>
  <img src="https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/eval-pipeline.png?fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=eed60b03742320f061499f0fc8e0a7bd" alt="Eval pipeline setup" data-og-width="2488" width="2488" data-og-height="1314" height="1314" data-path="new-quickstart-images/eval-pipeline.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/eval-pipeline.png?w=280&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=5be3a92fdcd0104ff6c753122e219a53 280w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/eval-pipeline.png?w=560&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=5bf7e1205fc460a5acec389ff0bb6702 560w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/eval-pipeline.png?w=840&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=badb23a1b4889eacd76095d345193fc0 840w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/eval-pipeline.png?w=1100&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=e50354572372662f833bcf812733db94 1100w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/eval-pipeline.png?w=1650&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=a9a53ddc34460dabf738bcde101930ca 1650w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/eval-pipeline.png?w=2500&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=d09a96c92117736cbfc380f43accf4c1 2500w" />
</Frame>

Run the evaluation to see scores across all test cases. Learn more about [Evaluations](/features/evaluations/overview).

<Accordion title="Other evaluation types">
  Beyond LLM-as-judge, PromptLayer supports:

  * **Human grading**: Collect scores from domain experts
  * **Equality Comparison**: Compare outputs to expected results
  * **Cosine similarity**: Measure semantic similarity between outputs
  * **Code evaluators**: Write custom Python scoring functions

  Agent nodes work the same way in eval pipelines.
</Accordion>

### Testing Different Models

Want to compare how your prompt performs across GPT, Claude, and Gemini? Create a new evaluation for model comparison.

Add multiple **Prompt Template** columns, each configured with a different model override. The pipeline runs your prompt on each model and shows results side by side.

<Frame>
  <img src="https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/model-comparison.png?fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=ab87559fb7eb88a96668c36a98426e15" alt="Comparing models" data-og-width="2506" width="2506" data-og-height="1160" height="1160" data-path="new-quickstart-images/model-comparison.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/model-comparison.png?w=280&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=6c70bc281e68e8af24bf4f3f7158c020 280w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/model-comparison.png?w=560&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=f69e595c8492deafba172df52f70bb47 560w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/model-comparison.png?w=840&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=71ca52f22d867f2b6c78bff319014420 840w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/model-comparison.png?w=1100&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=b73203b8f7746f9d6822647d2cc60bee 1100w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/model-comparison.png?w=1650&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=d84ead001ec218bdb0bd492ff581118a 1650w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/model-comparison.png?w=2500&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=88860b3f838dd78cf711b88eda2f8b9e 2500w" />
</Frame>

This helps you find the best price/performance balance for your use case. PromptLayer supports all major providers, plus any OpenAI-compatible API via [custom base URLs](/features/custom-providers).

## Historical Backtests

Once your prompt is in production, you'll have real request logs. Use these to test new prompt versions against actual user inputs.

### Creating a Historical Dataset

Go to **Datasets** and click **Add from Request History**. This opens a request log browser where you can filter and select requests.

<Frame>
  <img src="https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/add-from-request-history.png?fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=ddd3065e52d29e29d40f7ddbb153c972" alt="Adding from request history" data-og-width="2048" width="2048" data-og-height="1376" height="1376" data-path="new-quickstart-images/add-from-request-history.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/add-from-request-history.png?w=280&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=b495f3d91189715b7b316c9296c95d09 280w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/add-from-request-history.png?w=560&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=7b60b4c3084f7684bc711b2cbc270e35 560w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/add-from-request-history.png?w=840&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=267749a005f85a8d9c7d528e900a3537 840w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/add-from-request-history.png?w=1100&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=c385c9c8b1021a5b8a9b37ed995a7474 1100w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/add-from-request-history.png?w=1650&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=00448511ff7724afa04cd2d591e22e97 1650w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/add-from-request-history.png?w=2500&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=21d4c79daedf2c1687f089af646f05f7 2500w" />
</Frame>

Filter by prompt name, date range, metadata, or search content. Select the requests you want and click **Add Requests**. This captures the real inputs your users sent, along with the outputs your current prompt produced.

### Running a Backtest

Create an evaluation that runs your new prompt version against this historical dataset. Add columns for:

* **New prompt output**: The response from your updated prompt version
* **Equality Comparison**: Side-by-side comparison highlighting changes from the original output

<Frame>
  <img src="https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/backtest-results.png?fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=a32c1d28bf237b4357692a9e40b7b289" alt="Backtest results" data-og-width="2500" width="2500" data-og-height="1226" height="1226" data-path="new-quickstart-images/backtest-results.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/backtest-results.png?w=280&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=eb2d61835497827164554235bde1df91 280w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/backtest-results.png?w=560&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=eeec7fd55b0abfb6c6c6d42afee3f111 560w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/backtest-results.png?w=840&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=b407ed4b7aacd0c7f2585fa98c773c26 840w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/backtest-results.png?w=1100&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=7ecc86a5ef8840f741fbe6d77cd647ef 1100w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/backtest-results.png?w=1650&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=1ac445e558da709220fb4688be9884b8 1650w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/backtest-results.png?w=2500&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=af218f67b9243d17a764173fbf8df01c 2500w" />
</Frame>

Backtests are powerful because they show impact on real user data without needing to define exact pass/fail criteria upfront. You can quickly spot if a change produces dramatically different outputs.

Learn more about [backtesting](/features/evaluations/continuous-integration#backtesting).

## CI/CD Evaluation

Attach an evaluation pipeline to run automatically every time you save a new prompt version - similar to GitHub Actions running tests on each commit.

When saving a prompt, the commit dialog lets you select an evaluation pipeline. Choose one and click **Next**.

From then on, each new version you create will run through the eval and show its score in the version history. This makes it easy to spot regressions before they reach production.

<Frame>
  <img src="https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/ci-cd-scores.png?fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=4bdb7f891c07768c7c0fc41157030456" alt="Eval scores by version" data-og-width="1320" width="1320" data-og-height="1152" height="1152" data-path="new-quickstart-images/ci-cd-scores.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/ci-cd-scores.png?w=280&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=2e078841b3188d56b595d1702dc68ff6 280w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/ci-cd-scores.png?w=560&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=98f85acd8f79d3d27140f0475649c73e 560w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/ci-cd-scores.png?w=840&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=eb7274366e0ce64a309a93fd69bd26eb 840w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/ci-cd-scores.png?w=1100&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=831ccfe6a05cbebc010196f31956fac6 1100w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/ci-cd-scores.png?w=1650&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=f816d972baa9eb6c78183b078da12e26 1650w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/ci-cd-scores.png?w=2500&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=18bb9011928f8e9a8add2b9229220296 2500w" />
</Frame>

Learn more about [continuous integration](/features/evaluations/continuous-integration).

## Ad-Hoc Batch Runs

Evaluations aren't just for testing prompts - they're one of the best tools for running prompts in batch. Think of it like a spreadsheet where each column can be an AI-powered computation.

Upload a CSV or create a dataset, add prompt columns, run the batch, and export the results. Common use cases:

* **Data labeling**: Run GPT over production data to create labeled training datasets
* **Research**: Use web search prompts to find information about a list of companies or people
* **Content generation**: Process hundreds of items (commits, support tickets, reviews) to generate summaries or emails
* **Data enrichment**: Take a list of names and enrich with company, location, or other attributes

You don't need to build permanent evaluation infrastructure for this. One-off, ad-hoc batch runs are a perfectly valid use case. Create a dataset, add your prompt columns, run it, export, and move on.

## Connecting in Code

PromptLayer serves as the source of truth for your prompts. Your application fetches prompts by name, keeping prompt logic out of your codebase and enabling non-engineers to make changes.

### Installation

<CodeGroup>
  ```bash Python theme={null}
  pip install promptlayer
  ```

  ```bash JavaScript theme={null}
  npm install promptlayer
  ```
</CodeGroup>

### Running Prompts

Initialize the client and run a prompt. The SDK fetches the prompt template from PromptLayer, runs it against your configured LLM provider locally, then logs the result back.

<CodeGroup>
  ```python Python theme={null}
  from promptlayer import PromptLayer

  client = PromptLayer()  # Uses PROMPTLAYER_API_KEY env var

  response = client.run(
      prompt_name="cake-recipe",
      input_variables={
          "cake_type": "Chocolate Cake",
          "serving_size": "8"
      }
  )
  ```

  ```javascript JavaScript theme={null}
  import { PromptLayer } from "promptlayer";

  const client = new PromptLayer();

  const response = await client.run({
      promptName: "cake-recipe",
      inputVariables: {
          cake_type: "Chocolate Cake",
          serving_size: "8"
      }
  });
  ```
</CodeGroup>

<Accordion title="Output Format">
  The response includes a [prompt blueprint](/running-requests/prompt-blueprints) - a model-agnostic format that works the same whether you're using OpenAI, Anthropic, or any other provider. Access the generated content with:

  ```python  theme={null}
  print(response["prompt_blueprint"]["prompt_template"]["messages"][-1]["content"])
  ```

  This lets you switch models without changing how you read responses.
</Accordion>

After running, head to **Logs** in PromptLayer to see your request with the full input, output, and latency.

<Frame>
  <img src="https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/request-log.png?fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=c5117daff77c9f9be39e854f409a696e" alt="Log from SDK run" data-og-width="2620" width="2620" data-og-height="1266" height="1266" data-path="new-quickstart-images/request-log.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/request-log.png?w=280&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=5ea5070fdee73d50b75f90c2440bb6ec 280w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/request-log.png?w=560&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=e49e5ca8b737eae7a3953d8bd429c29d 560w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/request-log.png?w=840&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=841fed97e41f20a873baf1c1e117a573 840w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/request-log.png?w=1100&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=bac4f7cc36421e16d2e5e38280061c07 1100w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/request-log.png?w=1650&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=f6fada517ad9d115106262cbb8d1b022 1650w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/request-log.png?w=2500&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=813498c3da942c56e742a137ecb6da5f 2500w" />
</Frame>

Use `prompt_release_label="production"` to fetch the version labeled for production. Use `prompt_version=3` to pin to a specific version number. Agents work the same way - just pass the agent name. Store API keys as environment variables (`PROMPTLAYER_API_KEY`, `OPENAI_API_KEY`) - the client reads these automatically.

### Metadata and Logging

Add metadata to track requests by user, session, or feature flag:

```python  theme={null}
response = client.run(
    prompt_name="cake-recipe",
    input_variables={"cake_type": "Chocolate", "serving_size": "8"},
    tags=["production", "recipe-feature"],
    metadata={
        "user_id": "user_123",
        "session_id": "sess_abc"
    }
)

# Add a score after reviewing the output
client.track.score(request_id=response["request_id"], score=95)
```

Your metadata and tags appear in the log details, letting you filter and search by user or feature.

<Frame>
  <img src="https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/metadata-search.png?fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=47ca4b7b678fcade8aa60b57700ec6e2" alt="Log with metadata" data-og-width="890" width="890" data-og-height="1184" height="1184" data-path="new-quickstart-images/metadata-search.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/metadata-search.png?w=280&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=4278f6d35cc213b22244a0974516b7ba 280w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/metadata-search.png?w=560&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=59be4ca24ece2f2993c521f3fc0f0d87 560w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/metadata-search.png?w=840&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=b363e68a1e4101998bb95291884d30bf 840w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/metadata-search.png?w=1100&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=adb5912b5b3e19b9e51d148f898de07a 1100w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/metadata-search.png?w=1650&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=c7a226f3ceda9d6bbcefee11544a9307 1650w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/metadata-search.png?w=2500&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=ce6f3df9e18d11708255ebbb4124410c 2500w" />
</Frame>

Learn more about [metadata](/features/prompt-history/metadata) and [tagging](/features/prompt-history/tagging-requests).

For agents or complex workflows, enable tracing with `client = PromptLayer(enable_tracing=True)` and use the `@client.traceable` decorator on your functions to see each step as spans. Learn more about [traces](/running-requests/traces).

## Organizations

Use [organizations and workspaces](/why-promptlayer/shared-workspaces) to manage teams and environments. Common setups include separate workspaces for Production, Staging, and Development.

<Frame>
  <img src="https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/changelog.png?fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=c71a52ef879873ea99f53dd5b58fad24" alt="Changelog" data-og-width="2402" width="2402" data-og-height="1140" height="1140" data-path="new-quickstart-images/changelog.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/changelog.png?w=280&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=d472706b960402fb9086142f5d4101b0 280w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/changelog.png?w=560&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=52fb050986adda2d6309d9aa9d4bf56a 560w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/changelog.png?w=840&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=2a0bd047abb72fb8b23993d492eed315 840w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/changelog.png?w=1100&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=39321a13504359021a72d4e522b73e93 1100w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/changelog.png?w=1650&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=fd28e721fc87923cddf979a438f14b48 1650w, https://mintcdn.com/promptlayer/2Nw4D0YQ3AERsqEA/new-quickstart-images/changelog.png?w=2500&fit=max&auto=format&n=2Nw4D0YQ3AERsqEA&q=85&s=9ffdadaf48838cc8947fd8095e7244c4 2500w" />
</Frame>

Key features:

* **Role-based access control**: Owner, Admin, Editor, and Viewer roles at organization and workspace levels
* **Audit logs**: Track who changed what and when
* **Author attribution**: See who created and modified each prompt version
* **Centralized billing**: Manage usage across all workspaces

Each workspace has its own API key. Switch between workspaces using the dropdown in the top navigation.

## Next Steps

* [Deployment Strategies](/onboarding-guides/deployment-strategies) - Caching, webhooks, and production patterns
* [Tutorial Videos](/tutorial-videos) - Watch walkthroughs of common workflows
* [API Reference](/reference) - Full SDK documentation
