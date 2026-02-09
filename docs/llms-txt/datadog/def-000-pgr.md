# Source: https://docs.datadoghq.com/security/default_rules/def-000-pgr.md

---
title: Verify permissions of log files
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify permissions of log files
---

# Verify permissions of log files
 
## Description{% #description %}

Any operating system providing too much information in error messages risks compromising the data and security of the structure, and content of error messages needs to be carefully considered by the organization. Organizations carefully consider the structure/content of error messages. The extent to which information systems are able to identify and handle error conditions is guided by organizational policy and operational requirements. Information that could be exploited by adversaries includes, for example, erroneous logon attempts with passwords entered by mistake as the username, mission/business information that can be derived from (if not stated explicitly by) information recorded, and personal information, such as account numbers, social security numbers, and credit card numbers.

## Rationale{% #rationale %}

The Ubuntu 20.04 must generate error messages that provide information necessary for corrective actions without revealing information that could be exploited by adversaries.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

find  /var/log/  -perm /u+xs,g+xws,o+xwrt ! -name 'history.log*' ! -name 'eipp.log.xz*' ! -name '[bw]tmp' ! -name '[bw]tmp.*' ! -name '[bw]tmp-*' ! -name 'lastlog' ! -name 'lastlog.*' -type f -regextype posix-extended -regex '.*' -exec chmod u-xs,g-xws,o-xwrt {} \;
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Find /var/log/ file(s) recursively
  command: find  /var/log/  -perm /u+xs,g+xws,o+xwrt ! -name "history.log*" ! -name
    "eipp.log.xz*" ! -name "[bw]tmp" ! -name "[bw]tmp.*" ! -name "[bw]tmp-*" ! -name
    "lastlog" ! -name "lastlog.*" -type f -regextype posix-extended -regex ".*"
  register: files_found
  changed_when: false
  failed_when: false
  check_mode: false
  tags:
  - DISA-STIG-UBTU-20-010416
  - NIST-800-53-SI-11(a)
  - NIST-800-53-SI-11(b)
  - NIST-800-53-SI-11.1(iii)
  - PCI-DSSv4-10.3
  - PCI-DSSv4-10.3.1
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - permissions_local_var_log

- name: Set permissions for /var/log/ file(s)
  file:
    path: '{{ item }}'
    mode: u-xs,g-xws,o-xwrt
    state: file
  with_items:
  - '{{ files_found.stdout_lines }}'
  tags:
  - DISA-STIG-UBTU-20-010416
  - NIST-800-53-SI-11(a)
  - NIST-800-53-SI-11(b)
  - NIST-800-53-SI-11.1(iii)
  - PCI-DSSv4-10.3
  - PCI-DSSv4-10.3.1
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - permissions_local_var_log
```
