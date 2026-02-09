# Source: https://docs.datadoghq.com/security/default_rules/j9z-sms-f3m.md

---
title: Containers should not mount the Docker socket docker.sock inside them
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Containers should not mount the Docker
  socket docker.sock inside them
---

# Containers should not mount the Docker socket docker.sock inside them
Classification:complianceFramework:cis-dockerControl:5.31 
## Description{% #description %}

The Docker socket docker.sock should not be mounted inside a container.

## Rationale{% #rationale %}

If the Docker socket is mounted inside a container it could allow processes running within the container to execute Docker commands which would effectively allow for full control of the host.

## Audit{% #audit %}

Run this command: `docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: Volumes={{ .Mounts }}' | grep docker.sock` This returns any instances where `docker.sock` has been mapped to a container as a volume.

## Remediation{% #remediation %}

You should ensure that no containers mount docker.sock as a volume.

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, docker.sock is not mounted inside containers.

## References{% #references %}

1. [https://raesene.github.io/blog/2016/03/06/The-Dangers-Of-Docker.sock/](https://raesene.github.io/blog/2016/03/06/The-Dangers-Of-Docker.sock/)
1. [https://forums.docker.com/t/docker-in-docker-vs-mounting-var-run-docker-sock/9450/2](https://forums.docker.com/t/docker-in-docker-vs-mounting-var-run-docker-sock/9450/2)
1. [https://github.com/docker/docker/issues/21109](https://github.com/docker/docker/issues/21109)

## CIS controls{% #cis-controls %}

Version 6

9 Limitation and Control of Network Ports, Protocols, and Services
