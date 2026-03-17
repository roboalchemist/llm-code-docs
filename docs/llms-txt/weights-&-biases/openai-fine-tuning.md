# Source: https://docs.wandb.ai/models/integrations/openai-fine-tuning.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Fine-tune OpenAI models with W&B to log training metrics, monitor jobs, and compare model performance over time.

# OpenAI Fine-Tuning

export const ColabLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="colab-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05zm-6.3 1.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09 3.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01.21.03zm-6.47 14.25l-.23.33-.08.41.08.41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08z" />
    </svg>
    Try in Colab
  </a>;

<ColabLink url="https://wandb.me/openai-colab" />

Log your OpenAI GPT-3.5 or GPT-4 model's fine-tuning metrics and configuration to W\&B. Utilize the W\&B ecosystem to track your fine-tuning experiments, models, and datasets and share your results with your colleagues.

<Note>
  See the [OpenAI documentation](https://platform.openai.com/docs/guides/fine-tuning/which-models-can-be-fine-tuned) for a list of models that you can fine tune.
</Note>

See the [W\&B Integration](https://developers.openai.com/cookbook/examples/third_party/gpt_finetuning_with_wandb) section in the OpenAI documentation for supplemental information on how to integrate W\&B with OpenAI for fine-tuning.

## Install or update OpenAI Python API

The W\&B OpenAI fine-tuning integration works with OpenAI version 1.0 and above. See the PyPI documentation for the latest version of the [OpenAI Python API](https://pypi.org/project/openai/) library.

To install OpenAI Python API, run:

```python  theme={null}
pip install openai
```

If you already have OpenAI Python API installed, you can update it with:

```python  theme={null}
pip install -U openai
```

## Sync your OpenAI fine-tuning results

Integrate W\&B with OpenAI's fine-tuning API to log your fine-tuning metrics and configuration to W\&B. To do this, use the `WandbLogger` class from the `wandb.integration.openai.fine_tuning` module.

```python  theme={null}
from wandb.integration.openai.fine_tuning import WandbLogger

# Finetuning logic

WandbLogger.sync(fine_tune_job_id=FINETUNE_JOB_ID)
```

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/mVjDwbx0mC8gYx-b/images/integrations/open_ai_auto_scan.png?fit=max&auto=format&n=mVjDwbx0mC8gYx-b&q=85&s=6d152aaf27c90463e32ed3e85602f4a8" alt="OpenAI auto-scan feature" width="1600" height="779" data-path="images/integrations/open_ai_auto_scan.png" />
</Frame>

### Sync your fine-tunes

Sync your results from your script

```python  theme={null}
from wandb.integration.openai.fine_tuning import WandbLogger

# one line command
WandbLogger.sync()

# passing optional parameters
WandbLogger.sync(
    fine_tune_job_id=None,
    num_fine_tunes=None,
    project="OpenAI-Fine-Tune",
    entity=None,
    overwrite=False,
    model_artifact_name="model-metadata",
    model_artifact_type="model",
    **kwargs_wandb_init
)
```

### Reference

| Argument                | Description                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| fine\_tune\_job\_id     | This is the OpenAI Fine-Tune ID which you get when you create your fine-tune job using `client.fine_tuning.jobs.create`. If this argument is None (default), all the OpenAI fine-tune jobs that haven't already been synced will be synced to W\&B.                                                                                                                                                         |
| openai\_client          | Pass an initialized OpenAI client to `sync`. If no client is provided, one is initialized by the logger itself. By default it is None.                                                                                                                                                                                                                                                                      |
| num\_fine\_tunes        | If no ID is provided, then all the unsynced fine-tunes will be logged to W\&B. This argument allows you to select the number of recent fine-tunes to sync. If num\_fine\_tunes is 5, it selects the 5 most recent fine-tunes.                                                                                                                                                                               |
| project                 | W\&B project name where your fine-tune metrics, models, data, etc. will be logged. By default, the project name is "OpenAI-Fine-Tune."                                                                                                                                                                                                                                                                      |
| entity                  | W\&B Username or team name where you're sending runs. By default, your default entity is used, which is usually your username.                                                                                                                                                                                                                                                                              |
| overwrite               | Forces logging and overwrite existing wandb run of the same fine-tune job. By default this is False.                                                                                                                                                                                                                                                                                                        |
| wait\_for\_job\_success | Once an OpenAI fine-tuning job is started it usually takes a bit of time. To ensure that your metrics are logged to W\&B as soon as the fine-tune job is finished, this setting will check every 60 seconds for the status of the fine-tune job to change to `succeeded`. Once the fine-tune job is detected as being successful, the metrics will be synced automatically to W\&B. Set to True by default. |
| model\_artifact\_name   | The name of the model artifact that is logged. Defaults to `"model-metadata"`.                                                                                                                                                                                                                                                                                                                              |
| model\_artifact\_type   | The type of the model artifact that is logged. Defaults to `"model"`.                                                                                                                                                                                                                                                                                                                                       |
| \*\*kwargs\_wandb\_init | Aany additional argument passed directly to [`wandb.init()`](/models/ref/python/functions/init)                                                                                                                                                                                                                                                                                                             |

## Dataset versioning and visualization

### Versioning

The training and validation data that you upload to OpenAI for fine-tuning are automatically logged as W\&B Artifacts for easier version control. Below is an view of the training file in Artifacts. Here you can see the W\&B run that logged this file, when it was logged, what version of the dataset this is, the metadata, and DAG lineage from the training data to the trained model.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/mVjDwbx0mC8gYx-b/images/integrations/openai_data_artifacts.png?fit=max&auto=format&n=mVjDwbx0mC8gYx-b&q=85&s=dac293cde2af9b21a77c049a41fd18c7" alt="W&B Artifacts with training datasets" width="3450" height="1166" data-path="images/integrations/openai_data_artifacts.png" />
</Frame>

### Visualization

The datasets are visualized as W\&B Tables, which allows you to explore, search, and interact with the dataset. Check out the training samples visualized using W\&B Tables below.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/mVjDwbx0mC8gYx-b/images/integrations/openai_data_visualization.png?fit=max&auto=format&n=mVjDwbx0mC8gYx-b&q=85&s=545f9a3355dfe483b87aa2dcb5e0b3f4" alt="OpenAI data" width="2758" height="1294" data-path="images/integrations/openai_data_visualization.png" />
</Frame>

## The fine-tuned model and model versioning

OpenAI gives you an id of the fine-tuned model. Since we don't have access to the model weights, the `WandbLogger` creates a `model_metadata.json` file with all the details (hyperparameters, data file ids, etc.) of the model along with the \`fine\_tuned\_model\`\` id and is logged as a W\&B Artifact.

This model (metadata) artifact can further be linked to a model in the [W\&B Registry](/models/registry/).

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/mVjDwbx0mC8gYx-b/images/integrations/openai_model_metadata.png?fit=max&auto=format&n=mVjDwbx0mC8gYx-b&q=85&s=e39d37d961780edd14ce663b1b5c3d9e" alt="OpenAI model metadata" width="3450" height="1512" data-path="images/integrations/openai_model_metadata.png" />
</Frame>

## Frequently asked questions

### How do I share my fine-tune results with my team in W\&B?

Log your fine-tune jobs to your team account with:

```python  theme={null}
WandbLogger.sync(entity="YOUR_TEAM_NAME")
```

### How can I organize my runs?

Your W\&B runs are automatically organized and can be filtered/sorted based on any configuration parameter such as job type, base model, learning rate, training filename and any other hyper-parameter.

In addition, you can rename your runs, add notes or create tags to group them.

Once you’re satisfied, you can save your workspace and use it to create report, importing data from your runs and saved artifacts (training/validation files).

### How can I access my fine-tuned model?

Fine-tuned model ID is logged to W\&B as artifacts (`model_metadata.json`) as well config.

```python  theme={null}
import wandb
    
with wandb.init(project="OpenAI-Fine-Tune", entity="YOUR_TEAM_NAME") as run:
    ft_artifact = run.use_artifact("ENTITY/PROJECT/model_metadata:VERSION")
    artifact_dir = ft_artifact.download()
```

where `VERSION` is either:

* a version number such as `v2`
* the fine-tune id such as `ft-xxxxxxxxx`
* an alias added automatically such as `latest` or manually

You can then access `fine_tuned_model` id by reading the downloaded `model_metadata.json` file.

### What if a fine-tune was not synced successfully?

If a fine-tune was not logged to W\&B successfully, you can use the `overwrite=True` and pass the fine-tune job id:

```python  theme={null}
WandbLogger.sync(
    fine_tune_job_id="FINE_TUNE_JOB_ID",
    overwrite=True,
)
```

### Can I track my datasets and models with W\&B?

The training and validation data are logged automatically to W\&B as artifacts. The metadata including the ID for the fine-tuned model is also logged as artifacts.

You can always control the pipeline using low level wandb APIs like `wandb.Artifact`, `wandb.Run.log`, etc. This will allow complete traceability of your data and models.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/mVjDwbx0mC8gYx-b/images/integrations/open_ai_faq_can_track.png?fit=max&auto=format&n=mVjDwbx0mC8gYx-b&q=85&s=df528635783bca105c81c18389b11781" alt="OpenAI tracking FAQ" width="1088" height="260" data-path="images/integrations/open_ai_faq_can_track.png" />
</Frame>

## Resources

* [OpenAI Fine-tuning Documentation](https://platform.openai.com/docs/guides/fine-tuning/) is very thorough and contains many useful tips
* [Demo Colab](https://wandb.me/openai-colab)
* [How to Fine-Tune Your OpenAI GPT-3.5 and GPT-4 Models with W\&B](https://wandb.me/openai-report) report
