# Source: https://docs.datadoghq.com/security/default_rules/def-000-siy.md

---
title: Add nosuid Option to /dev/shm
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Add nosuid Option to /dev/shm
---

# Add nosuid Option to /dev/shm
 
## Description{% #description %}

The `nosuid` mount option can be used to prevent execution of setuid programs in `/dev/shm`. The SUID and SGID permissions should not be required in these world-writable directories. Add the `nosuid` option to the fourth column of `/etc/fstab` for the line which controls mounting of `/dev/shm`.

## Rationale{% #rationale %}

The presence of SUID and SGID executables should be tightly controlled. Users should not be able to execute SUID or SGID binaries from temporary storage partitions.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if ! ( [ -f /.dockerenv ] || [ -f /run/.containerenv ] ); then

function perform_remediation {
    


    mount_point_match_regexp="$(printf "^[[:space:]]*[^#].*[[:space:]]%s[[:space:]]" /dev/shm)"

    # If the mount point is not in /etc/fstab, get previous mount options from /etc/mtab
    if ! grep -q "$mount_point_match_regexp" /etc/fstab; then
        # runtime opts without some automatic kernel/userspace-added defaults
        previous_mount_opts=$(grep "$mount_point_match_regexp" /etc/mtab | head -1 |  awk '{print $4}' \
                    | sed -E "s/(rw|defaults|seclabel|nosuid)(,|$)//g;s/,$//")
        [ "$previous_mount_opts" ] && previous_mount_opts+=","
        # In iso9660 filesystems mtab could describe a "blocksize" value, this should be reflected in
        # fstab as "block".  The next variable is to satisfy shellcheck SC2050.
        fs_type="tmpfs"
        if [  "$fs_type" == "iso9660" ] ; then
            previous_mount_opts=$(sed 's/blocksize=/block=/' <<< "$previous_mount_opts")
        fi
        echo "tmpfs /dev/shm tmpfs defaults,${previous_mount_opts}nosuid 0 0" >> /etc/fstab
    # If the mount_opt option is not already in the mount point's /etc/fstab entry, add it
    elif ! grep "$mount_point_match_regexp" /etc/fstab | grep -q "nosuid"; then
        previous_mount_opts=$(grep "$mount_point_match_regexp" /etc/fstab | awk '{print $4}')
        sed -i "s|\(${mount_point_match_regexp}.*${previous_mount_opts}\)|\1,nosuid|" /etc/fstab
    fi


    if mkdir -p "/dev/shm"; then
        if mountpoint -q "/dev/shm"; then
            mount -o remount --target "/dev/shm"
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
- name: 'Add nosuid Option to /dev/shm: Check information associated to mountpoint'
  command: findmnt  '/dev/shm'
  register: device_name
  failed_when: device_name.rc > 1
  changed_when: false
  when: not ( ansible_virtualization_type in ["docker", "lxc", "openvz", "podman",
    "container"] )
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
  - mount_option_dev_shm_nosuid
  - no_reboot_needed

- name: 'Add nosuid Option to /dev/shm: Create mount_info dictionary variable'
  set_fact:
    mount_info: '{{ mount_info|default({})|combine({item.0: item.1}) }}'
  with_together:
  - '{{ device_name.stdout_lines[0].split() | list | lower }}'
  - '{{ device_name.stdout_lines[1].split() | list }}'
  when:
  - not ( ansible_virtualization_type in ["docker", "lxc", "openvz", "podman", "container"]
    )
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
  - mount_option_dev_shm_nosuid
  - no_reboot_needed

- name: 'Add nosuid Option to /dev/shm: If /dev/shm not mounted, craft mount_info
    manually'
  set_fact:
    mount_info: '{{ mount_info|default({})|combine({item.0: item.1}) }}'
  with_together:
  - - target
    - source
    - fstype
    - options
  - - /dev/shm
    - tmpfs
    - tmpfs
    - defaults
  when:
  - not ( ansible_virtualization_type in ["docker", "lxc", "openvz", "podman", "container"]
    )
  - ("" | length == 0)
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
  - mount_option_dev_shm_nosuid
  - no_reboot_needed

- name: 'Add nosuid Option to /dev/shm: Make sure nosuid option is part of the to
    /dev/shm options'
  set_fact:
    mount_info: '{{ mount_info | combine( {''options'':''''~mount_info.options~'',nosuid''
      }) }}'
  when:
  - not ( ansible_virtualization_type in ["docker", "lxc", "openvz", "podman", "container"]
    )
  - mount_info is defined and "nosuid" not in mount_info.options
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
  - mount_option_dev_shm_nosuid
  - no_reboot_needed

- name: 'Add nosuid Option to /dev/shm: Ensure /dev/shm is mounted with nosuid option'
  mount:
    path: /dev/shm
    src: '{{ mount_info.source }}'
    opts: '{{ mount_info.options }}'
    state: mounted
    fstype: '{{ mount_info.fstype }}'
  when:
  - not ( ansible_virtualization_type in ["docker", "lxc", "openvz", "podman", "container"]
    )
  - mount_info is defined
  - (device_name.stdout is defined and (device_name.stdout | length > 0)) or ("" |
    length == 0)
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
  - mount_option_dev_shm_nosuid
  - no_reboot_needed
```
