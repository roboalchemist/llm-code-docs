# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md

Title: Overview — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html

Published Time: Thu, 30 Oct 2025 07:07:33 GMT

Markdown Content:
Overview[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#overview "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

NVIDIA NeMo Framework is a scalable and cloud-native generative AI framework built for researchers and developers working on [Large Language Models](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/index.html.md#nemo-2-llms), Multimodal, and [Speech AI](https://docs.nvidia.com/nemo-framework/user-guide/latest/speech_ai/index.html.md) (e.g. [Automatic Speech Recognition](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/intro.html.md) and [Text-to-Speech](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/intro.html.md)). It enables users to efficiently create, customize, and deploy new generative AI models by leveraging existing code and pre-trained model checkpoints.

**Setup Instructions**: [Install NeMo Framework](https://docs.nvidia.com/nemo-framework/user-guide/latest/installation.html.md#install-nemo-framework)

Large Language Models and Multimodal Models[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#large-language-models-and-multimodal-models "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

NeMo Framework provides end-to-end support for developing Large Language Models (LLMs) and Multimodal Models (MMs). It provides the flexibility to be used on-premises, in a data-center, or with your preferred cloud provider. It also supports execution on SLURM or Kubernetes enabled environments.

![Image 1: _images/nemo-llm-mm-stack.png](https://docs.nvidia.com/nemo-framework/user-guide/latest/_images/nemo-llm-mm-stack.png)
### Data Curation[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#data-curation "Link to this heading")

[NeMo Curator](https://github.com/NVIDIA/NeMo-Curator)[[1]](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html#f1) is a Python library that includes a suite of modules for data-mining and synthetic data generation. They are scalable and optimized for GPUs, making them ideal for curating natural language data to train or fine-tune LLMs. With NeMo Curator, you can efficiently extract high-quality text from extensive raw web data sources.

### Training and Customization[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#training-and-customization "Link to this heading")

NeMo Framework provides tools for efficient training and customization of [LLMs](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/index.html.md#nemo-2-llms) and Multimodal models. It includes default configurations for compute cluster setup, data downloading, and model hyperparameters, which can be adjusted to train on new datasets and models. In addition to pre-training, NeMo supports both Supervised Fine-Tuning (SFT) and Parameter Efficient Fine-Tuning (PEFT) techniques like LoRA, Ptuning, and more.

Two options are available to launch training in NeMo - using the NeMo 2.0 API interface or with [NeMo Run](https://github.com/NVIDIA/NeMo-Run).

*   **With NeMo Run (Recommended):** NeMo Run provides an interface to streamline configuration, execution and management of experiments across various compute environments. This includes launching jobs on your workstation locally or on big clusters - both SLURM enabled or Kubernetes in a cloud environment.

*   **Using the NeMo 2.0 API:** This method works well with a simple setup involving small models, or if you are interested in writing your own custom dataloader, training loops, or change model layers. It gives you more flexibility and control over configurations, and makes it easy to extend and customize configurations programmatically.

### RL[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#rl "Link to this heading")

[NeMo RL](https://github.com/NVIDIA/NeMo-RL)[[1]](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html#f1) is a scalable and efficient post-training library designed for models ranging from 1 GPU to thousands, and from tiny to over 100 billion parameters.

What you can expect:

*   **Seamless integration with Hugging Face** for ease of use, allowing users to leverage a wide range of pre-trained models and tools.

*   **High-performance implementation with Megatron Core**, supporting various parallelism techniques for large models (>100B) and large context lengths.

*   **Efficient resource management using Ray**, enabling scalable and flexible deployment across different hardware configurations.

*   **Flexibility** with a modular design that allows easy integration and customization.

*   **Comprehensive documentation** that is both detailed and user-friendly, with practical examples.

Check out the [NeMo RL Documentation](https://docs.nvidia.com/nemo/rl/latest/index.html.md) for more information.

### Multimodal Models[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#multimodal-models "Link to this heading")

NeMo Framework provides optimized software to train and deploy state-of-the-art multimodal models across several categories: Multimodal Language Models, Vision-Language Foundations, Text-to-Image models, and Beyond 2D Generation using Neural Radiance Fields (NeRF).

Each category is designed to cater to specific needs and advancements in the field, leveraging cutting-edge models to handle a wide range of data types, including text, images, and 3D models.

Note

We are migrating support for multimodal models from NeMo 1.0 to NeMo 2.0. If you want to explore this domain in the meantime, please refer to the documentation for the NeMo 24.07 (previous) release.

### Deployment and Inference[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#deployment-and-inference "Link to this heading")

NeMo Framework provides various paths for LLM inference, catering to different deployment scenarios and performance needs.

#### Deploy with NVIDIA NIM[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#deploy-with-nvidia-nim "Link to this heading")

NeMo Framework seamlessly integrates with enterprise-level model deployment tools through [NVIDIA NIM](https://www.nvidia.com/en-gb/launchpad/ai/generative-ai-inference-with-nim.md). This integration is powered by NVIDIA TensorRT-LLM ensuring optimized and scalable inference.

For more information on NIM, visit the [NVIDIA website](https://www.nvidia.com/en-gb/launchpad/ai/generative-ai-inference-with-nim).

#### Deploy with TensorRT-LLM or vLLM[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#deploy-with-tensorrt-llm-or-vllm "Link to this heading")

NeMo Framework offers scripts and APIs to export models to two inference optimized libraries, TensorRT-LLM and vLLM, and to deploy the exported model with the NVIDIA Triton Inference Server.

For scenarios requiring optimized performance, NeMo models can leverage TensorRT-LLM, a specialized library for accelerating and optimizing LLM inference on NVIDIA GPUs. This process involves converting NeMo models into a format compatible with TensorRT-LLM using the nemo.export module.

> LLM Deployment Overview
> 
> 
> Deploy NeMo Large Language Models with NIM
> 
> 
> Deploy NeMo Large Language Models with TensorRT-LLM
> 
> 
> Deploy NeMo Large Language Models with vLLM

### Supported Models[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#supported-models "Link to this heading")

#### Large Language Models[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#large-language-models "Link to this heading")

Large Language Models[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#id3 "Link to this table")| Large Language Models | Pretraining & SFT | PEFT | Alignment | FP8 Training Convergence | TRT/TRTLLM | Convert To & From Hugging Face | Evaluation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Llama3 8B/70B, Llama3.1 405B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/llama3.html.md#llama) | Yes | Yes | x | Yes (partially verified) | Yes | Both | Yes |
| [Mixtral 8x7B/8x22B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/mixtral.html.md#mixtral) | Yes | Yes | x | Yes (unverified) | Yes | Both | Yes |
| [Nemotron 3 8B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/nemotron.html.md#nemotron) | Yes | x | x | Yes (unverified) | x | Both | Yes |
| [Nemotron 4 340B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/nemotron.html.md#nemotron) | Yes | x | x | Yes (unverified) | x | Both | Yes |
| [Baichuan2 7B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/baichuan2.html.md#baichuan) | Yes | Yes | x | Yes (unverified) | x | Both | Yes |
| [ChatGLM3 6B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/chatglm3.html.md#chatglm) | Yes | Yes | x | Yes (unverified) | x | Both | Yes |
| [DeepSeek V2/V3](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/deepseek_v3.html.md#deepseek-v3) | Yes | Yes | x | Yes (unverified) | x | Both | Yes |
| [Gemma 2B/7B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gemma.html.md#gemma) | Yes | Yes | x | Yes (unverified) | Yes | Both | Yes |
| [Gemma2 2B/9B/27B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gemma2.html.md#gemma2) | Yes | Yes | x | Yes (unverified) | x | Both | Yes |
| [GPT-OSS 20B/120B/](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gpt_oss.html.md#gpt-oss) | Yes | Yes | x | Yes (unverified) | x | Both | Yes |
| [Mamba2 130M/370M/780M/1.3B/2.7B/8B/ Hybrid-8B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/mamba.html.md#mamba) | Yes | Yes | x | Yes (unverified) | x | x | Yes |
| [Phi3 mini 4k](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/phi3.html.md#phi3) | x | Yes | x | Yes (unverified) | x | x | x |
| [Qwen2 0.5B/1.5B/7B/72B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/qwen2.html.md#qwen2) | Yes | Yes | x | Yes (unverified) | Yes | Both | Yes |
| [Qwen3 0.6B/1.7B/4B/8B/14B/32B/30B_A3B/235B_A22B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/qwen3.html.md#qwen3) | Yes | Yes | x | Yes (unverified) | Yes | Both | Yes |
| [StarCoder 15B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/starcoder.html.md#starcoder) | Yes | Yes | x | Yes (unverified) | Yes | Both | Yes |
| [StarCoder2 3B/7B/15B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/starcoder2.html.md#starcoder2) | Yes | Yes | x | Yes (unverified) | Yes | Both | Yes |
| [BERT 110M/340M](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/bert.html.md#bert) | Yes | Yes | x | Yes (unverified) | x | Both | x |
| [T5 220M/3B/11B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/t5.html.md#t5) | Yes | Yes | x | x | x | x | x |

#### Vision Language Models[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#vision-language-models "Link to this heading")

Vision Language Models[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#id4 "Link to this table")| Vision Language Models | Pretraining & SFT | PEFT | Alignment | FP8 Training Convergence | TRT/TRTLLM | Convert To & From Hugging Face | Evaluation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [NeVA (LLaVA 1.5)](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/neva.html.md#neva) | Yes | Yes | x | Yes (unverified) | x | From | x |
| [Llama 3.2 Vision 11B/90B](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/mllama.html.md#mllama) | Yes | Yes | x | Yes (unverified) | x | From | x |
| [LLaVA Next (LLaVA 1.6)](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/llavanext.html.md#llavanext) | Yes | Yes | x | Yes (unverified) | x | From | x |
| [Llama Nemotron Nano VL 8B](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/llama_nemotron_vl.html.md#llama-nemotron-vl) | Yes | Yes | x | Yes (unverified) | x | From | x |

#### Embedding Models[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#embedding-models "Link to this heading")

Embedding Models[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#id5 "Link to this table")| Embedding Language Models | Pretraining & SFT | PEFT | Alignment | FP8 Training Convergence | TRT/TRTLLM | Convert To & From Hugging Face | Evaluation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [SBERT 340M](https://docs.nvidia.com/nemo-framework/user-guide/latest/embeddingmodels/bert/sbert.html.md#sbert) | Yes | x | x | Yes (unverified) | x | Both | x |
| [Llama 3.2 Embedding 1B](https://docs.nvidia.com/nemo-framework/user-guide/latest/embeddingmodels/gpt/llama_embedding.html.md#llama-embed) | Yes | x | x | Yes (unverified) | x | Both | x |

#### World Foundation Models[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#world-foundation-models "Link to this heading")

World Foundation Models[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#id6 "Link to this table")| World Foundation Models | Post-Training | Accelerated Inference |
| --- | --- | --- |
| [Cosmos-1.0-Diffusion-Text2World-7B](https://huggingface.co/nvidia/Cosmos-1.0-Diffusion-7B-Text2World) | [Yes](https://github.com/NVIDIA/Cosmos/blob/main/cosmos1/models/diffusion/nemo/post_training/README.md) | [Yes](https://github.com/NVIDIA/Cosmos/blob/main/cosmos1/models/diffusion/nemo/inference/README.md) |
| [Cosmos-1.0-Diffusion-Text2World-14B](https://huggingface.co/nvidia/Cosmos-1.0-Diffusion-14B-Text2World) | [Yes](https://github.com/NVIDIA/Cosmos/blob/main/cosmos1/models/diffusion/nemo/post_training/README.md) | [Yes](https://github.com/NVIDIA/Cosmos/blob/main/cosmos1/models/diffusion/nemo/inference/README.md) |
| Cosmos-1.0-Diffusion-Video2World-7B | Coming Soon | Coming Soon |
| Cosmos-1.0-Diffusion-Video2World-14B | Coming Soon | Coming Soon |
| [Cosmos-1.0-Autoregressive-4B](https://huggingface.co/nvidia/Cosmos-1.0-Autoregressive-4B) | [Yes](https://github.com/NVIDIA/Cosmos/blob/main/cosmos1/models/autoregressive/nemo/post_training/README.md) | [Yes](https://github.com/NVIDIA/Cosmos/blob/main/cosmos1/models/autoregressive/nemo/inference/README.md) |
| Cosmos-1.0-Autoregressive-Video2World-5B | Coming Soon | Coming Soon |
| [Cosmos-1.0-Autoregressive-12B](https://huggingface.co/nvidia/Cosmos-1.0-Autoregressive-12B) | [Yes](https://github.com/NVIDIA/Cosmos/blob/main/cosmos1/models/autoregressive/nemo/post_training/README.md) | [Yes](https://github.com/NVIDIA/Cosmos/blob/main/cosmos1/models/autoregressive/nemo/inference/README.md) |
| Cosmos-1.0-Autoregressive-Video2World-13B | Coming Soon | Coming Soon |

Note

NeMo also supports pretraining for both [diffusion](https://github.com/NVIDIA/NeMo/tree/main/nemo/collections/diffusion) and [autoregressive](https://github.com/NVIDIA/NeMo/tree/main/nemo/collections/multimodal_autoregressive) architectures `text2world` foundation models.

Speech AI[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#speech-ai "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

Developing conversational AI models is a complex process that involves defining, constructing, and training models within particular domains. This process typically requires several iterations to reach a high level of accuracy. It often involves multiple iterations to achieve high accuracy, fine-tuning on various tasks and domain-specific data, ensuring training performance, and preparing models for inference deployment.

![Image 2: _images/nemo-speech-ai.png](https://docs.nvidia.com/nemo-framework/user-guide/latest/_images/nemo-speech-ai.png)
NeMo Framework provides support for the training and customization of Speech AI models. This includes tasks like Automatic Speech Recognition (ASR) and Text-To-Speech (TTS) synthesis. It offers a smooth transition to enterprise-level production deployment with [NVIDIA Riva](https://developer.nvidia.com/riva.md). To assist developers and researchers, NeMo Framework includes state-of-the-art pre-trained checkpoints, tools for reproducible speech data processing, and features for interactive exploration and analysis of speech datasets. The components of the NeMo Framework for Speech AI are as follows:

Training and Customization
NeMo Framework contains everything needed to train and customize speech models ([ASR](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/intro.html.md), [Speech Classification](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speech_classification/intro.html.md), [Speaker Recognition](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_recognition/intro.html.md), [Speaker Diarization](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_diarization/intro.html.md), and [TTS](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/intro.html.md)) in a reproducible manner.

SOTA Pre-trained Models
NeMo Framework provides state-of-the-art recipes and pre-trained checkpoints of several [ASR](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/results.html.md) and [TTS](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/checkpoints.html.md) models, as well as instructions on how to load them.

[Speech Tools](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tools/intro.html.md)
NeMo Framework provides a set of tools useful for developing ASR and TTS models, including:

*   [NeMo Forced Aligner (NFA)](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tools/nemo_forced_aligner.html.md) for generating token-, word- and segment-level timestamps of speech in audio using NeMo’s CTC-based Automatic Speech Recognition models.

*   [Speech Data Processor (SDP)](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tools/speech_data_processor.html.md), a toolkit for simplifying speech data processing. It allows you to represent data processing operations in a config file, minimizing boilerplate code, and allowing reproducibility and shareability.

*   [Speech Data Explorer (SDE)](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tools/speech_data_explorer.html.md), a Dash-based web application for interactive exploration and analysis of speech datasets.

*   [Dataset creation tool](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tools/ctc_segmentation.html.md) which provides functionality to align long audio files with the corresponding transcripts and split them into shorter fragments that are suitable for Automatic Speech Recognition (ASR) model training.

*   [Comparison Tool](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tools/intro.html.md) for ASR Models to compare predictions of different ASR models at word accuracy and utterance level.

*   [ASR Evaluator](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tools/asr_evaluator.html.md) for evaluating the performance of ASR models and other features such as Voice Activity Detection.

*   [Text Normalization Tool](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/nlp/text_normalization/intro.html.md) for converting text from the written form to the spoken form and vice versa (e.g. “31st” vs “thirty first”).

Path to Deployment
NeMo models that have been trained or customized using the NeMo Framework can be optimized and deployed with [NVIDIA Riva](https://developer.nvidia.com/riva.md). Riva provides containers and Helm charts specifically designed to automate the steps for push-button deployment.

Getting Started with Speech AI

Other Resources[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#other-resources "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------

### GitHub Repos[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#github-repos "Link to this heading")

*   [NeMo](https://github.com/NVIDIA/NeMo): The main repository for the NeMo Framework

*   [NeMo-Run](https://github.com/NVIDIA/NeMo-Run): A tool to configure, launch and manage your machine learning experiments.

*   [NeMo-RL](https://github.com/NVIDIA/NeMo-RL): A Scalable and Efficient Post-Training Library

*   [NeMo-Curator](https://github.com/NVIDIA/NeMo-Curator): Scalable data pre-processing and curation toolkit for LLMs

### Getting Help[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#getting-help "Link to this heading")

Engage with the NeMo community, ask questions, get support, or report bugs.

*   [NeMo Discussions](https://github.com/NVIDIA/NeMo/discussions)

*   [NeMo Issues](https://github.com/NVIDIA/NeMo/issues)

Programming Languages and Frameworks[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#programming-languages-and-frameworks "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Python: The main interface to use NeMo Framework

*   Pytorch: NeMo Framework is built on top of PyTorch

Licenses[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#licenses "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

*   NeMo Github repo is licensed under the [Apache 2.0 license](https://github.com/NVIDIA/NeMo?tab=Apache-2.0-1-ov-file#readme)

*   NeMo Framework is licensed under the [NVIDIA AI PRODUCT AGREEMENT](https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/). By pulling and using the container, you accept the terms and conditions of this license.

*   The NeMo Framework container contains Llama materials governed by the [Meta Llama3 Community License Agreement](https://huggingface.co/meta-llama/Meta-Llama-3-8B/tree/main).

Footnotes

Links/Buttons:
- [1](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#id1)
- [2](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#id2)
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md#licenses)
- [Large Language Models](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/index.html.md#nemo-2-llms)
- [Speech AI](https://docs.nvidia.com/nemo-framework/user-guide/latest/speech_ai/index.html.md)
- [Automatic Speech Recognition](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/intro.html.md)
- [Text-to-Speech](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/intro.html.md)
- [Install NeMo Framework](https://docs.nvidia.com/nemo-framework/user-guide/latest/installation.html.md#install-nemo-framework)
- [NeMo Curator](https://github.com/NVIDIA/NeMo-Curator)
- [[1]](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html#f1)
- [Getting Started Tutorials](https://docs.nvidia.com/nemo-framework/user-guide/latest/playbooks/index.html.md#data-curation-tutorials)
- [Data Curation features and usage](https://docs.nvidia.com/nemo/curator/latest/index.html.md)
- [API Documentation](https://docs.nvidia.com/nemo/curator/latest/apidocs/index.html.md)
- [NeMo Run](https://github.com/NVIDIA/NeMo-Run)
- [Pre-training & PEFT Quickstart with NeMo Run](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/quickstart.html.md#nemo-2-quickstart-nemo-run)
- [Training Quickstart with NeMo 2.0 API](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/index.html.md#nemo-2-quickstart-api)
- [Migrating from NeMo 1.0 to NeMo 2.0 API](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/index.html.md#nemo-2-migration)
- [NeMo RL](https://github.com/NVIDIA/NeMo-RL)
- [NeMo RL Documentation](https://docs.nvidia.com/nemo/rl/latest/index.html.md)
- [NVIDIA NIM](https://www.nvidia.com/en-gb/launchpad/ai/generative-ai-inference-with-nim.md)
- [Llama3 8B/70B, Llama3.1 405B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/llama3.html.md#llama)
- [Mixtral 8x7B/8x22B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/mixtral.html.md#mixtral)
- [Nemotron 3 8B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/nemotron.html.md#nemotron)
- [Baichuan2 7B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/baichuan2.html.md#baichuan)
- [ChatGLM3 6B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/chatglm3.html.md#chatglm)
- [DeepSeek V2/V3](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/deepseek_v3.html.md#deepseek-v3)
- [Gemma 2B/7B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gemma.html.md#gemma)
- [Gemma2 2B/9B/27B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gemma2.html.md#gemma2)
- [GPT-OSS 20B/120B/](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gpt_oss.html.md#gpt-oss)
- [Mamba2 130M/370M/780M/1.3B/2.7B/8B/ Hybrid-8B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/mamba.html.md#mamba)
- [Phi3 mini 4k](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/phi3.html.md#phi3)
- [Qwen2 0.5B/1.5B/7B/72B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/qwen2.html.md#qwen2)
- [Qwen3 0.6B/1.7B/4B/8B/14B/32B/30B_A3B/235B_A22B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/qwen3.html.md#qwen3)
- [StarCoder 15B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/starcoder.html.md#starcoder)
- [StarCoder2 3B/7B/15B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/starcoder2.html.md#starcoder2)
- [BERT 110M/340M](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/bert.html.md#bert)
- [T5 220M/3B/11B](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/t5.html.md#t5)
- [NeVA (LLaVA 1.5)](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/neva.html.md#neva)
- [Llama 3.2 Vision 11B/90B](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/mllama.html.md#mllama)
- [LLaVA Next (LLaVA 1.6)](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/llavanext.html.md#llavanext)
- [Llama Nemotron Nano VL 8B](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/llama_nemotron_vl.html.md#llama-nemotron-vl)
- [SBERT 340M](https://docs.nvidia.com/nemo-framework/user-guide/latest/embeddingmodels/bert/sbert.html.md#sbert)
- [Llama 3.2 Embedding 1B](https://docs.nvidia.com/nemo-framework/user-guide/latest/embeddingmodels/gpt/llama_embedding.html.md#llama-embed)
- [Cosmos-1.0-Diffusion-Text2World-7B](https://huggingface.co/nvidia/Cosmos-1.0-Diffusion-7B-Text2World)
- [Yes](https://github.com/NVIDIA/Cosmos/blob/main/cosmos1/models/autoregressive/nemo/inference/README.md)
- [Cosmos-1.0-Diffusion-Text2World-14B](https://huggingface.co/nvidia/Cosmos-1.0-Diffusion-14B-Text2World)
- [Cosmos-1.0-Autoregressive-4B](https://huggingface.co/nvidia/Cosmos-1.0-Autoregressive-4B)
- [Cosmos-1.0-Autoregressive-12B](https://huggingface.co/nvidia/Cosmos-1.0-Autoregressive-12B)
- [diffusion](https://github.com/NVIDIA/NeMo/tree/main/nemo/collections/diffusion)
- [autoregressive](https://github.com/NVIDIA/NeMo/tree/main/nemo/collections/multimodal_autoregressive)
- [NVIDIA Riva](https://developer.nvidia.com/riva.md)
- [Speech Classification](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speech_classification/intro.html.md)
- [Speaker Recognition](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_recognition/intro.html.md)
- [Speaker Diarization](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_diarization/intro.html.md)
- [ASR](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/results.html.md)
- [TTS](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/checkpoints.html.md)
- [Speech Tools](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tools/intro.html.md)
- [NeMo Forced Aligner (NFA)](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tools/nemo_forced_aligner.html.md)
- [Speech Data Processor (SDP)](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tools/speech_data_processor.html.md)
- [Speech Data Explorer (SDE)](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tools/speech_data_explorer.html.md)
- [Dataset creation tool](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tools/ctc_segmentation.html.md)
- [ASR Evaluator](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tools/asr_evaluator.html.md)
- [Text Normalization Tool](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/nlp/text_normalization/intro.html.md)
- [Quickstart Guide](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/starthere/intro.html.md)
- [Tutorial Notebooks](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/starthere/tutorials.html.md)
- [NeMo](https://github.com/NVIDIA/NeMo)
- [NeMo Discussions](https://github.com/NVIDIA/NeMo/discussions)
- [NeMo Issues](https://github.com/NVIDIA/NeMo/issues)
- [Apache 2.0 license](https://github.com/NVIDIA/NeMo?tab=Apache-2.0-1-ov-file#readme)
- [NVIDIA AI PRODUCT AGREEMENT](https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/)
- [Meta Llama3 Community License Agreement](https://huggingface.co/meta-llama/Meta-Llama-3-8B/tree/main)
