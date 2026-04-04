# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/using-datasets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

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

<img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/new-dataset.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=bc820517d5a8cd6f74266c0096e2d8d5" data-og-width="1652" width="1652" data-og-height="1081" height="1081" data-path="images/new-dataset.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/new-dataset.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=b565d599e2e566f986f3cc96fb5759e8 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/new-dataset.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=212964ec6f41a634056d98a91ded2e07 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/new-dataset.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=0d4e5f491763885aa65fe2c532a93a1d 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/new-dataset.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=c9203b4c2a60f7e01d17d63e79a8e0d1 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/new-dataset.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=6e311e72787ea0c1467977ce4bf99621 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/new-dataset.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=1fd98cd07d17129c07bac40e667e24fb 2500w" />

You can upload a CSV, JSON, JSONL, or Feather file, or enter data directly into the table.

### Using a dataset in an evaluation run

When creating a new evaluation run, you can select a dataset to use as input.

<Frame>
  <img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/select-dataset.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=9466be8eff02684b7cdbdef6590d27fb" data-og-width="245" width="245" data-og-height="425" height="425" data-path="images/select-dataset.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/select-dataset.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=911b30ca1ed688a0df4e7cea5589a0b5 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/select-dataset.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=14e2ba6c206765587e08ab4b53a538ea 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/select-dataset.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=d1e489e4e1882eed4909c72e7c23b77a 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/select-dataset.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=6216a670786aca3f4ff8f145a6912c94 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/select-dataset.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=0f560be14bfca44a61522e299c45a39a 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/select-dataset.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=d61f915715f46eba797660ec753fd3c1 2500w" />
</Frame>

## Using Datasets in code

### Prerequisites

For Python, install the [`promptquality`](/client-reference/evaluate/python) library.

For TypeScript, install the [`@rungalileo/galileo`](/client-reference/evaluate/typescript) package.

### Create a dataset

You can create a new dataset by running:

<CodeGroup>
  ```python Python theme={null}
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

  ```typescript TypeScript theme={null}
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
     ```python Python theme={null}
     dataset = pq.create_dataset(
         [
             {"input": {"virtue": "benevolence", "voice": "Oprah Winfrey"}},
             {"input": {"virtue": "trustworthiness", "voice": "Barack Obama"}},
         ]
     )
     ```

     ```typescript TypeScript theme={null}
     const dataset = await createDataset([{ input: { virtue: "benevolence", voice: "Oprah Winfrey" } }, { input: { virtue: "trustworthiness", voice: "Barack Obama" } }], "My data");
     ```
   </CodeGroup>

3. A path to a file in either CSV, Feather, or JSONL format, e.g.

   <CodeGroup>
     ```python Python theme={null}
     dataset = pq.create_dataset("path/to/dataset.csv")
     ```

     ```typescript TypeScript theme={null}
     const dataset = await uploadDataset("path/to/dataset.csv", "My data");
     ```
   </CodeGroup>

### Using a dataset in an evaluation run

To use the dataset in an evaluation run, provide the dataset ID to the run function (Python only).

<CodeGroup>
  ```python Python theme={null}
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
  ```python Python theme={null}
  rows = pq.get_dataset_content(dataset.id)
  for row in rows:
      print(row)
  ```

  ```typescript TypeScript theme={null}
  const rows = await getDatasetRows(dataset.id);
  rows.forEach((row) => console.log(row));
  ```
</CodeGroup>
