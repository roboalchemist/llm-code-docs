# Source: https://docs.baseten.co/training/getting-started.md

# Source: https://docs.baseten.co/development/chain/getting-started.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Your first Chain

> Build and deploy two example Chains

This quickstart guide contains instructions for creating two Chains:

1. A simple CPU-only “hello world”-Chain.
2. A Chain that implements Phi-3 Mini and uses it to write poems.

## Prerequisites

To use Chains, install a recent Truss version and ensure pydantic is v2:

```bash  theme={"system"}
pip install --upgrade truss 'pydantic>=2.0.0'
```

<Accordion title="Help for setting up a clean development environment">
  Truss requires python `>=3.9,<3.15`. To set up a fresh development environment,
  you can use the following commands, creating a environment named `chains_env`
  using `pyenv`:

  ```bash  theme={"system"}
  curl https://pyenv.run | bash
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  echo 'eval "$(pyenv init -)"' >> ~/.bashrc
  source ~/.bashrc
  pyenv install 3.11.0
  ENV_NAME="chains_env"
  pyenv virtualenv 3.11.0 $ENV_NAME
  pyenv activate $ENV_NAME
  pip install --upgrade truss 'pydantic>=2.0.0'
  ```
</Accordion>

To deploy Chains remotely, you also need a
[Baseten account](https://app.baseten.co/signup).
It is handy to export your API key to the current shell session or permanently in your `.bashrc`:

```bash ~/.bashrc theme={"system"}
export BASETEN_API_KEY="nPh8..."
```

## Example: Hello World

Chains are written in Python files. In your working directory,
create `hello_chain/hello.py`:

```sh  theme={"system"}
mkdir hello_chain
cd hello_chain
touch hello.py
```

In the file, we'll specify a basic Chain. It has two Chainlets:

* `HelloWorld`, the entrypoint, which handles the input and output.
* `RandInt`, which generates a random integer. It is used a as a dependency
  by `HelloWorld`.

Via the entrypoint, the Chain takes a maximum value and returns the string "
Hello World!" repeated a
variable number of times.

```python hello.py theme={"system"}
import random
import truss_chains as chains


class RandInt(chains.ChainletBase):
    async def run_remote(self, max_value: int) -> int:
        return random.randint(1, max_value)


@chains.mark_entrypoint
class HelloWorld(chains.ChainletBase):
    def __init__(self, rand_int=chains.depends(RandInt, retries=3)) -> None:
        self._rand_int = rand_int

    async def run_remote(self, max_value: int) -> str:
        num_repetitions = await self._rand_int.run_remote(max_value)
        return "Hello World! " * num_repetitions
```

### The Chainlet class-contract

Exactly one Chainlet must be marked as the entrypoint with
the [`@chains.mark_entrypoint`](/reference/sdk/chains#truss-chains-mark-entrypoint)
decorator. This Chainlet is responsible for
handling public-facing input and output for the whole Chain in response to an
API call.

A Chainlet class has a single public method,
[`run_remote()`](/development/chain/concepts#run-remote-chaining-chainlets), which is
the API
endpoint for the entrypoint Chainlet and the function that other Chainlets can
use as a dependency. The
[`run_remote()`](/development/chain/concepts#run-remote-chaining-chainlets)
method must be fully type-annotated
with <Tooltip tip="E.g. `int`, `str`, `list[float]`">primitive python
types</Tooltip>
or <Tooltip tip="They have builtin JSON serialization.">[pydantic models](https://docs.pydantic.dev/latest/)</Tooltip>.

Chainlets cannot be <Tooltip tip="I.e. creating instances like `chainlet = RandInt()` in arbitrary locations in your code.">naively</Tooltip> instantiated. The only correct usages are:

1. Make one Chainlet depend on another one via the
   [`chains.depends()`](/reference/sdk/chains#truss-chains-depends) directive
   as an `__init__`-argument as shown above for the `RandInt` Chainlet.
2. In the [local debugging mode](/development/chain/localdev#test-a-chain-locally).

Beyond that, you can structure your code as you like, with private methods,
imports from other files, and so forth.

<Warning>
  Keep in mind that Chainlets are intended for distributed, replicated, remote
  execution, so using global variables, global state, and certain Python
  features like importing modules dynamically at runtime should be avoided as
  they may not work as intended.
</Warning>

### Deploy your Chain to Baseten

To deploy your Chain to Baseten, run:

```bash  theme={"system"}
truss chains push hello.py
```

The deploy command results in an output like this:

```
                  ⛓️   HelloWorld - Chainlets  ⛓️
╭──────────────────────┬─────────────────────────┬─────────────╮
│ Status               │ Name                    │ Logs URL    │
├──────────────────────┼─────────────────────────┼─────────────┤
│  💚 ACTIVE           │ HelloWorld (entrypoint) │ https://... │
├──────────────────────┼─────────────────────────┼─────────────┤
│  💚 ACTIVE           │ RandInt (dep)           │ https://... │
╰──────────────────────┴─────────────────────────┴─────────────╯
Deployment succeeded.
You can run the chain with:
curl -X POST 'https://chain-.../run_remote' \
    -H "Authorization: Api-Key $BASETEN_API_KEY" \
    -d '<JSON_INPUT>'
```

Wait for the status to turn to `ACTIVE` and test invoking your Chain (replace
`$INVOCATION_URL` in below command):

```bash  theme={"system"}
curl -X POST $INVOCATION_URL \
  -H "Authorization: Api-Key $BASETEN_API_KEY" \
  -d '{"max_value": 10}'
# "Hello World! Hello World! Hello World! "
```

## Example: Poetry with LLMs

Our second example also has two Chainlets, but is somewhat more complex and
realistic. The Chainlets are:

* `PoemGenerator`, the entrypoint, which handles the input and output and
  orchestrates calls to the LLM.
* `PhiLLM`, which runs inference on Phi-3 Mini.

This Chain takes a list of words and returns a poem about each word, written by
Phi-3. Here's the architecture:

<Frame>
  <img src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/poems.svg?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=f6d5826651ed54b5464edb18e21112d4" data-og-width="971" width="971" data-og-height="118" height="118" data-path="development/chain/images/poems.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/poems.svg?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=94a069566ed45a94e144cd5b5d82289e 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/poems.svg?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=fe60b7bdd7c7b113547a915c773aad60 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/poems.svg?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=1e8f723e57f205675dbfde2014e320a5 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/poems.svg?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=6cf0e32c25402c8628de88e29ff0b4f4 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/poems.svg?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=441a6836e2430a400929d66cd532f80c 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/poems.svg?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=f5ef9b81e5e444b95485c61a06b5e171 2500w" />
</Frame>

We build this Chain in a new working directory (if you are still inside
`hello_chain/`, go up one level with `cd ..` first):

```sh  theme={"system"}
mkdir poetry_chain
cd poetry_chain
touch poems.py
```

<Tip>
  A similar end-to-end code example, using Mistral as an LLM, is available in
  the [examples
  repo](https://github.com/basetenlabs/model/tree/main/truss-chains/examples/mistral).
</Tip>

### Building the LLM Chainlet

The main difference between this Chain and the previous one is that we now have
an LLM that needs a GPU and more complex dependencies.

Copy the following code into `poems.py`:

```python poems.py theme={"system"}
import asyncio
from typing import List

import pydantic
import truss_chains as chains
from truss import truss_config

PHI_HF_MODEL = "microsoft/Phi-3-mini-4k-instruct"
# This configures to cache model weights from the hunggingface repo
# in the docker image that is used for deploying the Chainlet.
PHI_CACHE = truss_config.ModelRepo(
    repo_id=PHI_HF_MODEL, allow_patterns=["*.json", "*.safetensors", ".model"]
)


class Messages(pydantic.BaseModel):
    messages: List[dict[str, str]]


class PhiLLM(chains.ChainletBase):
    # `remote_config` defines the resources required for this chainlet.
    remote_config = chains.RemoteConfig(
        docker_image=chains.DockerImage(
            # The phi model needs some extra python packages.
            pip_requirements=[
                "accelerate==0.30.1",
                "einops==0.8.0",
                "transformers==4.41.2",
                "torch==2.3.0",
            ]
        ),
        # The phi model needs a GPU and more CPUs.
        compute=chains.Compute(cpu_count=2, gpu="T4"),
        # Cache the model weights in the image
        assets=chains.Assets(cached=[PHI_CACHE]),
    )

    def __init__(self) -> None:
        # Note the imports of the *specific* python requirements are
        # pushed down to here. This code will only be executed on the
        # remotely deployed Chainlet, not in the local environment,
        # so we don't need to install these packages in the local
        # dev environment.
        import torch
        import transformers

        self._model = transformers.AutoModelForCausalLM.from_pretrained(
            PHI_HF_MODEL,
            torch_dtype=torch.float16,
            device_map="auto",
        )
        self._tokenizer = transformers.AutoTokenizer.from_pretrained(
            PHI_HF_MODEL,
        )
        self._generate_args = {
            "max_new_tokens"      : 512,
            "temperature"         : 1.0,
            "top_p"               : 0.95,
            "top_k"               : 50,
            "repetition_penalty"  : 1.0,
            "no_repeat_ngram_size": 0,
            "use_cache"           : True,
            "do_sample"           : True,
            "eos_token_id"        : self._tokenizer.eos_token_id,
            "pad_token_id"        : self._tokenizer.pad_token_id,
        }

    async def run_remote(self, messages: Messages) -> str:
        import torch

        model_inputs = self._tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = self._tokenizer(model_inputs, return_tensors="pt")
        input_ids = inputs["input_ids"].to("cuda")
        with torch.no_grad():
            outputs = self._model.generate(
                input_ids=input_ids, **self._generate_args)
            output_text = self._tokenizer.decode(
                outputs[0], skip_special_tokens=True)
        return output_text
```

### Building the entrypoint

Now that we have an LLM, we can use it in a poem generator Chainlet. Add the
following code to `poems.py`:

```python poems.py theme={"system"}
import asyncio


@chains.mark_entrypoint
class PoemGenerator(chains.ChainletBase):
    def __init__(self, phi_llm: PhiLLM = chains.depends(PhiLLM)) -> None:
        self._phi_llm = phi_llm

    async def run_remote(self, words: list[str]) -> list[str]:
        tasks = []
        for word in words:
            messages = Messages(
                messages=[
                    {
                        "role"   : "system",
                        "content": (
                            "You are poet who writes short, "
                            "lighthearted, amusing poetry."
                        ),
                    },
                    {"role": "user", "content": f"Write a poem about {word}"},
                ]
            )
            tasks.append(
                asyncio.ensure_future(self._phi_llm.run_remote(messages)))
            await asyncio.sleep(0)  # Yield to event loop, to allow starting tasks.

        return list(await asyncio.gather(*tasks))
```

Note that we use `asyncio.ensure_future` around each RPC to the LLM chainlet.
This makes the current python process start these remote calls concurrently,
i.e. the next call is started before the previous one has finished and we can
minimize our overall runtime. In order to await the results of all calls,
`asyncio.gather` is used which gives us back normal python objects.
If the LLM is hit with many concurrent requests, it can auto-scale up (if
autoscaling is configured). More advanced LLM models have batching capabilities,
so for those even a single instance can serve concurrent request.

### Deploy your Chain to Baseten

To deploy your Chain to Baseten, run:

```bash  theme={"system"}
truss chains push poems.py
```

Wait for the status to turn to `ACTIVE` and test invoking your Chain (replace
`$INVOCATION_URL` in below command):

```bash  theme={"system"}
curl -X POST $INVOCATION_URL \
    -H "Authorization: Api-Key $BASETEN_API_KEY" \
    -d '{"words": ["bird", "plane", "superman"]}'
#[[
#"<s> [INST] Generate a poem about: bird [/INST] In the quiet hush of...</s>",
#"<s> [INST] Generate a poem about: plane [/INST] In the vast, boundless...</s>",
#"<s> [INST] Generate a poem about: superman [/INST] In the realm where...</s>"
#]]
```
