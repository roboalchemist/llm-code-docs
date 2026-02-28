# Source: https://docs.datadoghq.com/security/default_rules/def-000-6be.md

---
title: Uninstall rsh Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Uninstall rsh Package
---

# Uninstall rsh Package

## Description{% #description %}

The `rsh-client` package contains the client commands for the rsh services

## Rationale{% #rationale %}

These legacy clients contain numerous security exposures and have been replaced with the more secure SSH package. Even if the server is removed, it is best to ensure the clients are also removed to prevent users from inadvertently attempting to use these commands and therefore exposing their credentials. Note that removing the `rsh-client` package removes the clients for `rsh`,`rcp`, and `rlogin`.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove rsh-client
# from the system, and may remove any packages
# that depend on rsh-client. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "rsh-client"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Uninstall rsh Package: Ensure rsh-client is removed'
  ansible.builtin.package:
    name: rsh-client
    state: absent
  tags:
  - NIST-800-171-3.1.13
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.4
  - disable_strategy
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - package_rsh_removed
  - unknown_severity
```
