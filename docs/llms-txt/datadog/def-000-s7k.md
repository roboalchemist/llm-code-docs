# Source: https://docs.datadoghq.com/security/default_rules/def-000-s7k.md

---
title: Add noexec Option to /var/log/audit
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Add noexec Option to /var/log/audit
---

# Add noexec Option to /var/log/audit
 
## Description{% #description %}

The `noexec` mount option can be used to prevent binaries from being executed out of `/var/log/audit`. Add the `noexec` option to the fourth column of `/etc/fstab` for the line which controls mounting of `/var/log/audit`.

## Rationale{% #rationale %}

Allowing users to execute binaries from directories containing audit log files such as `/var/log/audit` should never be necessary in normal operation and can expose the system to potential compromise.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if ! ( [ -f /.dockerenv ] || [ -f /run/.containerenv ] ) && { findmnt --kernel "/var/log/audit" > /dev/null || findmnt --fstab "/var/log/audit" > /dev/null; }; then

function perform_remediation {
    
        # the mount point /var/log/audit has to be defined in /etc/fstab
        # before this remediation can be executed. In case it is not defined, the
        # remediation aborts and no changes regarding the mount point are done.
        mount_point_match_regexp="$(printf "^[[:space:]]*[^#].*[[:space:]]%s[[:space:]]" "/var/log/audit")"

    grep "$mount_point_match_regexp" -q /etc/fstab \
        || { echo "The mount point '/var/log/audit' is not even in /etc/fstab, so we can't set up mount options" >&2;
                echo "Not remediating, because there is no record of /var/log/audit in /etc/fstab" >&2; return 1; }
    


    mount_point_match_regexp="$(printf "^[[:space:]]*[^#].*[[:space:]]%s[[:space:]]" /var/log/audit)"

    # If the mount point is not in /etc/fstab, get previous mount options from /etc/mtab
    if ! grep -q "$mount_point_match_regexp" /etc/fstab; then
        # runtime opts without some automatic kernel/userspace-added defaults
        previous_mount_opts=$(grep "$mount_point_match_regexp" /etc/mtab | head -1 |  awk '{print $4}' \
                    | sed -E "s/(rw|defaults|seclabel|noexec)(,|$)//g;s/,$//")
        [ "$previous_mount_opts" ] && previous_mount_opts+=","
        # In iso9660 filesystems mtab could describe a "blocksize" value, this should be reflected in
        # fstab as "block".  The next variable is to satisfy shellcheck SC2050.
        fs_type=""
        if [  "$fs_type" == "iso9660" ] ; then
            previous_mount_opts=$(sed 's/blocksize=/block=/' <<< "$previous_mount_opts")
        fi
        echo " /var/log/audit  defaults,${previous_mount_opts}noexec 0 0" >> /etc/fstab
    # If the mount_opt option is not already in the mount point's /etc/fstab entry, add it
    elif ! grep "$mount_point_match_regexp" /etc/fstab | grep -q "noexec"; then
        previous_mount_opts=$(grep "$mount_point_match_regexp" /etc/fstab | awk '{print $4}')
        sed -i "s|\(${mount_point_match_regexp}.*${previous_mount_opts}\)|\1,noexec|" /etc/fstab
    fi


    if mkdir -p "/var/log/audit"; then
        if mountpoint -q "/var/log/audit"; then
            mount -o remount --target "/var/log/audit"
        fi
    fi
}

perform_remediation

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: 'Add noexec Option to /var/log/audit: Check information associated to mountpoint'
  command: findmnt --fstab '/var/log/audit'
  register: device_name
  failed_when: device_name.rc > 1
  changed_when: false
  when:
  - not ( ansible_virtualization_type in ["docker", "lxc", "openvz", "podman", "container"]
    )
  - '"/var/log/audit" in ansible_mounts | map(attribute="mount") | list'
  tags:
  - NIST-800-53-AC-6
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-MP-7
  - configure_strategy
  - high_disruption
  - low_complexity
  - medium_severity
  - mount_option_var_log_audit_noexec
  - no_reboot_needed

- name: 'Add noexec Option to /var/log/audit: Create mount_info dictionary variable'
  set_fact:
    mount_info: '{{ mount_info|default({})|combine({item.0: item.1}) }}'
  with_together:
  - '{{ device_name.stdout_lines[0].split() | list | lower }}'
  - '{{ device_name.stdout_lines[1].split() | list }}'
  when:
  - not ( ansible_virtualization_type in ["docker", "lxc", "openvz", "podman", "container"]
    )
  - '"/var/log/audit" in ansible_mounts | map(attribute="mount") | list'
  - device_name.stdout is defined and device_name.stdout_lines is defined
  - (device_name.stdout | length > 0)
  tags:
  - NIST-800-53-AC-6
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-MP-7
  - configure_strategy
  - high_disruption
  - low_complexity
  - medium_severity
  - mount_option_var_log_audit_noexec
  - no_reboot_needed

- name: 'Add noexec Option to /var/log/audit: If /var/log/audit not mounted, craft
    mount_info manually'
  set_fact:
    mount_info: '{{ mount_info|default({})|combine({item.0: item.1}) }}'
  with_together:
  - - target
    - source
    - fstype
    - options
  - - /var/log/audit
    - ''
    - ''
    - defaults
  when:
  - not ( ansible_virtualization_type in ["docker", "lxc", "openvz", "podman", "container"]
    )
  - '"/var/log/audit" in ansible_mounts | map(attribute="mount") | list'
  - ("--fstab" | length == 0)
  - device_name.stdout is defined and device_name.stdout_lines is defined
  - (device_name.stdout | length == 0)
  tags:
  - NIST-800-53-AC-6
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-MP-7
  - configure_strategy
  - high_disruption
  - low_complexity
  - medium_severity
  - mount_option_var_log_audit_noexec
  - no_reboot_needed

- name: 'Add noexec Option to /var/log/audit: Make sure noexec option is part of the
    to /var/log/audit options'
  set_fact:
    mount_info: '{{ mount_info | combine( {''options'':''''~mount_info.options~'',noexec''
      }) }}'
  when:
  - not ( ansible_virtualization_type in ["docker", "lxc", "openvz", "podman", "container"]
    )
  - '"/var/log/audit" in ansible_mounts | map(attribute="mount") | list'
  - mount_info is defined and "noexec" not in mount_info.options
  tags:
  - NIST-800-53-AC-6
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-MP-7
  - configure_strategy
  - high_disruption
  - low_complexity
  - medium_severity
  - mount_option_var_log_audit_noexec
  - no_reboot_needed

- name: 'Add noexec Option to /var/log/audit: Ensure /var/log/audit is mounted with
    noexec option'
  mount:
    path: /var/log/audit
    src: '{{ mount_info.source }}'
    opts: '{{ mount_info.options }}'
    state: mounted
    fstype: '{{ mount_info.fstype }}'
  when:
  - not ( ansible_virtualization_type in ["docker", "lxc", "openvz", "podman", "container"]
    )
  - '"/var/log/audit" in ansible_mounts | map(attribute="mount") | list'
  - mount_info is defined
  - (device_name.stdout is defined and (device_name.stdout | length > 0)) or ("--fstab"
    | length == 0)
  tags:
  - NIST-800-53-AC-6
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-MP-7
  - configure_strategy
  - high_disruption
  - low_complexity
  - medium_severity
  - mount_option_var_log_audit_noexec
  - no_reboot_needed
```
