# set api keys
os.environ["DEEPGRAM_API_KEY"] = ""
audio_file = open("/path/to/audio.mp3", "rb")

response = transcription(model="deepgram/nova-2", file=audio_file)

print(f"response: {response}")

```

### **Fireworks AI - Vision** support for all models [​](https://docs.litellm.ai/release_notes\#fireworks-ai---vision-support-for-all-models "Direct link to fireworks-ai---vision-support-for-all-models")

LiteLLM supports document inlining for Fireworks AI models. This is useful for models that are not vision models, but still need to parse documents/images/etc.
LiteLLM will add `#transform=inline` to the url of the image\_url, if the model is not a vision model [See Code](https://github.com/BerriAI/litellm/blob/1ae9d45798bdaf8450f2dfdec703369f3d2212b7/litellm/llms/fireworks_ai/chat/transformation.py#L114)

## Proxy Admin UI [​](https://docs.litellm.ai/release_notes\#proxy-admin-ui "Direct link to Proxy Admin UI")

- `Test Key` Tab displays `model` used in response

![](https://docs.litellm.ai/assets/ideal-img/ui_model.72a8982.1920.png)

- `Test Key` Tab renders content in `.md`, `.py` (any code/markdown format)

![](https://docs.litellm.ai/assets/ideal-img/ui_format.337282b.1920.png)

## Dependency Upgrades [​](https://docs.litellm.ai/release_notes\#dependency-upgrades "Direct link to Dependency Upgrades")

- (Security fix) Upgrade to `fastapi==0.115.5` [https://github.com/BerriAI/litellm/pull/7447](https://github.com/BerriAI/litellm/pull/7447)

## Bug Fixes [​](https://docs.litellm.ai/release_notes\#bug-fixes "Direct link to Bug Fixes")

- Add health check support for realtime models [Here](https://docs.litellm.ai/docs/proxy/health#realtime-models)
- Health check error with audio\_transcription model [https://github.com/BerriAI/litellm/issues/5999](https://github.com/BerriAI/litellm/issues/5999)

`guardrails`, `logging`, `virtual key management`, `new models`

info

Get a 7 day free trial for LiteLLM Enterprise [here](https://litellm.ai/#trial).

**no call needed**

## New Features [​](https://docs.litellm.ai/release_notes\#new-features "Direct link to New Features")

### ✨ Log Guardrail Traces [​](https://docs.litellm.ai/release_notes\#-log-guardrail-traces "Direct link to ✨ Log Guardrail Traces")

Track guardrail failure rate and if a guardrail is going rogue and failing requests. [Start here](https://docs.litellm.ai/docs/proxy/guardrails/quick_start)

#### Traced Guardrail Success [​](https://docs.litellm.ai/release_notes\#traced-guardrail-success "Direct link to Traced Guardrail Success")

#### Traced Guardrail Failure [​](https://docs.litellm.ai/release_notes\#traced-guardrail-failure "Direct link to Traced Guardrail Failure")

### `/guardrails/list` [​](https://docs.litellm.ai/release_notes\#guardrailslist "Direct link to guardrailslist")

`/guardrails/list` allows clients to view available guardrails + supported guardrail params

```codeBlockLines_e6Vv
curl -X GET 'http://0.0.0.0:4000/guardrails/list'

```

Expected response

```codeBlockLines_e6Vv
{
    "guardrails": [\
        {\
        "guardrail_name": "aporia-post-guard",\
        "guardrail_info": {\
            "params": [\
            {\
                "name": "toxicity_score",\
                "type": "float",\
                "description": "Score between 0-1 indicating content toxicity level"\
            },\
            {\
                "name": "pii_detection",\
                "type": "boolean"\
            }\
            ]\
        }\
        }\
    ]
}

```

### ✨ Guardrails with Mock LLM [​](https://docs.litellm.ai/release_notes\#-guardrails-with-mock-llm "Direct link to ✨ Guardrails with Mock LLM")

Send `mock_response` to test guardrails without making an LLM call. More info on `mock_response` [here](https://docs.litellm.ai/docs/proxy/guardrails/quick_start)

```codeBlockLines_e6Vv
curl -i http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-npnwjPQciVRok5yNZgKmFQ" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [\
      {"role": "user", "content": "hi my email is ishaan@berri.ai"}\
    ],
    "mock_response": "This is a mock response",
    "guardrails": ["aporia-pre-guard", "aporia-post-guard"]
  }'

```

### Assign Keys to Users [​](https://docs.litellm.ai/release_notes\#assign-keys-to-users "Direct link to Assign Keys to Users")

You can now assign keys to users via Proxy UI

## New Models [​](https://docs.litellm.ai/release_notes\#new-models "Direct link to New Models")

- `openrouter/openai/o1`
- `vertex_ai/mistral-large@2411`

## Fixes [​](https://docs.litellm.ai/release_notes\#fixes "Direct link to Fixes")

- Fix `vertex_ai/` mistral model pricing: [https://github.com/BerriAI/litellm/pull/7345](https://github.com/BerriAI/litellm/pull/7345)
- Missing model\_group field in logs for aspeech call types [https://github.com/BerriAI/litellm/pull/7392](https://github.com/BerriAI/litellm/pull/7392)

`key management`, `budgets/rate limits`, `logging`, `guardrails`

info

Get a 7 day free trial for LiteLLM Enterprise [here](https://litellm.ai/#trial).

**no call needed**

## ✨ Budget / Rate Limit Tiers [​](https://docs.litellm.ai/release_notes\#-budget--rate-limit-tiers "Direct link to ✨ Budget / Rate Limit Tiers")

Define tiers with rate limits. Assign them to keys.

Use this to control access and budgets across a lot of keys.

**[Start here](https://docs.litellm.ai/docs/proxy/rate_limit_tiers)**

```codeBlockLines_e6Vv
curl -L -X POST 'http://0.0.0.0:4000/budget/new' \
-H 'Authorization: Bearer sk-1234' \
-H 'Content-Type: application/json' \
-d '{
    "budget_id": "high-usage-tier",
    "model_max_budget": {
        "gpt-4o": {"rpm_limit": 1000000}
    }
}'

```

## OTEL Bug Fix [​](https://docs.litellm.ai/release_notes\#otel-bug-fix "Direct link to OTEL Bug Fix")

LiteLLM was double logging litellm\_request span. This is now fixed.

[Relevant PR](https://github.com/BerriAI/litellm/pull/7435)

## Logging for Finetuning Endpoints [​](https://docs.litellm.ai/release_notes\#logging-for-finetuning-endpoints "Direct link to Logging for Finetuning Endpoints")

Logs for finetuning requests are now available on all logging providers (e.g. Datadog).

What's logged per request:

- file\_id
- finetuning\_job\_id
- any key/team metadata

**Start Here:**

- [Setup Finetuning](https://docs.litellm.ai/docs/fine_tuning)
- [Setup Logging](https://docs.litellm.ai/docs/proxy/logging#datadog)

## Dynamic Params for Guardrails [​](https://docs.litellm.ai/release_notes\#dynamic-params-for-guardrails "Direct link to Dynamic Params for Guardrails")

You can now set custom parameters (like success threshold) for your guardrails in each request.

[See guardrails spec for more details](https://docs.litellm.ai/docs/proxy/guardrails/custom_guardrail#-pass-additional-parameters-to-guardrail)

`batches`, `guardrails`, `team management`, `custom auth`

info

Get a free 7-day LiteLLM Enterprise trial here. [Start here](https://www.litellm.ai/enterprise#trial)

**No call needed**

## ✨ Cost Tracking, Logging for Batches API ( `/batches`) [​](https://docs.litellm.ai/release_notes\#-cost-tracking-logging-for-batches-api-batches "Direct link to -cost-tracking-logging-for-batches-api-batches")

Track cost, usage for Batch Creation Jobs. [Start here](https://docs.litellm.ai/docs/batches)

## ✨ `/guardrails/list` endpoint [​](https://docs.litellm.ai/release_notes\#-guardrailslist-endpoint "Direct link to -guardrailslist-endpoint")

Show available guardrails to users. [Start here](https://litellm-api.up.railway.app/#/Guardrails)

## ✨ Allow teams to add models [​](https://docs.litellm.ai/release_notes\#-allow-teams-to-add-models "Direct link to ✨ Allow teams to add models")

This enables team admins to call their own finetuned models via litellm proxy. [Start here](https://docs.litellm.ai/docs/proxy/team_model_add)

## ✨ Common checks for custom auth [​](https://docs.litellm.ai/release_notes\#-common-checks-for-custom-auth "Direct link to ✨ Common checks for custom auth")

Calling the internal common\_checks function in custom auth is now enforced as an enterprise feature. This allows admins to use litellm's default budget/auth checks within their custom auth implementation. [Start here](https://docs.litellm.ai/docs/proxy/virtual_keys#custom-auth)

## ✨ Assigning team admins [​](https://docs.litellm.ai/release_notes\#-assigning-team-admins "Direct link to ✨ Assigning team admins")

Team admins is graduating from beta and moving to our enterprise tier. This allows proxy admins to allow others to manage keys/models for their own teams (useful for projects in production). [Start here](https://docs.litellm.ai/docs/proxy/virtual_keys#restricting-key-generation)

A new LiteLLM Stable release [just went out](https://github.com/BerriAI/litellm/releases/tag/v1.55.8-stable). Here are 5 updates since v1.52.2-stable.

`langfuse`, `fallbacks`, `new models`, `azure_storage`

## Langfuse Prompt Management [​](https://docs.litellm.ai/release_notes\#langfuse-prompt-management "Direct link to Langfuse Prompt Management")

This makes it easy to run experiments or change the specific models `gpt-4o` to `gpt-4o-mini` on Langfuse, instead of making changes in your applications. [Start here](https://docs.litellm.ai/docs/proxy/prompt_management)

## Control fallback prompts client-side [​](https://docs.litellm.ai/release_notes\#control-fallback-prompts-client-side "Direct link to Control fallback prompts client-side")

> Claude prompts are different than OpenAI

Pass in prompts specific to model when doing fallbacks. [Start here](https://docs.litellm.ai/docs/proxy/reliability#control-fallback-prompts)

## New Providers / Models [​](https://docs.litellm.ai/release_notes\#new-providers--models "Direct link to New Providers / Models")

- [NVIDIA Triton](https://developer.nvidia.com/triton-inference-server) `/infer` endpoint. [Start here](https://docs.litellm.ai/docs/providers/triton-inference-server)
- [Infinity](https://github.com/michaelfeil/infinity) Rerank Models [Start here](https://docs.litellm.ai/docs/providers/infinity)

## ✨ Azure Data Lake Storage Support [​](https://docs.litellm.ai/release_notes\#-azure-data-lake-storage-support "Direct link to ✨ Azure Data Lake Storage Support")

Send LLM usage (spend, tokens) data to [Azure Data Lake](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction). This makes it easy to consume usage data on other services (eg. Databricks)
[Start here](https://docs.litellm.ai/docs/proxy/logging#azure-blob-storage)

## Docker Run LiteLLM [​](https://docs.litellm.ai/release_notes\#docker-run-litellm "Direct link to Docker Run LiteLLM")

```codeBlockLines_e6Vv
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
ghcr.io/berriai/litellm:litellm_stable_release_branch-v1.55.8-stable

```

## Get Daily Updates [​](https://docs.litellm.ai/release_notes\#get-daily-updates "Direct link to Get Daily Updates")

LiteLLM ships new releases every day. [Follow us on LinkedIn](https://www.linkedin.com/company/berri-ai/) to get daily updates.

## LiteLLM Release Notes
[Skip to main content](https://docs.litellm.ai/release_notes/archive#__docusaurus_skipToContent_fallback)

### 2024

- [December 29, 2024 \- v1.56.4](https://docs.litellm.ai/release_notes/v1.56.4)
- [December 28, 2024 \- v1.56.3](https://docs.litellm.ai/release_notes/v1.56.3)
- [December 27, 2024 \- v1.56.1](https://docs.litellm.ai/release_notes/v1.56.1)
- [December 24, 2024 \- v1.55.10](https://docs.litellm.ai/release_notes/v1.55.10)
- [December 22, 2024 \- v1.55.8-stable](https://docs.litellm.ai/release_notes/v1.55.8-stable)

### 2025

- [May 17, 2025 \- v1.70.1-stable - Gemini Realtime API Support](https://docs.litellm.ai/release_notes/v1.70.1-stable)
- [May 10, 2025 \- v1.69.0-stable - Loadbalance Batch API Models](https://docs.litellm.ai/release_notes/v1.69.0-stable)
- [May 3, 2025 \- v1.68.0-stable](https://docs.litellm.ai/release_notes/v1.68.0-stable)
- [April 26, 2025 \- v1.67.4-stable - Improved User Management](https://docs.litellm.ai/release_notes/v1.67.4-stable)
- [April 19, 2025 \- v1.67.0-stable - SCIM Integration](https://docs.litellm.ai/release_notes/v1.67.0-stable)
- [April 12, 2025 \- v1.66.0-stable - Realtime API Cost Tracking](https://docs.litellm.ai/release_notes/v1.66.0-stable)
- [April 5, 2025 \- v1.65.4-stable](https://docs.litellm.ai/release_notes/v1.65.4-stable)
- [March 30, 2025 \- v1.65.0-stable - Model Context Protocol](https://docs.litellm.ai/release_notes/v1.65.0-stable)
- [March 28, 2025 \- v1.65.0 - Team Model Add - update](https://docs.litellm.ai/release_notes/v1.65.0)
- [March 22, 2025 \- v1.63.14-stable](https://docs.litellm.ai/release_notes/v1.63.14-stable)
- [March 15, 2025 \- v1.63.11-stable](https://docs.litellm.ai/release_notes/v1.63.11-stable)
- [March 8, 2025 \- v1.63.2-stable](https://docs.litellm.ai/release_notes/v1.63.2-stable)
- [March 5, 2025 \- v1.63.0 - Anthropic 'thinking' response update](https://docs.litellm.ai/release_notes/v1.63.0)
- [March 1, 2025 \- v1.61.20-stable](https://docs.litellm.ai/release_notes/v1.61.20-stable)
- [January 31, 2025 \- v1.59.8-stable](https://docs.litellm.ai/release_notes/v1.59.8-stable)
- [January 17, 2025 \- v1.59.0](https://docs.litellm.ai/release_notes/v1.59.0)
- [January 11, 2025 \- v1.57.8-stable](https://docs.litellm.ai/release_notes/v1.57.8-stable)
- [January 10, 2025 \- v1.57.7](https://docs.litellm.ai/release_notes/v1.57.7)
- [January 8, 2025 \- v1.57.3 - New Base Docker Image](https://docs.litellm.ai/release_notes/v1.57.3)

## LiteLLM Release Tags
[Skip to main content](https://docs.litellm.ai/release_notes/tags#__docusaurus_skipToContent_fallback)