# Source: https://firebase.google.com/docs/firestore/monitor-usage.md.txt

# Source: https://firebase.google.com/docs/database/usage/monitor-usage.md.txt

<br />

As part of managing your Firebase projects, you'll want to review the resource usage of yourRealtime Database(for example, how many users are connected, how much storage your database uses) and how that usage is affecting your bill.

To review yourRealtime Databasebilled usage, check the[*Usage and Billing*dashboard](https://console.firebase.google.com/project/_/usage). For more information about billing, see[UnderstandRealtime Databasebilling](https://firebase.google.com/docs/database/usage/billing).

For resource usage, both the[**Usage** tab in theFirebaseconsole](https://firebase.google.com/docs/database/usage/monitor-usage#firebase_console)and the[metrics available throughCloud Monitoring](https://firebase.google.com/docs/database/usage/monitor-usage#cloud-monitoring)can help you monitorRealtime Databaseusage.

## Receive Firebase alerts

You can choose to receive email alerts when yourRealtime Databaseusage is approaching one of the limits for your pricing plan. By default, Firebase sends email alerts when you've reached or exceeded a plan limit, but you can opt-in to these earlier notifications to adjust your plan or usage and avoid any service disruptions.

These Firebase alerts and their settings are project-wide. This means that, by default, every project member with the[required permissions to receive alerts](https://support.google.com/firebase/answer/7276542#required-permissions-roles)will get an email when aRealtime Databasealert is triggered. Emails are sent to individual email addresses (not to groupings of accounts like Google groups or Google Workspace accounts).

#### Turn on/off alerts for your own account

For your own account, you can turn on/offRealtime Databasealerts without affecting other project members. Note that you still need the required permissions to receive alerts.

To turnRealtime Databasealerts on or off, follow these steps:

1. In theFirebaseconsole, in the top right-corner, go tonotifications*Firebase alerts*.
2. Then, go tosettings*Settings*and set your account preference forRealtime Databasealerts.

## Monitor usage in theFirebaseconsole

To see your currentRealtime Databaseconnections and data usage, check the[Usage](https://console.firebase.google.com/project/_/database/usage/current-billing/)tab in theFirebaseconsole. You can check usage over the current billing period, the last 30 days, or the last 24 hours.

Firebase shows usage statistics for the following metrics:

- **Connections:**The number of simultaneous, currently open, realtime connections to your database. This includes the following realtime connections: WebSocket, long polling, and HTML server-sent events. It does not include RESTful requests.
- **Storage:**How much data is stored in your database. This doesn't include Firebase hosting or data stored through other Firebase products.
- **Downloads:**All bytes downloaded from your database, including protocol and encryption overhead.
- **Load:**This graph shows how much of your database is in use, processing requests, over a given 1-minute interval. You might see performance issues as your database approaches 100%.

| **Note:** As a result of how the dashboard computes usage, the numbers reported can differ slightly from billing reports. The billing reports are the final usage numbers.

![The Rules tab for Realtime Database in the Firebase console.](https://firebase.google.com/docs/database/usage/images/database-usage-console-view.png)

Additionally, theFirebaseconsole provides aFirebase Security Rulesevaluation dashboard, a useful, at-a-glance view of rules invocations. You can also monitorFirebase Security Rulesusage through[Cloud Monitoring](https://firebase.google.com/docs/firestore/monitor-usage#cloud-monitoring). This provides the same rule evaluation metrics, along with the ability to build custom dashboards, analyze trends, and configure alerts (for example, when denied requests spike). See the[Cloud Monitoringmetrics reference](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-firestore)for the complete list of available metrics.

For more information see[Monitor Security Rules inCloud Monitoring](https://firebase.google.com/docs/database/usage/monitor-performance#monitor_security_rules_in).

![The Usage tab for Realtime Database in the Firebase console.](https://firebase.google.com/docs/database/usage/images/database_rules_monitor.png)

## Monitor usage withCloud Monitoring

### Usage metrics

To useCloud Monitoringto monitor your billed usage, track the following metrics. Note all metric type names are prefixed with`firebasedatabase.googleapis.com/`.

|              Metric Name              |                                                                                                                                                                                                                                                                                                                                                                                                                          Description                                                                                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sent Payload Byte Count               | `network/sent_payload_bytes_count`. This metric reflects the size of the data requested through database operations (including gets, queries, writes, realtime listener updates, and broadcasts). It does not include any connection overhead (protocol or encryption). The \`sent_payload_bytes_count\` contributes to your outgoing bandwidth costs, but it doesn't account for the total billed costs. It's an estimate of the data sent from your database in response to requests, but, since it measures the payload size of the data requested, not the data actually sent, it may not always be accurate.                                                                                                                                                                                                                                             |
| Sent Payload and Protocol Bytes Count | `network/sent_payload_and_protocol_bytes_count`. This metric reflects the size of both the payload data described above and the protocol overhead necessitated by the connection (for example, HTTP headers, WebSocket frames, and Firebase realtime protocol frames). It doesn't account for encryption costs on secure connections.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Sent Bytes Count                      | `network/sent_bytes_count`. This metric reflects an estimate of the total size of data sent out from your database through reads. It includes the payload data that is actually sent to clients, in addition to the protocol and encryption overhead that results in connection costs. This most accurately reflects the total outgoing bandwidth on yourRealtime Databasebill.In rare cases, the`sent_bytes_count`might be lower than the`sent_payload_bytes_count`. This typically happens if the size of the data requested doesn't match the size of the data that was actually sent from the database. For example, if a client requests a data payload, but the connection times out before all the data was sent, the resulting`sent_bytes_count`is lower than the`sent_payload_bytes_count`because not all of the data requested was ultimately sent. |
| Total Bytes                           | `storage/total_bytes`. Use this metric to monitor how much data you're storing in your database. Data you store inRealtime Databasecontributes to your billing costs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

Combine metrics in charts on your dashboard for helpful insights and overviews. For example, try the following combinations:

- **Outgoing data:** Use the`network/sent_bytes_count`,`network/sent_payload_and_protocol_bytes_count`, and`network/sent_payload_bytes_count`metrics to spot potential issues with protocol or encryption overhead contributing to unexpected costs on your bill. If you see a large discrepancy between the size of the data payloads requested and the other metrics reflecting connection overhead, you might want to troubleshoot issues that might be leading to timeouts or frequent connections. If you're not using[TLS session tickets](https://tools.ietf.org/html/rfc5077), you might try implementing them to reduce SSL connection overhead for resumed connections.
- **Operations:** Use the`io/database_load`metric to see how much of your total database load is used by each operation type. Make sure to group`io/database_load`by type to troubleshoot different operation types.
- **Storage:** Use the`storage/limit`and`storage/total_bytes`to monitor your storage utilization in relation to theRealtime Databasestorage limits.If you're on the Blaze pricing plan, you aren't subject to storage limits, so you might prefer to monitor the total size of data stored in your database alone through`storage/total_bytes`.

See the[full list ofRealtime Databasemetrics available throughCloud Monitoring](https://cloud.google.com/monitoring/api/metrics_gcp_d_h#gcp-firebasedatabase).

### Create a Cloud Monitoring workspace

To monitorRealtime Databasewith Cloud Monitoring, you must set up a workspace for your project. A workspace organizes monitoring information from one or more projects. After setting up a workspace, you can create custom dashboards and alerting policies.

1. [Open the Cloud Monitoring Page](https://console.cloud.google.com/monitoring/)

   If your project is already part of a workspace, the Cloud Monitoring Page opens. Otherwise, select a workspace for your project.
2. Select the**New Workspace**option or select an existing workspace.

3. Click**Add**. After your workspace builds, the Cloud Monitoring Page opens.

### Create a dashboard and add a chart

Display theRealtime Databasemetrics collected from Cloud Monitoring in your own charts and dashboards.

Before you proceed, make sure your project is part of a[Cloud Monitoring workspace](https://firebase.google.com/docs/database/usage/monitor-usage#stackdriver-setup).

1. In the Cloud Monitoring Page, open your workspace and go to the**Dashboards**page.

   [Go to the Dashboards page](https://console.cloud.google.com/monitoring/dashboards)
2. Click**Create Dashboard**and enter a dashboard name.

3. In the upper-right hand corner, click**Add Chart**.

4. In the**Add Chart** window, enter a chart title. Click the**Metric**tab.

5. In the**Find resource type and metric** field, enter**Firebase Realtime Database** . From the auto-populated dropdown, select one of theRealtime Databasemetrics..

6. To add more metrics to the same chart, click**Add Metric**and repeat the previous step.

7. Optionally, tailor your chart as needed. For example, in the**Filter** field, click**+ Add a filter**. Scroll down, then select a value or range for the metric of interest you wish to filter the chart on.

8. Click**Save**.

For more on Cloud Monitoring charts, see[Working with charts](https://cloud.google.com/monitoring/charts/).

### Create an alerting policy

You can create an alerting policy based on theRealtime Databasemetrics. Follow the steps below can create an alerting policy that emails you whenever a specificRealtime Databasemetric meets a certain threshold.

Before you proceed, make sure your project is part of a[Cloud Monitoring workspace](https://firebase.google.com/docs/database/usage/monitor-usage#stackdriver-setup).

1. In the Cloud Monitoring Page, open your workspace, and go to the**Alerting**page.

   [Go to the Create New Alerting Policy page](https://console.cloud.google.com/monitoring/alerting)
2. Click**Create Policy**.

3. Enter a name for your alerting policy.

4. Add an alerting condition based on one of theRealtime Databasemetrics. Click**Add Condition**.

5. Select a**Target** . In the**Find resource type and metric** field, enter**Realtime Database** . From the auto-populated dropdown, select one of theRealtime Databasemetrics.

6. Under**Policy triggers**, use the dropdown fields to define your alerting condition.

7. Add a notification channel to your alerting policy. Under**Notifications** , Click**Add Notification Channel** . Select**Email**from the dropdown menu.

8. Enter your email in the**Email address** field. Click**Add**.

9. Optionally, fill out the documentation field to include additional information in your email notification.

10. Click**Save**.

If yourRealtime Databaseusage exceeds the configured threshold, you will receive an email alert.

For more on alerting policies, see[Introduction to alerting](https://cloud.google.com/monitoring/alerts/).

## What's next

- [Learn more aboutCloud Monitoring.](https://cloud.google.com/monitoring/docs/)