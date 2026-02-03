# Source: https://docs.datadoghq.com/security/default_rules/tpb-xvh-rnd.md

---
title: The file permissions on docker.socket should be set to 644 or stricter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The file permissions on docker.socket
  should be set to 644 or stricter
---

# The file permissions on docker.socket should be set to 644 or stricter
Classification:complianceFramework:cis-dockerControl:3.4 
## Description{% #description %}

You should verify that the file permissions on the docker.socket file are correctly set to 644 or more restrictively.

## Rationale{% #rationale %}

The docker.socket file contains sensitive parameters that may alter the behavior of the Docker remote API. It should therefore be writeable only by root in order to ensure that it is not modified by less privileged users.

## Audit{% #audit %}

1. Locate the `docker.socket` file by running:
   ```
   systemctl show -p FragmentPath docker.socket 
   ```
1. If the file does not exist, this recommendation is not applicable. If the file exists, verify that the file permissions are set to `644` or more restrictively, by running the following command with the correct filepath:
   ```
   stat -c %a /usr/lib/systemd/system/docker.socket
   ```

## Remediation{% #remediation %}

1. Find out the file location: `systemctl show -p FragmentPath docker.socket`
1. If the file does not exist, this recommendation is not applicable. If the file does exist, you should execute the command below, including the correct file path to set the file permissions to 644. For example, `chmod 644 /usr/lib/systemd/system/docker.socket`

## Impact{% #impact %}

None

## Default value{% #default-value %}

This file may not be present on the system and in that case, this recommendation is not applicable. By default, if the file is present, the permissions should be set to 644 or more restrictively.

## References{% #references %}

1. [https://docs.docker.com/engine/reference/commandline/dockerd/#bind-docker-to-another-hostport-or-a-unix-socket](https://docs.docker.com/engine/reference/commandline/dockerd/#bind-docker-to-another-hostport-or-a-unix-socket)
1. [https://github.com/YungSang/fedora-atomic-packer/blob/master/oem/docker.socket](https://github.com/YungSang/fedora-atomic-packer/blob/master/oem/docker.socket)
1. [http://daviddaeschler.com/2014/12/14/centos-7rhel-7-and-docker-containers-on-boot/](http://daviddaeschler.com/2014/12/14/centos-7rhel-7-and-docker-containers-on-boot/)

## CIS controls{% #cis-controls %}

Version 6

14.4 Protect Information With Access Control Lists - All information stored on systems shall be protected with file system, network share, claims, application, or database specific access control lists. These controls will enforce the principle that only authorized individuals should have access to the information based on their need to access the information as a part of their responsibilities.

Version 7

14.6 Protect Information through Access Control Lists - Protect all information stored on systems with file system, network share, claims, application, or database specific access control lists. These controls will enforce the principle that only authorized individuals should have access to the information based on their need to access the information as a part of their responsibilities.
