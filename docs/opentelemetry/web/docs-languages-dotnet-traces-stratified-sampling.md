# Source: https://opentelemetry.io/docs/languages/dotnet/traces/stratified-sampling/

Title: Stratified sampling

URL Source: https://opentelemetry.io/docs/languages/dotnet/traces/stratified-sampling/

Markdown Content:
Stratified sampling | OpenTelemetry
===============

[OpenTelemetry](https://opentelemetry.io/)

*   [Docs](https://opentelemetry.io/docs/)
*   [Ecosystem](https://opentelemetry.io/ecosystem/)
*   [Status](https://opentelemetry.io/status/)
*   [Community](https://opentelemetry.io/community/)
*   [Training](https://opentelemetry.io/training/)
*   [Blog](https://opentelemetry.io/blog/)
*   
[English EN](https://opentelemetry.io/docs/languages/dotnet/traces/stratified-sampling/#)
    *   [বাংলা (Bengali)](https://opentelemetry.io/bn/docs/languages/dotnet/traces/stratified-sampling/)
    *   English
    *   [Español](https://opentelemetry.io/es/docs/languages/dotnet/traces/stratified-sampling/)
    *   [Français](https://opentelemetry.io/fr/docs/languages/dotnet/traces/stratified-sampling/)
    *   [日本語 (Japanese)](https://opentelemetry.io/ja/docs/languages/dotnet/traces/stratified-sampling/)
    *   [Português](https://opentelemetry.io/pt/docs/languages/dotnet/traces/stratified-sampling/)
    *   [Română (Romanian)](https://opentelemetry.io/ro/docs/languages/dotnet/traces/stratified-sampling/)
    *   [Українська (Ukrainian)](https://opentelemetry.io/uk/docs/languages/dotnet/traces/stratified-sampling/)
    *   [中文 (Chinese)](https://opentelemetry.io/zh/docs/languages/dotnet/traces/stratified-sampling/)

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

[View page source](https://github.com/open-telemetry/opentelemetry.io/tree/main/content/en/docs/languages/dotnet/traces/stratified-sampling.md)[Edit this page](https://github.com/open-telemetry/opentelemetry.io/edit/main/content/en/docs/languages/dotnet/traces/stratified-sampling.md)[Create child page](https://github.com/open-telemetry/opentelemetry.io/new/main/content/en/docs/languages/dotnet/traces?filename=change-me.md&value=---%0Atitle%3A+%22Long+Page+Title%22%0AlinkTitle%3A+%22Short+Nav+Title%22%0Aweight%3A+100%0Adescription%3A+%3E-%0A+++++Page+description+for+heading+and+indexes.%0A---%0A%0A%23%23+Heading%0A%0AEdit+this+template+to+create+your+new+page.%0A%0A%2A+Give+it+a+good+name%2C+ending+in+%60.md%60+-+e.g.+%60get-started.md%60%0A%2A+Edit+the+%22front+matter%22+section+at+the+top+of+the+page+%28weight+controls+how+its+ordered+amongst+other+pages+in+the+same+directory%3B+lowest+number+first%29.%0A%2A+Add+a+good+commit+message+at+the+bottom+of+the+page+%28%3C80+characters%3B+use+the+extended+description+field+for+more+detail%29.%0A%2A+Create+a+new+branch+so+you+can+preview+your+new+file+and+request+a+review+via+Pull+Request.%0A)[Create documentation issue](https://github.com/open-telemetry/opentelemetry.io/issues/new?title=Stratified%20sampling)

On this page[](https://opentelemetry.io/docs/languages/dotnet/traces/stratified-sampling/# "Top of page")

*   [What is stratified sampling?](https://opentelemetry.io/docs/languages/dotnet/traces/stratified-sampling/#what-is-stratified-sampling)
*   [Implementation approach](https://opentelemetry.io/docs/languages/dotnet/traces/stratified-sampling/#implementation-approach)
*   [Example code](https://opentelemetry.io/docs/languages/dotnet/traces/stratified-sampling/#example-code)
*   [Example output](https://opentelemetry.io/docs/languages/dotnet/traces/stratified-sampling/#example-output)
*   [Complete example](https://opentelemetry.io/docs/languages/dotnet/traces/stratified-sampling/#complete-example)

1.   [Docs](https://opentelemetry.io/docs/)
2.   [Language APIs & SDKs](https://opentelemetry.io/docs/languages/)
3.   [.NET](https://opentelemetry.io/docs/languages/dotnet/)
4.   [Traces](https://opentelemetry.io/docs/languages/dotnet/traces/)
5.   Stratified sampling

Stratified sampling
===================

Learn how to implement stratified sampling for OpenTelemetry traces in .NET

This guide demonstrates one possible way to achieve stratified sampling in OpenTelemetry .NET.

What is stratified sampling?[](https://opentelemetry.io/docs/languages/dotnet/traces/stratified-sampling/#what-is-stratified-sampling)
--------------------------------------------------------------------------------------------------------------------------------------

Stratified sampling is a way to divide a population into mutually exclusive sub-populations or “strata”. For example, the strata for a population of “queries” could be “user-initiated queries” and “programmatic queries”. Each stratum is then sampled using a probabilistic sampling method. This ensures that all sub-populations are represented.

Implementation approach[](https://opentelemetry.io/docs/languages/dotnet/traces/stratified-sampling/#implementation-approach)
-----------------------------------------------------------------------------------------------------------------------------

The SDK achieves this by using a custom `Sampler` that internally holds two samplers. Based on the stratum, the appropriate sampler is invoked.

One prerequisite for this is that the tag (for example, `queryType`) used for the stratified sampling decision must be provided as part of activity creation.

The SDK uses disproportionate stratified sampling, also known as “unequal probability sampling”. For example, the sample size of each sub-population is not proportionate to their occurrence in the overall population. In this example, we want to ensure that all user initiated queries are represented, so we use a 100% sampling rate for it, while the sampling rate chosen for programmatic queries is much lower.

Example code[](https://opentelemetry.io/docs/languages/dotnet/traces/stratified-sampling/#example-code)
-------------------------------------------------------------------------------------------------------

The key component is a custom `StratifiedSampler` class:

```csharp
public class StratifiedSampler : Sampler
{
    private readonly string _stratifyByTagName;
    private readonly Dictionary<string, Sampler> _samplersByStratum;
    private readonly Sampler _defaultSampler;

    public StratifiedSampler(
        string stratifyByTagName,
        Dictionary<string, Sampler> samplersByStratum,
        Sampler defaultSampler)
        : base()
    {
        _stratifyByTagName = stratifyByTagName;
        _samplersByStratum = samplersByStratum;
        _defaultSampler = defaultSampler;
    }

    public override SamplingResult ShouldSample(
        in SamplingParameters samplingParameters)
    {
        ReadOnlySpan<KeyValuePair<string, object>> attributes =
            samplingParameters.Tags;

        for (int i = 0; i < attributes.Length; i++)
        {
            if (attributes[i].Key.Equals(_stratifyByTagName,
                StringComparison.OrdinalIgnoreCase))
            {
                string stratum = attributes[i].Value.ToString().ToLowerInvariant();
                if (_samplersByStratum.TryGetValue(stratum, out Sampler sampler))
                {
                    Console.WriteLine($"StratifiedSampler handling {stratum} query");
                    return sampler.ShouldSample(samplingParameters);
                }

                break;
            }
        }

        return _defaultSampler.ShouldSample(samplingParameters);
    }

    public override string Description => $"StratifiedSampler: {_stratifyByTagName}";
}
```

Example output[](https://opentelemetry.io/docs/languages/dotnet/traces/stratified-sampling/#example-output)
-----------------------------------------------------------------------------------------------------------

When you run an application using this sampler, you should see output similar to the following:

```text
StratifiedSampler handling userinitiated query
Activity.TraceId:            1a122d63e5f8d32cb8ebd3e402eb5389
Activity.SpanId:             83bdc6bbebea1df8
Activity.TraceFlags:         Recorded
Activity.ParentSpanId:       1ddd00d845ad645e
Activity.ActivitySourceName: StratifiedSampling.POC
Activity.DisplayName:        Main
Activity.Kind:               Internal
Activity.StartTime:          2023-02-09T05:19:30.8156879Z
Activity.Duration:           00:00:00.0008656
Activity.Tags:
    queryType: userInitiated
    foo: child
Resource associated with Activity:
    service.name: unknown_service:Examples.StratifiedSamplingByQueryType

Activity.TraceId:            1a122d63e5f8d32cb8ebd3e402eb5389
Activity.SpanId:             1ddd00d845ad645e
Activity.TraceFlags:         Recorded
Activity.ActivitySourceName: StratifiedSampling.POC
Activity.DisplayName:        Main
Activity.Kind:               Internal
Activity.StartTime:          2023-02-09T05:19:30.8115186Z
Activity.Duration:           00:00:00.0424036
Activity.Tags:
    queryType: userInitiated
    foo: bar
Resource associated with Activity:
    service.name: unknown_service:Examples.StratifiedSamplingByQueryType
```

This shows that the two sub-populations (strata) are being sampled independently, with different sampling rates applied to each stratum.

Complete example[](https://opentelemetry.io/docs/languages/dotnet/traces/stratified-sampling/#complete-example)
---------------------------------------------------------------------------------------------------------------

For the complete example including a working application, see the [OpenTelemetry .NET repository](https://github.com/open-telemetry/opentelemetry-dotnet/tree/main/examples).

Feedback
--------

Was this page helpful?

Yes No
Thank you. Your feedback is appreciated!

Please let us know [how we can improve this page](https://github.com/open-telemetry/opentelemetry.io/issues/new?template=PAGE_FEEDBACK.yml&title=[Page+feedback]%3A+ADD+A+SUMMARY+OF+YOUR+FEEDBACK+HERE). Your feedback is appreciated!

Last modified August 12, 2025: [Add dotnet docs from /docs folder of opentelemetry-dotnet (#7474) (bb927496)](https://github.com/open-telemetry/opentelemetry.io/commit/bb9274966fe63396fc2e1787489f999aa124cf43)

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
