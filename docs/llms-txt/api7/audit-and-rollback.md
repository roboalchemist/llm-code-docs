# Source: https://docs.api7.ai/apisix/enterprise-feature/audit-and-rollback.md

# Audit and Rollback

As the frequency of API calls and system operations increases, the lack of effective monitoring and recording mechanisms can lead to security risks and operational hazards. Many industries face compliance management requirements, necessitating detailed recording and auditing of critical operations.

API7 Enterprise provides the audit logging feature to monitor and record user activities within API7 Enterprise, including all operations during user logins to the dashboard and API/ADC calls. API7 Enterprise uses tokens as credentials to authenticate users or applications while the audit logs capture all token-related authentication and authorization actions.

## How Audit and Rollback Work[â](#how-audit-and-rollback-work "Direct link to How Audit and Rollback Work")

All user actions within API7 Enterprise will be recorded. Any additional alteration to audit logs is forbidden, which can ensure data authenticity.

All API calls generate corresponding audit logs. Each audit log includes the operation time, operator, event type, resource ID and name, operator's IP address, and source of the operation.

Users with permission to view and download audit logs, such as auditors, can access detailed information and export the logs in JSON or CSV format for further analysis.

Furthermore, API7 Enterprise has implemented strict data masking mechanisms to protect sensitive information within the logs. Additionally, these audit logs are retained for 180 days by default to meet compliance requirements.

Through the audit logging feature, users can promptly identify and address potential security threats, and effectively enhance the platform's security and compliance.

## Key Features[â](#key-features "Direct link to Key Features")

* Monitor and log all activities and user actions that are immutable, ensuring data integrity.
* Implement fine-grained audit log access control, ensuring only authorized administrators can view logs or perform rollbacks.
* The rollback feature ensures data consistency and transaction integrity, minimizing manual intervention and reducing recovery time.
* Audit logs are retained for 180 days for archival and backup purposes, ensuring compliance with auditing and regulatory requirements.

## Use Cases[â](#use-cases "Direct link to Use Cases")

### Real-Time Detection and Recording[â](#real-time-detection-and-recording "Direct link to Real-Time Detection and Recording")

Consider a scenario where a user mistakenly configures a new API service, leading to service disruption. In this case, the audit logging feature in API7 Enterprise captures the action in real-time, documenting every modification made to the API gateway configuration.

When auditors log into the system and review the audit logs, they can quickly identify any anomalies or misconfigurations that contributed to the disruption. The audit logging feature enables them to pinpoint issues promptly and take corrective action before any significant damage occurs. The real-time detection and recording of such events provide a proactive approach to managing security and operational risks.

### Rollback for Swift Restoration[â](#rollback-for-swift-restoration "Direct link to Rollback for Swift Restoration")

In the case of a service disruption caused by a misconfigured API service, internal auditors or system administrators can leverage the audit logging feature within API7 Enterprise to quickly trace and investigate the root cause. Once the issue is localized, the rollback feature in API7 Enterprise allows administrators to restore the system to a stable state by reverting the service to its prior configuration.

The rollback capability is particularly useful in scenarios where multiple changes are made in quick succession, and it is difficult to pinpoint exactly which modification caused the problem. In such cases, administrators can perform a rollback based on the resource ID, enabling them to specifically undo changes made to the affected resource. By allowing precise rollbacks, API7 Enterprise facilitates efficient troubleshooting and minimizes the risk of operational disruption.

### Post-Event Audit Logs Analysis[â](#post-event-audit-logs-analysis "Direct link to Post-Event Audit Logs Analysis")

The detailed recording and auditing of critical operations provide a basis for subsequent compliance audits. These logs offer insights into user actions, system changes, and potential security incidents, making them invaluable for assessing adherence to security policies and regulatory requirements.

Through post-event analysis, administrators can easily and efficiently conduct targeted security audits on information systems. Moreover, the insights gained from post-event audits not only help in immediate issue resolution but also inform future policy adjustments and improvements. This makes audit logs a cornerstone for continuous security monitoring, risk management, and regulatory compliance.
