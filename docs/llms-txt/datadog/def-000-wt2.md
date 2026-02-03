# Source: https://docs.datadoghq.com/security/default_rules/def-000-wt2.md

---
title: 'Mimecast Alert: phishing email detected'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: 'Docs > Datadog Security > OOTB Rules > Mimecast Alert: phishing email detected'
---

# Mimecast Alert: phishing email detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1566-phishing](https://attack.mitre.org/techniques/T1566) 
## Goal{% #goal %}

Detect when Mimecast identifies a phishing email.

## Strategy{% #strategy %}

Targeted Threat Protection - Impersonation Protect tackles the increasing threat of socially engineered "whaling" attacks. This rule can used to detect an email which contains impersonation attempts that have been flagged as external and malicious with definition as phishing.

For more details: [Click here](https://community.mimecast.com/s/article/email-security-cloud-gateway-targeted-threat-protection-impersonation-protect)

## Triage and response{% #triage-and-response %}

1. Investigate the suspected phishing email, including sender information, email content, and any attachments.
1. Verify whether sensitive information has been compromised and assess the impact.
1. Apply appropriate remediation steps according to the company's incident response policy, which may include:
   - Marking the email as phishing and reporting it to your security team.
   - Investgate sender: {{@senderAddress}} or blocking the sender's email address.
   - Notifying potentially affected users and providing guidance on next steps.
   - Updating email filters and security measures to prevent similar attacks.
