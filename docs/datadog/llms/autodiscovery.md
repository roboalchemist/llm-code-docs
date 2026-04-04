# Source: https://docs.datadoghq.com/getting_started/containers/autodiscovery.md

# Source: https://docs.datadoghq.com/agent/troubleshooting/autodiscovery.md

---
title: Autodiscovery Troubleshooting
description: >-
  Debug Docker Agent Autodiscovery configuration issues and resolve template
  loading problems with configcheck commands.
breadcrumbs: Docs > Agent > Agent Troubleshooting > Autodiscovery Troubleshooting
---

# Autodiscovery Troubleshooting

To start troubleshooting the Docker Agent Autodiscovery, run the `configcheck` init script command:

```shell
docker exec -it <AGENT_CONTAINER_NAME> agent configcheck -v
```

**Note**: The `-v` option allows you to see all templates including the one that are unresolved.

For example, the following example is a valid Autodiscovery configuration for a Redis template being loaded from a Docker label annotationânot the default `redisdb.d/auto_conf.yaml` file:

```text
# docker exec -it <AGENT_CONTAINER_NAME> agent configcheck -v
.
..
...
=== Provider: Docker container labels ===

--- redisdb check ---
Instance 1:
host: 172.17.0.3
port: "6379"
tags:
- short_image:redis
- image_tag:latest
- docker_image:redis:latest
- image_name:redis
~
Auto-discovery IDs:
* docker://81e66fd4c948a502b4428417d8cf2ebc58caaff55a6e5879a41887057342aec2
```

The following examples show issues that could appear when failing to load a valid Autodiscovery configuration for a Redis template:

```text
# docker exec -it <AGENT_CONTAINER_NAME> agent configcheck -v
.
..
...
=== Resolve warnings ===

redisdb
* No service found with this AD identifier: redis
* Can't resolve the template for redisdb at this moment.

=== Unresolved Configs ===

Auto-discovery IDs: redis
Template:
init_config:
instances:
- host: '%%host%%'
  port: '%%port%%'
```

If you're still unsure about the issue, reach out to the [Datadog support team](https://docs.datadoghq.com/help/) with [a flare](https://docs.datadoghq.com/agent/troubleshooting/send_a_flare/) from your Agent.

## Further Reading{% #further-reading %}

- [Agent Troubleshooting](https://docs.datadoghq.com/agent/troubleshooting/)
- [Agent Debug Mode](https://docs.datadoghq.com/agent/troubleshooting/debug_mode/)
- [Send an Agent Flare](https://docs.datadoghq.com/agent/troubleshooting/send_a_flare/)
