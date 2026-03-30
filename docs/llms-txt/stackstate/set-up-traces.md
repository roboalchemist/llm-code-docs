# Source: https://archivedocs.stackstate.com/5.1/configure/traces/set-up-traces.md

# Set up traces

## Overview

This page describes the steps to set up traces that can be viewed in the StackState [Traces Perspective](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/perspectives/traces-perspective).

For traces to be available in StackState, the [StackState Agent V2 StackPack](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/agent) must be installed with one or more tracing integrations configured.

## Set up

### 1) Install StackState Agent V3

The StackState Agent V2 StackPack enables integration with external systems to receive trace data. You can check if it's installed on the StackPacks page in StackState. If it isn't installed, follow the [StackState Agent setup instructions](https://archivedocs.stackstate.com/5.1/setup/agent/about-stackstate-agent).

### 2) Configure tracing integrations

When the StackState Agent V2 StackPack is installed, you can configure integrations to receive trace data from external systems. One or more of the StackState integrations below can be configured to populate the Traces Perspective.

* The [AWS X-ray integration](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/aws/aws-x-ray) collects tracing information from the in-built AWS distributed tracing system.
* The [OpenTelemetry integration](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/opentelemetry/opentelemetry-nodejs) adds topology and telemetry information from AWS Lambdas to traces.
* The [DotNet APM integration](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/dotnet-apm) enables instrumentation for DotNet applications and sends traces back to StackState.
* The [Java APM integration](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/java-apm) enables tracing support for Java JVM based systems.
* The [Traefik integration](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/traefik) adds topology and telemetry information from Traefik to traces.
