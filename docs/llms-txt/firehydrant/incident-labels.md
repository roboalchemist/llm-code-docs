# Source: https://docs.firehydrant.com/docs/incident-labels.md

# Incident Labels

This article describes how to use incident labels on incidents. Labels are another way of tracking custom data and organizing incidents. Incident labels are separate and different from Service Catalog labels.

Labels were the original way to track custom data and information on FireHydrant, but we recommend [Custom Fields](https://docs.firehydrant.com/docs/incident-custom-fields) for this now. Labels will still continue to be supported, but they lack a lot of the automation and flexibility that custom fields have.

## Setting Labels on incidents

Labels can be added to incidents both during declaration and mid- and post-incident. If a label doesn't exist, it will automatically be created when added to the incident.

Keys and values support alphanumeric, dashes, underscores, and forward slashes.

### via Slack

Labels are available as a field in both the declaration form as well as when editing an incident's details via `/fh edit`.

The field will be visible or tucked away under "Additional Details" depending on your [field configuration settings](https://docs.firehydrant.com/docs/incident-fields).

<Image alt="Example Slack modal with Labels set to &#x22;Visible&#x22;" align="center" width="400px" src="https://files.readme.io/34087d7-image.png">
  Example Slack modal with Labels set to "Visible"
</Image>

### via Web UI

As with Slack, Labels are also available as a default visible field or as an optional field under "Additional Details" depending on your configuration settings.

<Image alt="Labels field in the UI when set to &#x22;Visible&#x22;" align="center" width="650px" src="https://files.readme.io/dc97907-image.png">
  Labels field in the UI when set to "Visible"
</Image>

Once you've started an incident, Labels can be modified just like all other incident details by clicking the Edit pencil in the right-side details panel. Labels tend to be at the bottom of the details panel.

<Image alt="Editing Labels in the Command Center" align="center" src="https://files.readme.io/0a5765f-Screenshot_2023-12-08_at_4.55.45_PM.png">
  Editing Labels in the Command Center
</Image>

## Using labels to filter incidents

<Image alt="Labels filter in the Incidents page" align="center" width="400px" src="https://files.readme.io/32f3e58-image.png">
  Labels filter in the Incidents page
</Image>

On your [Incidents page](https://app.firehydrant.io/incidents), you can filter the list of incidents by both Label Key and Label Key = Label Value.

* Specifying only **Label Key** (e.g. "Foo") will show you all incidents that have a "Foo" label regardless of what the value is
* Specifying **Label Key = Label Value** (e.g. "Foo=Bar") will show you specifically only incidents that both have a "Foo" label and its value is "Bar"

This filtering capability also exists via the [`GET /incidents`](https://developers.firehydrant.com/#/operations/getV1Incidents) API endpoint, and all incidents returned will also contain **Labels** in the body.

## Next Steps

* Look at using [Incident Custom Fields](https://docs.firehydrant.com/docs/incident-custom-fields) for more custom and robust data gathering
* Continue customizing FireHydrant by tweaking [Incident Roles](https://docs.firehydrant.com/docs/incident-roles), [Severities and Priorities](https://docs.firehydrant.com/docs/severities-and-priorities), and more
* Look at our [Template Variables](https://docs.firehydrant.com/docs/template-variables) guide to see how to use incident data in various places and automations