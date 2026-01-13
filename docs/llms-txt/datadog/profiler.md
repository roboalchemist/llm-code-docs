# Source: https://docs.datadoghq.com/profiler.md

---
title: Continuous Profiler
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Continuous Profiler
source_url: https://docs.datadoghq.com/index.html
---

# Continuous Profiler

Find CPU, memory, and IO bottlenecks, broken down by method name, class name, and line number, to significantly reduce end-user latency and infrastructure costs.

### Low impact in production{% #low-impact-in-production %}

Continuous profiler runs in production across all services by leveraging technologies such as JDK Flight Recorder to have minimal impact on your host's CPU and memory usage.

## Getting started{% #getting-started %}

Profiling your service to visualize all your stack traces in one place takes just minutes.

### Instrument your application{% #instrument-your-application %}

- [go](https://docs.datadoghq.com/profiler/enabling/go)
- [Java](https://docs.datadoghq.com/profiler/enabling/java)
- [Node.js](https://docs.datadoghq.com/profiler/enabling/nodejs)
- [PHP](https://docs.datadoghq.com/profiler/enabling/php)
- [Python](https://docs.datadoghq.com/profiler/enabling/python)
- [Ruby](https://docs.datadoghq.com/profiler/enabling/ruby)
- [.NET](https://docs.datadoghq.com/profiler/enabling/dotnet)
- [Rust](https://docs.datadoghq.com/profiler/enabling/ddprof)
- [C](https://docs.datadoghq.com/profiler/enabling/ddprof)
- [C++](https://docs.datadoghq.com/profiler/enabling/ddprof)

## Guide to using the profiler{% #guide-to-using-the-profiler %}

The [Getting Started with Profiler](https://docs.datadoghq.com/getting_started/profiler/) guide takes a sample service with a performance problem and shows you how to use Continuous Profiler to understand and fix the problem.

## Explore Datadog profiler{% #explore-datadog-profiler %}

After you configure your application to send profiles to Datadog, start getting insights into your code performance.

By default, profiles are retained for seven days, and metrics generated from profile data are retained for one month.

{% callout %}
##### Try Diagnose Code Performance Issues in the Learning Center

The Datadog Learning Center is full of hands-on courses to help you learn about this topic. Enroll at no cost to investigate and improve application code performance in production with Datadog Continuous Profiler.

[ENROLL NOW](https://learn.datadoghq.com/courses/continuous-profiler-course)
{% /callout %}

### Profile types{% #profile-types %}

See [Profile Types](https://docs.datadoghq.com/profiler/profile_types/) for descriptions of the kinds of profile data collected for each supported language.

{% image
   source="https://datadog-docs.imgix.net/images/profiler/profile-types.d54490df9c84d66ec1a7f42c5978d6fc.png?auto=format"
   alt="The list of profile types collected for Java applications" /%}

### Search profiles by tags{% #search-profiles-by-tags %}

[Use tags to search profiles](https://docs.datadoghq.com/profiler/search_profiles) across any dimensionâwhether it's a specific host, service, version, or any combination.

{% video
   url="https://datadog-docs.imgix.net/images/profiler/search_profiles2.mp4" /%}

### Track function performance over deployments{% #track-function-performance-over-deployments %}

Obtain key profiling metrics from services such as top CPU usage by method, top memory allocations by thread, and CPU usage by version to visualize in your dashboards.

{% video
   url="https://datadog-docs.imgix.net/images/profiler/profiling-metric-dashboard.mp4" /%}

### Connect traces to profiling data{% #connect-traces-to-profiling-data %}

Application processes that have both [APM distributed tracing](https://docs.datadoghq.com/tracing/) and continuous profiler enabled are automatically linked, so you can move directly from span information to profiling data on the [Profiles tab](https://docs.datadoghq.com/profiler/connect_traces_and_profiles/) to find specific lines of code related to performance issues.

{% image
   source="https://datadog-docs.imgix.net/images/profiler/profiles_tab.0e581f4836c2c600a56470f30a4c1ecf.png?auto=format"
   alt="Profiles tab shows profiling information for a APM trace span" /%}

### Find changes in performance by comparing profiles{% #find-changes-in-performance-by-comparing-profiles %}

Comparing similar profiles from different times, environments, or deployments can help you understand the possible causes of and solutions to performance problems. The Datadog profiler offers [comparison visualizations](https://docs.datadoghq.com/profiler/compare_profiles/) to make sense of why profiles are different based on time frames or tags that you scope by.

## Further Reading{% #further-reading %}

- [Enable continuous profiler for your application](https://docs.datadoghq.com/profiler/enabling)
- [Getting Started with Continuous Profiler](https://docs.datadoghq.com/getting_started/profiler)
- [Learn more about available profile types](https://docs.datadoghq.com/profiler/search_profiles)
- [Data collection and resolution](https://docs.datadoghq.com/developers/guide/data-collection-resolution/)
- [Focus on code that matters with source code previews in Continuous Profiler](https://www.datadoghq.com/blog/source-code-preview/)
- [Introducing always-on production profiling in Datadog](https://www.datadoghq.com/blog/introducing-datadog-profiling/)
- [Datadog GitHub Action for continuous vulnerability analysis](https://www.datadoghq.com/blog/datadog-github-action-vulnerability-analysis/)
- [Compare and optimize your code with Datadog Profile Comparison.](https://www.datadoghq.com/blog/code-optimization-datadog-profile-comparison/)
- [How we optimized our Akka application using Datadog's Continuous Profiler](https://www.datadoghq.com/blog/engineering/how-we-optimized-our-akka-application-using-datadogs-continuous-profiler/)
- [Analyze Ruby code performance with Datadog Continuous Profiler](https://www.datadoghq.com/blog/ruby-profiling-datadog-continuous-profiler/)
- [How our Cloud SIEM team uses context attributes with Continuous Profiler to get crucial performance insights](https://www.datadoghq.com/blog/continuous-profiler-context-attributes/)
- [Making profiling visualizations accessible to engineers at all levels](https://www.datadoghq.com/blog/profiling-visualizations/)
- [Why continuous profiling is the fourth pillar of observability](https://www.datadoghq.com/blog/continuous-profiling-fourth-pillar/)
- [Monitor your Kubernetes operators to keep applications running smoothly](https://www.datadoghq.com/blog/kubernetes-operator-performance)
- [Troubleshoot faster with the GitLab Source Code integration in Datadog](https://www.datadoghq.com/blog/gitlab-source-code-integration)
