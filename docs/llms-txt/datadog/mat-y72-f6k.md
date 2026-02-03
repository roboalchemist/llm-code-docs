# Source: https://docs.datadoghq.com/security/default_rules/mat-y72-f6k.md

---
title: Sensitive host system directories should not be mounted on containers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Sensitive host system directories
  should not be mounted on containers
---

# Sensitive host system directories should not be mounted on containers
Classification:complianceFramework:cis-dockerControl:5.5 
## Description{% #description %}

You should not allow sensitive host system directories such as those listed below to be mounted as container volumes, especially in read-write mode. `/` `/boot` `/dev` `/etc` `/lib` `/proc` `/sys` `/usr`

## Rationale{% #rationale %}

If sensitive directories are mounted in read-write mode, it is possible to make changes to files within them. This has obvious security implications and should be avoided.

## Audit{% #audit %}

Run this command: `docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: Volumes={{ .Mounts }}'` This command returns a list of currently mapped directories and indicates whether they are mounted in read-write mode for each container instance.

## Remediation{% #remediation %}

Do not mount directories which are security sensitive on the host within containers, especially in read-write mode.

## Impact{% #impact %}

None

## Default value{% #default-value %}

Docker defaults to using a read-write volume but you can also mount a directory read-only. By default, no sensitive host directories are mounted within containers.

## References{% #references %}

1. [https://docs.docker.com/engine/tutorials/dockervolumes/](https://docs.docker.com/engine/tutorials/dockervolumes/)

## CIS controls{% #cis-controls %}

Version 6

14 Controlled Access Based on the Need to Know Controlled Access Based on the Need to Know
