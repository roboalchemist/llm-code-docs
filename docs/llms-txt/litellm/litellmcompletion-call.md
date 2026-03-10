# litellm.completion() call
response = completion(
    model="gpt-3.5-turbo",
    messages=[\
        {\
            "role": "user",\
            "content": "Hi 👋 - i'm openai"\
        }\
    ],
    stream=True
)

```

## **LiteLLM Proxy Server (LLM Gateway)** [​](https://docs.litellm.ai/\#litellm-proxy-server-llm-gateway "Direct link to litellm-proxy-server-llm-gateway")

Track spend across multiple projects/people

![ui_3](https://github.com/BerriAI/litellm/assets/29436595/47c97d5e-b9be-4839-b28c-43d7f4f10033)

The proxy provides:

1. [Hooks for auth](https://docs.litellm.ai/docs/proxy/virtual_keys#custom-auth)
2. [Hooks for logging](https://docs.litellm.ai/docs/proxy/logging#step-1---create-your-custom-litellm-callback-class)
3. [Cost tracking](https://docs.litellm.ai/docs/proxy/virtual_keys#tracking-spend)
4. [Rate Limiting](https://docs.litellm.ai/docs/proxy/users#set-rate-limits)

### 📖 Proxy Endpoints - [Swagger Docs](https://litellm-api.up.railway.app/) [​](https://docs.litellm.ai/\#-proxy-endpoints---swagger-docs "Direct link to -proxy-endpoints---swagger-docs")

Go here for a complete tutorial with keys + rate limits - [**here**](https://docs.litellm.ai/proxy/docker_quick_start.md)

### Quick Start Proxy - CLI [​](https://docs.litellm.ai/\#quick-start-proxy---cli "Direct link to Quick Start Proxy - CLI")

```codeBlockLines_e6Vv
pip install 'litellm[proxy]'

```

#### Step 1: Start litellm proxy [​](https://docs.litellm.ai/\#step-1-start-litellm-proxy "Direct link to Step 1: Start litellm proxy")

- pip package
- Docker container

```codeBlockLines_e6Vv
$ litellm --model huggingface/bigcode/starcoder

#INFO: Proxy running on http://0.0.0.0:4000

```

### Step 1. CREATE config.yaml [​](https://docs.litellm.ai/\#step-1-create-configyaml "Direct link to Step 1. CREATE config.yaml")

Example `litellm_config.yaml`

```codeBlockLines_e6Vv
model_list:
  - model_name: gpt-3.5-turbo
    litellm_params:
      model: azure/<your-azure-model-deployment>
      api_base: os.environ/AZURE_API_BASE # runs os.getenv("AZURE_API_BASE")
      api_key: os.environ/AZURE_API_KEY # runs os.getenv("AZURE_API_KEY")
      api_version: "2023-07-01-preview"

```

### Step 2. RUN Docker Image [​](https://docs.litellm.ai/\#step-2-run-docker-image "Direct link to Step 2. RUN Docker Image")

```codeBlockLines_e6Vv
docker run \
    -v $(pwd)/litellm_config.yaml:/app/config.yaml \
    -e AZURE_API_KEY=d6*********** \
    -e AZURE_API_BASE=https://openai-***********/ \
    -p 4000:4000 \
    ghcr.io/berriai/litellm:main-latest \
    --config /app/config.yaml --detailed_debug

```

#### Step 2: Make ChatCompletions Request to Proxy [​](https://docs.litellm.ai/\#step-2-make-chatcompletions-request-to-proxy "Direct link to Step 2: Make ChatCompletions Request to Proxy")

```codeBlockLines_e6Vv
import openai # openai v1.0.0+
client = openai.OpenAI(api_key="anything",base_url="http://0.0.0.0:4000") # set proxy to base_url