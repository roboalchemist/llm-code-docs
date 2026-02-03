# Source: https://braintrust.dev/docs/evaluate/playgrounds.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Use playgrounds

> Rapidly prototype and test prompts, models, and scorers

Playgrounds provide a no-code workspace for rapidly iterating on prompts, models, scorers, and datasets. Run full evaluations in real-time, compare results side-by-side, and share configurations with teammates.

<img src="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/simple-playground.png?fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=9ef12a540b5c84893c45716f9c10c88b" alt="Empty Playground" data-og-width="2436" width="2436" data-og-height="1674" height="1674" data-path="images/guides/playground/simple-playground.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/simple-playground.png?w=280&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=330f0643ea857e778f23deea5c7f28de 280w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/simple-playground.png?w=560&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=c1ee4c1300fa21b5a9771b6cc77e5757 560w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/simple-playground.png?w=840&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=1dcc72eedc64b5d1329041f4ea72c8b2 840w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/simple-playground.png?w=1100&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=cd81c2a2dd11529a012aa2b077bcd7a7 1100w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/simple-playground.png?w=1650&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=23a9b8b06f97878396b66edabec6734d 1650w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/simple-playground.png?w=2500&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=43b4218a6109a1b8495a42a30adbe8e8 2500w" />

<Tip>
  Try the [playground](https://www.braintrust.dev/playground) without signing up. Work is saved if you create an account.
</Tip>

## Create a playground

Navigate to **Evaluations** > **Playgrounds** or select **Create playground with prompt** from a prompt dialog.

A playground includes:

* **Tasks**: One or more prompts, workflows, or scorers to evaluate
* **Scorers**: Functions that measure output quality
* **Dataset**: Optional test cases with inputs and expected outputs

## Add tasks

Tasks define what you're testing. Choose from four types:

### Prompts

Configure AI model, prompt messages, parameters, tools, and MCP servers. This is the most common task type for testing model responses. See [Write prompts](/evaluate/write-prompts) for details.

### Workflows

Chain multiple prompts together to test complex workflows. Workflows allow you to create multi-step processes where the output of one prompt becomes the input for the next.

<Warning>
  Workflows are in beta. They currently only work in playgrounds and are limited to prompt chaining functionality. If you are on a hybrid deployment, workflows are available starting with `v0.0.66`.
</Warning>

To create a workflow, select **+ Workflow** and create or select prompts to chain together. The prompts run consecutively, with each prompt receiving the previous prompt's output as input.

**Variables in workflows:**

Workflows use templating to reference variables from datasets and previous prompts:

* **First prompt node**: Access dataset variables directly using `{{input}}`, `{{expected}}`, and `{{metadata}}`. For consistency, you can also use `{{dataset.input}}`, `{{dataset.expected}}`, and `{{dataset.metadata}}`.
* **Later prompts**: Access the previous node's output using `{{input}}`. If the previous node outputs structured data, use dot notation like `{{input.bar}}`.
* **Global dataset access**: The `{{dataset}}` variable is available in any prompt node to access the original dataset values (available in hybrid deployments starting with `v1.1.1`).

<video className="border rounded-md" loop autoPlay muted poster="/images/core/functions/agents-poster.png">
  <source src="https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/functions/agents.mp4?fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=8374829b853fa3873d121a7b1f2f728b" type="video/mp4" data-path="images/core/functions/agents.mp4" />
</video>

### Remote evals

Connect to evaluations running on your own infrastructure while using Braintrust's playground for iteration, comparison, and analysis. Use remote evals when you need custom infrastructure, specific runtime environments, security/compliance requirements, or long-running evaluations. See [Run remote evaluations](/evaluate/remote-evals) for setup details.

### Scorers

Run scorers as tasks to validate and iterate on them before using them to evaluate other tasks. See [Write scorers](/evaluate/write-scorers) for details.

<Note>
  Scorers-as-tasks are different from scorers used to evaluate tasks. You can even score your scorers-as-tasks.
</Note>

An empty playground prompts you to create a base task and optional comparison tasks. The base task is the source for diffing outputs.

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/base-task.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=dc74b3cc874fa428bd71e427ef8ade03" alt="Base task empty playground" data-og-width="2428" width="2428" data-og-height="822" height="822" data-path="images/guides/playground/base-task.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/base-task.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=df43d83fa354c2a9eefbebfe124f9e27 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/base-task.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=1e98155ec5a6bb320b52cb7d1c1dcf0c 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/base-task.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=2f67cf6faf8b81f9bb884b1cebbc9770 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/base-task.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=df231cecf23a41a65b5ffb14010b92de 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/base-task.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=d95eddd06320a96d80545c9df92d8592 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/base-task.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=cd8b9ced2c2395b91316699dce7ed707 2500w" />

<Note>
  Configure [AI providers](/admin/organizations#configure-ai-providers) in organization settings, or configure them inline directly from the playground when you first run it.
</Note>

## Add scorers

Scorers quantify output quality using LLM judges or code. Use built-in [autoevals](/reference/autoevals) or create [custom scorers](/evaluate/write-scorers).

To add a scorer, select **+ Scorer** and choose from the list or create a new one:

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/add-scorer.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=4395472d2198a018b8552b8b994a19b2" alt="Add scorer" data-og-width="2436" width="2436" data-og-height="592" height="592" data-path="images/guides/playground/add-scorer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/add-scorer.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=1646e3859283d4da21ee82fe57b07f35 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/add-scorer.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=1ca942a24bab25c9cfd495c6a0b9e655 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/add-scorer.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=b9fd81480c612140d339589ae8536bdb 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/add-scorer.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=50ffb328d30de2a7faf8784d8ebbd3d7 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/add-scorer.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=ee12a458d449b4f987605cece63a29b0 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/add-scorer.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=fbebb04719117ee7a277b5cc6697fe64 2500w" />

## Add datasets

Link a dataset to test multiple inputs at once. Without a dataset, the playground runs a single evaluation. With a dataset, it runs a matrix of evaluations across all test cases.

You can select an existing dataset or create a new one inline without leaving the playground. When creating a dataset, you have two options:

* **Upload CSV/JSON**: Import test cases from a file
* **Empty dataset**: Create a blank dataset to populate manually later

Once linked, you'll see a row for each dataset record.

Reference dataset fields in prompts using template variables:

```
Analyze this input: {{input}}
Expected output: {{expected}}
User category: {{metadata.category}}
```

<img src="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/prompt-with-dataset.png?fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=39ae72da8c0fac4ea67959baa25356da" alt="Prompt with dataset" data-og-width="2428" width="2428" data-og-height="1556" height="1556" data-path="images/guides/playground/prompt-with-dataset.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/prompt-with-dataset.png?w=280&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=5cab6c2b5b82a3cfd76ce39eae6bd954 280w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/prompt-with-dataset.png?w=560&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=09daacf5e9f5f1dba954914e668194c3 560w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/prompt-with-dataset.png?w=840&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=0d0c085dca05439970f1221cbefad4c9 840w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/prompt-with-dataset.png?w=1100&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=51a7c168e1c7954db93bfb60743dbeb2 1100w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/prompt-with-dataset.png?w=1650&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=40c021df26286dc4965a5354f591dc7e 1650w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/prompt-with-dataset.png?w=2500&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=ae711b57e80cb76d33bd323ddd2edfa2 2500w" />

The playground supports [Mustache and Nunjucks templating](/evaluate/write-prompts#use-templating). Access nested fields like `{{input.formula}}`.

### For scorers-as-tasks

When evaluating scorers, dataset inputs should match scorer convention: `{ input, expected, metadata, output }`. These fields are hoisted into global scope for easy reference.

Example scorer prompt:

```
Is {{output}} funny and concerning the same topic as {{expected}}?
```

Example dataset row:

```json  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
{
  "input": {
    "output": "Why did the chicken cross the road? To get to the other side!",
    "expected": "Why's six afraid of seven? Because seven ate nine!"
  },
  "expected": {
    "choice": 0,
    "rationale": "Output is a clichéd joke about a different topic."
  }
}
```

## Run evaluations

Select <Icon icon="play" /> **Run** (or Cmd/Ctrl+Enter) to run all tasks and dataset rows in parallel. Results stream into the grid below.

<video className="border rounded-md" loop autoPlay muted poster="/images/guides/playground/running-playground-poster.png">
  <source src="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/running-playground.mp4?fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=583be95e02824efde3b0d61ebe43a524" type="video/mp4" data-path="images/guides/playground/running-playground.mp4" />
</video>

You can also:

* Run a single task
* Run a single dataset row
* View results in grid, list, or summary layout

For multimodal workflows, supported attachments will have a preview shown in the inline embedded view.

<Note>
  UI experiments timeout after 15 minutes. For longer evaluations, use the [programmatic SDK](/evaluate/run-evaluations).
</Note>

### View traces

Select a row to compare traces side-by-side and identify differences in outputs, scores, metrics, and inputs:

<img src="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/trace-viewer.png?fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=a4220e1134dcce7d6f2d6fcb26f851f2" alt="Trace viewer" data-og-width="2428" width="2428" data-og-height="718" height="718" data-path="images/guides/playground/trace-viewer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/trace-viewer.png?w=280&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=d11d0e18a58c555b997a2d84e1937bd9 280w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/trace-viewer.png?w=560&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=0e0b837826b144af9e7f9cf9fcb7e097 560w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/trace-viewer.png?w=840&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=2b489e3b1564ef417135a1a05f02300d 840w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/trace-viewer.png?w=1100&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=f0d790b5b61a9ff939875fdc584a0402 1100w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/trace-viewer.png?w=1650&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=a778b5864435ae7efc203da9e65245a8 1650w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/trace-viewer.png?w=2500&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=57e455fbab227b01482d5da9ad06c01e 2500w" />

From this view, select <Icon icon="play" /> **Run row** to re-run a single test case.

## Compare with diff mode

Enable the diff toggle to visually compare variations across models, prompts, or workflows:

<video className="border rounded-md" loop autoPlay muted poster="/images/guides/playground/diffing-poster.png">
  <source src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/diffing.mp4?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=fd3c52fc17317a244fa6ca5442f4ab5b" type="video/mp4" data-path="images/guides/playground/diffing.mp4" />
</video>

Diff mode highlights:

* Output differences between tasks
* Score changes
* Timing and token usage variations

## Save as experiment

Playgrounds overwrite previous runs for fast iteration. When you need an immutable snapshot for long-term reference or comparison, create an experiment:

1. Run your playground.
2. Select **+ Experiment**.
3. Name your experiment.
4. Access it from the Experiments page.

Experiments preserve exact results and enable systematic comparison over time. Each playground task will map to its own experiment.

<video className="border rounded-md" loop autoPlay muted poster="/images/guides/playground/create-experiment-poster.png">
  <source src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/create-experiment-from-playground.mp4?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=f3b55552ab767c405d63b24a7edcef79" type="video/mp4" data-path="images/guides/playground/create-experiment-from-playground.mp4" />
</video>

## Share playgrounds

Collaborate by sharing playground URLs with teammates. They'll see the same configuration and can run their own evaluations or make changes. Playgrounds automatically synchronize in real-time.

Your collaborators must be members of your organization to view the playground. You can invite users from the settings page.

## Best practices

**Start simple**: Test one prompt or model first. Add comparisons once the base works.

**Use representative data**: Build datasets from production logs or known edge cases.

**Compare systematically**: Change one variable at a time (model, temperature, prompt wording) to isolate effects.

**Look for patterns**: Group by metadata fields to see which input types cause issues.

**Iterate quickly**: Playgrounds excel at rapid experimentation. Save experiments only when you need permanent records.

## Advanced options

### Append dataset messages

You may have additional messages in a dataset that you want to append to a prompt. This option lets you specify a path to a messages array in the dataset. For example, if `input` is specified as the appended messages path and a dataset row has the following input, all prompts in the playground will run with additional messages:

```json  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
[
  {
    "role": "assistant",
    "content": "Is there anything else I can help you with?"
  },
  {
    "role": "user",
    "content": "Yes, I have another question."
  }
]
```

To append messages from a dataset to your prompts, open the advanced settings menu next to your dataset selection and enter the path to the messages you want to append.

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/append-dataset-messages.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=b9bfed529035a2d8560b2713405dcd43" alt="Screenshot of advanced settings menu" data-og-width="614" width="614" data-og-height="792" height="792" data-path="images/guides/playground/append-dataset-messages.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/append-dataset-messages.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=1be205f15ce44ad9155b934de07e31b2 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/append-dataset-messages.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=bae7082fe9d2d1f9eb1eef8532c07fa2 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/append-dataset-messages.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=e0557db3c0060bafa08de9fdb229fefa 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/append-dataset-messages.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=c84bfdee233e6b7ccc7347c4f6574c05 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/append-dataset-messages.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=2764cd5bfd432412e0eb37d764ff12a4 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/append-dataset-messages.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=cccc0f86b15e918a905ed1d0162a24b3 2500w" />

### Max concurrency

The maximum number of tasks/scorers that will be run concurrently in the playground. This is useful for avoiding rate limits (429 - Too many requests) from AI/MCP providers.

### Strict variables

When this option is enabled, evaluations will fail if the dataset row does not include all of the variables referenced in prompts.

## Reasoning models

<Note>
  If you are on a hybrid deployment, reasoning support is available starting with `v0.0.74`.
</Note>

Reasoning models like OpenAI's o4, Anthropic's Claude 3.5 Sonnet, and Google's Gemini 2.5 Flash generate intermediate reasoning steps before producing a final response. Braintrust provides unified support for these models, so you can work with reasoning outputs no matter which provider you choose.

When you enable reasoning, models generate "thinking tokens" that show their step-by-step reasoning process. This is useful for complex tasks like math problems, logical reasoning, coding, and multi-step analysis.

In playgrounds, you can configure reasoning parameters directly in the model settings.

<img src="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/reasoning-params.gif?s=2cb393dc424678c82a3a6ac5cd86496a" alt="Screenshot showing reasoning parameters" data-og-width="640" width="640" data-og-height="500" height="500" data-path="images/guides/playground/reasoning-params.gif" data-optimize="true" data-opv="3" />

To enable reasoning in a playground:

1. Select a reasoning-capable model (like `claude-3-7-sonnet-latest`, `o4-mini`, or `publishers/google/models/gemini-2.5-flash-preview-04-17` for Gemini via Vertex AI).
2. In the model parameters section, configure your reasoning settings:
   * Set `reasoning_effort` to **low**, **medium**, or **high**.
   * Or enable `reasoning_enabled` and specify a `reasoning_budget`.
3. Run your prompt to see reasoning in action.

<img src="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/reasoning-stream-response.gif?s=357659392bc26d54d676ae398a329489" alt="Screenshot showing reasoning in action" data-og-width="640" width="640" data-og-height="896" height="896" data-path="images/guides/playground/reasoning-stream-response.gif" data-optimize="true" data-opv="3" />

## Next steps

* [Write prompts](/evaluate/write-prompts) to test in playgrounds
* [Write scorers](/evaluate/write-scorers) to measure quality
* [Interpret results](/evaluate/interpret-results) from playground runs
* [Compare experiments](/evaluate/compare-experiments) saved from playgrounds
