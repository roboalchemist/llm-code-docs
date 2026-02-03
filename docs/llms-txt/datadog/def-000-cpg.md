# Source: https://docs.datadoghq.com/security/default_rules/def-000-cpg.md

---
title: Verify Permissions and Ownership of Old Passwords File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Permissions and Ownership of Old
  Passwords File
---

# Verify Permissions and Ownership of Old Passwords File
 
## Description{% #description %}

To properly set the owner of `/etc/security/opasswd`, run the command:

```
$ sudo chown root /etc/security/opasswd 
```

To properly set the group owner of `/etc/security/opasswd`, run the command:

```
$ sudo chgrp root /etc/security/opasswd
```

To properly set the permissions of `/etc/security/opasswd`, run the command:

```
$ sudo chmod 0600 /etc/security/opasswd
```

## Rationale{% #rationale %}

The `/etc/security/opasswd` file stores old passwords to prevent password reuse. Protection of this file is critical for system security.
