# Source: https://docs.datadoghq.com/security/cloud_siem/guide/automate-the-remediation-of-detected-threats.md

---
title: Automate the Remediation of Detected Threats with Webhooks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud SIEM > Cloud SIEM Guides > Automate the
  Remediation of Detected Threats with Webhooks
---

# Automate the Remediation of Detected Threats with Webhooks

## Overview{% #overview %}

[Cloud SIEM](https://docs.datadoghq.com/security/cloud_siem/) allows you to set Detection Rules that trigger auto-remediation workflows. With Datadog's [webhook integration](https://app.datadoghq.com/account/settings#integrations/webhooks), set up webhooks to deliver payloads to the services you want to automate whenever a [Detection Rule](https://docs.datadoghq.com/security/detection_rules/) is triggered. Every webhook payload contains information about the triggering event and a custom message that can be used to initiate services downstream. Automate commands for any service that has a webhook URL. Security orchestration and automation response tools accept incoming HTTP requests and these webhooks initiate any workflow you have defined.

Choose a security scenario below to begin automating remediation.

{% alert level="info" %}
Datadog does not send security notifications through webhooks due to HIPAA restrictions. Security alerts won't be sent to the webhook for HIPAA-enabled accounts. If you have a HIPAA-enabled account, you cannot use `@webhook...` in the Notify the following recipients setting within Datadog security notifications. If you want these alerts sent, please [contact support](https://docs.datadoghq.com/help/).
{% /alert %}

## Delete misconfigured security groups{% #delete-misconfigured-security-groups %}

In a cloud environment, it's important to delete a misconfigured resource as soon as it is created. In this scenario, you can configure a [webhook integration](https://app.datadoghq.com/account/settings#integrations/webhooks) to send a [webhook](https://app.datadoghq.com/account/settings#integrations/webhooks) to your cloud provider's API management service.

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/guide/automate-the-remediation-of-detected-threats/automation-diagram.2f2b909ab230fa3cc62a2f5193426c14.png?auto=format"
   alt="A diagram for a webhook sent to a cloud provider's API" /%}

Once configured, if an AWS user creates a poorly configured resource (for example, an overly permissive security group, or user role) within your AWS environment, Datadog Log Management ingests the related log, which triggers a security group-based Detection Rule. This process automatically sends the webhook's JSON payload to the designated Amazon API Gateway URL, which in turn activates an AWS Lambda function that automatically deletes the offending resource.

## Ban a suspicious IP address{% #ban-a-suspicious-ip-address %}

A sign-in from an unrecognized IP address might represent an attacker manipulating a trusted user's credentials, with which they can then access your data and gain persistence in your environment.

To combat this type of attack, you can use the [New Value detection method](https://www.datadoghq.com/blog/new-term-detection-method-datadog/), which analyzes your account's historical data over a chosen period of time and alerts on previously unseen values in your cloud logs.

First, set up a [new Detection Rule](https://docs.datadoghq.com/security/cloud_siem/detect_and_monitor/custom_detection_rules/?tab=threshold#new-value) using the New Value detection method.

Then, set up a [webhook](https://app.datadoghq.com/account/settings#integrations/webhooks) that sends a payload to your cloud's identity and access management (IAM) service to ban the unknown IP when this rule is triggered.

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/guide/automate-the-remediation-of-detected-threats/webhook-ip.ece3b9fbbcc34dbbb2b003408a7658d5.png?auto=format"
   alt="A new webhook that bans an unknown IP address" /%}

The following example illustrates what the relevant webhook payload could look like when a security signal is produced by Datadog:

In the `webhook-payload.json` file:

```json
{
  "SECURITY_RULE_NAME": "Request from unexpected IP address",
  "SECURITY_SIGNAL_ID": "abcd1234",
  "SECURITY_SIGNAL_ATTRIBUTES": {
    "network": {
      "client": {
        "ip": [
          "1.2.3.4"
        ]
      }
    }
  }
}
```

## Application abuse and fraud{% #application-abuse-and-fraud %}

With Datadog Cloud SIEM, you can uncover patterns of [abuse or fraud](https://www.datadoghq.com/blog/detect-abuse-of-functionality-with-datadog/) across your application. For example, set up a [Detection Rule](https://docs.datadoghq.com/security/cloud_siem/detect_and_monitor/custom_detection_rules/?tab=threshold#define-a-search-query) that is triggered when a user repeatedly attempts to purchase something in your application with invalid credit card details. Then, set up a webhook that sends a payload with remediation instructions to a service that will disable the user's credentials.

The following example illustrates what the relevant webhook payload could look like when a security signal is produced by Datadog:

In the `webhook-payload.json` file:

```json
{
  "SECURITY_RULE_NAME": "Fraudulent Credit Card Authorizations",
  "SECURITY_SIGNAL_ID": "efgh5678",
  "SECURITY_SIGNAL_ATTRIBUTES": {
    "usr": {
      "id": "john.doe@your_domain.com"
    },
    "evt": {
      "name": "credit_card_authorization",
      "outcome": "fail"
    },
    "network": {
      "client": {
        "ip": [
          "1.2.3.4"
        ]
      }
    }
  }
}
```

Datadog generates the Security Signal, which details the offense as well as the suspicious user's information, such as their IP address and user ID, and the webhook payload sends remediation instructions to a service to disable the user's credentials.

## Further Reading{% #further-reading %}

- [Start investigating signals in the Signals Explorer](https://docs.datadoghq.com/security/cloud_siem/triage_and_investigate/investigate_security_signals)
