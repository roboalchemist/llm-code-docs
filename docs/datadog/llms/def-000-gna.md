# Source: https://docs.datadoghq.com/security/default_rules/def-000-gna.md

---
title: Configure server restrictions for ntpd
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Configure server restrictions for ntpd
---

# Configure server restrictions for ntpd

## Description{% #description %}

ntpd is a daemon which implements the Network Time Protocol (NTP). It is designed to synchronize system clocks across a variety of systems and use a source that is highly accurate. More information on NTP can be found at [http://www.ntp.org](http://www.ntp.org). ntp can be configured to be a client and/or a server. To ensure that ntpd implements correct server restrictions, make sure that the following lines exist in the file `/etc/ntpd.conf`:

```
restrict -4 default kod nomodify notrap nopeer noquery
```

```
restrict -6 default kod nomodify notrap nopeer noquery
```

This recommendation only applies if ntp is in use on the system.

## Rationale{% #rationale %}

If ntp is in use on the system proper configuration is vital to ensuring time synchronization is working properly.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$' && { dpkg-query --show --showformat='${db:Status-Status}' 'ntp' 2>/dev/null | grep -q '^installed$'; }; then

if [ -e "/etc/ntp.conf" ] ; then

    LC_ALL=C sed -i "/^\s*restrict \-4\s\+/Id" "/etc/ntp.conf"
else
    touch "/etc/ntp.conf"
fi
# make sure file has newline at the end
sed -i -e '$a\' "/etc/ntp.conf"

cp "/etc/ntp.conf" "/etc/ntp.conf.bak"
# Insert at the end of the file
printf '%s\n' "restrict -4 default kod nomodify notrap nopeer noquery" >> "/etc/ntp.conf"
# Clean up after ourselves.
rm "/etc/ntp.conf.bak"
if [ -e "/etc/ntp.conf" ] ; then

    LC_ALL=C sed -i "/^\s*restrict \-6\s\+/Id" "/etc/ntp.conf"
else
    touch "/etc/ntp.conf"
fi
# make sure file has newline at the end
sed -i -e '$a\' "/etc/ntp.conf"

cp "/etc/ntp.conf" "/etc/ntp.conf.bak"
# Insert at the end of the file
printf '%s\n' "restrict -6 default kod nomodify notrap nopeer noquery" >> "/etc/ntp.conf"
# Clean up after ourselves.
rm "/etc/ntp.conf.bak"

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```
