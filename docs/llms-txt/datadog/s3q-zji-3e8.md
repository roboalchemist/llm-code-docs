# Source: https://docs.datadoghq.com/security/default_rules/s3q-zji-3e8.md

---
title: The Docker daemon log level should be set to 'info'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Docker daemon log level should be
  set to 'info'
---

# The Docker daemon log level should be set to 'info'
Classification:complianceFramework:cis-dockerControl:2.2
## Description{% #description %}

Set Docker daemon log level to `info`.

## Rationale{% #rationale %}

Setting up an appropriate log level configures the Docker daemon to log events that you would want to review later. A base log level of `info` and above captures all logs except `debug` logs. Unless required, you should not run Docker daemon at `debug` log level.

## Audit{% #audit %}

To confirm that the log level setting is `info`, review both the `dockerd` startup options, and also the log level settings in `/etc/docker/daemon.json`. To review the `dockerd` startup options, run:

```
ps -ef | grep dockerd
```

Ensure that either the `--log-level` parameter is not present or if present, that it is set to `info`.

Similarly, review the `/etc/docker/daemon.json` for the `log-level` setting.

## Remediation{% #remediation %}

Ensure that the Docker daemon configuration file has the following configuration included:

```
"log-level": "info"
```

Alternatively, run the Docker daemon with the `log-level` specified:

```
dockerd --log-level="info"
```

## Impact{% #impact %}

None.

## Default value{% #default-value %}

By default, Docker daemon is set to log level of `info`.

## References{% #references %}

1. [https://docs.docker.com/edge/engine/reference/commandline/dockerd/](https://docs.docker.com/edge/engine/reference/commandline/dockerd/)

## CIS controls{% #cis-controls %}

Version 6.6.2 Ensure Audit Log Settings Support Appropriate Log Entry Formatting - Validate audit log settings for each hardware device and the software installed on it, ensuring that logs include a date, timestamp, source addresses, destination addresses, and various other useful elements of each packet and/or transaction. Systems should record logs in a standardized format such as syslog entries or those outlined by the Common Event Expression initiative. If systems cannot generate logs in a standardized format, log normalization tools can be deployed to convert logs into such a format.

Version 7.6.2 Activate audit logging - Ensure that local logging has been enabled on all systems and networking devices.

Version 6.3 Enable Detailed Logging - Enable system logging to include detailed information such as an event source, date, user, timestamp, source addresses, destination addresses, and other useful elements.
