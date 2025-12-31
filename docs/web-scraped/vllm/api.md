# Source: https://docs.vllm.ai/en/stable/api/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/api/README.md "Edit this page")

# Summary[¶](#summary "Permanent link")

## Configuration[¶](#configuration "Permanent link")

API documentation for vLLM\'s configuration classes.

-   [vllm.config.ModelConfig](vllm/config/#vllm.config.ModelConfig "            ModelConfig")
-   [vllm.config.CacheConfig](vllm/config/#vllm.config.CacheConfig "            CacheConfig")
-   [vllm.config.LoadConfig](vllm/config/#vllm.config.LoadConfig "            LoadConfig")
-   [vllm.config.ParallelConfig](vllm/config/#vllm.config.ParallelConfig "            ParallelConfig")
-   [vllm.config.SchedulerConfig](vllm/config/#vllm.config.SchedulerConfig "            SchedulerConfig")
-   [vllm.config.DeviceConfig](vllm/config/#vllm.config.DeviceConfig "            DeviceConfig")
-   [vllm.config.SpeculativeConfig](vllm/config/#vllm.config.SpeculativeConfig "            SpeculativeConfig")
-   [vllm.config.LoRAConfig](vllm/config/#vllm.config.LoRAConfig "            LoRAConfig")
-   [vllm.config.MultiModalConfig](vllm/config/#vllm.config.MultiModalConfig "            MultiModalConfig")
-   [vllm.config.PoolerConfig](vllm/config/#vllm.config.PoolerConfig "            PoolerConfig")
-   [vllm.config.StructuredOutputsConfig](vllm/config/#vllm.config.StructuredOutputsConfig "            StructuredOutputsConfig")
-   [vllm.config.ProfilerConfig](vllm/config/#vllm.config.ProfilerConfig "            ProfilerConfig")
-   [vllm.config.ObservabilityConfig](vllm/config/#vllm.config.ObservabilityConfig "            ObservabilityConfig")
-   [vllm.config.KVTransferConfig](vllm/config/#vllm.config.KVTransferConfig "            KVTransferConfig")
-   [vllm.config.CompilationConfig](vllm/config/#vllm.config.CompilationConfig "            CompilationConfig")
-   [vllm.config.VllmConfig](vllm/config/#vllm.config.VllmConfig "            VllmConfig")

## Offline Inference[¶](#offline-inference "Permanent link")

LLM Class.

-   [vllm.LLM](vllm/#vllm.LLM "            LLM")

LLM Inputs.

-   [vllm.inputs.PromptType](vllm/inputs/#vllm.inputs.PromptType "            PromptType

      
          module-attribute
      ")
-   [vllm.inputs.TextPrompt](vllm/inputs/#vllm.inputs.TextPrompt "            TextPrompt")
-   [vllm.inputs.TokensPrompt](vllm/inputs/#vllm.inputs.TokensPrompt "            TokensPrompt")

## vLLM Engines[¶](#vllm-engines "Permanent link")

Engine classes for offline and online inference.

-   [vllm.LLMEngine](vllm/#vllm.LLMEngine "            LLMEngine

      
          module-attribute
      ")
-   [vllm.AsyncLLMEngine](vllm/#vllm.AsyncLLMEngine "            AsyncLLMEngine

      
          module-attribute
      ")

## Inference Parameters[¶](#inference-parameters "Permanent link")

Inference parameters for vLLM APIs.

-   [vllm.SamplingParams](vllm/#vllm.SamplingParams "            SamplingParams")
-   [vllm.PoolingParams](vllm/#vllm.PoolingParams "            PoolingParams")

## Multi-Modality[¶](#multi-modality "Permanent link")

vLLM provides experimental support for multi-modal models through the [vllm.multimodal](vllm/multimodal/#vllm.multimodal "            vllm.multimodal") package.

Multi-modal inputs can be passed alongside text and token prompts to [supported models](../models/supported_models/#list-of-multimodal-language-models) via the `multi_modal_data` field in [vllm.inputs.PromptType](vllm/inputs/#vllm.inputs.PromptType "            PromptType

  
      module-attribute
  ").

Looking to add your own multi-modal model? Please follow the instructions listed [here](../contributing/model/multimodal/).

-   [vllm.multimodal.MULTIMODAL_REGISTRY](vllm/multimodal/#vllm.multimodal.MULTIMODAL_REGISTRY "            MULTIMODAL_REGISTRY

      
          module-attribute
      ")

### Inputs[¶](#inputs "Permanent link")

User-facing inputs.

-   [vllm.multimodal.inputs.MultiModalDataDict](vllm/multimodal/inputs/#vllm.multimodal.inputs.MultiModalDataDict "            MultiModalDataDict

      
          module-attribute
      ")

Internal data structures.

-   [vllm.multimodal.inputs.PlaceholderRange](vllm/multimodal/inputs/#vllm.multimodal.inputs.PlaceholderRange "            PlaceholderRange

      
          dataclass
      ")
-   [vllm.multimodal.inputs.NestedTensors](vllm/multimodal/inputs/#vllm.multimodal.inputs.NestedTensors "            NestedTensors

      
          module-attribute
      ")
-   [vllm.multimodal.inputs.MultiModalFieldElem](vllm/multimodal/inputs/#vllm.multimodal.inputs.MultiModalFieldElem "            MultiModalFieldElem

      
          dataclass
      ")
-   [vllm.multimodal.inputs.MultiModalFieldConfig](vllm/multimodal/inputs/#vllm.multimodal.inputs.MultiModalFieldConfig "            MultiModalFieldConfig

      
          dataclass
      ")
-   [vllm.multimodal.inputs.MultiModalKwargsItem](vllm/multimodal/inputs/#vllm.multimodal.inputs.MultiModalKwargsItem "            MultiModalKwargsItem")
-   [vllm.multimodal.inputs.MultiModalKwargsItems](vllm/multimodal/inputs/#vllm.multimodal.inputs.MultiModalKwargsItems "            MultiModalKwargsItems")
-   [vllm.multimodal.inputs.MultiModalKwargs](vllm/multimodal/inputs/#vllm.multimodal.inputs.MultiModalKwargs "            MultiModalKwargs")
-   [vllm.multimodal.inputs.MultiModalInputs](vllm/multimodal/inputs/#vllm.multimodal.inputs.MultiModalInputs "            MultiModalInputs")

### Data Parsing[¶](#data-parsing "Permanent link")

-   [vllm.multimodal.parse](vllm/multimodal/parse/#vllm.multimodal.parse "            vllm.multimodal.parse")

### Data Processing[¶](#data-processing "Permanent link")

-   [vllm.multimodal.processing](vllm/multimodal/processing/#vllm.multimodal.processing "            vllm.multimodal.processing")

### Memory Profiling[¶](#memory-profiling "Permanent link")

-   [vllm.multimodal.profiling](vllm/multimodal/profiling/#vllm.multimodal.profiling "            vllm.multimodal.profiling")

### Registry[¶](#registry "Permanent link")

-   [vllm.multimodal.registry](vllm/multimodal/registry/#vllm.multimodal.registry "            vllm.multimodal.registry")

## Model Development[¶](#model-development "Permanent link")

-   [vllm.model_executor.models.interfaces_base](vllm/model_executor/models/interfaces_base/#vllm.model_executor.models.interfaces_base "            vllm.model_executor.models.interfaces_base")
-   [vllm.model_executor.models.interfaces](vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces "            vllm.model_executor.models.interfaces")
-   [vllm.model_executor.models.adapters](vllm/model_executor/models/adapters/#vllm.model_executor.models.adapters "            vllm.model_executor.models.adapters")

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [December 9, 2025] ]