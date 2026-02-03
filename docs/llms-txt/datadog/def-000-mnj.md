# Source: https://docs.datadoghq.com/security/default_rules/def-000-mnj.md

---
title: System Audit Logs Must Have Mode 0750 or Less Permissive
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > System Audit Logs Must Have Mode 0750
  or Less Permissive
---

# System Audit Logs Must Have Mode 0750 or Less Permissive
 
## Description{% #description %}

If `log_group` in `/etc/audit/auditd.conf` is set to a group other than the `root` group account, change the mode of the audit log files with the following command:

```gdscript3
$ sudo chmod 0750 /var/log/audit
```

Otherwise, change the mode of the audit log files with the following command:

```gdscript3
$ sudo chmod 0700 /var/log/audit
```

## Rationale{% #rationale %}

If users can write to audit logs, audit trails can be modified or destroyed.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'auditd' 2>/dev/null | grep -q '^installed$' && dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

if LC_ALL=C grep -iw ^log_file /etc/audit/auditd.conf; then
  DIR=$(awk -F "=" '/^log_file/ {print $2}' /etc/audit/auditd.conf | tr -d ' ' | rev | cut -d"/" -f2- | rev)
else
  DIR="/var/log/audit"
fi


if LC_ALL=C grep -m 1 -q ^log_group /etc/audit/auditd.conf; then
  GROUP=$(awk -F "=" '/log_group/ {print $2}' /etc/audit/auditd.conf | tr -d ' ')
  if ! [ "${GROUP}" == 'root' ] ; then
    chmod 0750 $DIR
  else
    chmod 0700 $DIR
  fi
else
  chmod 0700 $DIR
fi

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```
