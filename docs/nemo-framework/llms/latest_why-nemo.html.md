# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/why-nemo.html.md

Title: Why NeMo Framework? — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/why-nemo.html

Published Time: Fri, 05 Sep 2025 18:59:42 GMT

Markdown Content:
Why NeMo Framework?[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/why-nemo.html.md#why-nemo-framework "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------

Developing deep learning models for Gen AI is a complex process, encompassing the design, construction, and training of models across specific domains. Achieving high accuracy requires extensive experimentation, fine-tuning for diverse tasks and domain-specific datasets, ensuring optimal training performance, and preparing models for deployment.

NeMo simplifies this intricate development landscape through its modular approach. It introduces neural modules—logical blocks of AI applications with typed inputs and outputs—facilitating the seamless construction of models by chaining these blocks based on neural types. This methodology accelerates development, improves model accuracy on domain-specific data, and promotes modularity, flexibility, and reusability within AI workflows.

Further enhancing its utility, NeMo provides collections of modules designed for core tasks in speech recognition, natural language processing, and speech synthesis. It supports the training of new models or fine-tuning of existing pre-trained modules, leveraging pre-trained weights to expedite the training process.

The framework encompasses models trained and optimized for multiple languages, including Mandarin, and offers extensive tutorials for conversational AI development across these languages. NeMo’s emphasis on interoperability with other research tools broadens its applicability and ease of use.

Large Language Models & Multimodal (LLM & MM)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/why-nemo.html.md#large-language-models-multimodal-llm-mm "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

NeMo excels in training large-scale LLM & MM, utilizing optimizations from the Megatron Core library and Transformer Engine to deliver state-of-the-art performance. It includes a comprehensive feature set for large-scale training:

*   Supports Multi-GPU and Multi-Node computing to enable scalability.

*   Precision options including FP32/TF32, FP16, BF16, and TransformerEngine/FP8.

*   Parallelism strategies: Data parallelism, Tensor parallelism, Pipeline parallelism, Interleaved Pipeline parallelism, Sequence parallelism and Context parallelism, Distributed Optimizer, and Fully Shared Data Parallel.

*   Optimized utilities such as Flash Attention, Activation Recomputation, and Communication Overlap.

*   Advanced checkpointing through the Distributed Checkpoint Format.

Speech AI[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/why-nemo.html.md#speech-ai "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

### Data Augmentation[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/why-nemo.html.md#data-augmentation "Link to this heading")

Augmenting ASR data is essential but can be time-consuming during training. NeMo advocates for offline dataset preprocessing to conserve training time, illustrated in a tutorial covering speed perturbation and noise augmentation techniques.

### Speech Data Explorer[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/why-nemo.html.md#speech-data-explorer "Link to this heading")

A Dash-based tool for interactive exploration of ASR/TTS datasets, providing insights into dataset statistics, utterance inspections, and error analysis. Installation instructions for this tool are available in NeMo’s GitHub repository.

### Using Kaldi Formatted Data[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/why-nemo.html.md#using-kaldi-formatted-data "Link to this heading")

NeMo supports Kaldi-formatted datasets, enabling the development of models with existing Kaldi data by substituting the AudioToTextDataLayer with the KaldiFeatureDataLayer.

### Speech Command Recognition[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/why-nemo.html.md#speech-command-recognition "Link to this heading")

Specialized training for speech command recognition is covered in a dedicated NeMo Jupyter notebook, guiding users through the process of training a QuartzNet model on a speech commands dataset.

General Optimizations[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/why-nemo.html.md#general-optimizations "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

### Mixed Precision Training[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/why-nemo.html.md#mixed-precision-training "Link to this heading")

Utilizing NVIDIA’s Apex AMP, mixed precision training enhances training speeds with minimal precision loss, especially on hardware equipped with Tensor Cores.

### Multi-GPU Training[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/why-nemo.html.md#multi-gpu-training "Link to this heading")

NeMo enables multi-GPU training, substantially reducing training durations for large models. This section clarifies the advantages of mixed precision and the distinctions between multi-GPU and multi-node training.

### NeMo, PyTorch Lightning, and Hydra[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/why-nemo.html.md#nemo-pytorch-lightning-and-hydra "Link to this heading")

Integrating PyTorch Lightning for training efficiency and Hydra for configuration management, NeMo streamlines conversational AI research by organizing PyTorch code and automating training workflows.

### Optimized Pretrained Models[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/why-nemo.html.md#optimized-pretrained-models "Link to this heading")

Through NVIDIA GPU Cloud (NGC), NeMo offers a collection of optimized, pre-trained models for various conversational AI applications, facilitating easy integration into research projects and providing a head start in conversational AI development.

Resources[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/why-nemo.html.md#resources "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

Ensure you are familiar with the following resources for NeMo.

*   Developer blogs
    *   [How to Build Domain Specific Automatic Speech Recognition Models on GPUs](https://developer.nvidia.com/blog/how-to-build-domain-specific-automatic-speech-recognition-models-on-gpus.md/)

    *   [Develop Smaller Speech Recognition Models with NVIDIA’s NeMo Framework](https://developer.nvidia.com/blog/develop-smaller-speech-recognition-models-with-nvidias-nemo-framework.md/)

    *   [Neural Modules for Fast Development of Speech and Language Models](https://developer.nvidia.com/blog/neural-modules-for-speech-language-models.md/)

*   Domain specific, transfer learning, Docker container with Jupyter Notebooks
    *   [Domain Specific NeMo ASR Application](https://ngc.nvidia.com/catalog/containers/nvidia:nemo_asr_app_img)

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/why-nemo.html.md#resources)
- [How to Build Domain Specific Automatic Speech Recognition Models on GPUs](https://developer.nvidia.com/blog/how-to-build-domain-specific-automatic-speech-recognition-models-on-gpus.md/)
- [Develop Smaller Speech Recognition Models with NVIDIA’s NeMo Framework](https://developer.nvidia.com/blog/develop-smaller-speech-recognition-models-with-nvidias-nemo-framework.md/)
- [Neural Modules for Fast Development of Speech and Language Models](https://developer.nvidia.com/blog/neural-modules-for-speech-language-models.md/)
- [Domain Specific NeMo ASR Application](https://ngc.nvidia.com/catalog/containers/nvidia:nemo_asr_app_img)
