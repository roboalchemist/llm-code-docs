# Source: https://docs.datadoghq.com/agent/guide/environment-variables.md

---
title: Agent Environment Variables
description: >-
  Configure Datadog Agent settings using environment variables as an alternative
  to datadog.yaml, including naming conventions and systemd usage.
breadcrumbs: Docs > Agent > Agent Guides > Agent Environment Variables
---

# Agent Environment Variables

{% alert level="danger" %}
For Agent v5, reference the [Docker Agent GitHub repo](https://github.com/DataDog/docker-dd-agent#environment-variables).
{% /alert %}

## Overview{% #overview %}

For Agent v6, most of the configuration options in the [Agent's main configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/#agent-main-configuration-file) (`datadog.yaml`) can be set through environment variables.

## Recommendations{% #recommendations %}

As a best practice, Datadog recommends using unified service tagging when assigning tags. Unified service tagging ties Datadog telemetry together through the use of three standard tags: `env`, `service`, and `version`. To learn how to configure your environment with unified tagging, see the [unified service tagging documentation](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging).

## General use{% #general-use %}

In general, use the following rules:

- Option names should be uppercase with the `DD_` prefix: `hostname` -> `DD_HOSTNAME`

- List values should be separated by spaces (Include rules support regexes, and are defined as a list of comma-separated strings):

  ```yaml
     container_include:
       - "image:cp-kafka"
       - "image:k8szk"
     # DD_CONTAINER_INCLUDE="image:cp-kafka image:k8szk"
  ```

- The nesting of config options with **predefined** keys should be separated with an underscore:

  ```yaml
     cluster_agent:
       cmd_port: 5005
     # DD_CLUSTER_AGENT_CMD_PORT=5005
  ```

- The nesting of config options with **user-defined** keys must be JSON-formatted:

  ```yaml
     container_env_as_tags:
       ENVVAR_NAME: tag_name
     # DD_CONTAINER_ENV_AS_TAGS='{"ENVVAR_NAME": "tag_name"}'
  ```

### Property definition priority{% #property-definition-priority %}

- If a property is defined in both the global configuration file (`datadog.yaml`) and as an environment variable, the environment variable takes precedence.
- Specifying a nested option with an environment variable overrides *all* the nested options specified under the config option. The exception to this rule is the `proxy` config option. Reference the [Agent proxy documentation](https://docs.datadoghq.com/agent/configuration/proxy/#environment-variables) for more details.

### Exceptions{% #exceptions %}

- Not all `datadog.yaml` options are available with environment variables. See [config.go](https://github.com/DataDog/datadog-agent/blob/main/pkg/config/setup/config.go) in the Datadog Agent GitHub repo. Options with environment variables start with `config.BindEnv*`.

- Component-specific environment variables not listed in [config.go](https://github.com/DataDog/datadog-agent/blob/main/pkg/config/setup/config.go) may also be supported.

  - **APM Trace Agent**

    - [Docker APM Agent Environment Variables](https://docs.datadoghq.com/agent/docker/apm/#docker-apm-agent-environment-variables)

    - [trace-agent config/apm.go](https://github.com/DataDog/datadog-agent/blob/main/pkg/config/setup/apm.go)

    - example

      ```yaml
         apm_config:
             enabled: true
             env: dev
         # DD_APM_ENABLED=true
         # DD_APM_ENV=dev
      ```

  - **Live Process Agent**

    - [process-agent config/process.go](https://github.com/DataDog/datadog-agent/blob/main/pkg/config/setup/process.go)

    - example

      ```yaml
         process_config:
             process_collection:
                 enabled: true
             process_dd_url: https://process.datadoghq.com
         # DD_PROCESS_AGENT_PROCESS_COLLECTION_ENABLED=true
         # DD_PROCESS_AGENT_URL=https://process.datadoghq.com
      ```

## Using environment variables in systemd units{% #using-environment-variables-in-systemd-units %}

In operating systems that uses systemd to manage services, environment variablesâglobal (for example, `/etc/environment`) or session-based (for example, `export VAR=value`)âare not generally made available to services unless configured to do so. See [systemd Exec manual page](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#Environment) for more details.

From Datadog Agent 7.45, the Datadog Agent service (`datadog-agent.service` unit) can optionally load environment variables assignments from a file (`<ETC_DIR>/environment`).

1. Create `/etc/datadog-agent/environment` if it does not exist.
1. Define newline-separated environment variable assignments. Example:

```
GODEBUG=x509ignoreCN=0,x509sha1=1
DD_HOSTNAME=myhost.local
DD_TAGS=env:dev service:foo
```
Restart the service for changes to take effect
## Further Reading{% #further-reading %}

- [Docker Agent environment variables](https://docs.datadoghq.com/agent/docker/#environment-variables)
- [APM Agent environment variables](https://docs.datadoghq.com/agent/docker/apm/#docker-apm-agent-environment-variables)
- [Container log collection](https://docs.datadoghq.com/logs/log_collection/#container-log-collection)
- [Proxy environment variables](https://docs.datadoghq.com/agent/configuration/proxy/#environment-variables)
