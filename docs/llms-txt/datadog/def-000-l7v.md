# Source: https://docs.datadoghq.com/security/default_rules/def-000-l7v.md

---
title: Set Password Warning Age
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Set Password Warning Age
---

# Set Password Warning Age
 
## Description{% #description %}

To specify how many days prior to password expiration that a warning will be issued to users, edit the file `/etc/login.defs` and add or correct the following line:

```
PASS_WARN_AGE 7
         
```

The DoD requirement is 7. The profile requirement is `7`.

## Rationale{% #rationale %}

Setting the password warning age enables users to make the change at a practical time.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'login' 2>/dev/null | grep -q '^installed$'; then

var_accounts_password_warn_age_login_defs='7'

# Strip any search characters in the key arg so that the key can be replaced without
# adding any search characters to the config file.
stripped_key=$(sed 's/[\^=\$,;+]*//g' <<< "^PASS_WARN_AGE")

# shellcheck disable=SC2059
printf -v formatted_output "%s %s" "$stripped_key" "$var_accounts_password_warn_age_login_defs"

# If the key exists, change it. Otherwise, add it to the config_file.
# We search for the key string followed by a word boundary (matched by \>),
# so if we search for 'setting', 'setting2' won't match.
if LC_ALL=C grep -q -m 1 -i -e "^PASS_WARN_AGE\\>" "/etc/login.defs"; then
    escaped_formatted_output=$(sed -e 's|/|\\/|g' <<< "$formatted_output")
    LC_ALL=C sed -i --follow-symlinks "s/^PASS_WARN_AGE\\>.*/$escaped_formatted_output/gi" "/etc/login.defs"
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
