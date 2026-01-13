# Source: https://docs.datadoghq.com/tracing/trace_collection/single-step-apm.md

---
title: Single Step APM Instrumentation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > APM > Application Instrumentation > Single Step APM Instrumentation
source_url: https://docs.datadoghq.com/trace_collection/single-step-apm/index.html
---

# Single Step APM Instrumentation

## Overview{% #overview %}

Single Step Instrumentation (SSI) automatically installs the Datadog SDKs with no additional configuration required, reducing onboarding time from days to minutes.

To learn more about how it works, see the [injector guide for Single Step Instrumentation](https://docs.datadoghq.com/tracing/guide/injectors).

## Prerequisites{% #prerequisites %}

1. Remove any custom instrumentation code from your application and restart it. SSI is automatically disabled if custom instrumentation is detected.
1. Confirm environment compatibility by reviewing the [SSI compatibility guide](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/compatibility/) for supported languages, operating systems, and architectures.

## Instrument SDKs across applications{% #instrument-sdks-across-applications %}

When you [install or update the Datadog Agent](https://app.datadoghq.com/account/settings/agent/latest) with **APM Instrumentation** enabled, the Agent instruments your applications by loading the Datadog SDK into supported processes. This enables distributed tracing by capturing and sending trace data from your services without requiring code changes.

After instrumentation, you can optionally:

- [configure Unified Service Tags (USTs)](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging)
- enable additional SDK-dependent products and features, such as Continuous Profiler or Application Security Monitoring

Click on one of the following tiles to learn how to set up SSI for your deployment type:


## Troubleshooting{% #troubleshooting %}

If you encounter problems enabling APM with SSI, see the [SSI troubleshooting guide](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/troubleshooting).

## Further reading{% #further-reading %}

- [Enable Runtime Metrics](https://docs.datadoghq.com/tracing/metrics/runtime_metrics/)
- [Understanding injector behavior with Single Step Instrumentation](https://docs.datadoghq.com/tracing/guide/injectors)
- [Troubleshooting Single Step APM](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/troubleshooting/)
- [Troubleshooting APM Instrumentation on a Host](https://learn.datadoghq.com/courses/troubleshooting-apm-instrumentation-on-a-host)
- [Instrument your applications using local SDK injection](https://docs.datadoghq.com/tracing/guide/local_sdk_injection)
- [Bring high-performance observability to secure Kubernetes environments with Datadog's CSI driver](https://www.datadoghq.com/blog/datadog-csi-driver/)
