# Source: https://www.elastic.co/docs/release-notes/cloud-serverless

﻿---
title: Elastic Cloud Serverless changelog
description: Review the changes, fixes, and more to Elastic Cloud Serverless. Adds a new line-optimized color palette for line charts in Lens #253437, Adds sort order...
url: https://www.elastic.co/docs/release-notes/cloud-serverless
products:
  - Elastic Cloud Serverless
---

# Elastic Cloud Serverless changelog
Review the changes, fixes, and more to Elastic Cloud Serverless.

## March 2, 2026


### Features and enhancements

- Adds a new line-optimized color palette for line charts in Lens [#253437](https://github.com/elastic/kibana/pull/253437)
- Adds sort order controls for heatmap visualization axes [#244696](https://github.com/elastic/kibana/pull/244696)
- Adds library support for the Markdown embeddable panel [#248779](https://github.com/elastic/kibana/pull/248779)
- Adds a borderless option to the panel settings [#255021](https://github.com/elastic/kibana/pull/255021)
- Displays warnings for deprecated integration features [#253923](https://github.com/elastic/kibana/pull/253923)
- Adds an out-of-the-box alerting rule template to newly installed integrations for monitoring idle data streams [#254730](https://github.com/elastic/kibana/pull/254730)
- Adds an **Alerting** tab to the integrations UI for viewing and managing alerting-related assets [#253948](https://github.com/elastic/kibana/pull/253948)
- Enables dashboard and URL drilldowns for ES|QL charts in Lens [#253223](https://github.com/elastic/kibana/pull/253223)
- Simplifies the ES|QL query button states to show **Search** or **Cancel** with consistent styling [#254121](https://github.com/elastic/kibana/pull/254121)
- Improves the commenting and uncommenting behavior in the ES|QL editor to match standard IDE conventions [#254851](https://github.com/elastic/kibana/pull/254851)
- Adds an EUI Tour to the Tab menu for switching between classic and ES|QL modes [#254183](https://github.com/elastic/kibana/pull/254183)
- Adds notifications when background searches complete [#249857](https://github.com/elastic/kibana/pull/249857)
- Reduces the private location monitors sync task interval and makes it configurable [#252708](https://github.com/elastic/kibana/pull/252708)
- Improves the maintenance window callout for private location monitors [#252847](https://github.com/elastic/kibana/pull/252847)
- Replaces the legacy waterfall component with the new unified trace waterfall in APM, supporting unprocessed OpenTelemetry data [#248629](https://github.com/elastic/kibana/pull/248629)
- Adds error handling to the Observability landing page to prevent stalled navigation when status checks fail [#254171](https://github.com/elastic/kibana/pull/254171)
- Adds an entity analytics skill to Agent Builder for answering risk score questions about users and hosts [#252400](https://github.com/elastic/kibana/pull/252400)
- Adds a space ID filter in **Advanced Settings** [#247733](https://github.com/elastic/kibana/pull/247733)
- Adds the ability to configure a space-level default project routing expression in the **Space Management** UI [#250990](https://github.com/elastic/kibana/pull/250990)
- Adds the Gemini 2.5 Flash Lite, Claude 4.5 Haiku, and Claude 4.6 Sonnet preconfigured connectors [#253109](https://github.com/elastic/kibana/pull/253109)
- Redesigns dashboard panel titles with updated margins, reduced font weight, and a teal hover color [#251720](https://github.com/elastic/kibana/pull/251720)
- Improves the **Inference endpoints** management page by adding a view to group endpoints by service [#254296](https://github.com/elastic/kibana/pull/254296)
- Adds a server-side workflow validation endpoint [#254502](https://github.com/elastic/kibana/pull/254502)
- Adds Streams APIs as allowed Kibana workflow steps [#252068](https://github.com/elastic/kibana/pull/252068)
- Adds Cases workflow steps [#253119](https://github.com/elastic/kibana/pull/253119)
- Defaults to a line chart when dropping a timestamp field into the Lens workspace [#253930](https://github.com/elastic/kibana/pull/253930)
- Adds table borders to metadata and dimensions in the **View details** flyout [#252329](https://github.com/elastic/kibana/pull/252329)
- Respects the `observability:enableInspectEsQueries` setting in the **Hosts** UI [#253618](https://github.com/elastic/kibana/pull/253618)
- Connects the fields list breakdown with the dimensions breakdown in Discover [#248920](https://github.com/elastic/kibana/pull/248920)
- Adds server-side support for user-created skills in Agent Builder [#252493](https://github.com/elastic/kibana/pull/252493)
- Adds agent and tools RBAC subfeature privileges [#254464](https://github.com/elastic/kibana/pull/254464)


### Fixes

- Fixes uncaught errors from `scheduleUnusedUrlsCleanupTask()` [#254574](https://github.com/elastic/kibana/pull/254574)
- Fixes a blank page appearing at the end of PDF exports when using the **Print format** option with an even number of dashboard visualizations [#254957](https://github.com/elastic/kibana/pull/254957)
- Fixes report generation failing with multi-page Canvas workpads [#255022](https://github.com/elastic/kibana/pull/255022)
- Fixes the dashboard background color not displaying correctly [#253068](https://github.com/elastic/kibana/pull/253068)
- Removes mode from stored `timeRange` to prevent schema validation errors [#255178](https://github.com/elastic/kibana/pull/255178)
- Filters out unenrolled agents in the cleanup policy revisions task [#254899](https://github.com/elastic/kibana/pull/254899)
- Fixes incorrect KQL bar results for some indices [#254119](https://github.com/elastic/kibana/pull/254119)
- Aborts in-flight long-running queries when navigating away [#254487](https://github.com/elastic/kibana/pull/254487)
- Resets the default profile state when transitioning between tab modes in Discover [#255226](https://github.com/elastic/kibana/pull/255226)
- Marks ES|QL rule execution errors as user-triggered for improved error reporting [#255011](https://github.com/elastic/kibana/pull/255011)
- Fixes the annotation API on Elastic Cloud Serverless [#254285](https://github.com/elastic/kibana/pull/254285)
- Passes the alerts data view to `buildEsQuery` for correct wildcard queries on keyword fields [#255225](https://github.com/elastic/kibana/pull/255225)
- Fixes alert visibility and filters for grouped SLOs on the details page [#254601](https://github.com/elastic/kibana/pull/254601)
- Falls back to the Elasticsearch API key when granting the Unified Identity and Access Management (UIAM) API key fails [#254707](https://github.com/elastic/kibana/pull/254707)
- Fixes the notes filtering logic to show notes attached to alerts, events, and timelines [#248110](https://github.com/elastic/kibana/pull/248110)
- Standardizes and persists the rows-per-page preference across tables [#253499](https://github.com/elastic/kibana/pull/253499)
- Enables `defaultModel` for the Azure OpenAI connector to support Azure API Management (APIM) endpoints [#253577](https://github.com/elastic/kibana/pull/253577)
- Fixes an issue where the analyzer was not showing when the `newDataViewPickerEnabled` feature flag was turned off [#255182](https://github.com/elastic/kibana/pull/255182)
- Prevents the embeddable console from auto-closing on Chrome or overlay clicks [#253382](https://github.com/elastic/kibana/pull/253382)
- Fixes API key pagination to handle more than 10,000 keys [#250826](https://github.com/elastic/kibana/pull/250826)
- Fixes an issue where the AI Connector inference endpoint creation failed when adaptive allocations were enabled and the `elasticsearch` provider was used [#251357](https://github.com/elastic/kibana/pull/251357)
- Fixes the trace sample title wrapping vertically in APM [#254536](https://github.com/elastic/kibana/pull/254536)
- Fixes dashboard scanning to include collapsible sections when fetching related dashboards [#254600](https://github.com/elastic/kibana/pull/254600)
- Updates the metrics flyout in Discover to use ES|QL instead of SQL [#254537](https://github.com/elastic/kibana/pull/254537)
- Fixes focus management when entering full-screen mode in the metrics grid [#254701](https://github.com/elastic/kibana/pull/254701)
- Propagates inference errors correctly to users [#254815](https://github.com/elastic/kibana/pull/254815)
- Prevents the Workflows table from re-sorting when toggling a workflow's enabled state [#252724](https://github.com/elastic/kibana/pull/252724)
- Fixes the dimensions dropdown position in full-screen mode [#255049](https://github.com/elastic/kibana/pull/255049)
- Fixes false validation errors for template-local variables in Liquid templates [#253405](https://github.com/elastic/kibana/pull/253405)
- Fixes a rendering issue where the **Attributes** tab in the Doc Viewer flyout showed erratic scroll behavior [#255173](https://github.com/elastic/kibana/pull/255173)
- Fixes out-of-memory crashes and Kibana restarts caused by the gap auto-fill scheduler creating excessively large saved objects [#254788](https://github.com/elastic/kibana/pull/254788)
- Fixes a race condition in the Streams data quality controller that caused incorrect Discover navigation [#254139](https://github.com/elastic/kibana/pull/254139)
- Fixes the processor name overlapping the badge in streams [#251874](https://github.com/elastic/kibana/pull/251874)


## February 23, 2026


### Features and enhancements

- Adds four new Microsoft Azure [regions](https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud/regions) for Elastic Cloud Serverless:
  - East US 2 (`eastus2`) located in Virginia
- Germany West Central (`germanywestcentral`) located in Frankfurt
- Southeast Asia (`southeastasia`) located in Singapore
- Spain Central (`spaincentral`) located in Madrid
- Shows warnings in the UI when an integration is deprecated, including badges, callout messages, and tooltip icons [#251860](https://github.com/elastic/kibana/pull/251860)
- Allows integration rollback even when not all integration policies have been upgraded [#253646](https://github.com/elastic/kibana/pull/253646)
- Redesigns the ES|QL editor with a new menu for query history, help, and starring, and repositions the date picker, run button, and keyboard shortcuts [#251223](https://github.com/elastic/kibana/pull/251223)
- Adds the ability to acknowledge and unacknowledge alerts directly from the alerts table, with audit logging for workflow status transitions [#252945](https://github.com/elastic/kibana/pull/252945)
- Adds SLO and Service entity attachments to Agent Builder, enabling entity-grounded conversations with automatic context fetching [#252390](https://github.com/elastic/kibana/pull/252390)
- Adds high-level rule execution info logging to the **Execution events** tab, showing matched events, alerts created, and suppressed alert counts [#253992](https://github.com/elastic/kibana/pull/253992)
- Moves rule summary, definition, and schedule into a dedicated **Overview** tab on the rule details page, and surfaces alerts, exceptions, results, and events at the top of the page [#251662](https://github.com/elastic/kibana/pull/251662)
- Adds support for fetching entity relationships in the **Entity Graph API**, including ownership, supervision, dependency, and access patterns [#251178](https://github.com/elastic/kibana/pull/251178)
- Enables Splunk v2 dashboard parsing in Automatic Migrations [#253970](https://github.com/elastic/kibana/pull/253970)
- Adds a **Show entity relationships** action to entity node popovers in the graph visualization [#252803](https://github.com/elastic/kibana/pull/252803)
- Adds a dynamic default connector fallback in **GenAI Settings** that automatically selects a preferred connector when no default is configured [#252861](https://github.com/elastic/kibana/pull/252861)
- Replaces custom agent icons with the standard EUI `productAgent` icon across all solutions [#252526](https://github.com/elastic/kibana/pull/252526)
- Adds a network direction processor to Streams that calculates traffic direction from source and destination IP addresses [#250894](https://github.com/elastic/kibana/pull/250894)
- Improves condition filtering in Streams data enrichment with match-rate badges and the ability to filter simulation results by condition [#251129](https://github.com/elastic/kibana/pull/251129)
- Improves the **Inference Endpoints** management page by adding a view to group endpoints by model, and makes this the default view [#252984](https://github.com/elastic/kibana/pull/252984)
- Displays a warning callout on the **Rules** page when the gap auto-fill scheduler encounters errors, with a link to the scheduler logs [#250393](https://github.com/elastic/kibana/pull/250393)
- Migrates Agent Builder from a flyout to the sidebar API for a more consistent experience [#252918](https://github.com/elastic/kibana/pull/252918)
- Adds pre-execution workflows to Agent Builder, enabling agents to run one or more workflows before each execution to modify prompts or cancel the agent run [#252452](https://github.com/elastic/kibana/pull/252452)
- Adds a Slack data source for Workplace AI with message search and send capabilities [#252972](https://github.com/elastic/kibana/pull/252972)
- Supports multi-dimension breakdowns in Lens series layers, allowing up to five dimensions in the **Discover** dimension dropdown [#251731](https://github.com/elastic/kibana/pull/251731)
- Adds a `get_traces` tool to the Observability AI agent for retrieving distributed trace samples, including transactions, spans, errors, and correlated logs [#250952](https://github.com/elastic/kibana/pull/250952)
- Adds host infrastructure metrics and service correlation to Alert AI Insights, improving root cause analysis for both APM and infrastructure alerts [#252973](https://github.com/elastic/kibana/pull/252973)
- Adds a `get_service_topology` tool to the Observability AI agent for retrieving service dependencies with latency, throughput, and error rate metrics [#251770](https://github.com/elastic/kibana/pull/251770)
- Adds OpenTelemetry entity support to the APM **Infrastructure** tab for Kubernetes pods, Kubernetes containers, and Docker containers [#252188](https://github.com/elastic/kibana/pull/252188)
- Reduces output tokens for the `get_anomaly_detection_jobs` tool by lowering default limits and adding filtering parameters for anomaly score, job group, and influencer [#251415](https://github.com/elastic/kibana/pull/251415)
- Adds support for ECS-formatted error documents in the APM service details **Errors** tab, properly displaying `error.message` and `error.type` fields [#254138](https://github.com/elastic/kibana/pull/254138)


### Fixes

- Fixes a bug with PagerDuty where setting the **Custom details** field caused rules to fail [#253683](https://github.com/elastic/kibana/pull/253683)
- Fixes config panel scrolling in the Lens editor so that all configuration options are accessible when content exceeds the visible area [#253247](https://github.com/elastic/kibana/pull/253247)
- Fixes overly restrictive filter `meta.value` validation that rejected valid phrase and range filter values [#253537](https://github.com/elastic/kibana/pull/253537)
- Fixes an issue where an agent that was rolled back after an upgrade could not be upgraded again in the Fleet UI [#253850](https://github.com/elastic/kibana/pull/253850)
- Fixes incorrect ES|QL validation of the `TS` (time series) command that was wrongly applying `FROM` command rules [#253635](https://github.com/elastic/kibana/pull/253635)
- Fixes the Synthetics monitor toggle state leaking between monitors in the details flyout when switching between different monitors [#253314](https://github.com/elastic/kibana/pull/253314)
- Speeds up bulk rule deletion, significantly reducing the time to delete large numbers of prebuilt rules [#253116](https://github.com/elastic/kibana/pull/253116)
- Fixes Comprehensive File Timeline template filters to combine with AND instead of OR [#251242](https://github.com/elastic/kibana/pull/251242)
- Adds an optional `region` field to the Amazon Bedrock connector, fixing SigV4 request signing for custom endpoint domains [#252960](https://github.com/elastic/kibana/pull/252960)
- Fixes rule details **Overview** tab responsiveness, preventing overflow of MITRE ATT&CK fields on narrow viewports [#252890](https://github.com/elastic/kibana/pull/252890)
- Fixes the legacy `rules/prepackaged` endpoints from returning 500 errors on a Basic license when rules include machine learning rules [#253574](https://github.com/elastic/kibana/pull/253574)
- Fixes **Today** and **This week** time filters for Log Rate Analysis and Log Pattern Analysis embeddables on dashboards [#252925](https://github.com/elastic/kibana/pull/252925)
- Fixes autocomplete not working in the embedded console [#253306](https://github.com/elastic/kibana/pull/253306)
- Fixes an error in the Streams AI pipeline suggestions when generated grok patterns contain empty strings [#251113](https://github.com/elastic/kibana/pull/251113)
- Fixes the refresh button in the Streams app query bar not triggering a data refetch [#253295](https://github.com/elastic/kibana/pull/253295)
- Fixes ML inference pipeline operations failing due to system-managed date fields introduced in Elasticsearch 9.2 [#252579](https://github.com/elastic/kibana/pull/252579)
- Includes external reference IDs in the attached documents check when selecting cases [#253107](https://github.com/elastic/kibana/pull/253107)
- Fixes Beats tutorial authentication instructions in Elastic Cloud Serverless to show the correct API key-based configuration instead of unsupported `cloud.id`/`cloud.auth` instructions [#253164](https://github.com/elastic/kibana/pull/253164)
- Fixes a bug in Vega where `runtime_mappings` defined in `data[].url.body` were ignored or overridden [#253560](https://github.com/elastic/kibana/pull/253560)
- Adds parameter validation to the **Entity store install API**, including KQL filter validation, index pattern checks, and minimum frequency enforcement [#252366](https://github.com/elastic/kibana/pull/252366)
- Fixes execution tree rendering where steps after a large `foreach` loop were hidden or overlapped after collapsing and re-expanding the loop [#253576](https://github.com/elastic/kibana/pull/253576)
- Fixes scrollbar colors in Safari when the macOS appearance setting is the opposite of the selected Kibana color mode [#253484](https://github.com/elastic/kibana/pull/253484)


## February 16, 2026


### Features and enhancements

- Suggests lines for time series queries in Lens [#252661](https://github.com/elastic/kibana/pull/252661)
- Adds an alerting rule template to newly installed integration packages for inactivity monitoring [#252546](https://github.com/elastic/kibana/pull/252546)
- Adds authentication fields to Elastic Agent binary download sources managed by Fleet to support connecting to self-hosted artifact registries [#250557](https://github.com/elastic/kibana/pull/250557)
- Persists query mode to local storage [#250388](https://github.com/elastic/kibana/pull/250388)
- Makes the `RERANK` command generally available [#252242](https://github.com/elastic/kibana/pull/252242)
- Uses a restorable state in the doc viewer's **JSON** tab [#252054](https://github.com/elastic/kibana/pull/252054)
- Adds a **View in Discover** link to APM rule-based alert details to view related documents in Discover [#248990](https://github.com/elastic/kibana/pull/248990)
- Adds `get_runtime_metrics` tool [#251768](https://github.com/elastic/kibana/pull/251768)
- Adds support for duplicating packs and saved queries in the osquery plugin [#252517](https://github.com/elastic/kibana/pull/252517)
- Improves the **User** and **Host** entity details flyouts to show a skeleton loading state for observed data [#252657](https://github.com/elastic/kibana/pull/252657)
- Adds an Anthropic Claude Opus 4.6 preconfigured connector [#252177](https://github.com/elastic/kibana/pull/252177)
- Adds **Zoom in** button to the date picker [#252252](https://github.com/elastic/kibana/pull/252252)
- Adds a new `redact` processor [#250389](https://github.com/elastic/kibana/pull/250389)
- Adds a summary statistics bar to the Inference endpoints page to show counts of services, models, types, and endpoints [#251558](https://github.com/elastic/kibana/pull/251558)
- Adds sorting capabilities to the Inference endpoints page to sort by endpoint, service, type, or model [#252189](https://github.com/elastic/kibana/pull/252189)
- Consolidates badges under the endpoint name and removes the Type column on the Inference endpoints page [#252621](https://github.com/elastic/kibana/pull/252621)
- Adds support for multi-dimension breakdowns [#250727](https://github.com/elastic/kibana/pull/250727)
- Adds a data source browser to the ES|QL editor [#251897](https://github.com/elastic/kibana/pull/251897)
- Adds a Jira Cloud data source [#251345](https://github.com/elastic/kibana/pull/251345)
- Adds a fields browser to the ES|QL editor in Discover [#252749](https://github.com/elastic/kibana/pull/252749)
- Migrates metrics in Discover flyout to the new flyout system [#251395](https://github.com/elastic/kibana/pull/251395)
- Adds audit logging for agent and tool actions [#252143](https://github.com/elastic/kibana/pull/252143)
- Allows sorting and retrieving latency percentiles in the `get_trace_metrics` tool [#249488](https://github.com/elastic/kibana/pull/249488)
- Adds the **Indexing Tier** view to AutoOps for Elastic Cloud Serverless, which provides insights into indexing performance and ingest VCU usage.


### Fixes

- Fixes rule execution failing due to null execution UUIDs [#252618](https://github.com/elastic/kibana/pull/252618)
- Adjusts the horizontal link panel height to two rows [#252707](https://github.com/elastic/kibana/pull/252707)
- Fixes `TypeError` when an integration has no SVG icons [#251308](https://github.com/elastic/kibana/pull/251308)
- Restores support for generating CSV reports of Fleet agent data in Serverless environments [#247185](https://github.com/elastic/kibana/pull/247185)
- Fixes handling of missing values [#251892](https://github.com/elastic/kibana/pull/251892)
- Applies integration limit check after the deduplication step in `parseIntegrationsTSV` [#252486](https://github.com/elastic/kibana/pull/252486)
- Fixes accessibility issues in the **Confirm delete** modal [#251962](https://github.com/elastic/kibana/pull/251962)
- Updates the OpenAI connector to use `labelAppend` to indicate optional fields [#251857](https://github.com/elastic/kibana/pull/251857)
- Replaces the deprecated `listAdd` icon with `indexOpen` icon [#251930](https://github.com/elastic/kibana/pull/251930)
- Excludes failed rules from non-failed status filters [#252263](https://github.com/elastic/kibana/pull/252263)
- Updates the rule management APIs to ensure that response actions are validated [#251352](https://github.com/elastic/kibana/pull/251352)
- Adds an option to update mappings with index patterns instead of individual indices [#252431](https://github.com/elastic/kibana/pull/252431)
- Adds `region` to the Amazon Bedrock connector schema [#252956](https://github.com/elastic/kibana/pull/252956)
- Fixes file size limit checks in file uploads [#251515](https://github.com/elastic/kibana/pull/251515)
- Fixes document count loading in the Index Management UI when using larger page sizes with long index names [#252422](https://github.com/elastic/kibana/pull/252422)
- Improves the tooltip for missing trace/span relationships in APM [#251850](https://github.com/elastic/kibana/pull/251850)
- Propagates connector API errors [#252372](https://github.com/elastic/kibana/pull/252372)
- Fixes a UI issue with the workflow tool type [#252563](https://github.com/elastic/kibana/pull/252563)
- Fixes an issue with the Create new tool page when switching tool types [#252811](https://github.com/elastic/kibana/pull/252811)
- Adds datemath support to the KQL evaluator [#252840](https://github.com/elastic/kibana/pull/252840)


## February 9, 2026


### Features and enhancements

- Allows you to search IP fields in controls using CIDR (Classless Inter-Domain Routing) notation [#250875](https://github.com/elastic/kibana/pull/250875)
- Makes `contains` the default search technique for the options list [#250992](https://github.com/elastic/kibana/pull/250992)
- Allows you to drag panels while they're in focus for editing [#251327](https://github.com/elastic/kibana/pull/251327)
- Allows Fleet to install integration-managed SLO templates [#250369](https://github.com/elastic/kibana/pull/250369)
- Adds the By Value editing flow for Discover embeddable widgets [#250438](https://github.com/elastic/kibana/pull/250438)
- Adds timezone support in ES|QL [#247917](https://github.com/elastic/kibana/pull/247917)
- Adds query stats in Lens [#251029](https://github.com/elastic/kibana/pull/251029)
- Uses restorable state in doc viewer's **Table** tab [#249682](https://github.com/elastic/kibana/pull/249682)
- Adds health scans for SLOs to allow cluster-wide analysis of SLO operational health [#248004](https://github.com/elastic/kibana/pull/248004)
- Adds support for KQL filtering in all types of aggregations in custom threshold rules [#248845](https://github.com/elastic/kibana/pull/248845)
- Introduces AI-assisted detection rule creation [#247674](https://github.com/elastic/kibana/pull/247674)
- Adds support for v2 Splunk dashboards to Automatic Migration [#251199](https://github.com/elastic/kibana/pull/251199)
- Updates the `fast-xml-parser` package dependencies [#251644](https://github.com/elastic/kibana/pull/251644)
- Adds a user feedback plugin [#225074](https://github.com/elastic/kibana/pull/225074)
- Adds `maxSize` for entries in security endpoints related API schemas [#246359](https://github.com/elastic/kibana/pull/246359)
- Opens matching pattern docs in a new Discover tab [#245695](https://github.com/elastic/kibana/pull/245695)
- Adds missing ES|QL commands and functions documentation for inference tasks [#249089](https://github.com/elastic/kibana/pull/249089)
- Refreshes the machine learning Overview page [#247573](https://github.com/elastic/kibana/pull/247573)
- Adds the `xpack.productDocBase.artifactRepositoryProxyUrl` setting to `kibana.yml` [#250771](https://github.com/elastic/kibana/pull/250771)
- Adds a copy-to-clipboard button next to inference endpoint names in the Inference endpoints page [#251494](https://github.com/elastic/kibana/pull/251494)
- Adds a default model suggestion to AI Connector configuration menus [#250506](https://github.com/elastic/kibana/pull/250506)
- Adds descriptions to the inference endpoint selection interface for the `semantic_text` field [#249265](https://github.com/elastic/kibana/pull/249265)
- Introduces the SharePoint Online Data Source definition and related built-in workflow YAML files [#251544](https://github.com/elastic/kibana/pull/251544)
- Adds support for array parameter types in ES|QL tools [#250386](https://github.com/elastic/kibana/pull/250386)
- Enhances `get_log_groups` (formerly `get_log_categories`) with exceptions [#250331](https://github.com/elastic/kibana/pull/250331).
- Adds asymmetric quantization of DiskBBQ centroids to improve query latency [#141137](https://github.com/elastic/elasticsearch/pull/141137)
- Improves handling of preconfigured Inference API endpoints with embedding task type [#141788](https://github.com/elastic/elasticsearch/pull/141788)
- Adds multimodal embedding task support to Elastic Inference Service (EIS) [#141547](https://github.com/elastic/elasticsearch/pull/141547)
- Adds `SlowCustomBinaryDocValuesTermInSetQuery` to replace separate term queries in `TextFieldMapper` [#141891](https://github.com/elastic/elasticsearch/pull/141891)
- Adds support for `doc_values` to text fields [#141225](https://github.com/elastic/elasticsearch/pull/141225)
- Adds `task_settings` to the ES|QL `COMPLETION` command [#140613](https://github.com/elastic/elasticsearch/pull/140613)
- Adds count aggregation for histograms [#141138](https://github.com/elastic/elasticsearch/pull/141138)
- Blocks DiskBBQ encode doc vectors [#141598](https://github.com/elastic/elasticsearch/pull/141598)
- Adds multi-value field support to the ES|QL `CHUNK` function [#141240](https://github.com/elastic/elasticsearch/pull/141240)
- Adds APM telemetry for the ES|QL `SET` command [#141719](https://github.com/elastic/elasticsearch/pull/141719)
- Adds logic to fold project tags metadata on data nodes [#141935](https://github.com/elastic/elasticsearch/pull/141935)
- Adds a warning for `SORT` under `LOOKUP JOIN` [#141482](https://github.com/elastic/elasticsearch/pull/141482)
- Adds failure store support for cross-cluster search (CCS) [#139760](https://github.com/elastic/elasticsearch/pull/139760)
- Makes the `TDigest` field a time series metric [#141386](https://github.com/elastic/elasticsearch/pull/141386)
- Optimizes search shard iterator sorting [#140747](https://github.com/elastic/elasticsearch/pull/140747)
- Optimizes `TopNOperator` when the input is already sorted [#141094](https://github.com/elastic/elasticsearch/pull/141094)


### Fixes

- Excludes QRadar building-block rules from migration eligibility [#250558](https://github.com/elastic/kibana/pull/250558)
- Fixes KQL character escaping for queries generated from the Top values column in Lens [#250925](https://github.com/elastic/kibana/pull/250925)
- Fixes `COMPLETION` quick help syntax [#251939](https://github.com/elastic/kibana/pull/251939)
- Fixes SLO filter containing spaces and wildcards [#251033](https://github.com/elastic/kibana/pull/251033)
- Fixes shared exception list showing ID instead of name [#249778](https://github.com/elastic/kibana/pull/249778)
- Fixes backslash being removed when typed into the exception field [#250117](https://github.com/elastic/kibana/pull/250117)
- Fixes `spaceId` in Agent Builder security tools [#251513](https://github.com/elastic/kibana/pull/251513)
- Fixes exception list `os_types` field returning empty array [#250279](https://github.com/elastic/kibana/pull/250279)
- Fixes an accessibility issue caused by a missing label in a flyout component [#251656](https://github.com/elastic/kibana/pull/251656)
- Fixes ARIA announcement issue in the **Add exception list** dialog [#250624](https://github.com/elastic/kibana/pull/250624)
- Fixes an issue where a timeline automatically opened when navigating to the Network page [#250469](https://github.com/elastic/kibana/pull/250469)
- Fixes flyout section local storage not honoring all values [#251999](https://github.com/elastic/kibana/pull/251999)
- Fixes a rounding issue in the share feature [#251073](https://github.com/elastic/kibana/pull/251073)
- Hides links on the Search homepage for users without access [#251437](https://github.com/elastic/kibana/pull/251437)
- Adds a badge to the Agent Builder UI when your license doesn't support it [#251484](https://github.com/elastic/kibana/pull/251484)
- Reduces background polling on the index details page to avoid unnecessary API requests [#251446](https://github.com/elastic/kibana/pull/251446)
- Fixes pagination dimensions list in Discover flyouts [#251250](https://github.com/elastic/kibana/pull/251250)
- Improves handling of 204 responses to Cases webhooks [#251090](https://github.com/elastic/kibana/pull/251090)
- Fixes ES|QL test tool failing when the numerical value is zero [#251901](https://github.com/elastic/kibana/pull/251901)
- Fixes document flyout loading loop with relative time ranges [#251647](https://github.com/elastic/kibana/pull/251647)
- Fixes Agent Builder index search support for special text fields `match_only_text` and `pattern_text` [#252082](https://github.com/elastic/kibana/pull/252082)
- Improves errors on some ES|QL queries missing timestamps [#141503](https://github.com/elastic/elasticsearch/pull/141503)
- Fixes ES|QL bug when grouping on aliases [#141568](https://github.com/elastic/elasticsearch/pull/141568)
- Extends the `read` index privilege to consistently cover all actions required to run cross-cluster search queries [#141376](https://github.com/elastic/elasticsearch/pull/141376)
- Adds validation to inference update operation [#140003](https://github.com/elastic/elasticsearch/pull/140003)
- Fixes the parsing of `TO_IP(input, {"leading_zeros":"octal"})` in ES|QL [#141776](https://github.com/elastic/elasticsearch/pull/141776)
- Prevents a possible null point exception in ES|QL [#141711](https://github.com/elastic/elasticsearch/pull/141711)
- Improves handling of duplicate ES|QL doc IDs [#142055](https://github.com/elastic/elasticsearch/pull/142055)
- Fixes the ES|QL `IP_PREFIX` function leaking data in scratch [#141940](https://github.com/elastic/elasticsearch/pull/141940)
- Prevents ES|QL from reusing `BlockLoad.ColumnAtATimeReader` when loading many fields at once [#141672](https://github.com/elastic/elasticsearch/pull/141672)Stops
- Fixes build failure due to merge collision [#141722](https://github.com/elastic/elasticsearch/pull/141722)
- Fixes downsampling configuration validation [#141873](https://github.com/elastic/elasticsearch/pull/141873)
- Fixes handling of empty collapse construct [#141973](https://github.com/elastic/elasticsearch/pull/141973)
- Allows shadowing of time-series parameters in non-time-series mappings [#141549](https://github.com/elastic/elasticsearch/pull/141549)
- Fixes top hits counts when sorting across indices [#142046](https://github.com/elastic/elasticsearch/pull/142046)
- Fixes typo in ARM `int2int4` bulk implementation [#141813](https://github.com/elastic/elasticsearch/pull/141813)
- Improves mutability handling of `Source#source()`'s map [#141534](https://github.com/elastic/elasticsearch/pull/141534)
- Prevents large `CancelTasksRequest` descriptions by truncating nodes and actions [#141815](https://github.com/elastic/elasticsearch/pull/141815)
- Reduces cancellation check interval in `CancellableBulkScorer` for better responsiveness [#141747](https://github.com/elastic/elasticsearch/pull/141747)
- Refreshes SQL PIT ID after each response [#141736](https://github.com/elastic/elasticsearch/pull/141736)
- Updates constant-value fields to support normalized wildcard queries [#141784](https://github.com/elastic/elasticsearch/pull/141784)


## February 2, 2026


### Features and enhancements

- Adds PromQL validation parameters to alert rules for improved query validation [#249708](https://github.com/elastic/kibana/pull/249708)
- Updates the footer layout in the ES|QL editor for improved navigation [#244284](https://github.com/elastic/kibana/pull/244284)
- Migrates traces in Discover to the new flyout system for a more consistent experience [#247451](https://github.com/elastic/kibana/pull/247451)
- Adds a troubleshooting view for requests between nodes in the Service Map [#248646](https://github.com/elastic/kibana/pull/248646)
- Makes APM SLOs available directly from the Service Inventory page [#249374](https://github.com/elastic/kibana/pull/249374)
- Adds Cloud Forwarder onboarding tile to the Observability onboarding page [#250325](https://github.com/elastic/kibana/pull/250325)
- Adds filtering for cloud connectors by account type and provider [#250107](https://github.com/elastic/kibana/pull/250107)
- Adds granular subfeature privileges for rule exceptions [#245722](https://github.com/elastic/kibana/pull/245722)
- Adds the `includes` operator to KQL queries [#248985](https://github.com/elastic/kibana/pull/248985)
- Improves Index Management index list performance on large clusters with many indices [#246276](https://github.com/elastic/kibana/pull/246276)
- Adds a new documentation validation CLI to streamline the development workflow [#249305](https://github.com/elastic/kibana/pull/249305)
- Improves the Inference Endpoints page by adding a **Model** column and enabling search by model name [#249779](https://github.com/elastic/kibana/pull/249779)
- Shows RED (Rate, Errors, Duration) metric charts for trace queries in APM [#249909](https://github.com/elastic/kibana/pull/249909)
- Introduces a severity color palette for color mapping in visualizations [#250198](https://github.com/elastic/kibana/pull/250198)
- Adds an auto-push option to case connectors, enabling automatic case synchronization [#249251](https://github.com/elastic/kibana/pull/249251)
- Adds a stream features table with detail flyout and bulk delete functionality [#250379](https://github.com/elastic/kibana/pull/250379)
- Adds a new SharePoint Online connector to the available connector list [#248737](https://github.com/elastic/kibana/pull/248737)
- Renders `tdigest` and `exponential_histogram` metric types in the metrics grid [#249269](https://github.com/elastic/kibana/pull/249269)
- Simplifies parameter types in the ES|QL test tool [#249855](https://github.com/elastic/kibana/pull/249855)
- Exposes `configuration_overrides` in the Agent Builder converse API [#249256](https://github.com/elastic/kibana/pull/249256)
- Reorganizes the unified metrics grid package for improved maintainability [#248992](https://github.com/elastic/kibana/pull/248992)
- Prevents flyout remount when switching document types in the trace waterfall view [#250406](https://github.com/elastic/kibana/pull/250406)
- Adds support for IP and boolean types in the ES|QL `FIRST` and `LAST` functions [#140097](https://github.com/elastic/elasticsearch/pull/140097)
- Adds support for reranking multi-valued fields in ES|QL [#140672](https://github.com/elastic/elasticsearch/pull/140672)
- Optimizes ARM SVE functions for BBQ (Better Binary Quantization) Int4 to 1-bit dot product calculations [#141047](https://github.com/elastic/elasticsearch/pull/141047)
- Adds `max_batch_size` setting to Elastic Inference Service (EIS) sparse embedding settings [#141185](https://github.com/elastic/elasticsearch/pull/141185)
- Adds an optimized hash table for grouping by two long fields in ES|QL aggregations [#140838](https://github.com/elastic/elasticsearch/pull/140838)
- Adds `_size` metadata attribute support from the mapper-size plugin [#141427](https://github.com/elastic/elasticsearch/pull/141427)
- Adds native operations for float-based scoring, improving search performance [#140169](https://github.com/elastic/elasticsearch/pull/140169)
- Adds the `MV_INTERSECTS` function to ES|QL for testing if two multi-value fields share common values [#140662](https://github.com/elastic/elasticsearch/pull/140662)
- Adds approximate query execution mode to ES|QL, enabling faster results for exploratory queries [#131828](https://github.com/elastic/elasticsearch/pull/131828)
- The ES|QL `RERANK` command is now generally available (GA) [#141508](https://github.com/elastic/elasticsearch/pull/141508)
- Adds Views support to ES|QL for creating reusable query definitions [#134995](https://github.com/elastic/elasticsearch/pull/134995)
- Limits IDs queries to the `max_result_window` setting (default: 10,000) for improved resource protection [#140515](https://github.com/elastic/elasticsearch/pull/140515)
- Introduces an adaptive block hash for improved ES|QL aggregation performance with high-cardinality data [#141237](https://github.com/elastic/elasticsearch/pull/141237)
- Adds configurable quantization levels (1, 2, or 4 bits) for `bbq_disk` dense vector index type [#139944](https://github.com/elastic/elasticsearch/pull/139944)
- Enables cross-project search compatibility for the scroll API [#140977](https://github.com/elastic/elasticsearch/pull/140977)
- Optimizes count grouping aggregation in ES|QL for improved performance [#141499](https://github.com/elastic/elasticsearch/pull/141499)
- Periodically emits partial aggregation results in ES|QL, reducing memory usage for high-cardinality queries [#141392](https://github.com/elastic/elasticsearch/pull/141392)
- Supports point-in-time (PIT) context relocation when nodes shut down and shards relocate [#137675](https://github.com/elastic/elasticsearch/pull/137675)
- Enables ES|QL `FIRST` and `LAST` functions for general use (removes snapshot restriction) [#141617](https://github.com/elastic/elasticsearch/pull/141617)
- Improves IP field term query performance using doc values for low-cardinality fields [#140735](https://github.com/elastic/elasticsearch/pull/140735)


### Fixes

- Fixes the handling of quote character as a dead key in the ES|QL editor [#246773](https://github.com/elastic/kibana/pull/246773)
- Adds support for functions and aggregators in PromQL autocomplete [#250078](https://github.com/elastic/kibana/pull/250078)
- Reverts a change that removed infrastructure UI custom dashboards [#249973](https://github.com/elastic/kibana/pull/249973)
- Fixes index update failures caused by invalid API payload format [#250758](https://github.com/elastic/kibana/pull/250758)
- Fixes an issue where the **Add connector** button appeared inactive and could not be clicked [#250921](https://github.com/elastic/kibana/pull/250921)
- Fixes an issue where alert info in the privileged user monitoring table did not re-query when the time range changed [#250618](https://github.com/elastic/kibana/pull/250618)
- Fixes occasional file preview corruption during file upload [#250532](https://github.com/elastic/kibana/pull/250532)
- Fixes persistence issues in Streams [#247544](https://github.com/elastic/kibana/pull/247544)
- Updates connector description terminology for consistency [#250649](https://github.com/elastic/kibana/pull/250649)
- Fixes an issue where clearing AI Connector form fields with a backspace reset them to default values [#251095](https://github.com/elastic/kibana/pull/251095)
- Fixes incorrect dependencies statistics in APM service views [#249434](https://github.com/elastic/kibana/pull/249434)
- Fixes the waterfall summary width for traces in Discover [#250556](https://github.com/elastic/kibana/pull/250556)
- Propagates ES|QL execution errors correctly to users [#250605](https://github.com/elastic/kibana/pull/250605)
- Handles empty results correctly in ES|QL alerting rule execution [#250759](https://github.com/elastic/kibana/pull/250759)
- Adjusts panel height in Discover for improved layout [#250778](https://github.com/elastic/kibana/pull/250778)
- Fixes an issue where metrics grid titles were not updated when the column order changed [#250963](https://github.com/elastic/kibana/pull/250963)
- Fixes server-side search in the user prompts API [#250882](https://github.com/elastic/kibana/pull/250882)
- Fixes incorrect handling of action metadata in Workflows `elasticsearch.bulk` steps, ensuring proper support for all bulk operation types [#249771](https://github.com/elastic/kibana/pull/249771)
- Fixes an infinite loop in ES|QL Analyzer when subqueries reference indices with empty mappings [#141371](https://github.com/elastic/elasticsearch/pull/141371)
- Fixes ES|QL to use standard logic for conflicting metric types in time-series data, preserving the original type information [#141496](https://github.com/elastic/elasticsearch/pull/141496)
- Appends an implicit limit to ES|QL subqueries with an unbounded sort for consistent behavior [#141025](https://github.com/elastic/elasticsearch/pull/141025)
- Fixes machine learning the model cache to evict old models before loading new ones, preventing circuit breaker exceptions [#140844](https://github.com/elastic/elasticsearch/pull/140844)
- Fixes potential data corruption in ES|QL when creating constant vector blocks with BytesRef values [#141242](https://github.com/elastic/elasticsearch/pull/141242)
- Fixes folding of the ES|QL `CASE()` function when using date period and time duration values [#141157](https://github.com/elastic/elasticsearch/pull/141157)
- Fixes attribute ID generation in ES|QL `UNION ALL` branches for unmapped fields [#141262](https://github.com/elastic/elasticsearch/pull/141262)
- Fixes ES|QL `TOP_SNIPPETS` function to accept string-formatted numeric parameters [#141130](https://github.com/elastic/elasticsearch/pull/141130)
- Fixes `match_only_text` field incorrectly delegating value loading to a parent keyword field [#141399](https://github.com/elastic/elasticsearch/pull/141399)
- Reduces locking contention when persisting machine learning job statistics [#141519](https://github.com/elastic/elasticsearch/pull/141519)
- Fixes OpenTelemetry dynamic mappings to resolve `*.geo.location` fields as `geo_point` type [#141397](https://github.com/elastic/elasticsearch/pull/141397)


## January 26, 2026


### Features and enhancements

- Elastic will regularly be adding new ML models which will appear as pre-configured AI connectors in your projects. Refer to [the Elastic Inference Service page](https://www.elastic.co/docs/explore-analyze/elastic-inference/eis) for more details
- Adds support for PromQL queries in the ES|QL editor [#249230](https://github.com/elastic/kibana/pull/249230)
- Opts in to the flyout session for the Unified Doc Viewer flyout [#246719](https://github.com/elastic/kibana/pull/246719)
- Enables cascading documents for `STATS` queries in ES|QL [#220119](https://github.com/elastic/kibana/pull/220119)
- Adds the ability to create and manage SLOs from the Service Inventory page [#249259](https://github.com/elastic/kibana/pull/249259)
- Adds a `concat` processor for data management [#247940](https://github.com/elastic/kibana/pull/247940)
- Enables ES|QL multi-terms charts in Lens [#244743](https://github.com/elastic/kibana/pull/244743)
- Adds support for unmapped fields in Discover [#248606](https://github.com/elastic/kibana/pull/248606)
- Supports KQL autocomplete in the search visor in ES|QL [#247224](https://github.com/elastic/kibana/pull/247224)
- Adds support for restorable state for **Doc Viewer** flyout tabs [#249030](https://github.com/elastic/kibana/pull/249030)
- Adds basic support for PromQL in Kibana [#249854](https://github.com/elastic/kibana/pull/249854)
- Allows you to filter ES|QL sessions within a dashboard [#249357](https://github.com/elastic/kibana/pull/249357)
- Supports autocomplete functionality inside KQL functions [#249510](https://github.com/elastic/kibana/pull/249510)
- Adds a new `approximate` ES|QL setting [#248946](https://github.com/elastic/kibana/pull/248946)
- Improves the context for AI Assistant insights in Alerts [#248195](https://github.com/elastic/kibana/pull/248195)
- Adds Elastic Inference Service (EIS) pricing communication for Knowledge Base models in Elastic AI Assistant [#249298](https://github.com/elastic/kibana/pull/249298)
- Moves the results view buttons closer to the job selection controls in Anomaly Detection [#249261](https://github.com/elastic/kibana/pull/249261)
- Adds new preconfigured connectors [#249379](https://github.com/elastic/kibana/pull/249379)
- Replaces the AJV library with Zod for improved schema validation across Kibana [#248317](https://github.com/elastic/kibana/pull/248317)
- Adds an option to convert an index to a lookup index in the **Manage index** dropdown [#248730](https://github.com/elastic/kibana/pull/248730)
- Adds Chat Completion to Amazon Bedrock for the Inference API [#139411](https://github.com/elastic/elasticsearch/pull/139411)
- Adds dot product functions for Int4 to 1-bit in BBQ [#140264](https://github.com/elastic/elasticsearch/pull/140264)
- Adds IntRangeVector for selected groups in aggregation [#141205](https://github.com/elastic/elasticsearch/pull/141205)
- Adds Case and Coalesce Support for Compound Types [#140677](https://github.com/elastic/elasticsearch/pull/140677)
- Adds ES|QL support for project METADATA [#140592](https://github.com/elastic/elasticsearch/pull/140592)
- Adds partitioning for time-series sources to speed up queries and improve memory management [#140475](https://github.com/elastic/elasticsearch/pull/140475)
- Adds preconditioning utilities to help with edge cases where quantization causes vectors to become indistinguishable [#140198](https://github.com/elastic/elasticsearch/pull/140198)
- Implements the Observability Agent in AI Assistant insights and flyout configurations [#249776](https://github.com/elastic/kibana/pull/249776)


### Fixes

- Fixes an issue with reporting in dashboards and visualizations [#249644](https://github.com/elastic/kibana/pull/249644)
- Updates the logs overview component to use Zod v4 [#249583](https://github.com/elastic/kibana/pull/249583)
- Fixes KQL autocomplete functionality during custom threshold rule creation [#250044](https://github.com/elastic/kibana/pull/250044)
- Fixes a bug that caused an incorrect number of users to be displayed for CSV uploads [#249032](https://github.com/elastic/kibana/pull/249032)
- Removes the **Technical preview** badge for the privileged access detection package [#249500](https://github.com/elastic/kibana/pull/249500)
- Fixes a bug where tooltip information for status tags was not displayed on the Gap fill scheduler logs flyout [#247695](https://github.com/elastic/kibana/pull/247695)
- Fixes pagination issues in the Installation review frontend [#248259](https://github.com/elastic/kibana/pull/248259)
- Fixes an issue where schedules and conversations referencing outdated connector IDs using Elastic Managed LLMs failed to execute or display correctly [#249891](https://github.com/elastic/kibana/pull/249891)
- Disables the **Rule summary** button when a user lacks the required rule privileges [#248221](https://github.com/elastic/kibana/pull/248221)
- Fixes broken breadcrumbs and sidebar navigation for Data Visualizer and AIOps [#248167](https://github.com/elastic/kibana/pull/248167)
- Ensures the abort signal is passed to Elasticsearch during file uploads [#249623](https://github.com/elastic/kibana/pull/249623)
- Fixes a word-breaking issue in Anomaly Detection page titles [#250058](https://github.com/elastic/kibana/pull/250058)
- Ensures child stream names do not contain spaces [#249384](https://github.com/elastic/kibana/pull/249384)
- Fixes an error that occurred when adding items to an index template [#249168](https://github.com/elastic/kibana/pull/249168)
- Ensures that parsing of `on_disk_rescore` accounts for valid false values [#141158](https://github.com/elastic/elasticsearch/pull/141158)
- Fixes incorrect pruning of the `INLINE STATS GROUP BY null` ES|QL expression [#140027](https://github.com/elastic/elasticsearch/pull/140027)
- Fixes date fields sort formatting with missing values [#135899](https://github.com/elastic/elasticsearch/pull/135899)
- Quantizes ST_X, ST_Y and related functions [#140963](https://github.com/elastic/elasticsearch/pull/140963)
- Uses Double.compare to compare doubles in `tdigest.Sort` [#141049](https://github.com/elastic/elasticsearch/pull/141049)
- Refactors ES|QL lookup join to allow for streaming [#139406](https://github.com/elastic/elasticsearch/pull/139406)


## January 19, 2026


### Features and enhancements

- [Elastic Agent Builder](https://www.elastic.co/docs/explore-analyze/ai-features/elastic-agent-builder) is now generally available in Elastic Cloud Serverless. Enabled by default in Elasticsearch projects, you can now [opt in](https://www.elastic.co/docs/explore-analyze/ai-features/ai-chat-experiences/ai-agent-or-ai-assistant) in Observability and Security projects. Learn how to [get started](https://www.elastic.co/docs/explore-analyze/ai-features/agent-builder/get-started).
- [Elastic Workflows](https://www.elastic.co/docs/explore-analyze/workflows) is now available in technical preview. Build YAML-based workflows to automate actions across Elasticsearch,Kibana, external systems, and AI. Workflows support manual, scheduled, and alert-based triggers, conditional logic, and integrations with existing connectors and Agent Builder. You must turn on the feature to get started.
- Adds support for ES|QL in Vega [#247186](https://github.com/elastic/kibana/pull/247186)
- Improves Fleet setup memory usage by deferring package reinstalls to async tasks [#248235](https://github.com/elastic/kibana/pull/248235)
- Adds tab-scoped, retainable flyout behavior in Discover [#246612](https://github.com/elastic/kibana/pull/246612)
- Adds hover previews to the recently closed tabs menu in Discover [#246973](https://github.com/elastic/kibana/pull/246973)
- Adds unified rules list [#242208](https://github.com/elastic/kibana/pull/242208)
- Adds Windows support to the OTel host onboarding flow [#248478](https://github.com/elastic/kibana/pull/248478)
- Integrates the new app menu with dashboards [#246153](https://github.com/elastic/kibana/pull/246153)
- Enhances anomaly detection model memory estimation for user-supplied configurations [#248479](https://github.com/elastic/kibana/pull/248479)
- Adds time window buttons to the date picker in Machine Learning views [#248142](https://github.com/elastic/kibana/pull/248142)
- Adds a `timeout` parameter to `InferenceChatModel` [#248326](https://github.com/elastic/kibana/pull/248326)
- Redesigns the empty state for the Streams listing [#248636](https://github.com/elastic/kibana/pull/248636)
- Redesigns the empty states for the **Partitioning** and **Processing** tabs [#248463](https://github.com/elastic/kibana/pull/248463)
- Allows filtering from legend actions in ES|QL when supported [#248789](https://github.com/elastic/kibana/pull/248789)
- Adds a **Queries** tab to the Significant Events Discovery page [#248243](https://github.com/elastic/kibana/pull/248243)
- Adds a `get_trace_change_points` tool for trace change point analysis [#247810](https://github.com/elastic/kibana/pull/247810)
- Adds a background task for significant events query generation [#248608](https://github.com/elastic/kibana/pull/248608)
- Refactors the ES|QL inference operator architecture to support multi-value fields [#139694](https://github.com/elastic/elasticsearch/pull/139694)
- Removes the implicit `limit` appended to each subquery branch in ES|QL [#139058](https://github.com/elastic/elasticsearch/pull/139058)
- Makes the ES|QL `TEXT_EMBEDDING` function generally available (GA) [#140555](https://github.com/elastic/elasticsearch/pull/140555)
- Adds support for the multimodal embedding task type to the JinaAI service [#140323](https://github.com/elastic/elasticsearch/pull/140323)
- Adds `CHICKEN` function to ES|QL [#140645](https://github.com/elastic/elasticsearch/pull/140645)
- Adds a suggestion for resolving the Machine learning node allocation error [#139520](https://github.com/elastic/elasticsearch/pull/139520)
- Adds top-level arithmetic operations support to `TS | STATS` [#140135](https://github.com/elastic/elasticsearch/pull/140135)
- Adds `dense_vector` support for `COUNT`, `PRESENT`, and `ABSENT` aggregations in ES|QL [#139914](https://github.com/elastic/elasticsearch/pull/139914)
- Enables `NULLIFY` and `FAIL` unmapped field resolution in technical preview [#140528](https://github.com/elastic/elasticsearch/pull/140528)
- Adds support for mapping unavailable fields [#140463](https://github.com/elastic/elasticsearch/pull/140463)
- Moves union types out of `BlockLoader` in ES|QL [#140384](https://github.com/elastic/elasticsearch/pull/140384)
- Adds timezone support to `TO_STRING`, `TO_DATETIME`, and `TO_DATENANOS` converters in ES|QL [#138985](https://github.com/elastic/elasticsearch/pull/138985)
- Adds timezone support to `TRange` in ES|QL [#139911](https://github.com/elastic/elasticsearch/pull/139911)
- Increases DiskBBQ vector block bulk size to 32 [#138217](https://github.com/elastic/elasticsearch/pull/138217)
- Prefetches vectors during rescoring [#139955](https://github.com/elastic/elasticsearch/pull/139955)
- Stores fallback match-only text fields in binary doc values [#140189](https://github.com/elastic/elasticsearch/pull/140189)
- Stores flattened field data in binary doc values [#140246](https://github.com/elastic/elasticsearch/pull/140246)
- Stores raw pattern text fields in binary doc values [#140191](https://github.com/elastic/elasticsearch/pull/140191)
- Updates Grok to use `Matcher#setTimeout` [#139405](https://github.com/elastic/elasticsearch/pull/139405)
- Makes vector functions generally available (GA) [#140545](https://github.com/elastic/elasticsearch/pull/140545)
- Makes the auto-expand indices functionality use the desired cluster topology when one is available
- Runs replica topology boundary enforcement when receiving the desired topology
- Adds tests for ES|QL index exclusion


### Fixes

- Fixes incorrect time zone for CSV reports that use local date comparison [#244405](https://github.com/elastic/kibana/pull/244405)
- Fixes timestamp override for ES|QL CSV-formatted scheduled reports with relative time ranges [#248169](https://github.com/elastic/kibana/pull/248169)
- Limits variable suggestions to in-scope variables [#248365](https://github.com/elastic/kibana/pull/248365)
- Expands the time range of all documents with `date_nanos` time fields [#248495](https://github.com/elastic/kibana/pull/248495)
- Fixes query drafts when switching tabs [#247968](https://github.com/elastic/kibana/pull/247968)
- Prevents loss of UI state in signal-specific Discover flyout tabs when refreshing a query [#248203](https://github.com/elastic/kibana/pull/248203)
- Fixes missing spans when viewing a trace with a large number of spans in Discover [#247689](https://github.com/elastic/kibana/pull/247689)
- Uses monitor query ID for project monitor package policies [#248762](https://github.com/elastic/kibana/pull/248762)
- Fixes duplicated test results in the monitor status heat map at higher granularity [#248761](https://github.com/elastic/kibana/pull/248761)
- Adds no-data behavior options for metric threshold alerts [#247669](https://github.com/elastic/kibana/pull/247669)
- Prevents unauthorized delete attempts for Notes and improves the error message [#247617](https://github.com/elastic/kibana/pull/247617)
- Fixes an issue where the pagination on the Notes tab was showing `1-0 of 0` when no notes exist [#248481](https://github.com/elastic/kibana/pull/248481)
- Fixes an issue with share modal where all time ranges were shared as absolute [#248804](https://github.com/elastic/kibana/pull/248804)
- Fixes missing `counter` fields in the anomaly detection dropdown [#248187](https://github.com/elastic/kibana/pull/248187)
- Updates Packetbeat DNS tunneling datafeed to include runtime mappings [#249317](https://github.com/elastic/kibana/pull/249317)
- Fixes the document rejection when partitioning streams while data is ingested [#247953](https://github.com/elastic/kibana/pull/247953)
- Fixes the timestamps in the Recent Log Entries table to respect the time zone setting in Kibana (`dateFormat:tz`) [#249016](https://github.com/elastic/kibana/pull/249016)
- Fixes an issue where the agent count was not updating on the homepage [#248657](https://github.com/elastic/kibana/pull/248657)
- Fixes missing service environment in custom links [#248631](https://github.com/elastic/kibana/pull/248631)
- Fixes an issue where duplicated managed ILM (index lifecycle management) policies were marked as managed [#248586](https://github.com/elastic/kibana/pull/248586)
- Adds a `cold start` badge to unified waterfall visualization [#248857](https://github.com/elastic/kibana/pull/248857)
- Fixes broken links pointing from the View in context modal to Discover [#248939](https://github.com/elastic/kibana/pull/248939)
- Fixes series tooltips not working in full screen [#248148](https://github.com/elastic/kibana/pull/248148)
- Changes the Gauge chart default color palette to the status palette [#246734](https://github.com/elastic/kibana/pull/246734)
- Fixes EIS OpenAI GPT-OSS 120B reasoning error [#248943](https://github.com/elastic/kibana/pull/248943)
- Adds `maxQueue` backpressure to the anonymization regex worker pool [#249108](https://github.com/elastic/kibana/pull/249108)
- Adds a check to ensure ES|QL is valid before matching a metrics profile [#248917](https://github.com/elastic/kibana/pull/248917)
- Makes the static lookup formatter work with aggregated boolean fields [#249311](https://github.com/elastic/kibana/pull/249311)
- Adds datasource name to namespace [#249123](https://github.com/elastic/kibana/pull/249123)
- Fixes an issue where the Discover histogram legend in ES|QL mode was not filtering out null values correctly [#249302](https://github.com/elastic/kibana/pull/249302)
- Fixes class cast exceptions in pipeline aggregations [#140069](https://github.com/elastic/elasticsearch/pull/140069)
- Fixes an issue where `numCands` was passed instead of `k` [#140839](https://github.com/elastic/elasticsearch/pull/140839)
- Fixes an issue where `ENRICH` in ES|QL didn't work when using `dense_vector` as a column for adding as part of the `ENRICH` command [#139774](https://github.com/elastic/elasticsearch/pull/139774)
- Fixes aggregation on null values in ES|QL [#139797](https://github.com/elastic/elasticsearch/pull/139797)
- Fixes nested aggregation `top_hits` with query `inner_hits` [#137351](https://github.com/elastic/elasticsearch/pull/137351)
- Fixes converted fields not propagating through projections [#137923](https://github.com/elastic/elasticsearch/pull/137923)
- Reduces priority of clear-cache tasks [#139685](https://github.com/elastic/elasticsearch/pull/139685)
- Rejects `max_number_of_allocations` > 1 for low-priority model deployments [#140163](https://github.com/elastic/elasticsearch/pull/140163)
- Sorts legacy histogram values during downsampling [#140771](https://github.com/elastic/elasticsearch/pull/140771)
- Uses a sub keyword block loader with `ignore_above` for text fields [#140622](https://github.com/elastic/elasticsearch/pull/140622)
- Fixes auto-expand code for replicas


## January 13, 2026


### Features and enhancements

- Adds controls as a panel type, allowing you to place them anywhere in dashboards with section-scoped output filters or pin them globally [#245588](https://github.com/elastic/kibana/pull/245588)
- Adds the ability to roll back a recent upgrade of a Fleet-managed Elastic Agent using the Fleet UI or API [#247398](https://github.com/elastic/kibana/pull/247398)
- Marks the `MATCH_PHRASE` second argument as constant-only [#247003](https://github.com/elastic/kibana/pull/247003)
- Enhances the SLO details page to properly handle grouped SLOs when no specific instance is selected, allowing you to search SLO instances [#247638](https://github.com/elastic/kibana/pull/247638)
- Enhances the Monitoring Entity Source CRUD APIs [#246978](https://github.com/elastic/kibana/pull/246978)
- Improves Attack Discovery hallucination detection [#247965](https://github.com/elastic/kibana/pull/247965)
- Improves error handling for 429 errors related to the Inference and AI connectors [#246640](https://github.com/elastic/kibana/pull/246640)
- Adds a **Synchronize saved objects** button to the Trained models page [#247691](https://github.com/elastic/kibana/pull/247691)
- Adds full end-to-end support for the range operator in the condition editor for Streams [#243011](https://github.com/elastic/kibana/pull/243011)
- Adds `uppercase`, `lowercase`, and `trim` processors to Streamlang [#246540](https://github.com/elastic/kibana/pull/246540)
- Sets the default Node.js heap limit for containers to 75% of available memory, up to a maximum of 4096 MB [#246073](https://github.com/elastic/kibana/pull/246073)
- Improves the inference endpoint selector layout to keep long endpoint names readable and stable while clarifying ML-node startup behavior [#247417](https://github.com/elastic/kibana/pull/247417)
- Improves the Connection Details flyout by hiding the **API Keys** tab for users without API key management permissions [#246979](https://github.com/elastic/kibana/pull/246979)
- Improves default Synthetics rule creation [#245441](https://github.com/elastic/kibana/pull/245441)
- Changes the placement of **Migrations** and **Inventory** in the Security solution's navigation menu [#247002](https://github.com/elastic/kibana/pull/247002)
- Changes the alert suppression icon [#247964](https://github.com/elastic/kibana/pull/247964)
- Hides tabs for generic attack groups [#248444](https://github.com/elastic/kibana/pull/248444)
- Updates the total event count in Elasticsearch documents when you attach an event to a case [#247996](https://github.com/elastic/kibana/pull/247996)
- Converts `PackedValuesBlockHash.bytes` to `BreakingBytesRefBuilder` for better memory tracking in ES|QL [#140171](https://github.com/elastic/elasticsearch/pull/140171)
- Logs connection failures at `WARN` level for sniffed nodes [#140149](https://github.com/elastic/elasticsearch/pull/140149)
- Adds base64 format for dense vector doc values [#140094](https://github.com/elastic/elasticsearch/pull/140094)
- Ensures DiskBBQ tail centroids are always block-encoded [#139835](https://github.com/elastic/elasticsearch/pull/139835)
- Adds syntax support and parsing for `SET approximate` in ES|QL [#139908](https://github.com/elastic/elasticsearch/pull/139908)
- Adds timezone support to `add` and `sub` operators and planning support for `ConfigurationAware` in ES|QL [#140101](https://github.com/elastic/elasticsearch/pull/140101)
- Improves Lookup Join performance with `CachedDirectoryReader` in ES|QL [#139314](https://github.com/elastic/elasticsearch/pull/139314)
- Improves locality by placing parent-child centroids next to each other [#140293](https://github.com/elastic/elasticsearch/pull/140293)
- Retrieves routing hash from synthetic ID for translog operations [#140221](https://github.com/elastic/elasticsearch/pull/140221)
- Includes rerank in supported tasks for the IBM Watsonx integration in the Inference API [#140331](https://github.com/elastic/elasticsearch/pull/140331)


### Fixes

- Ensures ES|QL control options get updated when the time range changes [#248068](https://github.com/elastic/kibana/pull/248068)
- Increases the default top values for new Lens visualizations to nine categories [#247015](https://github.com/elastic/kibana/pull/247015)
- Fixes the icon in the **Elastic documentation not available** callout in AI Assistant settings [#247885](https://github.com/elastic/kibana/pull/247885)
- Prevents extra Synthetics package policies from being updated when maintenance windows are updated or deleted, even if the monitor itself does not use maintenance windows [#246088](https://github.com/elastic/kibana/pull/246088)
- Fixes a validation error with maintenance windows on lightweight Synthetics monitors [#247880](https://github.com/elastic/kibana/pull/247880)
- Fixes a bug that prevented user and host names from being escaped when they appeared in URLs [#247707](https://github.com/elastic/kibana/pull/247707)
- Fixes an issue where the rule settings pop-up remained open after clicking **Save** when enabling or disabling auto gap fill [#247678](https://github.com/elastic/kibana/pull/247678)
- Fixes an issue where the Security AI Assistant API did not apply the system prompt associated with a conversation [#248020](https://github.com/elastic/kibana/pull/248020)
- Fixes Attack Discovery misclassifying the system error "Security AI Anonymization settings configured to not allow any fields" [#248439](https://github.com/elastic/kibana/pull/248439)
- Fixes the display of map view for small screen sizes in Data Visualizer [#247615](https://github.com/elastic/kibana/pull/247615)
- Removes ES|QL field stats for the `TS` command [#247641](https://github.com/elastic/kibana/pull/247641)
- Fixes an accessibility issue where the **Show API key** button did not update to **Hide API key** when toggled [#247982](https://github.com/elastic/kibana/pull/247982)
- Deactivates the **API keys** button on the Elasticsearch homepage when you have insufficient permissions [#248072](https://github.com/elastic/kibana/pull/248072)
- Fixes the OpenAI connector's add header flow so the newly added header key input receives focus instead of leaving focus on the **Add header** button [#248204](https://github.com/elastic/kibana/pull/248204)
- Fixes an issue that could cause errors when updating index mappings [#248462](https://github.com/elastic/kibana/pull/248462)
- Fixes a bug where Agent Builder Index Search tools would fail on aliases that contained `semantic_text` fields [#247877](https://github.com/elastic/kibana/pull/247877)
- Fixes link color contrast [#247721](https://github.com/elastic/kibana/pull/247721)
- Fixes `ToolbarSelector` when clicking on tabs in Discover [#247836](https://github.com/elastic/kibana/pull/247836)
- Fixes trace links calculating date ranges incorrectly in Discover [#247531](https://github.com/elastic/kibana/pull/247531)
- Fixes decoding errors for terms with symbols in Cases [#247992](https://github.com/elastic/kibana/pull/247992)
- Fixes an issue where API requests returned deleted async searches [#140385](https://github.com/elastic/elasticsearch/pull/140385)
- Fixes double scroll in fullscreen flyouts [#247744](https://github.com/elastic/kibana/pull/247744)
- Fixes the React DOM nesting warning `validateDOMNesting(...): <button> cannot appear as a descendant of <button>` that appears in the Trace Waterfall component [#247808](https://github.com/elastic/kibana/pull/247808)


## January 6, 2026


### Features and enhancements

- Makes scheduled exports generally available (GA) [#245882](https://github.com/elastic/kibana/pull/245882)
- Makes alert deletion generally available (GA) [#247465](https://github.com/elastic/kibana/pull/247465)
- Adds API support for searching rules by action parameters [#246123](https://github.com/elastic/kibana/pull/246123)
- Allows the Slack connector to send messages to any channel by channel name [#245423](https://github.com/elastic/kibana/pull/245423)
- Simplifies the Primary Metric editor by removing the **Supporting visualization** title in Lens [#245979](https://github.com/elastic/kibana/pull/245979)
- Shows multi-fields by default in the DocViewer [#245890](https://github.com/elastic/kibana/pull/245890)
- Adds computed suggestions for expressions [#246421](https://github.com/elastic/kibana/pull/246421)
- Adds a toggle icon for adding and removing field columns [#246024](https://github.com/elastic/kibana/pull/246024)
- Allows chart interval settings in saved objects to persist [#246426](https://github.com/elastic/kibana/pull/246426)
- Adds an ES|QL editor shortcut for indentation [#247234](https://github.com/elastic/kibana/pull/247234)
- Introduces a **Find Alert Rule Templates** API and uses it to show installed templates in the "Create rule" dialog [#245373](https://github.com/elastic/kibana/pull/245373)
- Adds a math processor for data transformations [#246050](https://github.com/elastic/kibana/pull/246050)
- Allows users to manage SLO stale threshold settings in Elastic Observability Serverless [#246760](https://github.com/elastic/kibana/pull/246760)
- Adds observability tools for log and metric change point analysis [#242423](https://github.com/elastic/kibana/pull/242423)
- Displays alert workflow tags on the **Overview** tab of the alert details flyout [#246440](https://github.com/elastic/kibana/pull/246440)
- Upgrades Osquery manager schemas to ECS 9.2.0 and Osquery 5.19.0 [#246005](https://github.com/elastic/kibana/pull/246005)
- Updates the Entity Highlight UI to align with the new design [#245532](https://github.com/elastic/kibana/pull/245532)
- Removes the technical preview designation from the public Attack Discovery and Attack Discovery Schedules APIs [#246788](https://github.com/elastic/kibana/pull/246788)
- Allows the analyzer data view in local storage to persist [#245002](https://github.com/elastic/kibana/pull/245002)
- Aligns graph visualizations with ECS entity namespace fields for actor and target identification [#243711](https://github.com/elastic/kibana/pull/243711)
- Adds a server setting that turns off automatic endpoint rule installation when creating a policy [#246418](https://github.com/elastic/kibana/pull/246418)
- Updates Kibana MITRE data to version 18.1 [#246770](https://github.com/elastic/kibana/pull/246770)
- Improves chat experience documentation links [#246334](https://github.com/elastic/kibana/pull/246334)
- Shows partial results when a search is canceled [#242346](https://github.com/elastic/kibana/pull/242346)
- Adds a classic stream creation flyout to the Streams page [#245975](https://github.com/elastic/kibana/pull/245975)
- Adds support for abort and silent mode to stream description generation [#247082](https://github.com/elastic/kibana/pull/247082)
- Improves copy behavior with clear visual confirmation [#246090](https://github.com/elastic/kibana/pull/246090)
- Updates the Search Homepage design [#246777](https://github.com/elastic/kibana/pull/246777)
- Introduces a connector for web search using Brave Search [#245329](https://github.com/elastic/kibana/pull/245329)
- Adds search capabilities to the attachment tab [#246265](https://github.com/elastic/kibana/pull/246265)
- Adds Linux support for the `populate_file_data` advanced option, enabling `entropy` and `header_bytes` fields in file events [#246197](https://github.com/elastic/kibana/pull/246197)
- Adds error markers to the unified trace waterfall [#245161](https://github.com/elastic/kibana/pull/245161)
- Syncs badges in the unified trace waterfall [#246510](https://github.com/elastic/kibana/pull/246510)
- Adds critical path visualization to traces in Discover [#246952](https://github.com/elastic/kibana/pull/246952)
- Cleans up unified trace waterfall tests [#247252](https://github.com/elastic/kibana/pull/247252)


### Fixes

- Adds maximum character validation for email connector parameters and configuration [#246453](https://github.com/elastic/kibana/pull/246453)
- Removes the default `| LIMIT 10` clause from ES|QL panels created in Lens dashboards [#247427](https://github.com/elastic/kibana/pull/247427)
- Fixes compound filters incorrectly showing unsaved changes while dashboards load [#247309](https://github.com/elastic/kibana/pull/247309)
- Fixes default app state handling when detecting unsaved changes [#246664](https://github.com/elastic/kibana/pull/246664)
- Fixes unrecognized GROK patterns [#246871](https://github.com/elastic/kibana/pull/246871)
- Fixes the default alerts editing flow when default rules are missing [#245736](https://github.com/elastic/kibana/pull/245736)
- Addresses multiple onboarding issues [#246208](https://github.com/elastic/kibana/pull/246208)
- Prevents the Elastic Agent from interpreting JavaScript template literals as policy variables by using Unicode escaping [#247284](https://github.com/elastic/kibana/pull/247284)
- Fixes the console state persisting across onboarding journey steps [#247376](https://github.com/elastic/kibana/pull/247376)
- Fixes related dashboards for Elasticsearch query and other observability-supported stack rules [#247564](https://github.com/elastic/kibana/pull/247564)
- Fixes the **Manage data sources** integration card from always showing a “no data stream” warning [#246180](https://github.com/elastic/kibana/pull/246180)
- Fixes Timeline actions appearing in Alert table bulk actions without sufficient privileges [#246150](https://github.com/elastic/kibana/pull/246150)
- Fixes incorrect vulnerability data returned by the Entity Highlight API [#246889](https://github.com/elastic/kibana/pull/246889)
- Updates Active Directory matchers to use the SID-derived privileged group field [#246763](https://github.com/elastic/kibana/pull/246763)
- Fixes an issue where the Threat intelligence section in the alert details flyout was not displaying multiple values [#245449](https://github.com/elastic/kibana/pull/245449)
- Ensures the analyzer preview uses the same data view selected in the analyzer component [#246081](https://github.com/elastic/kibana/pull/246081)
- Fixes an issue where ES|QL risk scoring queries that contained special characters caused parse errors [#247060](https://github.com/elastic/kibana/pull/247060)
- Fixes a filter display issue on the MITRE coverage overview page [#246794](https://github.com/elastic/kibana/pull/246794)
- Ensures the analyzer renders only after the data view is ready [#245712](https://github.com/elastic/kibana/pull/245712)
- Fixes onboarding issues when users have read-only rule privileges [#247355](https://github.com/elastic/kibana/pull/247355)
- Uses exact matching for the `createdBy` notes filter [#247351](https://github.com/elastic/kibana/pull/247351)
- Fixes audit event creation always returning a failure outcome [#247152](https://github.com/elastic/kibana/pull/247152)
- Fixes case sensitivity inconsistencies for fields on the Roles page [#246069](https://github.com/elastic/kibana/pull/246069)
- Re-enables and optimizes text field analysis for Log Rate Analysis contextual insights [#244109](https://github.com/elastic/kibana/pull/244109)
- Fixes creating anomaly detection jobs from Discover sessions without a data view [#246410](https://github.com/elastic/kibana/pull/246410)
- Fixes an empty query issue in anomaly charts [#246841](https://github.com/elastic/kibana/pull/246841)
- Adds validation for manual ingest pipeline scripts [#245439](https://github.com/elastic/kibana/pull/245439)
- Fixes `mapper_parsing_exception` errors in wired streams [#245838](https://github.com/elastic/kibana/pull/245838)
- Fixes an issue where the field autocomplete functionality was not working for newly added fields [#246934](https://github.com/elastic/kibana/pull/246934)
- Fixes authorization checks by intersecting allowed and authorized types [#244967](https://github.com/elastic/kibana/pull/244967)
- Fixes token count display issues in Search Playground [#246589](https://github.com/elastic/kibana/pull/246589)
- Adds a table caption when top categories are empty in the logs category table [#246041](https://github.com/elastic/kibana/pull/246041)
- Corrects ES|QL query column names using selected index mappings [#241911](https://github.com/elastic/kibana/pull/241911)
- Requires the `manage` permission to perform bulk actions on Streams features [#246129](https://github.com/elastic/kibana/pull/246129)
- Fixes the alert history chart background color in dark mode [#246017](https://github.com/elastic/kibana/pull/246017)
- Replaces `host.hostname` with `host.name` in the Infrastructure tab [#246386](https://github.com/elastic/kibana/pull/246386)
- Truncates long values in the value list modal column [#246679](https://github.com/elastic/kibana/pull/246679)
- Adds a refusal field to assistant conversations [#243423](https://github.com/elastic/kibana/pull/243423)
- Fixes an error rate chart warning shown on first load [#247052](https://github.com/elastic/kibana/pull/247052)
- Fixes layout issues with the Metric Explorer search bar on certain screen sizes [#246945](https://github.com/elastic/kibana/pull/246945)
- Re-enables a previously flaky test for retrieving Elastic documents [#247533](https://github.com/elastic/kibana/pull/247533)
- Improves anonymization error messages when the NER model is unavailable [#247696](https://github.com/elastic/kibana/pull/247696)


## December 16, 2025


### Features and enhancements

- Adds four new Google Cloud Platform [regions](https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud/regions) for Elastic Cloud Serverless: GCP Singapore (`asia-southeast1`), GCP London (`europe-west2`), GCP Frankfurt (`europe-west3`), and GCP Netherlands (`europe-west4`)
- Adds an integration knowledge opt-out UI setting and feature flag [#245080](https://github.com/elastic/kibana/pull/245080)
- Redesigns the single and bulk agent actions menus in Fleet, organizing commonly used actions at the top level and grouping other actions into nested menus by use case [#245174](https://github.com/elastic/kibana/pull/245174)
- Adds agent internal YAML settings [#245819](https://github.com/elastic/kibana/pull/245819)
- Adds support for chain controls [#242909](https://github.com/elastic/kibana/pull/242909)
- Improves validation and autocomplete for CASE [#244280](https://github.com/elastic/kibana/pull/244280)
- Avoids redundant requests when breakdown or chart interval changes [#245523](https://github.com/elastic/kibana/pull/245523)
- Adds support for filtering on multivalue fields [#245554](https://github.com/elastic/kibana/pull/245554)
- Adds an example plugin for UX testing of the ES|QL editor [#245792](https://github.com/elastic/kibana/pull/245792)
- Adds a **Copy as Markdown** option for selected results [#245545](https://github.com/elastic/kibana/pull/245545)
- Adds an internal API for global params sync [#239284](https://github.com/elastic/kibana/pull/239284)
- Adds the ability to bulk mute and unmute alerts [#245690](https://github.com/elastic/kibana/pull/245690)
- Adds Rules feature privileges, allowing access to Elastic Security rules to be explicitly set for user roles [#239634](https://github.com/elastic/kibana/pull/239634)
- Updates the threat hunting UI [#243311](https://github.com/elastic/kibana/pull/243311)
- Adds support for QRadar reference sets as lookups [#244924](https://github.com/elastic/kibana/pull/244924)
- Shows analyzer in full height [#245857](https://github.com/elastic/kibana/pull/245857)
- Shows session view in full height [#245888](https://github.com/elastic/kibana/pull/245888)
- Adds an integration knowledge platform tool to Agent Builder [#245259](https://github.com/elastic/kibana/pull/245259)
- Adds Agent Builder UI settings, RBAC, navigation, and tour [#246089](https://github.com/elastic/kibana/pull/246089)
- Redesigns Lookup join file upload [#244550](https://github.com/elastic/kibana/pull/244550)
- Adds an action to create an anomaly detection alerting rule [#241274](https://github.com/elastic/kibana/pull/241274)
- Adds an empty state for the Partitioning tab [#244893](https://github.com/elastic/kibana/pull/244893)
- Improves attachment filters with multi-type selection, server-side filtering, and a suggestions limit [#245248](https://github.com/elastic/kibana/pull/245248)
- Adds a new **Similar errors** section with an occurrences chart [#244665](https://github.com/elastic/kibana/pull/244665)
- Adds dashboard ownership and write-restricted mode, allowing you to control who can edit your dashboards regardless of broader space permissions [#224552](https://github.com/elastic/kibana/pull/224552)
- Adds a new gap fill status column to the Rules page [#242595](https://github.com/elastic/kibana/pull/242595)
- Validates space ownership when unlinking attachments [#245250](https://github.com/elastic/kibana/pull/245250)
- Adds `deactivate_all_instrumentations`, `deactivate_instrumentations`, `send_logs`, `send_metrics`, and `send_traces` agent configuration settings for EDOT PHP [#246021](https://github.com/elastic/kibana/pull/246021)
- Adds dashboard suggestions for ECS Kubernetes and OTel dashboards when selecting pods in the Infrastructure inventory UI [#245784](https://github.com/elastic/kibana/pull/245784)
- Enhances search for the main Cases page [#245321](https://github.com/elastic/kibana/pull/245321)
- Adds concurrency to KMeansLocal [#139239](https://github.com/elastic/elasticsearch/pull/139239)
- Enables CCS tests for ES|QL subqueries [#137776](https://github.com/elastic/elasticsearch/pull/137776)
- Adds CCS support for the ES|QL Inference command [#139244](https://github.com/elastic/elasticsearch/pull/139244)
- Introduces usage limits for COMPLETION and RERANK [#139074](https://github.com/elastic/elasticsearch/pull/139074)
- Adds privileges to the Kibana System role to manage internal indexes in support of Elastic Defend features [#138993](https://github.com/elastic/elasticsearch/pull/138993)
- Optimizes native bulk dot product scoring for Int7 [#139069](https://github.com/elastic/elasticsearch/pull/139069)
- Adds Azure OpenAI chat completion support [#138726](https://github.com/elastic/elasticsearch/pull/138726)
- Adds NVIDIA support to the inference plugin [#132388](https://github.com/elastic/elasticsearch/pull/132388)
- Adds TDigest histogram as a metric [#139247](https://github.com/elastic/elasticsearch/pull/139247)
- Adds a `TOP_SNIPPETS` function to return the best snippets for a field [#138940](https://github.com/elastic/elasticsearch/pull/138940)
- Takes `TOP_SNIPPETS` out of snapshot [#139272](https://github.com/elastic/elasticsearch/pull/139272)
- Prevents `AggregateMetricDouble` fields from building BKD indexes [#138724](https://github.com/elastic/elasticsearch/pull/138724)
- Bumps jruby/joni to 2.2.6 [#139075](https://github.com/elastic/elasticsearch/pull/139075)
- Enables bfloat16 and on-disk rescoring for dense vectors [#138492](https://github.com/elastic/elasticsearch/pull/138492)
- Enables the new `exponential_histogram` field type [#138968](https://github.com/elastic/elasticsearch/pull/138968)
- Adds planning detailed timing to profile information in ES|QL [#138564](https://github.com/elastic/elasticsearch/pull/138564)
- Optimizes `GROUP BY ALL` in ES|QL [#139130](https://github.com/elastic/elasticsearch/pull/139130)
- Pulls `OrderBy` above `InlineJoin` in ES|QL [#137648](https://github.com/elastic/elasticsearch/pull/137648)
- Re-enables bfloat16 in semantic text [#139347](https://github.com/elastic/elasticsearch/pull/139347)
- Adds filter support for pushing down `COUNT(*) BY DATE_TRUNC` [#138765](https://github.com/elastic/elasticsearch/pull/138765)
- Restricts GPU indexing to FLOAT element types [#139084](https://github.com/elastic/elasticsearch/pull/139084)
- Introduces an adaptive HNSW Patience collector [#138685](https://github.com/elastic/elasticsearch/pull/138685)
- Rewrites terms queries to a filter on `constant_keyword` fields [#139106](https://github.com/elastic/elasticsearch/pull/139106)
- Minimizes doc values fetches in `TSDBSyntheticIdFieldsProducer` [#139053](https://github.com/elastic/elasticsearch/pull/139053)
- Monitors `/proc/net/tcp{,6}` for retransmissions
- Removes the `DOC_VALUES_SKIPPER` feature flag [#138723](https://github.com/elastic/elasticsearch/pull/138723)
- Removes the `gpu_vectors_indexing` feature flag [#139318](https://github.com/elastic/elasticsearch/pull/139318)
- Adds semantic search CCS support when `ccs_minimize_roundtrips=false` [#138982](https://github.com/elastic/elasticsearch/pull/138982)
- Stores the `@timestamp` field value range in the compound commit header
- Uses the existing `DocumentMapper` when creating a new `MapperService` [#138489](https://github.com/elastic/elasticsearch/pull/138489)
- Uses the new bulk scoring dot product for max inner product [#139409](https://github.com/elastic/elasticsearch/pull/139409)


### Fixes

- Enables storing secrets in Fleet Server host config if Fleet Server is running at a minimum supported version [#237464](https://github.com/elastic/kibana/pull/237464)
- Fixes Discover tab initialization [#245752](https://github.com/elastic/kibana/pull/245752)
- Improves error handling for tool responses [#241425](https://github.com/elastic/kibana/pull/241425)
- Updates Gemini connector configuration [#245647](https://github.com/elastic/kibana/pull/245647)
- Limits the API for retrieving gap summaries to 100 `rule_id`s per request [#245924](https://github.com/elastic/kibana/pull/245924)
- Fixes "now" and mixed-format date handling in the share modal [#245539](https://github.com/elastic/kibana/pull/245539)
- Ensures chart tooltips are always shown correctly in anomaly detection result views [#246077](https://github.com/elastic/kibana/pull/246077)
- Turns off geopoint mapping in the processing preview [#245506](https://github.com/elastic/kibana/pull/245506)
- Validates child stream input [#242581](https://github.com/elastic/kibana/pull/242581)
- Fixes an issue where the upgrade assistant would incorrectly warn about nodes breaching the low watermark despite the `max_headroom` setting [#243906](https://github.com/elastic/kibana/pull/243906)
- Fixes an ECS-incompatible value in the logs [#245706](https://github.com/elastic/kibana/pull/245706)
- Fixes grammatical issues in the Solution Nav tour and simplifies the content by consolidating multiple links into one [#245718](https://github.com/elastic/kibana/pull/245718)
- Fixes Discover trace waterfall behavior with duplicate spans [#244984](https://github.com/elastic/kibana/pull/244984)
- Avoids JVM metric conflicts with explicit cast [#244151](https://github.com/elastic/kibana/pull/244151)
- Fixes an issue where metadata filtering was confusing or broken when typing "OR" in Host view [#233836](https://github.com/elastic/kibana/pull/233836)
- Compares ES|QL query builders using identity [#139080](https://github.com/elastic/elasticsearch/pull/139080)
- Adds support for chunking settings for sparse embeddings in a custom service to the Inference API [#138776](https://github.com/elastic/elasticsearch/pull/138776)
- Uses the `dimensions` field in JinaAI `text_embedding` requests to the Inference API [#139395](https://github.com/elastic/elasticsearch/pull/139395)
- Adds a configurable `max_batch_size` for GoogleVertexAI embedding service settings [#138047](https://github.com/elastic/elasticsearch/pull/138047)
- Improves `CompoundRetrieverBuilder` failure handling [#136732](https://github.com/elastic/elasticsearch/pull/136732)
- Treats dash-prefixed expressions as index exclusions [#138467](https://github.com/elastic/elasticsearch/pull/138467)
- Enables auto prefiltering for queries on dense `semantic_text` fields [#138989](https://github.com/elastic/elasticsearch/pull/138989)
- Disallows index type updates to `bbq_disk`, reverting (#131760) [#139061](https://github.com/elastic/elasticsearch/pull/139061)
- Enforces DiskBBQ licensing [#139087](https://github.com/elastic/elasticsearch/pull/139087)
- Ensures integer sorts are rewritten to long sorts for backward compatible indexes [#139293](https://github.com/elastic/elasticsearch/pull/139293)
- Fixes `project_routing` in EQL [#139366](https://github.com/elastic/elasticsearch/pull/139366)
- Changes `FUSE KEY BY` to accept a list of `qualifiedName` [#139071](https://github.com/elastic/elasticsearch/pull/139071)
- Fixes metrics that took between 1 and 10 hours in ES|QL [#139257](https://github.com/elastic/elasticsearch/pull/139257)
- Prunes `InlineJoin` right aggregations by delegating to the child plan in ES|QL [#139357](https://github.com/elastic/elasticsearch/pull/139357)
- Fixes downsampling with disabled subobjects [#138715](https://github.com/elastic/elasticsearch/pull/138715)
- Fixes an offset maths bug in `InetAddress` parsing [#139420](https://github.com/elastic/elasticsearch/pull/139420)
- Avoids `EsqlIllegalArgumentException` for invalid window values [#139470](https://github.com/elastic/elasticsearch/pull/139470)


## December 8, 2025


### Features and enhancements

- Allows you to search scheduled reports by title and creator [#243841](https://github.com/elastic/kibana/pull/243841)
- Updates the rule flapping schema to add an optional `enabled` field [#243855](https://github.com/elastic/kibana/pull/243855)
- Improves suggestions for `LIKE` and `RLIKE` operators so they only suggest string-compatible options [#244903](https://github.com/elastic/kibana/pull/244903)
- Redesigns the Lookup index editor with a new layout and controls [#244480](https://github.com/elastic/kibana/pull/244480)
- Adds support for global custom ingest pipelines for service-level objectives (SLOs), allowing you to create a single pipeline that applies to all SLO rollup and summary documents [#245025](https://github.com/elastic/kibana/pull/245025)
- Changes SLO rollup indexing to store service level indicator (SLI) data daily instead of monthly by default, with override support through a global custom ingest pipeline [#244978](https://github.com/elastic/kibana/pull/244978)
- Adds ELSER in Elastic Inference Service (EIS) as a model option for the Observability AI Assistant knowledge base [#243298](https://github.com/elastic/kibana/pull/243298)
- Adds an **Edit tags** action that lets you manually apply workflow tags to alerts [#243792](https://github.com/elastic/kibana/pull/243792)
- Allows you to view and filter alerts by manually added workflow tags [#244251](https://github.com/elastic/kibana/pull/244251)
- Adds a built-in product documentation tool to Agent Builder, available only when product documentation is installed [#242598](https://github.com/elastic/kibana/pull/242598)
- Adds a platform cases tool and experimental security attachments and tools to Agent Builder to support existing **Ask AI Assistant** and **View in Agent Builder** workflows [#243574](https://github.com/elastic/kibana/pull/243574).
- Adds an alerts search tool and two security agents (Alerts Agent and Entity Agent) to Agent Builder [#245205](https://github.com/elastic/kibana/pull/245205)
- Updates the API keys management page to default to displaying personal API keys only [#245261](https://github.com/elastic/kibana/pull/245261)
- Adds two new preconfigured connectors (General Purpose LLM v2 and General Purpose LLM v3) and renames the Elastic Managed LLM connector to General Purpose LLM v1 [#242791](https://github.com/elastic/kibana/pull/242791)
- Adds the Groq icon to the providers list displayed during AI Connector and Inference endpoint creation [#244962](https://github.com/elastic/kibana/pull/244962)
- Adds the **Suggest a pipeline** option in the Processing tab of streams to help generate ingest pipelines [#243950](https://github.com/elastic/kibana/pull/243950)
- Adds support for `geo_point` fields in the schema editor for classic streams [#244356](https://github.com/elastic/kibana/pull/244356)
- Enhances the Streams attachments feature with a details flyout, a better user experience, and better user feedback [#244880](https://github.com/elastic/kibana/pull/244880)
- Adds validation for Streamlang DSL to enforce field namespacing in wired streams and detect type mismatches in processor configurations [#244221](https://github.com/elastic/kibana/pull/244221)
- Adds an onboarding tour to the Streams UI to guide new users through core workflows [#244808](https://github.com/elastic/kibana/pull/244808)
- Allows you to filter ES|QL charts in dashboards [#243439](https://github.com/elastic/kibana/pull/243439)
- Enables Value reports in Elastic Cloud Hosted and adds logic to export them using the share plugin [#243511](https://github.com/elastic/kibana/pull/243511)
- Adds a **Span links** badge to the unified trace waterfall view [#244389](https://github.com/elastic/kibana/pull/244389)
- Adds dynamic form elements for the IBM Resilient connector fields, improving the configuration experience [#238869](https://github.com/elastic/kibana/pull/238869)
- Adds a time range selector to the Cases page to simplify filtering by timeframe [#243409](https://github.com/elastic/kibana/pull/243409)


### Fixes

- Fixes an issue where `alert.consecutiveMatches` was missing in the action context for rule executions [#244997](https://github.com/elastic/kibana/pull/244997)
- Fixes an issue where the Security alerts table did not update columns correctly when switching view mode [#245253](https://github.com/elastic/kibana/pull/245253)
- Handles alias resolution when checking lock index mappings [#244559](https://github.com/elastic/kibana/pull/244559)
- Fixes an issue where the SLOs page could cause inconsistent browser back button behavior [#242761](https://github.com/elastic/kibana/pull/242761)
- Standardizes error logging to make troubleshooting more consistent [#245030](https://github.com/elastic/kibana/pull/245030)
- Fixes an issue that prevented IdP-initiated authentication when multiple OIDC providers were configured [#243869](https://github.com/elastic/kibana/pull/243869)
- Improves UIAM reliability by increasing container health check timeouts and populating the UIAM shared secret in Elasticsearch [#245238](https://github.com/elastic/kibana/pull/245238)
- Fixes CSP-agnostic regressions by removing cloud provider host checks, ensuring all cloud providers for Elastic Cloud Hosted deployments and Serverless projects are supported [#242592](https://github.com/elastic/kibana/pull/242592)


## December 2, 2025


### Features and enhancements

- Adds the **Read global parameters** sub-feature privilege which allows you to read the values of synthetics global parameters [#243821](https://github.com/elastic/kibana/pull/243821)
- Adds Cc, Bcc, Subject, and Message fields with Mustache templating support to the Schedule exports flyout for email notifications [#242922](https://github.com/elastic/kibana/pull/242922)
- Allows users to enable scheduled reports [#244202](https://github.com/elastic/kibana/pull/244202)
- Adds a background Fleet policy revisions cleanup task to automatically remove excess policy revisions from the `.fleet-policies` index [#242612](https://github.com/elastic/kibana/pull/242612)
- Automatically migrates component template ILM policies during setup [#243333](https://github.com/elastic/kibana/pull/243333)
- Improves suggestion ordering using categorization to provide more relevant results [#243312](https://github.com/elastic/kibana/pull/243312)
- Allows you to select a column type in the lookup index editor [#241637](https://github.com/elastic/kibana/pull/241637)
- Ensures that infrastructure inventory UIs accurately reflect supported schemas [#244481](https://github.com/elastic/kibana/pull/244481)
- Adds a warning when deleting API keys currently in use by alerting rules [#243353](https://github.com/elastic/kibana/pull/243353)
- Removes the median line length check in the categorization anomaly detection job [#243827](https://github.com/elastic/kibana/pull/243827)
- Allows you to filter alerts using the KQL search bar [#240100](https://github.com/elastic/kibana/pull/240100)
- Introduces the Attachments API for streams [#243597](https://github.com/elastic/kibana/pull/243597)
- Introduces new UI components for the Drop processor [#243131](https://github.com/elastic/kibana/pull/243131)
- Adds service-level objective (SLO) support for streams attachments, migrates the UI to use the Attachments API for dashboards, rules, and SLOs, and removes deprecated API endpoints [#244092](https://github.com/elastic/kibana/pull/244092)
- Allows you to add custom descriptions for enrichment processors [#243998](https://github.com/elastic/kibana/pull/243998)
- Prevents conflicting actions in the Partitioning tab [#244228](https://github.com/elastic/kibana/pull/244228)
- Improves handling of missing streams [#244366](https://github.com/elastic/kibana/pull/244366)
- Allows you to configure the visibility of the Streams app per space [#244285](https://github.com/elastic/kibana/pull/244285)
- Improves error messaging when expensive queries are turned off in the Streams schema editor [#243406](https://github.com/elastic/kibana/pull/243406)
- Improves the Console UI to make key actions more intuitive [#242487](https://github.com/elastic/kibana/pull/242487)
- Adds targeted Elastic Inference Service (EIS) callouts and dismissible guided tours to Kibana for Elastic Cloud Hosted and Elastic Cloud Serverless users [#244626](https://github.com/elastic/kibana/pull/244626)
- Redesigns the Lens configuration flyout to show layers as tabs instead of vertically stacked panels [#235372](https://github.com/elastic/kibana/pull/235372)
- Consolidates attachments into a single Attachments tab with sub-tab navigation [#243708](https://github.com/elastic/kibana/pull/243708)
- Adds the ES|QL `CHUNK` function in technical preview [#138621](https://github.com/elastic/elasticsearch/pull/138621)
- Improves support for the `first()` and `last()` aggregation functions in ES|QL by disabling vector dispatch for blocks [#138390](https://github.com/elastic/elasticsearch/pull/138390)
- Adds informative timestamps to async ES|QL query results [#137957](https://github.com/elastic/elasticsearch/pull/137957)
- Add Groq as a chat completion inference service for machine learning [#138251](https://github.com/elastic/elasticsearch/pull/138251)
- Adds the node-scoped `vectors.indexing.use_gpu` setting to control GPU usage for vector indexing [#138738](https://github.com/elastic/elasticsearch/pull/138738)
- Adds routing support to the `_project/tags` endpoint
- Allows point-in-time (PIT) searches to span multiple projects [#137966](https://github.com/elastic/elasticsearch/pull/137966)
- Excludes synthetic `_id` postings from disk usage statistics [#138745](https://github.com/elastic/elasticsearch/pull/138745)
- Allows `project_routing` to be specified as a query parameter in EQL requests [#138559](https://github.com/elastic/elasticsearch/pull/138559)
- Avoids retrieving unnecessary fields during the node-reduce phase in ES|QL queries [#137920](https://github.com/elastic/elasticsearch/pull/137920)
- Updates `KNN` function options in ES|QL to align with the latest vector search behavior [#138372](https://github.com/elastic/elasticsearch/pull/138372)
- Updates the ES|QL `CHUNK` function to support `chunking_settings` as an optional argument [#138123](https://github.com/elastic/elasticsearch/pull/138123)
- Pushes down `COUNT(*) BY DATE_TRUNC` aggregations in ES|QL to improve performance [#138023](https://github.com/elastic/elasticsearch/pull/138023)
- Adds support for parameters to `LIKE` and `RLIKE` operators in ES|QL [#138051](https://github.com/elastic/elasticsearch/pull/138051)
- Adds support for the `time_zone` request parameter to `KQL` and `QSTR` functions in ES|QL [#138695](https://github.com/elastic/elasticsearch/pull/138695)
- Adds timezone support to the ES|QL `DateDiff` function [#138316](https://github.com/elastic/elasticsearch/pull/138316)
- Fuses the `MV_MIN` and `MV_MAX` functions in ES|QL and documents the fusion process [#138029](https://github.com/elastic/elasticsearch/pull/138029)
- Adds `GROUP BY ALL` support in ES|QL [#137367](https://github.com/elastic/elasticsearch/pull/137367)
- Extends `GROUP BY ALL` in ES|QL to support the dimensions output [#138595](https://github.com/elastic/elasticsearch/pull/138595)
- Extends the field capabilities API to support `project_routing` in the request body [#138681](https://github.com/elastic/elasticsearch/pull/138681)
- Improves security migration resilience by handling version conflicts more robustly [#137558](https://github.com/elastic/elasticsearch/pull/137558)
- Adds dynamic template parameters in bulk requests so OTLP metric units can be stored in index mappings [#134709](https://github.com/elastic/elasticsearch/pull/134709)
- Adds the `project_routing` option to SQL requests [#138718](https://github.com/elastic/elasticsearch/pull/138718)
- Uses a doc values skipper for `_tsid` when resolving synthetic `_id` values to skip unnecessary documents [#138568](https://github.com/elastic/elasticsearch/pull/138568)


### Fixes

- Verifies an alert exists before muting it [#242847](https://github.com/elastic/kibana/pull/242847)
- Prevents URL restore errors in Discover and Dashboards [#242788](https://github.com/elastic/kibana/pull/242788)
- Adds an authentication header to Kibana tool requests [#244017](https://github.com/elastic/kibana/pull/244017)
- Fixes an issue where the dashboard selector did not return results when trying to link dashboards to a rule [#243496](https://github.com/elastic/kibana/pull/243496)
- Fixes a validation error when creating custom threshold rules with data view objects [#244134](https://github.com/elastic/kibana/pull/244134)
- Ensures deleted text in form fields is not sent as an empty string during Inference endpoint and LLM Connector creation [#244059](https://github.com/elastic/kibana/pull/244059)
- Prevents cell selection from being cleared after you dismiss the alerts table popover in Anomaly Explorer [#244183](https://github.com/elastic/kibana/pull/244183)
- Fixes an issue where cell actions on empty cells populated the condition value with `undefined` [#243766](https://github.com/elastic/kibana/pull/243766)
- Removes references to Mustache template snippets from the UI form fields and descriptions for the Set processor [#243656](https://github.com/elastic/kibana/pull/243656)
- Fixes a screen-reader text mismatch on the Index management page [#243802](https://github.com/elastic/kibana/pull/243802)
- Fixes a sizing issue in the flyout for API key creation [#244072](https://github.com/elastic/kibana/pull/244072)
- Improves the error message that appears when the IBM Resilient connector fails [#244012](https://github.com/elastic/kibana/pull/244012)
- Catches connector errors without interrupting the case creation flow [#244188](https://github.com/elastic/kibana/pull/244188)
- Allows file paths containing spaces to be used in Observables [#244350](https://github.com/elastic/kibana/pull/244350)
- Fixes the serialization of `meta.error` in JSON layouts [#244364](https://github.com/elastic/kibana/pull/244364)
- Fixes an issue that could cause an infinite loading state after submitting the case creation form [#244543](https://github.com/elastic/kibana/pull/244543)
- Adds supprot for pruning columns when using `FORK` branches in ES|QL [#137907](https://github.com/elastic/elasticsearch/pull/137907)
- Fixes an Inference API issue to support correct type identification during deserialization [#138484](https://github.com/elastic/elasticsearch/pull/138484)
- Fixes `chunkedInfer()` to correctly handle empty inputs [#138632](https://github.com/elastic/elasticsearch/pull/138632)
- Ensures the circuit breaker limit is honored when building global ordinals by accounting their memory usage and breaking when the limit is exceeded [#108875](https://github.com/elastic/elasticsearch/pull/108875)
- Changes `DatabaseNodeService` error logs to warnings to reduce noise [#138438](https://github.com/elastic/elasticsearch/pull/138438)
- Avoids using `MIN` or `MAX` as `TOP`'s surrogate when an `outputField` is defined [#138380](https://github.com/elastic/elasticsearch/pull/138380)
- Uses the correct minimum transport version when resolving ES|QL `ENRICH` and `LOOKUP JOIN` types [#137431](https://github.com/elastic/elasticsearch/pull/137431)
- Fixes `SearchContext` circuit breaker memory accounting [#138002](https://github.com/elastic/elasticsearch/pull/138002)
- Adds missing `vector_similarity_support` flags in `InferenceFeatures` [#138644](https://github.com/elastic/elasticsearch/pull/138644)
- Extends the semantic text highlighter to improve the handling of vector-based queries [#138140](https://github.com/elastic/elasticsearch/pull/138140)
- Handles individual document parsing failures in bulk requests with ingest pipelines without failing the entire request [#138624](https://github.com/elastic/elasticsearch/pull/138624)
- Handles search timeouts that occur during collector initialization in `QueryPhase` by returning partial results instead of shard-level failures [#138084](https://github.com/elastic/elasticsearch/pull/138084)
- Fixes serialization of `null` blocks in `AggregateMetricDoubleBlock` [#138539](https://github.com/elastic/elasticsearch/pull/138539)
- Ensures filters are correctly applied to kNN queries [#138457](https://github.com/elastic/elasticsearch/pull/138457)
- Ensures filter queries, including semantic queries, are correctly rewritten and applied to kNN searches during coordinator-side inference [#138457](https://github.com/elastic/elasticsearch/pull/138457)
- Speeds up `LeafCollector#setScorer` in `TopHitsAggregator` [#138883](https://github.com/elastic/elasticsearch/pull/138883)\
- Reduces `LeafCollector#setScorer` overhead in `TopHitsAggregator` for multi-bucket aggregations by sharing a single `Scorable` instance across buckets [#138883](https://github.com/elastic/elasticsearch/pull/138883)
- Updates the `jts` dependency to version `1.20.0` [#138351](https://github.com/elastic/elasticsearch/pull/138351)
- Moves the `CrossProjectRoutingResolver` functionality to Serverless


## November 24, 2025


### Features and enhancements

- Allows users to edit scheduled exports [#241928](https://github.com/elastic/kibana/pull/241928)
- Uses `type@lifecycle` ILMs for new package installations [#241992](https://github.com/elastic/kibana/pull/241992)
- Allows ES|QL to support subqueries in the `FROM` command [#241921](https://github.com/elastic/kibana/pull/241921)
- Suggests adding curly braces after the `WITH` keyword for Rerank and Completion [#243047](https://github.com/elastic/kibana/pull/243047)
- Supports the new `exponential_histogram` Elasticsearch field type [#242748](https://github.com/elastic/kibana/pull/242748)
- Wraps the fork subcommands inside the `parens` node [#242369](https://github.com/elastic/kibana/pull/242369)
- Simplifies the search visor experience [#242123](https://github.com/elastic/kibana/pull/242123)
- Auto-scrolls to the suggestions panel in Streams  [#242891](https://github.com/elastic/kibana/pull/242891)
- Shows user-readable output for the MDE runscript response action [#242441](https://github.com/elastic/kibana/pull/242441)
- Saves the selected prevalence time to local storage [#243543](https://github.com/elastic/kibana/pull/243543)
- Saves the selected threat intelligence time to local storage [#243571](https://github.com/elastic/kibana/pull/243571)
- Adds custom header support for inference endpoint creation [#242187](https://github.com/elastic/kibana/pull/242187)
- Adds the `replace` processor to Streamlang DSL for string patterns replacement using regular expressions [#242310](https://github.com/elastic/kibana/pull/242310)
- Adds automatic dissect pattern generation capabilities to the Streams processing pipeline [#242377](https://github.com/elastic/kibana/pull/242377)
- Adds a rows per page selector to the tools, agents, and agent tools selection views [#242207](https://github.com/elastic/kibana/pull/242207)


### Fixes

- Uses the real dimensions when taking a screenshot of reports [#242127](https://github.com/elastic/kibana/pull/242127)
- Fixes a print mode regression in Dashboards [#242780](https://github.com/elastic/kibana/pull/242780)
- Fixes an issue where users could not save a dashboard after switching a dashboard link to an external URL [#243134](https://github.com/elastic/kibana/pull/243134)
- Uses `max_value` instead of infinity for the default maximum height of a panel in Dashboards [#243572](https://github.com/elastic/kibana/pull/243572)
- Adds retry behavior for `/api/fleet/agents` when transient issues with Elasticsearch are encountered [#243105](https://github.com/elastic/kibana/pull/243105)
- Uses a long expiration time for upgrade agents [#243443](https://github.com/elastic/kibana/pull/243443)
- Fixes retrying stuck agents in auto upgrade logic [#243326](https://github.com/elastic/kibana/pull/243326)
- Fixes the CPU query in Pod details by changing the gap policy to include zeros [#239596](https://github.com/elastic/kibana/pull/239596)
- Fixes the KPIs subtitle logic [#243217](https://github.com/elastic/kibana/pull/243217)
- Fixes custom links clearing filter values when a new field is selected or deleted [#241164](https://github.com/elastic/kibana/pull/241164)
- Updates the system prompt title for generic deployments [#243266](https://github.com/elastic/kibana/pull/243266)
- Fixes the squished Apple icon on Auto Detect flow cards [#242452](https://github.com/elastic/kibana/pull/242452)
- Handles the missing `error.id` when processing causes an error [#243638](https://github.com/elastic/kibana/pull/243638)
- Removes the block that prevented saving a Timeline with an ad-hoc dataview [#240537](https://github.com/elastic/kibana/pull/240537)
- Fixes the response actions API for Elastic Defend agent types, not sending the action to more than 10 agents [#243387](https://github.com/elastic/kibana/pull/243387)
- Fixes favicon CSS specificity issues [#243351](https://github.com/elastic/kibana/pull/243351)
- Fixes infinite loading of roles on the Edit spaces screen [#242954](https://github.com/elastic/kibana/pull/242954)
- Fixes import and improves validation for Anomaly Detection and Data Frame Analytics jobs [#242263](https://github.com/elastic/kibana/pull/242263)
- Fixes keyboard focus getting trapped in pages using document preview [#243791](https://github.com/elastic/kibana/pull/243791)
- Reverts "Fix issue where filters do not apply to overview stats" [#242978](https://github.com/elastic/kibana/pull/242978)
- Disables custom suggestion on embedded console [#241516](https://github.com/elastic/kibana/pull/241516)
- Shows the AI log assistant with fallback message fields [#243437](https://github.com/elastic/kibana/pull/243437)
- Ignores `resource_already_exists_exception` for value list creation hook [#243642](https://github.com/elastic/kibana/pull/243642)
- Prevents crashes on the Retention page for certain ILM policies [#243826](https://github.com/elastic/kibana/pull/243826)


## November 17, 2025


### Features and enhancements

- Enables the following HTTP request methods for the webhook connector: `POST` (default), `PUT`, `PATCH`, `GET`, and `DELETE` [#238072](https://github.com/elastic/kibana/pull/238072)
- Persists filter state for Fleet agent table during navigation [#228875](https://github.com/elastic/kibana/pull/228875)
- Displays inline suggestions in the ES|QL editor [#235162](https://github.com/elastic/kibana/pull/235162)
- Improves Attack Discovery prompts [#241346](https://github.com/elastic/kibana/pull/241346)
- Fixes grouping in the Alerts table [#237911](https://github.com/elastic/kibana/pull/237911)
- Collects cloud connector telemetry for the Cloud Asset Discovery integration [#240272](https://github.com/elastic/kibana/pull/240272)
- Syncs recently used date ranges in the time picker across browser tabs [#242467](https://github.com/elastic/kibana/pull/242467)
- Adds `drop_document` processor to Streamlang [#242161](https://github.com/elastic/kibana/pull/242161)
- Extracts `AbstractGeoIpDownloader` to share concurrency logic across GeoIP downloaders [#137660](https://github.com/elastic/elasticsearch/pull/137660)
- Iterates directly over `RoutingNode` contents to reduce allocation overhead [#137694](https://github.com/elastic/elasticsearch/pull/137694)
- Speeds up sorts that use secondary sort fields [#137533](https://github.com/elastic/elasticsearch/pull/137533)
- Updates HDFS version references in the documentation [#137576](https://github.com/elastic/elasticsearch/pull/137576)
- Reduces worst-case inference API latency by removing an additional 50 ms delay for non–rate-limited requests [#136167](https://github.com/elastic/elasticsearch/pull/136167)
- Updates ES|QL documentation to cover newly supported data types [#137726](https://github.com/elastic/elasticsearch/pull/137726)
- Uses the `DEFAULT_UNSORTABLE` topN encoder for `TSID_DATA_TYPE` in ES|QL to improve sorting behavior [#137706](https://github.com/elastic/elasticsearch/pull/137706)
- Transitions Elastic Indexing Service auth polling to a single-node persistent task for improved reliability [#136713](https://github.com/elastic/elasticsearch/pull/136713)
- Makes ES|QL field fusion generic so it can be reused across more field types [#137382](https://github.com/elastic/elasticsearch/pull/137382)
- Releases the ES|QL `decay` function [#137830](https://github.com/elastic/elasticsearch/pull/137830)
- Adds additional APM attributes to coordinator-phase duration metrics for richer tracing [#137409](https://github.com/elastic/elasticsearch/pull/137409)
- Adds telemetry to track CPS usage [#137705](https://github.com/elastic/elasticsearch/pull/137705)
- Introduces simple bulk loading for binary doc values to improve indexing throughput [#137860](https://github.com/elastic/elasticsearch/pull/137860)
- Uses IVF_PQ for GPU-based index builds on large datasets to improve vector indexing performance [#137126](https://github.com/elastic/elasticsearch/pull/137126)
- Aligns match-phase shard APM metrics with the originating search request context [#137196](https://github.com/elastic/elasticsearch/pull/137196)
- Improves Serverless filtering behavior when creating resources from existing configurations [#137850](https://github.com/elastic/elasticsearch/pull/137850)
- Refactors model field parsing in `AnthropicChatCompletionStreamingProcessor` to better handle model variants [#137926](https://github.com/elastic/elasticsearch/pull/137926)
- Adds balancer-round summary metrics to shard allocation to aid tuning and diagnostics [#136043](https://github.com/elastic/elasticsearch/pull/136043)
- Adds merge support to `ES93BloomFilterStoredFieldsFormat` [#137622](https://github.com/elastic/elasticsearch/pull/137622)
- Adds additional DEBUG-level logging for authentication failures [#137941](https://github.com/elastic/elasticsearch/pull/137941)
- Adds support for an extra output field in the ES|QL `TOP` function [#135434](https://github.com/elastic/elasticsearch/pull/135434)
- Introduces the `INDEX_SHARD_COUNT_FORMAT` setting for index shard count formatting [#137210](https://github.com/elastic/elasticsearch/pull/137210)
- Implements an OpenShift AI integration for chat completion, embeddings, and reranking workloads [#136624](https://github.com/elastic/elasticsearch/pull/136624)
- Adds `first()` and `last()` aggregation functions to ES|QL [#137408](https://github.com/elastic/elasticsearch/pull/137408)
- Adds support for the `project_routing` parameter on `_search` and `_async_search` requests [#137566](https://github.com/elastic/elasticsearch/pull/137566)
- Adds a daily maintenance task to manage `.ml-state` indices in machine learning [#137653](https://github.com/elastic/elasticsearch/pull/137653)
- Adds an `es812` postings format index setting for advanced indexing control [#137857](https://github.com/elastic/elasticsearch/pull/137857)
- Adds centroid filtering support to DiskBBQ for more restrictive filters [#137959](https://github.com/elastic/elasticsearch/pull/137959)
- Adds timezone support to ES|QL `DATE_TRUNC`, `BUCKET`, and `TBUCKET` functions [#137450](https://github.com/elastic/elasticsearch/pull/137450)
- Further improves bulk loading performance for binary doc values [#137995](https://github.com/elastic/elasticsearch/pull/137995)
- Updates the Gradle wrapper to version `9.2.0`
- Improves logging for the sampled metrics provider
- Updates `BlobCacheIndexInput` to use `sliceDescription` as the resource description when available, improving diagnostics
- Switches APM trace detection to use `hasApmTraceContext` and its variant APIs


### Fixes

- Fixes a bug that caused the Alerts table's pagination to hang on Rule pages [#242275](https://github.com/elastic/kibana/pull/242275)
- Fixes an error that occurred when deselecting a `(blank)` option from an options list [#242036](https://github.com/elastic/kibana/pull/242036)
- Fixes an issue that caused the 'sync colors' and 'sync tooltips' settings to be ON by default [#242442](https://github.com/elastic/kibana/pull/242442)
- Fixes package icons loading [#242406](https://github.com/elastic/kibana/pull/242406)
- Fixes the docker image reference in the **Add agent** flyout's Kubernetes manifest [#242691](https://github.com/elastic/kibana/pull/242691)
- Fixes text truncation in tables [#241440](https://github.com/elastic/kibana/pull/241440)
- Fixes charts not filtering by `host.name` [#242673](https://github.com/elastic/kibana/pull/242673)
- Reverts show transform errors accross all SLO pages [#243013](https://github.com/elastic/kibana/pull/243013)
- Adds encoding of `cloudFormation` URL parameters [#242365](https://github.com/elastic/kibana/pull/242365)
- Changes `must_not` risk scoring filter to `must` [#242171](https://github.com/elastic/kibana/pull/242171)
- Fixes the rule link in a timeline’s alert flyout [#242313](https://github.com/elastic/kibana/pull/242313)
- Fixes the data frame analytics wizard for data views with runtime fields [#242557](https://github.com/elastic/kibana/pull/242557)
- Updates the default semantic text endpoint when adding semantic text field mappings to ELSER in EIS [#242436](https://github.com/elastic/kibana/pull/242436)
- Fixes auto extraction in event bulk actions [#242325](https://github.com/elastic/kibana/pull/242325)
- Fixes the extraction of the current JDK major version [#137779](https://github.com/elastic/elasticsearch/pull/137779)
- Fixes OTLP responses to return the correct response type for partial successes [#137718](https://github.com/elastic/elasticsearch/pull/137718)
- Fixes the get data stream API when a data stream's index mode has been changed to `time_series` [#137852](https://github.com/elastic/elasticsearch/pull/137852)
- Ensures `include_execution_metadata` in ES|QL always returns data, including for local-only queries [#137641](https://github.com/elastic/elasticsearch/pull/137641)
- Fixes an ES|QL vector similarity concurrency issue affecting byte vectors [#137883](https://github.com/elastic/elasticsearch/pull/137883)
- Reverts a previous change to `statsByShard` that regressed performance for very large shard counts [#137984](https://github.com/elastic/elasticsearch/pull/137984)
- Fixes scalability issues when updating machine learning calendar events [#136886](https://github.com/elastic/elasticsearch/pull/136886)
- Prevents ES|QL queries from failing when an index is deleted during query execution [#137702](https://github.com/elastic/elasticsearch/pull/137702)
- Fixes `GET /_migration/deprecations` not reporting node deprecations when the disk low watermark is exceeded, and improves reporting of node-level failures [#137964](https://github.com/elastic/elasticsearch/pull/137964)
- Fixes `GET /_migration/deprecations` incorrectly checking deprecated affix index settings [#137976](https://github.com/elastic/elasticsearch/pull/137976)
- Prevents passing an ingest pipeline with a logs stream index request, avoiding invalid configurations [#137992](https://github.com/elastic/elasticsearch/pull/137992)
- Removes vectors from `_source` documents in ES|QL when appropriate to reduce payload size [#138013](https://github.com/elastic/elasticsearch/pull/138013)
- Prevents the delete index API from failing if an index is removed while the request is in progress [#138015](https://github.com/elastic/elasticsearch/pull/138015)
- Prevents renaming a field to `timestamp` in ES|QL before its implicit use, avoiding type errors [#137713](https://github.com/elastic/elasticsearch/pull/137713)
- Fixes `KDE.evaluate()` to return the correct `ValueAndMagnitude` object [#128602](https://github.com/elastic/elasticsearch/pull/128602)
- Fixes file settings handling in the Restore API [#137585](https://github.com/elastic/elasticsearch/pull/137585)


## November 10, 2025


### Features and enhancements

- Adds nightly maintenance for anomaly detection results indices to keep to manageable size [#136065](https://github.com/elastic/elasticsearch/pull/136065)
- Adds the ability to preview index requests in transforms [#137455](https://github.com/elastic/elasticsearch/pull/137455)
- Allows field capabilities to span across Elasticsearch Serverless projects [#137530](https://github.com/elastic/elasticsearch/pull/137530)
- Improves ES|QL performance by skipping unnecessary query plan diff calculations in Elasticsearch Serverless [#137721](https://github.com/elastic/elasticsearch/pull/137721)
- Passes the Elasticsearch version in the EIS inference request header in Elasticsearch Serverless [#137643](https://github.com/elastic/elasticsearch/pull/137643)
- Introduces a synthetic `_id` format for time-series data streams [#137274](https://github.com/elastic/elasticsearch/pull/137274)
- Updates the Dashboard top navigation to include a **Save** menu [#237211](https://github.com/elastic/kibana/pull/237211)
- Moves visualization configuration settings, including appearance, titles and text, axis, and legend to a flyout panel in **Lens** [#240804](https://github.com/elastic/kibana/pull/240804)
- Supports subqueries in the Discover pretty printer [#241473](https://github.com/elastic/kibana/pull/241473)
- Adds context-aware autocomplete for Discover subqueries with nesting restrictions [#241912](https://github.com/elastic/kibana/pull/241912)
- Adds subquery support for columns after and validation in Discover [#241567](https://github.com/elastic/kibana/pull/241567)
- Adds support for Discover subqueries in FROM clauses across tools [#242166](https://github.com/elastic/kibana/pull/242166)
- Enables users to view the SLO associated with a burn rate rule on the rule details page in Elastic Observability Serverless [#240535](https://github.com/elastic/kibana/pull/240535)
- Exposes `sampling_rate` agent central config options to users in Elastic Observability Serverless [#241908](https://github.com/elastic/kibana/pull/241908)
- Makes the Elastic logo open a custom home page in solution view [#241571](https://github.com/elastic/kibana/pull/241571)
- Enforces the `object_src 'none'` directive in the Kibana content security policy [#241029](https://github.com/elastic/kibana/pull/241029)
- Adds origin configuration options for authentication providers [#239993](https://github.com/elastic/kibana/pull/239993)
- Adds the ability to cancel machine learning file uploads [#241297](https://github.com/elastic/kibana/pull/241297)
- Improves display of long field values in Data Visualizer top values list [#241006](https://github.com/elastic/kibana/pull/241006)
- Adds a temperature parameter to Inference AI, and OpenAI, Bedrock, and Gemini connectors [#239806](https://github.com/elastic/kibana/pull/239806)
- Adds support for custom headers in the OpenAI integration [#238710](https://github.com/elastic/kibana/pull/238710)
- Fixes public Update spaces APIs [#242136](https://github.com/elastic/kibana/pull/242136)
- Improves layout for custom inference endpoints [#241779](https://github.com/elastic/kibana/pull/241779)
- Displays field data types in the Processing table and step editor [#241825](https://github.com/elastic/kibana/pull/241825)
- Adds timezone and locale parameters to Streamlang [#241369](https://github.com/elastic/kibana/pull/241369)
- Displays field data types in the Streams Partitioning UI [#242134](https://github.com/elastic/kibana/pull/242134)
- Adds autocomplete for field values in Streams Partitioning and Processing tabs [#241119](https://github.com/elastic/kibana/pull/241119)
- Hides document match filter controls for users without manage privileges [#242119](https://github.com/elastic/kibana/pull/242119)


### Fixes

- Fixes feature display order when using explain in Learning to Rank (LTR) [#137671](https://github.com/elastic/elasticsearch/pull/137671)
- Fixes an issue where missing geotile buckets caused errors in Transform [#137476](https://github.com/elastic/elasticsearch/pull/137476)
- Ensures ES|QL full text functions accept `null` values as field parameters in Elasticsearch Serverless  [#137430](https://github.com/elastic/elasticsearch/pull/137430)
- Fixes a missing attribute issue in ES|QL full text functions in Elasticsearch Serverless [#137395](https://github.com/elastic/elasticsearch/pull/137395)
- Fixes a bug in `RankDocRetrieverBuilder` when `from` is set to the default -1 value [#137637](https://github.com/elastic/elasticsearch/pull/137637)
- Prevents use-after-close errors in async search by making `MutableSearchResponse` reference-counted  [#134359](https://github.com/elastic/elasticsearch/pull/134359)
- Removes early phase failures during batched search execution [#136889](https://github.com/elastic/elasticsearch/pull/136889)
- Improves SQL validation errors by providing more descriptive exception messages [#137560](https://github.com/elastic/elasticsearch/pull/137560)
- Correctly accounts for additional settings providers when determining data stream effective settings [#137407](https://github.com/elastic/elasticsearch/pull/137407)
- Adds proxy SSL options for download sources [#241115](https://github.com/elastic/kibana/pull/241115)
- Ensures Fleet policy name uniqueness is enforced consistently across spaces [#239631](https://github.com/elastic/kibana/pull/239631)
- Shows warnings on the sync integrations UI when referencing other entities [#241623](https://github.com/elastic/kibana/pull/241623)
- Escapes special characters when creating ES|QL queries for **Lens** charts in Elastic Observability Serverless [#241662](https://github.com/elastic/kibana/pull/241662)
- Fixes "Values" dropdown display on smaller screens in Elastic Observability Serverless [#241812](https://github.com/elastic/kibana/pull/241812)
- Excludes stale SLOs from group-by statistics in Elastic Observability Serverless [#240077](https://github.com/elastic/kibana/pull/240077)
- Fixes missing `EngineMetadata.type` in generic entity popovers in Elastic Security Serverless [#239661](https://github.com/elastic/kibana/pull/239661)
- Sanitizes lookup names when creating indices in Elastic Security Serverless [#240228](https://github.com/elastic/kibana/pull/240228)
- Supports multiple values in IOC flyout table tab in Elastic Security Serverless [#236110](https://github.com/elastic/kibana/pull/236110)
- Fixes top-N popover overlapping the new case flyout in Elastic Security Serverless [#242045](https://github.com/elastic/kibana/pull/242045)
- Fixes threshold source event handling in Elastic Security Serverless [#238707](https://github.com/elastic/kibana/pull/238707)
- Ensures Timeline ES|QL query editor displays correctly in full screen mode in Elastic Security Serverless  [#242027](https://github.com/elastic/kibana/pull/242027)
- Fixes invalid state for the **Enable wired streams** toggle [#241266](https://github.com/elastic/kibana/pull/241266)
- Fixes simulation of geo points in Streams [#241824](https://github.com/elastic/kibana/pull/241824)
- Decouples Streams AI features from Observability AI Assistant [#242019](https://github.com/elastic/kibana/pull/242019)
- Only applies tag changes when the connector supports them [#241944](https://github.com/elastic/kibana/pull/241944)


## November 3, 2025


### Features and enhancements

- Moves the **Lens** visualization toolbar from the workspace section to the configuration panel [#239879](https://github.com/elastic/kibana/pull/239879)
- Adds support for rolling back integrations to previous versions [#240761](https://github.com/elastic/kibana/pull/240761)
- Adds support for subqueries in the ES|QL abstract syntax tree (AST) [#241227](https://github.com/elastic/kibana/pull/241227)
- Adds subquery support for the walker and visitor in the ES|QL AST [#241451](https://github.com/elastic/kibana/pull/241451)
- Adds support for expressions in `LOOKUP JOIN` autocomplete [#240735](https://github.com/elastic/kibana/pull/240735)
- Adds support for multi-value variables in `MV_CONTAINS` [#239266](https://github.com/elastic/kibana/pull/239266)
- Adds client-side validation for `LOOKUP JOIN ON` expressions [#240930](https://github.com/elastic/kibana/pull/240930)
- Improves the ES|QL suggestions logic to provide more semantically intelligent suggestions [#241081](https://github.com/elastic/kibana/pull/241081)
- Adds an `isStream` parameter to the `chat/complete` endpoint to support non-streaming responses in the Observability AI Assistant [#240819](https://github.com/elastic/kibana/pull/240819)
- Makes the `opamp_polling_interval` and `sampling_rate` agent configuration variables available to EDOT Node.js [#241048](https://github.com/elastic/kibana/pull/241048)
- Adds a free-text popup for the `runscript` argument to provide user input to the selected script [#239436](https://github.com/elastic/kibana/pull/239436)
- Adds the deployment name to the breadcrumbs in Elastic Cloud Hosted [#238078](https://github.com/elastic/kibana/pull/238078)
- Adds a **Give feedback** button to the Anomaly Explorer and Single Metric Viewer [#239883](https://github.com/elastic/kibana/pull/239883)
- Adds a new `temperature` parameter to the AI Connector configuration schema [#239626](https://github.com/elastic/kibana/pull/239626)
- Makes the Update spaces APIs public [#241109](https://github.com/elastic/kibana/pull/241109)
- Adds support for the `convert` processor in stream data processing [#240023](https://github.com/elastic/kibana/pull/240023)
- Improves message feedback in collapsed Processors/Conditions sections [#240778](https://github.com/elastic/kibana/pull/240778)
- Optimizes workflow output in Agent Builder tools by removing workflow execution details from tool calls, reducing LLM token consumption and improving agent performance and reliability [#241040](https://github.com/elastic/kibana/pull/241040)
- Improves value loading for `match_only_text` mapping in ES|QL [#137026](https://github.com/elastic/elasticsearch/pull/137026)
- Introduces a new interface to declare functions depending on the `@timestamp` attribute in ES|QL [#137040](https://github.com/elastic/elasticsearch/pull/137040)
- Adds support for `first` and `last` functions in ES|QL [#137195](https://github.com/elastic/elasticsearch/pull/137195)
- Adds non-correlated subquery support in `FROM` command for ES|QL [#135744](https://github.com/elastic/elasticsearch/pull/135744)
- Adds circuit breakers endpoint to CAT API [#136890](https://github.com/elastic/elasticsearch/pull/136890)
- Defaults semantic_text fields to ELSER on EIS when available [#134708](https://github.com/elastic/elasticsearch/pull/134708)
- Adds `chunk_rescorer` usage to output of explain and profile for `text_similarity_rank_retriever` [#137249](https://github.com/elastic/elasticsearch/pull/137249)
- Enables `score` function in release builds for ES|QL [#136988](https://github.com/elastic/elasticsearch/pull/136988)
- Adds `CHUNK` function to ES|QL [#134320](https://github.com/elastic/elasticsearch/pull/134320)
- Adds base64 indexing for vector values [#137072](https://github.com/elastic/elasticsearch/pull/137072)
- Updates field caps transport to return what each original expression was resolved to [#136632](https://github.com/elastic/elasticsearch/pull/136632)
- Uses `DOC_VALUES_REWRITE` rewrite method where possible in keyword queries [#137536](https://github.com/elastic/elasticsearch/pull/137536)
- Adds `ES93BloomFilterStoredFieldsFormat` for efficient field existence checks [#137331](https://github.com/elastic/elasticsearch/pull/137331)


### Fixes

- Fixes layout issues for Markdown embeddables in small panels [#240806](https://github.com/elastic/kibana/pull/240806)
- Fixes an issue where labels in the **Create index** flow did not automatically render with the default vector tile scaling after saving or applying styling changes [#240728](https://github.com/elastic/kibana/pull/240728)
- Fixes `template_path` asset selection for certain integration packages [#240750](https://github.com/elastic/kibana/pull/240750)
- Omits system properties when syncing ingest pipelines [#241096](https://github.com/elastic/kibana/pull/241096)
- Fixes autocomplete for time series sources after a comma [#241402](https://github.com/elastic/kibana/pull/241402)
- Fixes a bottom gap that appeared while loading data in some cases [#238879](https://github.com/elastic/kibana/pull/238879)
- Hides non-trace services in service maps [#240104](https://github.com/elastic/kibana/pull/240104)
- Fixes an issue where the `kibana` tool failed when running Kibana behind a proxy [#236653](https://github.com/elastic/kibana/pull/236653)
- Fixes overlapping components in the Observability AI Assistant flyout on small screens [#241026](https://github.com/elastic/kibana/pull/241026)
- Aligns the **Members** link in the side navigation across all solutions [#240992](https://github.com/elastic/kibana/pull/240992)
- Updates Metrics experience API routes to delegate authorization to Elasticsearch [#241195](https://github.com/elastic/kibana/pull/241195)
- Copies alert states to the payload [#240411](https://github.com/elastic/kibana/pull/240411)
- Adds missing fields to transaction data [#241336](https://github.com/elastic/kibana/pull/241336)
- Simplifies metrics profile resolution by removing index pattern and time series validation [#241047](https://github.com/elastic/kibana/pull/241047)
- Allows partial matches on rule names when searching installed rules [#237496](https://github.com/elastic/kibana/pull/237496)
- Fixes a regression in threshold rule logic where threshold rules with no `group by` fields defined would no longer generate alerts [#241022](https://github.com/elastic/kibana/pull/241022)
- Fixes an issue where the alert details flyout on the **Risk contributions** tab did not display data in some cases [#241153](https://github.com/elastic/kibana/pull/241153)
- Fixes a table pagination issue on the Intelligence page [#241108](https://github.com/elastic/kibana/pull/241108)
- Fixes an issue with the **Regenerate** button in the Security Assistant [#241240](https://github.com/elastic/kibana/pull/241240)
- Fixes an issue where the Security AI Assistant's Index Entry form was showing incorrect field suggestions, missing searchable fields that exist as multi-fields or nested properties in Elasticsearch mappings [#239453](https://github.com/elastic/kibana/pull/239453)
- Fixes an issue where agent-based integrations failed to produce data [#241390](https://github.com/elastic/kibana/pull/241390)
- Fixes an infinite loop bug related to bootstrapping list resources [#241052](https://github.com/elastic/kibana/pull/241052)
- Reduces re-renders on resize and items change [#239888](https://github.com/elastic/kibana/pull/239888)
- Fixes index names causing an incompatible cluster error when product docs are installed with multiple inference IDs [#240506](https://github.com/elastic/kibana/pull/240506)
- Ensures all authentication fields are displayed correctly [#240913](https://github.com/elastic/kibana/pull/240913)
- Ensures the `max_tokens` parameter is passed as expected by the service [#241188](https://github.com/elastic/kibana/pull/241188)
- Updates the inference creation endpoint to ensure the `max_tokens` parameter is passed as expected when creating an Anthropic Connector [#241212](https://github.com/elastic/kibana/pull/241212)
- Removes the default fallback region for the Bedrock Connector [#241157](https://github.com/elastic/kibana/pull/241157)
- Fixes wrapping issues in the Streams UI [#240883](https://github.com/elastic/kibana/pull/240883)
- Speeds up field simulation in Streams [#241313](https://github.com/elastic/kibana/pull/241313)
- Updates action response codes [#240420](https://github.com/elastic/kibana/pull/240420)
- Fixes an infinite loop bug in the **Investigation guide** editor [#240472](https://github.com/elastic/kibana/pull/240472)
- Performs query field validation for rerank task type [#137219](https://github.com/elastic/elasticsearch/pull/137219)
- Preserves deployments with zero allocations during assignment planning [#137244](https://github.com/elastic/elasticsearch/pull/137244)
- Skips dataframes when disabled [#137220](https://github.com/elastic/elasticsearch/pull/137220)
- Refrains from creating an inference endpoint if ID is used in existing mappings [#137055](https://github.com/elastic/elasticsearch/pull/137055)
- Adds support for choosing the downsampling method in data stream lifecycle [#137023](https://github.com/elastic/elasticsearch/pull/137023)
- Fixes `illegal_access_exception: class com.maxmind.db.Decoder` from `ip_location` processor [#137479](https://github.com/elastic/elasticsearch/pull/137479)
- Catches and rethrows `TooComplexToDeterminizeException` in ES|QL [#137024](https://github.com/elastic/elasticsearch/pull/137024)
- Fixes `ReplaceAliasingEvalWithProject` in case of shadowing for ES|QL [#137025](https://github.com/elastic/elasticsearch/pull/137025)
- Rejects invalid `reverse_nested` aggregations [#137047](https://github.com/elastic/elasticsearch/pull/137047)
- Extends constant multi-value handling with warnings to general binary comparisons in ES|QL [#137387](https://github.com/elastic/elasticsearch/pull/137387)
- Improves type resolution for `Clamp` [#137226](https://github.com/elastic/elasticsearch/pull/137226)
- Enables `_otlp` usage with `create_doc` and `auto_configure` privileges [#137325](https://github.com/elastic/elasticsearch/pull/137325)
- Fixes inconsistency in the `isSyntheticSourceEnabled` flag [#137297](https://github.com/elastic/elasticsearch/pull/137297)
- Fixes dropped ignore above fields [#137394](https://github.com/elastic/elasticsearch/pull/137394)


## October 27, 2025


### Features and enhancements

- Adds support for deleting export schedules [#238197](https://github.com/elastic/kibana/pull/238197)
- Moves the **Lens** visualization toolbar from the **Visualization parameters** section to the flyout header [#239176](https://github.com/elastic/kibana/pull/239176)
- Changes the processing order in ES|QL so the breakdown is applied before the date histogram [#239685](https://github.com/elastic/kibana/pull/239685)
- Adds a **View in Discover** button to the Alert details page for infrastructure rules [#236880](https://github.com/elastic/kibana/pull/236880)
- Introduces CDR Data View versioning and migration logic [#238547](https://github.com/elastic/kibana/pull/238547)
- Fixes layout wrapping for fields in the Machine Learning Overview and Notifications pages [#239113](https://github.com/elastic/kibana/pull/239113)
- Removes the AI Assistant Settings privilege [#239144](https://github.com/elastic/kibana/pull/239144)
- Adds ingest pipeline processor template suggestions to the manual ingest pipeline processor editor [#236919](https://github.com/elastic/kibana/pull/236919)
- Adds the `kibana.alert.index_pattern` field to all alerts [#239450](https://github.com/elastic/kibana/pull/239450)
- Adds cached tokens to Unified API response [#136412](https://github.com/elastic/elasticsearch/pull/136412)
- Adds new sampling method to the downsample API [#136813](https://github.com/elastic/elasticsearch/pull/136813)
- Adds new timeseries aggregations: `Stddev` and variance over time [#136712](https://github.com/elastic/elasticsearch/pull/136712)
- Allows single fork branch for ES|QL [#136805](https://github.com/elastic/elasticsearch/pull/136805)
- Adjusts GPU graph building parameters [#137074](https://github.com/elastic/elasticsearch/pull/137074)
- Implements `network_direction` function [#136133](https://github.com/elastic/elasticsearch/pull/136133)
- Adds support for `first` and `last` functions in ES|QL [#136419](https://github.com/elastic/elasticsearch/pull/136419)
- Adds `TRANGE` ES|QL function [#136441](https://github.com/elastic/elasticsearch/pull/136441)
- Adds support for Full Text Functions and Lucene Pushable Predicates for `LOOKUP JOIN` in ES|QL [#136104](https://github.com/elastic/elasticsearch/pull/136104)
- Enables new data types with created version [#136327](https://github.com/elastic/elasticsearch/pull/136327)
- Adds `Locale` and timezone argument for `date_parse` [#136548](https://github.com/elastic/elasticsearch/pull/136548)


### Fixes

- Fixes missing accessibility announcements in form rows [#240132](https://github.com/elastic/kibana/pull/240132)
- Improves the **Cases** table loading behavior to prevent flashing [#240155](https://github.com/elastic/kibana/pull/240155)
- Fixes a bug in Lens that incorrectly assigned unsaved data view references [#239431](https://github.com/elastic/kibana/pull/239431)
- Fixes an error when selecting the `(blank)` value in options lists [#239791](https://github.com/elastic/kibana/pull/239791)
- Pauses fetch operations until initialization completes [#239228](https://github.com/elastic/kibana/pull/239228)
- Fixes a bug that prevented users from resetting unsaved changes when enabling **timeRestore** and setting a time range [#239992](https://github.com/elastic/kibana/pull/239992)
- Fixes a search session restoration issue [#239822](https://github.com/elastic/kibana/pull/239822)
- Allows Fleet setup retries on start in all environments [#240342](https://github.com/elastic/kibana/pull/240342)
- Adds **FORK with KEEP/STATS** options to transformational commands [#240011](https://github.com/elastic/kibana/pull/240011)
- Fixes dependencies and service map issues for `txn == exit-span` use cases [#235392](https://github.com/elastic/kibana/pull/235392)
- Fixes the model label display in AI Assistant Settings [#239824](https://github.com/elastic/kibana/pull/239824)
- Updates the **Open in Discover** query in the related Logs section of the **Overview** tab [#240409](https://github.com/elastic/kibana/pull/240409)
- Fixes an issue where the Onboarding Integrations list wasn’t fetched for all pages [#239709](https://github.com/elastic/kibana/pull/239709)
- Fixes an issue where schedules couldn’t be created with **Cases** as the connector type [#239748](https://github.com/elastic/kibana/pull/239748)
- Fixes an issue where operators couldn’t be removed after selection in the **Add rule exception** flyout [#236051](https://github.com/elastic/kibana/pull/236051)
- Fixes `react-query` ID collision issues [#240517](https://github.com/elastic/kibana/pull/240517)
- Updates GenAI Settings to reflect the selected `AI Assistants Visibility` value from the header selector on the Settings page [#239555](https://github.com/elastic/kibana/pull/239555)
- Fixes the inference endpoints UI to ensure the list loads correctly when the provider is custom [#240189](https://github.com/elastic/kibana/pull/240189)
- Fixes the URL in **Disk Usage** alerting rules [#240279](https://github.com/elastic/kibana/pull/240279)
- Fixes data preview metadata pop-up display issues by adding a tooltip and copy button to handle long IDs [#239768](https://github.com/elastic/kibana/pull/239768)
- Fixes the **Agents** and **Playground** icons in the side navigation to render correctly in dark mode [#240475](https://github.com/elastic/kibana/pull/240475)
- Ensures only valid queries are returned for significant events [#239501](https://github.com/elastic/kibana/pull/239501)
- Hides filtering capabilities in Hosts Metrics [#239724](https://github.com/elastic/kibana/pull/239724)
- Releases cluster state so that it can be garbage collected as soon as possible [#136769](https://github.com/elastic/elasticsearch/pull/136769)
- Allows dynamic updates to frequency [#136757](https://github.com/elastic/elasticsearch/pull/136757)
- Returns `ConstNullBlock` in `FromAggMetricDouble` for ES|QL [#136773](https://github.com/elastic/elasticsearch/pull/136773)
- Fixes geo point block loader slowness [#136147](https://github.com/elastic/elasticsearch/pull/136147)
- Prevents `MV_EXPAND` prior to `STATS` with TS in ES|QL [#136931](https://github.com/elastic/elasticsearch/pull/136931)
- Returns a better error message when Timestamp is renamed in TS queries [#136231](https://github.com/elastic/elasticsearch/pull/136231)
- Uses suppliers to get inference results in semantic queries [#136720](https://github.com/elastic/elasticsearch/pull/136720)
- Pushes down eval expressions when they require data access for ES|QL [#136610](https://github.com/elastic/elasticsearch/pull/136610)
- Fixes bug when handling 1-dimension literal vectors for ES|QL [#136891](https://github.com/elastic/elasticsearch/pull/136891)
- Disallows `dot_product` and `max_inner_product` for `int8_hnsw` GPU type [#136881](https://github.com/elastic/elasticsearch/pull/136881)
- Does not attempt to canonicalize `InnerAggregate` [#136854](https://github.com/elastic/elasticsearch/pull/136854)
- Makes equals include ids for `Alias`, `TypedAttribute` [#132455](https://github.com/elastic/elasticsearch/pull/132455)
- Fixes lookup join filter pushdown to use semantic equality [#136818](https://github.com/elastic/elasticsearch/pull/136818)
- Fixes `ignore_unmapped` setting when using `geo_shape` query with a pre-indexed shape [#136961](https://github.com/elastic/elasticsearch/pull/136961)
- Fixes columns ordering when pruning an `INLINE STATS` in ES|QL [#136827](https://github.com/elastic/elasticsearch/pull/136827)
- Validates multiple `GROK` patterns individually [#137082](https://github.com/elastic/elasticsearch/pull/137082)
- Manages `INLINE STATS` count(*) on result sets with no columns in ES|QL [#137017](https://github.com/elastic/elasticsearch/pull/137017)
- Fixes handling equality with `MV constants` properly in ES|QL [#137032](https://github.com/elastic/elasticsearch/pull/137032)
- Improves concurrency design of `EnterpriseGeoIpDownloader` [#134223](https://github.com/elastic/elasticsearch/pull/134223)
- Fixes mapping conflicts in clone, split, and shrink APIs [#137096](https://github.com/elastic/elasticsearch/pull/137096)


## October 20, 2025


### Features and enhancements

- [Agent Builder](https://www.elastic.co/docs/explore-analyze/ai-features/elastic-agent-builder) is now available in technical preview and is enabled by default on Elastic Cloud Serverless
- Lets you remove root privileges from Fleet managed agents [#237790](https://github.com/elastic/kibana/pull/237790)
- Adds the `xpack.fleet.experimentalFeatures` setting [#238840](https://github.com/elastic/kibana/pull/238840)
- Supports expression suggestions within function parameters [#236343](https://github.com/elastic/kibana/pull/236343)
- Updates the Observability Serverless navigation menu [#235984](https://github.com/elastic/kibana/pull/235984)
- Allows the Observability AI Assistant to retrieve information from the  `.integration_knowledge*` system index [#237085](https://github.com/elastic/kibana/pull/237085)
- Adds file download relative URI to response actions that provide file output [#237713](https://github.com/elastic/kibana/pull/237713)
- Updates the UI and API for process descendants in trusted applications [#236318](https://github.com/elastic/kibana/pull/236318)
- Adds usage statistics collection for CSPM cloud connectors [#236992](https://github.com/elastic/kibana/pull/236992)
- Enhances the error message for malformed roles [#239098](https://github.com/elastic/kibana/pull/239098)
- Enables editing feature condition in the feature identification flyout and adds the **Open in Discover** button [#238646](https://github.com/elastic/kibana/pull/238646)
- Improves processing warnings for Streams [#239188](https://github.com/elastic/kibana/pull/239188)
- Enables AI-powered significant event identification for Streams [#239070](https://github.com/elastic/kibana/pull/239070)
- Enables numerical ID service for Cases [#238555](https://github.com/elastic/kibana/pull/238555)
- Adds agent ID as a default observables type [#238533](https://github.com/elastic/kibana/pull/238533)


### Fixes

- Updates `nodemailer` [#238816](https://github.com/elastic/kibana/pull/238816)
- Improves error handling on the **Visualize Listing** page [#238355](https://github.com/elastic/kibana/pull/238355)
- Prevents adhoc dataviews in ES|QL charts from being filtered out in the KQL search bar [#238731](https://github.com/elastic/kibana/pull/238731)
- Fixes a bug in Lens that broke **Click to filter** on table rows when any column was used as a formula [#239222](https://github.com/elastic/kibana/pull/239222)
- Fixes metric color assignment when breakdown and a max dimension are defined in Lens [#238901](https://github.com/elastic/kibana/pull/238901)
- Fixes "package not found" error when skipping cloud onboarding for a prerelease package [#238629](https://github.com/elastic/kibana/pull/238629)
- Fixes an issue with integration policy upgrades [#238542](https://github.com/elastic/kibana/pull/238542)
- Fixes `ignore_above` mapping for `flattened` fields [#238890](https://github.com/elastic/kibana/pull/238890)
- Fixes missing fields when using combined filters with the `ignoreFilterIfFieldNotInIndex` UI setting [#238945](https://github.com/elastic/kibana/pull/238945)
- Displays the available options when editing an existing variable control [#239315](https://github.com/elastic/kibana/pull/239315)
- Fixes `KEEP` behavior in ES|QL when a query initially returns no results [#239063](https://github.com/elastic/kibana/pull/239063)
- Adds a 10 second request timeout to ES|QL query execution [#238200](https://github.com/elastic/kibana/pull/238200)
- Uses `runWithCache` for bulk Fleet operations [#238326](https://github.com/elastic/kibana/pull/238326)
- Fixes error when Observability AI Assistant was disabled [#238811](https://github.com/elastic/kibana/pull/238811)
- Removes unecessary `_source` field from queries [#239205](https://github.com/elastic/kibana/pull/239205)
- Makes the rule condition chart parser replace metric names inside filter values (for example, A in "Accounts") [#238849](https://github.com/elastic/kibana/pull/238849)
- Fixes recover alert while monitor is down [#237479](https://github.com/elastic/kibana/pull/237479)
- Fixes layout of SLO management page combo box filter [#239418](https://github.com/elastic/kibana/pull/239418)
- Adds missing aria-label to BetaBadge component [#239400](https://github.com/elastic/kibana/pull/239400)
- Fixes the "missing authentication credentials" issue in `TelemetryConfigWatcher` and `PolicyWatcher` [#237796](https://github.com/elastic/kibana/pull/237796)
- Fixes an issue with Automatic Migration that prevented you from switching between migrations while translating rules [#238679](https://github.com/elastic/kibana/pull/238679)
- Fixes artifacts spaces migration (`v9.1`) to ensure all artifacts are processed [#238740](https://github.com/elastic/kibana/pull/238740)
- Checks for integrations permissions before loading component [#239122](https://github.com/elastic/kibana/pull/239122)
- Prioritizes connector `defaultModel` over stored conversation model [#237947](https://github.com/elastic/kibana/pull/237947)
- Deselects current selection after index pattern update [#239245](https://github.com/elastic/kibana/pull/239245)
- Fixes graph not rendering when switching tabs or refreshing the page [#238038](https://github.com/elastic/kibana/pull/238038)
- Adds unique accessible labels for **Show top field values** buttons [#237972](https://github.com/elastic/kibana/pull/237972)
- Fixes tool calling unavailable tools [#237174](https://github.com/elastic/kibana/pull/237174)
- Adds Jira's `otherFields` JSON editor to case creation flow [#238435](https://github.com/elastic/kibana/pull/238435)
- Updates connector API [#236863](https://github.com/elastic/kibana/pull/236863)
- Separates sync alert and auto-extract updates in activity log [#236519](https://github.com/elastic/kibana/pull/236519)
- Fixes auto extraction of observables in EASE [#239000](https://github.com/elastic/kibana/pull/239000)
- Removes `autoFocus` to preserve proper focus upon modal close [#239366](https://github.com/elastic/kibana/pull/239366)
- Adds manual focus to the Cases action button's actions [#239504](https://github.com/elastic/kibana/pull/239504)
- Fixes the behavior of Security serverless projects' Tier 1 and Tier 2 analyst roles by revoking their Endpoint exceptions read access


## October 15, 2025

- Elastic Cloud Serverless is now available in two new Amazon Web Services [regions](https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud/regions): `ap-northeast-1` (Tokyo) and `eu-west-2` (London)


## October 13, 2025


### Features and enhancements

- Adds a new `MIGRATE` action type for migrating agents to a different cluster [#237342](https://github.com/elastic/kibana/pull/237342).
- Adds a **Show agentless resources** toggle on the Fleet > Settings page for debugging and diagnostics [#237528](https://github.com/elastic/kibana/pull/237528)
- Allows you to carry over the controls when navigating to a dashboard, preserving the histogram [#237070](https://github.com/elastic/kibana/pull/237070)
- Enables the risk score reset feature [#237829](https://github.com/elastic/kibana/pull/237829)
- Uses ES|QL for calculating risk scores [#237871](https://github.com/elastic/kibana/pull/237871)
- Adds Security ML modules for GCP Audit and Azure Activity Logs [#236849](https://github.com/elastic/kibana/pull/236849)
- Removes the global empty state redirect [#237612](https://github.com/elastic/kibana/pull/237612)
- Replaces the existing document count chart with RED metrics [#236635](https://github.com/elastic/kibana/pull/236635)
- Blocks disabling adaptive allocations
- Adds Google Model Garden's Meta, Mistral, Hugging Face and Ai21 providers support to Inference Plugin [#135701](https://github.com/elastic/elasticsearch/pull/135701)
- Adds `Clamp` family of functions [#135822](https://github.com/elastic/elasticsearch/pull/135822)
- Optionally ignores field when indexed field name exceeds length limit [#136143](https://github.com/elastic/elasticsearch/pull/136143)
- Adds optional parameters support to KQL function for ES|QL [#135895](https://github.com/elastic/elasticsearch/pull/135895)
- Adds on-disk rescoring to disk BBQ [#135778](https://github.com/elastic/elasticsearch/pull/135778)
- Enables the `TEXT_EMBEDDING` function in non-snapshot builds for ES|QL [#136103](https://github.com/elastic/elasticsearch/pull/136103)
- Adds DirectIO bulk rescoring [#135380](https://github.com/elastic/elasticsearch/pull/135380)
- Late materialization after `TopN` (Node level) [#132757](https://github.com/elastic/elasticsearch/pull/132757)
- Adds `m` alias for `minute` duration literal [#136448](https://github.com/elastic/elasticsearch/pull/136448)
- Adds convenience API key parameter to remote reindex [#135949](https://github.com/elastic/elasticsearch/pull/135949)
- Adds `match_only_text` subfield to `*.display_name` fields in `ecs@mappings` to be compliant with the latest additions in ECS [#136265](https://github.com/elastic/elasticsearch/pull/136265)


### Fixes

- Fixes an error that occurred when deleting orphaned integration policies [#237875](https://github.com/elastic/kibana/pull/237875)
- Prevents creation of default alerts when no connectors are defined [#237504](https://github.com/elastic/kibana/pull/237504)
- Turns off the maximum attempts limit for the private locations sync task [#237784](https://github.com/elastic/kibana/pull/237784)
- Fixes a flyout rendering issue [#237840](https://github.com/elastic/kibana/pull/237840)
- Corrects icon colors in the side navigation [#237970](https://github.com/elastic/kibana/pull/237970)
- Fixes a bug that affected the controls on the Alerts page [#236756](https://github.com/elastic/kibana/pull/236756)
- Updates the names of the **Security solution default** and **Security solution alerts** data views in the data view picker [#238354](https://github.com/elastic/kibana/pull/238354)
- Fixes a bug that caused the flyout on the Files management page to crash when there were uploaded files [#237588](https://github.com/elastic/kibana/pull/237588)
- Introduces a separate error message for empty login attempts with `saml/oidc` providers [#237611](https://github.com/elastic/kibana/pull/237611)
- Fixes an issue in the component template creation flow where creating a new template with an `@custom` suffix in its name could incorrectly update mappings for unrelated data streams and trigger rollover prompts [#237952](https://github.com/elastic/kibana/pull/237952)
- Fixes an issue where the retriever query copied from the **Search your data** JavaScript tutorial failed with `parsing_exception` when passed as a query parameter in the Node.js client; retriever queries are now passed in the request body to ensure correct serialization [#237654](https://github.com/elastic/kibana/pull/237654)
- Ensures the Index management mappings editor synchronizes the model deployment status correctly [#237812](https://github.com/elastic/kibana/pull/237812)
- Fixes an accessibility issue where resetting changes or removing all terms in the Synonyms panel was not announced by screen readers [#237877](https://github.com/elastic/kibana/pull/237877)
- Fixes an issue in the RAG Playground where invalid fields were highlighted but no error message appeared [#238284](https://github.com/elastic/kibana/pull/238284)
- Improves the performance of the clustering algorithm [#238394](https://github.com/elastic/kibana/pull/238394)
- Makes the Cohere service Model Id field required [#136017](https://github.com/elastic/elasticsearch/pull/136017)
- Ensures queued `AbstractRunnables` are notified when executor stops [#135966](https://github.com/elastic/elasticsearch/pull/135966)
- Removes rate limit field from services API for EIS [#135838](https://github.com/elastic/elasticsearch/pull/135838)
- Initializes `TermsEnum` eagerly [#136279](https://github.com/elastic/elasticsearch/pull/136279)
- Fixes LogsDB settings provider mapping filters [#136119](https://github.com/elastic/elasticsearch/pull/136119)
- Provides defaults for index sort settings [#135886](https://github.com/elastic/elasticsearch/pull/135886)
- Stores full path in `_ignored` when ignoring dynamic array field [#136315](https://github.com/elastic/elasticsearch/pull/136315)
- Removes null from `syntheticSourceFallbackFieldName` [#136344](https://github.com/elastic/elasticsearch/pull/136344)
- Delays automaton creation in BinaryDvConfirmedQuery to avoid out of memory (OOM) on queries against WildCard fields [#136086](https://github.com/elastic/elasticsearch/pull/136086)
- Fixes inference fields handling on old indices [#136312](https://github.com/elastic/elasticsearch/pull/136312)
- Fixes projection generation when pruning `left join` [#135446](https://github.com/elastic/elasticsearch/pull/135446)
- Replaces any `Attribute` type when pushing down past Project [#135295](https://github.com/elastic/elasticsearch/pull/135295)
- Fixes an ES|QL breaker bug [#136105](https://github.com/elastic/elasticsearch/pull/136105)
- Fixes `Page.equals()` [#136266](https://github.com/elastic/elasticsearch/pull/136266)
- Uses index setting providers for data stream setting validation [#136214](https://github.com/elastic/elasticsearch/pull/136214)


## October 6, 2025


### Features and enhancements

- Adds support for encrypted headers in the Webhook connector to enhance security [#233695](https://github.com/elastic/kibana/pull/233695)
- Allows users to add custom fields to the IBM Resilient connector [#236144](https://github.com/elastic/kibana/pull/236144)
- Renames Fleet Server Host SSL options for clarity [#236887](https://github.com/elastic/kibana/pull/236887)
- Enables Discover tabs by default, allowing you to manage multiple data explorations in parallel [#235150](https://github.com/elastic/kibana/pull/235150)
- Automatically extracts case observables in the **Add to case** workflow [#233027](https://github.com/elastic/kibana/pull/233027)
- Introduces missing icons and updates v2 icons for the ECH Observability navigation [#236808](https://github.com/elastic/kibana/pull/236808)
- Adds a metrics dashboard for non-EDOT agents in the OpenTelemetry native ingestion path [#236978](https://github.com/elastic/kibana/pull/236978)
- Adds public APIs for Attack Discovery and Attack Discovery schedules [#236736](https://github.com/elastic/kibana/pull/236736)
- Enables automatic observable extraction in the Alerts table [#235433](https://github.com/elastic/kibana/pull/235433)
- Turns on the `newDataViewPickerEnabled` feature flag [#234101](https://github.com/elastic/kibana/pull/234101)
- Adds the ability to discover privileged users from the Entity Analytics Okta integration [#237129](https://github.com/elastic/kibana/pull/237129)
- Allows you to select which AI Assistant to show in the Elastic header; moves the **AI Assistant visibility** setting to the **GenAI Settings** page [#233727](https://github.com/elastic/kibana/pull/233727)
- Adds a new `update_all` endpoint for product documentation management [#231884](https://github.com/elastic/kibana/pull/231884)
- Adds an icon for Contextual AI in the AI Connector and inference endpoint creation UI [#236951](https://github.com/elastic/kibana/pull/236951)
- Enables the new background search experience for improved performance [#236818](https://github.com/elastic/kibana/pull/236818)
- Adds triple-quote support to the Manual Ingest Pipeline Processor editor [#236595](https://github.com/elastic/kibana/pull/236595)
- Introduces the German locale for Kibana in `beta` [#236903](https://github.com/elastic/kibana/pull/236903)
- Adds an advanced option to disable filtering of file-backed volumes and CD-ROMs in the **Device Control** plugin [#236620](https://github.com/elastic/kibana/pull/236620)
- Adds `RerankRequestChunker` [#130485](https://github.com/elastic/elasticsearch/pull/130485)
- Adds usage stats for semantic_text fields [#135262](https://github.com/elastic/elasticsearch/pull/135262)
- Upgrades to Lucene 10.3.0
- Improves TSDB ingestion by hashing dimensions only once, using a new auto-populeted `index.dimensions` private index setting [#135402](https://github.com/elastic/elasticsearch/pull/135402)
- Adds index setting that disables the `index.dimensions` based routing and `_tsid` creation strategy [#135673](https://github.com/elastic/elasticsearch/pull/135673)
- Updates to Lucene 10.3.1
- Adds GPUPlugin for building vector indices on GPU [#135545](https://github.com/elastic/elasticsearch/pull/135545)
- Makes FUSE available in release builds for ES|QL [#135603](https://github.com/elastic/elasticsearch/pull/135603)
- Adds `dense_vector` field type and `to_dense_vector` function to release builds for ES|QL [#135604](https://github.com/elastic/elasticsearch/pull/135604)
- Updates to Lucene 10.3.1 [#136030](https://github.com/elastic/elasticsearch/pull/136030)
- Adds KNN function in ES|QL [#135709](https://github.com/elastic/elasticsearch/pull/135709)
- Runs single phase aggregation when possible [#131485](https://github.com/elastic/elasticsearch/pull/131485)
- Fills in `topn` values if competitive [#135734](https://github.com/elastic/elasticsearch/pull/135734)
- Makes order in TOP optional [#135932](https://github.com/elastic/elasticsearch/pull/135932)
- Adds option for `Append Processor` to skip/allow empty values [#105718](https://github.com/elastic/elasticsearch/pull/105718)
- Adds small optimizations to `PUT _component_template` API [#135644](https://github.com/elastic/elasticsearch/pull/135644)


### Fixes

- Rolls over the reporting data stream automatically when a newer template version is available [#234119](https://github.com/elastic/kibana/pull/234119)
- Fixes an issue where exported CSV columns in Lens tables could appear out of order [#236673](https://github.com/elastic/kibana/pull/236673)
- Fixes a bug causing Controls to fetch data twice [#237169](https://github.com/elastic/kibana/pull/237169)
- Removes the incorrect `fleet.ssl` configuration option [#236788](https://github.com/elastic/kibana/pull/236788)
- Fixes MSI commands (#233750) [#236994](https://github.com/elastic/kibana/pull/236994)
- Removes unnecessary span documents from the `getServiceAgent` function [#236732](https://github.com/elastic/kibana/pull/236732)
- Cleans up extra Synthetics package policies [#235200](https://github.com/elastic/kibana/pull/235200)
- Reverts a change to the page attachment type in Elastic Observability Serverless [#236958](https://github.com/elastic/kibana/pull/236958)
- Removes `null` values in the confirmation dialog when bulk-editing index patterns for rules [#236572](https://github.com/elastic/kibana/pull/236572)
- Increases the z-index of Timeline and related flyout components so they appear above the side navigation [#236655](https://github.com/elastic/kibana/pull/236655)
- Adds support for API key wildcard search [#221959](https://github.com/elastic/kibana/pull/221959)
- Hides the **Show forecast** button when changing jobs in the Single Metric Viewer [#236724](https://github.com/elastic/kibana/pull/236724)
- Improves performance of the Trained Models list [#237072](https://github.com/elastic/kibana/pull/237072)
- Fixes partition field settings errors in the Single Metric Viewer dashboard panels [#237046](https://github.com/elastic/kibana/pull/237046)
- Fixes layout issues with the **Parse in streams** button on smaller flyouts [#236548](https://github.com/elastic/kibana/pull/236548)
- Displays `(missing value)` and `(empty)` instead of `null` in charts and tables [#233369](https://github.com/elastic/kibana/pull/233369)
- Fixes privilege requirements for reindexing indices in Upgrade Assistant [#237055](https://github.com/elastic/kibana/pull/237055)
- Resets the health status on a successful empty checkpoint [#135653](https://github.com/elastic/elasticsearch/pull/135653)
- Switches `TextExpansionQueryBuilder` and `TextEmbeddingQueryVectorBuilder` to return 400 instead of 500 errors [#135800](https://github.com/elastic/elasticsearch/pull/135800)
- Allows merging of passthrough mappers with object mappers under certain conditions in downsampling [#135431](https://github.com/elastic/elasticsearch/pull/135431)
- Prevents storing keyword multi fields when they trip `ignore_above` [#132962](https://github.com/elastic/elasticsearch/pull/132962)
- Fixes KQL case-sensitivity for keyword fields in ES|QL [#135776](https://github.com/elastic/elasticsearch/pull/135776)
- Passes fixed size instead of `maxPageSize` to `LuceneTopNOperator` scorer for ES|QL [#135767](https://github.com/elastic/elasticsearch/pull/135767)
- Fixes missing minimum competitive similarity check on tail documents in DiskBBQ [#135851](https://github.com/elastic/elasticsearch/pull/135851)
- Applies source excludes early when retrieving `_inference_fields` [#135897](https://github.com/elastic/elasticsearch/pull/135897)
- Fixes `UnsupportedOperationException` when cardinality aggregator field type is vector [#135994](https://github.com/elastic/elasticsearch/pull/135994)
- Fixes crash when creating semantic_text fields on pre-8.11 indices [#135845](https://github.com/elastic/elasticsearch/pull/135845)
- Fixes union types lost attributes in `StubRelation` for `inlinestats` [#135547](https://github.com/elastic/elasticsearch/pull/135547)
- Fixes wrong pruning of plans with no output columns [#133405](https://github.com/elastic/elasticsearch/pull/133405)
- Supports dot and parameters in `FUSE GROUP BY` [#135901](https://github.com/elastic/elasticsearch/pull/135901)
- Avoids rewrite `round_to` with expensive queries [#135987](https://github.com/elastic/elasticsearch/pull/135987)


## September 29, 2025


### Features and enhancements

- Updates the Observability navigation menu [#236001](https://github.com/elastic/kibana/pull/236001)
- Enables cancelling response actions sent to hosts running Microsoft Defender Endpoint [#230399](https://github.com/elastic/kibana/pull/230399)
- Adds each alert's reason for closing to the Alerts page [#226590](https://github.com/elastic/kibana/pull/226590)
- Adds the Endpoint exceptions sub-privilege [#233433](https://github.com/elastic/kibana/pull/233433)
- Updates the source saved object schema to enable integrations sync markers [#236457](https://github.com/elastic/kibana/pull/236457)
- Updates the indicator details flyout [#230593](https://github.com/elastic/kibana/pull/230593)
- Adds an advanced policy `windows.advanced.firewall_anti_tamper` that lets you set the firewall anti-tamper plugin to off or detect-only [#236431](https://github.com/elastic/kibana/pull/236431)
- Displays document count chart for ES|QL categorize queries [#231459](https://github.com/elastic/kibana/pull/231459)
- Lets you manually map new fields from the schema editor [#235919](https://github.com/elastic/kibana/pull/235919)
- Adds AI-generative partition suggestions to Streams [#235759](https://github.com/elastic/kibana/pull/235759)
- In Streams, allows you to create routing conditions directly from preview table cells [#235560](https://github.com/elastic/kibana/pull/235560)
- Adds an option to convert an index to a lookup index to the **Manage index** menu [#233998](https://github.com/elastic/kibana/pull/233998)
- Improves code examples in the Synonyms UI [#235944](https://github.com/elastic/kibana/pull/235944)
- Automatically copies source data into the alerts-as-data documents for other ES Query rule types [#230010](https://github.com/elastic/kibana/pull/230010)
- Replaces the dashboard editor toolbar with the **Add** menu [#230324](https://github.com/elastic/kibana/pull/230324)
- Adds support for package spec v3.5 [#235942](https://github.com/elastic/kibana/pull/235942)
- Adds **View in discover** button in alert details page for SLO burn rate and ES query rules [#233855](https://github.com/elastic/kibana/pull/233855)
- Adds custom headers support for OpenAI text embeddings [#134960](https://github.com/elastic/elasticsearch/pull/134960)
- Adds ContextualAI inference service [#134933](https://github.com/elastic/elasticsearch/pull/134933)
- Adds classes to represent raw docs sampling configs [#134585](https://github.com/elastic/elasticsearch/pull/134585)
- Adds ES|QL support for expressions with LOOKUP JOIN in tech preview [#134952](https://github.com/elastic/elasticsearch/pull/134952)
- Un-snapshots all 3 URL scalar functions in ES|QL [#135272](https://github.com/elastic/elasticsearch/pull/135272)
- Takes `INLINE STATS` out of snapshot in ES|QL [#135403](https://github.com/elastic/elasticsearch/pull/135403)
- Improves performance for `LOOKUP JOIN` on Expression in ES|QL [#135036](https://github.com/elastic/elasticsearch/pull/135036)
- Releases DiskBBQ (`bbq_disk`) index type for `dense_vector` fields [#135299](https://github.com/elastic/elasticsearch/pull/135299)
- Adds 'profile' support for knn query on HNSW with early termination [#135342](https://github.com/elastic/elasticsearch/pull/135342)
- Enables chunk_rescorer in text_similarity_reranker [#135198](https://github.com/elastic/elasticsearch/pull/135198)
- Enables Semantic Search CCS When ccs_minimize_roundtrips=true [#135309](https://github.com/elastic/elasticsearch/pull/135309)
- Adds support for extended search usage telemetry [#135306](https://github.com/elastic/elasticsearch/pull/135306)
- Implements `Delta` function for absolute change in gauges over time [#135035](https://github.com/elastic/elasticsearch/pull/135035)
- Improves the block loader for source-only runtime date fields [#135373](https://github.com/elastic/elasticsearch/pull/135373)
- Adds an OTLP metrics endpoint (`_otlp/v1/metrics`) as tech preview [#135401](https://github.com/elastic/elasticsearch/pull/135401)
- Adds `pattern_text` field mapper in tech preview [#135370](https://github.com/elastic/elasticsearch/pull/135370)
- Uses optimized field visitor for ignored source queries [#135039](https://github.com/elastic/elasticsearch/pull/135039)
- Improves the block loader for source-only runtime IP fields [#135393](https://github.com/elastic/elasticsearch/pull/135393)


### Fixes

- Adjusts **Cancel** button height in Discover's tabs enabled view [#236118](https://github.com/elastic/kibana/pull/236118)
- Fixes dashboard title not updating when edited from content editor [#236561](https://github.com/elastic/kibana/pull/236561)
- Adds a unique count to transforms on the integrations overview to fix overcounting error [#236177](https://github.com/elastic/kibana/pull/236177)
- Fixes malformed synthetics package policies [#236176](https://github.com/elastic/kibana/pull/236176)
- Fixes controls trigger across various commands [#236121](https://github.com/elastic/kibana/pull/236121)
- Reverts filter policy inputs [#236104](https://github.com/elastic/kibana/pull/236104)
- Fixes the multiselect issue inside the toolbar selector when search is used [#236091](https://github.com/elastic/kibana/pull/236091)
- Integrates dataview logic into host KPIs charts [#236084](https://github.com/elastic/kibana/pull/236084)
- Fixes integrations RAG [#234211](https://github.com/elastic/kibana/pull/234211)
- Ensures the data view picker icon is always vertically centered [#236379](https://github.com/elastic/kibana/pull/236379)
- Fixes browser fields cache [#234381](https://github.com/elastic/kibana/pull/234381)
- Fixes the URL passed to detection rule actions using the `{{context.results_link}}` placeholder [#236067](https://github.com/elastic/kibana/pull/236067)
- Refactors `nav_control_popover` [#235780](https://github.com/elastic/kibana/pull/235780)
- Allows `xpack.spaces.defaultSolution` to be configured using docker [#236570](https://github.com/elastic/kibana/pull/236570)
- Fixes the Job details fly-out on the Analytics Map page [#236131](https://github.com/elastic/kibana/pull/236131)
- Limits `msearch` usage for log rate analysis [#235611](https://github.com/elastic/kibana/pull/235611)
- Fixes display of alerts from anomaly detection rules in [#236289](https://github.com/elastic/kibana/pull/236289)
- Adds `time` field to the get data views response schema [#235975](https://github.com/elastic/kibana/pull/235975)
- Adds `managed` field to the get data views response schema [#236237](https://github.com/elastic/kibana/pull/236237)
- Validates Logstash pipeline IDs sent to Kibana APIs [#236347](https://github.com/elastic/kibana/pull/236347)
- Adds `.reindexed-v7-ml-anomalies-*` to anomaly results template index pattern (#135270) [#135286](https://github.com/elastic/elasticsearch/pull/135286)
- Tolerates mixed types in datafeed stats sort [#135096](https://github.com/elastic/elasticsearch/pull/135096)
- Fixes a bug in the get transform API that incorrectly claims some transform configurations are missing [#134963](https://github.com/elastic/elasticsearch/pull/134963)
- Gracefully shuts down model deployment when node is removed from assignment routing [#134673](https://github.com/elastic/elasticsearch/pull/134673)
- Throws 4xx instead of 5xx for ES|QL malformed query params [#134879](https://github.com/elastic/elasticsearch/pull/134879)
- Renames `index.mapping.patterned_text.disable_templating` [#135049](https://github.com/elastic/elasticsearch/pull/135049)
- Fixes async query inconsistent headers [#135078](https://github.com/elastic/elasticsearch/pull/135078)
- Fixes alias id when dropping all aggregates [#135247](https://github.com/elastic/elasticsearch/pull/135247)
- Handles right hand side of inline stats becoming optimized with `LocalRelation` shortcut in ES|QL [#135011](https://github.com/elastic/elasticsearch/pull/135011)
- Correctly apply field path to JSON processor when adding contents to document root [#135479](https://github.com/elastic/elasticsearch/pull/135479)


## September 22, 2025


### Features and enhancements

- Adds a new connector for Jira Service Management [#235408](https://github.com/elastic/kibana/pull/235408)
- Adds OAuth2 client credentials authentication support to Kibana Webhook connectors [#218442](https://github.com/elastic/kibana/pull/218442)
- Completes OTel configuration pipelines by adding an exporter [#233090](https://github.com/elastic/kibana/pull/233090)
- Enables controls in Discover from the editor [#229598](https://github.com/elastic/kibana/pull/229598)
- Displays errors in the context of a trace [#234178](https://github.com/elastic/kibana/pull/234178)
- Creates functional tests for the Logs Essentials tier [#234904](https://github.com/elastic/kibana/pull/234904)
- Sets up the saved object infrastructure for Cloud Connectors and implements the end-to-end persistence flow for creating integrations with Cloud Connector support [#230137](https://github.com/elastic/kibana/pull/230137)
- Removes the **Tech Preview** badge and feature flag for Automatic Troubleshooting [#234853](https://github.com/elastic/kibana/pull/234853)
- Adds advanced options for opting out of collecting ransomware diagnostics on macOS [#235193](https://github.com/elastic/kibana/pull/235193)
- Adds the **Tech Preview** badge for the preconfigured `rerank` endpoint in the inference endpoints UI [#235222](https://github.com/elastic/kibana/pull/235222)
- Adds a default placeholder icon for future AI connectors [#235166](https://github.com/elastic/kibana/pull/235166)
- Adds search functionality to the Query rules details page [#232579](https://github.com/elastic/kibana/pull/232579)
- Adds a link to Agent Builder in the **View Data** dropdown [#234679](https://github.com/elastic/kibana/pull/234679)
- Adds the AutoOps Search tier page, which provides project-level insights and deeper insights into Serverless resources (VCUs) and performances
- Adds headers support for OpenAI chat completion [#134504](https://github.com/elastic/elasticsearch/pull/134504)
- Better `max_age` rollover for tiny retentions in data lifecycle management [#134941](https://github.com/elastic/elasticsearch/pull/134941)
- Removes ingest conditionals `_type` deprecation warning [#134851](https://github.com/elastic/elasticsearch/pull/134851)
- Adds telemetry support for `LOOKUP JOIN` on Expression in ES|QL [#134942](https://github.com/elastic/elasticsearch/pull/134942)
- Adds support for include_execution_metadata parameter in ES|QL [#134446](https://github.com/elastic/elasticsearch/pull/134446)
- Adds `LOOKUP JOIN` with expressions in ES|QL [#134098](https://github.com/elastic/elasticsearch/pull/134098)
- Allows including semantic field embeddings in `_source` [#134717](https://github.com/elastic/elasticsearch/pull/134717)
- Integrates weights into simplified RRF retriever syntax [#132680](https://github.com/elastic/elasticsearch/pull/132680)
- Supports querying multiple indices with the simplified RRF retriever [#134822](https://github.com/elastic/elasticsearch/pull/134822)
- Improves the block loader for source-only runtime fields with keyword scripts [#135026](https://github.com/elastic/elasticsearch/pull/135026)

- Adds relevant attributes to search took time APM metrics [#134232](https://github.com/elastic/elasticsearch/pull/134232)
- Adds headers support for OpenAI chat completion [#134504](https://github.com/elastic/elasticsearch/pull/134504)
- Extends `kibana-system` permissions to manage security entities [#133968](https://github.com/elastic/elasticsearch/pull/133968)
- Tracks `shardStarted` events for simulation in `DesiredBalanceComputer` [#133630](https://github.com/elastic/elasticsearch/pull/133630)
- Adds file extension metadata to cache miss counter when it’s updated by `SharedBlobCacheService` [#134374](https://github.com/elastic/elasticsearch/pull/134374)
- Removes the `_type` deprecation warning in ingest conditional scripts [#134851](https://github.com/elastic/elasticsearch/pull/134851)
- Allows including semantic field embeddings in `_source` [#134717](https://github.com/elastic/elasticsearch/pull/134717)
- Integrates weights into simplified RRF retriever syntax [#132680](https://github.com/elastic/elasticsearch/pull/132680)
- Adjusts rollover criteria to have a better `max_age` rollover for tiny retentions [#134941](https://github.com/elastic/elasticsearch/pull/134941)
- Adds support for the `include_execution_metadata` parameter in ES|QL [#134446](https://github.com/elastic/elasticsearch/pull/134446)
- Adds telemetry support for Lookup Join On Expression in ES|QL [#134942](https://github.com/elastic/elasticsearch/pull/134942)
- Improves block loader for source-only runtime fields of type keyword [#135026](https://github.com/elastic/elasticsearch/pull/135026)
- Optimizes `BytesArray::indexOf` used in ndjson parsing [#135087](https://github.com/elastic/elasticsearch/pull/135087)
- Modifies `SecureString` methods (`equals`, `startsWith` and `regionMatches`) to operate in constant time relative to the length of the comparison string [#135053](https://github.com/elastic/elasticsearch/pull/135053)
- Updates URL encoding in ES|QL [#134503](https://github.com/elastic/elasticsearch/pull/134503)
- Adds new `/_security/stats` endpoint [#134835](https://github.com/elastic/elasticsearch/pull/134835)
- Makes the last source shard completely remove reshard metadata
- Adds a monitor for estimated heap usage


### Fixes

- Skips automatic scrolling when a panel is visible [#233226](https://github.com/elastic/kibana/pull/233226)
- Fixes an issue with the Actions column header size [#235227](https://github.com/elastic/kibana/pull/235227)
- Clears time field sorting when switching from classic to ES|QL mode [#235338](https://github.com/elastic/kibana/pull/235338)
- Fixes a bug where previously installed product docs (E5) were not upgraded during a Kibana version upgrade [#234792](https://github.com/elastic/kibana/pull/234792)
- Improves the accessibility of the badges on individual stream pages [#235625](https://github.com/elastic/kibana/pull/235625)
- Fixes the autocomplete configuration for the `pinned` retriever by removing the `match_criteria` field [#234903](https://github.com/elastic/kibana/pull/234903)
- Fixes a bug by allowing the use of `cmd + /` for comment toggling in the Monaco editor [#235334](https://github.com/elastic/kibana/pull/235334)
- Adds a check for all privileges for Elastic Security Serverless when creating lists [#234602](https://github.com/elastic/kibana/pull/234602)
- Fixes a bug to correctly update SLM stats when the master node is shut down after an SLM-triggered snapshot is completed [#134152](https://github.com/elastic/elasticsearch/pull/134152)
- Fixes a bug to facilitate second retrieval of the same value [#134790](https://github.com/elastic/elasticsearch/pull/134790)
- Avoids holding references to `SearchExecutionContext` in `SourceConfirmedTextQuery` [#134887](https://github.com/elastic/elasticsearch/pull/134887)
- Adds an exception for perform embedding inference requests which include a query [#131641](https://github.com/elastic/elasticsearch/pull/131641)
- Fixes a bug where the match only text block loader was not working correctly when a keyword multi-field was present [#134582](https://github.com/elastic/elasticsearch/pull/134582)
- Fixes conditional processor mutability bugs [#134936](https://github.com/elastic/elasticsearch/pull/134936)
- Fixes a bug where transforms did not wait for PITs to close [#134955](https://github.com/elastic/elasticsearch/pull/134955)
- Bypasses MMap arena grouping which caused issues with too many regions being mapped [#135012](https://github.com/elastic/elasticsearch/pull/135012)
- Fixes a deadlock in `ThreadPoolMergeScheduler` when a failing merge closes the `IndexWriter` [#134656](https://github.com/elastic/elasticsearch/pull/134656)
- Fixes `countDistinctWithConditions` in csv-spec tests [#135097](https://github.com/elastic/elasticsearch/pull/135097)
- Fixes a bug where `CentroidCalculator` did not return negative summation weights [#135176](https://github.com/elastic/elasticsearch/pull/135176)
- Limits the `topn` operations pushed to Lucene to 10,000 [#134497](https://github.com/elastic/elasticsearch/pull/134497)
- Bans `LIMIT` and `MV_EXPAND` before remote `ENRICH` [#135051](https://github.com/elastic/elasticsearch/pull/135051)
- Fixes expiration time in ES|QL async [#135209](https://github.com/elastic/elasticsearch/pull/135209)
- Fixes match only text block loader not working when a keyword multi field is present [#134582](https://github.com/elastic/elasticsearch/pull/134582)
- Avoids holding references to `SearchExecutionContext` in `SourceConfirmedTextQuery` [#134887](https://github.com/elastic/elasticsearch/pull/134887)


## September 19, 2025


### Features and enhancements

- Elastic Cloud Serverless is now available in three new Google Cloud Platform [regions](https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud/regions): GCP South Carolina (`us-east1`), GCP Virginia (`us-east4`), and GCP Oregon (`us-west1`).


## September 15, 2025


### Features and enhancements

- Improves the ES|QL suggestions logic when a query changes [#231767](https://github.com/elastic/kibana/pull/231767)
- Updates the appearance popover in Lens metric charts [#233992](https://github.com/elastic/kibana/pull/233992)
- Adds support for installing `alerting_rule_template` assets from packages [#233533](https://github.com/elastic/kibana/pull/233533)
- Removes the default query limit of 10 [#234349](https://github.com/elastic/kibana/pull/234349)
- Adds support for remote cluster lookup mode indices in the editor [#232907](https://github.com/elastic/kibana/pull/232907)
- Extends ES|QL autocomplete to include columns from lookup indices and enrichment policies after `LOOKUP JOIN` and `ENRICH` commands [#233221](https://github.com/elastic/kibana/pull/233221)
- Adds a trace waterfall visualization for logs [#234072](https://github.com/elastic/kibana/pull/234072)
- Adds end-to-end UI tests for onboarding page validation [#232363](https://github.com/elastic/kibana/pull/232363)
- Updates the Playwright end-to-end tests to support Logs Essentials tier functionality [#234644](https://github.com/elastic/kibana/pull/234644)
- Introduces a Security Risk Scoring AI Assistant tool [#233647](https://github.com/elastic/kibana/pull/233647)
- Enables the SentinelOne `runscript` response action [#234492](https://github.com/elastic/kibana/pull/234492)
- Extends the `origin_info_collection` advanced policy setting to include `origin_url`, `origin_referrer_url`, and `Ext.windows.zone_identifier` fields for Windows process events [#234268](https://github.com/elastic/kibana/pull/234268)
- Restricts access to the Value report page to `admin` and `soc_manager` roles in complete tier [#234377](https://github.com/elastic/kibana/pull/234377)
- Ensures the **Tech Preview** badge is shown for the default inference endpoint for e5 on the inference endpoints UI [#234811](https://github.com/elastic/kibana/pull/234811)
- Ensures mapped fields are remembered across simulations [#233799](https://github.com/elastic/kibana/pull/233799)
- Adds time series telemetry in xpack usage [#134214](https://github.com/elastic/elasticsearch/pull/134214)
- Caches inference endpoints [#133860](https://github.com/elastic/elasticsearch/pull/133860)
- Adds `recover_failure_document` processor to remediate failurestore docs [#133360](https://github.com/elastic/elasticsearch/pull/133360)
- Adds SET instruction in ES|QL [#134029](https://github.com/elastic/elasticsearch/pull/134029)
- Adds `PRESENT` ES|QL function [#133986](https://github.com/elastic/elasticsearch/pull/133986)
- Adds `PresentOverTime` ES|QL function [#134355](https://github.com/elastic/elasticsearch/pull/134355)
- Allows multivalued query parameters in ES|QL [#134317](https://github.com/elastic/elasticsearch/pull/134317)
- Adds `Absent` and `AbsentOverTime` ES|QL functions [#134475](https://github.com/elastic/elasticsearch/pull/134475)
- Enables caching of all filters in `knn` queries [#134458](https://github.com/elastic/elasticsearch/pull/134458)
- Enables text similarity reranker to chunk and score snippets [#133576](https://github.com/elastic/elasticsearch/pull/133576)
- Supports querying multiple indices with the simplified linear retriever [#133720](https://github.com/elastic/elasticsearch/pull/133720)
- Adds time series telemetry in xpack usage for downsampling [#134214](https://github.com/elastic/elasticsearch/pull/134214)
- Skips null metrics in ES|QL [#133087](https://github.com/elastic/elasticsearch/pull/133087)
- Improves block loader for source only runtime fields of type long [#134117](https://github.com/elastic/elasticsearch/pull/134117)
- Improves block loader for source only runtime fields of type double [#134629](https://github.com/elastic/elasticsearch/pull/134629)
- Implements `idelta` function for ES|QL [#134510](https://github.com/elastic/elasticsearch/pull/134510)


### Fixes

- Hides the side navigation during report generation [#234675](https://github.com/elastic/kibana/pull/234675)
- Fixes a bug where the save modal allowed duplicate saves of dashboards, visualizations, and other assets [#233933](https://github.com/elastic/kibana/pull/233933)
- Fixes an issue with special character handling when creating a pipeline from the flyout [#233651](https://github.com/elastic/kibana/pull/233651)
- Fixes a bug where the toggle column only worked on the Alerts page [#234278](https://github.com/elastic/kibana/pull/234278)
- Correctly updates the `@timestamp` and `event.ingested` fields when a privileged user is updated [#233735](https://github.com/elastic/kibana/pull/233735)
- Returns a `500` response code if there is an error during monitoring engine initialization [#234368](https://github.com/elastic/kibana/pull/234368)
- Fixes table highlighting issues in flyouts [#234222](https://github.com/elastic/kibana/pull/234222)
- Fixes issues in AI Assistant where it didn't append conversation messages or update titles [#233219](https://github.com/elastic/kibana/pull/233219)
- Enables repeated System Prompt navigation from the **Conversations** tab [#234812](https://github.com/elastic/kibana/pull/234812)
- Increases the `bulkGet` limit [#234151](https://github.com/elastic/kibana/pull/234151)
- Fixes an issue on the API Keys Management page that occurred when loading API keys with null names [#234083](https://github.com/elastic/kibana/pull/234083)
- Fixes an Anomaly Detection bug where custom URLs omitted generated fields in datafeed preview requests [#234709](https://github.com/elastic/kibana/pull/234709)
- Ensures full tool traces are displayed in flyouts [#234654](https://github.com/elastic/kibana/pull/234654)
- Prevents field caps from failing due to can match failure [#134134](https://github.com/elastic/elasticsearch/pull/134134)
- Uses inner query for `equals` and `hashCode` in `SourceConfirmedTextQuery` [#134451](https://github.com/elastic/elasticsearch/pull/134451)
- Fixes a bug where text fields in LogsDB indices did not use their keyword multi fields for block loading [#134253](https://github.com/elastic/elasticsearch/pull/134253)
- Uses latest setting value when initializing setting watch [#134091](https://github.com/elastic/elasticsearch/pull/134091)
- Reserves memory for Lucene's `TopN` in  ES|QL [#134235](https://github.com/elastic/elasticsearch/pull/134235)
- Stops sharing weight between drivers in ES|QL [#133446](https://github.com/elastic/elasticsearch/pull/133446)
- Adds ES|QL telemetry with `inlinestats` [#134309](https://github.com/elastic/elasticsearch/pull/134309)
- Fixes `CB` on reduction phase in aggregations [#133398](https://github.com/elastic/elasticsearch/pull/133398)
- Fixes exceptions in index pattern conflict checks [#134231](https://github.com/elastic/elasticsearch/pull/134231)
- Fixes `allow_duplicates` edge case bug in append processor [#134319](https://github.com/elastic/elasticsearch/pull/134319)
- Adds support for flexible access pattern to `NormalizeForStreamProcessor` [#134524](https://github.com/elastic/elasticsearch/pull/134524)
- Returns 429 status when `RequestExecutorService` queue full [#134178](https://github.com/elastic/elasticsearch/pull/134178)
- Fixes model assignment error handling and assignment explanation generation [#133916](https://github.com/elastic/elasticsearch/pull/133916)
- Implements latency improvements for EIS integration [#133861](https://github.com/elastic/elasticsearch/pull/133861)


## September 8, 2025


### Features and enhancements

- Makes maintenance windows globally available [#233870](https://github.com/elastic/kibana/pull/233870)
- Updates `@elastic/charts` to 71.0.0 and enables new metric chart in Lens [#229815](https://github.com/elastic/kibana/pull/229815)
- Adds toggle that grants permission for agents to write to `logs` datastream [#233374](https://github.com/elastic/kibana/pull/233374).
- Adds Knowledge Base integration support [#230107](https://github.com/elastic/kibana/pull/230107)
- Adds support for duration variable type to Fleet [#231027](https://github.com/elastic/kibana/pull/231027)
- Uses native function calling for self-managed LLMs [#232109](https://github.com/elastic/kibana/pull/232109)
- Unifies installation settings and improves status display for AI Assistant's Knowledge Base & product documentation [#232559](https://github.com/elastic/kibana/pull/232559)
- Links dashboards to SLO [#233265](https://github.com/elastic/kibana/pull/233265)
- Disables add-to-case functionality when all selected alerts are already attached [#231877](https://github.com/elastic/kibana/pull/231877)
- Disables save button on empty input [#233184](https://github.com/elastic/kibana/pull/233184)
- Adds **View in discover** button to alert details header [#233259](https://github.com/elastic/kibana/pull/233259)
- Adds `send_traces`, `send_metrics`, and `send_logs` agent configuration settings for EDOT Node.js [#233798](https://github.com/elastic/kibana/pull/233798)
- Updates missing index pattern table action [#233258](https://github.com/elastic/kibana/pull/233258)
- Shows trace context for logs [#232784](https://github.com/elastic/kibana/pull/232784)
- Adds IPv6 support to address fields in the Remote Clusters UI [#233415](https://github.com/elastic/kibana/pull/233415)
- Updates the Elasticsearch Serverless project creation in the UI to use the general purpose profile.
  The API continues to support alternative `optimized_for` options. Refer to [Elasticsearch Serverless billing dimensions > Managing Elasticsearch costs](/docs/deploy-manage/cloud-organization/billing/elasticsearch-billing-dimensions#elasticsearch-billing-managing-elasticsearch-costs).
  


### Fixes

- Fixes resize bug [#233755](https://github.com/elastic/kibana/pull/233755)
- Fixes the page height of the Observability AI Assistant page [#233924](https://github.com/elastic/kibana/pull/233924)
- Updates kibana MITRE data to `v17.1` [#231375](https://github.com/elastic/kibana/pull/231375)
- Fixes import of endpoint exceptions [#233142](https://github.com/elastic/kibana/pull/233142)
- Fixes a bug that affected display of mitre attack data [#233805](https://github.com/elastic/kibana/pull/233805).
- Prevents users who don't have crud privilege from deleting notes [#233948](https://github.com/elastic/kibana/pull/233948).
- Fixes rule editor flyout for Anomaly Explorer when no filter lists have been configured [#233085](https://github.com/elastic/kibana/pull/233085)
- Fixes `FormattedMessage` rendering escaped HTML instead of markup [#234079](https://github.com/elastic/kibana/pull/234079)


## September 1, 2025


### Features and enhancements

- Allows users to configure index settings when importing geospatial files in **File Upload** [#232308](https://github.com/elastic/kibana/pull/232308)
- Adds tooltip support for the ES|QL layer [#232147](https://github.com/elastic/kibana/pull/232147)
- Enables automatic content package installation when matching datasets are ingested using the `enableAutoInstallContentPackages` feature flag [#232668](https://github.com/elastic/kibana/pull/232668)
- Increases query history capacity to store more than 20 queries [#232955](https://github.com/elastic/kibana/pull/232955)
- Improves validation for functions in query inputs [#230139](https://github.com/elastic/kibana/pull/230139)
- Adds support for native function calling schema to the OpenAI connector when the API provider is set to "Other" [#232097](https://github.com/elastic/kibana/pull/232097)
- Retries inference calls when aborted due to transient errors [#232610](https://github.com/elastic/kibana/pull/232610)
- Adds the `raw_request` field to traces for better debugging [#232229](https://github.com/elastic/kibana/pull/232229)
- Adds dashboard references to SLO saved objects [#232583](https://github.com/elastic/kibana/pull/232583)
- Displays span links when APM indices are available [#232135](https://github.com/elastic/kibana/pull/232135)
- Adds a new `policy_response_failure` defend insight type [#231908](https://github.com/elastic/kibana/pull/231908)
- Enables conversation sharing in chat interfaces [#230614](https://github.com/elastic/kibana/pull/230614)
- Adds a new data view to the Privmon dashboard page [#233264](https://github.com/elastic/kibana/pull/233264)
- Improves the layout of custom URLs list in **Data Frame Analytics** [#232575](https://github.com/elastic/kibana/pull/232575)
- Adds icons for **AI21 Labs** and **Llama Stack** to the AI connector/inference endpoints creation UI [#232098](https://github.com/elastic/kibana/pull/232098)
- Ensures consistent Grok pattern generation across features [#230076](https://github.com/elastic/kibana/pull/230076)
- Removes upper limit for chunking settings [#133718](https://github.com/elastic/elasticsearch/pull/133718)
- Supports filters on `inlinestats` in ES|QL [#132934](https://github.com/elastic/elasticsearch/pull/132934)
- Adds `MV_CONTAINS` ES|QL function [#133099](https://github.com/elastic/elasticsearch/pull/133099)
- Adds `TBUCKET` ES|QL function [#131449](https://github.com/elastic/elasticsearch/pull/131449)
- Adds `url_encode` ES|QL function [#133494](https://github.com/elastic/elasticsearch/pull/133494)
- Updates `FIRST` and `LAST` to accept keyword and text in ES|QL [#133642](https://github.com/elastic/elasticsearch/pull/133642)
- Adds `mv_contains` ES|QL function [#133636](https://github.com/elastic/elasticsearch/pull/133636)
- Supports `geohash`, `geotile`, and `geohex` grid types in ES|QL [#129581](https://github.com/elastic/elasticsearch/pull/129581)
- Allows trailing empty string field names in paths of flattened fields [#133611](https://github.com/elastic/elasticsearch/pull/133611)


### Fixes

- Ensures that maintenance windows with scoped queries apply to all rule types [#232307](https://github.com/elastic/kibana/pull/232307)
- Fixes pagination issues in alerting tables [#233030](https://github.com/elastic/kibana/pull/233030)
- Removes unused `availableOptions` from ES|QL values in query saved objects [#231690](https://github.com/elastic/kibana/pull/231690)
- Removes unnecessary output warning messages in Serverless deployments [#232785](https://github.com/elastic/kibana/pull/232785)
- Requires the `agents:all` privilege to use **Manage auto-upgrade agent** UI actions [#232429](https://github.com/elastic/kibana/pull/232429)
- Fixes read permission failures on the lookup indexes route [#233282](https://github.com/elastic/kibana/pull/233282)
- Refactors anonymization logic to walk JSON objects instead of stringifying them [#232319](https://github.com/elastic/kibana/pull/232319)
- Disables the **Save** button until a file is detected [#233141](https://github.com/elastic/kibana/pull/233141)
- Adds a missing **Alert details actions** button to the UI [#233113](https://github.com/elastic/kibana/pull/233113)
- Prevents SessionView crashes by normalizing event process arguments [#232462](https://github.com/elastic/kibana/pull/232462)
- Adds maximum function call limits to prevent recursive tool invocations [#231719](https://github.com/elastic/kibana/pull/231719)
- Ensures validation logic so Elastic Managed LLMs behave as expected during testing [#231873](https://github.com/elastic/kibana/pull/231873)
- Fixes the **Restore status** tab display for system indices [#232839](https://github.com/elastic/kibana/pull/232839)
- Fixes responsiveness issues in the Stream management code editor area [#232630](https://github.com/elastic/kibana/pull/232630)
- Fixes an empty tooltip issue when creating tags [#232853](https://github.com/elastic/kibana/pull/232853)
- Ensures only a single request executor object is created [#133424](https://github.com/elastic/elasticsearch/pull/133424)
- Fixes an issue where the **Create tag** modal wouldn't close properly [#233012](https://github.com/elastic/kibana/pull/233012)
- Fixes service destination template file name [#133403](https://github.com/elastic/elasticsearch/pull/133403)
- Avoids stale enrich results after policy execution [#133752](https://github.com/elastic/elasticsearch/pull/133752)
- Fixes enrich caches outdated value after policy run [#133680](https://github.com/elastic/elasticsearch/pull/133680)
- Tracks memory in ES|QL `evaluators` [#133392](https://github.com/elastic/elasticsearch/pull/133392)
- Fixes bug in `topn` [#133601](https://github.com/elastic/elasticsearch/pull/133601)
- Fixes wrong marking of a field as `unmapped` when indices shared the same mapping [#133298](https://github.com/elastic/elasticsearch/pull/133298)
- Updates `DefBootstrap` to handle `Error` from `ClassValue` [#133604](https://github.com/elastic/elasticsearch/pull/133604)
- Fixes `GeneralScriptException` to return 400 HTTP status code [#133659](https://github.com/elastic/elasticsearch/pull/133659)
- Disallows creating `semantic_text` fields in indices created prior to 8.11.0 [#133080](https://github.com/elastic/elasticsearch/pull/133080)


## August 28, 2025


### Features and enhancements

- Elastic Cloud Serverless is now available in three new Microsoft Azure [regions](https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud/regions):
  - `northeurope` (North Europe), located in Ireland
- `australiaeast` (Australia East), located in Victoria, Australia
- ` westus2` (West US 2), located in Washington, United States


## August 25, 2025


### Features and enhancements

- Adds support for a new `url` variable type in Fleet packages, enabling improved input validation of URL values [#231062](https://github.com/elastic/kibana/pull/231062)
- Adds the `kibana.alert.grouping` field to the **Synthetics monitor status** rule in Elastic Observability Serverless  [#230513](https://github.com/elastic/kibana/pull/230513)
- Enables polling and sampling for EDOT central configuration in Elastic Observability Serverless [#231835](https://github.com/elastic/kibana/pull/231835)
- Adds a check to confirm that uploaded files are indexed and searchable in Machine learning [#231614](https://github.com/elastic/kibana/pull/231614)
- Updates sections and improves field handling in Machine learning [#231037](https://github.com/elastic/kibana/pull/231037)
- Improves the layout of the custom URLs list in Machine learning [#231751](https://github.com/elastic/kibana/pull/231751)
- Returns 429 status code instead of 500 for timeout handlers [#133111](https://github.com/elastic/elasticsearch/pull/133111)
- Allows configuring SAML private attributes [#133154](https://github.com/elastic/elasticsearch/pull/133154)
- Adds new rescorer based on script [#74274](https://github.com/elastic/elasticsearch/pull/74274)
- Adds the `v_hamming` function for calculating the Hamming distance between two dense vectors [#132959](https://github.com/elastic/elasticsearch/pull/132959)
- Adds top level normalizer for linear retriever [#129693](https://github.com/elastic/elasticsearch/pull/129693)
- Adds ordinal range encode for TSID (Time Series Identifier) [#133018](https://github.com/elastic/elasticsearch/pull/133018)
- Limits the depth of a filter [#133113](https://github.com/elastic/elasticsearch/pull/133113)
- Stops running ES|QL planning and scheduling on transport threads [#133313](https://github.com/elastic/elasticsearch/pull/133313)
- Adds query heads priority to `SliceQueue` [#133245](https://github.com/elastic/elasticsearch/pull/133245)
- Upgrades to tika 3.2.2 [#133410](https://github.com/elastic/elasticsearch/pull/133410)
- Adds index mode to resolve index response [#132858](https://github.com/elastic/elasticsearch/pull/132858)


### Fixes

- Fixes a rendering issue that affected progress elements in Canvas [#232432](https://github.com/elastic/kibana/pull/232432)
- Fixes the enforcement of deployment mode restrictions when creating package policies in Fleet [#231679](https://github.com/elastic/kibana/pull/231679)
- Ensures transform index templates include `index.mapping.ignore_malformed: true` to prevent failures due to invalid values in source indices in Fleet [#232439](https://github.com/elastic/kibana/pull/232439)
- Fixes visibility issues with the DocViewer flyout in **Saved Search** embeddables in Discover [#229108](https://github.com/elastic/kibana/pull/229108)
- Restores legacy monitor filters in Elastic Observability Serverless [#231562](https://github.com/elastic/kibana/pull/231562)
- Handles multi-line values more reliably in Elastic Observability Serverless [#230929](https://github.com/elastic/kibana/pull/230929)
- Fixes broken views on AI Assistant settings pages for non-Enterprise license holders in Elastic Observability Serverless [#231989](https://github.com/elastic/kibana/pull/231989)
- Enables the recovery strategy toggle for monitor status rules in Elastic Observability Serverless [#231091](https://github.com/elastic/kibana/pull/231091)
- Fixes AI Assistant anonymization rules to avoid nested or overlapping masks when processing text in Elastic Observability Serverless [#231981](https://github.com/elastic/kibana/pull/231981)
- Fixes an issue that prevented the contextual flyout from showing full details in vulnerability findings in Elastic Security Serverless [#231778](https://github.com/elastic/kibana/pull/231778)
- Includes various bug fixes and improvements to the Manifest Manager in Elastic Security Serverless [#231039](https://github.com/elastic/kibana/pull/231039)
- Fixes an issue where the `unusedUrlsCLeanupTask` run interval did not update correctly when changed [#231883](https://github.com/elastic/kibana/pull/231883)
- Updates the prompt text for the `mv_slice` feature in Machine learning [#231870](https://github.com/elastic/kibana/pull/231870)
- Fixes a broken link in the **Build** breadcrumb that incorrectly pointed to the search indices page in Elasticsearch Serverless [#232504](https://github.com/elastic/kibana/pull/232504)
- Fixes inconsistencies in case activity statistics [#231948](https://github.com/elastic/kibana/pull/231948)
- Adds support for a `reporting_user` role with a reserved set of privileges [#231533](https://github.com/elastic/kibana/pull/231533)
- Disables child span for streaming tasks [#132945](https://github.com/elastic/elasticsearch/pull/132945)
- Changes `GeoIpCache` and `EnrichCache` to `LongAdder` [#132922](https://github.com/elastic/elasticsearch/pull/132922)
- Returns 400 on invalid processors in simulate API [#130325](https://github.com/elastic/elasticsearch/pull/130325)
- Forces rollover on write to true when data stream indices list is empty [#133347](https://github.com/elastic/elasticsearch/pull/133347)
- Marks `LOOKUP JOIN` as `ExecutesOn.Any` by default in ES|QL [#133064](https://github.com/elastic/elasticsearch/pull/133064)
- Fixes update expiration for async query in ES|QL [#133021](https://github.com/elastic/elasticsearch/pull/133021)
- Fixes `AsyncOperator` status values and adds emitted rows [#132738](https://github.com/elastic/elasticsearch/pull/132738)
- Fixes sequences with conditions involving keys and non-keys [#133134](https://github.com/elastic/elasticsearch/pull/133134)
- Fixes a bug where search failed when the bottom doc could not be formatted [#133188](https://github.com/elastic/elasticsearch/pull/133188)


## August 18, 2025


### Features and enhancements

- Removes the category selection step when adding filters to maintenance windows so you can add filters to maintenance windows based on alert fields from all solutions [#227888](https://github.com/elastic/kibana/pull/227888)
- Adds the ability to see all available log events in the shared logs overview even when ML features are not available [#225785](https://github.com/elastic/kibana/pull/225785)
- Improves Gemini prompts [#223476](https://github.com/elastic/kibana/pull/223476)
- Improves the AI Assistant Settings page by adding solution-specific logos [#224906](https://github.com/elastic/kibana/pull/224906)
- Enables the `trustedAppsAdvancedMode` feature flag by default [#230111](https://github.com/elastic/kibana/pull/230111)
- Updates the PrivMon UX [#231921](https://github.com/elastic/kibana/pull/231921)
- Improves error messages when your Kibana session fails to refresh a token [#231118](https://github.com/elastic/kibana/pull/231118)
- Adds inline markdown visualization [#229191](https://github.com/elastic/kibana/pull/229191)
- Adds an `AI` section to the `Stack Management` menu [#227289](https://github.com/elastic/kibana/pull/227289)
- Sets the default retention period for Logs anomaly detection to 120 days [#231080](https://github.com/elastic/kibana/pull/231080)
- Adds a `merge_type` parameter to the ingest simulate API [#132210](https://github.com/elastic/elasticsearch/pull/132210)
- Only allows enabling streams if no conflicting indices exist [#132064](https://github.com/elastic/elasticsearch/pull/132064)
- Adds simulate ingest effective mapping [#132833](https://github.com/elastic/elasticsearch/pull/132833)
- Adds `created_date` and `modified_date` in index templates [#132083](https://github.com/elastic/elasticsearch/pull/132083)
- Improves CPU utilization with dynamic slice size in doc partitioning [#132774](https://github.com/elastic/elasticsearch/pull/132774)
- Considers `min`/`max` from predicates when transforming `date_trunc`/bucket to `round_to` option 2 in ES|QL [#132143](https://github.com/elastic/elasticsearch/pull/132143)
- Adds some optimizations for constant blocks [#132456](https://github.com/elastic/elasticsearch/pull/132456)
- Adds `DAY_NAME` ES|QL function [#132535](https://github.com/elastic/elasticsearch/pull/132535)
- Adds support for `LOOKUP JOIN` on multiple fields in ES|QL [#131559](https://github.com/elastic/elasticsearch/pull/131559)
- Speeds up loading keyword fields with index sorts [#132950](https://github.com/elastic/elasticsearch/pull/132950)
- Adds `MONTH_NAME` ES|QL function [#132968](https://github.com/elastic/elasticsearch/pull/132968)
- Restricts indexing to child streams when streams mode is enabled [#132011](https://github.com/elastic/elasticsearch/pull/)
- Adds support for retrieving semantic_text's indexed chunks via fields API [#132410](https://github.com/elastic/elasticsearch/pull/132410)
- Implements `v_magnitude` function [#132765](https://github.com/elastic/elasticsearch/pull/132765)
- Restricts indexing to child streams when streams mode is enabled [#132011](https://github.com/elastic/elasticsearch/pull/132011)
- Adds support for passing the `dimensions` field in the Google Vertex AI request [#132689](https://github.com/elastic/elasticsearch/pull/132689)


### Fixes

- Fixes a bug that stopped reports from spaces with a dash in them from appearing in the reporting list [#230876](https://github.com/elastic/kibana/pull/230876)
- Fixes Timeslider focus ring visibility in Firefox [#231351](https://github.com/elastic/kibana/pull/231351)
- Fixes error handling in the Links panel's **Save to library** modal [#231168](https://github.com/elastic/kibana/pull/231168)
- Fixes keyboard interaction on range slider control [#230893](https://github.com/elastic/kibana/pull/230893)
- Fixes older color mapping configuration in Lens [#231563](https://github.com/elastic/kibana/pull/231563)
- Fixes lost references when returning to unsaved dashboards with reference panels [#231517](https://github.com/elastic/kibana/pull/231517)
- Fixes rendering of aggregate metric fields in ES|QL mode [#231481](https://github.com/elastic/kibana/pull/231481)
- Disables sorting for json-like fields in ES|QL mode [#231289](https://github.com/elastic/kibana/pull/231289)
- Fixes a bug affecting the Inventory date picker's state [#231141](https://github.com/elastic/kibana/pull/231141)
- Fixes title generation for the Observability AI Assistant in conversations with self-managed LLMs [#231198](https://github.com/elastic/kibana/pull/231198)
- Fixes an endless loop that could occur during ES|QL `LOOKUP JOIN`s [#231217](https://github.com/elastic/kibana/pull/231217)
- Adjusts the Kubernetes OTel test to work in serverless nightly workflow [#231462](https://github.com/elastic/kibana/pull/231462)
- Updates the `ContentManagement` plugin to enable linked dashboards in more places [#229685](https://github.com/elastic/kibana/pull/229685)
- Provides the `aria-labelledby` attribute to the **Add cases** selector modal [#231887](https://github.com/elastic/kibana/pull/231887)
- Fixes incorrect threat enrichment for partially matched `AND` conditions in IM rules [#230773](https://github.com/elastic/kibana/pull/230773)
- Fixes Benchmark page accessibility issues [#229521](https://github.com/elastic/kibana/pull/229521)
- Fixes an issue that prevented the creation of Knowledge Base `Index` entries in deployments with a large number of indices and mappings [#231376](https://github.com/elastic/kibana/pull/231376)
- Fixes an index sync bug that prevented deletion of stale users [#229789](https://github.com/elastic/kibana/pull/229789)
- Fixes custom field grouping options in the Alerts table [#230121](https://github.com/elastic/kibana/pull/230121)
- Fixes a bug that made the ES|QL form read-only in the Rule upgrade flyout [#231699](https://github.com/elastic/kibana/pull/231699)
- Removes the default port the from interactive setup cluster address form, unless specified [#230582](https://github.com/elastic/kibana/pull/230582)
- Fixes positioning of the **Add rule** popover on the Role Mappings page [#231551](https://github.com/elastic/kibana/pull/231551)
- Handles special regex cases for version fields [#132511](https://github.com/elastic/elasticsearch/pull/132511)
- Tracks top-level kNN searches in query stats [#132548](https://github.com/elastic/elasticsearch/pull/132548)
- Tests for FORK's evaluation of field names used in `field_caps` resolve calls in ES|QL [#131723](https://github.com/elastic/elasticsearch/pull/131723)
- Strings outside BMP have 2 chars per code points [#132593](https://github.com/elastic/elasticsearch/pull/132593)
- Adds small fixes for `COPY_SIGN` [#132459](https://github.com/elastic/elasticsearch/pull/132459)
- Fixes async operator warnings not always sent when blocking [#132744](https://github.com/elastic/elasticsearch/pull/132744)
- Improves error message for sequences with only one clause plus UNTIL [#132638](https://github.com/elastic/elasticsearch/pull/132638)
- Updates EIS sparse and dense embedding max batch size to 16 [#132646](https://github.com/elastic/elasticsearch/pull/132646)
- Improves `EIS` auth call logs and fixes revocation bug [#132546](https://github.com/elastic/elasticsearch/pull/132546)
- Retries when failing to start indexer [#132048](https://github.com/elastic/elasticsearch/pull/132048)
- Preserves lost thread context in node inference action [#132973](https://github.com/elastic/elasticsearch/pull/132973)


## August 11, 2025


### Features and enhancements

- Adds **DOES NOT MATCH** capability to the IM rule type in Elastic Security Serverless [#227084](https://github.com/elastic/kibana/pull/227084)
- Adds Automatic Import documentation links to log descriptions and error messages [#229375](https://github.com/elastic/kibana/pull/229375)
- Improves dashboard usability at 400% zoom [#228978](https://github.com/elastic/kibana/pull/228978)
- Adds an **unsaved changes** modal in Discover [#225252](https://github.com/elastic/kibana/pull/225252)
- Adds a recovery mode switch for status alerts in Elastic Observability Serverless [#229962](https://github.com/elastic/kibana/pull/229962)
- Adds an error parameter to the agent config API in Elastic Observability Serverless [#230298](https://github.com/elastic/kibana/pull/230298)
- Adds an inference timeout to anonymization settings in Elastic Observability Serverless [#230640](https://github.com/elastic/kibana/pull/230640)
- Fetches referenced panels when loading dashboards in Elastic Observability Serverless [#228811](https://github.com/elastic/kibana/pull/228811)
- Installs product docs with KB installation in Elastic Observability Serverless [#228695](https://github.com/elastic/kibana/pull/228695)
- Links from alert details to related dashboards now include a time range filter in Elastic Observability Serverless [#230601](https://github.com/elastic/kibana/pull/230601)
- Updates the default Gemini model for the Gemini Connector in Playground from Gemini 1.5 Pro to Gemini 2.5 Pro in Elasticsearch Serverless [#230457](https://github.com/elastic/kibana/pull/230457)
- Support nested fields for term vectors API when using artificial documents [#92568](https://github.com/elastic/elasticsearch/pull/92568)


### Fixes

- Removes unnecessary promises in dashboards [#230313](https://github.com/elastic/kibana/pull/230313)
- Fixes date math plus sign encoding in dashboards [#230469](https://github.com/elastic/kibana/pull/230469)
- Logs a warning if filter and query state are malformed in dashboards [#230088](https://github.com/elastic/kibana/pull/230088)
- Fixes duplicate panel action hangs when a dashboard has collapsed sections closed on page load [#230842](https://github.com/elastic/kibana/pull/230842)
- Fixes a screen reader–only header for accessibility in dashboards [#230470](https://github.com/elastic/kibana/pull/230470)
- Fixes missing validation errors in the package policy editor in Fleet [#229932](https://github.com/elastic/kibana/pull/229932)
- Fixes agentless integrations where `organization`, `division`, or `team` data fields were being overwritten by package metadata in Fleet [#230479](https://github.com/elastic/kibana/pull/230479)
- Fixes the output SSL config order in Fleet [#230758](https://github.com/elastic/kibana/pull/230758)
- Fixes glitches in the **data view creation** flyout in Discover when accessed from another page [#228749](https://github.com/elastic/kibana/pull/228749)
- Fixes a setup bug in the Elastic Observability Serverless lock manager [#230519](https://github.com/elastic/kibana/pull/230519)
- Adds a loading state in Elastic Observability Serverless for installing or uninstalling product docs [#229579](https://github.com/elastic/kibana/pull/229579)
- Includes a timestamp range filter to exclude the frozen tier in Elastic Observability Serverless [#230375](https://github.com/elastic/kibana/pull/230375)
- Adjusts e2e onboarding tests to work in Elastic Observability Serverless [#229969](https://github.com/elastic/kibana/pull/229969)
- Moves the `scheduleNow` call to the privmon engine init instead of the monitoring source engine in Elastic Security Serverless [#230263](https://github.com/elastic/kibana/pull/230263)
- Creates the Privileged user monitoring default index source only if it doesn't already exist in Elastic Security Serverless [#229693](https://github.com/elastic/kibana/pull/229693)
- Fixes Privileged user monitoring index sync in non-default spaces in Elastic Security Serverless [#230420](https://github.com/elastic/kibana/pull/230420)
- Adds a validation error if the actions throttle is shorter than the rule interval in Elastic Security Serverless [#229976](https://github.com/elastic/kibana/pull/229976)
- Excludes deprecated features from spaces solution visibility [#230385](https://github.com/elastic/kibana/pull/230385)
- Ensures form fields persist when validation fails in Machine Learning [#230321](https://github.com/elastic/kibana/pull/230321)
- Improves accessibility of the Streams table [#225659](https://github.com/elastic/kibana/pull/225659)
- Fixes a bug that prevented saving linked TSVB visualizations when changing the data view [#228685](https://github.com/elastic/kibana/pull/228685)
- Fixes a null property error in the Elasticsearch Serverless Playground [#230729](https://github.com/elastic/kibana/pull/230729)
- Adjusts date docvalue formatting to return 4xx instead of 5xx [#132414](https://github.com/elastic/elasticsearch/pull/132414)
- Corrects exception for missing nested path [#132408](https://github.com/elastic/elasticsearch/pull/132408)
- Adds validation to bucket script pipeline aggregation [#132320](https://github.com/elastic/elasticsearch/pull/132320)
- Fixes index lookup when `field-caps` returns empty mapping [#132138](https://github.com/elastic/elasticsearch/pull/132138)
- Handles internally created `IN` in a different way for EQL [#132167](https://github.com/elastic/elasticsearch/pull/132167)
- Disables inference API partial search results [#132362](https://github.com/elastic/elasticsearch/pull/132362)


## August 4, 2025


### Features and enhancements

- Updates AGENTLESS_DISABLED_INPUTS list in Fleet [#229117](https://github.com/elastic/kibana/pull/229117)
- Enables filter and saved query options in the optional Elastic Observability Serverless query filter [#229453](https://github.com/elastic/kibana/pull/229453)
- Introduces dashboard migration endpoints in Elastic Security Serverless [#229112](https://github.com/elastic/kibana/pull/229112)
- Adds the ability to save Playgrounds within a space in Elasticsearch Serverless [#229511](https://github.com/elastic/kibana/pull/229511)
- Enhances grok semantics extraction with Onigurama regex patterns in Discover [#229409](https://github.com/elastic/kibana/pull/229409)
- Adds **Prettify** button to the editor and removes the ability to unwrap in Discover [#228159](https://github.com/elastic/kibana/pull/228159)
- Adds support for expressions in Discover STATS [#229513](https://github.com/elastic/kibana/pull/229513)
- Allows pasting screenshots into Markdown comment fields for cases in Elastic Observability Serverless [#226077](https://github.com/elastic/kibana/pull/226077)
- Adds `detection_rule_upgrade_status` to snapshot telemetry in Elastic Security Serverless [#223086](https://github.com/elastic/kibana/pull/223086)
- Adds EASE value report in Elastic Security Serverless [#228877](https://github.com/elastic/kibana/pull/228877)
- Adds Machine Learning ability to filter AI Connector providers by solution type [#228116](https://github.com/elastic/kibana/pull/228116)
- Improves Console reliability by removing odd retry logic and adding Elasticsearch host selector [#229574](https://github.com/elastic/kibana/pull/229574)
- Improves rate limiter UX [#227678](https://github.com/elastic/kibana/pull/227678)
- Adds table list view to the space selector screen [#229046](https://github.com/elastic/kibana/pull/229046)
- Adds `kibana.alert.grouping` field to infra alerts [#229054](https://github.com/elastic/kibana/pull/229054)
- Skips search shards with `INDEX_REFRESH_BLOCK`
- Adds the `created_date` and `modified_date` system-managed properties to pipelines #130847]([https://github.com/elastic/elasticsearch/pull/130847](https://github.com/elastic/elasticsearch/pull/130847))
- Adds the `created_date` and `modified_date` system-managed properties to component templates [#131536](https://github.com/elastic/elasticsearch/pull/131536)
- Adds entity store and asset criticality index privileges to built-in roles [#129662](https://github.com/elastic/elasticsearch/pull/129662)
- Organization IdP routes are now public in the OpenAPI specifications.
- Supports kNN filter on nested metadata [#113949](https://github.com/elastic/elasticsearch/pull/113949)
- Replaces "representable" type error messages [#131775](https://github.com/elastic/elasticsearch/pull/131775)
- Adds fast path for single value in `VALUES` aggregator [#130510](https://github.com/elastic/elasticsearch/pull/130510)
- Replaces `RoundTo` linear search evaluator with manual evaluators in ES|QL [#131733](https://github.com/elastic/elasticsearch/pull/131733)
- Fails `profile` on text response formats [#128627](https://github.com/elastic/elasticsearch/pull/128627)
- Adds pruning in ES|QL for columns added by `InlineJoin` [#131204](https://github.com/elastic/elasticsearch/pull/131204)
- Adds `{created,modified}_date` in component templates [#131536](https://github.com/elastic/elasticsearch/pull/131536)
- Adds `created_date` and `modified_date` in pipelines [#130847](https://github.com/elastic/elasticsearch/pull/130847)
- Handles structured log messages [#131027](https://github.com/elastic/elasticsearch/pull/131027)
- Enable failure store for new `logs-*-*` data streams [#131261](https://github.com/elastic/elasticsearch/pull/131261)
- Adds support to configure query timeout for inference [#131551](https://github.com/elastic/elasticsearch/pull/131551)
- Adds AI21 support to Inference Plugin [#131238](https://github.com/elastic/elasticsearch/pull/131238)


### Fixes

- Fixes loading of saved queries in the Alerting rule definition [#229964](https://github.com/elastic/kibana/pull/229964)
- Fixes dashboard panel rendering when the defer-below-the-fold setting is on and panels are focused/unfocused [#229662](https://github.com/elastic/kibana/pull/229662)
- Fixes ES|QL loading button state for long-running queries in **Lens** [#226565](https://github.com/elastic/kibana/pull/226565)
- Fixes extra padding below Advanced Options when inline editing in **Lens** [#229967](https://github.com/elastic/kibana/pull/229967)
- Improves Discover document viewer error handling where errors in one tab no longer break other tabs [#229220](https://github.com/elastic/kibana/pull/229220)
- Improves performance of breakdown field search in Discover [#229335](https://github.com/elastic/kibana/pull/229335)
- Enables **Save query** button after making changes in the Discover save query menu [#229053](https://github.com/elastic/kibana/pull/229053)
- Displays function license availability in Discover inline docs [#229961](https://github.com/elastic/kibana/pull/229961)
- Fixes incorrect filtering logic when removing a comment field in Discover [#230116](https://github.com/elastic/kibana/pull/230116)
- Modifies title generation to be scope-aware in Elastic Observability Serverless [#227434](https://github.com/elastic/kibana/pull/227434)
- Prevents destructive actions using the Elasticsearch tool in Elastic Observability Serverless [#229497](https://github.com/elastic/kibana/pull/229497)
- Replaces `EuiErrorBoundary` with `KibanaErrorBoundary` in Elastic Observability Serverless [#229710](https://github.com/elastic/kibana/pull/229710)
- Fixes keyboard accessibility for the Waterfall flyout in Elastic Observability Serverless [#229926](https://github.com/elastic/kibana/pull/229926)
- Allows knowledge base UI to work offline in Elastic Observability Serverless [#229874](https://github.com/elastic/kibana/pull/229874)
- Fixes diff display bug when importing rule customizations in Elastic Security Serverless [#228475](https://github.com/elastic/kibana/pull/228475)
- Adds missing announcements for filter in/out actions on bar charts in Elastic Security Serverless [#227388](https://github.com/elastic/kibana/pull/227388)
- Fixes toast counter badge stacking order [#229300](https://github.com/elastic/kibana/pull/229300)
- Fixes console error when adding Region map visualization for Machine Learning to a dashboard [#228669](https://github.com/elastic/kibana/pull/228669)
- Fixes product docs install logic when the target version is higher than the current version for Machine Learning [#229704](https://github.com/elastic/kibana/pull/229704)
- Adds support for the `name` attribute in create and update actions for saved objects [#228464](https://github.com/elastic/kibana/pull/228464)
- Fixes missing data view [#229467](https://github.com/elastic/kibana/pull/229467)
- Avoids internal server error on suggester ngram bad request [#132321](https://github.com/elastic/elasticsearch/pull/132321)
- Fixes default missing index sort value of `data_nanos` pre 7.14 [#132162](https://github.com/elastic/elasticsearch/pull/132162)
- Implements support for weighted RRF [#130658](https://github.com/elastic/elasticsearch/pull/130658)
- Adds sparse vector index options settings to semantic text fields [#131058](https://github.com/elastic/elasticsearch/pull/131058)
- Fixes decoding of non-ascii field names in ignored source [#132018](https://github.com/elastic/elasticsearch/pull/132018)
- Fixes `Driver` creating status with a live list of operators [#132260](https://github.com/elastic/elasticsearch/pull/132260)
- Changes equals and `hashcode` for `ConstantNullBlock` in ES|QL  [#131817](https://github.com/elastic/elasticsearch/pull/131817)
- Fixes `NPE` on empty `to_lower`/`to_upper` call [#131917](https://github.com/elastic/elasticsearch/pull/131917)
- Fixes `aggregate_metric_double` sorting and `mv_expand` issues in ES|QL [#131658](https://github.com/elastic/elasticsearch/pull/131658)
- Restricts remote `ENRICH` after `FORK` [#131945](https://github.com/elastic/elasticsearch/pull/131945)
- Fixes combine result for `ingest_took` [#132088](https://github.com/elastic/elasticsearch/pull/132088)
- Prevents auto-sharding for data streams in `LOOKUP` index mode [#131429](https://github.com/elastic/elasticsearch/pull/131429)
- Simulate ingest API uses existing index mapping when `mapping_addition` is given [#132101](https://github.com/elastic/elasticsearch/pull/132101)
- Prevents the trained model deployment memory estimation from double-counting allocations [#131990](https://github.com/elastic/elasticsearch/pull/131990)


## July 28, 2025


### Features and enhancements

- Enhances the integrations overview by rendering an accordion for sample events in Data ingestion and Fleet [#228799](https://github.com/elastic/kibana/pull/228799)
- Displays related dashboard tags directly in the Elastic Observability Serverless UI [#228902](https://github.com/elastic/kibana/pull/228902)
- Adds the `kibana.alert.grouping` field to ES|QL rule definitions [#228580](https://github.com/elastic/kibana/pull/228580)
- Adds support for ingress IP filters. IP filter policies allow you to restrict traffic coming into your project to specific IP addresses or CIDR blocks.
- Speeds up `OptimizedScalarQuantizer` [#131599](https://github.com/elastic/elasticsearch/pull/131599)
- Integrates `LIKE`/`RLIKE` LIST with `ReplaceStringCasingWithInsensitiveRegexMatch` rule [#131531](https://github.com/elastic/elasticsearch/pull/131531)
- Adds optimized path for intermediate values aggregator [#131390](https://github.com/elastic/elasticsearch/pull/131390)
- Accepts unsigned longs on `MAX` and `MIN` aggregations [#131694](https://github.com/elastic/elasticsearch/pull/131694)
- Removes deprecated function `isNotNullAndFoldable` [#130944](https://github.com/elastic/elasticsearch/pull/130944)


### Fixes

- Fixes incorrect handling of the `pollEnabled` configuration in reporting [#228707](https://github.com/elastic/kibana/pull/228707)
- Fixes an issue in Firefox where scrolling was disabled in the **Lens** editor flyout [#228625](https://github.com/elastic/kibana/pull/228625)
- Fixes an issue in Firefox that prevented scrolling in the **ES|QL** inline editor in Discover [#228849](https://github.com/elastic/kibana/pull/228849)
- Fixes an issue in *Lens* reports where PNG and PDF exports were clipped or misaligned [#228603](https://github.com/elastic/kibana/pull/228603)
- Corrects how the **Body cell lines** display option is handled when the default value is `-1` [#228697](https://github.com/elastic/kibana/pull/228697)
- Updates field stats logic to better select sub-fields when needed [#228969](https://github.com/elastic/kibana/pull/228969)
- Prevents search highlighting from affecting field action filters in the logs overview [#227652](https://github.com/elastic/kibana/pull/227652)
- Fixes an issue where dependency panels could infinitely load when no data was available [#228094](https://github.com/elastic/kibana/pull/228094)
- Fixes column sorting in the service error table [#229199](https://github.com/elastic/kibana/pull/229199)
- Ensures artifact links are visible even without endpoint list privileges [#226561](https://github.com/elastic/kibana/pull/226561)
- Fixes the incorrect background color in **Build Block Alerts** rows [#228226](https://github.com/elastic/kibana/pull/228226)
- Simplifies the **Misconfigurations** index pattern logic [#227995](https://github.com/elastic/kibana/pull/227995)
- Fixes an issue where **Security Assistant** settings landed on the wrong page when using a basic license [#229163](https://github.com/elastic/kibana/pull/229163)
- Removes the use of `removeIfExists` in the sync task scheduler [#228783](https://github.com/elastic/kibana/pull/228783)
- Fixes the width of the patterns field selector menu [#228791](https://github.com/elastic/kibana/pull/228791)
- Ensures the Gemini Vertex AI documentation link is available in the AI Connector [#228348](https://github.com/elastic/kibana/pull/228348)
- Fixes a skipped autocomplete test in the console [#229274](https://github.com/elastic/kibana/pull/229274)
- Ignores missing filters in rule parameters instead of causing errors [#229422](https://github.com/elastic/kibana/pull/229422)
- Correctly handles `download_database_on_pipeline_creation` within a pipeline processor within a default or final pipeline [#131236](https://github.com/elastic/elasticsearch/pull/131236)
- Adds `Sample operator` `NamedWritable` to plugin [#131541](https://github.com/elastic/elasticsearch/pull/131541)
- Supports semantic reranking using contextual snippets instead of entire field text [#129369](https://github.com/elastic/elasticsearch/pull/129369)
- Fixes memory usage estimation for ELSER models [#131630](https://github.com/elastic/elasticsearch/pull/131630)


## July 22, 2025


### Features and enhancements

- Improves perceived performance for dashboard flyouts [#226052](https://github.com/elastic/kibana/pull/226052)
- Renders ES|QL controls using **OptionsList** UI components [#227334](https://github.com/elastic/kibana/pull/227334)
- Adds `MIGRATE` to signed actions [#228566](https://github.com/elastic/kibana/pull/228566)
- Excludes metrics data streams [#227842](https://github.com/elastic/kibana/pull/227842)
- Adds a package rollback API [#226754](https://github.com/elastic/kibana/pull/226754)
- Displays related error count and adds a failure badge [#227413](https://github.com/elastic/kibana/pull/227413)
- Adds form row labels to the ES|QL Editor [#228103](https://github.com/elastic/kibana/pull/228103)
- Registers a UI setting for anonymization [#224607](https://github.com/elastic/kibana/pull/224607)
- Adds support for span types [#227208](https://github.com/elastic/kibana/pull/227208)
- Introduces a public "test now" endpoint [#227760](https://github.com/elastic/kibana/pull/227760)
- Enables custom roles by default [#227878](https://github.com/elastic/kibana/pull/227878)
- Allows submitting case comments by pressing **⌘+Enter** (or **Ctrl+Enter**) [#228473](https://github.com/elastic/kibana/pull/228473)
- Increases the number of supported **Group by** fields in threshold rules from 3 to 5 [#227465](https://github.com/elastic/kibana/pull/227465)
- Adds the **Search AI Lake** view to AutoOps for Elastic Cloud Serverless to provide storage usage insights
- Enhances `semantic_text` inference error messages [#131519](https://github.com/elastic/elasticsearch/pull/131519)
- Fixes a semantic highlighting bug on flat quantized fields [#131525](https://github.com/elastic/elasticsearch/pull/131525)
- Enables force option to delete inference endpoints when there are invalid models or when stopping model deployment fails [#129090](https://github.com/elastic/elasticsearch/pull/129090)
- Adds ES|QL categorize options [#131104](https://github.com/elastic/elasticsearch/pull/131104)
- Adds Azure AI Rerank support [#129848](https://github.com/elastic/elasticsearch/pull/129848)
- Blocks trained model updates from inference [#130940](https://github.com/elastic/elasticsearch/pull/130940)
- Tracks duration and errors when inference endpoints deploy trained models [#131442](https://github.com/elastic/elasticsearch/pull/131442)
- Adds Llama support to Inference Plugin [#130092](https://github.com/elastic/elasticsearch/pull/130092)
- Enables failure store for newly created APM datastreams [#131296](https://github.com/elastic/elasticsearch/pull/131296)
- Enables failure store for newly created OTel data streams [#131395](https://github.com/elastic/elasticsearch/pull/131395)
- Speeds up reading multivalued keywords [#131061](https://github.com/elastic/elasticsearch/pull/131061)
- Substitutes `date_trunc` with `round_to` when the pre-calculated rounding points are available [#128639](https://github.com/elastic/elasticsearch/pull/128639)
- Adds support for `RLIKE` LIST with pushdown [#129929](https://github.com/elastic/elasticsearch/pull/129929)
- Adds checks that optimizers do not modify the layout [#130855](https://github.com/elastic/elasticsearch/pull/130855)


### Fixes

- Fixes an issue in **Lens** where **Partition** charts (for example, Pie) blocked selection of legacy palettes [#228051](https://github.com/elastic/kibana/pull/228051)
- Correctly forwards the secondary prefix when the state value is an empty string (`None` option) in **Lens** [#228183](https://github.com/elastic/kibana/pull/228183)
- Fixes loading state and improves error handling in the dashboard save modal [#227861](https://github.com/elastic/kibana/pull/227861)
- Hides hidden indices from autocomplete when using a lookup index [#227819](https://github.com/elastic/kibana/pull/227819)
- Fixes incorrect validation between aggregation expressions [#227989](https://github.com/elastic/kibana/pull/227989)
- Fixes product docs installation status [#226919](https://github.com/elastic/kibana/pull/226919).
- Resolves issues in the `metric_item` component [#227969](https://github.com/elastic/kibana/pull/227969)
- Fixes a bug with the embeddings model dropdown when upgrading with a legacy endpoint [#226878](https://github.com/elastic/kibana/pull/226878)
- Fixes filtering by "unmodified" rules in the update table [#227859](https://github.com/elastic/kibana/pull/227859)
- Fixes an issue where alert status showed as untracked for newly created schedule rules [#226575](https://github.com/elastic/kibana/pull/226575)
- Improves copy in the bulk update modal [#227803](https://github.com/elastic/kibana/pull/227803).
- Enables soft-deleting of rule gaps on rule deletion [#227231](https://github.com/elastic/kibana/pull/227231)
- Migrates the anonymization in-memory table to `EuiBasicTable` for improved selection control [#222825](https://github.com/elastic/kibana/pull/222825)
- Fixes styling issues in flyouts [#228078](https://github.com/elastic/kibana/pull/228078)
- Fixes sub-menu behavior in the solution nav when collapsed [#227705](https://github.com/elastic/kibana/pull/227705)
- Fixes semantic highlighting bug on flat quantized fields [#131525](https://github.com/elastic/elasticsearch/pull/131525)
- Fixes semantic query rewrite interception dropping boosts [#129282](https://github.com/elastic/elasticsearch/pull/129282)
- Prepares `Index Like` fix for backport to 9.1 and 8.19 [#130947](https://github.com/elastic/elasticsearch/pull/130947)
- Splits large pages on load sometimes in ES|QL [#131053](https://github.com/elastic/elasticsearch/pull/131053)
- Fixes `mv_expand` inconsistent column order [#129745](https://github.com/elastic/elasticsearch/pull/129745)
- Disallows remote `enrich` after lookup join [#131426](https://github.com/elastic/elasticsearch/pull/131426)
- Moves streams status actions to `cluster:monitor` group [#131015](https://github.com/elastic/elasticsearch/pull/131015)
- Includes `max_tokens` through the Service API for Anthropic [#131113](https://github.com/elastic/elasticsearch/pull/131113)
- Syncs inference with trained model stats [#130544](https://github.com/elastic/elasticsearch/pull/130544)


## July 15, 2025


### Features and enhancements

- Elastic Cloud Serverless is now available in two new Amazon Web Services [regions](https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud/regions): `eu-central-1` (Frankfurt) and `us-east-2` (Ohio).
- Adds the ability to add tags from the **Agent details** page [#225433](https://github.com/elastic/kibana/pull/225433)
- Adds a **Profiles inspector** to Discover [#222999](https://github.com/elastic/kibana/pull/222999)
- Displays a callout about new rules in Elastic Observability Serverless **Metrics**, **Logs**, and **Inventory** rule types [#224387](https://github.com/elastic/kibana/pull/224387)
- Adds a manual test for bulk import functionality in Elastic Observability Serverless [#225497](https://github.com/elastic/kibana/pull/225497)
- Groups vulnerabilities by resource and cloud account using IDs instead of names in Elastic Security Serverless [#225492](https://github.com/elastic/kibana/pull/225492)
- Updates the default Gemini model in Elastic Security Serverless [#225917](https://github.com/elastic/kibana/pull/225917)
- Streamlines the side navigation in Elasticsearch Serverless [#225709](https://github.com/elastic/kibana/pull/225709)
- Adds synthetic vectors support for rank_vectors [#130715](https://github.com/elastic/elasticsearch/pull/130715)
- Adds synthetic vectors support for sparse_vector [#130756](https://github.com/elastic/elasticsearch/pull/130756)
- Ensure vectors are always included in reindex actions [#130834](https://github.com/elastic/elasticsearch/pull/130834)
- Removes vectors from `_source` transparently [#130382](https://github.com/elastic/elasticsearch/pull/130382)
- Implements `INLINESTATS` with multiple `LogicalPlan` updates [#128917](https://github.com/elastic/elasticsearch/pull/128917)
- Adds `Dependency Checker` for `LogicalLocalPlanOptimizer` [#130409](https://github.com/elastic/elasticsearch/pull/130409)
- Implements remote `LOOKUP JOIN` [#129013](https://github.com/elastic/elasticsearch/pull/129013)


### Fixes

- Fixes an issue where reports timed out and failed with an invalid header error [#225919](https://github.com/elastic/kibana/pull/225919)
- Ensures "Values from a query" options refresh when reloading dashboards [#225101](https://github.com/elastic/kibana/pull/225101)
- Removes warnings related to kebab-case naming [#226114](https://github.com/elastic/kibana/pull/226114)
- Prevents custom titles from being overwritten in Lens embeddables after reload [#225664](https://github.com/elastic/kibana/pull/225664)
- Prevents adhoc data views from being recommended in **Controls** [#225705](https://github.com/elastic/kibana/pull/225705)
- Hides the **Select all** checkbox in single-select controls [#226311](https://github.com/elastic/kibana/pull/226311)
- Fixes a bug where edited queries were overwritten when a request completed [#224671](https://github.com/elastic/kibana/pull/224671)
- Keeps the selected document stable when resizing the flyout with keyboard controls [#225594](https://github.com/elastic/kibana/pull/225594)
- Ensures suggested dashboards only appear for custom threshold alerts in Elastic Observability Serverless [#224458](https://github.com/elastic/kibana/pull/224458)
- Fixes schema page rendering issues in Elastic Observability Serverless [#225481](https://github.com/elastic/kibana/pull/225481)
- Limits environment name length when creating a Machine Learning job in Elastic Observability Serverless [#225973](https://github.com/elastic/kibana/pull/225973)
- Fixes broken **Operation** page in Elastic Observability Serverless [#226036](https://github.com/elastic/kibana/pull/226036)
- Fixes visual issues in Elastic Observability Serverless chat when `prefers-reduce-motion` is enabled [#226552](https://github.com/elastic/kibana/pull/226552)
- Prevents collapse of *query tool* calls in Elastic Observability Serverless [#226078](https://github.com/elastic/kibana/pull/226078)
- Adds a title to the rule gap histogram on the **Rules** dashboard in Elastic Security Serverless [#225274](https://github.com/elastic/kibana/pull/225274)
- Moves alerts redirect higher in the Elastic Security Serverless component tree to improve routing [#225650](https://github.com/elastic/kibana/pull/225650)
- Opens entity links in a flyout instead of navigating away in Elastic Security Serverless [#225381](https://github.com/elastic/kibana/pull/225381)
- Stops showing ML rule installation and upgrade errors on Basic license for Elastic Security Serverless [#224676](https://github.com/elastic/kibana/pull/224676)
- Updates the **Related Interactions** input placeholder and validation message in Elastic Security Serverless [#225775](https://github.com/elastic/kibana/pull/225775)
- Falls back to default value when `lookbackInterval` is empty in Anomaly Detection rules [#225249](https://github.com/elastic/kibana/pull/225249)
- Fixes time range handling in embedded anomaly swim lanes [#225803](https://github.com/elastic/kibana/pull/225803)
- Adds discernible text to the **Refresh data preview** button [#225816](https://github.com/elastic/kibana/pull/225816)
- Improves error handling in **Search Playground** when context limit is exceeded using Elastic Managed LLMs [#225360](https://github.com/elastic/kibana/pull/225360)
- Fixes knn search error when dimensions are not set [#131081](https://github.com/elastic/elasticsearch/pull/131081)
- Fixes `GET _synonyms` API to include rulesets with empty rules [#131032](https://github.com/elastic/elasticsearch/pull/131032)
- Prevents field caps from using semantic queries as index filters [#131111](https://github.com/elastic/elasticsearch/pull/131111)
- Adds cancellation checks to `FilterByFilter` aggregator [#130452](https://github.com/elastic/elasticsearch/pull/130452)
- Fixes `BytesRef2BlockHash` [#130705](https://github.com/elastic/elasticsearch/pull/130705)
- Disallows brackets in unquoted index patterns [#130427](https://github.com/elastic/elasticsearch/pull/130427)
- Fixes wildcard `DROP` after `LOOKUP JOIN` [#130448](https://github.com/elastic/elasticsearch/pull/130448)
- Avoids O(N^2) in `VALUES` with ordinals grouping [#130576](https://github.com/elastic/elasticsearch/pull/130576)
- Fixes behavior for `_index` LIKE for ES|QL [#130849](https://github.com/elastic/elasticsearch/pull/130849)
- Fixes `LIMIT` null pointer exception with null value [#130914](https://github.com/elastic/elasticsearch/pull/130914)
- Specifies master timeout when submitting alias tasks [#130733](https://github.com/elastic/elasticsearch/pull/130733)
- Adds existing shards allocator settings to failure store allowed list [#131056](https://github.com/elastic/elasticsearch/pull/131056)


## July 7, 2025


### Features and enhancements

- Adds action to add or remove tags on the **Agent details** page in Fleet [#225433](https://github.com/elastic/kibana/pull/225433)
- Adds a new **Profiles** tab to the Inspector flyout in Discover [#222999](https://github.com/elastic/kibana/pull/222999)
- Adds new rules callout to Metric, Logs, and Inventory rules in Elastic Observability Serverless [#224387](https://github.com/elastic/kibana/pull/224387)
- Adds manual test for bulk import functionality in Elastic Observability Serverless [#225497](https://github.com/elastic/kibana/pull/225497)
- Uses `id` instead of `name` to group vulnerabilities by resource and cloud account in Elastic Security Serverless [#225492](https://github.com/elastic/kibana/pull/225492)
- Updates Gemini model in Elastic Security Serverless [#225917](https://github.com/elastic/kibana/pull/225917)
- Updates the navigation menu in Elasticsearch Serverless [#225709](https://github.com/elastic/kibana/pull/225709)
- Adds performance charts to the **Usage and performance** section on the project overview page in Elastic Cloud Serverless
- Speeds up (filtered) KNN queries for flat vector fields [#130251](https://github.com/elastic/elasticsearch/pull/130251)
- Wraps ES KNN queries with PatienceKNN query [#127223](https://github.com/elastic/elasticsearch/pull/127223)
- Adds low-level optimized Neon, AVX2, and AVX 512 float32 vector operations [#130635](https://github.com/elastic/elasticsearch/pull/130635)
- Adds IBM Granite completion and chat completion support [#129146](https://github.com/elastic/elasticsearch/pull/129146)


### Fixes

- Fixes an issue causing reports to fail with an invalid header error [#225919](https://github.com/elastic/kibana/pull/225919)
- Refreshes `Values from a query` options upon dashboard reload [#225101](https://github.com/elastic/kibana/pull/225101)
- Removes kebab-case warnings in Console [#226114](https://github.com/elastic/kibana/pull/226114)
- Fixes the default title being overwritten by a custom title upon reload in Lens [#225664](https://github.com/elastic/kibana/pull/225664)
- Fixes an issue with dashboards where adhoc dataviews were recommended as most relevant when creating a control [#225705](https://github.com/elastic/kibana/pull/225705)
- Hides the **Select all** checkbox from single select controls in dashboards [#226311](https://github.com/elastic/kibana/pull/226311)
- Fixes edited query being overwritten by the original query when it is resolved in Discover [#224671](https://github.com/elastic/kibana/pull/224671)
- Prevents selected document from changing when resizing the **Document** flyout with a keyboard in Discover [#225594](https://github.com/elastic/kibana/pull/225594)
- Only returns suggested dashboards for custom threshold alerts in Elastic Observability Serverless [#224458](https://github.com/elastic/kibana/pull/224458)
- Fixes `Unable to load page` error on the **Schema** page in Elastic Observability Serverless [#225481](https://github.com/elastic/kibana/pull/225481)
- Limits environment name length when creating an ML job in Elastic Observability Serverless [#225973](https://github.com/elastic/kibana/pull/225973)
- Fixes `Unable to load page` error on the **Operations** page in Elastic Observability Serverless [#226036](https://github.com/elastic/kibana/pull/226036)
- Fixes an issue with the AI assistant chat display in Elastic Observability Serverless when a device has `Reduce motion` turned on [#226552](https://github.com/elastic/kibana/pull/226552)
- Collapses *query tool calls in Elastic Observability Serverless [#226078](https://github.com/elastic/kibana/pull/226078)
- Adds a title to the rule gap histogram in the **Rules** dashboard in Elastic Security Serverless [#225274](https://github.com/elastic/kibana/pull/225274)
- Moves the alerts redirect higher in the components tree in Elastic Security Serverless [#225650](https://github.com/elastic/kibana/pull/225650)
- Updates entity links across Elastic Security Serverless to open flyouts instead of redirecting to other pages [#225381](https://github.com/elastic/kibana/pull/225381)
- Stops ML rule installation and upgrade errors from showing up for users with Basic licenses [#224676](https://github.com/elastic/kibana/pull/224676)
- Updates placeholder text and validation message for **Related integrations** in Elastic Security Serverless  [#225775](https://github.com/elastic/kibana/pull/225775)
- Resets to the default value when the `lookbackInterval` field is empty in Machine Learning [#225249](https://github.com/elastic/kibana/pull/225249)
- Fixes the handling of time range in embedded anomaly swim lane in Machine Learning [#225803](https://github.com/elastic/kibana/pull/225803)
- Adds discernible text to the refresh button on the **Streams** > **Processing** page [#225816](https://github.com/elastic/kibana/pull/225816)
- Fixes handling of context limit errors in Playground when using Elastic Managed LLMs [#225360](https://github.com/elastic/kibana/pull/225360)
- Adds check for `isIndexed` in text fields when generating field exists queries to avoid `IllegalStateException` when field is stored but not indexed or with `doc_values` [#130531](https://github.com/elastic/elasticsearch/pull/130531)
- Forces `niofs` for `fdt tmp` file read access when flushing stored fields [#130308](https://github.com/elastic/elasticsearch/pull/130308)
- Releases `Row` on failure in `TopNOperator` [#130330](https://github.com/elastic/elasticsearch/pull/130330)
- Fixes queries with missing index, `skip_unavailable`, and filters [#130344](https://github.com/elastic/elasticsearch/pull/130344)
- Supports `avg` on aggregate metric double [#130421](https://github.com/elastic/elasticsearch/pull/130421)
- Handles unavailable `MD5` in ES|QL [#130158](https://github.com/elastic/elasticsearch/pull/130158)
- Prevents search functions from working with a non-STANDARD index [#130638](https://github.com/elastic/elasticsearch/pull/130638)
- Allows timeout during trained model download process [#129003](https://github.com/elastic/elasticsearch/pull/129003)
- Renames the ELSER V2 default model and the default inference endpoint [#130336](https://github.com/elastic/elasticsearch/pull/130336)


## June 30, 2025


### Features and enhancements

- Adds the ability to schedule reports with a recurring schedule and view previously scheduled reports [#224849](https://github.com/elastic/kibana/pull/224849)
- Adds internal CRUD API routes in *Lens* [#223296](https://github.com/elastic/kibana/pull/223296)
- Adds `Select all` and `Deselect all` buttons to the options list popover to allow you to make bulk selections in Dashboards and Visualizations [#221010](https://github.com/elastic/kibana/pull/221010)
- Adds the flip LOOKUP JOIN parameter in ES|QL to GA in docs [#225117](https://github.com/elastic/kibana/pull/225117)
- Passes the `TimeRange` into the `getESQLResults` in order for queries with `_tstart` and `_tend` to work properly in Discover [#225054](https://github.com/elastic/kibana/pull/225054)
- Enables the "expand to fit" query function on mount in Discover [#225509](https://github.com/elastic/kibana/pull/225509)
- Adds Logs Essentials for APM/Infra in Elastic Observability Serverless [#223030](https://github.com/elastic/kibana/pull/223030)
- Allows users to choose which space monitors will be available in Elastic Observability Serverless [#221568](https://github.com/elastic/kibana/pull/221568)
- Remaps `iInCircle` and `questionInCircle`, and deprecates the `help` icon in the global header [#223142](https://github.com/elastic/kibana/pull/223142)
- Adds docs for the chat completion public API in Elastic Observability Serverless [#224235](https://github.com/elastic/kibana/pull/224235)
- Enables the Security Entity Analytics Privileged user monitoring feature in Elastic Security Serverless [#224638](https://github.com/elastic/kibana/pull/224638)
- Displays visualizations in the key insights panel of the Privileged User Monitoring dashboard in Elastic Security Serverless [#223092](https://github.com/elastic/kibana/pull/223092)
- Introduces a new UI to optionally update the `kibana.alert.workflow_status` field for alerts associated with Attack discoveries in Elastic Security Serverless [#225029](https://github.com/elastic/kibana/pull/225029)
- Enables the runscript feature flag in Elastic Security Serverless [#224819](https://github.com/elastic/kibana/pull/224819)
- Adds the incremental ID service; exposes the ID in the UI in Elastic Security Serverless [#222874](https://github.com/elastic/kibana/pull/222874)
- Adds the `windows.advanced.events.security.provider_etw` field as an advanced policy option in Elastic Defend in Elastic Security Serverless [#222197](https://github.com/elastic/kibana/pull/222197)
- Adds new starter prompts to the AI Assistant in Elastic Security Serverless [#224981](https://github.com/elastic/kibana/pull/224981)
- Adds the ability to revert prebuilt rules to their base version in Elastic Security Serverless [#223301](https://github.com/elastic/kibana/pull/223301)
- Adds support for a collapsible section in the integration readme in Kibana Security [#223916](https://github.com/elastic/kibana/pull/223916)
- Adds new severity colors, alignment, and UX for filtering anomalies in Machine learning [#221081](https://github.com/elastic/kibana/pull/221081)
- Updates NL-2-ESQL docs [#224868](https://github.com/elastic/kibana/pull/224868)
- Adds keyword highlighting for ES|QL patterns, and the ability to open a new Discover tab to filter for docs that match the selected pattern [#222871](https://github.com/elastic/kibana/pull/222871)
- Enables adaptive allocations and allows you to set max allocations in Machine learning [#222726](https://github.com/elastic/kibana/pull/222726)
- Adds a loading indicator while data sources are being fetched [#225005](https://github.com/elastic/kibana/pull/225005)
- Introduces a new home page in Elasticsearch Serverless [#223172](https://github.com/elastic/kibana/pull/223172)
- Adds a Search Home page in Elastic Stack classic and the solution navigation in Elasticsearch Serverless [#225162](https://github.com/elastic/kibana/pull/225162)
- Adds updates to streamline the solution navigation in Elasticsearch Serverless [#224755](https://github.com/elastic/kibana/pull/224755)


### Fixes

- Fixes the panel title sync with saved object when using `defaultTitle` in Dashboards and Visualizations [#225237](https://github.com/elastic/kibana/pull/225237)
- Fixes a performance issue in the Lens ES|QL charts in Dashboards and Visualizations [#225067](https://github.com/elastic/kibana/pull/225067)
- Fixes visual issues with truncated long labels and hover styles in Dashboards and Visualizations [#225430](https://github.com/elastic/kibana/pull/225430)
- Fixes controls selections that caused multiple fetches in Dashboards and Visualizations [#224761](https://github.com/elastic/kibana/pull/224761)
- Ensures package policy names are unique when moving across spaces in Data ingestion and Fleet [#224804](https://github.com/elastic/kibana/pull/224804)
- Fixes export CSV in the Agent list in Data ingestion and Fleet [#225050](https://github.com/elastic/kibana/pull/225050)
- Replaces call to registry when deleting Kibana assets for custom packages in Data ingestion and Fleet [#224886](https://github.com/elastic/kibana/pull/224886)
- Fixes UI error when no tags filter is selected in Data ingestion and Fleet [#225413](https://github.com/elastic/kibana/pull/225413)
- Uses bulk helper for bulk importing knowledge base entries in Elastic Observability Serverless [#223526](https://github.com/elastic/kibana/pull/223526)
- Improves the knowledge base retrieval by rewriting the user prompt before querying Elasticsearch in Elastic Observability Serverless [#224498](https://github.com/elastic/kibana/pull/224498)
- Fixes the Agent Explorer page in Elastic Observability Serverless [#225071](https://github.com/elastic/kibana/pull/225071)
- Hides Settings from serverless navigation in Elastic Observability Serverless [#225436](https://github.com/elastic/kibana/pull/225436)
- Replaces hard-coded CSS values to us the `euiTheme` instead in Elastic Security Serverless [#225307](https://github.com/elastic/kibana/pull/225307)
- Fixes URL query handling for asset inventory flyout in Elastic Security Serverless [#225199](https://github.com/elastic/kibana/pull/225199)
- Adds missing model Claude 3.7 to accepted models in Elasticsearch Serverless [#224943](https://github.com/elastic/kibana/pull/224943)
- Supports returning default `index_options` for `semantic_text` fields when `include_defaults` is true [#129967](https://github.com/elastic/elasticsearch/pull/129967)
- Avoids dropping aggregate groupings in local plans [#129370](https://github.com/elastic/elasticsearch/pull/129370)
- Prevents duplication of "invalid index name" string in the final exception error message [#130027](https://github.com/elastic/elasticsearch/pull/130027)
- Fixes timeout bug in `DBQ` deletion of unused and orphan ML data [#130083](https://github.com/elastic/elasticsearch/pull/130083)
- Fixes incorrect accounting of semantic text indexing memory pressure [#130221](https://github.com/elastic/elasticsearch/pull/130221)


## June 26, 2025


### Features and enhancements

- Elastic Cloud Serverless is now available in the Microsoft Azure `eastus` [region](https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud/regions).
- Checks if cluster aliases and index patterns are valid before executing query [#122497](https://github.com/elastic/elasticsearch/pull/122497)
- Aggressively releases shard contexts [#129454](https://github.com/elastic/elasticsearch/pull/129454)


## June 23, 2025


### Features and enhancements

- Adds new setting `xpack.actions.webhook.ssl.pfx.enabled` to disable PFX file support for SSL client authentication in Webhook connectors [#222507](https://github.com/elastic/kibana/pull/222507)
- Introduces **Scheduled Reports** feature [#221028](https://github.com/elastic/kibana/pull/221028)
- Adds `xpack.actions.email.services.enabled` setting to control availability of email services in connectors [#223363](https://github.com/elastic/kibana/pull/223363)
- Enables support for adding observables, procedures, and custom fields to alerts for TheHive [#207255](https://github.com/elastic/kibana/pull/207255)
- Improves visual highlight behavior in the add panel UI [#223614](https://github.com/elastic/kibana/pull/223614)
- Supports agentless traffic filters for Elastic Agent [#222082](https://github.com/elastic/kibana/pull/222082)
- Adds support for suggesting all operators in the query editor [#223503](https://github.com/elastic/kibana/pull/223503)
- Introduces accordion sections and attribute tables in UI components [#224185](https://github.com/elastic/kibana/pull/224185)
- Adds monitor downtime alert when no data is available [#220127](https://github.com/elastic/kibana/pull/220127)
- Introduces **Maintenance Windows** functionality [#222174](https://github.com/elastic/kibana/pull/222174)
- Enables editing of labels and tags for private locations in **Synthetics** [#221515](https://github.com/elastic/kibana/pull/221515)
- Adds new tail-based sampling settings to integration policies [#224479](https://github.com/elastic/kibana/pull/224479)
- Enables model ID retrieval from anonymization rules [#224280](https://github.com/elastic/kibana/pull/224280)
- Updates SLO starter prompt text for improved guidance [#224493](https://github.com/elastic/kibana/pull/224493)
- Introduces `deactivate_...` agent configuration settings for EDOT Node.js [#224502](https://github.com/elastic/kibana/pull/224502)
- Updates system prompt to include information about anonymization [#224211](https://github.com/elastic/kibana/pull/224211)
- Adds support for Microsoft Defender's `runscript` command in the **Response Console** [#222377](https://github.com/elastic/kibana/pull/222377)
- Moves Automatic Migration from **Tech Preview** to General Availability [#224544](https://github.com/elastic/kibana/pull/224544)
- Adds simplified bulk editing for alert suppression rules [#223090](https://github.com/elastic/kibana/pull/223090)
- Introduces **XSOAR Connector** [#212049](https://github.com/elastic/kibana/pull/212049)
- Adds `name` field to the Rule Migrations UI and data model [#223860](https://github.com/elastic/kibana/pull/223860)
- Enables collection of `dns` events for macOS in **Elastic Defend** [#223566](https://github.com/elastic/kibana/pull/223566)
- Adds usage callout for **Elastic Indexing Service (EIS)** [#221566](https://github.com/elastic/kibana/pull/221566)
- Adds `ecs@mappings` component template to transform destination index templates [#223878](https://github.com/elastic/kibana/pull/223878)
- Renames advanced policy setting `disable_origin_info_collection` to `origin_info_collection` and changed its default behavior to Opt-In [#223882](https://github.com/elastic/kibana/pull/223882)
- Introduces cleanup task for unused URLs [#220138](https://github.com/elastic/kibana/pull/220138)
- Marks the **Session Invalidation API** as Stable [#224076](https://github.com/elastic/kibana/pull/224076)
- Hides the Adaptive Allocations toggle for Trained Models in **Serverless** environments [#224097](https://github.com/elastic/kibana/pull/224097)
- Adds option to disable **AIOps** features in Kibana [#221286](https://github.com/elastic/kibana/pull/221286)
- Enables autocompletion for **ES|QL** queries in the Console UI [#219980](https://github.com/elastic/kibana/pull/219980)
- Improves layout and content of rule listing and overview pages [#223603](https://github.com/elastic/kibana/pull/223603)
- Adds support for changing settings when re-processing Rule Migrations [#222542](https://github.com/elastic/kibana/pull/222542)
- Implements navigation UI for the **Overview Page** in **Entity Analytics** [#221748](https://github.com/elastic/kibana/pull/221748)
- Adds support for partial result handling in **ES|QL** [#223198](https://github.com/elastic/kibana/pull/223198)
- Adds an **Executable Name** tab to the TopN view [#224291](https://github.com/elastic/kibana/pull/224291)
- Adds a SageMaker Elastic payload [#129413](https://github.com/elastic/elasticsearch/pull/129413)
- Adds recursive chunker [#126866](https://github.com/elastic/elasticsearch/pull/126866)
- Moves to the Cohere V2 API for new inference endpoints [#129884](https://github.com/elastic/elasticsearch/pull/129884)
- Adds RemoveBlock API to allow `DELETE /{index}/_block/{block}` [#129128](https://github.com/elastic/elasticsearch/pull/129128)
- Makes `FORK` available in release builds [#129606](https://github.com/elastic/elasticsearch/pull/129606)
- Adds support for `LIKE` LIST [#129170](https://github.com/elastic/elasticsearch/pull/129170)
- Pushes down `LOOKUP JOIN` past `Project` [#129503](https://github.com/elastic/elasticsearch/pull/129503)
- Improves performance for LIKE (LIST) in ES|QL [#129557](https://github.com/elastic/elasticsearch/pull/129557)
- Makes dense_vector fields updatable to `bbq_flat` or `bbq_hnsw` [#128291](https://github.com/elastic/elasticsearch/pull/128291)
- Updates `sparse_vector` field mapping to include default setting for token pruning [#129089](https://github.com/elastic/elasticsearch/pull/129089)
- Upgrades the Lucene version to 10.2.2 [#129546](https://github.com/elastic/elasticsearch/pull/129546)
- Adds a simplified syntax for the `linear` retriever [#129200](https://github.com/elastic/elasticsearch/pull/129200)


### Fixes

- Fixes pagination not working correctly in certain tables [#223537](https://github.com/elastic/kibana/pull/223537)
- Fixes bulk actions selecting incorrect agents when `namespace` filter is used [#224036](https://github.com/elastic/kibana/pull/224036)
- Corrects `z-index` issues in the **ESQL Query Editor** [#222841](https://github.com/elastic/kibana/pull/222841)
- Updates ARIA tags for improved accessibility in selected fields UI [#224224](https://github.com/elastic/kibana/pull/224224)
- Ensures **Last Successful Screenshot** matches the correct step in Synthetics [#224220](https://github.com/elastic/kibana/pull/224220)
- Improves network error handling for error details panel [#224296](https://github.com/elastic/kibana/pull/224296)
- Fixes broken **EDOT JVM Metrics Dashboard** when classic agent metrics are present [#224052](https://github.com/elastic/kibana/pull/224052)
- Fixes **SLO federated view** bug caused by exceeding index name byte limit [#224478](https://github.com/elastic/kibana/pull/224478)
- Fixes issue where OSS models failed when streaming was enabled [#224129](https://github.com/elastic/kibana/pull/224129)
- Corrects display issues for rule filters in the UI [#222963](https://github.com/elastic/kibana/pull/222963)
- Fixes time normalization bug for day units in rule scheduling [#224083](https://github.com/elastic/kibana/pull/224083)
- Resolves issue where unknown fields weren't supported in **Data Visualizer** and **Field Statistics** [#223903](https://github.com/elastic/kibana/pull/223903)
- Fixes Bedrock connector not using proxy configuration settings [#224130](https://github.com/elastic/kibana/pull/224130)
- Passes correct namespace to `migrateInputDocument` logic [#222313](https://github.com/elastic/kibana/pull/222313)
- Adjusts app menu header `z-index` to avoid clashing with the portable dev console [#224708](https://github.com/elastic/kibana/pull/224708)
- Reverts to using `.watches` system index in Watcher UI [#223898](https://github.com/elastic/kibana/pull/223898)
- Fixes several issues introduced in versions 8.18.0 through 9.1.0, including broken pagination (limited to 10 items), erroneous error banners, and broken search functionality.
- Fixes **Discard** button state change logic for toggles [#223493](https://github.com/elastic/kibana/pull/223493)
- Removes `originId` from connectors during rule import [#223454](https://github.com/elastic/kibana/pull/223454)
- Fixes null pointer exception (NPE) in flat_bbq scorer when all vectors are missing [#129548](https://github.com/elastic/elasticsearch/pull/129548)
- Fixes filtered knn vector search when query timeouts are enabled [#129440](https://github.com/elastic/elasticsearch/pull/129440)
- Fixes NPE in `SemanticTextHighlighter` [#129509](https://github.com/elastic/elasticsearch/pull/129509)
- Adds simplified linear retriever [#129200](https://github.com/elastic/elasticsearch/pull/129200)
- Adds `index_options` to `semantic_text` field mappings [#119967](https://github.com/elastic/elasticsearch/pull/119967)
- Adds simplified RRF retriever [#129659](https://github.com/elastic/elasticsearch/pull/129659)
- Simplified linear and RRF retrievers - Return error on empty fields parameter [#129962](https://github.com/elastic/elasticsearch/pull/129962)
- Checks prefixes when constructing synthetic source for flattened fields [#129580](https://github.com/elastic/elasticsearch/pull/129580)
- Makes flattened synthetic source concatenate object keys on scalar/object mismatch [#129600](https://github.com/elastic/elasticsearch/pull/129600)
- Fixes `PushQueriesIT.testLike()` fails [#129647](https://github.com/elastic/elasticsearch/pull/129647)
- Fixes `PushQueryIT#testEqualityOrTooBig` [#129657](https://github.com/elastic/elasticsearch/pull/129657)
- Uses a temp `IndexService` for template validation [#129507](https://github.com/elastic/elasticsearch/pull/129507)
- Sets `event.dataset` if empty for logs [#129074](https://github.com/elastic/elasticsearch/pull/129074)
- Checks for model deployment in inference endpoints before stopping [#129325](https://github.com/elastic/elasticsearch/pull/129325)


## June 17, 2025


### Features and enhancements

- Elastic Cloud Serverless is now available in two new Google Cloud Platform [regions](https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud/regions): GCP Belgium (`europe-west1`) and GCP Mumbai (`asia-south1`)


## June 16, 2025


### Features and enhancements

- Adds support for deleting active or inactive alerts after one day without a status update [#216613](https://github.com/elastic/kibana/pull/216613)
- Adds AWS SES email configuration options: `xpack.actions.email.services.ses.host` and `ses.port` [#221389](https://github.com/elastic/kibana/pull/221389)
- Adds point visibility option for area and line charts in **Lens** [#222187](https://github.com/elastic/kibana/pull/222187)
- Enables feature flag for the tabular integrations Fleet UI [#222842](https://github.com/elastic/kibana/pull/222842)
- Displays partial results when an ES|QL query times out due to the `search:timeout` setting [#219027](https://github.com/elastic/kibana/pull/219027)
- Improves handling of long fields in the **Discover** editor [#223222](https://github.com/elastic/kibana/pull/223222)
- Adds a primary **Add to case** button to Elastic Observability Serverless [#223184](https://github.com/elastic/kibana/pull/223184)
- Renders suggested dashboards in relevant contexts in Elastic Observability Serverless [#223424](https://github.com/elastic/kibana/pull/223424)
- Adds a **History** tab for calendar-based SLOs in the Elastic Observability Serverless SLO details page [#223825](https://github.com/elastic/kibana/pull/223825)
- Updates the `spec.max` setting to version 3.4 for Elastic Observability Serverless [#221544](https://github.com/elastic/kibana/pull/221544)
- Adds support for anonymizing sensitive data for Elastic Observability Serverless [#223351](https://github.com/elastic/kibana/pull/223351)
- Adds `logging_level` configuration in Elastic Observability Serverless for EDOT Node.js agent [#222883](https://github.com/elastic/kibana/pull/222883)
- Removes `is_correction` and `confidence` attributes from Elastic Observability Serverless Knowledge Base entries [#222814](https://github.com/elastic/kibana/pull/222814)
- Displays linked cases in the Elastic Observability Serverless alert details overview [#222903](https://github.com/elastic/kibana/pull/222903)
- Refetches alert rule data when edits are submitted in the Elastic Observability Serverless flyout [#222118](https://github.com/elastic/kibana/pull/222118)
- Adds `disable_origin_info_collection` to endpoint policy advanced settings in Elastic Security Serverless [#222030](https://github.com/elastic/kibana/pull/222030)
- Improves alert filtering in Elastic Security Serverless by including ECS `data_stream` fields under `kibana.alert.original_data_stream.*` [#220447](https://github.com/elastic/kibana/pull/220447)
- Adds a rare scripts job to the preconfigured Security:Windows anomaly detection jobs [#223041](https://github.com/elastic/kibana/pull/223041)
- Adds `converse` and `converseStream` subActions to Bedrock connectors for Machine Learning [#223033](https://github.com/elastic/kibana/pull/223033)
- Improves error handling in the AI Connector creation UI for Machine Learning [#221859](https://github.com/elastic/kibana/pull/221859)
- Disables trace visualizations in **Discover** for Logs Essentials serverless mode in Elastic Observability Serverles [#222991](https://github.com/elastic/kibana/pull/222991)
- Adds the **Attributes** tab to the Elastic Observability Serverless document viewer [#222391](https://github.com/elastic/kibana/pull/222391)


### Fixes

- Reverts instructions for installing the complete Elastic Agent [#223520](https://github.com/elastic/kibana/pull/223520)
- Fixes incorrect function signatures in bucket functions for **Discover** [#222553](https://github.com/elastic/kibana/pull/222553)
- Reverts CSV export time range fix in **Discover** [#223249](https://github.com/elastic/kibana/pull/223249)
- Adds `aria-labelledby` to Elastic Charts SVG for accessibility in Elastic Observability Serverless [#220298](https://github.com/elastic/kibana/pull/220298)
- Hides **Data set details** when `dataStream` comes from a remote cluster in Elastic Observability Serverless [#220529](https://github.com/elastic/kibana/pull/220529)
- Prevents unnecessary re-render after completing a **Run test** action in Elastic Observability Serverless [#222503](https://github.com/elastic/kibana/pull/222503)
- Skips tool instructions in system messages when tools are disabled in Elastic Observability Serverless [#223278](https://github.com/elastic/kibana/pull/223278)
- Fixes broken **View in Discover** link in Elastic Security Serverless [#217993](https://github.com/elastic/kibana/pull/217993)
- Expands metrics pattern for the Java EDOT dashboard  in Elastic Observability Serverless [#223539](https://github.com/elastic/kibana/pull/223539)
- Applies `autoFocus` to the `cc` and `bcc` fields in the Elastic Observability Serverless email connector form [#223828](https://github.com/elastic/kibana/pull/223828)
- Fixes rendering issues in the Elastic Security Serverless Threat Enrichment component [#223164](https://github.com/elastic/kibana/pull/223164)
- Ensures ingest pipelines are installed in all relevant spaces and assigned to appropriate indices in Elastic Security Serverless [#221937](https://github.com/elastic/kibana/pull/221937)
- Fixes card overflow issues on the **Machine Learning Overview** page [#223431](https://github.com/elastic/kibana/pull/223431)
- Applies chunking algorithm to `getIndexBasicStats` to improve performance [#221153](https://github.com/elastic/kibana/pull/221153)


## June 9, 2025


### Features and enhancements

- Ensures the Report UI only displays reports generated in the current space [#221375](https://github.com/elastic/kibana/pull/221375).
- Color mapping is now GA. `palette` definitions are deprecated and turning off Legacy mode will replace the palette with an equivalent color mapping configuration in* **Lens**. [#220296](https://github.com/elastic/kibana/pull/220296).
- Updates time based charts to use the multi-layer time axis by default, providing a better time window context and improved label positioning. [#210579](https://github.com/elastic/kibana/pull/210579).
- Adds an integration flyout to Agent policy details in Fleet [#220229](https://github.com/elastic/kibana/pull/220229).
- Enables the `enableSyncIntegrationsOnRemote` feature flag in Fleet [#220215](https://github.com/elastic/kibana/pull/220215).
- Enables migration of a single agent to another cluster using the actions menu in Fleet. [#222111](https://github.com/elastic/kibana/pull/222111).
- Adds a button allowing users to skip to the next section in the fields list in **Discover** [#221792](https://github.com/elastic/kibana/pull/221792).
- Adds the **SLO Management** page to Elastic Observability Serverless, allowing users to view definitions, delete SLOs, and purge SLI data without having to consider instances [#222238](https://github.com/elastic/kibana/pull/222238).
- Adds a new APM dashboard for the Golang OpenTelemetry runtime metrics in Elastic Observability Serverless [#220242](https://github.com/elastic/kibana/pull/220242).
- Uses the bulk API to import knowledge base entries in Elastic Observability Serverless [#222084](https://github.com/elastic/kibana/pull/222084).
- Improves system prompt and instructions for the `context` function in the Elastic Observability AI Assistant to work better with Claude models [#221965](https://github.com/elastic/kibana/pull/221965).
- Sets `observabilityAIAssistantAPIClient` as the preferred test for type-safe endpoint calls with scoped users in the Elastic Observability AI Assistant [#222753](https://github.com/elastic/kibana/pull/222753).
- Adds a custom script selector component to the **Response console** in Elastic Security Serverless [#204965](https://github.com/elastic/kibana/pull/204965).
- Updates the `AssetCriticalityBadge` colors to the Borealis theme in Elastic Security Serverless [#222024](https://github.com/elastic/kibana/pull/222024).
- Updates the risk severity colors to the Borealis theme in Elastic Security Serverless [#222061](https://github.com/elastic/kibana/pull/222061).
- Enables **Content Connectors** in the **Stack Management** menu in Elastic Security Serverless [#221856](https://github.com/elastic/kibana/pull/221856).
- Implements PKI authentication support for the `.gen-ai` connector’s `OpenAI Other` provider [#219984](https://github.com/elastic/kibana/pull/219984).
- Enables sort optimization on int, short and byte fields [#127968](https://github.com/elastic/elasticsearch/pull/127968)
- Adds `bucketedSort` based on int [#128848](https://github.com/elastic/elasticsearch/pull/128848)
- Adds `l2_norm` normalization support to linear retriever [#128504](https://github.com/elastic/elasticsearch/pull/128504)
- Implements SAML custom attributes support in the Identity Provider plugin [#128176](https://github.com/elastic/elasticsearch/pull/128176)
- Fixes unsupported privileges error message during role and API key creation [#128858](https://github.com/elastic/elasticsearch/pull/128858)
- Makes adaptive allocations scale to zero configurable and sets default to 24h [#128914](https://github.com/elastic/elasticsearch/pull/128914)
- Adds Mistral AI Chat Completion support to Inference Plugin [#128538](https://github.com/elastic/elasticsearch/pull/128538)
- Adds `NormalizeForStreamProcessor` [#125699](https://github.com/elastic/elasticsearch/pull/125699)
- Adds another option for ES|QL date nanos implicit casting in union types  [#127797](https://github.com/elastic/elasticsearch/pull/127797)
- Adds COMPLETION command as a tech preview ES|QL feature [#128948](https://github.com/elastic/elasticsearch/pull/128948)
- Adds ES|QL support for `ST_GEOHASH`, `ST_GEOTILE`, and `ST_GEOHEX`" [#125143](https://github.com/elastic/elasticsearch/pull/125143)
- Adds support for `LOOKUP JOIN` on aliases [#128519](https://github.com/elastic/elasticsearch/pull/128519)
- Implements `copy_sign` function for ES|QL [#128281](https://github.com/elastic/elasticsearch/pull/128281)
- Adds `MATCH_PHRASE` in ES|QL[#127661](https://github.com/elastic/elasticsearch/pull/127661)


### Fixes

- Fixes Kibana being stuck in a reboot loop when `cancelAlertsOnRuleTimeout` is set to `false` [#222263](https://github.com/elastic/kibana/pull/222263).
- Adds saved object version for collapsible sections [#222450](https://github.com/elastic/kibana/pull/222450).
- Fixes the `UnenrollInactiveAgentsTask` query in Fleet to un-enroll only those agents that are inactive for longer than `unenroll_timeout` [#222592](https://github.com/elastic/kibana/pull/222592).
- Adds **Actions** header to the unified data table in **Discover** [#220824](https://github.com/elastic/kibana/pull/220824).
- Fixes `COALESCE` validation in **ES|QL** [#222425](https://github.com/elastic/kibana/pull/222425).
- Fixes incorrect suggestions after a named variable such as `?value` is entered in a `WHERE` query in **ES|QL** [#222312](https://github.com/elastic/kibana/pull/222312).
- Replaces `onChangedItemIndices` with `onChangeRenderedItems` when determining which service details to fetch in Elastic Observability Serverless [#222439](https://github.com/elastic/kibana/pull/222439).
- Fixes pagination on the Services **Inventory** page when progressive loading is enabled in Elastic Observability Serverless [#220514](https://github.com/elastic/kibana/pull/220514).
- Refactors styling for the timeline in Elastic Security Serverless from `styled-components` to `emotion` [#222438](https://github.com/elastic/kibana/pull/222438).
- Fixes wrong content appearing when switching tabs in the **Ingest your data** section on the **Get started** page in Elastic Security Serverless [#222271](https://github.com/elastic/kibana/pull/222271).
- Fixes incorrect header text in the **Rule exception** flyout in Elastic Security Serverless [#222248](https://github.com/elastic/kibana/pull/222248).
- Fixes an issue with adding a field when no pipeline has been generated during import in Machine Learning [#222775](https://github.com/elastic/kibana/pull/222775).
- Fixes an issue with the OpenAI connector not using the action proxy configuration for all subactions in Machine Learning [#219617](https://github.com/elastic/kibana/pull/219617).
- Fixes an issue with **Anomaly Explorer** where the selected Overall swimlane bucket is not respected for `viewBy jobId` in Machine Learning [#222845](https://github.com/elastic/kibana/pull/222845).
- Fixes error handling when one or more connectors is deleted [#221958](https://github.com/elastic/kibana/pull/221958).
- Fixes NPE in semantic highlighter [#128989](https://github.com/elastic/elasticsearch/pull/128989)
- Improves execution of terms queries over wildcard fields [#128986](https://github.com/elastic/elasticsearch/pull/128986)
- Fixes minmax normalizer handling of single-doc result sets [#128689](https://github.com/elastic/elasticsearch/pull/128689)
- Fix missing highlighting in `match_all` queries for `semantic_text` fields [#128702](https://github.com/elastic/elasticsearch/pull/128702)
- Adds retry for `AccessDeniedException` in `AbstractFileWatchingService` [#128653](https://github.com/elastic/elasticsearch/pull/128653)
- Fixes conversion of a Lucene wildcard pattern to a regex [#128750](https://github.com/elastic/elasticsearch/pull/128750)
- Fixes significant terms not finding background documents for nested fields [#128472](https://github.com/elastic/elasticsearch/pull/128472)
- Supports `DATE_NANOS` in `LOOKUP JOIN` [#127962](https://github.com/elastic/elasticsearch/pull/127962)
- Adds workaround for `RLike` handling of empty lang pattern [#128895](https://github.com/elastic/elasticsearch/pull/128895)
- Throws `ISE` instead of `IAE` for illegal block in page [#128960](https://github.com/elastic/elasticsearch/pull/128960)
- Avoids unnecessary determinization in index pattern conflict checks [#128362](https://github.com/elastic/elasticsearch/pull/128362)
- Fixes null pointer exception when `date_buckets` aggregation is missing in the response [#128974](https://github.com/elastic/elasticsearch/pull/128974)


## June 2, 2025


### Features and enhancements

- Adds collapsible sections to Dashboards [#220877](https://github.com/elastic/kibana/pull/220877)
- Introduces a new `Density` setting for the Lens Data Table[#220252](https://github.com/elastic/kibana/pull/220252)
- Allows the "Open in lens" button to open in the same tab [#217528](https://github.com/elastic/kibana/pull/217528)
- Allows you to select the data stream type when creating policies for input packages in Fleet [#214216](https://github.com/elastic/kibana/pull/214216)
- Adds a single agent migration endpoint in Fleet, allowing a user to migrate an individual agent to another cluster [#220601](https://github.com/elastic/kibana/pull/220601)
- Adds shortcuts to the editor in Discover [#221331](https://github.com/elastic/kibana/pull/221331)
- Allows you to change the Knowledge Base model after installation in Elastic Observability Serverless [#221319](https://github.com/elastic/kibana/pull/221319)
- Adds investigation guide configuration to all Observability rules in Elastic Observability Serverless [#217106](https://github.com/elastic/kibana/pull/217106)
- Remove semantic_text migration from Elastic Observability Serverless [#220886](https://github.com/elastic/kibana/pull/220886)
- Searches for the CVE ID in all search parameters instead of only the name in Elastic Security Serverless [#221099](https://github.com/elastic/kibana/pull/221099)
- Updates the "Highlighted fields" button in the details flyout and enables the feature flag in Elastic Security Serverless [#221862](https://github.com/elastic/kibana/pull/221862)
- Introduces new `empty` states for the Change Point Detection page in Machine learning [#219072](https://github.com/elastic/kibana/pull/219072)
- Conditionally force sequential reading in `LuceneSyntheticSourceChangesSnapshot` [#128473](https://github.com/elastic/elasticsearch/pull/128473)
- Skips indexing points for `seq_no` in tsdb and logsdb [#128139](https://github.com/elastic/elasticsearch/pull/128139)
- Combines small pages in `LIMIT` [#128531](https://github.com/elastic/elasticsearch/pull/128531)
- Adds `ROUND_TO` function [#128278](https://github.com/elastic/elasticsearch/pull/128278)
- Allows lookup join on mixed numeric fields in ES|QL [#128263](https://github.com/elastic/elasticsearch/pull/128263)
- Adds optimization to purge join on null merge key [#127583](https://github.com/elastic/elasticsearch/pull/127583)
- Adds support for parameters in `LIMIT` command [#128464](https://github.com/elastic/elasticsearch/pull/128464)
- Pushes down constructs doing case-insensitive regexes [#128393](https://github.com/elastic/elasticsearch/pull/128393)
- Adds VoyageAI's v3.5 models [#128241](https://github.com/elastic/elasticsearch/pull/128241)
- Integrates OpenAi Chat Completion in SageMaker [#127767](https://github.com/elastic/elasticsearch/pull/127767)
- Improves exception for trained model deployment scale up timeout [#128218](https://github.com/elastic/elasticsearch/pull/128218)
- Adds support for aliases in `InferenceService` [#128584](https://github.com/elastic/elasticsearch/pull/128584)
- Implements ChatCompletion task for Google VertexAI with Gemini Models [#128105](https://github.com/elastic/elasticsearch/pull/128105)
- Adds configurable inference service [#127939](https://github.com/elastic/elasticsearch/pull/127939)


### Fixes

- Uses msearch to fetch the alerts for maintenance windows with a scoped query [#221702](https://github.com/elastic/kibana/pull/221702)
- Fixes querying installed packages in Fleet [#221624](https://github.com/elastic/kibana/pull/221624)
- Fixes an issue that prevented the style components from receiving the correct `colorMode` in Fleet [#221979](https://github.com/elastic/kibana/pull/221979)
- Makes the **Pin** button more accessible in Discover [#219230](https://github.com/elastic/kibana/pull/219230)
- Fixes an issue where the `Filter by field type` menu screen reader announcements were using duplicated in Discover [#221090](https://github.com/elastic/kibana/pull/221090)
- Removes an unneeded tabindex from Discover [#221265](https://github.com/elastic/kibana/pull/221265)
- Changes the field list icon when mapping changes from unmapped to mapped in Discover [#221308](https://github.com/elastic/kibana/pull/221308)
- Updates the doc viewer table's `aria-label` in Discover [#221736](https://github.com/elastic/kibana/pull/221736)
- Shows the ES|QL request URL in the Inspector flyout in Discover [#221816](https://github.com/elastic/kibana/pull/221816)
- Fixes index pattern parsing in Discover, which previously led to incomplete index pattern values being displayed [#221084](https://github.com/elastic/kibana/pull/221084)
- Ensures a non-aggregatable message is not shown if no data matches on the Dataset quality page in Elastic Observability Serverless [#221599](https://github.com/elastic/kibana/pull/221599)
- Deletes user instruction if the text is empty in Elastic Observability Serverless [#221560](https://github.com/elastic/kibana/pull/221560)
- Adjusts the bulk import knowledge base example to ndjson format in Elastic Observability Serverless [#221617](https://github.com/elastic/kibana/pull/221617)
- Modifies `RuleTypeModalComponent` to filter rule types that have `requiresAppContext` in Elastic Observability Serverless [#220005](https://github.com/elastic/kibana/pull/220005)
- Correctly nests APM > Synthetics Serverless navigation in Elastic Observability Serverless [#222115](https://github.com/elastic/kibana/pull/222115)
- Removes the "run soon for sync private location" task in Elastic Observability Serverless [#222062](https://github.com/elastic/kibana/pull/222062)
- Fixes the error count waterfall navigation reload issue in Elastic Observability Serverless [#221664](https://github.com/elastic/kibana/pull/221664)
- Fixes the Bedrock model on preconfigured connectors in Elastic Security Serverless [#221411](https://github.com/elastic/kibana/pull/221411)
- Removes the hard-coded width settings for the Threat Match mapping components in Elastic Security Serverless [#218628](https://github.com/elastic/kibana/pull/218628)
- Fixes the banner title in event preview in Elastic Security Serverless  [#222266](https://github.com/elastic/kibana/pull/222266)
- Ensures to only auto deploy Elastic models during file upload in Machine learning [#221357](https://github.com/elastic/kibana/pull/221357)
- Fixes the inference endpoint assignment to the trained model object in Machine learning  [#222076](https://github.com/elastic/kibana/pull/222076)
- Fixes an issue where `/etc/default/kibana` on deb packages and `/etc/sysconfig/kibana` on rpm packages would be overwritten during upgrading [#221276](https://github.com/elastic/kibana/pull/221276)
- Fixes and tests off-heap stats when using direct IO for accessing the raw vectors [#128615](https://github.com/elastic/elasticsearch/pull/128615)
- Allows non-score sorts in pinned retriever sub-retrievers [#128323](https://github.com/elastic/elasticsearch/pull/128323)
- Adds geometry validation for GEO types to exit early on invalid latitudes [#128259](https://github.com/elastic/elasticsearch/pull/128259)
- Fixes validation for null pointer exceptions (NPE) in `Enrich` and adds extra `@Nullable` annotations [#128260](https://github.com/elastic/elasticsearch/pull/128260)
- Passes timeout to chat completion [#128338](https://github.com/elastic/elasticsearch/pull/128338)
- Prevents retention classes from failing when deleting documents in read-only indices [#125408](https://github.com/elastic/elasticsearch/pull/125408)


## May 26, 2025


### Features and enhancements

- Suggests full text search in our recommendations [#221239](https://github.com/elastic/kibana/pull/221239)
- Flattens grid layout [#218900](https://github.com/elastic/kibana/pull/218900)
- Enables ELSER and E5 on EIS [#220993](https://github.com/elastic/kibana/pull/220993)
- Links dashboards on the Rule and Alert pages [#219019](https://github.com/elastic/kibana/pull/219019)
- Saves `group by` information with dynamic mapping [#219826](https://github.com/elastic/kibana/pull/219826)
- Introduces a new endpoint scheme for SIEM migration [#219597](https://github.com/elastic/kibana/pull/219597)
- Extends default log pattern on server side to include error information [#219940](https://github.com/elastic/kibana/pull/219940)
- Enables telemetry for `COMPLETION` command in ES|QL [#127731](https://github.com/elastic/elasticsearch/pull/127731)
- Refactors `SourceProvider` creation to consistently use `MappingLookup` [#128213](https://github.com/elastic/elasticsearch/pull/128213)
- Ensures config reload on `..data` symlink switch for CSI driver support [#127628](https://github.com/elastic/elasticsearch/pull/127628)
- Limits `Replace` function memory usage [#127924](https://github.com/elastic/elasticsearch/pull/127924)
- Adds `scalb` function [#127696](https://github.com/elastic/elasticsearch/pull/127696)
- Adds local optimizations for `constant_keyword` [#127549](https://github.com/elastic/elasticsearch/pull/127549)
- Adds Hugging Face Rerank support [#127966](https://github.com/elastic/elasticsearch/pull/127966)


### Fixes

- Fixes `getTimezone` default value [#220658](https://github.com/elastic/kibana/pull/220658)
- Loads correct system color mode at bootstrap [#218417](https://github.com/elastic/kibana/pull/218417)
- Fixes embeddables not refreshing on manual refresh or auto-refresh [#221326](https://github.com/elastic/kibana/pull/221326)
- Improves Discover session input focus behavior [#220876](https://github.com/elastic/kibana/pull/220876)
- Fixes suggestions after triple quote pair [#221200](https://github.com/elastic/kibana/pull/221200)
- Passes app state and global state to locator when redirecting from `/stream` path [#215867](https://github.com/elastic/kibana/pull/215867)
- Considers status rule locations only if not an empty array [#220983](https://github.com/elastic/kibana/pull/220983)
- Fixes a bug where update of an SLO created in a version older than 8.18 failed due to an invalid ingest pipeline [#221158](https://github.com/elastic/kibana/pull/221158)
- Checks for documents before starting semantic text migration [#221152](https://github.com/elastic/kibana/pull/221152)
- Improves error telemetry [#220938](https://github.com/elastic/kibana/pull/220938)
- Retrieves active integrations from installed integrations API [#218988](https://github.com/elastic/kibana/pull/218988)
- Fixes spaces search functionality for spaces created with avatar type as image [#220398](https://github.com/elastic/kibana/pull/220398)
- Fixes inability to clear Document ID in data view field editor preview [#220891](https://github.com/elastic/kibana/pull/220891)
- Reworks cookie and session storage to prevent unexpected logouts for certain users with certain use cases [#220430](https://github.com/elastic/kibana/pull/220430)
- Changes the AI Connector description [#221154](https://github.com/elastic/kibana/pull/221154)
- Checks the transform update index against its alias during updates [#124825](https://github.com/elastic/elasticsearch/pull/124825)
- Uses internal user for internal inference action [#128327](https://github.com/elastic/elasticsearch/pull/128327)
- Adds `NamedWriteable` for `RuleQueryRankDoc` [#128153](https://github.com/elastic/elasticsearch/pull/128153)
- Fixes null pointer exception in `APMTracer` through `RestController` [#128314](https://github.com/elastic/elasticsearch/pull/128314)
- Fixes alias removal in regex extraction with `JOIN` [#127687](https://github.com/elastic/elasticsearch/pull/127687)
- Avoids unintended attribute removal [#127563](https://github.com/elastic/elasticsearch/pull/127563)
- Considers `inlinestats` when having field_caps check for field names [#127564](https://github.com/elastic/elasticsearch/pull/127564)
- System data streams incorrectly show up in the list of template validation problems [#128161](https://github.com/elastic/elasticsearch/pull/128161)


## May 19, 2025


### Features and enhancements

- Supports recurring task scheduling with `rrule` in Alerting [#217728](https://github.com/elastic/kibana/pull/217728)
- Adds an embeddable panel to display alerts in **Dashboards** [#216076](https://github.com/elastic/kibana/pull/216076)
- Adds **Compare to** badge for **Metric chart** visualizations [#214811](https://github.com/elastic/kibana/pull/214811)
- Allows specifying an embedding model during onboarding for the Elastic Observability Serverless Knowledge Base [#218448](https://github.com/elastic/kibana/pull/218448)
- Enables click actions for **Stacktrace** and **Degraded Fields** in **Discover** for Elastic Observability Serverless [#214413](https://github.com/elastic/kibana/pull/214413)
- Shows **ELSER** in **EIS** only when available in Elastic Observability Serverless [#220096](https://github.com/elastic/kibana/pull/220096)
- Adds the ability to create alert rules from **ES|QL** dashboard visualizations through context menu or right-clicking a data point [#217719](https://github.com/elastic/kibana/pull/217719)
- Enables the `enableAutomaticAgentUpgrades` feature flag for Fleet [#219932](https://github.com/elastic/kibana/pull/219932)
- Adds Cloud Connectors support to Fleet for **CSPM** [#212200](https://github.com/elastic/kibana/pull/212200)
- Ensures alerts created within **Maintenance Windows** trigger actions after the window expires [#219797](https://github.com/elastic/kibana/pull/219797)
- Adds **Copy value** button to field value cells in **Discover** [#218817](https://github.com/elastic/kibana/pull/218817)
- Hides the **Selected only** toggle in pages that don't support value-based filtering in **Discover** [#220624](https://github.com/elastic/kibana/pull/220624)
- Updates default model IDs for **Bedrock** and **OpenAI** connectors in Elastic Security Serverless [#220146](https://github.com/elastic/kibana/pull/220146)
- Integrates AI prompts in Elastic Security Serverless [#216106](https://github.com/elastic/kibana/pull/216106)
- Adds an **ES|QL** control option to the dashboard controls dropdown [#219495](https://github.com/elastic/kibana/pull/219495)
- Enables full-text search in `STATS ... WHERE` **ES|QL** queries [#220691](https://github.com/elastic/kibana/pull/220691)
- Prevents downloading trained models that are already present in other spaces and displays a warning in Machine Learning [#220238](https://github.com/elastic/kibana/pull/220238)
- Adds support for creating and deleting per-project object stores
- Improves HNSW filtered search speed through new heuristic [#126876](https://github.com/elastic/elasticsearch/pull/126876)
- Do not respect `synthetic_source_keep=arrays` if type parses arrays [#127796](https://github.com/elastic/elasticsearch/pull/127796)
- Runs coordinating can_match in `field-caps` [#127734](https://github.com/elastic/elasticsearch/pull/127734)
- Specializes aggregations `AddInput` for each block type [#127582](https://github.com/elastic/elasticsearch/pull/127582)
- Optimizes ordinal inputs in `VALUES` aggregation [#127849](https://github.com/elastic/elasticsearch/pull/127849)
- Pushes down `text ==` and `text !=` [#127355](https://github.com/elastic/elasticsearch/pull/127355)
- Allows full text functions to be used in ES|QL STATS [#125479](https://github.com/elastic/elasticsearch/pull/125479)
- Adds emit time to hash aggregation status [#127988](https://github.com/elastic/elasticsearch/pull/127988)
- Adds Hugging Face Chat Completion support to Inference Plugin [#127254](https://github.com/elastic/elasticsearch/pull/127254)
- Adds ES|QL SAMPLE aggregation function [#127629](https://github.com/elastic/elasticsearch/pull/127629)


### Fixes

- Removes extra icon from map visualization tooltips [#220134](https://github.com/elastic/kibana/pull/220134)
- Fixes color mapping issues for custom ranges and multi-field values in visualizations [#207957](https://github.com/elastic/kibana/pull/207957)
- Fixes layout issues in embeddable dashboard panel headings with descriptions [#219428](https://github.com/elastic/kibana/pull/219428)
- Fixes invalid dashboards incorrectly showing 404 errors instead of validation messages [#211661](https://github.com/elastic/kibana/pull/211661)
- Fixes success message and auto-scroll behavior after adding a panel to a dashboard from the library [#220122](https://github.com/elastic/kibana/pull/220122)
- Fixes drill-down state not saving in by-value **Discover** sessions [#219857](https://github.com/elastic/kibana/pull/219857)
- Marks icons as presentational for accessibility in **Discover** [#219696](https://github.com/elastic/kibana/pull/219696)
- Fixes broken **Span Links** flyout in **Trace Explorer** in Elastic Observability Serverless [#219763](https://github.com/elastic/kibana/pull/219763)
- Prevents undefined errors in **Transaction flyout** in Elastic Observability Serverless [#220224](https://github.com/elastic/kibana/pull/220224)
- Fixes issues with **Processes** query in Elastic Observability Serverless [#220381](https://github.com/elastic/kibana/pull/220381)
- Removes unnecessary index write blocks in Elastic Observability Serverless [#220362](https://github.com/elastic/kibana/pull/220362)
- Improves resilience of API tests in Elastic Observability Serverless [#220503](https://github.com/elastic/kibana/pull/220503)
- Uses update-by-query for `semantic_text` migration in Elastic Observability Serverless [#220255](https://github.com/elastic/kibana/pull/220255)
- Fixes errors in `error_marker.tsx` to support **Mobile Services** in Elastic Observability Serverless [#220424](https://github.com/elastic/kibana/pull/220424)
- Moves from visualization responses to visualization tables in Elastic Security Serverless [#214888](https://github.com/elastic/kibana/pull/214888)
- Prevents risk score search requests from being aborted in Elastic Security Serverless [#219858](https://github.com/elastic/kibana/pull/219858)
- Fixes issue where exceptions list and actions were overwritten during legacy prebuilt rule upgrades in Elastic Security Serverless [#218519](https://github.com/elastic/kibana/pull/218519)
- Fixes incorrect validation for names containing asterisks in **ES|QL** [#219832](https://github.com/elastic/kibana/pull/219832)
- Fixes overridden SSL config in full agent policy advanced YAML for Fleet [#219902](https://github.com/elastic/kibana/pull/219902)
- Reverts enabling `madvise` by default for all builds [#127921](https://github.com/elastic/elasticsearch/pull/127921)
- Changes the handling of passthrough dimenensions [#127752](https://github.com/elastic/elasticsearch/pull/127752)
- Avoids nested docs in Painless execute API [#127991](https://github.com/elastic/elasticsearch/pull/127991)
- Fixes union types in ES|QL cross-cluster search [#128111](https://github.com/elastic/elasticsearch/pull/128111)
- Fixes a bug in `significant_terms` [#127975](https://github.com/elastic/elasticsearch/pull/127975)
- Does not push down filters on the right hand side of an inline join [#127383](https://github.com/elastic/elasticsearch/pull/127383)
- Resolves groupings in aggregate before resolving references to groupings in the aggregations [#127524](https://github.com/elastic/elasticsearch/pull/127524)
- Ensures ordinal builder emits ordinal blocks [#127949](https://github.com/elastic/elasticsearch/pull/127949)
- Keeps `DROP` attributes when resolving field names [#127009](https://github.com/elastic/elasticsearch/pull/127009)
- Skips the validation when retrieving the index mode during reindexing a time series data stream [#127824](https://github.com/elastic/elasticsearch/pull/127824)
- Appends all data to Chat Completion buffer [#127658](https://github.com/elastic/elasticsearch/pull/127658)
- Adds timeout to request for creating inference endpoint [#126805](https://github.com/elastic/elasticsearch/pull/126805)
- Fixes Google Vertex AI Rerank task type location field [#127856](https://github.com/elastic/elasticsearch/pull/127856)


## May 5, 2025


### Features and enhancements

- Adds grouping per row to the ES|QL rule type [#212135](https://github.com/elastic/kibana/pull/212135)
- Adds a compact view on the Monitors overview page in Elastic Observability Serverless [#219060](https://github.com/elastic/kibana/pull/219060)
- Adds backend schema changes for investigation guides in Elastic Observability Serverless [#216377](https://github.com/elastic/kibana/pull/216377)
- Adds the `context.grouping` action variable for the SLO Burn rate and ES|QL rules in Elastic Observability Serverless [#213550](https://github.com/elastic/kibana/pull/213550)
- Updates the styles for the color formatter to appear like a badge in Discover [#189391](https://github.com/elastic/kibana/pull/189391)
- Enhances the handling of missing `service.environment` attributes in Elastic Observability Serverless [#217899](https://github.com/elastic/kibana/pull/217899)
- Adds `logging_level` to the agent central configuration for the EDOT Java agent in Elastic Observability Serverless [#219722](https://github.com/elastic/kibana/pull/219722)
- Updates Kibana MITRE data to `v16.1` [#215026](https://github.com/elastic/kibana/pull/215026)
- Makes the Fleet agents tag filter searchable and sortable [#219639](https://github.com/elastic/kibana/pull/219639)
- Adds logic to exclude the `temperature` parameter from the body request of some OpenAI models [#218887](https://github.com/elastic/kibana/pull/218887)
- Adds the ability to switch between relative and absolute time range in Discover [#218056](https://github.com/elastic/kibana/pull/218056)
- Introduces default retention for failure indices [#127573](https://github.com/elastic/elasticsearch/pull/127573)


### Fixes

- Fixes ignored dynamic templates [#219875](https://github.com/elastic/kibana/pull/219875)

- Syncs the Dashboard ES|QL query and filters with the corresponding one in Visualizations [#218997](https://github.com/elastic/kibana/pull/218997)
- Fixes the option list control, making two requests upon refreshing [#219625](https://github.com/elastic/kibana/pull/219625)
- Ensures that an individual alert is sent per monitor configuration when the "Receive distinct alerts per location" toggle is unchecked in Elastic Observability Serverless [#219291](https://github.com/elastic/kibana/pull/219291)
- Fixes an error that occurred when you interacted with the monitor status rule flyout's numeric controls in Elastic Observability Serverless [#218994](https://github.com/elastic/kibana/pull/218994)
- Fixes an issue where the Observability AI Assistant flyout reopened after navigating to another page URL [#219420](https://github.com/elastic/kibana/pull/219420)
- Fixes an issue with alerts filtering when the service environment was not defined in Elastic Observability Serverless [#219228](https://github.com/elastic/kibana/pull/219228)
- Handles missing `trace` in API response [#219512](https://github.com/elastic/kibana/pull/219512)
- Correctly displays an error message if there are failures when creating anomaly detection jobs [#219364](https://github.com/elastic/kibana/pull/219364)
- Adds optional chaining to prevent undefined error in `custom_link_flyout.tsx` in Elastic Observability Serverless [#219668](https://github.com/elastic/kibana/pull/219668)
- Corrects quotes in ES|QL queries for function arguments in Elastic Observability Serverless [#217680](https://github.com/elastic/kibana/pull/217680)
- Queries alerts using the `alert.start` field in Elastic Observability Serverless [#219651](https://github.com/elastic/kibana/pull/219651)
- Fixes a scroll error for the Rules flyout in Elastic Security Serverless [#218697](https://github.com/elastic/kibana/pull/218697)
- Adds a privilege check for enabling the **Run Engine** button in Elastic Security Serverless  [#213054](https://github.com/elastic/kibana/pull/213054)
- Removes checks for an unused connector role in Elastic Security Serverless [#219358](https://github.com/elastic/kibana/pull/219358)
- Fixes the rule import error message display [#218701](https://github.com/elastic/kibana/pull/218701)
- Fixes the capability required for the SIEM Migrations Topic in Fleet [#219427](https://github.com/elastic/kibana/pull/219427)
- Ensures the ability to change providers without error in Machine learning [#219020](https://github.com/elastic/kibana/pull/219020)
- Fixes broken icons in integrations from the Home plugin [#219206](https://github.com/elastic/kibana/pull/219206)


## April 28, 2025


### Features and enhancements

- Adds the option to use the logical `AND` when filtering Monitors by multiple tags or locations [#217985](https://github.com/elastic/kibana/pull/217985)
- Makes Attack Discovery alerts persistent and searchable [#218906](https://github.com/elastic/kibana/pull/218906)
- Improves edit ReadMe functionality for custom integrations [#215259](https://github.com/elastic/kibana/pull/215259)
- Removes metrics and logs from the `get_service_stats` API [#218346](https://github.com/elastic/kibana/pull/218346)
- Allows you to customize the table tab [#218686](https://github.com/elastic/kibana/pull/218686)
- Enables keyboard navigation for the create annotations form [#217918](https://github.com/elastic/kibana/pull/217918)
- Adds ES|QL random sampling [#125570](https://github.com/elastic/elasticsearch/pull/125570)
- Adds ability to redirect ingestion failures on data streams to a failure store [#126973](https://github.com/elastic/elasticsearch/pull/126973)
- Adds `documents_found` and `values_loaded` [#125631](https://github.com/elastic/elasticsearch/pull/125631)
- Retries shard movements during ES|QL query [#126653](https://github.com/elastic/elasticsearch/pull/126653)
- Pushes more `==` on text fields to Lucene [#126641](https://github.com/elastic/elasticsearch/pull/126641)
- Emits ordinal output block for `VALUES` aggregate [#127201](https://github.com/elastic/elasticsearch/pull/127201)
- Add refresh to put and delete synonyms APIs to wait for synonyms to be accessible and reload analyzers [#126935](https://github.com/elastic/elasticsearch/pull/126935)
- Adds dense vector off-heap stats to node stats and index stats APIs [#126704](https://github.com/elastic/elasticsearch/pull/126704)
- Adds panama vector accelerated optimized scalar quantization [#127118](https://github.com/elastic/elasticsearch/pull/127118)
- Updates tika to 2.9.3 [#127353](https://github.com/elastic/elasticsearch/pull/127353)


### Fixes

- Fixes keyword format in metric visualizations [#218233](https://github.com/elastic/kibana/pull/218233)
- Fixes monitor history histogram and group by location issue [#218550](https://github.com/elastic/kibana/pull/218550)
- Prevents other conditions from changing when you change the condition type of a monitor status rule [#216426](https://github.com/elastic/kibana/pull/216426)
- Filters out null values from `sourceDataStreams` [#218772](https://github.com/elastic/kibana/pull/218772)
- Fixes span url link when `transactionId` is missing in span links [#218232](https://github.com/elastic/kibana/pull/218232)
- Fixes logical `AND` behavior when a filter is removed [#218910](https://github.com/elastic/kibana/pull/218910)
- Fixes a bug that prevented index template creation [#218901](https://github.com/elastic/kibana/pull/218901)
- Prevents unnecessary suggestion requests [#218927](https://github.com/elastic/kibana/pull/218927)
- Uses fields instead of `_source` in the metadata endpoint [#218869](https://github.com/elastic/kibana/pull/218869)
- Fills gaps in table tooltips [#218926](https://github.com/elastic/kibana/pull/218926)
- Makes output and fleet server non-editable for agentless integration policies [#218905](https://github.com/elastic/kibana/pull/218905)
- Improves anomaly charts object safety [#217552](https://github.com/elastic/kibana/pull/217552)
- Fixes title announcements in the details step of the anomaly detection job wizard [#218570](https://github.com/elastic/kibana/pull/218570)
- Fixes incorrect optimization for endpoint artifacts [#216437](https://github.com/elastic/kibana/pull/216437)
- Fixes `vec_caps` to test for OS support too (on x64) [#126911](https://github.com/elastic/elasticsearch/pull/126911)
- Fixes top level knn search with scroll [#126035](https://github.com/elastic/elasticsearch/pull/126035)
- Bypasses competitive iteration in single filter bucket case [#127267](https://github.com/elastic/elasticsearch/pull/127267)
- Temporarily bypasses competitive iteration for filters aggregation [#126956](https://github.com/elastic/elasticsearch/pull/126956)
- Fixes rare terms aggregation false positive [#126884](https://github.com/elastic/elasticsearch/pull/126884)
- Preserves single aggregate when all attributes are pruned [#126397](https://github.com/elastic/elasticsearch/pull/126397)
- Fixes bug in single value query [#127146](https://github.com/elastic/elasticsearch/pull/127146)
- Disables a bugged commit in ES|QL [#127199](https://github.com/elastic/elasticsearch/pull/127199)
- Retains aggregate when grouping [#126598](https://github.com/elastic/elasticsearch/pull/126598)
- Bumps plugin version to release `_metric_names_hash` changes [#126850](https://github.com/elastic/elasticsearch/pull/126850)
- Correctly handle non-integers in nested paths in the remove processor [#127006](https://github.com/elastic/elasticsearch/pull/127006)
- Adds missing onFailure call for inference API start model request [#126930](https://github.com/elastic/elasticsearch/pull/126930)
- Refactors inference request executor to leverage scheduled execution [#126858](https://github.com/elastic/elasticsearch/pull/126858)


## April 21, 2025


### Features and enhancements

- Adds public Maintenance Window APIs for Alerting [#216756](https://github.com/elastic/kibana/pull/216756)
- Enables KQL filter for Elastic Observability Serverless TLS rules [#216973](https://github.com/elastic/kibana/pull/216973)
- Adds drilldown to synthetics stats overview embeddable for Elastic Observability Serverless [#217688](https://github.com/elastic/kibana/pull/217688)
- Updates the Elastic Observability Serverless embeddable view when only one monitor in one location is selected [#218402](https://github.com/elastic/kibana/pull/218402)
- Improves accessibility in the Elastic Observability Serverless create connector flyout [#218426](https://github.com/elastic/kibana/pull/218426)
- Removes double confirmation when deleting conversations in Elastic Observability Serverless [#217991](https://github.com/elastic/kibana/pull/217991)
- APM URLs now encode the service name in Elastic Observability Serverless [#217092](https://github.com/elastic/kibana/pull/217092)
- Adds improvements to the Embeddable Trace Waterfall in Elastic Observability Serverless [#217679](https://github.com/elastic/kibana/pull/217679)
- Updates the highlighted fields in the Elastic Security Serverless overview tab [#216740](https://github.com/elastic/kibana/pull/216740)
- Adds the ability to handle ELASTIC_PROFILER_STACK_TRACE_IDS for apm-profiler integration in Elastic Obserbability Serverless [#217020](https://github.com/elastic/kibana/pull/217020)
- Adds the ability to open links in a new window for Vega visualizations [#216200](https://github.com/elastic/kibana/pull/216200)
- Adds the ability to opt out of event-driven Memory Protection scanning in Elastic Security Serverless advanced policies [#218354](https://github.com/elastic/kibana/pull/218354)
- Replaces the Elastic Security Serverless analyzer sourcerer [#218183](https://github.com/elastic/kibana/pull/218183)
- Enables suggestions for `CHANGE_POINT` command in ES|QL [#218100](https://github.com/elastic/kibana/pull/218100)
- Adds callouts for Fleet breaking changes for integration upgrades [#217257](https://github.com/elastic/kibana/pull/217257)
- Adds support for local `xpack.productDocBase.artifactRepositoryUrl` file path in Machine Learning [#217046](https://github.com/elastic/kibana/pull/217046)
- Adds defaultSolution to spaces configuration [#218360](https://github.com/elastic/kibana/pull/218360)
- Adds support for dots in the role mappings. Dots (.) can be used as part of the role mappings and the groups that are returned by the custom IdPs to match to.


### Fixes

- Fixes allow_hidden usage in the request for fields in Discover [#217628](https://github.com/elastic/kibana/pull/217628)
- Fixes an issue in Discover where keydown event propagation now stops when unified doc tabs are focused [#218300](https://github.com/elastic/kibana/pull/218300)
- Fixes an issue where sync global parameters are now called in the endpoints to add, edit, or delete global params in Elastic Observability Serverless [#216197](https://github.com/elastic/kibana/pull/216197)
- Adds the ability to allow group for ip type fields in Elastic Observability Serverless [#216062](https://github.com/elastic/kibana/pull/216062)
- Fixes the EDOT error summary in Elastic Observability Serverless [#217885](https://github.com/elastic/kibana/pull/217885)
- Fixes test run logs per page in Elastic Observability Serverless [#218458](https://github.com/elastic/kibana/pull/218458)
- Fixes the display results and Visualize query Bedrock error in Elastic Observability Serverless [#218213](https://github.com/elastic/kibana/pull/218213)
- Fixes prebuilt rules force upgrade on Endpoint policy creation in Elastic Security Serverless [#217959](https://github.com/elastic/kibana/pull/217959)
- Fixes related integrations render performance on rule editing pages in Elastic Security Serverless [#217254](https://github.com/elastic/kibana/pull/217254)
- Fixes the broken tooltip suggestions descriptions in ES|QL [#218067](https://github.com/elastic/kibana/pull/218067)
- Adds the ability to retrieve empty columns in ES|QL [#218085](https://github.com/elastic/kibana/pull/218085)
- Fixes an issue in ES|QL where tables with no data would break [#217937](https://github.com/elastic/kibana/pull/217937)
- Fixes the ES|QL editor menus when using Safari [#218167](https://github.com/elastic/kibana/pull/218167)
- Fixes the wrong source validation in case of unknown patterns in ES|QL [#218352](https://github.com/elastic/kibana/pull/218352)
- Fixes vCPU usage message in the Machine Learning start deployment dialog [#218557](https://github.com/elastic/kibana/pull/218557)
- Removes the listing limit warning [#217945](https://github.com/elastic/kibana/pull/217945)
- Fixes an issue where the placeholder in the monaco editor would disappear when a value is set [#217828](https://github.com/elastic/kibana/pull/217828)
- Fixes an issue where the Saved Objects Rotate Encryption Key API would not affect sharable encrypted object types that exist in all spaces [#217625](https://github.com/elastic/kibana/pull/217625)
- Fixes an issue where refreshing multiple tabs when you log out will simultaneously log in successfully [#212148](https://github.com/elastic/kibana/pull/212148)


## April 14, 2025


### Features and enhancements

- Enables archiving of conversations in the Elastic Observability Serverless AI Assistant [#216012](https://github.com/elastic/kibana/pull/216012)
- Moves job and trained model management features into **Stack Management** [#204290](https://github.com/elastic/kibana/pull/204290)
- Adds Engine initialization API to Elastic Security Serverless [#215663](https://github.com/elastic/kibana/pull/215663)
- Allows creating an ES|QL control by entering a question mark (`?`) in the query [#216839](https://github.com/elastic/kibana/pull/216839)
- Improves UI handling of multiple CVEs and package fields [#216411](https://github.com/elastic/kibana/pull/216411)
- Adds support for Windows MSI commands for Fleet and Elastic Agent installations [#217217](https://github.com/elastic/kibana/pull/217217)
- Reuses shared integration policies when duplicating agent policies in Fleet [#217872](https://github.com/elastic/kibana/pull/217872)
- Enables adding badges to all list items in the side navigation except the section header [#217301](https://github.com/elastic/kibana/pull/217301)
- Adds endpoint creation validation to `ElasticsearchInternalService` [#123044](https://github.com/elastic/elasticsearch/pull/123044)
- Adds support for Amazon Bedrock Cohere task settings [#126493](https://github.com/elastic/elasticsearch/pull/126493)
- Enables sort optimization on float and half_float [#126342](https://github.com/elastic/elasticsearch/pull/126342)
- Upgrades to Lucene 10.2.0 [#126594](https://github.com/elastic/elasticsearch/pull/126594)
- Uses `FallbackSyntheticSourceBlockLoader` for text fields [#126237](https://github.com/elastic/elasticsearch/pull/126237)
- Adds block loader from stored field and source for ip field [#126644](https://github.com/elastic/elasticsearch/pull/126644)
- `FileWatchingService` should not throw for missing file [#126264](https://github.com/elastic/elasticsearch/pull/126264)
- Speeds up `TO_IP` [#126338](https://github.com/elastic/elasticsearch/pull/126338)
- Adds list and get query APIs [#124832](https://github.com/elastic/elasticsearch/pull/124832)
- Implments the grammar and logical plan in the `COMPLETION` command in ES|QL [#126319](https://github.com/elastic/elasticsearch/pull/126319)
- Adds heuristics to pick efficient partitioning [#125739](https://github.com/elastic/elasticsearch/pull/125739)


### Fixes

- Fixes error message when previewing index templates used by data streams [#217604](https://github.com/elastic/kibana/pull/217604)
- Wraps text in search bars [#217556](https://github.com/elastic/kibana/pull/217556)
- Adds support for `textBased` layers in ES|QL visualizations [#216358](https://github.com/elastic/kibana/pull/216358)
- Corrects the alert count displayed in **Monitor** details [#216761](https://github.com/elastic/kibana/pull/216761)
- Fixes the **Save visualization** action on the Monitors **Overview** tab [#216695](https://github.com/elastic/kibana/pull/216695)
- Removes direct function calling from the chat input Elastic Observability Serverless AI Assistant [#217359](https://github.com/elastic/kibana/pull/217359)
- Adds missing `aria-label` attributes to some buttons under the Services and Services Groups pages [#217325](https://github.com/elastic/kibana/pull/217325)
- Improves knowledge base installation flow and inference endpoint management [#214133](https://github.com/elastic/kibana/pull/214133)
- Improves `aria-label` for `EuiCodeBlock` on the APM onboarding page [#217292](https://github.com/elastic/kibana/pull/217292)
- Adds `source` and `target` fields to the `Dataset Quality Navigated` event [#217575](https://github.com/elastic/kibana/pull/217575)
- Improves `aria-label` attributes for latency correlations [#217512](https://github.com/elastic/kibana/pull/217512)
- Fixes navigation to the **Search Connectors** page [#217749](https://github.com/elastic/kibana/pull/217749)
- Sorts the **Environment** dropdown alphabetically in the APM UI [#217710](https://github.com/elastic/kibana/pull/217710)
- Ensures the Request Inspector shows accurate request and response data for successful scenarios [#216519](https://github.com/elastic/kibana/pull/216519)
- Fixes the `Change Point Detection` embeddable in dashboards [#217178](https://github.com/elastic/kibana/pull/217178)
- Fixes page crashes caused by the **Use full data** button [#217291](https://github.com/elastic/kibana/pull/217291)
- Filters inference connectors that lack existing endpoints in **Connectors** [#217641](https://github.com/elastic/kibana/pull/217641)
- Fixes focusability and keyboard access issues with the **Export** tab in the **Share this dashboard** modal [#217313](https://github.com/elastic/kibana/pull/217313)
- Fixes LTR rescorer with model alias [#126273](https://github.com/elastic/elasticsearch/pull/126273)
- Fixes bbq quantization algorithm but for differently distributed components [#126778](https://github.com/elastic/elasticsearch/pull/126778)
- Improves resiliency of `UpdateTimeSeriesRangeService` [#126637](https://github.com/elastic/elasticsearch/pull/126637)
- Improves handling of empty response [#125562](https://github.com/elastic/elasticsearch/pull/125562)
- Adds leniency to missing array values in mustache [#126550](https://github.com/elastic/elasticsearch/pull/126550)
- Adds a custom `toString` to `DynamicMap` [#126562](https://github.com/elastic/elasticsearch/pull/126562)
- Fixes Painless return type cast for list shortcut [#126724](https://github.com/elastic/elasticsearch/pull/126724)
- Fails with `500` not `400` for `ValueExtractor` bugs [#126296](https://github.com/elastic/elasticsearch/pull/126296)
- Fixes usage of already released null block in `ValueSourceReaderOperator` [#126411](https://github.com/elastic/elasticsearch/pull/126411)
- Fixes `NULL` handling in `IN` clause [#125832](https://github.com/elastic/elasticsearch/pull/125832)
- Retrieves token text only when necessary in ES|QL [#126578](https://github.com/elastic/elasticsearch/pull/126578)
- `TO_IP` can handle leading zeros [#126532](https://github.com/elastic/elasticsearch/pull/126532)
- Correctly handles nulls in nested paths in the remove processor [#126417](https://github.com/elastic/elasticsearch/pull/126417)
- Fixes ELAND endpoints not updating dimensions [#126537](https://github.com/elastic/elasticsearch/pull/126537)
- Changes `ModelLoaderUtils.split` to return the correct number of chunks and ranges [#126009](https://github.com/elastic/elasticsearch/pull/126009)
- Reverts endpoint creation validation for `ELSER` and `E5` [#126792](https://github.com/elastic/elasticsearch/pull/126792)


## April 7, 2025


### Features and enhancements

- Adds keyboard navigation for drag-and-drop interactions in Dashboards [#208286](https://github.com/elastic/kibana/pull/208286)
- Adds 'Read More' and 'Read Less' functionality to fields in Document view in Discover [#215326](https://github.com/elastic/kibana/pull/215326)
- Injects and extracts tag references in Dashboards [#214788](https://github.com/elastic/kibana/pull/214788)
- Adds an option to User Settings that allows the Kibana interface to display in a high contrast mode [#216242](https://github.com/elastic/kibana/pull/216242)
- Adds a back external link indicator to the side navigation [#215946](https://github.com/elastic/kibana/pull/215946)
- Adds a default metrics dashboard for Node.js open telemetry in Elastic Observability Serverless [#215735](https://github.com/elastic/kibana/pull/215735)
- Replaces Sourcerer with the the Discover Data View picker in Elastic Security Serverless [#210585](https://github.com/elastic/kibana/pull/210585)
- Replaces Sourcerer in the global header in Elastic Security Serverless [#216685](https://github.com/elastic/kibana/pull/216685)
- Handles grouping in multivalue fields in Elastic Security Serverless [#215913](https://github.com/elastic/kibana/pull/215913)
- Adds validation and autocomplete support for the `CHANGE_POINT` command in ES|QL [#216043](https://github.com/elastic/kibana/pull/216043)
- Adds support for aggregrate filtering in the ES|QL editor [#216379](https://github.com/elastic/kibana/pull/216379)
- Changes the agent details last activity value to show the formatted datetime in Fleet [#215531](https://github.com/elastic/kibana/pull/215531)
- Allows SSL configuration to be disabled for the Fleet agent Logstash output [#216216](https://github.com/elastic/kibana/pull/216216)
- Enhances the display for anomaly time function values for Machine Learning [#216142](https://github.com/elastic/kibana/pull/216142)
- Adds Voyage AI and DeepSeek icons for Machine Learning [#216651](https://github.com/elastic/kibana/pull/216651)
- Moves rule settings to a flyout instead of a modal [#216162](https://github.com/elastic/kibana/pull/216162)
- Marks `rescore_vector` as generally available [#126038](https://github.com/elastic/elasticsearch/pull/126038)
- Adds reranker command for ES|QL [#123074](https://github.com/elastic/elasticsearch/pull/123074)
- Uses `FallbackSyntheticSourceBlockLoader` for point and geo_point [#125816](https://github.com/elastic/elasticsearch/pull/125816)
- Infers the score mode to use from the Lucene collector in ES|QL [#125930](https://github.com/elastic/elasticsearch/pull/125930)
- Supports explicit `Z`/`M` attributes using `WKT` geometry [#125896](https://github.com/elastic/elasticsearch/pull/125896)
- Enhances `DATE_TRUNC` with arbitrary intervals [#120302](https://github.com/elastic/elasticsearch/pull/120302)
- Runs `TransportGetSettingsAction` on local node [#126051](https://github.com/elastic/elasticsearch/pull/126051)
- Runs `TransportGetIndexAction` on local node [#125652](https://github.com/elastic/elasticsearch/pull/125652)


### Fixes

- Fixes a race condition in `useBatchedPublishingSubjects` in Dashboards and visualizations [#216399](https://github.com/elastic/kibana/pull/216399)
- Fixes State being dropped when editing visualize embeddables in Dashboards and visualizations [#216901](https://github.com/elastic/kibana/pull/216901)
- Updates the HTTP API response from 201 to 200 in Dashboards and visualizations [#217054](https://github.com/elastic/kibana/pull/217054)
- Fixes an issue where scaling edits weren't saved in Dashboards and visualizations [#217235](https://github.com/elastic/kibana/pull/217235)
- Fixes an issue where the Discover flyout closed when the focus was on filter [#216630](https://github.com/elastic/kibana/pull/216630)
- Fixes the CSV export for ES|QL embeddable in Discover [#216325](https://github.com/elastic/kibana/pull/216325)
- Fixes the JSON view for ES|QL record in DocViewer [#216642](https://github.com/elastic/kibana/pull/216642)
- Adds items count to fields accordion titled `aria-label` in Discover  [#216993](https://github.com/elastic/kibana/pull/216993)
- Makes service inventory icons visible if the `agentName` is returned in Elastic Observability Serverless [#216220](https://github.com/elastic/kibana/pull/216220)
- Changes the TPM abbreviation to trace per minute for screen readers in Elastic Observability Serverless [#216282](https://github.com/elastic/kibana/pull/216282)
- Adds the `aria-label` to the fold traces button in Elastic Observability Serverless [#216485](https://github.com/elastic/kibana/pull/216485)
- Adds the `aria-label` to the technical preview badge in Elastic Observability Serverless [#216483](https://github.com/elastic/kibana/pull/216483)
- Allows only `.ndjson` files when bulk importing to the knowledge base in Elastic Observability Serverless [#215433](https://github.com/elastic/kibana/pull/215433)
- Fixes the span link invalid filter in Elastic Observability Serverless [#215322](https://github.com/elastic/kibana/pull/215322)
- Fixes the missing URL in the transaction summary in Elastic Observability Serverless [#215397](https://github.com/elastic/kibana/pull/215397)
- Fixes the query for transaction marks in Elastic Observability Serverless [#215819](https://github.com/elastic/kibana/pull/215819)
- Updates the `retrieve_elastic_doc` API test in Elastic Observability Serverless [#215237](https://github.com/elastic/kibana/pull/215237)
- Adds error text in the environment filter when the input is invalid in Elastic Observability Serverless [#216782](https://github.com/elastic/kibana/pull/216782)
- Fixes the **Fold/unfold** button in traces waterfall explorer in Elastic Observability Serverless [#216972](https://github.com/elastic/kibana/pull/216972)
- Fixes the alert severity order in Elastic Security Serverless [#215813](https://github.com/elastic/kibana/pull/215813)
- Fixes the error callout placement on the **Entity Store** page's **Engine Status** tab in Elastic Security Serverless [#216228](https://github.com/elastic/kibana/pull/216228)
- Reads `config` from preconfigured connectors in AI Assistant and Attack Discovery in Elastic Security Serverless [#216700](https://github.com/elastic/kibana/pull/216700)
- Fixes bedrock `modelId` encoding in Elastic Security Serverless [#216915](https://github.com/elastic/kibana/pull/216915)
- Fixes the AI Assistant prompt in Elastic Security Serverless [#217058](https://github.com/elastic/kibana/pull/217058)
- Hides "not" operators from the suggestions menu in ES|QL [#216355](https://github.com/elastic/kibana/pull/216355)
- Fixes the CSV report time range when exporting from Discover in ES|QL [#216792](https://github.com/elastic/kibana/pull/216792)
- Fixes unenroll inactive agent tasks if the first set of agents returned is equal to `UNENROLLMENT_BATCH_SIZE` in Fleet [#216283](https://github.com/elastic/kibana/pull/216283)
- Supports integrations having secrets with multiple values in Fleet [#216918](https://github.com/elastic/kibana/pull/216918)
- Adds overlay to the add/edit integration page in Fleet [#217151](https://github.com/elastic/kibana/pull/217151)
- Prevents get datafeeds stats API from returning an error when local tasks are slow to stop [#125477](https://github.com/elastic/elasticsearch/pull/125477)
- Adds bounded window to inference models for rescoring to ensure a positive score range [#125694](https://github.com/elastic/elasticsearch/pull/125694)
- Prevents `ConcurrentModificationException` when updating settings for more than one index [#126077](https://github.com/elastic/elasticsearch/pull/126077)
- Reverts "Allow partial results by default in ES|QL" [#126286](https://github.com/elastic/elasticsearch/pull/126286)
- Fixes `ReplaceMissingFieldsWithNull` [#125764](https://github.com/elastic/elasticsearch/pull/125764)


## March 31, 2025


### Features and enhancements

- Introduced an embeddable trace waterfall visualization in Elastic Observability Serverless [#216098](https://github.com/elastic/kibana/pull/216098)
- Adds support for span links in Elastic Observability Serverless service maps [#215645](https://github.com/elastic/kibana/pull/215645)
- Enables KQL filting for TLS alerting rules in Elastic Observability Serverless [#215110](https://github.com/elastic/kibana/pull/215110)
- Ensures a 404 response is returned only when `screenshot_ref` is truly missing in Elastic Observability Serverless [#215241](https://github.com/elastic/kibana/pull/215241)
- Adds a rule gaps histogram to the Elastic Security Serverless rules dashboard [#214694](https://github.com/elastic/kibana/pull/214694)
- Adds support for multiple CVEs and improves the vulnerability data grid, flyout, and contextual flyout UI in Elastic Security Serverless [#213039](https://github.com/elastic/kibana/pull/213039)
- Updates API key permissions for refreshing data view API for Elastic Security Serverless [#215738](https://github.com/elastic/kibana/pull/215738)
- Adds the ability to limit notes per document instead of globally in Elastic Security Serverless [#214922](https://github.com/elastic/kibana/pull/214922)
- Adds the ability to add badges to subitems in the side navigation [#214854](https://github.com/elastic/kibana/pull/214854)
- Checks if the anomaly results index has been rolled over (#125404) [#125786](https://github.com/elastic/elasticsearch/pull/125786)
- Adds common rerank options to the perform inference API [#125239](https://github.com/elastic/elasticsearch/pull/125239)
- Adds panama implementations of byte-bit and float-bit script operations [#124722](https://github.com/elastic/elasticsearch/pull/124722)
- Allows zero for `rescore_vector.oversample` to indicate by-passing oversample and rescoring [#125599](https://github.com/elastic/elasticsearch/pull/125599)
- Stores arrays offsets for scaled float fields natively with synthetic source [#125793](https://github.com/elastic/elasticsearch/pull/125793)
- Stores arrays offsets for boolean fields natively with synthetic source [#125529](https://github.com/elastic/elasticsearch/pull/125529)
- Stores arrays offsets for unsigned long fields natively with synthetic source [#125709](https://github.com/elastic/elasticsearch/pull/125709)
- Calculates concurrent node limit [#124901](https://github.com/elastic/elasticsearch/pull/124901)
- Takes double parameter markers for identifiers out of snapshot in ES|QL[#125690](https://github.com/elastic/elasticsearch/pull/125690)
- Adds `original_types` to description in unsuppored fields in ES|QL [#124913](https://github.com/elastic/elasticsearch/pull/124913)
- Fixes sorting when `aggregate_metric_double` present in ES|QL [#125191](https://github.com/elastic/elasticsearch/pull/125191)
- Avoids creating `known_fields` for every check in alias [#124690](https://github.com/elastic/elasticsearch/pull/124690)


### Fixes

- Fixes color palette assignment issues in partition charts [#215426](https://github.com/elastic/kibana/pull/215426)
- Adjusts page height for the AI Assistant app in solution views [#215646](https://github.com/elastic/kibana/pull/215646)
- Adds the `aria-label` to latency selector in Elastic Observabiity Serverless service overview [#215644](https://github.com/elastic/kibana/pull/215644)
- Adds the `aria-label` to popover service in Elastic Observabiity Serverless service overview [#215640](https://github.com/elastic/kibana/pull/215640)
- Adds the `aria-label` to "Try our new inventory" button in Elastic Observabiity Serverless [#215633](https://github.com/elastic/kibana/pull/215633)
- Adds the `aria-label` to Transaction type select in Elastic Observabiity Serverless service overview [#216014](https://github.com/elastic/kibana/pull/216014)
- Fixes an issue when selecting monitor frequency [#215823](https://github.com/elastic/kibana/pull/215823)
- Implements the `nameTooltip` API for Elastic Observabiity Serverless dependency tables [#215940](https://github.com/elastic/kibana/pull/215940)
- Fixes a location filter issue in the Elastic Observabiity Serverless status rule executor [#215514](https://github.com/elastic/kibana/pull/215514)
- Consolidates custom Fleet onboarding logic in Elastic Observabiity Serverless [#215561](https://github.com/elastic/kibana/pull/215561)
- Fixes left margin positioning in Elastic Observabiity Serverless waterfall visualizations [#216229](https://github.com/elastic/kibana/pull/216229)
- Corrects risk score table refresh issues in the Elastic Security Serverless Entity Analytics Dashboard [#215472](https://github.com/elastic/kibana/pull/215472)
- Fixes the Elastic Security Serverless host details flyout left panel tabs [#215672](https://github.com/elastic/kibana/pull/215672)
- Fixes an issue where the Entity Store init API did not check for index privileges in Elastic Security Serverless [#215329](https://github.com/elastic/kibana/pull/215329)
- Adds a `manage_ingest_pipeline` privilege check for Risk Engine enablement in Elastic Security Serverless [#215544](https://github.com/elastic/kibana/pull/215544)
- Updates API to dynamically retrieve `spaceID` for Elastic Security Serverless [#216063](https://github.com/elastic/kibana/pull/216063)
- Fixes the visibility of the ES|QL date picker [#214728](https://github.com/elastic/kibana/pull/214728)
- Enables the ES|QL time picker when time parameters are used with `cast` [#215820](https://github.com/elastic/kibana/pull/215820)
- Updates the Fleet minimum package spec version to 2.3 [#214600](https://github.com/elastic/kibana/pull/214600)
- Fixes text overflow and alignment in agent details integration input status in Fleet [#215807](https://github.com/elastic/kibana/pull/215807)
- Fixes pagination in the Anomaly Explorer Anomalies Table for Machine Learning [#214714](https://github.com/elastic/kibana/pull/214714)
- Ensures proper permissions for viewing Machine Learning nodes [#215503](https://github.com/elastic/kibana/pull/215503)
- Adds a custom link color option for the top banner [#214241](https://github.com/elastic/kibana/pull/214241)
- Updates the task state version after execution [#215559](https://github.com/elastic/kibana/pull/215559)
- Returns a conflict status code if the model deployment is stopped by a user [#125204](https://github.com/elastic/elasticsearch/pull/125204)
- Returns appropriate error on null dims update instead of NPE [#125716](https://github.com/elastic/elasticsearch/pull/125716)
- Fixes shard recovery failure due to missing synonyms sets [#125659](https://github.com/elastic/elasticsearch/pull/125659)
- Fixes ES|QL `date nanos`range bug [#125345](https://github.com/elastic/elasticsearch/pull/125345)
- Fixes Lucene push down behavior when a range contains nanos and millis [#125595](https://github.com/elastic/elasticsearch/pull/125595)
- Makes `numberOfChannels` consistent with layout map by removing duplicated `ChannelSet` in ES|QL [#125636](https://github.com/elastic/elasticsearch/pull/125636)


## March 24, 2025


### Features and enhancements

- Enables smoother scrolling in Kibana [#214512](https://github.com/elastic/kibana/pull/214512)
- Adds `context.grouping` action variable in Custom threshold and APM rules [#212895](https://github.com/elastic/kibana/pull/212895)
- Adds the ability to create an APM availability or latency SLO for all services [#214653](https://github.com/elastic/kibana/pull/214653)
- Enables editing central config for EDOT Agents / SDKs [#211468](https://github.com/elastic/kibana/pull/211468)
- Uses Data View name for Rule Data View display [#214495](https://github.com/elastic/kibana/pull/214495)
- Highlights the code examples in our inline docs [#214915](https://github.com/elastic/kibana/pull/214915)
- Updates data feeds for anomaly detection jobs to exclude Elastic Agent and Beats processes [#213927](https://github.com/elastic/kibana/pull/213927)
- Adds Mustache lambdas for alerting action [#213859](https://github.com/elastic/kibana/pull/213859)
- Adds 'page reload' screen reader warning [#214822](https://github.com/elastic/kibana/pull/214822)
- Adds support for spreading a single reserved state across several files instead of a single file to enable projects to be created in one cluster state update instead of several.
- Allows passing several `reserved state` chunks in single process call [#124574](https://github.com/elastic/elasticsearch/pull/124574)
- Leverages scorer supplier in `QueryFeatureExtractor` [#125259](https://github.com/elastic/elasticsearch/pull/125259)
- Uses `FallbackSyntheticSourceBlockLoader` for `shape` and `geo_shape` [#124927](https://github.com/elastic/elasticsearch/pull/124927)
- Stores arrays offsets for numeric fields natively with synthetic source [#124594](https://github.com/elastic/elasticsearch/pull/124594)
- Adds ES|QL slow log [#124094](https://github.com/elastic/elasticsearch/pull/124094)
- Adds ES|QL `ToAggregateMetricDouble` function [#124595](https://github.com/elastic/elasticsearch/pull/124595)
- Reuses child `outputSet` inside the plan where possible in ES|QL [#124611](https://github.com/elastic/elasticsearch/pull/124611)
- Keeps ordinals in ES|QL conversion functions [#125357](https://github.com/elastic/elasticsearch/pull/125357)
- Reindexes data stream indices on different nodes [#125171](https://github.com/elastic/elasticsearch/pull/125171)
- Runs `TransportGetDataStreamLifecycleAction` on local node [#125214](https://github.com/elastic/elasticsearch/pull/125214)
- Runs `TransportGetDataStreamOptionsAction` on local node [#125213](https://github.com/elastic/elasticsearch/pull/125213)


### Fixes

- Fixes color by value for Last value array mode [#213917](https://github.com/elastic/kibana/pull/213917)
- Fixes can edit check [#213887](https://github.com/elastic/kibana/pull/213887)
- Fixes opening a rollup data view in Discover [#214656](https://github.com/elastic/kibana/pull/214656)
- Fixes entry item in waterfall shouldn't be orphan [#214700](https://github.com/elastic/kibana/pull/214700)
- Filters out upstream orphans in waterfall [#214704](https://github.com/elastic/kibana/pull/214704)
- Fixes KB bulk import UI example [#214970](https://github.com/elastic/kibana/pull/214970)
- Ensures that when an SLO is created, its ID is verified across all spaces [#214496](https://github.com/elastic/kibana/pull/214496)
- Fixes contextual insights scoring [#214259](https://github.com/elastic/kibana/pull/214259)
- Prevents `getChildrenGroupedByParentId` from including the parent in the children list [#214957](https://github.com/elastic/kibana/pull/214957)
- Fixes ID overflow bug [#215199](https://github.com/elastic/kibana/pull/215199)
- Removes unnecessary `field service.environment` from top dependency spans endpoint [#215321](https://github.com/elastic/kibana/pull/215321)
- Fixes missing `user_agent` version field and shows it on the trace summary [#215403](https://github.com/elastic/kibana/pull/215403)
- Fixes rule preview works for form's invalid state [#213801](https://github.com/elastic/kibana/pull/213801)
- Fixes session view error on the alerts tab [#214887](https://github.com/elastic/kibana/pull/214887)
- Adds index privileges check to `applyDataViewIndices` [#214803](https://github.com/elastic/kibana/pull/214803)
- Changes the default Risk score lookback period from `30m` to `30d` [#215093](https://github.com/elastic/kibana/pull/215093)
- Fixes issue with alert grouping re-render [#215086](https://github.com/elastic/kibana/pull/215086)
- Limits the `transformID` length to 36 characters [#213405](https://github.com/elastic/kibana/pull/213405)
- Fixes Data view refresh not supporting the `indexPattern` parameter [#215151](https://github.com/elastic/kibana/pull/215151)
- Uses Risk Engine `SavedObject` intead of `localStorage` on the Risk Score web page [#215304](https://github.com/elastic/kibana/pull/215304)
- Fixes autocomplete for comments when there is a space [#214696](https://github.com/elastic/kibana/pull/214696)
- Makes sure that the variables in the editor are always up to date [#214833](https://github.com/elastic/kibana/pull/214833)
- Calculates the query for retrieving the values correctly [#214905](https://github.com/elastic/kibana/pull/214905)
- Fixes overlay in integrations on mobile [#215312](https://github.com/elastic/kibana/pull/215312)
- Fixes chart in single metric anomaly detection wizard [#214837](https://github.com/elastic/kibana/pull/214837)
- Fixes regression that caused the cases actions to disappear from the detections engine alerts table bulk actions menu [#215111](https://github.com/elastic/kibana/pull/215111)
- Changes "Close project" to "Log out" in nav menu in serverless mode [#211463](https://github.com/elastic/kibana/pull/211463)
- Fixes search profiler index reset field when query is changed [#215420](https://github.com/elastic/kibana/pull/215420)
- Fixes `AlibabaCloudSearchCompletionAction` not accepting `ChatCompletionInputs` [#125023](https://github.com/elastic/elasticsearch/pull/125023)
- Sets default similarity for Cohere model to cosine [#125370](https://github.com/elastic/elasticsearch/pull/125370)
- Fixes null pointer exception in rolling over unknown target and returns 404 [#125352](https://github.com/elastic/elasticsearch/pull/125352)
- Lets terms run in global ords mode with no match [#124782](https://github.com/elastic/elasticsearch/pull/124782)
- Fixes scoring for non-full text functions in ES|QL [#124540](https://github.com/elastic/elasticsearch/pull/124540)
- Aligns `RENAME` behavior with `EVAL` for sequential processing [#122250](https://github.com/elastic/elasticsearch/pull/122250)
- Fails in `AggregateFunction` when `LogicPlan` is not an `Aggregate` [#124446](https://github.com/elastic/elasticsearch/pull/124446)
- Fixes LTR query feature with phrases (and two-phase) queries [#125103](https://github.com/elastic/elasticsearch/pull/125103)


## March 17, 2025


### Features and enhancements

- Enables read-only editor mode in Lens to explore panel configuration [#208554](https://github.com/elastic/kibana/pull/208554)
- Allows you to share Observability AI Assistant conversations [#211854](https://github.com/elastic/kibana/pull/211854)
- Adds context-aware logic to Logs view in Discover [#211176](https://github.com/elastic/kibana/pull/211176)
- Replaces the Alerts status filter with filter controls [#198495](https://github.com/elastic/kibana/pull/198495)
- Adds SSL fields to agent binary source settings [#213211](https://github.com/elastic/kibana/pull/213211)
- Allows users to create a snooze schedule for rules using API [#210584](https://github.com/elastic/kibana/pull/210584)
- Splits up the top dependencies API for improved speed and response size [#211441](https://github.com/elastic/kibana/pull/211441)
- Adds working default metrics dashboard for Python OTel [#213599](https://github.com/elastic/kibana/pull/213599)
- Includes spaceID in SLI documents [#214278](https://github.com/elastic/kibana/pull/214278)
- Adds support for the `MV_EXPAND` command with the ES|QL rule type [#212675](https://github.com/elastic/kibana/pull/212675)
- Enables endpoint actions for events [#206857](https://github.com/elastic/kibana/pull/206857)
- Introduces GA support for the [`semantic_text`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/semantic-text) field type on Elastic Cloud Serverless
- Adds the ability for users to [customize prebuilt rules](https://github.com/elastic/kibana/issues/174168). Users can modify most rule parameters, export and import prebuilt rules — including customized ones — and upgrade prebuilt rules while retaining customization settings [#212761](https://github.com/elastic/kibana/pull/212761)
- Adds `vector_rescore` parameter as a quantized index type option [#124581](https://github.com/elastic/elasticsearch/pull/124581)
- Indicates when errors represent timeouts [#124936](https://github.com/elastic/elasticsearch/pull/124936)
- Runs `TransportGetMappingsAction` on local node [#122921](https://github.com/elastic/elasticsearch/pull/122921)
- Runs `TransportGetDataStreamsAction` on local node [#122852](https://github.com/elastic/elasticsearch/pull/122852)
- Speeds up block serialization [#124394](https://github.com/elastic/elasticsearch/pull/124394)
- Adds initial grammar and planning for `RRF` (snapshot) [#123396](https://github.com/elastic/elasticsearch/pull/123396)
- Pushes down `StartsWith` and `EndsWith` functions to Lucene [#123381](https://github.com/elastic/elasticsearch/pull/123381)
- Adds scoring for full text functions disjunctions in ES|QL [#121793](https://github.com/elastic/elasticsearch/pull/121793)
- Supports `::date` in inline cast [#123460](https://github.com/elastic/elasticsearch/pull/123460)
- Adds pragma to load from stored fields [#122891](https://github.com/elastic/elasticsearch/pull/122891)
- Removes page alignment in exchange sink [#124610](https://github.com/elastic/elasticsearch/pull/124610)
- Reports failures on partial results [#124823](https://github.com/elastic/elasticsearch/pull/124823)
- Adds double parameter markers for identifiers in ES|QL [#122459](https://github.com/elastic/elasticsearch/pull/122459)
- Includes failures in partial response [#124929](https://github.com/elastic/elasticsearch/pull/124929)
- Propagates product use case HTTP header to EIS [#124025](https://github.com/elastic/elasticsearch/pull/124025)
- Integrates with DeepSeek API [#122218](https://github.com/elastic/elasticsearch/pull/122218)
- Adds `max.chunks` to `EmbeddingRequestChunker` to prevent out of memory error [#123150](https://github.com/elastic/elasticsearch/pull/123150)
- Upgrades AWS v2 SDK to 2.30.38 [#124738](https://github.com/elastic/elasticsearch/pull/124738)
- Exposes `input_type` option at root level for `text_embedding` task type in the perform inference API [#122638](https://github.com/elastic/elasticsearch/pull/122638)
- Adds `ModelRegistryMetadata` to cluster state [#121106](https://github.com/elastic/elasticsearch/pull/121106)
- Improves downsample performance by buffering docids and doing bulk processing [#124477](https://github.com/elastic/elasticsearch/pull/124477)
- Improves rolling up metrics [#124739](https://github.com/elastic/elasticsearch/pull/124739)


### Fixes

- Fixes a bug with ServiceNow where users could not create the connector from the UI form using OAuth [#213658](https://github.com/elastic/kibana/pull/213658)
- Prevents unnecessary re-render when switching between View and Edit modes [#213902](https://github.com/elastic/kibana/pull/213902)
- Adds `event-annotation-group` to saved object privileges for dashboards [#212926](https://github.com/elastic/kibana/pull/212926)
- Makes the **Inspect configuration** button permanently visible [#213619](https://github.com/elastic/kibana/pull/213619)
- Fixes service maps not building paths when the trace's root transaction has a `parent.id` [#212998](https://github.com/elastic/kibana/pull/212998)
- Fixes span links with OTel data [#212806](https://github.com/elastic/kibana/pull/212806)
- Makes Kibana retrieval namespace-specific [#213505](https://github.com/elastic/kibana/pull/213505)
- Ensures semantic queries contribute to scoring when retrieving knowledge from search connectors [#213870](https://github.com/elastic/kibana/pull/213870)
- Passes `telemetry.sdk` data when loading a dashboard [#214356](https://github.com/elastic/kibana/pull/214356)
- Fixes `checkPrivilege` to query with indices [#214002](https://github.com/elastic/kibana/pull/214002)
- Adds support for rollup data views that reference aliases [#212592](https://github.com/elastic/kibana/pull/212592)
- Fixes an issue with the **Save** button not working when editing event filters [#213805](https://github.com/elastic/kibana/pull/213805)
- Fixes dragged elements becoming invisible when dragging-and-dropping in Lens [#213928](https://github.com/elastic/kibana/pull/213928)
- Fixes alignment of the Alerts table in the Rule Preview panel [#214028](https://github.com/elastic/kibana/pull/214028)
- Fixes Bedrock defaulting region to `us-east-1` [#214251](https://github.com/elastic/kibana/pull/214251)
- Fixes an issue with the Agent binary download field being blank when a policy uses the default download source [#214360](https://github.com/elastic/kibana/pull/214360)
- Fixes navigation issues with alert previews [#213455](https://github.com/elastic/kibana/pull/213455)
- Fixes an issue with changing the width of a Timeline column width bug [#214178](https://github.com/elastic/kibana/pull/214178)
- Reworks the `enforce_registry_filters` advanced option in Elastic Defend to align with Endpoint [#214106](https://github.com/elastic/kibana/pull/214106)
- Ensures cell actions are initialized in Event Rendered view and fixes cell action handling for nested event renderers [#212721](https://github.com/elastic/kibana/pull/212721)
- Supports `date_nanos` in `BUCKET` in the ES|QL editor [#213319](https://github.com/elastic/kibana/pull/213319)
- Fixes appearance of warnings in the ES|QL editor [#213685](https://github.com/elastic/kibana/pull/213685)
- Makes the Apply time range switch visible in the Job selection flyout when opened from the Anomaly Explorer [#213382](https://github.com/elastic/kibana/pull/213382)
- Migrates `model_version` to `model_id` when parsing persistent elser inference endpoints [#124769](https://github.com/elastic/elasticsearch/pull/124769)
- Avoids unnecessary calls to `Task#getDescription` in model download [#124527](https://github.com/elastic/elasticsearch/pull/124527)
- Provides `model_size_stats` as soon as an anomaly detection job is opened [#124638](https://github.com/elastic/elasticsearch/pull/124638)
- Restores `TextSimilarityRankBuilder` XContent output [#124564](https://github.com/elastic/elasticsearch/pull/124564)
- Lets `MLTQuery` throw `IllegalArgumentException` (IAE) when no analyzer is set [#124662](https://github.com/elastic/elasticsearch/pull/124662)
- Restores V8 REST compatibility around highlight `force_source` parameter [#124873](https://github.com/elastic/elasticsearch/pull/124873)
- Fixes EQL double invoking `listener` [#124918](https://github.com/elastic/elasticsearch/pull/124918)
- Uses lazy collection copying during node transform [#124424](https://github.com/elastic/elasticsearch/pull/124424)
- Catches parsing exception [#124958](https://github.com/elastic/elasticsearch/pull/124958)
- Changes the order of the optimization rules [#124335](https://github.com/elastic/elasticsearch/pull/124335)
- `TO_LOWER` processes all values [#124676](https://github.com/elastic/elasticsearch/pull/124676)
- Improves error message for `(` and `[` in ES|QL [#124177](https://github.com/elastic/elasticsearch/pull/124177)
- Fixes geoip databases index access after system feature migration [#124604](https://github.com/elastic/elasticsearch/pull/124604)
- Avoids reading unnecessary dimension values when downsampling [#124451](https://github.com/elastic/elasticsearch/pull/124451)
- Merges template mappings properly during validation [#124784](https://github.com/elastic/elasticsearch/pull/124784)


## March 10, 2025


### Features and enhancements

- Adds an improved rule form for the Create Rule flyout in Elastic Observability Serverless [#206685](https://github.com/elastic/kibana/pull/206685)
- Resolves duplicate conversations in Elastic Observability Serverless [#208044](https://github.com/elastic/kibana/pull/208044)
- Splits the SLO Details view from the Overview page in Elastic Observability Serverless [#212826](https://github.com/elastic/kibana/pull/212826)
- Adds the reason message to the rules recovery context in Elastic Observability Serverless [#211411](https://github.com/elastic/kibana/pull/211411)
- Runtime metrics dashboards now support different ingest paths in Elastic Observability Serverless [#211822](https://github.com/elastic/kibana/pull/211822)
- Adds SSL options for Fleet Server hosts settings in Fleet [#208091](https://github.com/elastic/kibana/pull/208091)
- Introduces globe projection for Dashboards and visualizations [#212437](https://github.com/elastic/kibana/pull/212437)
- Registers a custom integrations search provider in Fleet [#213013](https://github.com/elastic/kibana/pull/213013)
- Adds support for searchAfter and PIT (point-in-time) parameters in the Get Agents List API in Fleet [#213486](https://github.com/elastic/kibana/pull/213486)
- Adds support for specifying embedding type to Jina AI service settings [#121548](https://github.com/elastic/elasticsearch/pull/121548)
- Adds basic implementations of float-byte script comparisons [#122381](https://github.com/elastic/elasticsearch/pull/122381)
- Adds optional parameters to QSTR ES|QL function [#121787](https://github.com/elastic/elasticsearch/pull/121787)
- Enables synthetic recovery source by default when synthetic source is enabled.
  Using synthetic recovery source significantly improves indexing performance compared to regular recovery source [#122615](https://github.com/elastic/elasticsearch/pull/122615)
- Uses `FallbackSyntheticSourceBlockLoader` for boolean and date fields [#124050](https://github.com/elastic/elasticsearch/pull/124050)
- Fixes `Driver` status iterations and `cpuTime` [#123290](https://github.com/elastic/elasticsearch/pull/123290)
- Allows skipping shards with `_tier` and `_index` in ES|QL [#123728](https://github.com/elastic/elasticsearch/pull/123728)
- Introduces `allow_partial_results` setting in ES|QL [#122890](https://github.com/elastic/elasticsearch/pull/122890)
- Adds index mode to get data stream API [#122486](https://github.com/elastic/elasticsearch/pull/122486)
- Retries ILM async action after reindexing data stream [#124149](https://github.com/elastic/elasticsearch/pull/124149)
- Sets cause on create index request in create from action [#124363](https://github.com/elastic/elasticsearch/pull/124363)


### Fixes

- Fixes an issue where Korean characters were split into two characters with a space in between when typing in the options list search input in Dashboards and visualizations [#213164](https://github.com/elastic/kibana/pull/213164)
- Prevents crashes when editing a Lens chart with a by-reference annotation layer in Dashboards and visualizations [#213090](https://github.com/elastic/kibana/pull/213090)
- Improves instructions for the summarize function in Elastic Observability Serverless [#212936](https://github.com/elastic/kibana/pull/212936)
- Fixes a "Product Documentation function not available" error in Elastic Observability Serverless [#212676](https://github.com/elastic/kibana/pull/212676)
- Fixes conversation tests in Elastic Observability Serverless [#213338](https://github.com/elastic/kibana/pull/213338)
- Allows wildcard filters in SLO queries in Elastic Observability Serverless [#213119](https://github.com/elastic/kibana/pull/213119)
- Fixes missing summary data in error samples in Elastic Observability Serverless [#213430](https://github.com/elastic/kibana/pull/213430)
- Fixes a failing test: Stateful Observability - Deployment-agnostic A… in Elastic Observability Serverless [#213530](https://github.com/elastic/kibana/pull/213530)
- Reduces the review rule upgrade endpoint response size in Elastic Security Serverless [#211045](https://github.com/elastic/kibana/pull/211045)
- Refactors conversation pagination in Elastic Security Serverless [#211831](https://github.com/elastic/kibana/pull/211831)
- Fixes alert insights color order in Elastic Security Serverless [#212980](https://github.com/elastic/kibana/pull/212980)
- Prevents empty conversation IDs in the chat/complete route in Elastic Security Serverless [#213049](https://github.com/elastic/kibana/pull/213049)
- Fixes issues with unstructured syslog flow in Elastic Security Serverless [#213042](https://github.com/elastic/kibana/pull/213042)
- Adds bulkGetUserProfiles privilege to Security Feature in Elastic Security Serverless [#211824](https://github.com/elastic/kibana/pull/211824)
- Fixes a Risk Score Insufficient Privileges warning due to missing cluster privileges in Elastic Security Serverless [#212405](https://github.com/elastic/kibana/pull/212405)
- Updates Bedrock prompts in Elastic Security Serverless [#213160](https://github.com/elastic/kibana/pull/213160)
- Adds organizationId and projectId OpenAI headers, along with support for arbitrary headers in Elastic Security Serverless [#213117](https://github.com/elastic/kibana/pull/213117)
- Ensures dataview selections persist reliably in timeline for Elastic Security Serverless [#211343](https://github.com/elastic/kibana/pull/211343)
- Fixes incorrect validation when a named parameter was used as a function in ES|QL [#213355](https://github.com/elastic/kibana/pull/213355)
- Fixes incorrect overall swim lane height in Machine Learning [#213245](https://github.com/elastic/kibana/pull/213245)
- Prevented a crash when applying a filter in the Machine Learning anomaly table [#213075](https://github.com/elastic/kibana/pull/213075)
- Fixes suppressed alerts alignment in the alert flyout in Elastic Security Serverless [#213029](https://github.com/elastic/kibana/pull/213029)
- Fixes an issue in solution project navigation where panels sometimes failed to toggle closed [#211852](https://github.com/elastic/kibana/pull/211852)
- Updates wording for options in the sortBy dropdown component [#206464](https://github.com/elastic/kibana/pull/206464)
- Allows EU hooks hostname in the Torq connector for Elastic Security Serverless [#212563](https://github.com/elastic/kibana/pull/212563)
- Retries on streaming errors [#123076](https://github.com/elastic/elasticsearch/pull/123076)
- Fixes output stream ordering in `InferenceActionProxy` [#124225](https://github.com/elastic/elasticsearch/pull/124225)
- Prevents `ShardBulkInferenceActionFilter` from unwrapping or rewrappring `ESExceptions` [#123890](https://github.com/elastic/elasticsearch/pull/123890)
- Adjusts exception thrown when unable to load hunspell dictionary [#123743](https://github.com/elastic/elasticsearch/pull/123743)
- Avoids serializing empty _source fields in mappings [#122606](https://github.com/elastic/elasticsearch/pull/122606)
- Fixes function registry concurrency issues on constructor [#123492](https://github.com/elastic/elasticsearch/pull/123492)
- Disables concurrency when top_hits sorts on anything but `_score` [#123610](https://github.com/elastic/elasticsearch/pull/123610)
- Avoids over collecting in `LIMIT` or Lucene Operator [#123296](https://github.com/elastic/elasticsearch/pull/123296)
- Ensures non-zero row size in `EstimatesRowSize` [#122762](https://github.com/elastic/elasticsearch/pull/122762)
- Uses a must boolean statement when pushing down to Lucene when scoring is also needed [#124001](https://github.com/elastic/elasticsearch/pull/124001)
- Revives some more of `inlinestats` functionality [#123589](https://github.com/elastic/elasticsearch/pull/123589)
- Avoids hoarding cluster state references during rollover [#124107](https://github.com/elastic/elasticsearch/pull/124107)


## March 3, 2025


### Features and enhancements

- Introduces a background task that streamlines the upgrade process for agentless deployments in Elastic Security Serverless [#207143](https://github.com/elastic/kibana/pull/207143)
- Improves asset inventory onboarding with better context integration in Elastic Security Serverless [#212315](https://github.com/elastic/kibana/pull/212315)
- Adds syntax highlighting for working with ES|QL queries in Elastic Observability Serverless [#212669](https://github.com/elastic/kibana/pull/212669)
- Updates the delete confirmation modal in Elastic Observability Serverless [#212695](https://github.com/elastic/kibana/pull/212695)
- Removes the enablement check in PUT /api/streams/{id} for classic streams [#212289](https://github.com/elastic/kibana/pull/212289)


### Fixes

- Fixes issues affecting popularity scores in Discover [#211201](https://github.com/elastic/kibana/pull/211201)
- Corrects sorting behavior in the profiler storage explorer for Elastic Observability Serverless [#212583](https://github.com/elastic/kibana/pull/212583)
- Adds a loader to prevent flickering in the KB settings tab in Elastic Observability Serverless [#212678](https://github.com/elastic/kibana/pull/212678)
- Resolves incorrect enable button behavior in the Entity Store modal in Elastic Security Serverless [#212078](https://github.com/elastic/kibana/pull/212078)
- Converts the isolate host action into a standalone flyout in Elastic Security Serverless [#211853](https://github.com/elastic/kibana/pull/211853)
- Ensures model responses are correctly persisted to the chosen conversation ID in Elastic Security Serverless [#212122](https://github.com/elastic/kibana/pull/212122)
- Corrects image resizing issues for xpack.security.loginAssistanceMessage in Elastic Security Serverless [#212035](https://github.com/elastic/kibana/pull/212035)
- Fixes automatic import to correctly generate pipelines for parsing CSV files with special characters in Elastic Security Serverless column names [#212513](https://github.com/elastic/kibana/pull/212513)
- Fixes validation issues for empty EQL queries in Elastic Security Serverless [#212117](https://github.com/elastic/kibana/pull/212117)
- Resolves dual hover actions in the table tab in Elastic Security Serverless [#212316](https://github.com/elastic/kibana/pull/212316)
- Updates structured log processing to support multiple log types in Elastic Security Serverless [#212611](https://github.com/elastic/kibana/pull/212611)
- Ensures the delete model dialog prevents accidental multiple clicks in Machine Learning [#211580](https://github.com/elastic/kibana/pull/211580)


## February 24, 2025


### Features and enhancements

- Exposes SSL options for Elasticsearch and remote Elasticsearch outputs in the UI [#208745](https://github.com/elastic/kibana/pull/208745)
- Displays a warning and a tooltip for the _score column in the Discover grid [#211013](https://github.com/elastic/kibana/pull/211013)
- Allows `Command/Ctrl` click for the "New" action in the top navigation [#210982](https://github.com/elastic/kibana/pull/210982)
- Adds the ability for a user to create an API Key in synthetics settings that applies only to specified space(s) [#211816](https://github.com/elastic/kibana/pull/211816)
- Adds "unassigned" as an asset criticality level for bulk_upload [#208884](https://github.com/elastic/kibana/pull/208884)
- Sets the Enable visualizations in flyout advanced setting to "On" by default [#211319](https://github.com/elastic/kibana/pull/211319)
- Preserves user-made chart configurations when changing the query if the actions are compatible with the current chart, such as adding a "where" filter or switching compatible chart types [#210780](https://github.com/elastic/kibana/pull/210780)
- Adds effects when clicking the **Favorite** button in the list of dashboards and ES|QL queries, and adds the button to breadcrumb trails [#201596](https://github.com/elastic/kibana/pull/201596)
- Enables `/api/streams/{id}/_group` endpoints for GroupStreams [#210114](https://github.com/elastic/kibana/pull/210114)
- Adds endpoint creation validation to `ElasticInferenceService` [#117642](https://github.com/elastic/elasticsearch/pull/117642)
- Adds integration for VoyageAI embeddings and rerank models [#122134](https://github.com/elastic/elasticsearch/pull/122134)
- Optionally allows text similarity reranking to fail [#121784](https://github.com/elastic/elasticsearch/pull/121784)
- Stores arrays offsets for ip fields natively with synthetic source [#122999](https://github.com/elastic/elasticsearch/pull/122999)
- Uses `FallbackSyntheticSourceBlockLoader` for `unsigned_long` and `scaled_float` fields [#122637](https://github.com/elastic/elasticsearch/pull/122637)
- Stores arrays offsets for keyword fields natively with synthetic source [#113757](https://github.com/elastic/elasticsearch/pull/113757)
- Supports partial results in cross-cluster search in ES|QL [#122708](https://github.com/elastic/elasticsearch/pull/122708)
- Renders `aggregate_metric_double` in ES|QL [#122660](https://github.com/elastic/elasticsearch/pull/122660)
- Adds initial grammar and changes for `FORK` (snapshot) [#121948](https://github.com/elastic/elasticsearch/pull/121948)
- Allows setting the `type` in the reroute processor [#122409](https://github.com/elastic/elasticsearch/pull/122409)


### Fixes

- Fixes Discover session embeddable drilldown [#211678](https://github.com/elastic/kibana/pull/211678)
- Passes system message to inferenceCliente.chatComplete [#211263](https://github.com/elastic/kibana/pull/211263)
- Ensures system message is passed to the inference plugin [#209773](https://github.com/elastic/kibana/pull/209773)
- Adds automatic re-indexing when encountering a semantic_text bug [#210386](https://github.com/elastic/kibana/pull/210386)
- Removes unnecessary breadcrumbs in profiling [#211081](https://github.com/elastic/kibana/pull/211081)
- Adds minHeight to profiler flamegraphs [#210443](https://github.com/elastic/kibana/pull/210443)
- Adds system message in copy conversation JSON payload [#212009](https://github.com/elastic/kibana/pull/212009)
- Changes the confirmation message after RiskScore Saved Object configuration is updated [#211372](https://github.com/elastic/kibana/pull/211372)
- Adds a no data message in the flyout when an analyzer is not enabled [#211981](https://github.com/elastic/kibana/pull/211981)
- Fixes the Fleet **Save and continue** button [#211563](https://github.com/elastic/kibana/pull/211563)
- Suggests triple quotes when the user selects the KQL / QSTR [#211457](https://github.com/elastic/kibana/pull/211457)
- Adds remote cluster instructions for syncing integrations [#211997](https://github.com/elastic/kibana/pull/211997)
- Allows deploying a model after a failed deployment in Machine Learning [#211459](https://github.com/elastic/kibana/pull/211459)
- Ensures the members array is unique for GroupStreamDefinitions [#210089](https://github.com/elastic/kibana/pull/210089)
- Improves function search for easier navigation and discovery [#210437](https://github.com/elastic/kibana/pull/210437)
- Updates to allow using Cohere binary embedding response in semantic search queries [#121827](https://github.com/elastic/elasticsearch/pull/121827)
- Adds enterprise license check to inference action for semantic text fields [#122293](https://github.com/elastic/elasticsearch/pull/122293)
- Adds `ElasticInferenceServiceCompletionServiceSettings` [#123155](https://github.com/elastic/elasticsearch/pull/123155)
- Sets Connect Timeout to 5s [#123272](https://github.com/elastic/elasticsearch/pull/123272)
- Uses ordered maps for `PipelineConfiguration` xcontent deserialization [#123403](https://github.com/elastic/elasticsearch/pull/123403)
- Fixes redact processor arraycopy bug [#122640](https://github.com/elastic/elasticsearch/pull/122640)
- Adds `_metric_names_hash` field to OTel metric mappings [#120952](https://github.com/elastic/elasticsearch/pull/120952)
- Updates the deprecation info API to not warn about system indices and data streams [#122951](https://github.com/elastic/elasticsearch/pull/122951)
- Registers `IngestGeoIpMetadata` as a `NamedXContent` [#123079](https://github.com/elastic/elasticsearch/pull/123079)
- Updates `TransportRolloverAction.checkBlock` so that non-write-index blocks do not prevent data stream rollover [#122905](https://github.com/elastic/elasticsearch/pull/122905)
- Uses representative count as `event.success_count` in APM data if available [#119995](https://github.com/elastic/elasticsearch/pull/119995)
- Fixes geoip databases index access after system feature migration [#122938](https://github.com/elastic/elasticsearch/pull/122938)
- Uses min node version to guard injecting settings in logs provider [#123005](https://github.com/elastic/elasticsearch/pull/123005)
- Fixes stale data in synthetic source for string stored field [#123105](https://github.com/elastic/elasticsearch/pull/123105)
- Speeds up `VALUES` for many buckets [#123073](https://github.com/elastic/elasticsearch/pull/123073)
- Fixes early termination in `LuceneSourceOperator` [#123197](https://github.com/elastic/elasticsearch/pull/123197)
- Adds support to `VALUES` aggregation for spatial types [#122886](https://github.com/elastic/elasticsearch/pull/122886)
- Fixes precision of `scaled_float` field values retrieved from stored source [#122586](https://github.com/elastic/elasticsearch/pull/122586)
- Adds implicit numeric casting for `CASE`,`GREATEST`, and `LEAST` in ES|QL [#122601](https://github.com/elastic/elasticsearch/pull/122601)
- Removes duplicated nested commands [#123085](https://github.com/elastic/elasticsearch/pull/123085)
- Fixes functions emitting warnings with no source [#122821](https://github.com/elastic/elasticsearch/pull/122821)


## February 17, 2025


### Features and enhancements

- Adds alert status management to the AI Assistant connector [#203729](https://github.com/elastic/kibana/pull/203729)
- Enables the new Borealis theme [#210468](https://github.com/elastic/kibana/pull/210468)
- Applies compact Display options Popover layout [#210180](https://github.com/elastic/kibana/pull/210180)
- Increases search timeout toast lifetime to 1 week [#210576](https://github.com/elastic/kibana/pull/210576)
- Improves performance in dependencies endpoints to prevent high CPU usage [#209999](https://github.com/elastic/kibana/pull/209999)
- Adds "Logs" tab to mobile services [#209944](https://github.com/elastic/kibana/pull/209944)
- Adds "All logs" data view to the Classic navigation [#209042](https://github.com/elastic/kibana/pull/209042)
- Changes default to "native" function calling if the connector configuration is not exposed [#210455](https://github.com/elastic/kibana/pull/210455)
- Updates entity insight badge to open entity flyouts [#208287](https://github.com/elastic/kibana/pull/208287)
- Standardizes actions in Alerts KPI visualizations [#206340](https://github.com/elastic/kibana/pull/206340)
- Allows the creation of dynamic aggregations controls for ES|QL charts [#210170](https://github.com/elastic/kibana/pull/210170)
- Fixes the values control FT [#211159](https://github.com/elastic/kibana/pull/211159)
- Trained models: Replaces the **Download** button by extending the deploy action [#205699](https://github.com/elastic/kibana/pull/205699)
- Adds the useCustomDragHandle property [#210463](https://github.com/elastic/kibana/pull/210463)
- Upcoming removal of SMS multifactor authentication method. In October, we made multifactor authentication mandatory for all users. As an additional security measure, the SMS MFA method will be removed in April. If you’re still using SMS, you will be prompted to set up a more secure MFA method, and your registered SMS MFA devices will be automatically deleted from Elastic Cloud.
- Adds ELSER default endpoint for EIS [#122066](https://github.com/elastic/elasticsearch/pull/122066)
- Renames `model_id` property to `model` in EIS sparse inference API request body [#122272](https://github.com/elastic/elasticsearch/pull/122272)
- Uses `FallbackSyntheticSourceBlockLoader` for number fields [#122280](https://github.com/elastic/elasticsearch/pull/122280)
- Enables the use of nested field type with `index.mode=time_series` [#122224](https://github.com/elastic/elasticsearch/pull/122224)
- Adds initial support for unmapped fields [#119886](https://github.com/elastic/elasticsearch/pull/119886)
- Supports partial results in ES|QL [#121942](https://github.com/elastic/elasticsearch/pull/121942)


### Fixes

- Fixes an issue where clicking on the name badge for a synthetics monitor on an SLO details page would lead to a page that failed to load monitor details [#210695](https://github.com/elastic/kibana/pull/210695)
- Fixes an issue where the popover in the rules page may get stuck when being clicked more than once [#208996](https://github.com/elastic/kibana/pull/208996)
- Fixes an error in the cases list when the case assignee is an empty string [#209973](https://github.com/elastic/kibana/pull/209973)
- Fixes an issue with assigning color mappings when multiple layers are defined [#208571](https://github.com/elastic/kibana/pull/208571)
- Fixes an issue where behind text colors were not correctly assigned, such as in Pie, Treemap, and Mosaic charts [#209632](https://github.com/elastic/kibana/pull/209632)
- Fixes an issue where dynamic coloring has been disabled from Last value aggregation types [#209110](https://github.com/elastic/kibana/pull/209110)
- Fixes panel styles [#210113](https://github.com/elastic/kibana/pull/210113)
- Fixes incorrectly serialized searchSessionId attribute [#210765](https://github.com/elastic/kibana/pull/210765)
- Fixes the "Save to library" action that could break the chart panel [#210125](https://github.com/elastic/kibana/pull/210125)
- Fixes link settings not persisting [#211041](https://github.com/elastic/kibana/pull/211041)
- Fixes "Untitled" export title when exporting CSV from a dashboard [#210143](https://github.com/elastic/kibana/pull/210143)
- Missing items in the trace waterfall shouldn't break it entirely [#210210](https://github.com/elastic/kibana/pull/210210)
- Removes unused `error.id` in `getErrorGroupMainStatistics` queries [#210613](https://github.com/elastic/kibana/pull/210613)
- Fixes connector test in MKI [#211235](https://github.com/elastic/kibana/pull/211235)
- Fixes an issue where clicking a link in the host/user flyout did not refresh the details panel [#209863](https://github.com/elastic/kibana/pull/209863)
- Makes 7.x signals/alerts compatible with 8.18 alerts UI [#209936](https://github.com/elastic/kibana/pull/209936)
- Handles empty categorization results from LLM [#210420](https://github.com/elastic/kibana/pull/210420)
- Remembers page index in Rule Updates table [#209537](https://github.com/elastic/kibana/pull/209537)
- Adds concurrency limits and request throttling to prebuilt rule routes [#209551](https://github.com/elastic/kibana/pull/209551)
- Fixes package name validation on the Datastream page [#210770](https://github.com/elastic/kibana/pull/210770)
- Makes entity store description more generic [#209130](https://github.com/elastic/kibana/pull/209130)
- Deletes 'critical services' count from the Entity Analytics Dashboard header [#210827](https://github.com/elastic/kibana/pull/210827)
- Disables sorting IP ranges in value list modal [#210922](https://github.com/elastic/kibana/pull/210922)
- Updates entity store copies [#210991](https://github.com/elastic/kibana/pull/210991)
- Fixes generated name for integration title [#210916](https://github.com/elastic/kibana/pull/210916)
- Fixes formatting and sorting for custom ES|QL vars [#209360](https://github.com/elastic/kibana/pull/209360)
- Fixes WHERE autocomplete with MATCH before LIMIT [#210607](https://github.com/elastic/kibana/pull/210607)
- Updates install snippets to include all platforms [#210249](https://github.com/elastic/kibana/pull/210249)
- Updates component templates with deprecated setting [#210200](https://github.com/elastic/kibana/pull/210200)
- Hides saved query controls in AIOps [#210556](https://github.com/elastic/kibana/pull/210556)
- Fixes unattended transforms in integration packages not automatically restarting after reauthorizing [#210217](https://github.com/elastic/kibana/pull/210217)
- Reinstates switch to support generating public URLs for embed when supported [#207383](https://github.com/elastic/kibana/pull/207383)
- Provides a fallback view to recover from Stack Alerts page filters bar errors [#209559](https://github.com/elastic/kibana/pull/209559)
- Adds Knn vector rescoring to sort score docs [#122653](https://github.com/elastic/elasticsearch/pull/122653)
- Fixes synthetic source bug that would mishandle nested dense_vector fields [#122425](https://github.com/elastic/elasticsearch/pull/122425)
- Fixes issues that prevent using search-only snapshots for indices that use index sorting. This includes LogsDB and time series indices [#122199](https://github.com/elastic/elasticsearch/pull/122199)
- Fixes listener leak in exchange service [#122417](https://github.com/elastic/elasticsearch/pull/122417)
- Revives `inlinestats` [#122257](https://github.com/elastic/elasticsearch/pull/122257)
- Deduplicates `IngestStats` and `IngestStats.Stats` identity records when deserializing [#122496](https://github.com/elastic/elasticsearch/pull/122496)
- Canonicalizes processor names and types in `IngestStats` [#122610](https://github.com/elastic/elasticsearch/pull/122610)
- Ensures removal of index blocks does not leave key with null value [#122246](https://github.com/elastic/elasticsearch/pull/122246)
- Fixes serialising the inference update request [#122278](https://github.com/elastic/elasticsearch/pull/122278)
- If the transform is configured to write to an alias as its destination index,
  when the `delete_dest_index parameter` is set to true, the delete API will now
  delete the write index backing the alias [#122074](https://github.com/elastic/elasticsearch/pull/122074)


## February 10, 2025


### Features and enhancements

- Handles multiple prompt for the Rule connector [#209221](https://github.com/elastic/kibana/pull/209221)
- Adds `max_file_size_bytes` advanced option to malware for all operating systems [#209541](https://github.com/elastic/kibana/pull/209541)
- Introducs GroupStreams [#208126](https://github.com/elastic/kibana/pull/208126)
- Service example added to entity store upload [#209023](https://github.com/elastic/kibana/pull/209023)
- Updates the bucket_span for ML jobs in the security_host module [#209663](https://github.com/elastic/kibana/pull/209663)
- Improves handling for operator-defined role mappings [#208710](https://github.com/elastic/kibana/pull/208710)
- Adds object_src directive to Content-Security-Policy-Report-Only header [#209306](https://github.com/elastic/kibana/pull/209306)


### Fixes

- Fixes highlight for HJSON [#208858](https://github.com/elastic/kibana/pull/208858)
- Disables pointer events on drag + resize [#208647](https://github.com/elastic/kibana/pull/208647)
- Restores show missing dataView error message in case of missing datasource [#208363](https://github.com/elastic/kibana/pull/208363)
- Fixes issue with Amsterdam theme where charts render with the incorrect background color [#209595](https://github.com/elastic/kibana/pull/209595)
- Fixes an issue in Lens Table where a split-by metric on a terms rendered incorrect colors in table cells [#208623](https://github.com/elastic/kibana/pull/208623)
- Forces return 0 on empty buckets on count if null flag is disabled [#207308](https://github.com/elastic/kibana/pull/207308)
- Fixes all embeddables rebuilt on refresh [#209677](https://github.com/elastic/kibana/pull/209677)
- Fixes using data view runtime fields during rule execution for the custom threshold rule [#209133](https://github.com/elastic/kibana/pull/209133)
- Fixes running processes that were missing from the processes table [#209076](https://github.com/elastic/kibana/pull/209076)
- Fixes missing exception stack trace [#208577](https://github.com/elastic/kibana/pull/208577)
- Fixes the preview chart in the Custom Threshold rule creation form when the field name has slashes [#209263](https://github.com/elastic/kibana/pull/209263)
- Display No Data in Threshold breached component [#209561](https://github.com/elastic/kibana/pull/209561)
- Fixes an issue where APM charts were rendered without required transaction type or service name, causing excessive alerts to appear [#209552](https://github.com/elastic/kibana/pull/209552)
- Fixes bug that caused issues with loading SLOs by status, SLI type, or instance id [#209910](https://github.com/elastic/kibana/pull/209910)
- Updates colors in the AI Assistant icon [#210233](https://github.com/elastic/kibana/pull/210233)
- Updates the simulate function calling setting to support "auto" [#209628](https://github.com/elastic/kibana/pull/209628)
- Fixes structured log template to use single quotes [#209736](https://github.com/elastic/kibana/pull/209736)
- Fixes ES|QL alert on alert [#208894](https://github.com/elastic/kibana/pull/208894)
- Fixes issue with multiple IP addresses in strings [#209475](https://github.com/elastic/kibana/pull/209475)
- Keeps the histogram config on time change [#208053](https://github.com/elastic/kibana/pull/208053)
- WHERE replacement ranges correctly generated for every case [#209684](https://github.com/elastic/kibana/pull/209684)
- Updates removed parameters of the Fleet -> Logstash output configurations [#210115](https://github.com/elastic/kibana/pull/210115)
- Fixes log rate analysis, change point detection, and pattern analysis embeddables not respecting filters from Dashboard's controls [#210039](https://github.com/elastic/kibana/pull/210039)


## February 3, 2025


### Features and enhancements

- Rework saved query privileges [#202863](https://github.com/elastic/kibana/pull/202863)
- In-table search [#206454](https://github.com/elastic/kibana/pull/206454)
- Refactor RowHeightSettings component to EUI layout [#203606](https://github.com/elastic/kibana/pull/203606)
- Chat history details in conversation list [#207426](https://github.com/elastic/kibana/pull/207426)
- Cases assignees sub feature [#201654](https://github.com/elastic/kibana/pull/201654)
- Adds preview logged requests for new terms, threshold, query, ML rule types [#203320](https://github.com/elastic/kibana/pull/203320)
- Adds in-text citations to security solution AI assistant responses [#206683](https://github.com/elastic/kibana/pull/206683)
- Remove Tech preview badge for GA [#208523](https://github.com/elastic/kibana/pull/208523)
- Adds new View job detail flyouts for Anomaly detection and Data Frame Analytics [#207141](https://github.com/elastic/kibana/pull/207141)
- Adds a default "All logs" temporary data view in the Observability Solution view [#205991](https://github.com/elastic/kibana/pull/205991)
- Adds Knowledge Base entries API [#206407](https://github.com/elastic/kibana/pull/206407)
- Adds Kibana Support for Security AI Prompts Integration [#207138](https://github.com/elastic/kibana/pull/207138)
- Changes to support event.ingested as a configurable timestamp field for init and enable endpoints [#208201](https://github.com/elastic/kibana/pull/208201)
- Adds Spaces column to Anomaly Detection, Data Frame Analytics and Trained Models management pages [#206696](https://github.com/elastic/kibana/pull/206696)
- Adds simple flyout based file upload to Search [#206864](https://github.com/elastic/kibana/pull/206864)
- Bump kube-stack Helm chart onboarding version [#208217](https://github.com/elastic/kibana/pull/208217)
- Log deprecated api usages [#207904](https://github.com/elastic/kibana/pull/207904)
- Added support for human readable name attribute for saved objects audit events [#206644](https://github.com/elastic/kibana/pull/206644)
- Enhanced Role management to manage larger number of roles by adding server side filtering, pagination and querying [#194630](https://github.com/elastic/kibana/pull/194630)
- Added Entity Store data view refresh task [#208543](https://github.com/elastic/kibana/pull/208543)
- Increase maximum Osquery timeout to 24 hours [#207276](https://github.com/elastic/kibana/pull/207276)


### Fixes

- Remove use of fr unit [#208437](https://github.com/elastic/kibana/pull/208437)
- Fixes load more request size [#207901](https://github.com/elastic/kibana/pull/207901)
- Persist runPastTimeout setting [#208611](https://github.com/elastic/kibana/pull/208611)
- Allow panel to extend past viewport on resize [#208828](https://github.com/elastic/kibana/pull/208828)
- Knowledge base install updates [#208250](https://github.com/elastic/kibana/pull/208250)
- Fixes conversations test in MKI [#208649](https://github.com/elastic/kibana/pull/208649)
- Fixes ping heatmap regression when Inspect flag is turned off [#208726](https://github.com/elastic/kibana/pull/208726)
- Fixes monitor status rule for empty kql query results [#208922](https://github.com/elastic/kibana/pull/208922)
- Fixes multiple flyouts [#209158](https://github.com/elastic/kibana/pull/209158)
- Adds missing fields to input manifest templates [#208768](https://github.com/elastic/kibana/pull/208768)
- "Select a Connector" popup does not show up after the user selects any connector and then cancels it from Endpoint Insights [#208969](https://github.com/elastic/kibana/pull/208969)
- Logs shard failures for eql event queries on rule details page and in event log [#207396](https://github.com/elastic/kibana/pull/207396)
- Adds filter to entity definitions schema [#208588](https://github.com/elastic/kibana/pull/208588)
- Fixes missing ecs mappings [#209057](https://github.com/elastic/kibana/pull/209057)
- Apply the timerange to the fields fetch in the editor [#208490](https://github.com/elastic/kibana/pull/208490)
- Update java.ts - removing serverless link [#204571](https://github.com/elastic/kibana/pull/204571)


## January 27, 2025


### Features and enhancements

- Breaks out timeline and note privileges in Elastic Security Serverless [#201780](https://github.com/elastic/kibana/pull/201780)
- Adds service enrichment to the detection engine in Elastic Security Serverless [#206582](https://github.com/elastic/kibana/pull/206582)
- Updates the Entity Store Dashboard to prompt for the Service Entity Type in Elastic Security Serverless [#207336](https://github.com/elastic/kibana/pull/207336)
- Adds enrichPolicyExecutionInterval to entity enablement and initialization APIs in Elastic Security Serverless [#207374](https://github.com/elastic/kibana/pull/207374)
- Introduces a lookback period configuration for the Entity Store in Elastic Security Serverless [#206421](https://github.com/elastic/kibana/pull/206421)
- Allows pre-configured connectors to opt into exposing their configurations by setting exposeConfig in Alerting [#207654](https://github.com/elastic/kibana/pull/207654)
- Adds selector syntax support to log source profiles in Elastic Observability Serverless [#206937](https://github.com/elastic/kibana/pull/206937)
- Displays stack traces in the logs overview tab in Elastic Observability Serverless [#204521](https://github.com/elastic/kibana/pull/204521)
- Enables the use of the rule form to create rules in Elastic Observability Serverless [#206774](https://github.com/elastic/kibana/pull/206774)
- Checks only read privileges of existing indices during rule execution in Elastic Security Serverless [#177658](https://github.com/elastic/kibana/pull/177658)
- Updates KNN search and query template autocompletion in Elasticsearch Serverless [#207187](https://github.com/elastic/kibana/pull/207187)
- Updates JSON schemas for code editors in Machine Learning [#207706](https://github.com/elastic/kibana/pull/207706)
- Reindexes the .kibana_security_session_1 index to the 8.x format in Security [#204097](https://github.com/elastic/kibana/pull/204097)
- Disables `prompt=login` and sign out of Okta before initiating SSO. Fixes an issue when using organization SAML SSO where users are required to re-authenticate with the external IdP due to ForceAuthn=true being sent in SAML requests. SAML requests will now send `ForceAuthn=false`.


### Fixes

- Fixes editing alerts filters for multi-consumer rule types in Alerting [#206848](https://github.com/elastic/kibana/pull/206848)
- Resolves an issue where Chrome was no longer hidden for reports in Dashboards and Visualizations [#206988](https://github.com/elastic/kibana/pull/206988)
- Updates library transforms and duplicate functionality in Dashboards and Visualizations [#206140](https://github.com/elastic/kibana/pull/206140)
- Fixes an issue where drag previews are now absolutely positioned in Dashboards and Visualizations [#208247](https://github.com/elastic/kibana/pull/208247)
- Fixes an issue where an accessible label now appears on the range slider in Dashboards and Visualizations [#205308](https://github.com/elastic/kibana/pull/205308)
- Fixes a dropdown label sync issue when sorting by "Type" [#206424](https://github.com/elastic/kibana/pull/206424)
- Fixes an access bug related to user instructions in Elastic Observability Serverless [#207069](https://github.com/elastic/kibana/pull/207069)
- Fixes the Open Explore in Discover link to open in a new tab in Elastic Observability Serverless [#207346](https://github.com/elastic/kibana/pull/207346)
- Returns an empty object for tool arguments when none are provided in Elastic Observability Serverless [#207943](https://github.com/elastic/kibana/pull/207943)
- Ensures similar cases count is not fetched without the proper license in Elastic Security Serverless [#207220](https://github.com/elastic/kibana/pull/207220)
- Fixes table leading actions to use standardized colors in Elastic Security Serverless [#207743](https://github.com/elastic/kibana/pull/207743)
- Adds missing fields to the AWS S3 manifest in Elastic Security Serverless [#208080](https://github.com/elastic/kibana/pull/208080)
- Prevents redundant requests when loading Discover sessions and toggling chart visibility in ES|QL [#206699](https://github.com/elastic/kibana/pull/206699)
- Fixes a UI error when agents move to an orphaned state in Fleet [#207746](https://github.com/elastic/kibana/pull/207746)
- Restricts non-local Elasticsearch output types for agentless integrations and policies in Fleet [#207296](https://github.com/elastic/kibana/pull/207296)
- Fixes table responsiveness in the Notifications feature of Machine Learning [#206956](https://github.com/elastic/kibana/pull/206956)


## January 13, 2025


### Features and enhancements

- Adds last alert status change to Elastic Security Serverless flyout [#205224](https://github.com/elastic/kibana/pull/205224)
- Case templates are now GA [#205940](https://github.com/elastic/kibana/pull/205940)
- Adds format to JSON messages in Elastic Observability Serverless Logs profile [#205666](https://github.com/elastic/kibana/pull/205666)
- Adds inference connector in Elastic Security Serverless AI features [#204505](https://github.com/elastic/kibana/pull/204505)
- Adds inference connector for Auto Import in Elastic Security Serverless [#206111](https://github.com/elastic/kibana/pull/206111)
- Adds Feature Flag Support for Cloud Security Posture Plugin in Elastic Security Serverless [#205438](https://github.com/elastic/kibana/pull/205438)
- Adds the ability to sync Machine Learning saved objects to all spaces [#202175](https://github.com/elastic/kibana/pull/202175)
- Improves messages for recovered alerts in Machine Learning Transforms [#205721](https://github.com/elastic/kibana/pull/205721)
- Introduces new deployment performance metrics charts. AutoOps provides aggregate metrics at the cluster level for key performance indicators. The data is tier-based, offering users a comprehensive understanding of each tier and the entire cluster.
- Deprecates Cloud Defend billing alerts. Following the deprecation of Cloud Defend in Serverless, removes the billing logic associated with the feature.


### Fixes

- Fixes an issue where "KEEP" columns are not applied after an Elasticsearch error in Discover [#205833](https://github.com/elastic/kibana/pull/205833)
- Resolves padding issues in the document comparison table in Discover [#205984](https://github.com/elastic/kibana/pull/205984)
- Fixes a bug affecting bulk imports for the knowledge base in Elastic Observability Serverless [#205075](https://github.com/elastic/kibana/pull/205075)
- Enhances the Find API by adding cursor-based pagination (search_after) as an alternative to offset-based pagination [#203712](https://github.com/elastic/kibana/pull/203712)
- Updates Elastic Observability Serverless to use architecture-specific Elser models [#205851](https://github.com/elastic/kibana/pull/205851)
- Fixes dynamic batching in the timeline for Elastic Security Serverless [#204034](https://github.com/elastic/kibana/pull/204034)
- Resolves a race condition bug in Elastic Security Serverless related to OpenAI errors [#205665](https://github.com/elastic/kibana/pull/205665)
- Improves the integration display by ensuring all policies are listed in Elastic Security Serverless [#205103](https://github.com/elastic/kibana/pull/205103)
- Renames color variables in the user interface for better clarity and consistency [#204908](https://github.com/elastic/kibana/pull/204908)
- Allows editor suggestions to remain visible when the inline documentation flyout is open in ES|QL [#206064](https://github.com/elastic/kibana/pull/206064)
- Ensures the same time range is applied to documents and the histogram in ES|QL [#204694](https://github.com/elastic/kibana/pull/204694)
- Fixes validation for the "required" field in multi-text input fields in Fleet [#205768](https://github.com/elastic/kibana/pull/205768)
- Fixes timeout issues for bulk actions in Fleet [#205735](https://github.com/elastic/kibana/pull/205735)
- Handles invalid RRule parameters to prevent infinite loops in alerts [#205650](https://github.com/elastic/kibana/pull/205650)
- Fixes privileges display for features and sub-features requiring "All Spaces" permissions in Fleet [#204402](https://github.com/elastic/kibana/pull/204402)
- Prevents password managers from modifying disabled input fields [#204269](https://github.com/elastic/kibana/pull/204269)
- Updates the listing control in the user interface [#205914](https://github.com/elastic/kibana/pull/205914)
- Improves consistency in the help dropdown design [#206280](https://github.com/elastic/kibana/pull/206280)


## January 6, 2025


### Features and enhancements

- Introduces case observables in Elastic Security Serverless [#190237](https://github.com/elastic/kibana/pull/190237)
- Adds a JSON field called "additional fields" to ServiceNow cases when sent using connector, containing the internal names of the ServiceNow table columns [#201948](https://github.com/elastic/kibana/pull/201948)
- Adds the ability to configure the appearance color mode to sync dark mode with the system value [#203406](https://github.com/elastic/kibana/pull/203406)
- Makes the "Copy" action visible on cell hover in Discover [#204744](https://github.com/elastic/kibana/pull/204744)
- Updates the EnablementModalCallout name to AdditionalChargesMessage in Elastic Security Serverless [#203061](https://github.com/elastic/kibana/pull/203061)
- Adds more control over which Elastic Security Serverless alerts in Attack Discovery are included as context to the large language model [#205070](https://github.com/elastic/kibana/pull/205070)
- Adds a consistent layout and other UI enhancements for machine learning pages [#203813](https://github.com/elastic/kibana/pull/203813)


### Fixes

- Fixes an issue that caused dashboards to lag when dragging the time slider [#201885](https://github.com/elastic/kibana/pull/201885)
- Updates the CloudFormation template to the latest version and adjusts the documentation to reflect the use of a single Firehose stream created by the new template [#204185](https://github.com/elastic/kibana/pull/204185)
- Fixes Integration and Datastream name validation in Elastic Security Serverless [#204943](https://github.com/elastic/kibana/pull/204943)
- Fixes an issue in the Automatic Import process where there is now inclusion of the @timestamp field in ECS field mappings whenever possible [#204931](https://github.com/elastic/kibana/pull/204931)
- Allows Automatic Import to safely parse Painless field names that are not valid Painless identifiers in if contexts [#205220](https://github.com/elastic/kibana/pull/205220)
- Aligns the Box Native Connector configuration fields with the source of truth in the connectors codebase, correcting mismatches and removing unused configurations [#203241](https://github.com/elastic/kibana/pull/203241)
- Fixes the "Show all agent tags" option in Fleet when the agent list is filtered [#205163](https://github.com/elastic/kibana/pull/205163)
- Updates the Results Explorer flyout footer buttons alignment in Data Frame Analytics [#204735](https://github.com/elastic/kibana/pull/204735)
- Adds a missing space between lines in the Data Frame Analytics delete job modal [#204732](https://github.com/elastic/kibana/pull/204732)
- Fixes an issue where the **Refresh** button in the Anomaly Detection Datafeed counts table was unresponsive [#204625](https://github.com/elastic/kibana/pull/204625)
- Fixes the inference timeout check in File Upload [#204722](https://github.com/elastic/kibana/pull/204722)
- Fixes the side bar navigation for the Data Visualizer [#205170](https://github.com/elastic/kibana/pull/205170)


## December 16, 2024


### Features and enhancements

- Optimizes the Kibana Trained Models API [#200977](https://github.com/elastic/kibana/pull/200977)
- Adds a Create Case action to the Log rate analysis page [#201549](https://github.com/elastic/kibana/pull/201549)
- Improves AI Assistant’s response quality by giving it access to Elastic’s product documentation [#199694](https://github.com/elastic/kibana/pull/199694)
- Adds support for suppressing EQL sequence alerts [#189725](https://github.com/elastic/kibana/pull/189725)
- Adds an Advanced settings section to the SLO form [#200822](https://github.com/elastic/kibana/pull/200822)
- Adds a new sub-feature privilege under Synthetics and Uptime Can manage private locations [#201100](https://github.com/elastic/kibana/pull/201100)


### Fixes

- Fixes point visibility regression [#202358](https://github.com/elastic/kibana/pull/202358)
- Improves help text of creator and view count features on dashboard listing page [#202488](https://github.com/elastic/kibana/pull/202488)
- Highlights matching field values when performing a KQL search on a keyword field [#201952](https://github.com/elastic/kibana/pull/201952)
- Supports "Inspect" in saved search embeddables [#202947](https://github.com/elastic/kibana/pull/202947)
- Fixes your ability to clear the user-specific system prompt [#202279](https://github.com/elastic/kibana/pull/202279)
- Fixes error when opening rule flyout [#202386](https://github.com/elastic/kibana/pull/202386)
- Fixes to Ops Genie as a default connector [#201923](https://github.com/elastic/kibana/pull/201923)
- Fixes actions on charts [#202443](https://github.com/elastic/kibana/pull/202443)
- Adds flyout to table view in Infrastructure Inventory [#202646](https://github.com/elastic/kibana/pull/202646)
- Fixes service names with spaces not being URL encoded properly for context.viewInAppUrl [#202890](https://github.com/elastic/kibana/pull/202890)
- Allows access query logic to handle user ID and name conditions [#202833](https://github.com/elastic/kibana/pull/202833)
- Fixes APM rule error message for invalid KQL filter [#203096](https://github.com/elastic/kibana/pull/203096)
- Rejects CEF logs from Automatic Import and redirects you to the CEF integration instead [#201792](https://github.com/elastic/kibana/pull/201792)
- Updates the install rules title and message [#202226](https://github.com/elastic/kibana/pull/202226)
- Fixes error on second entity engine init API call [#202903](https://github.com/elastic/kibana/pull/202903)
- Restricts unsupported log formats [#202994](https://github.com/elastic/kibana/pull/202994)
- Removes errors related to Enterprise Search nodes [#202437](https://github.com/elastic/kibana/pull/202437)
- Improves web crawler name consistency [#202738](https://github.com/elastic/kibana/pull/202738)
- Fixes editor cursor jumpiness [#202389](https://github.com/elastic/kibana/pull/202389)
- Fixes rollover datastreams on subobjects mapper exception [#202689](https://github.com/elastic/kibana/pull/202689)
- Fixes spaces sync to retrieve 10,000 trained models [#202712](https://github.com/elastic/kibana/pull/202712)
- Fixes log rate analysis embeddable error on the Alerts page [#203093](https://github.com/elastic/kibana/pull/203093)
- Fixes Slack API connectors not displayed under Slack connector type when adding new connector to rule [#202315](https://github.com/elastic/kibana/pull/202315)


## December 9, 2024


### Features and enhancements

- Elastic Observability Serverless adds a new sub-feature for managing private locations [#201100](https://github.com/elastic/kibana/pull/201100)
- Elastic Observability Serverless adds the ability to configure SLO advanced settings from the UI [#200822](https://github.com/elastic/kibana/pull/200822)
- Elastic Security Serverless adds support for suppressing EQL sequence alerts [#189725](https://github.com/elastic/kibana/pull/189725)
- Elastic Security Serverless adds a /trained_models_list endpoint to retrieve complete data for the Trained Model UI [#200977](https://github.com/elastic/kibana/pull/200977)
- Machine Learning adds an action to include log rate analysis in a case [#199694](https://github.com/elastic/kibana/pull/199694)
- Machine Learning enhances the Kibana API to optimize trained models [#201549](https://github.com/elastic/kibana/pull/201549)


### Fixes

- Fixes Slack API connectors not being displayed under the Slack connector type when adding a new connector to a rule in Alerting [#202315](https://github.com/elastic/kibana/pull/202315)
- Fixes point visibility regression in dashboard visualizations [#202358](https://github.com/elastic/kibana/pull/202358)
- Improves help text for creator and view count features on the Dashboard listing page [#202488](https://github.com/elastic/kibana/pull/202488)
- Highlights matching field values when performing a KQL search on a keyword field in Discover [#201952](https://github.com/elastic/kibana/pull/201952)
- Adds support for the Inspect option in saved search embeddables in Discover [#202947](https://github.com/elastic/kibana/pull/202947)
- Enables the ability to clear user-specific system prompts in Elastic Observability Serverless [#202279](https://github.com/elastic/kibana/pull/202279)
- Fixes an error when opening the rule flyout in Elastic Observability Serverless [#202386](https://github.com/elastic/kibana/pull/202386)
- Improves handling of Opsgenie as the default connector in Elastic Observability Serverless [#201923](https://github.com/elastic/kibana/pull/201923)
- Fixes issues with actions on charts in Elastic Observability Serverless [#202443](https://github.com/elastic/kibana/pull/202443)
- Adds a flyout to the table view in Infrastructure Inventory in Elastic Observability Serverless [#202646](https://github.com/elastic/kibana/pull/202646)
- Fixes service names with spaces not being URL-encoded properly for `{{context.viewInAppUrl}}` in Elastic Observability Serverless [#202890](https://github.com/elastic/kibana/pull/202890)
- Enhances access query logic to handle user ID and name conditions in Elastic Observability Serverless [#202833](https://github.com/elastic/kibana/pull/202833)
- Fixes an APM rule error message when a KQL filter is invalid in Elastic Observability Serverless [#203096](https://github.com/elastic/kibana/pull/203096)
- Restricts and rejects CEF logs in automatic import and redirects them to the CEF integration in Elastic Security Serverless [#201792](https://github.com/elastic/kibana/pull/201792)
- Updates the copy of the install rules title and message in Elastic Security Serverless [#202226](https://github.com/elastic/kibana/pull/202226)
- Clears errors on the second entity engine initialization API call in Elastic Security Serverless [#202903](https://github.com/elastic/kibana/pull/202903)
- Restricts unsupported log formats in Elastic Security Serverless [#202994](https://github.com/elastic/kibana/pull/202994)
- Removes errors related to Enterprise Search nodes in Elasticsearch Serverless [#202437](https://github.com/elastic/kibana/pull/202437)
- Ensures consistency in web crawler naming in Elasticsearch Serverless [#202738](https://github.com/elastic/kibana/pull/202738)
- Fixes editor cursor jumpiness in ES|QL [#202389](https://github.com/elastic/kibana/pull/202389)
- Implements rollover of data streams on subobject mapper exceptions in Fleet [#202689](https://github.com/elastic/kibana/pull/202689)
- Fixes trained models to retrieve up to 10,000 models when spaces are synced in Machine Learning [#202712](https://github.com/elastic/kibana/pull/202712)
- Fixes a Log Rate Analysis embeddable error on the Alerts page in AiOps [#203093](https://github.com/elastic/kibana/pull/203093)


## December 3, 2024


### Features and enhancements

- Adds tabs for Import Entities and Engine Status to the Entity Store [#201235](https://github.com/elastic/kibana/pull/201235)
- Adds status tracking for agentless integrations to Fleet [#199567](https://github.com/elastic/kibana/pull/199567)
- Adds a new machine learning module that can detect anomalous activity in host-based logs [#195582](https://github.com/elastic/kibana/pull/195582)
- Allows custom Mapbox Vector Tile sources to style map layers and provide custom legends [#200656](https://github.com/elastic/kibana/pull/200656)
- Excludes stale SLOs from counts of healthy and violated SLOs [#201027](https://github.com/elastic/kibana/pull/201027)
- Adds a "Continue without adding integrations" message to the Elastic Security Dashboards page that takes you to the Entity Analytics dashboard [#201363](https://github.com/elastic/kibana/pull/201363)
- Displays visualization descriptions under their titles [#198816](https://github.com/elastic/kibana/pull/198816)


### Fixes

- Hides the **Clear** button when no filters are selected [#200177](https://github.com/elastic/kibana/pull/200177)
- Fixes a mismatch between how wildcards were handled in previews versus actual rule executions [#201553](https://github.com/elastic/kibana/pull/201553)
- Fixes incorrect Y-axis and hover values in the Service Inventory’s Log rate chart [#201361](https://github.com/elastic/kibana/pull/201361)
- Disables the **Add note** button in the alert details flyout for users who lack privileges [#201707](https://github.com/elastic/kibana/pull/201707)
- Fixes the descriptions of threshold rules that use cardinality [#201162](https://github.com/elastic/kibana/pull/201162)
- Disables the **Install All** button on the Add Elastic Rules page when rules are installing [#201731](https://github.com/elastic/kibana/pull/201731)
- Reintroduces a data usage warning on the Entity Analytics Enablement modal [#201920](https://github.com/elastic/kibana/pull/201920)
- Improves accessibility for the Create a connector page [#201590](https://github.com/elastic/kibana/pull/201590)
- Fixes a bug that could cause Elastic Agents to get stuck updating during scheduled upgrades [#202126](https://github.com/elastic/kibana/pull/202126)
- Fixes a bug related to starting machine learning deployments with autoscaling and no active nodes [#201256](https://github.com/elastic/kibana/pull/201256)
- Initializes saved objects when the Trained Model page loads [#201426](https://github.com/elastic/kibana/pull/201426)
- Fixes the display of deployment stats for unallocated deployments of machine learning models [#202005](https://github.com/elastic/kibana/pull/202005)
- Enables the solution type search for instant deployments [#201688](https://github.com/elastic/kibana/pull/201688)
- Improves the consistency of alert counts across different views [#202188](https://github.com/elastic/kibana/pull/202188)