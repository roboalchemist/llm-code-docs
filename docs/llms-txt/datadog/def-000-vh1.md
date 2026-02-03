# Source: https://docs.datadoghq.com/security/default_rules/def-000-vh1.md

---
title: Set Password Hashing Algorithm in /etc/login.defs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Set Password Hashing Algorithm in
  /etc/login.defs
---

# Set Password Hashing Algorithm in /etc/login.defs
 
## Description{% #description %}

In `/etc/login.defs`, add or update the following line to ensure the system will use SHA512 as the hashing algorithm:

```
ENCRYPT_METHOD SHA512
         
```

## Rationale{% #rationale %}

Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Passwords that are encrypted with a weak algorithm are no more protected than if they are kept in plain text.

Using a stronger hashing algorithm makes password cracking attacks more difficult.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'login' 2>/dev/null | grep -q '^installed$'; then

var_password_hashing_algorithm='SHA512'


# Allow multiple algorithms, but choose the first one for remediation
#
var_password_hashing_algorithm="$(echo $var_password_hashing_algorithm | cut -d \| -f 1)"

# Strip any search characters in the key arg so that the key can be replaced without
# adding any search characters to the config file.
stripped_key=$(sed 's/[\^=\$,;+]*//g' <<< "^ENCRYPT_METHOD")

# shellcheck disable=SC2059
printf -v formatted_output "%s %s" "$stripped_key" "$var_password_hashing_algorithm"

# If the key exists, change it. Otherwise, add it to the config_file.
# We search for the key string followed by a word boundary (matched by \>),
# so if we search for 'setting', 'setting2' won't match.
if LC_ALL=C grep -q -m 1 -i -e "^ENCRYPT_METHOD\\>" "/etc/login.defs"; then
    escaped_formatted_output=$(sed -e 's|/|\\/|g' <<< "$formatted_output")
    LC_ALL=C sed -i --follow-symlinks "s/^ENCRYPT_METHOD\\>.*/$escaped_formatted_output/gi" "/etc/login.defs"
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
