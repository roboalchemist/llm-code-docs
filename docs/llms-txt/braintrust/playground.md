# Source: https://braintrust.dev/docs/core/playground.md

# Playgrounds

> Explore, compare, and evaluate prompts

Playgrounds are a powerful workspace for rapidly iterating on AI engineering primitives. Tune prompts, models, scorers and datasets in an editor-like interface, and run full evaluations in real-time, side by side.

Use playgrounds to build and test hypotheses and evaluation configurations in a flexible environment. Playgrounds leverage the same underlying `Eval` structure as experiments, with support for running thousands of dataset rows directly in the browser. Collaborating with teammates is also simple with a shared URL.

Playgrounds are designed for quick prototyping of ideas. When a playground is run, its previous generations are overwritten. You can create [experiments](/core/experiments) from playgrounds when you need to capture an immutable snapshot of your evaluations for long-term reference or point-in-time comparison.

<Tip>
  You can [try the playground](https://www.braintrust.dev/playground) without
  signing up. Any work you do in a demo playground will be saved if you [make an
  account](https://www.braintrust.dev/signup).
</Tip>

## Create a playground

A playground includes one or more evaluation tasks, one or more scorers, and optionally, a dataset.

You can create a playground by navigating to **Evaluations** > **Playgrounds**, or by selecting **Create playground with prompt** at the bottom of a prompt dialog.

<img src="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/simple-playground.png?fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=9ef12a540b5c84893c45716f9c10c88b" alt="Empty Playground" data-og-width="2436" width="2436" data-og-height="1674" height="1674" data-path="images/guides/playground/simple-playground.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/simple-playground.png?w=280&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=330f0643ea857e778f23deea5c7f28de 280w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/simple-playground.png?w=560&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=c1ee4c1300fa21b5a9771b6cc77e5757 560w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/simple-playground.png?w=840&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=1dcc72eedc64b5d1329041f4ea72c8b2 840w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/simple-playground.png?w=1100&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=cd81c2a2dd11529a012aa2b077bcd7a7 1100w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/simple-playground.png?w=1650&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=23a9b8b06f97878396b66edabec6734d 1650w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/simple-playground.png?w=2500&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=43b4218a6109a1b8495a42a30adbe8e8 2500w" />

### Tasks

Tasks define LLM instructions. There are four types of tasks:

* [Prompts](/core/functions/prompts): AI model, prompt messages, parameters, tools, and MCP servers.

* [Agents](/core/functions/agents): A chain of prompts.

* [Remote evals](/guides/remote-evals): Prompts and scorers from external sources.

* [Scorers](/core/functions/scorers): Prompts or heuristics used to evaluate the output of LLMs. Running scorers as tasks is useful to validate and iterate on them.

<Note>
  Note the difference between scorers-as-tasks and
  [scorers](/core/playground#scorers) used to evaluate tasks. You can even score
  your scorers-as-tasks in the playground.
</Note>

An empty playground will prompt you to create a base task, and optional comparison tests. The base task is used as the source when diffing output traces.

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/base-task.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=dc74b3cc874fa428bd71e427ef8ade03" alt="Base task empty playground" data-og-width="2428" width="2428" data-og-height="822" height="822" data-path="images/guides/playground/base-task.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/base-task.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=df43d83fa354c2a9eefbebfe124f9e27 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/base-task.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=1e98155ec5a6bb320b52cb7d1c1dcf0c 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/base-task.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=2f67cf6faf8b81f9bb884b1cebbc9770 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/base-task.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=df231cecf23a41a65b5ffb14010b92de 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/base-task.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=d95eddd06320a96d80545c9df92d8592 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/base-task.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=cd8b9ced2c2395b91316699dce7ed707 2500w" />

When you select **Run** (or the keyboard shortcut Cmd/Ctrl+Enter), each task runs in parallel and the results stream into the grid below. You can also choose to view in list or summary layout.

<Note>
  [AI providers](/core/organizations#ai-providers) must be configured before
  playgrounds can be run.
</Note>

For multimodal workflows, supported [attachments](/guides/attachments#viewing-attachments) will have a preview shown in the inline embedded view.

### Scorers

Scorers quantify the quality of evaluation outputs using an LLM judge or code. You can use built-in [autoevals](/reference/autoevals) for common evaluation scenarios to help you get started quickly, or write [custom scorers](/core/functions/scorers) tailored to your use case.

To add a scorer, select **+ Scorer** and choose from the list or create a custom scorer.

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/add-scorer.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=4395472d2198a018b8552b8b994a19b2" alt="Add scorer" data-og-width="2436" width="2436" data-og-height="592" height="592" data-path="images/guides/playground/add-scorer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/add-scorer.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=1646e3859283d4da21ee82fe57b07f35 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/add-scorer.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=1ca942a24bab25c9cfd495c6a0b9e655 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/add-scorer.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=b9fd81480c612140d339589ae8536bdb 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/add-scorer.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=50ffb328d30de2a7faf8784d8ebbd3d7 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/add-scorer.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=ee12a458d449b4f987605cece63a29b0 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/add-scorer.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=fbebb04719117ee7a277b5cc6697fe64 2500w" />

### Datasets

[Datasets](/core/datasets) provide structured inputs, expected values, and metadata for evaluations.

A playground can be run without a dataset to view a single set of task outputs, or with a dataset to view a matrix of outputs for many inputs.

Datasets can be linked to a playground by selecting existing library datasets, or creating/importing a new one.

Once you link a dataset, you will see a new row in the grid for each record in the dataset. You can reference the
data from each record in your prompt using the `input`, `expected`, and `metadata` variables. The playground supports [Mustache and Nunjucks templating syntax](/core/functions/prompts/use-templating).

<img src="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/prompt-with-dataset.png?fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=39ae72da8c0fac4ea67959baa25356da" alt="Prompt with dataset" data-og-width="2428" width="2428" data-og-height="1556" height="1556" data-path="images/guides/playground/prompt-with-dataset.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/prompt-with-dataset.png?w=280&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=5cab6c2b5b82a3cfd76ce39eae6bd954 280w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/prompt-with-dataset.png?w=560&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=09daacf5e9f5f1dba954914e668194c3 560w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/prompt-with-dataset.png?w=840&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=0d0c085dca05439970f1221cbefad4c9 840w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/prompt-with-dataset.png?w=1100&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=51a7c168e1c7954db93bfb60743dbeb2 1100w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/prompt-with-dataset.png?w=1650&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=40c021df26286dc4965a5354f591dc7e 1650w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/prompt-with-dataset.png?w=2500&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=ae711b57e80cb76d33bd323ddd2edfa2 2500w" />

Each value can be arbitrarily complex JSON, for example, `{{input.formula}}`.

#### For scorers-as-task

When evaluating scorers in the playground, ensure that your dataset input schema adheres to scorer convention. Like when a scorer is used on a prompt or agent, the *input* to the scorer should have the shape `{ input, expected, metadata, output }`.
Unlike other task types, those reserved dataset keywords are hoisted into the global scope, meaning you can use your saved scorers in the playground and reference variables without any changes.

For example, to tune a scorer with the prompt:

```
is {{output}} funny and concerning the same topic as {{expected}}?
```

Then, your dataset rows should look something like:

```
{
  "input": {
    "output": "Why did the chicken cross the road? To get to the other side!",
    "expected": "Why's six afraid of seven? Because seven ate nine!" // `expected` here is hoisted and interpolated into the scorer.
  },
  "expected": {
    "choice": 0,
    "rationale": "The output is a clichéd joke. Output and expected contain jokes concerning different topics."
  } // `expected` here refers to the expected output of the scorer as task. it can be used by scorers running on the output of this task - itself a scorer.
}
```

## Run a playground

To run a playground, select the <Icon icon="play" /> **Run** button at the top of the playground to run all tasks and all dataset rows. You can also run a single task individually, or run a single dataset row.

<video className="border rounded-md" loop autoPlay muted poster="/images/guides/playground/running-playground-poster.png">
  <source src="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/running-playground.mp4?fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=583be95e02824efde3b0d61ebe43a524" type="video/mp4" data-path="images/guides/playground/running-playground.mp4" />
</video>

<Note>
  Experiments run from the UI have a 15-minute timeout, after which the
  experiment stops executing. For longer-running evaluations, use the
  [programmatic SDK approach](/core/experiments/run) instead.
</Note>

### View traces

Select a row in the results table to compare evaluation traces side-by-side. This allows you to identify differences in outputs, scores, metrics, and input data.

<img src="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/trace-viewer.png?fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=a4220e1134dcce7d6f2d6fcb26f851f2" alt="Trace viewer" data-og-width="2428" width="2428" data-og-height="718" height="718" data-path="images/guides/playground/trace-viewer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/trace-viewer.png?w=280&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=d11d0e18a58c555b997a2d84e1937bd9 280w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/trace-viewer.png?w=560&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=0e0b837826b144af9e7f9cf9fcb7e097 560w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/trace-viewer.png?w=840&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=2b489e3b1564ef417135a1a05f02300d 840w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/trace-viewer.png?w=1100&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=f0d790b5b61a9ff939875fdc584a0402 1100w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/trace-viewer.png?w=1650&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=a778b5864435ae7efc203da9e65245a8 1650w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/trace-viewer.png?w=2500&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=57e455fbab227b01482d5da9ad06c01e 2500w" />

From this view, you can also run a single row by selecting <Icon icon="play" /> **Run row**.

### Diffing

Diffing allows you to visually compare variations across models, prompts, or agents to quickly understand differences in outputs.

To turn on diff mode, select the diff toggle.

<video className="border rounded-md" loop autoPlay muted poster="/images/guides/playground/diffing-poster.png">
  <source src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/diffing.mp4?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=fd3c52fc17317a244fa6ca5442f4ab5b" type="video/mp4" data-path="images/guides/playground/diffing.mp4" />
</video>

## Create experiment snapshots

Experiments formalize evaluation results for comparison and historical reference. While playgrounds are better for fast, iterative exploration, experiments are immutable, point-in-time evaluation snapshots ideal for detailed analysis and reporting.

To create an experiment from a playground, select **+ Experiment**. Each playground task will map to its own experiment.

<video className="border rounded-md" loop autoPlay muted poster="/images/guides/playground/create-experiment-poster.png">
  <source src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/playground/create-experiment-from-playground.mp4?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=f3b55552ab767c405d63b24a7edcef79" type="video/mp4" data-path="images/guides/playground/create-experiment-from-playground.mp4" />
</video>

## Advanced options

### Append dataset messages

You may sometimes have additional messages in a dataset that you want to append to a prompt. This option lets you specify a path to a messages array in the dataset. For example, if `input` is specified as the appended messages path and a dataset row has the following input, all prompts in the playground will run with additional messages.

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

## Collaboration

Playgrounds are designed for collaboration and automatically synchronize in real-time.

To share a playground, copy the URL and send it to your collaborators. Your collaborators
must be members of your organization to view the playground. You can invite users from the <Link href="/app/settings?subroute=team" target="_blank">settings</Link> page.

## Reasoning

<Note>
  If you are on a hybrid deployment, reasoning support is available starting
  with `v0.0.74`.
</Note>

Reasoning models like OpenAI’s o4, Anthropic’s Claude 3.5 Sonnet, and Google’s Gemini 2.5 Flash generate intermediate reasoning steps before producing a final response. Braintrust provides unified support for these models, so you can work with reasoning outputs no matter which provider you choose.

When you enable reasoning, models generate "thinking tokens" that show their step-by-step reasoning process. This is useful for complex tasks like math problems, logical reasoning, coding, and multi-step analysis.

In playgrounds, you can configure reasoning parameters directly in the model settings.

<img src="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/reasoning-params.gif?s=2cb393dc424678c82a3a6ac5cd86496a" alt="Screenshot showing reasoning parameters in playground model settings - reasoning_effort dropdown, reasoning_enabled toggle, reasoning_budget input field" data-og-width="640" width="640" data-og-height="500" height="500" data-path="images/guides/playground/reasoning-params.gif" data-optimize="true" data-opv="3" />

To enable reasoning in a playground:

1. Select a reasoning-capable model (like `claude-3-7-sonnet-latest`, `o4-mini`, or `publishers/google/models/gemini-2.5-flash-preview-04-17` (Gemini provided by Vertex AI))
2. In the model parameters section, configure your reasoning settings:
   * Set `reasoning_effort` to **low**, **medium**, or **high**
   * Or enable `reasoning_enabled` and specify a `reasoning_budget`
3. Run your prompt to see reasoning in action

<img src="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/playground/reasoning-stream-response.gif?s=357659392bc26d54d676ae398a329489" alt="Screenshot showing a prompt being run with reasoning enabled, displaying the streaming thinking tokens in real-time" data-og-width="640" width="640" data-og-height="896" height="896" data-path="images/guides/playground/reasoning-stream-response.gif" data-optimize="true" data-opv="3" />


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt