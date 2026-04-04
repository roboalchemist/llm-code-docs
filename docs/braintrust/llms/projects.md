# Source: https://braintrust.dev/docs/admin/projects.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage projects

> Configure project settings and features

Projects organize AI features in your application. Each project contains logs, experiments, datasets, prompts, and other functions. Configure project-specific settings to customize behavior for your use case.

## Create a project

<Tabs>
  <Tab title="UI" icon="mouse-pointer-2">
    1. Navigate to your organization's project list
    2. Click **+ Project**
    3. Enter a project name
    4. Optionally add a description
    5. Click **Create**
  </Tab>

  <Tab title="SDK" icon="terminal">
    <Note>
      If a project already exists, `projects.create()` returns a handle. There is no separate `.get()` method.
    </Note>

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import * as braintrust from "braintrust";

      // Get a handle to the project (creates if it doesn't exist)
      const project = braintrust.projects.create({ name: "my-project" });

      // Use the project to create functions
      project.prompts.create({...});
      project.tools.create({...});
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import braintrust

      # Get a handle to the project (creates if it doesn't exist)
      project = braintrust.projects.create(name="my-project")

      # Use the project to create functions
      project.prompts.create(...)
      project.tools.create(...)
      ```
    </CodeGroup>

    Projects are automatically created when initializing experiments or loggers:

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import * as braintrust from "braintrust";

      // Creates "my-project" if it doesn't exist
      const experiment = braintrust.init("my-project", {
        experiment: "my-experiment"
      });
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import braintrust

      # Creates "my-project" if it doesn't exist
      experiment = braintrust.init(
          project="my-project",
          experiment="my-experiment"
      )
      ```
    </CodeGroup>

    For more details, see the SDK reference for [Python](/reference/sdks/python#projectbuilder) or [TypeScript](/reference/sdks/typescript#projectbuilder).
  </Tab>
</Tabs>

## Configure AI providers

Project-level AI provider keys override [organization-level keys](/admin/organizations#configure-ai-providers). Use project-level keys when:

* Different projects need separate billing or rate limits
* You want to isolate API usage by project
* Projects require different provider accounts or credentials

You can also configure project-level AI providers inline from playgrounds within that project. When running a playground, you can set up providers without navigating to configuration settings.

To configure project-level AI providers:

1. Navigate to your project.
2. Go to <Icon icon="settings-2" /> **Configuration**.
3. Under **Project**, select **Project AI providers**.
4. Click the provider you want to configure.
5. Enter your API key for that provider.
6. Click **Save**.

Project-level providers are available in a project's playgrounds, experiments, and when using the AI Proxy with the project's context.

<Note>
  API keys are encrypted at rest using [transparent data encryption](https://en.wikipedia.org/wiki/Transparent_data_encryption) with a [unique 256-bit key and nonce](https://libsodium.gitbook.io/doc/secret-key_cryptography/aead).
</Note>

### Add custom providers

Braintrust supports custom AI providers at both the organization and project level. See [Custom providers](/integrations/ai-providers/custom) for details on configuring custom endpoints.

## Add tags

Tags help organize and filter logs, datasets, and experiments:

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Project**, select **Tags**.
3. Click **Add tag**.
4. Enter tag details:
   * **Name**: Tag identifier.
   * **Color**: Visual indicator.
   * **Description**: Optional explanation.
5. Click **Save**.

Use tags to track data by user type, feature, environment, or any custom category. Filter by tags in logs, experiments, and datasets. For more information about using tags, see [View logs](/observe/view-logs#tags-and-queues).

## Configure human review

Review scores appear in all logs and experiments in a project. Use them for quality control, data labeling, or [feedback collection](/annotate/human-review).

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Project**, select **Human review**.
3. Click **+ Human review score**.
4. Enter a name and description for your score. Descriptions support Markdown.
5. Select a score type:
   * **Categorical score**: Predefined options with assigned scores. Each option gets a unique percentage value between 0% and 100% (stored as 0 to 1). Use for classification tasks like sentiment or correctness categories. Also supports writing to the `expected` field instead of creating a score.
   * **Continuous score**: Numeric values between 0% and 100% with a slider input control. Use for subjective quality assessments like helpfulness or tone.
   * **Free-form input**: String values written to the `metadata` field at a specified path. Use for explanations, corrections, or structured feedback.
6. Click **Save**.

<Tip>
  You can also create human review scores as you review traces. In the trace view, click **+ Human review score** and define the score as described above.
</Tip>

For more information, see [Add human feedback](/annotate/human-review).

## Create aggregate scores

Combine multiple scores into a single metric:

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Project**, select **Aggregate scores**.
3. Click **Add aggregate score**.
4. Define the aggregation:
   * **Name**: Score identifier.
   * **Type**: Weighted average, minimum, or maximum.
   * **Selected scores**: Scores to aggregate.
   * **Weights**: For weighted averages, set score weights.
   * **Description**: Optional explanation.
5. Click **Save**.

Aggregate scores appear in experiment summaries and comparisons. Use them to create composite quality metrics or overall performance indicators. For more information, see [Interpret evaluation results](/evaluate/interpret-results#use-aggregate-scores).

## Set up online scoring

Define project-level scoring rules that automatically evaluate production logs as they arrive. These rules can be created here or when creating and editing scorers.

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Project**, select **Online scoring**.
3. Click **Add rule**.
4. Configure the rule:
   * **Name**: Rule identifier.
   * **Scorers**: Select which scorers to run.
   * **Sampling rate**: Percentage of logs to evaluate (1-100%).
   * **Filter**: Optional SQL query to select specific logs.
   * **Span type**: Apply to root spans or all spans.
5. Click **Save**.

Online scoring rules run asynchronously in the background. View results in the logs page alongside other scores. Rules can also be created and managed when working with individual scorers. For more information, see [Create scoring rules](/observe/score-online#create-scoring-rules).

## Configure span iframes

Customize how specific span fields render in the UI:

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Project**, select **Span iframes**.
3. Click **Add iframe**.
4. Configure rendering:
   * **Field path**: Which field to render (e.g., `output.html`).
   * **iframe URL**: Template for the iframe src attribute.
5. Click **Save**.

Use span iframes to render HTML, charts, or custom visualizations directly in trace views. For more information, see [Extend traces](/instrument/advanced-tracing#custom-rendering-for-span-fields).

## Set comparison key

Customize how experiments match test cases:

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Project**, select **Advanced**.
3. Enter a SQL expression (default: `input`).
4. Click **Save**.

Examples:

* `input.question` - Match by question field only.
* `input.user_id` - Match by user.
* `[input.query, metadata.category]` - Match by multiple fields.

The comparison key determines which test cases are considered the same across experiments. For more information, see [Compare experiments](/evaluate/compare-experiments#customize-the-comparison-key).

## Edit project details

Update project name and description:

1. Navigate to your project.
2. Click **Edit project** in the top-right.
3. Modify name and description.
4. Click **Save**.

## Delete a project

<Warning>
  Deleting a project permanently removes all logs, experiments, datasets, and functions. This cannot be undone.
</Warning>

1. Navigate to **Configuration**.
2. Scroll to the bottom of the page.
3. Click **Delete project**.
4. Confirm by typing the project name.
5. Click **Delete**.

## Next steps

* [Control access](/admin/access-control) to projects with permission groups
* [Set up automations](/admin/automations) for project-specific alerts
* [View logs](/observe/view-logs) filtered by tags and metadata
* [Run evaluations](/evaluate/run-evaluations) on project datasets
