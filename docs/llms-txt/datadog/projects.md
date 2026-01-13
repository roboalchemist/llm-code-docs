# Source: https://docs.datadoghq.com/incident_response/case_management/projects.md

---
title: Projects
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Case Management > Projects
source_url: https://docs.datadoghq.com/case_management/projects/index.html
---

# Projects

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

A project is a container object that holds a set of cases. Organize your work around the groups that make sense to your organization, whether that's teams, services, or initiatives. Cases in each project are isolated from one another, helping you to focus on what's relevant.

## Create a project{% #create-a-project %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/case_management/projects/projects_create_a_project_cropped.8ea7c2137622b1ba39b0b89cf2068d0c.png?auto=format"
   alt="Create a new project page under Case management Settings" /%}

To create a project:

1. Select **New Project** on the Projects view or click on the **+** icon next to *Your Projects* in the left navigation bar.
1. Enter a project name and key. Project keys must be between one and 10 characters long. Case ID numbers are prefixed with a combination of letters, for example, `NOC-123`. Project keys are immutable.
1. Click **Create Project**.

## Delete a project{% #delete-a-project %}

{% alert level="danger" %}
Deleted cases cannot be recovered.
{% /alert %}

You can delete a project from a project's Settings page.

Deleting a project also deletes all the cases within it. If you want to keep cases, Datadog recommends moving cases to another project before deleting.

Deleting a project automatically disables any event correlation patterns tied to the project. Other automation, such as case creation through Datadog Workflows or monitor `@case` mentions, also break when you delete the linked project.

## Further Reading{% #further-reading %}

- [Create a case](https://docs.datadoghq.com/incident_response/case_management/create_case)
