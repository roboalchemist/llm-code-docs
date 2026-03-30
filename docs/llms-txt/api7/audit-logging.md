# Source: https://docs.api7.ai/enterprise/getting-started/audit-logging.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/getting-started/audit-logging.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/getting-started/audit-logging.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/getting-started/audit-logging.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/getting-started/audit-logging.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/getting-started/audit-logging.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/getting-started/audit-logging.md

# Source: https://docs.api7.ai/enterprise/3.8.x/getting-started/audit-logging.md

# Source: https://docs.api7.ai/enterprise/3.7.x/getting-started/audit-logging.md

# Source: https://docs.api7.ai/enterprise/3.6.x/getting-started/audit-logging.md

# Source: https://docs.api7.ai/enterprise/3.5.x/getting-started/audit-logging.md

# Source: https://docs.api7.ai/enterprise/3.4.x/getting-started/audit-logging.md

# Source: https://docs.api7.ai/enterprise/3.3.x/getting-started/audit-logging.md

# Track Operator Activities Using Audit Logging

API7 Enterprise provides an audit logging feature to monitor and record user activities within API7 Enterprise, including all operations during user logins to the dashboard and API/ADC calls. API7 Enterprise uses tokens as credentials to authenticate users or applications. At the same time, the audit logs capture all token-related authentication and authorization actions, complementing the token mechanism and providing robust security for the platform.

All API call operations generate corresponding audit logs. Users with permission to view and download audit logs can access detailed information and export the logs in JSON or csv format for further analysis. Each audit log includes the operation time, operator, event type, resource ID and name, operator's IP address, and source of the operation.

API7 Enterprise has implemented strict data masking mechanisms to protect sensitive information within the logs. Additionally, these audit logs are retained for 180 days by default to meet compliance requirements. Through the audit logging feature, users can comprehensively understand the usage of API7 Enterprise, promptly identify and address potential security threats, and effectively enhance the platform's security and compliance.

## Background[â](#background "Direct link to Background")

With the increasing frequency of API interface calls and system operations, the lack of effective monitoring and recording mechanisms can lead to security risks and operational hazards. Many industries face compliance management requirements, necessitating detailed recording and auditing of critical operations.

Audit logs can detail various user actions, enabling enterprises to promptly detect anomalies and quickly pinpoint issues, allowing for timely security measures and reducing security risks. Furthermore, detailed recording and auditing of critical operations provide a basis for subsequent compliance audits.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. Install [API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).

2. Prepare an account with `super admin` permissions or an account with the permissions to view or download audit logs.

## Use Case 1: Audit Logs of Services Created within 30 Days[â](#use-case-1-audit-logs-of-services-created-within-30-days "Direct link to Use Case 1: Audit Logs of Services Created within 30 Days")

1. Navigate to the **Audit** module under the **Organization** category.

2. Select `Add Service` in the **Event** filter, choose the corresponding user (e.g., `Ops`).

3. Set the **Date Range** to `30 days` at the top to display all logs of service creation by the `Ops` user within the last 30 days.

4. Click **Search**.

5. Click **Detail** to view the operation logs of the corresponding events. Each log includes "Time", "Operator", "Event", "Resource ID", "Resource Name", "IP Address", and "Source".

6. Click **Export** and select "JSON" or "csv" format to download the logs.

Below is an interactive demo for this use case. Click and follow the steps in this demo, you will better understand how to use it in API7 Enterprise.

## Use Case 2: Audit Logs of `httpbin` Service within 7 Days[â](#use-case-2-audit-logs-of-httpbin-service-within-7-days "Direct link to use-case-2-audit-logs-of-httpbin-service-within-7-days")

1. Copy the service ID of the `httpbin` service: `fb2a549b-f5a8-46ee-b9c6-b0cc167ec5ae`.

2. Navigate to the **Audit** module under the **Organization** category, and paste the copied service ID into the **Resource ID** field.

3. Set the **Date Range** to `7 Days` at the top to display all logs of the `httpbin` service within the last 7 days.

4. Click **Search**.

5. Click **Detail** to view the operation logs of the corresponding events. Each log entry includes "Time", "Operator", "Event", "Resource ID", "Resource Name", "IP Address" and "Source".

6. Click **Export** and select "JSON" or "csv" format to download the logs.

Below is an interactive demo for this use case. Click and follow the steps in this demo, you will better understand how to use it in API7 Enterprise.

## Analyze Logs[â](#analyze-logs "Direct link to Analyze Logs")

Besides basic querying and filtering capabilities, API7 Enterprise also supports exporting audit logs as JSON or csv files. It is recommended to import these data into specialized analysis platforms, such as the ELK Stack (Elasticsearch, Logstash, Kibana), for further analysis and processing, such as data mining and visualization.

## Conclusion[â](#conclusion "Direct link to Conclusion")

The audit logging feature of API7 Enterprise provides comprehensive log records and real-time analysis capabilities, helping administrators quickly locate the root cause of issues and take appropriate corrective actions. Additionally, this feature strongly supports the enterprise's information security and compliance management.
