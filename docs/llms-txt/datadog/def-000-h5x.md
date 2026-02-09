# Source: https://docs.datadoghq.com/security/default_rules/def-000-h5x.md

---
title: Ensure User Bash History File Has Correct Permissions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure User Bash History File Has
  Correct Permissions
---

# Ensure User Bash History File Has Correct Permissions
 
## Description{% #description %}

Set the mode of the bash history file to `0600` with the following command:

```
$ sudo chmod 0600 /home/USER/.bash_history
```

## Rationale{% #rationale %}

Incorrect permissions may enable malicious users to recover other users' command history.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

readarray -t interactive_users < <(awk -F: '$3>=1000   {print $1}' /etc/passwd)
readarray -t interactive_users_home < <(awk -F: '$3>=1000   {print $6}' /etc/passwd)
readarray -t interactive_users_shell < <(awk -F: '$3>=1000   {print $7}' /etc/passwd)

USERS_IGNORED_REGEX='nobody|nfsnobody'

for (( i=0; i<"${#interactive_users[@]}"; i++ )); do
    if ! grep -qP "$USERS_IGNORED_REGEX" <<< "${interactive_users[$i]}" && \
        [ "${interactive_users_shell[$i]}" != "/sbin/nologin" ]; then
        
        chmod u-sx,go= "${interactive_users_home[$i]}/.bash_history"
    fi
done
```
