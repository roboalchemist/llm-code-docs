# Source: https://docs.datadoghq.com/security/default_rules/def-000-hyz.md

---
title: Windows OpenSSH server listening on socket
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows OpenSSH server listening on
  socket
---

# Windows OpenSSH server listening on socket

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0008-lateral-movement](https://attack.mitre.org/tactics/TA0008)Technique:[T1021-remote-services](https://attack.mitre.org/techniques/T1021) 
## Goal{% #goal %}

Detects when Windows OpenSSH server starts listening on network sockets, potentially indicating unauthorized remote access establishment.

## Strategy{% #strategy %}

This rule monitors Windows OpenSSH server events where `@evt.id` is `4` from the `sshd` process when `@Event.EventData.Data.payload` contains `Server listening on` messages. While OpenSSH can be legitimately installed on Windows systems for remote administration, unexpected SSH server activation may indicate attacker-installed persistence mechanisms or unauthorized remote access capabilities. Attackers often deploy SSH servers to maintain persistent access to compromised systems and facilitate lateral movement within the network.

## Triage and response{% #triage-and-response %}

- Verify if the OpenSSH server installation and activation on `{{host}}` was authorized and follows organizational IT policies for remote access tools.
- Check the network interface and port configuration to determine if the SSH server is accessible from external networks or only internal systems.
- Review system installation logs and recent administrative activities to identify who installed or configured the OpenSSH server.
- Examine SSH server configuration files for any unusual settings, authorized keys, or access controls that may indicate malicious configuration.
- Monitor for subsequent SSH connection attempts to determine if the server is being used for legitimate administration or unauthorized access.
