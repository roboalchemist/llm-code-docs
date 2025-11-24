# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-llm-fine-tune/quickstart/dq.auto.md

# Configuring Dq Auto

> Automatic Data Insights on your Seq2Seq dataset

### auto

While using auto with default settings is as simple as running `dq.auto()`, you can also set granular control over dataset settings, training parameters, and generation configuration. The `auto` function takes in optional parameters for `dataset_config`, `training_config`, and `generation_config`. If a configuration parameter is omitted, default values from below will be used.

#### Example

```py
from dataquality.integrations.seq2seq.auto import auto
from dataquality.integrations.seq2seq.schema import (
    Seq2SeqDatasetConfig,
    Seq2SeqGenerationConfig,
    Seq2SeqTrainingConfig
)

# Config parameters can be found below
dataset_config = Seq2SeqDatasetConfig(...)
training_config = Seq2SeqTrainingConfig(...)
generation_config = Seq2SeqGenerationConfig(...)

auto(
    project_name="s2s_auto",
    run_name="my_run",
    dataset_config=dataset_config,
    training_config=training_config
    generation_config=generation_config
)
```

## Parameters

* **Parameters**

  * **project\_name** (`Union`\[`str`, `None`]) -- Optional project name. If not set, a default name will be used. Default "s2s\_auto"

  * **run\_name** (`Union`\[`str`, `None`]) -- Optional run name. If not set, a random name will be generated

  * **train\_path** (`Union`\[`str`, `None`]) -- Optional training data to use. Must be a path to a local file of type `.csv`, `.json`, or `.jsonl`.

  * **dataset\_config** (`Union`\[`Seq2SeqDatasetConfig`, `None`]) -- Optional config for loading the dataset. See `Seq2SeqDatasetConfig` for more details

  * **training\_config** (`Union`\[`Seq2SeqTrainingConfig`, `None`]) -- Optional config for training the model. See `Seq2SeqTrainingConfig` for more details

  * **generation\_config** (`Union`\[`Seq2SeqGenerationConfig`, `None`]) -- Optional config for post training model generation. See `Seq2SeqGenerationConfig` for more details

  * **wait** (`bool`) -- Whether to wait for Galileo to complete processing your run. Default True

### Dataset Config

Use the `Seq2SeqGenerationConfig()` class to set the dataset for auto training.

Given either a pandas dataframe, local file path, or huggingface dataset path, this function will load the data, train a huggingface transformer model, and provide Galileo insights via a link to the Galileo Console.

One of `hf_data`, `train_path`, or `train_data` should be provided.

```py
from dataquality.integrations.seq2seq.schema import Seq2SeqDatasetConfig

dataset_config = Seq2SeqDatasetConfig(
    train_path="/Home/Datasets/train.csv",
    val_path="/Home/Datasets/val.csv",
    test_path="/Home/Datasets/test.csv",
    input_col="text",
    target_col="label",
)
```

### Parameters

* **Parameters**

  * **hf\_data** (`Union`\[`DatasetDict`, `str`, `None`]) -- Use this param if you have huggingface data in the hub or in memory. Otherwise see train\_path or train\_data, val\_path or val\_data, and test\_path or test\_data. If provided, other dataset parameters are ignored.

  * **train\_path** (`Union`\[`str`, `None`]) -- Optional training data to use. Must be a path to a local file of type `.csv`, `.json`, or `.jsonl`.

  * **val\_path** (`Union`\[`str`, `None`]) -- Optional validation data to use. Must be a path to a local file of type `.csv`, `.json`, or `.jsonl`. If not provided, but test\_path is, that will be used as the evaluation set. If neither val nor test are available, the train data will be randomly split 80/20 for use as evaluation data.

  * **test\_path** (`Union`\[`str`, `None`]) -- Optional test data to use. Must be a path to a local file of type `.csv`, `.json`, or `.jsonl`. The test data, if provided with val, will be used after training is complete, as the hold-out set. If no validation data is provided, this will instead be used as the evaluation set.

  * **train\_data** (`Union`\[`DataFrame`, `Dataset`, `None`]) -- Optional training data to use. Can be one of \* Pandas dataframe \* Huggingface dataset \* Huggingface dataset hub path

  * **val\_data** (`Union`\[`DataFrame`, `Dataset`, `None`]) -- Optional validation data to use. The validation data is what is used for the evaluation dataset in huggingface, and what is used for early stopping. If not provided, but test\_data is, that will be used as the evaluation set. If neither val nor test are available, the train data will be randomly split 80/20 for use as evaluation data. Can be one of \* Pandas dataframe \* Huggingface dataset \* Huggingface dataset hub path

  * **test\_data** (`Union`\[`DataFrame`, `Dataset`, `None`]) -- Optional test data to use. The test data, if provided with val, will be used after training is complete, as the hold-out set. If no validation data is provided, this will instead be used as the evaluation set. Can be one of \* Pandas dataframe \* Huggingface dataset \* Huggingface dataset hub path

  * **input\_col** (`str`) -- Column name of the model input in the provided dataset. Default `text`

  * **target\_col** (`str`) -- Column name of the model target output in the provided dataset. Default `label`

## Training Config

Use the `Seq2SeqTrainingConfig()` class to set the training parameters for auto training.

```
from dataquality.integrations.seq2seq.schema import Seq2SeqTrainingConfig

training_config = Seq2SeqTrainingConfig(
    epochs=3
    learning_rate=3e-4,
    batch_size=4,
)
```

### Parameters

* **Parameters**

  * **model** (`int`) -- The pretrained AutoModel from huggingface that will be used to tokenize and train on the provided data. Default `google/flan-t5-base`

  * **epochs** (`int`) -- The number of epochs to train. Defaults to 3. If set to 0, training/fine-tuning will be skipped and auto will only do a forward pass with the data to gather all the necessary info to display it in the console.

  * **learning\_rate** (`float`) -- Optional learning rate. Defaults to 3e-4

  * **batch\_size** (`int`) -- Optional batch size. Default 4

  * **accumulation\_steps** (`int`) -- Optional accumulation steps. Default 4

  * **max\_input\_tokens** (`int`) -- Optional the maximum length in number of tokens for the inputs to the transformer model. If not set, will use tokenizer default or default 512 if tokenizer has no default

  * **max\_target\_tokens** (`int`) -- Optional the maximum length in number of tokens for the target outputs to the transformer model. If not set, will use tokenizer default or default 128 if tokenizer has no default

  * **create\_data\_embs** (`Optional`\[`bool`]) -- Whether to create data embeddings for this run. If True, Sentence-Transformers will be used to generate data embeddings for this dataset and uploaded with this run. You can access these embeddings via dq.metrics.get\_data\_embeddings in the emb column or dq.metrics.get\_dataframe(..., include\_data\_embs=True) in the data\_emb col. Default True if a GPU is available, else default False.

### Generation Config

Use the `Seq2SeqGenerationConfig()` class to set the training parameters for auto training.

```
from dataquality.integrations.seq2seq.schema import Seq2SeqGenerationConfig

generation_config = Seq2SeqGenerationConfig(
    max_new_tokens=16,
    temperature=0.2,
)
```

### Parameters

* **Parameters**

  * **max\_new\_tokens** (`int`) -- The maximum numbers of tokens to generate, ignoring the number of tokens in the prompt. Default 16

  * **temperature** (`float`) -- The value used to modulate the next token probabilities. Default 0.2

  * **do\_sample** (`float`) -- Whether or not to use sampling ; use greedy decoding otherwise. Default False

  * **top\_p** (`float`) -- If set to float \< 1, only the smallest set of most probable tokens with probabilities that add up to `top_p` or higher are kept for generation. Default 1.0

  * **top\_k** (`int`) -- The number of highest probability vocabulary tokens to keep for top-k-filtering. Default 50

  * **generation\_splits** (`Union[List[str], None]`) -- Optional list of splits to perform generation on after training the model. These generated outputs will show up in the console for specified splits. Default \["test"]

### Examples

An example using `auto` with a hosted huggingface summarization dataset

```
import dataquality.integrations.seq2seq.auto as auto

dq.auto(hf_data="tatsu-lab/alpaca")
```

An example of using `auto` with a local jsonl file

```
import dataquality.integrations.seq2seq.auto as auto

from dataquality.integrations.seq2seq.schema import Seq2SeqDatasetConfig

dataset_config = Seq2SeqDatasetConfig(
    train_path="./train.jsonl",
    val_path="./val.jsonl",
    test_path="./test.jsonl",
    input_col="text",
    target_col="label",
)

dq.auto(
    project_name="data_from_local",
    run_name="run_1_raw_data",
    dataset_config=dataset_config,
)
```

Where `train.jsonl` might be a file with `prompt` and `completion` columns that looks like:

```
{"prompt": "Write a short story about a curious cat.", "completion": "Once upon a time, in a small town, there lived a curious cat named Whiskers. Whiskers was known for exploring every nook and cranny, always on the lookout for adventure."}
{"prompt": "Describe your favorite vacation destination.", "completion": "My favorite vacation destination is a remote tropical island. The crystal-clear waters, white sandy beaches, and lush green forests make it a paradise on Earth."}
{"prompt": "List your top 5 favorite books.", "completion": "1. 'To Kill a Mockingbird' by Harper Lee\n2. 'The Great Gatsby' by F. Scott Fitzgerald\n3. 'Harry Potter and the Sorcerer's Stone' by J.K. Rowling\n4. 'Pride and Prejudice' by Jane Austen\n5. 'The Catcher in the Rye' by J.D. Salinger"}
{"prompt": "Explain the concept of time travel.", "completion": "Time travel is a theoretical concept that involves moving between different points in time. While it remains a popular subject in science fiction, it has not been achieved in reality."}
{"prompt": "Share your favorite recipe.", "completion": "One of my favorite recipes is for homemade lasagna. It's a comforting dish made with layers of pasta, ricotta cheese, marinara sauce, ground beef, and melted mozzarella. It's a family favorite!"}
```

### Get started with a notebook <Icon icon="book" />

* [Auto Notebook](https://colab.research.google.com/github/rungalileo/examples/blob/main/examples/sequence_to_sequence/LLM_Fine_Tuning_chat_data_with_DQ_auto_using_%F0%9F%94%AD_Galileo.ipynb)

* [Auto Notebook for Chat Data](https://colab.research.google.com/github/rungalileo/examples/blob/main/examples/sequence_to_sequence/LLM_Fine_Tuning_chat_data_with_DQ_auto_using_%F0%9F%94%AD_Galileo.ipynb)
