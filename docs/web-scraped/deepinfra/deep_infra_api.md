# Source: https://deepinfra.com/docs/deep_infra_api

We use essential cookies to make our site work. With your consent, we may also
use non-essential cookies to improve user experience and analyze website
traffic…

AcceptReject

[FLUX.2 is live!](https://deepinfra.com/models?q=flux-2) High-fidelity image
generation made simple.

[](/)

[Models](/models)

By Category

* * *

[Automatic Speech Recognition](/models/automatic-speech-
recognition)[Embeddings](/models/embeddings)[Reranker](/models/reranker)[Text
Generation](/models/text-generation)[Text To Image](/models/text-to-
image)[Text To Speech](/models/text-to-speech)[Text To Video](/models/text-to-
video)[Zero Shot Image Classification](/models/zero-shot-image-classification)

[View all models](/models)

By Family

* * *

[![anthropic
logo](/_next/static/media/anthropic.c6636fa8.svg)/Claude](/claude)[![deepseek-
ai
logo](/_next/static/media/deepseek.b1ec6c4e.svg)/DeepSeek](/deepseek)[![black-
forest-labs logo](/_next/static/media/bfl.7e050ff6.svg)/Flux](/flux)[![google
logo](/_next/static/media/google.09551b71.svg)/Gemini](/gemini)[![meta-llama
logo](/_next/static/media/meta.56a2e6fd.svg)/Llama](/llama)[![mistralai
logo](/_next/static/media/mistralai.ecbe51d4.svg)/Mistral](/mistral)[![nvidia
logo](/_next/static/media/nvidia.2165073d.svg)/Nemotron](/nemotron)[![qwen
logo](/_next/static/media/qwen.d6d74288.svg)/Qwen](/qwen)

[Docs](/docs)[Pricing](/pricing)[GPUs](/gpu-
instances)[Chat](/chat)[DeepStart](/deepstart)[Blog](/blog)

[Contact Sales](/contact-sales)[Log In](/login)

[Models](/models)

[Automatic Speech Recognition](/models/automatic-speech-
recognition)[Embeddings](/models/embeddings)[Reranker](/models/reranker)[Text
Generation](/models/text-generation)[Text To Image](/models/text-to-
image)[Text To Speech](/models/text-to-speech)[Text To Video](/models/text-to-
video)[Zero Shot Image Classification](/models/zero-shot-image-classification)

[Docs](/docs)

[Pricing](/pricing)

[GPUs](/gpu-instances)

[Chat](/chat)

[DeepStart](/deepstart)

[Blog](/blog)

Feedback

[Contact Sales](/contact-sales)

[Log In](/login)

  1. [Getting Started](/docs)

     1. [Quick Start Guide](/docs/getting-started)

     2. [Available Models](/docs/models)

     3. [Running Inference](/docs/inference)

     4. [Data Privacy & Security](/docs/data)

  2. [API Reference](/docs/api-reference)

     1. [OpenAI-Compatible API](/docs/openai_api)

     2. DeepInfra Native API

     3. [Rate Limits](/docs/advanced/rate-limits)

     4. [Webhooks](/docs/advanced/webhooks)

     5. [Authentication & Tokens](/docs/advanced/scoped_jwt)

  3. [Model Features](/docs/model-features)

     1. [Function Calling](/docs/advanced/function_calling)

     2. [JSON Mode](/docs/advanced/json_mode)

     3. [Multimodal Models](/docs/advanced/multimodal)

     4. [Log Probabilities](/docs/advanced/log_probs)

     5. [Max Output Tokens](/docs/advanced/max_tokens_limit)

  4. [GPU Instances](/docs/gpu-instances)

     1. [Containers](/docs/gpu-instances/containers)

  5. [Custom Deployments](/docs/custom-deployments)

     1. [Custom LLMs](/docs/advanced/custom_llms)

     2. [LoRA Adapter Models](/docs/advanced/lora)

     3. [LoRA Image Adapters](/docs/advanced/lora_text_to_image)

  6. [Integrations](/docs/integrations)

     1. [LangChain](/docs/advanced/langchain)

     2. [LlamaIndex](/docs/advanced/llama-index)

     3. [AI SDK](/docs/advanced/aisdk)

     4. [AutoGen](/docs/advanced/autogen)

     5. [Okta SSO](/docs/advanced/okta)

  7. [Tutorials & Examples](/docs/tutorials)

     1. [Stable Diffusion (Text to Image)](/docs/tutorials/stable-diffusion)

     2. [Whisper (Speech to Text)](/docs/tutorials/whisper)

     3. [Deprecated Models](/docs/advanced/deprecated)

  8. [Miscellaneous](/docs/misc)

     1. [Data Subprocessors](/docs/misc/subprocessors)

Documentation

  1. [Getting Started](/docs)

     1. [Quick Start Guide](/docs/getting-started)

     2. [Available Models](/docs/models)

     3. [Running Inference](/docs/inference)

     4. [Data Privacy & Security](/docs/data)

  2. [API Reference](/docs/api-reference)

     1. [OpenAI-Compatible API](/docs/openai_api)

     2. DeepInfra Native API

     3. [Rate Limits](/docs/advanced/rate-limits)

     4. [Webhooks](/docs/advanced/webhooks)

     5. [Authentication & Tokens](/docs/advanced/scoped_jwt)

  3. [Model Features](/docs/model-features)

     1. [Function Calling](/docs/advanced/function_calling)

     2. [JSON Mode](/docs/advanced/json_mode)

     3. [Multimodal Models](/docs/advanced/multimodal)

     4. [Log Probabilities](/docs/advanced/log_probs)

     5. [Max Output Tokens](/docs/advanced/max_tokens_limit)

  4. [GPU Instances](/docs/gpu-instances)

     1. [Containers](/docs/gpu-instances/containers)

  5. [Custom Deployments](/docs/custom-deployments)

     1. [Custom LLMs](/docs/advanced/custom_llms)

     2. [LoRA Adapter Models](/docs/advanced/lora)

     3. [LoRA Image Adapters](/docs/advanced/lora_text_to_image)

  6. [Integrations](/docs/integrations)

     1. [LangChain](/docs/advanced/langchain)

     2. [LlamaIndex](/docs/advanced/llama-index)

     3. [AI SDK](/docs/advanced/aisdk)

     4. [AutoGen](/docs/advanced/autogen)

     5. [Okta SSO](/docs/advanced/okta)

  7. [Tutorials & Examples](/docs/tutorials)

     1. [Stable Diffusion (Text to Image)](/docs/tutorials/stable-diffusion)

     2. [Whisper (Speech to Text)](/docs/tutorials/whisper)

     3. [Deprecated Models](/docs/advanced/deprecated)

  8. [Miscellaneous](/docs/misc)

     1. [Data Subprocessors](/docs/misc/subprocessors)

# DeepInfra API

DeepInfra's API is more advanced but gives you access to every model we
provide unlike OpenAI which only works with LLMs and embeddings. You can also
do Image Generation, Speech Recognition, Object detection, Token
classification, Fill mask, Image classification, Zero-shot image
classification and Text classification

### JavaScript

JavaScript is a first class citizen at DeepInfra. You can install our official
client <https://github.com/deepinfra/deepinfra-node> with

    
    
    npm install deepinfra
    
    
    copy

### HTTP/Curl

Don't want another dependency?

You prefer Go, C#, Java, PHP, Swift, Ruby, C++ or something exotic?

No problem. You can always use HTTP and have full access to all features by
DeepInfra.

### Completions/Text Generation

[List of text generation models](/models/text-generation)

You should know how to format the input to make completions work. Different
models might have a different input format. The example below is for [meta-
llama/Meta-Llama-3-8B-Instruct](/meta-llama/Meta-Llama-3-8B-Instruct)

JavaScriptbash

    
    
    import { TextGeneration } from "deepinfra";
    
    const DEEPINFRA_API_KEY = "$DEEPINFRA_TOKEN";
    const MODEL_URL = 'https://api.deepinfra.com/v1/inference/meta-llama/Meta-Llama-3-8B-Instruct';
    
    async function main() {
      const client = new TextGeneration(MODEL_URL, DEEPINFRA_API_KEY);
      const res = await client.generate({
        "input": "<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\nHello!<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
        "stop": [
          "<|eot_id|>"
        ]
      });
    
      console.log(res.results[0].generated_text);
      console.log(res.inference_status.tokens_input, res.inference_status.tokens_generated)
    }
    
    main();
    
    
    copy

For every model you can check its input format in its API section.

### Embeddings

[List of embeddings models](/models/embeddings)

The following creates an embedding vector representing the input text

JavaScriptbash

    
    
    import { Embeddings } from "deepinfra";
    
    const DEEPINFRA_API_KEY = "$DEEPINFRA_TOKEN";
    const MODEL = "BAAI/bge-large-en-v1.5";
    
    const main = async () => {
      const client = new Embeddings(MODEL, DEEPINFRA_API_KEY);
      const body = {
        inputs: [
          "What is the capital of France?",
          "What is the capital of Germany?",
          "What is the capital of Italy?",
        ],
      };
      const output = await client.generate(body);
      console.log(output.embeddings[0]);
    };
    
    main();
    
    
    copy

### Image Generation

[List of image generation models](/models/text-to-image)

JavaScriptbash

    
    
    import { TextToImage } from "deepinfra";
    import { createWriteStream } from "fs";
    import { Readable } from "stream";
    
    const DEEPINFRA_API_KEY = "$DEEPINFRA_TOKEN";
    const MODEL = "stabilityai/stable-diffusion-2-1";
    
    const main = async () => {
      const model = new TextToImage(MODEL, DEEPINFRA_API_KEY);
      const response = await model.generate({
        prompt: "a burger with a funny hat on the beach",
      });
    
      const result = await fetch(response.images[0]);
    
      if (result.ok && result.body) {
        let writer = createWriteStream("image.png");
        Readable.fromWeb(result.body).pipe(writer);
      }
    };
    
    main();
    
    
    copy

### Speech Recognition

[List of speech recognition models](/models/automatic-speech-recognition)

Text to speed for a locally stored `audio.mp3` file

JavaScriptbash

    
    
    import { AutomaticSpeechRecognition } from "deepinfra";
    import path from "path";
    import { fileURLToPath } from 'url';
    
    
    const __filename = fileURLToPath(import.meta.url);
    const __dirname = path.dirname(__filename);
    
    const DEEPINFRA_API_KEY = "$DEEPINFRA_TOKEN";
    const MODEL = "openai/whisper-large";
    
    const main = async () => {
      const client = new AutomaticSpeechRecognition(MODEL, DEEPINFRA_API_KEY);
    
      const input = {
        audio: path.join(__dirname, "audio.mp3"),
      };
      const response = await client.generate(input);
      console.log(response.text);
    };
    
    main();
    
    
    copy

### Object Detection

[List of object detection models](/models/object-detection)

Send an image for detection

JavaScriptbash

    
    
    import { ObjectDetection } from "deepinfra";
    import path from "path";
    import { fileURLToPath } from 'url';
    
    
    const __filename = fileURLToPath(import.meta.url);
    const __dirname = path.dirname(__filename);
    
    const DEEPINFRA_API_KEY = "$DEEPINFRA_TOKEN";
    const MODEL = "hustvl/yolos-small";
    
    const main = async () => {
      const model = new ObjectDetection(MODEL, DEEPINFRA_API_KEY);
    
      const input = {
        image: path.join(__dirname, "image.jpg"),
      };
      const response = await model.generate(input);
    
      for (const result of response.results) {
        console.log(result.label, result.score, result.box);
      }
    };
    
    main();
    
    
    copy

### Token Classification

[List of token classification models](/models/token-classification)

JavaScriptbash

    
    
    import { TokenClassification } from "deepinfra";
    
    const DEEPINFRA_API_KEY = "$DEEPINFRA_TOKEN";
    const MODEL = "Davlan/bert-base-multilingual-cased-ner-hrl";
    
    const main = async () => {
      const model = new TokenClassification(MODEL, DEEPINFRA_API_KEY);
    
      const input = {
        input: "My name is John Doe and I live in San Francisco.",
      };
      const response = await model.generate(input);
    
      console.log(response.results);
    };
    
    main();
    
    
    copy

### Fill Mask

[List of fill mask models](/models/fill-mask)

JavaScriptbash

    
    
    import { FillMask } from "deepinfra";
    
    const DEEPINFRA_API_KEY = "$DEEPINFRA_TOKEN";
    const MODEL = "bert-base-cased";
    
    const main = async () => {
      const model = new FillMask(MODEL, DEEPINFRA_API_KEY);
    
      const body = {
        input: "I need my [MASK] right now!",
      };
      const response = await model.generate(body);
    
      console.log(response.results);
    };
    
    main();
    
    
    
    copy

### Image Classification

[List of image classification models](/models/image-classification)

JavaScriptbash

    
    
    import { ImageClassification } from "deepinfra";
    import path from "path";
    import { fileURLToPath } from 'url';
    
    
    const __filename = fileURLToPath(import.meta.url);
    const __dirname = path.dirname(__filename);
    
    const DEEPINFRA_API_KEY = "$DEEPINFRA_TOKEN";
    const MODEL = "google/vit-base-patch16-224";
    
    const main = async () => {
      const model = new ImageClassification(MODEL, DEEPINFRA_API_KEY);
    
      const input = {
        image: path.join(__dirname, "image.jpg"),
      };
      const response = await model.generate(input);
    
      console.log(response.results);
    };
    
    main();
    
    
    copy

### Zero-Shot Image Classification

[List of zero-shot image classification models](/models/zero-shot-image-
classification)

JavaScriptbash

    
    
    import { ZeroShotImageClassification } from "deepinfra";
    import path from "path";
    import { fileURLToPath } from 'url';
    
    
    const __filename = fileURLToPath(import.meta.url);
    const __dirname = path.dirname(__filename);
    
    const DEEPINFRA_API_KEY = "$DEEPINFRA_TOKEN";
    const MODEL = "openai/clip-vit-base-patch32";
    
    const main = async () => {
      const model = new ZeroShotImageClassification(MODEL, DEEPINFRA_API_KEY);
    
      const body = {
        image: path.join(__dirname, "image.jpg"),
        candidate_labels: ["dog", "cat", "car", "horse", "person"],
      };
    
      const response = await model.generate(body);
      console.log(response.results);
    };
    
    main();
    
    
    copy

### Text Classification

[List of text classification models](/models/text-classification)

JavaScriptbash

    
    
    import { TextClassification } from "deepinfra";
    
    const DEEPINFRA_API_KEY = "$DEEPINFRA_TOKEN";
    const MODEL = "ProsusAI/finbert";
    
    const main = async () => {
      const model = new TextClassification(MODEL, DEEPINFRA_API_KEY);
    
      const body = {
        input:
          "Nvidia announces new AI chips months after latest launch as market competition heats up",
      };
    
      const response = await model.generate(body);
      console.log(response.results);
    };
    
    main();
    
    
    copy
    
    
    curl -X POST \
        -d '{"input": "Nvidia announces new AI chips months after latest launch as market competition heats up"}'  \
        -H "Authorization: Bearer $DEEPINFRA_TOKEN" \
        -H 'Content-Type: application/json'  \
        'https://api.deepinfra.com/v1/inference/ProsusAI/finbert'
    
    
    copy

[OpenAI-Compatible API](/docs/openai_api)[Rate Limits](/docs/advanced/rate-
limits)

![Footer Logo](/_next/static/media/footer_logo.b3e9d8d3.svg)

![SOC 2
Certified](https://static.sprinto.com/_next/static/images/framework/soc2.png)![ISO
27001
Certified](https://static.sprinto.com/_next/static/images/framework/iso-27001.png)

Have questions or need a custom solution?

[Contact Sales](/contact-sales)

Company

[Pricing](/pricing)

[Docs](/docs)

[Compare](/compare)

[DeepStart](/deepstart)

[About](/about_us)

[Careers](https://jobs.gem.com/deep-infra)

[Contact us](/contact-sales)

[Trust Center](https://trust.deepinfra.com)

[DeepGPT](https://deepgpt.com)

Latest Models

[moonshotai/Kimi-K2-Instruct-0905](/moonshotai/Kimi-K2-Instruct-0905)[deepseek-
ai/DeepSeek-V3.2-Exp](/deepseek-ai/DeepSeek-V3.2-Exp)[deepseek-
ai/DeepSeek-V3.1](/deepseek-ai/DeepSeek-V3.1)[zai-org/GLM-4.6](/zai-
org/GLM-4.6)[anthropic/claude-3-7-sonnet-latest](/anthropic/claude-3-7-sonnet-
latest)

Featured Models

[anthropic/claude-4-sonnet](/anthropic/claude-4-sonnet)[openai/gpt-
oss-120b](/openai/gpt-
oss-120b)[google/gemma-3-27b-it](/google/gemma-3-27b-it)[MiniMaxAI/MiniMax-M2](/MiniMaxAI/MiniMax-M2)[mistralai/Voxtral-
Mini-3B-2507](/mistralai/Voxtral-Mini-3B-2507)

![Built With Love in Palo Alto](/_next/static/media/love.ce60156e.svg)

[](https://linkedin.com/company/deep-
infra)[](https://x.com/DeepInfra)[](https://github.com/DeepInfra)[](https://discord.gg/x88dCvhqYq)

© 2026 Deep Infra. All rights reserved.

[Privacy Policy](/privacy)[Terms of Service](/terms)

