# Source: https://developer.nvidia.com/cosmos.md

1. [Topic](/topics/)

[Artificial Intelligence](/topics/ai/)

Cosmos  

# NVIDIA Cosmos for Developers

[NVIDIA Cosmos™](http://www.nvidia.com/en-us/ai/cosmos) is a platform purpose-built for physical AI, featuring state-of-the-art generative [world foundation models](https://www.nvidia.com/en-us/glossary/world-models/) (WFMs), guardrails, and an accelerated data processing and curation pipeline for [autonomous vehicle (AV)](https://www.nvidia.com/en-us/use-cases/autonomous-vehicle-simulation/), [robotics](https://www.nvidia.com/en-us/solutions/robotics-and-edge-computing/), and [AI agent developers](https://www.nvidia.com/en-us/use-cases/video-analytics-ai-agents/).  
  
Build, evaluate, deploy, and simulate [physical AI](https://www.nvidia.com/en-us/glossary/physical-ai/) models faster while minimizing testing and validation risks in the real world.

[Download from GitHub](https://github.com/nvidia-cosmos)[Documentation  
](http://docs.nvidia.com/cosmos)[Cookbook](https://nvidia-cosmos.github.io/cosmos-cookbook/)

 
* * *

## How It Works
 ![Diagram showing the application and Omniverse Cloud using USD framework](https://developer.download.nvidia.com/images/cosmos/nvidia-cosmos-how-it-works-diagram-ari.jpg)

Cosmos WFMs accelerate physical AI development, helping developers augment datasets and post-train downstream world models for robots and autonomous vehicles.  
  
[Cosmos Predict](https://huggingface.co/collections/nvidia/cosmos-predict1-67c9d1b97678dbf7669c89a7) generates next frames based on input to build datasets predicting various edge cases and serves as the foundation for all world models.  
  
[Cosmos Reason](https://huggingface.co/collections/nvidia/cosmos-reason1-67c9e926206426008f1da1b7) acts as a critic, using chain-of-thought reasoning to evaluate synthetic visuals and reward outcomes. It can also generate captions to speed up data curation.  
  
[Cosmos Transfer](https://huggingface.co/collections/nvidia/cosmos-reason1-67c9e926206426008f1da1b7) amplifies structured video across various environments and lighting conditions.  
  
Developers can use the available PyTorch inference and post-training scripts along with model checkpoints. Cosmos NIM microservices are in development—Cosmos Predict NIM microservices are available [here](https://build.nvidia.com/search?q=%22cosmos%22+-nemotron).

* * *

## NVIDIA Cosmos World Foundation Models

A family of pretrained models for world generation as videos and world understanding for accelerating physical AI development. Available openly to developers on NGC, Hugging Face, and [GitHub](https://github.com/nvidia-cosmos).

### Cosmos Predict 

For future world state generation or as a base for custom world models.  
  
Input: Text or Image  
  
Output: Video 

[Get Started on GitHub](https://github.com/nvidia-cosmos/cosmos-predict2.5)

[Try Model Checkpoint on Hugging Face](https://huggingface.co/nvidia/Cosmos-Predict2.5-2B)

### Cosmos Transfer  

Multicontrol net for fast, photorealistic video data augmentation.  
  
Input: Segmentation maps, depth signals, HD maps, or CG simulation videos.  
  
Pair with: NVIDIA Omniverse  
  
Output: Photorealistic world scenes

[Get Started on GitHub](https://github.com/nvidia-cosmos/cosmos-transfer2.5)

[Try Model Checkpoint on Hugging Face](https://huggingface.co/nvidia/Cosmos-Transfer2.5-2B)

### Cosmos Reason  

World reasoning for synthetic data curation, robot decision-making, and runtime video analytics for AI agents.   
  
Input: Image or Video  
  
Output: Chain-of-thoughts reasoning and text

[Experience Model as NVIDIA NIM API](https://build.nvidia.com/nvidia/cosmos-reason1-7b)[Get Started on GitHub](https://github.com/nvidia-cosmos/cosmos-reason1)

### Cosmos Curator  

Filter, annotate, and deduplicate large datasets for physical AI development using advanced AI models and distributed computing.

[Get Started](https://github.com/nvidia-cosmos/cosmos-curate)

### Cosmos Dataset Search

Instantly search and retrieve scenarios from massive training datasets for targeted post-training using the Cosmos Dataset Search vector-based search workflow.

[Try Now](https://build.nvidia.com/nvidia/cosmos-dataset-search)

### Cosmos Guardrails  

A set of guardrails, including a pre-guard to block harmful inputs and a post-guard to ensure safety and consistency in generations.

[Download Cosmos Guardrail](https://huggingface.co/nvidia/Cosmos-1.0-Guardrail)

### Cosmos Prompt Upsampler

Transform original input prompts into more detailed and enriched versions for higher-quality outputs from Cosmos WFMs.

[Download Cosmos Prompt Upsampler](https://huggingface.co/nvidia/Cosmos-1.0-Prompt-Upsampler-12B-Text2World)

### Sample AV Models

Try sample post-trained Cosmos models specialized for autonomous vehicle development, including multi-view and lidar generation.

[Try Now](https://github.com/nv-tlabs/Cosmos-Drive-Dreams)

## Introductory Resources  

### Cosmos Cookbook: A Practical Guide to Physical AI Models

The Cosmos Cookbook is an open-source guide with step-by-step workflows and examples for deploying and customizing NVIDIA Cosmos world foundation models in real-world applications.

[Read Cookbook](https://nvidia-cosmos.github.io/cosmos-cookbook/)

### Updated Versions of Cosmos Predict 2.5 &amp; Transfer 2.5

Cosmos Predict 2.5 and Transfer 2.5 advance NVIDIA’s world foundation models by unifying multimodal world generation and improving spatially controlled world transformation, driving scalable, efficient physical AI.

[Read Hugging Face Blog](https://huggingface.co/blog/nvidia/cosmos-predict-and-transfer2-5)

### World Simulation With Video Foundation Models 

This NVIDIA Cosmos white paper presents an open platform of world foundation models, video curation tools, and tokenizers to help developers efficiently customize, generate, and simulate physics-based data for advancing physical AI applications like robotics and autonomous vehicles.

[Read White Paper](https://research.nvidia.com/publication/2025-09_world-simulation-video-foundation-models-physical-ai)

* * *

## Starter Kits  

Start solving physical AI challenges by developing custom world models with Cosmos or using Cosmos WFMs for downstream use cases. Explore implementation scripts, explainer blogs, and more how-to documentation for various stages of physical AI development.

### Post-Training Cosmos WFMs  

Cosmos WFMs are purpose-built for post-training. Use domain-specific datasets to build world models, or post-train for different types of output, such as action generation for policy models.

- 

[Post-Training Cookbook](https://github.com/nvidia-cosmos/cosmos-cookbook)

- 

[Cosmos Tokenizer Documentation](https://research.nvidia.com/labs/dir/cosmos-tokenizer/) and [Script](https://docs.nvidia.com/cosmos/latest/predict1/tokenizer/index.html)

- 

[NVIDIA NeMo™ Data Curator Early Access](/nemo-microservices)

- 

[Physical AI Open Dataset](https://huggingface.co/collections/nvidia/physicalai-67c643edbb024053dcbcd6d8)

### Synthetic Data Generation  

Build and deploy world models for infinite domain-specific synthetic data. Use NVIDIA Omniverse for physics-based conditioning.

- 

[Inference Script ](https://github.com/nvidia-cosmos/cosmos-transfer2.5/blob/main/docs/inference.md)

- 

[Workflow Guide and Documentation](https://docs.omniverse.nvidia.com/guide-sdg/latest/index.html)

- 

[Cosmos NVIDIA NIM™ Microservice](https://build.nvidia.com/search?q=%22cosmos%22+-nemotron)

- 

[Intro to Cosmos for Physical AI Course](https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-OV-42+V1)

- 

[Cosmos Synthetic Dataset Augmentation](https://docs.omniverse.nvidia.com/guide-sdg/latest/case-studies/case4.html)

### Vision-Language Models

Vision language models (VLMs) are multimodal, generative AI models that can understand and process video, images, and text.

- 

[Product Education Tech Blog](https://developer.nvidia.com/blog/maximize-robotics-performance-by-post-training-nvidia-cosmos-reason/)

- 

[Github Resources](https://github.com/nvidia-cosmos/cosmos-reason1)

- 

[Post-training Script](https://github.com/nvidia-cosmos/cosmos-reason1/blob/main/examples/post_training/README.md)

- 

[Cosmos Cookbook](https://nvidia-cosmos.github.io/cosmos-cookbook/)

- 

[Start Prototyping](https://build.nvidia.com/nvidia/cosmos-reason1-7b/deploy)

- 

[Documentation](https://docs.nvidia.com/cosmos/latest/reason1/quickstart_guide.html#)

### Video Analytics AI Agent

Build a video analytics AI agent using NVIDIA Cosmos Reason with NVIDIA Blueprint for video search and summarization (VSS). 

- 

[Product Education Tech Blog](https://developer.nvidia.com/blog/how-to-integrate-computer-vision-pipelines-with-generative-ai-and-reasoning/)

- 

[Try the Blueprint](https://build.nvidia.com/nvidia/video-search-and-summarization)

- 

[Github Resources](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization)

- 

[Deploy Launchable](https://brev.nvidia.com/launchable/deploy?launchableID=env-2tYIjRXL4eMCbH9Az8mJC5WPAI4)

- 

[Documentation](https://docs.nvidia.com/vss/latest/index.html#)

* * *

## Cosmos Learning Library

## 
* * *
More Resources

 ![NVIDIA Developer Forums](https://developer.download.nvidia.com/icons/m48-communication-chat.svg)
### GitHub Forums

 ![NVIDIA Training and Certification](https://developer.download.nvidia.com/icons/m48-misc-question-faq.svg)
### Read Cosmos FAQ  

 ![NVIDIA Inception Program for Startups](https://developer.download.nvidia.com/icons/m48-email-settings.svg)
### Sign Up for the   
Developer Newsletter

* * *

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility, and we have established policies and practices to enable development for a wide array of AI applications. When downloading or using this model in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.   
  
NVIDIA has collaborated with Google Deepmind to watermark generated videos from the NVIDIA API catalog.  
  
For more detailed information on ethical considerations for this model, please see the [System Card](https://nvdam.widen.net/s/knnqs6ghqn/nvidia-cosmos-system-card), Model Card++ Explainability, Bias, Safety &amp; Security, and Privacy Subcards. Please report security vulnerabilities or NVIDIA AI concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

**Get Started With NVIDIA Cosmos Today**

[Try Now  
](https://github.com/nvidia-cosmos)


