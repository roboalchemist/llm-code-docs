# Source: https://firebase.google.com/docs/ai-logic/models.md.txt

<br />

For mobile and web apps, theFirebase AI LogicSDKs let you interact with the supported**Geminimodels** and**Imagenmodels**directly from your app.

Geminimodels are considered*multimodal* because they're capable of processing and even generating multiple modalities, including text, code, PDFs, images, video, and audio.Imagenmodels can be prompted with text to generate images.

Also, review our[FAQ](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#supported-models)about all the models thatFirebase AI Logicsupports and does not support.

## General use models

[arrow_downwardJump to model comparisons](https://firebase.google.com/docs/ai-logic/models#compare-models)  
OUR MOST INTELLIGENT MODEL

### Gemini 3 Pro

`gemini-3-pro-preview`

Our best model for multimodal understanding, and our most powerful agentic and vibe-coding model yet, delivering richer visuals and deeper interactivity, all built on a foundation of state-of-the-art reasoning.*(billing required)*  
OUR FASTEST MOST INTELLIGENT MODEL

### Gemini 3 Flash

`gemini-3-flash-preview`

Our most intelligent model built for speed, efficiency, and cost. It enables everyday tasks with improved reasoning, while still able to tackle the most complex agentic workflows.*(billing**not**required)*  

OUR ADVANCED THINKING MODEL

### Gemini 2.5 Pro

`gemini-2.5-pro`

Our state-of-the-art thinking model, capable of reasoning over complex problems in code, math, and STEM, as well as analyzing large datasets, codebases, and documents using long context.*(billing**not**required)*  
FAST AND INTELLIGENT

### Gemini 2.5 Flash

`gemini-2.5-flash`

Our best model in terms of price-performance, offering well-rounded capabilities. 2.5 Flash is best for large scale processing, low-latency, high volume tasks that require thinking, and agentic use cases.*(billing**not**required)*  
ULTRA FAST

### Gemini 2.5 Flash-Lite

`gemini-2.5-flash-lite`

Our fastest flash model optimized for cost-efficiency and high throughput.*(billing**not**required)*

## Image generating models

You can generate images with either[Gemini](https://firebase.google.com/docs/ai-logic/models#image-generating-models-gemini)or[Imagen](https://firebase.google.com/docs/ai-logic/models#image-generating-models-imagen)models.

[arrow_downwardJump to model comparisons](https://firebase.google.com/docs/ai-logic/models#compare-models)

### Gemini

### Gemini 3 Pro Image (aka*nano banana pro*)

`gemini-3-pro-image-preview`

Designed for professional asset production and complex instructions. It features real-world grounding using Google Search, a default "Thinking" process that refines composition prior to generation, and can generate images of up to 4K resolution.*(billing required)*  

### Gemini 2.5 Flash Image (aka*nano banana*)

`gemini-2.5-flash-image`

Designed for speed and efficiency. It's optimized for high-volume, low-latency tasks and generates images at 1024px resolution.*(billing required)*

### Imagen

### Imagen 4

`imagen-4.0-generate-001`

Generates realistic, high-quality images from natural language text prompts.*(billing required)*  

### Imagen 4 Fast

`imagen-4.0-fast-generate-001`

Generates images for prototyping or low-latency use cases.*(billing required)*  

### Imagen 4 Ultra

`imagen-4.0-ultra-generate-001`

Generates realistic, high-quality images from natural language text prompts.*(billing required)*

## Audio generating models

You can generate*streamed* audio with models that support theGemini Live API.

[arrow_downwardJump to model comparisons](https://firebase.google.com/docs/ai-logic/models#compare-models)  

### Gemini 2.5 Flash with Gemini Live API native audio

Gemini Developer API:`gemini-2.5-flash-native-audio-preview-12-2025`

Vertex AI Gemini API:`gemini-live-2.5-flash-native-audio`

Enables low-latency, real-time voice and video interactions with a Gemini model that is*bidirectional* .*(billing**not**required)*

## Previous generation models

The following are active, but previous generation models. We recommend using one of the latest models instead when possible.

[arrow_downwardJump to model comparisons](https://firebase.google.com/docs/ai-logic/models#older-models)

### Gemini models

OUR SECOND GENERATION WORKHORSE MODEL

### Gemini 2.0 Flash

`gemini-2.0-flash-001`

Our second generation workhorse model, with a 1 million token context window. Delivers next-gen features and improved capabilities, including superior speed and native tool use.*(billing**not**required)*  
OUR SECOND GENERATION FAST MODEL

### Gemini 2.0 Flash-Lite

`gemini-2.0-flash-lite-001`

Our second generation small workhorse model, with a 1 million token context window. Optimized for cost efficiency and low latency.*(billing**not**required)*

<br />

**The remainder of this page provides detailed information about the models supported byFirebase AI Logic.**

- [Compare models](https://firebase.google.com/docs/ai-logic/models#compare-models):

  - Supported input and output
  - High-level comparison of the supported capabilities
  - Specifications and limitations, for example max input tokens or max length of input video
- Description of[how models are versioned](https://firebase.google.com/docs/ai-logic/models#versions), specifically their*stable* ,*auto-updated* ,*preview* , and*experimental*versions

- Lists of[available model names](https://firebase.google.com/docs/ai-logic/models#available-model-names)to include in your code during initialization

- Lists of[supported languages](https://firebase.google.com/docs/ai-logic/models#languages)for the models

At the bottom of this page, you can[view detailed information about previous generation models](https://firebase.google.com/docs/ai-logic/models#older-models).

<br />

*** ** * ** ***

## Compare models

Each model has different capabilities to support various use cases. Note that each of tables in this section describe each model*when used withFirebase AI Logic*. Each model might have additional capabilities that aren't available when using our SDKs.

If you can't find the information you're looking for in the following sub-sections, you can find even more information in your chosen API provider documentation:

- Gemini Developer API:[Geminimodels](https://ai.google.dev/gemini-api/docs/models)and[Imagenmodels](https://ai.google.dev/gemini-api/docs/imagen#model-versions)

- Vertex AIGemini API:[Geminimodels](https://cloud.google.com/vertex-ai/generative-ai/docs/models)and[Imagenmodels](https://cloud.google.com/vertex-ai/generative-ai/docs/models)

| **Note:** We recommend reviewing details about[the location for where you access a model](https://firebase.google.com/docs/ai-logic/locations). TheGemini Developer APIprovides only global access to models, but theVertex AIGemini APIprovides both global access (recommended for most use cases) and setting a specific location (supported locations depend on the model).

### Supported input and output

These are the supported input and output types*when using each model withFirebase AI Logic*:

|                                | Gemini 3 Pro, Flash | Gemini 3 Pro Image | Gemini 2.5 Pro, Flash, Flash-Lite | Gemini 2.5 Flash Image | Gemini 2.5 Flash- Live[**\*\*\***](https://firebase.google.com/docs/ai-logic/models#gemini-live-api-models) | Imagen(generate) | Imagen(capability) |
|--------------------------------|---------------------|--------------------|-----------------------------------|------------------------|-------------------------------------------------------------------------------------------------------------|------------------|--------------------|
| **Input types**                                                                                                                                                                                                                                                                       ||||||||
| Text                           |                     |                    |                                   |                        | (streaming)                                                                                                 |                  |                    |
| Code                           |                     |                    |                                   |                        |                                                                                                             |                  |                    |
| Documents (PDFs or plain-text) |                     |                    |                                   |                        |                                                                                                             |                  |                    |
| Images                         |                     |                    |                                   |                        |                                                                                                             |                  |                    |
| Video                          |                     |                    |                                   |                        | (streaming)                                                                                                 |                  |                    |
| Audio                          |                     |                    |                                   |                        | (streaming)                                                                                                 |                  |                    |
| **Output types**                                                                                                                                                                                                                                                                      ||||||||
| Text                           |                     |                    |                                   |                        |                                                                                                             |                  |                    |
| Text (streaming)               |                     |                    |                                   |                        | (transcription)                                                                                             |                  |                    |
| Code                           |                     |                    |                                   |                        |                                                                                                             |                  |                    |
| Structured output (like JSON)  |                     |                    |                                   |                        |                                                                                                             |                  |                    |
| Images                         |                     |                    |                                   |                        |                                                                                                             |                  |                    |
| Audio                          |                     |                    |                                   |                        | (streaming)                                                                                                 |                  |                    |

To learn about supported file types, see[Supported input files and requirements](https://firebase.google.com/docs/ai-logic/input-file-requirements).

### Supported capabilities and features

These are the supported capabilities and features*when using each model withFirebase AI Logic*:

|                                                                                                                                                                           | Gemini 3 Pro, Flash |                                          Gemini 3 Pro Image                                           | Gemini 2.5 Pro, Flash, Flash-Lite |                                        Gemini 2.5 Flash Image                                         | Gemini 2.5 Flash- Live[**\*\*\***](https://firebase.google.com/docs/ai-logic/models#gemini-live-api-models) | Imagen(generate) | Imagen(capability) |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|-------------------------------------------------------------------------------------------------------|-----------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|------------------|--------------------|
| [Thinking](https://firebase.google.com/docs/ai-logic/thinking)                                                                                                            |                     |                                                                                                       |                                   |                                                                                                       |                                                                                                             |                  |                    |
| [Generate text](https://firebase.google.com/docs/ai-logic/generate-text)from text-only or multimodal inputs                                                               |                     | [*interleaved or as part of image*](https://firebase.google.com/docs/ai-logic/generate-images-gemini) |                                   | [*interleaved or as part of image*](https://firebase.google.com/docs/ai-logic/generate-images-gemini) | [*transcription only*](https://firebase.google.com/docs/ai-logic/live-api/configuration#transcriptions)     |                  |                    |
| Generate images ([Gemini](https://firebase.google.com/docs/ai-logic/generate-images-gemini)or[Imagen](https://firebase.google.com/docs/ai-logic/generate-images-imagen))  |                     |                                                                                                       |                                   |                                                                                                       |                                                                                                             |                  |                    |
| Edit images ([Gemini](https://firebase.google.com/docs/ai-logic/generate-images-gemini)or[Imagen](https://firebase.google.com/docs/ai-logic/edit-images-imagen-overview)) |                     |                                                                                                       |                                   |                                                                                                       |                                                                                                             |                  |                    |
| Generate audio                                                                                                                                                            |                     |                                                                                                       |                                   |                                                                                                       | [*streaming only*](https://firebase.google.com/docs/ai-logic/live-api/capabilities#audio-in-audio-out)      |                  |                    |
| [Generate structured output](https://firebase.google.com/docs/ai-logic/generate-structured-output) (like JSON)                                                            |                     |                                                                                                       |                                   |                                                                                                       |                                                                                                             |                  |                    |
| [Analyze documents](https://firebase.google.com/docs/ai-logic/analyze-documents) (PDFs or plain-text)                                                                     |                     |                                                                                                       |                                   |                                                                                                       |                                                                                                             |                  |                    |
| [Analyze images](https://firebase.google.com/docs/ai-logic/analyze-images)(vision)                                                                                        |                     |                                                                                                       |                                   |                                                                                                       |                                                                                                             |                  |                    |
| [Analyze video](https://firebase.google.com/docs/ai-logic/analyze-videos)(vision)                                                                                         |                     |                                                                                                       |                                   |                                                                                                       | [*streaming only*](https://firebase.google.com/docs/ai-logic/live-api/capabilities#video-in-audio-out)      |                  |                    |
| [Analyze audio](https://firebase.google.com/docs/ai-logic/analyze-audio)                                                                                                  |                     |                                                                                                       |                                   |                                                                                                       | [*streaming only*](https://firebase.google.com/docs/ai-logic/live-api/capabilities#audio-in-audio-out)      |                  |                    |
| [Multi-turn chat](https://firebase.google.com/docs/ai-logic/chat)                                                                                                         |                     |                                                                                                       |                                   |                                                                                                       | [*streaming only*](https://firebase.google.com/docs/ai-logic/live-api)                                      |                  |                    |
| [Bidirectional multimodal streaming](https://firebase.google.com/docs/ai-logic/live-api)                                                                                  |                     |                                                                                                       |                                   |                                                                                                       |                                                                                                             |                  |                    |
| [Function calling](https://firebase.google.com/docs/ai-logic/function-calling)                                                                                            |                     |                                                                                                       |                                   |                                                                                                       |                                                                                                             |                  |                    |
| [Code execution](https://firebase.google.com/docs/ai-logic/code-execution)                                                                                                |                     |                                                                                                       |                                   |                                                                                                       |                                                                                                             |                  |                    |
| [Grounding with Google Search](https://firebase.google.com/docs/ai-logic/grounding-google-search)                                                                         |                     |                                                                                                       |                                   |                                                                                                       |                                                                                                             |                  |                    |
| [System instructions](https://firebase.google.com/docs/ai-logic/system-instructions)                                                                                      |                     |                                                                                                       |                                   |                                                                                                       |                                                                                                             |                  |                    |
| [Count tokens](https://firebase.google.com/docs/ai-logic/count-tokens)                                                                                                    |                     |                                                                                                       |                                   |                                                                                                       |                                                                                                             |                  |                    |

| **Note:** *When usingFirebase AI Logic* , the following capabilities are***not yet*** supported: context caching, fine tuning a model, embeddings generation, semantic retrieval, native audio for theLive API, and some[advanced features ofImagenmodels](https://firebase.google.com/docs/ai-logic/generate-images-imagen#supported-features-requirements).

### Specifications and limitations

These are the specifications and limitations*when using each model withFirebase AI Logic*:

|                    Property                    | Gemini 3 Pro, Flash | Gemini 3 Pro Image | Gemini 2.5 Pro, Flash, Flash-Lite | Gemini 2.5 Flash Image | Gemini 2.5 Flash- Live[**\*\*\***](https://firebase.google.com/docs/ai-logic/models#gemini-live-api-models) | Imagen(generate) | Imagen(capability) |
|------------------------------------------------|---------------------|--------------------|-----------------------------------|------------------------|-------------------------------------------------------------------------------------------------------------|------------------|--------------------|
| Input token limit**\***                        | 1,048,576 tokens    | 65,536 tokens      | 1,048,576 tokens                  | 32,768 tokens          | 32K (default; upgradable to 128K) tokens                                                                    | 480 tokens       | 480 tokens         |
| Output token limit**\***                       | 65,536 tokens       | 32,768 tokens      | 65,536 tokens                     | 8,192 tokens           | 64K tokens                                                                                                  | ---              | ---                |
| Knowledge cutoff date                          | January 2025        | January 2025       | January 2025                      | June 2025              | January 2025                                                                                                | ---              | ---                |
| **PDFs (per request)**                                                                                                                                                                                                                                                                                ||||||||
| Max number of input PDF files**\*\***          | 900 files           | 14 files           | 3,000 files                       | 3 files                | ---                                                                                                         | ---              | ---                |
| Max number of pages per input PDF file**\*\*** | 900 pages           | 14 pages           | 1,000 pages                       | 3 pages                | ---                                                                                                         | ---              | ---                |
| Max size per input PDF file                    | 50 MB               | 50 MB              | 50 MB                             | 50 MB                  | ---                                                                                                         | ---              | ---                |
| **Images (per request)**                                                                                                                                                                                                                                                                              ||||||||
| Max number of*input*images                     | 1,000 images        | 14 images          | 3,000 images                      | 3 images               | ---                                                                                                         | ---              | 4 images           |
| Max number of*output*images                    | ---                 | 10 images          | ---                               | 10 images              | ---                                                                                                         | 4 images         | 4 images           |
| Max size per input base64-encoded image        | 7 MB                | 7 MB               | 7 MB                              | 7 MB                   | ---                                                                                                         | ---              | ---                |
| **Video (per request)**                                                                                                                                                                                                                                                                               ||||||||
| Max number of input video files                | 10 files            | ---                | 10 files                          | ---                    | ---                                                                                                         | ---              | ---                |
| Max length of all input video (frames only)    | \~60 minutes        | ---                | \~60 minutes                      | ---                    | ---                                                                                                         | ---              | ---                |
| Max length of all input video (frames+audio)   | \~45 minutes        | ---                | \~45 minutes                      | ---                    | ---                                                                                                         | ---              | ---                |
| **Audio (per request)**                                                                                                                                                                                                                                                                               ||||||||
| Max number of*input*audio files                | 1 file              | ---                | 1 file                            | ---                    | ---                                                                                                         | ---              | ---                |
| Max number of*output*audio files               | ---                 | ---                | ---                               | ---                    | ---                                                                                                         | ---              | ---                |
| Max length of all*input*audio                  | \~8.4 hours         | ---                | \~8.4 hours                       | ---                    | ---                                                                                                         | ---              | ---                |
| Max length of all*output*audio                 | ---                 | ---                | ---                               | ---                    | ---                                                                                                         | ---              | ---                |

^\**For allGeminimodels, a token is equivalent to about 4 characters, so 100 tokens are about 60-80 English words. ForGeminimodels, you can determine the total count of tokens in your requests using[`countTokens`](https://firebase.google.com/docs/ai-logic/count-tokens).*^

^\*\**PDFs are treated as images, so a single page of a PDF is treated as one image. The number of pages allowed in a request is limited to the number of images the model can support.*^

^\*\*\**Gemini 2.5 Flash-Live models are the native audio models that support theGemini Live API.*^

#### Find additional detailed information

- [Quotas](https://firebase.google.com/docs/ai-logic/quotas)and[pricing](https://firebase.google.com/docs/ai-logic/pricing)are different for each model. Pricing also depends on input and output.

- Learn about supported input file types, how to specify MIME type, and how to make sure that your input files and multimodal requests meet the requirements and follow best practices in[Supported input files and requirements](https://firebase.google.com/docs/ai-logic/input-file-requirements).

  <br />

  | **Important** :**The total request size limit is 20 MB.** To send large files, review the[options for providing files in multimodal requests](https://firebase.google.com/docs/ai-logic/input-file-requirements).

  <br />

<br />

*** ** * ** ***

## Model versioning and naming patterns

Models are offered in*stable* ,*preview* , and*experimental*versions. For convenience, aliases without explicit version values are supported.

To find specific model names to use in your code, see the["available model names"](https://firebase.google.com/docs/ai-logic/models#available-model-names)section later on this page.
| **Important** : StableGemini 2.5model names do***not*** have a three-digit suffix, and they do***not***have an auto-updated alias.

|               Version type / Release stage               ||                                                                                                                                                                                                                                                                                             Description                                                                                                                                                                                                                                                                                              |                                                                                                                                                                   Model name pattern                                                                                                                                                                   |
|---|-------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Stable**                                               || ***Stable*** versions are available and supported for production use starting on the release date. - A stable model version is typically released with a retirement date, which indicates the last day that the model is available. After this date, the model is no longer accessible or supported by Google.                                                                                                                                                                                                                                                                                       | - **Gemini 2.5models** Model names of stable versions have no suffix Example:`gemini-2.5-pro` - **Gemini 2.0andImagenmodels** Model names of stable versions are appended with a specific three-digit version number Example:`gemini-2.0-flash-001` Example:`imagen-3.0-generate-002`                                                                  |
|   | **Auto-updated stable alias** (Gemini 2.0models only) | ***Auto-updated*** stable aliases always point to the*latest**stable*** version of that model. - If a new stable version is released, the*auto-updated*alias automatically starts pointing to that new stable version.                                                                                                                                                                                                                                                                                                                                                                               | **Gemini 2.0models only** Model names of aliases have no suffix Example:`gemini-2.0-flash`                                                                                                                                                                                                                                                             |
| **Preview**                                              || ***Preview*** versions have new capabilities and are considered*not stable* . - These models are*not*recommended for production use, come with more restrictive rate limits, and may have billing requirements. - These models are retired within a few weeks or months after their associated stable version is released. - For theVertex AIGemini API, preview models released after June 2025 usually require you to[set the model's location to`global`](https://firebase.google.com/docs/ai-logic/locations).                                                                                   | Model names of preview versions are appended with`-preview`and often the model's release date (`-MM-DD`for older models or`-MM-YYYY`for newer models) Examples: `gemini-2.5-flash-preview-04-17` (released on April 17, 2025) or `gemini-2.5-flash-preview-09-2025` (released in September 2025) or `gemini-3-pro-preview` (released in November 2025) |
| **Experimental**                                         || ***Experimental*** versions have new capabilities and are considered*not stable* . - These models are*not*recommended for production use and come with more restrictive rate limits. Experimental models are intended for gathering feedback and to enable experimentation with our latest features. - These models are retired within a few weeks or months after their associated stable version is released. - For theVertex AIGemini API, experimental models released after June 2025 require you to[set the model's location to`global`](https://firebase.google.com/docs/ai-logic/locations). | Model names of experimental versions are appended with`-exp`along with the model's release date (`-MM-DD`) Example:`gemini-2.5-pro-exp-03-25` (released on March 25, 2025)                                                                                                                                                                             |
| **Retired**                                              || ***Retired*** versions are past their retirement date and have been permanently deactivated. - Retired models are no longer accessible or supported by Google, and a request using a retired model name returns a 404 error.                                                                                                                                                                                                                                                                                                                                                                         | ---                                                                                                                                                                                                                                                                                                                                                    |

| **For production use cases, we recommend using the explicit model name for the most recent*stable*version.** Even though an*auto-updated stable alias* points to a stable version, the actual model version it points to will automatically change whenever a new stable version is released, which could mean unexpected behavior or responses.
|
| ***Preview* and*experimental* versions are recommended during*prototyping only*.**
|
| We also recommend usingFirebase Remote Configso that you can[dynamically change the model and version in your app](https://firebase.google.com/docs/ai-logic/change-model-name-remotely)without releasing a new version of your app.

<br />

*** ** * ** ***

## Available model names

Model names are the explicit values that you include*in your code*during initialization of the model.

[arrow_downwardJump toGeminimodel names](https://firebase.google.com/docs/ai-logic/models#model-names-gemini)[arrow_downwardJump toImagenmodel names](https://firebase.google.com/docs/ai-logic/models#model-names-imagen)

#### Programmatically list all available models

You can list all available models names using the REST API:

- Gemini Developer API: Call the[`models.list`endpoint](https://ai.google.dev/api/models#method:-models.list)

- Vertex AIGemini API: Call the[`publishers.models.list`endpoint](https://cloud.google.com/vertex-ai/docs/reference/rest/v1beta1/publishers.models/list)

Note that this returned list will include*all* models supported by the API providers, butFirebase AI Logiconly supports theGeminiandImagenmodels described on this page. Also note that auto-updated aliases (for example,`gemini-2.0-flash`) aren't listed because they're a convenience alias for the base model.

### Geminimodel names

For initialization examples for your platform, see the[getting started guide](https://firebase.google.com/docs/ai-logic/get-started).

For details about the release stages (especially for use cases, billing, and retirement), see[model versioning and naming patterns](https://firebase.google.com/docs/ai-logic/models#versions).
| **Important** : StableGemini 2.5model names do***not*** have a three-digit suffix, and they do***not*** have an auto-updated alias.  
|
| Also, if you're using theVertex AIGemini API, allGemini 3andGemini 2.5***preview*** models (exceptGemini Live APImodels) that are released after June 2025 are*only* available in the`global`location.

#### Gemini 3 Promodel names

^*Requires the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing)regardless of yourGemini APIprovider.*^

|     **Model name**     |        **Description**         | **Release stage** | **Release date** | **Retirement date** |
|------------------------|--------------------------------|-------------------|------------------|---------------------|
| `gemini-3-pro-preview` | Preview version ofGemini 3 Pro | Preview           | 2025-11-18       | To be determined    |

#### Gemini 3 Flashmodel names

^*Does**not** require the pay-as-you-go Blaze pricing plan if you're using theGemini Developer API(usually preview models require a paid plan).*^

|      **Model name**      |         **Description**          | **Release stage** | **Release date** | **Retirement date** |
|--------------------------|----------------------------------|-------------------|------------------|---------------------|
| `gemini-3-flash-preview` | Preview version ofGemini 3 Flash | Preview           | 2025-12-17       | To be determined    |

#### Gemini 3 Pro Imagemodel names (aka "nano banana pro")

^*Requires the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing)regardless of yourGemini APIprovider.*^

|        **Model name**        |                       **Description**                        | **Release stage** | **Release date** | **Retirement date** |
|------------------------------|--------------------------------------------------------------|-------------------|------------------|---------------------|
| `gemini-3-pro-image-preview` | Preview version ofGemini 3 Pro Image (aka "nano banana pro") | Preview           | 2025-11-20       | To be determined    |

#### Gemini 2.5 Promodel names

^*Does**not** require the pay-as-you-go Blaze pricing plan if you're using theGemini Developer API.*^

|  **Model name**  |         **Description**         | **Release stage** | **Release date** |    **Retirement date**     |
|------------------|---------------------------------|-------------------|------------------|----------------------------|
| `gemini-2.5-pro` | Stable version ofGemini 2.5 Pro | Stable            | 2025-06-17       | No earlier than 2026-06-17 |

#### Gemini 2.5 Flashmodel names

^*Does**not** require the pay-as-you-go Blaze pricing plan if you're using theGemini Developer API.*^

|   **Model name**   |          **Description**          | **Release stage** | **Release date** |    **Retirement date**     |
|--------------------|-----------------------------------|-------------------|------------------|----------------------------|
| `gemini-2.5-flash` | Stable version ofGemini 2.5 Flash | Stable            | 2025-06-17       | No earlier than 2026-06-17 |

#### Gemini 2.5 FlashâLitemodel names

^*Does**not** require the pay-as-you-go Blaze pricing plan if you're using theGemini Developer API.*^

|     **Model name**      |            **Description**             | **Release stage** | **Release date** |    **Retirement date**     |
|-------------------------|----------------------------------------|-------------------|------------------|----------------------------|
| `gemini-2.5-flash-lite` | Stable version ofGemini 2.5 FlashâLite | Stable            | 2025-07-22       | No earlier than 2026-07-22 |

#### Gemini 2.5 Flash Imagemodel names (aka "nano banana")

^*Requires the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing)regardless of yourGemini APIprovider.*^

|      **Model name**      |                       **Description**                       | **Release stage** | **Release date** |    **Retirement date**     |
|--------------------------|-------------------------------------------------------------|-------------------|------------------|----------------------------|
| `gemini-2.5-flash-image` | Stable version forGemini 2.5 Flash Image(aka "nano banana") | Stable            | 2025-10-02       | No earlier than 2026-10-02 |

#### Gemini 2.5 Flash Livemodel names

^*Does**not** require the pay-as-you-go Blaze pricing plan if you're using theGemini Developer API(usually preview models require a paid plan).*^

Gemini 2.5 Flash Livemodels are the*native audio* models that support theGemini Live API. Even though the model has different model names depending on theGeminiAPI provider, the behavior and features of the model are the same.

|        **Gemini Developer API Model name**         |                          **Description**                          | **Release stage** | **Release date** | **Retirement date** |
|----------------------------------------------------|-------------------------------------------------------------------|-------------------|------------------|---------------------|
| `gemini-2.5-flash-native-audio-preview-12-2025`^1^ | Latest preview version for theLive APIon theGemini Developer API  | Preview           | 2025-12-12       | To be determined    |
| `gemini-2.5-flash-native-audio-preview-09-2025`^1^ | Initial preview version for theLive APIon theGemini Developer API | Preview           | 2025-09-18       | To be determined    |

|           **Vertex AIGemini API Model name**            |                     **Description**                      | **Release stage** | **Release date** |    **Retirement date**     |
|---------------------------------------------------------|----------------------------------------------------------|-------------------|------------------|----------------------------|
| `gemini-live-2.5-flash-native-audio`^2^                 | Stable version for theLive APIon theVertex AIGemini API  | Stable            | 2025-12-12       | No earlier than 2026-12-12 |
| `gemini-live-2.5-flash-preview-native-audio-09-2025`^2^ | Preview version for theLive APIon theVertex AIGemini API | Preview           | 2025-09-18       | To be determined           |

^**1** ***Only** supported by theGemini Developer API. Also, even though these are preview models, they're available on the "free tier" of theGemini Developer API.*^  
^**2** ***Only** supported by theVertex AIGemini API. Also, these models are not supported in the`global`location.*^

### Imagenmodel names

For initialization examples for your platform, see the[generate images withImagenguide](https://firebase.google.com/docs/ai-logic/generate-images-imagen).

For details about the release stages (especially for use cases, billing, and retirement), see[model versioning and naming patterns](https://firebase.google.com/docs/ai-logic/models#versions).
| **Important:** AllImagenmodels require the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing)regardless of yourGemini APIprovider.

#### Imagen 4model names

|      **Model name**       |      **Description**      | **Release stage** | **Release date** |    **Retirement date**     |
|---------------------------|---------------------------|-------------------|------------------|----------------------------|
| `imagen-4.0-generate-001` | Stable version ofImagen 4 | Stable            | 2025-08-14       | No earlier than 2026-08-14 |

#### Imagen 4 Fastmodel names

|         **Model name**         |        **Description**         | **Release stage** | **Release date** |    **Retirement date**     |
|--------------------------------|--------------------------------|-------------------|------------------|----------------------------|
| `imagen-4.0-fast-generate-001` | Stable version ofImagen 4 Fast | Stable            | 2025-08-14       | No earlier than 2026-08-14 |

#### Imagen 4 Ultramodel names

|         **Model name**          |         **Description**         | **Release stage** | **Release date** |    **Retirement date**     |
|---------------------------------|---------------------------------|-------------------|------------------|----------------------------|
| `imagen-4.0-ultra-generate-001` | Stable version ofImagen 4 Ultra | Stable            | 2025-08-14       | No earlier than 2026-08-14 |

#### Imagen 3 Capabilitymodel names

|         **Model name**         |               **Description**                | **Release stage** | **Release date** |    **Retirement date**     |
|--------------------------------|----------------------------------------------|-------------------|------------------|----------------------------|
| `imagen-3.0-capability-001`^2^ | Initial stable version ofImagen 3 Capability | Stable            | 2024-12-10       | No earlier than 2025-12-10 |

^**2** *Not supported by theGemini Developer APIno matter how you access it.*^

<br />

*** ** * ** ***

## Supported languages

| **Note:** These languages*do not represent the locations for accessing the model* ; instead, these are the*languages* that the models can understand and (forGemini) respond in (for example, the text input and output). If needed, see[specify the location for accessing a model](https://firebase.google.com/docs/ai-logic/locations).

### Gemini

- All theGeminimodels can understand and respond in the following languages:

  Arabic (ar), Bengali (bn), Bulgarian (bg), Chinese simplified and traditional (zh), Croatian (hr), Czech (cs), Danish (da), Dutch (nl), English (en), Estonian (et), Finnish (fi), French (fr), German (de), Greek (el), Hebrew (iw), Hindi (hi), Hungarian (hu), Indonesian (id), Italian (it), Japanese (ja), Korean (ko), Latvian (lv), Lithuanian (lt), Norwegian (no), Polish (pl), Portuguese (pt), Romanian (ro), Russian (ru), Serbian (sr), Slovak (sk), Slovenian (sl), Spanish (es), Swahili (sw), Swedish (sv), Thai (th), Turkish (tr), Ukrainian (uk), Vietnamese (vi)
- Gemini 2.0 Flash,Gemini 1.5 ProandGemini 1.5 Flashmodels can understand and respond in the following*additional*languages:

  Afrikaans (af), Amharic (am), Assamese (as), Azerbaijani (az), Belarusian (be), Bosnian (bs), Catalan (ca), Cebuano (ceb), Corsican (co), Welsh (cy), Dhivehi (dv), Esperanto (eo), Basque (eu), Persian (fa), Filipino (Tagalog) (fil), Frisian (fy), Irish (ga), Scots Gaelic (gd), Galician (gl), Gujarati (gu), Hausa (ha), Hawaiian (haw), Hmong (hmn), Haitian Creole (ht), Armenian (hy), Igbo (ig), Icelandic (is), Javanese (jv), Georgian (ka), Kazakh (kk), Khmer (km), Kannada (kn), Krio (kri), Kurdish (ku), Kyrgyz (ky), Latin (la), Luxembourgish (lb), Lao (lo), Malagasy (mg), Maori (mi), Macedonian (mk), Malayalam (ml), Mongolian (mn), Meiteilon (Manipuri) (mni-Mtei), Marathi (mr), Malay (ms), Maltese (mt), Myanmar (Burmese) (my), Nepali (ne), Nyanja (Chichewa) (ny), Odia (Oriya) (or), Punjabi (pa), Pashto (ps), Sindhi (sd), Sinhala (Sinhalese) (si), Samoan (sm), Shona (sn), Somali (so), Albanian (sq), Sesotho (st), Sundanese (su), Tamil (ta), Telugu (te), Tajik (tg), Uyghur (ug), Urdu (ur), Uzbek (uz), Xhosa (xh), Yiddish (yi), Yoruba (yo), Zulu (zu)

### Imagen

- **General availability**: English

- **Preview**: Chinese (simplified), Chinese (traditional), Hindi, Japanese, Korean, Portuguese, Spanish

<br />

*** ** * ** ***

## Information about previous models

The following are active, but previous generation models. We recommend using one of the latest models instead when possible.

#### Geminimodels

- `gemini-2.0-flash-001`(and its auto-updated alias`gemini-2.0-flash`)
- `gemini-2.0-flash-lite-001`(and its auto-updated alias`gemini-2.0-flash-lite`)

For information about olderGemini Live APImodels, see theGemini APIprovider documentation:

- [`gemini-2.0-flash-live-001`](https://ai.google.dev/gemini-api/docs/models#gemini-2.0-flash-live)
- [`gemini-2.0-flash-live-preview-04-09`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-0-flash#live-api)
- [`gemini-live-2.5-flash-preview`](https://ai.google.dev/gemini-api/docs/models#gemini-2.5-flash-live)

#### Imagenmodels

- `imagen-3.0-generate-002`
- `imagen-3.0-fast-generate-001`

| AllGemini 1.0models andGemini 1.5are retired, and all requests to these models return a 404 error. To avoid service disruption, update to a[newer model](https://firebase.google.com/docs/ai-logic/models)(for example,`gemini-2.5-flash-lite`).[Learn more.](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#discontinued-models)
|
| When you start seriously developing your app,**we recommend usingFirebase Remote Configso that you can[remotely change the model and version in your app](https://firebase.google.com/docs/ai-logic/change-model-name-remotely)without releasing a new version of your app.**

<br />

View supported input and output of previous generation models

<br />

These are the input and output types*when using each model withFirebase AI Logic*:

|                                | Gemini 2.0 Flash | Gemini 2.0 Flash- Lite |
|--------------------------------|------------------|------------------------|
| **Input types**                                                          |||
| Text                           |                  |                        |
| Text (streaming)               |                  |                        |
| Code                           |                  |                        |
| Documents (PDFs or plain-text) |                  |                        |
| Images                         |                  |                        |
| Video                          |                  |                        |
| Audio                          |                  |                        |
| Audio (streaming)              |                  |                        |
| **Output types**                                                         |||
| Text                           |                  |                        |
| Text (streaming)               |                  |                        |
| Code                           |                  |                        |
| Structured output (like JSON)  |                  |                        |
| Images                         |                  |                        |
| Audio                          |                  |                        |
| Audio (streaming)              |                  |                        |

<br />

<br />

<br />

Supported capabilities and features of previous generation models

<br />

These are the capabilities and features*when using each model withFirebase AI Logic*:

|                                                                                                                                                                           | Gemini 2.0 Flash | Gemini 2.0 Flash- Lite |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|------------------------|
| [Thinking](https://firebase.google.com/docs/ai-logic/thinking)                                                                                                            |                  |                        |
| [Generate text](https://firebase.google.com/docs/ai-logic/generate-text)from text-only or multimodal inputs                                                               |                  |                        |
| Generate images ([Gemini](https://firebase.google.com/docs/ai-logic/generate-images-gemini)or[Imagen](https://firebase.google.com/docs/ai-logic/generate-images-imagen))  |                  |                        |
| Edit images ([Gemini](https://firebase.google.com/docs/ai-logic/generate-images-gemini)or[Imagen](https://firebase.google.com/docs/ai-logic/edit-images-imagen-overview)) |                  |                        |
| Generate audio                                                                                                                                                            |                  |                        |
| [Generate structured output](https://firebase.google.com/docs/ai-logic/generate-structured-output) (like JSON)                                                            |                  |                        |
| [Analyze documents](https://firebase.google.com/docs/ai-logic/analyze-documents) (PDFs or plain-text)                                                                     |                  |                        |
| [Analyze images](https://firebase.google.com/docs/ai-logic/analyze-images)(vision)                                                                                        |                  |                        |
| [Analyze video](https://firebase.google.com/docs/ai-logic/analyze-videos)(vision)                                                                                         |                  |                        |
| [Analyze audio](https://firebase.google.com/docs/ai-logic/analyze-audio)                                                                                                  |                  |                        |
| [Multi-turn chat](https://firebase.google.com/docs/ai-logic/chat)                                                                                                         |                  |                        |
| [Bidirectional multimodal streaming](https://firebase.google.com/docs/ai-logic/live-api)                                                                                  |                  |                        |
| [Function calling](https://firebase.google.com/docs/ai-logic/function-calling)                                                                                            |                  |                        |
| [Code execution](https://firebase.google.com/docs/ai-logic/code-execution)                                                                                                |                  |                        |
| [Grounding with Google Search](https://firebase.google.com/docs/ai-logic/grounding-google-search)                                                                         |                  |                        |
| [System instructions](https://firebase.google.com/docs/ai-logic/system-instructions)                                                                                      |                  |                        |
| [Count tokens](https://firebase.google.com/docs/ai-logic/count-tokens)                                                                                                    |                  |                        |

<br />

<br />

<br />

Specifications and limitations of previous generation models

<br />

These are the specifications and limitations*when using each model withFirebase AI Logic*:

|                             Property                             | Gemini 2.0 Flash | Gemini 2.0 Flash- Lite |
|------------------------------------------------------------------|------------------|------------------------|
| Context window**\*** *Total token limit (combined input+output)* | 1,048,576 tokens | 1,048,576 tokens       |
| Output token limit**\***                                         | 8,192 tokens     | 8,192 tokens           |
| Knowledge cutoff date                                            | June 2024        | June 2024              |
| **PDFs (per request)**                                                                                     |||
| Max number of input PDF files**\*\***                            | 3,000 files      | 3,000 files            |
| Max number of pages per input PDF file**\*\***                   | 1,000 pages      | 1,000 pages            |
| Max size per input PDF file                                      | 50 MB            | 50 MB                  |
| **Images (per request)**                                                                                   |||
| Max number of*input*images                                       | 3,000 images     | 3,000 images           |
| Max number of*output*images                                      | ---              | ---                    |
| Max size per input base64-encoded image                          | 7 MB             | 7 MB                   |
| **Video (per request)**                                                                                    |||
| Max number of input video files                                  | 10 files         | 10 files               |
| Max length of all input video (frames only)                      | \~60 minutes     | \~60 minutes           |
| Max length of all input video (frames+audio)                     | \~45 minutes     | \~45 minutes           |
| **Audio (per request)**                                                                                    |||
| Max number of*input*audio files                                  | 1 file           | 1 file                 |
| Max number of*output*audio files                                 | ---              | ---                    |
| Max length of all*input*audio                                    | \~8.4 hours      | \~8.4 hours            |
| Max length of all*output*audio                                   | ---              | ---                    |

^\**For allGeminimodels, a token is equivalent to about 4 characters, so 100 tokens are about 60-80 English words. ForGeminimodels, you can determine the total count of tokens in your requests using[`countTokens`](https://firebase.google.com/docs/ai-logic/count-tokens).*^

^\*\**PDFs are treated as images, so a single page of a PDF is treated as one image. The number of pages allowed in a request is limited to the number of images the model can support.*^

<br />

<br />

<br />

Available model names of previous generation models (including retirement dates)

<br />

Model names are the explicit values that you include*in your code*during initialization of the model.

### Gemini models

#### Gemini 2.0 Flashmodel names

|     **Model name**     |                                                **Description**                                                 | **Release stage** | **Release date** |    **Retirement date**     |
|------------------------|----------------------------------------------------------------------------------------------------------------|-------------------|------------------|----------------------------|
| `gemini-2.0-flash-001` | Latest stable version ofGemini 2.0 Flash                                                                       | Stable            | 2025-02-05       | No earlier than 2026-02-05 |
| `gemini-2.0-flash`     | Auto-updated alias pointing to the*latest stable* version ofGemini 2.0 Flash (currently`gemini-2.0-flash-001`) | Stable            | 2025-02-10       | ---                        |

#### Gemini 2.0 FlashâLitemodel names

|       **Model name**        |                                                     **Description**                                                      | **Release stage** | **Release date** |    **Retirement date**     |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------|-------------------|------------------|----------------------------|
| `gemini-2.0-flash-lite-001` | Latest stable version ofGemini 2.0 FlashâLite                                                                            | Stable            | 2025-02-25       | No earlier than 2026-02-25 |
| `gemini-2.0-flash-lite`     | Auto-updated alias pointing to the*latest stable* version ofGemini 2.0 FlashâLite (currently`gemini-2.0-flash-lite-001`) | Stable            | 2025-02-25       | ---                        |

### Imagen models

#### Imagen 3model names

|        **Model name**        |          **Description**          | **Release stage** | **Release date** |    **Retirement date**     |
|------------------------------|-----------------------------------|-------------------|------------------|----------------------------|
| `imagen-3.0-generate-002`    | Latest stable version ofImagen 3  | Stable            | 2025-01-23       | No earlier than 2026-01-23 |
| `imagen-3.0-generate-001`^3^ | Initial stable version ofImagen 3 | Stable            | 2024-07-31       | No earlier than 2025-07-31 |

#### Imagen 3 Fastmodel names

|          **Model name**           |            **Description**             | **Release stage** | **Release date** |    **Retirement date**     |
|-----------------------------------|----------------------------------------|-------------------|------------------|----------------------------|
| `imagen-3.0-fast-generate-001`^3^ | Initial stable version ofImagen 3 Fast | Stable            | 2024-07-31       | No earlier than 2025-07-31 |

^**3** *Not supported by theGemini Developer APIno matter how you access it.*^

<br />

<br />

<br />

*** ** * ** ***

## Next steps

<br />

#### Try out the capabilities of theGemini API

- Build[multi-turn conversations (chat)](https://firebase.google.com/docs/ai-logic/chat).
- Generate text from[text-only prompts](https://firebase.google.com/docs/ai-logic/generate-text).
- Generate text by prompting with various file types, like[images](https://firebase.google.com/docs/ai-logic/analyze-images),[PDFs](https://firebase.google.com/docs/ai-logic/analyze-documents),[video](https://firebase.google.com/docs/ai-logic/analyze-video), and[audio](https://firebase.google.com/docs/ai-logic/analyze-audio).
- Generate[structured output (like JSON)](https://firebase.google.com/docs/ai-logic/generate-structured-output)from both text and multimodal prompts.
- Generate images from text prompts ([Gemini](https://firebase.google.com/docs/ai-logic/generate-images-gemini)or[Imagen](https://firebase.google.com/docs/ai-logic/generate-images-imagen)).
- [Stream input and output](https://firebase.google.com/docs/ai-logic/live-api)(including audio) using theGemini Live API.
- Use tools (like[function calling](https://firebase.google.com/docs/ai-logic/function-calling)and[grounding with Google Search](https://firebase.google.com/docs/ai-logic/grounding-google-search)) to connect aGeminimodel to other parts of your app and external systems and information.

<br />