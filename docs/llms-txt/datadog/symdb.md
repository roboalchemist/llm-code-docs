# Source: https://docs.datadoghq.com/tracing/trace_collection/dynamic_instrumentation/symdb.md

---
title: Autocomplete and Search
description: >-
  Enable IDE-like autocomplete and search functionality for Dynamic
  Instrumentation to improve developer experience.
breadcrumbs: >-
  Docs > APM > Application Instrumentation > Dynamic Instrumentation >
  Autocomplete and Search
---

# Autocomplete and Search

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### Join the Preview!

Autocomplete and search are in Preview for Python and .NET.
{% /callout %}

## Overview{% #overview %}

Autocomplete and search enhance the user experience of [Dynamic Instrumentation](https://docs.datadoghq.com/dynamic_instrumentation/) by adding IDE-like features like class and method search and autocomplete for [Dynamic Instrumentation Expression Language](https://docs.datadoghq.com/dynamic_instrumentation/expression-language).

To provide autocomplete and search, nonsensitive symbols and metadata are uploaded from your application to Datadog. The uploaded data includes the names of classes, methods, arguments, fields, and local variables, along with related metadata, like line numbers.

## Getting started{% #getting-started %}

### Prerequisites{% #prerequisites %}

Autocomplete and search require the following:

- [Dynamic Instrumentation](https://docs.datadoghq.com/dynamic_instrumentation/) is enabled for your service.
- [Datadog Agent](https://docs.datadoghq.com/agent/) 7.49.0 or higher is installed alongside your service.
- [Remote Configuration](https://docs.datadoghq.com/tracing/guide/remote_config) is enabled in the Agent.
- The [Unified Service Tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/) tags `service`, `env`, and `version` are applied to your deployment.

### Enable autocomplete and search for your service{% #enable-autocomplete-and-search-for-your-service %}

Select your runtime below:

- [Java](https://docs.datadoghq.com/dynamic_instrumentation/symdb/java)
- [Python](https://docs.datadoghq.com/dynamic_instrumentation/symdb/python)
- [Dotnet](https://docs.datadoghq.com/dynamic_instrumentation/symdb/dotnet)
- [Dotnet](https://docs.datadoghq.com/dynamic_instrumentation/symdb/dotnet)

## Explore autocomplete and search{% #explore-autocomplete-and-search %}

With autocomplete and search, the user experience of Dynamic Instrumentation is improved to behave more like an IDE.

Dynamic Instrumentation provides search for class and method names:

{% image
   source="https://datadog-docs.imgix.net/images/dynamic_instrumentation/symdb_method_search.fed394a5243c49a3bc5adecce2f8b695.png?auto=format"
   alt="Search for methods when creating a Dynamic Instrumentation log probe" /%}



When you select a method in the Dynamic Instrumentation configuration, the code for that method is displayed:

{% image
   source="https://datadog-docs.imgix.net/images/dynamic_instrumentation/symdb_method_highlight.3c2c5b425699884c6e013a51c7143351.png?auto=format"
   alt="Autocomplete and search highlights the selected method" /%}



Dynamic Instrumentation also provides autocomplete for log templates and other templates that use the [Dynamic Instrumentation expression language](https://docs.datadoghq.com/dynamic_instrumentation/expression-language):

{% image
   source="https://datadog-docs.imgix.net/images/dynamic_instrumentation/symdb_completion.65cd4c4059701781f26889ca2167d787.png?auto=format"
   alt="Autocomplete suggestions for log templates" /%}



## Further Reading{% #further-reading %}

- [Learn more about Dynamic Instrumentation](https://docs.datadoghq.com/dynamic_instrumentation/)
