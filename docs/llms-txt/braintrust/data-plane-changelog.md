# Source: https://braintrust.dev/docs/data-plane-changelog.md

# Data plane changelog

> New data plane versions

This changelog is for customers who [self-host the Braintrust data plane](/guides/self-hosting/index).

<Update label="December 2025">
  ### v1.1.29 - December 17, 2025

  * Added local shared read cache for Brainstore writers
  * Added support for SQL as a frontend to BTQL
  * Added braintrust.origin attribute support for OTEL logs
  * Added capability to run API, realtime, and brainstore containers as a non-root user "braintrust"
  * Fixed Azure Blob metadata key formatting (hyphen → underscore)

  ### v1.1.28 - December 4, 2025

  * Fixed enforcement of `BRAINSTORE_QUERY_TIMEOUT_SECONDS` parameter.
  * Added support for enforcing access to only certain data plane URL patterns.
  * Added custom annotation view support.
  * Enable adding MCP servers to prompts. After authenticating with OAuth, these can be used in the UI in Prompt Chat, Playgrounds, and Experiments.
</Update>

<Update label="November 2025">
  ### v1.1.27

  * Added ability to share log and experiment traces publicly
  * A built-in rate limit for API queries. You can enable this by setting
    `RATELIMIT_BTQL_DEFAULT`, which controls how many BTQL queries are allowed per
    object per minute, per object.
  * Better query cancellation for long-running aggregation queries.
  * Add `comments`, `audit_data`, and `_async_scoring_state` to the BTQL schema.
    You can now query for these fields alongside existing ones.
</Update>

<Update label="October 2025">
  ### v1.1.26

  * Faster performance for indexing (compaction and merging)
  * Improved I/O utilization for queries that read a long time horizon
  * Fix a longstanding deadlock bug that can occur with high query volume
  * Many small improvements to query performance

  ### v1.1.25

  * Faster real-time queries (no "excluded docs" in most cases)
  * Fix thinking for Mistral models
  * Significantly faster indexing for large payloads
  * Fix a bug with floating point division in queries
  * Fix MCP OAuth flow for self-hosted deployments
  * More iterations in hosted tools (100)
  * Improve performance for high selectivity filter queries
  * Fix gemini tool calls that included `$defs` and `$refs` in the schema
  * Fix bug in `/feedback` endpoint when updating non-root spans
</Update>

<Update label="August 2025">
  ### v1.1.21

  * Process pydantic-ai OTel spans
  * AI proxy now supports temperature > 1 for models which allow it
  * Preview of data retention on logs, datasets, and experiments

  ### v1.1.20

  * Brainstore vacuum is enabled by default. This will reclaim space from object storage. As a bonus, vacuum also cleans up more data (segment-level write-ahead logs)
  * AI proxy now dynamically fetches updates to the model registry
  * Performance improvements to summary, `IS NOT NULL`, and `!= NULL` queries
  * Handle cancelled BTQL queries earlier and optimize schema inference queries
  * Added a REST API for managing service tokens. See [docs](/api-reference)
  * Support custom columns on the experiments page
  * Aggregate custom metrics and include more built-in agent metrics in experiments and logs
  * Preview of data retention on logs. You can define a per-project policy on logs which will be deleted on a schedule and no longer available in the UI and API

  ### v1.1.19

  * Add support for GPT-5 models
  * OTel tracing support for Google Agent Development Kit
  * OTel support for deleting fields
  * Fix binder error handling for malformed BTQL queries
  * Enable environment tags on prompt versions

  ### v1.1.22

  * Added ability to create and edit custom charts in the monitor dashboard
  * Added support for more Grok models and improved model refresh handling in `/invoke` endpoint
  * Added support for `IN` clause in BTQL queries
  * Improved processing of pydantic-ai OpenTelemetry spans with tool names in span names and proper input/output field mapping
  * Added OpenAI Agents logs formatter for better span rendering in the UI
  * Added retention support for Postgres WAL and object WAL (write-ahead logs)
  * Add S3 lifecycle policies to reclaim additional space from bucket
  * Added authentication support for remote evaluation endpoints
  * Improved ability to fetch all datasets efficiently
  * New `MAX_LIMIT_FOR_QUERIES` parameter to set the maximum allowable limit for BTQL queries. Larger result sets can still be queried through pagination

  ### v1.1.18

  This is our largest data plane release in a while, and it includes several significant performance improvements, bug fixes, and new features:

  * Improve performance for non-selective searches. Eg make `foo != 'bar'` faster
  * Improve performance for score filters. Eg make `scores.correctness = 0` faster
  * Improve group by performance. This should make the monitor page and project summary page significantly faster
  * Add syntax for explicit casting. You can now use explicit casting functions to cast data to any datatype. e.g. `to_number(input.foo)`, `to_datetime(input.foo)`, etc
  * Fix ILIKE queries on nested json: ILIKE queries previously returned incorrect results on nested json objects. ILIKE now works as expected for all json objects
  * Improve backfill performance. New objects should get picked up faster
  * Improve compaction latency. Indexing should kick in much faster, and in particular, this means data gets indexed a lot faster
  * Improved support for OTel mappings, including the new [GenAI Agent](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/) conventions and [strands framework](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/)
  * Add Gemini 2.5 Flash-Lite GA, GPT-OSS models on several providers, and Claude Opus 4.1

  ### v1.1.15

  * Add ability to run scorers as tasks in the playground
  * You can now use object storage, instead of Redis, as a locks manager
  * Support async python in inline code functions
  * Don't re-trigger online scoring on existing traces if only metadata fields like `tags` change

  ### v1.1.14

  * Switch the default query shape from `traces` to `spans` in the API. This means that btql queries will now return 1 row per span, rather than per trace. This change also applies to the REST API
  * Service tokens with scoped, user-independent credentials for system integrations
  * Fix a bug where very large experiments (run through the API) would drop spans if they could not flush data fast enough
  * Support built-in OTel metrics (contact your account team for more details)
  * New parallel backfiller improves performance of loading data into Brainstore across many projects

  ### v1.1.13

  * Fix support for `COALESCE` with variadic arguments
  * Add option to select logs for online scoring with a BTQL filter
  * Add ability to test online scoring configuration on existing logs
  * Mmap based indexing optimization enabled by default for Brainstore
</Update>

<Update label="June 2025">
  ### v1.1.11

  * Add support for LLaMa 4 Scout for Cerebras
  * Turn on index validation (which enables self-healing failed compactions) in the Cloudformation by default

  ### v1.1.7

  * Improve performance of error count queries in Brainstore
  * Automatically heal segments that fail to compact
  * Add support for new models including o3 pro
  * Improve error messages for LLM-originated errors in the proxy

  ### v1.1.6

  * Patch a bug in 1.1.5 related to the `realtime_state` field in the API response

  ### v1.1.5

  * Default query timeout in Brainstore is now 32 seconds
  * Auto-recompact segments which have been rendered unusable due to an S3-related issue
  * Gemini 2.5 models

  ### v1.1.4

  * Optimize "Activity" (audit log) queries, which reduces the query workload on Postgres for large traces (even if you are using Brainstore)
  * Automatically convert base64 payloads to attachments in the data plane
  * Improve AI proxy errors for status codes 401->409
  * Increase real-time query memory limit to 10GB in Brainstore
</Update>

<Update label="April 2025">
  ### v0.0.65

  * Improve error messages when trying to insert invalid unicode
  * Backend support for appending messages

  ### SDK (version 0.0.197)

  * Fix a bug in `init_function` in the Python SDK which prevented the `input` argument from being passed to the function correctly when it was used as a scorer
  * Support setting `description` and `summarizeScores`/`summarize_scores` in `Eval(...)`
</Update>

<Update label="March 2025">
  * Many improvements to the playground experience:
    * Fixed many crashes and infinite loading spinner states
    * Improved performance across large datasets
    * Better support for running single rows for the first time
    * Fixed re-ordering prompts
    * Fixed adding and removing dataset rows
    * You can now re-run specific prompts for individual cells and columns
  * You can now do "does not contain" filters for tags in experiments and datasets
  * When you `invoke()` a function, inline base64 payloads will be automatically logged as attachments
  * Add a strict mode to evals and functions which allows you to fail test cases when a variable is not present in a prompt
  * Add Fireworks' DeepSeek V3 03-24 and DeepSeek R1 (Basic), along with Qwen QwQ 32B in Fireworks and Together.ai, to the playground and AI proxy
  * Fix bug that prevented Databricks custom provider form from being submitted without toggling authentication types
  * Unify Vertex AI, Azure, and Databricks custom provider authentication inputs
  * Add Llama 4 Maverick and Llama 4 Scout models to Together.ai, Fireworks, and Groq providers in the playground and AI proxy
  * Add Mistral Saba and Qwen QwQ 32B models to the Groq provider in the playground and AI proxy
  * Add Gemini 2.5 Pro Experimental and Gemini 2.0 Flash Thinking Mode models to the Vertex provider in the playground and AI proxy
  * Add OpenAI's [o1-pro](https://platform.openai.com/docs/models/o1-pro) model to the playground and AI proxy
  * Support OpenAI Responses API in the AI proxy
  * Add support for the Gemini 2.5 Pro Experimental model in the playground and AI proxy
  * Option to disable the experiment comparison auto-select behavior
  * Add support for Databricks custom provider as a default cloud provider in the playground and AI proxy
  * Allow supplying a base API URL for Mistral custom providers in the playground and AI proxy
  * Support pushed code bundles larger than 50MB
  * The OTEL endpoint now understands structured output calls from the Vercel AI SDK
  * Added support for `concat`, `lower`, and `upper` string functions in BTQL
  * Correctly propagate Bedrock streaming errors through the AI proxy and playground
  * Online scoring supports sampling rates with decimal precision
  * Added support for OpenAI GPT-4o Search Preview and GPT-4o mini Search Preview in the playground and AI proxy
  * Add support for making Anthropic and Google-format requests to corresponding models in the AI proxy
  * Fix bug in model provider key modal that prevents submitting a Vertex provider with an empty base URL
  * Add column menu in grid layout with sort and visibility options
  * Enable logging the `origin` field through the REST API
  * Add support for "image" pdfs in the AI proxy
  * Fix issue in which code function executions could hang indefinitely
  * Add support for custom base URLs for Vertex AI providers
  * Add dataset column to experiments table
  * Add python3.13 support to user-defined functions
  * Fix bug that prevented calling Python functions from the new unified playground

  ### v0.0.64

  * Brainstore is now set as the default storage option
  * Improved backfilling performance and overall database load
  * Enabled relaxed search mode for ClickHouse to improve query flexibility
  * Added strict mode option to prompts that fails when required template arguments are missing
  * Enhanced error reporting for missing functions and eval failures
  * Fixed streaming errors that previously resulted in missing cells instead of visible error states
  * Abort evaluations on server when stopped from playground
  * Added support for external bucket attachments
  * Improved handling of large base64 images by converting them to attachments
  * Fixed proper handling of UTF-8 characters in attachment filenames
  * Added the ability to set telemetry URL through admin settings
</Update>

<Update label="February 2025">
  ### v0.0.63

  * Support for Claude 3.7 Sonnet, Gemini 2.0 Flash-Lite, and several other models in the proxy
  * Stability and performance improvements for ETL processes
  * A new `/status` endpoint to check the health of Braintrust services
</Update>

<Update label="December 2024">
  ### v0.0.61

  * Upgraded to Node.js 22 in Docker containers

  ### v0.0.60

  * Make PG\_URL configuration more uniform between nodeJS and python clients
</Update>

<Update label="November 2024">
  ### v0.0.59

  * Fix permissions bug with updating org-scoped env vars
  * Support uploading [file attachments](/guides/attachments)
  * You can now export [OpenTelemetry (OTel)](https://opentelemetry.io/docs/specs/otel/) traces to Braintrust
</Update>

<Update label="September 2024">
  ### v0.0.56

  * Hosted tools are now available in the API
  * Environment variables are now supported in the API
  * Automatically backfill `function_data` for prompts created via the API

  ### v0.0.54

  * Support for bundled eval uploads
  * The `PATCH` endpoint for prompts now supports updating the `slug` field
  * Don't fail insertion requests if realtime broadcast fails
  * Performance optimizations to filters on `scores`, `metrics`, and `created` fields
  * Performance optimizations to filter subfields of `metadata` and `span_attributes`
</Update>

<Update label="August 2024">
  ### v0.0.53

  * The API now supports running custom LLM and code (TypeScript and Python) functions

  ### v0.0.51

  * The proxy is now a first-class citizen in the API service, which simplifies deployment
  * The proxy is now accessible at `https://api.braintrust.dev/v1/proxy`
  * If you are self-hosting, the proxy is now bundled into the API service
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt