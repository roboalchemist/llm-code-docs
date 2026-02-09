# Source: https://docs.datadoghq.com/profiler/guide/solve-memory-leaks.md

---
title: Solve Memory Leaks with Profiling
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Continuous Profiler > Continuous Profiler Guides > Solve Memory Leaks
  with Profiling
---

# Solve Memory Leaks with Profiling

## Overview{% #overview %}

Profiling has several datasets to help solve memory leaks, such as the Heap profile type, which is [available for multiple languages](https://docs.datadoghq.com/profiler/enabling/supported_versions/#profile-types).

To help you get started, Datadog provides an end-to-end, guided walkthrough for your service within the [APM service page](https://docs.datadoghq.com/tracing/services/service_page/#memory-leaks):

{% image
   source="https://datadog-docs.imgix.net/images/profiler/guide-memory-leak/service-page-memory-leak.069daab2faec710855ddcf3d3f629efd.png?auto=format"
   alt="Memory Leak walkthrough entrypoint in the Service Page" /%}

## What to expect{% #what-to-expect %}

Following this walkthrough requires zero prior knowledge, and it is accessible for first-time investigations.

The walkthrough guides you through several steps to:

1. Scope to the relevant data.
1. Recommend Datadog integrations and upgrades that assist in the investigation.
1. Explain how memory management works in your runtime.
1. Confirm potential memory leaks by inspecting retained objects using profile comparisons.

## Requirements{% #requirements %}

To use this walkthrough, you need:

- A containerized service with either the Datadog Kubernetes integration or the Datadog Container integration installed.
- [Continuous Profiler enabled](https://docs.datadoghq.com/profiler/enabling).
  - Ensure that your profiles are tagged with `container_id`. This is necessary to link between container memory utilization metrics and profiling data.
  - For Java ([Enabling the heap histogram metrics](https://docs.datadoghq.com/profiler/profiler_troubleshooting/java/?tab=jfr#enabling-the-heap-histogram-metrics)) and .NET ([Heap snapshot](https://docs.datadoghq.com/profiler/enabling/dotnet/#configuration)) ensure that heap profiling is enabled so that heap data is available for analysis.

## Get started{% #get-started %}

To investigate a memory leak using the guided walkthrough:

1. Go to **[APM > Software Catalog](https://app.datadoghq.com/services)**.
1. Hover over the service you want to investigate and click **Service Page**.
1. Click the **Memory Leaks** tab.
1. Follow the guided steps to complete your investigation.

## Further reading{% #further-reading %}

- [Datadog Continuous Profiler](https://docs.datadoghq.com/profiler)
- [Comparing Profiles](https://docs.datadoghq.com/profiler/compare_profiles/)
