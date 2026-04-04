# Source: https://docs.datadoghq.com/security/workload_protection.md

---
title: Workload Protection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Workload Protection
---

# Workload Protection

Workload Protection monitors file, network, and process activity across your environment to detect real-time threats to your infrastructure. As part of the Datadog platform, you can combine the real-time threat detection of Workload Protection with metrics, logs, traces, and other telemetry to see the full context surrounding a potential attack on your workloads.

## Detect threats to your production workloads in real-time{% #detect-threats-to-your-production-workloads-in-real-time %}

Monitor file and process activity at the kernel level to detect threats to your infrastructure, such as Amazon EC2 instances, Docker containers, and Kubernetes clusters. Combine Workload Protection with [Cloud Network Monitoring](https://docs.datadoghq.com/network_monitoring/performance/) and detect suspicious activity at the network level before a workload is compromised.

Workload Protection Threats uses the Datadog Agent to monitor your environment. If you don't already have the Datadog Agent set up, [start with setting up the Agent](https://docs.datadoghq.com/agent/) on a [supported operating system](https://docs.datadoghq.com/security/cloud_security_management/setup/). There are four types of monitoring that the Datadog Agent uses for Workload Protection:

1. **Process Execution Monitoring** to watch process executions for malicious activity on hosts or containers in real-time.
1. **File Integrity Monitoring** to watch for changes to key files and directories on hosts or containers in real-time.
1. **DNS Activity Monitoring** to watch network traffic for malicious activity on hosts and containers in real-time.
1. **Kernel Activity Monitoring** to watch for kernel-layer attacks like process hijacking, container breakouts, and more in real-time.

## Proactively block threats with Active Protection{% #proactively-block-threats-with-active-protection %}

By default, all OOTB Agent crypto mining threat detection rules are enabled and actively monitoring for threats.

[Active Protection](https://docs.datadoghq.com/security/workload_protection/guide/active-protection) enables you to proactively block and terminate crypto mining threats identified by the Datadog Agent threat detection rules.

## Manage out-of-the-box and custom detection rules{% #manage-out-of-the-box-and-custom-detection-rules %}

Workload Protection Threats comes with more than 50 out-of-the-box detection rules that are maintained by a team of security experts. The rules surface the most important risks so that you can immediately take steps to remediate. Agent expression rules define the workload activities to be collected for analysis while backend detection rules analyze the activities and identify attacker techniques and other risky patterns of behavior.

Set up [Cloud Security](https://docs.datadoghq.com/security/cloud_security_management/setup/) with Remote Configuration (Remote Configuration enables users to remotely configure and change the behavior of Datadog components deployed in their environment.) to automatically deploy new and updated rules to the Agent. [Customize the rules](https://docs.datadoghq.com/security/notifications/#detection-rule-notifications) by defining how each rule monitors process, network, and file activity, [create custom rules](https://docs.datadoghq.com/security/workload_protection/agent_expressions), and set up real-time notifications for new signals.

## Set up real-time notifications{% #set-up-real-time-notifications %}

[Send real-time notifications](https://docs.datadoghq.com/security/notifications/) when a threat is detected in your environment, so that your teams can take action to mitigate the risk. Notifications can be sent to [Slack, email, PagerDuty, webhooks, and more](https://docs.datadoghq.com/security/notifications/#notification-channels).

Use template variables and Markdown to [customize notification messages](https://docs.datadoghq.com/security/notifications/#detection-rule-notifications). Edit, disable, and delete existing notification rules, or create new rules and define custom logic for when a notification is triggered based on severity and rule type.

## Investigate and remediate security signals{% #investigate-and-remediate-security-signals %}

Investigate and triage security signals in the [Signals Explorer](https://docs.datadoghq.com/security/workload_protection/security_signals). View detailed information about the impacted files or processes, related signals and logs, and remediation steps.

{% callout %}
##### Active Protection

Datadog is introducing a new feature called Active Protection to address the crypto threats detected in your environment automatically. Active Protection is in Preview. Fill out the form to request access.

[Request Access](https://docs.google.com/forms/d/e/1FAIpQLSfzQARsTPr3tiJDnS_4bGx7w35LDfAbGUggaUzHYoL0dIUMWQ/viewform)
{% /callout %}

## Get started{% #get-started %}

- [Complete setup and configuration](https://docs.datadoghq.com/security/cloud_security_management/setup/)
- [Datadog role permissions for Workload Protection](https://docs.datadoghq.com/account_management/rbac/permissions/#cloud-security-platform)
- [Learn about Workload Protection detection rules](https://docs.datadoghq.com/security/workload_protection/workload_security_rules)
- [Start using out-of-the-box Workload Protection detection rules](https://docs.datadoghq.com/security/default_rules/#cat-workload-security)
- [Getting Started with Cloud Security Management](https://docs.datadoghq.com/getting_started/cloud_security_management)

## Further reading{% #further-reading %}

- [Turn fragmented runtime signals into coherent attack stories with Datadog Workload Protection](https://www.datadoghq.com/blog/workload-protection-investigation/)
