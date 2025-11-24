# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/galileo-product-features/galileo-+-delta-lake-databricks.md

# Galileo + Delta Lake  Databricks

> Integrate Galileo with Delta Lake on Databricks to manage large-scale data, ensuring seamless collaboration and enhanced NLP workflows.

# Galileo + Delta Lake (Databricks)

This page shows how to export data directly into Delta Lake from the Galileo UI and then reading the same data using Galileo's Python SDK and executing a Galileo Run.

### Setting Up a Databricks Connection

First, go to the Integrations Page and set up your Databricks connection.

Setting up Databricks connection in Galileo

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/data-lake.png" />
</Frame>

### Using Galileo to Read from Delta Lake and Execute a Run

The following code snippet shows how to read labeled data from Delta Lake and execute a Galileo training run.

```py
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
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/data-lake-2.png" />
</Frame>
