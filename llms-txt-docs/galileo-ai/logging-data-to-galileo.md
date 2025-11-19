# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/text-classification/logging-data-to-galileo.md

# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/natural-language-inference/logging-data-to-galileo.md

# Logging Data | Natural Language Inference in Galileo

> The fastest way to find data errors in Galileo.

When focusing on data-centric techniques for modeling, we believe it is important to focus on the data while keeping the model static. To enable this rapid workflow, we suggest you use the `dq.auto` workflow:

After installing dataquality: `pip install dataquality`

You simply add your data and wait for the model to train under the hood, and for Galileo to process the data. This processing can take between 5-15 minutes, depending on how much data you have.

`auto` will wait until Galileo is completely done processing your data. At that point, you can go to the Galileo Console and begin inspecting.

```
import dataquality as dq

dq.auto(train_data=train_df, val_data=val_df, test_data=test_df)
```

There are 3 general ways to use `auto`

* Pass dataframes to `train_data`, `val_data` and `test_data` (pandas or huggingface)

* Pass paths to local files to `train_data`, `val_data` and `test_data`

* Pass a path to a huggingface Dataset to the `hf_data` parameter

`dq.auto` supports both Text Classification and Named Entity Recognition tasks, with Multi-Label support coming soon. `dq.auto` automatically determines the task type based off of the provided data schema.

To see the other available parameters as well as more usage examples, see `help(dq.auto)`

To learn more about how `dq.auto` works, and why we suggest this paradigm, see DQ Auto

#### Looking to inspect your own model?

Use `auto` if:

* You are looking to apply the most data-centric techniques to improve your data

* You don’t yet have a model to train

* You want to agnostically understand and fix your available training data

If you have a well-trained model and want to understand its performance on your data, or you are looking to deploy an existing model and monitor it with Galileo, please use our custom framework integrations.

## Galileo Auto

Welcome to `auto`, your newest superpower in the world of Machine Learning!

We know now that **more** data isn’t the answer, **better** data is. But how do you find that data? We already know the answer to that: <Icon icon="sparkles" />Galileo<Icon icon="sparkles" />

But how do you get started now, and iterate quickly with ***data-centric*** techniques?

Enter: `dq.auto` the secret sauce to instant data insights. We handle the training, you focus on the data.

### What is DQ auto?

`dq.auto` is a helper function to train the most cutting-edge transformer (or any of your choosing from HuggingFace) on your dataset so it can be processed by Galileo. You provide the data, let Galileo train the model, and you’re off to the races.

The goal of this tool, and Galileo at large, is to build a data-centric view of machine learning. Keep your model static and iterate on the dataset until it’s well-formed and well-representative of your problem space. This is the path to robust and stable ML models.

### What DQ auto *isn't?*

`auto` is ***not*** an AutoML tool. It will not perform hyperparameter tuning, and will not search through a gallery of models to optimize every percentage of f1.

In fact, `auto` is quite the opposite. It intentionally keeps the model static, forcing you to understand and fix your data to improve performance.

### Why?

It turns out that in many (most) cases, **you don’t need to train your own model to find data insights**. In fact, you often don’t need to build your own custom model at all! [HuggingFace](https://huggingface.co/), and in particular [transformers](https://huggingface.co/docs/transformers/index), has brought the most cutting-edge deep learning algorithms straight to your fingertips, allowing you to leverage the best research has to offer in 1 line of code.

Transformer models have consistently outperformed their predecessors, and HuggingFace is constantly updating their fleet of *free* models for anyone to download.

<Check>So if you don’t *need* to build a custom model anymore, why not let Galileo do it for you?</Check>

### Get Started

Simply install: `pip install --upgrade dataquality`

and use!

```py

import dataquality as dq

# Get insights on the official 'emotion' dataset
dq.auto(hf_data="emotion")
```

You can also provide data as files or pandas dataframes

```py

import pandas as pd
from sklearn.datasets import fetch_20newsgroups
import dataquality as dq

# Load the newsgroups dataset from sklearn
newsgroups_train = fetch_20newsgroups(subset='train')
newsgroups_test = fetch_20newsgroups(subset='test')
# Convert to pandas dataframes
df_train = pd.DataFrame({"text": newsgroups_train.data, "label": newsgroups_train.target})
df_test = pd.DataFrame({"text": newsgroups_test.data, "label": newsgroups_test.target})

dq.auto(
     train_data=df_train,
     test_data=df_test,
     labels=newsgroups_train.target_names,
     project_name="newsgroups_work",
     run_name="run_1_raw_data"
)
```

`dq.auto` works for:

* Text Classification datasets (given columns `text` and `label`). [Trec6 Example.](https://huggingface.co/datasets/rungalileo/trec6)

* NER datasets (give columns `tokens` and `tags` or `ner_tags`). [MIT\_movies Example.](https://huggingface.co/datasets/rungalileo/mit_movies)

`auto` will automatically figure out your task and start the process for you.

For more docs and examples, see `help(dq.auto)` in your notebook! Happy data fixing <Icon icon="rocket" />
