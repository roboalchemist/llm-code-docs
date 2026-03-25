# Source: https://docs.wandb.ai/weave/quickstart.md

# Source: https://docs.wandb.ai/models/quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Install W&B and start tracking, visualizing, and managing machine learning experiments in minutes.

# W&B Quickstart

export const GitHubLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
    </svg>
    GitHub source
  </a>;

export const ColabLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="colab-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05zm-6.3 1.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09 3.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01.21.03zm-6.47 14.25l-.23.33-.08.41.08.41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08z" />
    </svg>
    Try in Colab
  </a>;

Install W\&B to track, visualize, and manage machine learning experiments of any size.

<Note>
  Are you looking for information on W\&B Weave? See the [Weave Python SDK quickstart](/weave/quickstart) or [Weave TypeScript SDK quickstart](/weave/reference/generated_typescript_docs/intro-notebook).
</Note>

## Sign up and create an API key

To authenticate your machine with W\&B, you need an API key.

To create an API key, select the **Personal API key** or **Service Account API key** tab for details.

<Tabs>
  <Tab title="Personal API key">
    To create a personal API key owned by your user ID:

    1. Log in to W\&B, click your user profile icon, then click **User Settings**.
    2. Click **Create new API key**.
    3. Provide a descriptive name for your API key.
    4. Click **Create**.
    5. Copy the displayed API key immediately and store it securely.
  </Tab>

  <Tab title="Service account API key">
    To create an API key owned by a service account:

    1. Navigate to the **Service Accounts** tab in your team or organization settings.
    2. Find the service account in the list.
    3. Click the action menu (`...`), then click **Create API key**.
    4. Provide a name for the API key, then click **Create**.
    5. Copy the displayed API key immediately and store it securely.
    6. Click **Done**.

    You can create multiple API keys for a single service account to support different environments or workflows.
  </Tab>
</Tabs>

<Warning>
  The full API key is only shown once at creation time. After you close the dialog, you cannot view the full API key again. Only the key ID (first part of the key) is visible in your settings. If you lose the full API key, you must create a new API key.
</Warning>

For secure storage options, see [Store API keys securely](/platform/app/settings-page/user-settings/#store-and-handle-api-keys-securely).

This quickstart is also available as a Colab notebook:

<div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap' }}>
  <ColabLink url="https://colab.research.google.com/github/wandb/examples/blob/master/colabs/intro/run_quickstart.ipynb" />

  <GitHubLink url="https://github.com/wandb/examples/blob/master/colabs/intro/run_quickstart.ipynb" />
</div>

## Install the `wandb` library and log in

<Tabs>
  <Tab title="Command Line">
    1. Set the `WANDB_API_KEY` [environment variable](/models/track/environment-variables/).

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

## Initialize a run and track hyperparameters

In your Python script or notebook, initialize a W\&B run object with [`wandb.init()`](/models/ref/python/experiments/run/). Use a dictionary for the `config` parameter
to specify hyperparameter names and values. Within the `with` statement, you can log metrics and other information to W\&B.

```python  theme={null}
import wandb

wandb.login()

# Project that the run is recorded to
project = "my-awesome-project"

# Dictionary with hyperparameters
config = {
    'epochs' : 10,
    'lr' : 0.01
}

with wandb.init(project=project, config=config) as run:
    # Training code here
    # Log values to W&B with run.log()
    run.log({"accuracy": 0.9, "loss": 0.1})
```

See the next section for a complete example that simulates a training run and logs accuracy and loss metrics to W\&B.

<Info>
  A [run](/models/runs/) is a core element of W\&B. You use runs to [track metrics](/models/track/), [create logs](/models/track/log/), track artifacts, and more.
</Info>

## Create a machine learning training experiment

This mock training script logs simulated accuracy and loss metrics to W\&B. Copy and paste the following code into a Python script or notebook cell and run it:

```python  theme={null}
import wandb
import random

wandb.login()

# Project that the run is recorded to
project = "my-awesome-project"

# Dictionary with hyperparameters
config = {
    'epochs' : 10,
    'lr' : 0.01
}

with wandb.init(project=project, config=config) as run:
    offset = random.random() / 5
    print(f"lr: {config['lr']}")
    
    # Simulate a training run
    for epoch in range(2, config['epochs']):
        acc = 1 - 2**-config['epochs'] - random.random() / config['epochs'] - offset
        loss = 2**-config['epochs'] + random.random() / config['epochs'] + offset
        print(f"epoch={config['epochs']}, accuracy={acc}, loss={loss}")
        run.log({"accuracy": acc, "loss": loss})
```

Visit [wandb.ai/home](https://wandb.ai/home) to view recorded metrics such as accuracy and loss and how they changed during each training step. The following image shows the loss and accuracy tracked from each run. Each run object appears in the **Runs** column with generated names.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/mmuC1X8m1VKb0ElQ/images/quickstart/quickstart_image.png?fit=max&auto=format&n=mmuC1X8m1VKb0ElQ&q=85&s=220f7435e1cb29fc63fd00fc561116e8" alt="Shows loss and accuracy tracked from each run." width="3456" height="2004" data-path="images/quickstart/quickstart_image.png" />
</Frame>

## Next steps

Explore more features of the W\&B ecosystem:

1. Read the [W\&B Integration tutorials](/models/integrations) that combine W\&B with frameworks like PyTorch, libraries like Hugging Face, and services like SageMaker.
2. Organize runs, automate visualizations, summarize findings, and share updates with collaborators using [W\&B Reports](/models/reports).
3. Create [W\&B Artifacts](/models/artifacts) to track datasets, models, dependencies, and results throughout your machine learning pipeline.
4. Automate hyperparameter searches and optimize models with [W\&B Sweeps](/models/sweeps).
5. Analyze runs, visualize model predictions, and share insights on a [central dashboard](/models/tables).
6. Visit [W\&B AI Academy](https://wandb.ai/site/courses/) to learn about LLMs, MLOps, and W\&B Models through hands-on courses.
7. Visit [weave-docs.wandb.ai](/weave) to learn how to track, experiment with, evaluate, deploy, and improve your LLM-based applications using Weave.
