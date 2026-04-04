# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/galileo-product-features/galileo-+-delta-lake-databricks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Galileo + Delta Lake  Databricks

> Integrate Galileo with Delta Lake on Databricks to manage large-scale data, ensuring seamless collaboration and enhanced NLP workflows.

# Galileo + Delta Lake (Databricks)

This page shows how to export data directly into Delta Lake from the Galileo UI and then reading the same data using Galileo's Python SDK and executing a Galileo Run.

### Setting Up a Databricks Connection

First, go to the Integrations Page and set up your Databricks connection.

Setting up Databricks connection in Galileo

<Frame>
  <img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/data-lake.png?fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=6522df4b9e979b19e0153bbf4ab36315" data-og-width="769" width="769" data-og-height="664" height="664" data-path="images/data-lake.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/data-lake.png?w=280&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=f7b4f012a65223006f6a8da50f719045 280w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/data-lake.png?w=560&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=af9b8db775f5921d7469ac191759bd99 560w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/data-lake.png?w=840&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=789935de78b2e553a295e1ce639de2e7 840w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/data-lake.png?w=1100&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=8690c5932fce755fd53d748b83ced395 1100w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/data-lake.png?w=1650&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=2df17d0c6cec028009d7ba0767889698 1650w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/data-lake.png?w=2500&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=607ba37389a9311b4ca9d9eefe4954c8 2500w" />
</Frame>

### Using Galileo to Read from Delta Lake and Execute a Run

The following code snippet shows how to read labeled data from Delta Lake and execute a Galileo training run.

```py  theme={null}
import os

import pandas as pd
from deltalake import DeltaTable, write_deltalake

# Dataframe with 2 columns: text and label
df_train = pd.DataFrame({"text": newsgroups_train.data, "label": newsgroups_train.target})
df_test = pd.DataFrame({"text": newsgroups_test.data, "label": newsgroups_test.target})

write_deltalake("tmp/delta_lake_path", df_train)
write_deltalake("tmp/delta_lake_path", df_test)

df_train_from_deltalake = DeltaTable("tmp/delta_lake_path").to_pandas()
df_test_from_deltalake = DeltaTable("tmp/delta_lake_path").to_pandas()

dq.auto(
     train_data=df_test_from_deltalake,
     test_data=df_test_from_deltalake,
     labels=newsgroups_train.target_names,
     project_name="my_newsgroups_project",
     run_name="run_1"
)
```

### Exporting Data from Galileo UI into Delta Lake

<Frame>
  <img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/data-lake-2.png?fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=c0f708ff0f1c42fd0c663c5c95b51606" data-og-width="765" width="765" data-og-height="729" height="729" data-path="images/data-lake-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/data-lake-2.png?w=280&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=e0c6d5d106a68a386a44673e4e81a2e0 280w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/data-lake-2.png?w=560&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=63e0486776acb34a73502bcf8f54b609 560w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/data-lake-2.png?w=840&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=0ec32e4e472da5ffe422b404ddbf6946 840w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/data-lake-2.png?w=1100&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=bcb23f6d78f12f71f32fc86bef65e723 1100w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/data-lake-2.png?w=1650&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=06dae2e7b3dcdc79cf76d3d6527773e3 1650w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/data-lake-2.png?w=2500&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=d942acfda96eefb4b7fbc873e27f4eb2 2500w" />
</Frame>
