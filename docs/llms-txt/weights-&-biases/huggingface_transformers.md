# Source: https://docs.wandb.ai/models/integrations/huggingface_transformers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Hugging Face Transformers

> Use W&B with Hugging Face Transformers Trainer for experiment tracking, model checkpointing, and dataset versioning.

export const ColabLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="colab-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05zm-6.3 1.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09 3.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01.21.03zm-6.47 14.25l-.23.33-.08.41.08.41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08z" />
    </svg>
    Try in Colab
  </a>;

<ColabLink url="https://colab.research.google.com/github/wandb/examples/blob/master/colabs/huggingface/Optimize_Hugging_Face_models_with_Weights_&_Biases.ipynb" />

The [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) library makes state-of-the-art NLP models like BERT and training techniques like mixed precision and gradient checkpointing easy to use. The [W\&B integration](https://huggingface.co/transformers/main_classes/callback.html#transformers.integrations.WandbCallback) adds rich, flexible experiment tracking and model versioning to interactive centralized dashboards without compromising that ease of use.

## Next-level logging in few lines

```python  theme={null}
os.environ["WANDB_PROJECT"] = "<my-amazing-project>"  # name your W&B project
os.environ["WANDB_LOG_MODEL"] = "checkpoint"  # log all model checkpoints

from transformers import TrainingArguments, Trainer

args = TrainingArguments(..., report_to="wandb")  # turn on W&B logging
trainer = Trainer(..., args=args)
```

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/mVjDwbx0mC8gYx-b/images/integrations/huggingface_gif.gif?s=a04b851a6423d962aadb3cc690690e0d" alt="HuggingFace dashboard" width="600" height="320" data-path="images/integrations/huggingface_gif.gif" />
</Frame>

<Note>
  If you'd rather dive straight into working code, check out this [Google Colab](https://wandb.me/hf).
</Note>

## Get started: track experiments

### Sign up and create an API key

An API key authenticates your machine to W\&B. You can generate an API key from your user profile.

<Note>
  For a more streamlined approach, create an API key by going directly to [User Settings](https://wandb.ai/settings). Copy the newly created API key immediately and save it in a secure location such as a password manager.
</Note>

1. Click your user profile icon in the upper right corner.
2. Select **User Settings**, then scroll to the **API Keys** section.

### Install the `wandb` library and log in

To install the `wandb` library locally and log in:

<Tabs>
  <Tab title="Command Line">
    1. Set the `WANDB_API_KEY` [environment variable](/models/track/environment-variables/) to your API key.

       ```bash  theme={null}
       export WANDB_API_KEY=<your_api_key>
       ```

    2. Install the `wandb` library and log in.

       ```shell  theme={null}
       pip install wandb

       wandb login
       ```
  </Tab>

  <Tab title="Python">
    ```bash  theme={null}
    pip install wandb
    ```

    ```python  theme={null}
    import wandb
    wandb.login()
    ```
  </Tab>

  <Tab title="Python notebook">
    ```notebook  theme={null}
    !pip install wandb

    import wandb
    wandb.login()
    ```
  </Tab>
</Tabs>

If you are using W\&B for the first time you might want to check out our [quickstart](/models/quickstart/)

### Name the project

A W\&B Project is where all of the charts, data, and models logged from related runs are stored. Naming your project helps you organize your work and keep all the information about a single project in one place.

To add a run to a project simply set the `WANDB_PROJECT` environment variable to the name of your project. The `WandbCallback` will pick up this project name environment variable and use it when setting up your run.

<Tabs>
  <Tab title="Command Line">
    ```bash  theme={null}
    WANDB_PROJECT=amazon_sentiment_analysis
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    import os
    os.environ["WANDB_PROJECT"]="amazon_sentiment_analysis"
    ```
  </Tab>

  <Tab title="Python notebook">
    ```notebook  theme={null}
    %env WANDB_PROJECT=amazon_sentiment_analysis
    ```
  </Tab>
</Tabs>

<Note>
  Make sure you set the project name *before* you initialize the `Trainer`.
</Note>

If a project name is not specified the project name defaults to `huggingface`.

### Log your training runs to W\&B

This is **the most important step** when defining your `Trainer` training arguments, either inside your code or from the command line, is to set `report_to` to `"wandb"` in order enable logging with W\&B.

The `logging_steps` argument in `TrainingArguments` will control how often training metrics are pushed to W\&B during training. You can also give a name to the training run in W\&B using the `run_name` argument.

That's it. Now your models will log losses, evaluation metrics, model topology, and gradients to W\&B while they train.

<Tabs>
  <Tab title="Command Line">
    ```bash  theme={null}
    python run_glue.py \     # run your Python script
      --report_to wandb \    # enable logging to W&B
      --run_name bert-base-high-lr \   # name of the W&B run (optional)
      # other command line arguments here
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    from transformers import TrainingArguments, Trainer

    args = TrainingArguments(
        # other args and kwargs here
        report_to="wandb",  # enable logging to W&B
        run_name="bert-base-high-lr",  # name of the W&B run (optional)
        logging_steps=1,  # how often to log to W&B
    )

    trainer = Trainer(
        # other args and kwargs here
        args=args,  # your training args
    )

    trainer.train()  # start training and logging to W&B
    ```
  </Tab>
</Tabs>

<Note>
  Using TensorFlow? Just swap the PyTorch `Trainer` for the TensorFlow `TFTrainer`.
</Note>

### Turn on model checkpointing

Using [Artifacts](/models/artifacts/), you can store up to 100GB of models and datasets for free and then use the W\&B [Registry](/models/registry/). Using Registry, you can register models to explore and evaluate them, prepare them for staging, or deploy them in your production environment.

To log your Hugging Face model checkpoints to Artifacts, set the `WANDB_LOG_MODEL` environment variable to *one* of:

* **`checkpoint`**: Upload a checkpoint every `args.save_steps` from the [`TrainingArguments`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments).
* **`end`**: Upload the model at the end of training, if `load_best_model_at_end` is also set.
* **`false`**: Do not upload the model.

<Tabs>
  <Tab title="Command Line">
    ```bash  theme={null}
    WANDB_LOG_MODEL="checkpoint"
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    import os

    os.environ["WANDB_LOG_MODEL"] = "checkpoint"
    ```
  </Tab>

  <Tab title="Python notebook">
    ```notebook  theme={null}
    %env WANDB_LOG_MODEL="checkpoint"
    ```
  </Tab>
</Tabs>

Any Transformers `Trainer` you initialize from now on will upload models to your W\&B project. The model checkpoints you log will be viewable through the [Artifacts](/models/artifacts/) UI, and include the full model lineage (see an example model checkpoint in the UI [here](https://wandb.ai/wandb/arttest/artifacts/model/iv3_trained/5334ab69740f9dda4fed/lineage?_gl=1*yyql5q*_ga*MTQxOTYyNzExOS4xNjg0NDYyNzk1*_ga_JH1SJHJQXJ*MTY5MjMwNzI2Mi4yNjkuMS4xNjkyMzA5NjM2LjM3LjAuMA..)).

<Note>
  By default, your model will be saved to W\&B Artifacts as `model-{run_id}` when `WANDB_LOG_MODEL` is set to `end` or `checkpoint-{run_id}` when `WANDB_LOG_MODEL` is set to `checkpoint`.
  However, If you pass a [`run_name`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.run_name) in your `TrainingArguments`, the model will be saved as `model-{run_name}` or `checkpoint-{run_name}`.
</Note>

#### W\&B Registry

Once you have logged your checkpoints to Artifacts, you can then register your best model checkpoints and centralize them across your team with [Registry](/models/registry/). Using Registry, you can organize your best models by task, manage the lifecycles of models, track and audit the entire ML lifecyle, and [automate](/models/automations/) downstream actions.

To link a model Artifact, refer to [Registry](/models/registry/).

### Visualise evaluation outputs during training

Visualing your model outputs during training or evaluation is often essential to really understand how your model is training.

By using the callbacks system in the Transformers Trainer, you can log additional helpful data to W\&B such as your models' text generation outputs or other predictions to W\&B Tables.

See the [Custom logging section](#custom-logging-log-and-view-evaluation-samples-during-training) below for a full guide on how to log evaluation outputs while training to log to a W\&B Table like this:

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/mVjDwbx0mC8gYx-b/images/integrations/huggingface_eval_tables.png?fit=max&auto=format&n=mVjDwbx0mC8gYx-b&q=85&s=2d0a1df193ab80cde6aa914b56c8b279" alt="Shows a W&B Table with evaluation outputs" width="2002" height="1214" data-path="images/integrations/huggingface_eval_tables.png" />
</Frame>

### Finish your W\&B Run (Notebook only)

If your training is encapsulated in a Python script, the W\&B run will end when your script finishes.

If you are using a Jupyter or Google Colab notebook, you'll need to tell us when you're done with training by calling `run.finish()`.

```python  theme={null}
run = wandb.init()
trainer.train()  # start training and logging to W&B

# post-training analysis, testing, other logged code

run.finish()
```

### Visualize your results

Once you have logged your training results you can explore your results dynamically in the [W\&B Dashboard](/models/track/workspaces/). It's easy to compare across dozens of runs at once, zoom in on interesting findings, and coax insights out of complex data with flexible, interactive visualizations.

## Advanced features and FAQs

### How do I save the best model?

If you pass `TrainingArguments` with `load_best_model_at_end=True` to your `Trainer`, W\&B saves the best performing model checkpoint to Artifacts.

If you save your model checkpoints as Artifacts, you can promote them to the [Registry](/models/registry/). In Registry, you can:

* Organize your best model versions by ML task.
* Centralize models and share them with your team.
* Stage models for production or bookmark them for further evaluation.
* Trigger downstream CI/CD processes.

### How do I load a saved model?

If you saved your model to W\&B Artifacts with `WANDB_LOG_MODEL`, you can download your model weights for additional training or to run inference. You just load them back into the same Hugging Face architecture that you used before.

```python  theme={null}
# Create a new run
with wandb.init(project="amazon_sentiment_analysis") as run:
    # Pass the name and version of Artifact
    my_model_name = "model-bert-base-high-lr:latest"
    my_model_artifact = run.use_artifact(my_model_name)

    # Download model weights to a folder and return the path
    model_dir = my_model_artifact.download()

    # Load your Hugging Face model from that folder
    #  using the same model class
    model = AutoModelForSequenceClassification.from_pretrained(
        model_dir, num_labels=num_labels
    )

    # Do additional training, or run inference
```

### How do I resume training from a checkpoint?

If you had set `WANDB_LOG_MODEL='checkpoint'` you can also resume training by you can using the `model_dir` as the `model_name_or_path` argument in your `TrainingArguments` and pass `resume_from_checkpoint=True` to `Trainer`.

```python  theme={null}
last_run_id = "xxxxxxxx"  # fetch the run_id from your wandb workspace

# resume the wandb run from the run_id
with wandb.init(
    project=os.environ["WANDB_PROJECT"],
    id=last_run_id,
    resume="must",
) as run:
    # Connect an Artifact to the run
    my_checkpoint_name = f"checkpoint-{last_run_id}:latest"
    my_checkpoint_artifact = run.use_artifact(my_model_name)

    # Download checkpoint to a folder and return the path
    checkpoint_dir = my_checkpoint_artifact.download()

    # reinitialize your model and trainer
    model = AutoModelForSequenceClassification.from_pretrained(
        "<model_name>", num_labels=num_labels
    )
    # your awesome training arguments here.
    training_args = TrainingArguments()

    trainer = Trainer(model=model, args=training_args)

    # make sure use the checkpoint dir to resume training from the checkpoint
    trainer.train(resume_from_checkpoint=checkpoint_dir)
```

### How do I log and view evaluation samples during training

Logging to W\&B via the Transformers `Trainer` is taken care of by the [`WandbCallback`](https://huggingface.co/transformers/main_classes/callback.html#transformers.integrations.WandbCallback) in the Transformers library. If you need to customize your Hugging Face logging you can modify this callback by subclassing `WandbCallback` and adding additional functionality that leverages additional methods from the Trainer class.

Below is the general pattern to add this new callback to the HF Trainer, and further down is a code-complete example to log evaluation outputs to a W\&B Table:

```python  theme={null}
# Instantiate the Trainer as normal
trainer = Trainer()

# Instantiate the new logging callback, passing it the Trainer object
evals_callback = WandbEvalsCallback(trainer, tokenizer, ...)

# Add the callback to the Trainer
trainer.add_callback(evals_callback)

# Begin Trainer training as normal
trainer.train()
```

#### View evaluation samples during training

The following section shows how to customize the `WandbCallback` to run model predictions and log evaluation samples to a W\&B Table during training. We will every `eval_steps` using the `on_evaluate` method of the Trainer callback.

Here, we wrote a `decode_predictions` function to decode the predictions and labels from the model output using the tokenizer.

Then, we create a pandas DataFrame from the predictions and labels and add an `epoch` column to the DataFrame.

Finally, we create a `wandb.Table` from the DataFrame and log it to wandb.
Additionally, we can control the frequency of logging by logging the predictions every `freq` epochs.

**Note**: Unlike the regular `WandbCallback` this custom callback needs to be added to the trainer **after** the `Trainer` is instantiated and not during initialization of the `Trainer`.
This is because the `Trainer` instance is passed to the callback during initialization.

```python  theme={null}
from transformers.integrations import WandbCallback
import pandas as pd


def decode_predictions(tokenizer, predictions):
    labels = tokenizer.batch_decode(predictions.label_ids)
    logits = predictions.predictions.argmax(axis=-1)
    prediction_text = tokenizer.batch_decode(logits)
    return {"labels": labels, "predictions": prediction_text}


class WandbPredictionProgressCallback(WandbCallback):
    """Custom WandbCallback to log model predictions during training.

    This callback logs model predictions and labels to a wandb.Table at each
    logging step during training. It allows to visualize the
    model predictions as the training progresses.

    Attributes:
        trainer (Trainer): The Hugging Face Trainer instance.
        tokenizer (AutoTokenizer): The tokenizer associated with the model.
        sample_dataset (Dataset): A subset of the validation dataset
          for generating predictions.
        num_samples (int, optional): Number of samples to select from
          the validation dataset for generating predictions. Defaults to 100.
        freq (int, optional): Frequency of logging. Defaults to 2.
    """

    def __init__(self, trainer, tokenizer, val_dataset, num_samples=100, freq=2):
        """Initializes the WandbPredictionProgressCallback instance.

        Args:
            trainer (Trainer): The Hugging Face Trainer instance.
            tokenizer (AutoTokenizer): The tokenizer associated
              with the model.
            val_dataset (Dataset): The validation dataset.
            num_samples (int, optional): Number of samples to select from
              the validation dataset for generating predictions.
              Defaults to 100.
            freq (int, optional): Frequency of logging. Defaults to 2.
        """
        super().__init__()
        self.trainer = trainer
        self.tokenizer = tokenizer
        self.sample_dataset = val_dataset.select(range(num_samples))
        self.freq = freq

    def on_evaluate(self, args, state, control, **kwargs):
        super().on_evaluate(args, state, control, **kwargs)
        # control the frequency of logging by logging the predictions
        # every `freq` epochs
        if state.epoch % self.freq == 0:
            # generate predictions
            predictions = self.trainer.predict(self.sample_dataset)
            # decode predictions and labels
            predictions = decode_predictions(self.tokenizer, predictions)
            # add predictions to a wandb.Table
            predictions_df = pd.DataFrame(predictions)
            predictions_df["epoch"] = state.epoch
            records_table = self._wandb.Table(dataframe=predictions_df)
            # log the table to wandb
            self._wandb.log({"sample_predictions": records_table})


# First, instantiate the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=lm_datasets["train"],
    eval_dataset=lm_datasets["validation"],
)

# Instantiate the WandbPredictionProgressCallback
progress_callback = WandbPredictionProgressCallback(
    trainer=trainer,
    tokenizer=tokenizer,
    val_dataset=lm_dataset["validation"],
    num_samples=10,
    freq=2,
)

# Add the callback to the trainer
trainer.add_callback(progress_callback)
```

For a more detailed example please refer to this [colab](https://colab.research.google.com/github/wandb/examples/blob/master/colabs/huggingface/Custom_Progress_Callback.ipynb)

### What additional W\&B settings are available?

Further configuration of what is logged with `Trainer` is possible by setting environment variables. A full list of W\&B environment variables [can be found here](/platform/hosting/env-vars).

| Environment Variable | Usage                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `WANDB_PROJECT`      | Give your project a name (`huggingface` by default)                                                                                                                                                                                                                                                                                                                            |
| `WANDB_LOG_MODEL`    | <p>Log the model checkpoint as a W\&B Artifact (`false` by default) </p><ul><li><code>false</code> (default): No model checkpointing </li><li><code>checkpoint</code>: A checkpoint will be uploaded every args.save\_steps (set in the Trainer's TrainingArguments). </li><li><code>end</code>: The final model checkpoint will be uploaded at the end of training.</li></ul> |
| `WANDB_WATCH`        | <p>Set whether you'd like to log your models gradients, parameters or neither</p><ul><li><code>false</code> (default): No gradient or parameter logging </li><li><code>gradients</code>: Log histograms of the gradients </li><li><code>all</code>: Log histograms of gradients and parameters</li></ul>                                                                       |
| `WANDB_DISABLED`     | Set to `true` to turn off logging entirely (`false` by default)                                                                                                                                                                                                                                                                                                                |
| `WANDB_QUIET`.       | Set to `true` to limit statements logged to standard output to critical statements only (`false` by default)                                                                                                                                                                                                                                                                   |
| `WANDB_SILENT`       | Set to `true` to silence the output printed by wandb (`false` by default)                                                                                                                                                                                                                                                                                                      |

<Tabs>
  <Tab title="Command Line">
    ```bash  theme={null}
    WANDB_WATCH=all
    WANDB_SILENT=true
    ```
  </Tab>

  <Tab title="Notebook">
    ```notebook  theme={null}
    %env WANDB_WATCH=all
    %env WANDB_SILENT=true
    ```
  </Tab>
</Tabs>

### How do I customize `wandb.init`?

The `WandbCallback` that `Trainer` uses will call `wandb.init` under the hood when `Trainer` is initialized. You can alternatively set up your runs manually by calling `wandb.init` before the`Trainer` is initialized. This gives you full control over your W\&B run configuration.

An example of what you might want to pass to `init` is below. For `wandb.init()` details, see the [`wandb.init()` reference](/models/ref/python/functions/init).

```python  theme={null}
wandb.init(
    project="amazon_sentiment_analysis",
    name="bert-base-high-lr",
    tags=["baseline", "high-lr"],
    group="bert",
)
```

## Additional resources

Below are 6 Transformers and W\&B related articles you might enjoy

<details>
  <summary>Hyperparameter Optimization for Hugging Face Transformers</summary>

  * Three strategies for hyperparameter optimization for Hugging Face Transformers are compared: Grid Search, Bayesian Optimization, and Population Based Training.
  * We use a standard uncased BERT model from Hugging Face transformers, and we want to fine-tune on the RTE dataset from the SuperGLUE benchmark
  * Results show that Population Based Training is the most effective approach to hyperparameter optimization of our Hugging Face transformer model.

  Read the [Hyperparameter Optimization for Hugging Face Transformers report](https://wandb.ai/amogkam/transformers/reports/Hyperparameter-Optimization-for-Hugging-Face-Transformers--VmlldzoyMTc2ODI).
</details>

<details>
  <summary>Hugging Tweets: Train a Model to Generate Tweets</summary>

  * In the article, the author demonstrates how to fine-tune a pre-trained GPT2 HuggingFace Transformer model on anyone's Tweets in five minutes.
  * The model uses the following pipeline: Downloading Tweets, Optimizing the Dataset, Initial Experiments, Comparing Losses Between Users, Fine-Tuning the Model.

  Read the full report [here](https://wandb.ai/wandb/huggingtweets/reports/HuggingTweets-Train-a-Model-to-Generate-Tweets--VmlldzoxMTY5MjI).
</details>

<details>
  <summary>Sentence Classification With Hugging Face BERT and WB</summary>

  * In this article, we'll build a sentence classifier leveraging the power of recent breakthroughs in Natural Language Processing, focusing on an application of transfer learning to NLP.
  * We'll be using The Corpus of Linguistic Acceptability (CoLA) dataset for single sentence classification, which is a set of sentences labeled as grammatically correct or incorrect that was first published in May 2018.
  * We'll use Google's BERT to create high performance models with minimal effort on a range of NLP tasks.

  Read the full report [here](https://wandb.ai/cayush/bert-finetuning/reports/Sentence-Classification-With-Huggingface-BERT-and-W-B--Vmlldzo4MDMwNA).
</details>

<details>
  <summary>A Step by Step Guide to Tracking Hugging Face Model Performance</summary>

  * We use W\&B and Hugging Face transformers to train DistilBERT, a Transformer that's 40% smaller than BERT but retains 97% of BERT's accuracy, on the GLUE benchmark
  * The GLUE benchmark is a collection of nine datasets and tasks for training NLP models

  Read the full report [here](https://wandb.ai/jxmorris12/huggingface-demo/reports/A-Step-by-Step-Guide-to-Tracking-HuggingFace-Model-Performance--VmlldzoxMDE2MTU).
</details>

<details>
  <summary>Examples of Early Stopping in HuggingFace</summary>

  * Fine-tuning a Hugging Face Transformer using Early Stopping regularization can be done natively in PyTorch or TensorFlow.
  * Using the EarlyStopping callback in TensorFlow is straightforward with the `tf.keras.callbacks.EarlyStopping`callback.
  * In PyTorch, there is not an off-the-shelf early stopping method, but there is a working early stopping hook available on GitHub Gist.

  Read the full report [here](https://wandb.ai/ayush-thakur/huggingface/reports/Early-Stopping-in-HuggingFace-Examples--Vmlldzo0MzE2MTM).
</details>

<details>
  <summary>How to Fine-Tune Hugging Face Transformers on a Custom Dataset</summary>

  We fine tune a DistilBERT transformer for sentiment analysis (binary classification) on a custom IMDB dataset.

  Read the full report [here](https://wandb.ai/ayush-thakur/huggingface/reports/How-to-Fine-Tune-HuggingFace-Transformers-on-a-Custom-Dataset--Vmlldzo0MzQ2MDc).
</details>

## Get help or request features

For any issues, questions, or feature requests for the Hugging Face W\&B integration, feel free to post in [this thread on the Hugging Face forums](https://discuss.huggingface.co/t/logging-experiment-tracking-with-w-b/498) or open an issue on the Hugging Face [Transformers GitHub repo](https://github.com/huggingface/transformers).
