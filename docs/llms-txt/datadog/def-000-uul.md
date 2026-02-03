# Source: https://docs.datadoghq.com/security/default_rules/def-000-uul.md

---
title: Ensure gpgcheck Enabled for All yum Package Repositories
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure gpgcheck Enabled for All yum
  Package Repositories
---

# Ensure gpgcheck Enabled for All yum Package Repositories
 
## Description{% #description %}

To ensure signature checking is not disabled for any repos, remove any lines from files in `/etc/yum.repos.d` of the form:

```
gpgcheck=0
```

## Rationale{% #rationale %}

Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This ensures the software has not been tampered with and that it has been provided by a trusted vendor. Self-signed certificates are disallowed by this requirement. Certificates used to verify the software must be from an approved Certificate Authority (CA)."

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

sed -i 's/gpgcheck\s*=.*/gpgcheck=1/g' /etc/yum.repos.d/*
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: Grep for yum repo section names
  shell: |
    set -o pipefail
    grep -HEr '^\[.+\]' -r /etc/yum.repos.d/
  register: repo_grep_results
  failed_when: repo_grep_results.rc not in [0, 1]
  changed_when: false
  tags:
  - CCE-26876-3
  - CJIS-5.10.4.1
  - NIST-800-171-3.4.8
  - NIST-800-53-CM-11(a)
  - NIST-800-53-CM-11(b)
  - NIST-800-53-CM-5(3)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-SA-12
  - NIST-800-53-SA-12(10)
  - NIST-800-53-SC-12
  - NIST-800-53-SC-12(3)
  - NIST-800-53-SI-7
  - PCI-DSS-Req-6.2
  - PCI-DSSv4-6.3.3
  - enable_strategy
  - ensure_gpgcheck_never_disabled
  - high_severity
  - low_complexity
  - medium_disruption
  - no_reboot_needed

- name: Set gpgcheck=1 for each yum repo
  ini_file:
    path: '{{ item[0] }}'
    section: '{{ item[1] }}'
    option: gpgcheck
    value: '1'
    no_extra_spaces: true
  loop: '{{ repo_grep_results.stdout |regex_findall( ''(.+\.repo):\[(.+)\]\n?'' )
    if repo_grep_results is not skipped else [] }}'
  when: repo_grep_results is not skipped
  tags:
  - CCE-26876-3
  - CJIS-5.10.4.1
  - NIST-800-171-3.4.8
  - NIST-800-53-CM-11(a)
  - NIST-800-53-CM-11(b)
  - NIST-800-53-CM-5(3)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-SA-12
  - NIST-800-53-SA-12(10)
  - NIST-800-53-SC-12
  - NIST-800-53-SC-12(3)
  - NIST-800-53-SI-7
  - PCI-DSS-Req-6.2
  - PCI-DSSv4-6.3.3
  - enable_strategy
  - ensure_gpgcheck_never_disabled
  - high_severity
  - low_complexity
  - medium_disruption
  - no_reboot_needed
```
