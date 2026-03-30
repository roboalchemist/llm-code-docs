# Source: https://docs.fiddler.ai/changelog/release-notes/product-releases.md

# Product Releases

### Release 26.4 Notes

*February 24, 2026*

#### What's New and Improved

**Fiddler LangGraph SDK 1.4.0: Decorator and Manual Instrumentation**

The Fiddler LangGraph SDK (1.4.0) introduces decorator-based and manual instrumentation modes alongside the existing `LangGraphInstrumentor` auto-instrumentation, giving you fine-grained control over trace structure and metadata for custom application logic and non-LangGraph components.

Key additions include the `@trace()` decorator, context managers for explicit span control, typed span wrappers with semantic helpers, and a global `get_client()` singleton.

For the full changelog, see the [LangGraph SDK 1.4.0 release notes](https://docs.fiddler.ai/changelog/langgraph-sdk#id-1.4.0). For implementation guides and code examples, see the [LangGraph SDK integration guide](https://app.gitbook.com/s/kcq97TxAnbTVaNJOQHbQ/agentic-ai-and-llm-frameworks/agentic-ai/langgraph-sdk) and the [SDK API reference](https://app.gitbook.com/s/rsvU8AIQ2ZL9arerribd/fiddler-langgraph-sdk).

**GenAI Application Page Redesign**

The GenAI Applications page now offers a grid-based card view alongside the existing list view, giving you a more visual and scannable overview of your applications at a glance.

<figure><img src="https://3312761812-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzZiGARdlnXHf9T9LX6r5%2Fuploads%2Fgit-blob-c4d75057194f28f3b3a78368c21f80a4004284c4%2Fgenai-applications-grid-overview.png?alt=media" alt="GenAI Applications page with grid-based card layout"><figcaption><p>The new grid view on the GenAI Applications page displays applications as cards</p></figcaption></figure>

* **Grid-Based Application View**: A new card-based grid layout is available as an alternative to the existing list view
  * *Benefit*: Faster visual scanning and easier identification of applications, especially in environments with many GenAI applications
* **Project-Level Administration**: Projects are now exposed as a manageable entity within the admin console
  * *Benefit*: Administrators can manage project-level RBAC permissions and perform project deletion directly from the UI
  * *Note*: This enables customers to manage access control and lifecycle for projects without requiring backend intervention

**GenAI Chart and Alert Controls Rework**

Chart controls and alert controls across GenAI experiences have been redesigned for a more unified and intuitive monitoring workflow.

<figure><img src="https://3312761812-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzZiGARdlnXHf9T9LX6r5%2Fuploads%2Fgit-blob-f1a138d95236234fed321f1894081c04dc98fdc2%2Fgenai-chart-controls-rework.png?alt=media" alt="Reworked GenAI chart and alert controls showing the bank_churn application dashboard"><figcaption><p>The redesigned chart controls provide a unified monitoring experience across GenAI views</p></figcaption></figure>

* **Unified Chart Controls**: Reworked chart controls provide a consistent experience across all GenAI monitoring views
  * *Benefit*: Streamlined chart configuration with fewer clicks and a more intuitive layout
* **Reworked Alert Controls**: Alert configuration within GenAI experiences has been updated to align with the new chart controls
  * *Benefit*: Consistent interaction patterns between charting and alerting workflows
* **Automatic Chart Migration**: Existing GenAI charts are automatically migrated to the new format during the upgrade
  * **Breaking Change**: This is a breaking change to chart and alert configurations. The automatic migration supports all valid configurations. In the rare event that a migration fails, the affected chart should be recreated manually

**Model TTL Management**

You can now configure Time-to-Live (TTL) policies for ClickHouse event data at the organization, project, or model level, enabling fine-grained control over data retention.

* **Hierarchical TTL Configuration**: TTL values can be set at organization, project, or model scope by platform administrators using the config manager APIs
  * *How it works*: More specific levels take precedence — model-level TTL overrides project-level, which overrides organization-level
  * *Unit*: Days (minimum 7 days)
* **Lazy Pruning**: Data pruning occurs on a background schedule, at intervals of at least 4 hours
  * *Note*: Pruning is irreversible. Once data is pruned, it cannot be recovered
  * *Note*: Dashboards and historical charts are unaffected; only raw event queries are limited to data within the TTL window
* **Opt-In by Default**: Existing deployments are unaffected unless custom TTL values are explicitly configured
  * *Note*: The deployment-wide default is controlled by the `EVENTS_TABLE_TTL_DAYS` environment variable, which defaults to no TTL

**OTel Collector Performance Improvements**

Infrastructure improvements to the OpenTelemetry Collector enhance throughput and reliability for high-volume trace ingestion.

* **Size-Based Batching**: Sending queues now use byte-based sizing instead of count-based
  * *Benefit*: More predictable batching behavior for payloads of varying sizes, especially large spans
* **Percentage-Based Memory Limiter**: The collector's memory limiter is now percentage-based, adapting to container memory limits automatically
  * *Benefit*: Better suited to containerized deployments compared to the previous fixed-value approach
* **Configurable Kafka Producer**: Kafka producer max request size is now configurable with optional compression
  * *Benefit*: Supports larger trace and event payloads without hitting message size limits

#### Client Versions

| Component             | Version |
| --------------------- | ------- |
| Fiddler Python Client | 3.11    |
| Fiddler Evals SDK     | 0.3.0   |
| Fiddler LangGraph SDK | 1.4.0   |
| Fiddler Strands SDK   | 0.4.0   |

Refer to the [LangGraph SDK changelog](https://docs.fiddler.ai/changelog/release-notes/langgraph-sdk) for version-specific details.

#### Fixes and Security Updates

* **Security Updates**: Applied routine security patches and version updates to application frameworks to stay up-to-date with the latest improvements.

***

### Release 26.3 Notes

*February 10, 2026*

#### What's New and Improved

**RAG Health Metrics: Answer Relevance 2.0, Context Relevance, and RAG Faithfulness**

RAG Health Metrics is a purpose-built diagnostic framework for Retrieval-Augmented Generation applications. The three evaluators work together to pinpoint exactly where RAG pipelines fail — whether in retrieval, generation, or query understanding — transforming debugging from manual trial-and-error into targeted root cause analysis.

* **Answer Relevance 2.0** (Enhanced): Improved ordinal scoring system replaces binary scoring
  * *Scoring*: High (1.0), Medium (0.5), Low (0.0) with detailed reasoning
  * *Benefit*: Granular assessment of how well responses address user queries
  * *Availability*: Agentic Monitoring, Experiments, LLM Observability
* **Context Relevance** (New): Measures whether retrieved documents are relevant to the query
  * *Scoring*: High (1.0), Medium (0.5), Low (0.0) with detailed reasoning
  * *Benefit*: Isolate retrieval problems from generation problems in your RAG pipeline
  * *Availability*: Agentic Monitoring and Experiments (not available in LLM Observability)
* **RAG Faithfulness** (Repackaged): LLM-as-a-Judge faithfulness evaluator with standardized inputs and outputs, now part of the RAG Health Metrics triad
  * *Scoring*: Binary — Yes (1.0) / No (0.0) with detailed reasoning
  * *Inputs*: `user_query`, `rag_response`, `retrieved_documents`
  * *Outputs*: `label`, `value`, `reasoning`
  * *Benefit*: Combined with Answer Relevance and Context Relevance for comprehensive RAG pipeline diagnostics
  * *Availability*: Agentic Monitoring, Experiments, LLM Observability
  * *Note*: FTL Faithfulness (`ftl_response_faithfulness`) continues unchanged for guardrails and LLM Observability use cases
  * *Note*: RAG Faithfulness and FTL Faithfulness are separate evaluators with different architectures

**Diagnostic Framework Benefits:**

Use the three evaluators together to diagnose RAG pipeline issues:

| What the metrics tell you         | Why it's happening                    | Next Step                                        |
| --------------------------------- | ------------------------------------- | ------------------------------------------------ |
| High relevance + Low faithfulness | Hallucinations despite being on-topic | Check if retrieval provided sufficient grounding |
| High faithfulness + Low relevance | Grounded but didn't answer the query  | Check if retrieval provided relevant information |
| Low Context Relevance             | Retrieval pulling wrong documents     | Fix retrieval mechanism                          |

RAG Health Metrics works alongside Fiddler's existing 80+ LLM metrics (toxicity, PII, coherence, and more) — providing targeted RAG diagnostics that complement your existing observability stack.

**CustomJudge in Evals SDK**

The `CustomJudge` evaluator class is now available in the Fiddler Evals SDK (0.3.0), enabling custom LLM-as-a-Judge evaluators in Experiments workflows.

* **Prompt Template Style**: Define custom evaluators using `prompt_template` with Jinja `{{ placeholder }}` syntax and `output_fields` for structured evaluation results
  * *Benefit*: Build domain-specific evaluation criteria for any use case — brand voice compliance, bias detection, topic classification, and more
  * *Note*: This is the same `CustomJudge` class available in Agentic Monitoring, now also accessible through the Evals SDK for Experiments workflows

**Improved Reasoning Quality for LLM-as-a-Judge Evaluators**

The quality of the `reasoning` field has been improved for all LLM-as-a-Judge evaluators when using the Fiddler-hosted Llama model.

* **Better Reasoning Output**: More intelligent, consistent reasoning that better aligns with predicted labels
  * *Scope*: All pre-built LLM-as-a-Judge evaluators in Agentic Monitoring, and custom LLM-as-a-Judge evaluators using Prompt Template-style prompt specs in Traditional Monitoring
  * *Benefit*: More detailed and accurate reasoning explanations for evaluation results
  * *Note*: Evaluation speed may be slightly slower in some cases due to higher quality reasoning output; tokens per second remains constant

**Fiddler LangGraph SDK Enhancements**

The Fiddler LangGraph SDK (1.3.1) includes infrastructure upgrades and new observability capabilities.

* **OpenTelemetry Upgrade**: Updated to OpenTelemetry 1.39.1 / 0.60b1 (api, sdk, instrumentation, otlp exporter)
  * *Note*: Removed hardcoded OpenTelemetry span/batch limits; SDK now uses OpenTelemetry defaults
* **Full LLM Message History**: New span attributes `gen_ai.input.messages` and `gen_ai.output.messages` capture complete LLM message history
  * *Benefit*: Better debugging and observability of LLM interactions within agentic workflows

**Fiddler Strands Pipeline Support**

Message history from Strands span events is now extracted and stored as span attributes for querying.

* *Benefit*: Enables observability and analysis of Strands-based agentic pipelines within the Fiddler platform

#### Client Versions

| Component             | Version |
| --------------------- | ------- |
| Fiddler Python Client | 3.11    |
| Fiddler Evals SDK     | 0.3.0   |
| Fiddler LangGraph SDK | 1.3.1   |
| Fiddler Strands SDK   | 0.4.0   |

Refer to the [Evals SDK changelog](https://docs.fiddler.ai/changelog/release-notes/evals-sdk) and [LangGraph SDK changelog](https://docs.fiddler.ai/changelog/release-notes/langgraph-sdk) for version-specific details.

#### Deprecations and Removals

**DSPy-style Prompt Specifications Removed from Documentation**

DSPy-style Prompt Specifications are not supported in Agentic Monitoring or Experiments. Example notebooks have been updated to use the `CustomJudge` class with Prompt Template style exclusively.

* **Replacement**: Use `CustomJudge` with `prompt_template` (Jinja syntax) and `output_fields` for structured evaluation results
  * *Note*: DSPy-style prompt specs remain available in Traditional Monitoring but are no longer the recommended approach
  * *Action Required*: If using custom LLM-as-a-Judge evaluators, adopt `CustomJudge` with Prompt Template syntax

**Fixes and Security Updates**

* **Security Updates**: Applied routine security patches and version updates to application frameworks to stay up-to-date with the latest improvements.

***

### Release 26.2 Notes

*January 27, 2026*

#### What's New and Improved

**Enhanced Sentiment Evaluator Performance**

The Sentiment evaluator has been optimized to leverage GPU acceleration when available, significantly improving evaluation speed for all input sizes.

* **GPU Acceleration**: Sentiment evaluator now automatically detects and utilizes GPU resources when available
  * *Benefit*: Dramatically faster evaluation performance - under 80ms on the scoring endpoint for all input sizes
  * *Note*: Falls back to CPU processing if GPU is unavailable, maintaining backward compatibility
* **Performance Optimization**: Replaced model weights with GPU-compatible version
  * *Note*: Input is truncated at 512 tokens as before

**GenAI Application Deletion**

You can now delete GenAI applications directly from the GenAI Applications List page, providing better application lifecycle management.

* *Benefit*: Streamlined cleanup of test and deprecated applications

#### Deprecations and Removals

**Answer Relevance Evaluator**

The Answer Relevance evaluator has been removed from the list of available evaluators as we prepare to release an improved version.

* **Removed from Available Evaluators**: Answer Relevance is no longer available for new evaluation rules
  * *Note*: Existing Answer Relevance rules will continue to function normally
* **Replacement Timeline**: Answer Relevance v2 will be introduced in Fiddler v26.3
  * *Benefit*: The updated evaluator will provide improved accuracy and performance

**Fixes and Security Updates**

* **Security Updates**: Applied routine security patches and version updates to application frameworks to stay up-to-date with the latest improvements.

### Release 26.1 Notes

*January 13, 2026*

#### What's New and Improved

**Performance Optimization for Metrics**

Significant improvements to the metric fetching engine and metadata caching to enhance query performance and reduce database load.

* **Optimized Metric Fetching**: Metric fetching engine now retrieves sparse data from the database more efficiently
  * *Benefit*: Significantly reduced data transfer and processing overhead for metric queries
* **Smart In-Memory Processing**: Missing values are efficiently filled in-memory only when necessary
  * *Note*: For example, when preserving zero-traffic bins
  * *Benefit*: Improved query performance without sacrificing data completeness
* **LRU Metadata Caching**: Implemented Least Recently Used (LRU) caching for frequently accessed metadata
  * *Scope*: Caches Projects, Models, Baselines, Segments, and Applications metadata
  * *Benefit*: Further reduces database load and improves response times for common queries

**Span Latency Monitoring**

New charting capabilities for monitoring span latency across your agentic and LLM applications.

* **Span Latency Charts**: Added new charts specifically designed for span latency visualization
  * *Benefit*: Better visibility into performance characteristics of individual operations
* **Granular Latency Filtering**: Filter latencies by different time granularities
  * *Options*: Microseconds, milliseconds, or seconds
  * *Benefit*: Analyze performance at the appropriate scale for your use case

**Charts Preview in Agentic Alerts**

Enhanced alert configuration with visual chart previews to help you set accurate thresholds.

* **Visual Threshold Tuning**: Charts preview shows data points that fall under Critical and Warning thresholds
  * *Benefit*: Dynamically fine-tune alert thresholds based on observed trends
  * *Benefit*: Reduce false positives by visualizing actual data distribution before setting alerts

**Fixes and Security Updates**

* **Security Updates**: Applied routine security patches and version updates to application frameworks to stay up-to-date with the latest improvements.

### Release 25.22 Notes

*December 16 2025*

### What's New and Improved

**Enhanced Agentic Observability Dashboards**

Improved out-of-the-box monitoring experience for LLM and agentic applications with expanded default dashboards and automated safety evaluation.

* **Default Safety Evaluator**: New applications automatically include FTL safety evaluator rule
  * *Benefit*: Immediate safety monitoring for all LLM spans and outputs without manual configuration
* **Expanded Dashboard Charts**: Default dashboards now include 4 charts in addition to traffic monitoring and traffic metrics
  * *Safety Analysis*: Monitor safety evaluator results for responsible AI deployment
  * *Token Consumption*: Track LLM token usage for cost optimization
* **Accurate Token Counting**: SDK-based token counting replaces previous estimation method
  * *Benefit*: Precise cost tracking and optimization insights for LLM operations
* **Production Monitoring Parity**: Metric cards gaining feature parity with monitoring charts
  * *New Support*: Token counts and custom attributes now available in metric cards
  * *Benefit*: Consistent monitoring capabilities across different visualization types

**Extended Alert Capabilities for Agentic Applications**

Alert system expanded beyond traffic monitoring to support comprehensive LLM application observability.

* **Token Count Alerts**: Set thresholds for LLM token consumption
  * *Benefit*: Proactive cost management and budget protection for API usage
* **Attribute-Based Alerts**: Create alerts on numerical and categorical custom attributes
  * *Benefit*: Monitor business-specific metrics and application-specific dimensions

**Programmatic Model Schema Updates**

Add columns to production models after initial onboarding without downtime or data re-ingestion. Supports adding inputs, outputs, targets, and metadata columns with all data types.

*Action Required*: Requires Python Client SDK 3.11 or higher

**Important Notes**:

* New columns will have null values for historical events
* Future events must include data for newly added columns

**Event Deletion and Pipeline Improvements**

Critical fixes to data pipeline operations and rate limit handling for improved reliability.

* **Event Deletion Bug Fixes**: Resolved issues with event deletion operations in the data pipeline
  * *Benefit*: Reliable data cleanup and management for production systems
* **Rate Limit Handling**: Added HTTP 429 responses for rate limit scenarios
  * *Benefit*: Clear feedback when API rate limits are exceeded, enabling proper retry logic

### Client Version

This release works best with Python Client SDK **3.11** or higher.

### Release 25.21 Notes

*November 18, 2025*

### What's New and Improved

**Harrier Alerts MVP: Enhanced Traffic Monitoring**

Introducing the first release of Harrier Alerts, enabling you to set up granular traffic monitoring for your ML and LLM applications with configurable alert thresholds.

* **1-Hour Traffic Alerts**: Monitor traffic patterns with hourly granularity to catch issues quickly
  * *Benefit*: Detect traffic anomalies and potential problems within an hour of occurrence
* **1-Day Traffic Alerts**: Track daily traffic patterns for broader trend analysis
  * *Benefit*: Identify long-term traffic patterns and plan capacity accordingly
* **Configurable Thresholds**: Set custom alert thresholds based on your application needs
  * *Note*: Available for both hourly and daily monitoring periods

**User-Defined Attributes for Enhanced Observability**

Add custom attributes to your agentic and LLM application traces for deeper insights into your specific use cases and business metrics.

* **Span-Level Attributes**: Add granular metadata to individual operations
  * *Format*: `fiddler.span.user.{key}` for operation-specific attributes
* **Flexible Metadata**: Capture any custom data relevant to your monitoring needs
  * *Benefit*: Filter, group, and analyze traces using your own business dimensions
* *Action Required*: SDK update required to use this feature

**Rule-Based Evaluators**

Create custom evaluation rules for your LLM applications with flexible, condition-based logic.

* **Custom Evaluation Logic**: Define specific rules and conditions for evaluating LLM outputs
* **Flexible Conditions**: Set up complex evaluation criteria based on your use case
* *Benefit*: Tailor evaluation to your specific quality and safety requirements

**Custom LLM as a Judge (LLMaaJ)**

Build custom LLM-based evaluators using your preferred models and evaluation criteria.

* **Flexible Model Selection**: Use any LLM as an evaluator for your applications
* **Custom Prompts**: Define evaluation criteria with your own prompting strategies
* *Benefit*: Create domain-specific evaluators that understand your unique requirements

**Pre-Built LLMaaJ Improvements**

Enhanced Fiddler's pre-built LLM evaluators with improved accuracy and updated evaluation criteria.

* **Updated Evaluation Logic**: Refined prompts and evaluation criteria for better accuracy
* **Improved Response Quality**: More consistent and reliable evaluation results
* *Note*: Input and output formats have been updated for improved performance
* *Compatibility*: These evaluators were deactivated in 25.20 to prepare for these improvements

**Streamlined GenAI Application Onboarding**

Redesigned the GenAI application onboarding flow for a simpler, more intuitive setup experience.

* **Simplified Steps**: Reduced complexity in creating new GenAI applications
* **Improved Guidance**: Better in-app instructions and tooltips
* *Benefit*: Get your agentic and LLM applications monitored faster with less configuration

**Performance Optimization: Event Deletion**

Improved memory efficiency when deleting events by time range.

* **Reduced Memory Usage**: Delete operations now process data in chunks to minimize memory consumption
* **Better Scalability**: Handle large-scale deletions without resource constraints
* *Performance Impact*: Significantly lower memory footprint for bulk delete operations

### Deprecations

**Enrichment Features: Toxicity and Custom LLM Classifier**

The following enrichment features are being deprecated in favor of the improved LLMaaJ evaluators:

* **Deprecated Features**:
  * Toxicity enrichment
  * Custom LLM Classifier enrichment
* **Replacement**: Use the new Custom LLMaaJ or Pre-Built LLMaaJ evaluators
  * Enhanced evaluation capabilities with LLM-based judges
  * More flexible and accurate evaluation
* **Migration Path**: Configure equivalent evaluators using the new LLMaaJ framework
* *Benefit*: Modern evaluation infrastructure with better accuracy and flexibility

#### Fixes and Security Updates

* **Security Updates**: Applied routine security patches and version updates to application frameworks to stay up-to-date with the latest improvements.

#### Client Version

Client version updates are required for User-Defined Attributes functionality. Refer to the [Python SDK changelog](https://docs.fiddler.ai/changelog/release-notes/python-sdk) for version-specific details.

#### Documentation Updates

* **OpenTelemetry Integration**: New comprehensive documentation for OpenTelemetry integration
  * Quick Start guide for custom agent frameworks
  * Advanced patterns and production configurations
  * [OpenTelemetry Quick Start →](https://app.gitbook.com/s/jZC6ysdlGhDKECaPCjwm/agentic-ai-monitoring/opentelemetry-quick-start)
* **User-Defined Attributes**: Documentation for adding custom attributes to traces
  * Session and span-level attribute patterns
  * Best practices for custom metadata

### Release 25.20 Notes

*November 4, 2025*

### What's New and Improved

**Enhanced Fiddler Fast Trust Safety Model**

[Fiddler Fast Trust Safety](https://app.gitbook.com/s/82RHcnYWV62fvrxMeeBB/observability/llm/enrichments#fast-safety) model has been updated to improve accuracy and expand classification capabilities based on customer feedback.

* **Improved Cryptocurrency Handling**: Reduced false positives when analyzing content that references cryptocurrency and related financial terms
  * *Benefit*: More accurate safety assessments for fintech and Web3 applications without unnecessary flagging of legitimate cryptocurrency discussions
* **New Roleplaying Detection**: Added `roleplaying` label to identify content where the model is instructed to adopt a specific persona or character
  * *Impact*: Enhanced ability to detect potential prompt injection attempts and inappropriate persona adoption
  * *Note*: Users with existing FTL Safety enrichments that did not specify label subsets via the `classifiers` configuration will automatically see the new `roleplaying` label on newly ingested data

### Deprecations

**Custom LLM Classifier**

The Custom LLM Classifier feature is now deprecated and will be removed in a future release. Users should migrate to the more powerful and flexible LLM-as-a-Judge with Prompt Spec feature.

* **Replacement**: [LLM-as-a-Judge with Prompt Specs](https://app.gitbook.com/s/82RHcnYWV62fvrxMeeBB/observability/llm/llm-evaluation-prompt-specs) provides enhanced capabilities for custom evaluations with greater control and flexibility
* **Migration Path**: Refer to the LLM-as-a-Judge documentation for implementation guidance and examples
* *Benefit*: LLM-as-a-Judge offers more sophisticated evaluation workflows, better prompt engineering capabilities, and improved consistency for custom classification tasks

### Fixes and Security Updates

* **Security Updates**: Applied routine security patches and version updates to application frameworks to stay up-to-date with the latest improvements.

### Release 25.19 Notes

#### What's New and Improved

**Enhanced Session Management**

Fiddler 25.19 introduces improved session management that keeps users authenticated during active usage while maintaining security through standardized timeout policies.

* **Extended Active Sessions**: Users remain authenticated while actively using Fiddler, eliminating the previous 2-hour hard timeout that logged out active users
  * *Benefit*: Uninterrupted workflow for active users while maintaining robust security controls
* **Intelligent Idle Detection**: Sessions automatically expire after 2 hours of inactivity
  * *Default Configuration*: 2-hour idle timeout, 24-hour maximum session lifetime, 1-hour access token lifetime
* **Multi-Tab Session Synchronization**: Session state is synchronized across multiple browser tabs, providing a consistent experience
  * *Benefit*: Seamless transitions between browser tabs without unexpected logouts
* **Proactive Token Refresh**: Access tokens are automatically refreshed in the background when actively using the application

**Jobs Page Optimization**

The Jobs page now provides a more focused view of job history while improving system performance through intelligent data retention policies.

* **Streamlined Job Display**: The Succeeded/Failed tab shows only the jobs that require attention or review
  * Failed streaming jobs remain visible for 30 days
  * All batch ingestion jobs (successful and failed) remain visible for 30 days
  * Successful streaming jobs are removed immediately upon completion
  * *Benefit*: Cleaner job history makes it easier to identify jobs that need attention
* **Performance Improvements**: Chunk-level data purging reduces internal metadata table sizes
  * *Benefit*: Faster page load times, especially for high-volume environments
* **Smart Data Retention**: The system maintains a 30-day retention period for jobs that may need to be replayed or investigated while removing unnecessary successful streaming job entries

### Fixes and Security Updates

* **Security Updates**: Applied routine security patches and version updates to application frameworks to stay up-to-date with the latest improvements.

### Release 25.18 Notes

#### Fixes and Security Updates

* **Security Updates**: Applied routine security patches and version updates to application frameworks to stay up-to-date with the latest improvements.

### Release 25.17 Notes

#### Fixes and Security Updates

* **Security Updates**: Applied routine security patches and version updates to application frameworks to stay up-to-date with the latest improvements.

### Release 25.16 Notes

#### What's New and Improved

* **Login Redirection**
  * Users are now automatically redirected to their originally requested URL after signing in. This enhancement improves the user experience by eliminating the need to manually navigate back to the intended page after authentication.
* Customizable Identity Provider Group Prefix
  * Organizations can now configure a custom prefix for identity provider group mapping instead of the default `fiddler_` prefix. This enhancement allows Fiddler to work with existing organizational naming conventions for Active Directory, LDAP, and SSO groups.

    Previously, Fiddler required groups to follow the exact naming pattern:

    * `fiddler_ORG_ADMIN`
    * `fiddler_ORG_MEMBER`
    * `fiddler_<team_name>`

    With this update, administrators can specify a custom prefix that matches their organization's group naming policy. Refer to the [Mapping LDAP Groups & Users to Fiddler Teams](https://app.gitbook.com/s/82RHcnYWV62fvrxMeeBB/reference/access-control/mapping-ad-groups-to-fiddler-teams) guide for more details.

### Release 25.15 Notes

#### What's New and Improved

**New Fiddler AuthN Management Console**

We're excited to introduce the new Fiddler AuthN management console, built on a robust authentication framework. This upgrade enhances Fiddler's authentication and user management capabilities with improved security and administrative control.

**Key Features:**

* **Dedicated Management Console**: Access authentication administration at `https://authn-{your-instance}.cloud.fiddler.ai`
* **Enhanced SSO Integration**: Improved support for Okta, Microsoft Entra ID, Google, and Ping Identity with standardized configuration
* **Identity Provider Group Sync**: Automatic mapping of external groups to Fiddler teams with customizable group prefixes
* **Role-Based Administration**: Granular admin roles including "Org Owner" and "Org User Manager" for delegated management
* **Mixed Authentication Support**: Simultaneous SSO and email-based authentication methods

This enhancement delivers enterprise-grade authentication management while maintaining backward compatibility with existing configurations.

*Benefit*: Provides improved security, streamlined administration, and enhanced user experience through modern authentication infrastructure.

[Explore Authentication Documentation →](https://app.gitbook.com/s/82RHcnYWV62fvrxMeeBB/reference/access-control)

#### Fixes and Security Updates

* **Security Updates**: Applied routine security patches and version updates to application frameworks to stay up-to-date with the latest improvements.

### Release 25.14 Notes

#### What's New and Improved

**Fast Personally Identifiable Information (PII) Guardrails**

We've added Fast PII detection to Fiddler Guardrails, joining Fast Safety and Fast Faithfulness to provide comprehensive real-time protection for LLM applications.

* **Comprehensive PII Detection**: Automatically detects and flags PII leakage across 25+ categories including personal identifiers, financial data, government IDs, and digital identifiers
* **Detailed Output**: Returns detected PII spans with labels, confidence scores, and character offsets for precise identification and redaction
* **Enterprise Ready**: Optimized for low latency and high-scale deployment with consistent sub-second response times
* **Compliance Support**: Helps meet privacy regulations like GDPR, CCPA, and HIPAA by preventing PII exposure

The Fast PII Guardrails integrate seamlessly via REST API and can be used independently or combined with existing guardrails for layered protection.

For technical implementation details, see the [Guardrails documentation](https://app.gitbook.com/s/82RHcnYWV62fvrxMeeBB/getting-started/guardrails).

#### Fixes and Security Updates

* **Security Updates**: Applied routine security patches and version updates to application frameworks to stay up-to-date with the latest improvements.

### Release 25.13 Notes

**Fixes and Security Updates**

* **Security Updates**: Applied routine security patches and version updates to application frameworks to stay up-to-date with the latest improvements.
* **Alerts UI Consistency**: Fixed various display inconsistencies in the Alerts interface to improve user experience and visual consistency across the platform.

### Release 25.12 Notes

#### What's New and Improved

* **Concurrent Enrichment Processing**
  * Introduced parallel processing for independent enrichment operations, significantly improving performance when multiple enrichments are applied to your LLM data
  * *Performance Impact:* Reduces overall enrichment processing time by up to 70% when using multiple enrichments (e.g., combining PII detection, toxicity analysis, and sentiment scoring)
  * *Benefit:* Faster data processing enables near real-time monitoring for high-volume LLM applications, reducing the delay between data ingestion and actionable insights
  * *Note:* This feature is currently in controlled rollout. Contact your customer success manager if you'd like early access

#### Fixes and Security Updates

* **Security Updates**: Applied routine security patches and version updates to application frameworks to stay up-to-date with the latest improvements.

### Release 25.11 Notes

**Fixes and Security Updates**

* **Security Updates**: Applied routine security patches and version updates to application frameworks to stay up-to-date with the latest improvements.

### Release 25.10 Notes

#### What's New and Improved

* **Custom LLM Enrichment & Evaluations Enhancements**
  * *Improved Determinism:* Temperature parameter now defaults to 0 for classification use cases, ensuring more consistent and repeatable results
  * *Enhanced Flexibility:* The Evaluations endpoint now accepts a temperature parameter, matching the configuration options available in Enrichment
  * *Benefit:* Teams can achieve more predictable classification outputs while maintaining the flexibility to adjust temperature when needed for specific use cases
* **Fiddler Fast Trust Faithfulness v2.4.1**
  * *Performance Boost:* Up to 150ms faster processing on longer input texts
  * *Benefit:* Reduced latency for faithfulness checks on documents and extended conversations, enabling more responsive LLM monitoring at scale
  * *Impact:* Particularly beneficial for applications processing lengthy contexts or high-volume document analysis workflows

### Release 25.9 Notes

#### What's New and Improved

* **Custom Webhook Support for Alert Notifications**
  * Extended webhook integration capabilities beyond Slack and Microsoft Teams to support any webhook provider
  * *Key Features:*
    * [Create custom webhook](https://app.gitbook.com/s/82RHcnYWV62fvrxMeeBB/reference/settings) configurations for any third-party service or internal system
    * Configure custom webhooks with alert rules for flexible notification routing
    * Maintain existing Slack and Microsoft Teams integrations alongside custom webhooks
  * *Benefit:* Organizations can now integrate Fiddler alerts with their preferred communication platforms and incident management systems
* **Enhanced Data Ingestion Performance with ClickHouse Optimization**
  * *Performance Improvements include:*
    * End-to-end ingestion latency reduced by up to 10x for faster data processing
    * Label update operations now complete significantly faster
    * Event deletion performance dramatically improved
    * Enhanced ClickHouse storage efficiency and query performance
  * *Benefit:* Teams can now process and analyze data in near real-time, enabling faster decision-making and more responsive monitoring of production models

#### Fixes and Security Updates

* **Security Updates**: Applied routine security patches and version updates to application frameworks to stay up-to-date with the latest improvements.

### Release 25.8 Notes

#### What's New and Improved

* **Updated Fiddler Fast Trust Faithfulness Model**
  * *Classification Improvements:*
    * Improved accuracy on Q\&A and simple knowledge-retrieval tasks
    * Enhanced accuracy on Q\&A with longer contexts
    * Improved accuracy on "off-label" tasks like JSON-to-Text and Dialogue/Chat exchanges
  * *Performance Boost:*
    * 15-20% faster processing on longer contexts
* **Enhanced Fiddler Fast Trust Safety Model**
  * Increased Safety model context window from 4,000 to 800,000 tokens
  * *Benefit:* Enables comprehensive safety analysis on much larger documents and conversations without truncation
* **Multi-threading for Embedding Enrichment**
  * Implemented parallel processing for embedding generation
  * *Performance Impact:* At least a 5x improvement in processing speed for embedding enrichments
  * *Scalability:* Can achieve even greater performance with additional threads and resources
  * *Benefit:* Significantly reduces processing time for high-volume LLM monitoring pipelines
* **Microsoft Teams Webhook Integration**
  * Added native support for Microsoft Teams webhook notifications alongside existing Slack integration
  * *Benefit:* Teams can now receive alert notifications directly in their Microsoft Teams channels
  * *How to use:* Configure Microsoft Teams webhooks in the Webhook Integrations tab of the [Settings](https://app.gitbook.com/s/82RHcnYWV62fvrxMeeBB/reference/settings) page
  * *Impact:* Streamlines communication workflows for organizations using Microsoft Teams as their primary collaboration platform

#### Fixes and Security Updates

* **Security Updates**: Applied routine security patches and version updates to application frameworks to stay up-to-date with the latest improvements.

### Release 25.7 Notes

**Fixes and Security Updates**

* **Security Updates**: Applied routine security patches and version updates to application frameworks to stay up-to-date with the latest improvements.

**Documentation Updates**

* **New Glossary Feature:** We've expanded our Product Concepts guide with a comprehensive [glossary](https://app.gitbook.com/s/82RHcnYWV62fvrxMeeBB/reference/glossary). Each term now has its own dedicated page containing:

  * Detailed explanations
  * Implementation guidance
  * Related resources and references

  This enhancement makes it easier to understand key product terminology and concepts while providing deeper technical context when needed. We'll continue to add new terms to the glossary incrementally over time.

### Release 25.6 Notes

#### What's New and Improved

* **Custom LLM Enrichment**: Leverage [Llama3.1 8B](https://huggingface.co/meta-llama/Llama-3.1-8B) to categorize input data using your own prompts and custom categories
  * *Benefit*: Enables flexible classification tasks tailored to your specific business needs, going beyond pre-defined enrichment types

#### Fixes and Security Updates

* **Security Updates**: Applied routine security patches and version updates to application frameworks to stay up-to-date with the latest improvements.

#### Documentation Updates

* **Removed Deployment Guide**: The Deployment Guide is no longer relevant to Fiddler SaaS and managed SaaS offerings.

### Release 25.5 Notes

#### Improvements

* **Baseline Name Length**: Increased the maximum allowed characters from 30 to 256. This change enables more descriptive baseline names for complex projects with multiple models and datasets.
  * *Action Required*: None. Existing baselines remain unchanged.
* **Enhanced Job Error Messages**: Error messages during metrics aggregation now specifically identify which step in the data ingestion process failed, helping you troubleshoot pipeline issues faster.
  * *Benefit*: Reduces debugging time by pinpointing in which step jobs are failing.

#### Fixes and Security Updates

* **Security Updates**: Applied routine security patches to container images and application frameworks to address recent vulnerabilities.
* **Homepage Cache Timestamp**: Fixed an issue where cached dashboard data would display incorrect "Last Updated" timestamps, leading to confusion about data freshness.

#### Documentation Updates

* **Streamlined Structure**: Reorganized documentation with improved navigation paths between related topics.
  * *New Section*: Consolidated technical guides and API references into the "Technical Reference" section.

### Release 25.4 Notes

#### What's New and Improved

#### Now Available in Public Preview

* **UI-based Model Onboarding with Draft Mode**: Iteratively refine your model schema before publishing. Validate sample data, collaborate with your team, and deploy with confidence. This streamlines the model deployment process for faster time-to-value. See our new [Model Guides](https://app.gitbook.com/s/82RHcnYWV62fvrxMeeBB/observability/model-ui) for details and best practices.

#### Improvements

* **Enhanced Charts Framework**: Implemented significant improvements to our charting system, delivering more consistent rendering and reliable performance across all dashboards and visualizations.
* **Fast Faithfulness Trust Model Enhancements**: Improved classification accuracy overall by 23% and reduced the Q\&A benchmark error rate by 36%.

#### Fixes and Security Updates

* **Performance Optimization**: Updated application framework components to improve validation speed during model onboarding and data publishing processes.
* **Enhanced Error Handling**: Redesigned validation messages during Baseline creation to provide more actionable and detailed troubleshooting guidance.
* **Concurrency Improvements**: Optimized metrics calculation when model edits trigger recalculations, reducing processing time while preventing disruption to production data pipelines.

#### Documentation Updates

* **Streamlined Structure**: Merged the former UI Guide into the Product Guide for a more intuitive navigation experience.
* **Expanded Content**: Added comprehensive data publishing guides with practical examples and best practices for various data types and formats.
* **New UI Onboarding Guide**: Published detailed documentation for the new UI-based model onboarding feature, including step-by-step instructions and best practices.

### Release 25.3 Notes

#### What's New and Improved

**New Priority Queue for Streaming Data**

We've added a dedicated queue for processing streaming inference data. This improvement gives streaming events priority handling compared to batch processing jobs.

**Improvements**

This release enhances the clarity of error messages when configuring different baseline types for a model.

**How it helps you**

* Faster processing times for streaming data
* Reduced latency for real-time monitoring applications
* No delays from large batch upload operations

**How It Works**

Streaming events now flow through a separate, high-priority processing lane—similar to an HOV lane on a highway—bypassing any congestion from batch operations. This feature works automatically with your existing implementation. No configuration changes required.

### Release 25.2 Notes

#### What's New and Improved

We have added Token Count as a new addition to Fiddler's out-of-the-box enrichments. Token count visibility is a key factor for monitoring and optimizing LLM applications. This enrichment is particularly useful for cost analysis, as it tracks API usage and helps teams understand the financial implications of their LLM usage. It also aids in identifying performance issues related to token limits and supports system health monitoring by detecting unusual patterns or truncated responses. Teams can use token metrics to optimize prompts for efficiency and quality while understanding usage patterns across their application. Combined with existing quality metrics, token counts offer a more complete view of LLM system performance and help teams make data-driven decisions about their prompt engineering and resource allocation.

#### Client Version

Python client version is updated to [3.8](https://docs.fiddler.ai/changelog/python-sdk#id-3.8) and includes new support for updating additional parameters of Alert rules, including `warning_threshold`, `critical_threshold`, and `evaluation_delay`.

### Release 25.1 Notes

#### What's New and Improved

**Introducing Fiddler Guardrails!**

Fiddler AI has introduced Fiddler Guardrails, a new feature that extends the Fiddler Trust Service and is designed to enhance the safety and security of Large Language Model (LLM) applications. This tool proactively detects and mitigates risks such as hallucinations and prompt injection attacks, ensuring more reliable and trustworthy AI operations. Organizations can confidently deploy LLM applications with improved oversight and protection by integrating Fiddler Guardrails. You can see the full announcement [here](https://docs.fiddler.ai/changelog/readme) for a comprehensive overview of this feature.

**Improvements**

This release includes updates focused on improving system performance, stability, and scalability. These improvements ensure a smoother user experience and provide a more robust platform for future developments.

**Guardrails Endpoint Change**

This release updates the following Guardrails REST API endpoints. The [Guardrails guide ](https://app.gitbook.com/s/82RHcnYWV62fvrxMeeBB/getting-started/guardrails)provides detailed usage information.

| Guardrail Service            | Previous Endpoint           | Current Endpoint          |
| ---------------------------- | --------------------------- | ------------------------- |
| Fast Safety Guardrails       | ftl\_prompt\_safety         | ftl-safety                |
| Fast Faithfulness Guardrails | ftl\_response\_faithfulness | ftl-response-faithfulness |

### Release 25.0 Notes

#### What's New and Improved

Introducing **UI Model Onboarding**, a powerful new capability that enables teams to onboard models directly through the Fiddler user interface. This streamlined approach to model integration enhances the platform's accessibility while maintaining robust monitoring capabilities.

Here's what this means for you:

* Easy to use: We designed the Model Onboarding UI to be user-friendly, making it simple and intuitive to onboard your models.
* More accessible: This new feature makes it easy to onboard your models even if you're not a Python expert.

What can you do with it?

* Onboard models for different tasks: Currently, it supports three model task types: Not Set, Regression, and Binary/Multiclass Classification.
* Upload your data: Upload your sample data, and Fiddler will automatically try to understand its structure, saving you time from entering details manually.
* Review and edit: You can quickly review and edit the data structure (schema) inferred by Fiddler.
* Define targets: Specify the target variable that your model is designed to predict.
* Provide model details: Give your model a name and other important information.

This feature is currently in public preview which you can learn more about [here](https://app.gitbook.com/s/82RHcnYWV62fvrxMeeBB/reference/feature-maturity-definitions#public-preview). We appreciate your feedback as we work to enhance the UI Model Onboarding experience.

### Release 24.19 Notes

#### What's New and Improved

We're excited to introduce three updates in this release that will significantly improve workflow efficiency. These updates include enhancements to alert notifications, schema management, and model onboarding workflows.

* **Pause Alert Notifications**
  * Users can now pause and resume notifications for specific alert rules without interrupting their evaluation. This feature helps reduce alert fatigue and prioritize critical alerts.
  * Highlights:
    * New bell icon for toggling notification status directly from the alert rule table.
    * Notifications can be paused or resumed with clear visual feedback and confirmation messages.
  * Benefits:
    * Reduced alert fatigue.
    * Continued evaluation of paused alerts without disruption.
* **Model Schema Editing (Private Preview)**
  * Say goodbye to re-onboarding models for schema updates! This feature allows users to edit numerical and categorical columns and add metadata columns directly within the platform.
  * Highlights:
    * Adjust numerical ranges and add new categories to categorical columns.
    * Add metadata columns for enhanced schema flexibility.
    * Automatic recalculation of metrics and aggregates after edits.
  * Benefits:
    * Faster schema updates with no re-onboarding required.
    * Keeps metrics and alerts in sync with the latest schema changes.
* **UI-Based Model Onboarding (Private Preview)**
  * Simplify model onboarding with our new interactive UI. Add models without relying on Python APIs, making onboarding faster and more accessible to all team members.
  * Highlights:
    * Supports key task types: Not Set, Regression, and Binary Classification.
    * Automatic schema inference and validation with error detection.
  * Benefits:
    * Streamlines onboarding for non-technical users.
    * Reduces errors with built-in validation checks.

**Private Preview**

* The Model Schema Editing and UI-Based Model Onboarding features are available for private preview. For more details on how to participate, please refer to the private preview [guide](https://app.gitbook.com/s/82RHcnYWV62fvrxMeeBB/reference/feature-maturity-definitions#private-preview).

### Release 24.18 Notes

#### What's New and Improved

* **Native Integration with AWS SageMaker AI**
  * Fiddler is now natively supported within the newly launched Amazon SageMaker partner AI ecosystem. This integration enables enterprises to validate, monitor, analyze, and improve their ML models in production, all within their existing private and secure Amazon SageMaker AI environment. Read the official announcement [here](https://www.fiddler.ai/blog/fiddler-delivers-native-enterprise-grade-ai-observability-to-amazon-sagemaker-ai-customers). Note Fiddler Python client version [3.7+](https://docs.fiddler.ai/changelog/python-sdk#id-3.7) is required for this feature.
* **Download Dataset Code in UI**
  * Now you can download your baseline and non-production datasets faster than ever with just a click! Building on the popular feature we introduced for production data in the Root Cause Analysis Events table, we've added ready-to-use Python code snippets right in the interface. Simply copy and paste these snippets to jumpstart your data analysis in your notebooks.
* **Python Client Highlights**
  * The latest release of Fiddler's Python client brings two powerful new convenience features to streamline your workflow:
    * Our new Project.get\_or\_create() class function simplifies project creation in notebooks. This feature prevents name conflict errors during project creation when your notebook runs multiple times, saving you time and reducing the need for additional exception handling.
    * We've also added model.remove\_column(), a simpler way to remove columns during model onboarding. This function replaces the multi-step process previously required, making model configuration faster and more intuitive.
  * To enhance reliability, we've implemented a configurable HTTP retry mechanism that you can fine-tune to match your network environment.
  * For more details, please refer to the [Python Client Release notes](https://docs.fiddler.ai/changelog/release-notes/python-sdk).

#### Discontinued

* **The SQL Analyze Page Discontinued**
  * The legacy SQL Analyze page has been removed as of 24.18. The new Analyze experience within monitoring charts Root Cause Analysis now enables data table generation using Fiddler Query Language (FQL) and supports the creation of analytical charts such as confusion matrices, feature distribution charts, and more.

#### Client Version

Client version [3.7+](https://docs.fiddler.ai/changelog/python-sdk#id-3.7) is required for the updates and features mentioned in this release.

### Release 24.17 Notes

#### What's New and Improved

* **Feature Analytics in Root Cause Analysis (Public Preview)**
  * The root cause analysis experience within monitoring charts now allows users to view feature distribution, feature correlation, and correlation matrix.

#### Discontinued

* **SQL Methods in the Python Client Discontinued**
  * From Client 3.6 and onwards, `get_slice` and `download_slice` are discontinued. In their stead, use the new `download_data` method to download production and non-production data from your Fiddler models. If you have any questions or need any assistance migrating scripts using the deprecated methods, please contact your Fiddler customer success manager.
* Use of or support for **Python 3.8 is discontinued** by Fiddler. Note Python 3.8 has been designated [End of Life](https://devguide.python.org/versions/) as of October 7, 2024.

### Release 24.16 Notes

#### What's New and Improved

* **New Chart Type: Correlation Matrix (Public Preview)**
  * The Correlation Matrix chart enables users to visualize relationships between up to eight columns in a heatmap, making it easy to spot significant patterns. By clicking on any cell representing the relationship between two features, users can open a Feature Correlation chart for that pair, offering more detailed insights into the correlation score.
* **Events Table in Root Cause Analysis (Public Preview)**
  * The root cause analysis experience within monitoring charts now allows users to perform deeper investigations by viewing and downloading up to 1,000 raw events, providing valuable insights for understanding and addressing potential issues.

### Release 24.15 Notes

#### What's New and Improved

* **New Chart Type: Metric Card (Public Preview)**
  * We’re excited to introduce the Metric Card chart type, which allows users to display up to four key numerical values in a clear and concise card format. This new visualization enhances data presentation by enabling quick insights into critical metrics, making it easier for decision-makers to spot trends or performance indicators at a glance.
* **New Chart Type: Feature Correlation (Public Preview)**
  * The Feature Correlation chart, part of Feature Analytics charts, enables users to analyze and visualize the relationships between different features within their models. By offering a clear view of correlations, this tool supports more informed model diagnostics and refinement.

### Release 24.14 Notes

#### What's New and Improved

* This release focused on system performance, stability, and security enhancements. These improvements ensure a smoother user experience and provide a more robust platform for future developments.

### Release 24.13 Notes

#### What's New and Improved

* NEW Standalone Feature Distribution Chart (Public Preview)
  * Create feature distribution charts for numerical and categorical data types that can be added to dashboards.
* Embedding Visualization UX Improvements
  * User interface and usability improvements to the UMAP embedding visualization chart.
* Additional database performance improvements.

#### Deprecated and Decommissioned

* Fairness was decommissioned in v24.8, and the documentation has now been removed.

### Release 24.12 Notes

* Surfacing Error Messages for Failed Jobs
  * Error messages for failed jobs are now visible directly on the UI job status page, simplifying the process of diagnosing and resolving issues.
* User Selected Default Dashboards
  * Any dashboard within a project can now be assigned as the default dashboard for a model, with all insights leading directly to the assigned default dashboard.
* Custom Feature Impact Feature Release Notes
  * Introducing Custom Feature Impact: Upload custom feature impact scores for your models, leveraging domain-specific knowledge or external data without requiring the corresponding model artifact.
  * Easy data upload via API endpoint with required parameters: Model UUID, Feature Names, and Impact Scores.
  * View updated feature impact scores in:
    * Model details page
    * Charts page
    * Explain page
  * Flexible update options: Update existing feature impact data by uploading new data for the same model and Seamless integration with existing model artifacts.
* Flexible Model Deployment
  * The `python-38` base image is no longer supported.

### Release 24.11 Notes

#### Client Version

Client version 3.3+ is required for the updates and features mentioned in this release.

#### What's New and Improved:

* Performance Analytics (Preview) Embedded in Monitoring Charts
  * Visualize performance analytics charts as part of the root cause analysis flow for Binary Classification, Multiclass Classification, and Regression models, spanning from confusion matrices, precision recall charts, prediction scatterplots and more.

### Release 24.10 Notes

#### Client Version

Client version 3.3+ is required for the updates and features mentioned in this release.

#### What's New and Improved:

* Support for applied segments in monitoring charts
  * Create and apply segments dynamically in monitoring charts for exploratory analysis without requiring them to be saved to the model.
* User-Defined Feature Impact
  * The User-Defined Feature Impact enables you to upload custom feature impact for models. This feature addresses several issues reported by our customers, including model artifact size, onboarding complexity, and the need for custom feature impact.
  * Key highlights
    * New method: UploadFeatureImpact
    * Improved Fiddler UI to display uploaded feature impact

### Release 24.9 Note

#### What's New and Improved

* Enhanced access controls
  * Control access with precision: Manage user access to resources with Role-Based Access Control (RBAC), ensuring the right users have the right permissions.
  * Simplify user management: Assign roles to users and teams to streamline access control and enhance collaboration. \*≠ Protect sensitive resources: Restrict access to sensitive resources, such as models and project settings, with granular permissions.
  * Work efficiently: Focus on your work without worrying about unauthorized access or data breaches.

### Release 24.8 Notes

#### Release of Fiddler Platform Version 24.8:

* **Performance Analytics Charts (Public Preview)**
  * Visualize charts to aid in analyzing model performance for Binary Classification, Multiclass Classification, and Regression models.
  * Leverage applied segments in Performance Analytics charts to explore problematic cohorts of data.

### Release 24.7 Notes

#### What's New and Improved

TBD

### Release 24.6 Notes

#### Release of Fiddler Platform Version 24.6:

* Performance improvements
  * Improved the performance of various modules / APIs.
  * Improved observability which can help monitor health and performance of the operations.

#### Client Version

* Client version 3.1.2+ is required for the updates and features mentioned in this release.

### Release 24.5 Notes

#### Release of Fiddler Platform Version 24.5:

* Support for model versions for streamlined model management

#### What's New and Improved:

* **Model Versions**
  * Efficiently manage related models by creating structured versions, facilitating tasks like retraining and comparison analyses.
  * Users can maintain model lineage, efficiently manage updates, flexibly modify schemas, and adjust parameters.
* **Airgapped Enrichments (alpha)**
  * For privacy sensitive use cases, all data getting enriched stays within customer premises.
* **New Deployment Base Images**
  * We have added new deployment base images to support model versioning.

**Client Version**

Client version 3.1.0+ is required for the updates and features mentioned in this release.

### Release 24.4 Notes

#### Release of Fiddler Platform Version 24.4:

* UMAP UI changes
* SSO integration changes
* New concept: **Environments**
* Fundamental changes to product concepts

#### What's New and Improved:

* **UMAP UI**
  * Vertical scrolling instead of horizontal scrolling for data cards
  * "View More" option to open data cards in maximized modal
  * Ability to toggle between data cards in the maximized modal
* **SSO integration changes**
  * Fiddler now integrates with Azure AD SSO, allowing you to leverage existing user roles for access control within Fiddler. This eliminates the need for manual user creation and simplifies user management within your organization.
* **Environments**
  * Each Model now has two environments (Pre-Production and Production) used to house data in different ways.
  * A Model's Pre-Production environment is used to house non-time series data (Datasets).
  * A Model's Production environment is used to house time series data.
* **Product concept changes**
  * Datasets are no longer stored at the Project level. Instead, they're stored at the Model level under the Pre-Production Environment.
  * The Model Details page has been updated with a new design.

**Client Version**

Client version 3.0+ is required for the updates and features mentioned in this release.

#### Client 3.x Release:

We are launching Client 3.x, this is revamped client 2.x as we move to more object-oriented based methods. This means, any pipeline setup in client 2.x would eventually be required to upgrade to the new methods. **Client 2.x will sunset approximately 6 months post this release.**

#### Deprecations and Removals:

* All IDs will be UUIDs instead of strings.
* Dataset deletion is not allowed anymore.

For API level changes and updates please check [client history](https://docs.fiddler.ai/changelog/release-notes/python-sdk)
