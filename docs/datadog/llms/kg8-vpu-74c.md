# Source: https://docs.datadoghq.com/security/default_rules/kg8-vpu-74c.md

---
title: Container images should include HEALTHCHECK instructions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Container images should include
  HEALTHCHECK instructions
---

# Container images should include HEALTHCHECK instructions
Classification:complianceFramework:cis-dockerControl:4.6
## Description{% #description %}

You should add the `HEALTHCHECK` instruction to your Docker container images in order to ensure that health checks are executed against running containers.

## Rationale{% #rationale %}

An important security control is that of availability. Adding the `HEALTHCHECK` instruction to your container image ensures that the Docker engine periodically checks the running container instances against that instruction to ensure that containers are still operational. Based on the results of the health check, the Docker engine could terminate containers which are not responding correctly, and instantiate new ones.

## Audit{% #audit %}

Run this command to ensure that Docker images have the appropriate `HEALTHCHECK` instruction configured: `docker inspect --format='{{ .Config.Healthcheck }}' <IMAGE>`

## Remediation{% #remediation %}

You should follow the Docker documentation and rebuild your container images to include the `HEALTHCHECK` instruction.

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, `HEALTHCHECK` is not set.

## References{% #references %}

1. [https://docs.docker.com/engine/reference/builder/#healthcheck](https://docs.docker.com/engine/reference/builder/#healthcheck)

## CIS controls{% #cis-controls %}

Version 6

18 Application Software Security Application Software Security
