# Source: https://docs.baseten.co/development/chain/engine-builder-models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Engine-Builder LLM Models

> Engine-Builder LLM models are pre-trained models that are optimized for specific inference tasks.

Baseten's [Engine-Builder](/engines/engine-builder-llm/overview) enables the deployment of optimized model inference engines. Currently, it supports TensorRT-LLM. Truss Chains allows seamless integration of these engines into structured workflows. This guide provides a quick entry point for Chains users.

## LLama 7B Example

Use the `EngineBuilderLLMChainlet` baseclass to configure an LLM engine. The additional `engine_builder_config` field specifies model architecture, repository, and engine parameters and more, the full options are detailed in the [Engine-Builder configuration guide](/engines/engine-builder-llm/engine-builder-config).

```python  theme={"system"}
import truss_chains as chains
from truss.base import trt_llm_config, truss_config

class Llama7BChainlet(chains.EngineBuilderLLMChainlet):
    remote_config = chains.RemoteConfig(
        compute=chains.Compute(gpu=truss_config.Accelerator.H100),
        assets=chains.Assets(secret_keys=["hf_access_token"]),
    )
    engine_builder_config = truss_config.TRTLLMConfiguration(
        build=trt_llm_config.TrussTRTLLMBuildConfiguration(
            base_model=trt_llm_config.TrussTRTLLMModel.LLAMA,
            checkpoint_repository=trt_llm_config.CheckpointRepository(
                source=trt_llm_config.CheckpointSource.HF,
                repo="meta-llama/Llama-3.1-8B-Instruct",
            ),
            max_batch_size=8,
            max_seq_len=4096,
            tensor_parallel_count=1,
        )
    )
```

## Differences from Standard Chainlets

* No `run_remote` implementation: Unlike regular Chainlets, `EngineBuilderLLMChainlet` does not require users to implement `run_remote()`. Instead, it automatically wires into the deployed engine’s API. All LLM Chainlets have the same function signature: `chains.EngineBuilderLLMInput` as input and a stream (`AsyncIterator`) of strings as output. Likewise `EngineBuilderLLMChainlet`s can only be used as dependencies, but not have dependencies themselves.
* No `run_local` ([guide](/development/chain/localdev)) and `watch` ([guide](/development/chain/watch)) Standard Chains support a local debugging mode and watch. However, when using `EngineBuilderLLMChainlet`, local execution is not available, and testing must be done after deployment.
  For a faster dev loop of the rest of your chain (everything except the engine builder chainlet) you can substitute those chainlets with stubs like you can do for an already deployed truss model \[[guide](/development/chain/stub)].

## Integrate the Engine-Builder Chainlet

After defining an `EngineBuilderLLMInput` like `Llama7BChainlet` above, you can use it as a dependency in other conventional chainlets:

```python  theme={"system"}
from typing import AsyncIterator
import truss_chains as chains

@chains.mark_entrypoint
class TestController(chains.ChainletBase):
    """Example using the Engine-Builder Chainlet in another Chainlet."""

    def __init__(self, llm=chains.depends(Llama7BChainlet)) -> None:
        self._llm = llm

    async def run_remote(self, prompt: str) -> AsyncIterator[str]:
        messages = [{"role": "user", "content": prompt}]
        llm_input = chains.EngineBuilderLLMInput(messages=messages)
        async for chunk in self._llm.run_remote(llm_input):
            yield chunk
```
