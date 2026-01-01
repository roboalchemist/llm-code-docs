# Source: https://braintrust.dev/docs/changelog.md

# Product changelog

> New updates and product improvements

<Update label="December 2025">
  ### Claude Code integration

  You can now use Braintrust with [Claude Code](https://code.claude.com/docs/en/overview), Anthropic's agentic coding tool. The integration automatically traces Claude Code sessions to give you insight into LLM calls, tool usage, and performance, while enabling Claude to query logs, fetch experiment results, and log data using natural language, especially useful when writing and iterating on evals. For setup instructions and usage examples, see the [Claude Code integration guide](/integrations/sdk-integrations/claude-code).

  ### New SDKs: Java, Go, Ruby, and C\#

  Braintrust now offers native SDKs for Java, Go, Ruby, and C#/.NET that provide tools for evaluating and tracing AI applications in Braintrust.

  See the SDK documentation for setup instructions and examples: [Java](https://github.com/braintrustdata/braintrust-sdk-java), [Go](https://github.com/braintrustdata/braintrust-sdk-go), [Ruby](https://github.com/braintrustdata/braintrust-sdk-ruby), [C#](https://github.com/braintrustdata/braintrust-sdk-dotnet/tree/main).

  ### Nunjucks templating syntax for prompts

  You can now use [Nunjucks](https://mozilla.github.io/nunjucks/templating.html) as an advanced templating syntax for prompts in the UI. Nunjucks provides features like loops, conditionals, and filters for sophisticated prompt engineering workflows. For more details, see [Use templating](/core/functions/prompts#use-templating).

  ### Track dataset performance across experiments

  You can now see which experiments used your dataset and how each row performed. This helps you identify problematic test cases and understand your evaluation data quality. For more details, see [Track dataset performance](/core/datasets#track-dataset-performance).

  ### Slack integration for alerts

  You can now post alerts to Slack channels when conditions are met. For more details, see [Alerts](/guides/automations/alerts).

  <Badge size="md" className="text-xs px-2">Data plane v1.1.29+</Badge>

  ### SQL syntax support

  BTQL now supports standard SQL syntax as an alternative to the native clause-based syntax. The parser automatically detects whether your query is SQL or BTQL. For more details, see [BTQL](/reference/btql#sql-syntax).

  <Badge size="md" className="text-xs px-2">Data plane v1.1.29+</Badge>

  ### MCP servers in prompts

  You can now use public MCP (Model Context Protocol) servers to give your prompts access to external tools and data. This is useful for evaluating complex tool calling workflows, experimenting with external APIs and services, and tuning public MCP servers. For more details, see [Add MCP servers](/core/functions/prompts#add-mcp-servers)

  <Badge size="md" className="text-xs px-2">Data plane v1.1.28+</Badge>

  ### Custom views for traces

  Using Loop, you can now use natural language to create custom views of traces. This helps you highlight specific parts of a trace or visualize the trace in a way that is specific to your use case. For more details, see [Custom view](/guides/traces/view#custom-trace).

  ### Pass/fail thresholds for scorers

  You can now define a minimum score (between 0 and 1) that a scorer must achieve for a result to be considered passing. This helps you quickly identify which evaluations meet your quality standards. For more details, see [Pass/fail thresholds](/core/functions/scorers#pass/fail-thresholds).

  <Badge size="md" className="text-xs px-2">Data plane v1.1.28+</Badge>

  ### TypeScript SDK releases

  * [v1.0.0](https://github.com/braintrustdata/braintrust-sdk/releases/tag/js-sdk-v1.0.0) - This release moves OpenTelemetry functionality to the separate `@braintrust/otel` package. This solves ESM build issues in Next.js (edge), Cloudflare Workers, Bun, and TanStack applications, and adds support for both OpenTelemetry v1 and v2.

    If you are using OpenTelemetry functionality, this is a **breaking change**. See [TypeScript SDK upgrade guide](/reference/sdks/typescript-upgrade-guide) for migration instructions. If you are not using OpenTelemetry, upgrade as usual with `npm install braintrust@latest`.

  * [v1.0.1](https://github.com/braintrustdata/braintrust-sdk/releases/tag/js-sdk-v1.0.1) - This release makes URLs clickable in supported terminals when running evaluations and enables project-level AI secrets to work correctly in remote evaluations.

  * [v1.0.2](https://github.com/braintrustdata/braintrust-sdk/releases/tag/js-sdk-v1.0.2) - This release improves tracing for Vercel AI SDK applications, adding complete visibility into [multi-step tool interactions](/integrations/sdk-integrations/vercel#multi-step-tool-interactions) and automatic tracing for [AI SDK Agents](/integrations/sdk-integrations/vercel#tracing-agents).

  ### Improvements

  * Added `json_extract` function to BTQL for extracting values from JSON strings using path expressions with support for dot notation, array indexing, and nested paths.
  * Added progress bar for UI-triggered experiments.
  * Online scores now always show up in the list of scores in the summary view.
  * Online scores now always show up in the trace table, even if they haven't been run yet.
  * Added support for extracting last turn prompts and scorer-format dataset inputs in iterate in playground modals.
  * Updated BTQL filters to automatically extract filter statements from broader input.
  * Added docs on [attaching custom metadata to traces](/integrations/sdk-integrations/vercel#add-metadata) when using the Vercel AI SDK.
  * Expanded [deep search](/core/logs/use-deep-search) docs with setup instructions, query examples, and filtering workflows.
  * Improved Loop chart type and unit selection for data visualizations
  * Added ability to [filter logs and experiments by comments](/core/logs/view#filter-menu).
  * Added project description field to projects. This can be used to provide additional context to teammates and when using AI features.
  * Consolidate project configuration and organization settings pages into a single page.
</Update>

<Update label="November 2025">
  * Custom metric columns on the experiments list page
  * Aggregate table column headers on the experiments list page
  * Resizable trace timeline sidebar
  * Tag from prompt/scorer pages
  * Add option to maintain hierarchy in trace tree view while filtering span types
  * Dataset schemas with visual schema builder and form-based editing with validation
  * Aggregate table column headers on the projects list page
  * Added support for Loop to make btql queries with arbitrary time range
  * Added logs and dataset browsers to scorer detail page
  * Added support for Loop to generate monitoring chart in monitor page's edit chart dialog
  * BTQL now supports using `dimensions` and `measures` with the `summary` shape to group and aggregate traces. This enables analyzing patterns, monitoring performance trends, and comparing metrics across models or time periods. See [Aggregated trace analytics](/reference/btql#aggregated-trace-analytics).
  * BTQL queries issued through the API are now rate limited at 20 requests per object per minute.
  * Added automatic context mechanism to Loop to automatically add currently viewed trace as context in logs and experiments page
  * Added Grok 4.1 support
  * Added Claude Opus 4.5 support
  * If you are self-hosted, requests to [https://api.braintrust.dev](https://api.braintrust.dev) will now fail
  * Fix max tokens and reasoning token budget settings for Gemini models

  ### Python SDK version 0.3.8

  * Fixes logging very deep objects or with circular recursion

  ### Python SDK version 0.3.7

  * Added time to first token for Anthropic wrapper
  * Fixes nesting for OpenAI agents wrapper

  ### TypeScript SDK version 0.4.9

  * SDK integration rewrite. Based on customer feedback we rewrote the integration to be simpler and more robust. Now officially supports v3 up to v6 of the library. All users are recommended to switch to `wrapAISDK` instead of now deprecated `wrapAISDKModel` and `BraintrustMiddleware`. BREAKING CHANGE: spans have a different input/output and metadata and the do\* spans are no longer needed.

  ### SDK Integrations: Google ADK 0.2.3

  * Support MCP agent tracing

  ### SDK Integrations: LangChain / LangGraph JS  0.2.1

  * Added time to first token metric

  ### SDK Integrations: LangChain / LangGraph Python 0.1.5

  * Added time to first token metric
</Update>

<Update label="October 2025">
  * Enabled editing and resending Loop chat messages
  * Document how to integrate Apollo GraphQL and Braintrust for automatic tracing
  * Add support for Grok 4 Fast (Reasoning & Non-Reasoning)
  * Add support for Groq gwen/gwen3-32 & moonshotai/kimi-k2-instruct-0905
  * Deprecate Anthropic Claude 3.5 models as they are no longer supported by Anthropic
  * Modify Apply filter button in btql tool to be more prominent
  * Added AI-assisted generation to run data box in scorer details page
  * Added message queuing to Loop
  * Added a button to extract filter clause from a btql query in filter btql editor
  * Start a Loop conversation from the CMD-K menu
  * Move Loop button to the bottom right of the screen
  * Use case examples when creating a playground
  * Java SDK
  * Scope collapse state for span fields by the span type
  * Collapse/expand all button for LLM data view
  * By default, collapse all messages in LLM data view besides the last turn
  * Generate scorer spans when applying scores to logs
  * Added support for scoring experiment rows
  * Added AI-assisted generation in tools form, btql filter form and online scoring form
  * Increased default maximum agentic tool use roundtrips from 5 to 100
  * Added support for Gemini tracing
  * Added support for Claude 4.5 Haiku
  * Added Loop to the prompt and scorer detail pages
  * **Refreshed OpenAI Realtime Audio proxy support** - Updated AI proxy to support the latest OpenAI SDK (v6.0+) for realtime audio interactions
    * Added support for both `OpenAIRealtimeWebSocket` (browser/Cloudflare Workers) and `OpenAIRealtimeWS` (Node.js with ws library)
    * Updated event types to match the current OpenAI Realtime API specification (`response.output_audio.delta`, `response.output_text.delta`, etc.)
    * Added header-based authentication and logging with `x-bt-parent` and `x-bt-compress-audio` headers
    * Improved audio logging with automatic format detection and optional MP3 compression for reduced storage costs
  * Added "Pretty" span field display option that optimizes for object value readability and renders object values in markdown
    * The Pretty display option replaces the Markdown option since Pretty renders markdown by default
  * Added support for viewing spans in the table on the logs page
  * Added GPT-5 Pro support
  * Added **Review** page to see spans marked for review in logs, experiments and datasets across a project
  * Fixed Loop prompt optimization of remote evals
  * Fix issue with thinking events coming from Mistral
  * Added Toplist and Big number monitor chart types
  * Support for [JSON attachments](/guides/attachments#json-attachments)
  * Improve "Raw span data" and new buttons to download a span or entire trace as JSON from the trace viewer

  ### SDK Integrations: LangChain (Python) v0.1.2

  * Bug fix to ignore async context changed error

  ### Python SDK version 0.3.6

  * Fixed remote evals bug where experiments were not properly marked as completed on the backend
  * Fixed dataset `_internal_btql` parameter to properly override default BTQL settings (e.g., custom limit values)

  ### TypeScript SDK version 0.4.8

  * Added OpenTelemetry distributed tracing helpers (`contextFromSpanExport()` and `spanContextFromSpanExport()`) for seamless trace propagation between Braintrust and OpenTelemetry across service boundaries

  ### Python SDK version 0.3.5

  * Added DSPy integration with `wrap_dspy` wrapper for automatic tracing of DSPy applications
  * Added OpenTelemetry distributed tracing helpers (`context_from_span_export()` and `span_context_from_span_export()`) for seamless trace propagation between Braintrust and OpenTelemetry across service boundaries

  ### Python SDK version 0.3.4

  * Added support for `GEMINI_API_KEY` environment variable

  ### TypeScript SDK version 0.4.6

  * Properly support querying versioned datasets

  ### TypeScript SDK version 0.4.3

  * Improved LangChain integrations with simplified parsing for both TypeScript and Python
  * Added JSON attachment SDK support

  ### TypeScript SDK version 0.4.2

  * Add OpenTelemetry compatibility mode for TypeScript. This allows OTel spans to work with Evals

  ### TypeScript SDK version 0.4.1

  * Added Google GenAI wrapper support
  * Updated Mastra wrapper methods from `generateVNext`/`streamVNext` to `generate`/`stream`
  * Moved langchain-js braintrust dependency to peer dependencies
  * Fixed handling of attachments for Anthropic to avoid large base64 strings in UI
  * Fixed preservation of result object when returning from `wrappedStreamObject` in AI SDK
  * Fixed `LanguageModelV1#supportsUrl` being a function, not a property

  ### Python SDK version 0.3.3

  * Properly support querying versioned datasets
</Update>

<Update label="September 2025">
  * Added Anthropic Claude 4.5 Sonnet support
  * Fixed Gemini schema support to enable proper function calling and structured outputs when using Google's Gemini models through Braintrust and the AI proxy
  * Added Claude Agent SDK Integration support
  * Added Gemini Flash and Lite Preview (Sept 2025) support
  * Improved prompt detail chat logging and added link to corresponding trace
  * Fixed bugs with parallel tool calling in Loop
  * Enabled Loop to write BTQL queries against arbitrary data sources on non-BTQL-sandbox pages
  * Added support for creating datasets and scorers with Loop from the experiment, dataset, and logs pages
  * Resolved excessive `localStorage` usage in Loop and BTQL sandbox
  * Improved Loop's `from` clause handling in the BTQL sandbox
  * Fixed cross-tab syncing and session restoration bugs in Loop
  * Prompt/scorer activity view UI updates
    * Before: selecting a version showed a diff vs. the current editor content, where the selected version is the base of the diff
    * After: prompt versions can be viewed without diffing vs. editor. When diff is enabled, version is shown as incoming, to indicate what would occur when reverting to that version
  * Added support for updating the email associated with billing data
  * Added support for iterating on logs in playgrounds
  * Added support for scoring existing logs
  * Trace tree is now visible in human review mode
  * BTQL sandbox improvements
    * Loop is now on the page and can write queries, debug errors and answer syntax questions
    * Tabs
    * Simple charts
    * Improved auto-complete
  * Updated UI color palette
  * Custom charts added to the monitor page (requires data plane 1.1.22)
  * View state changes for non-saved views
    * Before: We would attempt to restore any previous edited view state to the URL
    * After: With a few exceptions, edited view state for non-saved views is only represented in the URL
  * Loop can search through Braintrust's docs and blog posts to help you answer questions about how to use Braintrust, including generating sample code

  ### Python SDK version 0.3.1

  * Ensure experiments use SpanComponentsV3 by default

  ### Python SDK version 0.3.0

  * Added OpenTelemetry compatibility mode for seamless integration between Braintrust and OTEL tracing
  * Added `setup_claude_agent_sdk` for automatic tracing of Claude Agent SDK applications
  * Improved Anthropic wrapper to log consistent input/output format
  * Added `strict` parameter to `Prompt.build` for strict schema validation
  * Added SpanComponentsV4 support

  ### TypeScript SDK version 0.4.0

  * Added `wrapClaudeAgentSDK` for automatic tracing of Claude Agent SDK applications
  * Improved Anthropic wrapper to log consistent input/output format
  * Fixed AI SDK model detection in `wrapGenerate` callback
  * Added SpanComponentsV4 support
</Update>

<Update label="August 2025">
  * Traces in the trace viewer on the logs page can now show all associated traces based on a metadata field or tag
  * Monitor page layout changed to be more responsive to screen size
  * Various UX improvements to prompt dialog
  * Improved onboarding experience
  * Trace timeline layout improvements
  * Pro plan organizations can now downgrade to the Free plan via the settings page without contacting support
  * Prevent read-only users from downloading data from the UI
  * @mention team members in comments to notify them via email. To mention someone, type "@" and a team member's name or email in any comment input
  * You can now assign users to rows in experiments, logs, and datasets. Once assigned, you can filter rows by a specific user or a group of users
  * View configuration has been changed to no longer auto-save changes. It now shows a dirty state and you have the option of saving or resetting those changes back to the base view

  ### TypeScript SDK version 0.3.7

  * Support locking down remote evals via `--dev-org-name` to only accept users from your org
  * Fixed parent span precedence issues for better trace hierarchy
  * Improved propagation of parentSpanId into parentSpanContext for OpenTelemetry JS v2 compatibility
  * Fold the `@braintrust/core` package into `braintrust`. This package consists of a small set of utility functions that is more easily-managed as part of the main `braintrust` package. After version `0.3.7`, you should no longer need a dependency on `@braintrust/core`

  ### Python SDK version 0.2.6

  * Python SDK now correctly nests spans logged from inside tool calls in OpenAI Agents

  ### Python SDK version 0.2.5

  * Support data masking (see [docs](/guides/traces/customize#masking-sensitive-data))
  * Remote evals in Python SDK
  * Support tags in Eval hooks
  * Validate attachment file readability at creation time

  ### Python SDK version 0.2.4

  * Allow non-batch span processors in `BraintrustSpanProcessor`

  ### Python SDK version 0.2.3

  * Fix openai-agents to inherit the right tracing context

  ### TypeScript SDK version 0.3.6

  * OpenAI responses wrapper no longer filters out span data fields when logging
  * Fixed `withResponse` and `wrapOpenAI` interaction to not hide response data

  ### TypeScript SDK version 0.2.5

  * Support data masking (see [docs](/guides/traces/customize#masking-sensitive-data))
  * Support tags in Eval hooks
  * Validate attachment file readability at creation time

  ### TypeScript SDK version 0.2.4

  * Support OpenAI Agents SDK

  ### SDK Integrations: Google ADK (Python) (version 0.1.1)

  * Added integration with [Google Agent Development Kit (ADK)](/integrations/sdk-integrations/google)

  ### SDK Integrations: OpenAI Agents (TS) (version 0.0.2)

  * Fix openai-agents to inherit the right tracing context

  ### Python SDK version 0.2.2

  * Added `environment` parameter to `load_prompt`
  * The Otel SpanProcessor now keeps `traceloop.*` spans by default
  * Experiments can now be run without sending results to the server
  * Span creation is significantly faster in Python

  ### TypeScript SDK version 0.2.3

  * Added `environment` parameter to `load_prompt`
  * The Otel SpanProcessor now keeps `traceloop.*` spans by default
  * Experiments can now be run without sending results to the server
  * Fix `npx braintrust pull` for large prompts

  ### TypeScript SDK version 0.2.2

  * Fix ai-sdk tool call formatting in output
  * Log OpenAI Agents input and output to root span
  * Wrap OpenAI responses.parse
  * Add wrapTraced support for generator functions

  ### Python SDK version 0.2.1

  * Fix langchain-py integration tracing when users use a @traced method
  * Wrap OpenAI responses.parse
  * Add @traced support for generator functions

  ### Autoevals PY (version 0.0.130)

  * Fold the `braintrust_core` external package into the `autoevals` package, since it is the only user of `braintrust_core`. Future braintrust packages will not depend on the `braintrust_core` py package
</Update>

<Update label="July 2025">
  * New improved UI for trace tree
  * Token and cost metrics are computed per sub-tree in the trace viewer
  * Download BTQL sandbox results as JSON or CSV
  * Moved monitor chart legends to the bottom and increased chart heights
  * Fixed a monitor chart issue where the series toggle selector would filter the incorrect series
  * Improved monitor fullscreen experience: charts now open faster and retain their series filter state
  * Loop is now available in the experiments page and has a new ability to render interactive components inside the chat that will help you find the UI element that Loop is referencing
  * You can now use remote evals with the "+Experiment" button to create a new experiment. Previously, they were only available in the playground
  * Add monitor page UTC timezone toggle
  * Improved trace view loading performance for large traces
  * Loop can now create custom code scorers in playgrounds
  * Schema builder UI for structured outputs
  * Sort datasets when the `Faster tables` feature flag is enabled
  * Change LLM duration to be the sum, not average, of LLM duration across spans
  * Add support for Grok 4 and Mistral's Devstral Small Latest

  ### TypeScript SDK version 0.2.1

  * Fix support for the `openai.chat.completions.parse` method when used with `wrapOpenAI`
  * Added support for ai-sdk\@beta with new `BraintrustMiddleware`
  * Support running remote evals as full experiments

  ### TypeScript SDK version 0.2.0

  * When running multiple trials per input (`trial_count > 1`), you can now access the current trial index (0-based) via `hooks.trialIndex` in your task function
  * Added `BraintrustExporter` in addition to `BraintrustSpanProcessor`
  * Bound max ancestors in git to 1,000

  ### Python SDK version 0.2.0

  * When running multiple trials per input (`trial_count > 1`), you can now access the current trial index (0-based) via `hooks.trial_index` in your task function
  * New LiteLLM `wrap_litellm` wrapper
  * Increase max ancestors in git to 1,000

  ### Python SDK version 0.1.8

  * Added `BraintrustSpanProcessor` to simplify Braintrust's integration with OpenTelemetry

  ### Python SDK version 0.1.7

  * Added support for loading prompts by ID via the `load_prompt` function. You can now load prompts directly by their unique identifier

  ### TypeScript SDK version 0.1.1

  * Added `BraintrustSpanProcessor` to simplify integration with OpenTelemetry

  ### TypeScript SDK version 0.1.0

  * Fix a bug where large experiments would drop spans if they could not flush data fast enough
  * Fix bug in attachment uploading in evals executed with `npx braintrust eval`
  * Upgrading zod dependency from `^3.22.4` to `^3.25.3`
  * Added support for loading prompts by ID via the `loadPrompt` function
</Update>

<Update label="June 2025">
  * Time range filters on the logs page
  * Add support for multi-factor authentication
  * Fix a bug with Vertex AI calls when the request includes the anthropic-beta header
  * Add Zapier integration to trigger Zaps when there's a new automation event or a new project
  * Add OpenAI's [o3-pro](https://platform.openai.com/docs/models/o3-pro) model to the playground and AI proxy
  * View parameters are now present in the url when viewing a default view
  * Experiments charting controls have been added into views
  * Experiment objects now support tags through the API and on the experiments view
  * Add support for Gemini 2.5 Pro, Gemini 2.5 Flash, and Gemini 2.5 Flash Lite
  * Correctly propagate `expected` and `metadata` values to function calls when running `invoke`
  * Chat-like thread layout that simplifies thread display to LLM and score data
  * Enable all agent nodes to access dataset variables with the mustache variable `{{dataset}}`
  * Improve reliability of online scoring when logging high volumes of data to a project
  * Tags can now be sorted in the project configuration page which will change their display order in other parts of the UI
  * System-only messages are now supported in Anthropic and Bedrock models
  * Logs page UI can now filter nested data fields in `metadata`, `input`, `output`, and `expected`
  * Support reasoning params and reasoning tokens in streaming and non-streaming responses in the [AI proxy](/guides/proxy) and across the product
  * New [braintrust-proxy](https://pypi.org/project/braintrust-proxy/) Python library to help developers integrate with their IDEs to support new reasoning input and output types
  * New `@braintrust/proxy/types` module to augment OpenAI libraries with reasoning input and output types
  * New streaming protocol between Brainstore and the API server speeds up queries
  * Time brushing interaction enabled on Monitor page charts
  * Can create user-defined views in the monitoring page
  * Live updating time mode added to the monitoring page
  * The `anthropic` package is now included by default in Python functions
  * Audit log queries must now specify an `id` filter for the set of rows to fetch
  * (Beta) continuously export logs, experiments, and datasets to S3
  * Enable passing `metadata` and `expected` as arguments to the first agent prompt node

  ### Autoevals.js v0.0.130

  * Remove dependency on `@braintrust/core`

  ### TypeScript SDK version 0.0.209

  * Ensure SpanComponentsV3 encoding works in the browser

  ### TypeScript SDK version 0.0.208

  * Ensure running remote evals (i.e. `runDevServer`) works without the CLI wrapper
  * Add span + parent ids to `StartSpanArgs`

  ### TypeScript SDK version 0.0.207

  * The SDK's under-the-hood queue for sending logs now has a default size of 5000 logs
  * You can configure the max size by setting `BRAINTRUST_LOG_QUEUE_MAX_SIZE` in your environment
  * Improvements to the logging of parallel tool calls
  * Attachments are now converted to base64 data URLs, making it easier to work with image attachments in prompts

  ### TypeScript SDK version 0.0.206

  * Add support for `project.publish()` to directly `push` prompts to Braintrust (without running `braintrust push`)
  * The OpenAI and Anthropic wrappers set `provider` metadata

  ### Python SDK version 0.1.5

  * The SDK's under-the-hood log queue will not block when full and has a default size of 25000 logs
  * You can configure the max size by setting `BRAINTRUST_LOG_QUEUE_MAX_SIZE` in your environment
  * Improvements to the logging of parallel tool calls
  * Attachments are now converted to base64 data URLs, making it easier to work with image attachments in prompts

  ### Python SDK version 0.1.4

  * Add `project.publish()` to directly `push` prompts to Braintrust (without running `braintrust push`)
  * `@traced` now works correctly with async generator functions
  * The OpenAI and Anthropic wrappers set `provider` metadata

  ### Python SDK version 0.1.3

  * Improve retry logic in the control plane connection (used to create new experiments and datasets)
</Update>

<Update label="May 2025">
  * The "Faster tables" flag is now the default. You should notice experiments, datasets, and the logs page load much faster
  * Add Claude 4 models in Bedrock and Vertex to the AI proxy and playground
  * Braintrust now incorporates cached tokens into the cost calculations for experiments and logs
  * The monitor page also now includes separate lines so you can track costs and counts for uncached, cached, and cache creation tokens
  * Native support for thinking parameters in the playground
  * Improved playground prompt editor stability and performance
  * Capture cached tokens from OpenAI and Anthropic models in a unified format and surface them in the UI
  * Create experiments from the experiments list page using saved prompts/agents
  * New BTQL sandbox page and editor with autocomplete
  * Fullscreen-able monitor charts
  * Added a 'Copy page' button to the top of every docs page
  * Brainstore now supports vacuuming data from object storage to reclaim space
  * Organization owners can manage API keys for all users in their organization in the UI
  * Add endpoint for admins to list all ACLs within an org
  * Collapsible sidebar navigation
  * Command bar (CMD/CTRL+K) to quickly navigate and between pages and projects
  * View monitor page logs across all projects in an organization
  * Added Mistral Medium 3 and Gemini 2.5 Pro Preview to the AI proxy and playground
  * Self-hosted builds now log in a structured JSON format that is easier to parse

  ### Python SDK version 0.1.2

  * Added support for `metadata` and `tags` arguments to `invoke`
  * The SDK now gracefully handles OpenAI's `NotGiven` parameter
  * Added `span.link()` to synchronously generate permalinks

  ### Python SDK version 0.1.1

  * Update cached token accounting in `wrap_anthropic` to correctly capture cached tokens
  * Pull additional metadata in `braintrust pull` for prompts and functions to improve tracing

  ### SDK (version 0.1.0)

  * Allow custom model descriptions in Braintrust
  * Improve support for PDF attachments to multimodal OpenAI models
  * The Python library no longer has a dependency on `braintrust_core`

  ### TypeScript SDK version 0.0.206

  * Add support for `metadata` and `tags` arguments to `invoke`

  ### TypeScript SDK version 0.0.205

  * Make the `_xact_id` field in `origin` optional
  * Added `span.link()` as a synchronous means of generating permalinks

  ### TypeScript SDK version 0.0.204

  * Update cached token accounting in `wrapAnthropic` to correctly capture cached tokens

  ### SDK (version 0.0.203)

  * Add new reasoning to OpenAI messages

  ### SDK (version 0.0.202)

  * Gracefully handle experiment summarization failures in Eval()
  * Fix a bug where `wrap_openai` was breaking `pydantic_ai run_stream` func
  * Add tracing to the `client.beta.messages` calls in the TypeScript Anthropic library
  * Fix some deprecation warnings in the Python SDK
</Update>

<Update label="April 2025">
  * Permission groups settings page now allows admins to set group-level permissions
  * Automations alpha: trigger webhooks based on log events
  * Preview attachments in playground input cells
  * Playground now support list mode which includes score and metric summaries
  * Handle structured outputs from OpenAI's responses API in the "Try prompt" experience
  * Allow users to remove themselves from any organization they are part of using the `/v1/organization/members` REST endpoint
  * Group monitor page charts by metadata path
  * Download playground contents as CSV
  * Add pending and streaming state indicators to playground cells
  * Distinguish per-row and global playground progress
  * Added GPT-4.1, o4-mini and o3 to the AI proxy and playground
  * On the monitor page, add aggregate values to chart legends
  * Add Gemini 2.5 Flash Preview model to the AI proxy and playground
  * Add support for audio and video inputs for Gemini models in the AI proxy and playground
  * Add support for PDF files for OpenAI models
  * Native tracing support in the proxy has finally arrived! Read more in [the docs](/guides/proxy#tracing)
  * Upload attachments directly in the UI in datasets, playgrounds, and prompts
  * Playground option to append messages from a dataset to the end of a prompt
  * A new toggle that lets you skip tracing scoring info for online scoring
  * GIF and image support in comments
  * Add embedded view and download action for inline attachments of supported file types

  ### SDK (version 0.0.201)

  * Support OpenAI `client.beta.chat.completions.parse` in the Python wrapper

  ### SDK (version 0.0.200)

  * Ensure the prompt cache properly handles any manner of prompt names
  * Ensure the output of `anthropic.messages.create` is properly traced when called with `stream=True` in an async program

  ### SDK (version 0.0.199)

  * Fix a bug that broke async calls to the Python version of `anthropic.messages.create`
  * Store detailed metrics from OpenAI's `chat.completion` TypeScript API

  ### SDK (version 0.0.198)

  * Trace the `openai.responses` endpoint in the Typescript SDK
  * Store the `token_details` metrics return by the `openai/responses` API

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

  ### SDK (version 0.0.196)

  * Adding Anthropic tracing for our TypeScript SDK. See `braintrust.wrapAnthropic`
  * The SDK now paginates datasets and experiments, which should improve performance for large datasets and experiments
  * Add `strict` flag to `invoke` which implements the strict mode described above
  * Raise if a Python tool is pushed without without defined parameters, instead of silently not showing the tool in the UI
  * Fix Python OpenAI wrapper to work for older versions of the OpenAI library without `responses`
  * Set time\_to\_first\_token correctly from AI SDK wrapper

  ### SDK (version 0.0.195)

  * Improve the metadata collected by the Anthropic client
  * Anthropic client can now be run with `braintrust.wrap_anthropic`
  * Fix a bug when `messages.create` was called with `stream=True`

  ### SDK (version 0.0.194)

  * Add Anthropic tracing to the Python SDK with `wrap_anthropic_client`
  * Fix a bug calling `braintrust.permalink` with `NoopSpan`

  ### SDK (version 0.0.193)

  * Fix retry bug when downloading large datasets/experiments from the SDK
  * Background logger will load environment variables upon first use rather than when module is imported

  ### SDK (version 0.0.192)

  * Improve default retry handler in the python SDK to cover more network-related exceptions

  ### SDK (version 0.0.190)

  * Fix `prompt pull` for long prompts
  * Fix a bug in the Python SDK which would not retry requests that were severed after a connection timeout

  ### SDK (version 0.0.189)

  * Added integration with [OpenAI Agents SDK](/integrations/sdk-integrations/openai-agents-sdk)

  ### SDK (version 0.0.188)

  * Deprecated `braintrust.wrapper.langchain` in favor of the new `braintrust-langchain` package

  ### SDK (version 0.0.187)

  * Always bundle default python packages when pushing code with `braintrust push`
  * Fix bug in the TypeScript SDK where `asyncFlush` was not correctly defaulted to false
  * Fix a bug where `span_attributes` failed to propagate to child spans through propagated events
  * Added support for handling score values when an Eval has errored
  * Improve support for binary packages in `npx braintrust eval`
  * Support templated structured outputs
  * Fix dataset summary types in Typescript

  ### Autoevals (version 0.0.124)

  * Added `init` to set a global default client for all evaluators (Python and Node.js)
  * Added `client` argument to all evaluators to specify the client to use
  * Improved the Autoevals docs with more examples

  ### Autoevals (version 0.0.123)

  * Swapped `polyleven` for `levenshtein` for faster string matching

  ### SDK Integrations: LangChain (Python) (version 0.0.2)

  * Add a new `braintrust-langchain` integration with an improved `BraintrustCallbackHandler` and `set_global_handler` to set the handler globally for all LangChain components

  ### SDK Integrations: LangChain.js (version 0.0.6)

  * Small improvement to avoid logging unhelpful LangGraph spans
  * Updated peer dependencies with LangChain core that fixes the global handler for LangGraph runs

  ### SDK Integrations: Val Town

  * New `val.town` integration with example vals to quickly get started with Braintrust
</Update>

<Update label="February 2025">
  * Add support for removing all permissions for a group/user on an object with a single click
  * Add support for Claude 3.7 Sonnet model
  * Add [llms.txt](https://www.braintrust.dev/llms.txt) for docs content
  * Enable spellcheck for prompt message editors
  * Add support for Anthropic Claude models in Vertex AI
  * Add support for Claude 3.7 Sonnet in Bedrock and Vertex AI
  * Add support for Perplexity R1 1776, Mistral Saba, Gemini LearnLM, and more Groq models
  * Support system instructions in Gemini models
  * Add support for Gemini 2.0 Flash-Lite
  * Add support for default Bedrock cross-region inference profiles in the playground and AI proxy
  * Move score distribution charts to the experiment sidebar
  * Add support for OpenAI GPT-4.5 model in the playground and AI proxy
  * Add deprecation warning for `_parent_id` field in the REST API
  * Add support for stop sequences in Anthropic, Bedrock, and Google models
  * Resolve JSON Schema references when translating structured outputs to Gemini format
  * Add button to copy table cell contents to clipboard
  * Add support for basic Cache-Control headers in the AI proxy
  * Add support for selecting all or none in the categories of permission dialogs
  * Respect Bedrock providers not supporting streaming in the AI proxy
  * Store table grouping, row height, and layout options in the view configuration
  * Add the ability to set a default table view
  * Add support for Google Cloud Vertex AI in the playground and proxy
  * Add default cloud providers section to the organization AI providers page
  * Support streaming responses from OpenAI o1 models in the playground and AI proxy
  * Add complete support for Bedrock models in the playground and AI proxy
  * Fix model provider configuration issues in which custom models could clobber default models
  * Fix bug in streaming JSON responses from non-OpenAI providers
  * Supported templated structured outputs in experiments run from the playground
  * Support structured outputs in the playground and AI proxy for Anthropic models, Bedrock models, and any OpenAI-flavored models that support tool calls
  * Support templated custom headers for custom AI providers
  * Added and updated models across all providers in the playground and AI proxy
  * Support tool usage and structured outputs for Gemini models in the playground and AI proxy
  * Simplify playground model dropdown by showing model variations in a nested dropdown

  ### SDK (version 0.0.187)

  * Added support for handling score values when an Eval has errored
  * Improve support for binary packages in `npx braintrust eval`
  * Support templated structured outputs
  * Fix dataset summary types in Typescript
</Update>

<Update label="January 2025">
  * Add support for duplicating prompts, scorers, and tools
  * Fix pagination for the `/v1/prompt` REST API endpoint
  * "Unreviewed" default view on experiment and logs tables to filter out rows that have been human reviewed
  * Add o3-mini to the AI proxy and playground
  * Scorer dropdown now supports using custom scoring functions across projects
  * Drag and drop to reorder span fields in experiment/log traces and dataset rows
  * Small convenience improvement to the BTQL Sandbox
  * Add an attachments browser to view all attachments for a span in a sidebar
  * Add support for setting a baseline experiment for experiment comparisons
  * UI updates to experiment and log tables
    * Trace audit log now displays granular changes to span data
    * Start/end columns shown as dates/times
    * Non-existent trace records display an error message instead of loading indefinitely
  * Creating an experiment from a playground now correctly renders prompts with `input`, `metadata`, `expected`, and `output` mapped fields
  * The [AI proxy](/guides/proxy) now includes `x-bt-used-endpoint` as a response header
  * Add support for deeplinking to comments within spans
  * In Human Review mode, display all scores in a form
  * Experiment table rows can now be sorted based on score changes and regressions for each group
  * The OTEL endpoint now converts attributes under the `braintrust` namespace directly to the corresponding Braintrust fields
  * New OTEL attributes that accept JSON-serialized values have been added for convenience
  * Experiment tables and individual traces now support comparing trial data between experiments

  ### SDK Integrations: LangChain.js (version 0.0.5)

  * Less noisy logging from the LangChain.js integration
  * You can now pass a `NOOP_SPAN` to the `BraintrustCallbackHandler` to disable logging
  * Fixes a bug where the LangChain.js integration could not handle null/undefined values in chain inputs/outputs

  ### SDK Integrations: LangChain.js (version 0.0.4)

  * Support logging spans from inside evals in the LangChain.js integration

  ### SDK (version 0.0.184)

  * `span.export()` will no longer throw if braintrust is down
  * Improvement to the Python prompt rendering to correctly render formatted messages, LLM tool calls, and other structured outputs

  ### SDK (version 0.0.183)

  * Fix a bug related to `initDataset()` in the Typescript SDK creating links in `Eval()` calls
  * Fix a few type checking issues in the Python SDK

  ### SDK (version 0.0.182)

  * Improved logging for moderation models from the SDK wrappers

  ### SDK (version 0.0.181)

  * Add `ReadonlyAttachment.metadata` helper method to fetch a signed URL for downloading the attachment metadata

  ### SDK (version 0.0.179)

  * New `hook.expected` for reading and updating expected values in the Eval framework
  * Small type improvements for `hook` objects
  * Fixed a bug to enable support for `init_function` with LLM scorers in Python
  * Support nested attachments in Python
  * Add support for imports in Python functions pushed to Braintrust via `braintrust push`

  ### SDK (version 0.0.178)

  * Cache prompts locally in a two-layered memory/disk cache
  * Support for using custom functions that are stored in Braintrust in evals
  * Add support for running traced functions in a `ThreadPoolExecutor` in the Python SDK
  * Improved formatting of spans logged from the Vercel AI SDK's `generateObject` method
  * Default to `asyncFlush: true` in the TypeScript SDK

  ### SDK integrations: LangChain.js (version 0.0.2)

  * Add support for initializing global LangChain callback handler to avoid manually passing the handler to each LangChain object
</Update>

<Update label="December 2024">
  * Add support for free-form human review scores (written to the `metadata` field)
  * Add support for structured outputs in the playground
  * Sparkline charts added to the project home page
  * Better handling of missing data points in monitor charts
  * Clicking on monitor charts now opens a link to traces filtered to the selected time range
  * Add `Endpoint supports streaming` flag to custom provider configuration
  * Experiments chart can be resized vertically by dragging the bottom of the chart
  * BTQL sandbox to explore project data using [Braintrust Query Language](/reference/btql)
  * Add support for updating span data from custom span iframes
  * Significantly speed up loading performance for experiments and logs, especially with lots of spans
    * Searches inside experiments will only work over content in the tabular view, rather than over the full trace
    * While searching on the logs page, realtime updates are disabled
  * Starring rows in experiment and dataset tables now supported
  * "Order by regression" option in experiment column menu can now be toggled on and off without losing previous order
  * Add expanded timeline view for traces
  * Added a 'Request count' chart to the monitor page
  * Add headers to custom provider configuration which the [AI proxy](/guides/proxy) will include in the request to the custom endpoint
  * The logs viewer now supports exporting the currently loaded rows as a CSV or JSON file
  * Experiment columns can now be reordered from the column menu
  * You can now customize legends in monitor charts

  ### Autoevals (version 0.0.110)

  * Python Autoevals now support custom clients when calling evaluators

  ### SDK (version 0.0.179)

  * Add support for imports in Python functions pushed to Braintrust via `braintrust push`

  ### SDK (version 0.0.178)

  * Cache prompts locally in a two-layered memory/disk cache
  * Support for using custom functions that are stored in Braintrust in evals
  * Add support for running traced functions in a `ThreadPoolExecutor` in the Python SDK
  * Improved formatting of spans logged from the Vercel AI SDK's `generateObject` method
  * Default to `asyncFlush: true` in the TypeScript SDK

  ### SDK (version 0.0.177)

  * Support for creating and pushing custom scorers from your codebase with `braintrust push`

  ### SDK (version 0.0.176)

  * New `hook.metadata` for reading and updating Eval metadata when using the `Eval` framework

  ### SDK (version 0.0.175)

  * Fix bug with serializing ReadonlyAttachment in logs

  ### SDK (version 0.0.174)

  * AI SDK fixes: support for image URLs and properly formatted tool calls so "Try prompt" works in the UI

  ### SDK (version 0.0.173)

  * Attachments can now be loaded when iterating an experiment or dataset

  ### SDK (version 0.0.172)

  * Fix a bug where `braintrust eval` did not respect certain configuration options, like `base_experiment_id`
  * Fix a bug where `invoke` in the Python SDK did not properly stream responses

  ### SDK integrations: LangChain.js (version 0.0.1)

  * New LangChain.js integration to export traces from `langchainjs` runs
</Update>

<Update label="November 2024">
  * The Traceloop OTEL integration now uses the input and output attributes to populate the corresponding fields in Braintrust
  * The monitor page now supports querying experiment metrics
  * Removed the `filters` param from the REST API fetch endpoint
  * New experiment summary layout option, a url-friendly view for experiment summaries that respects all filters
  * Add a default limit of 10 to all fetch and `/btql` requests for project\_logs
  * You can now export your prompts from the playground as code snippets and run them through the [AI proxy](/guides/proxy)
  * Support for creating and pushing custom Python tools and prompts from your codebase with `braintrust push`
  * You can now view grouped summary data for all experiments by selecting **Include comparisons in group** from the **Group by** dropdown inside an experiment
  * The experiments page now supports downloading as CSV/JSON
  * Downloading or duplicating a dataset in the UI now properly copies all dataset rows
  * You can now view a score data as a bar chart for your experiments data by selecting **Score comparison** from the X axis selector
  * Trials information is now shown as a separate column in diff mode in the experiment table
  * Cmd/Ctrl + S hotkey to save from prompts in the playground and function dialogs
  * The Braintrust [AI Proxy](/guides/proxy) now supports the [OpenAI Realtime API](https://platform.openai.com/docs/guides/realtime)
  * Add "Group by" functionality to the monitor page
  * The experiment table can now be visualized in a [grid layout](/core/experiments/interpret#grid-layout)
  * 'Select all' button in permission dialogs
  * Create custom columns on dataset, experiment and logs tables from `JSON` values in `input`, `output`, `expected`, or `metadata` fields
  * The Braintrust [AI Proxy](/guides/proxy) can now [issue temporary credentials](/guides/proxy#api-key-management) to access the proxy for a limited time
  * Move experiment score summaries to the table column headers
  * You now receive a clear error message if you run out of free tier capacity while running an experiment from the playground
  * Filters on JSON fields now support array indexing, e.g. `metadata.foo[0] = 'bar'`

  ### SDK (version 0.0.171)

  * Add a `.data` method to the `Attachment` class, which lets you inspect the loaded attachment data

  ### SDK (version 0.0.170)

  * Support uploading [file attachments in the Python SDK](https://www.braintrust.dev/docs/reference/libs/python#attachment-objects)
  * Log, feedback, and dataset inputs to the Python SDK are now synchronously deep-copied for more consistent logging

  ### SDK (version 0.0.169)

  * The Python SDK `Eval()` function has been split into `Eval()` and `EvalAsync()`
  * Improved type annotations in the Python SDK

  ### SDK (version 0.0.168)

  * A new `Span.permalink()` method allows you to format a permalink for the current span
  * `braintrust push` support for Python tools and prompts
  * `initDataset()`/`init_dataset()` used in `Eval()` now tracks the dataset ID and links to each row in the dataset properly

  ### SDK (version 0.0.167)

  * Support uploading [file attachments in the TypeScript SDK](/guides/attachments)
  * Log, feedback, and dataset inputs to the TypeScript SDK are now synchronously deep-copied for more consistent logging
  * Address an issue where the TypeScript SDK could not make connections when running in a Cloudflare Worker
</Update>

<Update label="October 2024">
  * The Monitor page now shows an aggregate view of log scores over time
  * Improvement/Regression filters between experiments are now saved to the URL
  * Add `max_concurrency` and `trial_count` to the playground when kicking off evals
  * Show a button to scroll to a single search result in a span field when using trace search
  * Indicate spans with errors in the trace span list
  * After using "Copy to Dataset" to create a new dataset row, the audit log of the new row now links back to the original experiment, log, or other dataset
  * Tools now stream their `stdout` and `stderr` to the UI
  * Fix prompt, scorer, and tool dropdowns to only show the correct function types
  * The [Github action](/core/experiments/run#github-action) now supports Python runtimes
  * Add support for [Cerebras](https://cerebras.ai/) models in the proxy, playground, and saved prompts
  * You can now create [span iframe viewers](/guides/traces/customize#custom-span-iframes) to visualize span data in a custom iframe
  * `NOT LIKE`, `NOT ILIKE`, `NOT INCLUDES`, and `NOT CONTAINS` supported in BTQL
  * Add "Upload Rows" button to insert rows into an existing dataset from CSV or JSON
  * Add "Maximum" aggregate score type
  * The experiment table now supports grouping by input (for trials) or by a metadata field
  * Gemini models now support multimodal inputs
  * Preview [file attachments](/guides/attachments) in the trace view
  * View and filter by comments in the experiment table
  * Add table row numbers to experiments, logs, and datasets

  ### SDK (version 0.0.166)

  * Allow explicitly specifying git metadata info in the Eval framework

  ### SDK (version 0.0.165)

  * Support specifying dataset-level metadata in `initDataset/init_dataset`

  ### SDK (version 0.0.164)

  * Add `braintrust.permalink` function to create deep links pointing to particular spans in the Braintrust UI

  ### SDK (version 0.0.163)

  * Fix Python SDK compatibility with Python 3.8

  ### SDK (version 0.0.162)

  * Fix Python SDK compatibility with Python 3.9 and older

  ### SDK (version 0.0.161)

  * Add utility function `spanComponentsToObjectId` for resolving the object ID from an exported span slug
</Update>

<Update label="September 2024">
  * Basic monitor page that shows aggregate values for latency, token count, time to first token, and cost for logs
  * Create custom tools to use in your prompts and in the playground
  * Pull your prompts to your codebase using the `braintrust pull` command
  * Select and compare multiple experiments in the experiment view using the `compared with` dropdown
  * The playground now displays aggregate scores (avg/max/min) for each prompt and supports sorting rows by a score
  * Compare span field values side-by-side in the trace viewer when fullscreen and diff mode is enabled
  * The tag picker now includes tags that were added dynamically via API
  * You can now create server-side online evaluations for your logs
  * New member invitations now support being added to multiple permission groups
  * Move datasets and prompts to a new Library navigation tab, and include a list of custom scorers
  * Clean up tree view by truncating the root preview and showing a preview of a node only if collapsed
  * Automatically save changes to table views
  * You can now upload typescript evals from the command line as functions, and then use them in the playground
  * Click a span field line to highlight it and pin it to the URL
  * Copilot tab autocomplete for prompts and data in the Braintrust UI
  * Basic filter UI (no BTQL necessary)
  * Add to dataset dropdown now supports adding to datasets across projects
  * Add REST endpoint for batch-updating ACLs: `/v1/acl/batch_update`
  * Cmd/Ctrl click on a table row to open it in a new tab
  * Show the last 5 basic filters in the filter editor
  * You can now explicitly set and edit prompt slugs
  * Fixed comment deletion
  * You can now use `%` in BTQL queries to represent percent values

  ### Autoevals (version 0.0.86)

  * Add support for Azure OpenAI in node

  ### SDK (version 0.0.160)

  * Fix a bug with `setFetch()` in the TypeScript SDK

  ### SDK (version 0.0.159)

  * In Python, running the CLI with `--verbose` now uses the `INFO` log level
  * Create and push custom tools from your codebase with `braintrust push`
  * You can now pull prompts to your codebase using the `braintrust pull` command

  ### SDK (version 0.0.158)

  * A dedicated `update` method is now available for datasets
  * Fixed a Python-specific error causing experiments to fail initializing when git diff encounters invalid repositories
  * Token counts have the correct units when printing `ExperimentSummary` objects

  ### SDK (version 0.0.157)

  * Enable the `--bundle` flag for `braintrust eval` in the TypeScript SDK

  ### SDK (version 0.0.155)

  * The client wrappers `wrapOpenAI()`/`wrap_openai()` now support [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)
</Update>

<Update label="August 2024">
  * You can now create custom LLM and code (TypeScript and Python) evaluators in the playground
  * Fullscreen trace toggle
  * Datasets now accept JSON file uploads
  * When uploading a CSV/JSON file to a dataset, columns/fields named `input`, `expected`, and `metadata` are now auto-assigned to the corresponding dataset fields
  * Full text search UI for all span contents in a trace
  * New metrics in the UI and summary API: prompt tokens, completion tokens, total tokens, and LLM duration
  * Switching organizations via the header navigates to the same-named project in the selected organization
  * Errors now show up in the trace viewer
  * New cookbook recipe on [benchmarking LLM providers](/cookbook/recipes/ProviderBenchmark)
  * Viewer mode selections will no longer automatically switch to a non-editable view if the field is editable
  * Show `%` in diffs instead of `pp`
  * Add rename, delete and copy current project id actions to the project dropdown
  * Playgrounds can now be shared publicly
  * Duration now reflects the "task" duration not the overall test case duration
  * Duration is now also displayed in the experiment overview table
  * Add support for Fireworks and Lepton inference providers
  * "Jump to" menu to quickly navigate between span sections
  * Speed up queries involving metadata fields using the columnstore backend if it is available
  * Update to include the latest Mistral models in the proxy/playground
  * Categorical human review scores can now be re-ordered via Drag-n-Drop
  * Human review row selection is now a free text field, enabling a quick jump to a specific row

  ### Autoevals (version 0.0.85)

  * LLM calls used in autoevals are now marked with `span_attributes.purpose = "scorer"` so they can be excluded from metric and cost calculations

  ### Autoevals (version 0.0.84)

  * Fix a bug where `rationale` was incorrectly formatted in Python
  * Update the `full` docker deployment configuration to bundle the metadata DB (supabase) inside the main docker compose file

  ### SDK (version 0.0.151)

  * `Eval()` can now take a base experiment. Provide either `baseExperimentName`/`base_experiment_name` or `baseExperimentId`/`base_experiment_id`

  ### SDK (version 0.0.148)

  * While tracing, if your code errors, the error will be logged to the span

  ### SDK (version 0.0.147)

  * `project_name` is now `projectName`, etc. in the `invoke(...)` function in TypeScript
  * `Eval()` return values are printed in a nicer format
  * [`updateSpan()`/`update_span()`](/guides/traces/customize#updating-spans) allows you to update a span's fields after it has been created

  ### SDK (version 0.0.146)

  * Add support for `max_concurrency` in the Python SDK
  * Hill climbing evals that use a `BaseExperiment` as data will use that as the default base experiment
</Update>

<Update label="July 2024">
  * In preparation for auth changes, we are making a series of updates that may affect self-deployed instances
  * Human review scores are now sortable from the project configuration page
  * Streaming support for tool calls in Anthropic models through the proxy and playground
  * The playground now supports different "parsing" modes: `auto`, `parallel`, `raw`, `raw_stream`
  * Table views [can now be saved](/reference/views), persisting the BTQL filters, sorts, and column state
  * Add support for the new `window.ai` model into the playground
  * Use push history when navigating table rows to allow for back button navigation
  * In the experiments list, grouping by a metadata field will group rows in the table as well
  * Allow the trace tree panel to be resized
  * Port the log summary query to BTQL for improved speed
  * Update the experiment progress and experiment score distribution chart layouts
  * Format table column headers with icons
  * Move active filters to the table toolbar
  * Enable RBAC for all users
  * Use btql to power the datasets list, making it significantly faster if you have multiple large datasets
  * Experiments list chart supports click interactions
  * Jump into comparison view between 2 experiments by selecting them in the table an clicking "Compare"
  * Add support for labeling [expected fields using human review](/core/human-review#writing-categorical-scores-to-expected-field)
  * Create and edit descriptions for datasets
  * Create and edit metadata for prompts
  * Click scores and attributes (tree view only) in the trace view to filter by them
  * Highlight the experiments graph to filter down the set of experiments
  * Add support for new models including Claude 3.5 Sonnet
  * Improved empty state and instructions for custom evaluators in the playground
  * Show query examples when filtering/sorting
  * [Custom comparison keys](/core/experiments/interpret#customizing-the-comparison-key) for experiments
  * New model dropdown in the playground/prompt editor that is organized by provider and model type

  ### Autoevals (version 0.0.80)

  * New `ExactMatch` scorer for comparing two values for exact equality

  ### Autoevals (version 0.0.77)

  * Officially switch the default model to be `gpt-4o`
  * Support claude models

  ### Autoevals (version 0.0.76)

  * New `.partial(...)` syntax to initialize a scorer with partial arguments like `criteria` in `ClosedQA`
  * Allow messages to be inserted in the middle of a prompt

  ### SDK (version 0.0.140)

  * New `wrapTraced` function allows you to trace javascript functions in a more ergonomic way

  ### SDK (version 0.0.138)

  * The TypeScript SDK's `Eval()` function now takes a `maxConcurrency` parameter
  * `braintrust install api` now sets up your API and Proxy URL in your environment
  * You can now specify a custom `fetch` implementation in the TypeScript SDK

  ### Deployment

  * The proxy service now supports more advanced functionality which requires setting the `PG_URL` and `REDIS_URL` parameters
</Update>

<Update label="June 2024">
  * You can now collapse the trace tree. It's auto collapsed if you have a single span
  * Improvements to the experiment chart including greyed out lines for inactive scores and improved legend
  * Show diffs when you save a new prompt version
  * You can now see which users are viewing the same traces as you are in real-time
  * Improve whitespace and presentation of diffs in the trace view
  * Show markdown previews in score editor
  * Show cost in spans and display the average cost on experiment summaries and diff views
  * Published a new [Text2SQL eval recipe](/cookbook/recipes/Text2SQL-Data)
  * Add groups view for RBAC
  * Deprecate the legacy dataset format (`output` in place of `expected`) in a new version of the SDK
  * Improve the UX for saving and updating prompts from the playground
  * New hide/show column controls on all tables
  * New [model comparison](/cookbook/recipes/ModelComparison) cookbook recipe
  * Add support for model / metadata comparison on the experiments view
  * New experiment picker dropdown
  * Markdown support in the LLM message viewer
  * Support copying to clipboard from `input`, `output`, etc. views
  * Improve the empty-state experience for datasets
  * New multi-dimensional charts on the experiment page for comparing models and model parameters
  * Support `HTTPS_PROXY`, `HTTP_PROXY`, and `NO_PROXY` environment variables in the API containers
  * Support infinite scroll in the logs viewer and remove dataset size limitations
  * Denser trace view with span durations built in
  * Rework pagination and fix scrolling across multiple pages in the logs viewer
  * Make BTQL the default search method
  * Add support for Bedrock models in the playground and the proxy
  * Add "copy code" buttons throughout the docs
  * Automatically overflow large objects (e.g. experiments) to S3 for faster loading and better performance
  * Show images in LLM view
  * Send an invite email when you invite a new user to your organization
  * Support selecting/deselecting scores in the experiment view
  * Roll out [Braintrust Query Language](/reference/btql) (BTQL) for querying logs and traces
  * Smart relative time labels for dates (`1h ago`, `3d ago`, etc.)
  * Added double quoted string literals support
  * Jump to top button in trace details for easier navigation
  * Fix a race condition in distributed tracing
</Update>

<Update label="May 2024">
  * Incremental support for roles-based access control (RBAC) logic within the API server backend
  * Changed the semantics of experiment initialization with `update=True`
  * Added support for new multimodal models
  * Introduced [REST API for RBAC](/api-reference)
  * Improved AI search and added positive/negative tag filtering in AI search
  * Added functionality for distributed tracing
  * Introduce multimodal support for OpenAI and Anthropic models in the prompt playground and proxy
  * The REST API now gzips responses
  * You can now return dynamic arrays of scores in `Eval()` functions
  * Launched Reporters
  * New coat of paint in the trace view
  * Added support for Clickhouse as an additional storage backend
  * Implemented realtime checks using a WebSocket connection
  * Introduced an API version checker tool
  * Faster optimistic updates for large writes in the UI
  * "Open in playground" now opens a lighter weight modal instead of the full playground
  * Can create a new prompt playground from the prompt viewer
  * Shipped support for [prompt management](/core/functions/prompts)
  * Moved playground sessions to be within projects
  * Allowed customizing proxy and real-time URLs through the web application
  * Improved documentation for Docker deployments
  * Improved folding behavior in data editors
  * Support custom models and endpoint configuration for all providers
  * New add team modal with support for multiple users
  * New information architecture to enable faster project navigation
  * Experiment metadata now visible in the experiments table
  * Improve UI write performance with batching
  * Log filters now apply to *any* span
  * Share button for traces
  * Images now supported in the tree view
  * Show auto scores before manual scores (matching trace) in the table
  * New logo is live!
  * Any span can now submit scores, which automatically average in the trace
  * Improve sidebar scrolling behavior
  * Add AI search for datasets and logs
  * Add tags to the SDK
  * Support viewing and updating metadata on the experiment page
</Update>

<Update label="April 2024">
  * Add support for [tags](/core/logs/write#tags-and-queues)
  * Score fields are now sorted alphabetically
  * Add support for Groq ModuleResolutionKind
  * Improve tree viewer and XML parser
  * New experiment page redesign
  * Support duplicate `Eval` names
  * Fallback to `BRAINTRUST_API_KEY` if `OPENAI_API_KEY` is not set
  * Throw an error if you use `experiment.log` and `experiment.start_span` together
  * Add keyboard shortcuts (j/k/p/n) for navigation
  * Increased tooltip size and delay for better usability
  * Support more viewing modes: HTML, Markdown, and Text
</Update>

<Update label="March 2024">
  * Tons of improvements to the prompt playground
  * Cloudformation now supports more granular RDS configuration
  * Support optional slider params
  * Lots of style improvements for tables
  * Deleting a prompt takes you back to the prompts tab
</Update>

<Update label="February 2024">
  * New [REST API](/api-reference)
  * [Cookbook](/cookbook) of common use cases and examples
  * Support for [custom models](/core/playground#custom-models) in the playground
  * Search now works across spans, not just top-level traces
  * Show creator avatars in the prompt playground
  * Improved UI breadcrumbs and sticky table headers
  * UI improvements to the playground
  * Added an example of closed QA / extra fields
  * New YAML parser and new syntax highlighting colors for data editor
  * Added support for enabling/disabling certain git fields from collection
  * Added new GPT-3.5 and 4 models to the playground
  * Fixed scrolling jitter issue in the playground
  * Made table fields in the prompt playground sticky
</Update>

<Update label="January 2024">
  * Added ability to download dataset as CSV
  * Added YAML support for logging and visualizing traces
  * Added JSON mode in the playground
  * Added span icons and improved readability
  * Enabled shift modifier for selecting multiple rows in Tables
  * Improved tables to allow editing expected fields and moved datasets to trace view
  * Added ability to manually score results in the experiment UI
  * Added comments and audit log in the experiment UI
  * Added ability to upload dataset CSV files in prompt playgrounds
  * Published new [guide for tracing and logging your code](/guides/traces)
  * Added support to download experiment results as CSVs
</Update>

<Update label="December 2023">
  * Dropped the official 2023 Year-in-Review dashboard
  * Improved ergonomics for the Python SDK
    * The `@traced` decorator will automatically log inputs/outputs
    * You no longer need to use context managers to scope experiments or loggers
  * Enable skew protection in frontend deploys
  * Added syntax highlighting in the sidepanel to improve readability
  * Add `jsonl` mode to the eval CLI to log experiment summaries in an easy-to-parse format
  * Released new trials feature to rerun each input multiple times
  * Added ability to run evals in the prompt playground
  * Added support for Gemini and Mistral Platform in AI proxy and playground
  * Enabled the prompt playground and datasets for free users
  * Added Together.ai models including Mixtral to AI Proxy
  * Turned prompts tab on organization view into a list
  * Removed data row limit for the prompt playground
  * Enabled configuration for dark mode and light mode in settings
  * Added automatic logging of a diff if an experiment is run on a repo with uncommitted changes
  * API keys are now scoped to organizations
  * You can now search for experiments by any metadata, including their name, author, or even git metadata
  * Filters are now saved in URL state so you can share a link to a filtered view
  * Improve performance of project page by optimizing API calls
</Update>

<Update label="November 2023">
  * Added experiment search on project view to filter by experiment name
  * Upgraded AI Proxy to support tracking Prometheus metrics
  * Modified Autoevals library to use the [AI proxy](/guides/proxy)
  * Upgraded Python braintrust library to parallelize evals
  * Optimized experiment diff view for performance improvements
  * Added support for new Perplexity models to playground
  * Released [AI proxy](/guides/proxy): access many LLMs using one API w/ caching
  * Added [load balancing endpoints](/guides/proxy#load-balancing) to AI proxy
  * Updated org-level view to show projects and prompt playground sessions
  * Added ability to batch delete experiments
  * Added support for Claude 2.1 in playground
  * Made experiment column resized widths persistent
  * Fixed our libraries including Autoevals to work with OpenAI's new libraries
  * Added support for function calling and tools in our prompt playground
  * Added tabs on a project page for datasets, experiments, etc
  * Improved selectors for diffing and comparison modes on experiment view
  * Added support for new OpenAI models (GPT4 preview, 3.5turbo-1106) in playground
  * Added support for OS models (Mistral, Codellama, Llama2, etc.) in playground using Perplexity's APIs
</Update>

<Update label="October 2023">
  * Improved experiment sidebar to be fully responsive and resizable
  * Improved tooltips within the web UI
  * Multiple performance optimizations and bug fixes
  * Improved prompt playground variable handling and visualization
  * Added time duration statistics per row to experiment summaries
  * [Launched new tracing feature: log and visualize complex LLM chains and executions](/guides/traces)
  * Added a new "text-block" prompt type in the playground
  * Increased default # of rows per page from 10 to 100 for experiments
  * UI fixes and improvements for the side panel and tooltips
  * The experiment dashboard can be customized to show the most relevant charts
  * Performance improvements related to user sessions
  * All experiment loading HTTP requests are 100-200ms faster
  * The prompt playground now supports autocomplete
  * Dataset versions are now displayed on the datasets page
  * Projects in the summary page are now sorted alphabetically
  * Long text fields in logged data can be expanded into scrollable blocks
</Update>

<Update label="September 2023">
  * The Eval framework is now supported in Python!
  * Onboarding and signup flow for new users
  * Switch product font to Inter
  * Big performance improvements for registering experiments (down from \~5s to \<1s)
  * New graph shows aggregate accuracy between experiments for each score
  * Throw errors in the prompt playground if you reference an invalid variable
  * A significant backend database change which significantly improves performance while reducing costs
  * No more record size constraints (previously, strings could be at most 64kb long)
  * New autoevals for numeric diff and JSON diff
  * You can duplicate prompt sessions, prompts, and dataset rows in the prompt playground
  * You can download prompt sessions as JSON files
  * You can adjust model parameters (e.g. temperature) in the prompt playground
  * You can publicly share experiments
  * Datasets now support editing, deleting, adding, and copying rows in the UI
</Update>

<Update label="August 2023">
  * The prompt playground is now live!
  * A new chart shows experiment progress per score over time
  * The eval CLI now supports `--watch`, which will automatically re-run your evaluation
  * You can now edit datasets in the UI
  * Introducing datasets! You can now upload datasets to Braintrust and use them in your experiments
  * Fix several performance issues in the SDK and UI
  * Complex data is now substantially more performant in the UI
  * The UI updates in real-time as new records are logged to experiments
  * Ergonomic improvements to the SDK and CLI
    * The JS library is now Isomorphic and supports both Node.js and the browser
    * The Evals CLI warns you when no files match the `.eval.[ts|js]` pattern
</Update>

<Update label="July 2023">
  * You can now break down scores by metadata fields
  * Improve performance for experiment loading (especially complex experiments)
  * Support for renaming and deleting experiments
  * When you expand a cell in detail view, the row is now highlighted
  * A new [framework](/core/experiments) for expressing evaluations in a much simpler way
  * `inputs` is now `input` in the SDK (>= 0.0.23) and UI
  * Improved diffing behavior for nested arrays
  * SDK updates that allow you to update an existing experiment `init(..., update=True)` and specify an id in `log(..., id='my-custom-id')`
  * Tables with lots and lots of columns are now visually more compact in the UI
  * A new Node.js SDK which mirrors the Python SDK
  * You can now swap the primary and comparison experiment with a single click
  * You can now compare `output` vs. `expected` within an experiment
  * Version 0.0.19 is out for the SDK
  * Support for real-time updates, using Redis
  * New settings page that consolidates team, installation, and API key settings
  * The experiment page now shows commit information for experiments run inside of a git repository
</Update>

<Update label="June 2023">
  * Experiments track their git metadata and automatically find a "base" experiment to compare against
  * The Python SDK's `summarize()` method now returns an `ExperimentSummary` object with score differences
  * Organizations can now be "multi-tenant"
  * New scatter plot and histogram insights to quickly analyze scores and filter down examples
  * API keys that can be set in the SDK and do not require user login
  * Improved performance for event logging in the SDK
  * Auto-merge experiment fields with different types
  * Tutorial guide + notebook
  * Automatically refresh cognito tokens in the Python client
  * New filter and sort operators on the experiments table
  * SQL query explorer to run arbitrary queries against one or more experiments
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt