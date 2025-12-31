# Source: https://docs.vllm.ai/en/stable/models/hardware_supported_models/cpu/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/models/hardware_supported_models/cpu.md "Edit this page")

# CPU - Intel® Xeon®[¶](#cpu-intel-xeon "Permanent link") 

## Validated Hardware[¶](#validated-hardware "Permanent link")

  Hardware
  ------------------------------------------------------------------------------------------------------------------------------------------
  [Intel® Xeon® 6 Processors](https://www.intel.com/content/www/us/en/products/details/processors/xeon.html)
  [Intel® Xeon® 5 Processors](https://www.intel.com/content/www/us/en/products/docs/processors/xeon/5th-gen-xeon-scalable-processors.html)

## Supported Models[¶](#supported-models "Permanent link")

### Text-only Language Models[¶](#text-only-language-models "Permanent link")

  Model                                 Architecture         Supported
  ------------------------------------- -------------------- -----------
  meta-llama/Llama-3.1-8B-Instruct      LlamaForCausalLM     ✅
  meta-llama/Llama-3.2-3B-Instruct      LlamaForCausalLM     ✅
  ibm-granite/granite-3.2-2b-instruct   GraniteForCausalLM   ✅
  Qwen/Qwen3-1.7B                       Qwen3ForCausalLM     ✅
  Qwen/Qwen3-4B                         Qwen3ForCausalLM     ✅
  Qwen/Qwen3-8B                         Qwen3ForCausalLM     ✅
  zai-org/glm-4-9b-hf                   GLMForCausalLM       ✅
  google/gemma-7b                       GemmaForCausalLM     ✅

### Multimodal Language Models[¶](#multimodal-language-models "Permanent link")

  Model                         Architecture                      Supported
  ----------------------------- --------------------------------- -----------
  Qwen/Qwen2.5-VL-7B-Instruct   Qwen2VLForConditionalGeneration   ✅
  openai/whisper-large-v3       WhisperForConditionalGeneration   ✅

✅ Runs and optimized.\
🟨 Runs and correct but not optimized to green yet.\
❌ Does not pass accuracy test or does not run.

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [November 27, 2025] ]