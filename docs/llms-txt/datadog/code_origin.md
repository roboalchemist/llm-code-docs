# Source: https://docs.datadoghq.com/tracing/code_origin.md

---
title: Code Origin for Spans
description: >-
  Learn how to use Code Origin to understand where your spans originate in your
  codebase
breadcrumbs: Docs > APM > Code Origin for Spans
---

# Code Origin for Spans

## Overview{% #overview %}

Code Origin captures the exact locations in your codebase where APM spans are created. When enabled on a compatible service, it automatically adds file path, line number, and function name to each [service entry span](https://docs.datadoghq.com/glossary/#service-entry-span), making it easier to:

- Debug performance issues
- Understand code execution flow
- Identify performance bottlenecks

In Trace Explorer, select a span from an enabled service to see Code Origin details on the Overview tab:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/code_origin/code_origin_details_spotlight.10171a5059e9927169d8b0aab5a69ea0.png?auto=format"
   alt="Code Origin Details" /%}



## Getting started{% #getting-started %}

### Prerequisites{% #prerequisites %}

- [Datadog APM](https://docs.datadoghq.com/tracing/trace_collection/) is configured to capture spans.
- [Source Code Integration](https://docs.datadoghq.com/integrations/guide/source-code-integration/) is enabled (required for code previews).
- Your service meets the compatibility requirements.

### Compatibility requirements{% #compatibility-requirements %}

{% tab title="Java" %}

| Tracing Library Version | Frameworks                                                   |
| ----------------------- | ------------------------------------------------------------ |
| 1.47.0+                 | Spring Boot/Data, gRPC servers, Micronaut 4, Kafka consumers |

**Limitation:** On JDK 18 and below, classes compiled with the `-parameters` flag may not be supported. Spring 6+, Spring Boot 3+, and Scala use this flag by default.
{% /tab %}

{% tab title="Python" %}

| Tracing Library Version | Frameworks                                |
| ----------------------- | ----------------------------------------- |
| 2.15.0+                 | Django, Flask, Starlette, and derivatives |

{% /tab %}

{% tab title="Node.js" %}

| Tracing Library Version | Frameworks |
| ----------------------- | ---------- |
| 4.49.0+                 | Fastify    |
| 5.54.0+                 | Express    |

**Note:** NestJS is not supported, even though the underlying framework is either Express or Fastify.
{% /tab %}

{% tab title=".NET" %}

| Tracing Library Version | Frameworks            |
| ----------------------- | --------------------- |
| 3.15.0+                 | ASP.NET, ASP.NET Core |

{% /tab %}

### Enable Code Origin{% #enable-code-origin %}

Run your service with the following environment variable:

```shell
export DD_CODE_ORIGIN_FOR_SPANS_ENABLED=true
```

{% alert level="info" %}
For transpiled Node.js applications (for example, TypeScript), make sure to generate and publish source maps with the deployed application, run Node.js with the [`--enable-source-maps`](https://nodejs.org/docs/latest/api/cli.html#--enable-source-maps) flag, and use v5.59.0 or newer of the Node.js tracer. Otherwise, code previews do not work. See the Node.js [Source Code Integration](https://docs.datadoghq.com/integrations/guide/source-code-integration/?tab=nodejs#setup) documentation for more details.
{% /alert %}

## Using Code Origin{% #using-code-origin %}

### In the Trace Explorer{% #in-the-trace-explorer %}

1. Navigate to the [Trace Explorer](https://app.datadoghq.com/apm/traces).

1. Search for "Service Entry Spans" from your Code Origin-enabled services.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/code_origin/code_origin_service_entry_spans_filter.39f81532a0989c68548c6a3da007487a.png?auto=format"
      alt="Code Origin - Search for Service Entry Spans" /%}

1. Click on a span to view its details.

1. In the trace details side panel, look for the "Code Origin" section.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/code_origin/code_origin_details_spotlight.10171a5059e9927169d8b0aab5a69ea0.png?auto=format"
      alt="Code Origin Details in Traces Explorer" /%}

1. From the Code Origin section:

   - Kick off a [Live Debugger](https://docs.datadoghq.com/tracing/live_debugger/) session on the running service by clicking "Start Debug Session" to capture logs at the Code Origin method location. Or, select a breakpoint in the gutter of the code preview to capture logs at the selected line of code.

     {% image
        source="https://datadog-docs.imgix.net/images/tracing/code_origin/code_origin_start_debug_session.21c5483902fe2e45f85fa158dbbf42f8.png?auto=format"
        alt="Code Origin - Start Live Debugger Session" /%}

   - Click on source code variables to add them as attributes to future spans with [Dynamic Instrumentation](https://docs.datadoghq.com/dynamic_instrumentation/).

     {% image
        source="https://datadog-docs.imgix.net/images/tracing/code_origin/code_origin_add_span_tag_spotlight.e8ea782271c0a1337083c5791c735aaf.png?auto=format"
        alt="Code Origin - Add span tag with Dynamic Instrumentation" /%}

### In your IDE{% #in-your-ide %}

1. Set up your [Datadog IDE Integration](https://docs.datadoghq.com/developers/ide_plugins/).

   - Supported IDEs: IntelliJ, VS Code
   - Supported Languages: Java, Python

1. View RED metrics (Requests, Errors, and Duration) as inline annotations above your endpoint methods.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/code_origin/code_origin_ide_details.cc58ae4b94a1159222e11efe93da3e35.png?auto=format"
      alt="Code Origin Details in IDE" /%}

## Troubleshooting{% #troubleshooting %}

### Code Origin section is missing{% #code-origin-section-is-missing %}

- Verify Code Origin is enabled in your tracing library configuration.

- Confirm that your service meets all compatibility requirements (that is, service language, supported frameworks, and minimum tracer version).

- For most services, Code Origin data is captured for [service entry spans](https://docs.datadoghq.com/glossary/#service-entry-span) only. You can filter to "Service Entry Spans" in the [APM Trace Explorer](https://app.datadoghq.com/apm/traces).

  {% image
     source="https://datadog-docs.imgix.net/images/tracing/code_origin/code_origin_service_entry_spans_filter.39f81532a0989c68548c6a3da007487a.png?auto=format"
     alt="Code Origin - Search for Service Entry Spans" /%}

### Code preview is not visible or the file is not found{% #code-preview-is-not-visible-or-the-file-is-not-found %}

- Ensure all [Source Code Integration](https://docs.datadoghq.com/integrations/guide/source-code-integration/) setup requirements are met, including your `DD_GIT_*` environment variables are configured with the correct values.
- For transpiled Node.js applications (for example, TypeScript), make sure to generate and publish source maps with the deployed application, run Node.js with the [`--enable-source-maps`](https://nodejs.org/docs/latest/api/cli.html#--enable-source-maps) flag, and use v5.59.0 or newer of the Node.js tracer. Otherwise, code previews will not work. See the Node.js [Source Code Integration](https://docs.datadoghq.com/integrations/guide/source-code-integration/?tab=nodejs#setup) documentation for more details.
- Code Origin is designed to reference user code only, but in some cases, third-party code references may slip through. You can report these cases to [Datadog support](https://www.datadoghq.com/support/) and help improve these references.

## Further Reading{% #further-reading %}

- [Learn about APM terms and concepts](https://docs.datadoghq.com/tracing/glossary/)
- [Learn how to set up APM tracing with your application](https://docs.datadoghq.com/tracing/trace_collection/)
- [Learn more about services in Datadog](https://docs.datadoghq.com/tracing/services/service_page/)
- [Dive into your resource performance and traces](https://docs.datadoghq.com/tracing/services/resource_page/)
- [Learn how to debug production services with Live Debugger](https://docs.datadoghq.com/tracing/live_debugger/)
- [Learn how to add custom spans with Dynamic Instrumentation](https://docs.datadoghq.com/dynamic_instrumentation/)
