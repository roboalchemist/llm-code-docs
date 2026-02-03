# Source: https://braintrust.dev/docs/evaluate/write-scorers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Write scorers

> Create scorers to measure AI output quality

Scorers evaluate AI outputs by assigning scores between 0 and 100%. Use pre-built scorers from autoevals, write custom code scorers, or build LLM-as-a-judge scorers to measure what matters for your application.

## Scorer types

Braintrust offers three types of scorers:

* [**Autoevals**](#autoevals): Pre-built, battle-tested scorers for common tasks like factuality checking, semantic similarity, and format validation. Start here for standard evaluation needs.

* [**LLM-as-a-judge**](#llm-as-a-judge): Use a language model to evaluate outputs based on natural language criteria. Best for subjective judgments like tone, helpfulness, or creativity that are difficult to encode in code.

* [**Custom code**](#custom-code): Write custom evaluation logic in TypeScript or Python. Best when you have specific rules, patterns, or calculations to implement. Custom code scorers can evaluate either the final output or the entire execution trace for multi-step workflows.

## Create scorers

### Autoevals

Pre-built, battle-tested scorers for common evaluation tasks. Autoevals are open-source, deterministic (where possible), and optimized for speed and reliability.

<Tabs>
  <Tab title="SDK" icon="terminal">
    Import autoevals and use them directly in evaluations:

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import { Eval } from "braintrust";
      import { Factuality, Levenshtein, Semantic } from "autoevals";

      Eval("My Project", {
        data: myDataset,
        task: myTask,
        scores: [Factuality, Levenshtein, Semantic],
      });
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      from braintrust import Eval
      from autoevals import Factuality, Levenshtein, Semantic

      Eval(
          "My Project",
          data=my_dataset,
          task=my_task,
          scores=[Factuality, Levenshtein, Semantic],
      )
      ```
    </CodeGroup>

    Autoevals automatically receive these parameters when used in evaluations:

    * `input`: The input to your task
    * `output`: The output from your task
    * `expected`: The expected output (optional)
    * `metadata`: Custom metadata from the test case

    Available scorers:

    * **Factuality**: Check if output contains factual information
    * **Semantic**: Measure semantic similarity to expected output
    * **Levenshtein**: Calculate edit distance from expected output
    * **JSON**: Validate JSON structure and content
    * **SQL**: Validate SQL query syntax and semantics

    See the [autoevals library](https://github.com/braintrustdata/autoevals) for the complete list.
  </Tab>

  <Tab title="UI" icon="mouse-pointer-2">
    Autoevals are pre-built scorers that are available directly in the Braintrust UI. You don't need to create them - just select and use them.

    * **Use in playgrounds**: When testing prompts in [playgrounds](/evaluate/playgrounds), add autoevals in the scoring section to evaluate results interactively.

    * **Use in experiments**: When creating [experiments](/evaluate/run-evaluations#run-in-ui), select autoevals from the scorer dropdown to measure output quality across your dataset.

    * **Use in online scoring**: Add autoevals to [online scoring rules](/observe/score-online) to automatically evaluate production logs.
  </Tab>
</Tabs>

### LLM-as-a-judge

Use a language model to evaluate outputs based on natural language criteria. The model rates outputs and maps its choices to numeric scores.

<Tabs>
  <Tab title="SDK" icon="terminal">
    Define LLM-as-a-judge scorers in code and push to Braintrust:

    <CodeGroup dropdown>
      ```typescript title="scorer.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import braintrust from "braintrust";

      const project = braintrust.projects.create({ name: "my-project" });

      project.scorers.create({
        name: "Helpfulness scorer",
        slug: "helpfulness-scorer",
        description: "Evaluate helpfulness of response",
        messages: [
          {
            role: "user",
            content:
              'Rate the helpfulness of this response: {{output}}\n\nReturn "A" for very helpful, "B" for somewhat helpful, "C" for not helpful.',
          },
        ],
        model: "gpt-4o",
        useCot: true,
        choiceScores: {
          A: 1,
          B: 0.5,
          C: 0,
        },
        metadata: {
          __pass_threshold: 0.7,
        },
      });
      ```

      ```python title="scorer.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import braintrust

      project = braintrust.projects.create(name="my-project")

      project.scorers.create(
          name="Helpfulness scorer",
          slug="helpfulness-scorer",
          description="Evaluate helpfulness of response",
          messages=[
              {
                  "role": "user",
                  "content": 'Rate the helpfulness of this response: {{output}}\n\nReturn "A" for very helpful, "B" for somewhat helpful, "C" for not helpful.',
              }
          ],
          model="gpt-4o",
          use_cot=True,
          choice_scores={
              "A": 1,
              "B": 0.5,
              "C": 0,
          },
          metadata={"__pass_threshold": 0.7},
      )
      ```
    </CodeGroup>

    Push to Braintrust:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    npx braintrust push scorer.ts
    ```

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    braintrust push scorer.py
    ```

    Your prompt template can reference these variables:

    * `{{input}}`: The input to your task
    * `{{output}}`: The output from your task
    * `{{expected}}`: The expected output (optional)
    * `{{metadata}}`: Custom metadata from the test case
  </Tab>

  <Tab title="UI" icon="mouse-pointer-2">
    Create LLM-as-a-judge scorers in Braintrust:

    1. Go to <Icon icon="percent" /> **Scorers** > **+ Scorer**.
    2. Enter a scorer name and slug.
    3. Select **LLM-as-a-judge**.
    4. Configure:
       * **Prompt**: Instructions for evaluating the output
       * **Model**: Which model to use as judge
       * **Choice scores**: Map model choices (A, B, C) to numeric scores
       * **Use CoT**: Enable chain-of-thought reasoning for complex evaluations
    5. Click **Save as custom scorer**.
  </Tab>
</Tabs>

### Custom code

Write custom evaluation logic in TypeScript or Python to evaluate outputs. Custom code scorers give you full control over the evaluation logic and can use any packages you need.

<Tabs>
  <Tab title="SDK" icon="terminal">
    <CodeGroup dropdown>
      ```typescript title="output-scorer.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import braintrust from "braintrust";
      import { z } from "zod";

      const project = braintrust.projects.create({ name: "my-project" });

      project.scorers.create({
        name: "Equality scorer",
        slug: "equality-scorer",
        description: "Check if output equals expected",
        parameters: z.object({
          output: z.string(),
          expected: z.string(),
        }),
        handler: async ({ output, expected }) => {
          return output === expected ? 1 : 0;
        },
        metadata: {
          __pass_threshold: 0.5,
        },
      });
      ```

      ```python title="output_scorer.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import braintrust
      from pydantic import BaseModel

      project = braintrust.projects.create(name="my-project")

      class EqualityParams(BaseModel):
          output: str
          expected: str

      @project.scorers.create(
          name="Equality scorer",
          slug="equality-scorer",
          description="Check if output equals expected",
          parameters=EqualityParams,
          metadata={"__pass_threshold": 0.5},
      )
      def equality_scorer(output: str, expected: str):
          return 1 if output == expected else 0
      ```
    </CodeGroup>

    Push to Braintrust:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    npx braintrust push scorer.ts
    ```

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    braintrust push scorer.py
    ```

    Your handler function receives these parameters:

    * `input`: The input to your task
    * `output`: The output from your task
    * `expected`: The expected output (optional)
    * `metadata`: Custom metadata from the test case

    Return a number between 0 and 1, or an object with `score` and optional metadata:

    ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    // Simple return
    return 0.85;

    // With metadata
    return {
      score: 0.85,
      metadata: { reason: "Good factuality, minor tone issues" },
    };
    ```

    <Note>
      **Important notes for Python scorers:**

      * Scorers must be pushed from within their directory (e.g., `braintrust push scorer.py`); pushing with relative paths (e.g., `braintrust push path/to/scorer.py`) is unsupported and will cause import errors.
      * Scorers using local imports must be defined at the project root.
      * Braintrust uses uv to cross-bundle dependencies to Linux. This works for binary dependencies except libraries requiring on-demand compilation.
    </Note>

    <Accordion title="TypeScript bundling">
      In TypeScript, Braintrust uses `esbuild` to bundle your code and dependencies. This works for most dependencies but does not support native (compiled) libraries like SQLite.

      If you have trouble bundling dependencies, [file an issue in the braintrust-sdk repo](https://github.com/braintrustdata/braintrust-sdk/issues).
    </Accordion>

    <Accordion title="Python external dependencies">
      Python scorers created via the CLI have these default packages:

      * `autoevals`
      * `braintrust`
      * `openai`
      * `pydantic`
      * `requests`

      For additional packages, use the `--requirements` flag.

      For scorers with external dependencies:

      ```python title="scorer-with-deps.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import braintrust
      from langdetect import detect  # External package
      from pydantic import BaseModel

      project = braintrust.projects.create(name="my-project")

      class LanguageMatchParams(BaseModel):
          output: str
          expected: str

      @project.scorers.create(
          name="Language match",
          slug="language-match",
          description="Check if output and expected are same language",
          parameters=LanguageMatchParams,
          metadata={"__pass_threshold": 0.5},
      )
      def language_match_scorer(output: str, expected: str):
          return 1.0 if detect(output) == detect(expected) else 0.0
      ```

      Create requirements file:

      ```
      langdetect==1.0.9
      ```

      Push with requirements:

      ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      braintrust push scorer-with-deps.py --requirements requirements.txt
      ```
    </Accordion>
  </Tab>

  <Tab title="UI" icon="mouse-pointer-2">
    Write TypeScript or Python code that evaluates outputs:

    1. Go to <Icon icon="percent" /> **Scorers** > **+ Scorer**.
    2. Enter a scorer name and slug.
    3. Select **TypeScript** or **Python**.
    4. Write your scorer function. The code editor provides real-time linting and autocomplete to help you write correct code faster.
    5. Click **Save as custom scorer**.

    **Example:**

    ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    async function scorer({ output, expected }) {
      return output === expected ? 1 : 0;
    }
    ```

    <Note>
      UI scorers have access to these packages:

      * `anthropic`
      * `autoevals`
      * `braintrust`
      * `json`
      * `math`
      * `openai`
      * `re`
      * `requests`
      * `typing`

      For additional packages, use the SDK tab.
    </Note>
  </Tab>
</Tabs>

## Set pass thresholds

Define minimum acceptable scores to automatically mark results as passing or failing. When configured, scores that meet or exceed the threshold are marked as **passing** (green highlighting with checkmark), while scores below are marked as **failing** (red highlighting).

<Tabs>
  <Tab title="SDK" icon="terminal">
    Add `__pass_threshold` to the scorer's metadata (value between 0 and 1):

    ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    metadata: {
      __pass_threshold: 0.7,  // Scores below 0.7 are considered failures
    }
    ```

    Example with a custom code scorer:

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      project.scorers.create({
        name: "Quality checker",
        slug: "quality-checker",
        handler: async ({ output, expected }) => {
          return output === expected ? 1 : 0;
        },
        metadata: {
          __pass_threshold: 0.8,
        },
      });
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      @project.scorers.create(
          name="Quality checker",
          slug="quality-checker",
          metadata={"__pass_threshold": 0.8},
      )
      def quality_checker(output, expected):
          return 1 if output == expected else 0
      ```
    </CodeGroup>
  </Tab>

  <Tab title="UI" icon="mouse-pointer-2">
    When creating or editing a scorer in the UI:

    1. Look for the **Pass threshold** slider in the scorer configuration.
    2. Drag the slider to set your minimum acceptable score (0-1).
    3. Click **Save as custom scorer**.

    The threshold can be set for any scorer type (autoevals, LLM-as-a-judge, or custom code).
  </Tab>
</Tabs>

## Test scorers

Scorers need to be developed iteratively against real data. When creating or editing a scorer in the UI, use the <Icon icon="play" /> **Run** section to test your scorer with data from different sources. Each variable source populates the scorer's input parameters (like `input`, `output`, `expected`, `metadata`) from a different location.

### Test with manual input

Best for initial development when you have a specific example in mind. Use this to quickly prototype and verify basic scorer logic before testing on larger datasets.

1. Select **Editor** in the <Icon icon="play" /> **Run** section.
2. Enter values for `input`, `output`, `expected`, and `metadata` fields.
3. Click **Test** to see how your scorer evaluates the example
4. Iterate on your scorer logic based on the results

### Test with a dataset

Best for testing specific scenarios, edge cases, or regression testing. Use this when you want controlled, repeatable test cases or need to ensure your scorer handles specific situations correctly.

1. Select **Dataset** in the <Icon icon="play" /> **Run** section.
2. Choose a dataset from your project.
3. Select a record to test with.
4. Click **Test** to see how your scorer evaluates the example.
5. Review results to identify patterns and edge cases.

### Test with logs

Best for testing against actual usage patterns and debugging real-world edge cases. Use this when you want to see how your scorer performs on data your system is actually generating.

1. Select **Logs** in the <Icon icon="play" /> **Run** section.
2. Select the project containing the logs you want to test against.
3. Filter logs to find relevant examples:
   * Click <Icon icon="list-filter" /> **Add filter** and choose just root spans, specific span names, or a more advanced filter based on specific input, output, metadata, or other values.
   * Select a timeframe.
4. Click **Test** to see how your scorer evaluates real production data.
5. Identify cases where the scorer needs adjustment for real-world scenarios.

<Tip>
  To create a new online scoring rule with the filters automatically prepopulated from your current log filters, click <Icon icon="radio" /> **Online scoring**. This enables rapid iteration from logs to scoring rules. See [Create scoring rules](/observe/score-online#create-scoring-rules) for more details.
</Tip>

## Scorer permissions

Both [LLM-as-a-judge scorers](#llm-as-a-judge) and [custom code scorers](#custom-code) automatically receive a `BRAINTRUST_API_KEY` environment variable that allows them to:

* Make LLM calls using organization and project AI secrets
* Access attachments from the current project
* Read and write logs to the current project
* Read prompts from the organization

For custom code scorers that need expanded permissions beyond the current project (such as logging to other projects, reading datasets, or accessing other organization data), you can provide your own API key using the [`PUT /v1/env_var`](https://www.braintrust.dev/docs/api-reference/envvars/create-or-replace-env_var#create-or-replace-env_var) endpoint.

## Optimize with Loop

Generate and improve scorers using Loop:

Example queries:

* "Write an LLM-as-a-judge scorer for a chatbot that answers product questions"
* "Generate a code-based scorer based on project logs"
* "Optimize the Helpfulness scorer"
* "Adjust the scorer to be more lenient"

Loop can also tune scorers based on manual labels from the playground.

## Best practices

**Start with autoevals**: Use pre-built scorers when they fit your needs. They're well-tested and reliable.

**Be specific**: Define clear evaluation criteria in your scorer prompts or code.

**Use multiple scorers**: Measure different aspects (factuality, helpfulness, tone) with separate scorers.

**Choose the right scope**: Use trace scorers (custom code with `trace` parameter) for multi-step workflows and agents. Use output scorers for simple quality checks.

**Test scorers**: Run scorers on known examples to verify they behave as expected.

**Version scorers**: Like prompts, scorers are versioned automatically. Track what works.

**Balance cost and quality**: LLM-as-a-judge scorers are more flexible but cost more and take longer than custom code scorers.

## Next steps

* [Run evaluations](/evaluate/run-evaluations) using your scorers
* [Interpret results](/evaluate/interpret-results) to understand scores
* [Write prompts](/evaluate/write-prompts) to guide model behavior
* [Use playgrounds](/evaluate/playgrounds) to test scorers interactively
