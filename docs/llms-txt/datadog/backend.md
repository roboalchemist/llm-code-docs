# Source: https://docs.datadoghq.com/error_tracking/backend.md

---
title: Backend Error Tracking
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Error Tracking > Backend Error Tracking
---

# Backend Error Tracking

## Overview{% #overview %}

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/error-tracking-overview-2.aa2160eb75631cb79d8401f9448cc71f.png?auto=format"
   alt="The details of an issue in the Error Tracking Explorer" /%}

It is critical for your system's health to consistently monitor the errors that Datadog collects. When there are many individual error events, it becomes hard to prioritize errors for troubleshooting.

Error Tracking simplifies debugging by grouping thousands of similar errors into a single issue. Error Tracking enables you to:

- Track, triage, and debug fatal errors
- Group similar errors into issues, so that you can identify important errors and reduce noise
- Set monitors on error tracking events, such as high error volume or new issues
- Follow issues over time to know when they first started, if they are still ongoing, and how often they occur
- Automatically capture local variable values so you can reproduce exceptions, simplifying the process to resolve errors quickly

## Setup{% #setup %}

- [Standalone Backend Error Tracking](https://docs.datadoghq.com/error_tracking/backend/getting_started)
- [APM](https://docs.datadoghq.com/error_tracking/apm)
- [Logs](https://docs.datadoghq.com/error_tracking/backend/logs)

## Further Reading{% #further-reading %}

- [Getting Started with the Error Tracking Explorer](https://docs.datadoghq.com/error_tracking/explorer/)
- [Error Tracking Issue States and Workflows](https://docs.datadoghq.com/error_tracking/issue_states/)
- [Simplify production debugging with Datadog Exception Replay](https://docs.datadoghq.com/error_tracking/backend/exception_replay)
