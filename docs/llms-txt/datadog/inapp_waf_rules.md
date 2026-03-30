# Source: https://docs.datadoghq.com/security/application_security/policies/inapp_waf_rules.md

---
title: In-App WAF Rules
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > App and API Protection > Policies > In-App WAF Rules
---

# In-App WAF Rules

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

With App and API Protection (AAP) enabled, the Datadog tracing library actively monitors all web services and API requests for suspicious security activity.

An *In-App WAF rule* specifies conditions on the incoming request to define what the library considers suspicious. The Datadog tracing library includes hundreds of out-of-the-box AAP In-App WAF rules, which are used to display security traces in the trace explorer and in the default signal rules.

You can add to the In-App WAF rules without upgrading the tracing library.

## Structure of an AAP In-App WAF rule{% #structure-of-an-aap-in-app-waf-rule %}

An In-App WAF rule is a JSON object composed of a category, a name, tags, and conditions. When a security trace is detected, tags from the rules are propagated onto the security trace, and can be used to build [detection rules](https://docs.datadoghq.com/security/application_security/policies/custom_rules/).

### Conditions{% #conditions %}

Conditions define when the rule tags an incoming request. The conditions are composed of *inputs* and *operators*.

#### Inputs{% #inputs %}

An input represents which part of the request the operator is applied to. The following inputs are used in the In-App WAF rules:

| Name                                | Description                                                                     | Example                                            |
| ----------------------------------- | ------------------------------------------------------------------------------- | -------------------------------------------------- |
| `server.request.uri.raw`            | The full request URI received by the application service                        | `https://my.api.com/users/1234/roles?clientId=234` |
| `server.request.path_params`        | The parsed path parameters (key/value map)                                      | `userId => 1234`                                   |
| `server.request.query`              | The parsed query parameters (key/value map)                                     | `clientId => 234`                                  |
| `server.request.headers.no_cookies` | The incoming http requests headers, excluding the cookie header (key/value map) | `user-agent => Zgrab, referer => google.com`       |
| `grpc.server.request.message`       | The parsed gRPC message (key/value map)                                         | `data.items[0] => value0, data.items[1] => value1` |
| `server.request.body`               | The parsed HTTP body (key/value map)                                            | `data.items[0] => value0, data.items[1] => value1` |
| `server.response.status`            | The http status code                                                            | `200`                                              |

#### Operators{% #operators %}

| name           | Description                                                       |
| -------------- | ----------------------------------------------------------------- |
| `match_regex`  | Perform regular expression match on the inputs                    |
| `phrase_match` | Perform a fast keyword list matching                              |
| `is_xss`       | Special operator to check for cross-site scripting (XSS) payloads |
| `is_sqli`      | Special operator to check for SQL injection (SQLI) payloads       |

## Custom In-App WAF rules{% #custom-in-app-waf-rules %}

Custom In-App WAF rules enable users to log or block specific types of requests to their applications. For example, you can use custom rules to monitor login success or failure. To get started, navigate to **Security** -> **App and API Protection** -> **Policies** -> **In-App WAF** -> [**Custom Rules**](https://app.datadoghq.com/security/appsec/in-app-waf?config_by=custom-rules).

**Note:** Default rules in In-App WAF are read-only. To refine your In-App WAF behavior, modify the In-App WAF rules. Default rules cannot be modified, however, you can create a custom rule based on one of the default rules, and modify the match conditions to your needs. Be sure to disable the default rule so that you don't have two similar rules evaluating the same requests.

## Suggested rules{% #suggested-rules %}

Datadog's App and API Protection [Suggested Rules](https://app.datadoghq.com/security/appsec/policies/in-app-waf?config_by=suggested-rules) feature automatically analyzes application traffic and proposes rules to help monitor and protect login and API flows. Rules are pre-built around common authentication patterns like `users.login.success` or `users.login.failure`, which are the most critical signals for detecting suspicious login behavior.

Suggested rules benefits include:

- Reducing manual configuration by offering baseline coverage for authentication endpoints.
- Improving the speed of deploying protections across services and environments to guard against common attack vectors like brute force, credential stuffing, and automated login abuse.
- Providing high-fidelity telemetry on login attempts that can be correlated with anomalous patterns such as sudden bursts of failed logins, repeated attempts from the same IP, or login activity from unusual geographies.
- Providing visibility for [account takeover (ATO) protection](https://docs.datadoghq.com/security/account_takeover_protection), where most ATO campaigns are surfaced first through abnormal authentication activity.
- Detecting and responding to credential abuse before accounts are compromised.

Suggested rules use cases include:

- Quickly deploy protections for brute force, credential stuffing, and bot-driven login abuse.
- Use Suggested Rules as baselines for ATO protection by tracking successful and failed login attempts and tuning conditions (for example, the POST method plus 401/403 failures).
- Apply consistent detection logic across services to make it harder for attackers to bypass defenses in less monitored environments.
- Detect signs of **account takeover attempts** by monitoring abnormal login activity (for example, spikes in failures, unusual login success rates after repeated failures).

To use a suggested rule, do one of the following:

- Create a custom rule from a suggested rule:
  1. In [Suggested Rules](https://app.datadoghq.com/security/appsec/policies/in-app-waf?config_by=suggested-rules), select one or more rules and click **Create Selected Suggested Rules**.
  1. In **Create suggested custom In-App WAF rules**, click **Create rules**. This creates custom In-App WAF rules to monitor the security activities of the rules you selected.
- Modify a suggested rule to create a custom rule:
  1. In [Suggested Rules](https://app.datadoghq.com/security/appsec/policies/in-app-waf?config_by=suggested-rules), identify a rule you want to use and click **View suggested rule**.
  1. In **Add a new Business Logic**, edit the rule as needed.
  1. Click **Continue in In-App WAF**.
  1. In **Define your custom rule**, make any further changes.
  1. Click **Save Rule**.

## Configure an AAP In-App WAF rule{% #configure-an-aap-in-app-waf-rule %}

Blocking on a service is defined through the policy rules. Three Datadog default policies are included in the In-App WAF: *Datadog Recommended*, *Datadog Monitoring-only*, which monitors attacks only, and *Datadog Block Attack tools*, which blocks attack tools and monitors all other attacks.

Services using a policy are visible directly in the policy management page.

1. In Datadog, navigate to [Security > App and API Protection > Policies > In-App WAF](https://app.datadoghq.com/security/appsec/in-app-waf).

   {% image
      source="https://datadog-docs.imgix.net/images/security/application_security/threats/waf/in-app-waf.a20b10164ee9c124dd0179c9fb3275ac.png?auto=format"
      alt="In-App WAF configuration page, showing two default policies." /%}

1. Click on the three dots to the right of one of the policies, and select **Download Configuration of this Policy** to download the configuration file to your local machine.

1. Optionally, select **Apply this Policy to Services** to apply a default policy to one or more of your protection enabled AAP services.

**Note:** A policy can be applied to one or more services, but a service can only contain one *policy*.

1. Update the file to include the JSON definition of your new rule, following the specification above. For example:

   ```json
       {
           "id": "id-123",
           "name": "My In-App WAF rule",
           "tags": {
               "category": "attack_attempt",
               "crs_id": "920260",
               "type": "http_protocol_violation"
           },
           "conditions": [
               {
                   "operator": "match_regex",
                   "parameters": {
                       "inputs": [
                           {
                               "address": "server.request.uri.raw"
                           }
                       ],
                       "options": {
                           "case_sensitive": true,
                           "min_length": 6
                       },
                       "regex": "\\%u[fF]{2}[0-9a-fA-F]{2}"
                   }
               }
           ],
           "transformers": []
       },

```

1. Using a utility such as SCP or FTP, copy the `appsec-rules.json` file to your application server, for example, `/home/asm/appsec-rules.json`.

1. Following the instructions in [Enabling AAP](https://docs.datadoghq.com/security/application_security/setup/) for adding application variables in your environment, add the `DD_APPSEC_RULES` environment variable to your service with the full path to the file:

   ```
   DD_APPSEC_RULES=/home/asm/appsec-rules.json
   ```

1. Restart your service.

## What to do next{% #what-to-do-next %}

Next, [configure detection rules to create security signals](https://docs.datadoghq.com/security/application_security/policies/custom_rules/) based on those security traces defined by the In-App WAF rules you created. You can modify the provided out-of-the-box AAP detection rules or create new ones.
