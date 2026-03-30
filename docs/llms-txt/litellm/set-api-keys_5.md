# set api keys
os.environ["DEEPGRAM_API_KEY"] = ""
audio_file = open("/path/to/audio.mp3", "rb")

response = transcription(model="deepgram/nova-2", file=audio_file)

print(f"response: {response}")

```

### **Fireworks AI - Vision** support for all models [​](https://docs.litellm.ai/release_notes/tags/fireworks-ai\#fireworks-ai---vision-support-for-all-models "Direct link to fireworks-ai---vision-support-for-all-models")

LiteLLM supports document inlining for Fireworks AI models. This is useful for models that are not vision models, but still need to parse documents/images/etc.
LiteLLM will add `#transform=inline` to the url of the image\_url, if the model is not a vision model [See Code](https://github.com/BerriAI/litellm/blob/1ae9d45798bdaf8450f2dfdec703369f3d2212b7/litellm/llms/fireworks_ai/chat/transformation.py#L114)

## Proxy Admin UI [​](https://docs.litellm.ai/release_notes/tags/fireworks-ai\#proxy-admin-ui "Direct link to Proxy Admin UI")

- `Test Key` Tab displays `model` used in response

![](https://docs.litellm.ai/assets/ideal-img/ui_model.72a8982.1920.png)

- `Test Key` Tab renders content in `.md`, `.py` (any code/markdown format)

![](https://docs.litellm.ai/assets/ideal-img/ui_format.337282b.1920.png)

## Dependency Upgrades [​](https://docs.litellm.ai/release_notes/tags/fireworks-ai\#dependency-upgrades "Direct link to Dependency Upgrades")

- (Security fix) Upgrade to `fastapi==0.115.5` [https://github.com/BerriAI/litellm/pull/7447](https://github.com/BerriAI/litellm/pull/7447)

## Bug Fixes [​](https://docs.litellm.ai/release_notes/tags/fireworks-ai\#bug-fixes "Direct link to Bug Fixes")

- Add health check support for realtime models [Here](https://docs.litellm.ai/docs/proxy/health#realtime-models)
- Health check error with audio\_transcription model [https://github.com/BerriAI/litellm/issues/5999](https://github.com/BerriAI/litellm/issues/5999)

## Guardrails and Logging Updates
[Skip to main content](https://docs.litellm.ai/release_notes/tags/guardrails#__docusaurus_skipToContent_fallback)

`guardrails`, `logging`, `virtual key management`, `new models`

info

Get a 7 day free trial for LiteLLM Enterprise [here](https://litellm.ai/#trial).

**no call needed**

## New Features [​](https://docs.litellm.ai/release_notes/tags/guardrails\#new-features "Direct link to New Features")

### ✨ Log Guardrail Traces [​](https://docs.litellm.ai/release_notes/tags/guardrails\#-log-guardrail-traces "Direct link to ✨ Log Guardrail Traces")

Track guardrail failure rate and if a guardrail is going rogue and failing requests. [Start here](https://docs.litellm.ai/docs/proxy/guardrails/quick_start)

#### Traced Guardrail Success [​](https://docs.litellm.ai/release_notes/tags/guardrails\#traced-guardrail-success "Direct link to Traced Guardrail Success")

![](https://docs.litellm.ai/assets/ideal-img/gd_success.02a2daf.1862.png)

#### Traced Guardrail Failure [​](https://docs.litellm.ai/release_notes/tags/guardrails\#traced-guardrail-failure "Direct link to Traced Guardrail Failure")

![](https://docs.litellm.ai/assets/ideal-img/gd_fail.457338e.1848.png)

### `/guardrails/list` [​](https://docs.litellm.ai/release_notes/tags/guardrails\#guardrailslist "Direct link to guardrailslist")

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

### ✨ Guardrails with Mock LLM [​](https://docs.litellm.ai/release_notes/tags/guardrails\#-guardrails-with-mock-llm "Direct link to ✨ Guardrails with Mock LLM")

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

### Assign Keys to Users [​](https://docs.litellm.ai/release_notes/tags/guardrails\#assign-keys-to-users "Direct link to Assign Keys to Users")

You can now assign keys to users via Proxy UI

![](https://docs.litellm.ai/assets/ideal-img/ui_key.9642332.1212.png)

## New Models [​](https://docs.litellm.ai/release_notes/tags/guardrails\#new-models "Direct link to New Models")

- `openrouter/openai/o1`
- `vertex_ai/mistral-large@2411`

## Fixes [​](https://docs.litellm.ai/release_notes/tags/guardrails\#fixes "Direct link to Fixes")

- Fix `vertex_ai/` mistral model pricing: [https://github.com/BerriAI/litellm/pull/7345](https://github.com/BerriAI/litellm/pull/7345)
- Missing model\_group field in logs for aspeech call types [https://github.com/BerriAI/litellm/pull/7392](https://github.com/BerriAI/litellm/pull/7392)

`key management`, `budgets/rate limits`, `logging`, `guardrails`

info

Get a 7 day free trial for LiteLLM Enterprise [here](https://litellm.ai/#trial).

**no call needed**

## ✨ Budget / Rate Limit Tiers [​](https://docs.litellm.ai/release_notes/tags/guardrails\#-budget--rate-limit-tiers "Direct link to ✨ Budget / Rate Limit Tiers")

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

## OTEL Bug Fix [​](https://docs.litellm.ai/release_notes/tags/guardrails\#otel-bug-fix "Direct link to OTEL Bug Fix")

LiteLLM was double logging litellm\_request span. This is now fixed.

[Relevant PR](https://github.com/BerriAI/litellm/pull/7435)

## Logging for Finetuning Endpoints [​](https://docs.litellm.ai/release_notes/tags/guardrails\#logging-for-finetuning-endpoints "Direct link to Logging for Finetuning Endpoints")

Logs for finetuning requests are now available on all logging providers (e.g. Datadog).

What's logged per request:

- file\_id
- finetuning\_job\_id
- any key/team metadata

**Start Here:**

- [Setup Finetuning](https://docs.litellm.ai/docs/fine_tuning)
- [Setup Logging](https://docs.litellm.ai/docs/proxy/logging#datadog)

## Dynamic Params for Guardrails [​](https://docs.litellm.ai/release_notes/tags/guardrails\#dynamic-params-for-guardrails "Direct link to Dynamic Params for Guardrails")

You can now set custom parameters (like success threshold) for your guardrails in each request.

[See guardrails spec for more details](https://docs.litellm.ai/docs/proxy/guardrails/custom_guardrail#-pass-additional-parameters-to-guardrail)

`batches`, `guardrails`, `team management`, `custom auth`

![](https://docs.litellm.ai/assets/ideal-img/batches_cost_tracking.8fc9663.1208.png)

info

Get a free 7-day LiteLLM Enterprise trial here. [Start here](https://www.litellm.ai/enterprise#trial)

**No call needed**

## ✨ Cost Tracking, Logging for Batches API ( `/batches`) [​](https://docs.litellm.ai/release_notes/tags/guardrails\#-cost-tracking-logging-for-batches-api-batches "Direct link to -cost-tracking-logging-for-batches-api-batches")

Track cost, usage for Batch Creation Jobs. [Start here](https://docs.litellm.ai/docs/batches)

## ✨ `/guardrails/list` endpoint [​](https://docs.litellm.ai/release_notes/tags/guardrails\#-guardrailslist-endpoint "Direct link to -guardrailslist-endpoint")

Show available guardrails to users. [Start here](https://litellm-api.up.railway.app/#/Guardrails)

## ✨ Allow teams to add models [​](https://docs.litellm.ai/release_notes/tags/guardrails\#-allow-teams-to-add-models "Direct link to ✨ Allow teams to add models")

This enables team admins to call their own finetuned models via litellm proxy. [Start here](https://docs.litellm.ai/docs/proxy/team_model_add)

## ✨ Common checks for custom auth [​](https://docs.litellm.ai/release_notes/tags/guardrails\#-common-checks-for-custom-auth "Direct link to ✨ Common checks for custom auth")

Calling the internal common\_checks function in custom auth is now enforced as an enterprise feature. This allows admins to use litellm's default budget/auth checks within their custom auth implementation. [Start here](https://docs.litellm.ai/docs/proxy/virtual_keys#custom-auth)

## ✨ Assigning team admins [​](https://docs.litellm.ai/release_notes/tags/guardrails\#-assigning-team-admins "Direct link to ✨ Assigning team admins")

Team admins is graduating from beta and moving to our enterprise tier. This allows proxy admins to allow others to manage keys/models for their own teams (useful for projects in production). [Start here](https://docs.litellm.ai/docs/proxy/virtual_keys#restricting-key-generation)

## LLM Features and Updates
[Skip to main content](https://docs.litellm.ai/release_notes/tags/humanloop#__docusaurus_skipToContent_fallback)

`alerting`, `prometheus`, `secret management`, `management endpoints`, `ui`, `prompt management`, `finetuning`, `batch`

## New / Updated Models [​](https://docs.litellm.ai/release_notes/tags/humanloop\#new--updated-models "Direct link to New / Updated Models")

1. Mistral large pricing - [https://github.com/BerriAI/litellm/pull/7452](https://github.com/BerriAI/litellm/pull/7452)
2. Cohere command-r7b-12-2024 pricing - [https://github.com/BerriAI/litellm/pull/7553/files](https://github.com/BerriAI/litellm/pull/7553/files)
3. Voyage - new models, prices and context window information - [https://github.com/BerriAI/litellm/pull/7472](https://github.com/BerriAI/litellm/pull/7472)
4. Anthropic - bump Bedrock claude-3-5-haiku max\_output\_tokens to 8192

## General Proxy Improvements [​](https://docs.litellm.ai/release_notes/tags/humanloop\#general-proxy-improvements "Direct link to General Proxy Improvements")

1. Health check support for realtime models
2. Support calling Azure realtime routes via virtual keys
3. Support custom tokenizer on `/utils/token_counter` \- useful when checking token count for self-hosted models
4. Request Prioritization - support on `/v1/completion` endpoint as well

## LLM Translation Improvements [​](https://docs.litellm.ai/release_notes/tags/humanloop\#llm-translation-improvements "Direct link to LLM Translation Improvements")

1. Deepgram STT support. [Start Here](https://docs.litellm.ai/docs/providers/deepgram)
2. OpenAI Moderations - `omni-moderation-latest` support. [Start Here](https://docs.litellm.ai/docs/moderation)
3. Azure O1 - fake streaming support. This ensures if a `stream=true` is passed, the response is streamed. [Start Here](https://docs.litellm.ai/docs/providers/azure)
4. Anthropic - non-whitespace char stop sequence handling - [PR](https://github.com/BerriAI/litellm/pull/7484)
5. Azure OpenAI - support Entra ID username + password based auth. [Start Here](https://docs.litellm.ai/docs/providers/azure#entra-id---use-tenant_id-client_id-client_secret)
6. LM Studio - embedding route support. [Start Here](https://docs.litellm.ai/docs/providers/lm-studio)
7. WatsonX - ZenAPIKeyAuth support. [Start Here](https://docs.litellm.ai/docs/providers/watsonx)

## Prompt Management Improvements [​](https://docs.litellm.ai/release_notes/tags/humanloop\#prompt-management-improvements "Direct link to Prompt Management Improvements")

1. Langfuse integration
2. HumanLoop integration
3. Support for using load balanced models
4. Support for loading optional params from prompt manager

[Start Here](https://docs.litellm.ai/docs/proxy/prompt_management)

## Finetuning + Batch APIs Improvements [​](https://docs.litellm.ai/release_notes/tags/humanloop\#finetuning--batch-apis-improvements "Direct link to Finetuning + Batch APIs Improvements")

1. Improved unified endpoint support for Vertex AI finetuning - [PR](https://github.com/BerriAI/litellm/pull/7487)
2. Add support for retrieving vertex api batch jobs - [PR](https://github.com/BerriAI/litellm/commit/13f364682d28a5beb1eb1b57f07d83d5ef50cbdc)

## _NEW_ Alerting Integration [​](https://docs.litellm.ai/release_notes/tags/humanloop\#new-alerting-integration "Direct link to new-alerting-integration")

PagerDuty Alerting Integration.

Handles two types of alerts:

- High LLM API Failure Rate. Configure X fails in Y seconds to trigger an alert.
- High Number of Hanging LLM Requests. Configure X hangs in Y seconds to trigger an alert.

[Start Here](https://docs.litellm.ai/docs/proxy/pagerduty)

## Prometheus Improvements [​](https://docs.litellm.ai/release_notes/tags/humanloop\#prometheus-improvements "Direct link to Prometheus Improvements")

Added support for tracking latency/spend/tokens based on custom metrics. [Start Here](https://docs.litellm.ai/docs/proxy/prometheus#beta-custom-metrics)

## _NEW_ Hashicorp Secret Manager Support [​](https://docs.litellm.ai/release_notes/tags/humanloop\#new-hashicorp-secret-manager-support "Direct link to new-hashicorp-secret-manager-support")

Support for reading credentials + writing LLM API keys. [Start Here](https://docs.litellm.ai/docs/secret#hashicorp-vault)

## Management Endpoints / UI Improvements [​](https://docs.litellm.ai/release_notes/tags/humanloop\#management-endpoints--ui-improvements "Direct link to Management Endpoints / UI Improvements")

1. Create and view organizations + assign org admins on the Proxy UI
2. Support deleting keys by key\_alias
3. Allow assigning teams to org on UI
4. Disable using ui session token for 'test key' pane
5. Show model used in 'test key' pane
6. Support markdown output in 'test key' pane

## Helm Improvements [​](https://docs.litellm.ai/release_notes/tags/humanloop\#helm-improvements "Direct link to Helm Improvements")

1. Prevent istio injection for db migrations cron job
2. allow using migrationJob.enabled variable within job

## Logging Improvements [​](https://docs.litellm.ai/release_notes/tags/humanloop\#logging-improvements "Direct link to Logging Improvements")

1. braintrust logging: respect project\_id, add more metrics - [https://github.com/BerriAI/litellm/pull/7613](https://github.com/BerriAI/litellm/pull/7613)
2. Athina - support base url - `ATHINA_BASE_URL`
3. Lunary - Allow passing custom parent run id to LLM Calls

## Git Diff [​](https://docs.litellm.ai/release_notes/tags/humanloop\#git-diff "Direct link to Git Diff")

This is the diff between v1.56.3-stable and v1.57.8-stable.

Use this to see the changes in the codebase.

[Git Diff](https://github.com/BerriAI/litellm/compare/v1.56.3-stable...189b67760011ea313ca58b1f8bd43aa74fbd7f55)

## Key Management Overview
[Skip to main content](https://docs.litellm.ai/release_notes/tags/key-management#__docusaurus_skipToContent_fallback)

`key management`, `budgets/rate limits`, `logging`, `guardrails`

info

Get a 7 day free trial for LiteLLM Enterprise [here](https://litellm.ai/#trial).

**no call needed**

## ✨ Budget / Rate Limit Tiers [​](https://docs.litellm.ai/release_notes/tags/key-management\#-budget--rate-limit-tiers "Direct link to ✨ Budget / Rate Limit Tiers")

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

## OTEL Bug Fix [​](https://docs.litellm.ai/release_notes/tags/key-management\#otel-bug-fix "Direct link to OTEL Bug Fix")

LiteLLM was double logging litellm\_request span. This is now fixed.

[Relevant PR](https://github.com/BerriAI/litellm/pull/7435)

## Logging for Finetuning Endpoints [​](https://docs.litellm.ai/release_notes/tags/key-management\#logging-for-finetuning-endpoints "Direct link to Logging for Finetuning Endpoints")

Logs for finetuning requests are now available on all logging providers (e.g. Datadog).

What's logged per request:

- file\_id
- finetuning\_job\_id
- any key/team metadata

**Start Here:**

- [Setup Finetuning](https://docs.litellm.ai/docs/fine_tuning)
- [Setup Logging](https://docs.litellm.ai/docs/proxy/logging#datadog)

## Dynamic Params for Guardrails [​](https://docs.litellm.ai/release_notes/tags/key-management\#dynamic-params-for-guardrails "Direct link to Dynamic Params for Guardrails")

You can now set custom parameters (like success threshold) for your guardrails in each request.

[See guardrails spec for more details](https://docs.litellm.ai/docs/proxy/guardrails/custom_guardrail#-pass-additional-parameters-to-guardrail)

## LiteLLM Release Notes
[Skip to main content](https://docs.litellm.ai/release_notes/tags/langfuse#__docusaurus_skipToContent_fallback)

`alerting`, `prometheus`, `secret management`, `management endpoints`, `ui`, `prompt management`, `finetuning`, `batch`

## New / Updated Models [​](https://docs.litellm.ai/release_notes/tags/langfuse\#new--updated-models "Direct link to New / Updated Models")

1. Mistral large pricing - [https://github.com/BerriAI/litellm/pull/7452](https://github.com/BerriAI/litellm/pull/7452)
2. Cohere command-r7b-12-2024 pricing - [https://github.com/BerriAI/litellm/pull/7553/files](https://github.com/BerriAI/litellm/pull/7553/files)
3. Voyage - new models, prices and context window information - [https://github.com/BerriAI/litellm/pull/7472](https://github.com/BerriAI/litellm/pull/7472)
4. Anthropic - bump Bedrock claude-3-5-haiku max\_output\_tokens to 8192

## General Proxy Improvements [​](https://docs.litellm.ai/release_notes/tags/langfuse\#general-proxy-improvements "Direct link to General Proxy Improvements")

1. Health check support for realtime models
2. Support calling Azure realtime routes via virtual keys
3. Support custom tokenizer on `/utils/token_counter` \- useful when checking token count for self-hosted models
4. Request Prioritization - support on `/v1/completion` endpoint as well

## LLM Translation Improvements [​](https://docs.litellm.ai/release_notes/tags/langfuse\#llm-translation-improvements "Direct link to LLM Translation Improvements")

1. Deepgram STT support. [Start Here](https://docs.litellm.ai/docs/providers/deepgram)
2. OpenAI Moderations - `omni-moderation-latest` support. [Start Here](https://docs.litellm.ai/docs/moderation)
3. Azure O1 - fake streaming support. This ensures if a `stream=true` is passed, the response is streamed. [Start Here](https://docs.litellm.ai/docs/providers/azure)
4. Anthropic - non-whitespace char stop sequence handling - [PR](https://github.com/BerriAI/litellm/pull/7484)
5. Azure OpenAI - support Entra ID username + password based auth. [Start Here](https://docs.litellm.ai/docs/providers/azure#entra-id---use-tenant_id-client_id-client_secret)
6. LM Studio - embedding route support. [Start Here](https://docs.litellm.ai/docs/providers/lm-studio)
7. WatsonX - ZenAPIKeyAuth support. [Start Here](https://docs.litellm.ai/docs/providers/watsonx)

## Prompt Management Improvements [​](https://docs.litellm.ai/release_notes/tags/langfuse\#prompt-management-improvements "Direct link to Prompt Management Improvements")

1. Langfuse integration
2. HumanLoop integration
3. Support for using load balanced models
4. Support for loading optional params from prompt manager

[Start Here](https://docs.litellm.ai/docs/proxy/prompt_management)

## Finetuning + Batch APIs Improvements [​](https://docs.litellm.ai/release_notes/tags/langfuse\#finetuning--batch-apis-improvements "Direct link to Finetuning + Batch APIs Improvements")

1. Improved unified endpoint support for Vertex AI finetuning - [PR](https://github.com/BerriAI/litellm/pull/7487)
2. Add support for retrieving vertex api batch jobs - [PR](https://github.com/BerriAI/litellm/commit/13f364682d28a5beb1eb1b57f07d83d5ef50cbdc)

## _NEW_ Alerting Integration [​](https://docs.litellm.ai/release_notes/tags/langfuse\#new-alerting-integration "Direct link to new-alerting-integration")

PagerDuty Alerting Integration.

Handles two types of alerts:

- High LLM API Failure Rate. Configure X fails in Y seconds to trigger an alert.
- High Number of Hanging LLM Requests. Configure X hangs in Y seconds to trigger an alert.

[Start Here](https://docs.litellm.ai/docs/proxy/pagerduty)

## Prometheus Improvements [​](https://docs.litellm.ai/release_notes/tags/langfuse\#prometheus-improvements "Direct link to Prometheus Improvements")

Added support for tracking latency/spend/tokens based on custom metrics. [Start Here](https://docs.litellm.ai/docs/proxy/prometheus#beta-custom-metrics)

## _NEW_ Hashicorp Secret Manager Support [​](https://docs.litellm.ai/release_notes/tags/langfuse\#new-hashicorp-secret-manager-support "Direct link to new-hashicorp-secret-manager-support")

Support for reading credentials + writing LLM API keys. [Start Here](https://docs.litellm.ai/docs/secret#hashicorp-vault)

## Management Endpoints / UI Improvements [​](https://docs.litellm.ai/release_notes/tags/langfuse\#management-endpoints--ui-improvements "Direct link to Management Endpoints / UI Improvements")

1. Create and view organizations + assign org admins on the Proxy UI
2. Support deleting keys by key\_alias
3. Allow assigning teams to org on UI
4. Disable using ui session token for 'test key' pane
5. Show model used in 'test key' pane
6. Support markdown output in 'test key' pane

## Helm Improvements [​](https://docs.litellm.ai/release_notes/tags/langfuse\#helm-improvements "Direct link to Helm Improvements")

1. Prevent istio injection for db migrations cron job
2. allow using migrationJob.enabled variable within job

## Logging Improvements [​](https://docs.litellm.ai/release_notes/tags/langfuse\#logging-improvements "Direct link to Logging Improvements")

1. braintrust logging: respect project\_id, add more metrics - [https://github.com/BerriAI/litellm/pull/7613](https://github.com/BerriAI/litellm/pull/7613)
2. Athina - support base url - `ATHINA_BASE_URL`
3. Lunary - Allow passing custom parent run id to LLM Calls

## Git Diff [​](https://docs.litellm.ai/release_notes/tags/langfuse\#git-diff "Direct link to Git Diff")

This is the diff between v1.56.3-stable and v1.57.8-stable.

Use this to see the changes in the codebase.

[Git Diff](https://github.com/BerriAI/litellm/compare/v1.56.3-stable...189b67760011ea313ca58b1f8bd43aa74fbd7f55)

`langfuse`, `management endpoints`, `ui`, `prometheus`, `secret management`

## Langfuse Prompt Management [​](https://docs.litellm.ai/release_notes/tags/langfuse\#langfuse-prompt-management "Direct link to Langfuse Prompt Management")

Langfuse Prompt Management is being labelled as BETA. This allows us to iterate quickly on the feedback we're receiving, and making the status clearer to users. We expect to make this feature to be stable by next month (February 2025).

Changes:

- Include the client message in the LLM API Request. (Previously only the prompt template was sent, and the client message was ignored).
- Log the prompt template in the logged request (e.g. to s3/langfuse).
- Log the 'prompt\_id' and 'prompt\_variables' in the logged request (e.g. to s3/langfuse).

[Start Here](https://docs.litellm.ai/docs/proxy/prompt_management)

## Team/Organization Management + UI Improvements [​](https://docs.litellm.ai/release_notes/tags/langfuse\#teamorganization-management--ui-improvements "Direct link to Team/Organization Management + UI Improvements")

Managing teams and organizations on the UI is now easier.

Changes:

- Support for editing user role within team on UI.
- Support updating team member role to admin via api - `/team/member_update`
- Show team admins all keys for their team.
- Add organizations with budgets
- Assign teams to orgs on the UI
- Auto-assign SSO users to teams

[Start Here](https://docs.litellm.ai/docs/proxy/self_serve)

## Hashicorp Vault Support [​](https://docs.litellm.ai/release_notes/tags/langfuse\#hashicorp-vault-support "Direct link to Hashicorp Vault Support")

We now support writing LiteLLM Virtual API keys to Hashicorp Vault.

[Start Here](https://docs.litellm.ai/docs/proxy/vault)

## Custom Prometheus Metrics [​](https://docs.litellm.ai/release_notes/tags/langfuse\#custom-prometheus-metrics "Direct link to Custom Prometheus Metrics")

Define custom prometheus metrics, and track usage/latency/no. of requests against them

This allows for more fine-grained tracking - e.g. on prompt template passed in request metadata

[Start Here](https://docs.litellm.ai/docs/proxy/prometheus#beta-custom-metrics)

A new LiteLLM Stable release [just went out](https://github.com/BerriAI/litellm/releases/tag/v1.55.8-stable). Here are 5 updates since v1.52.2-stable.

`langfuse`, `fallbacks`, `new models`, `azure_storage`

![](https://docs.litellm.ai/assets/ideal-img/langfuse_prmpt_mgmt.19b8982.1920.png)

## Langfuse Prompt Management [​](https://docs.litellm.ai/release_notes/tags/langfuse\#langfuse-prompt-management "Direct link to Langfuse Prompt Management")

This makes it easy to run experiments or change the specific models `gpt-4o` to `gpt-4o-mini` on Langfuse, instead of making changes in your applications. [Start here](https://docs.litellm.ai/docs/proxy/prompt_management)

## Control fallback prompts client-side [​](https://docs.litellm.ai/release_notes/tags/langfuse\#control-fallback-prompts-client-side "Direct link to Control fallback prompts client-side")

> Claude prompts are different than OpenAI

Pass in prompts specific to model when doing fallbacks. [Start here](https://docs.litellm.ai/docs/proxy/reliability#control-fallback-prompts)

## New Providers / Models [​](https://docs.litellm.ai/release_notes/tags/langfuse\#new-providers--models "Direct link to New Providers / Models")

- [NVIDIA Triton](https://developer.nvidia.com/triton-inference-server) `/infer` endpoint. [Start here](https://docs.litellm.ai/docs/providers/triton-inference-server)
- [Infinity](https://github.com/michaelfeil/infinity) Rerank Models [Start here](https://docs.litellm.ai/docs/providers/infinity)

## ✨ Azure Data Lake Storage Support [​](https://docs.litellm.ai/release_notes/tags/langfuse\#-azure-data-lake-storage-support "Direct link to ✨ Azure Data Lake Storage Support")

Send LLM usage (spend, tokens) data to [Azure Data Lake](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction). This makes it easy to consume usage data on other services (eg. Databricks)
[Start here](https://docs.litellm.ai/docs/proxy/logging#azure-blob-storage)

## Docker Run LiteLLM [​](https://docs.litellm.ai/release_notes/tags/langfuse\#docker-run-litellm "Direct link to Docker Run LiteLLM")

```codeBlockLines_e6Vv
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
ghcr.io/berriai/litellm:litellm_stable_release_branch-v1.55.8-stable

```

## Get Daily Updates [​](https://docs.litellm.ai/release_notes/tags/langfuse\#get-daily-updates "Direct link to Get Daily Updates")

LiteLLM ships new releases every day. [Follow us on LinkedIn](https://www.linkedin.com/company/berri-ai/) to get daily updates.

## LLM Translation Updates
[Skip to main content](https://docs.litellm.ai/release_notes/tags/llm-translation#__docusaurus_skipToContent_fallback)

These are the changes since `v1.61.20-stable`.

This release is primarily focused on:

- LLM Translation improvements (more `thinking` content improvements)
- UI improvements (Error logs now shown on UI)

info

This release will be live on 03/09/2025

![](https://docs.litellm.ai/assets/ideal-img/v1632_release.7b42da1.1920.jpg)

## Demo Instance [​](https://docs.litellm.ai/release_notes/tags/llm-translation\#demo-instance "Direct link to Demo Instance")

Here's a Demo Instance to test changes:

- Instance: [https://demo.litellm.ai/](https://demo.litellm.ai/)
- Login Credentials:
  - Username: admin
  - Password: sk-1234

## New Models / Updated Models [​](https://docs.litellm.ai/release_notes/tags/llm-translation\#new-models--updated-models "Direct link to New Models / Updated Models")

1. Add `supports_pdf_input` for specific Bedrock Claude models [PR](https://github.com/BerriAI/litellm/commit/f63cf0030679fe1a43d03fb196e815a0f28dae92)
2. Add pricing for amazon `eu` models [PR](https://github.com/BerriAI/litellm/commits/main/model_prices_and_context_window.json)
3. Fix Azure O1 mini pricing [PR](https://github.com/BerriAI/litellm/commit/52de1949ef2f76b8572df751f9c868a016d4832c)

## LLM Translation [​](https://docs.litellm.ai/release_notes/tags/llm-translation\#llm-translation "Direct link to LLM Translation")

![](https://docs.litellm.ai/assets/ideal-img/anthropic_thinking.3bef9d6.1920.jpg)

01. Support `/openai/` passthrough for Assistant endpoints. [Get Started](https://docs.litellm.ai/docs/pass_through/openai_passthrough)
02. Bedrock Claude - fix tool calling transformation on invoke route. [Get Started](https://docs.litellm.ai/docs/providers/bedrock#usage---function-calling--tool-calling)
03. Bedrock Claude - response\_format support for claude on invoke route. [Get Started](https://docs.litellm.ai/docs/providers/bedrock#usage---structured-output--json-mode)
04. Bedrock - pass `description` if set in response\_format. [Get Started](https://docs.litellm.ai/docs/providers/bedrock#usage---structured-output--json-mode)
05. Bedrock - Fix passing response\_format: {"type": "text"}. [PR](https://github.com/BerriAI/litellm/commit/c84b489d5897755139aa7d4e9e54727ebe0fa540)
06. OpenAI - Handle sending image\_url as str to openai. [Get Started](https://docs.litellm.ai/docs/completion/vision)
07. Deepseek - return 'reasoning\_content' missing on streaming. [Get Started](https://docs.litellm.ai/docs/reasoning_content)
08. Caching - Support caching on reasoning content. [Get Started](https://docs.litellm.ai/docs/proxy/caching)
09. Bedrock - handle thinking blocks in assistant message. [Get Started](https://docs.litellm.ai/docs/providers/bedrock#usage---thinking--reasoning-content)
10. Anthropic - Return `signature` on streaming. [Get Started](https://docs.litellm.ai/docs/providers/bedrock#usage---thinking--reasoning-content)

- Note: We've also migrated from `signature_delta` to `signature`. [Read more](https://docs.litellm.ai/release_notes/v1.63.0)

11. Support format param for specifying image type. [Get Started](https://docs.litellm.ai/docs/completion/vision.md#explicitly-specify-image-type)
12. Anthropic - `/v1/messages` endpoint - `thinking` param support. [Get Started](https://docs.litellm.ai/docs/anthropic_unified.md)

- Note: this refactors the \[BETA\] unified `/v1/messages` endpoint, to just work for the Anthropic API.

13. Vertex AI - handle $id in response schema when calling vertex ai. [Get Started](https://docs.litellm.ai/docs/providers/vertex#json-schema)

## Spend Tracking Improvements [​](https://docs.litellm.ai/release_notes/tags/llm-translation\#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

1. Batches API - Fix cost calculation to run on retrieve\_batch. [Get Started](https://docs.litellm.ai/docs/batches)
2. Batches API - Log batch models in spend logs / standard logging payload. [Get Started](https://docs.litellm.ai/docs/proxy/logging_spec.md#standardlogginghiddenparams)

## Management Endpoints / UI [​](https://docs.litellm.ai/release_notes/tags/llm-translation\#management-endpoints--ui "Direct link to Management Endpoints / UI")

![](https://docs.litellm.ai/assets/ideal-img/error_logs.63c5dc9.1920.jpg)

1. Virtual Keys Page
   - Allow team/org filters to be searchable on the Create Key Page
   - Add created\_by and updated\_by fields to Keys table
   - Show 'user\_email' on key table
   - Show 100 Keys Per Page, Use full height, increase width of key alias
2. Logs Page
   - Show Error Logs on LiteLLM UI
   - Allow Internal Users to View their own logs
3. Internal Users Page
   - Allow admin to control default model access for internal users
4. Fix session handling with cookies

## Logging / Guardrail Integrations [​](https://docs.litellm.ai/release_notes/tags/llm-translation\#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

1. Fix prometheus metrics w/ custom metrics, when keys containing team\_id make requests. [PR](https://github.com/BerriAI/litellm/pull/8935)

## Performance / Loadbalancing / Reliability improvements [​](https://docs.litellm.ai/release_notes/tags/llm-translation\#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

1. Cooldowns - Support cooldowns on models called with client side credentials. [Get Started](https://docs.litellm.ai/docs/proxy/clientside_auth#pass-user-llm-api-keys--api-base)
2. Tag-based Routing - ensures tag-based routing across all endpoints ( `/embeddings`, `/image_generation`, etc.). [Get Started](https://docs.litellm.ai/docs/proxy/tag_routing)

## General Proxy Improvements [​](https://docs.litellm.ai/release_notes/tags/llm-translation\#general-proxy-improvements "Direct link to General Proxy Improvements")

1. Raise BadRequestError when unknown model passed in request
2. Enforce model access restrictions on Azure OpenAI proxy route
3. Reliability fix - Handle emoji’s in text - fix orjson error
4. Model Access Patch - don't overwrite litellm.anthropic\_models when running auth checks
5. Enable setting timezone information in docker image

## Complete Git Diff [​](https://docs.litellm.ai/release_notes/tags/llm-translation\#complete-git-diff "Direct link to Complete Git Diff")

[Here's the complete git diff](https://github.com/BerriAI/litellm/compare/v1.61.20-stable...v1.63.2-stable)

v1.63.0 fixes Anthropic 'thinking' response on streaming to return the `signature` block. [Github Issue](https://github.com/BerriAI/litellm/issues/8964)

It also moves the response structure from `signature_delta` to `signature` to be the same as Anthropic. [Anthropic Docs](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#implementing-extended-thinking)

## Diff [​](https://docs.litellm.ai/release_notes/tags/llm-translation\#diff "Direct link to Diff")

```codeBlockLines_e6Vv
"message": {
    ...
    "reasoning_content": "The capital of France is Paris.",
    "thinking_blocks": [\
        {\
            "type": "thinking",\
            "thinking": "The capital of France is Paris.",\
-            "signature_delta": "EqoBCkgIARABGAIiQL2UoU0b1OHYi+..." # 👈 OLD FORMAT\
+            "signature": "EqoBCkgIARABGAIiQL2UoU0b1OHYi+..." # 👈 KEY CHANGE\
        }\
    ]
}

```

These are the changes since `v1.61.13-stable`.

This release is primarily focused on:

- LLM Translation improvements (claude-3-7-sonnet + 'thinking'/'reasoning\_content' support)
- UI improvements (add model flow, user management, etc)

## Demo Instance [​](https://docs.litellm.ai/release_notes/tags/llm-translation\#demo-instance "Direct link to Demo Instance")

Here's a Demo Instance to test changes:

- Instance: [https://demo.litellm.ai/](https://demo.litellm.ai/)
- Login Credentials:
  - Username: admin
  - Password: sk-1234

## New Models / Updated Models [​](https://docs.litellm.ai/release_notes/tags/llm-translation\#new-models--updated-models "Direct link to New Models / Updated Models")

1. Anthropic 3-7 sonnet support + cost tracking (Anthropic API + Bedrock + Vertex AI + OpenRouter)
1. Anthropic API [Start here](https://docs.litellm.ai/docs/providers/anthropic#usage---thinking--reasoning_content)
2. Bedrock API [Start here](https://docs.litellm.ai/docs/providers/bedrock#usage---thinking--reasoning-content)
3. Vertex AI API [See here](https://docs.litellm.ai/docs/providers/vertex#usage---thinking--reasoning_content)
4. OpenRouter [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L5626)
2. Gpt-4.5-preview support + cost tracking [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L79)
3. Azure AI - Phi-4 cost tracking [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L1773)
4. Claude-3.5-sonnet - vision support updated on Anthropic API [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L2888)
5. Bedrock llama vision support [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L7714)
6. Cerebras llama3.3-70b pricing [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L2697)

## LLM Translation [​](https://docs.litellm.ai/release_notes/tags/llm-translation\#llm-translation "Direct link to LLM Translation")

1. Infinity Rerank - support returning documents when return\_documents=True [Start here](https://docs.litellm.ai/docs/providers/infinity#usage---returning-documents)
2. Amazon Deepseek - `<think>` param extraction into ‘reasoning\_content’ [Start here](https://docs.litellm.ai/docs/providers/bedrock#bedrock-imported-models-deepseek-deepseek-r1)
3. Amazon Titan Embeddings - filter out ‘aws\_’ params from request body [Start here](https://docs.litellm.ai/docs/providers/bedrock#bedrock-embedding)
4. Anthropic ‘thinking’ + ‘reasoning\_content’ translation support (Anthropic API, Bedrock, Vertex AI) [Start here](https://docs.litellm.ai/docs/reasoning_content)
5. VLLM - support ‘video\_url’ [Start here](https://docs.litellm.ai/docs/providers/vllm#send-video-url-to-vllm)
6. Call proxy via litellm SDK: Support `litellm_proxy/` for embedding, image\_generation, transcription, speech, rerank [Start here](https://docs.litellm.ai/docs/providers/litellm_proxy)
7. OpenAI Pass-through - allow using Assistants GET, DELETE on /openai pass through routes [Start here](https://docs.litellm.ai/docs/pass_through/openai_passthrough)
8. Message Translation - fix openai message for assistant msg if role is missing - openai allows this
9. O1/O3 - support ‘drop\_params’ for o3-mini and o1 parallel\_tool\_calls param (not supported currently) [See here](https://docs.litellm.ai/docs/completion/drop_params)

## Spend Tracking Improvements [​](https://docs.litellm.ai/release_notes/tags/llm-translation\#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

1. Cost tracking for rerank via Bedrock [See PR](https://github.com/BerriAI/litellm/commit/b682dc4ec8fd07acf2f4c981d2721e36ae2a49c5)
2. Anthropic pass-through - fix race condition causing cost to not be tracked [See PR](https://github.com/BerriAI/litellm/pull/8874)
3. Anthropic pass-through: Ensure accurate token counting [See PR](https://github.com/BerriAI/litellm/pull/8880)

## Management Endpoints / UI [​](https://docs.litellm.ai/release_notes/tags/llm-translation\#management-endpoints--ui "Direct link to Management Endpoints / UI")

01. Models Page - Allow sorting models by ‘created at’
02. Models Page - Edit Model Flow Improvements
03. Models Page - Fix Adding Azure, Azure AI Studio models on UI
04. Internal Users Page - Allow Bulk Adding Internal Users on UI
05. Internal Users Page - Allow sorting users by ‘created at’
06. Virtual Keys Page - Allow searching for UserIDs on the dropdown when assigning a user to a team [See PR](https://github.com/BerriAI/litellm/pull/8844)
07. Virtual Keys Page - allow creating a user when assigning keys to users [See PR](https://github.com/BerriAI/litellm/pull/8844)
08. Model Hub Page - fix text overflow issue [See PR](https://github.com/BerriAI/litellm/pull/8749)
09. Admin Settings Page - Allow adding MSFT SSO on UI
10. Backend - don't allow creating duplicate internal users in DB

## Helm [​](https://docs.litellm.ai/release_notes/tags/llm-translation\#helm "Direct link to Helm")

1. support ttlSecondsAfterFinished on the migration job - [See PR](https://github.com/BerriAI/litellm/pull/8593)
2. enhance migrations job with additional configurable properties - [See PR](https://github.com/BerriAI/litellm/pull/8636)

## Logging / Guardrail Integrations [​](https://docs.litellm.ai/release_notes/tags/llm-translation\#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

1. Arize Phoenix support
2. ‘No-log’ - fix ‘no-log’ param support on embedding calls

## Performance / Loadbalancing / Reliability improvements [​](https://docs.litellm.ai/release_notes/tags/llm-translation\#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

1. Single Deployment Cooldown logic - Use allowed\_fails or allowed\_fail\_policy if set [Start here](https://docs.litellm.ai/docs/routing#advanced-custom-retries-cooldowns-based-on-error-type)

## General Proxy Improvements [​](https://docs.litellm.ai/release_notes/tags/llm-translation\#general-proxy-improvements "Direct link to General Proxy Improvements")

1. Hypercorn - fix reading / parsing request body
2. Windows - fix running proxy in windows
3. DD-Trace - fix dd-trace enablement on proxy

## Complete Git Diff [​](https://docs.litellm.ai/release_notes/tags/llm-translation\#complete-git-diff "Direct link to Complete Git Diff")

View the complete git diff [here](https://github.com/BerriAI/litellm/compare/v1.61.13-stable...v1.61.20-stable).

## LiteLLM Logging Updates
[Skip to main content](https://docs.litellm.ai/release_notes/tags/logging#__docusaurus_skipToContent_fallback)

info

Get a 7 day free trial for LiteLLM Enterprise [here](https://litellm.ai/#trial).

**no call needed**

## New Models / Updated Models [​](https://docs.litellm.ai/release_notes/tags/logging\#new-models--updated-models "Direct link to New Models / Updated Models")

1. New OpenAI `/image/variations` endpoint BETA support [Docs](https://docs.litellm.ai/docs/image_variations)
2. Topaz API support on OpenAI `/image/variations` BETA endpoint [Docs](https://docs.litellm.ai/docs/providers/topaz)
3. Deepseek - r1 support w/ reasoning\_content ( [Deepseek API](https://docs.litellm.ai/docs/providers/deepseek#reasoning-models), [Vertex AI](https://docs.litellm.ai/docs/providers/vertex#model-garden), [Bedrock](https://docs.litellm.ai/docs/providers/bedrock#deepseek))
4. Azure - Add azure o1 pricing [See Here](https://github.com/BerriAI/litellm/blob/b8b927f23bc336862dacb89f59c784a8d62aaa15/model_prices_and_context_window.json#L952)
5. Anthropic - handle `-latest` tag in model for cost calculation
6. Gemini-2.0-flash-thinking - add model pricing (it’s 0.0) [See Here](https://github.com/BerriAI/litellm/blob/b8b927f23bc336862dacb89f59c784a8d62aaa15/model_prices_and_context_window.json#L3393)
7. Bedrock - add stability sd3 model pricing [See Here](https://github.com/BerriAI/litellm/blob/b8b927f23bc336862dacb89f59c784a8d62aaa15/model_prices_and_context_window.json#L6814) (s/o [Marty Sullivan](https://github.com/marty-sullivan))
8. Bedrock - add us.amazon.nova-lite-v1:0 to model cost map [See Here](https://github.com/BerriAI/litellm/blob/b8b927f23bc336862dacb89f59c784a8d62aaa15/model_prices_and_context_window.json#L5619)
9. TogetherAI - add new together\_ai llama3.3 models [See Here](https://github.com/BerriAI/litellm/blob/b8b927f23bc336862dacb89f59c784a8d62aaa15/model_prices_and_context_window.json#L6985)

## LLM Translation [​](https://docs.litellm.ai/release_notes/tags/logging\#llm-translation "Direct link to LLM Translation")

01. LM Studio -> fix async embedding call
02. Gpt 4o models - fix response\_format translation
03. Bedrock nova - expand supported document types to include .md, .csv, etc. [Start Here](https://docs.litellm.ai/docs/providers/bedrock#usage---pdf--document-understanding)
04. Bedrock - docs on IAM role based access for bedrock - [Start Here](https://docs.litellm.ai/docs/providers/bedrock#sts-role-based-auth)
05. Bedrock - cache IAM role credentials when used
06. Google AI Studio ( `gemini/`) \- support gemini 'frequency\_penalty' and 'presence\_penalty'
07. Azure O1 - fix model name check
08. WatsonX - ZenAPIKey support for WatsonX [Docs](https://docs.litellm.ai/docs/providers/watsonx)
09. Ollama Chat - support json schema response format [Start Here](https://docs.litellm.ai/docs/providers/ollama#json-schema-support)
10. Bedrock - return correct bedrock status code and error message if error during streaming
11. Anthropic - Supported nested json schema on anthropic calls
12. OpenAI - `metadata` param preview support
    1. SDK - enable via `litellm.enable_preview_features = True`
    2. PROXY - enable via `litellm_settings::enable_preview_features: true`
13. Replicate - retry completion response on status=processing

## Spend Tracking Improvements [​](https://docs.litellm.ai/release_notes/tags/logging\#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

1. Bedrock - QA asserts all bedrock regional models have same `supported_` as base model
2. Bedrock - fix bedrock converse cost tracking w/ region name specified
3. Spend Logs reliability fix - when `user` passed in request body is int instead of string
4. Ensure ‘base\_model’ cost tracking works across all endpoints
5. Fixes for Image generation cost tracking
6. Anthropic - fix anthropic end user cost tracking
7. JWT / OIDC Auth - add end user id tracking from jwt auth

## Management Endpoints / UI [​](https://docs.litellm.ai/release_notes/tags/logging\#management-endpoints--ui "Direct link to Management Endpoints / UI")

01. allows team member to become admin post-add (ui + endpoints)
02. New edit/delete button for updating team membership on UI
03. If team admin - show all team keys
04. Model Hub - clarify cost of models is per 1m tokens
05. Invitation Links - fix invalid url generated
06. New - SpendLogs Table Viewer - allows proxy admin to view spend logs on UI
    1. New spend logs - allow proxy admin to ‘opt in’ to logging request/response in spend logs table - enables easier abuse detection
    2. Show country of origin in spend logs
    3. Add pagination + filtering by key name/team name
07. `/key/delete` \- allow team admin to delete team keys
08. Internal User ‘view’ - fix spend calculation when team selected
09. Model Analytics is now on Free
10. Usage page - shows days when spend = 0, and round spend on charts to 2 sig figs
11. Public Teams - allow admins to expose teams for new users to ‘join’ on UI - [Start Here](https://docs.litellm.ai/docs/proxy/public_teams)
12. Guardrails
    1. set/edit guardrails on a virtual key
    2. Allow setting guardrails on a team
    3. Set guardrails on team create + edit page
13. Support temporary budget increases on `/key/update` \- new `temp_budget_increase` and `temp_budget_expiry` fields - [Start Here](https://docs.litellm.ai/docs/proxy/virtual_keys#temporary-budget-increase)
14. Support writing new key alias to AWS Secret Manager - on key rotation [Start Here](https://docs.litellm.ai/docs/secret#aws-secret-manager)

## Helm [​](https://docs.litellm.ai/release_notes/tags/logging\#helm "Direct link to Helm")

1. add securityContext and pull policy values to migration job (s/o [https://github.com/Hexoplon](https://github.com/Hexoplon))
2. allow specifying envVars on values.yaml
3. new helm lint test

## Logging / Guardrail Integrations [​](https://docs.litellm.ai/release_notes/tags/logging\#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

1. Log the used prompt when prompt management used. [Start Here](https://docs.litellm.ai/docs/proxy/prompt_management)
2. Support s3 logging with team alias prefixes - [Start Here](https://docs.litellm.ai/docs/proxy/logging#team-alias-prefix-in-object-key)
3. Prometheus [Start Here](https://docs.litellm.ai/docs/proxy/prometheus)
1. fix litellm\_llm\_api\_time\_to\_first\_token\_metric not populating for bedrock models
2. emit remaining team budget metric on regular basis (even when call isn’t made) - allows for more stable metrics on Grafana/etc.
3. add key and team level budget metrics
4. emit `litellm_overhead_latency_metric`
5. Emit `litellm_team_budget_reset_at_metric` and `litellm_api_key_budget_remaining_hours_metric`
4. Datadog - support logging spend tags to Datadog. [Start Here](https://docs.litellm.ai/docs/proxy/enterprise#tracking-spend-for-custom-tags)
5. Langfuse - fix logging request tags, read from standard logging payload
6. GCS - don’t truncate payload on logging
7. New GCS Pub/Sub logging support [Start Here](https://docs.litellm.ai/docs/proxy/logging#google-cloud-storage---pubsub-topic)
8. Add AIM Guardrails support [Start Here](https://docs.litellm.ai/docs/proxy/guardrails/aim_security)

## Security [​](https://docs.litellm.ai/release_notes/tags/logging\#security "Direct link to Security")

1. New Enterprise SLA for patching security vulnerabilities. [See Here](https://docs.litellm.ai/docs/enterprise#slas--professional-support)
2. Hashicorp - support using vault namespace for TLS auth. [Start Here](https://docs.litellm.ai/docs/secret#hashicorp-vault)
3. Azure - DefaultAzureCredential support

## Health Checks [​](https://docs.litellm.ai/release_notes/tags/logging\#health-checks "Direct link to Health Checks")

1. Cleanup pricing-only model names from wildcard route list - prevent bad health checks
2. Allow specifying a health check model for wildcard routes - [https://docs.litellm.ai/docs/proxy/health#wildcard-routes](https://docs.litellm.ai/docs/proxy/health#wildcard-routes)
3. New ‘health\_check\_timeout ‘ param with default 1min upperbound to prevent bad model from health check to hang and cause pod restarts. [Start Here](https://docs.litellm.ai/docs/proxy/health#health-check-timeout)
4. Datadog - add data dog service health check + expose new `/health/services` endpoint. [Start Here](https://docs.litellm.ai/docs/proxy/health#healthservices)

## Performance / Reliability improvements [​](https://docs.litellm.ai/release_notes/tags/logging\#performance--reliability-improvements "Direct link to Performance / Reliability improvements")

01. 3x increase in RPS - moving to orjson for reading request body
02. LLM Routing speedup - using cached get model group info
03. SDK speedup - using cached get model info helper - reduces CPU work to get model info
04. Proxy speedup - only read request body 1 time per request
05. Infinite loop detection scripts added to codebase
06. Bedrock - pure async image transformation requests
07. Cooldowns - single deployment model group if 100% calls fail in high traffic - prevents an o1 outage from impacting other calls
08. Response Headers - return
    1. `x-litellm-timeout`
    2. `x-litellm-attempted-retries`
    3. `x-litellm-overhead-duration-ms`
    4. `x-litellm-response-duration-ms`
09. ensure duplicate callbacks are not added to proxy
10. Requirements.txt - bump certifi version

## General Proxy Improvements [​](https://docs.litellm.ai/release_notes/tags/logging\#general-proxy-improvements "Direct link to General Proxy Improvements")

1. JWT / OIDC Auth - new `enforce_rbac` param,allows proxy admin to prevent any unmapped yet authenticated jwt tokens from calling proxy. [Start Here](https://docs.litellm.ai/docs/proxy/token_auth#enforce-role-based-access-control-rbac)
2. fix custom openapi schema generation for customized swagger’s
3. Request Headers - support reading `x-litellm-timeout` param from request headers. Enables model timeout control when using Vercel’s AI SDK + LiteLLM Proxy. [Start Here](https://docs.litellm.ai/docs/proxy/request_headers#litellm-headers)
4. JWT / OIDC Auth - new `role` based permissions for model authentication. [See Here](https://docs.litellm.ai/docs/proxy/jwt_auth_arch)

## Complete Git Diff [​](https://docs.litellm.ai/release_notes/tags/logging\#complete-git-diff "Direct link to Complete Git Diff")

This is the diff between v1.57.8-stable and v1.59.8-stable.

Use this to see the changes in the codebase.

[**Git Diff**](https://github.com/BerriAI/litellm/compare/v1.57.8-stable...v1.59.8-stable)

info

Get a 7 day free trial for LiteLLM Enterprise [here](https://litellm.ai/#trial).

**no call needed**

## UI Improvements [​](https://docs.litellm.ai/release_notes/tags/logging\#ui-improvements "Direct link to UI Improvements")

### \[Opt In\] Admin UI - view messages / responses [​](https://docs.litellm.ai/release_notes/tags/logging\#opt-in-admin-ui---view-messages--responses "Direct link to opt-in-admin-ui---view-messages--responses")

You can now view messages and response logs on Admin UI.

![](https://docs.litellm.ai/assets/ideal-img/ui_logs.17b0459.1497.png)

How to enable it - add `store_prompts_in_spend_logs: true` to your `proxy_config.yaml`

Once this flag is enabled, your `messages` and `responses` will be stored in the `LiteLLM_Spend_Logs` table.

```codeBlockLines_e6Vv
general_settings:
  store_prompts_in_spend_logs: true

```

## DB Schema Change [​](https://docs.litellm.ai/release_notes/tags/logging\#db-schema-change "Direct link to DB Schema Change")

Added `messages` and `responses` to the `LiteLLM_Spend_Logs` table.

**By default this is not logged.** If you want `messages` and `responses` to be logged, you need to opt in with this setting

```codeBlockLines_e6Vv
general_settings:
  store_prompts_in_spend_logs: true

```

`guardrails`, `logging`, `virtual key management`, `new models`

info

Get a 7 day free trial for LiteLLM Enterprise [here](https://litellm.ai/#trial).

**no call needed**

## New Features [​](https://docs.litellm.ai/release_notes/tags/logging\#new-features "Direct link to New Features")

### ✨ Log Guardrail Traces [​](https://docs.litellm.ai/release_notes/tags/logging\#-log-guardrail-traces "Direct link to ✨ Log Guardrail Traces")

Track guardrail failure rate and if a guardrail is going rogue and failing requests. [Start here](https://docs.litellm.ai/docs/proxy/guardrails/quick_start)

#### Traced Guardrail Success [​](https://docs.litellm.ai/release_notes/tags/logging\#traced-guardrail-success "Direct link to Traced Guardrail Success")

![](https://docs.litellm.ai/assets/ideal-img/gd_success.02a2daf.1862.png)

#### Traced Guardrail Failure [​](https://docs.litellm.ai/release_notes/tags/logging\#traced-guardrail-failure "Direct link to Traced Guardrail Failure")

![](https://docs.litellm.ai/assets/ideal-img/gd_fail.457338e.1848.png)

### `/guardrails/list` [​](https://docs.litellm.ai/release_notes/tags/logging\#guardrailslist "Direct link to guardrailslist")

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

### ✨ Guardrails with Mock LLM [​](https://docs.litellm.ai/release_notes/tags/logging\#-guardrails-with-mock-llm "Direct link to ✨ Guardrails with Mock LLM")

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

### Assign Keys to Users [​](https://docs.litellm.ai/release_notes/tags/logging\#assign-keys-to-users "Direct link to Assign Keys to Users")

You can now assign keys to users via Proxy UI

![](https://docs.litellm.ai/assets/ideal-img/ui_key.9642332.1212.png)

## New Models [​](https://docs.litellm.ai/release_notes/tags/logging\#new-models "Direct link to New Models")

- `openrouter/openai/o1`
- `vertex_ai/mistral-large@2411`

## Fixes [​](https://docs.litellm.ai/release_notes/tags/logging\#fixes "Direct link to Fixes")

- Fix `vertex_ai/` mistral model pricing: [https://github.com/BerriAI/litellm/pull/7345](https://github.com/BerriAI/litellm/pull/7345)
- Missing model\_group field in logs for aspeech call types [https://github.com/BerriAI/litellm/pull/7392](https://github.com/BerriAI/litellm/pull/7392)

`key management`, `budgets/rate limits`, `logging`, `guardrails`

info

Get a 7 day free trial for LiteLLM Enterprise [here](https://litellm.ai/#trial).

**no call needed**

## ✨ Budget / Rate Limit Tiers [​](https://docs.litellm.ai/release_notes/tags/logging\#-budget--rate-limit-tiers "Direct link to ✨ Budget / Rate Limit Tiers")

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

## OTEL Bug Fix [​](https://docs.litellm.ai/release_notes/tags/logging\#otel-bug-fix "Direct link to OTEL Bug Fix")

LiteLLM was double logging litellm\_request span. This is now fixed.

[Relevant PR](https://github.com/BerriAI/litellm/pull/7435)

## Logging for Finetuning Endpoints [​](https://docs.litellm.ai/release_notes/tags/logging\#logging-for-finetuning-endpoints "Direct link to Logging for Finetuning Endpoints")

Logs for finetuning requests are now available on all logging providers (e.g. Datadog).

What's logged per request:

- file\_id
- finetuning\_job\_id
- any key/team metadata

**Start Here:**

- [Setup Finetuning](https://docs.litellm.ai/docs/fine_tuning)
- [Setup Logging](https://docs.litellm.ai/docs/proxy/logging#datadog)

## Dynamic Params for Guardrails [​](https://docs.litellm.ai/release_notes/tags/logging\#dynamic-params-for-guardrails "Direct link to Dynamic Params for Guardrails")

You can now set custom parameters (like success threshold) for your guardrails in each request.

[See guardrails spec for more details](https://docs.litellm.ai/docs/proxy/guardrails/custom_guardrail#-pass-additional-parameters-to-guardrail)

## Management Endpoints Updates
[Skip to main content](https://docs.litellm.ai/release_notes/tags/management-endpoints#__docusaurus_skipToContent_fallback)

v1.65.0 updates the `/model/new` endpoint to prevent non-team admins from creating team models.

This means that only proxy admins or team admins can create team models.

## Additional Changes [​](https://docs.litellm.ai/release_notes/tags/management-endpoints\#additional-changes "Direct link to Additional Changes")

- Allows team admins to call `/model/update` to update team models.
- Allows team admins to call `/model/delete` to delete team models.
- Introduces new `user_models_only` param to `/v2/model/info` \- only return models added by this user.

These changes enable team admins to add and manage models for their team on the LiteLLM UI + API.

![](https://docs.litellm.ai/assets/ideal-img/team_model_add.1ddd404.1251.png)

`alerting`, `prometheus`, `secret management`, `management endpoints`, `ui`, `prompt management`, `finetuning`, `batch`

## New / Updated Models [​](https://docs.litellm.ai/release_notes/tags/management-endpoints\#new--updated-models "Direct link to New / Updated Models")

1. Mistral large pricing - [https://github.com/BerriAI/litellm/pull/7452](https://github.com/BerriAI/litellm/pull/7452)
2. Cohere command-r7b-12-2024 pricing - [https://github.com/BerriAI/litellm/pull/7553/files](https://github.com/BerriAI/litellm/pull/7553/files)
3. Voyage - new models, prices and context window information - [https://github.com/BerriAI/litellm/pull/7472](https://github.com/BerriAI/litellm/pull/7472)
4. Anthropic - bump Bedrock claude-3-5-haiku max\_output\_tokens to 8192

## General Proxy Improvements [​](https://docs.litellm.ai/release_notes/tags/management-endpoints\#general-proxy-improvements "Direct link to General Proxy Improvements")

1. Health check support for realtime models
2. Support calling Azure realtime routes via virtual keys
3. Support custom tokenizer on `/utils/token_counter` \- useful when checking token count for self-hosted models
4. Request Prioritization - support on `/v1/completion` endpoint as well

## LLM Translation Improvements [​](https://docs.litellm.ai/release_notes/tags/management-endpoints\#llm-translation-improvements "Direct link to LLM Translation Improvements")

1. Deepgram STT support. [Start Here](https://docs.litellm.ai/docs/providers/deepgram)
2. OpenAI Moderations - `omni-moderation-latest` support. [Start Here](https://docs.litellm.ai/docs/moderation)
3. Azure O1 - fake streaming support. This ensures if a `stream=true` is passed, the response is streamed. [Start Here](https://docs.litellm.ai/docs/providers/azure)
4. Anthropic - non-whitespace char stop sequence handling - [PR](https://github.com/BerriAI/litellm/pull/7484)
5. Azure OpenAI - support Entra ID username + password based auth. [Start Here](https://docs.litellm.ai/docs/providers/azure#entra-id---use-tenant_id-client_id-client_secret)
6. LM Studio - embedding route support. [Start Here](https://docs.litellm.ai/docs/providers/lm-studio)
7. WatsonX - ZenAPIKeyAuth support. [Start Here](https://docs.litellm.ai/docs/providers/watsonx)

## Prompt Management Improvements [​](https://docs.litellm.ai/release_notes/tags/management-endpoints\#prompt-management-improvements "Direct link to Prompt Management Improvements")

1. Langfuse integration
2. HumanLoop integration
3. Support for using load balanced models
4. Support for loading optional params from prompt manager

[Start Here](https://docs.litellm.ai/docs/proxy/prompt_management)

## Finetuning + Batch APIs Improvements [​](https://docs.litellm.ai/release_notes/tags/management-endpoints\#finetuning--batch-apis-improvements "Direct link to Finetuning + Batch APIs Improvements")

1. Improved unified endpoint support for Vertex AI finetuning - [PR](https://github.com/BerriAI/litellm/pull/7487)
2. Add support for retrieving vertex api batch jobs - [PR](https://github.com/BerriAI/litellm/commit/13f364682d28a5beb1eb1b57f07d83d5ef50cbdc)

## _NEW_ Alerting Integration [​](https://docs.litellm.ai/release_notes/tags/management-endpoints\#new-alerting-integration "Direct link to new-alerting-integration")

PagerDuty Alerting Integration.

Handles two types of alerts:

- High LLM API Failure Rate. Configure X fails in Y seconds to trigger an alert.
- High Number of Hanging LLM Requests. Configure X hangs in Y seconds to trigger an alert.

[Start Here](https://docs.litellm.ai/docs/proxy/pagerduty)

## Prometheus Improvements [​](https://docs.litellm.ai/release_notes/tags/management-endpoints\#prometheus-improvements "Direct link to Prometheus Improvements")

Added support for tracking latency/spend/tokens based on custom metrics. [Start Here](https://docs.litellm.ai/docs/proxy/prometheus#beta-custom-metrics)

## _NEW_ Hashicorp Secret Manager Support [​](https://docs.litellm.ai/release_notes/tags/management-endpoints\#new-hashicorp-secret-manager-support "Direct link to new-hashicorp-secret-manager-support")

Support for reading credentials + writing LLM API keys. [Start Here](https://docs.litellm.ai/docs/secret#hashicorp-vault)

## Management Endpoints / UI Improvements [​](https://docs.litellm.ai/release_notes/tags/management-endpoints\#management-endpoints--ui-improvements "Direct link to Management Endpoints / UI Improvements")

1. Create and view organizations + assign org admins on the Proxy UI
2. Support deleting keys by key\_alias
3. Allow assigning teams to org on UI
4. Disable using ui session token for 'test key' pane
5. Show model used in 'test key' pane
6. Support markdown output in 'test key' pane

## Helm Improvements [​](https://docs.litellm.ai/release_notes/tags/management-endpoints\#helm-improvements "Direct link to Helm Improvements")

1. Prevent istio injection for db migrations cron job
2. allow using migrationJob.enabled variable within job

## Logging Improvements [​](https://docs.litellm.ai/release_notes/tags/management-endpoints\#logging-improvements "Direct link to Logging Improvements")

1. braintrust logging: respect project\_id, add more metrics - [https://github.com/BerriAI/litellm/pull/7613](https://github.com/BerriAI/litellm/pull/7613)
2. Athina - support base url - `ATHINA_BASE_URL`
3. Lunary - Allow passing custom parent run id to LLM Calls

## Git Diff [​](https://docs.litellm.ai/release_notes/tags/management-endpoints\#git-diff "Direct link to Git Diff")

This is the diff between v1.56.3-stable and v1.57.8-stable.

Use this to see the changes in the codebase.

[Git Diff](https://github.com/BerriAI/litellm/compare/v1.56.3-stable...189b67760011ea313ca58b1f8bd43aa74fbd7f55)

`langfuse`, `management endpoints`, `ui`, `prometheus`, `secret management`

## Langfuse Prompt Management [​](https://docs.litellm.ai/release_notes/tags/management-endpoints\#langfuse-prompt-management "Direct link to Langfuse Prompt Management")

Langfuse Prompt Management is being labelled as BETA. This allows us to iterate quickly on the feedback we're receiving, and making the status clearer to users. We expect to make this feature to be stable by next month (February 2025).

Changes:

- Include the client message in the LLM API Request. (Previously only the prompt template was sent, and the client message was ignored).
- Log the prompt template in the logged request (e.g. to s3/langfuse).
- Log the 'prompt\_id' and 'prompt\_variables' in the logged request (e.g. to s3/langfuse).

[Start Here](https://docs.litellm.ai/docs/proxy/prompt_management)

## Team/Organization Management + UI Improvements [​](https://docs.litellm.ai/release_notes/tags/management-endpoints\#teamorganization-management--ui-improvements "Direct link to Team/Organization Management + UI Improvements")

Managing teams and organizations on the UI is now easier.

Changes:

- Support for editing user role within team on UI.
- Support updating team member role to admin via api - `/team/member_update`
- Show team admins all keys for their team.
- Add organizations with budgets
- Assign teams to orgs on the UI
- Auto-assign SSO users to teams

[Start Here](https://docs.litellm.ai/docs/proxy/self_serve)

## Hashicorp Vault Support [​](https://docs.litellm.ai/release_notes/tags/management-endpoints\#hashicorp-vault-support "Direct link to Hashicorp Vault Support")

We now support writing LiteLLM Virtual API keys to Hashicorp Vault.

[Start Here](https://docs.litellm.ai/docs/proxy/vault)

## Custom Prometheus Metrics [​](https://docs.litellm.ai/release_notes/tags/management-endpoints\#custom-prometheus-metrics "Direct link to Custom Prometheus Metrics")

Define custom prometheus metrics, and track usage/latency/no. of requests against them

This allows for more fine-grained tracking - e.g. on prompt template passed in request metadata

[Start Here](https://docs.litellm.ai/docs/proxy/prometheus#beta-custom-metrics)

## MCP Support Updates
[Skip to main content](https://docs.litellm.ai/release_notes/tags/mcp#__docusaurus_skipToContent_fallback)

v1.65.0-stable is live now. Here are the key highlights of this release:

- **MCP Support**: Support for adding and using MCP servers on the LiteLLM proxy.
- **UI view total usage after 1M+ logs**: You can now view usage analytics after crossing 1M+ logs in DB.

## Model Context Protocol (MCP) [​](https://docs.litellm.ai/release_notes/tags/mcp\#model-context-protocol-mcp "Direct link to Model Context Protocol (MCP)")

This release introduces support for centrally adding MCP servers on LiteLLM. This allows you to add MCP server endpoints and your developers can `list` and `call` MCP tools through LiteLLM.

Read more about MCP [here](https://docs.litellm.ai/docs/mcp).

![](https://docs.litellm.ai/assets/ideal-img/mcp_ui.4a5216a.1920.png)

Expose and use MCP servers through LiteLLM

## UI view total usage after 1M+ logs [​](https://docs.litellm.ai/release_notes/tags/mcp\#ui-view-total-usage-after-1m-logs "Direct link to UI view total usage after 1M+ logs")

This release brings the ability to view total usage analytics even after exceeding 1M+ logs in your database. We've implemented a scalable architecture that stores only aggregate usage data, resulting in significantly more efficient queries and reduced database CPU utilization.

![](https://docs.litellm.ai/assets/ideal-img/ui_usage.3ffdba3.1200.png)

View total usage after 1M+ logs

- How this works:

  - We now aggregate usage data into a dedicated DailyUserSpend table, significantly reducing query load and CPU usage even beyond 1M+ logs.
- Daily Spend Breakdown API:

  - Retrieve granular daily usage data (by model, provider, and API key) with a single endpoint.
    Example Request:



    Daily Spend Breakdown API





    ```codeBlockLines_e6Vv codeBlockLinesWithNumbering_o6Pm
    curl -L -X GET 'http://localhost:4000/user/daily/activity?start_date=2025-03-20&end_date=2025-03-27' \
    -H 'Authorization: Bearer sk-...'

    ```











    Daily Spend Breakdown API Response





    ```codeBlockLines_e6Vv codeBlockLinesWithNumbering_o6Pm
    {
        "results": [\
            {\
                "date": "2025-03-27",\
                "metrics": {\
                    "spend": 0.0177072,\
                    "prompt_tokens": 111,\
                    "completion_tokens": 1711,\
                    "total_tokens": 1822,\
                    "api_requests": 11\
                },\
                "breakdown": {\
                    "models": {\
                        "gpt-4o-mini": {\
                            "spend": 1.095e-05,\
                            "prompt_tokens": 37,\
                            "completion_tokens": 9,\
                            "total_tokens": 46,\
                            "api_requests": 1\
                    },\
                    "providers": { "openai": { ... }, "azure_ai": { ... } },\
                    "api_keys": { "3126b6eaf1...": { ... } }\
                }\
            }\
        ],
        "metadata": {
            "total_spend": 0.7274667,
            "total_prompt_tokens": 280990,
            "total_completion_tokens": 376674,
            "total_api_requests": 14
        }
    }

    ```

## New Models / Updated Models [​](https://docs.litellm.ai/release_notes/tags/mcp\#new-models--updated-models "Direct link to New Models / Updated Models")

- Support for Vertex AI gemini-2.0-flash-lite & Google AI Studio gemini-2.0-flash-lite [PR](https://github.com/BerriAI/litellm/pull/9523)
- Support for Vertex AI Fine-Tuned LLMs [PR](https://github.com/BerriAI/litellm/pull/9542)
- Nova Canvas image generation support [PR](https://github.com/BerriAI/litellm/pull/9525)
- OpenAI gpt-4o-transcribe support [PR](https://github.com/BerriAI/litellm/pull/9517)
- Added new Vertex AI text embedding model [PR](https://github.com/BerriAI/litellm/pull/9476)

## LLM Translation [​](https://docs.litellm.ai/release_notes/tags/mcp\#llm-translation "Direct link to LLM Translation")

- OpenAI Web Search Tool Call Support [PR](https://github.com/BerriAI/litellm/pull/9465)
- Vertex AI topLogprobs support [PR](https://github.com/BerriAI/litellm/pull/9518)
- Support for sending images and video to Vertex AI multimodal embedding [Doc](https://docs.litellm.ai/docs/providers/vertex#multi-modal-embeddings)
- Support litellm.api\_base for Vertex AI + Gemini across completion, embedding, image\_generation [PR](https://github.com/BerriAI/litellm/pull/9516)
- Bug fix for returning `response_cost` when using litellm python SDK with LiteLLM Proxy [PR](https://github.com/BerriAI/litellm/commit/6fd18651d129d606182ff4b980e95768fc43ca3d)
- Support for `max_completion_tokens` on Mistral API [PR](https://github.com/BerriAI/litellm/pull/9606)
- Refactored Vertex AI passthrough routes - fixes unpredictable behaviour with auto-setting default\_vertex\_region on router model add [PR](https://github.com/BerriAI/litellm/pull/9467)

## Spend Tracking Improvements [​](https://docs.litellm.ai/release_notes/tags/mcp\#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

- Log 'api\_base' on spend logs [PR](https://github.com/BerriAI/litellm/pull/9509)
- Support for Gemini audio token cost tracking [PR](https://github.com/BerriAI/litellm/pull/9535)
- Fixed OpenAI audio input token cost tracking [PR](https://github.com/BerriAI/litellm/pull/9535)

## UI [​](https://docs.litellm.ai/release_notes/tags/mcp\#ui "Direct link to UI")

### Model Management [​](https://docs.litellm.ai/release_notes/tags/mcp\#model-management "Direct link to Model Management")

- Allowed team admins to add/update/delete models on UI [PR](https://github.com/BerriAI/litellm/pull/9572)
- Added render supports\_web\_search on model hub [PR](https://github.com/BerriAI/litellm/pull/9469)

### Request Logs [​](https://docs.litellm.ai/release_notes/tags/mcp\#request-logs "Direct link to Request Logs")

- Show API base and model ID on request logs [PR](https://github.com/BerriAI/litellm/pull/9572)
- Allow viewing keyinfo on request logs [PR](https://github.com/BerriAI/litellm/pull/9568)

### Usage Tab [​](https://docs.litellm.ai/release_notes/tags/mcp\#usage-tab "Direct link to Usage Tab")

- Added Daily User Spend Aggregate view - allows UI Usage tab to work > 1m rows [PR](https://github.com/BerriAI/litellm/pull/9538)
- Connected UI to "LiteLLM\_DailyUserSpend" spend table [PR](https://github.com/BerriAI/litellm/pull/9603)

## Logging Integrations [​](https://docs.litellm.ai/release_notes/tags/mcp\#logging-integrations "Direct link to Logging Integrations")

- Fixed StandardLoggingPayload for GCS Pub Sub Logging Integration [PR](https://github.com/BerriAI/litellm/pull/9508)
- Track `litellm_model_name` on `StandardLoggingPayload` [Docs](https://docs.litellm.ai/docs/proxy/logging_spec#standardlogginghiddenparams)

## Performance / Reliability Improvements [​](https://docs.litellm.ai/release_notes/tags/mcp\#performance--reliability-improvements "Direct link to Performance / Reliability Improvements")

- LiteLLM Redis semantic caching implementation [PR](https://github.com/BerriAI/litellm/pull/9356)
- Gracefully handle exceptions when DB is having an outage [PR](https://github.com/BerriAI/litellm/pull/9533)
- Allow Pods to startup + passing /health/readiness when allow\_requests\_on\_db\_unavailable: True and DB is down [PR](https://github.com/BerriAI/litellm/pull/9569)

## General Improvements [​](https://docs.litellm.ai/release_notes/tags/mcp\#general-improvements "Direct link to General Improvements")

- Support for exposing MCP tools on litellm proxy [PR](https://github.com/BerriAI/litellm/pull/9426)
- Support discovering Gemini, Anthropic, xAI models by calling their /v1/model endpoint [PR](https://github.com/BerriAI/litellm/pull/9530)
- Fixed route check for non-proxy admins on JWT auth [PR](https://github.com/BerriAI/litellm/pull/9454)
- Added baseline Prisma database migrations [PR](https://github.com/BerriAI/litellm/pull/9565)
- View all wildcard models on /model/info [PR](https://github.com/BerriAI/litellm/pull/9572)

## Security [​](https://docs.litellm.ai/release_notes/tags/mcp\#security "Direct link to Security")

- Bumped next from 14.2.21 to 14.2.25 in UI dashboard [PR](https://github.com/BerriAI/litellm/pull/9458)

## Complete Git Diff [​](https://docs.litellm.ai/release_notes/tags/mcp\#complete-git-diff "Direct link to Complete Git Diff")

[Here's the complete git diff](https://github.com/BerriAI/litellm/compare/v1.63.14-stable.patch1...v1.65.0-stable)

## LiteLLM New Features
[Skip to main content](https://docs.litellm.ai/release_notes/tags/new-models#__docusaurus_skipToContent_fallback)

`guardrails`, `logging`, `virtual key management`, `new models`

info

Get a 7 day free trial for LiteLLM Enterprise [here](https://litellm.ai/#trial).

**no call needed**

## New Features [​](https://docs.litellm.ai/release_notes/tags/new-models\#new-features "Direct link to New Features")

### ✨ Log Guardrail Traces [​](https://docs.litellm.ai/release_notes/tags/new-models\#-log-guardrail-traces "Direct link to ✨ Log Guardrail Traces")

Track guardrail failure rate and if a guardrail is going rogue and failing requests. [Start here](https://docs.litellm.ai/docs/proxy/guardrails/quick_start)

#### Traced Guardrail Success [​](https://docs.litellm.ai/release_notes/tags/new-models\#traced-guardrail-success "Direct link to Traced Guardrail Success")

![](https://docs.litellm.ai/assets/ideal-img/gd_success.02a2daf.1862.png)

#### Traced Guardrail Failure [​](https://docs.litellm.ai/release_notes/tags/new-models\#traced-guardrail-failure "Direct link to Traced Guardrail Failure")

![](https://docs.litellm.ai/assets/ideal-img/gd_fail.457338e.1848.png)

### `/guardrails/list` [​](https://docs.litellm.ai/release_notes/tags/new-models\#guardrailslist "Direct link to guardrailslist")

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

### ✨ Guardrails with Mock LLM [​](https://docs.litellm.ai/release_notes/tags/new-models\#-guardrails-with-mock-llm "Direct link to ✨ Guardrails with Mock LLM")

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

### Assign Keys to Users [​](https://docs.litellm.ai/release_notes/tags/new-models\#assign-keys-to-users "Direct link to Assign Keys to Users")

You can now assign keys to users via Proxy UI

![](https://docs.litellm.ai/assets/ideal-img/ui_key.9642332.1212.png)

## New Models [​](https://docs.litellm.ai/release_notes/tags/new-models\#new-models "Direct link to New Models")

- `openrouter/openai/o1`
- `vertex_ai/mistral-large@2411`

## Fixes [​](https://docs.litellm.ai/release_notes/tags/new-models\#fixes "Direct link to Fixes")

- Fix `vertex_ai/` mistral model pricing: [https://github.com/BerriAI/litellm/pull/7345](https://github.com/BerriAI/litellm/pull/7345)
- Missing model\_group field in logs for aspeech call types [https://github.com/BerriAI/litellm/pull/7392](https://github.com/BerriAI/litellm/pull/7392)

A new LiteLLM Stable release [just went out](https://github.com/BerriAI/litellm/releases/tag/v1.55.8-stable). Here are 5 updates since v1.52.2-stable.

`langfuse`, `fallbacks`, `new models`, `azure_storage`

![](https://docs.litellm.ai/assets/ideal-img/langfuse_prmpt_mgmt.19b8982.1920.png)

## Langfuse Prompt Management [​](https://docs.litellm.ai/release_notes/tags/new-models\#langfuse-prompt-management "Direct link to Langfuse Prompt Management")

This makes it easy to run experiments or change the specific models `gpt-4o` to `gpt-4o-mini` on Langfuse, instead of making changes in your applications. [Start here](https://docs.litellm.ai/docs/proxy/prompt_management)

## Control fallback prompts client-side [​](https://docs.litellm.ai/release_notes/tags/new-models\#control-fallback-prompts-client-side "Direct link to Control fallback prompts client-side")

> Claude prompts are different than OpenAI

Pass in prompts specific to model when doing fallbacks. [Start here](https://docs.litellm.ai/docs/proxy/reliability#control-fallback-prompts)

## New Providers / Models [​](https://docs.litellm.ai/release_notes/tags/new-models\#new-providers--models "Direct link to New Providers / Models")

- [NVIDIA Triton](https://developer.nvidia.com/triton-inference-server) `/infer` endpoint. [Start here](https://docs.litellm.ai/docs/providers/triton-inference-server)
- [Infinity](https://github.com/michaelfeil/infinity) Rerank Models [Start here](https://docs.litellm.ai/docs/providers/infinity)

## ✨ Azure Data Lake Storage Support [​](https://docs.litellm.ai/release_notes/tags/new-models\#-azure-data-lake-storage-support "Direct link to ✨ Azure Data Lake Storage Support")

Send LLM usage (spend, tokens) data to [Azure Data Lake](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction). This makes it easy to consume usage data on other services (eg. Databricks)
[Start here](https://docs.litellm.ai/docs/proxy/logging#azure-blob-storage)

## Docker Run LiteLLM [​](https://docs.litellm.ai/release_notes/tags/new-models\#docker-run-litellm "Direct link to Docker Run LiteLLM")

```codeBlockLines_e6Vv
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
ghcr.io/berriai/litellm:litellm_stable_release_branch-v1.55.8-stable

```

## Get Daily Updates [​](https://docs.litellm.ai/release_notes/tags/new-models\#get-daily-updates "Direct link to Get Daily Updates")

LiteLLM ships new releases every day. [Follow us on LinkedIn](https://www.linkedin.com/company/berri-ai/) to get daily updates.

## Prometheus Integration Updates
[Skip to main content](https://docs.litellm.ai/release_notes/tags/prometheus#__docusaurus_skipToContent_fallback)

`alerting`, `prometheus`, `secret management`, `management endpoints`, `ui`, `prompt management`, `finetuning`, `batch`

## New / Updated Models [​](https://docs.litellm.ai/release_notes/tags/prometheus\#new--updated-models "Direct link to New / Updated Models")

1. Mistral large pricing - [https://github.com/BerriAI/litellm/pull/7452](https://github.com/BerriAI/litellm/pull/7452)
2. Cohere command-r7b-12-2024 pricing - [https://github.com/BerriAI/litellm/pull/7553/files](https://github.com/BerriAI/litellm/pull/7553/files)
3. Voyage - new models, prices and context window information - [https://github.com/BerriAI/litellm/pull/7472](https://github.com/BerriAI/litellm/pull/7472)
4. Anthropic - bump Bedrock claude-3-5-haiku max\_output\_tokens to 8192

## General Proxy Improvements [​](https://docs.litellm.ai/release_notes/tags/prometheus\#general-proxy-improvements "Direct link to General Proxy Improvements")

1. Health check support for realtime models
2. Support calling Azure realtime routes via virtual keys
3. Support custom tokenizer on `/utils/token_counter` \- useful when checking token count for self-hosted models
4. Request Prioritization - support on `/v1/completion` endpoint as well

## LLM Translation Improvements [​](https://docs.litellm.ai/release_notes/tags/prometheus\#llm-translation-improvements "Direct link to LLM Translation Improvements")

1. Deepgram STT support. [Start Here](https://docs.litellm.ai/docs/providers/deepgram)
2. OpenAI Moderations - `omni-moderation-latest` support. [Start Here](https://docs.litellm.ai/docs/moderation)
3. Azure O1 - fake streaming support. This ensures if a `stream=true` is passed, the response is streamed. [Start Here](https://docs.litellm.ai/docs/providers/azure)
4. Anthropic - non-whitespace char stop sequence handling - [PR](https://github.com/BerriAI/litellm/pull/7484)
5. Azure OpenAI - support Entra ID username + password based auth. [Start Here](https://docs.litellm.ai/docs/providers/azure#entra-id---use-tenant_id-client_id-client_secret)
6. LM Studio - embedding route support. [Start Here](https://docs.litellm.ai/docs/providers/lm-studio)
7. WatsonX - ZenAPIKeyAuth support. [Start Here](https://docs.litellm.ai/docs/providers/watsonx)

## Prompt Management Improvements [​](https://docs.litellm.ai/release_notes/tags/prometheus\#prompt-management-improvements "Direct link to Prompt Management Improvements")

1. Langfuse integration
2. HumanLoop integration
3. Support for using load balanced models
4. Support for loading optional params from prompt manager

[Start Here](https://docs.litellm.ai/docs/proxy/prompt_management)

## Finetuning + Batch APIs Improvements [​](https://docs.litellm.ai/release_notes/tags/prometheus\#finetuning--batch-apis-improvements "Direct link to Finetuning + Batch APIs Improvements")

1. Improved unified endpoint support for Vertex AI finetuning - [PR](https://github.com/BerriAI/litellm/pull/7487)
2. Add support for retrieving vertex api batch jobs - [PR](https://github.com/BerriAI/litellm/commit/13f364682d28a5beb1eb1b57f07d83d5ef50cbdc)

## _NEW_ Alerting Integration [​](https://docs.litellm.ai/release_notes/tags/prometheus\#new-alerting-integration "Direct link to new-alerting-integration")

PagerDuty Alerting Integration.

Handles two types of alerts:

- High LLM API Failure Rate. Configure X fails in Y seconds to trigger an alert.
- High Number of Hanging LLM Requests. Configure X hangs in Y seconds to trigger an alert.

[Start Here](https://docs.litellm.ai/docs/proxy/pagerduty)

## Prometheus Improvements [​](https://docs.litellm.ai/release_notes/tags/prometheus\#prometheus-improvements "Direct link to Prometheus Improvements")

Added support for tracking latency/spend/tokens based on custom metrics. [Start Here](https://docs.litellm.ai/docs/proxy/prometheus#beta-custom-metrics)

## _NEW_ Hashicorp Secret Manager Support [​](https://docs.litellm.ai/release_notes/tags/prometheus\#new-hashicorp-secret-manager-support "Direct link to new-hashicorp-secret-manager-support")

Support for reading credentials + writing LLM API keys. [Start Here](https://docs.litellm.ai/docs/secret#hashicorp-vault)

## Management Endpoints / UI Improvements [​](https://docs.litellm.ai/release_notes/tags/prometheus\#management-endpoints--ui-improvements "Direct link to Management Endpoints / UI Improvements")

1. Create and view organizations + assign org admins on the Proxy UI
2. Support deleting keys by key\_alias
3. Allow assigning teams to org on UI
4. Disable using ui session token for 'test key' pane
5. Show model used in 'test key' pane
6. Support markdown output in 'test key' pane

## Helm Improvements [​](https://docs.litellm.ai/release_notes/tags/prometheus\#helm-improvements "Direct link to Helm Improvements")

1. Prevent istio injection for db migrations cron job
2. allow using migrationJob.enabled variable within job

## Logging Improvements [​](https://docs.litellm.ai/release_notes/tags/prometheus\#logging-improvements "Direct link to Logging Improvements")

1. braintrust logging: respect project\_id, add more metrics - [https://github.com/BerriAI/litellm/pull/7613](https://github.com/BerriAI/litellm/pull/7613)
2. Athina - support base url - `ATHINA_BASE_URL`
3. Lunary - Allow passing custom parent run id to LLM Calls

## Git Diff [​](https://docs.litellm.ai/release_notes/tags/prometheus\#git-diff "Direct link to Git Diff")

This is the diff between v1.56.3-stable and v1.57.8-stable.

Use this to see the changes in the codebase.

[Git Diff](https://github.com/BerriAI/litellm/compare/v1.56.3-stable...189b67760011ea313ca58b1f8bd43aa74fbd7f55)

`langfuse`, `management endpoints`, `ui`, `prometheus`, `secret management`

## Langfuse Prompt Management [​](https://docs.litellm.ai/release_notes/tags/prometheus\#langfuse-prompt-management "Direct link to Langfuse Prompt Management")

Langfuse Prompt Management is being labelled as BETA. This allows us to iterate quickly on the feedback we're receiving, and making the status clearer to users. We expect to make this feature to be stable by next month (February 2025).

Changes:

- Include the client message in the LLM API Request. (Previously only the prompt template was sent, and the client message was ignored).
- Log the prompt template in the logged request (e.g. to s3/langfuse).
- Log the 'prompt\_id' and 'prompt\_variables' in the logged request (e.g. to s3/langfuse).

[Start Here](https://docs.litellm.ai/docs/proxy/prompt_management)

## Team/Organization Management + UI Improvements [​](https://docs.litellm.ai/release_notes/tags/prometheus\#teamorganization-management--ui-improvements "Direct link to Team/Organization Management + UI Improvements")

Managing teams and organizations on the UI is now easier.

Changes:

- Support for editing user role within team on UI.
- Support updating team member role to admin via api - `/team/member_update`
- Show team admins all keys for their team.
- Add organizations with budgets
- Assign teams to orgs on the UI
- Auto-assign SSO users to teams

[Start Here](https://docs.litellm.ai/docs/proxy/self_serve)

## Hashicorp Vault Support [​](https://docs.litellm.ai/release_notes/tags/prometheus\#hashicorp-vault-support "Direct link to Hashicorp Vault Support")

We now support writing LiteLLM Virtual API keys to Hashicorp Vault.

[Start Here](https://docs.litellm.ai/docs/proxy/vault)

## Custom Prometheus Metrics [​](https://docs.litellm.ai/release_notes/tags/prometheus\#custom-prometheus-metrics "Direct link to Custom Prometheus Metrics")

Define custom prometheus metrics, and track usage/latency/no. of requests against them

This allows for more fine-grained tracking - e.g. on prompt template passed in request metadata

[Start Here](https://docs.litellm.ai/docs/proxy/prometheus#beta-custom-metrics)

## Prompt Management Updates
[Skip to main content](https://docs.litellm.ai/release_notes/tags/prompt-management#__docusaurus_skipToContent_fallback)

`alerting`, `prometheus`, `secret management`, `management endpoints`, `ui`, `prompt management`, `finetuning`, `batch`

## New / Updated Models [​](https://docs.litellm.ai/release_notes/tags/prompt-management\#new--updated-models "Direct link to New / Updated Models")

1. Mistral large pricing - [https://github.com/BerriAI/litellm/pull/7452](https://github.com/BerriAI/litellm/pull/7452)
2. Cohere command-r7b-12-2024 pricing - [https://github.com/BerriAI/litellm/pull/7553/files](https://github.com/BerriAI/litellm/pull/7553/files)
3. Voyage - new models, prices and context window information - [https://github.com/BerriAI/litellm/pull/7472](https://github.com/BerriAI/litellm/pull/7472)
4. Anthropic - bump Bedrock claude-3-5-haiku max\_output\_tokens to 8192

## General Proxy Improvements [​](https://docs.litellm.ai/release_notes/tags/prompt-management\#general-proxy-improvements "Direct link to General Proxy Improvements")

1. Health check support for realtime models
2. Support calling Azure realtime routes via virtual keys
3. Support custom tokenizer on `/utils/token_counter` \- useful when checking token count for self-hosted models
4. Request Prioritization - support on `/v1/completion` endpoint as well

## LLM Translation Improvements [​](https://docs.litellm.ai/release_notes/tags/prompt-management\#llm-translation-improvements "Direct link to LLM Translation Improvements")

1. Deepgram STT support. [Start Here](https://docs.litellm.ai/docs/providers/deepgram)
2. OpenAI Moderations - `omni-moderation-latest` support. [Start Here](https://docs.litellm.ai/docs/moderation)
3. Azure O1 - fake streaming support. This ensures if a `stream=true` is passed, the response is streamed. [Start Here](https://docs.litellm.ai/docs/providers/azure)
4. Anthropic - non-whitespace char stop sequence handling - [PR](https://github.com/BerriAI/litellm/pull/7484)
5. Azure OpenAI - support Entra ID username + password based auth. [Start Here](https://docs.litellm.ai/docs/providers/azure#entra-id---use-tenant_id-client_id-client_secret)
6. LM Studio - embedding route support. [Start Here](https://docs.litellm.ai/docs/providers/lm-studio)
7. WatsonX - ZenAPIKeyAuth support. [Start Here](https://docs.litellm.ai/docs/providers/watsonx)

## Prompt Management Improvements [​](https://docs.litellm.ai/release_notes/tags/prompt-management\#prompt-management-improvements "Direct link to Prompt Management Improvements")

1. Langfuse integration
2. HumanLoop integration
3. Support for using load balanced models
4. Support for loading optional params from prompt manager

[Start Here](https://docs.litellm.ai/docs/proxy/prompt_management)

## Finetuning + Batch APIs Improvements [​](https://docs.litellm.ai/release_notes/tags/prompt-management\#finetuning--batch-apis-improvements "Direct link to Finetuning + Batch APIs Improvements")

1. Improved unified endpoint support for Vertex AI finetuning - [PR](https://github.com/BerriAI/litellm/pull/7487)
2. Add support for retrieving vertex api batch jobs - [PR](https://github.com/BerriAI/litellm/commit/13f364682d28a5beb1eb1b57f07d83d5ef50cbdc)

## _NEW_ Alerting Integration [​](https://docs.litellm.ai/release_notes/tags/prompt-management\#new-alerting-integration "Direct link to new-alerting-integration")

PagerDuty Alerting Integration.

Handles two types of alerts:

- High LLM API Failure Rate. Configure X fails in Y seconds to trigger an alert.
- High Number of Hanging LLM Requests. Configure X hangs in Y seconds to trigger an alert.

[Start Here](https://docs.litellm.ai/docs/proxy/pagerduty)

## Prometheus Improvements [​](https://docs.litellm.ai/release_notes/tags/prompt-management\#prometheus-improvements "Direct link to Prometheus Improvements")

Added support for tracking latency/spend/tokens based on custom metrics. [Start Here](https://docs.litellm.ai/docs/proxy/prometheus#beta-custom-metrics)

## _NEW_ Hashicorp Secret Manager Support [​](https://docs.litellm.ai/release_notes/tags/prompt-management\#new-hashicorp-secret-manager-support "Direct link to new-hashicorp-secret-manager-support")

Support for reading credentials + writing LLM API keys. [Start Here](https://docs.litellm.ai/docs/secret#hashicorp-vault)

## Management Endpoints / UI Improvements [​](https://docs.litellm.ai/release_notes/tags/prompt-management\#management-endpoints--ui-improvements "Direct link to Management Endpoints / UI Improvements")

1. Create and view organizations + assign org admins on the Proxy UI
2. Support deleting keys by key\_alias
3. Allow assigning teams to org on UI
4. Disable using ui session token for 'test key' pane
5. Show model used in 'test key' pane
6. Support markdown output in 'test key' pane

## Helm Improvements [​](https://docs.litellm.ai/release_notes/tags/prompt-management\#helm-improvements "Direct link to Helm Improvements")

1. Prevent istio injection for db migrations cron job
2. allow using migrationJob.enabled variable within job

## Logging Improvements [​](https://docs.litellm.ai/release_notes/tags/prompt-management\#logging-improvements "Direct link to Logging Improvements")

1. braintrust logging: respect project\_id, add more metrics - [https://github.com/BerriAI/litellm/pull/7613](https://github.com/BerriAI/litellm/pull/7613)
2. Athina - support base url - `ATHINA_BASE_URL`
3. Lunary - Allow passing custom parent run id to LLM Calls

## Git Diff [​](https://docs.litellm.ai/release_notes/tags/prompt-management\#git-diff "Direct link to Git Diff")

This is the diff between v1.56.3-stable and v1.57.8-stable.

Use this to see the changes in the codebase.

[Git Diff](https://github.com/BerriAI/litellm/compare/v1.56.3-stable...189b67760011ea313ca58b1f8bd43aa74fbd7f55)

## LLM Translation Updates
[Skip to main content](https://docs.litellm.ai/release_notes/tags/reasoning-content#__docusaurus_skipToContent_fallback)

These are the changes since `v1.61.20-stable`.

This release is primarily focused on:

- LLM Translation improvements (more `thinking` content improvements)
- UI improvements (Error logs now shown on UI)

info

This release will be live on 03/09/2025

![](https://docs.litellm.ai/assets/ideal-img/v1632_release.7b42da1.1920.jpg)

## Demo Instance [​](https://docs.litellm.ai/release_notes/tags/reasoning-content\#demo-instance "Direct link to Demo Instance")

Here's a Demo Instance to test changes:

- Instance: [https://demo.litellm.ai/](https://demo.litellm.ai/)
- Login Credentials:
  - Username: admin
  - Password: sk-1234

## New Models / Updated Models [​](https://docs.litellm.ai/release_notes/tags/reasoning-content\#new-models--updated-models "Direct link to New Models / Updated Models")

1. Add `supports_pdf_input` for specific Bedrock Claude models [PR](https://github.com/BerriAI/litellm/commit/f63cf0030679fe1a43d03fb196e815a0f28dae92)
2. Add pricing for amazon `eu` models [PR](https://github.com/BerriAI/litellm/commits/main/model_prices_and_context_window.json)
3. Fix Azure O1 mini pricing [PR](https://github.com/BerriAI/litellm/commit/52de1949ef2f76b8572df751f9c868a016d4832c)

## LLM Translation [​](https://docs.litellm.ai/release_notes/tags/reasoning-content\#llm-translation "Direct link to LLM Translation")

![](https://docs.litellm.ai/assets/ideal-img/anthropic_thinking.3bef9d6.1920.jpg)

01. Support `/openai/` passthrough for Assistant endpoints. [Get Started](https://docs.litellm.ai/docs/pass_through/openai_passthrough)
02. Bedrock Claude - fix tool calling transformation on invoke route. [Get Started](https://docs.litellm.ai/docs/providers/bedrock#usage---function-calling--tool-calling)
03. Bedrock Claude - response\_format support for claude on invoke route. [Get Started](https://docs.litellm.ai/docs/providers/bedrock#usage---structured-output--json-mode)
04. Bedrock - pass `description` if set in response\_format. [Get Started](https://docs.litellm.ai/docs/providers/bedrock#usage---structured-output--json-mode)
05. Bedrock - Fix passing response\_format: {"type": "text"}. [PR](https://github.com/BerriAI/litellm/commit/c84b489d5897755139aa7d4e9e54727ebe0fa540)
06. OpenAI - Handle sending image\_url as str to openai. [Get Started](https://docs.litellm.ai/docs/completion/vision)
07. Deepseek - return 'reasoning\_content' missing on streaming. [Get Started](https://docs.litellm.ai/docs/reasoning_content)
08. Caching - Support caching on reasoning content. [Get Started](https://docs.litellm.ai/docs/proxy/caching)
09. Bedrock - handle thinking blocks in assistant message. [Get Started](https://docs.litellm.ai/docs/providers/bedrock#usage---thinking--reasoning-content)
10. Anthropic - Return `signature` on streaming. [Get Started](https://docs.litellm.ai/docs/providers/bedrock#usage---thinking--reasoning-content)

- Note: We've also migrated from `signature_delta` to `signature`. [Read more](https://docs.litellm.ai/release_notes/v1.63.0)

11. Support format param for specifying image type. [Get Started](https://docs.litellm.ai/docs/completion/vision.md#explicitly-specify-image-type)
12. Anthropic - `/v1/messages` endpoint - `thinking` param support. [Get Started](https://docs.litellm.ai/docs/anthropic_unified.md)

- Note: this refactors the \[BETA\] unified `/v1/messages` endpoint, to just work for the Anthropic API.

13. Vertex AI - handle $id in response schema when calling vertex ai. [Get Started](https://docs.litellm.ai/docs/providers/vertex#json-schema)

## Spend Tracking Improvements [​](https://docs.litellm.ai/release_notes/tags/reasoning-content\#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

1. Batches API - Fix cost calculation to run on retrieve\_batch. [Get Started](https://docs.litellm.ai/docs/batches)
2. Batches API - Log batch models in spend logs / standard logging payload. [Get Started](https://docs.litellm.ai/docs/proxy/logging_spec.md#standardlogginghiddenparams)

## Management Endpoints / UI [​](https://docs.litellm.ai/release_notes/tags/reasoning-content\#management-endpoints--ui "Direct link to Management Endpoints / UI")

![](https://docs.litellm.ai/assets/ideal-img/error_logs.63c5dc9.1920.jpg)

1. Virtual Keys Page
   - Allow team/org filters to be searchable on the Create Key Page
   - Add created\_by and updated\_by fields to Keys table
   - Show 'user\_email' on key table
   - Show 100 Keys Per Page, Use full height, increase width of key alias
2. Logs Page
   - Show Error Logs on LiteLLM UI
   - Allow Internal Users to View their own logs
3. Internal Users Page
   - Allow admin to control default model access for internal users
4. Fix session handling with cookies

## Logging / Guardrail Integrations [​](https://docs.litellm.ai/release_notes/tags/reasoning-content\#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

1. Fix prometheus metrics w/ custom metrics, when keys containing team\_id make requests. [PR](https://github.com/BerriAI/litellm/pull/8935)

## Performance / Loadbalancing / Reliability improvements [​](https://docs.litellm.ai/release_notes/tags/reasoning-content\#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

1. Cooldowns - Support cooldowns on models called with client side credentials. [Get Started](https://docs.litellm.ai/docs/proxy/clientside_auth#pass-user-llm-api-keys--api-base)
2. Tag-based Routing - ensures tag-based routing across all endpoints ( `/embeddings`, `/image_generation`, etc.). [Get Started](https://docs.litellm.ai/docs/proxy/tag_routing)

## General Proxy Improvements [​](https://docs.litellm.ai/release_notes/tags/reasoning-content\#general-proxy-improvements "Direct link to General Proxy Improvements")

1. Raise BadRequestError when unknown model passed in request
2. Enforce model access restrictions on Azure OpenAI proxy route
3. Reliability fix - Handle emoji’s in text - fix orjson error
4. Model Access Patch - don't overwrite litellm.anthropic\_models when running auth checks
5. Enable setting timezone information in docker image

## Complete Git Diff [​](https://docs.litellm.ai/release_notes/tags/reasoning-content\#complete-git-diff "Direct link to Complete Git Diff")

[Here's the complete git diff](https://github.com/BerriAI/litellm/compare/v1.61.20-stable...v1.63.2-stable)

v1.63.0 fixes Anthropic 'thinking' response on streaming to return the `signature` block. [Github Issue](https://github.com/BerriAI/litellm/issues/8964)

It also moves the response structure from `signature_delta` to `signature` to be the same as Anthropic. [Anthropic Docs](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#implementing-extended-thinking)

## Diff [​](https://docs.litellm.ai/release_notes/tags/reasoning-content\#diff "Direct link to Diff")

```codeBlockLines_e6Vv
"message": {
    ...
    "reasoning_content": "The capital of France is Paris.",
    "thinking_blocks": [\
        {\
            "type": "thinking",\
            "thinking": "The capital of France is Paris.",\
-            "signature_delta": "EqoBCkgIARABGAIiQL2UoU0b1OHYi+..." # 👈 OLD FORMAT\
+            "signature": "EqoBCkgIARABGAIiQL2UoU0b1OHYi+..." # 👈 KEY CHANGE\
        }\
    ]
}

```

These are the changes since `v1.61.13-stable`.

This release is primarily focused on:

- LLM Translation improvements (claude-3-7-sonnet + 'thinking'/'reasoning\_content' support)
- UI improvements (add model flow, user management, etc)

## Demo Instance [​](https://docs.litellm.ai/release_notes/tags/reasoning-content\#demo-instance "Direct link to Demo Instance")

Here's a Demo Instance to test changes:

- Instance: [https://demo.litellm.ai/](https://demo.litellm.ai/)
- Login Credentials:
  - Username: admin
  - Password: sk-1234

## New Models / Updated Models [​](https://docs.litellm.ai/release_notes/tags/reasoning-content\#new-models--updated-models "Direct link to New Models / Updated Models")

1. Anthropic 3-7 sonnet support + cost tracking (Anthropic API + Bedrock + Vertex AI + OpenRouter)
1. Anthropic API [Start here](https://docs.litellm.ai/docs/providers/anthropic#usage---thinking--reasoning_content)
2. Bedrock API [Start here](https://docs.litellm.ai/docs/providers/bedrock#usage---thinking--reasoning-content)
3. Vertex AI API [See here](https://docs.litellm.ai/docs/providers/vertex#usage---thinking--reasoning_content)
4. OpenRouter [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L5626)
2. Gpt-4.5-preview support + cost tracking [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L79)
3. Azure AI - Phi-4 cost tracking [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L1773)
4. Claude-3.5-sonnet - vision support updated on Anthropic API [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L2888)
5. Bedrock llama vision support [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L7714)
6. Cerebras llama3.3-70b pricing [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L2697)

## LLM Translation [​](https://docs.litellm.ai/release_notes/tags/reasoning-content\#llm-translation "Direct link to LLM Translation")

1. Infinity Rerank - support returning documents when return\_documents=True [Start here](https://docs.litellm.ai/docs/providers/infinity#usage---returning-documents)
2. Amazon Deepseek - `<think>` param extraction into ‘reasoning\_content’ [Start here](https://docs.litellm.ai/docs/providers/bedrock#bedrock-imported-models-deepseek-deepseek-r1)
3. Amazon Titan Embeddings - filter out ‘aws\_’ params from request body [Start here](https://docs.litellm.ai/docs/providers/bedrock#bedrock-embedding)
4. Anthropic ‘thinking’ + ‘reasoning\_content’ translation support (Anthropic API, Bedrock, Vertex AI) [Start here](https://docs.litellm.ai/docs/reasoning_content)
5. VLLM - support ‘video\_url’ [Start here](https://docs.litellm.ai/docs/providers/vllm#send-video-url-to-vllm)
6. Call proxy via litellm SDK: Support `litellm_proxy/` for embedding, image\_generation, transcription, speech, rerank [Start here](https://docs.litellm.ai/docs/providers/litellm_proxy)
7. OpenAI Pass-through - allow using Assistants GET, DELETE on /openai pass through routes [Start here](https://docs.litellm.ai/docs/pass_through/openai_passthrough)
8. Message Translation - fix openai message for assistant msg if role is missing - openai allows this
9. O1/O3 - support ‘drop\_params’ for o3-mini and o1 parallel\_tool\_calls param (not supported currently) [See here](https://docs.litellm.ai/docs/completion/drop_params)

## Spend Tracking Improvements [​](https://docs.litellm.ai/release_notes/tags/reasoning-content\#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

1. Cost tracking for rerank via Bedrock [See PR](https://github.com/BerriAI/litellm/commit/b682dc4ec8fd07acf2f4c981d2721e36ae2a49c5)
2. Anthropic pass-through - fix race condition causing cost to not be tracked [See PR](https://github.com/BerriAI/litellm/pull/8874)
3. Anthropic pass-through: Ensure accurate token counting [See PR](https://github.com/BerriAI/litellm/pull/8880)

## Management Endpoints / UI [​](https://docs.litellm.ai/release_notes/tags/reasoning-content\#management-endpoints--ui "Direct link to Management Endpoints / UI")

01. Models Page - Allow sorting models by ‘created at’
02. Models Page - Edit Model Flow Improvements
03. Models Page - Fix Adding Azure, Azure AI Studio models on UI
04. Internal Users Page - Allow Bulk Adding Internal Users on UI
05. Internal Users Page - Allow sorting users by ‘created at’
06. Virtual Keys Page - Allow searching for UserIDs on the dropdown when assigning a user to a team [See PR](https://github.com/BerriAI/litellm/pull/8844)
07. Virtual Keys Page - allow creating a user when assigning keys to users [See PR](https://github.com/BerriAI/litellm/pull/8844)
08. Model Hub Page - fix text overflow issue [See PR](https://github.com/BerriAI/litellm/pull/8749)
09. Admin Settings Page - Allow adding MSFT SSO on UI
10. Backend - don't allow creating duplicate internal users in DB

## Helm [​](https://docs.litellm.ai/release_notes/tags/reasoning-content\#helm "Direct link to Helm")

1. support ttlSecondsAfterFinished on the migration job - [See PR](https://github.com/BerriAI/litellm/pull/8593)
2. enhance migrations job with additional configurable properties - [See PR](https://github.com/BerriAI/litellm/pull/8636)

## Logging / Guardrail Integrations [​](https://docs.litellm.ai/release_notes/tags/reasoning-content\#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

1. Arize Phoenix support
2. ‘No-log’ - fix ‘no-log’ param support on embedding calls

## Performance / Loadbalancing / Reliability improvements [​](https://docs.litellm.ai/release_notes/tags/reasoning-content\#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

1. Single Deployment Cooldown logic - Use allowed\_fails or allowed\_fail\_policy if set [Start here](https://docs.litellm.ai/docs/routing#advanced-custom-retries-cooldowns-based-on-error-type)

## General Proxy Improvements [​](https://docs.litellm.ai/release_notes/tags/reasoning-content\#general-proxy-improvements "Direct link to General Proxy Improvements")

1. Hypercorn - fix reading / parsing request body
2. Windows - fix running proxy in windows
3. DD-Trace - fix dd-trace enablement on proxy

## Complete Git Diff [​](https://docs.litellm.ai/release_notes/tags/reasoning-content\#complete-git-diff "Direct link to Complete Git Diff")

View the complete git diff [here](https://github.com/BerriAI/litellm/compare/v1.61.13-stable...v1.61.20-stable).

## Release Notes Overview
[Skip to main content](https://docs.litellm.ai/release_notes/tags/rerank#__docusaurus_skipToContent_fallback)

These are the changes since `v1.61.13-stable`.

This release is primarily focused on:

- LLM Translation improvements (claude-3-7-sonnet + 'thinking'/'reasoning\_content' support)
- UI improvements (add model flow, user management, etc)

## Demo Instance [​](https://docs.litellm.ai/release_notes/tags/rerank\#demo-instance "Direct link to Demo Instance")

Here's a Demo Instance to test changes:

- Instance: [https://demo.litellm.ai/](https://demo.litellm.ai/)
- Login Credentials:
  - Username: admin
  - Password: sk-1234

## New Models / Updated Models [​](https://docs.litellm.ai/release_notes/tags/rerank\#new-models--updated-models "Direct link to New Models / Updated Models")

1. Anthropic 3-7 sonnet support + cost tracking (Anthropic API + Bedrock + Vertex AI + OpenRouter)
1. Anthropic API [Start here](https://docs.litellm.ai/docs/providers/anthropic#usage---thinking--reasoning_content)
2. Bedrock API [Start here](https://docs.litellm.ai/docs/providers/bedrock#usage---thinking--reasoning-content)
3. Vertex AI API [See here](https://docs.litellm.ai/docs/providers/vertex#usage---thinking--reasoning_content)
4. OpenRouter [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L5626)
2. Gpt-4.5-preview support + cost tracking [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L79)
3. Azure AI - Phi-4 cost tracking [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L1773)
4. Claude-3.5-sonnet - vision support updated on Anthropic API [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L2888)
5. Bedrock llama vision support [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L7714)
6. Cerebras llama3.3-70b pricing [See here](https://github.com/BerriAI/litellm/blob/ba5bdce50a0b9bc822de58c03940354f19a733ed/model_prices_and_context_window.json#L2697)

## LLM Translation [​](https://docs.litellm.ai/release_notes/tags/rerank\#llm-translation "Direct link to LLM Translation")

1. Infinity Rerank - support returning documents when return\_documents=True [Start here](https://docs.litellm.ai/docs/providers/infinity#usage---returning-documents)
2. Amazon Deepseek - `<think>` param extraction into ‘reasoning\_content’ [Start here](https://docs.litellm.ai/docs/providers/bedrock#bedrock-imported-models-deepseek-deepseek-r1)
3. Amazon Titan Embeddings - filter out ‘aws\_’ params from request body [Start here](https://docs.litellm.ai/docs/providers/bedrock#bedrock-embedding)
4. Anthropic ‘thinking’ + ‘reasoning\_content’ translation support (Anthropic API, Bedrock, Vertex AI) [Start here](https://docs.litellm.ai/docs/reasoning_content)
5. VLLM - support ‘video\_url’ [Start here](https://docs.litellm.ai/docs/providers/vllm#send-video-url-to-vllm)
6. Call proxy via litellm SDK: Support `litellm_proxy/` for embedding, image\_generation, transcription, speech, rerank [Start here](https://docs.litellm.ai/docs/providers/litellm_proxy)
7. OpenAI Pass-through - allow using Assistants GET, DELETE on /openai pass through routes [Start here](https://docs.litellm.ai/docs/pass_through/openai_passthrough)
8. Message Translation - fix openai message for assistant msg if role is missing - openai allows this
9. O1/O3 - support ‘drop\_params’ for o3-mini and o1 parallel\_tool\_calls param (not supported currently) [See here](https://docs.litellm.ai/docs/completion/drop_params)

## Spend Tracking Improvements [​](https://docs.litellm.ai/release_notes/tags/rerank\#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

1. Cost tracking for rerank via Bedrock [See PR](https://github.com/BerriAI/litellm/commit/b682dc4ec8fd07acf2f4c981d2721e36ae2a49c5)
2. Anthropic pass-through - fix race condition causing cost to not be tracked [See PR](https://github.com/BerriAI/litellm/pull/8874)
3. Anthropic pass-through: Ensure accurate token counting [See PR](https://github.com/BerriAI/litellm/pull/8880)

## Management Endpoints / UI [​](https://docs.litellm.ai/release_notes/tags/rerank\#management-endpoints--ui "Direct link to Management Endpoints / UI")

01. Models Page - Allow sorting models by ‘created at’
02. Models Page - Edit Model Flow Improvements
03. Models Page - Fix Adding Azure, Azure AI Studio models on UI
04. Internal Users Page - Allow Bulk Adding Internal Users on UI
05. Internal Users Page - Allow sorting users by ‘created at’
06. Virtual Keys Page - Allow searching for UserIDs on the dropdown when assigning a user to a team [See PR](https://github.com/BerriAI/litellm/pull/8844)
07. Virtual Keys Page - allow creating a user when assigning keys to users [See PR](https://github.com/BerriAI/litellm/pull/8844)
08. Model Hub Page - fix text overflow issue [See PR](https://github.com/BerriAI/litellm/pull/8749)
09. Admin Settings Page - Allow adding MSFT SSO on UI
10. Backend - don't allow creating duplicate internal users in DB

## Helm [​](https://docs.litellm.ai/release_notes/tags/rerank\#helm "Direct link to Helm")

1. support ttlSecondsAfterFinished on the migration job - [See PR](https://github.com/BerriAI/litellm/pull/8593)
2. enhance migrations job with additional configurable properties - [See PR](https://github.com/BerriAI/litellm/pull/8636)

## Logging / Guardrail Integrations [​](https://docs.litellm.ai/release_notes/tags/rerank\#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

1. Arize Phoenix support
2. ‘No-log’ - fix ‘no-log’ param support on embedding calls

## Performance / Loadbalancing / Reliability improvements [​](https://docs.litellm.ai/release_notes/tags/rerank\#performance--loadbalancing--reliability-improvements "Direct link to Performance / Loadbalancing / Reliability improvements")

1. Single Deployment Cooldown logic - Use allowed\_fails or allowed\_fail\_policy if set [Start here](https://docs.litellm.ai/docs/routing#advanced-custom-retries-cooldowns-based-on-error-type)

## General Proxy Improvements [​](https://docs.litellm.ai/release_notes/tags/rerank\#general-proxy-improvements "Direct link to General Proxy Improvements")

1. Hypercorn - fix reading / parsing request body
2. Windows - fix running proxy in windows
3. DD-Trace - fix dd-trace enablement on proxy

## Complete Git Diff [​](https://docs.litellm.ai/release_notes/tags/rerank\#complete-git-diff "Direct link to Complete Git Diff")

View the complete git diff [here](https://github.com/BerriAI/litellm/compare/v1.61.13-stable...v1.61.20-stable).

## Responses API Release Notes
[Skip to main content](https://docs.litellm.ai/release_notes/tags/responses-api#__docusaurus_skipToContent_fallback)

## Deploy this version [​](https://docs.litellm.ai/release_notes/tags/responses-api\#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```codeBlockLines_e6Vv
docker run
-e STORE_MODEL_IN_DB=True
-p 4000:4000
ghcr.io/berriai/litellm:main-v1.67.4-stable

```

pip install litellm

```codeBlockLines_e6Vv
pip install litellm==1.67.4.post1

```

## Key Highlights [​](https://docs.litellm.ai/release_notes/tags/responses-api\#key-highlights "Direct link to Key Highlights")

- **Improved User Management**: This release enables search and filtering across users, keys, teams, and models.
- **Responses API Load Balancing**: Route requests across provider regions and ensure session continuity.
- **UI Session Logs**: Group several requests to LiteLLM into a session.

## Improved User Management [​](https://docs.litellm.ai/release_notes/tags/responses-api\#improved-user-management "Direct link to Improved User Management")

![](https://docs.litellm.ai/assets/ideal-img/ui_search_users.7472bdc.1920.png)

This release makes it easier to manage users and keys on LiteLLM. You can now search and filter across users, keys, teams, and models, and control user settings more easily.

New features include:

- Search for users by email, ID, role, or team.
- See all of a user's models, teams, and keys in one place.
- Change user roles and model access right from the Users Tab.

These changes help you spend less time on user setup and management on LiteLLM.

## Responses API Load Balancing [​](https://docs.litellm.ai/release_notes/tags/responses-api\#responses-api-load-balancing "Direct link to Responses API Load Balancing")

![](https://docs.litellm.ai/assets/ideal-img/ui_responses_lb.1e64cec.1204.png)

This release introduces load balancing for the Responses API, allowing you to route requests across provider regions and ensure session continuity. It works as follows:

- If a `previous_response_id` is provided, LiteLLM will route the request to the original deployment that generated the prior response — ensuring session continuity.
- If no `previous_response_id` is provided, LiteLLM will load-balance requests across your available deployments.

[Read more](https://docs.litellm.ai/docs/response_api#load-balancing-with-session-continuity)

## UI Session Logs [​](https://docs.litellm.ai/release_notes/tags/responses-api\#ui-session-logs "Direct link to UI Session Logs")

![](https://docs.litellm.ai/assets/ideal-img/ui_session_logs.926dffc.1920.png)

This release allow you to group requests to LiteLLM proxy into a session. If you specify a litellm\_session\_id in your request LiteLLM will automatically group all logs in the same session. This allows you to easily track usage and request content per session.

[Read more](https://docs.litellm.ai/docs/proxy/ui_logs_sessions)

## New Models / Updated Models [​](https://docs.litellm.ai/release_notes/tags/responses-api\#new-models--updated-models "Direct link to New Models / Updated Models")

- **OpenAI**
1. Added `gpt-image-1` cost tracking [Get Started](https://docs.litellm.ai/docs/image_generation)
2. Bug fix: added cost tracking for gpt-image-1 when quality is unspecified [PR](https://github.com/BerriAI/litellm/pull/10247)
- **Azure**
1. Fixed timestamp granularities passing to whisper in Azure [Get Started](https://docs.litellm.ai/docs/audio_transcription)
2. Added azure/gpt-image-1 pricing [Get Started](https://docs.litellm.ai/docs/image_generation), [PR](https://github.com/BerriAI/litellm/pull/10327)
3. Added cost tracking for `azure/computer-use-preview`, `azure/gpt-4o-audio-preview-2024-12-17`, `azure/gpt-4o-mini-audio-preview-2024-12-17` [PR](https://github.com/BerriAI/litellm/pull/10178)
- **Bedrock**
1. Added support for all compatible Bedrock parameters when model="arn:.." (Bedrock application inference profile models) [Get started](https://docs.litellm.ai/docs/providers/bedrock#bedrock-application-inference-profile), [PR](https://github.com/BerriAI/litellm/pull/10256)
2. Fixed wrong system prompt transformation [PR](https://github.com/BerriAI/litellm/pull/10120)
- **VertexAI / Google AI Studio**
1. Allow setting `budget_tokens=0` for `gemini-2.5-flash` [Get Started](https://docs.litellm.ai/docs/providers/gemini#usage---thinking--reasoning_content), [PR](https://github.com/BerriAI/litellm/pull/10198)
2. Ensure returned `usage` includes thinking token usage [PR](https://github.com/BerriAI/litellm/pull/10198)
3. Added cost tracking for `gemini-2.5-pro-preview-03-25` [PR](https://github.com/BerriAI/litellm/pull/10178)
- **Cohere**
1. Added support for cohere command-a-03-2025 [Get Started](https://docs.litellm.ai/docs/providers/cohere), [PR](https://github.com/BerriAI/litellm/pull/10295)
- **SageMaker**
1. Added support for max\_completion\_tokens parameter [Get Started](https://docs.litellm.ai/docs/providers/sagemaker), [PR](https://github.com/BerriAI/litellm/pull/10300)
- **Responses API**
1. Added support for GET and DELETE operations - `/v1/responses/{response_id}` [Get Started](https://docs.litellm.ai/docs/response_api)
2. Added session management support for all supported models [PR](https://github.com/BerriAI/litellm/pull/10321)
3. Added routing affinity to maintain model consistency within sessions [Get Started](https://docs.litellm.ai/docs/response_api#load-balancing-with-routing-affinity), [PR](https://github.com/BerriAI/litellm/pull/10193)

## Spend Tracking Improvements [​](https://docs.litellm.ai/release_notes/tags/responses-api\#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

- **Bug Fix**: Fixed spend tracking bug, ensuring default litellm params aren't modified in memory [PR](https://github.com/BerriAI/litellm/pull/10167)
- **Deprecation Dates**: Added deprecation dates for Azure, VertexAI models [PR](https://github.com/BerriAI/litellm/pull/10308)

## Management Endpoints / UI [​](https://docs.litellm.ai/release_notes/tags/responses-api\#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Users [​](https://docs.litellm.ai/release_notes/tags/responses-api\#users "Direct link to Users")

- **Filtering and Searching**:


  - Filter users by user\_id, role, team, sso\_id
  - Search users by email

![](https://docs.litellm.ai/assets/ideal-img/user_filters.e2b4a8c.1920.png)

- **User Info Panel**: Added a new user information pane [PR](https://github.com/BerriAI/litellm/pull/10213)

  - View teams, keys, models associated with User
  - Edit user role, model permissions

#### Teams [​](https://docs.litellm.ai/release_notes/tags/responses-api\#teams "Direct link to Teams")

- **Filtering and Searching**:


  - Filter teams by Organization, Team ID [PR](https://github.com/BerriAI/litellm/pull/10324)
  - Search teams by Team Name [PR](https://github.com/BerriAI/litellm/pull/10324)

![](https://docs.litellm.ai/assets/ideal-img/team_filters.c9c085b.1920.png)

#### Keys [​](https://docs.litellm.ai/release_notes/tags/responses-api\#keys "Direct link to Keys")

- **Key Management**:
  - Support for cross-filtering and filtering by key hash [PR](https://github.com/BerriAI/litellm/pull/10322)
  - Fixed key alias reset when resetting filters [PR](https://github.com/BerriAI/litellm/pull/10099)
  - Fixed table rendering on key creation [PR](https://github.com/BerriAI/litellm/pull/10224)

#### UI Logs Page [​](https://docs.litellm.ai/release_notes/tags/responses-api\#ui-logs-page "Direct link to UI Logs Page")

- **Session Logs**: Added UI Session Logs [Get Started](https://docs.litellm.ai/docs/proxy/ui_logs_sessions)

#### UI Authentication & Security [​](https://docs.litellm.ai/release_notes/tags/responses-api\#ui-authentication--security "Direct link to UI Authentication & Security")

- **Required Authentication**: Authentication now required for all dashboard pages [PR](https://github.com/BerriAI/litellm/pull/10229)
- **SSO Fixes**: Fixed SSO user login invalid token error [PR](https://github.com/BerriAI/litellm/pull/10298)
- \[BETA\] **Encrypted Tokens**: Moved UI to encrypted token usage [PR](https://github.com/BerriAI/litellm/pull/10302)
- **Token Expiry**: Support token refresh by re-routing to login page (fixes issue where expired token would show a blank page) [PR](https://github.com/BerriAI/litellm/pull/10250)

#### UI General fixes [​](https://docs.litellm.ai/release_notes/tags/responses-api\#ui-general-fixes "Direct link to UI General fixes")

- **Fixed UI Flicker**: Addressed UI flickering issues in Dashboard [PR](https://github.com/BerriAI/litellm/pull/10261)
- **Improved Terminology**: Better loading and no-data states on Keys and Tools pages [PR](https://github.com/BerriAI/litellm/pull/10253)
- **Azure Model Support**: Fixed editing Azure public model names and changing model names after creation [PR](https://github.com/BerriAI/litellm/pull/10249)
- **Team Model Selector**: Bug fix for team model selection [PR](https://github.com/BerriAI/litellm/pull/10171)

## Logging / Guardrail Integrations [​](https://docs.litellm.ai/release_notes/tags/responses-api\#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

- **Datadog**:
1. Fixed Datadog LLM observability logging [Get Started](https://docs.litellm.ai/docs/proxy/logging#datadog), [PR](https://github.com/BerriAI/litellm/pull/10206)
- **Prometheus / Grafana**:
1. Enable datasource selection on LiteLLM Grafana Template [Get Started](https://docs.litellm.ai/docs/proxy/prometheus#-litellm-maintained-grafana-dashboards-), [PR](https://github.com/BerriAI/litellm/pull/10257)
- **AgentOps**:
1. Added AgentOps Integration [Get Started](https://docs.litellm.ai/docs/observability/agentops_integration), [PR](https://github.com/BerriAI/litellm/pull/9685)
- **Arize**:
1. Added missing attributes for Arize & Phoenix Integration [Get Started](https://docs.litellm.ai/docs/observability/arize_integration), [PR](https://github.com/BerriAI/litellm/pull/10215)

## General Proxy Improvements [​](https://docs.litellm.ai/release_notes/tags/responses-api\#general-proxy-improvements "Direct link to General Proxy Improvements")

- **Caching**: Fixed caching to account for `thinking` or `reasoning_effort` when calculating cache key [PR](https://github.com/BerriAI/litellm/pull/10140)
- **Model Groups**: Fixed handling for cases where user sets model\_group inside model\_info [PR](https://github.com/BerriAI/litellm/pull/10191)
- **Passthrough Endpoints**: Ensured `PassthroughStandardLoggingPayload` is logged with method, URL, request/response body [PR](https://github.com/BerriAI/litellm/pull/10194)
- **Fix SQL Injection**: Fixed potential SQL injection vulnerability in spend\_management\_endpoints.py [PR](https://github.com/BerriAI/litellm/pull/9878)

## Helm [​](https://docs.litellm.ai/release_notes/tags/responses-api\#helm "Direct link to Helm")

- Fixed serviceAccountName on migration job [PR](https://github.com/BerriAI/litellm/pull/10258)

## Full Changelog [​](https://docs.litellm.ai/release_notes/tags/responses-api\#full-changelog "Direct link to Full Changelog")

The complete list of changes can be found in the [GitHub release notes](https://github.com/BerriAI/litellm/compare/v1.67.0-stable...v1.67.4-stable).

These are the changes since `v1.63.11-stable`.

This release brings:

- LLM Translation Improvements (MCP Support and Bedrock Application Profiles)
- Perf improvements for Usage-based Routing
- Streaming guardrail support via websockets
- Azure OpenAI client perf fix (from previous release)

## Docker Run LiteLLM Proxy [​](https://docs.litellm.ai/release_notes/tags/responses-api\#docker-run-litellm-proxy "Direct link to Docker Run LiteLLM Proxy")

```codeBlockLines_e6Vv
docker run
-e STORE_MODEL_IN_DB=True
-p 4000:4000
ghcr.io/berriai/litellm:main-v1.63.14-stable.patch1

```

## Demo Instance [​](https://docs.litellm.ai/release_notes/tags/responses-api\#demo-instance "Direct link to Demo Instance")

Here's a Demo Instance to test changes:

- Instance: [https://demo.litellm.ai/](https://demo.litellm.ai/)
- Login Credentials:
  - Username: admin
  - Password: sk-1234

## New Models / Updated Models [​](https://docs.litellm.ai/release_notes/tags/responses-api\#new-models--updated-models "Direct link to New Models / Updated Models")

- Azure gpt-4o - fixed pricing to latest global pricing - [PR](https://github.com/BerriAI/litellm/pull/9361)
- O1-Pro - add pricing + model information - [PR](https://github.com/BerriAI/litellm/pull/9397)
- Azure AI - mistral 3.1 small pricing added - [PR](https://github.com/BerriAI/litellm/pull/9453)
- Azure - gpt-4.5-preview pricing added - [PR](https://github.com/BerriAI/litellm/pull/9453)

## LLM Translation [​](https://docs.litellm.ai/release_notes/tags/responses-api\#llm-translation "Direct link to LLM Translation")

1. **New LLM Features**

- Bedrock: Support bedrock application inference profiles [Docs](https://docs.litellm.ai/docs/providers/bedrock#bedrock-application-inference-profile)
  - Infer aws region from bedrock application profile id - ( `arn:aws:bedrock:us-east-1:...`)
- Ollama - support calling via `/v1/completions` [Get Started](https://docs.litellm.ai/docs/providers/ollama#using-ollama-fim-on-v1completions)
- Bedrock - support `us.deepseek.r1-v1:0` model name [Docs](https://docs.litellm.ai/docs/providers/bedrock#supported-aws-bedrock-models)
- OpenRouter - `OPENROUTER_API_BASE` env var support [Docs](https://docs.litellm.ai/docs/providers/openrouter.md)
- Azure - add audio model parameter support - [Docs](https://docs.litellm.ai/docs/providers/azure#azure-audio-model)
- OpenAI - PDF File support [Docs](https://docs.litellm.ai/docs/completion/document_understanding#openai-file-message-type)
- OpenAI - o1-pro Responses API streaming support [Docs](https://docs.litellm.ai/docs/response_api.md#streaming)
- \[BETA\] MCP - Use MCP Tools with LiteLLM SDK [Docs](https://docs.litellm.ai/docs/mcp)

2. **Bug Fixes**

- Voyage: prompt token on embedding tracking fix - [PR](https://github.com/BerriAI/litellm/commit/56d3e75b330c3c3862dc6e1c51c1210e48f1068e)
- Sagemaker - Fix ‘Too little data for declared Content-Length’ error - [PR](https://github.com/BerriAI/litellm/pull/9326)
- OpenAI-compatible models - fix issue when calling openai-compatible models w/ custom\_llm\_provider set - [PR](https://github.com/BerriAI/litellm/pull/9355)
- VertexAI - Embedding ‘outputDimensionality’ support - [PR](https://github.com/BerriAI/litellm/commit/437dbe724620675295f298164a076cbd8019d304)
- Anthropic - return consistent json response format on streaming/non-streaming - [PR](https://github.com/BerriAI/litellm/pull/9437)

## Spend Tracking Improvements [​](https://docs.litellm.ai/release_notes/tags/responses-api\#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

- `litellm_proxy/` \- support reading litellm response cost header from proxy, when using client sdk
- Reset Budget Job - fix budget reset error on keys/teams/users [PR](https://github.com/BerriAI/litellm/pull/9329)
- Streaming - Prevents final chunk w/ usage from being ignored (impacted bedrock streaming + cost tracking) [PR](https://github.com/BerriAI/litellm/pull/9314)

## UI [​](https://docs.litellm.ai/release_notes/tags/responses-api\#ui "Direct link to UI")

1. Users Page
   - Feature: Control default internal user settings [PR](https://github.com/BerriAI/litellm/pull/9328)
2. Icons:
   - Feature: Replace external "artificialanalysis.ai" icons by local svg [PR](https://github.com/BerriAI/litellm/pull/9374)
3. Sign In/Sign Out
   - Fix: Default login when `default_user_id` user does not exist in DB [PR](https://github.com/BerriAI/litellm/pull/9395)

## Logging Integrations [​](https://docs.litellm.ai/release_notes/tags/responses-api\#logging-integrations "Direct link to Logging Integrations")

- Support post-call guardrails for streaming responses [Get Started](https://docs.litellm.ai/docs/proxy/guardrails/custom_guardrail#1-write-a-customguardrail-class)
- Arize [Get Started](https://docs.litellm.ai/docs/observability/arize_integration)
  - fix invalid package import [PR](https://github.com/BerriAI/litellm/pull/9338)
  - migrate to using standardloggingpayload for metadata, ensures spans land successfully [PR](https://github.com/BerriAI/litellm/pull/9338)
  - fix logging to just log the LLM I/O [PR](https://github.com/BerriAI/litellm/pull/9353)
  - Dynamic API Key/Space param support [Get Started](https://docs.litellm.ai/docs/observability/arize_integration#pass-arize-spacekey-per-request)
- StandardLoggingPayload - Log litellm\_model\_name in payload. Allows knowing what the model sent to API provider was [Get Started](https://docs.litellm.ai/docs/proxy/logging_spec#standardlogginghiddenparams)
- Prompt Management - Allow building custom prompt management integration [Get Started](https://docs.litellm.ai/docs/proxy/custom_prompt_management.md)

## Performance / Reliability improvements [​](https://docs.litellm.ai/release_notes/tags/responses-api\#performance--reliability-improvements "Direct link to Performance / Reliability improvements")

- Redis Caching - add 5s default timeout, prevents hanging redis connection from impacting llm calls [PR](https://github.com/BerriAI/litellm/commit/db92956ae33ed4c4e3233d7e1b0c7229817159bf)
- Allow disabling all spend updates / writes to DB - patch to allow disabling all spend updates to DB with a flag [PR](https://github.com/BerriAI/litellm/pull/9331)
- Azure OpenAI - correctly re-use azure openai client, fixes perf issue from previous Stable release [PR](https://github.com/BerriAI/litellm/commit/f2026ef907c06d94440930917add71314b901413)
- Azure OpenAI - uses litellm.ssl\_verify on Azure/OpenAI clients [PR](https://github.com/BerriAI/litellm/commit/f2026ef907c06d94440930917add71314b901413)
- Usage-based routing - Wildcard model support [Get Started](https://docs.litellm.ai/docs/proxy/usage_based_routing#wildcard-model-support)
- Usage-based routing - Support batch writing increments to redis - reduces latency to same as ‘simple-shuffle’ [PR](https://github.com/BerriAI/litellm/pull/9357)
- Router - show reason for model cooldown on ‘no healthy deployments available error’ [PR](https://github.com/BerriAI/litellm/pull/9438)
- Caching - add max value limit to an item in in-memory cache (1MB) - prevents OOM errors on large image url’s being sent through proxy [PR](https://github.com/BerriAI/litellm/pull/9448)

## General Improvements [​](https://docs.litellm.ai/release_notes/tags/responses-api\#general-improvements "Direct link to General Improvements")

- Passthrough Endpoints - support returning api-base on pass-through endpoints Response Headers [Docs](https://docs.litellm.ai/docs/proxy/response_headers#litellm-specific-headers)
- SSL - support reading ssl security level from env var - Allows user to specify lower security settings [Get Started](https://docs.litellm.ai/docs/guides/security_settings)
- Credentials - only poll Credentials table when `STORE_MODEL_IN_DB` is True [PR](https://github.com/BerriAI/litellm/pull/9376)
- Image URL Handling - new architecture doc on image url handling [Docs](https://docs.litellm.ai/docs/proxy/image_handling)
- OpenAI - bump to pip install "openai==1.68.2" [PR](https://github.com/BerriAI/litellm/commit/e85e3bc52a9de86ad85c3dbb12d87664ee567a5a)
- Gunicorn - security fix - bump gunicorn==23.0.0 [PR](https://github.com/BerriAI/litellm/commit/7e9fc92f5c7fea1e7294171cd3859d55384166eb)

## Complete Git Diff [​](https://docs.litellm.ai/release_notes/tags/responses-api\#complete-git-diff "Direct link to Complete Git Diff")

[Here's the complete git diff](https://github.com/BerriAI/litellm/compare/v1.63.11-stable...v1.63.14.rc)

These are the changes since `v1.63.2-stable`.

This release is primarily focused on:

- \[Beta\] Responses API Support
- Snowflake Cortex Support, Amazon Nova Image Generation
- UI - Credential Management, re-use credentials when adding new models
- UI - Test Connection to LLM Provider before adding a model

## Known Issues [​](https://docs.litellm.ai/release_notes/tags/responses-api\#known-issues "Direct link to Known Issues")

- 🚨 Known issue on Azure OpenAI - We don't recommend upgrading if you use Azure OpenAI. This version failed our Azure OpenAI load test

## Docker Run LiteLLM Proxy [​](https://docs.litellm.ai/release_notes/tags/responses-api\#docker-run-litellm-proxy "Direct link to Docker Run LiteLLM Proxy")

```codeBlockLines_e6Vv
docker run
-e STORE_MODEL_IN_DB=True
-p 4000:4000
ghcr.io/berriai/litellm:main-v1.63.11-stable

```

## Demo Instance [​](https://docs.litellm.ai/release_notes/tags/responses-api\#demo-instance "Direct link to Demo Instance")

Here's a Demo Instance to test changes:

- Instance: [https://demo.litellm.ai/](https://demo.litellm.ai/)
- Login Credentials:
  - Username: admin
  - Password: sk-1234

## New Models / Updated Models [​](https://docs.litellm.ai/release_notes/tags/responses-api\#new-models--updated-models "Direct link to New Models / Updated Models")

- Image Generation support for Amazon Nova Canvas [Getting Started](https://docs.litellm.ai/docs/providers/bedrock#image-generation)
- Add pricing for Jamba new models [PR](https://github.com/BerriAI/litellm/pull/9032/files)
- Add pricing for Amazon EU models [PR](https://github.com/BerriAI/litellm/pull/9056/files)
- Add Bedrock Deepseek R1 model pricing [PR](https://github.com/BerriAI/litellm/pull/9108/files)
- Update Gemini pricing: Gemma 3, Flash 2 thinking update, LearnLM [PR](https://github.com/BerriAI/litellm/pull/9190/files)
- Mark Cohere Embedding 3 models as Multimodal [PR](https://github.com/BerriAI/litellm/pull/9176/commits/c9a576ce4221fc6e50dc47cdf64ab62736c9da41)
- Add Azure Data Zone pricing [PR](https://github.com/BerriAI/litellm/pull/9185/files#diff-19ad91c53996e178c1921cbacadf6f3bae20cfe062bd03ee6bfffb72f847ee37)
  - LiteLLM Tracks cost for `azure/eu` and `azure/us` models

## LLM Translation [​](https://docs.litellm.ai/release_notes/tags/responses-api\#llm-translation "Direct link to LLM Translation")

![](https://docs.litellm.ai/assets/ideal-img/responses_api.01dd45d.1200.png)

1. **New Endpoints**

- \[Beta\] POST `/responses` API. [Getting Started](https://docs.litellm.ai/docs/response_api)

2. **New LLM Providers**

- Snowflake Cortex [Getting Started](https://docs.litellm.ai/docs/providers/snowflake)

3. **New LLM Features**

- Support OpenRouter `reasoning_content` on streaming [Getting Started](https://docs.litellm.ai/docs/reasoning_content)

4. **Bug Fixes**

- OpenAI: Return `code`, `param` and `type` on bad request error [More information on litellm exceptions](https://docs.litellm.ai/docs/exception_mapping)
- Bedrock: Fix converse chunk parsing to only return empty dict on tool use [PR](https://github.com/BerriAI/litellm/pull/9166)
- Bedrock: Support extra\_headers [PR](https://github.com/BerriAI/litellm/pull/9113)
- Azure: Fix Function Calling Bug & Update Default API Version to `2025-02-01-preview` [PR](https://github.com/BerriAI/litellm/pull/9191)
- Azure: Fix AI services URL [PR](https://github.com/BerriAI/litellm/pull/9185)
- Vertex AI: Handle HTTP 201 status code in response [PR](https://github.com/BerriAI/litellm/pull/9193)
- Perplexity: Fix incorrect streaming response [PR](https://github.com/BerriAI/litellm/pull/9081)
- Triton: Fix streaming completions bug [PR](https://github.com/BerriAI/litellm/pull/8386)
- Deepgram: Support bytes.IO when handling audio files for transcription [PR](https://github.com/BerriAI/litellm/pull/9071)
- Ollama: Fix "system" role has become unacceptable [PR](https://github.com/BerriAI/litellm/pull/9261)
- All Providers (Streaming): Fix String `data:` stripped from entire content in streamed responses [PR](https://github.com/BerriAI/litellm/pull/9070)

## Spend Tracking Improvements [​](https://docs.litellm.ai/release_notes/tags/responses-api\#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

1. Support Bedrock converse cache token tracking [Getting Started](https://docs.litellm.ai/docs/completion/prompt_caching)
2. Cost Tracking for Responses API [Getting Started](https://docs.litellm.ai/docs/response_api)
3. Fix Azure Whisper cost tracking [Getting Started](https://docs.litellm.ai/docs/audio_transcription)

## UI [​](https://docs.litellm.ai/release_notes/tags/responses-api\#ui "Direct link to UI")

### Re-Use Credentials on UI [​](https://docs.litellm.ai/release_notes/tags/responses-api\#re-use-credentials-on-ui "Direct link to Re-Use Credentials on UI")

You can now onboard LLM provider credentials on LiteLLM UI. Once these credentials are added you can re-use them when adding new models [Getting Started](https://docs.litellm.ai/docs/proxy/ui_credentials)

![](https://docs.litellm.ai/assets/ideal-img/credentials.8f19ffb.1920.jpg)

### Test Connections before adding models [​](https://docs.litellm.ai/release_notes/tags/responses-api\#test-connections-before-adding-models "Direct link to Test Connections before adding models")

Before adding a model you can test the connection to the LLM provider to verify you have setup your API Base + API Key correctly

![](https://docs.litellm.ai/assets/images/litellm_test_connection-029765a2de4dcabccfe3be9a8d33dbdd.gif)

### General UI Improvements [​](https://docs.litellm.ai/release_notes/tags/responses-api\#general-ui-improvements "Direct link to General UI Improvements")

1. Add Models Page
   - Allow adding Cerebras, Sambanova, Perplexity, Fireworks, Openrouter, TogetherAI Models, Text-Completion OpenAI on Admin UI
   - Allow adding EU OpenAI models
   - Fix: Instantly show edit + deletes to models
2. Keys Page
   - Fix: Instantly show newly created keys on Admin UI (don't require refresh)
   - Fix: Allow clicking into Top Keys when showing users Top API Key
   - Fix: Allow Filter Keys by Team Alias, Key Alias and Org
   - UI Improvements: Show 100 Keys Per Page, Use full height, increase width of key alias
3. Users Page
   - Fix: Show correct count of internal user keys on Users Page
   - Fix: Metadata not updating in Team UI
4. Logs Page
   - UI Improvements: Keep expanded log in focus on LiteLLM UI
   - UI Improvements: Minor improvements to logs page
   - Fix: Allow internal user to query their own logs
   - Allow switching off storing Error Logs in DB [Getting Started](https://docs.litellm.ai/docs/proxy/ui_logs)
5. Sign In/Sign Out
   - Fix: Correctly use `PROXY_LOGOUT_URL` when set [Getting Started](https://docs.litellm.ai/docs/proxy/self_serve#setting-custom-logout-urls)

## Security [​](https://docs.litellm.ai/release_notes/tags/responses-api\#security "Direct link to Security")

1. Support for Rotating Master Keys [Getting Started](https://docs.litellm.ai/docs/proxy/master_key_rotations)
2. Fix: Internal User Viewer Permissions, don't allow `internal_user_viewer` role to see `Test Key Page` or `Create Key Button` [More information on role based access controls](https://docs.litellm.ai/docs/proxy/access_control)
3. Emit audit logs on All user + model Create/Update/Delete endpoints [Getting Started](https://docs.litellm.ai/docs/proxy/multiple_admins)
4. JWT
   - Support multiple JWT OIDC providers [Getting Started](https://docs.litellm.ai/docs/proxy/token_auth)
   - Fix JWT access with Groups not working when team is assigned All Proxy Models access
5. Using K/V pairs in 1 AWS Secret [Getting Started](https://docs.litellm.ai/docs/secret#using-kv-pairs-in-1-aws-secret)

## Logging Integrations [​](https://docs.litellm.ai/release_notes/tags/responses-api\#logging-integrations "Direct link to Logging Integrations")

1. Prometheus: Track Azure LLM API latency metric [Getting Started](https://docs.litellm.ai/docs/proxy/prometheus#request-latency-metrics)
2. Athina: Added tags, user\_feedback and model\_options to additional\_keys which can be sent to Athina [Getting Started](https://docs.litellm.ai/docs/observability/athina_integration)

## Performance / Reliability improvements [​](https://docs.litellm.ai/release_notes/tags/responses-api\#performance--reliability-improvements "Direct link to Performance / Reliability improvements")

1. Redis + litellm router - Fix Redis cluster mode for litellm router [PR](https://github.com/BerriAI/litellm/pull/9010)

## General Improvements [​](https://docs.litellm.ai/release_notes/tags/responses-api\#general-improvements "Direct link to General Improvements")

1. OpenWebUI Integration - display `thinking` tokens

- Guide on getting started with LiteLLM x OpenWebUI. [Getting Started](https://docs.litellm.ai/docs/tutorials/openweb_ui)
- Display `thinking` tokens on OpenWebUI (Bedrock, Anthropic, Deepseek) [Getting Started](https://docs.litellm.ai/docs/tutorials/openweb_ui#render-thinking-content-on-openweb-ui)

![](https://docs.litellm.ai/assets/images/litellm_thinking_openweb-5ec7dddb7e7b6a10252694c27cfc177d.gif)

## Complete Git Diff [​](https://docs.litellm.ai/release_notes/tags/responses-api\#complete-git-diff "Direct link to Complete Git Diff")

[Here's the complete git diff](https://github.com/BerriAI/litellm/compare/v1.63.2-stable...v1.63.11-stable)

## Secret Management Updates
[Skip to main content](https://docs.litellm.ai/release_notes/tags/secret-management#__docusaurus_skipToContent_fallback)

`alerting`, `prometheus`, `secret management`, `management endpoints`, `ui`, `prompt management`, `finetuning`, `batch`

## New / Updated Models [​](https://docs.litellm.ai/release_notes/tags/secret-management\#new--updated-models "Direct link to New / Updated Models")

1. Mistral large pricing - [https://github.com/BerriAI/litellm/pull/7452](https://github.com/BerriAI/litellm/pull/7452)
2. Cohere command-r7b-12-2024 pricing - [https://github.com/BerriAI/litellm/pull/7553/files](https://github.com/BerriAI/litellm/pull/7553/files)
3. Voyage - new models, prices and context window information - [https://github.com/BerriAI/litellm/pull/7472](https://github.com/BerriAI/litellm/pull/7472)
4. Anthropic - bump Bedrock claude-3-5-haiku max\_output\_tokens to 8192

## General Proxy Improvements [​](https://docs.litellm.ai/release_notes/tags/secret-management\#general-proxy-improvements "Direct link to General Proxy Improvements")

1. Health check support for realtime models
2. Support calling Azure realtime routes via virtual keys
3. Support custom tokenizer on `/utils/token_counter` \- useful when checking token count for self-hosted models
4. Request Prioritization - support on `/v1/completion` endpoint as well

## LLM Translation Improvements [​](https://docs.litellm.ai/release_notes/tags/secret-management\#llm-translation-improvements "Direct link to LLM Translation Improvements")

1. Deepgram STT support. [Start Here](https://docs.litellm.ai/docs/providers/deepgram)
2. OpenAI Moderations - `omni-moderation-latest` support. [Start Here](https://docs.litellm.ai/docs/moderation)
3. Azure O1 - fake streaming support. This ensures if a `stream=true` is passed, the response is streamed. [Start Here](https://docs.litellm.ai/docs/providers/azure)
4. Anthropic - non-whitespace char stop sequence handling - [PR](https://github.com/BerriAI/litellm/pull/7484)
5. Azure OpenAI - support Entra ID username + password based auth. [Start Here](https://docs.litellm.ai/docs/providers/azure#entra-id---use-tenant_id-client_id-client_secret)
6. LM Studio - embedding route support. [Start Here](https://docs.litellm.ai/docs/providers/lm-studio)
7. WatsonX - ZenAPIKeyAuth support. [Start Here](https://docs.litellm.ai/docs/providers/watsonx)

## Prompt Management Improvements [​](https://docs.litellm.ai/release_notes/tags/secret-management\#prompt-management-improvements "Direct link to Prompt Management Improvements")

1. Langfuse integration
2. HumanLoop integration
3. Support for using load balanced models
4. Support for loading optional params from prompt manager

[Start Here](https://docs.litellm.ai/docs/proxy/prompt_management)

## Finetuning + Batch APIs Improvements [​](https://docs.litellm.ai/release_notes/tags/secret-management\#finetuning--batch-apis-improvements "Direct link to Finetuning + Batch APIs Improvements")

1. Improved unified endpoint support for Vertex AI finetuning - [PR](https://github.com/BerriAI/litellm/pull/7487)
2. Add support for retrieving vertex api batch jobs - [PR](https://github.com/BerriAI/litellm/commit/13f364682d28a5beb1eb1b57f07d83d5ef50cbdc)

## _NEW_ Alerting Integration [​](https://docs.litellm.ai/release_notes/tags/secret-management\#new-alerting-integration "Direct link to new-alerting-integration")

PagerDuty Alerting Integration.

Handles two types of alerts:

- High LLM API Failure Rate. Configure X fails in Y seconds to trigger an alert.
- High Number of Hanging LLM Requests. Configure X hangs in Y seconds to trigger an alert.

[Start Here](https://docs.litellm.ai/docs/proxy/pagerduty)

## Prometheus Improvements [​](https://docs.litellm.ai/release_notes/tags/secret-management\#prometheus-improvements "Direct link to Prometheus Improvements")

Added support for tracking latency/spend/tokens based on custom metrics. [Start Here](https://docs.litellm.ai/docs/proxy/prometheus#beta-custom-metrics)

## _NEW_ Hashicorp Secret Manager Support [​](https://docs.litellm.ai/release_notes/tags/secret-management\#new-hashicorp-secret-manager-support "Direct link to new-hashicorp-secret-manager-support")

Support for reading credentials + writing LLM API keys. [Start Here](https://docs.litellm.ai/docs/secret#hashicorp-vault)

## Management Endpoints / UI Improvements [​](https://docs.litellm.ai/release_notes/tags/secret-management\#management-endpoints--ui-improvements "Direct link to Management Endpoints / UI Improvements")

1. Create and view organizations + assign org admins on the Proxy UI
2. Support deleting keys by key\_alias
3. Allow assigning teams to org on UI
4. Disable using ui session token for 'test key' pane
5. Show model used in 'test key' pane
6. Support markdown output in 'test key' pane

## Helm Improvements [​](https://docs.litellm.ai/release_notes/tags/secret-management\#helm-improvements "Direct link to Helm Improvements")

1. Prevent istio injection for db migrations cron job
2. allow using migrationJob.enabled variable within job

## Logging Improvements [​](https://docs.litellm.ai/release_notes/tags/secret-management\#logging-improvements "Direct link to Logging Improvements")

1. braintrust logging: respect project\_id, add more metrics - [https://github.com/BerriAI/litellm/pull/7613](https://github.com/BerriAI/litellm/pull/7613)
2. Athina - support base url - `ATHINA_BASE_URL`
3. Lunary - Allow passing custom parent run id to LLM Calls

## Git Diff [​](https://docs.litellm.ai/release_notes/tags/secret-management\#git-diff "Direct link to Git Diff")

This is the diff between v1.56.3-stable and v1.57.8-stable.

Use this to see the changes in the codebase.

[Git Diff](https://github.com/BerriAI/litellm/compare/v1.56.3-stable...189b67760011ea313ca58b1f8bd43aa74fbd7f55)

`langfuse`, `management endpoints`, `ui`, `prometheus`, `secret management`

## Langfuse Prompt Management [​](https://docs.litellm.ai/release_notes/tags/secret-management\#langfuse-prompt-management "Direct link to Langfuse Prompt Management")

Langfuse Prompt Management is being labelled as BETA. This allows us to iterate quickly on the feedback we're receiving, and making the status clearer to users. We expect to make this feature to be stable by next month (February 2025).

Changes:

- Include the client message in the LLM API Request. (Previously only the prompt template was sent, and the client message was ignored).
- Log the prompt template in the logged request (e.g. to s3/langfuse).
- Log the 'prompt\_id' and 'prompt\_variables' in the logged request (e.g. to s3/langfuse).

[Start Here](https://docs.litellm.ai/docs/proxy/prompt_management)

## Team/Organization Management + UI Improvements [​](https://docs.litellm.ai/release_notes/tags/secret-management\#teamorganization-management--ui-improvements "Direct link to Team/Organization Management + UI Improvements")

Managing teams and organizations on the UI is now easier.

Changes:

- Support for editing user role within team on UI.
- Support updating team member role to admin via api - `/team/member_update`
- Show team admins all keys for their team.
- Add organizations with budgets
- Assign teams to orgs on the UI
- Auto-assign SSO users to teams

[Start Here](https://docs.litellm.ai/docs/proxy/self_serve)

## Hashicorp Vault Support [​](https://docs.litellm.ai/release_notes/tags/secret-management\#hashicorp-vault-support "Direct link to Hashicorp Vault Support")

We now support writing LiteLLM Virtual API keys to Hashicorp Vault.

[Start Here](https://docs.litellm.ai/docs/proxy/vault)

## Custom Prometheus Metrics [​](https://docs.litellm.ai/release_notes/tags/secret-management\#custom-prometheus-metrics "Direct link to Custom Prometheus Metrics")

Define custom prometheus metrics, and track usage/latency/no. of requests against them

This allows for more fine-grained tracking - e.g. on prompt template passed in request metadata

[Start Here](https://docs.litellm.ai/docs/proxy/prometheus#beta-custom-metrics)

## LiteLLM Security Updates
[Skip to main content](https://docs.litellm.ai/release_notes/tags/security#__docusaurus_skipToContent_fallback)

## Deploy this version [​](https://docs.litellm.ai/release_notes/tags/security\#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```codeBlockLines_e6Vv
docker run
-e STORE_MODEL_IN_DB=True
-p 4000:4000
ghcr.io/berriai/litellm:main-v1.67.4-stable

```

pip install litellm

```codeBlockLines_e6Vv
pip install litellm==1.67.4.post1

```

## Key Highlights [​](https://docs.litellm.ai/release_notes/tags/security\#key-highlights "Direct link to Key Highlights")

- **Improved User Management**: This release enables search and filtering across users, keys, teams, and models.
- **Responses API Load Balancing**: Route requests across provider regions and ensure session continuity.
- **UI Session Logs**: Group several requests to LiteLLM into a session.

## Improved User Management [​](https://docs.litellm.ai/release_notes/tags/security\#improved-user-management "Direct link to Improved User Management")

![](https://docs.litellm.ai/assets/ideal-img/ui_search_users.7472bdc.1920.png)

This release makes it easier to manage users and keys on LiteLLM. You can now search and filter across users, keys, teams, and models, and control user settings more easily.

New features include:

- Search for users by email, ID, role, or team.
- See all of a user's models, teams, and keys in one place.
- Change user roles and model access right from the Users Tab.

These changes help you spend less time on user setup and management on LiteLLM.

## Responses API Load Balancing [​](https://docs.litellm.ai/release_notes/tags/security\#responses-api-load-balancing "Direct link to Responses API Load Balancing")

![](https://docs.litellm.ai/assets/ideal-img/ui_responses_lb.1e64cec.1204.png)

This release introduces load balancing for the Responses API, allowing you to route requests across provider regions and ensure session continuity. It works as follows:

- If a `previous_response_id` is provided, LiteLLM will route the request to the original deployment that generated the prior response — ensuring session continuity.
- If no `previous_response_id` is provided, LiteLLM will load-balance requests across your available deployments.

[Read more](https://docs.litellm.ai/docs/response_api#load-balancing-with-session-continuity)

## UI Session Logs [​](https://docs.litellm.ai/release_notes/tags/security\#ui-session-logs "Direct link to UI Session Logs")

![](https://docs.litellm.ai/assets/ideal-img/ui_session_logs.926dffc.1920.png)

This release allow you to group requests to LiteLLM proxy into a session. If you specify a litellm\_session\_id in your request LiteLLM will automatically group all logs in the same session. This allows you to easily track usage and request content per session.

[Read more](https://docs.litellm.ai/docs/proxy/ui_logs_sessions)

## New Models / Updated Models [​](https://docs.litellm.ai/release_notes/tags/security\#new-models--updated-models "Direct link to New Models / Updated Models")

- **OpenAI**
1. Added `gpt-image-1` cost tracking [Get Started](https://docs.litellm.ai/docs/image_generation)
2. Bug fix: added cost tracking for gpt-image-1 when quality is unspecified [PR](https://github.com/BerriAI/litellm/pull/10247)
- **Azure**
1. Fixed timestamp granularities passing to whisper in Azure [Get Started](https://docs.litellm.ai/docs/audio_transcription)
2. Added azure/gpt-image-1 pricing [Get Started](https://docs.litellm.ai/docs/image_generation), [PR](https://github.com/BerriAI/litellm/pull/10327)
3. Added cost tracking for `azure/computer-use-preview`, `azure/gpt-4o-audio-preview-2024-12-17`, `azure/gpt-4o-mini-audio-preview-2024-12-17` [PR](https://github.com/BerriAI/litellm/pull/10178)
- **Bedrock**
1. Added support for all compatible Bedrock parameters when model="arn:.." (Bedrock application inference profile models) [Get started](https://docs.litellm.ai/docs/providers/bedrock#bedrock-application-inference-profile), [PR](https://github.com/BerriAI/litellm/pull/10256)
2. Fixed wrong system prompt transformation [PR](https://github.com/BerriAI/litellm/pull/10120)
- **VertexAI / Google AI Studio**
1. Allow setting `budget_tokens=0` for `gemini-2.5-flash` [Get Started](https://docs.litellm.ai/docs/providers/gemini#usage---thinking--reasoning_content), [PR](https://github.com/BerriAI/litellm/pull/10198)
2. Ensure returned `usage` includes thinking token usage [PR](https://github.com/BerriAI/litellm/pull/10198)
3. Added cost tracking for `gemini-2.5-pro-preview-03-25` [PR](https://github.com/BerriAI/litellm/pull/10178)
- **Cohere**
1. Added support for cohere command-a-03-2025 [Get Started](https://docs.litellm.ai/docs/providers/cohere), [PR](https://github.com/BerriAI/litellm/pull/10295)
- **SageMaker**
1. Added support for max\_completion\_tokens parameter [Get Started](https://docs.litellm.ai/docs/providers/sagemaker), [PR](https://github.com/BerriAI/litellm/pull/10300)
- **Responses API**
1. Added support for GET and DELETE operations - `/v1/responses/{response_id}` [Get Started](https://docs.litellm.ai/docs/response_api)
2. Added session management support for all supported models [PR](https://github.com/BerriAI/litellm/pull/10321)
3. Added routing affinity to maintain model consistency within sessions [Get Started](https://docs.litellm.ai/docs/response_api#load-balancing-with-routing-affinity), [PR](https://github.com/BerriAI/litellm/pull/10193)

## Spend Tracking Improvements [​](https://docs.litellm.ai/release_notes/tags/security\#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

- **Bug Fix**: Fixed spend tracking bug, ensuring default litellm params aren't modified in memory [PR](https://github.com/BerriAI/litellm/pull/10167)
- **Deprecation Dates**: Added deprecation dates for Azure, VertexAI models [PR](https://github.com/BerriAI/litellm/pull/10308)

## Management Endpoints / UI [​](https://docs.litellm.ai/release_notes/tags/security\#management-endpoints--ui "Direct link to Management Endpoints / UI")

#### Users [​](https://docs.litellm.ai/release_notes/tags/security\#users "Direct link to Users")

- **Filtering and Searching**:


  - Filter users by user\_id, role, team, sso\_id
  - Search users by email

![](https://docs.litellm.ai/assets/ideal-img/user_filters.e2b4a8c.1920.png)

- **User Info Panel**: Added a new user information pane [PR](https://github.com/BerriAI/litellm/pull/10213)

  - View teams, keys, models associated with User
  - Edit user role, model permissions

#### Teams [​](https://docs.litellm.ai/release_notes/tags/security\#teams "Direct link to Teams")

- **Filtering and Searching**:


  - Filter teams by Organization, Team ID [PR](https://github.com/BerriAI/litellm/pull/10324)
  - Search teams by Team Name [PR](https://github.com/BerriAI/litellm/pull/10324)

![](https://docs.litellm.ai/assets/ideal-img/team_filters.c9c085b.1920.png)

#### Keys [​](https://docs.litellm.ai/release_notes/tags/security\#keys "Direct link to Keys")

- **Key Management**:
  - Support for cross-filtering and filtering by key hash [PR](https://github.com/BerriAI/litellm/pull/10322)
  - Fixed key alias reset when resetting filters [PR](https://github.com/BerriAI/litellm/pull/10099)
  - Fixed table rendering on key creation [PR](https://github.com/BerriAI/litellm/pull/10224)

#### UI Logs Page [​](https://docs.litellm.ai/release_notes/tags/security\#ui-logs-page "Direct link to UI Logs Page")

- **Session Logs**: Added UI Session Logs [Get Started](https://docs.litellm.ai/docs/proxy/ui_logs_sessions)

#### UI Authentication & Security [​](https://docs.litellm.ai/release_notes/tags/security\#ui-authentication--security "Direct link to UI Authentication & Security")

- **Required Authentication**: Authentication now required for all dashboard pages [PR](https://github.com/BerriAI/litellm/pull/10229)
- **SSO Fixes**: Fixed SSO user login invalid token error [PR](https://github.com/BerriAI/litellm/pull/10298)
- \[BETA\] **Encrypted Tokens**: Moved UI to encrypted token usage [PR](https://github.com/BerriAI/litellm/pull/10302)
- **Token Expiry**: Support token refresh by re-routing to login page (fixes issue where expired token would show a blank page) [PR](https://github.com/BerriAI/litellm/pull/10250)

#### UI General fixes [​](https://docs.litellm.ai/release_notes/tags/security\#ui-general-fixes "Direct link to UI General fixes")

- **Fixed UI Flicker**: Addressed UI flickering issues in Dashboard [PR](https://github.com/BerriAI/litellm/pull/10261)
- **Improved Terminology**: Better loading and no-data states on Keys and Tools pages [PR](https://github.com/BerriAI/litellm/pull/10253)
- **Azure Model Support**: Fixed editing Azure public model names and changing model names after creation [PR](https://github.com/BerriAI/litellm/pull/10249)
- **Team Model Selector**: Bug fix for team model selection [PR](https://github.com/BerriAI/litellm/pull/10171)

## Logging / Guardrail Integrations [​](https://docs.litellm.ai/release_notes/tags/security\#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

- **Datadog**:
1. Fixed Datadog LLM observability logging [Get Started](https://docs.litellm.ai/docs/proxy/logging#datadog), [PR](https://github.com/BerriAI/litellm/pull/10206)
- **Prometheus / Grafana**:
1. Enable datasource selection on LiteLLM Grafana Template [Get Started](https://docs.litellm.ai/docs/proxy/prometheus#-litellm-maintained-grafana-dashboards-), [PR](https://github.com/BerriAI/litellm/pull/10257)
- **AgentOps**:
1. Added AgentOps Integration [Get Started](https://docs.litellm.ai/docs/observability/agentops_integration), [PR](https://github.com/BerriAI/litellm/pull/9685)
- **Arize**:
1. Added missing attributes for Arize & Phoenix Integration [Get Started](https://docs.litellm.ai/docs/observability/arize_integration), [PR](https://github.com/BerriAI/litellm/pull/10215)

## General Proxy Improvements [​](https://docs.litellm.ai/release_notes/tags/security\#general-proxy-improvements "Direct link to General Proxy Improvements")

- **Caching**: Fixed caching to account for `thinking` or `reasoning_effort` when calculating cache key [PR](https://github.com/BerriAI/litellm/pull/10140)
- **Model Groups**: Fixed handling for cases where user sets model\_group inside model\_info [PR](https://github.com/BerriAI/litellm/pull/10191)
- **Passthrough Endpoints**: Ensured `PassthroughStandardLoggingPayload` is logged with method, URL, request/response body [PR](https://github.com/BerriAI/litellm/pull/10194)
- **Fix SQL Injection**: Fixed potential SQL injection vulnerability in spend\_management\_endpoints.py [PR](https://github.com/BerriAI/litellm/pull/9878)

## Helm [​](https://docs.litellm.ai/release_notes/tags/security\#helm "Direct link to Helm")

- Fixed serviceAccountName on migration job [PR](https://github.com/BerriAI/litellm/pull/10258)

## Full Changelog [​](https://docs.litellm.ai/release_notes/tags/security\#full-changelog "Direct link to Full Changelog")

The complete list of changes can be found in the [GitHub release notes](https://github.com/BerriAI/litellm/compare/v1.67.0-stable...v1.67.4-stable).

## Key Highlights [​](https://docs.litellm.ai/release_notes/tags/security\#key-highlights "Direct link to Key Highlights")

- **SCIM Integration**: Enables identity providers (Okta, Azure AD, OneLogin, etc.) to automate user and team (group) provisioning, updates, and deprovisioning
- **Team and Tag based usage tracking**: You can now see usage and spend by team and tag at 1M+ spend logs.
- **Unified Responses API**: Support for calling Anthropic, Gemini, Groq, etc. via OpenAI's new Responses API.

Let's dive in.

## SCIM Integration [​](https://docs.litellm.ai/release_notes/tags/security\#scim-integration "Direct link to SCIM Integration")

![](https://docs.litellm.ai/assets/ideal-img/scim_integration.01959e2.1200.png)

This release adds SCIM support to LiteLLM. This allows your SSO provider (Okta, Azure AD, etc) to automatically create/delete users, teams, and memberships on LiteLLM. This means that when you remove a team on your SSO provider, your SSO provider will automatically delete the corresponding team on LiteLLM.

[Read more](https://docs.litellm.ai/docs/tutorials/scim_litellm)

## Team and Tag based usage tracking [​](https://docs.litellm.ai/release_notes/tags/security\#team-and-tag-based-usage-tracking "Direct link to Team and Tag based usage tracking")

![](https://docs.litellm.ai/assets/ideal-img/new_team_usage_highlight.60482cc.1920.jpg)

This release improves team and tag based usage tracking at 1m+ spend logs, making it easy to monitor your LLM API Spend in production. This covers:

- View **daily spend** by teams + tags
- View **usage / spend by key**, within teams
- View **spend by multiple tags**
- Allow **internal users** to view spend of teams they're a member of

[Read more](https://docs.litellm.ai/release_notes/tags/security#management-endpoints--ui)

## Unified Responses API [​](https://docs.litellm.ai/release_notes/tags/security\#unified-responses-api "Direct link to Unified Responses API")

This release allows you to call Azure OpenAI, Anthropic, AWS Bedrock, and Google Vertex AI models via the POST /v1/responses endpoint on LiteLLM. This means you can now use popular tools like [OpenAI Codex](https://docs.litellm.ai/docs/tutorials/openai_codex) with your own models.

![](https://docs.litellm.ai/assets/ideal-img/unified_responses_api_rn.0acc91a.1920.png)

[Read more](https://docs.litellm.ai/docs/response_api)

## New Models / Updated Models [​](https://docs.litellm.ai/release_notes/tags/security\#new-models--updated-models "Direct link to New Models / Updated Models")

- **OpenAI**
1. gpt-4.1, gpt-4.1-mini, gpt-4.1-nano, o3, o3-mini, o4-mini pricing - [Get Started](https://docs.litellm.ai/docs/providers/openai#usage), [PR](https://github.com/BerriAI/litellm/pull/9990)
2. o4 - correctly map o4 to openai o\_series model
- **Azure AI**
1. Phi-4 output cost per token fix - [PR](https://github.com/BerriAI/litellm/pull/9880)
2. Responses API support [Get Started](https://docs.litellm.ai/docs/providers/azure#azure-responses-api), [PR](https://github.com/BerriAI/litellm/pull/10116)
- **Anthropic**
1. redacted message thinking support - [Get Started](https://docs.litellm.ai/docs/providers/anthropic#usage---thinking--reasoning_content), [PR](https://github.com/BerriAI/litellm/pull/10129)
- **Cohere**
1. `/v2/chat` Passthrough endpoint support w/ cost tracking - [Get Started](https://docs.litellm.ai/docs/pass_through/cohere), [PR](https://github.com/BerriAI/litellm/pull/9997)
- **Azure**
1. Support azure tenant\_id/client\_id env vars - [Get Started](https://docs.litellm.ai/docs/providers/azure#entra-id---use-tenant_id-client_id-client_secret), [PR](https://github.com/BerriAI/litellm/pull/9993)
2. Fix response\_format check for 2025+ api versions - [PR](https://github.com/BerriAI/litellm/pull/9993)
3. Add gpt-4.1, gpt-4.1-mini, gpt-4.1-nano, o3, o3-mini, o4-mini pricing
- **VLLM**
1. Files - Support 'file' message type for VLLM video url's - [Get Started](https://docs.litellm.ai/docs/providers/vllm#send-video-url-to-vllm), [PR](https://github.com/BerriAI/litellm/pull/10129)
2. Passthrough - new `/vllm/` passthrough endpoint support [Get Started](https://docs.litellm.ai/docs/pass_through/vllm), [PR](https://github.com/BerriAI/litellm/pull/10002)
- **Mistral**
1. new `/mistral` passthrough endpoint support [Get Started](https://docs.litellm.ai/docs/pass_through/mistral), [PR](https://github.com/BerriAI/litellm/pull/10002)
- **AWS**
1. New mapped bedrock regions - [PR](https://github.com/BerriAI/litellm/pull/9430)
- **VertexAI / Google AI Studio**
1. Gemini - Response format - Retain schema field ordering for google gemini and vertex by specifying propertyOrdering - [Get Started](https://docs.litellm.ai/docs/providers/vertex#json-schema), [PR](https://github.com/BerriAI/litellm/pull/9828)
2. Gemini-2.5-flash - return reasoning content [Google AI Studio](https://docs.litellm.ai/docs/providers/gemini#usage---thinking--reasoning_content), [Vertex AI](https://docs.litellm.ai/docs/providers/vertex#thinking--reasoning_content)
3. Gemini-2.5-flash - pricing + model information [PR](https://github.com/BerriAI/litellm/pull/10125)
4. Passthrough - new `/vertex_ai/discovery` route - enables calling AgentBuilder API routes [Get Started](https://docs.litellm.ai/docs/pass_through/vertex_ai#supported-api-endpoints), [PR](https://github.com/BerriAI/litellm/pull/10084)
- **Fireworks AI**
1. return tool calling responses in `tool_calls` field (fireworks incorrectly returns this as a json str in content) [PR](https://github.com/BerriAI/litellm/pull/10130)
- **Triton**
1. Remove fixed remove bad\_words / stop words from `/generate` call - [Get Started](https://docs.litellm.ai/docs/providers/triton-inference-server#triton-generate---chat-completion), [PR](https://github.com/BerriAI/litellm/pull/10163)
- **Other**
1. Support for all litellm providers on Responses API (works with Codex) - [Get Started](https://docs.litellm.ai/docs/tutorials/openai_codex), [PR](https://github.com/BerriAI/litellm/pull/10132)
2. Fix combining multiple tool calls in streaming response - [Get Started](https://docs.litellm.ai/docs/completion/stream#helper-function), [PR](https://github.com/BerriAI/litellm/pull/10040)

## Spend Tracking Improvements [​](https://docs.litellm.ai/release_notes/tags/security\#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

- **Cost Control** \- inject cache control points in prompt for cost reduction [Get Started](https://docs.litellm.ai/docs/tutorials/prompt_caching), [PR](https://github.com/BerriAI/litellm/pull/10000)
- **Spend Tags** \- spend tags in headers - support x-litellm-tags even if tag based routing not enabled [Get Started](https://docs.litellm.ai/docs/proxy/request_headers#litellm-headers), [PR](https://github.com/BerriAI/litellm/pull/10000)
- **Gemini-2.5-flash** \- support cost calculation for reasoning tokens [PR](https://github.com/BerriAI/litellm/pull/10141)

## Management Endpoints / UI [​](https://docs.litellm.ai/release_notes/tags/security\#management-endpoints--ui "Direct link to Management Endpoints / UI")

- **Users**

1. Show created\_at and updated\_at on users page - [PR](https://github.com/BerriAI/litellm/pull/10033)
- **Virtual Keys**

1. Filter by key alias - [https://github.com/BerriAI/litellm/pull/10085](https://github.com/BerriAI/litellm/pull/10085)
- **Usage Tab**

1. Team based usage


     - New `LiteLLM_DailyTeamSpend` Table for aggregate team based usage logging - [PR](https://github.com/BerriAI/litellm/pull/10039)

     - New Team based usage dashboard + new `/team/daily/activity` API - [PR](https://github.com/BerriAI/litellm/pull/10081)

     - Return team alias on /team/daily/activity API - [PR](https://github.com/BerriAI/litellm/pull/10157)

     - allow internal user view spend for teams they belong to - [PR](https://github.com/BerriAI/litellm/pull/10157)

     - allow viewing top keys by team - [PR](https://github.com/BerriAI/litellm/pull/10157)


![](https://docs.litellm.ai/assets/ideal-img/new_team_usage.9237b43.1754.png)

2. Tag Based Usage

     - New `LiteLLM_DailyTagSpend` Table for aggregate tag based usage logging - [PR](https://github.com/BerriAI/litellm/pull/10071)
     - Restrict to only Proxy Admins - [PR](https://github.com/BerriAI/litellm/pull/10157)
     - allow viewing top keys by tag
     - Return tags passed in request (i.e. dynamic tags) on `/tag/list` API - [PR](https://github.com/BerriAI/litellm/pull/10157)
       ![](https://docs.litellm.ai/assets/ideal-img/new_tag_usage.cd55b64.1863.png)
3. Track prompt caching metrics in daily user, team, tag tables - [PR](https://github.com/BerriAI/litellm/pull/10029)

4. Show usage by key (on all up, team, and tag usage dashboards) - [PR](https://github.com/BerriAI/litellm/pull/10157)

5. swap old usage with new usage tab
- **Models**

1. Make columns resizable/hideable - [PR](https://github.com/BerriAI/litellm/pull/10119)
- **API Playground**

1. Allow internal user to call api playground - [PR](https://github.com/BerriAI/litellm/pull/10157)
- **SCIM**

1. Add LiteLLM SCIM Integration for Team and User management - [Get Started](https://docs.litellm.ai/docs/tutorials/scim_litellm), [PR](https://github.com/BerriAI/litellm/pull/10072)

## Logging / Guardrail Integrations [​](https://docs.litellm.ai/release_notes/tags/security\#logging--guardrail-integrations "Direct link to Logging / Guardrail Integrations")

- **GCS**
1. Fix gcs pub sub logging with env var GCS\_PROJECT\_ID - [Get Started](https://docs.litellm.ai/docs/observability/gcs_bucket_integration#usage), [PR](https://github.com/BerriAI/litellm/pull/10042)
- **AIM**
1. Add litellm call id passing to Aim guardrails on pre and post-hooks calls - [Get Started](https://docs.litellm.ai/docs/proxy/guardrails/aim_security), [PR](https://github.com/BerriAI/litellm/pull/10021)
- **Azure blob storage**
1. Ensure logging works in high throughput scenarios - [Get Started](https://docs.litellm.ai/docs/proxy/logging#azure-blob-storage), [PR](https://github.com/BerriAI/litellm/pull/9962)

## General Proxy Improvements [​](https://docs.litellm.ai/release_notes/tags/security\#general-proxy-improvements "Direct link to General Proxy Improvements")

- **Support setting `litellm.modify_params` via env var** [PR](https://github.com/BerriAI/litellm/pull/9964)
- **Model Discovery** \- Check provider’s `/models` endpoints when calling proxy’s `/v1/models` endpoint - [Get Started](https://docs.litellm.ai/docs/proxy/model_discovery), [PR](https://github.com/BerriAI/litellm/pull/9958)
- **`/utils/token_counter`** \- fix retrieving custom tokenizer for db models - [Get Started](https://docs.litellm.ai/docs/proxy/configs#set-custom-tokenizer), [PR](https://github.com/BerriAI/litellm/pull/10047)
- **Prisma migrate** \- handle existing columns in db table - [PR](https://github.com/BerriAI/litellm/pull/10138)

## Deploy this version [​](https://docs.litellm.ai/release_notes/tags/security\#deploy-this-version "Direct link to Deploy this version")

- Docker
- Pip

docker run litellm

```codeBlockLines_e6Vv
docker run
-e STORE_MODEL_IN_DB=True
-p 4000:4000
ghcr.io/berriai/litellm:main-v1.66.0-stable

```

pip install litellm

```codeBlockLines_e6Vv
pip install litellm==1.66.0.post1

```

v1.66.0-stable is live now, here are the key highlights of this release

## Key Highlights [​](https://docs.litellm.ai/release_notes/tags/security\#key-highlights "Direct link to Key Highlights")

- **Realtime API Cost Tracking**: Track cost of realtime API calls
- **Microsoft SSO Auto-sync**: Auto-sync groups and group members from Azure Entra ID to LiteLLM
- **xAI grok-3**: Added support for `xai/grok-3` models
- **Security Fixes**: Fixed [CVE-2025-0330](https://www.cve.org/CVERecord?id=CVE-2025-0330) and [CVE-2024-6825](https://www.cve.org/CVERecord?id=CVE-2024-6825) vulnerabilities

Let's dive in.

## Realtime API Cost Tracking [​](https://docs.litellm.ai/release_notes/tags/security\#realtime-api-cost-tracking "Direct link to Realtime API Cost Tracking")

![](https://docs.litellm.ai/assets/ideal-img/realtime_api.960b38e.1920.png)

This release adds Realtime API logging + cost tracking.

- **Logging**: LiteLLM now logs the complete response from realtime calls to all logging integrations (DB, S3, Langfuse, etc.)
- **Cost Tracking**: You can now set 'base\_model' and custom pricing for realtime models. [Custom Pricing](https://docs.litellm.ai/docs/proxy/custom_pricing)
- **Budgets**: Your key/user/team budgets now work for realtime models as well.

Start [here](https://docs.litellm.ai/docs/realtime)

## Microsoft SSO Auto-sync [​](https://docs.litellm.ai/release_notes/tags/security\#microsoft-sso-auto-sync "Direct link to Microsoft SSO Auto-sync")

![](https://docs.litellm.ai/assets/ideal-img/sso_sync.2f79062.1414.png)

Auto-sync groups and members from Azure Entra ID to LiteLLM

This release adds support for auto-syncing groups and members on Microsoft Entra ID with LiteLLM. This means that LiteLLM proxy administrators can spend less time managing teams and members and LiteLLM handles the following:

- Auto-create teams that exist on Microsoft Entra ID
- Sync team members on Microsoft Entra ID with LiteLLM teams

Get started with this [here](https://docs.litellm.ai/docs/tutorials/msft_sso)

## New Models / Updated Models [​](https://docs.litellm.ai/release_notes/tags/security\#new-models--updated-models "Direct link to New Models / Updated Models")

- **xAI**

1. Added reasoning\_effort support for `xai/grok-3-mini-beta` [Get Started](https://docs.litellm.ai/docs/providers/xai#reasoning-usage)
2. Added cost tracking for `xai/grok-3` models [PR](https://github.com/BerriAI/litellm/pull/9920)
- **Hugging Face**

1. Added inference providers support [Get Started](https://docs.litellm.ai/docs/providers/huggingface#serverless-inference-providers)
- **Azure**

1. Added azure/gpt-4o-realtime-audio cost tracking [PR](https://github.com/BerriAI/litellm/pull/9893)
- **VertexAI**

1. Added enterpriseWebSearch tool support [Get Started](https://docs.litellm.ai/docs/providers/vertex#grounding---web-search)
2. Moved to only passing keys accepted by the Vertex AI response schema [PR](https://github.com/BerriAI/litellm/pull/8992)
- **Google AI Studio**

1. Added cost tracking for `gemini-2.5-pro` [PR](https://github.com/BerriAI/litellm/pull/9837)
2. Fixed pricing for 'gemini/gemini-2.5-pro-preview-03-25' [PR](https://github.com/BerriAI/litellm/pull/9896)
3. Fixed handling file\_data being passed in [PR](https://github.com/BerriAI/litellm/pull/9786)
- **Azure**

1. Updated Azure Phi-4 pricing [PR](https://github.com/BerriAI/litellm/pull/9862)
2. Added azure/gpt-4o-realtime-audio cost tracking [PR](https://github.com/BerriAI/litellm/pull/9893)
- **Databricks**

1. Removed reasoning\_effort from parameters [PR](https://github.com/BerriAI/litellm/pull/9811)
2. Fixed custom endpoint check for Databricks [PR](https://github.com/BerriAI/litellm/pull/9925)
- **General**

1. Added litellm.supports\_reasoning() util to track if an llm supports reasoning [Get Started](https://docs.litellm.ai/docs/providers/anthropic#reasoning)
2. Function Calling - Handle pydantic base model in message tool calls, handle tools = \[\], and support fake streaming on tool calls for meta.llama3-3-70b-instruct-v1:0 [PR](https://github.com/BerriAI/litellm/pull/9774)
3. LiteLLM Proxy - Allow passing `thinking` param to litellm proxy via client sdk [PR](https://github.com/BerriAI/litellm/pull/9386)
4. Fixed correctly translating 'thinking' param for litellm [PR](https://github.com/BerriAI/litellm/pull/9904)

## Spend Tracking Improvements [​](https://docs.litellm.ai/release_notes/tags/security\#spend-tracking-improvements "Direct link to Spend Tracking Improvements")

- **OpenAI, Azure**
1. Realtime API Cost tracking with token usage metrics in spend logs [Get Started](https://docs.litellm.ai/docs/realtime)
- **Anthropic**
1. Fixed Claude Haiku cache read pricing per token [PR](https://github.com/BerriAI/litellm/pull/9834)
2. Added cost tracking for Claude responses with base\_model [PR](https://github.com/BerriAI/litellm/pull/9897)
3. Fixed Anthropic prompt caching cost calculation and trimmed logged message in db [PR](https://github.com/BerriAI/litellm/pull/9838)
- **General**
1. Added token tracking and log usage object in spend logs [PR](https://github.com/BerriAI/litellm/pull/9843)
2. Handle custom pricing at deployment level [PR](https://github.com/BerriAI/litellm/pull/9855)

## Management Endpoints / UI [​](https://docs.litellm.ai/release_notes/tags/security\#management-endpoints--ui "Direct link to Management Endpoints / UI")

- **Test Key Tab**

1. Added rendering of Reasoning content, ttft, usage metrics on test key page [PR](https://github.com/BerriAI/litellm/pull/9931)

     ![](https://docs.litellm.ai/assets/ideal-img/chat_metrics.c59fcfe.1920.png)

     View input, output, reasoning tokens, ttft metrics.
- **Tag / Policy Management**

1. Added Tag/Policy Management. Create routing rules based on request metadata. This allows you to enforce that requests with `tags="private"` only go to specific models. [Get Started](https://docs.litellm.ai/docs/tutorials/tag_management)



     ![](https://docs.litellm.ai/assets/ideal-img/tag_management.5bf985c.1920.png)

     Create and manage tags.
- **Redesigned Login Screen**

1. Polished login screen [PR](https://github.com/BerriAI/litellm/pull/9778)
- **Microsoft SSO Auto-Sync**

1. Added debug route to allow admins to debug SSO JWT fields [PR](https://github.com/BerriAI/litellm/pull/9835)
2. Added ability to use MSFT Graph API to assign users to teams [PR](https://github.com/BerriAI/litellm/pull/9865)
3. Connected litellm to Azure Entra ID Enterprise Application [PR](https://github.com/BerriAI/litellm/pull/9872)
4. Added ability for admins to set `default_team_params` for when litellm SSO creates default teams [PR](https://github.com/BerriAI/litellm/pull/9895)
5. Fixed MSFT SSO to use correct field for user email [PR](https://github.com/BerriAI/litellm/pull/9886)
6. Added UI support for setting Default Team setting when litellm SSO auto creates teams [PR](https://github.com/BerriAI/litellm/pull/9918)
- **UI Bug Fixes**

1. Prevented team, key, org, model numerical values changing on scrolling [PR](https://github.com/BerriAI/litellm/pull/9776)
2. Instantly reflect key and team updates in UI [PR](https://github.com/BerriAI/litellm/pull/9825)

## Logging / Guardrail Improvements [​](https://docs.litellm.ai/release_notes/tags/security\#logging--guardrail-improvements "Direct link to Logging / Guardrail Improvements")

- **Prometheus**
1. Emit Key and Team Budget metrics on a cron job schedule [Get Started](https://docs.litellm.ai/docs/proxy/prometheus#initialize-budget-metrics-on-startup)

## Security Fixes [​](https://docs.litellm.ai/release_notes/tags/security\#security-fixes "Direct link to Security Fixes")

- Fixed [CVE-2025-0330](https://www.cve.org/CVERecord?id=CVE-2025-0330) \- Leakage of Langfuse API keys in team exception handling [PR](https://github.com/BerriAI/litellm/pull/9830)
- Fixed [CVE-2024-6825](https://www.cve.org/CVERecord?id=CVE-2024-6825) \- Remote code execution in post call rules [PR](https://github.com/BerriAI/litellm/pull/9826)

## Helm [​](https://docs.litellm.ai/release_notes/tags/security\#helm "Direct link to Helm")

- Added service annotations to litellm-helm chart [PR](https://github.com/BerriAI/litellm/pull/9840)
- Added extraEnvVars to the helm deployment [PR](https://github.com/BerriAI/litellm/pull/9292)

## Demo [​](https://docs.litellm.ai/release_notes/tags/security\#demo "Direct link to Demo")

Try this on the demo instance [today](https://docs.litellm.ai/docs/proxy/demo)

## Complete Git Diff [​](https://docs.litellm.ai/release_notes/tags/security\#complete-git-diff "Direct link to Complete Git Diff")

See the complete git diff since v1.65.4-stable, [here](https://github.com/BerriAI/litellm/releases/tag/v1.66.0-stable)

`docker image`, `security`, `vulnerability`