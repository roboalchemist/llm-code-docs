# Source: https://docs.datadoghq.com/security/default_rules/2vc-udv-9at.md

---
title: The Docker socket file should have permissions of 660 or stricter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Docker socket file should have
  permissions of 660 or stricter
---

# The Docker socket file should have permissions of 660 or stricter
Classification:complianceFramework:cis-dockerControl:3.16 
## Description{% #description %}

You should verify that the Docker socket file has permissions of 660 or are configured more restrictively.

## Rationale{% #rationale %}

Only root and the members of the docker group should be allowed to read and write to the default Docker Unix socket. The Docker socket file should therefore have permissions of 660 or more restrictive permissions.

## Audit{% #audit %}

Verify that the Docker socket file has permissions of `660` or more restrictive, by running:

```gdscript3
stat -c %a /var/run/docker.sock
```

## Remediation{% #remediation %}

Run the command `chmod 660 /var/run/docker.sock`

This sets the file permissions of the Docker socket file to 660.

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, the permissions for the Docker socket file is correctly set to 660.

## References{% #references %}

1. [https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-socket-option](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-socket-option)
1. [https://docs.docker.com/engine/reference/commandline/dockerd/#bind-docker-to-another-hostport-or-a-unix-socket](https://docs.docker.com/engine/reference/commandline/dockerd/#bind-docker-to-another-hostport-or-a-unix-socket)

## CIS controls{% #cis-controls %}

Version 6

14.4 Protect Information With Access Control Lists - All information stored on systems shall be protected with file system, network share, claims, application, or database specific access control lists. These controls will enforce the principle that only authorized individuals should have access to the information based on their need to access the information as a part of their responsibilities.

Version 7

14.6 Protect Information through Access Control Lists Protect all information stored on systems with file system, network share, claims, application, or database specific access control lists. These controls will enforce the principle that only authorized individuals should have access to the information based on their need to access the information as a part of their responsibilities.
