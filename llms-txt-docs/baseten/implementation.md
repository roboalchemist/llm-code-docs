# Source: https://docs.baseten.co/development/model/implementation.md

# Implementation

> How to implement your model.

In this section, we'll cover how to implement the actual logic for your model.

As was mentioned in [Your First Model](/development/model/build-your-first-model), the
logic for the model itself is specified in a `model/model.py` file. To recap, the simplest
directory structure for a model is:

```
model/
  model.py
config.yaml
```

It's expected that the `model.py` file contains a class with particular methods:

```python model.py theme={"system"}
class Model:
  def __init__(self):
    pass

  def load(self):
    pass

  def predict(self, input_data):
    pass
```

* The `__init__` method is used to initialize the `Model` class, and allows you to read
  in configuration parameters and other information.
* The `load` method is where you define the logic for initializing the model. This might
  include downloading model weights, or loading them onto a GPU.
* The `predict` method is where you define the logic for inference.

In the next sections, we'll cover each of these methods in more detail.

## **init**

As mentioned above, the `__init__` method is used to initialize the `Model` class, and allows you to
read in configuration parameters and runtime information.

The simplest signature for `__init__` is:

```python model.py theme={"system"}
def __init__(self):
  pass
```

If you need more information, however, you have the option to define your **init** method
such that it accepts the following parameters:

```python model.py theme={"system"}
def __init__(self, config: dict, data_dir: str, secrets: dict, environment: str):
  pass
```

* `config`: A dictionary containing the config.yaml for the model.
* `data_dir`: A string containing the path to the data directory for the model.
* `secrets`: A dictionary containing the secrets for the model. Note that at runtime,
  these will be populated with the actual values as stored on Baseten.
* `environment`: A string containing the environment for the model, if the model has been
  deployed to an environment.

You can then make use of these parameters in the rest of your model but saving these as
attributes:

```python model.py theme={"system"}
def __init__(self, config: dict, data_dir: str, secrets: dict, environment: str):
  self._config = config
  self._data_dir = data_dir
  self._secrets = secrets
  self._environment = environment
```

## load

The `load` method is where you define the logic for initializing the model. As
mentioned before, this might include downloading model weights or loading them
onto the GPU.

`load`, unlike the other method mentioned, does not accept any parameters:

```python model.py theme={"system"}
def load(self):
  pass
```

After deploying your model, the deployment will not be considered "Ready" until `load` has
completed successfully. Note that there is a **timeout of 30 minutes** for this, after which,
if `load` has not completed, the deployment will be marked as failed.

## predict

The `predict` method is where you define the logic for performing inference.

The simplest signature for `predict` is:

```python model.py theme={"system"}
def predict(self, input_data) -> str:
  return "Hello"
```

The return type of `predict` must be JSON-serializable, so it can be:

* `dict`
* `list`
* `str`

If you would like to return a more strictly typed object, you can return a
`Pydantic` object.

```python model.py theme={"system"}
from pydantic import BaseModel

class Result(BaseModel):
  value: str
```

You can then return an instance of this model from `predict`:

```python model.py theme={"system"}
def predict(self, input_data) -> Prediction:
  return Result(value="Hello")
```

### Streaming

In addition to supporting a single request/response cycle, Truss also supports streaming.

See the [Streaming](/development/model/streaming) guide for more information.

### Async vs. Sync

Note that the `predict` method is synchronous by default. However, if your model inference
depends on APIs require `asyncio`, `predict` can also be written as a coroutine.

```python model.py theme={"system"}
import asyncio

async def predict(self, input_data) -> dict:
    # Async logic here

    await asyncio.sleep(1)
    return {"value": "Hello"}
```

<Warning>
  If you are using `asyncio` in your `predict` method, be sure not to perform any blocking
  operations, such as a synchronous file download. This can result in degraded performance.
</Warning>
