# Source: https://docs.datadoghq.com/security/default_rules/def-000-9fb.md

---
title: Ensure that chronyd is running under chrony user account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure that chronyd is running under
  chrony user account
---

# Ensure that chronyd is running under chrony user account

## Description{% #description %}

chrony is a daemon which implements the Network Time Protocol (NTP). It is designed to synchronize system clocks across a variety of systems and use a source that is highly accurate. More information on chrony can be found at [https://chrony-project.org/](https://chrony-project.org/). Chrony can be configured to be a client and/or a server. To ensure that chronyd is running under chrony user account, `user` variable in `/etc/chrony/chrony.conf` is set to `_chrony` or is absent:

```
user _chrony
```

This recommendation only applies if chrony is in use on the system.

## Rationale{% #rationale %}

If chrony is in use on the system proper configuration is vital to ensuring time synchronization is working properly.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$' && { dpkg-query --show --showformat='${db:Status-Status}' 'chrony' 2>/dev/null | grep -q '^installed$'; }; then

# Strip any search characters in the key arg so that the key can be replaced without
# adding any search characters to the config file.
stripped_key=$(sed 's/[\^=\$,;+]*//g' <<< "^user")

# shellcheck disable=SC2059
printf -v formatted_output "%s %s" "$stripped_key" "_chrony"

# If the key exists, change it. Otherwise, add it to the config_file.
# We search for the key string followed by a word boundary (matched by \>),
# so if we search for 'setting', 'setting2' won't match.
if LC_ALL=C grep -q -m 1 -i -e "^user\\>" "/etc/chrony/chrony.conf"; then
    escaped_formatted_output=$(sed -e 's|/|\\/|g' <<< "$formatted_output")
    LC_ALL=C sed -i --follow-symlinks "s/^user\\>.*/$escaped_formatted_output/gi" "/etc/chrony/chrony.conf"
else
    if [[ -s "/etc/chrony/chrony.conf" ]] && [[ -n "$(tail -c 1 -- "/etc/chrony/chrony.conf" || true)" ]]; then
        LC_ALL=C sed -i --follow-symlinks '$a'\\ "/etc/chrony/chrony.conf"
    fi
    printf '%s\n' "$formatted_output" >> "/etc/chrony/chrony.conf"
fi

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```
