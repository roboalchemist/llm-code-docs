# Source: https://docs.datadoghq.com/security/default_rules/def-000-myh.md

---
title: Set Account Expiration Following Inactivity
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Set Account Expiration Following
  Inactivity
---

# Set Account Expiration Following Inactivity
 
## Description{% #description %}

To specify the number of days after a password expires (which signifies inactivity) until an account is permanently disabled, add or correct the following line in `/etc/default/useradd`:

```
INACTIVE=30
         
```

If a password is currently on the verge of expiration, then `30` day(s) remain(s) until the account is automatically disabled. However, if the password will not expire for another 60 days, then 60 days plus `30` day(s) could elapse until the account would be automatically disabled. See the `useradd` man page for more information.

## Rationale{% #rationale %}

Inactive identifiers pose a risk to systems and applications because attackers may exploit an inactive identifier and potentially obtain undetected access to the system. Disabling inactive accounts ensures that accounts which may not have been responsibly removed are not available to attackers who may have compromised their credentials. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'login' 2>/dev/null | grep -q '^installed$'; then

var_account_disable_post_pw_expiration='30'


# Strip any search characters in the key arg so that the key can be replaced without
# adding any search characters to the config file.
stripped_key=$(sed 's/[\^=\$,;+]*//g' <<< "^INACTIVE")

# shellcheck disable=SC2059
printf -v formatted_output "%s=%s" "$stripped_key" "$var_account_disable_post_pw_expiration"

# If the key exists, change it. Otherwise, add it to the config_file.
# We search for the key string followed by a word boundary (matched by \>),
# so if we search for 'setting', 'setting2' won't match.
if LC_ALL=C grep -q -m 1 -i -e "^INACTIVE\\>" "/etc/default/useradd"; then
    escaped_formatted_output=$(sed -e 's|/|\\/|g' <<< "$formatted_output")
    LC_ALL=C sed -i --follow-symlinks "s/^INACTIVE\\>.*/$escaped_formatted_output/gi" "/etc/default/useradd"
else
    if [[ -s "/etc/default/useradd" ]] && [[ -n "$(tail -c 1 -- "/etc/default/useradd" || true)" ]]; then
        LC_ALL=C sed -i --follow-symlinks '$a'\\ "/etc/default/useradd"
    fi
    printf '%s\n' "$formatted_output" >> "/etc/default/useradd"
fi

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```
