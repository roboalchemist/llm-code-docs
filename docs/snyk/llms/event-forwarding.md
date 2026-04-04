# Source: https://docs.snyk.io/integrations/event-forwarding.md

# Event Forwarding

Snyk event forwarding integrations allow you to push Snyk platform events directly to certain products on other platforms, enabling you to set up custom alerting, build your own reporting, trigger automation, and more.

## Event types

Snyk supports sending two different types of events:

1. **Snyk issue events** - these events are sent when new issues are discovered in a Snyk Project, or when an issue is updated. Each event contains information about the vulnerability or other problem found, including whether a remediation is available.
2. **Snyk platform audit events** - these events are sent every time a Snyk user performs an action within the Snyk platform. For more information, see [Audit logs](https://docs.snyk.io/snyk-platform-administration/user-management-with-the-api/retrieve-audit-logs-of-user-initiated-activity-by-api-for-an-org-or-group).

{% hint style="info" %}
The **Snyk issue** event type does not include Snyk Cloud issues.
{% endhint %}

{% hint style="info" %}
The **Snyk platform audit** event type is available with Snyk Enterprise plans. See [Pricing plans](https://docs.snyk.io/implementation-and-setup/enterprise-implementation-guide/trial-limitations) for details.
{% endhint %}

## Supported integrations

Event forwarding integrations are available with the following products:

* [Amazon EventBridge](https://docs.snyk.io/integrations/event-forwarding/amazon-eventbridge) - **Issue events** and **Audit events**
* [AWS CloudTrail Lake](https://docs.snyk.io/integrations/event-forwarding/aws-cloudtrail-lake) - **Audit events**
* [AWS SecurityHub](https://docs.snyk.io/integrations/event-forwarding/aws-security-hub) - **Issue events**
* [Google Security Command Center](https://docs.snyk.io/integrations/event-forwarding/google-security-command-center) **- Issue events**
* [CrowdStrike Falcon Next-Gen SIEM](https://docs.snyk.io/integrations/event-forwarding/crowdstrike-falcon-next-gen-siem) - **Issue events**
