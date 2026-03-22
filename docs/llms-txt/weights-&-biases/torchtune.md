# Source: https://docs.wandb.ai/models/integrations/torchtune.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# PyTorch torchtune

> Use W&B logging in PyTorch torchtune for tracking LLM fine-tuning experiments with the WandBLogger metric logger.

export const ColabLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="colab-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05zm-6.3 1.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09 3.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01.21.03zm-6.47 14.25l-.23.33-.08.41.08.41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08z" />
    </svg>
    Try in Colab
  </a>;

<ColabLink url="https://colab.research.google.com/github/wandb/examples/blob/master/colabs/torchtune/torchtune_and_wandb.ipynb" />

[torchtune](https://meta-pytorch.org/torchtune/stable/index.html) is a PyTorch-based library designed to streamline the authoring, fine-tuning, and experimentation processes for large language models (LLMs). Additionally, torchtune has built-in support for [logging with W\&B](https://meta-pytorch.org/torchtune/stable/deep_dives/wandb_logging.html), enhancing tracking and visualization of training processes.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/w-lBKSCruauC3-2f/images/integrations/torchtune_dashboard.png?fit=max&auto=format&n=w-lBKSCruauC3-2f&q=85&s=b2ff48f4797a1d2c55b760c210c95408" alt="TorchTune training dashboard" width="1942" height="1286" data-path="images/integrations/torchtune_dashboard.png" />
</Frame>

Check the W\&B blog post on [Fine-tuning Mistral 7B using torchtune](https://wandb.ai/capecape/torchtune-mistral/reports/torchtune-The-new-PyTorch-LLM-fine-tuning-library---Vmlldzo3NTUwNjM0).

## W\&B logging at your fingertips

<Tabs>
  <Tab title="Command line">
    Override command line arguments at launch:

    ```bash  theme={null}
    tune run lora_finetune_single_device --config llama3/8B_lora_single_device \
      metric_logger._component_=torchtune.utils.metric_logging.WandBLogger \
      metric_logger.project="llama3_lora" \
      log_every_n_steps=5
    ```
  </Tab>

  <Tab title="Recipe">
    Enable W\&B logging on the recipe's config:

    ```yaml  theme={null}
    # inside llama3/8B_lora_single_device.yaml
    metric_logger:
      _component_: torchtune.utils.metric_logging.WandBLogger
      project: llama3_lora
    log_every_n_steps: 5
    ```
  </Tab>
</Tabs>

## Use the W\&B metric logger

Enable W\&B logging on the recipe's config file by modifying the `metric_logger` section. Change the `_component_` to `torchtune.utils.metric_logging.WandBLogger` class. You can also pass a `project` name and `log_every_n_steps` to customize the logging behavior.

You can also pass any other `kwargs` as you would to the [wandb.init()](/models/ref/python/functions/init) method. For example, if you are working on a team, you can pass the `entity` argument to the `WandBLogger` class to specify the team name.

<Tabs>
  <Tab title="Recipe">
    ```yaml  theme={null}
    # inside llama3/8B_lora_single_device.yaml
    metric_logger:
      _component_: torchtune.utils.metric_logging.WandBLogger
      project: llama3_lora
      entity: my_project
      job_type: lora_finetune_single_device
      group: my_awesome_experiments
    log_every_n_steps: 5
    ```
  </Tab>

  <Tab title="Command Line">
    ```shell  theme={null}
    tune run lora_finetune_single_device --config llama3/8B_lora_single_device \
      metric_logger._component_=torchtune.utils.metric_logging.WandBLogger \
      metric_logger.project="llama3_lora" \
      metric_logger.entity="my_project" \
      metric_logger.job_type="lora_finetune_single_device" \
      metric_logger.group="my_awesome_experiments" \
      log_every_n_steps=5
    ```
  </Tab>
</Tabs>

## What is logged?

You can explore the W\&B dashboard to see the logged metrics. By default W\&B logs all of the hyperparameters from the config file and the launch overrides.

W\&B captures the resolved config on the **Overview** tab. W\&B also stores the config in YAML format on the [Files tab](https://wandb.ai/capecape/torchtune/runs/joyknwwa/files).

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/w-lBKSCruauC3-2f/images/integrations/torchtune_config.png?fit=max&auto=format&n=w-lBKSCruauC3-2f&q=85&s=80ee1d6653d94ebea2cef75ced3bcd41" alt="TorchTune configuration" width="1806" height="1362" data-path="images/integrations/torchtune_config.png" />
</Frame>

### Logged metrics

Each recipe has its own training loop. Check each individual recipe to see its logged metrics, which include these by default:

| Metric              | Description                                                                                                                                                                                                                                                            |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `loss`              | The loss of the model                                                                                                                                                                                                                                                  |
| `lr`                | The learning rate                                                                                                                                                                                                                                                      |
| `tokens_per_second` | The tokens per second of the model                                                                                                                                                                                                                                     |
| `grad_norm`         | The gradient norm of the model                                                                                                                                                                                                                                         |
| `global_step`       | Corresponds to the current step in the training loop. Takes into account gradient accumulation, basically every time an optimizer step is taken, the model is updated, the gradients are accumulated and the model is updated once every `gradient_accumulation_steps` |

<Note>
  `global_step` is not the same as the number of training steps. It corresponds to the current step in the training loop. Takes into account gradient accumulation, basically every time an optimizer step is taken the `global_step` is incremented by 1. For example, if the dataloader has 10 batches, gradient accumulation steps is 2 and run for 3 epochs, the optimizer will step 15 times, in this case `global_step` will range from 1 to 15.
</Note>

The streamlined design of torchtune allows to easily add custom metrics or modify the existing ones. It suffices to modify the corresponding [recipe file](https://github.com/meta-pytorch/torchtune/tree/main/recipes), for example, computing one could log `current_epoch` as a percentage of the total number of epochs as following:

```python  theme={null}
# inside `train.py` function in the recipe file
self._metric_logger.log_dict(
    {"current_epoch": self.epochs * self.global_step / self._steps_per_epoch},
    step=self.global_step,
)
```

<Note>
  This is a fast evolving library, the current metrics are subject to change. If you want to add a custom metric, you should modify the recipe and call the corresponding `self._metric_logger.*` function.
</Note>

## Save and load checkpoints

The torchtune library supports various [checkpoint formats](https://meta-pytorch.org/torchtune/stable/deep_dives/checkpointer.html). Depending on the origin of the model you are using, you should switch to the appropriate [checkpointer class](https://meta-pytorch.org/torchtune/stable/deep_dives/checkpointer.html).

If you want to save the model checkpoints to [W\&B Artifacts](/models/artifacts/), the simplest solution is to override the `save_checkpoint` functions inside the corresponding recipe.

Here is an example of how you can override the `save_checkpoint` function to save the model checkpoints to W\&B Artifacts.

```python  theme={null}
def save_checkpoint(self, epoch: int) -> None:
    ...
    ## Let's save the checkpoint to W&B
    ## depending on the Checkpointer Class the file will be named differently
    ## Here is an example for the full_finetune case
    checkpoint_file = Path.joinpath(
        self._checkpointer._output_dir, f"torchtune_model_{epoch}"
    ).with_suffix(".pt")
    wandb_artifact = wandb.Artifact(
        name=f"torchtune_model_{epoch}",
        type="model",
        # description of the model checkpoint
        description="Model checkpoint",
        # you can add whatever metadata you want as a dict
        metadata={
            utils.SEED_KEY: self.seed,
            utils.EPOCHS_KEY: self.epochs_run,
            utils.TOTAL_EPOCHS_KEY: self.total_epochs,
            utils.MAX_STEPS_KEY: self.max_steps_per_epoch,
        },
    )
    wandb_artifact.add_file(checkpoint_file)
    wandb.log_artifact(wandb_artifact)
```
