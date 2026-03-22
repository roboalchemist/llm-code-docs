# Source: https://docs.rootly.com/integrations/sentry.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Sentry

> Connect Rootly with Sentry to ingest error monitoring issues as alerts and automatically create incidents based on configurable thresholds.

## Why

**Sentry** Integration allows you to:

* Ingest issues as alerts
* Create an incident if alerts > count ( you can specify )

## Installation

As an admin, go to [https://sentry.io/orgredirect/settings/:orgslug/sentry-apps/rootly/](https://sentry.io/orgredirect/settings/:orgslug/sentry-apps/rootly/ "https://sentry.io/orgredirect/settings/:orgslug/sentry-apps/rootly/")﻿

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/6qP0tS1GNk4jbxrs/images/integrations/sentry/images-1.webp?fit=max&auto=format&n=6qP0tS1GNk4jbxrs&q=85&s=f8ca00098f937ecfed09952f57d5877a" width="863" height="338" data-path="images/integrations/sentry/images-1.webp" />
</Frame>

Make sure you are logged in as an admin in Rootly and click on the Rootly app.

## Alerts

Create an Sentry alert and select Rootly as destination.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/6qP0tS1GNk4jbxrs/images/integrations/sentry/images-2.webp?fit=max&auto=format&n=6qP0tS1GNk4jbxrs&q=85&s=caa3fc8d24388d3523ee63728a8f4c3f" width="868" height="749" data-path="images/integrations/sentry/images-2.webp" />
</Frame>

Now your alerts conditions matched, they will be ingested as alerts as shown below. Use it in workflow with fetch alerts task to automatically linked recent alerts to your incident.

[/alert-workflows](/workflows/alert-workflows "/alert-workflows")

**Configure Alert Rules in Sentry:**

* Go to your project in Sentry.
* Navigate to **Alerts** > **Rules**.
* Create a new alert rule or edit an existing one.
* Set the conditions that should trigger an alert (e.g., when a new issue is created or an error frequency increases).
* In the **Actions** section, select **Send a notification via the Rootly integration**.
* Save the alert rule.

**Set Up Alert Workflows in Rootly:**

* In Rootly, navigate to **Workflows** > **Create Workflow**.
* Choose the **Alert** workflow type.
* **Trigger Event:** Select **Alert Created**.
* **Run Conditions:** Define conditions to filter alerts from Sentry, such as:
  * **Source:** Set to **Sentry**.
  * **Labels:** Specify any relevant labels.
  * **Payload:** Use JSON Path to filter specific fields if necessary.
* **Actions:** Add the **Create Incident** action to automatically declare an incident in Rootly when the workflow conditions are met.
* Save the workflow.

**Test the Integration:**

* Trigger an alert in Sentry that meets the conditions you've set.
* Verify that an incident is automatically created in Rootly as configured.

By following these steps, Sentry alerts will seamlessly initiate incidents in Rootly, ensuring prompt attention to critical issues.

[https://docs.sentry.io/organization/integrations/notification-incidents/rootly/](https://docs.sentry.io/organization/integrations/notification-incidents/rootly/ "https://docs.sentry.io/organization/integrations/notification-incidents/rootly/")﻿

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/6qP0tS1GNk4jbxrs/images/integrations/sentry/images-3.webp?fit=max&auto=format&n=6qP0tS1GNk4jbxrs&q=85&s=35baba7ff11649d05f46dee575920b63" width="866" height="375" data-path="images/integrations/sentry/images-3.webp" />
</Frame>

## Uninstall

You can **uninstall** this integration in the integrations panel by clicking **Configure > Delete**


Built with [Mintlify](https://mintlify.com).