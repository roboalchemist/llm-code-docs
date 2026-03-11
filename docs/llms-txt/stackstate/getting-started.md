# Source: https://archivedocs.stackstate.com/open-telemetry/getting-started.md

# Getting started

![Open Telemetry collector and 2 instrumented applications sending metrics and traces to StackState](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-9fc9eb9a0525a01f3e5331dfd2254b4f2bbeffc9%2Fopen-telemetry.svg?alt=media)

StackState supports [Open Telemetry](https://opentelemetry.io/docs/what-is-opentelemetry/). Open Telemetry is a set of standardized protocols and an open-source framework to collect, transform and ship telemetry data such as traces, metrics and logs. Open telemetry supports a wide variety of programming languages and platforms.

StackState has support for both metrics and traces and adds the Open Telemetry metrics and traces to the (Kubernetes) topology data that is provided by the StackState agent. Therefore it is still needed to also install the StackState agent. Support for logs and using Open Telemetry without the StackState agent is coming soon.

Open Telemetry consists of several different components. For usage with StackState, the [SDKs](https://archivedocs.stackstate.com/open-telemetry/languages) to instrument your application and the [Open Telemetry collector](https://archivedocs.stackstate.com/open-telemetry/collector) are the most important parts. We'll show how to configure both for usage with StackState.

If your application is already instrumented with Open Telemetry or with any other library that is supported by Open Telemetry, like Jaeger or Zipkin, the collector can be used to ship that data to StackState and no additional instrumentation is needed.

StackState requires the collector to be configured with specific processors and authentication to make sure all data used by StackState is available.

## References

* [Open Telemetry collector](https://opentelemetry.io/docs/collector/) on the Open Telemetry documentation
* [SDKs to instrument your application](https://opentelemetry.io/docs/languages/) on the Open Telemetry documentation
