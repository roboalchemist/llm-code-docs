# Running DeepSeek-R1 70B using Ollama -

Source: https://docs.lambda.ai/education/large-language-models/deepseek-r1-ollama/

---

[llm](../../../tags/#tag:llm)

# Running DeepSeek-R1 70B using Ollama [#](#running-deepseek-r1-70b-using-ollama)

## Introduction [#](#introduction)

This short tutorial teaches how to use a [Lambda Cloud on-demand instance](https://lambda.ai/service/gpu-cloud)to run the [DeepSeek-R1 distilled Llama 3.3 70B model using Ollama](https://ollama.com/library/deepseek-r1)in a Docker container. Since [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)is preinstalled as part of [Lambda Stack](https://lambda.ai/lambda-stack-deep-learning-software)on all on-demand instances, Docker containers can use instance GPUs without any additional configuration.

## Prerequisites [#](#prerequisites)

For this tutorial, it's recommended that you use an instance type with more than 40 GB of VRAM, for example, a 1x GH200 or 1x H100.

## Download Ollama and start the Ollama server [#](#download-ollama-and-start-the-ollama-server)

-
Log into your instance using SSH or by opening a terminal in Jupyter Lab.

-
Download Ollama and start the Ollama server:

```bash
`[](#__codelineno-0-1)sudo docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
`

```
