# Source: https://docs.datadoghq.com/security/cloud_siem/detect_and_monitor.md

---
title: Detect and Monitor
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Cloud SIEM > Detect and Monitor
---

# Detect and Monitor

## Overview{% #overview %}

Monitor your Datadog telemetry and use out-of-the-box detection rules or create custom rules to detect threats. When a threat is detected, a security signal is generated. Additionally, you can add suppressions to refine detection rules so that a signal is not generated under specific conditions. This can improve the accuracy and relevance of security signals generated.

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/detection_rule_side_panel.bfe99a73e4ede83621ae8ac0dfe06599.png?auto=format"
   alt="The side panel of a detection rule showing the conditions that trigger a signal" /%}

## Detection rules{% #detection-rules %}

### Out-of-the-box detection rules{% #out-of-the-box-detection-rules %}

Cloud SIEM provides you with an extensive list of [OOTB detection rules](https://docs.datadoghq.com/security/default_rules/#cat-cloud-siem-log-detection). After you have enabled and configured Cloud SIEM content packs, OOTB detection rules automatically begin analyzing your logs, Audit Trail events, and events from Event Management.

You can edit OOTB detection rules and do the following:

- Change the name of the rule.
- Extend the query. The original query cannot be edited, but you can add a custom query to it.
- Change the severity setting in the Set conditions section.
- Modify the playbook.

### Custom detection rules{% #custom-detection-rules %}

OOTB detection rules cover the majority of threat scenarios, but you can also create custom detection rules for your specific use cases. For custom detection rules, use the log search syntax to build and join log queries so you can target individual services, accounts, or events that you want to monitor. You can also enhance those queries with information such as the geolocation of an IP address or the status code of an HTTP request.

For logs that match the query, you can set conditions to determine whether it's a threat and if a security signal should be generated, as well as indicate the severity of the threat. Security signals provide details about the threat and include a customizable playbook, which provides information such as security policies and remediation steps.

See [Custom Detection Rules](https://docs.datadoghq.com/security/cloud_siem/detect_and_monitor/custom_detection_rules) for more information.

### Rule deprecation{% #rule-deprecation %}

Regular audits of all out-of-the-box detection rules are performed to maintain high fidelity signal quality. Deprecated rules are replaced with an improved rule.

The rule deprecation process is as follows:

1. There is a warning with the deprecation date on the rule. In the UI, the warning is shown in the:
   - Signal side panel's **Rule Details > Playbook** section
   - [Rule editor](https://docs.datadoghq.com/security/detection_rules/#clone-a-rule) for that specific rule
1. Once the rule is deprecated, there is a 15 month period before the rule is deleted. This is due to the signal retention period of 15 months. During this time, you can re-enable the rule by [cloning the rule](https://docs.datadoghq.com/security/detection_rules/#clone-a-rule) in the UI.
1. Once the rule is deleted, you can no longer clone and re-enable it.

## Suppressions{% #suppressions %}

Security signals warn you about possible threats to your infrastructure, but false positives can also be generated. For example, a large number of security signals might be triggered if a sudden influx of requests are generated from load testing an application. To reduce false positives in such scenarios, you can define a suppression query in a detection rule that prevents a signal from getting generated. You can also create suppression rules to set general suppression conditions across multiple detection rules.

See [Suppressions](https://docs.datadoghq.com/security/cloud_siem/detect_and_monitor/suppressions) for more information.

## MITRE ATT&CK Map{% #mitre-attck-map %}

After setting up your detection rules, use the Cloud SIEM [MITRE ATT&CK Map](https://docs.datadoghq.com/security/cloud_siem/detection_rules/mitre_attack_map/) to explore and visualize your rules against the MITRE ATT&CK framework so you have visibility into attacker techniques.

## Further reading{% #further-reading %}

- [Build, test, and scale detections as code with Datadog Cloud SIEM](https://www.datadoghq.com/blog/detection-as-code-cloud-siem/)
- [Identify gaps to strengthen detection coverage with the Datadog Cloud SIEM MITRE ATT&CK Map](https://www.datadoghq.com/blog/cloud-siem-mitre-attack-map/)
- [Build sufficient security coverage for your cloud environment](https://www.datadoghq.com/blog/building-security-coverage-for-cloud-environments/)
- [Best practices for creating custom detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/)
