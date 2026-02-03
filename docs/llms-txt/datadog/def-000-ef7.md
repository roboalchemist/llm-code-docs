# Source: https://docs.datadoghq.com/security/default_rules/def-000-ef7.md

---
title: >-
  Configure systemd-journal-upload TLS parameters: ServerKeyFile,
  ServerCertificateFile and TrustedCertificateFile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Configure systemd-journal-upload TLS
  parameters: ServerKeyFile, ServerCertificateFile and TrustedCertificateFile
---

# Configure systemd-journal-upload TLS parameters: ServerKeyFile, ServerCertificateFile and TrustedCertificateFile
 
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
    sed -i --follow-symlinks \
        -e 's/^ServerKeyFile\>/#&/g' \
        -e 's/^ServerCertificateFile\>/#&/g' \
        -e 's/^TrustedCertificateFile\>/#&/g' "${conf}"
done

var_journal_upload_server_key_file='/etc/pki/systemd/private/journal-upload.pem'

var_journal_upload_server_certificate_file='/etc/pki/systemd/certs/journal-upload.pem'

var_journal_upload_server_trusted_certificate_file='/etc/pki/systemd/ca/trusted.pem'


found=false

# set value in all files if they contain section or key
for f in $(echo -n "${dropin_conf}"); do
    if [ ! -e "$f" ]; then
        continue
    fi

    # find key in section and change value
    if grep -qzosP "[[:space:]]*\[Upload\]([^\n\[]*\n+)+?[[:space:]]*ServerKeyFile" "$f"; then

            sed -i "s/ServerKeyFile[^(\n)]*/ServerKeyFile=$var_journal_upload_server_key_file/" "$f"

            found=true

    # find section and add key = value to it
    elif grep -qs "[[:space:]]*\[Upload\]" "$f"; then

            sed -i "/[[:space:]]*\[Upload\]/a ServerKeyFile=$var_journal_upload_server_key_file" "$f"

            found=true
    fi
done

# if section not in any file, append section with key = value to FIRST file in files parameter
if ! $found ; then
    file=$(echo "${dropin_conf}" | cut -f1 -d ' ')
    mkdir -p "$(dirname "$file")"

    echo -e "[Upload]\nServerKeyFile=$var_journal_upload_server_key_file" >> "$file"

fi
found=false

# set value in all files if they contain section or key
for f in $(echo -n "${dropin_conf}"); do
    if [ ! -e "$f" ]; then
        continue
    fi

    # find key in section and change value
    if grep -qzosP "[[:space:]]*\[Upload\]([^\n\[]*\n+)+?[[:space:]]*ServerCertificateFile" "$f"; then

            sed -i "s/ServerCertificateFile[^(\n)]*/ServerCertificateFile=$var_journal_upload_server_certificate_file/" "$f"

            found=true

    # find section and add key = value to it
    elif grep -qs "[[:space:]]*\[Upload\]" "$f"; then

            sed -i "/[[:space:]]*\[Upload\]/a ServerCertificateFile=$var_journal_upload_server_certificate_file" "$f"

            found=true
    fi
done

# if section not in any file, append section with key = value to FIRST file in files parameter
if ! $found ; then
    file=$(echo "${dropin_conf}" | cut -f1 -d ' ')
    mkdir -p "$(dirname "$file")"

    echo -e "[Upload]\nServerCertificateFile=$var_journal_upload_server_certificate_file" >> "$file"

fi
found=false

# set value in all files if they contain section or key
for f in $(echo -n "${dropin_conf}"); do
    if [ ! -e "$f" ]; then
        continue
    fi

    # find key in section and change value
    if grep -qzosP "[[:space:]]*\[Upload\]([^\n\[]*\n+)+?[[:space:]]*TrustedCertificateFile" "$f"; then

            sed -i "s/TrustedCertificateFile[^(\n)]*/TrustedCertificateFile=$var_journal_upload_server_trusted_certificate_file/" "$f"

            found=true

    # find section and add key = value to it
    elif grep -qs "[[:space:]]*\[Upload\]" "$f"; then

            sed -i "/[[:space:]]*\[Upload\]/a TrustedCertificateFile=$var_journal_upload_server_trusted_certificate_file" "$f"

            found=true
    fi
done

# if section not in any file, append section with key = value to FIRST file in files parameter
if ! $found ; then
    file=$(echo "${dropin_conf}" | cut -f1 -d ' ')
    mkdir -p "$(dirname "$file")"

    echo -e "[Upload]\nTrustedCertificateFile=$var_journal_upload_server_trusted_certificate_file" >> "$file"

fi

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```
