# Source: https://docs.datadoghq.com/security/default_rules/ftc-kn6-yz8.md

---
title: The Docker socket file should be owned by root and Docker group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Docker socket file should be owned
  by root and Docker group
---

# The Docker socket file should be owned by root and Docker group
Classification:complianceFramework:cis-dockerControl:3.15 
## Description{% #description %}

You should verify that the Docker socket file is owned by root and group owned by docker.

## Rationale{% #rationale %}

The Docker daemon runs as root. The default Unix socket therefore must be owned by root. If any other user or process owns this socket, it might be possible for that non-privileged user or process to interact with the Docker daemon. Additionally, in this case a non-privileged user or process might be able to interact with containers which is neither a secure nor desired behavior. Additionally, the Docker installer creates a Unix group called docker. You can add users to this group, and in this case, those users would be able to read and write to the default Docker Unix socket. The membership of the docker group is tightly controlled by the system administrator. However, ff any other group owns this socket, then it might be possible for members of that group to interact with the Docker daemon. Such a group might not be as tightly controlled as the docker group. Again, this is not in line with good security practice. For these reason, the default Docker Unix socket file should be owned by root and group owned by docker to maintain the integrity of the socket file.

## Audit{% #audit %}

Verify that the Docker socket file is owned by root and group-owned by `docker` by running:

```gdscript3
stat -c %U:%G /var/run/docker.sock | grep -v root:docker
```

The command should return no results.

## Remediation{% #remediation %}

Run the following command: `chown root:docker /var/run/docker.sock`

This sets the ownership to root and group ownership to docker for the default Docker socket file.

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, the ownership and group ownership for the Docker socket file is correctly set to root:docker.

## References{% #references %}

1. [https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-socket-option](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-socket-option)
1. [https://docs.docker.com/engine/reference/commandline/dockerd/#bind-docker-to-another-hostport-or-a-unix-socket](https://docs.docker.com/engine/reference/commandline/dockerd/#bind-docker-to-another-hostport-or-a-unix-socket)

## CIS controls{% #cis-controls %}

Version 6

5.1 Minimize And Sparingly Use Administrative Privileges - Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.
