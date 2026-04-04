# Source: https://docs.datadoghq.com/security/workload_protection/workload_security_rules/custom_rules.md

# Source: https://docs.datadoghq.com/security/threats/workload_security_rules/custom_rules.md

# Source: https://docs.datadoghq.com/security/sensitive_data_scanner/scanning_rules/custom_rules.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/custom_rules.md

# Source: https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/custom_rules.md

# Source: https://docs.datadoghq.com/security/application_security/policies/custom_rules.md

---
title: Custom Detection Rules
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > App and API Protection > Policies > Custom Detection
  Rules
---

# Custom Detection Rules

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

App and API Protection (AAP) comes with a set of [out-of-the-box detection rules](https://docs.datadoghq.com/security/default_rules/?category=cat-application-security) which aim to catch attack attempts, vulnerabilities found by attacker, and business logic abuse that impact your production systems.

However, there are situations where you may want to customize a rule based on your environment or workload. For example, you may want to customize a detection rule that detects users performing sensitive actions from a geolocation where your business doesn't operate.

Another example is customizing a rule to exclude an internal security scanner. AAP detects its activity as expected. However, you may not want to be notified of its regularly occurring scan.

In these situations, a custom detection rule can be created to exclude such events. This guide shows you how to create a custom detection rule for AAP.

## Business logic abuse detection rule{% #business-logic-abuse-detection-rule %}

AAP offers out of the box rules to detect business logic abuse (for example, resetting a password through brute force). Those rules require [adding business logic information to traces](https://docs.datadoghq.com/security/application_security/how-it-works/add-user-info/?tab=set_user#adding-business-logic-information-login-success-login-failure-any-business-logic-to-traces).

Recent Datadog Tracing Libraries attempt to detect and send user login and signup events automatically without needing to modify the code. If needed, you can [opt out of the automatic user activity event tracking](https://docs.datadoghq.com/security/application_security/how-it-works/add-user-info/?tab=set_user#disabling-automatic-user-activity-event-tracking).

You can filter the rules, and identify which business logic to start tracking. Additionally, you can use these rules as a blueprint to create custom rules based on your own business logic.

See the section below to see how to configure your rules.

## Configuration{% #configuration %}

To customize an OOTB detection rule, you must first clone an existing rule. Navigate to your [Detection Rules](https://app.datadoghq.com/security/appsec/signals-rules) and select a rule. Scroll to the bottom of the rule and click the Clone Rule button. This now enables you to edit the existing rule.

### Define an AAP query{% #define-an-aap-query %}

Construct an AAP query using the [same query syntax as in the AAP Trace Explorer](https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/). For example, create a query to monitor login successes from outside of the United States: `@appsec.security_activity:business_logic.users.login.success -@actor.ip_details.country.iso_code:US`.

Optionally, define a unique count and signal grouping. Count the number of unique values observed for an attribute in a given timeframe. The defined group-by generates a signal for each group-by value. Typically, the group-by is an entity (like user, IP, or service). The group-by is also used to join the queries together.

Use the preview section to see which AAP traces match the search query. You can also add additional queries with the Add Query button.

##### Joining queries{% #joining-queries %}

Joining queries to span a timeframe can increase the confidence or severity of the Security Signal. For example, to detect a successful attack, both successful and unsuccessful triggers can be correlated for a service.

Queries are correlated together by using a `group by` value. The `group by` value is typically an entity (for example, `IP` or `Service`), but can be any attribute.

For example, create opposing queries that search for the same `business_logic.users.login.success` activity, but append opposing HTTP path queries for successful and unsuccessful attempts:

Query 1: `@appsec.security_activity:business_logic.users.login.success @actor.ip_details.country.iso_code:US`.

Query 2: `@appsec.security_activity:business_logic.users.login.success -@actor.ip_details.country.iso_code:US`.

In this instance, the joined queries technically hold the same attribute value: the value must be the same for the case to be met. If a `group by` value doesn't exist, the case will never be met. A Security Signal is generated for each unique `group by` value when a case is matched.

### Exclude benign activity with suppression queries{% #exclude-benign-activity-with-suppression-queries %}

In the **Only generate a signal if there is a match** field, you have the option to enter a query so that a trigger is only generated when a value is met.

In the **This rule will not generate a signal if there is a match** field, you have the option to enter suppression queries so that a trigger is not generated when the values are met. For example, if a service is triggering a signal, but the action is benign and you no longer want signals triggered from this service, create a query that excludes `service`.

### Set a rule case{% #set-a-rule-case %}

#### Trigger{% #trigger %}

Rule cases, such as `successful login > 0`, are evaluated as case statements. Thus, the first case to match generates the signal. Create one or multiple rule cases, and click on the grey area next to them to drag and manipulate their orderings.

A rule case contains logical operations (`>, >=, &&, ||`) to determine if a signal should be generated based on the event counts in the previously defined queries.

**Note**: The query label must precede the operator. For example, `a > 3` is allowed; `3 < a` is not allowed.

Provide a **name** for each rule case. This name is appended to the rule name when a signal is generated.

#### Severity and notification{% #severity-and-notification %}

In the **Set severity to** dropdown menu, select the appropriate severity level (`INFO`, `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`).

In the **Add notify** section, click **Add Recipient** to optionally configure [notification targets](https://docs.datadoghq.com/security_platform/notifications/#notification-channels).

You can also create [notification rules](https://docs.datadoghq.com/security/notifications/rules/) to avoid manual edits to notification preferences for individual detection rules.

### Time windows{% #time-windows %}

An `evaluation window` is specified to match when at least one of the cases matches true. This is a sliding window and evaluates cases in real time.

After a signal is generated, the signal remains "open" if a case is matched at least once within the `keep alive` window. Each time a new event matches any of the cases, the *last updated* timestamp is updated for the signal.

A signal closes once the time exceeds the `maximum signal duration`, regardless of the query being matched. This time is calculated from the first seen timestamp.

Click **Add Case** to add additional cases.

**Note**: The `evaluation window` must be less than or equal to the `keep alive` and `maximum signal duration`.

### Say what's happening{% #say-whats-happening %}

1. Enter a **Rule name**. The name appears in the detection rules list view and the title of the security signal.
1. In the **Rule message** section, use [notification variables](https://docs.datadoghq.com/security_platform/notifications/variables/) and Markdown to customize the notifications sent when a signal is generated.
   - You can use [template variables](https://docs.datadoghq.com/security_platform/notifications/variables/#template-variables) in the notification to inject dynamic context from triggered logs directly into a security signal and its associated notifications.
   - See the [Notification Variables documentation](https://docs.datadoghq.com/security_platform/notifications/variables/) for more information and examples.
1. Use the **Tag resulting signals** dropdown menu to add tags to your signals. For example, `security:attack` or `technique:T1110-brute-force`.
   - **Note**: the tag `security` is special. This tag is used to classify the security signal. The recommended options are: `attack`, `threat-intel`, `compliance`, `anomaly`, and `data-leak`.

Use the **Tag resulting signals** dropdown menu to add tags to your signals. For example, `attack:sql-injection-attempt`.

**Note**: The tag `security` is special. This tag is used to classify the security signal. The recommended options are: `attack`, `threat-intel`, `compliance`, `anomaly`, and `data-leak`.

## Further Reading{% #further-reading %}

- [Protect against threats with Datadog App and API Protection](https://docs.datadoghq.com/security/application_security/)
- [Creating event rules](https://docs.datadoghq.com/security/application_security/event_rules/)
- [Troubleshoot common Datadog App and API Protection issues](https://docs.datadoghq.com/security/application_security/troubleshooting)
- [Learn more about Security notification variables](https://docs.datadoghq.com/security/notifications/variables/)
- [Syntax for defining the AAP query](https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/)
