# Source: https://docs.baseten.co/reference/cli/index.md

# Truss CLI overview

> Install and configure the Truss CLI for deploying models, chains, and training jobs.

The `truss` CLI is your primary interface for everything from packaging and
deploying AI models to building and orchestrating multi-step chains to launching and
managing training jobs.

Use the following commands to manage your models, chains, and training jobs:

* **Models**: Package and deploy individual model servers.
* **Chains**: Build and deploy multi-step inference pipelines.
* **Training**: Launch and manage training jobs.

<Accordion title="Install the Truss CLI">
  To use Truss, install a recent Truss version and ensure pydantic is v2:

  ```bash  theme={"system"}
  pip install --upgrade truss 'pydantic>=2.0.0'
  ```

  <Accordion title="Help for setting up a clean development environment">
    Truss requires python `>=3.9,<3.15`. To set up a fresh development environment,
    you can use the following commands, creating a environment named `truss_env`
    using `pyenv`:

    ```bash  theme={"system"}
    curl https://pyenv.run | bash
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    source ~/.bashrc
    pyenv install 3.11.0
    ENV_NAME="truss_env"
    pyenv virtualenv 3.11.0 $ENV_NAME
    pyenv activate $ENV_NAME
    pip install --upgrade truss 'pydantic>=2.0.0'
    ```
  </Accordion>

  To deploy Truss remotely, you also need a
  [Baseten account](https://app.baseten.co/signup).
  It is handy to export your API key to the current shell session or permanently in your `.bashrc`:

  ```bash ~/.bashrc theme={"system"}
  export BASETEN_API_KEY="nPh8..."
  ```
</Accordion>

## CLI structure

The `truss` CLI organizes commands by workflow:

```
truss [OPTIONS] COMMAND [ARGS]...
```

### Model commands

Use these commands to package, deploy, and iterate on individual models.

| Command                                               | Description                       |
| ----------------------------------------------------- | --------------------------------- |
| [`truss login`](/reference/cli/truss/login)           | Authenticate with Baseten         |
| [`truss init`](/reference/cli/truss/init)             | Create a new Truss project        |
| [`truss push`](/reference/cli/truss/push)             | Deploy a model to Baseten         |
| [`truss watch`](/reference/cli/truss/watch)           | Live reload during development    |
| [`truss predict`](/reference/cli/truss/predict)       | Call the packaged model           |
| [`truss model-logs`](/reference/cli/truss/model-logs) | Fetch logs for the packaged model |

### Chain commands

Use these commands to build multi-model pipelines with shared dependencies.

| Command                                                        | Description                    |
| -------------------------------------------------------------- | ------------------------------ |
| [`truss chains init`](/reference/cli/chains/chains-cli#init)   | Initialize a new Chain project |
| [`truss chains push`](/reference/cli/chains/chains-cli#push)   | Deploy a Chain to Baseten      |
| [`truss chains watch`](/reference/cli/chains/chains-cli#watch) | Live reload Chain development  |

### Training commands

Use these commands to launch, monitor, and manage training jobs.

| Command                                                         | Description                     |
| --------------------------------------------------------------- | ------------------------------- |
| [`truss train init`](/reference/cli/training/training-cli#init) | Initialize a training project   |
| [`truss train push`](/reference/cli/training/training-cli#push) | Deploy and run a training job   |
| [`truss train logs`](/reference/cli/training/training-cli#logs) | Stream logs from a training job |
| [`truss train view`](/reference/cli/training/training-cli#view) | List and inspect training jobs  |

## Authentication

After installing Truss, authenticate with Baseten using either method:

**Option 1: Environment variable (recommended for CI/CD)**

```sh  theme={"system"}
export BASETEN_API_KEY="YOUR_API_KEY"
```

**Option 2: Interactive login**

```sh  theme={"system"}
truss login
```

This opens a browser window to authenticate and stores your credentials locally.

## Next steps

<CardGroup cols={2}>
  <Card title="Deploy your first model" icon="rocket" href="/examples/deploy-your-first-model">
    Package and deploy a model in minutes.
  </Card>

  <Card title="Build a Chain" icon="link" href="/development/chain/getting-started">
    Create multi-step inference pipelines.
  </Card>

  <Card title="Launch a training job" icon="dumbbell" href="/training/getting-started">
    Fine-tune models on Baseten infrastructure.
  </Card>

  <Card title="Truss configuration" icon="gear" href="/reference/truss-configuration">
    Configure dependencies, resources, and more.
  </Card>
</CardGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.baseten.co/llms.txt