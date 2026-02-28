# Source: https://docs.datadoghq.com/security/default_rules/def-000-ksw.md

---
title: Okta user reported suspicious activity
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Okta user reported suspicious activity
---

# Okta user reported suspicious activity
Classification:attack
## Goal{% #goal %}

Detect when an Okta user reports suspicious activity in response to an end user security notification.

## Strategy{% #strategy %}

This rule monitors the case when an Okta user reports suspicious activity in response to an end user security notification. [Suspicious Activity Reporting](https://help.okta.com/en-us/content/topics/security/suspicious-activity-reporting.htm) provides a user with the option to report unrecognized activity from email notifications about account activity. Account activity includes:

- New sign-on notification
- Authenticator enrolled
- Authenticator reset
- Password changed

## Triage and response{% #triage-and-response %}

1. Identify the event type (`@debugContext.debugData.suspiciousActivityEventType`) that occurred and the IP address (`@debugContext.debugData.suspiciousActivityEventIp`) from which suspicious activity originated.
1. Determine if any other activity has originated from this address by using the Cloud SIEM - IP Investigation dashboard.
1. If the activity appears to be harmful:
   - Begin your organization's incident response process and investigate for any account takeovers.
