# Source: https://docs.baseten.co/development/model/build-your-first-model.md

# Your first model

> Build and deploy your first model

This quickstart guide shows you how to build and deploy your first model,
using Baseten's Truss framework.

## Prerequisites

To use Truss, install a recent Truss version and ensure pydantic is v2:

```bash  theme={"system"}
pip install --upgrade truss 'pydantic>=2.0.0'
```

<Accordion title="Help for setting up a clean development environment">
  Truss requires python `>=3.8,<3.13`. To set up a fresh development environment,
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

## Initialize your model

Truss is a tool that helps you package your model code and configuration, and ship it to Baseten for deployment, testing, and scaling.

To create your first model, you can use the `truss init` command.

```bash  theme={"system"}
$ truss init hello-world
? 📦 Name this model: HelloWorld
Truss HelloWorld was created in ~/hello-world
```

This will create a new directory called `hello-world` with the following files:

* `config.yaml` - A configuration file for your model.
* `model/model.py` - A Python file that contains your model code
* `packages/` - A folder to hold any dependencies your model needs
* `data/` - A folder to hold any data your model needs

For this example, we'll focus on the `config.yaml` file and the `model.py` file.

### `config.yaml`

The `config.yaml` file is used to configure dependencies, resources, and
other settings for your model.

Let's take a look at the contents:

```yaml config.yaml theme={"system"}
build_commands: []
environment_variables: {}
external_package_dirs: []
model_metadata: {}
model_name: HelloWorld
python_version: py311
requirements: []
resources:
  accelerator: null
  cpu: '1'
  memory: 2Gi
  use_gpu: false
secrets: {}
system_packages: []
```

Some key fields to note:

* `requirements`: This is a list of `pip` packages that will be installed when
  your model is deployed.
* `resources`: This is where you can specify the resources your model will use.
* `secrets`: This is where you can specify any secrets your model will need, such as
  HuggingFace API keys.

See the [Configuration](/development/model/configuration) page for more information on the `config.yaml` file.

### `model.py`

Next, let's take a look at the `model.py` file.

```python  theme={"system"}
class Model:
    def __init__(self, **kwargs):
        pass

    def load(self):
        pass

    def predict(self, model_input):
        return model_input 
```

In Truss models, we expect users to provide a Python class with the following methods:

* `__init__`: This is the constructor.
* `load`: This is called at model startup, and should include any setup logic, such as weight downloading or initialization
* `predict`: This is the method that is called during inference.

## Deploy your model

To deploy your model, you can use the `truss push` command.

```bash  theme={"system"}
$ truss push
```

This will deploy your model to Baseten.

## Invoke your model

After deploying your model, you can invoke it with the invocation URL provided:

```bash  theme={"system"}
$ curl -X POST https://model-{model-id}.api.baseten.co/development/predict \
  -H "Authorization: Api-Key $BASETEN_API_KEY" \
  -d '"some text"'
"some text"
```

## A Real Example

To show a slightly more complex example, let's deploy a text classification model
from HuggingFace!

In this example, we'll use the `transformers` library to load a pre-trained model,
from HuggingFace, and use it to classify the given text.

### `config.yaml`

To deploy this model, we need to add a few more dependencies to our `config.yaml` file.

```yaml config.yaml theme={"system"}
requirements:
  - transformers
  - torch
```

### `model.py`

Next, let's change our `model.py` file to use the `transformers` library to load the model,
and then use it to predict the sentiment of a given text.

```python model.py theme={"system"}
from transformers import pipeline

class Model:
    def __init__(self, **kwargs):
        pass

    def load(self):
        self._model = pipeline("text-classification")

    def predict(self, model_input):
        return self._model(model_input)
```

## Running inference

Similarly to our previous example, we can deploy this model using `truss push`

```bash  theme={"system"}
$ truss push
```

And then invoke it using the invocation URL on Baseten.

```bash  theme={"system"}
$ curl -X POST https://model-{model-id}.api.baseten.co/development/predict \
  -H "Authorization: Api-Key $BASETEN_API_KEY" \
  -d '{"text": "some text"}'
```

## Next steps

Now that you've deployed your first model, you can learn more about more
options for [configuring your model](/development/model/configuration),
and [implementing your model](/development/model/implementation).
