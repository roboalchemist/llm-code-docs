# Install dependencies - CHANGE THIS to `apk`
RUN apt-get update && apt-get install -y dumb-init

```

Before Change

```codeBlockLines_e6Vv
RUN apt-get update && apt-get install -y dumb-init

```

After Change

```codeBlockLines_e6Vv
RUN apk update && apk add --no-cache dumb-init

```

## LiteLLM Release Notes
[Skip to main content](https://docs.litellm.ai/release_notes/tags/fallbacks#__docusaurus_skipToContent_fallback)

A new LiteLLM Stable release [just went out](https://github.com/BerriAI/litellm/releases/tag/v1.55.8-stable). Here are 5 updates since v1.52.2-stable.

`langfuse`, `fallbacks`, `new models`, `azure_storage`

## Langfuse Prompt Management [​](https://docs.litellm.ai/release_notes/tags/fallbacks\#langfuse-prompt-management "Direct link to Langfuse Prompt Management")

This makes it easy to run experiments or change the specific models `gpt-4o` to `gpt-4o-mini` on Langfuse, instead of making changes in your applications. [Start here](https://docs.litellm.ai/docs/proxy/prompt_management)

## Control fallback prompts client-side [​](https://docs.litellm.ai/release_notes/tags/fallbacks\#control-fallback-prompts-client-side "Direct link to Control fallback prompts client-side")

> Claude prompts are different than OpenAI

Pass in prompts specific to model when doing fallbacks. [Start here](https://docs.litellm.ai/docs/proxy/reliability#control-fallback-prompts)

## New Providers / Models [​](https://docs.litellm.ai/release_notes/tags/fallbacks\#new-providers--models "Direct link to New Providers / Models")

- [NVIDIA Triton](https://developer.nvidia.com/triton-inference-server) `/infer` endpoint. [Start here](https://docs.litellm.ai/docs/providers/triton-inference-server)
- [Infinity](https://github.com/michaelfeil/infinity) Rerank Models [Start here](https://docs.litellm.ai/docs/providers/infinity)

## ✨ Azure Data Lake Storage Support [​](https://docs.litellm.ai/release_notes/tags/fallbacks\#-azure-data-lake-storage-support "Direct link to ✨ Azure Data Lake Storage Support")

Send LLM usage (spend, tokens) data to [Azure Data Lake](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction). This makes it easy to consume usage data on other services (eg. Databricks)
[Start here](https://docs.litellm.ai/docs/proxy/logging#azure-blob-storage)

## Docker Run LiteLLM [​](https://docs.litellm.ai/release_notes/tags/fallbacks\#docker-run-litellm "Direct link to Docker Run LiteLLM")

```codeBlockLines_e6Vv
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
ghcr.io/berriai/litellm:litellm_stable_release_branch-v1.55.8-stable

```

## Get Daily Updates [​](https://docs.litellm.ai/release_notes/tags/fallbacks\#get-daily-updates "Direct link to Get Daily Updates")

LiteLLM ships new releases every day. [Follow us on LinkedIn](https://www.linkedin.com/company/berri-ai/) to get daily updates.

## Finetuning Updates and Improvements
[Skip to main content](https://docs.litellm.ai/release_notes/tags/finetuning#__docusaurus_skipToContent_fallback)

`alerting`, `prometheus`, `secret management`, `management endpoints`, `ui`, `prompt management`, `finetuning`, `batch`

## New / Updated Models [​](https://docs.litellm.ai/release_notes/tags/finetuning\#new--updated-models "Direct link to New / Updated Models")

1. Mistral large pricing - [https://github.com/BerriAI/litellm/pull/7452](https://github.com/BerriAI/litellm/pull/7452)
2. Cohere command-r7b-12-2024 pricing - [https://github.com/BerriAI/litellm/pull/7553/files](https://github.com/BerriAI/litellm/pull/7553/files)
3. Voyage - new models, prices and context window information - [https://github.com/BerriAI/litellm/pull/7472](https://github.com/BerriAI/litellm/pull/7472)
4. Anthropic - bump Bedrock claude-3-5-haiku max\_output\_tokens to 8192

## General Proxy Improvements [​](https://docs.litellm.ai/release_notes/tags/finetuning\#general-proxy-improvements "Direct link to General Proxy Improvements")

1. Health check support for realtime models
2. Support calling Azure realtime routes via virtual keys
3. Support custom tokenizer on `/utils/token_counter` \- useful when checking token count for self-hosted models
4. Request Prioritization - support on `/v1/completion` endpoint as well

## LLM Translation Improvements [​](https://docs.litellm.ai/release_notes/tags/finetuning\#llm-translation-improvements "Direct link to LLM Translation Improvements")

1. Deepgram STT support. [Start Here](https://docs.litellm.ai/docs/providers/deepgram)
2. OpenAI Moderations - `omni-moderation-latest` support. [Start Here](https://docs.litellm.ai/docs/moderation)
3. Azure O1 - fake streaming support. This ensures if a `stream=true` is passed, the response is streamed. [Start Here](https://docs.litellm.ai/docs/providers/azure)
4. Anthropic - non-whitespace char stop sequence handling - [PR](https://github.com/BerriAI/litellm/pull/7484)
5. Azure OpenAI - support Entra ID username + password based auth. [Start Here](https://docs.litellm.ai/docs/providers/azure#entra-id---use-tenant_id-client_id-client_secret)
6. LM Studio - embedding route support. [Start Here](https://docs.litellm.ai/docs/providers/lm-studio)
7. WatsonX - ZenAPIKeyAuth support. [Start Here](https://docs.litellm.ai/docs/providers/watsonx)

## Prompt Management Improvements [​](https://docs.litellm.ai/release_notes/tags/finetuning\#prompt-management-improvements "Direct link to Prompt Management Improvements")

1. Langfuse integration
2. HumanLoop integration
3. Support for using load balanced models
4. Support for loading optional params from prompt manager

[Start Here](https://docs.litellm.ai/docs/proxy/prompt_management)

## Finetuning + Batch APIs Improvements [​](https://docs.litellm.ai/release_notes/tags/finetuning\#finetuning--batch-apis-improvements "Direct link to Finetuning + Batch APIs Improvements")

1. Improved unified endpoint support for Vertex AI finetuning - [PR](https://github.com/BerriAI/litellm/pull/7487)
2. Add support for retrieving vertex api batch jobs - [PR](https://github.com/BerriAI/litellm/commit/13f364682d28a5beb1eb1b57f07d83d5ef50cbdc)

## _NEW_ Alerting Integration [​](https://docs.litellm.ai/release_notes/tags/finetuning\#new-alerting-integration "Direct link to new-alerting-integration")

PagerDuty Alerting Integration.

Handles two types of alerts:

- High LLM API Failure Rate. Configure X fails in Y seconds to trigger an alert.
- High Number of Hanging LLM Requests. Configure X hangs in Y seconds to trigger an alert.

[Start Here](https://docs.litellm.ai/docs/proxy/pagerduty)

## Prometheus Improvements [​](https://docs.litellm.ai/release_notes/tags/finetuning\#prometheus-improvements "Direct link to Prometheus Improvements")

Added support for tracking latency/spend/tokens based on custom metrics. [Start Here](https://docs.litellm.ai/docs/proxy/prometheus#beta-custom-metrics)

## _NEW_ Hashicorp Secret Manager Support [​](https://docs.litellm.ai/release_notes/tags/finetuning\#new-hashicorp-secret-manager-support "Direct link to new-hashicorp-secret-manager-support")

Support for reading credentials + writing LLM API keys. [Start Here](https://docs.litellm.ai/docs/secret#hashicorp-vault)

## Management Endpoints / UI Improvements [​](https://docs.litellm.ai/release_notes/tags/finetuning\#management-endpoints--ui-improvements "Direct link to Management Endpoints / UI Improvements")

1. Create and view organizations + assign org admins on the Proxy UI
2. Support deleting keys by key\_alias
3. Allow assigning teams to org on UI
4. Disable using ui session token for 'test key' pane
5. Show model used in 'test key' pane
6. Support markdown output in 'test key' pane

## Helm Improvements [​](https://docs.litellm.ai/release_notes/tags/finetuning\#helm-improvements "Direct link to Helm Improvements")

1. Prevent istio injection for db migrations cron job
2. allow using migrationJob.enabled variable within job

## Logging Improvements [​](https://docs.litellm.ai/release_notes/tags/finetuning\#logging-improvements "Direct link to Logging Improvements")

1. braintrust logging: respect project\_id, add more metrics - [https://github.com/BerriAI/litellm/pull/7613](https://github.com/BerriAI/litellm/pull/7613)
2. Athina - support base url - `ATHINA_BASE_URL`
3. Lunary - Allow passing custom parent run id to LLM Calls

## Git Diff [​](https://docs.litellm.ai/release_notes/tags/finetuning\#git-diff "Direct link to Git Diff")

This is the diff between v1.56.3-stable and v1.57.8-stable.

Use this to see the changes in the codebase.

[Git Diff](https://github.com/BerriAI/litellm/compare/v1.56.3-stable...189b67760011ea313ca58b1f8bd43aa74fbd7f55)

## Fireworks AI Updates
[Skip to main content](https://docs.litellm.ai/release_notes/tags/fireworks-ai#__docusaurus_skipToContent_fallback)

`deepgram`, `fireworks ai`, `vision`, `admin ui`, `dependency upgrades`

## New Models [​](https://docs.litellm.ai/release_notes/tags/fireworks-ai\#new-models "Direct link to New Models")

### **Deepgram Speech to Text** [​](https://docs.litellm.ai/release_notes/tags/fireworks-ai\#deepgram-speech-to-text "Direct link to deepgram-speech-to-text")

New Speech to Text support for Deepgram models. [**Start Here**](https://docs.litellm.ai/docs/providers/deepgram)

```codeBlockLines_e6Vv
from litellm import transcription
import os