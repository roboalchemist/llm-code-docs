# Source: https://docs.datadoghq.com/security/default_rules/def-000-jsc.md

---
title: Ensure Users Cannot Change GNOME3 Screensaver Settings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure Users Cannot Change GNOME3
  Screensaver Settings
---

# Ensure Users Cannot Change GNOME3 Screensaver Settings
 
## Description{% #description %}

If not already configured, ensure that users cannot change GNOME3 screensaver lock settings by adding `/org/gnome/desktop/screensaver/lock-delay` to `/etc/dconf/db/local.d/locks/00-security-settings-lock` to prevent user modification. For example:

```
/org/gnome/desktop/screensaver/lock-delay
```

After the settings have been set, run `dconf update`.

## Rationale{% #rationale %}

A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not logout because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, GNOME desktops can be configured to identify when a user's session has idled and take action to initiate the session lock. As such, users should not be allowed to change session settings.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if rpm --quiet -q gdm && { [ ! -f /.dockerenv ] && [ ! -f /run/.containerenv ]; }; then

# Check for setting in any of the DConf db directories
LOCKFILES=$(grep -r "^/org/gnome/desktop/screensaver/lock-delay$" "/etc/dconf/db/" \
            | grep -v 'distro\|ibus\|local.d' | grep ":" | cut -d":" -f1)
LOCKSFOLDER="/etc/dconf/db/local.d/locks"

mkdir -p "${LOCKSFOLDER}"

# Comment out the configurations in databases different from the target one
if [[ ! -z "${LOCKFILES}" ]]
then
    sed -i -E "s|^/org/gnome/desktop/screensaver/lock-delay$|#&|" "${LOCKFILES[@]}"
fi

if ! grep -qr "^/org/gnome/desktop/screensaver/lock-delay$" /etc/dconf/db/local.d/
then
    echo "/org/gnome/desktop/screensaver/lock-delay" >> "/etc/dconf/db/local.d/locks/00-security-settings-lock"
fi

dconf update

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
  - CCE-80371-8
  - DISA-STIG-RHEL-07-010081
  - NIST-800-171-3.1.10
  - NIST-800-53-CM-6(a)
  - dconf_gnome_screensaver_user_locks
  - low_complexity
  - medium_disruption
  - medium_severity
  - no_reboot_needed
  - unknown_strategy

- name: Prevent user modification of GNOME lock-delay
  lineinfile:
    path: /etc/dconf/db/local.d/locks/00-security-settings-lock
    regexp: ^/org/gnome/desktop/screensaver/lock-delay$
    line: /org/gnome/desktop/screensaver/lock-delay
    create: true
  when:
  - '"gdm" in ansible_facts.packages'
  - ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  tags:
  - CCE-80371-8
  - DISA-STIG-RHEL-07-010081
  - NIST-800-171-3.1.10
  - NIST-800-53-CM-6(a)
  - dconf_gnome_screensaver_user_locks
  - low_complexity
  - medium_disruption
  - medium_severity
  - no_reboot_needed
  - unknown_strategy

- name: Dconf Update
  command: dconf update
  when:
  - '"gdm" in ansible_facts.packages'
  - ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  tags:
  - CCE-80371-8
  - DISA-STIG-RHEL-07-010081
  - NIST-800-171-3.1.10
  - NIST-800-53-CM-6(a)
  - dconf_gnome_screensaver_user_locks
  - low_complexity
  - medium_disruption
  - medium_severity
  - no_reboot_needed
  - unknown_strategy
```
