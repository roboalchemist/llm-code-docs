# Source: https://docs.together.ai/docs/fine-tuning-models.md

# Supported Models

> A list of all the models available for fine-tuning.

The following models are available to use with our fine-tuning API. Get started with [fine-tuning a model](/docs/fine-tuning-quickstart)!

**Note:** This list is different from the models that support Serverless LoRA inference, which allows you to perform LoRA fine-tuning and run inference immediately. See the [LoRA inference page](/docs/lora-training-and-inference#supported-base-models) for the list of supported base models for serverless LoRA.

**Important:** When uploading LoRA adapters for serverless inference, you must use base models from the serverless LoRA list, not the fine-tuning models list. Using an incompatible base model (such as Turbo variants) will result in a "No lora\_model specified" error during upload. For example, use `meta-llama/Meta-Llama-3.1-8B-Instruct-Reference` instead of `meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo` for serverless LoRA adapters.

* *Training Precision Type* indicates the precision type used during training for each model.

  * AMP (Automated Mixed Precision): AMP allows the training speed to be faster with less memory usage while preserving convergence behavior compared to using float32. Learn more about AMP in [this PyTorch blog](https://pytorch.org/blog/what-every-user-should-know-about-mixed-precision-training-in-pytorch/).
  * bf16 (bfloat 16): This uses bf16 for all weights. Some large models on our platform use full bf16 training for better memory usage and training speed.

* For batch sizes of 1, Gradient accumulation 8 is used, so effectively you will get batch size 8 (iteration time is slower).

* Long-context fine-tuning of Llama 3.1 (8B) Reference, Llama 3.1 (70B) Reference, Llama 3.1 Instruct (70B) Reference for context sizes of 32K-131K is only supported using the LoRA method.

* For Llama 3.1 (405B) Fine-tuning, please [contact us](https://www.together.ai/forms/contact-sales?prod_source=405B).

*[Request a model](https://www.together.ai/forms/model-requests)*

## LoRA Fine-tuning

| Organization | Model Name                                 | Model String for API                                  | Context Length (SFT) | Context Length (DPO) | Max Batch Size (SFT) | Max Batch Size (DPO) | Min Batch Size |
| ------------ | ------------------------------------------ | ----------------------------------------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------- |
| OpenAI       | gpt-oss-20b                                | openai/gpt-oss-20b                                    | 16384                | 8192                 | 8                    | 8                    | 8              |
| OpenAI       | gpt-oss-120b                               | openai/gpt-oss-120b                                   | 16384                | 8192                 | 16                   | 16                   | 16             |
| DeepSeek     | DeepSeek-R1-0528                           | deepseek-ai/DeepSeek-R1-0528                          | 131072               | 32768                | 1                    | 1                    | 2              |
| DeepSeek     | DeepSeek-R1                                | deepseek-ai/DeepSeek-R1                               | 131072               | 32768                | 1                    | 1                    | 2              |
| DeepSeek     | DeepSeek-V3.1                              | deepseek-ai/DeepSeek-V3.1                             | 131072               | 32768                | 1                    | 1                    | 2              |
| DeepSeek     | DeepSeek-V3-0324                           | deepseek-ai/DeepSeek-V3-0324                          | 131072               | 32768                | 1                    | 1                    | 2              |
| DeepSeek     | DeepSeek-V3                                | deepseek-ai/DeepSeek-V3                               | 131072               | 32768                | 1                    | 1                    | 2              |
| DeepSeek     | DeepSeek-V3.1-Base                         | deepseek-ai/DeepSeek-V3.1-Base                        | 131072               | 32768                | 1                    | 1                    | 2              |
| DeepSeek     | DeepSeek-V3-Base                           | deepseek-ai/DeepSeek-V3-Base                          | 131072               | 32768                | 1                    | 1                    | 2              |
| DeepSeek     | DeepSeek-R1-Distill-Llama-70B              | deepseek-ai/DeepSeek-R1-Distill-Llama-70B             | 24576                | 12288                | 8                    | 8                    | 8              |
| DeepSeek     | DeepSeek-R1-Distill-Llama-70B              | deepseek-ai/DeepSeek-R1-Distill-Llama-70B-32k         | 32768                | 16384                | 1                    | 1                    | 1              |
| DeepSeek     | DeepSeek-R1-Distill-Llama-70B              | deepseek-ai/DeepSeek-R1-Distill-Llama-70B-131k        | 131072               | 16384                | 1                    | 1                    | 1              |
| DeepSeek     | DeepSeek-R1-Distill-Qwen-14B               | deepseek-ai/DeepSeek-R1-Distill-Qwen-14B              | 65536                | 49152                | 8                    | 8                    | 8              |
| DeepSeek     | DeepSeek-R1-Distill-Qwen-1.5B              | deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B             | 131072               | 131072               | 8                    | 8                    | 8              |
| Meta         | Llama-4-Scout-17B-16E                      | meta-llama/Llama-4-Scout-17B-16E                      | 16384                | 12288                | 8                    | 8                    | 8              |
| Meta         | Llama-4-Scout-17B-16E-Instruct             | meta-llama/Llama-4-Scout-17B-16E-Instruct             | 16384                | 12288                | 8                    | 8                    | 8              |
| Meta         | Llama-4-Maverick-17B-128E                  | meta-llama/Llama-4-Maverick-17B-128E                  | 16384                | 24576                | 16                   | 16                   | 16             |
| Meta         | Llama-4-Maverick-17B-128E-Instruct         | meta-llama/Llama-4-Maverick-17B-128E-Instruct         | 16384                | 24576                | 16                   | 16                   | 16             |
| Google       | gemma-3-270m                               | google/gemma-3-270m                                   | 32768                | 32768                | 128                  | 128                  | 8              |
| Google       | gemma-3-270m-it                            | google/gemma-3-270m-it                                | 32768                | 32768                | 128                  | 128                  | 8              |
| Google       | gemma-3-1b-it                              | google/gemma-3-1b-it                                  | 32768                | 32768                | 32                   | 32                   | 8              |
| Google       | gemma-3-1b-pt                              | google/gemma-3-1b-pt                                  | 32768                | 32768                | 32                   | 32                   | 8              |
| Google       | gemma-3-4b-it                              | google/gemma-3-4b-it                                  | 131072               | 65536                | 8                    | 8                    | 8              |
| Google       | gemma-3-4b-pt                              | google/gemma-3-4b-pt                                  | 131072               | 65536                | 8                    | 8                    | 8              |
| Google       | gemma-3-12b-it                             | google/gemma-3-12b-it                                 | 16384                | 49152                | 8                    | 8                    | 8              |
| Google       | gemma-3-12b-pt                             | google/gemma-3-12b-pt                                 | 65536                | 49152                | 8                    | 8                    | 8              |
| Google       | gemma-3-27b-it                             | google/gemma-3-27b-it                                 | 49152                | 24576                | 8                    | 8                    | 8              |
| Google       | gemma-3-27b-pt                             | google/gemma-3-27b-pt                                 | 49152                | 24576                | 8                    | 8                    | 8              |
| Qwen         | Qwen3-Next-80B-A3B-Instruct                | Qwen/Qwen3-Next-80B-A3B-Instruct                      | 65536                | 16384                | 8                    | 8                    | 8              |
| Qwen         | Qwen3-Next-80B-A3B-Thinking                | Qwen/Qwen3-Next-80B-A3B-Thinking                      | 65536                | 16384                | 8                    | 8                    | 8              |
| Qwen         | Qwen3-0.6B                                 | Qwen/Qwen3-0.6B                                       | 32768                | 40960                | 64                   | 64                   | 8              |
| Qwen         | Qwen3-0.6B-Base                            | Qwen/Qwen3-0.6B-Base                                  | 32768                | 32768                | 64                   | 64                   | 8              |
| Qwen         | Qwen3-1.7B                                 | Qwen/Qwen3-1.7B                                       | 32768                | 40960                | 32                   | 32                   | 8              |
| Qwen         | Qwen3-1.7B-Base                            | Qwen/Qwen3-1.7B-Base                                  | 32768                | 32768                | 32                   | 32                   | 8              |
| Qwen         | Qwen3-4B                                   | Qwen/Qwen3-4B                                         | 32768                | 40960                | 16                   | 16                   | 8              |
| Qwen         | Qwen3-4B-Base                              | Qwen/Qwen3-4B-Base                                    | 32768                | 32768                | 16                   | 16                   | 8              |
| Qwen         | Qwen3-8B                                   | Qwen/Qwen3-8B                                         | 32768                | 40960                | 8                    | 8                    | 8              |
| Qwen         | Qwen3-8B-Base                              | Qwen/Qwen3-8B-Base                                    | 32768                | 32768                | 16                   | 16                   | 8              |
| Qwen         | Qwen3-14B                                  | Qwen/Qwen3-14B                                        | 32768                | 40960                | 8                    | 8                    | 8              |
| Qwen         | Qwen3-14B-Base                             | Qwen/Qwen3-14B-Base                                   | 32768                | 40960                | 8                    | 8                    | 8              |
| Qwen         | Qwen3-32B                                  | Qwen/Qwen3-32B                                        | 24576                | 24576                | 8                    | 8                    | 8              |
| Qwen         | Qwen3-30B-A3B-Base                         | Qwen/Qwen3-30B-A3B-Base                               | 8192                 | 32768                | 16                   | 16                   | 8              |
| Qwen         | Qwen3-30B-A3B                              | Qwen/Qwen3-30B-A3B                                    | 8192                 | 32768                | 16                   | 16                   | 8              |
| Qwen         | Qwen3-30B-A3B-Instruct-2507                | Qwen/Qwen3-30B-A3B-Instruct-2507                      | 8192                 | 32768                | 16                   | 16                   | 8              |
| Qwen         | Qwen3-235B-A22B                            | Qwen/Qwen3-235B-A22B                                  | 32768                | 24576                | 1                    | 1                    | 8              |
| Qwen         | Qwen3-235B-A22B-Instruct-2507              | Qwen/Qwen3-235B-A22B-Instruct-2507                    | 32768                | 24576                | 1                    | 1                    | 8              |
| Qwen         | Qwen3-Coder-30B-A3B-Instruct               | Qwen/Qwen3-Coder-30B-A3B-Instruct                     | 8192                 | 8192                 | 16                   | 16                   | 8              |
| Qwen         | Qwen3-Coder-480B-A35B-Instruct             | Qwen/Qwen3-Coder-480B-A35B-Instruct                   | 131072               | 32768                | 1                    | 1                    | 2              |
| Meta         | Llama-3.3-70B-Instruct-Reference           | meta-llama/Llama-3.3-70B-Instruct-Reference           | 24576                | 8192                 | 8                    | 8                    | 8              |
| Meta         | Llama-3.3-70B-32k-Instruct-Reference       | meta-llama/Llama-3.3-70B-32k-Instruct-Reference       | 32768                | 65536                | 1                    | 1                    | 1              |
| Meta         | Llama-3.3-70B-131k-Instruct-Reference      | meta-llama/Llama-3.3-70B-131k-Instruct-Reference      | 131072               | 65536                | 1                    | 1                    | 1              |
| Meta         | Llama-3.2-3B-Instruct                      | meta-llama/Llama-3.2-3B-Instruct                      | 131072               | 65536                | 8                    | 8                    | 8              |
| Meta         | Llama-3.2-3B                               | meta-llama/Llama-3.2-3B                               | 131072               | 65536                | 8                    | 8                    | 8              |
| Meta         | Llama-3.2-1B-Instruct                      | meta-llama/Llama-3.2-1B-Instruct                      | 131072               | 131072               | 8                    | 8                    | 8              |
| Meta         | Llama-3.2-1B                               | meta-llama/Llama-3.2-1B                               | 131072               | 131072               | 8                    | 8                    | 8              |
| Meta         | Meta-Llama-3.1-8B-Instruct-Reference       | meta-llama/Meta-Llama-3.1-8B-Instruct-Reference       | 131072               | 65536                | 8                    | 8                    | 8              |
| Meta         | Meta-Llama-3.1-8B-131k-Instruct-Reference  | meta-llama/Meta-Llama-3.1-8B-131k-Instruct-Reference  | 131072               | 131072               | 4                    | 4                    | 1              |
| Meta         | Meta-Llama-3.1-8B-Reference                | meta-llama/Meta-Llama-3.1-8B-Reference                | 131072               | 65536                | 8                    | 8                    | 8              |
| Meta         | Meta-Llama-3.1-8B-131k-Reference           | meta-llama/Meta-Llama-3.1-8B-131k-Reference           | 131072               | 131072               | 4                    | 4                    | 1              |
| Meta         | Meta-Llama-3.1-70B-Instruct-Reference      | meta-llama/Meta-Llama-3.1-70B-Instruct-Reference      | 24576                | 12288                | 8                    | 8                    | 8              |
| Meta         | Meta-Llama-3.1-70B-32k-Instruct-Reference  | meta-llama/Meta-Llama-3.1-70B-32k-Instruct-Reference  | 32768                | 32768                | 1                    | 1                    | 1              |
| Meta         | Meta-Llama-3.1-70B-131k-Instruct-Reference | meta-llama/Meta-Llama-3.1-70B-131k-Instruct-Reference | 131072               | 65536                | 1                    | 1                    | 1              |
| Meta         | Meta-Llama-3.1-70B-Reference               | meta-llama/Meta-Llama-3.1-70B-Reference               | 24576                | 12288                | 8                    | 8                    | 8              |
| Meta         | Meta-Llama-3.1-70B-32k-Reference           | meta-llama/Meta-Llama-3.1-70B-32k-Reference           | 32768                | 32768                | 1                    | 1                    | 1              |
| Meta         | Meta-Llama-3.1-70B-131k-Reference          | meta-llama/Meta-Llama-3.1-70B-131k-Reference          | 131072               | 65536                | 1                    | 1                    | 1              |
| Meta         | Meta-Llama-3-8B-Instruct                   | meta-llama/Meta-Llama-3-8B-Instruct                   | 8192                 | 8192                 | 64                   | 64                   | 8              |
| Meta         | Meta-Llama-3-8B                            | meta-llama/Meta-Llama-3-8B                            | 8192                 | 8192                 | 64                   | 64                   | 8              |
| Meta         | Meta-Llama-3-70B-Instruct                  | meta-llama/Meta-Llama-3-70B-Instruct                  | 8192                 | 8192                 | 8                    | 8                    | 8              |
| Qwen         | Qwen2.5-72B-Instruct                       | Qwen/Qwen2.5-72B-Instruct                             | 32768                | 12288                | 8                    | 8                    | 8              |
| Qwen         | Qwen2.5-72B                                | Qwen/Qwen2.5-72B                                      | 24576                | 12288                | 8                    | 8                    | 8              |
| Qwen         | Qwen2.5-32B-Instruct                       | Qwen/Qwen2.5-32B-Instruct                             | 32768                | 32768                | 8                    | 8                    | 8              |
| Qwen         | Qwen2.5-32B                                | Qwen/Qwen2.5-32B                                      | 49152                | 32768                | 8                    | 8                    | 8              |
| Qwen         | Qwen2.5-14B-Instruct                       | Qwen/Qwen2.5-14B-Instruct                             | 32768                | 32768                | 8                    | 8                    | 8              |
| Qwen         | Qwen2.5-14B                                | Qwen/Qwen2.5-14B                                      | 65536                | 49152                | 8                    | 8                    | 8              |
| Qwen         | Qwen2.5-7B-Instruct                        | Qwen/Qwen2.5-7B-Instruct                              | 32768                | 32768                | 16                   | 16                   | 8              |
| Qwen         | Qwen2.5-7B                                 | Qwen/Qwen2.5-7B                                       | 131072               | 65536                | 8                    | 8                    | 8              |
| Qwen         | Qwen2.5-3B-Instruct                        | Qwen/Qwen2.5-3B-Instruct                              | 32768                | 32768                | 32                   | 32                   | 8              |
| Qwen         | Qwen2.5-3B                                 | Qwen/Qwen2.5-3B                                       | 32768                | 32768                | 32                   | 32                   | 8              |
| Qwen         | Qwen2.5-1.5B-Instruct                      | Qwen/Qwen2.5-1.5B-Instruct                            | 32768                | 32768                | 32                   | 32                   | 8              |
| Qwen         | Qwen2.5-1.5B                               | Qwen/Qwen2.5-1.5B                                     | 32768                | 131072               | 8                    | 8                    | 8              |
| Qwen         | Qwen2-72B-Instruct                         | Qwen/Qwen2-72B-Instruct                               | 32768                | 12288                | 16                   | 16                   | 16             |
| Qwen         | Qwen2-72B                                  | Qwen/Qwen2-72B                                        | 32768                | 12288                | 16                   | 16                   | 16             |
| Qwen         | Qwen2-7B-Instruct                          | Qwen/Qwen2-7B-Instruct                                | 32768                | 32768                | 8                    | 8                    | 8              |
| Qwen         | Qwen2-7B                                   | Qwen/Qwen2-7B                                         | 131072               | 24576                | 8                    | 8                    | 8              |
| Qwen         | Qwen2-1.5B-Instruct                        | Qwen/Qwen2-1.5B-Instruct                              | 32768                | 32768                | 32                   | 32                   | 8              |
| Qwen         | Qwen2-1.5B                                 | Qwen/Qwen2-1.5B                                       | 131072               | 131072               | 8                    | 8                    | 8              |
| Mistral      | Mixtral-8x7B-Instruct-v0.1                 | mistralai/Mixtral-8x7B-Instruct-v0.1                  | 32768                | 32768                | 8                    | 8                    | 8              |
| Mistral      | Mixtral-8x7B-v0.1                          | mistralai/Mixtral-8x7B-v0.1                           | 32768                | 32768                | 8                    | 8                    | 8              |
| Mistral      | Mistral-7B-Instruct-v0.2                   | mistralai/Mistral-7B-Instruct-v0.2                    | 32768                | 32768                | 16                   | 16                   | 8              |
| Mistral      | Mistral-7B-v0.1                            | mistralai/Mistral-7B-v0.1                             | 32768                | 32768                | 16                   | 16                   | 8              |
| Teknium      | OpenHermes-2p5-Mistral-7B                  | teknium/OpenHermes-2p5-Mistral-7B                     | 32768                | 32768                | 16                   | 16                   | 8              |
| Meta         | CodeLlama-7b-hf                            | codellama/CodeLlama-7b-hf                             | 16384                | 16384                | 16                   | 16                   | 8              |
| Together     | llama-2-7b-chat                            | togethercomputer/llama-2-7b-chat                      | 4096                 | 4096                 | 64                   | 64                   | 8              |

## LoRA Long-context Fine-tuning

| Organization | Model Name                                 | Model String for API                                  | Context Length (SFT) | Context Length (DPO) | Max Batch Size (SFT) | Max Batch Size (DPO) | Min Batch Size |
| ------------ | ------------------------------------------ | ----------------------------------------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------- |
| DeepSeek     | DeepSeek-R1-0528                           | deepseek-ai/DeepSeek-R1-0528                          | 131072               | 32768                | 1                    | 1                    | 2              |
| DeepSeek     | DeepSeek-R1                                | deepseek-ai/DeepSeek-R1                               | 131072               | 32768                | 1                    | 1                    | 2              |
| DeepSeek     | DeepSeek-V3.1                              | deepseek-ai/DeepSeek-V3.1                             | 131072               | 32768                | 1                    | 1                    | 2              |
| DeepSeek     | DeepSeek-V3-0324                           | deepseek-ai/DeepSeek-V3-0324                          | 131072               | 32768                | 1                    | 1                    | 2              |
| DeepSeek     | DeepSeek-V3                                | deepseek-ai/DeepSeek-V3                               | 131072               | 32768                | 1                    | 1                    | 2              |
| DeepSeek     | DeepSeek-V3.1-Base                         | deepseek-ai/DeepSeek-V3.1-Base                        | 131072               | 32768                | 1                    | 1                    | 2              |
| DeepSeek     | DeepSeek-V3-Base                           | deepseek-ai/DeepSeek-V3-Base                          | 131072               | 32768                | 1                    | 1                    | 2              |
| DeepSeek     | DeepSeek-R1-Distill-Llama-70B              | deepseek-ai/DeepSeek-R1-Distill-Llama-70B-32k         | 32768                | 16384                | 1                    | 1                    | 1              |
| DeepSeek     | DeepSeek-R1-Distill-Llama-70B              | deepseek-ai/DeepSeek-R1-Distill-Llama-70B-131k        | 131072               | 16384                | 1                    | 1                    | 1              |
| Qwen         | Qwen3-235B-A22B                            | Qwen/Qwen3-235B-A22B                                  | 32768                | 24576                | 1                    | 1                    | 8              |
| Qwen         | Qwen3-235B-A22B-Instruct-2507              | Qwen/Qwen3-235B-A22B-Instruct-2507                    | 32768                | 24576                | 1                    | 1                    | 8              |
| Qwen         | Qwen3-Coder-480B-A35B-Instruct             | Qwen/Qwen3-Coder-480B-A35B-Instruct                   | 131072               | 32768                | 1                    | 1                    | 2              |
| Meta         | Llama-3.3-70B-32k-Instruct-Reference       | meta-llama/Llama-3.3-70B-32k-Instruct-Reference       | 32768                | 65536                | 1                    | 1                    | 1              |
| Meta         | Llama-3.3-70B-131k-Instruct-Reference      | meta-llama/Llama-3.3-70B-131k-Instruct-Reference      | 131072               | 65536                | 1                    | 1                    | 1              |
| Meta         | Meta-Llama-3.1-8B-131k-Instruct-Reference  | meta-llama/Meta-Llama-3.1-8B-131k-Instruct-Reference  | 131072               | 131072               | 4                    | 4                    | 1              |
| Meta         | Meta-Llama-3.1-8B-131k-Reference           | meta-llama/Meta-Llama-3.1-8B-131k-Reference           | 131072               | 131072               | 4                    | 4                    | 1              |
| Meta         | Meta-Llama-3.1-70B-32k-Instruct-Reference  | meta-llama/Meta-Llama-3.1-70B-32k-Instruct-Reference  | 32768                | 32768                | 1                    | 1                    | 1              |
| Meta         | Meta-Llama-3.1-70B-131k-Instruct-Reference | meta-llama/Meta-Llama-3.1-70B-131k-Instruct-Reference | 131072               | 65536                | 1                    | 1                    | 1              |
| Meta         | Meta-Llama-3.1-70B-32k-Reference           | meta-llama/Meta-Llama-3.1-70B-32k-Reference           | 32768                | 32768                | 1                    | 1                    | 1              |
| Meta         | Meta-Llama-3.1-70B-131k-Reference          | meta-llama/Meta-Llama-3.1-70B-131k-Reference          | 131072               | 65536                | 1                    | 1                    | 1              |

## Full Fine-tuning

| Organization | Model Name                            | Model String for API                             | Context Length (SFT) | Context Length (DPO) | Max Batch Size (SFT) | Max Batch Size (DPO) | Min Batch Size |
| ------------ | ------------------------------------- | ------------------------------------------------ | -------------------- | -------------------- | -------------------- | -------------------- | -------------- |
| DeepSeek     | DeepSeek-R1-Distill-Llama-70B         | deepseek-ai/DeepSeek-R1-Distill-Llama-70B        | 24576                | 12288                | 32                   | 32                   | 32             |
| DeepSeek     | DeepSeek-R1-Distill-Qwen-14B          | deepseek-ai/DeepSeek-R1-Distill-Qwen-14B         | 65536                | 49152                | 8                    | 8                    | 8              |
| DeepSeek     | DeepSeek-R1-Distill-Qwen-1.5B         | deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B        | 131072               | 131072               | 8                    | 8                    | 8              |
| Google       | gemma-3-270m                          | google/gemma-3-270m                              | 32768                | 32768                | 128                  | 128                  | 8              |
| Google       | gemma-3-270m-it                       | google/gemma-3-270m-it                           | 32768                | 32768                | 128                  | 128                  | 8              |
| Google       | gemma-3-1b-it                         | google/gemma-3-1b-it                             | 32768                | 32768                | 64                   | 64                   | 8              |
| Google       | gemma-3-1b-pt                         | google/gemma-3-1b-pt                             | 32768                | 32768                | 64                   | 64                   | 8              |
| Google       | gemma-3-4b-it                         | google/gemma-3-4b-it                             | 131072               | 65536                | 8                    | 8                    | 8              |
| Google       | gemma-3-4b-pt                         | google/gemma-3-4b-pt                             | 131072               | 65536                | 8                    | 8                    | 8              |
| Google       | gemma-3-12b-it                        | google/gemma-3-12b-it                            | 16384                | 49152                | 8                    | 8                    | 8              |
| Google       | gemma-3-12b-pt                        | google/gemma-3-12b-pt                            | 65536                | 49152                | 8                    | 8                    | 8              |
| Google       | gemma-3-27b-it                        | google/gemma-3-27b-it                            | 49152                | 24576                | 16                   | 16                   | 16             |
| Google       | gemma-3-27b-pt                        | google/gemma-3-27b-pt                            | 49152                | 24576                | 16                   | 16                   | 16             |
| Qwen         | Qwen3-0.6B                            | Qwen/Qwen3-0.6B                                  | 32768                | 40960                | 64                   | 64                   | 8              |
| Qwen         | Qwen3-0.6B-Base                       | Qwen/Qwen3-0.6B-Base                             | 32768                | 32768                | 64                   | 64                   | 8              |
| Qwen         | Qwen3-1.7B                            | Qwen/Qwen3-1.7B                                  | 32768                | 40960                | 32                   | 32                   | 8              |
| Qwen         | Qwen3-1.7B-Base                       | Qwen/Qwen3-1.7B-Base                             | 32768                | 32768                | 32                   | 32                   | 8              |
| Qwen         | Qwen3-4B                              | Qwen/Qwen3-4B                                    | 32768                | 40960                | 16                   | 16                   | 8              |
| Qwen         | Qwen3-4B-Base                         | Qwen/Qwen3-4B-Base                               | 32768                | 32768                | 16                   | 16                   | 8              |
| Qwen         | Qwen3-8B                              | Qwen/Qwen3-8B                                    | 32768                | 40960                | 8                    | 8                    | 8              |
| Qwen         | Qwen3-8B-Base                         | Qwen/Qwen3-8B-Base                               | 32768                | 32768                | 16                   | 16                   | 8              |
| Qwen         | Qwen3-14B                             | Qwen/Qwen3-14B                                   | 32768                | 40960                | 8                    | 8                    | 8              |
| Qwen         | Qwen3-14B-Base                        | Qwen/Qwen3-14B-Base                              | 32768                | 40960                | 8                    | 8                    | 8              |
| Qwen         | Qwen3-32B                             | Qwen/Qwen3-32B                                   | 24576                | 24576                | 16                   | 16                   | 16             |
| Qwen         | Qwen3-30B-A3B-Base                    | Qwen/Qwen3-30B-A3B-Base                          | 8192                 | 32768                | 8                    | 8                    | 8              |
| Qwen         | Qwen3-30B-A3B                         | Qwen/Qwen3-30B-A3B                               | 8192                 | 32768                | 8                    | 8                    | 8              |
| Qwen         | Qwen3-30B-A3B-Instruct-2507           | Qwen/Qwen3-30B-A3B-Instruct-2507                 | 8192                 | 32768                | 8                    | 8                    | 8              |
| Qwen         | Qwen3-Coder-30B-A3B-Instruct          | Qwen/Qwen3-Coder-30B-A3B-Instruct                | 8192                 | 8192                 | 8                    | 8                    | 8              |
| Meta         | Llama-3.3-70B-Instruct-Reference      | meta-llama/Llama-3.3-70B-Instruct-Reference      | 24576                | 8192                 | 32                   | 32                   | 32             |
| Meta         | Llama-3.2-3B-Instruct                 | meta-llama/Llama-3.2-3B-Instruct                 | 131072               | 65536                | 8                    | 8                    | 8              |
| Meta         | Llama-3.2-3B                          | meta-llama/Llama-3.2-3B                          | 131072               | 65536                | 8                    | 8                    | 8              |
| Meta         | Llama-3.2-1B-Instruct                 | meta-llama/Llama-3.2-1B-Instruct                 | 131072               | 131072               | 8                    | 8                    | 8              |
| Meta         | Llama-3.2-1B                          | meta-llama/Llama-3.2-1B                          | 131072               | 131072               | 8                    | 8                    | 8              |
| Meta         | Meta-Llama-3.1-8B-Instruct-Reference  | meta-llama/Meta-Llama-3.1-8B-Instruct-Reference  | 131072               | 65536                | 8                    | 8                    | 8              |
| Meta         | Meta-Llama-3.1-8B-Reference           | meta-llama/Meta-Llama-3.1-8B-Reference           | 131072               | 65536                | 8                    | 8                    | 8              |
| Meta         | Meta-Llama-3.1-70B-Instruct-Reference | meta-llama/Meta-Llama-3.1-70B-Instruct-Reference | 24576                | 12288                | 32                   | 32                   | 32             |
| Meta         | Meta-Llama-3.1-70B-Reference          | meta-llama/Meta-Llama-3.1-70B-Reference          | 24576                | 12288                | 32                   | 32                   | 32             |
| Meta         | Meta-Llama-3-8B-Instruct              | meta-llama/Meta-Llama-3-8B-Instruct              | 8192                 | 8192                 | 64                   | 64                   | 8              |
| Meta         | Meta-Llama-3-8B                       | meta-llama/Meta-Llama-3-8B                       | 8192                 | 8192                 | 64                   | 64                   | 8              |
| Meta         | Meta-Llama-3-70B-Instruct             | meta-llama/Meta-Llama-3-70B-Instruct             | 8192                 | 8192                 | 32                   | 32                   | 32             |
| Qwen         | Qwen2-7B-Instruct                     | Qwen/Qwen2-7B-Instruct                           | 32768                | 32768                | 8                    | 8                    | 8              |
| Qwen         | Qwen2-7B                              | Qwen/Qwen2-7B                                    | 131072               | 24576                | 8                    | 8                    | 8              |
| Qwen         | Qwen2-1.5B-Instruct                   | Qwen/Qwen2-1.5B-Instruct                         | 32768                | 32768                | 32                   | 32                   | 8              |
| Qwen         | Qwen2-1.5B                            | Qwen/Qwen2-1.5B                                  | 131072               | 131072               | 8                    | 8                    | 8              |
| Mistral      | Mixtral-8x7B-Instruct-v0.1            | mistralai/Mixtral-8x7B-Instruct-v0.1             | 32768                | 32768                | 16                   | 16                   | 16             |
| Mistral      | Mixtral-8x7B-v0.1                     | mistralai/Mixtral-8x7B-v0.1                      | 32768                | 32768                | 16                   | 16                   | 16             |
| Mistral      | Mistral-7B-Instruct-v0.2              | mistralai/Mistral-7B-Instruct-v0.2               | 32768                | 32768                | 16                   | 16                   | 8              |
| Mistral      | Mistral-7B-v0.1                       | mistralai/Mistral-7B-v0.1                        | 32768                | 32768                | 16                   | 16                   | 8              |
| Teknium      | OpenHermes-2p5-Mistral-7B             | teknium/OpenHermes-2p5-Mistral-7B                | 32768                | 32768                | 16                   | 16                   | 8              |
| Meta         | CodeLlama-7b-hf                       | codellama/CodeLlama-7b-hf                        | 16384                | 16384                | 16                   | 16                   | 8              |
| Together     | llama-2-7b-chat                       | togethercomputer/llama-2-7b-chat                 | 4096                 | 4096                 | 64                   | 64                   | 8              |


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt