# Source: https://docs.datadoghq.com/security/default_rules/def-000-v8u.md

---
title: Ensure Only Users Logged In To Real tty Can Execute Sudo - sudo use_pty
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure Only Users Logged In To Real tty
  Can Execute Sudo - sudo use_pty
---

# Ensure Only Users Logged In To Real tty Can Execute Sudo - sudo use_pty

## Description{% #description %}

The sudo `use_pty` tag, when specified, will only execute sudo commands from users logged in to a real tty. This should be enabled by making sure that the `use_pty` tag exists in `/etc/sudoers` configuration file or any sudo configuration snippets in `/etc/sudoers.d/`.

## Rationale{% #rationale %}

Requiring that sudo commands be run in a pseudo-terminal can prevent an attacker from retaining access to the user's terminal after the main program has finished executing.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'sudo' 2>/dev/null | grep -q '^installed$'; then

if /usr/sbin/visudo -qcf /etc/sudoers; then
    cp /etc/sudoers /etc/sudoers.bak
    if ! grep -P '^[\s]*Defaults\b[^!\n]*\buse_pty.*$' /etc/sudoers; then
        # sudoers file doesn't define Option use_pty
        echo "Defaults use_pty" >> /etc/sudoers
    fi

    # Check validity of sudoers and cleanup bak
    if /usr/sbin/visudo -qcf /etc/sudoers; then
        rm -f /etc/sudoers.bak
    else
        echo "Fail to validate remediated /etc/sudoers, reverting to original file."
        mv /etc/sudoers.bak /etc/sudoers
        false
    fi
else
    echo "Skipping remediation, /etc/sudoers failed to validate"
    false
fi

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```go
- name: Gather the package facts
  package_facts:
    manager: auto
  tags:
  - PCI-DSS-Req-10.2.5
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sudo_add_use_pty

- name: Ensure use_pty is enabled in /etc/sudoers
  lineinfile:
    path: /etc/sudoers
    regexp: ^[\s]*Defaults.*\buse_pty\b.*$
    line: Defaults use_pty
    validate: /usr/sbin/visudo -cf %s
  when: '"sudo" in ansible_facts.packages'
  tags:
  - PCI-DSS-Req-10.2.5
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sudo_add_use_pty
```
