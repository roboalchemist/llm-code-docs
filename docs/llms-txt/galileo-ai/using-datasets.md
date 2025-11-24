# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/using-datasets.md

# Using Datasets

> How to use datasets in Galileo

Datasets serve as inputs to an Evaluate run.
Datasets have 3 standard columns: `input`, `output`, and `metadata`.
The `input` column is what you can reference inside a prompt template to craft your prompt.
The `output` column can be used to store reference outputs or ground truth outputs.
The `metadata` column can be used to store any properties useful to group and filter the rows in the dataset.

## Using Datasets in the Galileo Console

### Create a dataset

From the Datasets page, click the "Create Dataset" button.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/new-dataset.png" />

You can upload a CSV, JSON, JSONL, or Feather file, or enter data directly into the table.

### Using a dataset in an evaluation run

When creating a new evaluation run, you can select a dataset to use as input.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/select-dataset.png" />
</Frame>

## Using Datasets in code

### Prerequisites

For Python, install the [`promptquality`](/client-reference/evaluate/python) library.

For TypeScript, install the [`@rungalileo/galileo`](/client-reference/evaluate/typescript) package.

### Create a dataset

You can create a new dataset by running:

<CodeGroup>
  ```python Python
  import os
  import promptquality as pq

  pq.login(os.environ["GALILEO_CONSOLE_URL"])

  dataset = pq.create_dataset(
      {
          "input": [
              {"virtue": "benevolence", "voice": "Oprah Winfrey"},
              {"virtue": "trustworthiness", "voice": "Barack Obama"},
          ]
      }
  )
  ```

  ```typescript TypeScript
  import { getDatasets, uploadDataset, getDatasetRows } from "@rungalileo/galileo";

  const dataset = await createDataset(
    {
      input: [
        { virtue: "benevolence", voice: "Oprah Winfrey" },
        { virtue: "trustworthiness", voice: "Barack Obama" },
      ],
    },
    "My data",
  );
  ```
</CodeGroup>

These functions accept a few different formats for the dataset.

1. A dictionary mapping column names to lists of values (as shown above).

2. A list of dictionaries, where each dictionary represents a row in the dataset, e.g.

   <CodeGroup>
     ```python Python
     dataset = pq.create_dataset(
         [
             {"input": {"virtue": "benevolence", "voice": "Oprah Winfrey"}},
             {"input": {"virtue": "trustworthiness", "voice": "Barack Obama"}},
         ]
     )
     ```

     ```typescript TypeScript
     const dataset = await createDataset([{ input: { virtue: "benevolence", voice: "Oprah Winfrey" } }, { input: { virtue: "trustworthiness", voice: "Barack Obama" } }], "My data");
     ```
   </CodeGroup>

3. A path to a file in either CSV, Feather, or JSONL format, e.g.

   <CodeGroup>
     ```python Python
     dataset = pq.create_dataset("path/to/dataset.csv")
     ```

     ```typescript TypeScript
     const dataset = await uploadDataset("path/to/dataset.csv", "My data");
     ```
   </CodeGroup>

### Using a dataset in an evaluation run

To use the dataset in an evaluation run, provide the dataset ID to the run function (Python only).

<CodeGroup>
  ```python Python
  template = "Explain {virtue} to me in the voice of {voice}"

  pq.run(
      project_name="test_dataset_project",
      template=template,
      dataset=dataset.id,
      settings=pq.Settings(
          model_alias="ChatGPT (16K context)", temperature=0.8, max_tokens=400
      ),
  )
  ```
</CodeGroup>

Note that the TypeScript client does not currently support creating runs.
However, you can use the dataset for [logging workflows](/client-reference/evaluate/typescript#log-workflows).

### Getting the contents of a dataset

You can list the dataset's contents like so:

<CodeGroup>
  ```python Python
  rows = pq.get_dataset_content(dataset.id)
  for row in rows:
      print(row)
  ```

  ```typescript TypeScript
  const rows = await getDatasetRows(dataset.id);
  rows.forEach((row) => console.log(row));
  ```
</CodeGroup>
