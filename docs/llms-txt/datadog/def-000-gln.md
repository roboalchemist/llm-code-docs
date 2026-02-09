# Source: https://docs.datadoghq.com/security/default_rules/def-000-gln.md

---
title: Disable the Automounter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable the Automounter
---

# Disable the Automounter
 
## Description{% #description %}

The `autofs` daemon mounts and unmounts filesystems, such as user home directories shared via NFS, on demand. In addition, autofs can be used to handle removable media, and the default configuration provides the cdrom device as `/misc/cd`. However, this method of providing access to removable media is not common, so autofs can almost always be disabled if NFS is not in use. Even if NFS is required, it may be possible to configure filesystem mounts statically by editing `/etc/fstab` rather than relying on the automounter.

The `autofs` service can be disabled with the following command:

```
$ sudo systemctl mask --now autofs.service
```

## Rationale{% #rationale %}

Disabling the automounter permits the administrator to statically control filesystem mounting through `/etc/fstab`.

Additionally, automatically mounting filesystems permits easy introduction of unknown devices, thereby facilitating malicious activity.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if ( dpkg-query --show --showformat='${db:Status-Status}' 'autofs' 2>/dev/null | grep -q '^installed$' && dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$' ); then

SYSTEMCTL_EXEC='/usr/bin/systemctl'
if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
  "$SYSTEMCTL_EXEC" stop 'autofs.service'
fi
"$SYSTEMCTL_EXEC" disable 'autofs.service'
"$SYSTEMCTL_EXEC" mask 'autofs.service'
# Disable socket activation if we have a unit file for it
if "$SYSTEMCTL_EXEC" -q list-unit-files autofs.socket; then
    if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
      "$SYSTEMCTL_EXEC" stop 'autofs.socket'
    fi
    "$SYSTEMCTL_EXEC" mask 'autofs.socket'
fi
# The service may not be running because it has been started and failed,
# so let's reset the state so OVAL checks pass.
# Service should be 'inactive', not 'failed' after reboot though.
"$SYSTEMCTL_EXEC" reset-failed 'autofs.service' || true

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
  - NIST-800-171-3.4.6
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-MP-7
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_autofs_disabled

- name: Disable the Automounter - Collect systemd Services Present in the System
  ansible.builtin.command: systemctl -q list-unit-files --type service
  register: service_exists
  changed_when: false
  failed_when: service_exists.rc not in [0, 1]
  check_mode: false
  when: ( "autofs" in ansible_facts.packages and "linux-base" in ansible_facts.packages
    )
  tags:
  - NIST-800-171-3.4.6
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-MP-7
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_autofs_disabled

- name: Disable the Automounter - Ensure autofs.service is Masked
  ansible.builtin.systemd:
    name: autofs.service
    state: stopped
    enabled: false
    masked: true
  when:
  - ( "autofs" in ansible_facts.packages and "linux-base" in ansible_facts.packages
    )
  - service_exists.stdout_lines is search("autofs.service", multiline=True)
  tags:
  - NIST-800-171-3.4.6
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-MP-7
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_autofs_disabled

- name: Unit Socket Exists - autofs.socket
  ansible.builtin.command: systemctl -q list-unit-files autofs.socket
  register: socket_file_exists
  changed_when: false
  failed_when: socket_file_exists.rc not in [0, 1]
  check_mode: false
  when: ( "autofs" in ansible_facts.packages and "linux-base" in ansible_facts.packages
    )
  tags:
  - NIST-800-171-3.4.6
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-MP-7
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_autofs_disabled

- name: Disable the Automounter - Disable Socket autofs
  ansible.builtin.systemd:
    name: autofs.socket
    enabled: false
    state: stopped
    masked: true
  when:
  - ( "autofs" in ansible_facts.packages and "linux-base" in ansible_facts.packages
    )
  - socket_file_exists.stdout_lines is search("autofs.socket", multiline=True)
  tags:
  - NIST-800-171-3.4.6
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-MP-7
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_autofs_disabled
```
