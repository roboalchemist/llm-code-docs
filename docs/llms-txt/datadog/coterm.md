# Source: https://docs.datadoghq.com/coterm.md

---
title: Datadog CoTerm
description: >-
  Record terminal sessions, analyze them in Datadog, and protect against
  dangerous terminal commands with CoTerm's validation layer.
breadcrumbs: Docs > Datadog CoTerm
---

# Datadog CoTerm

Datadog CoTerm is a CLI utility that can record terminal sessions and add a layer of validation to your terminal commands.

{% image
   source="https://datadog-docs.imgix.net/images/coterm/hero.0b5702e04be40a3b7d96eea2462b7d57.png?auto=format"
   alt="In Datadog, a page titled Terminal Session. An embedded video showing a terminal session. A scrubber bar controls video playback." /%}

With CoTerm, you can:

- **Record terminal sessions and analyze these recordings in Datadog**.

Investigating terminal sessions provides context about how system and security incidents were caused and remediated.

- **Protect against the accidental execution of dangerous terminal commands**.

CoTerm can intercept terminal commands and warn you before you execute a risky command. For even more oversight, you can use CoTerm with [Datadog Case Management](https://docs.datadoghq.com/incident_response/case_management/) to require approvals for particularly impactful commands.

For your security, CoTerm uses [Sensitive Data Scanner](https://docs.datadoghq.com/security/sensitive_data_scanner/) to detect and obfuscate sensitive data, such as passwords and API keys.

## Get started{% #get-started %}

- [Installation: Install CoTerm and authorize it to access your Datadog account.](https://docs.datadoghq.com/coterm/install)
- [Usage: Use the CoTerm CLI, set up automatic recording, and safeguard against dangerous commands.](https://docs.datadoghq.com/coterm/usage)
- [Configuration Rules: Set highly configurable rules for how CoTerm handles specific commands.](https://docs.datadoghq.com/coterm/rules)

## Review terminal sessions in Datadog{% #review-terminal-sessions-in-datadog %}

You can review your recorded terminal sessions and process data in Datadog:

- **As replays**: Watch [terminal sessions](https://app.datadoghq.com/terminal-streams) in a video-like player.
- **As events**: In [Event Explorer](http://app.datadoghq.com/event/explorer?query=source%3Acoterm_process_info), each recorded command appears as an event.
- **As logs**: In [Log Explorer](https://app.datadoghq.com/logs?query=service%3Addcoterm), you can perform full-text searches and queries of terminal sessions as multi-line logs.

## Known limitations{% #known-limitations %}

- The maximum duration of a recorded session is approximately 24 hours.
- [Sensitive data redaction](https://docs.datadoghq.com/security/sensitive_data_scanner/) can fail if the sensitive data is spread across multiple lines.
- On Linux, `seccomp`-based tracing prevents you from elevating your permissions during a recording.

## Further reading{% #further-reading %}

- [Livestream, record, and log terminal sessions with Datadog CoTerm](https://www.datadoghq.com/blog/introducing-coterm/)
