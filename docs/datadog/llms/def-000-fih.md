# Source: https://docs.datadoghq.com/security/default_rules/def-000-fih.md

---
title: Ensure All Files Are Owned by a User
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Ensure All Files Are Owned by a User
---

# Ensure All Files Are Owned by a User

## Description{% #description %}

If any files are not owned by a user, then the cause of their lack of ownership should be investigated. Following this, the files should be deleted or assigned to an appropriate user. Locate the mount points related to local devices by the following command:

```
$ findmnt -n -l -k -it $(awk '/nodev/ { print $2 }' /proc/filesystems | paste -sd,)
```

For all mount points listed by the previous command, it is necessary to search for files which do not belong to a valid user using the following command:

```
$ sudo find MOUNTPOINT -xdev -nouser 2>/dev/null
```

## Rationale{% #rationale %}

Unowned files do not directly imply a security problem, but they are generally a sign that something is amiss. They may be caused by an intruder, by incorrect software installation or draft software removal, or by failure to remove all files belonging to a deleted account, or other similar cases. The files should be repaired so they will not cause problems when accounts are created in the future, and the cause should be discovered and addressed.

## Warning{% #warning %}

For this rule to evaluate centralized user accounts, `getent` must be working properly so that running the command

```
getent passwd
```

returns a list of all users in your organization. If using the System Security Services Daemon (SSSD),

```gdscript3
enumerate = true
```

must be configured in your organization's domain to return a complete list of users
