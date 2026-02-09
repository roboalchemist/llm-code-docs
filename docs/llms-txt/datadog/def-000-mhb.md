# Source: https://docs.datadoghq.com/security/default_rules/def-000-mhb.md

---
title: Remove Rsh Trust Files
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Remove Rsh Trust Files
---

# Remove Rsh Trust Files
 
## Description{% #description %}

The files `/etc/hosts.equiv` and `~/.rhosts` (in each user's home directory) list remote hosts and users that are trusted by the local system when using the rshd daemon. To remove these files, run the following command to delete them from any location:

```
$ sudo rm /etc/hosts.equiv
```

```
$ rm ~/.rhosts
```

## Rationale{% #rationale %}

This action is only meaningful if `.rhosts` support is permitted through PAM. Trust files are convenient, but when used in conjunction with the R-services, they can allow unauthenticated access to a system.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'rsh-server' 2>/dev/null | grep -q '^installed$'; then

find /root -xdev -type f -name ".rhosts" -exec rm -f {} \;
find /home -maxdepth 2 -xdev -type f -name ".rhosts" -exec rm -f {} \;
rm -f /etc/hosts.equiv

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```
