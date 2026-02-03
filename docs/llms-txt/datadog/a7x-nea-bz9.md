# Source: https://docs.datadoghq.com/security/default_rules/a7x-nea-bz9.md

---
title: The Docker daemon should be allowed to configure the firewall rules
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Docker daemon should be allowed to
  configure the firewall rules
---

# The Docker daemon should be allowed to configure the firewall rules
Classification:complianceFramework:cis-dockerControl:2.3 
## Description{% #description %}

The `iptables` firewall is used to set up, maintain, and inspect the tables of IP packet filter rules within the Linux kernel. The Docker daemon should be allowed to make changes to the `iptables` ruleset.

## Rationale{% #rationale %}

Docker will not make changes to your system `iptables` rules unless you allow it to do so. If you do allow this, Docker server will automatically make any required changes. You should let Docker make changes to `iptables` automatically in order to avoid networking misconfigurations that could affect the communication between containers and with the outside world. Additionally, this reduces the administrative overhead of updating `iptables` every time you add containers or modify networking options.

## Audit{% #audit %}

To confirm that the Docker daemon is allowed to change the `iptables` ruleset, review the `dockerd` startup options and the settings in `/etc/docker/daemon.json`. To review the `dockerd` startup options, run:

```
ps -ef | grep dockerd 
```

Ensure that the `--iptables` parameter is either not present or not set to `false`. Also review the `/etc/docker/daemon.json` file to check that the `iptables` setting is not set to `false`.

## Remediation{% #remediation %}

Do not run the Docker daemon with `--iptables=false` parameter.

## Impact{% #impact %}

The Docker daemon service requires `iptables` rules to be enabled before it starts. Any restarts of `iptables` during Docker daemon operation may result in losing Docker-created rules. Adding `iptables-persistent` to your `iptables` install can mitigate.

## Default value{% #default-value %}

By default, `iptables` is set to true.

## References{% #references %}

1. [https://docs.docker.com/engine/userguide/networking/default_network/container-communication/](https://docs.docker.com/engine/userguide/networking/default_network/container-communication/)
1. [https://fralef.me/docker-and-iptables.html](https://fralef.me/docker-and-iptables.html)

## CIS controls{% #cis-controls %}

Version 6.5 Controlled Use of Administration Privileges
