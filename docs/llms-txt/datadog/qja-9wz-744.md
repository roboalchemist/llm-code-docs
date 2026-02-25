# Source: https://docs.datadoghq.com/security/default_rules/qja-9wz-744.md

---
title: The container's health should be constantly monitored
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The container's health should be
  constantly monitored
---

# The container's health should be constantly monitored
Classification:complianceFramework:cis-dockerControl:5.26
## Description{% #description %}

If the container image does not have an HEALTHCHECK instruction defined, you should use the `--health-cmd` parameter at container runtime to check container health.

## Rationale{% #rationale %}

If the container image you are using does not have a pre-defined HEALTHCHECK instruction, use the `--health-cmd` parameter to check container health at runtime. Based on the reported health status, remedial actions can be taken if necessary.

## Audit{% #audit %}

Run this command and ensure that all containers are reporting their health status: `docker ps --quiet | xargs docker inspect --format '{{ .Id }}: Health={{ .State.Health.Status }}'`

## Remediation{% #remediation %}

You should run the container using the `--health-cmd` parameter. For example, `docker run -d --health-cmd='stat /etc/passwd || exit 1' nginx`

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, health checks are not carried out at container runtime.

## References{% #references %}

1. [https://docs.docker.com/engine/reference/run/#healthcheck](https://docs.docker.com/engine/reference/run/#healthcheck)

## CIS controls{% #cis-controls %}

Version 6

18 Application Software Security Application Software Security
