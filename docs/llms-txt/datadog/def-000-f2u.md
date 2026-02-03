# Source: https://docs.datadoghq.com/security/default_rules/def-000-f2u.md

---
title: Install firewalld Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Install firewalld Package
---

# Install firewalld Package
 
## Description{% #description %}

The `firewalld` package can be installed with the following command:

```

$ sudo yum install firewalld
```

## Rationale{% #rationale %}

"Firewalld" provides an easy and effective way to block/limit remote access to the system via ports, services, and protocols. Remote access services, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Red Hat Enterprise Linux 7 functionality (e.g., SSH) must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets)."

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if [ ! -f /.dockerenv ] && [ ! -f /run/.containerenv ]; then

if ! rpm -q --quiet "firewalld" ; then
    yum install -y "firewalld"
fi

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: Ensure firewalld is installed
  package:
    name: firewalld
    state: present
  when: ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  tags:
  - CCE-82999-4
  - NIST-800-53-CM-6(a)
  - PCI-DSSv4-1.2.1
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_firewalld_installed
```
