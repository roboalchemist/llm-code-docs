# Make sure to install the huggingface_hub package before
from huggingface_hub import InferenceClient

client = InferenceClient(model="http://127.0.0.1:8080")
client.text_generation(prompt="What is Deep Learning?")
```

  </TabItem>
  <TabItem value="typescript" label="Using JavaScript" default>

```typescript
async function query() {
    const response = await fetch(
        'http://127.0.0.1:8080/generate',
        {
            method: 'POST',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify({
                'inputs': 'What is Deep Learning?'
            })
        }
    );
}

query().then((response) => {
    console.log(JSON.stringify(response));
});
```

  </TabItem>
  <TabItem value="curl" label="Using cURL" default>

```
curl 127.0.0.1:8080/generate \
-X POST \
-d '{"inputs":"What is Deep Learning?","parameters":{"max_new_tokens":20}}' \
-H 'Content-Type: application/json'
```

  </TabItem>
</Tabs>


[TensorRT]
Source: https://docs.mistral.ai/docs/deployment/self-deployment/trt

## Building the engine

Follow the official TensorRT-LLM documentation to [build the engine](https://github.com/NVIDIA/TensorRT-LLM/tree/main#quick-start).
- For Mistral-7B, you can use the [LLaMA example](https://github.com/NVIDIA/TensorRT-LLM/tree/main/examples/llama#mistral-v01)
- For Mixtral-8X7B, official documentation coming soon...


## Deploying the engine

Once the engine is built, it can be deployed using the Triton inference server and its TensorRTLLM backend.

Follow the [official documentation](https://github.com/triton-inference-server/tensorrtllm_backend#using-the-tensorrt-llm-backend).


[vLLM]
Source: https://docs.mistral.ai/docs/deployment/self-deployment/vllm

[vLLM](https://github.com/vllm-project/vllm) is an open-source LLM inference and serving 
engine. It is particularly appropriate as a target platform for self-deploying Mistral 
models on-premise.

## Pre-requisites

- The hardware requirements for vLLM are listed on its [installation documentation page](https://docs.vllm.ai/en/latest/getting_started/installation.html).
- By default, vLLM sources the model weights from Hugging Face. To access Mistral model
  repositories you need to be authenticated on Hugging Face, so an access
  token `HF_TOKEN` with the `READ` permission will be required. You should also make sure that you have
  accepted the conditions of access on each model card page.
- If you already have the model artifacts on your infrastructure you can use 
  them directly by pointing vLLM to their local path instead of a Hugging Face
  model ID. In this scenario you will be able to skip all Hugging Face related 
  setup steps.


## Getting started

The following sections will guide you through the process of deploying and
querying Mistral models on vLLM.

### Installing vLLM

- Create a Python virtual environment and install the `vllm` package (version 
  `>=0.6.1.post1` to ensure maximum compatibility with all Mistral models).

- Authenticate on the HuggingFace Hub using your access token `$HF_TOKEN` :
  ```bash
  huggingface-cli login --token $HF_TOKEN
  ```

### Offline mode inference

When using vLLM in _offline mode_ the model is loaded and used for one-off
batch inference workloads.

<Tabs>
    <TabItem value="vllm-batch-nemo" label="Text input (Mistral NeMo)">

        ```python
        from vllm import LLM
        from vllm.sampling_params import SamplingParams

        model_name = "mistralai/Mistral-NeMo-Instruct-2407"
        sampling_params = SamplingParams(max_tokens=8192)

        llm = LLM(
            model=model_name,
            tokenizer_mode="mistral",
            load_format="mistral",
            config_format="mistral",
        )

        messages = [
            {
                "role": "user",
                "content": "Who is the best French painter. Answer with detailed explanations.",
            }
        ]

        res = llm.chat(messages=messages, sampling_params=sampling_params)
        print(res[0].outputs[0].text)

        ```

    </TabItem>

        <TabItem value="vllm-batch-small" label="Text input (Mistral Small)">

        ```python
        from vllm import LLM
        from vllm.sampling_params import SamplingParams

        model_name = "mistralai/Mistral-Small-Instruct-2409"
        sampling_params = SamplingParams(max_tokens=8192)

        llm = LLM(
            model=model_name,
            tokenizer_mode="mistral",
            load_format="mistral",
            config_format="mistral",
        )

        messages = [
            {
                "role": "user",
                "content": "Who is the best French painter. Answer with detailed explanations.",
            }
        ]

        res = llm.chat(messages=messages, sampling_params=sampling_params)
        print(res[0].outputs[0].text)

        ```

    </TabItem>

    <TabItem value="vllm-batch-pixtral" label="Image + text input (Pixtral-12B)">
        Suppose you want to caption the following images:
          <center>
              <a href="https://picsum.photos/id/1/512/512"><img alt="" src="/img/laptop.png" width="20%"/></a>
              <a href="https://picsum.photos/id/11/512/512"><img alt="" src="/img/countryside.png"  width="20%"/></a>
              <a href="https://picsum.photos/id/111/512/512"><img alt="" src="/img/vintage_car.png"  width="20%"/></a>
          </center>

        You can do so by running the following code:

        ```python
        from vllm import LLM
        from vllm.sampling_params import SamplingParams

        model_name = "mistralai/Pixtral-12B-2409"
        max_img_per_msg = 3

        sampling_params = SamplingParams(max_tokens=8192)
        llm = LLM(
            model=model_name,
            tokenizer_mode="mistral",
            load_format="mistral",
            config_format="mistral",
            limit_mm_per_prompt={"image": max_img_per_msg},
        )

        urls = [f"https://picsum.photos/id/{id}/512/512" for id in ["1", "11", "111"]]

        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this image"},
                    ] + [{"type": "image_url", "image_url": {"url": f"{u}"}} for u in urls],
            },
        ]

        res = llm.chat(messages=messages, sampling_params=sampling_params)
        print(res[0].outputs[0].text)
        ```
    </TabItem>
</Tabs>

### Server mode inference

In _server mode_, vLLM spawns an HTTP server that continuously
waits for clients to connect and send requests concurrently.
The server exposes a REST API that implements the OpenAI protocol,
allowing you to directly reuse existing code relying on the OpenAI API.

<Tabs>
    <TabItem value="vllm-server-text" label="Text input (Mistral NeMo)">
        Start the inference server to deploy your model, e.g. for Mistral NeMo:

          ```bash
          vllm serve mistralai/Mistral-Nemo-Instruct-2407 \
            --tokenizer_mode mistral \
            --config_format mistral \
            --load_format mistral
          ```

        You can now run inference requests with text input:

          <Tabs>
            <TabItem value="vllm-infer-nemo-curl" label="cURL">
                ```bash
                curl --location 'http://localhost:8000/v1/chat/completions' \
                    --header 'Content-Type: application/json' \
                    --header 'Authorization: Bearer token' \
                    --data '{
                        "model": "mistralai/Mistral-Nemo-Instruct-2407",
                        "messages": [
                          {
                            "role": "user",
                            "content": "Who is the best French painter? Answer in one short sentence."
                          }
                        ]
                      }'
                ```
            </TabItem>
            <TabItem value="vllm-infer-nemo-python" label="Python">
                ```python
                import httpx

                url = 'http://localhost:8000/v1/chat/completions'
                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer token'
                }
                data = {
                    "model": "mistralai/Mistral-Nemo-Instruct-2407",
                    "messages": [
                        {
                            "role": "user",
                            "content": "Who is the best French painter? Answer in one short sentence."
                        }
                    ]
                }

                response = httpx.post(url, headers=headers, json=data)

                print(response.json())

                ```
            </TabItem>
          </Tabs>

    </TabItem>

        <TabItem value="vllm-server-text-small" label="Text input (Mistral Small)">
        Start the inference server to deploy your model, e.g. for Mistral Small:

          ```bash
          vllm serve mistralai/Mistral-Small-Instruct-2409 \
            --tokenizer_mode mistral \
            --config_format mistral \
            --load_format mistral
          ```

        You can now run inference requests with text input:

          <Tabs>
            <TabItem value="vllm-infer-small-curl" label="cURL">
                ```bash
                curl --location 'http://localhost:8000/v1/chat/completions' \
                    --header 'Content-Type: application/json' \
                    --header 'Authorization: Bearer token' \
                    --data '{
                        "model": "mistralai/Mistral-Small-Instruct-2409",
                        "messages": [
                          {
                            "role": "user",
                            "content": "Who is the best French painter? Answer in one short sentence."
                          }
                        ]
                      }'
                ```
            </TabItem>
            <TabItem value="vllm-infer-small-python" label="Python">
                ```python
                import httpx

                url = 'http://localhost:8000/v1/chat/completions'
                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer token'
                }
                data = {
                    "model": "mistralai/Mistral-Small-Instruct-2409",
                    "messages": [
                        {
                            "role": "user",
                            "content": "Who is the best French painter? Answer in one short sentence."
                        }
                    ]
                }

                response = httpx.post(url, headers=headers, json=data)

                print(response.json())

                ```
            </TabItem>
          </Tabs>

    </TabItem>

    <TabItem value="vllm-server-mm" label="Image + text input (Pixtral-12B)">


Start the inference server to deploy your model, e.g. for Pixtral-12B:

    ```bash
    vllm serve mistralai/Pixtral-12B-2409 \
        --tokenizer_mode mistral \
        --config_format mistral \
        --load_format mistral
    ```
:::info

- The default number of image inputs per prompt is set to 1. To increase it, set the
  `--limit_mm_per_prompt` option (e.g. `--limit_mm_per_prompt 'image=4'`).

- If you encounter memory issues, set the `--max_model_len` option to reduce the
  memory requirements of vLLM (e.g. `--max_model_len 16384`). More troubleshooting
  details can be found in the 
  [vLLM documentation](https://qwen.readthedocs.io/en/latest/deployment/vllm.html#troubleshooting).

:::

You can now run inference requests with images and text inputs. Suppose you
want to caption the following image:

        <center>
            <a href="https://picsum.photos/id/237/512/512"><img alt="" src="/img/doggo.png"  width="20%"/></a>
        </center>
        <br/>

You can prompt the model and retrieve its response like so:
    <Tabs>
        <TabItem value="vllm-infer-pixtral-curl" label="cURL">
        ```bash
        curl --location 'http://localhost:8000/v1/chat/completions' \
        --header 'Content-Type: application/json' \
        --header 'Authorization: Bearer token' \
        --data '{
            "model": "mistralai/Pixtral-12B-2409",
            "messages": [
              {
                "role": "user",
                "content": [
                    {"type" : "text", "text": "Describe this image in a short sentence."},
                    {"type": "image_url", "image_url": {"url": "https://picsum.photos/id/237/200/300"}}
                ]
              }
            ]
          }'
          ```
        </TabItem>
        <TabItem value="vllm-infer-pixtral-python" label="Python">
      ```python
        import httpx

        url = "http://localhost:8000/v1/chat/completions"
        headers = {"Content-Type": "application/json", "Authorization": "Bearer token"}
        data = {
            "model": "mistralai/Pixtral-12B-2409",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Describe this image in a short sentence."},
                        {
                            "type": "image_url",
                            "image_url": {"url": "https://picsum.photos/id/237/200/300"},
                        },
                    ],
                }
            ],
        }

        response = httpx.post(url, headers=headers, json=data)

        print(response.json())
        ```
        </TabItem>
    </Tabs>


    </TabItem>
</Tabs>

## Deploying with Docker

If you are looking to deploy vLLM as a containerized inference server you can leverage
the project's official Docker image (see more details in the 
[vLLM Docker documentation](https://docs.vllm.ai/en/latest/serving/deploying_with_docker.html)).

- Set the HuggingFace access token environment variable in your shell:
  ```bash
  export HF_TOKEN=your-access-token
  ```

- Run the Docker command to start the container:
  <Tabs>
    <TabItem value="vllm-docker-nemo" label="Mistral NeMo">
        ```bash
        docker run --runtime nvidia --gpus all \
            -v ~/.cache/huggingface:/root/.cache/huggingface \
            --env "HUGGING_FACE_HUB_TOKEN=${HF_TOKEN}" \
            -p 8000:8000 \
            --ipc=host \
            vllm/vllm-openai:latest \
            --model mistralai/Mistral-NeMo-Instruct-2407 \
            --tokenizer_mode mistral \
            --load_format mistral \
            --config_format mistral
        ```
    </TabItem>

    <TabItem value="vllm-docker-small" label="Mistral Small">
        ```bash
        docker run --runtime nvidia --gpus all \
            -v ~/.cache/huggingface:/root/.cache/huggingface \
            --env "HUGGING_FACE_HUB_TOKEN=${HF_TOKEN}" \
            -p 8000:8000 \
            --ipc=host \
            vllm/vllm-openai:latest \
            --model mistralai/Mistral-Small-Instruct-2409 \
            --tokenizer_mode mistral \
            --load_format mistral \
            --config_format mistral
        ```
    </TabItem>

    <TabItem value="vllm-docker-pixtral" label="Pixtral-12B">
        ```bash
        docker run --runtime nvidia --gpus all \
            -v ~/.cache/huggingface:/root/.cache/huggingface \
            --env "HUGGING_FACE_HUB_TOKEN=${HF_TOKEN}" \
            -p 8000:8000 \
            --ipc=host \
            vllm/vllm-openai:latest \
            --model mistralai/Pixtral-12B-2409 \
            --tokenizer_mode mistral \
            --load_format mistral \
            --config_format mistral 
        ```
    </TabItem>
  </Tabs>
  
Once the container is up and running you will be able to run inference on your model
using the same code as in a standalone deployment.


[SDK Clients]
Source: https://docs.mistral.ai/docs/getting-started/clients

We provide client codes in both Python and Typescript.

## Python 

You can install our [Python Client](https://github.com/mistralai/client-python) by running:
```bash
pip install mistralai
```

Once installed, you can run the chat completion: 
```python

from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model = model,
    messages = [
        {
            "role": "user",
            "content": "What is the best French cheese?",
        },
    ]
)

print(chat_response.choices[0].message.content)

```

See more examples [here](https://github.com/mistralai/client-python/tree/main/examples).

## Typescript

You can install our [Typescript Client](https://github.com/mistralai/client-ts) in your project using:

```bash
npm install @mistralai/mistralai
```

Once installed, you can run the chat completion:

```typescript


const apiKey = process.env.MISTRAL_API_KEY || 'your_api_key';

const client = new Mistral({apiKey: apiKey});

const chatResponse = await client.chat.complete({
  model: 'mistral-tiny',
  messages: [{role: 'user', content: 'What is the best French cheese?'}],
});

console.log('Chat:', chatResponse.choices[0].message.content);
```

See more examples [here](https://github.com/mistralai/client-js/tree/main/examples).

## Third-party clients

Here are some clients built by the community for various other languages:

This section lists third-party clients in other languages provided by the community.
Please note that these clients are not actively maintained or supported by Mistral AI.
We recommend reaching out to the respective maintainers for any assistance or inquiries.

### CLI
[icebaker/nano-bots](https://github.com/icebaker/ruby-nano-bots)

### Dart
[nomtek/mistralai_client_dart](https://github.com/nomtek/mistralai_client_dart)

### Elixir
[axonzeta/mistral_elixir](https://github.com/axonzeta/mistral_elixir)

### Go
[Gage-Technologies](https://github.com/Gage-Technologies/mistral-go)

### Java
[langchain4j](https://github.com/langchain4j/langchain4j)
[Spring AI](https://github.com/spring-projects/spring-ai)

### JavaScript / TypeScript
[Vercel AI SDK](https://github.com/vercel/ai)

### PHP
[HelgeSverre/mistral](https://github.com/HelgeSverre/mistral)
[partITech/php-mistral](https://github.com/partITech/php-mistral)

### Ruby
[gbaptista/mistral-ai](https://github.com/gbaptista/mistral-ai)
[wilsonsilva/mistral](https://github.com/wilsonsilva/mistral)

### Rust
[ivangabriele/mistralai-client-rs](https://github.com/ivangabriele/mistralai-client-rs)


[Bienvenue to Mistral AI Documentation]
Source: https://docs.mistral.ai/docs/getting-started/docs_introduction

Mistral AI is a research lab building the best open source models in the world. La Plateforme enables developers and enterprises to build new products and applications, powered by Mistral’s open source and commercial LLMs. 

## Mistral AI Large Language Models (LLMs)

We release both premier models and free models, driving innovation and convenience for our developer community. Our models are state-of-the-art for their multilingual, code generation, maths, and advanced reasoning capabilities.

### Premier models

- Mistral Medium, a state-of-the-art model perfectly balancing frontier-class multimodal performance with size and pricing, was released [May 2025](https://mistral.ai/news/mistral-medium-3/)
- Codestral, our cutting-edge language model for coding with the latest version released [January 2025](https://mistral.ai/news/codestral-2501/)
- Mistral OCR, our OCR service that enables our users to extract interleaved text and images released [May 2025](https://mistral.ai/solutions/document-ai)
- Mistral Saba, a leader in small models category trained extensively on languages from the Middle East and South Asia released [February 2025](https://mistral.ai/news/mistral-saba/)
- Mistral Large, our top-tier reasoning model for high-complexity tasks with the lastest version released [November 2024](https://mistral.ai/news/pixtral-large/)
- Pixtral Large, our frontier-class multimodal model released [November 2024](https://mistral.ai/news/pixtral-large/)
- Ministral 3B, world’s best edge model released [October 2024](https://mistral.ai/news/ministraux/)
- Ministral 8B, powerful edge model with extremely high performance/price ratio released [October 2024](https://mistral.ai/news/ministraux/)
- Mistral Embed, our state-of-the-art semantic for extracting representation of text extracts
- Mistral Moderation, our moderation service that enables our users to detect harmful text content

### Free models
- Mistral Small, a new multimodal leader in the small models category with the lastest version v3.1 released [March 2025](https://mistral.ai/news/mistral-small-3-1/)
- Devstral Small, a new SOTA coding model that excels at using tools to explore codebases, editing multiple files and power software engineering agents released [May 2025](https://mistral.ai/news/devstral/)
- Pixtral, a 12B model with image understanding capabilities in addition to text released [September 2024](https://mistral.ai/news/pixtral-12b/)
- Mistral NeMo, a powerfull open source model released [July 2024](https://mistral.ai/news/mistral-nemo/)
- Codestral Mamba, our first mamba 2 open source model released [July 2024](https://mistral.ai/news/codestral-mamba/)
- Mathstral 7b, our first math open source model released [July 2024](https://mistral.ai/news/mathstral/)

Learn more about our models [here](/getting-started/models/models_overview).

## Explore the Mistral AI APIs

The [Mistral AI APIs](https://console.mistral.ai/) empower LLM applications via:

- [Text generation](/capabilities/completion), enables streaming and provides the ability to display partial model results in real-time
- [Vision](/capabilities/vision), enables the analysis of images and provides insights based on visual content in addition to text.
- [OCR](/capabilities/OCR/basic_ocr), allows the extraction of interleaved text and images from documents.
- [Code generation](/capabilities/code_generation), enpowers code generation tasks, including fill-in-the-middle and code completion.
- [Embeddings](/capabilities/embeddings/overview), useful for RAG where it represents the meaning of text as a list of numbers.
- [Function calling](/capabilities/function_calling), enables Mistral models to connect to external tools.
- [Citations](/capabilities/citations), allows the output of citations for RAG use cases.
- [Structured Outputs](/capabilities/structured-output/structured_output_overview), enables Mistral models to have structured or json outputs.
- [Fine-tuning](/capabilities/finetuning), enables developers to create customized and specialized models.
- [Guardrailing](/capabilities/guardrailing), enables developers to enforce policies at the system level of Mistral models.


[Glossary]
Source: https://docs.mistral.ai/docs/getting-started/glossary

## LLM

LLMs (Large Language Models), such as the Mistral AI models, are AI models trained on 
extensive text data to predict the next word in a sentence. 
They are capable of understanding and generating text in a way that's similar to how humans communicate. 
They can answer questions, draft documents, summarize texts, extract information, translate languages, write code, and more. 

## Text generation
Text generation in large language models is the process of producing coherent and contextually relevant text 
based on a given input prompt. These models, such as Mistral AI, are trained on vast amounts of text data to 
predict the next word in a sentence, given the previous words as context. This capability enables them to 
generate text that is similar to human communication and can be used for various applications, 
including answering questions, drafting documents, summarizing texts, translating languages, 
and coding. 

## Tokens 
Tokens serve as the smallest individual units that a language model processes, typically 
representing common sequences of characters such as words or subwords. In order for a 
language model to comprehend text, it must be converted into numerical representations. 
This is accomplished by encoding the text into a series of tokens, where each token is 
assigned a unique numerical index. The process of converting text into tokens is known
as tokenization. One widely used tokenization algorithm is Byte-Pair Encoding (BPE), 
which initially treats each byte in a text as a separate token. BPE then iteratively adds 
new tokens to the vocabulary for the most frequent pair of tokens in the corpus, replacing
occurrences of the pair with the new token, until no more replacements can be made. This 
results in a compact and efficient representation of the text for processing by the 
language model.

## Mixture of Experts 
Mixture of Experts (MoE) is the underlying architecture of 
Mixtral 8x7b and Mixtral 8x22b. It is a neural network architecture 
that incorporates expert layers within the Transformer block, 
allowing models to be pretrained with much less compute 
while maintaining the same quality as dense models. 
This is achieved by replacing dense feed-forward network (FFN) layers with sparse MoE layers,
which contain multiple "experts" (FFNs). 
A gate network or router determines which input tokens are sent to which expert 
for computation. MoE offers benefits such as efficient pretraining and faster inference, 
but also presents challenges like overfitting during fine-tuning and high memory 
requirements. Nevertheless, MoE is a valuable method for achieving improved model 
quality at lower computing costs by dynamically assigning input tokens to 
specialized experts for processing.

## RAG
Retrieval-augmented generation (RAG) is an AI framework that synergizes the capabilities of LLMs and information 
retrieval systems. There are two main steps in RAG: 1) retrieval: retrieve relevant information from a knowledge base with text 
embeddings stored in a vector store; 2) generation: insert the relevant information to the prompt for the LLM 
to generate information. RAG is useful to answer questions or generate content leveraging external knowledge including
up-to-date information and domain-specific information.
RAG allows the model to access and utilize information beyond its training data, reducing hallucination and 
improving factual accuracy. Check out our [Basic RAG](/guides/rag/) guide for details. 

## Fine-tuning
Fine-tuning is a process used in large language models to adapt a pre-trained model to a specific task or domain. 
It involves continuing the training process on a smaller, task-specific dataset and adjusting the model's 
parameters to optimize its performance on the new dataset. This enables the model to learn task-specific 
language patterns and improve its performance on the target task. Fine-tuning can be 
beneficial for adapting the model to a particular format or tone, 
domain-specific tasks, and improving performance through distillation from a larger model.
This approach can achieve state-of-the-art performance with fewer data and computational 
resources compared to training a model from scratch.

## Function calling 
Function calling allows Mistral models to connect to external tools and 
call external functions or APIs to perform tasks 
beyond the model's capabilities. This allows the model to access and leverage external 
tools and resources to improve its performance and provide more accurate responses. 
Function calling can be used for tasks such as retrieving real-time data, 
performing calculations, accessing databases, and interacting with other systems or services.
It improves the model's accuracy, efficiency, and versatility. 
Check out our [Function Calling](/capabilities/function_calling/) guide to learn more. 


## Embeddings 
Embeddings are vectorial representations of text that capture the semantic meaning of 
paragraphs through their position in a high dimensional vector space. 
These vectors capture the semantic meaning and context of the text, 
allowing the model to understand and generate language more effectively.
Mistral AI Embeddings API offers cutting-edge, state-of-the-art embeddings for text, 
which can be used for many NLP tasks. Check out our [Embeddings](/capabilities/embeddings/overview) guide 
to learn more. 

## Temperature
Temperature is a fundamental sampling parameter in LLMs that controls the randomness and diversity of the generated outputs. Lower Temperature values result in more deterministic and accurate responses, while higher values introduce more creativity and randomness. This parameter affects the softmax function, which normalizes logits into a probability distribution. Higher Temperatures flatten the distribution, making less likely tokens more probable, while lower Temperatures sharpen the distribution, favoring the most likely tokens. Adjusting the Temperature allows for tailoring the model's behavior to suit different applications, such as requiring high accuracy for tasks like mathematics or classification, or enhancing creativity for tasks like brainstorming or writing novels. Balancing creativity and coherence is crucial, as increasing Temperature can also introduce inaccuracies. Some models, such as `pixtral-12b`, `ministral-3b-2410`, `ministral-8b-2410` and `open-mistral-nemo` have a factor of 0.43 on temperature when used via our services, to align better with how it impacts other models and unify model behaviour.


[Model customization]
Source: https://docs.mistral.ai/docs/getting-started/model_customization

### Otherwise known as "How to Build an Application with a Custom Model"

## Overview
The following is a quick guide on how to build an application with a custom model. Our goal is to help developers build product operations for LLMs to go from a prototype to deployment.

AI is a tool, building applications that harness AI make them more useful and practical to your end users.

Before LLMs, AI applications were built around personalization, precision, and prediction. Traditional AI applications are catered towards predicting your next choice and recommending it to you based on your previous behavior and “customers like you”.

In contrast, LLM applications are built around Human-AI collaboration. As a developer and the end user, you have more agency in the customisation of your product. You can create something that did not exist before. 

Applications built with custom LLMs require an iterative development cycle, relying on continuous end user feedback and rigorous evals to ensure that your custom model behavior is aligned to the intended application behavior.

## Key terms
Before we get started, let’s define key terms:

**Application behavior** can be defined as the user interaction. It takes into account usability, performance, safety, and adaptability. Application behavior includes Objectives and Values.

**Model behavior** can be defined as the expected, appropriate, and acceptable way of an LLM acting in a specific context or application boundaries. Model behavior includes Objectives and Values.

**Objectives** determine whether the model behavior is in line with the expected application behavior. 

**Values** denotes the developers’ intended policy for the model and application. This can be a set of rules, a Constitution, or even a fictional character’s morals.

## Steerability: three methods
There are several techniques (with varying levels of engineering complexity) available to steer model behavior within your application context. We recommend leveraging the three methods below to do so:
1. **System prompt**
2. **Tune a model**
3. **Deploy a moderation layer** for input/output processing

A **System Prompt** is a method to provide context, instructions, and guidelines to your model before the model is tasked with user input data ([prompt guide](/guides/prompting_capabilities/)). By using a system prompt, you can steer the model to better align to your intended product behavior - whether the application is a conversation or task, you can specify a persona, personality, tone, values, or any other relevant information that may help your model better perform in response to the end user’s input.

System prompts can include:
- Clear and specific instructions and objectives
- Roles, desired persona and tone
- Guidance on style e.g. verbosity constraints
- Value definitions e.g. policies, rules and safeguards
- Desired output format

**Tuning a model** is a method to train the model on your intended application behavior ([fine-tuning guide](/guides/finetuning/)). Two popular approaches for tuning LLMs:
1. **Application tuning**, where you leverage a dataset of examples specified to the desired behavior of your application.
2. **Safety tuning**, where you leverage a dataset that specifies both example inputs that might result in unsafe behavior, along with the desired safe output in that situation.

**Deploying a classifier for content moderation** is a third method to create guardrails for your model’s behavior within the application. This is considered an extra security measure in case you are deploying your application to end users.

## Guide for tuning a model to your intended application behavior
### Step 1: Define your intended Application Behavior
The first step is to define the Objectives, i.e. how you want users to interact with your LLM product. 

For inspiration, look to developers building with Mistral models: 
- standalone products like conversational assistants; 
- within pre-existing products to complete a specific task like “Summarize” or “Translate” or enable new capabilities like function calling with API access for “Knowledge retrieval”.

Learn how others are building products with custom models here: [developer examples](/getting-started/stories/).
### Step 2: Define your policies based on your Values
When you deploy an LLM within an end-user facing application, you identify which Values the model will need to abide by in order to meet your Content Moderation guidelines along with your user expectations.

For Content Moderation, look for inspiration from [Llama Guard](https://ai.meta.com/research/publications/llama-guard-llm-based-input-output-safeguard-for-human-ai-conversations/)’s categories like Privacy, Hate, and Specialized Advice and [ML Commons Taxonomy](https://drive.google.com/file/d/1V8KFfk8awaAXc83nZZzDV2bHgPT8jbJY/view) categories like CSAM and Hate.

### Step 3: Create your Application Evals
The goal of your evals is to enable you to have better signal on whether your custom model’s behavior will meet your Application behavior before deployment. Identifying how you want to evaluate your custom model will help determine the type of training data to include in the fine-tuning.

There are two methods to evaluate an LLM:
- **Automated Evals**
    - **Metrics-based**, similar to the public benchmark evaluations where you can derive a metric from pre-annotated data for example.
    - **LLM-based**, where you leverage a different LLM like Mistral Large to evaluate or judge the output of your custom model.
- **Human-based Evals**, where you employ Content Annotators to evaluate or judge the output of your custom model and collect Human annotations.

For more on how to conduct an LLM Evaluation, check out our [evaluation guide](/guides/evaluation).

### Step 4: Test your application behavior hypothesis with an MVP powered by Mistral Large
Once you understand the intent of your custom LLM and the contours of how you want the model to behave, begin by testing your application hypothesis with Mistral Large and collect the interaction data to better understand how your end users may interact with your LLM. For example, many developers begin their process by creating a Demo or MVP with limited access (a Private Beta).

For some applications, a system prompt is the best solution for an aligned model behavior. If you need help deciding between the two, look to our [fine-tuning guide](/capabilities/finetuning). 

If a system prompt works creating a Custom Model, skip to Step 6.

### Step 5: Tune for model alignment
Now that you have sense of the Application Behavior - Values and Objectives included - you are intending to adopt a custom model, you can begin the process of replacing Mistral Large for a smaller, custom model.

Look to our guide on how to [prepare your Tuning dataset](/guides/finetuning/#prepare-the-dataset).

Areas to consider when preparing your Tuning Dataset for better model performance:
- **Data Comprehension**, include all content policies for each application use case in your dataset (such as question-answering, summarization, and reasoning).
- **Data Variety**, ensure dataset diversity across query length, structure, tone, topic, levels of complexity, and demographic considerations.
- **Deduplication**, remove duplicates to prevent your tuning data being memorized.
- **Avoid Data Contamination**, isolate evaluation data from the tuning dataset.
- **Ethical Data Practices**, provide clear labeling guidelines and Annotator diversity to minimize model errors and bias.

For content moderation, get started with open source datasets like [Safety-Tuned LlaMAs](https://arxiv.org/abs/2309.07875).

At Mistral, we support two ways to customize our models:
1. OSS with the [FT Codebase](https://github.com/mistralai/mistral-finetune/)
2. Via [la Plateforme](https://console.mistral.ai/)

Head to our FT API within la Plateforme, upload and validate your training data. Run the job, and when completed, you can access your custom model via your own model API endpoint.

### Step 6: Test your custom model with your Evals
Now that you have your custom model API endpoint, you can run Application Evals from Step 4. Depending on your Application, remember to include Safety Evals in your Eval set:
- **Development Evaluations**, include ongoing assessments during training and fine-tuning to compare model performance against launch criteria and evaluate the impact of mitigation strategies. These evaluations use adversarial queries or external academic benchmarks.
- **Assurance Evaluations**, set up governance and review assessments at key milestones by an external group. These standardized evaluations use strictly managed datasets and provide high-level insights for mitigation efforts. They test safety policies and dangerous capabilities, such as biohazards, persuasion, and cybersecurity.
- **Red Teaming** requires adversarial testing by specialist teams using less structured methods to discover potential weaknesses and improve risk mitigation and evaluation approaches.
- **External Evaluations**, includes assessments by independent, external domain experts to identify model limitations and stress-test performance.

Based on the model performance, either retrain your model with new training data to support better model performance or deploy into your application by switching the Mistral Large API with your custom model endpoint.

### Step 7: Once deployed, continuously monitor and update your custom model, evals, and testing based on real life application data

Congrats! You’ve deployed your custom model into your application.


[Models Benchmarks]
Source: https://docs.mistral.ai/docs/getting-started/models/benchmark

LLM (Large Language Model) benchmarks are standardized tests or datasets used to evaluate the performance of large language models. These benchmarks help researchers and developers understand the strengths and weaknesses of their models and compare them with other models in a systematic way. 

## Mistral benchmarks
Mistral demonstrates top-tier reasoning capabilities and excels in advanced reasoning, multilingual tasks, math, and code generation. The company reports benchmark results on popular public benchmarks such as MMLU (Massive Multitask Language Understanding), MT-bench, and others.

You can find the benchmark results in the following blog posts: 
- [Magistral Medium](https://mistral.ai/news/magistral/): Our frontier-class reasoning model built on top of Mistral Medium 3, offering state-of-the-art reasoning capabilities for enterprise use cases.
- [Magistral Small](https://mistral.ai/news/magistral/): Our small reasoning model built on top of Mistral Small 3, a compact open model with high-performance reasoning.
- [Mistral Medium](https://mistral.ai/news/mistral-medium-3/): A cutting-edge multimodal model.
It can be used for professional use cases, coding, function-calling and reasoning tasks.
- [Pixtral Large](https://mistral.ai/news/pixtral-large/): Pixtral Large is a 124B open-weights multimodal model built on top of Mistral Large 2. It is the second model in our multimodal family and demonstrates frontier-level image understanding.
- [Pixtral 12B](https://mistral.ai/news/pixtral-12b/): Pixtral 12B the first open-source model to demonstrate state-of-the-art multimodal understanding, without regressing on abilities in pure text. 
- [Mistral Large](https://mistral.ai/news/mistral-large-2407/): A cutting-edge text generation model with top-tier reasoning capabilities.
It can be used for complex multilingual reasoning tasks, including text understanding, transformation, and code generation.
- [Mistral Small](https://mistral.ai/news/mistral-small-3-1/): A powerful and efficient multimodal model with high level conversational and translation capabilities.
- [Devstral Small](https://mistral.ai/news/devstral/): A powerful and efficient 24B text model. Debuting as #1 open source model on SWE-bench. This model has high agentic capabilities, performing well with OpenHands and SWE-agent code agent frameworks.
- [Mistral Saba](https://mistral.ai/news/mistral-saba/): A powerful and efficient text generation model trained extensively on languages from the Middle East and South Asia, achieving state-of-the-art quality comparable to much larger models.
It can be used for complex multilingual reasoning tasks, including text understanding, transformation, and code generation.
- [Mistral Nemo](https://mistral.ai/news/mistral-nemo/): Mistral Nemo's reasoning, world knowledge, and coding performance are state-of-the-art in its size category.  As it relies on standard architecture, Mistral Nemo is easy to use and a drop-in replacement in any system using Mistral 7B that it supersedes.
- [Codestral](https://mistral.ai/news/codestral-2501/): Codestral sets a new standard on the performance/latency space for code generation compared to previous models used for coding.
- [Codestral-Mamba](https://mistral.ai/news/codestral-mamba/): we have trained this model with advanced code and reasoning capabilities, enabling the model to have a strong performance on par with SOTA transformer-based models.
- [Mathstral](https://mistral.ai/news/mathstral/): Mathstral stands on the shoulders of Mistral 7B and specialises in STEM subjects. It achieves state-of-the-art reasoning capacities in its size category across various industry-standard benchmarks. 
- [Mixtral 8x22B](https://mistral.ai/news/mixtral-8x22b/): our most performant open model. It handles English,
  French, Italian, German, Spanish and performs strongly on code-related tasks. Natively handles function calling. 
- [Mixtral 8x7B](https://mistral.ai/news/mixtral-of-experts/): outperforms Llama 2 70B on most benchmarks with 6x faster inference and matches 
or outperforms GPT3.5 on most standard benchmarks. It handles English, French, Italian, German and Spanish, and shows strong performance in code generation.
- [Mistral 7B](https://mistral.ai/news/announcing-mistral-7b/): outperforms Llama 2 13B on all benchmarks and Llama 1 34B on many benchmarks. 

## Scale Seal Leaderboard

[Scale AI](https://scale.com/leaderboard) reports private benchmark results in coding, instruction following, math, and Spanish. Mistral Large performs exceptionally well in code and Spanish, outperforming Llama 3 405B in these areas.

## Artificial Analysis

[Artificial Analysis](https://artificialanalysis.ai/models) compares and evaluates AI models across key performance metrics, including quality, price, output speed, latency, context window, and others. Our model has several areas of outstanding performance worth highlighting.

- Artificial Analysis Quality Index: Our model ranks 3rd in this benchmark, surpassing even the 405B model. This achievement underscores our model's superior ability to analyze and generate high-quality insights.
- Coding (HumanEval): In the HumanEval benchmark, our model secures the 3rd position, again outperforming the 405B model. This highlights our model's exceptional proficiency in coding tasks.
- Quantitative Reasoning (MATH): Our model places 4th in the MATH benchmark, ahead of the 405B model. This demonstrates our model's strong quantitative reasoning capabilities.
- Scientific Reasoning & Knowledge (GPQA): In the GPQA benchmark, our model ranks 4th, showcasing its robust scientific reasoning and knowledge retention abilities.

## Qualitative feedback
We've gathered a lot of valuable insights from platforms like Reddit and Twitter. Below are some highlights and quotes from users who have shared their experiences with our models.

### Pixtral: 

> Pixtral absolutely SLAYS at OCR. 

> Very impressive at charts and diagrams and drawings and photos of screens.

> It outperforms GPT-4o-mini in many examples I’ve tested.

### Mistral Large:

> Mistral large 2 has been my go to model.

> This model is so good. In terms of local models, this is probably the first that I honestly felt was proprietary tier for coding.

### Mistral Nemo:

> I’ve been playing with Nemo for a few days now, and it blows me away at how coherent it is. It’s slightly ‘less creative and more repetitive’ than Llama 3 8B fine-tunes… But it feels ‘more coherent and has better instruction capabilities’.

> Just wanna say thank you to those genius french over at Mistral for Nemo. 12B parameters and 128k context is a very useful combination. It’s enough of a size improvement over 7B to feel a little more “solid” when talking to it, and it runs circles around Llama-2-13B, with 32x the context length. Thank you mistral!


[Model selection]
Source: https://docs.mistral.ai/docs/getting-started/models/model_selection

This guide will explore the performance and cost trade-offs, and discuss how to select the appropriate model for different use cases. We will delve into various factors to consider, offering guidance on choosing the right model for your specific needs.

Today, Mistral models are behind many LLM applications at scale. Here is a brief overview on the types of use cases we see along with their respective Mistral model:

1) Simple tasks that one can do in bulk (Classification, Customer Support, or Text Generation) can be powered by Mistral Nemo.
2) Intermediate tasks that require moderate reasoning (Data extraction, Summarizing a Document, Writing emails, Writing a Job Description, or Writing Product Descriptions) are powered by Mistral Small.
3) Complex tasks that require large reasoning capabilities or are highly specialized (Synthetic Text Generation, Code Generation, RAG, or Agents) are powered by Mistral Large.

Our Legacy models can currently be replaced by our more recent, high-quality models. If you are considering an upgrade, here are some general comments that may assist you:
- Mistral Nemo currently outperforms Mistral 7B and is more cost-effective.
- Mistral Small currently outperforms Mixtral 8x7B and is more cost-effective.
- Mistral Large currently outperforms Mixtral 8x22B while maintaining the same price ratio.

## Performance and cost trade-offs 

When selecting a model, it is essential to evaluate the performance, and cost trade-offs. Depending on what’s most important for your application, your choice may differ significantly. Note that the models will be updated over time, the information we share below only reflect the current state of the models.

Notably, Mistral Large v2 is currently outperforming all of our other models across almost all benchmarks. By considering the performance, speed, and cost details, hopefully you can find the best model that suits your application's needs.

As a general rule, if you are new to using Large Language Models, you can always start with Mistral Large first. This will allow you to evaluate its cost and performance and determine whether you need to downgrade to Mistral Small or even Mistral Nemo. If you are already using another large language model and are looking to replace a particularly powerful one, then Mistral Large may be the best choice for you. 

## Use cases 

### Mistral Nemo: Simple tasks that one can do in bulk
Mistral Nemo is the ideal choice for simpe tasks that one can do in builk - like Classification, Customer Support, or Text Generation. It offers excellent performance at an affordable price point. For instance, it can be effectively used for a classification task to classify if an email is spam or not: 

**Prompt:**
```
Classify the following email to determine if it is spam or not. Only respond with the exact words "Spam" or "Not spam".

🎉 Urgent! You've Won a $1,000,000 Cash Prize! 💰 To claim your prize, please click on the link below: https://bit.ly/claim-your-prize
```

All of our models can accurately classify this email correctly as “Spam”. Mistral Nemo is capable to provide the correct classification as the larger models. So it is the most efficient and affordable choice for this kind of tasks. 

### Mistral Small: Intermediate tasks that require language transformation
Mistral Small is the ideal for intermediate tasks that require moderate reasoning - like Data extraction, Summarizing a Document, Writing a Job Description, or Writing Product Descriptions. Mistral Small strikes a balance between performance and capability, making it suitable for a wide range of tasks that only require language transformaion. For example, Mistral Small can write an email:

**Prompt:**
```
Compose a welcome email for new customers who have just made their first purchase with your product. 
Start by expressing your gratitude for their business, and then convey your excitement for having them as a customer. 
Include relevant details about their recent order. Sign the email with "The Fun Shop Team".

Order details:
- Customer name: Anna
- Product: hat 
- Estimate date of delivery: Feb. 25, 2024
- Return policy: 30 days
```

**Output:**
```
Subject: Welcome to The Fun Shop, Anna! Your Hat is on its Way!

Dear Anna,

We hope this message finds you well. We are thrilled to welcome you to The Fun Shop family! We are incredibly grateful for your business and are excited to have you as our new customer.

We are processing your recent order for the fabulous hat you've selected. Your new accessory is set to be delivered by Feb. 25, 2024. We hope it arrives just in time to add a touch of fun and style to your outfits!

Please remember that our return policy allows you to return any item within 30 days of receipt if you are not completely satisfied. We want you to love every item you purchase from us, so if there's any issue, please don't hesitate to reach out.

Thank you once again for choosing The Fun Shop. We look forward to serving you and making your shopping experience a fun and enjoyable one!

Best Regards,
The Fun Shop Team
```

### Mistral Large: Complex tasks that require large reasoning capabilities or are highly specialized 
Mistral Large is ideal for complex tasks that require large reasoning capabilities or are highly specialized - like Synthetic Text Generation, Code Generation, RAG, or Agents.

- **Complex reasoning**

Mistral Large outperforms our other four models in commonsense and reasoning benchmarks, making it the best choice for complex reasoning tasks. 

In this example, we ask Mistral Large to calculate the difference in payment dates between the two customers whose payment amounts are closest to each other in the given dataset. Mistral Large can easily and automatically break down the problem into smaller steps: identify the two closest payment amounts, find their respective payment dates, and calculate the date difference. Mistral Large is an excellent choice for tasks that require complex reasoning and problem-solving skills.

**Prompt:**
```
Calculate the difference in payment dates between the two customers whose payment amounts are closest to each other in the given dataset: 

'{
  "transaction_id":{"0":"T1001","1":"T1002","2":"T1003","3":"T1004","4":"T1005"},
    "customer_id":{"0":"C001","1":"C002","2":"C003","3":"C002","4":"C001"},
    "payment_amount":{"0":125.5,"1":89.99,"2":120.0,"3":54.3,"4":210.2},
"payment_date":{"0":"2021-10-05","1":"2021-10-06","2":"2021-10-07","3":"2021-10-05","4":"2021-10-08"},
    "payment_status":{"0":"Paid","1":"Unpaid","2":"Paid","3":"Paid","4":"Pending"}
}'
```

**Output:**
```
To find the difference in payment dates between the two customers whose payment amounts are closest to each other, we first need to identify the two closest payment amounts and then find their respective payment dates.

The payment amounts are: 125.5, 89.99, 120.0, 54.3, 210.2

The two closest payment amounts are 125.5 and 120.0. The payment date for the payment amount 125.5 is '2021-10-05' and for the payment amount 120.0 is '2021-10-07'.

The difference in payment dates can be calculated as follows:

Date difference = |'2021-10-07' - '2021-10-05'| = 2 days

So, the difference in payment dates between the two customers whose payment amounts are closest to each other is 2 days.
```

Let’s try another prompt we found online that requires reasoning and logic understanding. Mistral Large is able to answer it correctly. 

**Prompt:**
```
There's an apple inside a blue box. There's also a red box inside the blue box. The red box has a lid on it. How can I get the apple?
```
**Output:**
```
You can get the apple by opening the blue box. The apple is not inside the red box, so you don't need to open the red box. Simply reach into the blue box and take the apple.
```

Here is another example. Mistral Large is able to answer it correctly. 

**Prompt:**
```
Which one is heavier a pound of iron or a kilogram of feather
```
**Output:**
```
A kilogram of feathers is heavier than a pound of iron.

A pound is a unit of weight that is equivalent to approximately 0.453592 kilograms. Therefore, a pound of iron weighs less than a kilogram of feathers.
```
It may seem counterintuitive because we often think of iron as being a heavy material and feathers as being light, but the weight of an object depends on its mass and the force of gravity acting upon it, not on its material or composition.

- **Coding**

Mistral Large, the top performer in coding tasks, is the ideal choice for users who priortize coding capabilities in their model selection. 

Here is an example of Mistral Large giving the correct code following the prompt. 

**Prompt:**
```
Write a function to find the maximum number of segments of lengths a, b and c that can be formed from n.
```
**Output:**
```python