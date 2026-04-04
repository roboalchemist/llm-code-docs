# Source: https://docs.datadoghq.com/tracing/error_tracking.md

---
title: Error Tracking for Backend Services
description: Learn how to search and manage errors collected from your backend services.
breadcrumbs: Docs > APM > Error Tracking for Backend Services
---

# Error Tracking for Backend Services

## Overview{% #overview %}

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/error-tracking-overview-2.aa2160eb75631cb79d8401f9448cc71f.png?auto=format"
   alt="The details of an issue in the Error Tracking Explorer" /%}

It is critical for your system's health to consistently monitor the errors collected by Datadog. When there are many individual error events, it becomes hard to prioritize errors for troubleshooting.

Error Tracking simplifies debugging by grouping thousands of similar errors into a single issue. An issue is an aggregation of error data that provides insights such as

- How many users have been impacted
- When the error first occurred
- Which commit probably caused the error

Error Tracking enables you to:

- Track, triage, and debug fatal errors
- Group similar errors into issues, so that you can more easily identify important errors and reduce noise
- Set monitors on error tracking events, such as high error volume or new issues
- Follow issues over time to know when they first started, if they are still ongoing, and how often they occur

## Setup{% #setup %}

Error Tracking is available for all languages supported by APM. It requires no additional SDK and no configuration changes.

Optionally, to see code snippets in your stack traces, set up the [GitHub integration](https://docs.datadoghq.com/tracing).

{% image
   source="https://datadog-docs.imgix.net/images/tracing/error_tracking/inline_code_snippet.d66611583dc16b5ed75b660043cae0ab.png?auto=format"
   alt="An inline code snippet in a stack trace" /%}

To get started with configuring your repository, see the [Source Code Integration documentation](https://docs.datadoghq.com/integrations/guide/source-code-integration).

## Use span attributes to track error spans{% #use-span-attributes-to-track-error-spans %}

The Datadog tracers collect errors through integrations and the manual instrumentation of your backend services' source code. An error span must contain the `error.stack`, `error.message`, and `error.type` [span attributes](https://docs.datadoghq.com/tracing/visualization/trace/?tab=spantags#more-information) and belong to a complete trace to be tracked. If an error is reported multiple times within a service, only the top-most error is kept.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/error_tracking/flamegraph_with_errors.0d4a1c89fc86e42851e4e533013b8061.png?auto=format"
   alt="Flame graph with errors" /%}

Error Tracking computes a fingerprint for each error span it processes using the error type, the error message, and the frames that form the stack trace. Errors with the same fingerprint are grouped together and belong to the same issue. For more information, see the [Trace Explorer documentation](https://docs.datadoghq.com/tracing/trace_explorer/trace_view/?tab=spantags).

## Control which errors are tracked{% #control-which-errors-are-tracked %}

Error Tracking automatically processes all error spans, but you can control which errors are ingested and how they are managed:

- **Filter errors with inclusion and exclusion rules**: Define rules to include or exclude errors based on attributes such as service, environment, or error type. See [Manage Data Collection](https://docs.datadoghq.com/error_tracking/manage_data_collection/).
- **Set rate limits**: Control the volume of errors ingested per day to manage costs. See [Manage Data Collection](https://docs.datadoghq.com/error_tracking/manage_data_collection/).
- **Exclude specific issues**: Mark recurring non-actionable issues as `EXCLUDED` to stop collecting them. See [Issue States](https://docs.datadoghq.com/error_tracking/issue_states/).
- **Filter entire traces**: Prevent traces from being sent to Datadog (rather than filtering errors). See [Ignoring Unwanted Resources in APM](https://docs.datadoghq.com/tracing/guide/ignoring_apm_resources/).

## Examine issues to start troubleshooting or debugging{% #examine-issues-to-start-troubleshooting-or-debugging %}

Error Tracking automatically categorizes errors into issues collected from your backend services in the [Error Tracking Explorer](https://app.datadoghq.com/apm/error-tracking). See the [Error Tracking Explorer documentation](https://docs.datadoghq.com/tracing/error_tracking/explorer) for a tour of key features.

Issues created from APM include the distribution of impacted spans, the latest most relevant stack trace, span attributes, host tags, container tags, and metrics.

## Further Reading{% #further-reading %}

- [Explore a centralized view into service telemetry, Error Tracking, SLOs, and more](https://www.datadoghq.com/blog/service-page/)
- [Learn about the Trace Explorer](https://docs.datadoghq.com/tracing/trace_explorer/trace_view/)
- [Learn about the Error Tracking Explorer](https://docs.datadoghq.com/tracing/error_tracking/explorer)
- [Create an Error Tracking monitor](https://docs.datadoghq.com/monitors/types/error_tracking/)
