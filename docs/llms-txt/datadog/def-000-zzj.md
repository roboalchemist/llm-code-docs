# Source: https://docs.datadoghq.com/security/default_rules/def-000-zzj.md

---
title: Set Password Minimum Age
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Set Password Minimum Age
---

# Set Password Minimum Age
 
## Description{% #description %}

To specify password minimum age for new accounts, edit the file `/etc/login.defs` and add or correct the following line:

```
PASS_MIN_DAYS 1
         
```

A value of 1 day is considered sufficient for many environments. The DoD requirement is 1. The profile requirement is `1`.

## Rationale{% #rationale %}

Enforcing a minimum password lifetime helps to prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, then the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.

Setting the minimum password age protects against users cycling back to a favorite password after satisfying the password reuse requirement.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'login' 2>/dev/null | grep -q '^installed$'; then

var_accounts_minimum_age_login_defs='1'

# Strip any search characters in the key arg so that the key can be replaced without
# adding any search characters to the config file.
stripped_key=$(sed 's/[\^=\$,;+]*//g' <<< "^PASS_MIN_DAYS")

# shellcheck disable=SC2059
printf -v formatted_output "%s %s" "$stripped_key" "$var_accounts_minimum_age_login_defs"

# If the key exists, change it. Otherwise, add it to the config_file.
# We search for the key string followed by a word boundary (matched by \>),
# so if we search for 'setting', 'setting2' won't match.
if LC_ALL=C grep -q -m 1 -i -e "^PASS_MIN_DAYS\\>" "/etc/login.defs"; then
    escaped_formatted_output=$(sed -e 's|/|\\/|g' <<< "$formatted_output")
    LC_ALL=C sed -i --follow-symlinks "s/^PASS_MIN_DAYS\\>.*/$escaped_formatted_output/gi" "/etc/login.defs"
else
    if [[ -s "/etc/login.defs" ]] && [[ -n "$(tail -c 1 -- "/etc/login.defs" || true)" ]]; then
        LC_ALL=C sed -i --follow-symlinks '$a'\\ "/etc/login.defs"
    fi
    printf '%s\n' "$formatted_output" >> "/etc/login.defs"
fi

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```
