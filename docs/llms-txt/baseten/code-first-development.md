# Source: https://docs.baseten.co/development/model/code-first-development.md

# Python driven configuration for models 🆕

> Use code-first development tools to streamline model production.

<Info> This feature is still in beta. </Info>

In addition to our normal YAML configuration, we support configuring your model using pure Python. This offers the following benefits:

* **Typed configuration via Python code** with IDE autocomplete, instead of a separate `yaml` configuration file
* **Simpler directory structure** that IDEs support for module resolution

In this guide, we go through deploying a simple Model using this new framework.

### Step 1: Initializing your project

We leverage traditional `truss init` functionality with a new flag to create the directory structure:

```bash  theme={"system"}
truss init my-new-model --python-config
```

### Step 2: Write your model

To build a model with this new framework, we require two things:

* A class that inherits from `baseten.ModelBase`, which will serve as the entrypoint when invoking `/predict`
* A `predict` method with type hints

That’s it! The following is a contrived example of a complete model that will keep a running total of user provided input:

```python my_model.py theme={"system"}
import truss_chains as baseten


class RunningTotalCalculator(baseten.ModelBase):
    def __init__(self):
        self._running_total = 0

    async def predict(self, increment: int) -> int:
        self._running_total += increment
        return self._running_total
```

### Step 3: Deploy, patch, and public your model

In order to deploy the first version of your new model, you can run:

```bash  theme={"system"}
truss push my_model.py
```

Please note that `push` (as well as all other commands below) will require that you pass the path to the file containing the model as the final argument.

This new workflow also supports patching, so you can quickly iterate during development without building new images every time.

```bash  theme={"system"}
truss watch my_model.py
```

### Model Configuration

Models can configure requirements for compute hardware (CPU count, GPU type and count, etc) and software dependencies (Python libraries or system packages) via the [`remote_config`](/reference/sdk/chains#remote-configuration) class variable within the model:

```python my_model.py theme={"system"}
class RunningTotalCalculator(baseten.ModelBase):
    remote_config: baseten.RemoteConfig = baseten.RemoteConfig(
        compute=baseten.Compute(cpu_count=4, memory="1Gi", gpu="T4", gpu_count=2)
    )

    ...
```

See the [remote configuration reference](/reference/sdk/chains#remote-configuration) for a complete list of options.

### Context (access information)

You can add [`DeploymentContext`](/reference/sdk/chains#class-truss-chains-deploymentcontext) object as an optional final argument to the **`__init__`**-method of a Model. This allows you to use secrets within your Model, but note that they’ll also need to be added to the **`assets`**.

We only expose secrets to the model that were explicitly requested in `assets` to comply with best security practices.

```python my_model.py theme={"system"}
class RunningTotalCalculator(baseten.ModelBase):
    remote_config: baseten.RemoteConfig = baseten.RemoteConfig(
        ...
        assets=baseten.Assets(secret_keys=["token"])
    )

    def __init__(self, context: baseten.DeploymentContext = baseten.depends_context()):
        ...
        self._token = context.secrets["token"]

```

### Packages

If you want to include modules in your model, you can easily create them from the root of the project:

```bash  theme={"system"}
my-new-model/
    module_1/
	    submodule/
		    script.py
    module_2/
	    another_script.py
    my_model.py
```

With this file structure, you would import in `my_model.py` as follows:

```python my_model.py theme={"system"}
import truss_chains as baseten

from module_1.submodule import script
from module_2 import another_script

class RunningTotalCalculator(baseten.ModelBase):
    ....
```

### Known Limitations

* RemoteConfig does *not* support all the options exposed by the traditional `config.yaml`. If you’re excited about this new development experience but need a specific feature ported over, please reach out to us!
* This new framework does not support `preprocess` or `postprocess` hooks. We typically recommend inlining functionality from those functions if easy, or utilizing `chains` if the needs are more complex.
