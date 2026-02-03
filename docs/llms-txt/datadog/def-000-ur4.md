# Source: https://docs.datadoghq.com/security/default_rules/def-000-ur4.md

---
title: Ensure the Root Bash Umask is Set Correctly
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure the Root Bash Umask is Set
  Correctly
---

# Ensure the Root Bash Umask is Set Correctly
 
## Description{% #description %}

To ensure the root user's umask of the Bash shell is set properly, add or correct the `umask` setting in `/root/.bashrc` or `/root/.bashrc` to read as follows:

```
umask 0027
```

## Rationale{% #rationale %}

The umask value influences the permissions assigned to files when they are created. A misconfigured umask value could result in files with excessive permissions that can be read or written to by unauthorized users.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'bash' 2>/dev/null | grep -q '^installed$'; then

sed -i -E -e "s/^([^#]*\bumask)[[:space:]]+[[:digit:]]+/\1 0027/g" /root/.bashrc /root/.profile

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```
