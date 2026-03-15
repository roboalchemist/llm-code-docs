# Source: https://docs.firehydrant.com/docs/incident-types.md

# Incident Types

Many different kinds of incidents can happen. With incident types in FireHydrant, your responders can quickly declare an incident by selecting a type, which pre-populates fields. From there, users can modify the pre-filled values or immediately declare.

## Creating a new incident type

<Image align="center" alt="Incident type creation page" border={false} caption="Incident type creation page" src="https://files.readme.io/c8b33b7-CleanShot_2024-08-14_at_13.13.55.png" width="650px" />

Under **Incident Response** in the FireHydrant UI, click **Incident Types**. Click **New** in the top right corner of the page to create a new incident type.

This page is almost an exact mirror of the [incident declaration](https://docs.firehydrant.com/docs/starting-incidents) page, which allows you to pick and choose which fields to pre-populate and with what data. For an overview of all incident fields, see [Incident Fields](https://docs.firehydrant.com/docs/incident-fields) or configure [Incident Custom Fields](https://docs.firehydrant.com/docs/incident-custom-fields).

The only additional field here is **Incident type name**, which is the name you provide for this incident type. When users select an incident type from the dropdown while declaring, this is the name they will see.

### Required Fields

<Image align="center" border={false} caption="Setting a field as required in an incident type" src="https://files.readme.io/156943fd1a140b6ef566f1d842c5827516ca0ac3b583a1aada0b531391c049a2-image.png" width="650px" />

Incident types can additionally support different required fields for each type. These are in addition to [system-wide required fields](https://docs.firehydrant.com/docs/incident-fields). Type-specific required fields function identically to those set at the organization level, except they respect a hierarchy:

* Required fields defined org-wide will always be required, regardless of the chosen incident type or if one is chosen.
* Fields required for specific incident types will only be required when that specific incident type is chosen.

### Best Practices

The only required data for a new incident type, like when declaring an incident, is a Name, but of course, this is underutilizing the capabilities of Incident Types. Here are some ideas:

1. **Impact**: When you add impacted services, functionalities, and environments, it dramatically speeds up the process of declaring an incident. Additionally, your analytics in FireHydrant will be more consistent since templates guarantee that impacted component(s) will always be added.
2. **Severity**: In line with impacted infrastructure, sometimes users may pre-determine how severe an incident is based on its type. For example, an issue where a "database is completely unresponsive" would likely constitute a severe incident, and this can be predetermined without needed input from responders.
3. **Description**: The description has been used in multiple ways, from a pre-templated, general blurb about the type of issue this incident represents to a prompt to guide your responders with what to fill in when selecting this type.
4. **Runbooks**: Often, different situations demand different automation, and you can specify this by pre-attaching certain Runbooks to incident types. This ensures that specific automation is kicked off.

Effective incident types help responders for your organization quickly categorize and select the right type for whatever issue they may face. This will vary according to the organization, but generally, FireHydrant recommends incident types that are not too generalized. For example:

* ❌ "Infrastructure issues"
  * It seems very broad. Is it a database issue? Network traffic?
  * If almost all of your incidents can be categorized by the same incident type, then the type is too broad

**Examples of incident types we have seen that work:**

* ✔️ "Database disk capacity issues"
  * This always pulls in the platform engineers and executes a Runbook with a [Send a Webhook](https://docs.firehydrant.com/docs/runbook-step-send-a-webhook) step to query current and remaining disk space from databases
* ✔️ "UI Portal Issues"
  * This always pulls in the frontend engineering team to investigate what might be occurring, and they can pull in additional backend folks as needed if the contributing factors go deeper than HTML and Javascript
* ✔️ "Investigation Incident"
  * This is an incident type FireHydrant uses for its incidents. If we've discovered some issues but are unsure whether it is an incident or what the exact impact is, we kick off initial investigation incidents, which assign a `TRIAGE` severity, create the incident Slack channel and pull on an on-call engineer to do initial exploration. Then, things can escalate from there as needed.

## **Using an incident type**

<Image align="center" alt="Slack declaration form with incident type selection" border={false} caption="Slack declaration form with incident type selection" src="https://files.readme.io/2b2202f-image.png" width="400px" />

FireHydrant supports using an incident type to create an incident in Slack, MS Teams, and the web interface. You can configure whether to show or hide Incident Types dropdown in the [Incident Fields](https://docs.firehydrant.com/docs/incident-fields) settings.

Selecting a type will show all the preconfigured fields and data, allowing responders to edit/add more details if necessary.

<Image align="center" alt="Showing pre-filled fields when selecting a type" border={false} caption="Showing pre-filled fields when selecting a type" src="https://files.readme.io/0cbb3f9-types.gif" width="400px" />

MS Teams interface is slightly different, allowing you to choose an incident type before opening the modal to pre-filled values.

<Image align="center" alt="Incident types in MS Teams" border={false} caption="Incident types in MS Teams" src="https://files.readme.io/08d064b067b213e7de54f3ba5035e8329131a43a5c030f9e9031d344235f60f2-CleanShot_2025-01-09_at_17.07.26.gif" width="400px" />

To use incident types in the web interface, create a type and click the "Declare Incident" button. Incident types, if any exist, will appear as the first item in the Declare Incident form. Like Slack, selecting a type will show preconfigured fields with preconfigured values.

<Image align="center" alt="Example of selecting an Incident Type to quickly populate fields" border={false} caption="Example of selecting an Incident Type to quickly populate fields" src="https://files.readme.io/a3eb52f-CleanShot_2024-08-14_at_13.29.46.gif" width="650px" />

## Role-Based Access Control for Incident Types

Organizations can now restrict which incident types users can create incidents with based on their role. This ensures that only authorized users can declare specific types of incidents, providing additional security and governance for sensitive incident categories.

### How Incident Type RBAC Works

When configuring an incident type, you can specify which roles are allowed to use it during incident declaration:

1. Navigate to **Settings** > **Incident Types**
2. Click on an incident type to edit it or create a new one
3. In the incident type form, select which roles should have access to use this incident type
4. Save your changes

Users will only see and can select incident types their role has access to in the incident declaration dropdown. This least-privilege security model is particularly useful for incident types related to security incidents, compliance issues, or other sensitive scenarios that should only be accessible to specific teams.

## Hiding Incident Types

Don't use incident types? No problem. You can enable/disable Incident Types by visiting the **Incident settings** form where all of your other fields are configured. Incident Types are treated just like any other field.

<Image align="center" alt="Incident types are treated just like any other field and can be reordered or hidden" border={false} caption="Incident types are treated just like any other field and can be reordered or hidden" src="https://files.readme.io/c18638c22c53e6c13797004ee8e0a3a6e3648363a73f617e455a07f8a8e6baa9-CleanShot_2025-06-11_at_16.51.07.jpg" width="650px" />

## Next Steps

* Learn more about [Runbooks](https://docs.firehydrant.com/docs/introduction-to-runbooks), the powerful automation engine underneath the hood of FireHydrant
* Customize your [Incident Fields](https://docs.firehydrant.com/docs/incident-fields) as well as [Custom Fields](https://docs.firehydrant.com/docs/incident-custom-fields)
* Look at configuring [Severities and Priorities](https://docs.firehydrant.com/docs/severities-and-priorities) as well as [Service Catalog Conditions](https://docs.firehydrant.com/docs/conditions)