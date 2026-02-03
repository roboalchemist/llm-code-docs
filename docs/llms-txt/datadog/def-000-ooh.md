# Source: https://docs.datadoghq.com/security/default_rules/def-000-ooh.md

---
title: Ensure Logs Sent To Remote Host
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Ensure Logs Sent To Remote Host
---

# Ensure Logs Sent To Remote Host
 
## Description{% #description %}

To configure rsyslog to send logs to a remote log server, open `/etc/rsyslog.conf` and read and understand the last section of the file, which describes the multiple directives necessary to activate remote logging. Along with these other directives, the system can be configured to forward its logs to a particular log server by adding or correcting one of the following lines, substituting `logcollector` appropriately. The choice of protocol depends on the environment of the system; although TCP and RELP provide more reliable message delivery, they may not be supported in all environments.

To use UDP for log message delivery:

```
*.* @logcollector
        
```

Or in RainerScript:

```
*.* action(type="omfwd" ... target="logcollector" protocol="udp")
```

To use TCP for log message delivery:

```
*.* @@logcollector
        
```

Or in RainerScript:

```
*.* action(type="omfwd" ... target="logcollector" protocol="tcp")
```

To use RELP for log message delivery:

```
*.* :omrelp:logcollector
        
```

Or in RainerScript:

```
*.* action(type="omfwd" ... target="logcollector" protocol="relp")
```

There must be a resolvable DNS CNAME or Alias record set to "logcollector" for logs to be sent correctly to the centralized logging utility.

## Rationale{% #rationale %}

A log server (loghost) receives syslog messages from one or more systems. This data can be used as an additional log source in the event a system is compromised and its local logs are suspect. Forwarding log messages to a remote loghost also provides system administrators with a centralized place to view the status of multiple hosts within the enterprise.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

rsyslog_remote_loghost_address='logcollector'


# Strip any search characters in the key arg so that the key can be replaced without
# adding any search characters to the config file.
stripped_key=$(sed 's/[\^=\$,;+]*//g' <<< "^\*\.\*")

# shellcheck disable=SC2059
printf -v formatted_output "%s %s" "$stripped_key" "@@$rsyslog_remote_loghost_address"

# If the key exists, change it. Otherwise, add it to the config_file.
# We search for the key string followed by a word boundary (matched by \>),
# so if we search for 'setting', 'setting2' won't match.
if LC_ALL=C grep -q -m 1 -i -e "^\*\.\*\\>" "/etc/rsyslog.conf"; then
    escaped_formatted_output=$(sed -e 's|/|\\/|g' <<< "$formatted_output")
    LC_ALL=C sed -i --follow-symlinks "s/^\*\.\*\\>.*/$escaped_formatted_output/gi" "/etc/rsyslog.conf"
else
    if [[ -s "/etc/rsyslog.conf" ]] && [[ -n "$(tail -c 1 -- "/etc/rsyslog.conf" || true)" ]]; then
        LC_ALL=C sed -i --follow-symlinks '$a'\\ "/etc/rsyslog.conf"
    fi
    printf '%s\n' "$formatted_output" >> "/etc/rsyslog.conf"
fi

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

## Warning{% #warning %}

It is important to configure queues in case the client is sending log messages to a remote server. If queues are not configured, the system will stop functioning when the connection to the remote server is not available. Please consult Rsyslog documentation for more information about configuration of queues. The example configuration which should go into `/etc/rsyslog.conf` can look like the following lines:

```

$ActionQueueType LinkedList
$ActionQueueFileName queuefilename
$ActionQueueMaxDiskSpace 1g
$ActionQueueSaveOnShutdown on
$ActionResumeRetryCount -1
```

Or if using Rainer Script syntax, it could be:

```
*.* action(type="omfwd" queue.type="linkedlist" queue.filename="example_fwd" action.resumeRetryCount="-1" queue.saveOnShutdown="on" target="example.com" port="30514" protocol="tcp")
```
