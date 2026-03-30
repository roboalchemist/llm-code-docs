# Source: https://docs.api7.ai/apisix/enterprise-feature/alerts-and-contact-points.md

# Alerts and Contact Points

When using an API gateway, developers may encounter various exceptions, such as impending SSL certificate expiration or HTTP 5xx response codes exceeding predefined thresholds. To handle these scenarios, API7 Enterprise provides a set of exception event monitoring and alert triggering mechanisms. This mechanism allows real-time tracking of exceptions and, upon detecting issues, sends alert notifications immediately via email and Webhook to preset contacts, ensuring timely attention and resolution.

## How Do Alerts Work?[â](#how-do-alerts-work "Direct link to How Do Alerts Work?")

API7 Enterprise is pre-configured with more than 20 exception events, each of which can be customized with specific trigger rules and thresholds. Additionally, users can select gateway groups to which these rules will be applied.

Alert policies offer two modes for triggering conditions: **ALL** or **ANY**. The ALL mode requires all conditions to be met for activation, while the ANY mode takes effect when any conditions are met. Note that both modes cannot be used simultaneously in a single alert policy.

Users can choose the severity of alerts (High, Medium, Low) and set the check interval for the alert policy. The severity level will be included in the alert notification, but it does not affect the alert strategy or rule settings in API7 Enterprise. The minimum check interval is `1` minute, meaning that alert notifications for an event will be sent to designated contact points every minute after it takes effect.

Notifications can be sent via **Email** or **Webhook**. Users can flexibly customize notification content using [variables and templates](https://docs.api7.ai/enterprise/reference/alert-template) and integrate with various systems.

It is recommended to add the alert policy name `{{ .AlertPolicyName }}` and description `{{ .Description }}` in the notification to help identify which policy triggered the alert.

Multiple contact points can be configured for notifications, such as sending alerts to two emails and three Webhook contact points.

API7 Enterprise's control plane runs a background program that checks all alert policies every minute to see if they meet the trigger conditions and thresholds. If they do, notifications will be sent to the corresponding contact point list.

API7 Enterprise also provides alert logs for saving, viewing, and searching, with logs retained for up to 30 days. These logs record the alert policy configurations and capture the request and response details when delivering notifications for troubleshooting.

## Why Use Contact Points?[â](#why-use-contact-points "Direct link to Why Use Contact Points?")

A **Contact Point** is an organizational-level concept that abstracts the method of notification (Email or Webhook) and which channels (people, Slack, or operations platforms) receive the notifications.

For example, if you configure `tom@acme.com` as a recipient for multiple alert rules in the Alerts module, without contact points, you need to update the email address in every alert policy whenever a change is required. This process is cumbersome and prone to errors. Introducing contact points decouples the alert strategy from the specific notification configuration. For example, you can add an alert policy like `Alert_to_dev_team`, with the contact point `Notify_dev_team_slack` (Webhook type). Even if the URL or authentication token for the contact points changes, the alert policy does not need to be modified. Users need to ensure smooth network connectivity between the control plane server and contact points. Specifically, if the Email-type contact point is used, users need to pre-configure the SMTP server under the "organization" menu to ensure emails can be sent.

## Use Cases[â](#use-cases "Direct link to Use Cases")

### Data Plane Node Health[â](#data-plane-node-health "Direct link to Data Plane Node Health")

When the number of healthy gateway instances drops below a specified threshold, for example, 3, indicating a possible failure in the API gateway nodes providing external services. This is a high-priority event that requires sending alerts via Slack using Webhook and a set of designated email addresses.

### 5xx Response Code Ratio[â](#5xx-response-code-ratio "Direct link to 5xx Response Code Ratio")

If the proportion of API requests with 5xx response codes exceeds a specified ratio, e.g., 0.2%, it indicates that the API gateway or upstream services may have encountered a failure. This requires timely attention, and alerts should be sent to operations engineers via SMS configured using Webhook.

### SSL Certificate Expiry[â](#ssl-certificate-expiry "Direct link to SSL Certificate Expiry")

Suppose the SSL certificate of a website is about to expire within a certain period, such as 30 days. This indicates the need to rotate the SSL certificate, which is not an urgent task. A Jira task can be triggered to be created via Webhook for operations engineers.
