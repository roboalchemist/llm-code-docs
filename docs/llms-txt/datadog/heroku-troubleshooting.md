# Source: https://docs.datadoghq.com/agent/guide/heroku-troubleshooting.md

---
title: Datadog-Heroku Buildpack troubleshooting
description: >-
  Debug Heroku deployments using Datadog buildpack with the agent-wrapper
  command, custom metrics testing, and log collection.
breadcrumbs: Docs > Agent > Agent Guides > Datadog-Heroku Buildpack troubleshooting
source_url: https://docs.datadoghq.com/guide/heroku-troubleshooting/index.html
---

# Datadog-Heroku Buildpack troubleshooting

To start debugging Heroku, use the `agent-wrapper` command with the information/debugging commands listed in the [Agent documentation](https://docs.datadoghq.com/agent/configuration/agent-commands/#agent-status-and-information).

For example, to display the status of your Datadog Agent and enabled integrations, run:

```shell
agent-wrapper status
```

Next, verify the Datadog Agent is listening by sending a custom metric. From your project directory, run:

```shell
heroku run bash

# Once your Dyno has started and you are at the command line
echo -n "custom_metric:60|g|#shell" >/dev/udp/localhost/8125
```

After a few moments, use the metrics explorer to verify that the metric was received.

It can also be helpful to obtain Agent and Trace Agent logs from your running dyno.

Download Datadog Agent logs:

```shell
heroku ps:copy /app/.apt/var/log/datadog/datadog.log --dyno=<YOUR DYNO NAME>
```

Download Datadog Trace Agent logs:

```shell
heroku ps:copy /app/.apt/var/log/datadog/datadog-apm.log --dyno=<YOUR DYNO NAME>
```

## Send a flare{% #send-a-flare %}

Generate a flare by running the [`agent-wrapper` command](https://docs.datadoghq.com/agent/configuration/agent-commands/#agent-status-and-information):

```shell
agent-wrapper flare
```
