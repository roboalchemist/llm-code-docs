# Source: https://docs.datadoghq.com/security/default_rules/def-000-1if.md

---
title: Falco finding
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Falco finding
---

# Falco finding

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
 
## Goal{% #goal %}

Respond to potential security threats detected by Falco rules promptly and effectively, minimizing the risk of security breaches and ensuring the integrity of the system.

## Strategy{% #strategy %}

Trigger notifications for any potential security threat detected by Falco [default](https://github.com/falcosecurity/rules/tree/main/rules) or custom rules.

## Triage and Response{% #triage-and-response %}

1. Review the log detected with the specific rule, affected hostname, and priority level.
1. Investigate relevant logs, network traffic captures, and system data to identify the root cause.
1. Determine the potential impact and legitimacy of the activity. If the activity is deemed benign, tune the rule in Falco.

## Note{% #note %}

If the noise level is too high from these signals, you can [upgrade](https://falco.org/docs/setup/download/#rules), [tune](https://falco.org/docs/concepts/rules/exceptions/), or [override](https://falco.org/docs/concepts/rules/overriding/) your Falco rules, as appropriate. This 3rd party rule only elevates Falco alerts from logs if they have the `maturity_stable` value in the Falco `@tags` fields, not the Datadog `tags` field.

## References{% #references %}
