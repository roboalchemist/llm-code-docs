# Source: https://braintrust.dev/docs/core/datasets.md

# Datasets

Datasets allow you to collect data from production, staging, evaluations, and even manually, and then
use that data to run evaluations and track improvements over time.

For example, you can use Datasets to:

* Store evaluation test cases for your eval script instead of managing large JSONL or CSV files
* Log all production generations to assess quality manually or using model graded evals
* Store user reviewed (<Icon icon="thumbs-up" />, <Icon icon="thumbs-down" />) generations to find new test cases

In Braintrust, datasets have a few key properties:

* **Integrated**. Datasets are integrated with the rest of the Braintrust platform, so you can use them in
  evaluations, explore them in the playground, and log to them from your staging/production environments.
* **Versioned**. Every insert, update, and delete is versioned, so you can pin evaluations to a specific version
  of the dataset via the SDK.
* **Scalable**. Datasets are stored in a modern cloud data warehouse, so you can collect as much data as you want without worrying about
  storage or performance limits.
* **Secure**. If you run Braintrust [in your cloud environment](/guides/self-hosting), datasets are stored in your warehouse and
  never touch our infrastructure.

<Tabs>
  <Tab title="SDK" icon="terminal">
    ## Create a dataset

    Datasets are created automatically when you initialize them in the SDK.

    Records in a dataset are stored as JSON objects, and each record has three top-level fields:

    * `input` is a set of inputs that you could use to recreate the example in your application. For example, if you're logging
      examples from a question answering model, the input might be the question.
    * `expected` (optional) is the output of your model. For example, if you're logging examples from a question answering model, this
      might be the answer. You can access `expected` when running evaluations as the `expected` field; however, `expected` does not need to be
      the ground truth.
    * `metadata` (optional) is a set of key-value pairs that you can use to filter and group your data. For example, if you're logging
      examples from a question answering model, the metadata might include the knowledge source that the question came from.

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

    ## Read a dataset

    To read a dataset, use the same method as above for creating a dataset, but pass the name of the dataset you want to retrieve.

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      const dataset = initDataset("My App", { dataset: "My Existing Dataset" });

      // This will load the dataset in batches so large datasets aren't loaded entirely into memory.
      for await (const row of dataset) {
        console.log(row);
      }
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      dataset = braintrust.init_dataset(project="My App", name="My Existing Dataset")
      print("Dataset retrieved:")

      for row in dataset:
          print(row)
      ```
    </CodeGroup>

    ## Filter, sort, and limit datasets

    Use the `_internal_btql` parameter to filter, sort, and limit dataset records. This parameter accepts [BTQL](/reference/btql) query clauses to control which records are returned.

    <Note>
      The `_internal_btql` parameter uses the BTQL AST (Abstract Syntax Tree) format, not the string-based BTQL syntax shown in the UI. See examples below for the correct structure.
    </Note>

    ### Filter records

    The `filter` parameter is an object with a single `btql` field that contains the BTQL filter expression as a string.

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      const dataset = initDataset("My App", {
        dataset: "My Existing Dataset",
        _internal_btql: {
          filter: { btql: "metadata.user_type = 'premium' and input MATCH 'question'" },
          limit: 100,
        },
      });

      for await (const row of dataset) {
        console.log(row);
      }
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      dataset = braintrust.init_dataset(
          project="My App",
          name="My Existing Dataset",
          _internal_btql={
              "filter": {"btql": "metadata.user_type = 'premium' and input MATCH 'question'"},
              "limit": 100,
          },
      )

      for row in dataset:
          print(row)
      ```
    </CodeGroup>

    ### Sort records

    The `sort` parameter is an array of sort expressions with sort direction. The options are `"asc"` for ascending and `"desc"` for descending.

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      const dataset = initDataset("My App", {
        dataset: "My Existing Dataset",
        _internal_btql: {
          sort: [
            { expr: { btql: "created" }, dir: "desc" },
            { expr: { btql: "metadata.priority" }, dir: "asc" },
          ],
          limit: 50,
        },
      });
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      dataset = braintrust.init_dataset(
          project="My App",
          name="My Existing Dataset",
          _internal_btql={
              "sort": [
                  {"expr": {"btql": "created"}, "dir": "desc"},
                  {"expr": {"btql": "metadata.priority"}, "dir": "asc"},
              ],
              "limit": 50,
          },
      )
      ```
    </CodeGroup>

    ### Combine filters, sorts, and limits

    You can use both `filter` and `sort` parameters with multiple BTQL clauses to create complex queries.

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      const dataset = initDataset("My App", {
        dataset: "My Existing Dataset",
        _internal_btql: {
          filter: {
            btql: "metadata.domain = 'support' and created > now() - interval 7 day",
          },
          sort: [{ expr: { btql: "created" }, dir: "desc" }],
          limit: 1000,
        },
      });
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      dataset = braintrust.init_dataset(
          project="My App",
          name="My Existing Dataset",
          _internal_btql={
              "filter": {"btql": "metadata.domain = 'support' and created > now() - interval 7 day"},
              "sort": [{"expr": {"btql": "created"}, "dir": "desc"}],
              "limit": 1000,
          },
      )
      ```
    </CodeGroup>

    For more information on BTQL syntax and available operators, see the [BTQL reference documentation](/reference/btql).

    ## Insert records

    You can use the SDK to insert into a dataset:

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      for (let i = 0; i < 10; i++) {
        const id = dataset.insert({
          input: i,
          expected: { result: i + 1, error: null },
          metadata: { foo: i % 2 },
        });
        console.log("Inserted record with id", id);
      }
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      for i in range(10):
          id = dataset.insert(input=i, expected={"result": i + 1, "error": None}, metadata={"foo": i % 2})
          print("Inserted record with id", id)
      ```
    </CodeGroup>

    ## Update records

    In the above example, each `insert()` statement returns an `id`. You can use this `id` to update the record using `update()`:

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      dataset.update({
        id,
        input: i,
        expected: { result: i + 1, error: "Timeout" },
      });
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      dataset.update(input=i, expected={"result": i + 1, "error": "Timeout"}, id=id)
      ```
    </CodeGroup>

    The `update()` method applies a merge strategy: only the fields you provide will be updated, and all other existing fields in the record will remain unchanged.

    ## Delete records

    You can delete records via code by `id`:

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      await dataset.delete(id);
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      dataset.delete(id)
      ```
    </CodeGroup>

    To delete an entire dataset, use the [API command](/api-reference).

    ## Flush records

    In both TypeScript and Python, the Braintrust SDK flushes records as fast as possible and installs an exit handler that tries
    to flush records, but these hooks are not always respected (e.g. by certain runtimes, or if you `exit` a process yourself). If
    you need to ensure that records are flushed, you can call `flush()` on the dataset.

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      await dataset.flush();
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      dataset.flush()
      ```
    </CodeGroup>

    ## Multimodal datasets

    You may want to store or process images in your datasets. There are currently three ways to use images in Braintrust:

    * Image URLs (most performant)
    * Base64 (least performant)
    * Attachments (easiest to manage, stored in Braintrust)
    * External attachments (access files in your own object stores)

    If you're building a dataset of large images in Braintrust, we recommend using image URLs. This keeps your dataset lightweight and allows you to preview or process them without storing heavy binary data directly.

    If you prefer to keep all data within Braintrust, create a dataset of attachments instead. In addition to images, you can create datasets of attachments that have any arbitrary data type, including audio and PDFs. You can then [use these datasets in evaluations](/core/experiments/write#attachments).

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

      // Create a dataset with attachments.
      createPdfDataset();
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import os
      from typing import Any, Dict

      from braintrust import Attachment, init_dataset


      def create_pdf_dataset() -> None:
          """Create a dataset with attachments."""
          dataset = init_dataset("Project with PDFs", "My PDF Dataset")
          for filename in ["example.pdf"]:
              dataset.insert(
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
          dataset.flush()


      # Create a dataset with attachments.
      create_pdf_dataset()
      ```
    </CodeGroup>

    To invoke this script, run this in your terminal:

    <CodeGroup>
      ```bash Typescript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      npx tsx attachment_dataset.ts
      ```

      ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      python attachment_dataset.py
      ```
    </CodeGroup>
  </Tab>

  <Tab title="UI" icon="mouse-pointer-2">
    ## View a dataset

    You can view a dataset in the Braintrust UI by navigating to the project and then clicking on the dataset.

        <img src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/datasets/datasets.webp?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=c09b283688cf7b4b11e97bb7431974a3" alt="Dataset Viewer" data-og-width="3008" width="3008" data-og-height="670" height="670" data-path="images/guides/datasets/datasets.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/datasets/datasets.webp?w=280&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=48c4e43e3d672e9b1485e920d4eddbbd 280w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/datasets/datasets.webp?w=560&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=ec691abfcdaa57287eac71144f6f3510 560w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/datasets/datasets.webp?w=840&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=6fa914caec8c53163315b190ed3736e3 840w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/datasets/datasets.webp?w=1100&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=cb4ebc5d24e388cb9b53c97df8725123 1100w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/datasets/datasets.webp?w=1650&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=d7046926a7f63130671410846d982ea2 1650w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/datasets/datasets.webp?w=2500&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=3eae3a866e913bc5debf367436390125 2500w" />

    From the UI, you can filter records, create new ones, edit values, and delete records. You can also copy records
    between datasets and from experiments into datasets. This feature is commonly used to collect interesting or
    anomalous examples into a golden dataset.

    ### Create custom columns

    When viewing a dataset, create [custom columns](/core/experiments/interpret#create-custom-columns) to extract values from the root span.

    ## Create a dataset

    The easiest way to create a dataset is to upload a CSV file.

        <img src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/datasets/CSV-Upload.gif?s=1537f7484e98b0bb48dcbdf3f4063966" alt="Upload CSV" data-og-width="1753" width="1753" data-og-height="1152" height="1152" data-path="images/guides/datasets/CSV-Upload.gif" data-optimize="true" data-opv="3" />

    <Note>
      Uploaded records that include an `id` key are automatically deduplicated by their `id` value.
    </Note>

    ## Update records

    Once you've uploaded a dataset, you can update records or add new ones directly in the UI.

        <img src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/datasets/Edit-record.gif?s=ff905fd0f3d7fca2c1abed12537de762" alt="Edit record" data-og-width="1753" width="1753" data-og-height="1152" height="1152" data-path="images/guides/datasets/Edit-record.gif" data-optimize="true" data-opv="3" />

    ## Label records

    In addition to updating datasets through the API, you can edit and label them in the UI. Like experiments and logs, you can
    configure [categorical fields](/core/human-review#writing-to-expected-fields) to allow human reviewers
    to rapidly label records.

    <Note>
      This requires you to first [configure human review](/core/human-review#configuring-human-review) in the **Configuration** tab of your project.
    </Note>

        <img src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=406359641fc9f3de4f70086d56f236dd" alt="Write to expected" data-og-width="1852" width="1852" data-og-height="966" height="966" data-path="images/guides/human-review/expected-fields.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=280&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=74c2817c643f44e6bf10b5c872ad988b 280w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=560&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=2504bd28d1b54f4430d7458fd407be25 560w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=840&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=5691362eca4b4c03f9b2dbf32873bb51 840w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=1100&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=2d93b28ed1d8d7f62d65c15b4786a762 1100w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=1650&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=e2ee18d7f67b4b4f89c08d765a7734bb 1650w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=2500&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=a44f9ea41167ce86f27a572aac1c3f7d 2500w" />

    ## Delete records

    To delete a record, navigate to **Datasets** and select the dataset. Select the check box next to the individual record you'd like to delete, and then select the **Trash** icon.

    <video className="border rounded-md" loop autoPlay muted playsInline poster="/images/guides/datasets/delete-dataset-poster.png">
      <source src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/datasets/delete-dataset-record.mp4?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=92cc4a2e910a128a52d7f41d6fef243a" type="video/mp4" data-path="images/guides/datasets/delete-dataset-record.mp4" />
    </video>

    You can follow the same steps to delete an entire dataset from the **Datasets** page.

    ## Dataset schemas

    Dataset schemas allow you to define JSON schemas for the `input`, `expected`, and `metadata` fields in your dataset. When schemas are defined, you can:

    * **Validate data**: Enable schema enforcement to ensure all records conform to the defined structure
    * **Form-based editing**: Edit records using intuitive forms instead of raw JSON

    ### Define schemas

    To define schemas for your dataset:

    1. Navigate to your dataset
    2. Click the **Field schemas** button in the top toolbar
    3. Select the field you want to define a schema for (`input`, `expected`, or `metadata`)
    4. Use the visual schema builder to define your schema structure

    ### Infer schemas from data

    Instead of manually building a schema, you can automatically infer it from your existing data:

    1. Open the schema editor for a field
    2. Click the **Infer schema** button
    3. The schema will be generated based on the first 100 records in your dataset

    This is particularly useful when you have existing data and want to quickly create a schema that matches your current structure.

    ### Enable schema enforcement

    Once you've defined a schema, you can enable enforcement to validate all records:

    1. In the schema editor, toggle the **Enforce** switch
    2. Click **Save** to apply the schema

    When enforcement is enabled:

    * New records must conform to the schema or validation errors will be shown
    * Existing records that don't match the schema will display validation warnings
    * Form-based editing will automatically validate input as you type

    <Note>
      Enforcement is UI-only and does not affect SDK inserts or updates
    </Note>

    ### Form-based editing

    When a schema is defined for a field, the "Form" display type will be available in the field's data editor. Form-based editing makes it easier to maintain consistent data structures and reduces errors when manually editing records.

    <Note>
      Schemas are stored in the dataset's metadata and are versioned along with your dataset. This ensures that evaluations pinned to specific dataset versions use the correct schema definitions. The Form display type is only available on the dataset page.
    </Note>
  </Tab>
</Tabs>

## Use a dataset in an evaluation

You can use a dataset in an evaluation by passing it directly to the `Eval()` function.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { initDataset, Eval } from "braintrust";
  import { Levenshtein } from "autoevals";

  Eval(
    "Say Hi Bot", // Replace with your project name
    {
      data: initDataset("My App", { dataset: "My Dataset" }),
      task: async (input) => {
        return "Hi " + input; // Replace with your LLM call
      },
      scores: [Levenshtein],
    },
  );
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from autoevals import Levenshtein
  from braintrust import Eval, init_dataset

  Eval(
      "Say Hi Bot",  # Replace with your project name
      data=init_dataset(project="My App", name="My Dataset"),
      task=lambda input: "Hi " + input,  # Replace with your LLM call
      scores=[Levenshtein],
  )
  ```
</CodeGroup>

You can also manually iterate through a dataset's records and run your tasks,
then log the results to an experiment. Log the `id`s to link each dataset record
to the corresponding result.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { initDataset, init, Dataset, Experiment } from "braintrust";

  function myApp(input: any) {
    return `output of input ${input}`;
  }

  function myScore(output: any, rowExpected: any) {
    return Math.random();
  }

  async function main() {
    const dataset = initDataset("My App", { dataset: "My Dataset" });
    const experiment = init("My App", {
      experiment: "My Experiment",
      dataset: dataset,
    });
    for await (const row of dataset) {
      const output = myApp(row.input);
      const closeness = myScore(output, row.expected);
      experiment.log({
        input: row.input,
        output,
        expected: row.expected,
        scores: { closeness },
        datasetRecordId: row.id,
      });
    }

    console.log(await experiment.summarize());
  }

  main();
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import random

  import braintrust


  def my_app(input):
      return f"output of input {input}"


  def my_score(output, row_expected):
      return random.random()


  dataset = braintrust.init_dataset(project="My App", name="My Dataset")
  experiment = braintrust.init(project="My App", experiment="My Experiment", dataset=dataset)
  for row in dataset:
      output = my_app(row["input"])
      closeness = my_score(output, row["expected"])
      experiment.log(
          input=row["input"],
          output=output,
          expected=row["expected"],
          scores=dict(closeness=closeness),
          dataset_record_id=row["id"],
      )

  print(experiment.summarize())
  ```
</CodeGroup>

You can also use the results of an experiment as baseline data for future experiments by calling the `asDataset()`/`as_dataset()` function, which converts the experiment into dataset format (`input`, `expected`, and `metadata`).

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { init, Eval } from "braintrust";
  import { Levenshtein } from "autoevals";

  const experiment = init("My App", {
    experiment: "my-experiment",
    open: true,
  });

  Eval<string, string>("My App", {
    data: experiment.asDataset(),
    task: async (input) => {
      return `hello ${input}`;
    },
    scores: [Levenshtein],
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from autoevals import Levenshtein
  from braintrust import Eval, init

  experiment = braintrust.init(
      project="My App",
      experiment="my-experiment",
      open=True,
  )

  Eval(
      "My App",
      data=experiment.as_dataset(),
      task=lambda input: input + 1,  # Replace with your LLM call
      scores=[Levenshtein],
  )
  ```
</CodeGroup>

For a more advanced overview of how to use an experiment as a baseline for other experiments, see [hill climbing](/core/experiments/write#hill-climbing).

## Log from your application

To log to a dataset from your application, you can use the SDK and call `insert()`. Braintrust logs
are queued and sent asynchronously, so you don't need to worry about critical path performance.

Since the SDK uses API keys, it's recommended that you log from a privileged environment (e.g. backend server),
instead of client applications directly.

This example walks through how to track <Icon icon="thumbs-up" /> / <Icon icon="thumbs-down" /> from feedback:

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
      orgId: string,
      thumbsUp: boolean,
    ) {
      if (this.dataset) {
        this.dataset.insert({
          input,
          expected,
          metadata: { userId, orgId, thumbsUp },
        });
      } else {
        console.warn("Must initialize application before logging");
      }
    }
  }
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from typing import Any

  import braintrust


  class MyApplication:
      def init_app(self):
          self.dataset = braintrust.init_dataset(project="My App", name="logs")

      def log_user_example(self, input: Any, expected: Any, user_id: str, org_id: str, thumbs_up: bool):
          if self.dataset:
              self.dataset.insert(
                  input=input,
                  expected=expected,
                  metadata=dict(user_id=user_id, org_id=org_id, thumbs_up=thumbs_up),
              )
          else:
              print("Must initialize application before logging")
  ```
</CodeGroup>

## Track dataset performance

See which experiments use your dataset and how each row performs. This helps you identify problematic test cases and understand your evaluation data quality.

### View experiment runs

To view all experiment runs that have used a dataset:

1. Go to your dataset page.
2. In the right panel, select **<Icon icon="play" /> Runs**.
3. Review the dataset's performance metrics across experiments.

<img src="https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRuns.png?fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=1707b131eb5221f97b1efa1c5f1e7cc7" alt="Dataset experiment runs" data-og-width="3004" width="3004" data-og-height="1422" height="1422" data-path="core/datasets/datasetRuns.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRuns.png?w=280&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=5083cf7b224a32cd9cbcaded0ac6e3d8 280w, https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRuns.png?w=560&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=9ca03299384e6dd5907b8b9a6943c99b 560w, https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRuns.png?w=840&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=a543f104db72280b106ff1dd446f5a16 840w, https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRuns.png?w=1100&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=2040391f346b2b6598e126add48b53a5 1100w, https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRuns.png?w=1650&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=195cf495ae74a45f3e69672a6339bc48 1650w, https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRuns.png?w=2500&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=0817b0e4848d7e45ed2b92020b3e472f 2500w" />

### Analyze per-row performance

To see how an individual row performs across experiments:

1. In the dataset table, select a row.
2. In the right panel, select **<Icon icon="play" /> Runs**.
3. Review the row's performance metrics across experiments.

<Note>
  This view only shows experiments that set the `origin` field in eval traces.
</Note>

Look for patterns:

* Rows with consistently low scores may have ambiguous expectations
* Rows that fail across multiple experiments might be edge cases
* Rows with high variance suggest model or task instability

<img src="https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRowRuns.png?fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=2ef7ff5bcd7459048d858f378f61eecc" alt="Dataset row performance across experiments" data-og-width="2996" width="2996" data-og-height="1432" height="1432" data-path="core/datasets/datasetRowRuns.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRowRuns.png?w=280&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=20cd94924eaaec842ba71c59205ae216 280w, https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRowRuns.png?w=560&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=3e9f79eeee68dec86addff54328c5dd4 560w, https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRowRuns.png?w=840&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=165728bac2f9bb2a940c4ac1c9b23154 840w, https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRowRuns.png?w=1100&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=6e8e6438c1c6c35708316241c4237553 1100w, https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRowRuns.png?w=1650&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=0d5eb17737c78f8ab7c74cd6889edad6 1650w, https://mintcdn.com/braintrust/vjeEZtFDwoJ5HGGr/core/datasets/datasetRowRuns.png?w=2500&fit=max&auto=format&n=vjeEZtFDwoJ5HGGr&q=85&s=7bbaac0cb7c632cf5fd6cec1cb8cd06c 2500w" />


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt