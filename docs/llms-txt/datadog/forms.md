# Source: https://docs.datadoghq.com/actions/forms.md

---
title: Forms
description: Build forms to collect input, analyze responses, and trigger automations.
breadcrumbs: Docs > Forms
source_url: https://docs.datadoghq.com/forms/index.html
---

# Forms

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### Join the Preview!

Forms are in Preview. Click Request Access, and fill in the Datadog Product Preview Program form.

[Request Access](https://docs.google.com/forms/d/e/1FAIpQLSe_OxTl8E_djqF107dKJDhcUuLxh1n9ytEKT6CZa-u8ZPqokg/viewform)
{% /callout %}

## Overview{% #overview %}

Datadog Forms allow you to collect input, analyze responses, and trigger automations in Datadog. Forms and their responses can be shared across your organization, allowing you to collect and analyze data with your team.

## Examples{% #examples %}

Here are some ways you can use forms:

- Scaffold services from predefined templates.
- Collect engineering feedback in an internal developer portal (IDP).
- Create service requests for security, platform, or IT teams, directly from employee form responses.

## Create a form{% #create-a-form %}

When creating a form, you can use a template or start from scratch. Templates are starter forms that cover common use cases. They come loaded with a sample description and questions to help familiarize yourself with form elements. Templates also showcase best practices for setting up form elements.

{% image
   source="https://datadog-docs.imgix.net/images/actions/forms/forms-blueprint-selected.256906619c094e355d9aadb1fb99c8f3.png?auto=format"
   alt="The form creation page with the IDP Feedback Survey selected" /%}

To create a form:

1. On the [Forms](https://app.datadoghq.com/actions/forms) page, click **New Form**.
1. Select a template or **Start with a blank form**, then click **Continue**.
1. Optionally, name your form and give it a description. Click **Continue**.
1. New forms are auto-populated with placeholder components. To edit the form, click a placeholder component, or click the **{% icon name="icon-plus-circled-wui" /%}** icon to add a new component. Component types include short answer, paragraph, dropdown, checkboxes, ratings, and toggle. The following table lists the elements available inside components:
| Element       | Description                                                                                                                                                 | Component Availability                       |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| Required      | Determines whether the question requires an answer from the respondent; required questions are marked with a red asterisk on forms.                         | All components                               |
| Field name    | The name of the field. Appears in the JSON version in [**Responses**](https://docs.datadoghq.com/actions/forms/#view-in-forms). Not visible to respondents. | All components                               |
| Placeholder   | The text the respondent sees before entering any text.                                                                                                      | Short answer, paragraph, and dropdown        |
| Default value | The default item or text that is selected before the respondent makes a selection.                                                                          | All components except ratings and checkboxes |
| Data          | The available options that respondents can choose from.                                                                                                     | Dropdown and checkboxes                      |
| Questions     | The questions respondents are asked when rating their experience.                                                                                           | Ratings                                      |
1. Click **Save** to save your changes.

To preview, share, and debug your form:

1. Click **View** to display the form as it appears to respondents. Click **Edit** to return to the creator view.
1. Click **Share** to copy the form link.
1. In the **Debug** section, you can:
   - Click **Form** to show a mini-preview of your form.
   - Click **Data Definition** to show the JSON version of the components' definition.
   - Click **UI Definition** to show the JSON version of the form's UI.

### Add automation{% #add-automation %}

After creating a form, you can add an [action](https://app.datadoghq.com/actions/action-catalog/) or [workflow blueprint](https://app.datadoghq.com/workflow/blueprints) that triggers automatically when a form is submitted.

1. From the [Forms](https://app.datadoghq.com/actions/forms) page, click a form.
1. Click **Automation**.
1. Choose an action or blueprint.
1. The action or blueprint opens in a workflow canvas, where you can [edit it](https://docs.datadoghq.com/actions/workflows/build/#build-a-workflow-with-the-workflow-builder).
1. Click **Create**.

**Note**: Because forms are powered by workflows, automations triggered by forms appear under [Workflow Automation](https://app.datadoghq.com/workflow). Additionally, there is no charge associated with workflow executions that are triggered by a form.

## Manage access{% #manage-access %}

By default, only the creator of a form can access it. To change the permissions on a form:

1. From the [Forms](https://app.datadoghq.com/actions/forms) page, click a form.
1. Click the gear 
   {% icon name="icon-cog-2" /%}
 icon.
1. To change who can see the form and submit answers, click **Edit Form Permissions**.
1. To change who can see the submitted responses, click **Edit Response Permissions**.

## Analyze your data{% #analyze-your-data %}

### View in forms{% #view-in-forms %}

To view form responses in a table format:

1. From the [Forms](https://app.datadoghq.com/actions/forms) page, click a form.
1. Click **Responses**.
1. Click the edit icon on a response to view the JSON version.

**Note**: Datadog stores responses in a datastore, which is listed in [Datastores](https://app.datadoghq.com/actions/datastores).

### View in a dashboard{% #view-in-a-dashboard %}

To visualize form responses in a dashboard:

1. Navigate to the [DDSQL Editor](https://app.datadoghq.com/ddsql/editor).
1. In the **Data** tab, click **Actions Datastores**.
1. Select the datastore associated with your form, then click **Insert into editor**.
1. Optionally, click the query's title to rename it.
1. Click **Save**.
1. [Create a dashboard](https://docs.datadoghq.com/dashboards/#get-started), then [add a widget](https://docs.datadoghq.com/dashboards/widgets/#add-a-widget-to-your-dashboard). For forms, all widgets except Timeseries are supported.
1. When [defining the metric](https://docs.datadoghq.com/dashboards/querying/#define-the-metric), select **DDSQL Editor** and the datastore query you created earlier.
1. Finish [configuring your widget](https://docs.datadoghq.com/dashboards/widgets/configuration/), then click **Save**.

## Further reading{% #further-reading %}

- [Turn feedback into action across your engineering org with Datadog Forms](https://www.datadoghq.com/blog/datadog-forms)
