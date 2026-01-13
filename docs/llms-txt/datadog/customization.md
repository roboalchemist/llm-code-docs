# Source: https://docs.datadoghq.com/incident_response/case_management/customization.md

---
title: Customization
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Case Management > Customization
source_url: https://docs.datadoghq.com/case_management/customization/index.html
---

# Customization

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Datadog Case Management allows customization to align with your team's unique workflows, data capture needs, and reporting requirements.

## Custom Case Types{% #custom-case-types %}

{% alert level="danger" %}
You must have Case Shared Settings Write (`cases_shared_settings_write`) permissions. For more information, see [Datadog Role Permissions](https://docs.datadoghq.com/account_management/rbac/permissions/#case_management).
{% /alert %}

Datadog provides five [built-in case types](https://docs.datadoghq.com/incident_response/case_management/create_case#case-types), each designed for common workflows. To customize Case Management for your team's needs, you can define your own custom case types. This allows you to:

- Scope custom data capture to relevant work types
- Enable targeted automation
- Conduct more granular analytics and reporting

##### Create a custom case type{% #create-a-custom-case-type %}

1. Navigate to [**Settings > Shared Settings > Case Types**](https://app.datadoghq.com/cases/settings?type=shared).
1. Click **+ Create Case Type**.
1. Provide a **Name** and an optional **Description**.
1. Save your new case type.
1. (Optional) See the custom attributes section of this page to add custom attributes.

##### Enable a custom case type{% #enable-a-custom-case-type %}

After you create a custom case type, you must explicitly assign it to each project where it should be available. Follow the steps below to enable your new case type within a specific Case Management project.

1. Back on the [**Settings** page](https://app.datadoghq.com/cases/settings?type=shared), locate the target project under either **Starred Projects** or **Other Projects**.
1. Expand the project menu by clicking on the project name.
1. Click **General** to open the project's settings panel.
1. Scroll down to the Case Types section in the settings panel.
1. Under **From your organization**, open the dropdown and select the custom case type you created.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/case_management/customization/enable_custom_attribute.86a41c3ef1fecadc28a1c44ad8935569.png?auto=format"
   alt="Enable a custom case type in project settings" /%}

After you add the case type, it is available as an option when you create a new case within that project.

Your new case type is available for:

- Manual case creation
- API-based creation
- Automated case creation through Workflows

## Custom attributes{% #custom-attributes %}

Custom attributes allow you to capture the structured data your team needs to work efficiently and report effectively. All case types, whether Datadog-provided or custom, include five reserved attributes that cannot be removed or modified:

- Teams
- Services
- Environments
- Datacenters
- Versions

{% image
   source="https://datadog-docs.imgix.net/images/service_management/case_management/customization/add_custom_attribute.28b1bfc932e8931e3987ba3f39df0261.png?auto=format"
   alt="Add a custom attribute to a case type" /%}

You can add attributes that reflect your team's specific needs, such as escalation levels, component owners, business impact, or external links. To add a custom attribute:

1. Navigate to [**Settings > Shared Settings > Case Types**](https://app.datadoghq.com/cases/settings?type=shared).
1. Click the desired case type.
1. Click **+ Add Attribute**.
1. Provide:
   - Display Name (such as "Region")
   - Key (used for programmatic access and reporting)
   - Description (optional context for your team)
   - Data Type, choose from:
     - Text
     - URL
     - Number
   - Choose whether to allow multiple values for this attribute.

## Further reading{% #further-reading %}

- [Case Management Overview](https://docs.datadoghq.com/incident_response/case_management/)
- [Create a case](https://docs.datadoghq.com/incident_response/case_management/create_case)
- [Settings](https://docs.datadoghq.com/incident_response/case_management/settings)
