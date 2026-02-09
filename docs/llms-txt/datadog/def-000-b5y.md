# Source: https://docs.datadoghq.com/security/default_rules/def-000-b5y.md

---
title: Configure ntpd To Run As ntp User
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Configure ntpd To Run As ntp User
---

# Configure ntpd To Run As ntp User
 
## Description{% #description %}

ntp is a daemon which implements the Network Time Protocol (NTP). It is designed to synchronize system clocks across a variety of systems and use a source that is highly accurate. More information on NTP can be found at [http://www.ntp.org](http://www.ntp.org). ntp can be configured to be a client and/or a server. To ensure that ntpd is running as ntp user, Add or edit the `OPTIONS` variable in `/etc/sysconfig/ntpd` to include ' -u ntp:ntp ':

```
OPTIONS="-u ntp:ntp"
```

This recommendation only applies if ntp is in use on the system.

## Rationale{% #rationale %}

If ntp is in use on the system proper configuration is vital to ensuring time synchronization is working properly. Running ntpd under dedicated user accounts limits the attack surface for potential attacker exploiting security flaws in the daemon or the protocol.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$' && { dpkg-query --show --showformat='${db:Status-Status}' 'ntp' 2>/dev/null | grep -q '^installed$'; }; then

if grep -q 'OPTIONS=.*' /etc/sysconfig/ntpd; then
	# trying to solve cases where the parameter after OPTIONS
	#may or may not be enclosed in quotes
	sed -i -E 's/^([\s]*OPTIONS=["]?[^"]*)("?)/\1 -u ntp:ntp\2/' /etc/sysconfig/ntpd
else
	echo 'OPTIONS="-u ntp:ntp"' >> /etc/sysconfig/ntpd
fi

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```
