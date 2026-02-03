# Source: https://braintrust.dev/docs/evaluate/interpret-results.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Interpret evaluation results

> Understand scores, identify issues, and find improvement opportunities

To view the results of an evaluation, go to <Icon icon="beaker" /> **Experiments** in your project and select an experiment from the list.

### View summaries

The summary pane displays:

* Comparisons to other experiments
* Scorers used in the evaluation
* Datasets tested
* Metadata like model and parameters

Copy the experiment ID from the bottom of the summary pane for referencing in code or sharing with teammates.

## Understand metrics

Braintrust tracks these metrics automatically:

* **Duration**: Time to complete the task span
* **Offset**: Time elapsed since trace start
* **Prompt tokens**: Tokens in the input
* **Completion tokens**: Tokens in the output
* **Total tokens**: Combined token count
* **LLM duration**: Time spent in LLM calls
* **Estimated cost**: Approximate cost based on pricing

Metrics are computed on the `task` subspan, excluding LLM-as-a-judge scorer calls.

<Note>
  To compute LLM metrics, wrap your LLM calls with [Braintrust provider wrappers](/integrations).
</Note>

## Change the display

### Switch the view

Each project includes locked default views that cannot be modified, including:

* **Non-errors**: Shows only records without errors
* **Errors**: Shows only records with errors
* **Scorer errors**: Shows only records with scorer errors
* **Unreviewed**: Hides items that have been human-reviewed
* **Assigned to me**: Shows only records assigned to the current user for human review

Use the <Icon icon="layers-2" /> **View** menu to switch the view.

* To set the current view as default, select **Manage view** > **Set as your default view**.
* To discard unsaved changes and return to the default view, select **Reset**.

### Create a custom view

Custom views save your table configurations including filters, sorts, column order, column visibility, and display settings. This lets you quickly switch between different ways of analyzing your experiments.

To create a custom view:

1. Apply the filters, sorts, columns, and display settings you want.
2. Select **Save as** in the toolbar.
3. Enter a view name.

Views are accessible and configurable by any member of the organization.

When you create a custom view and set it as your default, it becomes your personal default view. The system default views remain available to all team members.

### Show and hide columns

Select <Icon icon="settings-2" /> **Display** > **Columns** and then:

* Show or hide columns to focus on relevant data
* Reorder columns by dragging them
* Pin important columns to the left

All column settings are automatically saved when you save a view.

### Create custom columns

Extract specific values from traces using custom columns:

1. Select <Icon icon="settings-2" /> **Display** > **Columns** > **+ Add custom column**.
2. Name your column.
3. Choose from inferred fields or write a SQL expression.

<video className="border rounded-md" loop autoPlay muted poster="/images/core/experiments/create-column-dialog-poster.png">
  <source src="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/create-column-dialog.mp4?fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=2b3f0a5192b81954f205f7caf295c3a0" type="video/mp4" data-path="images/core/experiments/create-column-dialog.mp4" />
</video>

Once created, filter and sort using your custom columns.

### Group results

Select <Icon icon="settings-2" /> **Display** > **Group by** to group the table by metadata fields to see patterns.

By default, group rows show one experiment's summary data. To view summary data for all experiments, select **Include comparisons in group**.

### Order by regressions

Score and metric columns show summary statistics in their headers. To order columns by regressions, select <Icon icon="settings-2" /> **Display** > **Columns** > **Order by regressions**.

Within grouped tables, this sorts rows by regressions of a specific score relative to a comparison experiment.

### Filter results

Select <Icon icon="list-filter" /> **Filter** to open the filter menu. Use the **Basic** tab for point-and-click filtering, or switch to **SQL** to write precise queries. The SQL editor includes <Icon icon="blend" /> **Generate** button that creates queries from natural language descriptions.

### Adjust table layout

To change the table density to see more or less detail per row, select <Icon icon="settings-2" /> **Display** > **Row height** > **Compact** or **Tall**.

To switch between different layouts, select <Icon icon="settings-2" /> **Display** > **Layout** and one of the following:

* List: Default table view.
* Grid: Compare outputs side-by-side.
* Summary: Large-type summary of scores and metrics across all experiments.

Layouts respect view filters and are automatically saved when you save a view.

## Examine individual traces

Select any row to open the trace view and see complete details:

* Input, output, and expected values
* Metadata and parameters
* All spans in the trace hierarchy
* Scores and their explanations
* Timing and token usage

<img src="https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/trace.png?fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=533697a2e36b8aa1e54cefa4e152b432" alt="Trace view" data-og-width="2372" width="2372" data-og-height="1516" height="1516" data-path="images/core/experiments/trace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/trace.png?w=280&fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=e9a2a837755dda8f762a11e85f0ea67d 280w, https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/trace.png?w=560&fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=cf7592a569f31dcef51baeb71ce4bf70 560w, https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/trace.png?w=840&fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=6b2cff2f3b365e8369a93a18eb7ad12c 840w, https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/trace.png?w=1100&fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=79af603c7015a4f7fd48661d080daf91 1100w, https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/trace.png?w=1650&fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=c751837ad787d8b7b7ff0cc8c0602a94 1650w, https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/trace.png?w=2500&fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=64b969d78c6a090c1264c1c2d2c2099a 2500w" />

Ask yourself: Do good scores correspond to good outputs? If not, update your scorers or test cases.

### Use aggregate scores

Aggregate scores combine multiple scores into a single metric. They are useful when you track many scores but need a single metric to represent overall experiment quality.

See [Create aggregate scores](/admin/projects#create-aggregate-scores) for more details.

### Score retrospectively

Apply scorers to existing experiments:

* **Multiple cases**: Select rows and use <Icon icon="percent" /> **Score** to apply chosen scorers
* **Single case**: Open a trace and use <Icon icon="percent" /> **Score** in the trace view

Scores appear as additional spans within the trace.

### View raw trace data

When viewing a trace, select a span and then select the <Icon icon="braces" /> button in the span's header to view the complete JSON representation. The raw data view shows all fields including metadata, inputs, outputs, and internal properties that may not be visible in other views.

The raw data view has two tabs:

* **This span** - Shows the complete JSON for the selected span only
* **Full trace** - Shows the complete JSON for the entire trace

Use the search bar at the top of the dialog to find specific content within the data.

Raw span data is useful when you need to:

* Inspect the complete span structure for debugging
* Find specific fields in large or deeply nested spans
* Verify exact values and data types
* Export or copy the full span for reproduction

## Analyze across experiments

Compare performance across multiple experiments using visualizations.

### Bar chart

On the Experiments page, view scores as a bar chart by selecting **Score comparison** from the X axis selector:

<video className="border rounded-md" loop autoPlay muted poster="/images/core/experiments/bar-score-comparison-poster.png">
  <source src="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/bar-score-comparison.mp4?fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=b25cb61270d179bd0a54ff73a1039167" type="video/mp4" data-path="images/core/experiments/bar-score-comparison.mp4" />
</video>

Group by metadata fields to create comparative bar charts:

<video className="border rounded-md" loop autoPlay muted poster="/images/core/experiments/group-by-dataset-poster.png">
  <source src="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/group-by-dataset.mov?fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=31e804217b233da7a4ad8e91de1839b7" type="video/mp4" data-path="images/core/experiments/group-by-dataset.mov" />
</video>

### Scatter plot

Select a metric on the x-axis to construct scatter plots. For example, compare the relationship between accuracy and duration:

<video className="border rounded-md" loop autoPlay muted poster="/images/core/experiments/scatterplot-poster.png">
  <source src="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/scatterplot.gif?fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=88b9ccd8f7e748c2d70e61e9cb0d047a" type="video/mp4" data-path="images/core/experiments/scatterplot.gif" />
</video>

## Export experiments

<Tabs>
  <Tab title="UI" icon="mouse-pointer-2">
    To export an experiment's results, open the menu next to the experiment name. You can export as CSV or JSON, and choose whether to download all fields.

        <img src="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/exporting-experiments.png?fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=c9d392fe5158555fa7547107c478ee4e" alt="Export experiments" data-og-width="2198" width="2198" data-og-height="1496" height="1496" data-path="images/core/experiments/exporting-experiments.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/exporting-experiments.png?w=280&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=eeb59d6a70a7b33e6661e46120719c56 280w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/exporting-experiments.png?w=560&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=fa9380daa3d79bad13d74ba638f585bc 560w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/exporting-experiments.png?w=840&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=db8ab9c4f1464a59d7f37b91ba85ed77 840w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/exporting-experiments.png?w=1100&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=cb2f3c5a357b0d4eb444eef87b82888d 1100w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/exporting-experiments.png?w=1650&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=c7d91686711eeff3b2f30bcd494d5bfb 1650w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/exporting-experiments.png?w=2500&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=038b655e9fdc2682ec9d60d05bd73bb7 2500w" />
  </Tab>

  <Tab title="SDK" icon="terminal">
    Access data from previous experiments by passing the `open` flag to `init()`:

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import { init } from "braintrust";

      async function openExperiment() {
        const experiment = init("My Project", {
          experiment: "my-experiment",
          open: true,
        });

        for await (const testCase of experiment) {
          console.log(testCase);
        }
      }
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import braintrust

      def open_experiment():
          experiment = braintrust.init(
              project="My Project",
              experiment="my-experiment",
              open=True,
          )
          for test_case in experiment:
              print(test_case)
      ```
    </CodeGroup>

    Convert experiments to dataset format using `asDataset()`/`as_dataset()`:

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import { init } from "braintrust";

      async function openExperiment() {
        const experiment = init("My Project", {
          experiment: "my-experiment",
          open: true,
        });

        for await (const testCase of experiment.asDataset()) {
          console.log(testCase);
        }
      }
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import braintrust

      def open_experiment():
          experiment = braintrust.init(
              project="My Project",
              experiment="my-experiment",
              open=True,
          )
          for test_case in experiment.as_dataset():
              print(test_case)
      ```
    </CodeGroup>
  </Tab>

  <Tab title="API" icon="code">
    Fetch experiment events via the API using [Fetch experiment (POST form)](https://www.braintrust.dev/docs/api-reference#fetch-experiment-post-form) or [Fetch experiment (GET form)](https://www.braintrust.dev/docs/api-reference#fetch-experiment-get-form).

    You can also query experiments with SQL for custom analysis. For example, to check review status:

    <CodeGroup dropdown>
      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import os
      import requests

      API_URL = "https://api.braintrust.dev/"
      headers = {"Authorization": "Bearer " + os.environ["BRAINTRUST_API_KEY"]}

      def fetch_experiment_review_status(experiment_id: str) -> dict:
          # Replace "response quality" with your review score column name
          query = f"""
          SELECT
            sum(CASE WHEN scores."response quality" IS NOT NULL THEN 1 ELSE 0 END) AS reviewed,
            sum(CASE WHEN is_root THEN 1 ELSE 0 END) AS total
          FROM experiment('{experiment_id}')
          """

          return requests.post(
              f"{API_URL}/btql",
              headers=headers,
              json={"query": query, "fmt": "json"},
          ).json()

      # Usage
      result = fetch_experiment_review_status("your-experiment-id")
      print(f"Reviewed: {result['data'][0]['reviewed']}/{result['data'][0]['total']}")
      ```

      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      const API_URL = "https://api.braintrust.dev/";
      const headers = {
        Authorization: `Bearer ${process.env.BRAINTRUST_API_KEY}`,
      };

      async function fetchExperimentReviewStatus(experimentId: string) {
        // Replace "response quality" with your review score column name
        const query = `
          SELECT
            sum(CASE WHEN scores."response quality" IS NOT NULL THEN 1 ELSE 0 END) AS reviewed,
            sum(CASE WHEN is_root THEN 1 ELSE 0 END) AS total
          FROM experiment('${experimentId}')
        `;

        const response = await fetch(`${API_URL}/btql`, {
          method: "POST",
          headers,
          body: JSON.stringify({ query, fmt: "json" }),
        });

        return await response.json();
      }

      // Usage
      const result = await fetchExperimentReviewStatus("your-experiment-id");
      console.log(`Reviewed: ${result.data[0].reviewed}/${result.data[0].total}`);
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Next steps

* [Compare experiments](/evaluate/compare-experiments) systematically
* [Write scorers](/evaluate/write-scorers) to measure what matters
* [Use playgrounds](/evaluate/playgrounds) for rapid iteration
* [Run evaluations](/evaluate/run-evaluations) in CI/CD
