# Source: https://developer.nvidia.com/nemo-curator.md

1. [Topics](https://developer.nvidia.com/topics/)

[AI](https://developer.nvidia.com/topics/ai)
2. [Generative AI](https://developer.nvidia.com/generative-ai)

NVIDIA NeMo Curator  

# NVIDIA NeMo Curator for Developers

[NVIDIA NeMo](https://www.nvidia.com/en-us/ai-data-science/products/nemo/)™ Curator improves generative AI model accuracy by processing text, image, and video data at scale for training and customization. It also provides prebuilt pipelines for generating synthetic data to customize and evaluate generative AI systems.  
  
With NeMo Curator, part of the [NVIDIA NeMo](https://www.nvidia.com/en-us/ai-data-science/products/nemo/) software suite for managing the AI agent lifecycle, developers can curate high-quality data and train highly accurate generative AI models for various industries, including finance, retail, manufacturing and telecommunications.  
  
NeMo Curator, along with [NeMo microservices](https://developer.nvidia.com/blog/maximize-ai-agent-performance-with-data-flywheels-using-nvidia-nemo-microservices/) enables developers to create [data flywheels](https://www.nvidia.com/en-us/glossary/data-flywheel/) and continuously optimize generative AI agents, enhancing the overall experience for end users.

[Download  
](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/nemo-curator &quot;Github Repo&quot;)[Documentation  
](https://docs.nvidia.com/nemo/curator/latest/ &quot;Download Workflows&quot;)[Forum  
](https://forums.developer.nvidia.com/tags/c/ai-data-science/nvidia-nemo/715/nemo-curator &quot;Download Workflows&quot;)

* * *

## How NVIDIA NeMo Curator Works

NeMo Curator streamlines data-processing tasks, such as data downloading, extraction, cleaning, quality filtering, deduplication, and blending or shuffling, providing them as Pythonic APIs, making it easier for developers to build data-processing pipelines. High-quality data processed from NeMo Curator enables you to achieve higher accuracy with less data and faster model convergence, reducing training time.   
  
NeMo Curator supports the processing of text, image, and video modalities and can scale up to 100+ PB of data.  
  
NeMo Curator provides a customizable and modular interface, allowing you to select the building blocks for your data processing pipelines. Please refer to the architecture diagrams below to see how you can build data processing pipelines.

### Text Data Processing

This architecture diagram shows the various features available for processing text. At a high level, a typical text processing pipeline begins with downloading data from public sources or private repositories and performing cleaning steps, such as fixing Unicode characters. Next, heuristic filters—such as word count—are applied, followed by deduplication, advanced quality filtering using [classifier models](https://huggingface.co/collections/nvidia/nemo-curator-classifier-models-66b25154213dafdcb8bde900) for quality and domain, and finally, data blending.

_Click to Enlarge_

[![NeMo Curator lets you use prebuilt synthetic data generation pipelines or build your own with easy-to-use set of tools](https://developer.download.nvidia.com/images/nemo-curator-sdg-general-arch.png)](https://developer.download.nvidia.com/images/nemo-curator-sdg-general-arch.png)
_Click to Enlarge_

### Synthetic Data Generation  

NeMo Curator has a simple, easy-to-use set of tools that let you use pre-built [synthetic data generation](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/syntheticdata.html) pipelines or build your own. Any model inference service that uses the OpenAI API is compatible with the synthetic data generation module, allowing you to generate your data from any model.  
  
NeMo Curator provides pre-built pipelines for several use cases to help you get started easily, including evaluating and customizing embedding models, prompt generation (open Q&amp;A, closed Q&amp;A, writing, math/coding), synthetic two-turn prompt generation, dialogue generation, and entity classification.

### Video Data Processing  

This architecture diagram illustrates the various features available through the early access program for processing high-quality videos.  
  
A typical pipeline has the following steps

- 
**Video decoding and splitting** : Decode long videos and split them into semantically shorter clips.
- 

**Transcoding** : Convert all the short videos to a consistent format.

- 

**Captioning** : Caption videos using domain-specific state-of-the-art vision language models (VLMs) to describe the clips in detail.

- 
**Text embedding** : Create embeddings of text captions for downstream semantic search and deduplication.

[![NeMo Curator supports the processing of video modalities](https://developer.download.nvidia.com/images/nemo-curator/nemo-video-data-processing.jpg)](https://developer.download.nvidia.com/images/nemo-curator/nemo-video-data-processing.jpg)
_Click to Enlarge_

_Click to Enlarge_

### Audio Data Processing  

This architecture diagram shows the various features available for processing audio.  
  
A typical pipeline has the following steps

- 

**Data download and extraction** : Fetch audio files from cloud, internet, or local disk sources.

- 

**Speech-to-text inference** : Transcribe audio with a NeMo ASR model, using GPU acceleration for speed.

- 

**Metric calculation (WER)**: Compute Word Error Rate to assess transcription accuracy.

- 

**Get audio duration** : Extract duration metadata for each file.

- 

**Feature-based filtering** : Filter samples by WER and duration thresholds.

- 

**Metadata conversion** : Transform curated outputs to document format and export as JSONL.

### Image Data Processing  

This architecture diagram shows the various features available for processing images.  
  
A typical pipeline begins with downloading the dataset in a WebDataset format, followed by creating CLIP embeddings. Next, the images are filtered for high quality using the NSFW and Aesthetic filters. Duplicate images are then removed using semantic deduplication, and finally, a high-quality dataset is created.

_Click to Enlarge_

* * *

## Introductory Resources  

### Introductory Blog  

Learn about the various features NeMo Curator offers for processing high-quality data in this introductory blog.

[Read Blog](https://developer.nvidia.com/blog/scale-and-curate-high-quality-datasets-for-llm-training-with-nemo-curator/)

### Tutorials

These tutorials provide the coding foundation for building applications that consume the data that NeMo Curator curates.

[Explore the Notebooks](https://github.com/NVIDIA/NeMo-Curator/tree/main/tutorials)

### Introductory Webinar  

Explore how to easily build scalable data-processing pipelines to create high-quality datasets for training and customization.

[Register Now](https://www.nvidia.com/en-us/events/enhance-generative-ai-model-accuracy/)

### Documentation  

These docs provide an in-depth overview of the various features supported, best practices, and tutorials.

[Read Documentation](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/index.html)

* * *

## Ways to Get Started With NVIDIA NeMo Curator  

Use the right tools and technologies to generate high-quality datasets for large language model (LLM) training.

 ![Decorative icon](https://developer.download.nvidia.com/icons/m48-download.svg)
### Download  

For those looking to use the NeMo framework for development, the container is available to download for free on the NVIDIA NGC™ catalog. 

[Pull Container](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/nemo)

 ![Decorative icon representing source code](https://developer.download.nvidia.com/images/icons/m48-coding-256px-blk.png)
### Access  

To use the latest pre-release features and source code, NeMo Curator is available as an open-source project on GitHub.

[Access Code](https://github.com/NVIDIA/NeMo-Curator)

* * *

## Performance

NeMo Curator leverages NVIDIA RAPIDS™ libraries like cuDF, cuML, and cuGraph along with Ray to scale workloads across multi-node, multi-GPU environments, significantly reducing data processing time. For video processing, it uses a combination of a hardware decoder (NVDEC) and a hardware encoder (NVENC) as well as Ray to avoid bottlenecks and ensure high performance. With NeMo Curator, developers can achieve 16x faster processing for text and 89x faster processing for video when compared to alternatives. Refer to the charts below for more details.

### Accelerate Video Processing From Years to Days With NeMo Curator

Processing time for 20 million hours of video.

 ![](https://developer.download.nvidia.com/images/nemo-curator/accelerate-video-processing@2x.svg)

\* Performance compared with ISO power consumption on 2,000 CPUs and 128 DGX nodes​ 

### 16x Faster Text Processing Time With NeMo Curator

Processing time for fuzzy duplication of the RedPajama-v2 subset (8 TB).

 ![](https://developer.download.nvidia.com/images/nemo-curator/16x-faster-text-processing-time@2x.svg)

**‘“On”** : Data processed with NeMo Curator ​  
**“Off”** : Data processed with a leading alternative library on CPUs

* * *

## Starter Kits

Start developing your generative AI application with NeMo Curator by accessing [tutorials](https://github.com/NVIDIA/NeMo-Curator/tree/main/tutorials), [best practices](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/bestpractices.html#data-curator-best-practices), and [documentation](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/index.html) for various use cases.

### Text Processing  

Process high-quality text data with features such as deduplication, quality filtering, and synthetic data generation.

- 
[Read Processing Custom Datasets for LLM Training Blog](https://developer.nvidia.com/blog/curating-custom-datasets-for-llm-training-with-nvidia-nemo-curator/)
- 
[Read Processing Non-English Datasets Blog](https://developer.nvidia.com/blog/curating-non-english-datasets-for-llm-training-with-nvidia-nemo-curator/)
- 
[Read Synthetic Data Generation With Llama 3.1-405B Blog](https://github.com/NVIDIA/NeMo-Curator/tree/main/tutorials/synthetic-preference-data)

### Image Processing  

Process high-quality image data with features such as semantic deduplication, CLIP image embedding, NSFW, and aesthetic filters.

- 
[Explore Image Curation Tutorial](https://github.com/NVIDIA/NeMo-Curator/blob/main/tutorials/image-curation/image-curation.ipynb)
- 
[Read Image Curation Documentation](https://github.com/NVIDIA/NeMo-Curator/tree/main/docs/user-guide/image)

### Audio Processing  

Process high-quality audio data with features such as splitting, transcoding, filtering, annotation, and semantic deduplication.

- 
[Explore Tutorial](https://github.com/NVIDIA-NeMo/Curator/tree/main/tutorials/audio)

### Video Processing  

Process high-quality video data with features such as splitting, transcoding, filtering, annotation, and semantic deduplication.

- 
[Apply for Early Access](https://developer.nvidia.com/nemo-early-access)
- 
[Read Video Tokenization Blog](https://developer.nvidia.com/blog/state-of-the-art-multimodal-generative-ai-model-development-with-nvidia-nemo/)
- 
[Read Video Foundation Model Blog](https://developer.nvidia.com/blog/accelerate-custom-video-foundation-model-pipelines-with-new-nvidia-nemo-framework-capabilities/)
- 
[Watch Video Foundation Model Video](https://youtu.be/dqP-I59wUwU)

* * *

## NVIDIA NeMo Curator Learning Library

* * *

## NVIDIA NeMo Curator Customers

[![NVIDIA NeMo Curator Customer - Coxwave](https://developer.download.nvidia.com/images/nemo-curator/coxwave-logo.svg)](https://developer.nvidia.com/blog/boost-embedding-model-accuracy-for-custom-information-retrieval/?fbclid=IwY2xjawLP6XtleHRuA2FlbQIxMABicmlkETFSZEhFUlJMYWxZeDVJemNiAR7ULxRvqhXiFwxG5F6w8ePItciehZLWchmUn2hUsfd5S6NqkUZG0_Rn6ISEMQ_aem_92ItzMFCBI3O0D97XWxUnw)

[![NVIDIA NeMo Curator Customer - gnani.ai](https://developer.download.nvidia.com/images/nemo-curator/gnani.ai-logo.svg)](https://www.nvidia.com/en-us/on-demand/session/gtc25-s71829/)

[![NVIDIA NeMo Curator Customer - Petrobras](https://developer.download.nvidia.com/images/nemo-curator/petrobras-logo.svg)](https://www.nvidia.com/en-us/on-demand/session/gtc25-s73150/)

[![NVIDIA NeMo Curator Customer - Quantiphi](https://developer.download.nvidia.com/images/nemo-curator/quantiphi-logo.svg)](https://quantiphi.com/blog/optimizing-ai-with-fine-tuned-slms-boost-efficiency-in-telecom-using-nvidia-nemo-microservices/)

[![NVIDIA NeMo Curator Customer - SES](https://developer.download.nvidia.com/images/nemo-curator/ses-ai-logo.svg)](https://developer.nvidia.com/blog/accelerating-the-future-of-transportation-with-ses-ais-nvidia-powered-innovation-for-electric-vehicles/)

[![NVIDIA NeMo Curator Customer - Trillion Labs](https://developer.download.nvidia.com/images/nemo-curator/trillion-labs-logo.svg)](https://www.nvidia.com/en-us/on-demand/session/gtc25-s73857/)

[![NVIDIA NeMo Curator Customer - Viettel Solutions](https://developer.download.nvidia.com/images/nemo-curator/viettel-solutions-logo.svg)](https://developer.nvidia.com/blog/processing-high-quality-vietnamese-language-data-with-nvidia-nemo-curator/)

[![NVIDIA NeMo Curator Customer - Zyphra](https://developer.download.nvidia.com/images/nemo-curator/zyphra-logo.svg)](https://developer.nvidia.com/blog/train-highly-accurate-llms-with-the-zyda-2-open-5t-token-dataset-processed-with-nvidia-nemo-curator/)

* * *

## More Resources

 ![Decorative image representing forums](https://developer.download.nvidia.com/images/omniverse/m48-people-group.svg)
### Explore the Community  

 ![](https://developer.download.nvidia.com/images/isaac/m48-certification-ribbon-2-256px-blk.png)
### Get Training and Certification  

 ![](https://developer.download.nvidia.com/images/isaac/m48-ai-startup-256px-blk.png)
### Accelerate Your Startup  

* * *

## Ethical AI   

NVIDIA’s platforms and application frameworks enable developers to build a wide array of AI applications. Consider potential algorithmic bias when choosing or creating the models being deployed. Work with the model’s developer to ensure that it meets the requirements for the relevant industry and use case; that the necessary instruction and documentation are provided to understand error rates, confidence intervals, and results; and that the model is being used under the conditions and in the manner intended.

Get started with NVIDIA NeMo Curator.

[Download Now](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/nemo-curator)


