# Source: https://docs.datadoghq.com/security/default_rules/def-000-bme.md

---
title: Configure systemd-journal-upload URL
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Configure systemd-journal-upload URL
---

# Configure systemd-journal-upload URL

## Description{% #description %}

Ubuntu 24.04 must offload rsyslog messages for networked systems in real time and offload standalone systems at least weekly

## Rationale{% #rationale %}

Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$' && { ! (systemctl is-active rsyslog &>/dev/null); }; then

dropin_conf=/etc/systemd/journal-upload.conf.d/60-journald_upload.conf
mkdir -p /etc/systemd/journal-upload.conf.d
touch "${dropin_conf}"

for conf in /etc/systemd/journal-upload.conf /etc/systemd/journal-upload.conf.d/*; do
    [[ -e "${conf}" ]] || continue
    sed -i --follow-symlinks 's/^URL\>/#&/g' "${conf}"
done

var_journal_upload_url='remotelogserver'


found=false

# set value in all files if they contain section or key
for f in $(echo -n "${dropin_conf}"); do
    if [ ! -e "$f" ]; then
        continue
    fi

    # find key in section and change value
    if grep -qzosP "[[:space:]]*\[Upload\]([^\n\[]*\n+)+?[[:space:]]*URL" "$f"; then

            sed -i "s/URL[^(\n)]*/URL=$var_journal_upload_url/" "$f"

            found=true

    # find section and add key = value to it
    elif grep -qs "[[:space:]]*\[Upload\]" "$f"; then

            sed -i "/[[:space:]]*\[Upload\]/a URL=$var_journal_upload_url" "$f"

            found=true
    fi
done

# if section not in any file, append section with key = value to FIRST file in files parameter
if ! $found ; then
    file=$(echo "${dropin_conf}" | cut -f1 -d ' ')
    mkdir -p "$(dirname "$file")"

    echo -e "[Upload]\nURL=$var_journal_upload_url" >> "$file"

fi

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```
