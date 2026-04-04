# Source: https://docs.api7.ai/enterprise/api-observability/alert.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/api-observability/alert.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/api-observability/alert.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/api-observability/alert.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/api-observability/alert.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/api-observability/alert.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/api-observability/alert.md

# Source: https://docs.api7.ai/enterprise/3.8.x/api-observability/alert.md

# Source: https://docs.api7.ai/enterprise/3.7.x/api-observability/alert.md

# Source: https://docs.api7.ai/enterprise/3.6.x/api-observability/alert.md

# Source: https://docs.api7.ai/enterprise/3.5.x/api-observability/alert.md

# Source: https://docs.api7.ai/enterprise/3.4.x/api-observability/alert.md

# Source: https://docs.api7.ai/enterprise/3.3.x/api-observability/alert.md

# Trigger Gateway Alerts

Abnormal traffic patterns or errors in API Gateway usage can indicate problems or malicious attacks. By setting up alerts for certain thresholds and activities, you can quickly detect and gain insights into patterns that might indicate a security breach, abuse, or abnormal usage.

This tutorial guides you through creating alert policies to receive email and webhook notifications for specific events. Below is an interactive demo providing a hands-on introduction to counting healthy gateway instances in gateway groups scenario.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
2. [Have a running API on the gateway group](https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md).
3. Get the webhook URL of your notification system.

## Set Up SMTP Server[â](#set-up-smtp-server "Direct link to Set Up SMTP Server")

1. Select **Organization** from the top navigation bar, and then select **Settings**.
2. Click the **SMTP Server** tab.
3. Click **Enable**.
4. In the dialog box, do the following:

* In the **SMTP Server Address** field, enter the address of your SMTP server. For example, `127.0.0.1`.
* In the **Username** and **Password** field, enter the credential to connect to your SMTP server.
* In the **From Name** field, enter `API7 Enterprise` to display this name as the sender in the email.
* In the **From Email Address** field, enter `noreply@api7.ai`. This will use as the actual sender address.
* Click **Enable**.

## Add Contact Points[â](#add-contact-points "Direct link to Add Contact Points")

A *Contact Point* defines a set of email addresses or webhook URLs that can be used by multiple alert policies.

### Add a Email Contact Point[â](#add-a-email-contact-point "Direct link to Add a Email Contact Point")

1. Select **Organization** from the top navigation bar, and then select **Contact Points**.
2. Click **Add Contact Points**.
3. In the dialog box, do the following:

* In the **Name** field, enter `Emergency Team Email List`.
* In the **Type** field, choose `Email`.
* In the **Email Addresses** field, enter the email addresses of the recipients, for example, `emergencyteamlist@api7.ai`.
* Click **Add**.

### Add a Webhook Contact Point[â](#add-a-webhook-contact-point "Direct link to Add a Webhook Contact Point")

Use a [Slack incoming webhook](https://api.slack.com/messaging/webhooks) to post messages from API7 Enterprise into Slack.

1. Select **Organization** from the top navigation bar, and then select **Contact Points**.
2. Click **Add Contact Points**.
3. In the dialog box, do the following:

* In the **Name** field, enter `Slack Notification`.
* In the **Type** field, choose `Webhook`.
* In the **URL** field, enter `https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX`. Replace with your IDs.
* Click **Add**.

## Add Essential Alert Polices[â](#add-essential-alert-polices "Direct link to Add Essential Alert Polices")

The following alert policies are strongly recommended for configuration, as they are crucial for most users.

### Monitor Control Plane to Data Plane mTLS Certificate Expiration[â](#monitor-control-plane-to-data-plane-mtls-certificate-expiration "Direct link to Monitor Control Plane to Data Plane mTLS Certificate Expiration")

API7 control plane certificate and API7 control plane CA certificate enable secure mTLS communication between the control plane and data plane, which are activated upon gateway instance deployment. These certificates have a 13-month validity period.

To proactively monitor and alert on expiring certificates on gateway instances, implement a daily task to check certificate expiration dates. If a gateway instance's certificate is nearing expiration (within 30 days), send email alerts to the emergency team and post a notification to Slack.

1. Select **Alert** from the side navigation bar, then click **Policies**.
2. Click **Add Alert Policy**.
3. In the dialog box, do the following:

* In the **Name** field, enter `Gateway Instance Certificate Expired`.

* In the **Severity** field, choose `High`.

* In the **Check Interval** field, enter `1440` minutes.

* In the **Conditions** field, do the following:

  * In the **Operator** field, choose `Meet all of the following conditions(AND)`.
  * In the **Event** field, choose `mTLS certificate between control plane and data plane will expire`.
  * In the **Trigger Gateway Group** field, choose `Select all`.
  * In the **Rule** field, fill in the blanks to `mTLS certificate between data plane and control plane will expire in 30 days`.

* Click **Add Notification**.

* In the dialog box, do the following:

  * In the **Type** field, choose `Email`.
  * In the **Contact Points** field, choose `Emergency Team Email List`.
  * In the **Alert Email Subject** field, enter `[API7 Alert] Gateway Instance Certificate Expiration Warning`.
  * In the **Alert Email Content** field, enter `Alert Time: {{.AlertTime.Format "2006 Jan 02 15:04:05"}}, Detail:{{.AlertDetail}}`.
  * Click **Add**.

* Click **Add Notification**.

* In the dialog box, do the following:

  * In the **Type** field, choose `Webhook`.
  * In the **Contact Points** field, choose `Slack Notification`.
  * In the **Alert Message** field, enter

  ```
   "text": "{{.AlertDetail}}.".
  ```

  * Click **Add**.

5. Click **Add**.

#### Validate[â](#validate "Direct link to Validate")

Imagine a control plane certificate expiring on 2024-12-31. On 2024-12-10, the alert policy triggers:

1. An email of the following:

```
* Subject: [API7 Alert] Gateway Instance Certificate Expiration Warning
* Alert Time: 2024 DEC 10 17:00:00, Detail: Certificate of gateway instance: gateway 123 expires in 21 days.
```

2. A message in Slack:

```
Certificate of gateway instance: gateway 123 expires in 21 days.
```

3. Select **Alert** from the side navigation bar, then click **History**.
4. An alert record corresponding to the event will be displayed. Click **Detail**:

* Alert Policy: Gateway Instance Certificate Expired
* Severity: High
* Alert Time: 5 minutes ago
* Trigger Gateway Group: production group
* Alert Detail: Certificate of gateway instance: gateway 123 expires in 21 days.

### Detect Gateway Instance Offline[â](#detect-gateway-instance-offline "Direct link to Detect Gateway Instance Offline")

If the gateway instance (data plane node) has not reported heartbeat to the control plane for more than 2 hours, and this state persists for 7 days, the data plane node will be automatically removed, and marked `offline`.

Implement a hourly task to detect and send email alerts to the emergency team and Slack notifications in case of issues. Then someone should try to recover offline gateway instances.

1. Select **Alert** from the side navigation bar, then click **Policies**.
2. Click **Add Alert Policy**.
3. In the dialog box, do the following:

* In the **Name** field, enter `Gateway Instance Offline`.

* In the **Severity** field, choose `High`.

* In the **Check Interval** field, enter `60` minutes.

* In the **Conditions** field, do the following:

  * In the **Operator** field, choose `Meet all of the following conditions(AND)`.
  * In the **Event** field, choose `Gateway instance offline`.
  * In the **Trigger Gateway Group** field, choose `Select all`.
  * In the **Rule** field, fill in the blanks to `Any gateway instance in the gateway group offline for more than 1 hour`.

* Click **Add Notification**.

* In the dialog box, do the following:

  * In the **Type** field, choose `Email`.
  * In the **Contact Points** field, choose `Emergency Team Email List`.
  * In the **Alert Email Subject** field, enter `[API7 Alert] Gateway Instance Offline Warning`.
  * In the **Alert Email Content** field, enter `Alert Time: {{.AlertTime.Format "2006 Jan 02 15:04:05"}}, Detail:{{.AlertDetail}}`.
  * Click **Add**.

* Click **Add Notification**.

* In the dialog box, do the following:

  * In the **Type** field, choose `Webhook`.
  * In the **Contact Points** field, choose `Slack Notification`.
  * In the **Alert Message** field, enter

  ```
   "text": "{{.AlertDetail}}".
  ```

  * Click **Add**.

5. Click **Add**.

#### Validate[â](#validate-1 "Direct link to Validate")

Imagine that two gateway instances went offline at 2024-12-31 14:00:00 and 2024-12-31 13:00:00. On 2024-12-31 17:00:00, the alert policy triggers:

1. An email of the following:

```
* Subject: [API7 Alert] Gateway Instance Offline Warning
* Alert Time: 2024 DEC 31 17:00:00, Detail: Gateway instance: gateway 123 in the gateway group: production group offline for 3 hours.\ Gateway instance: gateway 456 in the gateway group: test group offline for 4 hours.
```

2. A message in Slack:

```
Gateway instance: gateway 123 in the gateway group: production group offline for 3 hours
Gateway instance: gateway 456 in the gateway group: test group offline for 4 hours
```

3. A record in the alert history. Select **Alert** from the side navigation bar, then click **History** to see the record.
4. Record details. Clicking into the record **Detail**, you should see:

* Alert Policy: Gateway Instance Offline
* Severity: High
* Alert Time: 5 minutes ago
* Trigger Gateway Group: production group
* Alert Detail: Gateway instance: gateway 123 in the gateway group: production group offline for 3 hours.\ Gateway instance: gateway 456 in the gateway group: test group offline for 4 hours.

### Detect CPU Cores Exceeding Quota[â](#detect-cpu-cores-exceeding-quota "Direct link to Detect CPU Cores Exceeding Quota")

If CPU cores usage of all gateway groups exceeds the licensed CPU core limit for seven consecutive days, resource addition or modification will be restricted. However, existing services and routes will continue to function.

Implement a hourly task to detect all gateway groups for production environments, and send email alerts to the emergency team and Slack notifications in case of issues.

1. Select **Alert** from the side navigation bar, then click **Policies**.
2. Click **Add Alert Policy**.
3. In the dialog box, do the following:

* In the **Name** field, enter `CPU cores Exceeding Quota`.

* In the **Severity** field, choose `High`.

* In the **Check Interval** field, enter `60` minutes.

* In the **Conditions** field, do the following:

  * In the **Operator** field, choose `Meet all of the following conditions(AND)`.
  * In the **Event** field, choose `Allowed License CPU Quota Exceeded`.

* Click **Add Notification**.

* In the dialog box, do the following:

  * In the **Type** field, choose `Email`.
  * In the **Contact Points** field, choose `Emergency Team Email List`.
  * In the **Alert Email Subject** field, enter `[API7 Alert] CPU Cores Exceeding Quota`.
  * In the **Alert Email Content** field, enter `Alert Time: {{.AlertTime.Format "2006 Jan 02 15:04:05"}}, Detail:{{.AlertDetail}}`.
  * Click **Add**.

* Click **Add Notification**.

* In the dialog box, do the following:

  * In the **Type** field, choose `Webhook`.
  * In the **Contact Points** field, choose `Slack Notification`.
  * In the **Alert Message** field, enter

  ```
   "text": "{{.AlertDetail}}".
  ```

  * Click **Add**.

5. Click **Add**.

#### Validate[â](#validate-2 "Direct link to Validate")

Assume that your API7 Enterprise license limit of 100 CPU cores. On 2024-12-31 17:00:00, the alert policy triggers:

1. An email of the following:

```
* Subject: [API7 Alert] CPU Cores Exceeding Quota
* Alert Time: 2024 DEC 31 17:00:00, Detail: Total CPU usage for all gateway groups is 110c, exceeded allowed license CPU quota 100c.
```

2. A message in Slack:

```
Total CPU usage for all gateway groups is 110c, exceeded allowed license CPU quota 100c.
```

3. A record in the alert history. Select **Alert** from the side navigation bar, then click **History** to see the record.
4. Record details. Clicking into the record **Detail**, you should see:

* Alert Policy: CPU Cores Exceeding Quota
* Severity: High
* Alert Time: 5 minutes ago
* Alert Detail: Total CPU usage for all gateway groups is 110c, exceeded allowed license CPU quota 100c.

## More Alert Policy Examples[â](#more-alert-policy-examples "Direct link to More Alert Policy Examples")

### Monitor SSL Certificate Expiration[â](#monitor-ssl-certificate-expiration "Direct link to Monitor SSL Certificate Expiration")

To proactively monitor and alert on expiring SSL certificates, implement a daily task to check certificate expiration dates.

If a certificate is nearing expiration (within 30 days), send email alerts to the emergency team and post a notification to Slack.

1. Select **Alert** from the side navigation bar, then click **Policies**.
2. Click **Add Alert Policy**.
3. In the dialog box, do the following:

* In the **Name** field, enter `SSL Certificate Expired`.

* In the **Severity** field, choose `Medium`.

* In the **Check Interval** field, enter `1440` minutes.

* In the **Conditions** field, do the following:

  * In the **Operator** field, choose `Meet all of the following conditions(AND)`.
  * In the **Event** field, choose `SSL Certitificate will expire`.
  * In the **Trigger Gateway Group** field, choose `Select all`.
  * In the **Rule** field, fill in the blanks to `SSL certificate will expire in 30 days`.

* Click **Add Notification**.

* In the dialog box, do the following:

  * In the **Type** field, choose `Email`.
  * In the **Contact Points** field, choose `Emergency Team Email List`.
  * In the **Alert Email Subject** field, enter `[API7 Alert] SSL Certificate Expiration Warning`.
  * In the **Alert Email Content** field, enter `Alert Time: {{.AlertTime.Format "2006 Jan 02 15:04:05"}}, Detail:{{.AlertDetail}}`.
  * Click **Add**.

* Click **Add Notification**.

* In the dialog box, do the following:

  * In the **Type** field, choose `Webhook`.
  * In the **Contact Points** field, choose `Slack Notification`.
  * In the **Alert Message** field, enter

  ```
   "text": "{{.AlertDetail}}.".
  ```

  * Click **Add**.

5. Click **Add**.

#### Validate[â](#validate-3 "Direct link to Validate")

Suppose that a SSL certificate will expire on 2024-12-31. On 2024-12-10, the alert policy will trigger:

1. An email of the following:

```
* Subject: [API7 Alert]SSL Certificate Expiration Warning
* Alert Time: 2024 DEC 10 17:00:00, Detail: SSL Certificate: sslcert123 in gateway group: production group will expire in 21 days.
```

2. A message in Slack:

```
SSL Certificate: sslcert123 in gateway group: production group will expire in 21 days.
```

3. A record in the alert history. Select **Alert** from the side navigation bar, then click **History** to see the record.
4. Record details. Clicking into the record **Detail**, you should see:

* Alert Policy: SSL Certificate Expired
* Severity: Medium
* Alert Time: 5 minutes ago
* Trigger Gateway Group: production group
* Alert Detail: SSL Certificate: sslcert123 in gateway group: production group will expire in 21 days.

### Count Healthy Gateway Instances in a Gateway Group[â](#count-healthy-gateway-instances-in-a-gateway-group "Direct link to Count Healthy Gateway Instances in a Gateway Group")

If the number of healthy gateway instances in a gateway group falls below a critical threshold, it indicates potential service disruptions and impacts on traffic handling. This scenario is particularly relevant in Kubernetes deployments, where gateway instances may experience failures or be scaled down unexpectedly.

Implement a high frequent task to detect send email alerts to the emergency team and Slack notifications in case of issues.

1. Select **Alert** from the side navigation bar, then click **Policies**.
2. Click **Add Alert Policy**.
3. In the dialog box, do the following:

* In the **Name** field, enter `No Enough Healthy Gateway Instances in Production Group`.

* In the **Severity** field, choose `Medium`.

* In the **Check Interval** field, enter `30` minutes.

* In the **Trigger Gateway Group** field, choose `Production Group`.

* In the **Conditions** field, do the following:

  * In the **Operator** field, choose `Meet all of the following conditions(AND)`.
  * In the **Event** field, choose `Number of healthy gateway instances`.
  * In the **Rule** field, fill in the blanks to `Number of gateway instances in the gateway group is less than 50`.

* Click **Add Notification**.

* In the dialog box, do the following:

  * In the **Type** field, choose `Email`.
  * In the **Contact Points** field, choose `Emergency Team Email List`.
  * In the **Alert Email Subject** field, enter `[API7 Alert] No Enough Healthy Gateway Instances in Production Group`.
  * In the **Alert Email Content** field, enter `Alert Time: {{.AlertTime.Format "2006 Jan 02 15:04:05"}}, Detail:{{.AlertDetail}}`.
  * Click **Add**.

* Click **Add Notification**.

* In the dialog box, do the following:

  * In the **Type** field, choose `Webhook`.
  * In the **Contact Points** field, choose `Slack Notification`.
  * In the **Alert Message** field, enter

  ```
   "text": "{{.AlertDetail}}".
  ```

  * Click **Add**.

5. Click **Add**.

#### Validate[â](#validate-4 "Direct link to Validate")

Assume that your gateway group requires a minimum of 50 healthy gateway instances. However, as of 2024-12-31, only 40 instances are operational. This significant shortfall may lead to service degradation and potential outages. Immediate attention is required to address this issue.

1. An email of the following:

```
* Subject: [API7 Alert] No Enough Healthy Gateway Instances in Production Group
* Alert Time: 2024 DEC 31 17:00:00, Detail: Number of healthy gateway instances in the gateway group: Production Group is 40.
```

2. A message in Slack:

```
Number of healthy gateway instances in the gateway group: Production Group is 40.
```

3. A record in the alert history. Select **Alert** from the side navigation bar, then click **History** to see the record.
4. Record details. Clicking into the record **Detail**, you should see:

* Alert Policy: No Enough Healthy Gateway Instances in Production Group
* Severity: Medium
* Alert Time: 5 minutes ago
* Trigger Gateway Group: Production Group
* Alert Detail: Number of healthy gateway instances in the gateway group: Production Group is 40.

### Monitor Status Code[â](#monitor-status-code "Direct link to Monitor Status Code")

If the number of specific API response status code exceed the threshold, for example, too many 500 error, it indicates potential service disruptions and impacts on traffic handling.

Implement a high frequent task to detect send email alerts to the emergency team and Slack notifications in case of issues.

1. Select **Alert** from the side navigation bar, then click **Policies**.
2. Click **Add Alert Policy**.
3. In the dialog box, do the following:

* In the **Name** field, enter `Too many 500 status code in production gateway groups`.

* In the **Severity** field, choose `Medium`.

* In the **Check Interval** field, enter `30` minutes.

* In the **Trigger Gateway Group** field, select `Match Label` then enter key/value `envType: production`.

* In the **Conditions** field, do the following:

  * In the **Operator** field, choose `Meet all of the following conditions(OR)`.
  * In the **Event** field, choose `Number of status code 500`.
  * In the **Rule** field, fill in the blanks to `Number of requests with status code 500 received by all published services of any one of the gateway groups has reached or exceeded 100 times in the last 60 minutes`.

* Click **Add Condition**.

* In the **Conditions** field, do the following:

  * In the **Event** field, choose `Ratio of status code 500`.
  * In the **Rule** field, fill in the blanks to `Ratio of requests with status code 500 received by all published services of any one of the gateway groups has reached or exceeded 10% in the last 60 minutes`.

* Click **Add Notification**.

* In the dialog box, do the following:

  * In the **Type** field, choose `Email`.
  * In the **Contact Points** field, choose `Emergency Team Email List`.
  * In the **Alert Email Subject** field, enter `[API7 Alert] Too many 500 status code in {{.TriggerGatewayGroup}}`.
  * In the **Alert Email Content** field, enter `Alert Time: {{.AlertTime.Format "2006 Jan 02 15:04:05"}}, Detail:{{.AlertDetail}}`.
  * Click **Add**.

* Click **Add Notification**.

* In the dialog box, do the following:

  * In the **Type** field, choose `Webhook`.
  * In the **Contact Points** field, choose `Slack Notification`.
  * In the **Alert Message** field, enter

  ```
   "text": "{{.AlertDetail}}".
  ```

  * Click **Add**.

5. Click **Add**.

#### Validate[â](#validate-5 "Direct link to Validate")

Assume that your gateway group `VIP Group` has a label `envType:production`, experienced a 15% error rate between 16:00 and 17:00 on December 31, 2024. Out of 1000 requests, 150 resulted in 500 errors. And the gateway group `US Group` has a label `envType:production`, experienced a 10% error rate between 16:00 and 17:00 on December 31, 2024. Out of 500 requests, 50 resulted in 500 errors.

1. An email of the following:

```
* Subject: [API7 Alert] [API7 Alert] Too many 500 status code in VIP Group,US Group
* Alert Time: 2024 DEC 31 17:00:00, Detail:Number of requests with status code 500 received by all published services of the gateway group: VIP Group is 150 times in the last 60 minutes.
Ratio of requests with status code 500 received by all published services of the gateway group: VIP Group is 15% in the last 60 minutes.
Ratio of requests with status code 500 received by all published services of the gateway group: US Group is 10% in the last 60 minutes.
```

2. A message in Slack:

```
Number of requests with status code 500 received by all published services of the gateway group: VIP Group is 150 times in the last 60 minutes.
Ratio of requests with status code 500 received by all published services of the gateway group: VIP Group is 15% in the last 60 minutes.
Ratio of requests with status code 500 received by all published services of the gateway group: US Group is 10% in the last 60 minutes.
```

3. A record in the alert history. Select **Alert** from the side navigation bar, then click **History** to see the record.
4. Record details. Clicking into the record **Detail**, you should see:

* Alert Policy: Too many 500 in production gateway groups
* Severity: Medium
* Alert Time: 5 minutes ago
* Trigger Gateway Group: VIP Group
* Alert Detail: Number of requests with status code 500 received by all published services of the gateway group: VIP Group is 150 times in the last 60 minutes. Ratio of requests with status code 500 received by all published services of the gateway group: VIP Group is 15% in the last 60 minutes. Ratio of requests with status code 500 received by all published services of the gateway group: US Group is 10% in the last 60 minutes.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* References
  <!-- -->
  * [Alert Templates](https://docs.api7.ai/enterprise/3.3.x/reference/alert-template.md)
