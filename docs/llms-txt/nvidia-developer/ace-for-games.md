# Source: https://developer.nvidia.com/ace-for-games.md

1. [Home](/)

[ACE](https://developer.nvidia.com/ace)

ACE for Games

# NVIDIA ACE for Games

NVIDIA ACE is a suite of digital human technologies for middleware and game developers that powers knowledgeable, actionable and conversational game characters using generative AI. ACE provides ready-to-integrate cloud and on-device AI models for each aspect of digital humans—from speech to intelligence to animation.

[Get Started  
](#section-getting-started &quot;Github Repo&quot;)[Notify Me](https://developer.nvidia.com/ace-for-games/notify-me &quot;Github Repo&quot;)

 ![A digital human powered by NVIDIA ACE Unreal Engine 5](https://developer.download.nvidia.com/images/ace-for-gamedev/Hiroki1.png)
* * *
 
## Key Benefits

### **Models Purpose Built for Gaming**

ACE offers a curated suite of AI models—from speech, vision and intelligence to realistic animation and behavior built to enhance game assistants, actors and agents

### Optimized for On-Device Inference 

AI models fine-tuned and optimized for gaming hardware, provide high accuracy and low latency within a small memory footprint.

### Inference Alongside Graphics   

[NVIDIA In-Game Inferencing](https://developer.nvidia.com/rtx/in-game-inferencing) (NVIGI) plugins schedule AI inference for different models and inference backends across complex graphics workloads to maximize performance and the user experience.

* * *

## Partner Experiences Powered by AI  

NVIDIA ACE is being used by industry-leading game developers and ISVs to build autonomous game characters that inhabit living, breathing worlds and AI assistants that provide tips and guidance to gamers and creators.

### Autonomous Agents  

KRAFTON’s inZOI features Smart Zois, AI-driven agents that plan, act and reflect on their decisions for unique character dynamics.

https://www.youtube-nocookie.com/embed/Pk9z1upOj3U?
 

### Autonomous Companions  

KRAFTON’s PUBG introduces Co-Player Characters (CPC), AI-driven allies that communicate with natural language and act autonomously like a human teammate.

https://www.youtube-nocookie.com/embed/wEKUSMqrbzQ?
 

### Autonomous Enemies  

Wemade Next’s MIR5 introduces AI-powered bosses that continuously learn from previous player tactics to adapt and provide unique fights every run.

https://www.youtube-nocookie.com/embed/-8XeiZ4djKw?

### Conversational Game Characters

Dead Meat is a first of its kind murder mystery interrogation game where players can ask the suspect absolutely anything using their own words.

https://www.youtube-nocookie.com/embed/PFwIVnDU8KM?

### AI Assistants

Streamlabs and Inworld AI introduce an intelligent streaming assistant that serves as a producer, technical assistant and 3D sidekick.

https://www.youtube-nocookie.com/embed/909h0VZeOMM?

* * *

## Get Started with NVIDIA ACE

The [NVIDIA In-Game Inferencing](https://developer.nvidia.com/blog/bring-nvidia-ace-ai-characters-to-games-with-the-new-in-game-inference-sdk/?ncid=so-nvsh-920422) (NVIGI) SDK offers a streamlined and high performance path to integrate locally run AI models into games and applications via in-process (C++) execution and CUDA in Graphics. NVIGI supports all major inference backends, across different hardware accelerators (GPU, NPU, CPU), so developers can take advantage of the full range of available system resources on a user’s PC.

[Download NVIGI SDK](https://developer.nvidia.com/rtx/in-game-inferencing)

[Documentation](https://github.com/NVIDIA-RTX/NVIGI-Core)

[Compatibility Matrix](https://forums.developer.nvidia.com/t/ace-compatibility-table/334024)

[Archive](/rtx/in-game-inferencing#section-archive)

Animation

Intelligence

Speech

### NVIDIA® Riva ASR 

Takes an audio stream as input and returns a text transcript in real time. It’s NVIDIA GPU-accelerated for maximum performance and accuracy.

[Access Model Card](https://developer.nvidia.com/downloads/assets/ace/model_card/RIVA_Conformer_ASR_English.pdf)

[Download On-Device Model](https://developer.nvidia.com/downloads/assets/ace/model_zip/riva_pack_ga_1_0_0.zip)

[Access Cloud Model](https://build.nvidia.com/nvidia/parakeet-ctc-0_6b-asr/deploy)

[Documentation](https://docs.nvidia.com/deeplearning/riva/user-guide/docs/asr/asr-overview.html)

### Whisper ASR

Takes an audio stream as input and returns a text transcript in real time. It’s compatible with NVIDIA GPUs and any CPUs.

[Access Model Card](https://developer.nvidia.com/downloads/assets/ace/model_card/Whisper_ASR.pdf)

[Download On-Device Model](https://developer.nvidia.com/downloads/assets/ace/model_zip/whisper_asr_gguf_v1.0.7z)

[Access Cloud Model](https://build.nvidia.com/openai/whisper-large-v3)

[Documentation](https://github.com/NVIDIA-RTX/NVIGI-Plugins/blob/main/docs/ProgrammingGuideASRWhisper.md)

### Riva TTS  

Takes a text output and converts it into natural and expressive voices in multiple languages in real time. Built for agentic workflows and compatible with multi-vendor GPUs and CPUs. FP16 quantization offers higher accuracy for higher VRAM usage.

[Access Model Card](https://developer.nvidia.com/downloads/assets/ace/model_zip/riva-magpie-tts-flow-1p0.zip)

[Download On-Device Model (FP16)](https://developer.nvidia.com/downloads/rtx/In-Game-Inference-SDK/riva-magpie-tts-flow-ggml-1p5-fp16.zip)

[Download On-Device Model (Q4)](https://developer.nvidia.com/downloads/rtx/In-Game-Inference-SDK/riva-magpie-tts-flow-ggml-1p5-q4.zip)

[Access Cloud Model](https://build.nvidia.com/nvidia/magpie-tts-flow)

[Documentation](https://github.com/NVIDIA-RTX/NVIGI-Plugins/blob/main/docs/ProgrammingGuideTTSASqFlow.md)

### Qwen3-8B

8B parameter open source dense model optimized for on-device inference. Qwen3 delivers groundbreaking advancements in reasoning, instruction-following, agent capabilities, and multilingual support. It&#39;s compatible with multi-vendor GPUs and CPUs.

[Access Model Card](https://developer.nvidia.com/downloads/assets/ace/model_card/qwen3-8b-instruct.pdf)

[Download On-Device Model](https://developer.nvidia.com/downloads/assets/ace/model_zip/qwen3-8b-ggml.zip)

[Documentation](https://huggingface.co/Qwen/Qwen3-8B)

### Mistral-Nemo-Minitron Family

Agentic small language models that enable better role-play, retrieval-augmented generation (RAG) and function calling capabilities. They come in 8B, 4B and 2B parameter models to fit your VRAM and performance requirements. The on-device models are compatible with multi-vendor GPUs and CPUs.

[Access Model Card](https://developer.nvidia.com/downloads/assets/ace/model_card/Mistral-NeMo-Minitron-8B-128K-Instruct.pdf)

[Download On-Device 2B Model](https://developer.nvidia.com/downloads/assets/ace/model_zip/mistral-nemo-minitron-2b-128k-instruct_v1.0.0.7z)

[Download On-Device 4B Model](https://developer.nvidia.com/downloads/assets/ace/model_zip/mistral-nemo-minitron-4b-128k-instruct_v1.0.0.7z)

[Download On-Device 8B Model](https://developer.nvidia.com/downloads/assets/ace/model_zip/mistral-nemo-minitron-8b-128k-instruct_v1.0.0.7z)

[Documentation](https://github.com/NVIDIA-RTX/NVIGI-Plugins/blob/main/docs/ProgrammingGuideGPT.md)

### Llama3.2-3B-Instruct  

Agentic small language model that enables better role-play, retrieval-augmented generation (RAG) and function calling capabilities. This model is compatible with multi-vendor GPUs and CPUs.

[Access Model Card](https://developer.nvidia.com/downloads/assets/ace/model_card/llama-3.2-3b_for_Nv_IGI_SDK.pdf)

[Download On-Device Model](https://developer.nvidia.com/downloads/assets/ace/model_zip/llama-3.2-3b_v1.0.1.7z)

[Access Cloud Card](https://build.nvidia.com/meta/llama-3.2-3b-instruct/deploy)

[Documentation](https://github.com/NVIDIA-RTX/NVIGI-Plugins/blob/main/docs/ProgrammingGuideGPT.md)

### Nemovision-4B-Instruct  

Agentic vision-language model that combines visual understanding of on-screen elements and actions and reasons for better context aware responses. The on-device model is compatible with multi-vendor GPUs and CPUs.

[Access Model Card](https://developer.nvidia.com/downloads/assets/ace/model_card/mistral-nemotron-vision-4b-instruct_modelcard.pdf)

[Download On-Device Model](https://developer.nvidia.com/downloads/assets/ace/model_zip/mistral-nemotron-vision-4b-instruct_vv1.7z)

[Documentation](https://github.com/NVIDIA-RTX/NVIGI-Plugins/blob/main/docs/ProgrammingGuideGPT.md#90-vlm-visual-lanuage-models)

### Audio2Face-3D SDK  

Use AI to convert streaming audio to facial blendshapes for real-time lip-syncing and facial animations on-device or in the cloud. The SDK contains C++ and Python source code through the MIT license.

[Download Audio2Face-3D SDK](https://github.com/NVIDIA/Audio2Face-3D-SDK)

[Documentation](https://github.com/NVIDIA/Audio2Face-3D-SDK/tree/main/docs)

### Audio2Face-3D Models  

Audio2Face-3D regression (2.3) and diffusion (3.0) to generate lip-sync. Open weights in ONNX-TRT format available through the NVIDIA Open Model License. Unreal Engine models require the use of the ACE Unreal Engine Plugin.

[Download Audio2Face 3.0 Unreal Engine Models](https://developer.nvidia.com/downloads/assets/ace/ace_3.0_a2f_models.zip)

[Download Audio2Face 2.3 Unreal Engine Models](https://developer.nvidia.com/downloads/assets/ace/ace_2.5_v2.3_a2f_models.zip)

[Download Audio2Face-3D 3.0 Open Source Models](https://huggingface.co/collections/nvidia/audio2face-3d-6865d22d6daec4ac85887b17)

### Audio2Emotion-3D Models  

Audio2Emotion production (2.2) and experimental (3.0) models to infer emotional state from audio. Open weights in ONNX-TRT format available through a custom license.

[Download Audio2Emotion 3.0 Models](https://huggingface.co/nvidia/Audio2Emotion-v3.0)

[Download Audio2Emotion 2.2 Models](https://huggingface.co/nvidia/Audio2Emotion-v2.2)

### Audio2Face-3D Plugins  

The Audio2Face-3D plug-in for Unreal Engine 5 alongside a configuration sample enhances your Metahuman experience. The Autodesk Maya ACE plugin generates high-quality, audio-driven facial animation offline. Both plugins are available under the MIT license.

[Download Unreal Engine Gaming Sample](https://developer.nvidia.com/downloads/assets/ace/aceunrealsample-1.0.0.7z)

[Download Unreal Engine 5.6 Plugin](https://developer.nvidia.com/downloads/assets/ace/nv_ace_reference-ue5.6-v2.5.0rc3.zip)

[Download Unreal Engine 5.5 Plugin](https://developer.nvidia.com/downloads/assets/ace/nv_ace_reference-ue5.5-v2.5.0rc3.zip)

[Download Unreal Engine 5.4 Plugin](https://developer.nvidia.com/downloads/assets/ace/nv_ace_reference-ue5.4-v2.4.0.zip)

[Documentation](https://docs.nvidia.com/ace/ace-unreal-plugin/2.5/)

[Download Maya ACE Plugin and Documentation](https://github.com/NVIDIA/Maya-ACE)

### Audio2Face-3D Training  

Audio2Face-3D training framework allows developers to create Audio2Face-3D models with your data. Source code is available in Python through the Apache license. Leverage audio files, blendshape data, animated geometry caches, geometry files and transform files to get started with the training framework. The sample data is available through a custom license for evaluation only.

[Download Training Framework](https://github.com/NVIDIA/Audio2Face-3D-training-framework)

[Download Training Sample Data](https://huggingface.co/datasets/nvidia/Audio2Face-3D-Dataset-v1.0.0-claire)

* * *

## More Resources

 ![A decorative image representing Developer Community](https://developer.download.nvidia.com/icons/m48-people-group.svg)

### Developer Discord

 ![img-alt-text](https://developer.download.nvidia.com/icons/m48-email-settings.svg)

### Sign up for Developer Newsletter

* * *

## On-Demand Sessions

* * *

## Ethical AI

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.   
  
For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety &amp; Security, and Privacy Subcards. Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

Ready to try NVIDIA ACE?

[Get Started](#section-getting-started)


