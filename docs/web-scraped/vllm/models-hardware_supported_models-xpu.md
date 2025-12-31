# Source: https://docs.vllm.ai/en/stable/models/hardware_supported_models/xpu/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/models/hardware_supported_models/xpu.md "Edit this page")

# XPU - Intel® GPUs[¶](#xpu-intel-gpus "Permanent link") 

## Validated Hardware[¶](#validated-hardware "Permanent link")

  Hardware
  --------------------------------------------------------------------------------------------------------------------------------------------------
  [Intel® Arc™ Pro B-Series Graphics](https://www.intel.com/content/www/us/en/products/docs/discrete-gpus/arc/workstations/b-series/overview.html)

## Supported Models[¶](#supported-models "Permanent link")

### Text-only Language Models[¶](#text-only-language-models "Permanent link")

  Model                                       Architecture                                       FP16   Dynamic FP8   MXFP4
  ------------------------------------------- -------------------------------------------------- ------ ------------- -------
  openai/gpt-oss-20b                          GPTForCausalLM                                                          ✅
  openai/gpt-oss-120b                         GPTForCausalLM                                                          ✅
  deepseek-ai/DeepSeek-R1-Distill-Llama-8B    LlamaForCausalLM                                   ✅     ✅            
  deepseek-ai/DeepSeek-R1-Distill-Qwen-14B    QwenForCausalLM                                    ✅     ✅            
  deepseek-ai/DeepSeek-R1-Distill-Qwen-32B    QwenForCausalLM                                    ✅     ✅            
  deepseek-ai/DeepSeek-R1-Distill-Llama-70B   LlamaForCausalLM                                   ✅     ✅            
  Qwen/Qwen2.5-72B-Instruct                   Qwen2ForCausalLM                                   ✅     ✅            
  Qwen/Qwen3-14B                              Qwen3ForCausalLM                                   ✅     ✅            
  Qwen/Qwen3-32B                              Qwen3ForCausalLM                                   ✅     ✅            
  Qwen/Qwen3-30B-A3B                          Qwen3ForCausalLM                                   ✅     ✅            
  Qwen/Qwen3-30B-A3B-GPTQ-Int4                Qwen3ForCausalLM                                   ✅     ✅            
  Qwen/Qwen3-coder-30B-A3B-Instruct           Qwen3ForCausalLM                                   ✅     ✅            
  Qwen/QwQ-32B                                QwenForCausalLM                                    ✅     ✅            
  deepseek-ai/DeepSeek-V2-Lite                DeepSeekForCausalLM                                ✅     ✅            
  meta-llama/Llama-3.1-8B-Instruct            LlamaForCausalLM                                   ✅     ✅            
  baichuan-inc/Baichuan2-13B-Chat             BaichuanForCausalLM                                ✅     ✅            
  THUDM/GLM-4-9B-chat                         GLMForCausalLM                                     ✅     ✅            
  THUDM/CodeGeex4-All-9B                      CodeGeexForCausalLM                                ✅     ✅            
  chuhac/TeleChat2-35B                        LlamaForCausalLM (TeleChat2 based on Llama arch)   ✅     ✅            
  01-ai/Yi1.5-34B-Chat                        YiForCausalLM                                      ✅     ✅            
  THUDM/CodeGeex4-All-9B                      CodeGeexForCausalLM                                ✅     ✅            
  deepseek-ai/DeepSeek-Coder-33B-base         DeepSeekCoderForCausalLM                           ✅     ✅            
  baichuan-inc/Baichuan2-13B-Chat             BaichuanForCausalLM                                ✅     ✅            
  meta-llama/Llama-2-13b-chat-hf              LlamaForCausalLM                                   ✅     ✅            
  THUDM/CodeGeex4-All-9B                      CodeGeexForCausalLM                                ✅     ✅            
  Qwen/Qwen1.5-14B-Chat                       QwenForCausalLM                                    ✅     ✅            
  Qwen/Qwen1.5-32B-Chat                       QwenForCausalLM                                    ✅     ✅            

### Multimodal Language Models[¶](#multimodal-language-models "Permanent link")

  Model                          Architecture                       FP16   Dynamic FP8   MXFP4
  ------------------------------ ---------------------------------- ------ ------------- -------
  OpenGVLab/InternVL3_5-8B       InternVLForConditionalGeneration   ✅     ✅            
  OpenGVLab/InternVL3_5-14B      InternVLForConditionalGeneration   ✅     ✅            
  OpenGVLab/InternVL3_5-38B      InternVLForConditionalGeneration   ✅     ✅            
  Qwen/Qwen2-VL-7B-Instruct      Qwen2VLForConditionalGeneration    ✅     ✅            
  Qwen/Qwen2.5-VL-72B-Instruct   Qwen2VLForConditionalGeneration    ✅     ✅            
  Qwen/Qwen2.5-VL-32B-Instruct   Qwen2VLForConditionalGeneration    ✅     ✅            
  THUDM/GLM-4v-9B                GLM4vForConditionalGeneration      ✅     ✅            
  openbmb/MiniCPM-V-4            MiniCPMVForConditionalGeneration   ✅     ✅            

### Embedding and Reranker Language Models[¶](#embedding-and-reranker-language-models "Permanent link")

  Model                     Architecture                     FP16   Dynamic FP8   MXFP4
  ------------------------- -------------------------------- ------ ------------- -------
  Qwen/Qwen3-Embedding-8B   Qwen3ForTextEmbedding            ✅     ✅            
  Qwen/Qwen3-Reranker-8B    Qwen3ForSequenceClassification   ✅     ✅            

✅ Runs and optimized.\
🟨 Runs and correct but not optimized to green yet.\
❌ Does not pass accuracy test or does not run.

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [November 27, 2025] ]