# Source: https://docs.wandb.ai/models/track.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Track machine learning experiments with W&B to log metrics, hyperparameters, system metrics, and model artifacts.

# Experiments overview

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
  <ColabLink url="https://colab.research.google.com/github/wandb/examples/blob/master/colabs/intro/Intro_to_Weights_%26_Biases.ipynb" />

  <TryProductLink url="https://wandb.ai/stacey/deep-drive/workspace?workspace=user-lavanyashukla" />
</CardGroup>

Track machine learning experiments with a few lines of code. You can then review the results in an [interactive dashboard](/models/track/workspaces/) or export your data to Python for programmatic access using our [Public API](/models/ref/python/public-api/).

Utilize W\&B Integrations if you use popular frameworks such as [Keras](/models/integrations/keras). See [W\&B Integrations](/models/integrations) for a full list of integrations and information on how to add W\&B to your code.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/88iR80mZ8tuFCZUU/images/experiments/experiments_landing_page.png?fit=max&auto=format&n=88iR80mZ8tuFCZUU&q=85&s=3250a01d7dd14400455474aee6818e30" alt="Experiments dashboard" width="4354" height="2978" data-path="images/experiments/experiments_landing_page.png" />
</Frame>

The image above shows an example dashboard where you can view and compare metrics across multiple [runs](/models/runs/).

## How it works

Track a machine learning experiment with a few lines of code:

1. Create a [W\&B Run](/models/runs/).
2. Store a dictionary of hyperparameters, such as learning rate or model type, into your configuration ([`wandb.Run.config`](/models/track/config/)).
3. Log metrics ([`wandb.Run.log()`](/models/track/log/)) over time in a training loop, such as accuracy and loss.
4. Save outputs of a run, like the model weights or a table of predictions.

The following code demonstrates a common W\&B experiment tracking workflow:

```python  theme={null}
# Start a run.
#
# When this block exits, it waits for logged data to finish uploading.
# If an exception is raised, the run is marked failed.
with wandb.init(entity="", project="my-project-name") as run:
  # Save mode inputs and hyperparameters.
  run.config.learning_rate = 0.01

  # Run your experiment code.
  for epoch in range(num_epochs):
    # Do some training...

    # Log metrics over time to visualize model performance.
    run.log({"loss": loss})

  # Upload model outputs as artifacts.
  run.log_artifact(model)
```

## Get started

Depending on your use case, explore the following resources to get started with W\&B Experiments:

* Read the [W\&B Quickstart](/models/quickstart/) for a step-by-step outline of the W\&B Python SDK commands you could use to create, track, and use a dataset artifact.
* Explore this chapter to learn how to:
  * Create an experiment
  * Configure experiments
  * Log data from experiments
  * View results from experiments
* Explore the [W\&B Python Library](/models/ref/python/) within the [W\&B API Reference Guide](/models/ref/python/).

## Best practices and tips

For best practices and tips for experiments and logging, see [Best Practices: Experiments and Logging](https://wandb.ai/wandb/pytorch-lightning-e2e/reports/W-B-Best-Practices-Guide--VmlldzozNTU1ODY1#w\&b-experiments-and-logging).
