# Source: https://doc.keepnetlabs.com/next-generation-product/getting-started/7.-incident-responder-setup/step-2.-mail-configurations.md

# Step 2. Mail Configurations

This article section describes how to integrate the [Incident Responder](https://keepnetlabs.com/products/incident-responder) module with Google Workspace, Exchange, or Microsoft Office 365 email services. It's important to follow the steps accurately. Please contact your email server administrator if you don’t have the required permissions to make these configurations.

## Benefit of Email Server Integration

The Incident Responder module investigation tool can detect malicious emails in user inboxes and remove them automatically or can be removed by the admin as well.

Server-based integration with your email service provides the most comprehensive protection. While email investigations can be conducted with the Phishing Reporter plug-in, the user must have Outlook open and the plug-in active for the investigation to be successful. If the Outlook application is closed for any reason, a complete investigation can only be performed using a server-based integration.

The server-based integration has the advantage to start an investigation at any time.

## **Mail Configurations**

Select **Incident Responder > Mail Configurations** from the left sidebar menu of the dashboard to create a new mail configuration or view the details of an existing configuration.

To set initial configurations, select the appropriate email server integration:

* ​Office 365
* Exchange
* Google Workspace

The integration details are:

<table><thead><tr><th width="154.20164126611957"></th><th width="581.1428571428571"></th></tr></thead><tbody><tr><td>Name</td><td>Name of the configuration</td></tr><tr><td>Platform</td><td>Email service name to be integrated: Exchange EWS, Office 365, or Google Workspace</td></tr><tr><td>E-Mail</td><td>An active email address is required for testing purposes</td></tr><tr><td>Status</td><td>Status of the configuration: (running/not running)</td></tr><tr><td>Date Created</td><td>Integration start date</td></tr><tr><td>Action</td><td>Edit/remove the integration</td></tr></tbody></table>

## Shortcuts

* [How to integrate with Microsoft 365](https://doc.keepnetlabs.com/next-generation-product/getting-started/7.-incident-responder-setup/step-2.-mail-configurations/microsoft-365)
* [How to integrate with Google Workspace](https://doc.keepnetlabs.com/next-generation-product/getting-started/7.-incident-responder-setup/step-2.-mail-configurations/google-workspace-gsuite)
* [How to integrate with Exchange](https://doc.keepnetlabs.com/next-generation-product/getting-started/7.-incident-responder-setup/step-2.-mail-configurations/exchange-ews)
