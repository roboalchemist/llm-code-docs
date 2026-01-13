# Source: https://docs.datadoghq.com/tracing/guide/trace-agent-from-source.md

---
title: Installing the trace Agent from source
description: >-
  Learn how to install and compile the Datadog Trace Agent from source code
  using Go for development and testing purposes.
breadcrumbs: Docs > APM > Tracing Guides > Installing the trace Agent from source
source_url: https://docs.datadoghq.com/guide/trace-agent-from-source/index.html
---

# Installing the trace Agent from source

## Install from source{% #install-from-source %}

1. Install `Go 1.11+`. For more information, see the steps on the [official Go website](https://golang.org/dl).

1. Clone the [Datadog Agent repo](https://github.com/DataDog/datadog-agent).

1. Run this command in the root of the `datadog-agent` repository:

   ```bash
   go install ./cmd/trace-agent
   ```

1. Run the Agent using `trace-agent` (assuming the path `$GOPATH/bin` is in your system's `$PATH`).

### Troubleshooting{% #troubleshooting %}

Check the Agent output or logs (`/var/log/datadog/trace-agent.log` on Linux) to ensure that traces seem correct and that they are reaching the Datadog API.
