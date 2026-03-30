# Source: https://docs.ox.security/automate-with-ox-workflows/creating-a-workflow/workflow-actions.md

# Workflow Actions

Actions define what happens when a workflow is triggered and all conditions are met. Actions can range from sending a notification, opening a ticket, to setting an SLA. Actions are how workflows translate security intelligence into operational response.

to check the AI

| **Action**                 | **Category**   | **Description (if known)**                  |
| -------------------------- | -------------- | ------------------------------------------- |
| Azure Boards               | Ticketing      | Create or update work items in Azure Boards |
| Asana                      | Ticketing      | Create tasks in Asana                       |
| ServiceNow                 | Ticketing      | Open incidents or tickets in ServiceNow     |
| Monday                     | Ticketing      | Create/update items in Monday.com           |
| Github Issues              | Ticketing      | Open issues in GitHub repository            |
| Logz.io                    | SIEM & Logging | Send logs or alerts to Logz.io              |
| Splunk                     | SIEM & Logging | Send logs or events to Splunk               |
| Block Pipeline             | Pipeline       | Prevent pipeline execution                  |
| Alert Pipeline             | Pipeline       | Send alert within the pipeline process      |
| Set SLA                    | SLA            | Define a custom SLA for the issue           |
| Reset Severity             |                | Reset the severity level to default         |
| Increase/Decrease Severity | SLA            | Adjust severity level based on logic        |
| Slack                      | Notification   | Send notification to Slack channel          |
| Email                      | Notification   | Send email notification                     |
| Teams                      | Notification   | Send message to Microsoft Teams             |
| Webhook                    | Notification   | Trigger custom webhook                      |
| Zapier                     | Notification   | Trigger automated workflows via Zapier      |
| Open PR                    | Remediation    | Open a pull/merge request with the fix      |
| Jira                       | Ticketing      | Open ticket in Jira                         |
| Jira Comment               | Ticketing      | Add comment to an existing Jira ticket      |
