# Source: https://docs.firehydrant.com/docs/incident-fields.md

# Incident Fields

FireHydrant's incidents come with a powerful set of capabilities around incident fields: alongside default fields, you can also add custom fields, specify required fields, show/hide different fields, and even reorder fields according to your organization's needs.

> 📘 Note:
>
> Modifying incident field settings requires **<Glossary>Owner</Glossary> permissions** within your organization.

## Default Fields

<Image align="center" alt="Example view of the Incident Fields settings" border={false} caption="Example view of the Incident Fields settings" src="https://files.readme.io/4d1f75408a5b7f4ab50122ce2138666c980eb651c3e9d954438a94e57cc798d3-CleanShot_2025-06-11_at_16.54.12.jpg" width="650px" />

FireHydrant provides a comprehensive set of default fields for tracking key information on an incident:

* **Incident Name** (`string`): The name of the incident. This is the only field that is required by default, but you can modify this behavior (see next section).
* **Private incident** (`boolean`): Whether or not the incident is private. To learn more, see [Private Incidents](https://docs.firehydrant.com/docs/private-incidents).
* **Description** (`string`): A longer description and/or summary of the incident.
* **Customer Impact** (`string`): A field for describing the total impact to customers. You can also include links to Zendesk tickets, and FireHydrant will automatically link these tickets to the incident and post updates to those tickets. To learn more, visit [Zendesk](https://docs.firehydrant.com/docs/zendesk-integration).
* **Severity** (`string`): How major an incident is. FireHydrant provides default values, but you can [customize them](https://docs.firehydrant.com/docs/severities-and-priorities) for your needs.
* **Priority** (`string`): The priority of an incident. There is a strong correlation between how severe an incident is and how much it should be prioritized, so many FireHydrant users only use **Severity**.
* **Labels** (`object`): Custom key-value pairs of data for an incident. We generally recommend using [custom fields](#custom-fields) instead of labels, but for historical reasons, labels are still supported.
* **Incident Tags** (`array[string]`): Tags for an incident. FireHydrant has a filtering system that allows you to find incidents and filter Analytics/metrics by various traits, including tags.
* **Environments, Functionalities, Services** (`array[objects]`): FireHydrant's [Service Catalog](https://docs.firehydrant.com/docs/intro-to-service-catalog) is a valuable tool for not only tracking system components, but also collecting incident statistics and associating owning teams and responders.
* **Runbooks** (`array[objects]`): FireHydrant's automation engine. [Runbooks](https://docs.firehydrant.com/docs/introduction-to-runbooks) help automate steps within the IM process to reduce toil and time to assembly. Runbooks are defined as templates and then may be "attached" to an incident either manually or automatically via conditions.
* **Teams** (`array[objects]`): Teams consist of either individual users or external escalation policies/on-call schedules. Assigning teams to incidents will log team metrics as well as pull in the users/on-call personnel into the incident channel.
* **Incident Type** (`string`): Selection of a specific incident type, which will pre-populate other fields. For more information, visit [Incident Types](https://docs.firehydrant.com/docs/incident-types).

## Field Requirement and Visibility Settings

### Requiring Fields

**Name** is the only field that is always required by default, but you can modify other fields to be required. As of right now, FireHydrant supports requiring fields at declaration, which impacts the forms shown when declaring incidents in Slack and in the web UI as well as API call.

You can also configure different required fields for different Incident Types. For more information, visit [Incident Types](https://docs.firehydrant.com/docs/incident-types) documentation.

To modify field requirements settings:

1. Navigate to the same incident settings page at **Settings > Incident Settings**.
2. Click the Pencil icon next to whichever field you would like to edit.
3. On this page, you can configure the following items:
   1. **Requirement** - Choose from **Not required** (default), **Always required**, and **Required at and after milestone.** If always required, then the field will need to be filled out immediately upon incident declaration. Otherwise, you can require the field at a specific milestone and thereafter.
   2. **Visibility** - Choose from Visible, Available, and Hidden. Note that if you choose to require a field, it will always be set to visible.

> 📘 Note:
>
> If a field is **Required**, it will also automatically be set to **Visible**. See the [next section](#showinghiding-fields).
>
> Additionally, setting fields as **Required** will impact every place that incidents can be created or edited, including the web UI, Slack, MS Teams, and integrations like [Zendesk](https://docs.firehydrant.com/docs/zendesk-integration).

Attempting to declare an incident with any required fields empty will result in an error via almost all methods: web UI, Slack, [Alert Routing](https://docs.firehydrant.com/docs/alert-routing), and API. The one exception to this rule is [Scheduled Maintenances](https://docs.firehydrant.com/docs/scheduled-maintenances), which will bypass any required fields since they cannot be filled out at maintenance start.

<Image align="center" alt="Example required field preventing incident creation in Slack" border={false} caption="Example required field preventing incident creation in Slack" src="https://files.readme.io/65793d9-image.png" width="400px" />

```shell Terminal
$ curl --request POST \
  --url https://api.firehydrant.io/v1/incidents \
  --header 'Authorization: FH_API_TOKEN' \
  --header 'Content-Type: application/json' \
  --data '{
  "name": "Example Incident with no Description from API",
}'

{
  "detail": "",
  "messages": [
    "description Must be set"
  ],
  "meta": {}
}
```

Above is an example of API output when a required custom field is not filled out.

### Required Fields for Milestone Transitions

Organizations can enforce mandatory data entry at specific milestones throughout the incident lifecycle. This ensures that critical information is captured consistently, facilitating more effective incident analysis, reporting, and regulatory compliance.

To modify these settings, go to **Settings> Incident Settings** and click the Pencil icon next to the field you want to edit. Check or uncheck "Required at and after milestone," then select the milestone where the field should be required. The field will be required at the chosen milestone and any subsequent milestones.

<Image align="center" alt="Set a field as required for a Milestone" border={false} caption="Set a field as required for a Milestone" src="https://files.readme.io/c086f27381d0530202bfda4000c29f537cc05a4902a06bc7cc07763e200129c2-required-fields.jpg" width="400px" />

Attempting to transition a milestone with any required fields empty will result in an error via all methods: web UI, Slack, MS Teams, and API.

### Required Milestones

<Image align="center" alt="Milestones requirements in Incident Settings" border={false} caption="Milestones requirements in Incident Settings" src="https://files.readme.io/15e0b348cca984e1ff8028597132e2576bf3db9e3caeef294f17799e32cad153-CleanShot_2025-06-11_at_16.55.29.jpg" width="650px" />

Users may want to require milestones to be populated with timestamps to preserve data integrity and quality for their incidents.

To do this, users can go to their [Incident settings](https://app.firehydrant.io/settings/incident_fields) page and then go to the **Milestones** tab. On this page, you can select and configure certain milestone timestamps must be filled out before reaching certain states. Some examples of common flows:

* **Identified** and **Mitigated** milestones must be filled out before resolving an incident
* All milestones must have timestamps before **Retrospective Completed**
* ...etc.

Once a milestone timestamp has been set as required, any attempts to update or transition the milestone will prompt the user to fill in this field if it is empty.

### Showing/Hiding Fields

Given that so many fields are available, anyone reporting an incident could face analysis paralysis if they are presented with too many boxes and pieces of information to fill in.

Thus, modifying the visibility of fields at declaration time can cut down on the amount of noise and cognitive load for a responder so they can quickly fill out only what is relevant and declare as quickly as possible. You can modify every field's visibility settings except **Name**, which is always required and visible.

To do this, go to **Settings> Incident settings** and click the Pencil next to any field you want to edit, and select the appropriate setting under **When declaring incidents**:

* **Visible** means a field will be shown in the declaration form regardless of whether it is required
* **Available** means a field will not be visible at first, but in the UI and Slack during declaration, you will be able to find it under **Additional fields** and show it and fill it as necessary
* **Hidden** means the field is hidden entirely

<Image align="center" alt="The result of hiding every field except for **Name**, which is always required" border={false} caption="The result of hiding every field except for **Name**, which is always required" src="https://files.readme.io/c2890a9-image.png" width="400px" />

## Using fields in Liquid templating

Incident fields can be referenced anywhere [Template Variables](https://docs.firehydrant.com/docs/template-variables) are supported. You can reference the value of a  field directly as a parameter under the `incident` object. For example:

```Text Liquid
Name: {{ incident.name }}
Description: {{ incident.description }}

...etc.
```

Our editors have autocomplete enabled for any field that supports Liquid templating, so you should be able to browse the full list of accessible parameters in-app:

<Image align="center" alt="Example Liquid autocomplete view" border={false} caption="Example Liquid autocomplete view" src="https://files.readme.io/e29e5a0-image.png" />

For more information, visit the [Template Variables](https://docs.firehydrant.com/docs/template-variables) documentation.

## Field Requirements Updates

Note that field requirements are taking on a **snapshot-basis** for each incident - if you create an incident, and then someone modifies a specific field to be Required afterward, this will not change the requirement on that existing incident.

The intention is to ensure changing requirements don't interfere or disrupt ongoing incidents.

## Next Steps

* Learn about [creating custom incident fields](https://docs.firehydrant.com/docs/incident-custom-fields)
* See how you can make declaring incidents as easy as possible by templatizing fields with [Incident Types](https://docs.firehydrant.com/docs/incident-types)
* Tweak other settings such as [Incident Roles](https://docs.firehydrant.com/docs/incident-roles), [Severities and Priorities](https://docs.firehydrant.com/docs/severities-and-priorities), and more!