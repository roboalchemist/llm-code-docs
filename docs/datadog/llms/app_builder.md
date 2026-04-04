# Source: https://docs.datadoghq.com/actions/app_builder.md

---
title: App Builder
description: >-
  Low-code platform for building internal tools with drag-and-drop interface,
  JavaScript support, and integration with external services.
breadcrumbs: Docs > App Builder
---

# App Builder

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Datadog App Builder is a low-code application building platform. It streamlines the development of your internal tools with a user-friendly drag-and-drop interface and built-in support for JavaScript. App Builder integrates with popular services such as AWS and GitHub, allowing you to leverage data and seamlessly connect with external APIs and data stores. By integrating with Datadog's existing capabilities, App Builder provides a centralized context that enables you to take preventive actions or respond to ongoing incidents, all from within the same view that you use for troubleshooting.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/app_builder/app-builder-app.32ab6b92e841b592fd860a13b00df255.png?auto=format"
   alt="An app in App Builder" /%}
An app in App Builder
### Example use cases{% #example-use-cases %}

Below are a few examples of what App Builder apps can do:

- Identify the most likely causes of a regression given a text description of an incident and the most recent 150 commits to a repo.
- Monitor your PagerDuty service status to get complete context while working on incidents.
- Allow users to manage their EC2 instances directly from a dashboard.
- Allow users to explore and view the content of an S3 bucket.
- Use a PagerDuty integration to see who is on-call for each team in an organization.
- Summarize the progress of each PR in a given repo.

## How App Builder works with actions{% #how-app-builder-works-with-actions %}

Datadog App Builder provides an [Action Catalog](https://app.datadoghq.com/actions/action-catalog/) of hundreds of actions across multiple integrations. The Action Catalog and the connection credentials for each integration are shared with [Datadog Workflow Automation](https://docs.datadoghq.com/service_management/workflows/). If there isn't an integration that accomplishes your task, you can use generic actions such as the HTTP requests and JavaScript functions to perform any task that your app requires.

## Take action directly from dashboards{% #take-action-directly-from-dashboards %}

You can use your apps from the Apps page or [access them directly from within your dashboards](https://docs.datadoghq.com/service_management/app_builder/embedded_apps/#add-apps-to-your-dashboard). Datadog Apps function as native dashboard integrations, allowing you to customize and take action on your data straight from your dashboard.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/app_builder/app-builder-embedded-dashboard-2.8db1596fa619f1d28b1a0848f83abbe1.png?auto=format"
   alt="An ECS Task Balancer app embedded in a dashboard, with a cursor clicking the Scale Service button" /%}
An ECS Task Balancer app embedded in a dashboard, with a cursor clicking a button on it
### Apps created by Datadog{% #apps-created-by-datadog %}

Apps created by Datadog are apps that are embedded in Integration dashboards. They work without having to build them; all you need to do is choose a connection.

For example, the [EC2 integration dashboard](https://app.datadoghq.com/dash/integration/60) offers an EC2 instance management app. When you load the dashboard, the app is populated with demo data:

{% image
   source="https://datadog-docs.imgix.net/images/service_management/app_builder/ootb-app-ec2-demo-data.20995179321fcf822bc243897ecab3f1.png?auto=format"
   alt="An EC2 app created by Datadog" /%}
An EC2 app created by Datadog
To use the app with your data, click **+ Connect Data**, then either create a new connection or select an existing one. After you save your selection, the app displays data from your connection.

You can change the selected connection by clicking **Change Connection** in the app.

## App Builder Overview dashboard{% #app-builder-overview-dashboard %}

The App Builder Overview dashboard provides a high-level overview of your Datadog apps. To find the dashboard, go to your [Dashboard list](https://app.datadoghq.com/dashboard/lists) and search for `App Builder Overview`.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/app_builder/app-builder-overview-dashboard-2.43f6aaa5d9094d7b0432db26966fc82f.png?auto=format"
   alt="The App Builder Overview dashboard" /%}
The App Builder Overview dashboard
## Further reading{% #further-reading %}

- [Datadog Cloud SIEM: Driving innovation in security operations](https://www.datadoghq.com/blog/cloud-siem-enterprise-security)
- [Action Catalog](https://docs.datadoghq.com/actions/actions_catalog/)
- [Build custom monitoring and remediation tools with the Datadog App Builder](https://www.datadoghq.com/blog/datadog-app-builder-low-code-internal-tools/)
- [Remediate apps built using Datadog App Builder](https://www.datadoghq.com/blog/app-builder-remediation/)
- [Build Datadog workflows and apps in minutes with our AI assistant](https://www.datadoghq.com/blog/ai-assistant-workflows-apps/)
- [How we created a single app to automate repetitive tasks with Datadog Workflow Automation, Datastore, and App Builder](https://www.datadoghq.com/blog/pm-app-automation/)
- [Getting Started with App Builder](https://learn.datadoghq.com/courses/getting-started-app-builder/)
- [Build custom apps in seconds with conversational AI in App Builder](https://www.datadoghq.com/blog/generate-apps-with-ai/)

Do you have questions or feedback? Join the **#app-builder** channel on the [Datadog Community Slack](https://chat.datadoghq.com/).
