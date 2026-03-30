# Source: https://docs.wandb.ai/models/ref/sdk-coding-cheat-sheet/artifacts.md

# Source: https://docs.wandb.ai/models/ref/python/public-api/artifacts.md

# Source: https://docs.wandb.ai/models/artifacts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Overview of W&B Artifacts, how they work, and how to get started using them.

# Artifacts overview

export const TryProductLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" xmlns="http://www.w3.org/2000/svg">
      <line x1="4" y1="21" x2="4" y2="14"></line>
      <line x1="4" y1="10" x2="4" y2="3"></line>
      <line x1="12" y1="21" x2="12" y2="12"></line>
      <line x1="12" y1="8" x2="12" y2="3"></line>
      <line x1="20" y1="21" x2="20" y2="16"></line>
      <line x1="20" y1="12" x2="20" y2="3"></line>
      <circle cx="4" cy="12" r="2"></circle>
      <circle cx="12" cy="10" r="2"></circle>
      <circle cx="20" cy="14" r="2"></circle>
    </svg>
    Try in W&amp;B
  </a>;

export const ColabLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="colab-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05zm-6.3 1.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09 3.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01.21.03zm-6.47 14.25l-.23.33-.08.41.08.41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08z" />
    </svg>
    Try in Colab
  </a>;

<CardGroup cols={4}>
  <ColabLink url="https://colab.research.google.com/github/wandb/examples/blob/master/colabs/wandb-artifacts/Pipeline_Versioning_with_W&B_Artifacts.ipynb" />

  <TryProductLink url="https://wandb.ai/wandb/arttest/artifacts/model/iv3_trained/5334ab69740f9dda4fed/lineage" />
</CardGroup>

Use W\&B Artifacts to track and version data as the inputs and outputs of your [W\&B Runs](/models/runs). For example, a model training run might take in a dataset as input and produce a trained model as output. You can log hyperparameters, metadata, and metrics to a run, and you can use an artifact to log, track, and version the dataset used to train the model as input and another artifact for the resulting model checkpoints as output.

## Use cases

You can use artifacts throughout your entire ML workflow as inputs and outputs of [runs](/models/runs). You can use datasets, models, or even other artifacts as inputs for processing.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/wKCrMJZKG3PxyJhv/images/artifacts/artifacts_landing_page2.png?fit=max&auto=format&n=wKCrMJZKG3PxyJhv&q=85&s=e54ab1c9c22f8a7abfa6d2a08bb145d3" alt="Artifacts workflow diagram with inputs and outputs for model training, data processing, and model evaluation" width="1991" height="503" data-path="images/artifacts/artifacts_landing_page2.png" />
</Frame>

| Use Case               | Input                                  | Output                       |
| ---------------------- | -------------------------------------- | ---------------------------- |
| Model Training         | Dataset (training and validation data) | Trained Model                |
| Dataset Pre-Processing | Dataset (raw data)                     | Dataset (pre-processed data) |
| Model Evaluation       | Model + Dataset (test data)            | [W\&B Table](/models/tables) |
| Model Optimization     | Model                                  | Optimized Model              |

<Note>
  The following code snippets are meant to be run in order.
</Note>

## Create an artifact

Create an artifact with four lines of code:

1. Create a [W\&B run](/models/runs).
2. Create an artifact object with [`wandb.Artifact`](/models/ref/python/experiments/artifact).
3. Add one or more files, such as a model file or dataset, to the artifact object with `wandb.Artifact.add_file()`.
4. Log your artifact to W\&B with `wandb.Run.log_artifact()`.

For example, the following code snippet shows how to log a file called `dataset.h5` to an artifact called `example_artifact`:

```python  theme={null}
import wandb

with wandb.init(project="artifacts-example", job_type="add-dataset") as run:
    artifact = wandb.Artifact(name="example_artifact", type="dataset")
    artifact.add_file(local_path="./dataset.h5", name="training_dataset")
    run.log_artifact(artifact)
```

* The `type` of the artifact affects how it appears in the W\&B platform. If you do not specify a `type`, it defaults to `unspecified`.
* Each label of the dropdown represents a different `type` parameter value. In the above code snippet, the artifact's `type` is `dataset`.

<Note>
  See the [track external files](/models/artifacts/track-external-files) page for information on how to add references to files or directories stored in external object storage, like an Amazon S3 bucket.
</Note>

## Download an artifact

Indicate the artifact you want to mark as input to your run with the [`wandb.Run.use_artifact()`](/models/ref/python/experiments/run#use_artifact) method.

Continuing from the previous code snippet, the following code example shows how to use the artifact called `example_artifact` that was created earlier:

```python  theme={null}
with wandb.init(project="artifacts-example", job_type="add-dataset") as run:
    artifact = run.use_artifact("training_dataset:latest")  # returns a run object using the "my_data" artifact
```

This returns an artifact object.

Next, use the returned object to download all contents of the artifact:

```python  theme={null}
datadir = artifact.download()  # downloads the full `my_data` artifact to the default directory.
```

<Note>
  You can pass a custom path into the `root` [parameter](/models/ref/python/experiments/artifact) to download an artifact to a specific directory. For alternate ways to download artifacts and to see additional parameters, see the guide on [downloading and using artifacts](/models/artifacts/download-and-use-an-artifact).
</Note>

## Next steps

* Learn how to [version](/models/artifacts/create-a-new-artifact-version) and [update](/models/artifacts/update-an-artifact) artifacts.
* Learn how to trigger downstream workflows or notify a Slack channel in response to changes to your artifacts with [automations](/models/automations).
* Learn about the [registry](/models/registry), a space that houses trained models.
* Explore the [Python SDK](/models/ref/python/experiments/artifact) and [CLI](/models/ref/cli/wandb-artifact) reference guides.
