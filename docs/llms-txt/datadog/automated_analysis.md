# Source: https://docs.datadoghq.com/profiler/automated_analysis.md

---
title: Automated Analysis
description: >-
  Automatically surface critical issues with contextual insights and recommended
  next steps
breadcrumbs: Docs > Continuous Profiler > Automated Analysis
source_url: https://docs.datadoghq.com/automated_analysis/index.html
---

# Automated Analysis

{% callout %}
##### Join the Preview!

Automated Analysis is in Preview.

[Request Access](https://www.datadoghq.com/product-preview/automated-analysis/)
{% /callout %}

## Overview{% #overview %}

Automated Analysis automatically detects performance issues in your applications using Continuous Profiler data and provides actionable insights for resolution. When an issue is detected, Automated Analysis provides:

- A high-level summary explaining the issue and why it matters
- Contextual insights from profiling data (for example, affected methods, packages, or processes)
- Recommended next steps to help you resolve the issue

This reduces the profiling expertise needed to identify and resolve performance issues in your applications that might otherwise go unnoticed.

{% image
   source="https://datadog-docs.imgix.net/images/profiler/profiling_automated_analysis_detail.8c4ac81691d0649cc5ccfc112ae298ef.png?auto=format"
   alt="The Profiler Thread Time line showing a Thrown Exception insight" /%}

## Explore insights{% #explore-insights %}

Access Automated Analysis from the [Profile explorer](https://app.datadoghq.com/profiling/explorer). Insights are displayed:

- In the **Insights** section at the top of the page

  {% image
     source="https://datadog-docs.imgix.net/images/profiler/profiling_automated_analysis_section.4078514aa3810e986b62a116a3657118.png?auto=format"
     alt="The Automated Analysis banner displaying insights detected for a given service" /%}



- Within a flame graph view

  {% image
     source="https://datadog-docs.imgix.net/images/profiler/profiling_automated_analysis_flamegraph.f188f4ceefb116361190e440874e8b2b.png?auto=format"
     alt="The Automated Analysis column displaying insights detected for a given service within a flamegraph" /%}



- Within a timeline view

  {% image
     source="https://datadog-docs.imgix.net/images/profiler/profiling_automated_analysis_thread_timeline.d920953bee1566336d996b3419af9e18.png?auto=format"
     alt="The Automated Analysis column displaying insights detected for a given service within a timeline" /%}

Click an insight to see a high-level summary that explains the issue, contextual insights from profiling data, and recommended next steps.

{% image
   source="https://datadog-docs.imgix.net/images/profiler/profiling_automated_analysis_detail.8c4ac81691d0649cc5ccfc112ae298ef.png?auto=format"
   alt="Expanded Profiling Insights showing the details of a detected Issue" /%}



The Insights list page provides a centralized view of all detected issues across your services. It helps teams understand what's happening in their environments, prioritize what to investigate, and track whether recurring problems are improving over time.

{% image
   source="https://datadog-docs.imgix.net/images/profiler/profiling_automated_analysis_list_page_home.73a600e6ff2bf9d5c01d499dd7848b76.png?auto=format"
   alt="The list page showing detected insights across services" /%}

Each row represents an insight type, summarizing:

- Service and runtime affected
- Insight type (for example, GC Pauses or High Lock Contention)
- Severity (for example, Info or Warning)

You can filter insights by runtime, service, or environment to narrow the list to the most important insights. Teams often use this view to identify patterns, such as multiple services affected by the same inefficiency. Clicking on an insight opens its detail panel.

## Supported insights{% #supported-insights %}

Automated Analysis supports finding the following insights:

{% tab title="Java" %}

| Name                          | Priority | Description                                                                                                                                                                                                                    |
| ----------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Virtual Thread Pinning        | High     | Triggers if virtual threads were pinned to their carrier threads for a prolonged time.                                                                                                                                         |
| Virtual Thread Submit Failure | High     | Triggers if virtual threads could not be scheduled for execution.                                                                                                                                                              |
| Allocation Stall              | Medium   | Triggers if a thread had to be paused due to insufficient available memory.                                                                                                                                                    |
| Blocking VMOperations         | Medium   | Triggers if blocking VM operations (or combination of operations close in time) take more than 5% of a profile.                                                                                                                |
| Code Cache Size               | Medium   | Triggers if the Code Cache was filled during a profile.                                                                                                                                                                        |
| CPU Burst                     | Medium   | Triggers if there is more than 75% CPU utilization across a 10s window.                                                                                                                                                        |
| CPU Burst Saturation          | Medium   | Triggers if there is at least 1 second where CPU utilization is at 100%.                                                                                                                                                       |
| Deadlocked Threads Detected   | Medium   | Triggers if max number of deadlocked threads over query context is greater than 0.                                                                                                                                             |
| Explicit GC                   | Medium   | Triggers if there are `System.gc()` calls.                                                                                                                                                                                     |
| GC Pause Peak Duration        | Medium   | Triggers if at least one GC pause took more than one second.                                                                                                                                                                   |
| GC Pauses                     | Medium   | Triggers if more than 10% of time was spent in GC pauses.                                                                                                                                                                      |
| GC Setup                      | Medium   | Triggers when one of the following is detected: serial GC used on a multi-core machine, parallel GC on a single-core machine, more GC threads configured than available cores, or parallel GC configured to run in one thread. |
| Stackdepth Setting            | Medium   | Triggers if events were found with truncated stacktraces which may make it hard to understand profiling data.                                                                                                                  |
| Thrown Exceptions             | Medium   | Triggers when the rate of thrown (caught and uncaught) exceptions per minute goes above a threshold (defaults to 10K).                                                                                                         |
| VMOperation Peak Duration     | Medium   | Triggers if a blocking VM operation (or combination of operations close in time) takes more than two seconds. Reports details about the operation with the highest duration.                                                   |
| VMOperations Ratio            | Medium   | Triggers if the total amount of blocking VM operations is a significant part of a 60 second window.                                                                                                                            |
| Command Line Options Check    | Low      | Triggers if undocumented, deprecated, or non-recommended option flags were detected.                                                                                                                                           |
| Context Switches              | Low      | Triggers if the rate of context switches on the underlying system is greater than 50k per second.                                                                                                                              |
| DebugNonSafepoints            | Low      | Triggers if a service is run with potentially less accurate settings for the profiler.                                                                                                                                         |
| Duplicated Flags              | Low      | Triggers if duplicate flags were provided to the runtime (for example, `-Xmx2g -Xmx5g`). This is a problem as it may lead to changes not having the expected effect.                                                           |
| GC Overhead                   | Low      | Triggers if more than 20% of CPU time is related to GC activities or allocation overhead.                                                                                                                                      |
| Head of line blocking         | Low      | Triggers if a queue event gets stuck behind the given activity.                                                                                                                                                                |
| High Lock Contention          | Low      | Triggers if there is a high ratio of time waiting on locks to time spent on-CPU.                                                                                                                                               |
| Primitive Value Boxing        | Low      | Triggers if more than 5% of CPU time was spent converting values between primitive and object values.                                                                                                                          |
| Thread Pool Size              | Low      | Triggers if a thread pool is CPU-bound but is set to a size larger than the number of available cores.                                                                                                                         |
| Unbalanced Parallelism        | Low      | Triggers if at least one peer thread is performing less than half the work of another in the same span.                                                                                                                        |

{% /tab %}

{% tab title="Python" %}

| Name                 | Priority | Description                                                                      |
| -------------------- | -------- | -------------------------------------------------------------------------------- |
| High Lock Contention | Low      | Triggers if there is a high ratio of time waiting on locks to time spent on-CPU. |

{% /tab %}

{% tab title="Go" %}

| Name                 | Priority | Description                                                                               |
| -------------------- | -------- | ----------------------------------------------------------------------------------------- |
| GC Overhead          | Low      | Triggers if more than 20% of CPU time is related to GC activities or allocation overhead. |
| High Lock Contention | Low      | Triggers if there is a high ratio of time waiting on locks to time spent on-CPU.          |

{% /tab %}

{% tab title="Ruby" %}

| Name        | Priority | Description                                                                               |
| ----------- | -------- | ----------------------------------------------------------------------------------------- |
| GC Overhead | Low      | Triggers if more than 20% of CPU time is related to GC activities or allocation overhead. |

{% /tab %}

{% tab title="Node.js" %}

| Name                | Priority | Description                                                                                                 |
| ------------------- | -------- | ----------------------------------------------------------------------------------------------------------- |
| Event Loop Blocking | Medium   | Triggers if callbacks were running for an extended period of time on the Main Event Loop thread.            |
| GC Overhead         | Low      | Triggers if more than 20% of CPU time is related to GC activities or allocation overhead.                   |
| Libuv Pool Overload | Low      | Triggers if there were more concurrent tasks scheduled to run on the libuv thread pool than it has threads. |

{% /tab %}

{% tab title=".NET" %}

| Name                           | Priority | Description                                                                      |
| ------------------------------ | -------- | -------------------------------------------------------------------------------- |
| Sync-over-Async Blocking       | Medium   | Triggers if async functions are detected in CPU samples.                         |
| High Lock Contention           | Low      | Triggers if there is a high ratio of time waiting on locks to time spent on-CPU. |
| Exception Overhead             | Medium   | Triggers if an excessive amount of exceptions is thrown.                         |
| Excessive String Concatenation | Low      | Triggers if there is a high ratio of CPU time spent concatenating strings.       |
| GC Overhead                    | Low      | Triggers if more than 20% of CPU time is related to GC activities.               |

{% /tab %}

## Further reading{% #further-reading %}

- [Enable continuous profiler for your application](https://docs.datadoghq.com/profiler/enabling)
- [Getting Started with Profiler](https://docs.datadoghq.com/getting_started/profiler)
- [Introducing always-on production profiling in Datadog](https://www.datadoghq.com/blog/introducing-datadog-profiling/)
- [Diagnose runtime and code inefficiencies using Continuous Profiler's timeline view](https://www.datadoghq.com/blog/continuous-profiler-timeline-view/)
