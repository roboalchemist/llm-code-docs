# Source: https://docs.datadoghq.com/security/workload_protection/guide/active-protection.md

# Source: https://docs.datadoghq.com/security/cloud_security_management/guide/active-protection.md

---
title: Proactively block crypto mining threats with Active Protection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud Security > Cloud Security Guides > Proactively
  block crypto mining threats with Active Protection
---

# Proactively block crypto mining threats with Active Protection

{% alert level="danger" %}
Please contact [Datadog Support](https://docs.datadoghq.com/help/) to enable Active Protection.
{% /alert %}

{% alert level="info" %}
Workload Protection Active Protection is in Preview.
{% /alert %}

This topic explains how to use the Workload Protection **Active Protection** feature to block crypto mining threats automatically.

By default, all OOTB Agent [threat detection rules](https://docs.datadoghq.com/security/workload_protection/workload_security_rules) are enabled and actively monitoring for crypto threats.

Active Protection enables you to proactively block and terminate crypto mining threats identified by the Datadog Agent threat detection rules.

Active Protection streamlines threat detection and targeted response, resulting in risk reduction, allowing DevSecOps and security teams to tackle evolving crypto mining threats effectively:

- Security decides which threats warrant an automated action.
- DevOps decides which applications and resources are resilient enough to withstand targeted protection.

The end result is crypto mining threat detection followed by immediate surgical mitigation against high confidence, true positive attacks.

## RBAC for Active Protection{% #rbac-for-active-protection %}

Here are some important [role and permissions][11] to use for custom rules and Active Protection RBAC:

- The `security_monitoring_cws_agent_rules_actions` permission can be used to turn on and configure the Active Protection feature.
  - To use the `security_monitoring_cws_agent_rules_actions` permission, a user with the Datadog Admin role must create a role containing the `security_monitoring_cws_agent_rules_actions` permission and then add only those users that manage Active Protection to this role.
- The **Datadog Standard** role enables users to create/update a custom rule by default, as long as the operation does not change the **protection** settings on the rule.

## Protection options{% #protection-options %}

You have three options for Agent rules:

- **Monitoring:** This is the default setting for enabled rules, regardless of whether Active Protection is enabled. The Agent monitors for the enabled rule and displays detections in [Signals](https://app.datadoghq.com/security).
- **Blocking:**
  - Blocking is available when Active Protection is enabled. Blocking is available on select OOTB rules that have high confidence, true positives.
  - The Agent monitors for the enabled rule, terminates the corresponding actions instantly, and displays detections in [Signals](https://app.datadoghq.com/security).
- **Disabled:** The Agent does not monitor for the rule events and does not send detections to the Datadog backend.

{% alert level="info" %}
Blocking is applied to all threats detected after blocking is enabled. Blocking is not retroactive.
{% /alert %}

## Active Protection availability{% #active-protection-availability %}

Active Protection is enabled at the organization level.

{% alert level="info" %}
Active Protection blocking functionality is available in a subset of the OOTB Agent rules only. Agent rule monitoring runs regardless of whether Active Protection is enabled.
{% /alert %}

To check if Active Protection is already enabled in your organization, go to [Agent Configuration](https://app.datadoghq.com/security/configuration/workload/agent-rules). If Active Protection is enabled, a **Protection** column is displayed in the Agent rule list.

{% image
   source="https://datadog-docs.imgix.net/images/security/cws/guide/protection-column.81d23ab2feaf85f3ffa1d63e34edaca5.png?auto=format"
   alt="The protection column indicates that Active Protection is enabled in the org" /%}

If Active Protection is available for a crypto mining rule, then **Monitoring** or **Blocking** is listed in the **Protection** column.

If there is no **Monitoring** or **Blocking** in the **Protection** column, then Active Protection is not available for that crypto mining rule yet.

When Active Protection is enabled, and applies to a crypto mining rule that generated a signal, you can see it by doing the following:

1. In [Signals](https://app.datadoghq.com/security), open a signal.
1. In the signal, view **Next Steps**.
   - If Active Protection is enabled, in **Proactively block threats**, the **Active Protection Enabled** is displayed.
   - If Active Protection is not enabled, **Active Protection Enabled** is not displayed.

If Active Protection is enabled and available for an Agent crypto mining rule, you can see it by looking at the rule:

1. In [Agent Configuration](https://app.datadoghq.com/security/configuration/workload/agent-rules), select a crypto mining rule.
1. In the crypto mining rule, if Active Protection is enabled and available, there is a **Protection** section.

## Enable Active Protection{% #enable-active-protection %}

When you enable Active Protection, you are enabling the Active Protection capability for your entire Datadog org. Active Protection is not limited to individual users.

By default, all OOTB Agent crypto mining rules are in a monitoring state. Enabling Active Protection does not immediately change the default state. Enabling Active Protection allows you to change the state of a crypto mining rule from monitoring to blocking.

Consequently, you do not need to worry that enabling Active Protection immediately changes the state of threat detection.

To enable Active Protection:

1. Go to Cloud Security [Agent Configuration](https://app.datadoghq.com/security/configuration/workload/agent-rules) rules.

1. Select **Enable Active Protection**.

   {% image
      source="https://datadog-docs.imgix.net/images/security/cws/guide/enable-active-protection.4fe0a6171ddef4781bd3c21c058dc4bf.png?auto=format"
      alt="Enable Active Protection button" /%}

After Active Protection is enabled, the Agent Configuration rules list contains a **Protection** column.

The **Protection** column indicates if a rule is in the **Monitoring** or **Blocking** state. When you first enable Active Protection, rules are only in a monitoring state. You must configure the blocking option manually.

### Disabling Active Protection{% #disabling-active-protection %}

After Active Protection is enabled, you can disable it on each Agent Configuration rule.

## Block threats detected by an Agent rule{% #block-threats-detected-by-an-agent-rule %}

After Active Protection is enabled, you can configure the **Blocking** option on an Agent crypto mining rule and the Agent will terminate the corresponding crypto mining actions instantly.

To enable blocking on an Agent rule:

1. In [Agent Configuration](https://app.datadoghq.com/security/configuration/workload/agent-rules), open a crypto mining rule that has **Monitoring** in the **Protection** column. If there is no **Monitoring** or **Blocking** in the **Protection** column, then Active Protection is not available for that rule yet.

1. In the Agent rule, in **Protection**, select **Blocking**.

   {% image
      source="https://datadog-docs.imgix.net/images/security/cws/guide/protection-blocking-option.5d881440155fb0dfd3646db837b3b661.png?auto=format"
      alt="An Agent rule Protection section displaying the Blocking option" /%}

1. In **Where**, select **Everywhere** or **Custom**. For details on these options, see Scoping the Agent rule below.

1. Select **Save Changes**.

1. In Agent Configuration, select **Deploy Agent Policy**.

### Scoping the Agent rule{% #scoping-the-agent-rule %}

When you create or edit an Agent crypto mining rule after Active Protection is enabled, you can select **Blocking** in the rule **Protection** setting.

When you select **Blocking**, you can scope where Datadog should apply the rule using the **Everywhere** and **Custom** options.

#### Everywhere{% #everywhere %}

The rule applies to all services, hosts, and images.

#### Custom{% #custom %}

In **Custom**, you can specify services or tags to automatically generate an expression for where to apply blocking protection.

{% alert level="info" %}
Any service or image that is not matched by the expression is not blocked, but it is still monitored.
{% /alert %}

You can use services and tags to generate an expression. Datadog matches the rule using the services or tags you provide.

- **Services:** Enter one or more service names. You can use wildcards. For example, entering `a*` generates the expression `process.envp in ["DD_SERVICE=a*"]`.
- **Tags:** Enter one or more tags for container images. If you enter multiple tags, all tags must match for the **Protection** to apply. There are two options:
  - `image_tag`: The image tag only. For example, `stable-perl`.
  - `short_image`: The image name without a tag. For example, `nginx`.
  - For example, a Github Container registry image such as `ghcr.io/MY_NAMESPACE/MY_IMAGE:2.5` can be referenced using:
    - `image_tag`: `2.5`.
    - `short_image`: `MY_IMAGE`.

## Blocked attack example{% #blocked-attack-example %}

After Active Protection is enabled and set to **Blocking** for an Agent rule, blocked threats appear in [Signals](https://app.datadoghq.com/security).

A signal for a blocked threat contains the messages `SECURITY RESPONSE` and `The malicious process <THREAT NAME> has automatically been killed.`:

{% image
   source="https://datadog-docs.imgix.net/images/security/cws/guide/active-protection-signal-messages.e61f83e470d8dc9378b1bbadf0a97674.png?auto=format"
   alt="Signal messages" /%}
