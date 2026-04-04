# Source: https://docs.rootly.com/integrations/jira/rootly-to-jira-sync.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Rootly to Jira Sync

<Note>
  This page details the configuration to have **Rootly write to Jira**.
</Note>

## Workflow Configurations

### Create Jira Issue

The **Create Jira Issue** action is used to create a new ticket in Jira. In order to create an issue into Jira, you must select the specific project to created the ticket into (`Project Key` field) and select the `Issue Type` to create the ticket in.

This workflow action can be used to create Jira tickets for either **incidents** or **action items**. It is recommended that you use the Create Jira Subtask for action items. However, if your project teams don't use subtasks, you can use this action to create Jira issues as well.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/DEGWl8qg20zbzmSF/images/integrations/jira/rootly-to-jira-sync/images-1.webp?fit=max&auto=format&n=DEGWl8qg20zbzmSF&q=85&s=e8f168f938ab07f9f846e524c22f9634" width="917" height="1358" data-path="images/integrations/jira/rootly-to-jira-sync/images-1.webp" />
</Frame>

### Update Jira Issue

The **Update Jira Issue** action is used to update an existing ticket in Jira. In order to update an existing issue in Jira, you must reference it in the `Jira Issue to Update` field using the `{{ incident.jira_issue_id }}` variable.

<Warning>
  This workflow will only work if you have initially created a Jira issue for the incident or action item.
</Warning>

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/DEGWl8qg20zbzmSF/images/integrations/jira/rootly-to-jira-sync/images-2.webp?fit=max&auto=format&n=DEGWl8qg20zbzmSF&q=85&s=29ecad431fbd6eef77761bf864b24444" width="922" height="1376" data-path="images/integrations/jira/rootly-to-jira-sync/images-2.webp" />
</Frame>

### Create Jira Subtask

The **Create Jira Subtask** action is used to create a subtask under an existing Jira issue. In order to create a subtask for an existing Jira issue, you must you must reference the original Jira issue in the `Parent Jira Issue` field using the `{{ incident.jira_issue_id }}` variable. The `Project Key` entered here must be the same as the one used in the original Create Jira Issue action.

This workflow action is intended to be used for **action items** or **sub-incidents**.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/DEGWl8qg20zbzmSF/images/integrations/jira/rootly-to-jira-sync/images-3.webp?fit=max&auto=format&n=DEGWl8qg20zbzmSF&q=85&s=8dc61a8c2844653ca24a6f218385cdf7" width="918" height="1397" data-path="images/integrations/jira/rootly-to-jira-sync/images-3.webp" />
</Frame>

### Jira Native Field Mapping

#### Labels

Jira has a native field called Labels. The syntax to set this field is different than the one used to set a custom field of the labels type.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/EZBU89ISF00990Wy/images/integrations/jira/rootly-to-jira-sync/images-4.webp?fit=max&auto=format&n=EZBU89ISF00990Wy&q=85&s=436246f50fccf17cba7f78be2f1fc9d0" width="901" height="195" data-path="images/integrations/jira/rootly-to-jira-sync/images-4.webp" />
</Frame>

```json  theme={null}
//Rootly native multi-select to Jira native Labels
"customfield_12345": {{ incident.service_slugs | join: ","}}

//Rootly custom multi-select to Jira native Labels
"customfield_10033": {{ incident.custom_fields | find: 'custom_field.slug', 'your_custom_field_slug' | get: 'selected_options' | map: 'value' | join: "," }}

//Rootly custom labels to Jira labels
//Coming soon!
```

#### Team

Jira has a native field called `Team`, but it's stored as a "custom field". In addition, it only allows a single team to be selected. To map to this field in Jira, you'll need to use the following syntax format:

```json  theme={null}
//Format to map to Jira native Team field
{
"customfield_10001": "<jira_team_id>" 
}

//Rootly native Teams field to Jira native Team field. We used the "description field to store the corresponding jira_team_id
{
"customfield_10001": "{{ incident.raw_groups[0] | get: 'description' }}" 
}
```

### Advanced Configuration

The `Default` tabs in each of the above workflow actions will allow you to set default Jira fields. If you have custom fields defined in your Jira project or would like to dynamically set Jira fields, you will need to do so via custom mapping in the `Advanced` tab.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/EZBU89ISF00990Wy/images/integrations/jira/rootly-to-jira-sync/images-5.webp?fit=max&auto=format&n=EZBU89ISF00990Wy&q=85&s=a0ba02aef65f3ad9d26b0296a61be8c9" width="914" height="739" data-path="images/integrations/jira/rootly-to-jira-sync/images-5.webp" />
</Frame>

#### Custom Fields Mapping

It is highly likely that your Jira projects contain custom fields. The default tab in the above workflow actions will not be sufficient in mapping to these custom fields. You will need to input the custom syntax in the `Custom Fields Mapping` field in the `Advance` configuration tab.

In order to map to custom fields in Jira you would need to know the following information:

* The **custom field id** in Jira

* The **field type** in Jira

* The **incident property** that you would like to map from

<Note>
  This [Atlassian article](https://confluence.atlassian.com/jirakb/how-to-find-id-for-custom-field-s-744522503.html "Atlassian article") will show you how to find the id of the Jira custom field id.

  These are the [field types](https://support.atlassian.com/jira-cloud-administration/docs/custom-fields-types-in-company-managed-projects/ "field types") that a Jira custom field can have.

  Liquid variables for Rootly incident properties can be found [here](/configuration/incident-types).
</Note>

Map to Jira custom **text** or **paragraph** field type.

```json  theme={null}
//Rootly native text or textarea field to Jira text
"customfield_12345": "{{ incident.functionalities }}"

//Rootly native single or multiple select field to Jira text
"customfield_12345": "{{ incident.functionalities }}"

//Rootly custom text or textarea field to Jira text
"customfield_12345": "{{incident.custom_fields | find: 'custom_field.slug', 'your-slug' | get: 'selected_options' | map: 'value' }}"

//Rootly custom single or multiple select field to Jira text
"customfield_12345": "{{incident.custom_fields | find: 'custom_field.slug', 'your-slug' | get: 'selected_options' | map: 'value' }}"
```

Map to Jira's custom **single select** field type.

```json  theme={null}
//Rootly native single or multiple select to Jira single select
"customfield_12345": { "value": "{{ incident.raw_groups | first | get: 'name' }}" }

//Rootly custom single or multiple select to Jira single select
"customfield_12345": { "value": "{{ incident.custom_fields | find: 'custom_field.slug', 'your_custom_field_slug' | get: 'selected_options' | map: 'value' }}" }
```

Map to Jira's custom **multi-select** field type.

```json  theme={null}
//Rootly native multi-select to Jira multi-select
{% assign functions = incident.functionalities %}
   {% assign array = "" %}
{% for function in functions %}
   {% assign item = '{"value":"' | append: function | append: '"}' %}
   {% assign array = array | append: item | append: "," %}
{% endfor %}
{% capture final_array %}[{{ array | remove_last: ',' }}]{% endcapture %}
"customfield_12345": {{ final_array }}

//Rootly custom multi-select to Jira multi-select
"customfield_12345": {{ incident.custom_fields | find: 'custom_field.slug', 'your_custom_field_slug' | get: 'selected_options' | to_values }}
```

Map to Jira's custom **labels** field type.

```json  theme={null}
//Rootly native multi-select to Jira labels
"customfield_12345": {{ incident.service_slugs | to_json }}

//Rootly custom multi-select to Jira labels
"customfield_10033": {{ incident.custom_fields | find: 'custom_field.slug', 'your_custom_field_slug' | get: 'selected_options' | map: 'value' | to_json }}

//Rootly custom labels to Jira labels
//Coming soon!
```

Map to Jira's custom **number** field type.

```json  theme={null}
//Rootly custom number field to Jira number field
"customfield_26117": {{ incident.custom_fields | find: 'custom_field.slug', 'your_custom_field_slug' | get: 'selected_options.value' }}
```

Map to Jira's custom **datetime** field type.

```json  theme={null}
//Rootly native datetime to Jira datetime
"customfield_10030": "{{incident.started_at | date: '%FT%T%:z' }}"

//Rootly custom datetime to Jira datetime
"customfield_26218": "{{ incident.custom_fields | find: 'custom_field.slug', 'your_custom_field_slug' | get: 'selected_options.value' | date: '%Y-%m-%dT%H:%M:%S.%d%z' }}"
```

Map to Jira’s custom **user** field type.

```json  theme={null}
//Rootly user to Jira custom user field ( Single Select )
{% assign jira_email = incident.roles | find: 'incident_role.slug', 'incident-commander' | get: 'user.email' %}
"customfield_20825": { "id": "{{ team.jira_users | where: 'email', jira_email | first | get: 'account_id' }}" }
```

```json  theme={null}
//Rootly user to Jira custom user field ( Multi Select )
{% assign jira_email = incident.roles | find: 'incident_role.slug', 'incident-commander' | get: 'user.email' %}
"customfield_20825": [{ "id": "{{ team.jira_users | where: 'email', jira_email | first | get: 'account_id' }}" }]
```

#### API Payload

**Dynamically set Jira priority** field based on incident severity.

```json  theme={null}
{% if incident.severity_slug == 'sev0' %}
  { "priority": [ { "set": { "name" : "High" } } ] }
{% elsif incident.severity_slug == 'sev1' %}
  { "priority": [ { "set": { "name" : "Medium" } } ] }
{% elsif incident.severity_slug == 'sev2' %}
  { "priority": [ { "set": { "name" : "Low" } } ] }
{% endif %}
```

Add **comment** to existing Jira issue.

```json  theme={null}
{
  "comment": [
    {
      "add": {
        "body": "Enter your message here. Liquid syntax is supported here."
      }
    }
  ]
}
```

**Link Jira issue** created for action item to existing issue created for incident.

```json  theme={null}
//Set linkage to "Relates to"
{
  "issuelinks": [
    {
      "add": {
        "type": {
          "name": "Relates",
          "outward": "relates to"
        },
        "outwardIssue": {
          "id": "{{ incident.jira_issue_id}}"
        }
      }
    }
  ]
}

//Set linkage to "Action item for"
{
   "issuelinks": [
      {
         "add": {
            "type": {
               "name":"Action",
               "outward":"action item for"
            },
            "outwardIssue": {
               "id":"{{ incident.jira_issue_id}}"
            }
         }
      }
   ]
}
```

Set Jira's native **Labels** field in Jira. Since this is a native field in Jira, it can be updated via the API Payload field.

```json  theme={null}
{
"labels": [{"set": ["label1", "label2"]}]
}
```

Set default Components field in Jira. Since this is a default field in Jira, it will need to be updated via API Payload field.

<Warning>
  Typically, teams like to use the Services field in Rootly to represent Components in Jira. The sample below shows this common scenario. You can use other Rootly multi-select fields to represent Components in Jira as well, just make sure you adjust the code below to reference the Rootly property you're using.

  I order for this to work, you **MUST** ensure that the name of the Service in Rootly matches **EXACTLY** the name of the Components in Jira.
</Warning>

```json  theme={null}
{% assign components = incident.services %}
{
  "components": [
    {
      "set": [
      {% for component in components %}
        {
          "name": "{{ component }}"
        }{% unless forloop.last %},{% endunless %}
      {% endfor %}
      ]
    }
  ]
}
```

# Debugging

Below are common errors you might run into during your configuration process. To view the error response, you can locate the specific workflow you're trying to debug, select **...** **>** **View Runs** **>** **View**.

| Error                                              | Comment                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `issue_id cannot be null.`                         | **Reason for error...**<br />This often happens on Update Jira Issue action. This means the reference Jira issue you're attempting to update does not exist.<br /><br />**How to fix...**<br />Ensure your workflow does not run until AFTER a Jira issue has already been created and linked to the incident.                           |
| `"customfield_12345": "Custom Field is required."` | **Reason for error...**<br />This means the specified custom field is configured as a required field in the Jira project and your workflow isn't passing it any value.<br /><br />**How to fix...**<br />You can either add custom fields mapping to map to the specific field or configure the Jira project to make the field optional. |
| `unexpected token at '{ "customfield_10032": }'`   | **Reason for error...**<br />Your custom mapping syntax is incorrect.<br /><br />**How to fix...**<br />Correct your mapping syntax.                                                                                                                                                                                                     |
| `Specify a valid project ID or key`                | **Reason for error...**<br />This means the Jira Project Key you've selected in the action is not available in the selected Jira instance.<br /><br />**How to fix...**<br />Reselect the Jira Instance and then reselect the Project Key.                                                                                               |
| `The issue type selected is invalid.`              | **Reason for error...**<br />This means the Jira Issue Type you've selected in the action is not available in the selected Jira project.<br /><br />**How to fix...**<br />Reselect the Project Key and then reselect the Issue Type.                                                                                                    |


Built with [Mintlify](https://mintlify.com).