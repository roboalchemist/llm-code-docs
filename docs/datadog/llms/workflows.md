# Source: https://docs.datadoghq.com/actions/workflows.md

---
title: Workflow Automation
description: >-
  Orchestrate and automate end-to-end processes with workflows that connect
  actions across your infrastructure and tools.
breadcrumbs: Docs > Workflow Automation
---

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

Datadog Workflow Automation allows you to orchestrate and automate your end-to-end processes. Build workflows made up of [actions](https://docs.datadoghq.com/actions/actions_catalog/) that connect to your infrastructure and tools. These actions can also perform data and logical operations, allowing you to build complex flows with branches, decisions, and data operations.

## Configure workflow actions{% #configure-workflow-actions %}

Datadog Workflow Automation provides over 2000+ actions across several tools, along with Workflow-specific actions such as the HTTP action and the JavaScript data operator. These actions allow you to perform any task required in your flow.

## Start with blueprints{% #start-with-blueprints %}

Datadog provides you with preconfigured flows in the form of out of the box [blueprints](https://docs.datadoghq.com/workflows/build/#build-a-workflow-from-a-blueprint). Dozens of blueprints help you build processes around incident management, DevOps, change management, security, and remediation.

## Automate critical tasks{% #automate-critical-tasks %}

Trigger your workflows from monitors, security signals, or dashboards, or trigger them manually. This flexibility allows you to respond with the appropriate workflow at the point you become aware of an issue affecting the health of your system. Automating critical tasks with Datadog Workflow Automation helps keep your systems up and running by improving the time to resolution and reducing the possibility of errors.

## Workflows Overview dashboard{% #workflows-overview-dashboard %}

The Workflows Overview dashboard provides a high-level overview of your Datadog workflows and executions. To find the dashboard, go to your [Dashboard list](https://app.datadoghq.com/dashboard/lists) and search for `Workflows Overview`.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/workflows/workflows-dashboard.e556f0639a5fe440cf008dd9c3f2d176.png?auto=format"
   alt="The Workflows Overview dashboard" /%}

## Examples{% #examples %}

Below are a few examples of workflows you can build:

- Automate scaling of your AWS Auto Scaling Groups when monitors tracking critical metrics of these Auto Scaling Groups go into the alert state.
- Automatically create investigative notebooks of malicious IPs to be detected by Security Signals, and then block these IPs in CloudFlare with the click of a button.
- Execute workflows to roll back to stable versions of your application directly from the Dashboards you use to track the health of your systems.
- Manage feature flags by automatically updating your feature flag config files in GitHub and automating the pull request and merge process.

## Further reading{% #further-reading %}

- [Turn feedback into action across your engineering org with Datadog Forms](https://www.datadoghq.com/blog/datadog-forms)
- [Getting Started with Workflow Automation](https://docs.datadoghq.com/getting_started/workflow_automation/)
- [Automate end-to-end processes and quickly respond to events with Datadog Workflows](https://www.datadoghq.com/blog/automate-end-to-end-processes-with-datadog-workflows/)
- [Automate common security tasks and stay ahead of threats with Datadog Workflows and Cloud SIEM](https://www.datadoghq.com/blog/automate-security-tasks-with-workflows-and-cloud-siem/)
- [Automate identity protection, threat containment, and threat intelligence with Datadog SOAR workflows](https://www.datadoghq.com/blog/soar/)
- [Quickly remediate issues in your Azure applications with Datadog Workflow Automation](https://www.datadoghq.com/blog/azure-workflow-automation/)
- [Build Datadog workflows and apps in minutes with our AI assistant](https://www.datadoghq.com/blog/ai-assistant-workflows-apps/)
- [How we created a single app to automate repetitive tasks with Datadog Workflow Automation, Datastore, and App Builder](https://www.datadoghq.com/blog/pm-app-automation/)
- [Automating Meaningful Actions with Datadog Workflow Automation](https://learn.datadoghq.com/courses/automating-meaningful-actions)
- [Introducing Datadog Agent Builder: Build agentic workflows for alert response and remediation](https://www.datadoghq.com/blog/datadog-agent-builder/)

Do you have questions or feedback? Join the **#workflows** channel on the [Datadog Community Slack](https://chat.datadoghq.com/).
