# Source: https://docs.datadoghq.com/agent/troubleshooting/ntp.md

---
title: Network Time Protocol (NTP) issues
description: >-
  Diagnose and resolve NTP offset problems that can cause incorrect alert
  triggers, metric delays, and gaps in graphs.
breadcrumbs: Docs > Agent > Agent Troubleshooting > Network Time Protocol (NTP) issues
---

# Network Time Protocol (NTP) issues

If you have noticed any of the following issues, they may be related to the NTP offset on the hosts that are reporting metrics through the Agent:

- Incorrect alert triggers
- Metric delays
- Gaps in graphs of metrics

To check the NTP offset for a host, run the Agent [status command](https://docs.datadoghq.com/agent/configuration/agent-commands/#agent-status-and-information), using the instructions appropriate for your OS, and look for the Clocks section:

```
  Clocks
  ======
    NTP offset: -0.0036 s
    System UTC time: 2015-02-12 22:10:49.524660
```

Any significant offset can have undesired effects. To prevent NTP issues, leverage Datadog's monitor for NTP offset to alert you when there is drift on a host thanks to the [NTP Integration](https://docs.datadoghq.com/integrations/ntp/). Alternatively, use Datadog's [Check Summary page](https://app.datadoghq.com/check/summary) and inspect the check `ntp.in_sync` to see the list of hosts that have NTP issues.

**Note**: Outgoing UDP traffic over the port `123` should be allowed so the Agent can confirm that the local server time is reasonably accurate according to the Datadog NTP servers.

## Further Reading{% #further-reading %}

- [How To Synchronize Microsoft Windows with a NTP Server](https://support.microsoft.com/en-us/help/816042/how-to-configure-an-authoritative-time-server-in-windows-server)
- [How to force a clock update using NTP?](http://askubuntu.com/questions/254826/how-to-force-a-clock-update-using-ntp)
- [Clock Synchronization with NTP](http://www.freebsd.org/doc/en/books/handbook/network-ntp.html)
