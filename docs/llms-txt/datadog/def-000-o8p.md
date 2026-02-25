# Source: https://docs.datadoghq.com/security/default_rules/def-000-o8p.md

---
title: Ensure All Files Are Owned by a Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Ensure All Files Are Owned by a Group
---

# Ensure All Files Are Owned by a Group

## Description{% #description %}

If any file is not group-owned by a valid defined group, the cause of the lack of group-ownership must be investigated. Following this, those files should be deleted or assigned to an appropriate group. The groups need to be defined in `/etc/group` or in `/usr/lib/group` if `nss-altfiles` are configured to be used in `/etc/nsswitch.conf`. Locate the mount points related to local devices by the following command:

```
$ findmnt -n -l -k -it $(awk '/nodev/ { print $2 }' /proc/filesystems | paste -sd,)
```

For all mount points listed by the previous command, it is necessary to search for files which do not belong to a valid group using the following command:

```
$ sudo find MOUNTPOINT -xdev -nogroup 2>/dev/null
```

## Rationale{% #rationale %}

Unowned files do not directly imply a security problem, but they are generally a sign that something is amiss. They may be caused by an intruder, by incorrect software installation or draft software removal, or by failure to remove all files belonging to a deleted account, or other similar cases. The files should be repaired so they will not cause problems when accounts are created in the future, and the cause should be discovered and addressed.

## Warning{% #warning %}

This rule only considers local groups as valid groups. If you have your groups defined outside `/etc/group` or `/usr/lib/group`, the rule won't consider those.
