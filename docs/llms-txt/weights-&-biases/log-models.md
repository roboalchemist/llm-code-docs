# Source: https://docs.wandb.ai/models/track/log/log-models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Log models

> Log model artifacts to a W&B run and retrieve them later using the log_model and use_model SDK methods.

export const ColabLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="colab-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05zm-6.3 1.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09 3.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01.21.03zm-6.47 14.25l-.23.33-.08.41.08.41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08z" />
    </svg>
    Try in Colab
  </a>;

<ColabLink url="https://colab.research.google.com/github/wandb/examples/blob/ken-add-new-model-reg-api/colabs/wandb-model-registry/New_Model_Logging_in_W&B.ipynb" />

# Log models

The following guide describes how to log models to a W\&B run and interact with them.

<Note>
  The following APIs are useful for tracking models as a part of your experiment tracking workflow. Use the APIs listed on this page to log models to a run, and to access metrics, tables, media, and other objects.

  W\&B suggests that you use [W\&B Artifacts](/models/artifacts/) if you want to:

  * Create and keep track of different versions of serialized data besides models, such as datasets, prompts, and more.
  * Explore [lineage graphs](/models/artifacts/explore-and-traverse-an-artifact-graph/) of a model or any other objects tracked in W\&B.
  * Interact with the model artifacts these methods created, such as [updating properties](/models/artifacts/update-an-artifact/) (metadata, aliases, and descriptions)

  For more information on W\&B Artifacts and advanced versioning use cases, see the [Artifacts](/models/artifacts/) documentation.
</Note>

## Log a model to a run

Use the [`log_model`](/models/ref/python/experiments/run#log_model) to log a model artifact that contains content within a directory you specify. The [`log_model`](/models/ref/python/experiments/run#log_model) method also marks the resulting model artifact as an output of the W\&B run.

You can track a model's dependencies and the model's associations if you mark the model as the input or output of a W\&B run. View the lineage of the model within the W\&B App UI. See the [Explore and traverse artifact graphs](/models/artifacts/explore-and-traverse-an-artifact-graph/) page within the [Artifacts](/models/artifacts/) chapter for more information.

Provide the path where your model files are saved to the `path` parameter. The path can be a local file, directory, or [reference URI](/models/artifacts/track-external-files/#amazon-s3--gcs--azure-blob-storage-references) to an external bucket such as `s3://bucket/path`.

Ensure to replace values enclosed in `<>` with your own.

```python  theme={null}
import wandb

# Initialize a W&B run
with wandb.init(project="<your-project>", entity="<your-entity>") as run:

    # Log the model
    run.log_model(path="<path-to-model>", name="<name>")
```

Optionally provide a name for the model artifact for the `name` parameter. If `name` is not specified, W\&B will use the basename of the input path prepended with the run ID as the name.

<Note>
  Keep track of the `name` that you, or W\&B assigns, to the model. You will need the name of the model to retrieve the model path with the [`wandb.Run.use_model()`](/models/ref/python/experiments/run#use_model) method.
</Note>

See [`log_model`](/models/ref/python/experiments/run#log_model) in the API Reference for parameters.

<details>
  <summary>Example: Log a model to a run</summary>

  ```python  theme={null}
  import os
  import wandb
  from tensorflow import keras
  from tensorflow.keras import layers

  config = {"optimizer": "adam", "loss": "categorical_crossentropy"}

  # Initialize a W&B run
  with wandb.init(entity="charlie", project="mnist-experiments", config=config) as run:

      # Hyperparameters
      loss = run.config["loss"]
      optimizer = run.config["optimizer"]
      metrics = ["accuracy"]
      num_classes = 10
      input_shape = (28, 28, 1)

      # Training algorithm
      model = keras.Sequential(
          [
              layers.Input(shape=input_shape),
              layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
              layers.MaxPooling2D(pool_size=(2, 2)),
              layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
              layers.MaxPooling2D(pool_size=(2, 2)),
              layers.Flatten(),
              layers.Dropout(0.5),
              layers.Dense(num_classes, activation="softmax"),
          ]
      )

      # Configure the model for training
      model.compile(loss=loss, optimizer=optimizer, metrics=metrics)

      # Save model
      model_filename = "model.h5"
      local_filepath = "./"
      full_path = os.path.join(local_filepath, model_filename)
      model.save(filepath=full_path)

      # Log the model to the W&B run
      run.log_model(path=full_path, name="MNIST")
  ```

  When you call `log_model`, a model artifact named `MNIST` is created and the file `model.h5` is added to the model artifact. Your terminal or notebook will print information of where to find information about the run the model was logged to.

  ```python  theme={null}
  View run different-surf-5 at: https://wandb.ai/charlie/mnist-experiments/runs/wlby6fuw
  Synced 5 W&B file(s), 0 media file(s), 1 artifact file(s) and 0 other file(s)
  Find logs at: ./wandb/run-20231206_103511-wlby6fuw/logs
  ```
</details>

## Download and use a logged model

Use the [`use_model`](/models/ref/python/experiments/run#use_model) function to access and download models files previously logged to a W\&B run.

Provide the name of the model artifact where the model files you want to retrieve are stored. The name you provide must match the name of an existing logged model artifact.

If you did not define `name` when you originally logged the files with `log_model`, the default name assigned is the basename of the input path, prepended with the run ID.

Ensure to replace the values enclosed in `<>` with your own:

```python  theme={null}
import wandb

# Initialize a run
with wandb.init(project="<your-project>", entity="<your-entity>") as run:

    # Access and download model. Returns path to downloaded artifact
    downloaded_model_path = run.use_model(name="<your-model-name>")
```

The [use\_model](/models/ref/python/experiments/run#use_model) function returns the path of downloaded model files. Keep track of this path if you want to link this model later. In the preceding code snippet, the returned path is stored in a variable called `downloaded_model_path`.

<details>
  <summary>Example: Download and use a logged model</summary>

  For example, in the following code snippet a user called the `use_model` API. They specified the name of the model artifact they want to fetch and they also provided a version/alias. They then stored the path that is returned from the API to the `downloaded_model_path` variable.

  ```python  theme={null}
  import wandb

  entity = "luka"
  project = "NLP_Experiments"
  alias = "latest"  # semantic nickname or identifier for the model version
  model_artifact_name = "fine-tuned-model"

  # Initialize a run
  with wandb.init(project=project, entity=entity) as run:
      # Access and download model. Returns path to downloaded artifact
      downloaded_model_path = run.use_model(name = f"{model_artifact_name}:{alias}") 
  ```
</details>

See [`use_model`](/models/ref/python/experiments/run#use_model) in the API Reference for parameters and return type.
