# Source: https://docs.datadoghq.com/security/default_rules/9hi-unv-yy9.md

---
title: The Docker daemon should only be controlled by root and Docker group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Docker daemon should only be
  controlled by root and Docker group
---

# The Docker daemon should only be controlled by root and Docker group
Classification:complianceFramework:cis-dockerControl:1.2.2
## Description{% #description %}

The Docker daemon requires access to the Docker socket which is, by default, owned by the user `root` and the group `docker`.

## Rationale{% #rationale %}

Docker allows you to share a directory between the Docker host and a guest container without limiting the access rights of the container. This means that you can start a container and map the `/` directory on your host to the container. The container is able to modify your host file system without any restrictions. This means that you could gain elevated privileges simply by being a member of the `docker` group and subsequently start a container which maps the root `/` directory on the host.

## Audit{% #audit %}

Run the following command on the Docker host to see the members of the `docker` group, and ensure that only trusted users are members:

```bash
getent group docker
```

## Remediation{% #remediation %}

You should remove any untrusted users from the `docker` group. Additionally, you should not create a mapping of sensitive directories from the host to container volumes.

## Impact{% #impact %}

Provided the preceding instructions are implemented, rights to build and execute containers as a normal user would be restricted.

## Default value{% #default-value %}

Not Applicable.

## References{% #references %}

1. [https://docs.docker.com/engine/security/security/#docker-daemon-attack-surface]
1. [https://www.andreas-jung.com/contents/on-docker-security-docker-group-considered-harmful]
1. [http://www.projectatomic.io/blog/2015/08/why-we-dont-let-non-root-users-run-docker-in-centos-fedora-or-rhel/]

## CIS controls{% #cis-controls %}

Version 6.5.1 Minimize And Sparingly Use Administrative Privileges - Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.
