# Source: https://archivedocs.stackstate.com/5.1/stackpacks/integrations/opentelemetry/manual-instrumentation/prerequisites.md

# Prerequisites

To set up a OpenTelemetry manual instrumentations, you need to have:

* [StackState Agent](https://archivedocs.stackstate.com/5.1/setup/agent/about-stackstate-agent) v2.17 (or later)
* [Traces enabled](https://archivedocs.stackstate.com/5.1/setup/agent/advanced-agent-configuration#enable-traces) on StackState Agent. If traces aren't enabled on the Agent, OpenTelemetry won't generate any data.
* The [Agent StackPack](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/agent) should be installed in StackState.
