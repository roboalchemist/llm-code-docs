# Source: https://docs.rootly.com/integrations/jira/jira-to-rootly-sync.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Jira to Rootly Sync

<Note>
  This page details the configuration to have **Rootly respond to Jira**.
</Note>

## Listen for Jira Events

In order to respond to Jira events, you'll need to [set up a webhook](/integrations/jira/installation) in Jira so your Rootly platform can receive the events.

## Workflow Configurations

Select **workflow type**. Since Jira events will be created into Rootly as `alerts`, we will need to use an `Alert` workflow type.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/DEGWl8qg20zbzmSF/images/integrations/jira/jira-to-rootly-sync/images-1.webp?fit=max&auto=format&n=DEGWl8qg20zbzmSF&q=85&s=5fa86238e316c6a32a67d49eb23f120e" width="913" height="482" data-path="images/integrations/jira/jira-to-rootly-sync/images-1.webp" />
</Frame>

Select workflow **triggers**. `Alert Created` will be the only option to select here. This means the workflow will initialize whenever a new alert is created in Rootly.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/DEGWl8qg20zbzmSF/images/integrations/jira/jira-to-rootly-sync/images-2.webp?fit=max&auto=format&n=DEGWl8qg20zbzmSF&q=85&s=abfb737796319a2812b268e517e603f4" width="896" height="273" data-path="images/integrations/jira/jira-to-rootly-sync/images-2.webp" />
</Frame>

Configure **run conditions**. Set up your workflow to only run if...

* The alert `source` is from `Jira`
* The alert `labels`:
  * **Option 1:** `contains all of` the following `labels` (this is if you want to respond to a new Jira issue being created)
    * `event:jira:issue_created`
    * `project_key:RD1` (this label is optional - only include this if you want to respond to issues from a specific Jira project)
  * **Option 2:** `contains all of` the following `labels` (this is if you want to respond to an existing Jira issue being updated)
    * `event:jira:issue_updated`
    * `project_key:RD1` (this label is optional - only include this if you want to respond to issues from a specific Jira project)
* The alert `payload` has the `$.object.specific_field` equals to `/specific_value/i`
  * **JSON path syntax** is used to filter for a specific field from the alert payload (e.g. \$.issue.fields.issuetype.name). You can preview your syntax on [JSON Path Explorer](https://rootly.com/account/help/json-path-explorer "JSON Path Explorer").
  * **Ruby regular expression** can be used to specify what value to match to. You can test your regexp on this [Rubular tool](https://rubular.com/ "Rubular tool").

Currently, only a **single payload field** can be filtered on. So, try to configure your run conditions to filter by Label as much as you can before resorting to filtering by `Payload`.

We will be exploring the possibility of supporting filtering by multiple payload fields in the future.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/DEGWl8qg20zbzmSF/images/integrations/jira/jira-to-rootly-sync/images-3.webp?fit=max&auto=format&n=DEGWl8qg20zbzmSF&q=85&s=389f058734cde22b9454227cae233034" width="910" height="592" data-path="images/integrations/jira/jira-to-rootly-sync/images-3.webp" />
</Frame>

### Create Incident[](#DW5Rk)

The **Create Incident** action is used to declare an incident in Rootly. Since this action will be referencing alert data, the dynamic fields will be `{{ alert.properties }}`.

Rootly does NOT automatically link alerts to the incident. You'll need to include the following custom mapping in order to link the Jira ticket to the newly declared Rootly incident.

```json  theme={null}
{
  "jira_issue_id": "{{ alert.data.issue.id }}",
  "jira_issue_url": "https://your-jira-instance.atlassian.net/browse/{{alert.data.issue.key}}"
}
```

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/DEGWl8qg20zbzmSF/images/integrations/jira/jira-to-rootly-sync/images-4.webp?fit=max&auto=format&n=DEGWl8qg20zbzmSF&q=85&s=0eb9179b7e38018c4431af404cdffde4" width="933" height="1251" data-path="images/integrations/jira/jira-to-rootly-sync/images-4.webp" />
</Frame>

### Update Incident

The **Update Incident** action is used to update an existing incident in Rootly. Ensure that you set Attribute to Match field to `jira_issue_id` and `Attribute Value` to `{{ alert.data.issue.id }}`. These fields are required for Rootly to know which incident to update.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/DEGWl8qg20zbzmSF/images/integrations/jira/jira-to-rootly-sync/images-5.webp?fit=max&auto=format&n=DEGWl8qg20zbzmSF&q=85&s=971d205256a0331307daab5ee05b4168" width="959" height="1946" data-path="images/integrations/jira/jira-to-rootly-sync/images-5.webp" />
</Frame>

### Custom Fields Mapping

If you require more dynamic mapping of Rootly incident properties, you can input the following syntax into the `Custom Fields Mapping` field.

Dynamically set Rootly incident **severity**.

```json  theme={null}
{
  {% if alert.data.issue.fields.priority.name == 'Highest' %}
    "severity_id": "SEV0"
  {% elsif alert.data.issue.fields.priority.name == 'High' %}
    "severity_id": "SEV1"
  {% elsif alert.data.issue.fields.priority.name == 'Medium' %}
    "severity_id": "SEV2"
  {% else %}
    "severity_id": "SEV3"
  {% endif %}
}
```

Dynamically set Rootly incident **status**.

```json  theme={null}
{
  {% if alert.data.issue.fields.status.name == '<alert_status>' %}
    "status":"open"
  {% elsif alert.data.issue.fields.status.name == '<alert_status>' %}
    "status":"mitigated"
  {% elsif alert.data.issue.fields.status.name == '<alert_status>' %}
    "status":"resolved"
  {% else %}
    "status":"cancelled"
  {% endif %}
}
```

Set **custom field** for Rootly incident.

```json  theme={null}
//Setting Rootly text to hard-coded value
{
  "form_field_selections_attributes":[
    {
      "form_field_id":"e041106e-cb9a-404b-8ae1-51a1d6213a68",
      "value": "Nifty Gateway"
    }
  ]
}

//Setting Rootly text to value from the alert payload
{
  "form_field_selections_attributes":[
    {
      "form_field_id":"e041106e-cb9a-404b-8ae1-51a1d6213a68",
       "value":"{{alert.data.organization.name}}"
    }
  ]
}


//Setting Rootly single select or multi-select field
{
  "form_field_selections_attributes":[
    {
      "form_field_id":"e041106e-cb9a-404b-8ae1-51a1d6213a68",
       "selected_option_ids":["option_id"]
    }
  ]
}
```

# Debugging

Below are common errors you might run into during your configuration process. To view the error response, you can locate the specific workflow you're trying to debug, select **...** **>** **View Runs** **>** **View**.

| Error                                                 | Comment                                                                                                                                                                                                                                                                                                      |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `unknown attribute 'incident_property' for Incident.` | **Reason for error...**<br />This means the specified incident property you're trying to set is not an attribute you can set or the syntax is incorrect.<br /><br />**How to fix...**<br />Ensure that the field you're attempting to set is enabled to be set via workflow and that your syntax is correct. |
| `unexpected token at '{ "incident_property": }'`      | **Reason for error...**<br />Your custom mapping syntax is incorrect.<br /><br />**How to fix...**<br />Correct your mapping syntax.                                                                                                                                                                         |


Built with [Mintlify](https://mintlify.com).