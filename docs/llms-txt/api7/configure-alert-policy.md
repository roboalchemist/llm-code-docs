# Source: https://docs.api7.ai/cloud/guides/alert/configure-alert-policy.md

# Configure Alert Policy

A running system will not always be healthy. When something goes wrong, you need to be notified immediately. API7 Cloud provides a powerful alerting system to help you monitor your system and get notified when something goes wrong. That is why API7 Cloud provides a powerful alerting system to help you monitor your system and get notified when something goes wrong.

This guide will show you how to configure an alert policy.

## What Is Alert Policy[â](#what-is-alert-policy "Direct link to What Is Alert Policy")

An alert policy indicates the conditions under which an alert will be triggered. When the conditions are met, the alert will be triggered and it also indicates how you will receive the notification. In a nutshell, an alert policy is composed of the following parts:

1. Alert policy basic information like the alert message and alert title.
2. The trigger conditions.
3. The notification method, currently, only webhook is supported.

## Create an Alert Policy[â](#create-an-alert-policy "Direct link to Create an Alert Policy")

To create an alert policy, do the following:

1. Open the [API7 Cloud console](https://console.api7.cloud).

2. From the left navigation bar, choose **Alert Management**, then select **Alert Policies** from the secondary menu.

3. Click on the **Create Alert Policy** button.

4. Input the basic information of the alert policy.

   <!-- -->

   1. Input the alert policy name (be careful, it is not identical with the alert title).
   2. Input the alert policy description.

Please note a just created alert policy is not enabled by default. To enable an alert policy, do the following steps:

1. From the left navigation bar, choose **Alert Management**, then select **Alert Policies** from the secondary menu.
2. Search for the alert policy you want to enable (you can search by the alert policy name).
3. Click on the **On** button to enable the alert policy
   <!-- -->
   1. For an enabled alert policy, the button will be **Off**. Which means you can disable the alert policy.

### Configure the Trigger Conditions[â](#configure-the-trigger-conditions "Direct link to Configure the Trigger Conditions")

Trigger conditions in an alert policy control which time the alert will be triggered. A condition will contain three parts:

1. The event, e.g., `Gateway instance offline`, `Gateway certificate expire`.
2. The comparison operator, e.g., `>=`, `<=`.
3. The time duration, e.g., `5min`. `10s`.

The following table lists all the supported events.

| Event                              | Description                                                                                         |
| ---------------------------------- | --------------------------------------------------------------------------------------------------- |
| `Gateway instance offline`         | The gateway instance is offline                                                                     |
| `Gateway certificate expire`       | User uploaded certificate will expire soon                                                          |
| `Control Plane certificate expire` | The certificate that this gateway instance used for communicating with API7 Cloud will expire soon. |
| `Number of status code 5xx`        | The number of HTTP status codes `5XX`                                                               |
| `Number of status code 4xx`        | The number of HTTP status codes `4XX`                                                               |
| `Ratio of status code 5xx`         | The ratio of HTTP status codes `5XX`                                                                |
| `Ratio of status code 4xx`         | The ratio of HTTP status codes `4XX`                                                                |

tip

For events like `Number of status code 5xx`, you'll asked to input some complementary information to indicate the threshold.

### Configure the Webhook Notification[â](#configure-the-webhook-notification "Direct link to Configure the Webhook Notification")

You need to prepare a channel for receiving the alert notification. Currently, only HTTP webhook is supported. To configure the webhook notification, do the following:

1. Open the [API7 Cloud console](https://console.api7.cloud).

2. From the left navigation bar, choose **Alert Management**, then select **Alert Policies** from the secondary menu.

3. Search the alert policy that you want to configure the webhook notification.

4. On the alert policy detail page, click on the **Create Webhook Notification** button.

   <!-- -->

   1. Input the webhook name, description
   2. Input the Webhook URL
   3. Most importantly, input the message template. This is [Go template](https://pkg.go.dev/text/template) based.

You can use the following template variables in the message template:

| Variable Name        | Description                                                                                                                                                  |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `{{ .Title }}`       | The alert title                                                                                                                                              |
| `{{ .AlertTime }}`   | The alert trigger time                                                                                                                                       |
| `{{ .AlertTime }}`   | The alert trigger time, it is `time.Time` object, please use `.AlertTime.Format` to format the time, e.g., `{{ .AlertTime.Format "2006 Jan 02 15:04:05" }}`. |
| `{{ .AlertEvents }}` | The alert events map, it is `map` object, please use the event name to index it, e.g., `{{ .AlertEvents["gateway_instance_offline"] }}`                      |

tip

Some other tips for the webhook:

1. You can also configure some extra HTTP headers for the webhook notification.
2. If the certificate is not valid for your webhook server, skipping the TLS verify.
3. The HTTP method for sending alert message is `POST`.

tip

Candidates of the event name for `{{ .AlertEvents }}`:

1. `number_of_status_code`
2. `ratio_of_status_code`
3. `control_plane_certificate_will_expire_in`
4. `control_plane_certificate_will_expire_in`
5. `gateway_certificate_will_expire_in`
6. `gateway_instance_offline`

After you configure an alert policy and make it enabled, you'll receive the alert notification when the alert policy is triggered.
