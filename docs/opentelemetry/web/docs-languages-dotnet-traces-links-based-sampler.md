# Source: https://opentelemetry.io/docs/languages/dotnet/traces/links-based-sampler/

Title: Links-based sampling

URL Source: https://opentelemetry.io/docs/languages/dotnet/traces/links-based-sampler/

Markdown Content:
Links-based sampling | OpenTelemetry
===============

[OpenTelemetry](https://opentelemetry.io/)

*   [Docs](https://opentelemetry.io/docs/)
*   [Ecosystem](https://opentelemetry.io/ecosystem/)
*   [Status](https://opentelemetry.io/status/)
*   [Community](https://opentelemetry.io/community/)
*   [Training](https://opentelemetry.io/training/)
*   [Blog](https://opentelemetry.io/blog/)
*   
[English EN](https://opentelemetry.io/docs/languages/dotnet/traces/links-based-sampler/#)
    *   [বাংলা (Bengali)](https://opentelemetry.io/bn/docs/languages/dotnet/traces/links-based-sampler/)
    *   English
    *   [Español](https://opentelemetry.io/es/docs/languages/dotnet/traces/links-based-sampler/)
    *   [Français](https://opentelemetry.io/fr/docs/languages/dotnet/traces/links-based-sampler/)
    *   [日本語 (Japanese)](https://opentelemetry.io/ja/docs/languages/dotnet/traces/links-based-sampler/)
    *   [Português](https://opentelemetry.io/pt/docs/languages/dotnet/traces/links-based-sampler/)
    *   [Română (Romanian)](https://opentelemetry.io/ro/docs/languages/dotnet/traces/links-based-sampler/)
    *   [Українська (Ukrainian)](https://opentelemetry.io/uk/docs/languages/dotnet/traces/links-based-sampler/)
    *   [中文 (Chinese)](https://opentelemetry.io/zh/docs/languages/dotnet/traces/links-based-sampler/)

*   
    *    Light 
    *    Dark 
    *    Auto 

*   [Docs](https://opentelemetry.io/docs/ "Documentation")
    *   - [x] [What is OpenTelemetry?](https://opentelemetry.io/docs/what-is-opentelemetry/) 
    *   - [x] [Getting Started](https://opentelemetry.io/docs/getting-started/) 
        *   - [x] [Dev](https://opentelemetry.io/docs/getting-started/dev/ "Getting started for Developers") 
        *   - [x] [Ops](https://opentelemetry.io/docs/getting-started/ops/ "Getting started for Ops") 

    *   - [x] [Concepts](https://opentelemetry.io/docs/concepts/ "OpenTelemetry Concepts") 
        *   - [x] [Observability primer](https://opentelemetry.io/docs/concepts/observability-primer/) 
        *   - [x] [Context propagation](https://opentelemetry.io/docs/concepts/context-propagation/) 
        *   - [x] [Signals](https://opentelemetry.io/docs/concepts/signals/) 
            *   - [x] [Traces](https://opentelemetry.io/docs/concepts/signals/traces/) 
            *   - [x] [Metrics](https://opentelemetry.io/docs/concepts/signals/metrics/) 
            *   - [x] [Logs](https://opentelemetry.io/docs/concepts/signals/logs/) 
            *   - [x] [Baggage](https://opentelemetry.io/docs/concepts/signals/baggage/) 

        *   - [x] [Instrumentation](https://opentelemetry.io/docs/concepts/instrumentation/) 
            *   - [x] [Zero-code](https://opentelemetry.io/docs/concepts/instrumentation/zero-code/) 
            *   - [x] [Code-based](https://opentelemetry.io/docs/concepts/instrumentation/code-based/) 
            *   - [x] [Libraries](https://opentelemetry.io/docs/concepts/instrumentation/libraries/) 

        *   - [x] [Components](https://opentelemetry.io/docs/concepts/components/) 
        *   - [x] [Semantic Conventions](https://opentelemetry.io/docs/concepts/semantic-conventions/) 
        *   - [x] [Resources](https://opentelemetry.io/docs/concepts/resources/) 
        *   - [x] [Instrumentation scope](https://opentelemetry.io/docs/concepts/instrumentation-scope/) 
        *   - [x] [Sampling](https://opentelemetry.io/docs/concepts/sampling/) 
        *   - [x] [Distributions](https://opentelemetry.io/docs/concepts/distributions/) 
        *   - [x] [Glossary](https://opentelemetry.io/docs/concepts/glossary/) 

    *   - [x] [Demo](https://opentelemetry.io/docs/demo/ "OpenTelemetry Demo Docs") 
        *   - [x] [Architecture](https://opentelemetry.io/docs/demo/architecture/ "Demo Architecture") 
        *   - [x] [Collector Data Flow Dashboard](https://opentelemetry.io/docs/demo/collector-data-flow-dashboard/) 
        *   - [x] [Development](https://opentelemetry.io/docs/demo/development/) 
        *   - [x] [Docker](https://opentelemetry.io/docs/demo/docker-deployment/ "Docker deployment") 
        *   - [x] [Feature Flags](https://opentelemetry.io/docs/demo/feature-flags/) 
            *   - [x] [Diagnosing memory leaks](https://opentelemetry.io/docs/demo/feature-flags/recommendation-cache/ "Using Metrics and Traces to diagnose a memory leak") 

        *   - [x] [Forking](https://opentelemetry.io/docs/demo/forking/ "Forking the demo repository") 
        *   - [x] [Kubernetes](https://opentelemetry.io/docs/demo/kubernetes-deployment/ "Kubernetes deployment") 
        *   - [x] [Requirements](https://opentelemetry.io/docs/demo/requirements/ "Demo Requirements") 
            *   - [x] [Application](https://opentelemetry.io/docs/demo/requirements/application/ "Application Requirements") 
            *   - [x] [Architecture](https://opentelemetry.io/docs/demo/requirements/architecture/ "Architecture Requirements") 
            *   - [x] [OTel Requirements](https://opentelemetry.io/docs/demo/requirements/opentelemetry/ "OpenTelemetry Requirements") 
            *   - [x] [System](https://opentelemetry.io/docs/demo/requirements/system/ "System Requirements") 

        *   - [x] [Screenshots](https://opentelemetry.io/docs/demo/screenshots/ "Demo Screenshots") 
        *   - [x] [Services](https://opentelemetry.io/docs/demo/services/) 
            *   - [x] [Accounting](https://opentelemetry.io/docs/demo/services/accounting/ "Accounting Service") 
            *   - [x] [Ad](https://opentelemetry.io/docs/demo/services/ad/ "Ad Service") 
            *   - [x] [Cart](https://opentelemetry.io/docs/demo/services/cart/ "Cart Service") 
            *   - [x] [Checkout](https://opentelemetry.io/docs/demo/services/checkout/ "Checkout Service") 
            *   - [x] [Currency](https://opentelemetry.io/docs/demo/services/currency/ "Currency Service") 
            *   - [x] [Email](https://opentelemetry.io/docs/demo/services/email/ "Email Service") 
            *   - [x] [Flagd-UI](https://opentelemetry.io/docs/demo/services/flagd-ui/ "Flagd-UI Service") 
            *   - [x] [Fraud Detection](https://opentelemetry.io/docs/demo/services/fraud-detection/ "Fraud Detection Service") 
            *   - [x] [Frontend](https://opentelemetry.io/docs/demo/services/frontend/) 
            *   - [x] [Frontend Proxy](https://opentelemetry.io/docs/demo/services/frontend-proxy/ "Frontend Proxy (Envoy)") 
            *   - [x] [Image Provider](https://opentelemetry.io/docs/demo/services/image-provider/ "Image Provider Service") 
            *   - [x] [Kafka](https://opentelemetry.io/docs/demo/services/kafka/) 
            *   - [x] [Load Generator](https://opentelemetry.io/docs/demo/services/load-generator/) 
            *   - [x] [Payment](https://opentelemetry.io/docs/demo/services/payment/ "Payment Service") 
            *   - [x] [Product Catalog](https://opentelemetry.io/docs/demo/services/product-catalog/ "Product Catalog Service") 
            *   - [x] [Product Reviews](https://opentelemetry.io/docs/demo/services/product-reviews/ "Product Reviews Service") 
            *   - [x] [Quote](https://opentelemetry.io/docs/demo/services/quote/ "Quote Service") 
            *   - [x] [React Native App](https://opentelemetry.io/docs/demo/services/react-native-app/) 
            *   - [x] [Recommendation](https://opentelemetry.io/docs/demo/services/recommendation/ "Recommendation Service") 
            *   - [x] [Shipping](https://opentelemetry.io/docs/demo/services/shipping/ "Shipping Service") 

        *   - [x] [Telemetry Features](https://opentelemetry.io/docs/demo/telemetry-features/) 
            *   - [x] [Log Coverage](https://opentelemetry.io/docs/demo/telemetry-features/log-coverage/ "Log Coverage by Service") 
            *   - [x] [Manual Span Attributes](https://opentelemetry.io/docs/demo/telemetry-features/manual-span-attributes/) 
            *   - [x] [Metric Coverage](https://opentelemetry.io/docs/demo/telemetry-features/metric-coverage/ "Metric Coverage by Service") 
            *   - [x] [Trace Coverage](https://opentelemetry.io/docs/demo/telemetry-features/trace-coverage/ "Trace Coverage by Service") 

        *   - [x] [Tests](https://opentelemetry.io/docs/demo/tests/) 

    *   - [x] [Language APIs & SDKs](https://opentelemetry.io/docs/languages/) 
        *   - [x] [SDK Config](https://opentelemetry.io/docs/languages/sdk-configuration/ "SDK Configuration") 
            *   - [x] [General](https://opentelemetry.io/docs/languages/sdk-configuration/general/ "General SDK Configuration") 
            *   - [x] [OTLP Exporter](https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/ "OTLP Exporter Configuration") 
            *   - [x] [Declarative configuration](https://opentelemetry.io/docs/languages/sdk-configuration/declarative-configuration/) 

        *   - [x] [C++](https://opentelemetry.io/docs/languages/cpp/) 
            *   - [x] [Getting Started](https://opentelemetry.io/docs/languages/cpp/getting-started/) 
            *   - [x] [Instrumentation](https://opentelemetry.io/docs/languages/cpp/instrumentation/) 
            *   - [x] [Libraries](https://opentelemetry.io/docs/languages/cpp/library/ "Using instrumentation libraries") 
            *   - [x] [Exporters](https://opentelemetry.io/docs/languages/cpp/exporters/) 
            *   - [x] [API](https://opentelemetry.io/docs/languages/cpp/api/ "API reference") 
            *   - [x] [Examples](https://opentelemetry.io/docs/languages/cpp/examples/) 
            *   - [x] [Registry](https://opentelemetry.io/docs/languages/cpp/registry/) 

        *   - [x] [.NET](https://opentelemetry.io/docs/languages/dotnet/) 
            *   - [x] [Getting Started](https://opentelemetry.io/docs/languages/dotnet/getting-started/) 
            *   - [x] [Traces](https://opentelemetry.io/docs/languages/dotnet/traces/ "OpenTelemetry .NET traces") 
                *   - [x] [Console](https://opentelemetry.io/docs/languages/dotnet/traces/getting-started-console/ "Getting started with traces - Console") 
                *   - [x] [ASP.NET Core](https://opentelemetry.io/docs/languages/dotnet/traces/getting-started-aspnetcore/ "Getting started with traces - ASP.NET Core") 
                *   - [x] [Stratified sampling](https://opentelemetry.io/docs/languages/dotnet/traces/stratified-sampling/) 
                *   - [x] [Tail-based sampling](https://opentelemetry.io/docs/languages/dotnet/traces/tail-based-sampling/) 
                *   - [x] [Export to Jaeger](https://opentelemetry.io/docs/languages/dotnet/traces/jaeger/) 
                *   - [x] [Exceptions](https://opentelemetry.io/docs/languages/dotnet/traces/reporting-exceptions/ "Reporting exceptions") 
                *   - [x] [Links](https://opentelemetry.io/docs/languages/dotnet/traces/links-creation/ "Creating links between traces") 
                *   - [x] [Links-based sampling](https://opentelemetry.io/docs/languages/dotnet/traces/links-based-sampler/) 
                *   - [x] [Best practices](https://opentelemetry.io/docs/languages/dotnet/traces/best-practices/) 

            *   - [x] [Metrics](https://opentelemetry.io/docs/languages/dotnet/metrics/ "OpenTelemetry .NET metrics") 
                *   - [x] [Console](https://opentelemetry.io/docs/languages/dotnet/metrics/getting-started-console/ "Getting started with metrics - Console") 
                *   - [x] [ASP.NET Core](https://opentelemetry.io/docs/languages/dotnet/metrics/getting-started-aspnetcore/ "Getting started with metrics - ASP.NET Core") 
                *   - [x] [Export to Prometheus](https://opentelemetry.io/docs/languages/dotnet/metrics/getting-started-prometheus-grafana/ "Export to Prometheus and Grafana") 
                *   - [x] [Exemplars](https://opentelemetry.io/docs/languages/dotnet/metrics/exemplars/ "Using exemplars") 
                *   - [x] [Instruments](https://opentelemetry.io/docs/languages/dotnet/metrics/instruments/ "Metric instruments") 
                *   - [x] [Best practices](https://opentelemetry.io/docs/languages/dotnet/metrics/best-practices/) 

            *   - [x] [Logs](https://opentelemetry.io/docs/languages/dotnet/logs/ "OpenTelemetry .NET logs") 
                *   - [x] [Console](https://opentelemetry.io/docs/languages/dotnet/logs/getting-started-console/ "Getting started with logs - Console") 
                *   - [x] [ASP.NET Core](https://opentelemetry.io/docs/languages/dotnet/logs/getting-started-aspnetcore/ "Getting started with logs - ASP.NET Core") 
                *   - [x] [Complex objects](https://opentelemetry.io/docs/languages/dotnet/logs/complex-objects/ "Logging complex objects") 
                *   - [x] [Correlation](https://opentelemetry.io/docs/languages/dotnet/logs/correlation/ "Log correlation") 
                *   - [x] [Dedicated pipeline](https://opentelemetry.io/docs/languages/dotnet/logs/dedicated-pipeline/ "Setting up a dedicated logging pipeline") 
                *   - [x] [Redaction](https://opentelemetry.io/docs/languages/dotnet/logs/redaction/ "Log redaction") 
                *   - [x] [Best practices](https://opentelemetry.io/docs/languages/dotnet/logs/best-practices/) 

            *   - [x] [Instrumentation](https://opentelemetry.io/docs/languages/dotnet/instrumentation/) 
            *   - [x] [Libraries](https://opentelemetry.io/docs/languages/dotnet/libraries/ "Using instrumentation libraries") 
            *   - [x] [Resources](https://opentelemetry.io/docs/languages/dotnet/resources/ "Resources in OpenTelemetry .NET") 
            *   - [x] [Exporters](https://opentelemetry.io/docs/languages/dotnet/exporters/) 
            *   - [x] [.NET Framework](https://opentelemetry.io/docs/languages/dotnet/netframework/ ".NET Framework instrumentation configuration") 
            *   - [x] [Troubleshooting](https://opentelemetry.io/docs/languages/dotnet/troubleshooting/) 
            *   - [x] [Tracing Shim](https://opentelemetry.io/docs/languages/dotnet/shim/ "OpenTelemetry Tracing Shim") 
            *   - [x] [API - tracing](https://opentelemetry.io/docs/languages/dotnet/traces-api/ "Tracing API reference") 
            *   - [x] [API - metrics](https://opentelemetry.io/docs/languages/dotnet/metrics-api/ "Metrics API reference") 
            *   - [x] [Examples](https://opentelemetry.io/docs/languages/dotnet/examples/) 
            *   - [x] [Registry](https://opentelemetry.io/docs/languages/dotnet/registry/) 

        *   - [x] [Erlang/Elixir](https://opentelemetry.io/docs/languages/erlang/) 
            *   - [x] [Getting Started](https://opentelemetry.io/docs/languages/erlang/getting-started/) 
            *   - [x] [Instrumentation](https://opentelemetry.io/docs/languages/erlang/instrumentation/) 
            *   - [x] [Libraries](https://opentelemetry.io/docs/languages/erlang/libraries/ "Using instrumentation libraries") 
            *   - [x] [Exporters](https://opentelemetry.io/docs/languages/erlang/exporters/) 
            *   - [x] [Propagation](https://opentelemetry.io/docs/languages/erlang/propagation/) 
            *   - [x] [Resources](https://opentelemetry.io/docs/languages/erlang/resources/) 
            *   - [x] [Sampling](https://opentelemetry.io/docs/languages/erlang/sampling/) 
            *   - [x] [Testing](https://opentelemetry.io/docs/languages/erlang/testing/) 
            *   - [x] [API](https://opentelemetry.io/docs/languages/erlang/api/ "API reference") 
            *   - [x] [Examples](https://opentelemetry.io/docs/languages/erlang/examples/) 
            *   - [x] [Registry](https://opentelemetry.io/docs/languages/erlang/registry/) 

        *   - [x] [Go](https://opentelemetry.io/docs/languages/go/) 
            *   - [x] [Getting Started](https://opentelemetry.io/docs/languages/go/getting-started/) 
            *   - [x] [Instrumentation](https://opentelemetry.io/docs/languages/go/instrumentation/) 
            *   - [x] [Libraries](https://opentelemetry.io/docs/languages/go/libraries/ "Using instrumentation libraries") 
            *   - [x] [Exporters](https://opentelemetry.io/docs/languages/go/exporters/) 
            *   - [x] [Resources](https://opentelemetry.io/docs/languages/go/resources/) 
            *   - [x] [Sampling](https://opentelemetry.io/docs/languages/go/sampling/) 
            *   - [x] [API](https://opentelemetry.io/docs/languages/go/api/ "API reference") 
            *   - [x] [Examples](https://opentelemetry.io/docs/languages/go/examples/) 
            *   - [x] [Registry](https://opentelemetry.io/docs/languages/go/registry/) 

        *   - [x] [Java](https://opentelemetry.io/docs/languages/java/) 
            *   - [x] [Intro to OpenTelemetry Java](https://opentelemetry.io/docs/languages/java/intro/) 
            *   - [x] [Getting Started by Example](https://opentelemetry.io/docs/languages/java/getting-started/) 
            *   - [x] [Instrumentation ecosystem](https://opentelemetry.io/docs/languages/java/instrumentation/) 
            *   - [x] [Record Telemetry with API](https://opentelemetry.io/docs/languages/java/api/) 
            *   - [x] [Manage Telemetry with SDK](https://opentelemetry.io/docs/languages/java/sdk/) 
            *   - [x] [Configure the SDK](https://opentelemetry.io/docs/languages/java/configuration/) 
            *   - [x] [Examples](https://opentelemetry.io/docs/languages/java/examples/) 
            *   - [x] [Registry](https://opentelemetry.io/docs/languages/java/registry/) 

        *   - [x] [JavaScript](https://opentelemetry.io/docs/languages/js/) 
            *   - [x] [Getting Started](https://opentelemetry.io/docs/languages/js/getting-started/) 
                *   - [x] [Node.js](https://opentelemetry.io/docs/languages/js/getting-started/nodejs/) 
                *   - [x] [Browser](https://opentelemetry.io/docs/languages/js/getting-started/browser/) 

            *   - [x] [Instrumentation](https://opentelemetry.io/docs/languages/js/instrumentation/) 
            *   - [x] [Libraries](https://opentelemetry.io/docs/languages/js/libraries/ "Using instrumentation libraries") 
            *   - [x] [Exporters](https://opentelemetry.io/docs/languages/js/exporters/) 
            *   - [x] [Context](https://opentelemetry.io/docs/languages/js/context/) 
            *   - [x] [Propagation](https://opentelemetry.io/docs/languages/js/propagation/) 
            *   - [x] [Resources](https://opentelemetry.io/docs/languages/js/resources/) 
            *   - [x] [Sampling](https://opentelemetry.io/docs/languages/js/sampling/) 
            *   - [x] [Serverless](https://opentelemetry.io/docs/languages/js/serverless/) 
            *   - [x] [Benchmarks](https://opentelemetry.io/docs/languages/js/benchmarks/) 
            *   - [x] [API](https://opentelemetry.io/docs/languages/js/api/ "API reference") 
            *   - [x] [Examples](https://opentelemetry.io/docs/languages/js/examples/) 
            *   - [x] [Registry](https://opentelemetry.io/docs/languages/js/registry/) 

        *   - [x] [Kotlin](https://opentelemetry.io/docs/languages/kotlin/) 
            *   - [x] [Examples](https://opentelemetry.io/docs/languages/kotlin/examples/) 
            *   - [x] [Registry](https://opentelemetry.io/docs/languages/kotlin/registry/) 

        *   - [x] [PHP](https://opentelemetry.io/docs/languages/php/) 
            *   - [x] [Getting Started](https://opentelemetry.io/docs/languages/php/getting-started/) 
            *   - [x] [Instrumentation](https://opentelemetry.io/docs/languages/php/instrumentation/) 
            *   - [x] [Libraries](https://opentelemetry.io/docs/languages/php/libraries/ "Using instrumentation libraries") 
            *   - [x] [Exporters](https://opentelemetry.io/docs/languages/php/exporters/) 
            *   - [x] [Context](https://opentelemetry.io/docs/languages/php/context/) 
            *   - [x] [Propagation](https://opentelemetry.io/docs/languages/php/propagation/) 
            *   - [x] [Resources](https://opentelemetry.io/docs/languages/php/resources/) 
            *   - [x] [SDK](https://opentelemetry.io/docs/languages/php/sdk/) 
            *   - [x] [API](https://opentelemetry.io/docs/languages/php/api/ "API reference") 
            *   - [x] [Examples](https://opentelemetry.io/docs/languages/php/examples/) 
            *   - [x] [Registry](https://opentelemetry.io/docs/languages/php/registry/) 

        *   - [x] [Python](https://opentelemetry.io/docs/languages/python/) 
            *   - [x] [Getting Started](https://opentelemetry.io/docs/languages/python/getting-started/) 
            *   - [x] [Instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/) 
            *   - [x] [Libraries](https://opentelemetry.io/docs/languages/python/libraries/ "Using instrumentation libraries") 
            *   - [x] [Exporters](https://opentelemetry.io/docs/languages/python/exporters/) 
            *   - [x] [Propagation](https://opentelemetry.io/docs/languages/python/propagation/) 
            *   - [x] [Cookbook](https://opentelemetry.io/docs/languages/python/cookbook/) 
            *   - [x] [Distro](https://opentelemetry.io/docs/languages/python/distro/ "OpenTelemetry Distro") 
            *   - [x] [Using mypy](https://opentelemetry.io/docs/languages/python/mypy/) 
            *   - [x] [Benchmarks](https://opentelemetry.io/docs/languages/python/benchmarks/) 
            *   - [x] [API](https://opentelemetry.io/docs/languages/python/api/ "API reference") 
            *   - [x] [Examples](https://opentelemetry.io/docs/languages/python/examples/) 
            *   - [x] [Registry](https://opentelemetry.io/docs/languages/python/registry/) 

        *   - [x] [Ruby](https://opentelemetry.io/docs/languages/ruby/) 
            *   - [x] [Getting Started](https://opentelemetry.io/docs/languages/ruby/getting-started/) 
            *   - [x] [Instrumentation](https://opentelemetry.io/docs/languages/ruby/instrumentation/) 
            *   - [x] [Libraries](https://opentelemetry.io/docs/languages/ruby/libraries/ "Using instrumentation libraries") 
            *   - [x] [Exporters](https://opentelemetry.io/docs/languages/ruby/exporters/) 
            *   - [x] [Sampling](https://opentelemetry.io/docs/languages/ruby/sampling/) 
            *   - [x] [API](https://opentelemetry.io/docs/languages/ruby/api/ "API reference") 
            *   - [x] [Examples](https://opentelemetry.io/docs/languages/ruby/examples/) 
            *   - [x] [Registry](https://opentelemetry.io/docs/languages/ruby/registry/) 

        *   - [x] [Rust](https://opentelemetry.io/docs/languages/rust/) 
            *   - [x] [Getting Started](https://opentelemetry.io/docs/languages/rust/getting-started/) 
            *   - [x] [Libraries](https://opentelemetry.io/docs/languages/rust/libraries/ "Using instrumentation libraries") 
            *   - [x] [Exporters](https://opentelemetry.io/docs/languages/rust/exporters/) 
            *   - [x] [API](https://opentelemetry.io/docs/languages/rust/api/ "API reference") 
            *   - [x] [Examples](https://opentelemetry.io/docs/languages/rust/examples/) 
            *   - [x] [Registry](https://opentelemetry.io/docs/languages/rust/registry/) 

        *   - [x] [Swift](https://opentelemetry.io/docs/languages/swift/) 
            *   - [x] [Getting Started](https://opentelemetry.io/docs/languages/swift/getting-started/) 
            *   - [x] [Instrumentation](https://opentelemetry.io/docs/languages/swift/instrumentation/) 
            *   - [x] [Libraries](https://opentelemetry.io/docs/languages/swift/libraries/ "Instrumentation Libraries") 
            *   - [x] [Examples](https://opentelemetry.io/docs/languages/swift/examples/) 
            *   - [x] [Registry](https://opentelemetry.io/docs/languages/swift/registry/) 

        *   - [x] [Other](https://opentelemetry.io/docs/languages/other/ "Other languages") 

    *   - [x] [Platforms](https://opentelemetry.io/docs/platforms/ "Platforms and environments") 
        *   - [x] [Client-side Apps](https://opentelemetry.io/docs/platforms/client-apps/) 
            *   - [x] [Android](https://opentelemetry.io/docs/platforms/client-apps/android/) 
            *   - [x] [iOS](https://opentelemetry.io/docs/platforms/client-apps/ios/) 
            *   - [x] [Web](https://opentelemetry.io/docs/platforms/client-apps/web/) 

        *   - [x] [FaaS](https://opentelemetry.io/docs/platforms/faas/ "Functions as a Service") 
            *   - [x] [Lambda Auto-Instrumentation](https://opentelemetry.io/docs/platforms/faas/lambda-auto-instrument/) 
            *   - [x] [Lambda Collector Config](https://opentelemetry.io/docs/platforms/faas/lambda-collector/ "Lambda Collector Configuration") 
            *   - [x] [Lambda Manual Instrumentation](https://opentelemetry.io/docs/platforms/faas/lambda-manual-instrument/) 

        *   - [x] [Kubernetes](https://opentelemetry.io/docs/platforms/kubernetes/ "OpenTelemetry with Kubernetes") 
            *   - [x] [Getting Started](https://opentelemetry.io/docs/platforms/kubernetes/getting-started/) 
            *   - [x] [Collector](https://opentelemetry.io/docs/platforms/kubernetes/collector/ "OpenTelemetry Collector and Kubernetes") 
                *   - [x] [Components](https://opentelemetry.io/docs/platforms/kubernetes/collector/components/ "Important Components for Kubernetes") 

            *   - [x] [Helm Charts](https://opentelemetry.io/docs/platforms/kubernetes/helm/ "OpenTelemetry Helm Charts") 
                *   - [x] [Collector Chart](https://opentelemetry.io/docs/platforms/kubernetes/helm/collector/ "OpenTelemetry Collector Chart") 
                *   - [x] [Demo Chart](https://opentelemetry.io/docs/platforms/kubernetes/helm/demo/ "OpenTelemetry Demo Chart") 
                *   - [x] [Operator Chart](https://opentelemetry.io/docs/platforms/kubernetes/helm/operator/ "OpenTelemetry Operator Chart") 

            *   - [x] [Kubernetes Operator](https://opentelemetry.io/docs/platforms/kubernetes/operator/ "OpenTelemetry Operator for Kubernetes") 
                *   - [x] [Auto-instrumentation](https://opentelemetry.io/docs/platforms/kubernetes/operator/automatic/ "Injecting Auto-instrumentation") 
                *   - [x] [Horizontal Pod Autoscaling](https://opentelemetry.io/docs/platforms/kubernetes/operator/horizontal-pod-autoscaling/) 
                *   - [x] [Target Allocator](https://opentelemetry.io/docs/platforms/kubernetes/operator/target-allocator/) 
                *   - [x] [Troubleshooting](https://opentelemetry.io/docs/platforms/kubernetes/operator/troubleshooting/ "Troubleshooting the OpenTelemetry Operator for Kubernetes") 
                    *   - [x] [Auto-instrumentation](https://opentelemetry.io/docs/platforms/kubernetes/operator/troubleshooting/automatic/) 
                    *   - [x] [Prometheus Alerts Runbooks](https://opentelemetry.io/docs/platforms/kubernetes/operator/troubleshooting/prometheus-alerts-runbooks/) 
                    *   - [x] [Target Allocator](https://opentelemetry.io/docs/platforms/kubernetes/operator/troubleshooting/target-allocator/) 

    *   - [x] [Zero-code Instrumentation](https://opentelemetry.io/docs/zero-code/) 
        *   - [x] [OBI](https://opentelemetry.io/docs/zero-code/obi/ "OpenTelemetry eBPF Instrumentation") 
            *   - [x] [Configure](https://opentelemetry.io/docs/zero-code/obi/configure/ "Configure OBI") 
                *   - [x] [Export modes](https://opentelemetry.io/docs/zero-code/obi/configure/export-modes/ "Configure OBI export modes") 
                *   - [x] [Global properties](https://opentelemetry.io/docs/zero-code/obi/configure/options/ "OBI global configuration properties") 
                *   - [x] [Export data](https://opentelemetry.io/docs/zero-code/obi/configure/export-data/ "Configure OBI Prometheus and OpenTelemetry data export") 
                *   - [x] [Service discovery](https://opentelemetry.io/docs/zero-code/obi/configure/service-discovery/ "Configure OBI service discovery") 
                *   - [x] [Metrics attributes](https://opentelemetry.io/docs/zero-code/obi/configure/metrics-traces-attributes/ "Configure OBI metrics and traces attributes") 
                *   - [x] [Filter data](https://opentelemetry.io/docs/zero-code/obi/configure/filter-metrics-traces/ "Filter metrics and traces by attribute values") 
                *   - [x] [Routes decorator](https://opentelemetry.io/docs/zero-code/obi/configure/routes-decorator/ "Configure OBI routes decorator") 
                *   - [x] [Metrics histograms](https://opentelemetry.io/docs/zero-code/obi/configure/metrics-histograms/ "Configure OBI Prometheus and OpenTelemetry metrics histograms") 
                *   - [x] [Sample traces](https://opentelemetry.io/docs/zero-code/obi/configure/sample-traces/ "Configure OBI OpenTelemetry trace sampling") 
                *   - [x] [Internal metrics reporter](https://opentelemetry.io/docs/zero-code/obi/configure/internal-metrics-reporter/ "Configure the OBI internal metrics reporter") 
                *   - [x] [Tune performance](https://opentelemetry.io/docs/zero-code/obi/configure/tune-performance/ "Configure OBI performance") 
                *   - [x] [YAML example](https://opentelemetry.io/docs/zero-code/obi/configure/example/ "OBI configuration YAML example") 

            *   - [x] [Network](https://opentelemetry.io/docs/zero-code/obi/network/ "Network metrics") 
                *   - [x] [Measure traffic between Cloud availability zones](https://opentelemetry.io/docs/zero-code/obi/network/inter-az/) 
                *   - [x] [Quickstart](https://opentelemetry.io/docs/zero-code/obi/network/quickstart/ "OBI network metrics quickstart") 
                *   - [x] [Configuration](https://opentelemetry.io/docs/zero-code/obi/network/config/ "OBI Network Metrics configuration options") 

            *   - [x] [Setup](https://opentelemetry.io/docs/zero-code/obi/setup/ "Set up OBI") 
                *   - [x] [Helm chart](https://opentelemetry.io/docs/zero-code/obi/setup/kubernetes-helm/ "Deploy OBI in Kubernetes with Helm") 
                *   - [x] [Docker](https://opentelemetry.io/docs/zero-code/obi/setup/docker/ "Run OBI as a Docker container") 
                *   - [x] [Kubernetes](https://opentelemetry.io/docs/zero-code/obi/setup/kubernetes/ "Deploy OBI in Kubernetes") 
                *   - [x] [Standalone](https://opentelemetry.io/docs/zero-code/obi/setup/standalone/ "Run OBI as a standalone process") 

            *   - [x] [Exported metrics](https://opentelemetry.io/docs/zero-code/obi/metrics/ "OBI exported metrics") 
            *   - [x] [Distributed traces](https://opentelemetry.io/docs/zero-code/obi/distributed-traces/ "Distributed traces with OBI") 
            *   - [x] [Request times](https://opentelemetry.io/docs/zero-code/obi/requesttime/ "Measuring total request times, instead of service times") 
            *   - [x] [Security](https://opentelemetry.io/docs/zero-code/obi/security/ "OBI security, permissions, and capabilities") 
            *   - [x] [Troubleshooting](https://opentelemetry.io/docs/zero-code/obi/troubleshooting/) 
            *   - [x] [Cilium compatibility](https://opentelemetry.io/docs/zero-code/obi/cilium-compatibility/ "OBI and Cilium compatibility") 
            *   - [x] [Metrics cardinality](https://opentelemetry.io/docs/zero-code/obi/cardinality/ "OBI metrics cardinality") 

        *   - [x] [Go](https://opentelemetry.io/docs/zero-code/go/ "Go zero-code instrumentation") 
            *   - [x] [Auto SDK](https://opentelemetry.io/docs/zero-code/go/autosdk/ "Go Instrumentation Auto SDK") 

        *   - [x] [.NET](https://opentelemetry.io/docs/zero-code/dotnet/ ".NET zero-code instrumentation") 
            *   - [x] [Getting Started](https://opentelemetry.io/docs/zero-code/dotnet/getting-started/) 
            *   - [x] [Instrumentations](https://opentelemetry.io/docs/zero-code/dotnet/instrumentations/ "Available instrumentations") 
            *   - [x] [Configuration](https://opentelemetry.io/docs/zero-code/dotnet/configuration/ "Configuration and settings") 
            *   - [x] [Custom instrumentation](https://opentelemetry.io/docs/zero-code/dotnet/custom/ "Create custom traces and metrics") 
            *   - [x] [NuGet Packages](https://opentelemetry.io/docs/zero-code/dotnet/nuget-packages/ "Using the OpenTelemetry.AutoInstrumentation NuGet packages") 
            *   - [x] [Troubleshooting](https://opentelemetry.io/docs/zero-code/dotnet/troubleshooting/ "Troubleshooting .NET automatic instrumentation issues") 

        *   - [x] [PHP](https://opentelemetry.io/docs/zero-code/php/ "PHP zero-code instrumentation") 
        *   - [x] [Python](https://opentelemetry.io/docs/zero-code/python/ "Python zero-code instrumentation") 
            *   - [x] [Configuration](https://opentelemetry.io/docs/zero-code/python/configuration/ "Agent Configuration") 
            *   - [x] [Example](https://opentelemetry.io/docs/zero-code/python/example/ "Auto-Instrumentation Example") 
            *   - [x] [Logs Example](https://opentelemetry.io/docs/zero-code/python/logs-example/ "Logs Auto-Instrumentation Example") 
            *   - [x] [Operator](https://opentelemetry.io/docs/zero-code/python/operator/ "Using the OpenTelemetry Operator to Inject Auto-Instrumentation") 
            *   - [x] [Troubleshooting](https://opentelemetry.io/docs/zero-code/python/troubleshooting/ "Troubleshooting Python automatic instrumentation issues") 

        *   - [x] [Java](https://opentelemetry.io/docs/zero-code/java/ "Java zero-code instrumentation") 
            *   - [x] [Agent](https://opentelemetry.io/docs/zero-code/java/agent/ "Java Agent") 
                *   - [x] [Getting started](https://opentelemetry.io/docs/zero-code/java/agent/getting-started/) 
                *   - [x] [Configuration](https://opentelemetry.io/docs/zero-code/java/agent/configuration/) 
                *   - [x] [Declarative configuration](https://opentelemetry.io/docs/zero-code/java/agent/declarative-configuration/ "Java Agent Declarative configuration") 
                *   - [x] [Supported Libraries](https://opentelemetry.io/docs/zero-code/java/agent/supported-libraries/) 
                *   - [x] [Suppressing instrumentation](https://opentelemetry.io/docs/zero-code/java/agent/disable/ "Suppressing specific instrumentation") 
                *   - [x] [Annotations](https://opentelemetry.io/docs/zero-code/java/agent/annotations/) 
                *   - [x] [Extend with the API](https://opentelemetry.io/docs/zero-code/java/agent/api/ "Extending instrumentations with the API") 
                *   - [x] [Instrumentation config](https://opentelemetry.io/docs/zero-code/java/agent/instrumentation/ "Instrumentation configuration") 
                    *   - [x] [HTTP](https://opentelemetry.io/docs/zero-code/java/agent/instrumentation/http/ "HTTP instrumentation configuration") 

                *   - [x] [App server config](https://opentelemetry.io/docs/zero-code/java/agent/server-config/ "Application server configuration") 
                *   - [x] [Extensions](https://opentelemetry.io/docs/zero-code/java/agent/extensions/) 
                *   - [x] [Performance](https://opentelemetry.io/docs/zero-code/java/agent/performance/) 

            *   - [x] [Quarkus](https://opentelemetry.io/docs/zero-code/java/quarkus/ "Quarkus instrumentation") 
            *   - [x] [Spring Boot starter](https://opentelemetry.io/docs/zero-code/java/spring-boot-starter/) 
                *   - [x] [Getting started](https://opentelemetry.io/docs/zero-code/java/spring-boot-starter/getting-started/) 
                *   - [x] [Extend with the API](https://opentelemetry.io/docs/zero-code/java/spring-boot-starter/api/ "Extending instrumentations with the API") 
                *   - [x] [SDK configuration](https://opentelemetry.io/docs/zero-code/java/spring-boot-starter/sdk-configuration/) 
                *   - [x] [Out of the box instrumentation](https://opentelemetry.io/docs/zero-code/java/spring-boot-starter/out-of-the-box-instrumentation/) 
                *   - [x] [Annotations](https://opentelemetry.io/docs/zero-code/java/spring-boot-starter/annotations/) 
                *   - [x] [Additional instrumentation](https://opentelemetry.io/docs/zero-code/java/spring-boot-starter/additional-instrumentations/) 
                *   - [x] [Other Spring autoconfiguration](https://opentelemetry.io/docs/zero-code/java/spring-boot-starter/other-spring-autoconfig/) 

        *   - [x] [JavaScript](https://opentelemetry.io/docs/zero-code/js/ "JavaScript zero-code instrumentation") 
            *   - [x] [Configuration](https://opentelemetry.io/docs/zero-code/js/configuration/ "Zero-Code Instrumentation Configuration") 

    *   - [x] [Collector](https://opentelemetry.io/docs/collector/) 
        *   - [x] [Quick start](https://opentelemetry.io/docs/collector/quick-start/) 
        *   - [x] [Install](https://opentelemetry.io/docs/collector/install/ "Install the Collector") 
            *   - [x] [Docker](https://opentelemetry.io/docs/collector/install/docker/ "Install the Collector with Docker") 
            *   - [x] [Kubernetes](https://opentelemetry.io/docs/collector/install/kubernetes/ "Install the Collector with Kubernetes") 
            *   - [x] [Binary](https://opentelemetry.io/docs/collector/install/binary/ "Install from a Collector binary") 
                *   - [x] [Linux](https://opentelemetry.io/docs/collector/install/binary/linux/ "Install the Collector on Linux") 
                *   - [x] [macOS](https://opentelemetry.io/docs/collector/install/binary/macos/ "Install the Collector on macOS") 
                *   - [x] [Windows](https://opentelemetry.io/docs/collector/install/binary/windows/ "Install the Collector on Windows") 

        *   - [x] [Deploy](https://opentelemetry.io/docs/collector/deploy/ "Deploy the Collector") 
            *   - [x] [Agent pattern](https://opentelemetry.io/docs/collector/deploy/agent/ "Agent deployment pattern") 
            *   - [x] [Gateway pattern](https://opentelemetry.io/docs/collector/deploy/gateway/ "Gateway deployment pattern") 
            *   - [x] [Other patterns](https://opentelemetry.io/docs/collector/deploy/other/ "Other deployment patterns") 
                *   - [x] [No Collector](https://opentelemetry.io/docs/collector/deploy/other/no-collector/) 

        *   - [x] [Configuration](https://opentelemetry.io/docs/collector/configuration/) 
        *   - [x] [Components](https://opentelemetry.io/docs/collector/components/) 
            *   - [x] [Receivers](https://opentelemetry.io/docs/collector/components/receiver/) 
            *   - [x] [Processors](https://opentelemetry.io/docs/collector/components/processor/) 
            *   - [x] [Exporters](https://opentelemetry.io/docs/collector/components/exporter/) 
            *   - [x] [Connectors](https://opentelemetry.io/docs/collector/components/connector/) 
            *   - [x] [Extensions](https://opentelemetry.io/docs/collector/components/extension/) 

        *   - [x] [Management](https://opentelemetry.io/docs/collector/management/) 
        *   - [x] [Distributions](https://opentelemetry.io/docs/collector/distributions/) 
        *   - [x] [Internal telemetry](https://opentelemetry.io/docs/collector/internal-telemetry/) 
        *   - [x] [Troubleshooting](https://opentelemetry.io/docs/collector/troubleshooting/) 
        *   - [x] [Scaling the Collector](https://opentelemetry.io/docs/collector/scaling/) 
        *   - [x] [Transforming telemetry](https://opentelemetry.io/docs/collector/transforming-telemetry/) 
        *   - [x] [Architecture](https://opentelemetry.io/docs/collector/architecture/) 
        *   - [x] [Extend](https://opentelemetry.io/docs/collector/extend/ "Extend the Collector") 
            *   - [x] [Build from source](https://opentelemetry.io/docs/collector/extend/build-from-source/) 
            *   - [x] [Build a custom Collector](https://opentelemetry.io/docs/collector/extend/ocb/ "Build a custom Collector with OpenTelemetry Collector Builder") 
            *   - [x] [Build custom components](https://opentelemetry.io/docs/collector/extend/custom-component/) 
                *   - [x] [Receivers](https://opentelemetry.io/docs/collector/extend/custom-component/receiver/ "Build a receiver") 
                *   - [x] [Connectors](https://opentelemetry.io/docs/collector/extend/custom-component/connector/ "Build a connector") 
                *   - [x] [Extensions](https://opentelemetry.io/docs/collector/extend/custom-component/extension/ "Build an extension") 
                    *   - [x] [Authenticator](https://opentelemetry.io/docs/collector/extend/custom-component/extension/authenticator/ "Build an authenticator extension") 

        *   - [x] [Benchmarks](https://opentelemetry.io/docs/collector/benchmarks/) 
        *   - [x] [Registry](https://opentelemetry.io/docs/collector/registry/) 
        *   - [x] [Resiliency](https://opentelemetry.io/docs/collector/resiliency/) 

    *   - [x] [Migration](https://opentelemetry.io/docs/migration/) 
        *   - [x] [OpenTracing](https://opentelemetry.io/docs/migration/opentracing/ "Migrating from OpenTracing") 
        *   - [x] [OpenCensus](https://opentelemetry.io/docs/migration/opencensus/ "Migrating from OpenCensus") 

    *   - [x] [Specs](https://opentelemetry.io/docs/specs/ "Specifications") 
        *   - [x] [Status](https://opentelemetry.io/docs/specs/status/ "Specification Status Summary") 
        *   - [x] [OTel 1.54.0](https://opentelemetry.io/docs/specs/otel/ "OpenTelemetry Specification 1.54.0") 
            *   - [x] [Overview](https://opentelemetry.io/docs/specs/otel/overview/) 
            *   - [x] [Baggage](https://opentelemetry.io/docs/specs/otel/baggage/) 
                *   - [x] [API](https://opentelemetry.io/docs/specs/otel/baggage/api/ "Baggage API") 

            *   - [x] [Client Design Principles](https://opentelemetry.io/docs/specs/otel/library-guidelines/ "OpenTelemetry Client Design Principles") 
            *   - [x] [Common concepts](https://opentelemetry.io/docs/specs/otel/common/ "Common specification concepts") 
                *   - [x] [Attribute Naming](https://opentelemetry.io/docs/specs/otel/common/attribute-naming/) 
                *   - [x] [Attribute Requirement Levels](https://opentelemetry.io/docs/specs/otel/common/attribute-requirement-level/ "Attribute Requirement Levels for Semantic Conventions") 
                *   - [x] [Instrumentation Scope](https://opentelemetry.io/docs/specs/otel/common/instrumentation-scope/) 
                *   - [x] [Mapping to AnyValue](https://opentelemetry.io/docs/specs/otel/common/attribute-type-mapping/ "Mapping Arbitrary Data to OTLP AnyValue") 
                *   - [x] [Mapping to non-OTLP Formats](https://opentelemetry.io/docs/specs/otel/common/mapping-to-non-otlp/ "OpenTelemetry Transformation to non-OTLP Formats") 

            *   - [x] [Compatibility](https://opentelemetry.io/docs/specs/otel/compatibility/) 
                *   - [x] [OpenCensus](https://opentelemetry.io/docs/specs/otel/compatibility/opencensus/ "OpenCensus Compatibility") 
                *   - [x] [OpenTracing](https://opentelemetry.io/docs/specs/otel/compatibility/opentracing/ "OpenTracing Compatibility") 
                *   - [x] [Prometheus and OpenMetrics](https://opentelemetry.io/docs/specs/otel/compatibility/prometheus_and_openmetrics/ "Prometheus and OpenMetrics Compatibility") 
                *   - [x] [Trace Context in non-OTLP Log Formats](https://opentelemetry.io/docs/specs/otel/compatibility/logging_trace_context/) 

            *   - [x] [Configuration](https://opentelemetry.io/docs/specs/otel/configuration/) 
                *   - [x] [API](https://opentelemetry.io/docs/specs/otel/configuration/api/ "Instrumentation Configuration API") 
                *   - [x] [Data Model](https://opentelemetry.io/docs/specs/otel/configuration/data-model/ "Configuration Data Model") 
                *   - [x] [SDK](https://opentelemetry.io/docs/specs/otel/configuration/sdk/ "Configuration SDK") 
                *   - [x] [Common](https://opentelemetry.io/docs/specs/otel/configuration/common/ "Common Configuration Specification") 
                *   - [x] [Env var](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/ "Environment Variable Specification") 
                *   - [x] [Supplementary Guidelines](https://opentelemetry.io/docs/specs/otel/configuration/supplementary-guidelines/) 

            *   - [x] [Context](https://opentelemetry.io/docs/specs/otel/context/) 
                *   - [x] [Environment Variables as Context Propagation Carriers](https://opentelemetry.io/docs/specs/otel/context/env-carriers/) 
                *   - [x] [Propagators API](https://opentelemetry.io/docs/specs/otel/context/api-propagators/) 

            *   - [x] [Definitions of Document Statuses](https://opentelemetry.io/docs/specs/otel/document-status/) 
            *   - [x] [Entities](https://opentelemetry.io/docs/specs/otel/entities/) 
                *   - [x] [Data Model](https://opentelemetry.io/docs/specs/otel/entities/data-model/ "Entity Data Model") 
                *   - [x] [Entity Propagation](https://opentelemetry.io/docs/specs/otel/entities/entity-propagation/) 

            *   - [x] [Error handling in OpenTelemetry](https://opentelemetry.io/docs/specs/otel/error-handling/) 
            *   - [x] [Glossary](https://opentelemetry.io/docs/specs/otel/glossary/) 
            *   - [x] [Logs](https://opentelemetry.io/docs/specs/otel/logs/ "OpenTelemetry Logging") 
                *   - [x] [API](https://opentelemetry.io/docs/specs/otel/logs/api/ "Logs API") 
                *   - [x] [Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/ "Logs Data Model") 
                *   - [x] [SDK](https://opentelemetry.io/docs/specs/otel/logs/sdk/ "Logs SDK") 
                *   - [x] [Data Model Appendix](https://opentelemetry.io/docs/specs/otel/logs/data-model-appendix/) 
                *   - [x] [Exporters](https://opentelemetry.io/docs/specs/otel/logs/sdk_exporters/ "Logs Exporters") 
                    *   - [x] [Stdout](https://opentelemetry.io/docs/specs/otel/logs/sdk_exporters/stdout/ "Logs Exporter - Standard output") 

                *   - [x] [No-Op](https://opentelemetry.io/docs/specs/otel/logs/noop/ "Logs API No-Op Implementation") 
                *   - [x] [Supplementary Guidelines](https://opentelemetry.io/docs/specs/otel/logs/supplementary-guidelines/) 

            *   - [x] [Metrics](https://opentelemetry.io/docs/specs/otel/metrics/ "OpenTelemetry Metrics") 
                *   - [x] [API](https://opentelemetry.io/docs/specs/otel/metrics/api/ "Metrics API") 
                *   - [x] [Data Model](https://opentelemetry.io/docs/specs/otel/metrics/data-model/ "Metrics Data Model") 
                *   - [x] [SDK](https://opentelemetry.io/docs/specs/otel/metrics/sdk/ "Metrics SDK") 
                *   - [x] [Exporters](https://opentelemetry.io/docs/specs/otel/metrics/sdk_exporters/ "Metrics Exporters") 
                    *   - [x] [In-memory](https://opentelemetry.io/docs/specs/otel/metrics/sdk_exporters/in-memory/ "Metrics Exporter - In-memory") 
                    *   - [x] [OTLP](https://opentelemetry.io/docs/specs/otel/metrics/sdk_exporters/otlp/ "Metrics Exporter - OTLP") 
                    *   - [x] [Prometheus](https://opentelemetry.io/docs/specs/otel/metrics/sdk_exporters/prometheus/ "Metrics Exporter - Prometheus") 
                    *   - [x] [Stdout](https://opentelemetry.io/docs/specs/otel/metrics/sdk_exporters/stdout/ "Metrics Exporter - Standard output") 

                *   - [x] [Metric Requirement Levels](https://opentelemetry.io/docs/specs/otel/metrics/metric-requirement-level/ "Metric Requirement Levels for Semantic Conventions") 
                *   - [x] [No-Op](https://opentelemetry.io/docs/specs/otel/metrics/noop/ "Metrics No-Op API Implementation") 
                *   - [x] [Supplementary Guidelines](https://opentelemetry.io/docs/specs/otel/metrics/supplementary-guidelines/) 

            *   - [x] [Performance and Blocking of OpenTelemetry API](https://opentelemetry.io/docs/specs/otel/performance/) 
            *   - [x] [Performance Benchmark of OpenTelemetry API](https://opentelemetry.io/docs/specs/otel/performance-benchmark/) 
            *   - [x] [Profiles](https://opentelemetry.io/docs/specs/otel/profiles/ "OpenTelemetry Profiles") 
                *   - [x] [Mappings](https://opentelemetry.io/docs/specs/otel/profiles/mappings/) 
                *   - [x] [Pprof](https://opentelemetry.io/docs/specs/otel/profiles/pprof/) 

            *   - [x] [Project Package Layout](https://opentelemetry.io/docs/specs/otel/library-layout/ "OpenTelemetry Project Package Layout") 
            *   - [x] [Protocol](https://opentelemetry.io/docs/specs/otel/protocol/ "OpenTelemetry Protocol") 
                *   - [x] [Specification 1.9.0](https://opentelemetry.io/docs/specs/otel/protocol/otlp/ "OpenTelemetry Protocol Specification") 
                *   - [x] [Design Goals](https://opentelemetry.io/docs/specs/otel/protocol/design-goals/ "Design Goals for OpenTelemetry Wire Protocol") 
                *   - [x] [Exporter](https://opentelemetry.io/docs/specs/otel/protocol/exporter/ "OpenTelemetry Protocol Exporter") 
                *   - [x] [File Exporter](https://opentelemetry.io/docs/specs/otel/protocol/file-exporter/ "OpenTelemetry Protocol File Exporter") 
                *   - [x] [Requirements](https://opentelemetry.io/docs/specs/otel/protocol/requirements/ "OpenTelemetry Protocol Requirements") 

            *   - [x] [Resource](https://opentelemetry.io/docs/specs/otel/resource/) 
                *   - [x] [Data Model](https://opentelemetry.io/docs/specs/otel/resource/data-model/ "Resource Data Model") 
                *   - [x] [SDK](https://opentelemetry.io/docs/specs/otel/resource/sdk/ "Resource SDK") 

            *   - [x] [Schemas](https://opentelemetry.io/docs/specs/otel/schemas/ "Telemetry Schemas") 
                *   - [x] [1.0.0](https://opentelemetry.io/docs/specs/otel/schemas/file_format_v1.0.0/ "Schema File Format 1.0.0") 
                *   - [x] [1.1.0](https://opentelemetry.io/docs/specs/otel/schemas/file_format_v1.1.0/ "Schema File Format 1.1.0") 

            *   - [x] [Semantic Conventions](https://opentelemetry.io/docs/specs/otel/semantic-conventions/) 
            *   - [x] [Specification Principles](https://opentelemetry.io/docs/specs/otel/specification-principles/) 
            *   - [x] [Telemetry Stability](https://opentelemetry.io/docs/specs/otel/telemetry-stability/) 
            *   - [x] [The OpenTelemetry approach to upgrading](https://opentelemetry.io/docs/specs/otel/upgrading/) 
            *   - [x] [Trace](https://opentelemetry.io/docs/specs/otel/trace/) 
                *   - [x] [API](https://opentelemetry.io/docs/specs/otel/trace/api/ "Tracing API") 
                *   - [x] [SDK](https://opentelemetry.io/docs/specs/otel/trace/sdk/ "Tracing SDK") 
                *   - [x] [Exceptions](https://opentelemetry.io/docs/specs/otel/trace/exceptions/) 
                *   - [x] [Exporters](https://opentelemetry.io/docs/specs/otel/trace/sdk_exporters/ "Trace Exporters") 
                    *   - [x] [Stdout](https://opentelemetry.io/docs/specs/otel/trace/sdk_exporters/stdout/ "Span Exporter - Standard output") 
                    *   - [x] [Zipkin](https://opentelemetry.io/docs/specs/otel/trace/sdk_exporters/zipkin/ "OpenTelemetry to Zipkin Transformation") 

                *   - [x] [Probability Sampling](https://opentelemetry.io/docs/specs/otel/trace/tracestate-probability-sampling/ "TraceState: Probability Sampling") 
                *   - [x] [TraceState](https://opentelemetry.io/docs/specs/otel/trace/tracestate-handling/ "TraceState Handling") 

            *   - [x] [Vendors](https://opentelemetry.io/docs/specs/otel/vendors/) 
            *   - [x] [Versioning and stability for OpenTelemetry clients](https://opentelemetry.io/docs/specs/otel/versioning-and-stability/) 

        *   - [x] [OTLP 1.9.0](https://opentelemetry.io/docs/specs/otlp/ "OTLP Specification 1.9.0") 
        *   - [x] [OpAMP](https://opentelemetry.io/docs/specs/opamp/ "Open Agent Management Protocol") 
        *   - [x] [Semantic conventions 1.40.0](https://opentelemetry.io/docs/specs/semconv/ "OpenTelemetry semantic conventions 1.40.0") 
            *   - [x] [Registry](https://opentelemetry.io/docs/specs/semconv/registry/) 
                *   - [x] [Attributes](https://opentelemetry.io/docs/specs/semconv/registry/attributes/ "Attribute registry") 
                    *   - [x] [Android](https://opentelemetry.io/docs/specs/semconv/registry/attributes/android/) 
                    *   - [x] [App](https://opentelemetry.io/docs/specs/semconv/registry/attributes/app/) 
                    *   - [x] [Artifact](https://opentelemetry.io/docs/specs/semconv/registry/attributes/artifact/) 
                    *   - [x] [Aspnetcore](https://opentelemetry.io/docs/specs/semconv/registry/attributes/aspnetcore/) 
                    *   - [x] [AWS](https://opentelemetry.io/docs/specs/semconv/registry/attributes/aws/) 
                    *   - [x] [Azure](https://opentelemetry.io/docs/specs/semconv/registry/attributes/azure/) 
                    *   - [x] [Browser](https://opentelemetry.io/docs/specs/semconv/registry/attributes/browser/) 
                    *   - [x] [Cassandra](https://opentelemetry.io/docs/specs/semconv/registry/attributes/cassandra/) 
                    *   - [x] [CICD](https://opentelemetry.io/docs/specs/semconv/registry/attributes/cicd/) 
                    *   - [x] [Client](https://opentelemetry.io/docs/specs/semconv/registry/attributes/client/) 
                    *   - [x] [Cloud](https://opentelemetry.io/docs/specs/semconv/registry/attributes/cloud/) 
                    *   - [x] [CloudEvents](https://opentelemetry.io/docs/specs/semconv/registry/attributes/cloudevents/) 
                    *   - [x] [CloudFoundry](https://opentelemetry.io/docs/specs/semconv/registry/attributes/cloudfoundry/) 
                    *   - [x] [Code](https://opentelemetry.io/docs/specs/semconv/registry/attributes/code/) 
                    *   - [x] [Container](https://opentelemetry.io/docs/specs/semconv/registry/attributes/container/) 
                    *   - [x] [CPU](https://opentelemetry.io/docs/specs/semconv/registry/attributes/cpu/) 
                    *   - [x] [CPython](https://opentelemetry.io/docs/specs/semconv/registry/attributes/cpython/) 
                    *   - [x] [DB](https://opentelemetry.io/docs/specs/semconv/registry/attributes/db/) 
                    *   - [x] [Deployment](https://opentelemetry.io/docs/specs/semconv/registry/attributes/deployment/) 
                    *   - [x] [Destination](https://opentelemetry.io/docs/specs/semconv/registry/attributes/destination/) 
                    *   - [x] [Device](https://opentelemetry.io/docs/specs/semconv/registry/attributes/device/) 
                    *   - [x] [Disk](https://opentelemetry.io/docs/specs/semconv/registry/attributes/disk/) 
                    *   - [x] [DNS](https://opentelemetry.io/docs/specs/semconv/registry/attributes/dns/) 
                    *   - [x] [Dotnet](https://opentelemetry.io/docs/specs/semconv/registry/attributes/dotnet/) 
                    *   - [x] [Elasticsearch](https://opentelemetry.io/docs/specs/semconv/registry/attributes/elasticsearch/) 
                    *   - [x] [Enduser](https://opentelemetry.io/docs/specs/semconv/registry/attributes/enduser/) 
                    *   - [x] [Error](https://opentelemetry.io/docs/specs/semconv/registry/attributes/error/) 
                    *   - [x] [Event](https://opentelemetry.io/docs/specs/semconv/registry/attributes/event/) 
                    *   - [x] [Exception](https://opentelemetry.io/docs/specs/semconv/registry/attributes/exception/) 
                    *   - [x] [Faas](https://opentelemetry.io/docs/specs/semconv/registry/attributes/faas/) 
                    *   - [x] [Feature flag](https://opentelemetry.io/docs/specs/semconv/registry/attributes/feature-flag/) 
                    *   - [x] [File](https://opentelemetry.io/docs/specs/semconv/registry/attributes/file/) 
                    *   - [x] [GCP](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gcp/) 
                    *   - [x] [Gen AI](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/) 
                    *   - [x] [Geo](https://opentelemetry.io/docs/specs/semconv/registry/attributes/geo/) 
                    *   - [x] [Go](https://opentelemetry.io/docs/specs/semconv/registry/attributes/go/) 
                    *   - [x] [GraphQL](https://opentelemetry.io/docs/specs/semconv/registry/attributes/graphql/) 
                    *   - [x] [Hardware](https://opentelemetry.io/docs/specs/semconv/registry/attributes/hardware/) 
                    *   - [x] [Heroku](https://opentelemetry.io/docs/specs/semconv/registry/attributes/heroku/) 
                    *   - [x] [Host](https://opentelemetry.io/docs/specs/semconv/registry/attributes/host/) 
                    *   - [x] [HTTP](https://opentelemetry.io/docs/specs/semconv/registry/attributes/http/) 
                    *   - [x] [iOS](https://opentelemetry.io/docs/specs/semconv/registry/attributes/ios/) 
                    *   - [x] [JSONRPC](https://opentelemetry.io/docs/specs/semconv/registry/attributes/jsonrpc/) 
                    *   - [x] [JVM](https://opentelemetry.io/docs/specs/semconv/registry/attributes/jvm/) 
                    *   - [x] [K8s](https://opentelemetry.io/docs/specs/semconv/registry/attributes/k8s/) 
                    *   - [x] [Linux](https://opentelemetry.io/docs/specs/semconv/registry/attributes/linux/) 
                    *   - [x] [Log](https://opentelemetry.io/docs/specs/semconv/registry/attributes/log/) 
                    *   - [x] [Mainframe](https://opentelemetry.io/docs/specs/semconv/registry/attributes/mainframe/) 
                    *   - [x] [MCP](https://opentelemetry.io/docs/specs/semconv/registry/attributes/mcp/) 
                    *   - [x] [Messaging](https://opentelemetry.io/docs/specs/semconv/registry/attributes/messaging/) 
                    *   - [x] [Network](https://opentelemetry.io/docs/specs/semconv/registry/attributes/network/) 
                    *   - [x] [NFS](https://opentelemetry.io/docs/specs/semconv/registry/attributes/nfs/) 
                    *   - [x] [NodeJS](https://opentelemetry.io/docs/specs/semconv/registry/attributes/nodejs/) 
                    *   - [x] [OCI](https://opentelemetry.io/docs/specs/semconv/registry/attributes/oci/) 
                    *   - [x] [ONC RPC](https://opentelemetry.io/docs/specs/semconv/registry/attributes/onc-rpc/) 
                    *   - [x] [OpenAI](https://opentelemetry.io/docs/specs/semconv/registry/attributes/openai/) 
                    *   - [x] [Openshift](https://opentelemetry.io/docs/specs/semconv/registry/attributes/openshift/) 
                    *   - [x] [OpenTracing](https://opentelemetry.io/docs/specs/semconv/registry/attributes/opentracing/) 
                    *   - [x] [Oracle cloud](https://opentelemetry.io/docs/specs/semconv/registry/attributes/oracle-cloud/) 
                    *   - [x] [OracleDB](https://opentelemetry.io/docs/specs/semconv/registry/attributes/oracledb/) 
                    *   - [x] [OS](https://opentelemetry.io/docs/specs/semconv/registry/attributes/os/) 
                    *   - [x] [OTel](https://opentelemetry.io/docs/specs/semconv/registry/attributes/otel/) 
                    *   - [x] [Peer](https://opentelemetry.io/docs/specs/semconv/registry/attributes/peer/) 
                    *   - [x] [Pprof](https://opentelemetry.io/docs/specs/semconv/registry/attributes/pprof/) 
                    *   - [x] [Process](https://opentelemetry.io/docs/specs/semconv/registry/attributes/process/) 
                    *   - [x] [Profile](https://opentelemetry.io/docs/specs/semconv/registry/attributes/profile/) 
                    *   - [x] [RPC](https://opentelemetry.io/docs/specs/semconv/registry/attributes/rpc/) 
                    *   - [x] [Security rule](https://opentelemetry.io/docs/specs/semconv/registry/attributes/security-rule/) 
                    *   - [x] [Server](https://opentelemetry.io/docs/specs/semconv/registry/attributes/server/) 
                    *   - [x] [Service](https://opentelemetry.io/docs/specs/semconv/registry/attributes/service/) 
                    *   - [x] [Session](https://opentelemetry.io/docs/specs/semconv/registry/attributes/session/) 
                    *   - [x] [SignalR](https://opentelemetry.io/docs/specs/semconv/registry/attributes/signalr/) 
                    *   - [x] [Source](https://opentelemetry.io/docs/specs/semconv/registry/attributes/source/) 
                    *   - [x] [System](https://opentelemetry.io/docs/specs/semconv/registry/attributes/system/) 
                    *   - [x] [Telemetry](https://opentelemetry.io/docs/specs/semconv/registry/attributes/telemetry/) 
                    *   - [x] [Test](https://opentelemetry.io/docs/specs/semconv/registry/attributes/test/) 
                    *   - [x] [Thread](https://opentelemetry.io/docs/specs/semconv/registry/attributes/thread/) 
                    *   - [x] [TLS](https://opentelemetry.io/docs/specs/semconv/registry/attributes/tls/) 
                    *   - [x] [URL](https://opentelemetry.io/docs/specs/semconv/registry/attributes/url/) 
                    *   - [x] [User](https://opentelemetry.io/docs/specs/semconv/registry/attributes/user/) 
                    *   - [x] [User agent](https://opentelemetry.io/docs/specs/semconv/registry/attributes/user-agent/) 
                    *   - [x] [V8js](https://opentelemetry.io/docs/specs/semconv/registry/attributes/v8js/) 
                    *   - [x] [VCS](https://opentelemetry.io/docs/specs/semconv/registry/attributes/vcs/) 
                    *   - [x] [Webengine](https://opentelemetry.io/docs/specs/semconv/registry/attributes/webengine/) 
                    *   - [x] [zOS](https://opentelemetry.io/docs/specs/semconv/registry/attributes/zos/) 

                *   - [x] [Entities](https://opentelemetry.io/docs/specs/semconv/registry/entities/ "Entity registry") 
                    *   - [x] [Android](https://opentelemetry.io/docs/specs/semconv/registry/entities/android/) 
                    *   - [x] [App](https://opentelemetry.io/docs/specs/semconv/registry/entities/app/) 
                    *   - [x] [AWS](https://opentelemetry.io/docs/specs/semconv/registry/entities/aws/) 
                    *   - [x] [Browser](https://opentelemetry.io/docs/specs/semconv/registry/entities/browser/) 
                    *   - [x] [CICD](https://opentelemetry.io/docs/specs/semconv/registry/entities/cicd/) 
                    *   - [x] [Cloud](https://opentelemetry.io/docs/specs/semconv/registry/entities/cloud/) 
                    *   - [x] [CloudFoundry](https://opentelemetry.io/docs/specs/semconv/registry/entities/cloudfoundry/) 
                    *   - [x] [Container](https://opentelemetry.io/docs/specs/semconv/registry/entities/container/) 
                    *   - [x] [Deployment](https://opentelemetry.io/docs/specs/semconv/registry/entities/deployment/) 
                    *   - [x] [Device](https://opentelemetry.io/docs/specs/semconv/registry/entities/device/) 
                    *   - [x] [Faas](https://opentelemetry.io/docs/specs/semconv/registry/entities/faas/) 
                    *   - [x] [GCP](https://opentelemetry.io/docs/specs/semconv/registry/entities/gcp/) 
                    *   - [x] [Heroku](https://opentelemetry.io/docs/specs/semconv/registry/entities/heroku/) 
                    *   - [x] [Host](https://opentelemetry.io/docs/specs/semconv/registry/entities/host/) 
                    *   - [x] [K8s](https://opentelemetry.io/docs/specs/semconv/registry/entities/k8s/) 
                    *   - [x] [Openshift](https://opentelemetry.io/docs/specs/semconv/registry/entities/openshift/) 
                    *   - [x] [OS](https://opentelemetry.io/docs/specs/semconv/registry/entities/os/) 
                    *   - [x] [OTel](https://opentelemetry.io/docs/specs/semconv/registry/entities/otel/) 
                    *   - [x] [Process](https://opentelemetry.io/docs/specs/semconv/registry/entities/process/) 
                    *   - [x] [Service](https://opentelemetry.io/docs/specs/semconv/registry/entities/service/) 
                    *   - [x] [Telemetry](https://opentelemetry.io/docs/specs/semconv/registry/entities/telemetry/) 
                    *   - [x] [VCS](https://opentelemetry.io/docs/specs/semconv/registry/entities/vcs/) 
                    *   - [x] [Webengine](https://opentelemetry.io/docs/specs/semconv/registry/entities/webengine/) 
                    *   - [x] [zOS](https://opentelemetry.io/docs/specs/semconv/registry/entities/zos/) 

            *   - [x] [General](https://opentelemetry.io/docs/specs/semconv/general/ "General semantic conventions") 
                *   - [x] [Attribute requirement levels](https://opentelemetry.io/docs/specs/semconv/general/attribute-requirement-level/) 
                *   - [x] [Attributes](https://opentelemetry.io/docs/specs/semconv/general/attributes/ "General attributes") 
                *   - [x] [Events](https://opentelemetry.io/docs/specs/semconv/general/events/ "Semantic conventions for events") 
                *   - [x] [Logs](https://opentelemetry.io/docs/specs/semconv/general/logs/ "General logs attributes") 
                *   - [x] [Metric requirement levels](https://opentelemetry.io/docs/specs/semconv/general/metric-requirement-level/) 
                *   - [x] [Metrics](https://opentelemetry.io/docs/specs/semconv/general/metrics/ "Metrics semantic conventions") 
                *   - [x] [Naming](https://opentelemetry.io/docs/specs/semconv/general/naming/) 
                *   - [x] [Profiles](https://opentelemetry.io/docs/specs/semconv/general/profiles/ "Profiles attributes") 
                *   - [x] [Recording errors](https://opentelemetry.io/docs/specs/semconv/general/recording-errors/) 
                *   - [x] [Semantic convention groups](https://opentelemetry.io/docs/specs/semconv/general/semantic-convention-groups/) 
                *   - [x] [Session](https://opentelemetry.io/docs/specs/semconv/general/session/ "Semantic conventions for session") 
                *   - [x] [Trace](https://opentelemetry.io/docs/specs/semconv/general/trace/ "Trace semantic conventions") 
                *   - [x] [Tracing compatibility](https://opentelemetry.io/docs/specs/semconv/general/trace-compatibility/ "Semantic conventions for tracing compatibility components") 

            *   - [x] [.NET](https://opentelemetry.io/docs/specs/semconv/dotnet/ "Semantic conventions for .NET") 
                *   - [x] [ASP.NET Core](https://opentelemetry.io/docs/specs/semconv/dotnet/dotnet-aspnetcore-metrics/ "Semantic conventions for ASP.NET Core metrics") 
                *   - [x] [DNS](https://opentelemetry.io/docs/specs/semconv/dotnet/dotnet-dns-metrics/ "Semantic conventions for DNS metrics emitted by .NET") 
                *   - [x] [HTTP](https://opentelemetry.io/docs/specs/semconv/dotnet/dotnet-http-metrics/ "Semantic conventions for HTTP client and server metrics emitted by .NET") 
                *   - [x] [HTTP request and connection spans](https://opentelemetry.io/docs/specs/semconv/dotnet/dotnet-network-traces/ "Semantic Conventions for network spans emitted by .NET") 
                *   - [x] [Kestrel](https://opentelemetry.io/docs/specs/semconv/dotnet/dotnet-kestrel-metrics/ "Semantic conventions for Kestrel web server metrics") 
                *   - [x] [SignalR](https://opentelemetry.io/docs/specs/semconv/dotnet/dotnet-signalr-metrics/ "Semantic conventions for SignalR server metrics") 

            *   - [x] [App](https://opentelemetry.io/docs/specs/semconv/app/ "Semantic conventions for Apps") 
                *   - [x] [Events](https://opentelemetry.io/docs/specs/semconv/app/app-events/ "App Events") 

            *   - [x] [Azure](https://opentelemetry.io/docs/specs/semconv/azure/ "Semantic conventions for Azure resource logs") 
                *   - [x] [Events](https://opentelemetry.io/docs/specs/semconv/azure/azure-events/ "Semantic conventions for Azure resource log events") 

            *   - [x] [Browser](https://opentelemetry.io/docs/specs/semconv/browser/ "Semantic conventions for Browser") 
                *   - [x] [Events](https://opentelemetry.io/docs/specs/semconv/browser/browser-events/ "Semantic conventions for browser events") 

            *   - [x] [CICD](https://opentelemetry.io/docs/specs/semconv/cicd/ "Semantic conventions for CICD") 
                *   - [x] [Logs](https://opentelemetry.io/docs/specs/semconv/cicd/cicd-logs/ "Semantic conventions for CICD logs") 
                *   - [x] [Metrics](https://opentelemetry.io/docs/specs/semconv/cicd/cicd-metrics/ "Semantic conventions for CICD metrics") 
                *   - [x] [Spans](https://opentelemetry.io/docs/specs/semconv/cicd/cicd-spans/ "Semantic conventions for CICD spans") 

            *   - [x] [CLI programs](https://opentelemetry.io/docs/specs/semconv/cli/ "Semantic conventions for CLI programs") 
                *   - [x] [Spans](https://opentelemetry.io/docs/specs/semconv/cli/cli-spans/ "Semantic conventions for CLI (command line interface) programs") 

            *   - [x] [Cloud providers](https://opentelemetry.io/docs/specs/semconv/cloud-providers/ "Semantic conventions for cloud providers") 
                *   - [x] [AWS SDK](https://opentelemetry.io/docs/specs/semconv/cloud-providers/aws-sdk/ "Semantic conventions for AWS SDK client spans") 

            *   - [x] [CloudEvents](https://opentelemetry.io/docs/specs/semconv/cloudevents/ "Semantic conventions for CloudEvents") 
                *   - [x] [Spans](https://opentelemetry.io/docs/specs/semconv/cloudevents/cloudevents-spans/ "Semantic conventions for CloudEvents spans") 

            *   - [x] [Database](https://opentelemetry.io/docs/specs/semconv/db/ "Semantic conventions for database calls and systems") 
                *   - [x] [Cassandra](https://opentelemetry.io/docs/specs/semconv/db/cassandra/ "Semantic conventions for Cassandra client operations") 
                *   - [x] [Cosmos DB](https://opentelemetry.io/docs/specs/semconv/db/cosmosdb/ "Semantic conventions for Microsoft Azure Cosmos DB client operations") 
                *   - [x] [CouchDB](https://opentelemetry.io/docs/specs/semconv/db/couchdb/ "Semantic conventions for CouchDB client operations") 
                *   - [x] [DynamoDB](https://opentelemetry.io/docs/specs/semconv/db/dynamodb/ "Semantic conventions for AWS DynamoDB client operations") 
                *   - [x] [Elasticsearch](https://opentelemetry.io/docs/specs/semconv/db/elasticsearch/ "Semantic conventions for Elasticsearch client operations") 
                *   - [x] [Exceptions](https://opentelemetry.io/docs/specs/semconv/db/database-exceptions/ "Semantic conventions for database exceptions") 
                *   - [x] [HBase](https://opentelemetry.io/docs/specs/semconv/db/hbase/ "Semantic conventions for HBase client operations") 
                *   - [x] [MariaDB](https://opentelemetry.io/docs/specs/semconv/db/mariadb/ "Semantic conventions for MariaDB client operations") 
                *   - [x] [Metrics](https://opentelemetry.io/docs/specs/semconv/db/database-metrics/ "Semantic conventions for database client metrics") 
                *   - [x] [MongoDB](https://opentelemetry.io/docs/specs/semconv/db/mongodb/ "Semantic conventions for MongoDB client operations") 
                *   - [x] [MySQL](https://opentelemetry.io/docs/specs/semconv/db/mysql/ "Semantic conventions for MySQL client operations") 
                *   - [x] [Oracle Database](https://opentelemetry.io/docs/specs/semconv/db/oracledb/ "Semantic conventions for Oracle Database") 
                *   - [x] [PostgreSQL](https://opentelemetry.io/docs/specs/semconv/db/postgresql/ "Semantic conventions for PostgreSQL client operations") 
                *   - [x] [Redis](https://opentelemetry.io/docs/specs/semconv/db/redis/ "Semantic conventions for Redis client operations") 
                *   - [x] [Spans](https://opentelemetry.io/docs/specs/semconv/db/database-spans/ "Semantic conventions for database client spans") 
                *   - [x] [SQL](https://opentelemetry.io/docs/specs/semconv/db/sql/ "Semantic conventions for SQL databases client operations") 
                *   - [x] [SQL Server](https://opentelemetry.io/docs/specs/semconv/db/sql-server/ "Semantic conventions for Microsoft SQL Server client operations") 

            *   - [x] [DNS](https://opentelemetry.io/docs/specs/semconv/dns/ "Semantic conventions for DNS") 
                *   - [x] [Metrics](https://opentelemetry.io/docs/specs/semconv/dns/dns-metrics/ "Semantic conventions for DNS queries") 

            *   - [x] [Exceptions](https://opentelemetry.io/docs/specs/semconv/exceptions/ "Semantic conventions for exceptions") 
                *   - [x] [Logs](https://opentelemetry.io/docs/specs/semconv/exceptions/exceptions-logs/ "Semantic conventions for exceptions in logs") 
                *   - [x] [Spans](https://opentelemetry.io/docs/specs/semconv/exceptions/exceptions-spans/ "Semantic conventions for exceptions on spans") 

            *   - [x] [FaaS](https://opentelemetry.io/docs/specs/semconv/faas/ "Semantic conventions for Function-as-a-Service") 
                *   - [x] [AWS Lambda](https://opentelemetry.io/docs/specs/semconv/faas/aws-lambda/ "Instrumenting AWS Lambda") 
                *   - [x] [Metrics](https://opentelemetry.io/docs/specs/semconv/faas/faas-metrics/ "Semantic conventions for FaaS metrics") 
                *   - [x] [Spans](https://opentelemetry.io/docs/specs/semconv/faas/faas-spans/ "Semantic conventions for FaaS spans") 

            *   - [x] [Feature flags](https://opentelemetry.io/docs/specs/semconv/feature-flags/ "Semantic conventions for feature flags") 
                *   - [x] [Events](https://opentelemetry.io/docs/specs/semconv/feature-flags/feature-flags-events/ "Semantic conventions for feature flags in events") 

            *   - [x] [Generative AI](https://opentelemetry.io/docs/specs/semconv/gen-ai/ "Semantic conventions for generative AI systems") 
                *   - [x] [Agent spans](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/ "Semantic Conventions for GenAI agent and framework spans") 
                *   - [x] [Anthropic](https://opentelemetry.io/docs/specs/semconv/gen-ai/anthropic/ "Semantic conventions for Anthropic client operations") 
                *   - [x] [AWS Bedrock](https://opentelemetry.io/docs/specs/semconv/gen-ai/aws-bedrock/ "Semantic conventions for AWS Bedrock operations") 
                *   - [x] [Azure AI Inference](https://opentelemetry.io/docs/specs/semconv/gen-ai/azure-ai-inference/ "Semantic conventions for Azure AI Inference client operations") 
                *   - [x] [Events](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/ "Semantic conventions for Generative AI events") 
                *   - [x] [LLM call examples](https://opentelemetry.io/docs/specs/semconv/gen-ai/non-normative/examples-llm-calls/) 
                *   - [x] [Metrics](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-metrics/ "Semantic conventions for generative AI metrics") 
                *   - [x] [Model Context Protocol](https://opentelemetry.io/docs/specs/semconv/gen-ai/mcp/ "Semantic conventions for Model Context Protocol (MCP)") 
                *   - [x] [OpenAI](https://opentelemetry.io/docs/specs/semconv/gen-ai/openai/ "Semantic conventions for OpenAI client operations") 
                *   - [x] [Spans](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/ "Semantic conventions for generative client AI spans") 

            *   - [x] [GraphQL](https://opentelemetry.io/docs/specs/semconv/graphql/ "Semantic conventions for GraphQL") 
                *   - [x] [GraphQL server](https://opentelemetry.io/docs/specs/semconv/graphql/graphql-spans/ "Semantic conventions for GraphQL server spans") 

            *   - [x] [Hardware](https://opentelemetry.io/docs/specs/semconv/hardware/ "Semantic conventions for hardware") 
                *   - [x] [Battery](https://opentelemetry.io/docs/specs/semconv/hardware/battery/ "Semantic conventions for battery metrics") 
                *   - [x] [CPU](https://opentelemetry.io/docs/specs/semconv/hardware/cpu/ "Semantic conventions for CPU metrics") 
                *   - [x] [Disk Controller](https://opentelemetry.io/docs/specs/semconv/hardware/disk-controller/ "Semantic conventions for disk controller metrics") 
                *   - [x] [Enclosure](https://opentelemetry.io/docs/specs/semconv/hardware/enclosure/ "Semantic conventions for enclosure metrics") 
                *   - [x] [Fan](https://opentelemetry.io/docs/specs/semconv/hardware/fan/ "Semantic conventions for fan metrics") 
                *   - [x] [GPU](https://opentelemetry.io/docs/specs/semconv/hardware/gpu/ "Semantic conventions for GPU metrics") 
                *   - [x] [Logical Disk](https://opentelemetry.io/docs/specs/semconv/hardware/logical-disk/ "Semantic conventions for logical disk metrics") 
                *   - [x] [Memory](https://opentelemetry.io/docs/specs/semconv/hardware/memory/ "Semantic conventions for memory metrics") 
                *   - [x] [Metrics](https://opentelemetry.io/docs/specs/semconv/hardware/common/ "Semantic conventions for common hardware metrics") 
                *   - [x] [Network](https://opentelemetry.io/docs/specs/semconv/hardware/network/ "Semantic conventions for network metrics") 
                *   - [x] [Physical Disk](https://opentelemetry.io/docs/specs/semconv/hardware/physical-disk/ "Semantic conventions for physical disk metrics") 
                *   - [x] [Physical host](https://opentelemetry.io/docs/specs/semconv/hardware/host/ "Semantic conventions for physical host metrics") 
                *   - [x] [Power Supply](https://opentelemetry.io/docs/specs/semconv/hardware/power-supply/ "Semantic conventions for power supply metrics") 
                *   - [x] [Tape Drive](https://opentelemetry.io/docs/specs/semconv/hardware/tape-drive/ "Semantic conventions for tape drive metrics") 
                *   - [x] [Temperature](https://opentelemetry.io/docs/specs/semconv/hardware/temperature/ "Semantic conventions for temperature metrics") 
                *   - [x] [Voltage](https://opentelemetry.io/docs/specs/semconv/hardware/voltage/ "Semantic conventions for voltage metrics") 

            *   - [x] [How to write conventions](https://opentelemetry.io/docs/specs/semconv/how-to-write-conventions/ "How to write semantic conventions") 
                *   - [x] [Resource and Entities](https://opentelemetry.io/docs/specs/semconv/how-to-write-conventions/resource-and-entities/) 
                *   - [x] [Status Metrics](https://opentelemetry.io/docs/specs/semconv/how-to-write-conventions/status-metrics/ "State Metrics") 
                *   - [x] [T-shaped Signals](https://opentelemetry.io/docs/specs/semconv/how-to-write-conventions/t-shaped-signals/) 

            *   - [x] [HTTP](https://opentelemetry.io/docs/specs/semconv/http/ "Semantic conventions for HTTP") 
                *   - [x] [Exceptions](https://opentelemetry.io/docs/specs/semconv/http/http-exceptions/ "Semantic conventions for HTTP exceptions") 
                *   - [x] [Metrics](https://opentelemetry.io/docs/specs/semconv/http/http-metrics/ "Semantic conventions for HTTP metrics") 
                *   - [x] [Spans](https://opentelemetry.io/docs/specs/semconv/http/http-spans/ "Semantic conventions for HTTP spans") 

            *   - [x] [Messaging](https://opentelemetry.io/docs/specs/semconv/messaging/ "Semantic conventions for messaging systems") 
                *   - [x] [AWS SNS](https://opentelemetry.io/docs/specs/semconv/messaging/sns/ "Semantic conventions for AWS SNS") 
                *   - [x] [AWS SQS](https://opentelemetry.io/docs/specs/semconv/messaging/sqs/ "Semantic conventions for AWS SQS") 
                *   - [x] [Azure](https://opentelemetry.io/docs/specs/semconv/messaging/azure-messaging/ "Semantic conventions for Azure messaging systems") 
                *   - [x] [Google Cloud Pub/Sub](https://opentelemetry.io/docs/specs/semconv/messaging/gcp-pubsub/ "Semantic conventions for Google Cloud Pub/Sub") 
                *   - [x] [Kafka](https://opentelemetry.io/docs/specs/semconv/messaging/kafka/ "Semantic conventions for Kafka") 
                *   - [x] [Metrics](https://opentelemetry.io/docs/specs/semconv/messaging/messaging-metrics/ "Semantic conventions for messaging client metrics") 
                *   - [x] [RabbitMQ](https://opentelemetry.io/docs/specs/semconv/messaging/rabbitmq/ "Semantic conventions for RabbitMQ") 
                *   - [x] [RocketMQ](https://opentelemetry.io/docs/specs/semconv/messaging/rocketmq/ "Semantic conventions for RocketMQ") 
                *   - [x] [Spans](https://opentelemetry.io/docs/specs/semconv/messaging/messaging-spans/ "Semantic conventions for messaging spans") 

            *   - [x] [Mobile](https://opentelemetry.io/docs/specs/semconv/mobile/ "Semantic conventions for mobile platform") 
                *   - [x] [Events](https://opentelemetry.io/docs/specs/semconv/mobile/mobile-events/ "Semantic conventions for mobile events") 

            *   - [x] [NFS](https://opentelemetry.io/docs/specs/semconv/nfs/ "Semantic conventions for NFS") 
                *   - [x] [NFS](https://opentelemetry.io/docs/specs/semconv/nfs/nfs-metrics/ "Semantic conventions for NFS metrics") 

            *   - [x] [Non-normative](https://opentelemetry.io/docs/specs/semconv/non-normative/ "Non-normative supplementary information") 
                *   - [x] [Code attributes migration](https://opentelemetry.io/docs/specs/semconv/non-normative/code-attrs-migration/ "Code attributes semantic convention stability migration guide") 
                *   - [x] [Compatibility](https://opentelemetry.io/docs/specs/semconv/non-normative/compatibility/) 
                    *   - [x] [AWS](https://opentelemetry.io/docs/specs/semconv/non-normative/compatibility/aws/ "Compatibility considerations for AWS") 
                    *   - [x] [gRPC](https://opentelemetry.io/docs/specs/semconv/non-normative/compatibility/grpc/ "Compatibility between OpenTelemetry and gRPC semantic conventions") 

                *   - [x] [Database migration](https://opentelemetry.io/docs/specs/semconv/non-normative/db-migration/ "Database semantic convention stability migration guide") 
                *   - [x] [Generating semantic convention libraries](https://opentelemetry.io/docs/specs/semconv/non-normative/code-generation/) 
                *   - [x] [HTTP migration](https://opentelemetry.io/docs/specs/semconv/non-normative/http-migration/ "HTTP semantic convention stability migration") 
                *   - [x] [K8s attributes](https://opentelemetry.io/docs/specs/semconv/non-normative/k8s-attributes/ "Specify resource attributes using Kubernetes annotations") 
                *   - [x] [K8s migration](https://opentelemetry.io/docs/specs/semconv/non-normative/k8s-migration/ "K8s semantic convention stability migration") 
                *   - [x] [Naming known exceptions](https://opentelemetry.io/docs/specs/semconv/non-normative/naming-known-exceptions/ "Kubernetes naming exceptions") 
                *   - [x] [Recommended vs Opt-In CPU Metrics](https://opentelemetry.io/docs/specs/semconv/non-normative/groups/system/cpu-metrics-guidelines/) 
                *   - [x] [RPC migration](https://opentelemetry.io/docs/specs/semconv/non-normative/rpc-migration/ "RPC semantic convention stability migration guide") 
                *   - [x] [System semantic conventions: instrumentation design philosophy](https://opentelemetry.io/docs/specs/semconv/non-normative/groups/system/design-philosophy/) 
                *   - [x] [System use cases](https://opentelemetry.io/docs/specs/semconv/non-normative/groups/system/use-cases/ "System semantic conventions: general use cases") 

            *   - [x] [Object stores](https://opentelemetry.io/docs/specs/semconv/object-stores/ "Semantic conventions for object stores") 
                *   - [x] [S3](https://opentelemetry.io/docs/specs/semconv/object-stores/s3/ "Semantic conventions for AWS S3 client spans") 

            *   - [x] [OpenTelemetry SDK](https://opentelemetry.io/docs/specs/semconv/otel/ "Semantic conventions for OpenTelemetry SDK") 
                *   - [x] [SDK Metrics](https://opentelemetry.io/docs/specs/semconv/otel/sdk-metrics/ "Semantic conventions for OpenTelemetry SDK metrics") 

            *   - [x] [Resource](https://opentelemetry.io/docs/specs/semconv/resource/ "Resource semantic conventions") 
                *   - [x] [Android](https://opentelemetry.io/docs/specs/semconv/resource/android/) 
                *   - [x] [Browser](https://opentelemetry.io/docs/specs/semconv/resource/browser/) 
                *   - [x] [CICD](https://opentelemetry.io/docs/specs/semconv/resource/cicd/) 
                *   - [x] [Cloud](https://opentelemetry.io/docs/specs/semconv/resource/cloud/) 
                *   - [x] [Cloud provider](https://opentelemetry.io/docs/specs/semconv/resource/cloud-provider/) 
                    *   - [x] [AWS](https://opentelemetry.io/docs/specs/semconv/resource/cloud-provider/aws/ "AWS semantic conventions") 
                        *   - [x] [ECS](https://opentelemetry.io/docs/specs/semconv/resource/cloud-provider/aws/ecs/ "AWS ECS") 
                        *   - [x] [EKS](https://opentelemetry.io/docs/specs/semconv/resource/cloud-provider/aws/eks/ "AWS EKS") 
                        *   - [x] [Logs](https://opentelemetry.io/docs/specs/semconv/resource/cloud-provider/aws/logs/ "AWS logs") 

                    *   - [x] [GCP](https://opentelemetry.io/docs/specs/semconv/resource/cloud-provider/gcp/ "GCP semantic conventions") 
                        *   - [x] [Google Cloud AppHub](https://opentelemetry.io/docs/specs/semconv/resource/cloud-provider/gcp/apphub/) 
                        *   - [x] [Google Cloud Run](https://opentelemetry.io/docs/specs/semconv/resource/cloud-provider/gcp/cloud-run/) 
                        *   - [x] [Google Compute Engine](https://opentelemetry.io/docs/specs/semconv/resource/cloud-provider/gcp/gce/) 

                    *   - [x] [Heroku](https://opentelemetry.io/docs/specs/semconv/resource/cloud-provider/heroku/) 

                *   - [x] [CloudFoundry](https://opentelemetry.io/docs/specs/semconv/resource/cloudfoundry/) 
                *   - [x] [Container](https://opentelemetry.io/docs/specs/semconv/resource/container/) 
                *   - [x] [Deployment](https://opentelemetry.io/docs/specs/semconv/resource/deployment-environment/) 
                *   - [x] [Device](https://opentelemetry.io/docs/specs/semconv/resource/device/) 
                *   - [x] [FaaS](https://opentelemetry.io/docs/specs/semconv/resource/faas/ "Function as a Service") 
                *   - [x] [Host](https://opentelemetry.io/docs/specs/semconv/resource/host/) 
                *   - [x] [Kubernetes](https://opentelemetry.io/docs/specs/semconv/resource/k8s/) 
                    *   - [x] [Openshift](https://opentelemetry.io/docs/specs/semconv/resource/k8s/openshift/) 

                *   - [x] [Operating system](https://opentelemetry.io/docs/specs/semconv/resource/os/) 
                *   - [x] [Process](https://opentelemetry.io/docs/specs/semconv/resource/process/ "Process and process runtime resources") 
                *   - [x] [Service](https://opentelemetry.io/docs/specs/semconv/resource/service/ "Service semantic conventions") 
                *   - [x] [Webengine](https://opentelemetry.io/docs/specs/semconv/resource/webengine/) 
                *   - [x] [z/OS software](https://opentelemetry.io/docs/specs/semconv/resource/zos/) 

            *   - [x] [RPC](https://opentelemetry.io/docs/specs/semconv/rpc/ "Semantic conventions for RPC") 
                *   - [x] [Connect](https://opentelemetry.io/docs/specs/semconv/rpc/connect-rpc/ "Semantic conventions for Connect RPC") 
                *   - [x] [Dubbo](https://opentelemetry.io/docs/specs/semconv/rpc/dubbo/ "Semantic conventions for Apache Dubbo") 
                *   - [x] [Exceptions](https://opentelemetry.io/docs/specs/semconv/rpc/rpc-exceptions/ "Semantic conventions for RPC exceptions") 
                *   - [x] [gRPC](https://opentelemetry.io/docs/specs/semconv/rpc/grpc/ "Semantic conventions for gRPC") 
                *   - [x] [JSON-RPC](https://opentelemetry.io/docs/specs/semconv/rpc/json-rpc/ "Semantic conventions for JSON-RPC") 
                *   - [x] [Metrics](https://opentelemetry.io/docs/specs/semconv/rpc/rpc-metrics/ "Semantic conventions for RPC metrics") 
                *   - [x] [Spans](https://opentelemetry.io/docs/specs/semconv/rpc/rpc-spans/ "Semantic conventions for RPC spans") 

            *   - [x] [Runtime environment](https://opentelemetry.io/docs/specs/semconv/runtime/ "Semantic conventions for runtime environment") 
                *   - [x] [.NET](https://opentelemetry.io/docs/specs/semconv/runtime/dotnet-metrics/ "Semantic conventions for .NET Common Language Runtime (CLR) metrics") 
                *   - [x] [CPython](https://opentelemetry.io/docs/specs/semconv/runtime/cpython-metrics/ "Semantic conventions for CPython runtime metrics") 
                *   - [x] [Go](https://opentelemetry.io/docs/specs/semconv/runtime/go-metrics/ "Semantic conventions for Go runtime metrics") 
                *   - [x] [JVM](https://opentelemetry.io/docs/specs/semconv/runtime/jvm-metrics/ "Semantic conventions for JVM metrics") 
                *   - [x] [Node.js](https://opentelemetry.io/docs/specs/semconv/runtime/nodejs-metrics/ "Semantic conventions for Node.js runtime metrics") 
                *   - [x] [V8 JS engine](https://opentelemetry.io/docs/specs/semconv/runtime/v8js-metrics/ "Semantic conventions for V8 JS engine runtime metrics") 

            *   - [x] [System](https://opentelemetry.io/docs/specs/semconv/system/ "System semantic conventions") 
                *   - [x] [Container](https://opentelemetry.io/docs/specs/semconv/system/container-metrics/ "Semantic conventions for container metrics") 
                *   - [x] [Kubernetes](https://opentelemetry.io/docs/specs/semconv/system/k8s-metrics/ "Semantic conventions for Kubernetes metrics") 
                *   - [x] [OpenShift](https://opentelemetry.io/docs/specs/semconv/system/openshift-metrics/ "Semantic conventions for OpenShift metrics") 
                *   - [x] [OS process](https://opentelemetry.io/docs/specs/semconv/system/process-metrics/ "Semantic conventions for OS process metrics") 
                *   - [x] [System](https://opentelemetry.io/docs/specs/semconv/system/system-metrics/ "Semantic conventions for system metrics") 

            *   - [x] [URL](https://opentelemetry.io/docs/specs/semconv/url/ "Semantic conventions for URL") 

    *   - [x] [Security](https://opentelemetry.io/docs/security/) 
        *   - [x] [Common Vulnerabilities and Exposures](https://opentelemetry.io/docs/security/cve/) 
        *   - [x] [Handling sensitive data](https://opentelemetry.io/docs/security/handling-sensitive-data/) 
        *   - [x] [Community incident response guidelines](https://opentelemetry.io/docs/security/security-response/) 
        *   - [x] [Collector configuration](https://opentelemetry.io/docs/security/config-best-practices/ "Collector configuration best practices") 
        *   - [x] [Collector hosting](https://opentelemetry.io/docs/security/hosting-best-practices/ "Collector hosting best practices") 

    *   - [x] [Contributing](https://opentelemetry.io/docs/contributing/) 
        *   - [x] [Prerequisites](https://opentelemetry.io/docs/contributing/prerequisites/) 
        *   - [x] [Issues](https://opentelemetry.io/docs/contributing/issues/) 
        *   - [x] [Submitting content](https://opentelemetry.io/docs/contributing/pull-requests/) 
        *   - [x] [Style guide](https://opentelemetry.io/docs/contributing/style-guide/ "Documentation style guide") 
        *   - [x] [Localization](https://opentelemetry.io/docs/contributing/localization/ "Site localization") 
        *   - [x] [Blog](https://opentelemetry.io/docs/contributing/blog/) 
        *   - [x] [Pull request checks](https://opentelemetry.io/docs/contributing/pr-checks/) 
        *   - [x] [Announcements](https://opentelemetry.io/docs/contributing/announcements/) 
        *   - [x] [Dev setup and more](https://opentelemetry.io/docs/contributing/development/ "Development setup and commands to build, serve, and more") 
        *   - [x] [SIG practices](https://opentelemetry.io/docs/contributing/sig-practices/ "SIG practices for approver and maintainers") 
        *   - [x] [Acknowledgements](https://opentelemetry.io/docs/contributing/acknowledgements/) 

[View page source](https://github.com/open-telemetry/opentelemetry.io/tree/main/content/en/docs/languages/dotnet/traces/links-based-sampler.md)[Edit this page](https://github.com/open-telemetry/opentelemetry.io/edit/main/content/en/docs/languages/dotnet/traces/links-based-sampler.md)[Create child page](https://github.com/open-telemetry/opentelemetry.io/new/main/content/en/docs/languages/dotnet/traces?filename=change-me.md&value=---%0Atitle%3A+%22Long+Page+Title%22%0AlinkTitle%3A+%22Short+Nav+Title%22%0Aweight%3A+100%0Adescription%3A+%3E-%0A+++++Page+description+for+heading+and+indexes.%0A---%0A%0A%23%23+Heading%0A%0AEdit+this+template+to+create+your+new+page.%0A%0A%2A+Give+it+a+good+name%2C+ending+in+%60.md%60+-+e.g.+%60get-started.md%60%0A%2A+Edit+the+%22front+matter%22+section+at+the+top+of+the+page+%28weight+controls+how+its+ordered+amongst+other+pages+in+the+same+directory%3B+lowest+number+first%29.%0A%2A+Add+a+good+commit+message+at+the+bottom+of+the+page+%28%3C80+characters%3B+use+the+extended+description+field+for+more+detail%29.%0A%2A+Create+a+new+branch+so+you+can+preview+your+new+file+and+request+a+review+via+Pull+Request.%0A)[Create documentation issue](https://github.com/open-telemetry/opentelemetry.io/issues/new?title=Links-based%20sampling)

On this page[](https://opentelemetry.io/docs/languages/dotnet/traces/links-based-sampler/# "Top of page")

*   [How does this sampling example work?](https://opentelemetry.io/docs/languages/dotnet/traces/links-based-sampler/#how-does-this-sampling-example-work)
*   [When should you consider such an option? What are the tradeoffs?](https://opentelemetry.io/docs/languages/dotnet/traces/links-based-sampler/#when-should-you-consider-such-an-option-what-are-the-tradeoffs)
    *   [Not guaranteed to give consistent sampling in all situations](https://opentelemetry.io/docs/languages/dotnet/traces/links-based-sampler/#not-guaranteed-to-give-consistent-sampling-in-all-situations)
    *   [Can lead to higher volume of data](https://opentelemetry.io/docs/languages/dotnet/traces/links-based-sampler/#can-lead-to-higher-volume-of-data)

*   [Sample output](https://opentelemetry.io/docs/languages/dotnet/traces/links-based-sampler/#sample-output)

1.   [Docs](https://opentelemetry.io/docs/)
2.   [Language APIs & SDKs](https://opentelemetry.io/docs/languages/)
3.   [.NET](https://opentelemetry.io/docs/languages/dotnet/)
4.   [Traces](https://opentelemetry.io/docs/languages/dotnet/traces/)
5.   Links-based sampling

Links-based sampling
====================

Certain scenarios such as a producer consumer scenario can be modeled using “span links” to express causality between activities. An activity (span) in a trace can link to any number of activities in other traces. When using a parent based sampler, the sampling decision is made at the level of a single trace. This implies that the sampling decision across such linked traces is taken independently without any consideration to the links. This can result in incomplete information to reason about a system. Ideally, it would be desirable to sample all linked traces together.

As one possible way to address this, this example shows how we can increase the likelihood of having complete traces across linked traces.

How does this sampling example work?[](https://opentelemetry.io/docs/languages/dotnet/traces/links-based-sampler/#how-does-this-sampling-example-work)
------------------------------------------------------------------------------------------------------------------------------------------------------

We use a composite sampler that makes use of two samplers:

1.   A parent based sampler.
2.   A links based sampler.

This composite sampler first delegates to the parent based sampler. If the parent based sampler decides to sample, then the composite sampler decides to sample. However, if the parent based sampler decides to drop, the composite sampler delegates to the links based sampler. The links based sampler decides to sample if the activity has any linked activities and if at least ONE of those linked activities is sampled.

The links based sampler is not a probabilistic sampler. It is a biased sampler that decides to sample an activity if any of the linked contexts are sampled.

When should you consider such an option? What are the tradeoffs?[](https://opentelemetry.io/docs/languages/dotnet/traces/links-based-sampler/#when-should-you-consider-such-an-option-what-are-the-tradeoffs)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This may be a good option to consider if you want to get more complete traces across linked traces. However, there are a few tradeoffs to consider:

### Not guaranteed to give consistent sampling in all situations[](https://opentelemetry.io/docs/languages/dotnet/traces/links-based-sampler/#not-guaranteed-to-give-consistent-sampling-in-all-situations)

This approach doesn’t guarantee that you will get complete traces across linked traces in all situations.

Let’s look at a couple of cases using the same producer-consumer example scenario. Let’s say we have a producer activity (say with ID S1 in Trace T1) that produces a message and a consumer activity (say with ID S2 in Trace T2) that consumes the message.

Now, let’s say that the producing activity S1 in trace T1 is sampled, say using the decision of a parent based sampler. Let’s say that the activity S2 in trace T2 is not sampled based on the parent based sampler decision for T2. However, since this activity S2 in T2 is linked to the producing activity (S1 in T1) that is sampled, this mechanism ensures that the consuming activity (S2 in T2) will also get sampled.

Alternatively, let’s consider what happens if the producing activity S1 in trace T1 is not sampled, say using the decision of a parent based sampler. Now, let’s say that the consuming activity S2 in trace T2 is sampled, based on the decision of a parent based sampler. In this case, we can see that activity S2 in trace T2 is sampled even though activity S1 in trace T1 is not sampled. This is an example of a situation where this approach is not helpful.

Another example of a situation where you would get a partial trace is if the consuming activity S2 in trace T2 is not the root activity in trace T2. In this case, let’s say there’s a different activity S3 in trace T2 that is the root activity. Let’s say that the sampling decision for activity S3 was to drop it. Now, since S2 in trace T2 links to S1 in trace T1, with this approach S2 will be sampled (based on the linked context). Hence, the produced trace T2 will be a partial trace as it will not include activity S3 but will include activity S2.

### Can lead to higher volume of data[](https://opentelemetry.io/docs/languages/dotnet/traces/links-based-sampler/#can-lead-to-higher-volume-of-data)

Since this approach will sample in activities even if one of the linked activities is sampled, it can lead to higher volumes of data, as compared to regular head based sampling. This is because we are making a non-probabilistic sampling decision here based on the sampling decisions of linked activities. For example, if there are 20 linked activities and even if only one of them is sampled, then the linking activity will be sampled.

Sample output[](https://opentelemetry.io/docs/languages/dotnet/traces/links-based-sampler/#sample-output)
---------------------------------------------------------------------------------------------------------

You should see output such as the below when you run this example.

```text
af448bc1cb3e5be4e4b56a8b6650785c: ParentBasedSampler decision: Drop
af448bc1cb3e5be4e4b56a8b6650785c: No linked span is sampled. Hence,
LinksBasedSampler decision is Drop.

1b08120fa35c3f4a37e0b6326dc7688c: ParentBasedSampler decision: Drop
1b08120fa35c3f4a37e0b6326dc7688c: No linked span is sampled. Hence,
LinksBasedSampler decision is Drop.

ff710bd70baf2e8e843e7b38d1fc4cc1: ParentBasedSampler decision: RecordAndSample
Activity.TraceId:            ff710bd70baf2e8e843e7b38d1fc4cc1
Activity.SpanId:             620d9b218afbf926
Activity.TraceFlags:         Recorded
Activity.ActivitySourceName: LinksAndParentBasedSampler.Example
Activity.DisplayName:        Main
Activity.Kind:               Internal
Activity.StartTime:          2023-04-18T16:52:16.0373932Z
Activity.Duration:           00:00:00.0022481
Activity.Tags:
    foo: bar
Activity.Links:
    f7464f714b23713c9008f8fc884fc391 7d1c96a6f2c95556
    6660db8951e10644f63cd385e7b9549e 526e615b7a70121a
    4c94df8e520b32ff25fc44e0c8063c81 8080d0aaafa641af
    70d8ba08181b5ec073ec8b5db778c41f 99ea6162257046ab
    d96954e9e76835f442f62eece3066be4 ae9332547b80f50f
Resource associated with Activity:
    service.name: unknown_service:links-sampler

68121534d69b2248c4816c0c5281f908: ParentBasedSampler decision: Drop
68121534d69b2248c4816c0c5281f908: No linked span is sampled. Hence,
LinksBasedSampler decision is Drop.

5042f2c52a08143f5f42be3818eb41fa: ParentBasedSampler decision: Drop
5042f2c52a08143f5f42be3818eb41fa: At least one linked activity
(TraceID: 5c1185c94f56ebe3c2ccb4b9880afb17, SpanID: 1f77abf0bded4ab9) is sampled.
Hence, LinksBasedSampler decision is RecordAndSample

Activity.TraceId:            5042f2c52a08143f5f42be3818eb41fa
Activity.SpanId:             0f8a9bfa9d7770e6
Activity.TraceFlags:         Recorded
Activity.ActivitySourceName: LinksAndParentBasedSampler.Example
Activity.DisplayName:        Main
Activity.Kind:               Internal
Activity.StartTime:          2023-04-18T16:52:16.0806081Z
Activity.Duration:           00:00:00.0018874
Activity.Tags:
    foo: bar
Activity.Links:
    ed77487f4a646399aea5effc818d8bfa fcdde951f29a13e0
    f79860fdfb949f2c1f1698d1ed8036b9 e422cb771057bf7c
    6326338d0c0cf3afe7c5946d648b94dc affc7a6c013ea273
    c0750a9fa146062083b55227ac965ad4 b09d59ed3129779d
    5c1185c94f56ebe3c2ccb4b9880afb17 1f77abf0bded4ab9
Resource associated with Activity:
    service.name: unknown_service:links-sampler

568a2b9489c58e7a5a769d264a9ddf28: ParentBasedSampler decision: Drop
568a2b9489c58e7a5a769d264a9ddf28: No linked span is sampled. Hence,
LinksBasedSampler decision is Drop.

4f8d972b0d7727821ce4a307a7be8e8f: ParentBasedSampler decision: Drop
4f8d972b0d7727821ce4a307a7be8e8f: No linked span is sampled. Hence,
LinksBasedSampler decision is Drop.

ce940241ed33e1a030da3e9d201101d3: ParentBasedSampler decision: Drop
ce940241ed33e1a030da3e9d201101d3: At least one linked activity
(TraceID: ba0d91887309399029719e2a71a12f62, SpanID: 61aafe295913080f) is sampled.
Hence, LinksBasedSampler decision is RecordAndSample

Activity.TraceId:            ce940241ed33e1a030da3e9d201101d3
Activity.SpanId:             5cf3d63926ce4fd5
Activity.TraceFlags:         Recorded
Activity.ActivitySourceName: LinksAndParentBasedSampler.Example
Activity.DisplayName:        Main
Activity.Kind:               Internal
Activity.StartTime:          2023-04-18T16:52:16.1127688Z
Activity.Duration:           00:00:00.0021072
Activity.Tags:
    foo: bar
Activity.Links:
    5223cff39311c741ef50aca58e4270c3 e401b6840acebf43
    398b43fee8a75b068cdd11018ef528b0 24cfa4d5fb310b9d
    34351a0f492d65ef92ca0db3238f5146 5c0a56a16291d765
    ba0d91887309399029719e2a71a12f62 61aafe295913080f
    de18a8af2d20972cd4f9439fcd51e909 4c40bc6037e58bf9
Resource associated with Activity:
    service.name: unknown_service:links-sampler

ac46618da4495897bacd7d399e6fc6d8: ParentBasedSampler decision: Drop
ac46618da4495897bacd7d399e6fc6d8: No linked span is sampled. Hence,
LinksBasedSampler decision is Drop.

68a3a05e0348d2a2c1c3db34bc3fd2f5: ParentBasedSampler decision: Drop
68a3a05e0348d2a2c1c3db34bc3fd2f5: At least one linked activity
(TraceID: 87773d89fba942b0109d6ce0876bb67e, SpanID: 2aaac98d4e48c261) is sampled.
Hence, LinksBasedSampler decision is RecordAndSample

Activity.TraceId:            68a3a05e0348d2a2c1c3db34bc3fd2f5
Activity.SpanId:             3d0222f56b0e1e5d
Activity.TraceFlags:         Recorded
Activity.ActivitySourceName: LinksAndParentBasedSampler.Example
Activity.DisplayName:        Main
Activity.Kind:               Internal
Activity.StartTime:          2023-04-18T16:52:16.1553354Z
Activity.Duration:           00:00:00.0049821
Activity.Tags:
    foo: bar
Activity.Links:
    7175fbd18da2783dc594d1e8f3260c74 13019d9a06a5505b
    59c9bdd52eb5cf23eae9001006743fcf 25573e0f1b290b8d
    87773d89fba942b0109d6ce0876bb67e 2aaac98d4e48c261
    0a1f65c47f556336b4028b515d363810 0816a2a2b7d4ea0b
    7602375d3eae7e849a9dc27e858dc1c2 b918787b895b1374
Resource associated with Activity:
    service.name: unknown_service:links-sampler
```

Feedback
--------

Was this page helpful?

Yes No
Thank you. Your feedback is appreciated!

Please let us know [how we can improve this page](https://github.com/open-telemetry/opentelemetry.io/issues/new?template=PAGE_FEEDBACK.yml&title=[Page+feedback]%3A+ADD+A+SUMMARY+OF+YOUR+FEEDBACK+HERE). Your feedback is appreciated!

Last modified August 14, 2025: [Add remaining dotnet content (#7543) (79e067c8)](https://github.com/open-telemetry/opentelemetry.io/commit/79e067c8c5b770d89521a305c5fe410f07f46060)

*   [](https://github.com/open-telemetry/community#mailing-lists)
*   [](https://bsky.app/profile/opentelemetry.io)
*   [](https://fosstodon.org/@opentelemetry)
*   [](https://stackoverflow.com/questions/tagged/open-telemetry)
*   [](https://github.com/cncf/artwork/tree/master/projects/opentelemetry)
*   [](https://docs.google.com/spreadsheets/d/1SYKfjYhZdm2Wh2Cl6KVQalKg_m4NhTPZqq-8SzEVO6s)
*   [](https://lookerstudio.google.com/s/tSTKxK1ECeU)

*   [](https://github.com/open-telemetry)
*   [](https://cloud-native.slack.com/archives/CJFCJHG4Q)
*   [](https://opentelemetry.devstats.cncf.io/d/8/dashboards?orgId=1&refresh=15m)
*   [](https://www.linuxfoundation.org/legal/privacy-policy)
*   [](https://www.linuxfoundation.org/legal/trademark-usage)
*   [](https://opentelemetry.io/community/marketing-guidelines/)
*   [](https://opentelemetry.io/site/)

© 2019–present OpenTelemetry Authors | Docs [CC BY 4.0](https://creativecommons.org/licenses/by/4.0)All Rights Reserved
