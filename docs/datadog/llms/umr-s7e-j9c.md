# Source: https://docs.datadoghq.com/security/default_rules/umr-s7e-j9c.md

---
title: >-
  The container should restrict acquiring additional privileges via suid or sgid
  bits
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The container should restrict acquiring
  additional privileges via suid or sgid bits
---

# The container should restrict acquiring additional privileges via suid or sgid bits
Classification:complianceFramework:cis-dockerControl:5.25
## Description{% #description %}

You should restrict the container from acquiring additional privileges via SUID or SGID bits.

## Rationale{% #rationale %}

A process can set the `no_new_priv` bit in the kernel and this persists across forks, clones and execve. The `no_new_priv` bit ensures that the process and its child processes do not gain any additional privileges via SUID or SGID bits. This reduces the danger associated with many operations because the possibility of subverting privileged binaries is lessened.

## Audit{% #audit %}

Run this command: `docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: SecurityOpt={{ .HostConfig.SecurityOpt }}'`

This command returns all of the security options currently configured for containers. The option `no-new-privileges` should be one of them.

## Remediation{% #remediation %}

Start your container with the options `docker run --rm -it --security-opt=no-new-privileges ubuntu bash`

## Impact{% #impact %}

The `no_new_priv` option prevents LSMs like SELinux from allowing processes to acquire new privileges.

## Default value{% #default-value %}

By default, new privileges are not restricted.

## References{% #references %}

1. [https://github.com/projectatomic/atomic-site/issues/269](https://github.com/projectatomic/atomic-site/issues/269)
1. [https://github.com/docker/docker/pull/20727](https://github.com/docker/docker/pull/20727)
1. [https://www.kernel.org/doc/Documentation/prctl/no_new_privs.txt](https://www.kernel.org/doc/Documentation/prctl/no_new_privs.txt)
1. [https://lwn.net/Articles/475678/](https://lwn.net/Articles/475678/)
1. [https://lwn.net/Articles/475362/](https://lwn.net/Articles/475362/)

## CIS controls{% #cis-controls %}

Version 6

5 Controlled Use of Administration Privileges Controlled Use of Administration Privileges
