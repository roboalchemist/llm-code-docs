# Source: https://braintrust.dev/docs/annotate/datasets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Build datasets

> Create, manage, and version test cases for systematic evaluation

Datasets are versioned collections of test cases that you use to run evaluations and track improvements over time. Build datasets from production logs, user feedback, manual curation, or generate them with Loop.

After reviewing traces with scores and labels, compile them into structured datasets for evaluation.

## Why use datasets

Datasets in Braintrust have key advantages:

* **Integrated**: Use directly in evaluations, explore in playgrounds, and populate from production.
* **Versioned**: Every change is tracked, so experiments can pin to specific versions.
* **Scalable**: Stored in a modern data warehouse without storage or performance limits.
* **Secure**: Self-hosted deployments keep data in your warehouse.

## Create datasets

<Tabs>
  <Tab title="UI" icon="mouse-pointer-2">
    ### Upload CSV/JSON

    The fastest way to create a dataset is uploading a CSV or JSON file:

    1. Go to <Icon icon="database" /> **Datasets**.
    2. If there are existing datasets, click **+ Dataset**. Otherwise, click <Icon icon="upload" /> **Upload CSV/JSON**.
    3. Drag and drop your file in the **Upload dataset** dialog.
    4. Columns automatically map to the `input` field. Drag and drop them into different categories as needed:

       * **Input**: Fields used as inputs for your task.
       * **Expected**: Ground truth or ideal outputs for scoring.
       * **Metadata**: Additional context for filtering and grouping.
       * **Tags**: Labels for organizing and filtering. When you categorize columns as tags, they're automatically added to your project's [tag configuration](/admin/projects#add-tags).
       * **Do not import**: Exclude columns from the dataset.

       The preview table updates in real-time as you move columns between categories, showing exactly how your dataset will be structured.
    5. Click **Import**.

    <Note>
      If your data includes an `id` field, duplicate rows will be deduplicated, with only the last occurrence of each ID kept.
    </Note>

    ### Generate with Loop

    Ask Loop to create a dataset based on your logs or specific criteria:

        <img src="https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/generate-dataset-from-logs.png?fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=37336e72e52b9f902fd94930efe6c3b2" alt="Generate dataset from logs" data-og-width="2196" width="2196" data-og-height="1440" height="1440" data-path="images/core/loop/generate-dataset-from-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/generate-dataset-from-logs.png?w=280&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=785ed8b42659598dda1691b56f699551 280w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/generate-dataset-from-logs.png?w=560&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=24ec8f783bf99431a47667810d6b5142 560w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/generate-dataset-from-logs.png?w=840&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=1faf0cd0f303fe9cd24f0b6de0b67818 840w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/generate-dataset-from-logs.png?w=1100&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=0865dfcd4958a651495a7567ddab5355 1100w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/generate-dataset-from-logs.png?w=1650&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=c0f7badaa8b6b2f3d501f542651f458c 1650w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/generate-dataset-from-logs.png?w=2500&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=29a88190e99b6b806bb29b005b154ad7 2500w" />

    Example queries:

    * "Generate a dataset from the highest-scoring examples in this experiment"
    * "Create a dataset with the most common inputs in the logs"

    ### Add records manually

    Once you've created a dataset, add or edit records directly in the UI:

        <img src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/datasets/Edit-record.gif?s=ff905fd0f3d7fca2c1abed12537de762" alt="Edit record" data-og-width="1753" width="1753" data-og-height="1152" height="1152" data-path="images/guides/datasets/Edit-record.gif" data-optimize="true" data-opv="3" />

    ### From user feedback

    User feedback from production provides valuable test cases that reflect real user interactions. Use feedback to create datasets from highly-rated examples or problematic cases.

    See [Capture user feedback](/instrument/user-feedback) for implementation details on logging feedback programmatically.

    To build datasets from feedback:

    1. Filter logs by feedback scores using the <Icon icon="list-filter" /> **Filter** menu:
       * `scores.user_rating > 0.8` (SQL) or `filter: scores.user_rating > 0.8` (BTQL) for highly-rated examples
       * `metadata.thumbs_up = false` for negative feedback
       * `comment IS NOT NULL and scores.correctness < 0.5` for low-scoring feedback with comments
    2. Select the traces you want to include.
    3. Select **Add to dataset**.
    4. Choose an existing dataset or create a new one.

    You can also ask Loop to create datasets based on feedback patterns, such as "Create a dataset from logs with positive feedback" or "Build a dataset from cases where users clicked thumbs down."
  </Tab>

  <Tab title="SDK" icon="terminal">
    Datasets are created automatically when you initialize them:

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import { initDataset } from "braintrust";

      async function main() {
        const dataset = initDataset("My App", { dataset: "My New Dataset" });
        console.log("Dataset created:", dataset);
      }

      main();
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import braintrust

      dataset = braintrust.init_dataset(project="My App", name="My New Dataset")
      print("Dataset created:", dataset)
      ```
    </CodeGroup>

    ### Insert records

    Add records programmatically with `insert()`:

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      for (let i = 0; i < 10; i++) {
        const id = dataset.insert({
          input: { question: `What is ${i}?` },
          expected: { answer: `${i} is a number` },
          metadata: { category: i % 2 === 0 ? "even" : "odd" },
        });
        console.log("Inserted record with id", id);
      }
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      for i in range(10):
          id = dataset.insert(
              input={"question": f"What is {i}?"},
              expected={"answer": f"{i} is a number"},
              metadata={"category": "even" if i % 2 == 0 else "odd"},
          )
          print("Inserted record with id", id)
      ```
    </CodeGroup>

    ### Log from production

    Track user feedback from your application:

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import { initDataset, Dataset } from "braintrust";

      class MyApplication {
        private dataset: Dataset | undefined = undefined;

        async initApp() {
          this.dataset = await initDataset("My App", { dataset: "logs" });
        }

        async logUserExample(
          input: any,
          expected: any,
          userId: string,
          thumbsUp: boolean,
        ) {
          if (this.dataset) {
            this.dataset.insert({
              input,
              expected,
              metadata: { userId, thumbsUp },
            });
          }
        }
      }
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import braintrust

      class MyApplication:
          def init_app(self):
              self.dataset = braintrust.init_dataset(project="My App", name="logs")

          def log_user_example(self, input, expected, user_id, thumbs_up):
              if self.dataset:
                  self.dataset.insert(
                      input=input,
                      expected=expected,
                      metadata={"user_id": user_id, "thumbs_up": thumbs_up},
                  )
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Dataset structure

Each record has three top-level fields:

* **input**: Data to recreate the example in your application (required).
* **expected**: Ideal output or ground truth (optional but recommended for evaluation).
* **metadata**: Key-value pairs for filtering and grouping (optional).

## View and edit datasets

<img src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/datasets/datasets.webp?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=c09b283688cf7b4b11e97bb7431974a3" alt="Dataset Viewer" data-og-width="3008" width="3008" data-og-height="670" height="670" data-path="images/guides/datasets/datasets.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/datasets/datasets.webp?w=280&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=48c4e43e3d672e9b1485e920d4eddbbd 280w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/datasets/datasets.webp?w=560&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=ec691abfcdaa57287eac71144f6f3510 560w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/datasets/datasets.webp?w=840&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=6fa914caec8c53163315b190ed3736e3 840w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/datasets/datasets.webp?w=1100&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=cb4ebc5d24e388cb9b53c97df8725123 1100w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/datasets/datasets.webp?w=1650&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=d7046926a7f63130671410846d982ea2 1650w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/datasets/datasets.webp?w=2500&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=3eae3a866e913bc5debf367436390125 2500w" />

From the dataset page, you can:

* Filter and search records
* Create custom columns to extract nested values
* Edit records inline
* Copy records between datasets
* Delete individual records or entire datasets

### Create custom columns

Extract values from records using [custom columns](/evaluate/interpret-results#create-custom-columns). Use SQL expressions to surface important fields directly in the table.

## Label datasets

Configure categorical scores to allow reviewers to rapidly label records. See [Configure review scores](/annotate/human-review#configure-review-scores) for details.

<img src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=406359641fc9f3de4f70086d56f236dd" alt="Write to expected" data-og-width="1852" width="1852" data-og-height="966" height="966" data-path="images/guides/human-review/expected-fields.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=280&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=74c2817c643f44e6bf10b5c872ad988b 280w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=560&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=2504bd28d1b54f4430d7458fd407be25 560w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=840&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=5691362eca4b4c03f9b2dbf32873bb51 840w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=1100&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=2d93b28ed1d8d7f62d65c15b4786a762 1100w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=1650&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=e2ee18d7f67b4b4f89c08d765a7734bb 1650w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=2500&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=a44f9ea41167ce86f27a572aac1c3f7d 2500w" />

## Define schemas

Dataset schemas let you define JSON schemas for `input`, `expected`, and `metadata` fields. Schemas enable:

* **Validation**: Ensure records conform to your structure.
* **Form-based editing**: Edit records with intuitive forms instead of raw JSON.

### Infer from data

Automatically generate schemas from existing data:

1. Open the schema editor for a field.
2. Click **Infer schema**.
3. The schema generates from the first 100 records.

### Enable enforcement

Toggle **Enforce** in the schema editor to validate all records. When enabled:

* New records must conform or show validation errors.
* Existing non-conforming records display warnings.
* Form editing validates input automatically.

<Note>
  Enforcement is UI-only and doesn't affect SDK inserts or updates.
</Note>

## Read and filter datasets

<Tabs>
  <Tab title="UI" icon="mouse-pointer-2">
    Use the filter menu to narrow dataset views, or write SQL queries for complex filtering. See [Filter and search](/observe/filter) for details.
  </Tab>

  <Tab title="SDK" icon="terminal">
    Read datasets with the same method used to create them:

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      const dataset = initDataset("My App", { dataset: "My Existing Dataset" });

      // Loads in batches to avoid memory issues
      for await (const row of dataset) {
        console.log(row);
      }
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      dataset = braintrust.init_dataset(project="My App", name="My Existing Dataset")

      for row in dataset:
          print(row)
      ```
    </CodeGroup>

    ### Filter with SQL

    Use `_internal_btql` to filter, sort, and limit records:

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      const dataset = initDataset("My App", {
        dataset: "My Dataset",
        _internal_btql: {
          filter: { btql: "metadata.category = 'premium'" },
          sort: [{ expr: { btql: "created" }, dir: "desc" }],
          limit: 100,
        },
      });
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      dataset = braintrust.init_dataset(
          project="My App",
          name="My Dataset",
          _internal_btql={
              "filter": {"btql": "metadata.category = 'premium'"},
              "sort": [{"expr": {"btql": "created"}, "dir": "desc"}],
              "limit": 100,
          },
      )
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Track performance

Monitor how dataset rows perform across experiments:

### View experiment runs

See all experiments that used a dataset:

1. Go to your dataset page.
2. In the right panel, select <Icon icon="play" /> **Runs**.
3. Review performance metrics across experiments.

Runs display as charts that show score trends over time. The time axis flows from oldest (left) to newest (right), making it easy to track performance evolution.

<img src="https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRuns.png?fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=1707b131eb5221f97b1efa1c5f1e7cc7" alt="Dataset experiment runs" data-og-width="3004" width="3004" data-og-height="1422" height="1422" data-path="core/datasets/datasetRuns.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRuns.png?w=280&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=5083cf7b224a32cd9cbcaded0ac6e3d8 280w, https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRuns.png?w=560&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=9ca03299384e6dd5907b8b9a6943c99b 560w, https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRuns.png?w=840&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=a543f104db72280b106ff1dd446f5a16 840w, https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRuns.png?w=1100&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=2040391f346b2b6598e126add48b53a5 1100w, https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRuns.png?w=1650&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=195cf495ae74a45f3e69672a6339bc48 1650w, https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRuns.png?w=2500&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=0817b0e4848d7e45ed2b92020b3e472f 2500w" />

### Filter experiment runs

To narrow down the list of experiment runs, you can filter by time range or use SQL.

**Filter by time range**: Click and drag across any region of the chart to select a time range. The table below updates to show only experiments in that range. To clear the filter, click **clear**. This helps you focus on specific periods, like recent experiments or historical baselines.

**Filter with SQL**: Select <Icon icon="list-filter" /> **Filter** and use the **Basic** tab for common filters, or switch to **SQL** to write more precise [SQL queries](/reference/sql) based on criteria like score thresholds, time ranges, or experiment names.

Common filtering examples:

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Filter by time range
  WHERE created > '2024-01-01'

  -- Filter by score threshold
  WHERE scores.Accuracy > 0.8

  -- Filter by experiment name pattern
  WHERE name LIKE '%baseline%'

  -- Combine multiple conditions
  WHERE created > now() - interval 7 day
    AND scores.Factuality > 0.7
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Filter by time range
  filter: created > '2024-01-01'

  -- Filter by score threshold
  filter: scores.Accuracy > 0.8

  -- Filter by experiment name pattern
  filter: name LIKE '%baseline%'

  -- Combine multiple conditions
  filter:
    created > now() - interval 7 day and
    scores.Factuality > 0.7
  ```
</CodeGroup>

<Note>
  Filter states are persisted in the URL, allowing you to bookmark or share specific filtered views of experiment runs.
</Note>

### Analyze per-row performance

See how individual rows perform:

1. Select a row in the dataset table.
2. In the right panel, select <Icon icon="play" /> **Runs**.
3. Review the row's metrics across experiments.

<Note>
  This view only shows experiments that set the `origin` field in eval traces.
</Note>

<img src="https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRowRuns.png?fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=2ef7ff5bcd7459048d858f378f61eecc" alt="Dataset row performance" data-og-width="2996" width="2996" data-og-height="1432" height="1432" data-path="core/datasets/datasetRowRuns.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRowRuns.png?w=280&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=20cd94924eaaec842ba71c59205ae216 280w, https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRowRuns.png?w=560&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=3e9f79eeee68dec86addff54328c5dd4 560w, https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRowRuns.png?w=840&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=165728bac2f9bb2a940c4ac1c9b23154 840w, https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRowRuns.png?w=1100&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=6e8e6438c1c6c35708316241c4237553 1100w, https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRowRuns.png?w=1650&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=0d5eb17737c78f8ab7c74cd6889edad6 1650w, https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRowRuns.png?w=2500&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=7bbaac0cb7c632cf5fd6cec1cb8cd06c 2500w" />

Look for patterns:

* Consistently low scores suggest ambiguous expectations.
* Failures across experiments indicate edge cases.
* High variance suggests instability.

## Multimodal datasets

You can store and process images and other file types in your datasets. There are several ways to use files in Braintrust:

* **Image URLs** (most performant) - Keep datasets lightweight with external image references.
* **Base64** (least performant) - Encode images directly in records.
* **Attachments** (easiest to manage) - Store files directly in Braintrust.
* **External attachments** - Reference files in your own object stores.

For large images, use image URLs to keep datasets lightweight. To keep all data within Braintrust, use attachments. Attachments support any file type including images, audio, and PDFs.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Attachment, initDataset } from "braintrust";
  import path from "node:path";

  async function createPdfDataset(): Promise<void> {
    const dataset = initDataset({
      project: "Project with PDFs",
      dataset: "My PDF Dataset",
    });
    for (const filename of ["example.pdf"]) {
      dataset.insert({
        input: {
          file: new Attachment({
            filename,
            contentType: "application/pdf",
            data: path.join("files", filename),
          }),
        },
      });
    }
    await dataset.flush();
  }

  createPdfDataset();
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os
  from braintrust import Attachment, init_dataset

  def create_pdf_dataset() -> None:
      dataset = init_dataset("Project with PDFs", "My PDF Dataset")
      for filename in ["example.pdf"]:
          dataset.insert(
              input={
                  "file": Attachment(
                      filename=filename,
                      content_type="application/pdf",
                      data=os.path.join("files", filename),
                  )
              },
          )
      dataset.flush()

  create_pdf_dataset()
  ```
</CodeGroup>

## Use in evaluations

Pass datasets directly to `Eval()`:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { initDataset, Eval } from "braintrust";
  import { Levenshtein } from "autoevals";

  Eval("Say Hi Bot", {
    data: initDataset("My App", { dataset: "My Dataset" }),
    task: async (input) => {
      return "Hi " + input;
    },
    scores: [Levenshtein],
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from autoevals import Levenshtein
  from braintrust import Eval, init_dataset

  Eval(
      "Say Hi Bot",
      data=init_dataset(project="My App", name="My Dataset"),
      task=lambda input: "Hi " + input,
      scores=[Levenshtein],
  )
  ```
</CodeGroup>

## Next steps

* [Add human feedback](/annotate/human-review) to label datasets.
* [Run evaluations](/evaluate/run-evaluations) using your datasets.
* [Use the Loop](/observe/loop) to generate and optimize datasets.
* Read the [SQL reference](/reference/sql) for advanced filtering.
