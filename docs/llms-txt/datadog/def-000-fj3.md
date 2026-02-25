# Source: https://docs.datadoghq.com/security/default_rules/def-000-fj3.md

---
title: Uninstall dnsmasq Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Uninstall dnsmasq Package
---

# Uninstall dnsmasq Package

## Description{% #description %}

dnsmasq is a lightweight tool that provides DNS caching, DNS forwarding and DHCP (Dynamic Host Configuration Protocol) services.

The `dnsmasq` package can be removed with the following command:

```

$ apt-get remove dnsmasq
```

## Rationale{% #rationale %}

Unless a system is specifically designated to act as a DNS caching, DNS forwarding and/or DHCP server, it is recommended that the package be removed to reduce the potential attack surface.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove dnsmasq
# from the system, and may remove any packages
# that depend on dnsmasq. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "dnsmasq"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Uninstall dnsmasq Package: Ensure dnsmasq is removed'
  ansible.builtin.package:
    name: dnsmasq
    state: absent
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - low_severity
  - no_reboot_needed
  - package_dnsmasq_removed
```
