# Source: https://docs.datadoghq.com/error_tracking/backend/capturing_handled_errors.md

---
title: Capturing Handled Errors In Error Tracking
description: Learn how to capture handled errors in Error Tracking.
breadcrumbs: >-
  Docs > Error Tracking > Backend Error Tracking > Capturing Handled Errors In
  Error Tracking
---

# Capturing Handled Errors In Error Tracking

## Overview{% #overview %}

Datadog tracing libraries can automatically report handled errors. The errors are attached through span events to the span in which they are handled. They are also directly reported to Error Tracking.

## Requirements{% #requirements %}

{% dl %}

{% dt %}
Supported languages
{% /dt %}

{% dd %}
Python, Ruby
{% /dd %}

{% /dl %}

- Your Datadog Agent must be configured for [Standalone Backend Error Tracking](https://docs.datadoghq.com/error_tracking/backend/getting_started) or [APM](https://docs.datadoghq.com/error_tracking/apm). You must be running Agent version `7.61.0` or higher.
- Your application must be instrumented with:
  - `dd-trace-py` version `3.8.0` or higher for Python
  - `dd-trace-rb` version `2.16.0` or higher for Ruby

{% alert level="info" %}
Handled errors contain the span attribute `error.handling:handled`. For more details, see [Facets](https://docs.datadoghq.com/error_tracking/explorer/#facets).
{% /alert %}

Capturing handled errors is only available in APM Error Tracking or Standalone Backend Error Tracking. Error Tracking for Logs and RUM is not supported.

## Setup{% #setup %}

Set up your application to capture handled errors using one of the following official Datadog tracing libraries:



- [Python](https://docs.datadoghq.com/error_tracking/backend/capturing_handled_errors/python)
- [Ruby](https://docs.datadoghq.com/error_tracking/backend/capturing_handled_errors/ruby)



## Further reading{% #further-reading %}

- [Error Tracking Issue States and Workflows](https://docs.datadoghq.com/error_tracking/issue_states/)
- [Learn about the Error Tracking Explorer](https://docs.datadoghq.com/error_tracking/explorer)
- [Enable infrastructure monitoring](https://docs.datadoghq.com/error_tracking/guides/enable_infra)
- [Enable APM](https://docs.datadoghq.com/error_tracking/guides/enable_apm)
