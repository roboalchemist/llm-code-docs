# Source: https://braintrust.dev/docs/core/experiments/run.md

# Run evals

> Create evaluations directly in your code, and run them in your development workflow or CI/CD pipeline

Braintrust allows you to create evaluations directly in your code, and run them in your development workflow
or CI/CD pipeline. Once you have defined one or more evaluations, you can run them using the `braintrust eval` command. This command will run all evaluations in the specified files and directories. As they run, they will automatically
create experiments in Braintrust and display a summary in your terminal.

<Tabs>
  <Tab title="TypeScript">
    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    npx braintrust eval basic.eval.ts
    ```

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    npx braintrust eval [file or directory] [file or directory] ...
    ```
  </Tab>

  <Tab title="Python">
    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    braintrust eval eval_basic.py
    ```

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    braintrust eval [file or directory] [file or directory] ...
    ```
  </Tab>
</Tabs>

The `braintrust eval` command uses the Next.js convention to load environment variables from:

* `env.development.local`
* `.env.local`
* `env.development`
* `.env`

## Watch mode

You can run evaluations in watch-mode by passing the `--watch` flag. This will re-run evaluations whenever any of
the files they depend on change.

## Dev mode

You can expose an `Eval` running at a remote URL or your local machine by passing the `--dev` flag. For more information, check out the [remote evals guide](/guides/remote-evals).

## Local testing mode

Pass the `--no-send-logs` flag to run evaluations locally without sending logs to Braintrust. This is useful for testing scorers during development without uploading results to your Braintrust project.

<CodeGroup>
  ```bash TypeScript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  npx braintrust eval --no-send-logs basic.eval.ts
  ```

  ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  braintrust eval --no-send-logs eval_basic.py
  ```
</CodeGroup>

## Github action

Once you get the hang of running evaluations, you can integrate them into your CI/CD pipeline to automatically
run them on every pull request or commit. This workflow allows you to catch eval regressions early and often.

The [`braintrustdata/eval-action`](https://github.com/braintrustdata/eval-action) action allows you to run
evaluations directly in your Github workflow. Each time you run an evaluation, the action automatically posts
a comment:

<img src="https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/github-actions-comment.png?fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=752d544c3ec52212f8789e48909f0db0" alt="action comment" data-og-width="1548" width="1548" data-og-height="730" height="730" data-path="core/experiments/github-actions-comment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/github-actions-comment.png?w=280&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=f5f459d00622c6a0d1d4c4dc849c175a 280w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/github-actions-comment.png?w=560&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=bbb8db6137865e04f33ed8e739a75cd4 560w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/github-actions-comment.png?w=840&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=386bc814b9cf79eab514f4282aeca22e 840w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/github-actions-comment.png?w=1100&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=2e7605017cfa78344b40925065f00fa5 1100w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/github-actions-comment.png?w=1650&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=083e53ca1a8849526eff5c760651821c 1650w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/github-actions-comment.png?w=2500&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=2d458abde97fb0e969367589b146d02b 2500w" />

To use the action, include it in a workflow yaml file (`.github/workflows`):

<CodeGroup>
  ```yaml Node runtime theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  - name: Run Evals
    uses: braintrustdata/eval-action@v1
    with:
      api_key: ${{ secrets.BRAINTRUST_API_KEY }}
      runtime: node
  ```

  ```yaml Node full example theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  name: Run pnpm evals

  on:
    push:
      # Uncomment to run only when files in the 'evals' directory change
      # - paths:
      #     - "evals/**"

  permissions:
    pull-requests: write
    contents: read

  jobs:
    eval:
      name: Run evals
      runs-on: ubuntu-latest

      steps:
        - name: Checkout
          id: checkout
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Setup Node.js
          id: setup-node
          uses: actions/setup-node@v4
          with:
            node-version: 20

        - uses: pnpm/action-setup@v3
          with:
            version: 8

        - name: Install Dependencies
          id: install
          run: pnpm install

        - name: Run Evals
          uses: braintrustdata/eval-action@v1
          with:
            api_key: ${{ secrets.BRAINTRUST_API_KEY }}
            runtime: node
            root: my_eval_dir
  ```

  ```yaml Python runtime theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  - name: Run Evals
    uses: braintrustdata/eval-action@v1
    with:
      api_key: ${{ secrets.BRAINTRUST_API_KEY }}
      runtime: python
  ```

  ```yaml Python full example theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  name: Run Python evals

  on:
    push:
      # Uncomment to run only when files in the 'evals' directory change
      # - paths:
      #     - "evals/**"

  permissions:
    pull-requests: write
    contents: read

  jobs:
    eval:
      name: Run evals
      runs-on: ubuntu-latest

      steps:
        - name: Checkout
          id: checkout
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Set up Python
          uses: actions/setup-python@v4
          with:
            python-version: "3.12" # Replace with your Python version

        # Tweak this to a dependency manager of your choice
        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install -r test-eval-py/requirements.txt

        - name: Run Evals
          uses: braintrustdata/eval-action@v1
          with:
            api_key: ${{ secrets.BRAINTRUST_API_KEY }}
            runtime: python
            root: my_eval_dir
  ```
</CodeGroup>

<Note>
  You must specify `permissions` for the action to leave comments on your PR.
  Without these permissions, you'll see Github API errors.
</Note>

For more information, see the [`braintrustdata/eval-action` README](https://github.com/braintrustdata/eval-action), or check
out full workflow files in the [examples](https://github.com/braintrustdata/eval-action/tree/main/examples) directory.

<Note>
  The `braintrustdata/eval-action` GitHub action does not currently support custom reporters. If you use custom reporters, you'll need to run the `braintrust eval` command directly in your CI/CD pipeline.
</Note>

## Run code directly

Although you can invoke `Eval()` functions via the `braintrust eval` command, you can also call them directly in your code.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Factuality } from "autoevals";
  import { Eval } from "braintrust";

  async function main() {
    const result = await Eval("Say Hi Bot", {
      data: () => [
        {
          input: "David",
          expected: "Hi David",
        },
      ],
      task: (input) => {
        return "Hi " + input;
      },
      scores: [Factuality],
    });
    console.log(result);
  }

  main();
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from autoevals import Factuality
  from braintrust import Eval

  def main():
      result = Eval(
          "Say Hi Bot",
          data=lambda: [
              {
                  "input": "David",
                  "expected": "Hi David",
              },
          ],
          task=lambda input: "Hi " + input,
          scores=[Factuality],
      )
      print(result)

  async def main():
      result = await Eval(
          "Say Hi Bot",
          data=lambda: [
              {
                  "input": "David",
                  "expected": "Hi David",
              },
          ],
          task=lambda input: "Hi " + input,
          scores=[Factuality],
      )
      print(result)
  ```
</CodeGroup>

In TypeScript, `Eval()` is an async function that returns a `Promise`. You can run `Eval()`s concurrently
and wait for all of them to finish using `Promise.all()`.

In Python, `Eval()` returns a `Future` if it is called in an async context, and a `Result` if it is called in a
synchronous context. It is safe to run `Eval()`s concurrently in both async and sync contexts.

Generally speaking, Jupyter notebooks are async, so you should use `await Eval(...)`.

## Limiting concurrency

If you are writing asynchronous code (TypeScript or asynchronous Python), then Braintrust will automatically run each dataset row concurrently. This optimizes for speed, but you can run into errors if your LLM's rate limits are too low. In this case, `maxConcurrency`/`max_concurrency` allows you to constrain concurrency and avoid rate limits.

If you're using synchronous Python, Braintrust runs tasks on a thread pool, whose size is defaulted to the number of CPU cores. The `max_concurrency` parameter will still be respected, but global max concurrency will be bounded by the size of this thread pool. You can use the `set_thread_pool_max_workers` function to adjust the thread pool size and achieve more parallelism.

Both the task function and scoring functions respect the max concurrency limit.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Factuality, Levenshtein } from "autoevals";
  import { Eval } from "braintrust";

  Eval("Say Hi Bot", {
    data: () =>
      Array.from({ length: 100 }, (_, i) => ({
        input: `${i}`,
        expected: `${i + 1}`,
      })),
    task: (input) => {
      return input + 1;
    },
    scores: [Factuality, Levenshtein],
    maxConcurrency: 5, // Run 5 tests concurrently
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from autoevals import Factuality, Levenstein
  from braintrust import Eval

  result = Eval(
      "Test",
      data=lambda: [{"input": f"{i}", "expected": f"{i + 1}"} for i in range(100)],
      task=lambda input: str(int(input) + 1),
      scores=[Factuality, Levenstein],
      max_concurrency=5,  # Run 5 tests concurrently
  )
  ```
</CodeGroup>

### Concurrency performance and costs

Concurrency can significantly improve evaluation speed, especially when your tasks involve:

* API calls to language models or other external services
* Network requests or database queries
* I/O operations like file reading

By running multiple test cases concurrently, you can reduce total evaluation time since tasks can execute in parallel while waiting for external responses.

However, higher concurrency can increase costs in several ways:

* **Rate limits**: Many API providers (like OpenAI and Anthropic) have rate limits. Exceeding these can result in throttling, errors, or additional charges.
* **Resource usage**: More concurrent operations consume more memory, CPU, and network bandwidth
* **External service costs**: Some services charge based on concurrent connections or have tiered pricing for higher throughput

## Troubleshooting

### Stack traces

By default, the evaluation framework swallows errors in individual tasks, reports them to Braintrust,
and prints a single line per error to the console. If you want to see the full stack trace for each
error, you can pass the `--verbose` flag.

### Why are my scores getting averaged?

Braintrust organizes your data into traces, each of which is a row in the experiments table. Within a trace,
if you log the same score multiple times, it will be averaged in the table. This is a useful way to collect an overall
measurement, e.g. if you compute the relevance of each retrieved document in a RAG use case, and want to see the overall
relevance. However, if you want to see each score individually, you have a few options:

* Split the input into multiple independent traces, and log each score in a separate trace. The [trials](#trials) feature
  will naturally average the results at the top-level, but allow you to view each individual output as a separate test case.
* Compute a separate score for each instance. For example, if you have exactly 3 documents you retrieve every time, you may want
  to compute a separate score for the 1st, 2nd, and 3rd position.
* Create separate experiments for each thing you're trying to score. For example, you may want to try out two different models and
  compute a score for each. In this case, if you split into separate experiments, you'll be able to diff across experiments and compare
  outputs side-by-side.

### Node bundling errors (e.g. "cannot be marked as external")

The `.eval.ts` files are bundled in a somewhat limiting way, via `esbuild` and a special set of
build options that work in most cases, but not all. For example, if you have any `export` statements
in them, you may see errors like "cannot be marked as external".

You can usually fix this specific error by removing `export` statements. However, if that does not work,
or you want more control over how the files are bundled, you can also just run the files directly.
`Eval` is an async function, so you can just call it directly in a script:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
npx tsx my-app.eval.ts
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt