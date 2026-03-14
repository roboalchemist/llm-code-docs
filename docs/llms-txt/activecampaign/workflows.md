# Source: https://developers.activecampaign.com/docs/workflows.md

# workflows Array

The `workflows` array contains a list of `workflow` objects. Each object is associated with an action (e.g., create an ActiveCampaign Contact). For each workflow, you can define a guided setup experience, as well as how data should be processed.

> 📘
>
> The `workflows` can include *an inbound workflow*, *multiple outbound workflows* or *multiple outbound workflows with an inbound workflow*.

<Table align={["left", "left", "left"]}>
  <thead>
    <tr>
      <th>Key</th>
      <th>JSON Type</th>
      <th>Required</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><a href="#workflows-name">name</a></td>
      <td>string</td>
      <td>yes</td>
    </tr>

    <tr>
      <td><a href="#workflows-description">description</a></td>
      <td>string</td>
      <td>no</td>
    </tr>

    <tr>
      <td><a href="#workflows-label">label</a></td>
      <td>string</td>
      <td>yes</td>
    </tr>

    <tr>
      <td><a href="#workflows-type">type</a></td>
      <td>string</td>
      <td>yes</td>
    </tr>

    <tr>
      <td><a href="#workflows-resource_type">resource\_type</a></td>
      <td>string</td>
      <td>no</td>
    </tr>

    <tr>
      <td><a href="#workflows-auth">auth</a></td>
      <td>string</td>
      <td>yes</td>
    </tr>

    <tr>
      <td><a href="#workflows-data_intake">data\_intake</a></td>
      <td>string</td>
      <td>Depends on type of integration.<br />Inbound - yes<br />Outbound - no</td>
    </tr>

    <tr>
      <td><a href="#historical_data_intake">historical\_data\_intake</a></td>
      <td>string</td>
      <td>no</td>
    </tr>

    <tr>
      <td><a href="#resource_labels">resource\_labels</a></td>
      <td>object</td>
      <td>no</td>
    </tr>

    <tr>
      <td><a href="#setup">setup</a></td>
      <td>object</td>
      <td>yes</td>
    </tr>

    <tr>
      <td><a href="#data-pipeline">data\_pipeline</a></td>
      <td>object</td>
      <td>yes</td>
    </tr>
  </tbody>
</Table>

> ❗️ Be careful: Workflow can not be deleted, and their NAMES can not be updated!
>
> You can change the label (what users will see) at any time, but once a workflow is published, the workflow can not be deleted, and it's name can not be changed.\*\*
>
> When an app is published, users will implement these workflows into their automations. These workflows are identified in our system by the `name` you assigned to it. If in a future update the workflow is deleted, or its name is changed, users who have that workflow previously implemented will continue to use the old workflow- "branching" your configuration: Some users still using the old workflow, and new implementations using the new workflow.
>
> If a workflow is not deleted and its name is not changed, any workflow *content* updates will be provided to all users.

### `name` Property <a name="workflows-name" />

The *name* of the workflow, must be unique for the workflows of an app.

### `label` Property <a name="workflows-label" />

A "human-readable" name to distinguish different workflow objects. This value is used to list workflows. The `label` property should use the following format: *Brand Name - What it does*. For example, *Twilio - Send an SMS*.

### `description` Property <a name="workflows-description" />

A one sentence summary describing what the workflow does. This sentence should end with a period. For example, "Send messages to your Contacts using Twilio."

![](https://files.readme.io/13e9435-labels.png "labels.png")

### `type` Property <a name="workflows-type" />

The associated ActiveCampaign app. This helps workflows to be discovered and used in the appropriate context. An app can have multiple workflows for multiple ActiveCampaign apps.

> 🚧 Warning
>
> Currently, the type value is limited to "automations" for outbound workflows and "generic" for inbound workflows.

### `resource_type` Property <a name="workflows-resource_type" />

This is an **optional** field that is used by **inbound** apps to indicate what resource type is sending data to ActiveCampaign. This information is useful if your inbound app is also intended to be used as a trigger in Automations. **This value should always be the plural form of the resource type.** For example, if your resources are landing pages, the value can be set to "pages".

Below is an example of an app that has an inbound workflow with "resource\_type" set to "pages". Users can select this trigger when setting up automations in ActiveCampaign, so that every time MyApp processes a page, more actions can take place within our platform. You can learn more about how your app can be used as a trigger under the "Branded app triggers" section in [this article](https://help.activecampaign.com/hc/en-us/articles/218788707-Automation-triggers-explained).

![](https://files.readme.io/c8ac8b3-custom-start-trigger.png "custom-start-trigger.png")

### `auth` Property <a name="workflows-auth" />

The associated auth method. Attribute value must match one of the auth methods defined in the [auth section](https://developers.activecampaign.com/docs/auth).

### `data_intake` Property <a name="workflows-data_intake" />

The `data_intake` to use for the workflow. The value should match the *name* of a defined `data_intake` object. This property is not required for outbound integrations.

### `historical_data_intake` Property <a name="historical_data_intake" />

The `data_intake` to use for a one-time data import. The value should make the *name* of a defined `polling` type `data_intake` object. This is an optional feature for `webhook`-based workflows. This property is not required for outbound integrations.

> 📘 Using Polling with Custom Object Workflows
>
> Custom Object Workflows do not currently support displaying a `setup.schedule` step. To allow imports to operate with developer defined values, the following optional fields are available on the Polling Data Intake:
>
> `frequency`: *int* (Must be >= 60 (Seconds) **Recommended**: `1800`)\
> `import_option`: *string* (can be `single`, or `recurring`. **Recommended**: "recurring")
>
> ***These fields are only compared and used in Custom Object workflows, standard imports will ignore these values in favor of those defined by the user in the scheduling step.***

### `resource_labels` Object <a name="resource_labels" />

An optional object to override labels the customer sees for webhook and historical sync events and objects.

```json Example resource_labels
"resource_labels": {
  "webhook_events": ["Event A", "Event B"],
  "webhook_objects_updated": ["Object A"],
  "historical_sync_events": ["Sync Event A"],
  "historical_sync_objects_updated": ["Sync A", "Sync B"]
},
```

### `setup` Object <a name="setup" />

*setup* is where developers can define a guided user experience for setting up the integration.\
Typically, the setup should include the following sections also referred to as steps:

> * [connect](#setup-connect)
> * [select](#setup-select)
> * [review\_events](#setup-review-events-review-objects)
> * [review\_objects](#setup-review-events-review-objects)
> * [map](#setup-map)

> 📘 Note
>
> The above-mentioned setup steps are the same for both inbound and outbound workflows.
>
> All the 3 steps are *required* for inbound integrations.
>
> For outbound integrations:\
> Connect - required\
> Select - optional\
> Map - optional\
> and should be defined as per your use case.

#### connect <a name="setup-connect" />

This step allows the user to authorize the integration and ActiveCampaign to access their data.\
When this step is included in your setup, our integration layer will handle the authorization logic based on the [Auth](https://developers.activecampaign.com/docs/auth) section, but you need to define the following fields:

| Key                                                        | JSON Type | Required |
| :--------------------------------------------------------- | :-------- | :------- |
| [label](#setup-connect-label)                              | string    | yes      |
| [describe\_connection](#setup-connect-describe-connection) | object    | yes      |
| [help\_text](#setup-connect-help-text)                     | string    | no       |

##### `label` <a name="setup-connect-label" />

A user-friendly value used to display this step in the UI.

##### `describe_connection` <a name="setup-connect-describe-connection" />

"describe\_connection" is specific to the "connect" step, it provides information about the currently connected user.\
It's a command that gets data needed to display user information. The output should have the following attributes:

1. account\_id: the unique ID for the connected account. This is often the email.
2. description: what user information should be displayed when the connection is successful

##### `help_text` <a name="setup-connect-help-text" />

Help text that will be displayed during the "Connect" step. This section supports [commonmark](https://commonmark.org/help/) markdown. Please note, unless otherwise specified, other `help_text` fields may not support markdown at this time.

> 📘 Info
>
> This information is normally obtained from the publisher via an api call, and the response is formatted via jq. As a result, the command will often contain two commands: [!http](https://developers.activecampaign.com/docs/commands-1#http) and [!jq](https://developers.activecampaign.com/docs/commands-1#jq).

Example:

```json
{
      "label": "Connect",
      "describe_connection": {
        "!pipe": [
          {
            "!http": {
              "method": "GET",
              "path": "https://api.example-integration.com/me"
            }
          },
          {
            "!jq": ".body | {account_id: .email, description: (.name + \" - \" + .email)}"
          }
        ]
      },
      "help_text": "Connection level help text that does support [markdown](https://commonmark.org/help/)"
    }
```

![](https://files.readme.io/af72c3d-e01388a2-f252-41d5-b6cd-239a5ee8409d.jpg)

> 📘 About account\_id
>
> If your integration uses an application level webhook, the account\_id value must also appear in the webhook payload for us to properly link data to intended users. See [webhook scopes](https://developers.activecampaign.com/docs/data_intake#scope-a-namedataintake-scopea) for details.

#### select <a name="setup-select" />

The `select` step allows users to select the external resource that will be used to sync data with ActiveCampaign.\
For example, inbound - if an integration syncs Typeform form submissions data to ActiveCampaign, users can specify which form's data they need in this step.\
outbound - if an integration syncs changes within ActiveCampaign to Google Sheets, users can specify which sheet to send data to in this step.

| Key                                                     | JSON Type | Required              |
| :------------------------------------------------------ | :-------- | :-------------------- |
| [label](#setup-select-label)                            | string    | yes                   |
| [form\_fields](#setup-select-form-fields)               | list      | yes                   |
| [describe\_selection](#setup-select-describe-selection) | object    | only for inbound apps |

##### `label` <a name="setup-select-label" />

HTML label for this step field.

##### `form_fields` <a name="setup-select-form-fields" />

A list of HTML inputs to allow users to pin-point the desired external resource.

A form field has the following attributes:

| Key                                                 | JSON Type | Required                                   | Possible Values                                                                                                                                         |
| :-------------------------------------------------- | :-------- | :----------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [label](#setup-select-formfield-label)              | string    | yes                                        |                                                                                                                                                         |
| [id](#setup-select-formfield-id)                    | string    | yes                                        |                                                                                                                                                         |
| [required](#setup-select-formfield-required)        | boolean   | no                                         | true, false  <br /> default value: true                                                                                                                 |
| [type](#setup-select-formfield-type)                | string    | yes                                        | "text", "textarea", "dropdown", "multiselect"                                                                                                           |
| [placeholder](#setup-select-formfield-placeholder)  | string    | no                                         |                                                                                                                                                         |
| [search\_term](#setup-select-formfield-search_term) | string    | no                                         | Any string that will be used in the url as a search term. For example, a search term`userName` will become the query parameter `?userName=<user-input>` |
| [personalize](#setup-select-formfield-personalize)  | string    | no - For `type` of `textarea` only         | if defined, "ActiveCampaignContact"                                                                                                                     |
| [options](#setup-select-formfield-options)          | object    | yes - For any `type` other than `textarea` |                                                                                                                                                         |

##### `label` <a name="setup-select-formfield-label" />

The label shown in the form for the field.

##### `id` <a name="setup-select-formfield-id" />

A unique identifier for the field, suggested to be the value from the [label](#setup-select-formfield-label) but all lower case, with spaces replaced with dashes. This MUST be unique in a workflow, as it is used for [custom field expansion](#custom-data-expansion) in other parts of your configuration.

##### `required` <a name="setup-select-formfield-required" />

This is a boolean attribute indicating whether a form field is required or not. When required, this field must be filled out before the user can move to the next setup step. This defaults to **true**.\
When set to **false**, a field becomes optional. Users are allowed to move to the next setup step without providing any input to the optional fields.

##### `type` <a name="setup-select-formfield-type" />

The type of form field.

Available types are:

* dropdown
* textarea
* text
* multiselect

To allow users to select a single value from a list, use the "dropdown" type:

![](https://files.readme.io/f6c36be-Screen_Shot_2020-07-23_at_4.32.33_PM.png "Screen Shot 2020-07-23 at 4.32.33 PM.png")

To allow users to select multiple values, use the "multiselect" field type:

![](https://files.readme.io/e2925cf-multiselect.png "multiselect.png")

To allow users to define text (with or without personalization), use the "text" or "textarea" field type. Use "text" for shorter strings such as a single word or line of text. Use "textarea" for longer or multiline strings.

Below are examples of "textarea":

1. Textarea with personalization.

![](https://files.readme.io/95cd201-Screen_Shot_2020-07-23_at_10.29.43_AM.png "Screen Shot 2020-07-23 at 10.29.43 AM.png")

2. Textarea without personalization.

![](https://files.readme.io/a8bf9e2-textarea-without-personalize-dropdown.png "textarea-without-personalize-dropdown.png")

##### `placeholder` <a name="setup-select-formfield-placeholder" />

The placeholder value to show before a value is entered.

##### `search_term` <a name="setup-select-formfield-search_term" />

The optional `search_term` attribute is a part of the form\_fields section. If filled out, the value of this attribute will be used as a query parameter when executing that form field’s `!http` command. Of course, this will work only if search is supported by the API.

For example, when using a dropdown field, this would allow the user to search for a select option by typing into the dropdown field. The user’s input will end up as the search term’s value when the API call is made.

For example, providing the `search_term` a value of “search” will result in the `?search=<user-input>` query parameter.

Below is an example dropdown form field with with `search_term`:

```json search_term example
{
  ...,
  "form_fields": [
    {
      "label": "Choose Your Form",
      "type": "dropdown",
      "id": "form",
      "placeholder": "Select Form",
      "search_term": "search",
      "options": {
        "!pipe": [
          {
            "!http": {
              "method": "GET",
              "path": "/forms",
              "pagination": true
            }
          },
          {
            "!jq": "[.items[] | {display: .title, value: .id}]"
          }
        ]
      }
    }
  ]
}
```

##### `personalize` <a name="setup-select-formfield-personalize" />

For the "textarea" type, personalize is optional.\
If you want to let users define text with personalization (please see screenshot above for an UI example), then set this key to "ActiveCampaignContact" to allow users to customize the textarea with standard and custom fields defined for their contacts. When accessing this value in the [data\_pipeline](#data_pipeline-a-namedata-pipelinea) section of your configuration using [custom field expansion](#custom-data-expansion), the substitution strings in this value will be automatically replaced with values from the contact being processed.\
If the text being defined by users contains `%` characters or other characters that may be removed with personalization (ie: urls) set personalize to false. `"personalize": false`\
If you want to let users define text without personalization (please see screenshot above for an UI example), do not define the personalization attribute in the formfield definition.

##### `options` <a name="setup-select-formfield-options" />

When using anything but "textarea" type, you must specify a list of options for users to select from, each option should have two attributes: display and value.\
This information is normally obtained from the publisher via an api call, and the response is formatted via jq. As a result, the command will often contain two commands: [!http](https://developers.activecampaign.com/docs/commands-1#http) and [!jq](https://developers.activecampaign.com/docs/commands-1#jq).

> 📘 Note
>
> For any formfield, once the user selects a value from options, the selected value will be saved. To access a saved value, use [custom\_data](#custom-data-expansion).
>
> **Optional Fields**\
> When a field is declared as optional (using the [required attribute](#setup-select-formfield-required) above), you may not always get a value back if the user skipped it during setup. To refer to the value of an optional field, you must append the "default" filter to the expansion. This will default to an *empty string* if the optional field is not filled out by the user.
>
> See example below.

Example:

```json
{
      "label": "Select Your File",
      "form_fields": [
        {
          "label": "Folder",
          "id": "folder",
          "required": false,
          "type": "dropdown",
          "placeholder": "Select Folder",
          "options": {
            "!pipe": [
              {
                "!http": {
                  "method": "GET",
                  "path": "https://api.example-integration.com/folders/"
                }
              },
              {
                "!jq": "[.body.folders[] | {display: .name, value: .id}]"
              }
            ]
          }
        },
        {
          "label": "File",
          "id": "file",
          "type": "dropdown",
          "placeholder": "Select File",
          "options": {
            "!pipe": [
              {
                "!http": {
                  "method": "GET",
                  "path": "https://api.example-integration.com/folders/${custom_data.folder.value | default:1}/files"
                }
              },
              {
                "!jq": "[.body.files[] | {display: .file_info.name, value: .file_info.id}]"
              }
            ]
          }
        }
      ]
    }
```

This example will render 2 dropdowns, "Folder" and "File".

For the "Folder" field, the first !http command will make an API call to `https://api.example-integration.com/folders/`, which returns this response:

```json
{
      "folders": [
        {
          "id": "1",
          "name": "Folder 1"
        },
        {
          "id": "2",
          "name": "Folder 2"
        }
      ]
    }
```

The !jq command then transforms the response above into the following to render the first dropdown list:

```json
[
      {
        "display": "Folder 1",
        "value": "1"
      },
      {
        "name": "Folder 2",
        "value": "2"
      }
    ]
```

##### `custom_data` <a name="custom-data-expansion"> </a>

When the user selects a value from any input, their selection can be referenced via the "custom\_data" expansion.

```
${custom_data.ID.ATTRIBUTE} 
```

In the example above, if the user selects the first folder, then expressions below would evaluate to the correct values:

```
${custom_data.folder.display}.  # evaluates to "Folder 1"
${custom_data.folder.value}.     # evaluates to "1"
```

As the first input is defined as optional, the user could select nothing, in that case, reference will fail when we use expressions above. Always use the "default" filter to safely refer to an optional field. You can pass a default value to the default filter, or use it without any arguments:

```
${custom_data.folder.display|default:MyFolder}.  # evaluates to "MyFolder"
${custom_data.folder.display|default}.  # without any argument, default evaluates to empty string
```

These saved values can then be used in subsequent steps. In this example, we are using the selected folder value `(${custom_data.folder.value})` as part of the second API call to narrow down choices for the "File" dropdown.

##### `describe_selection` <a name="setup-select-describe-selection" />

This section is **required for inbound apps** and it allows the app to identify the resource that the user selected from the step above.

These two attributes are required:

* resource\_id
* display

Both these attributes should be defined by using a command that produces a string value. These values normally map to the custom data from user selection.

For the folder example, the section would look like:

```json
{
  "resource_id": {
    "!jq": "${custom_data.folder.value}"
  },
  "display": {
    "!jq": "${custom_data.folder.display}"
  }
}
```

> 📘 Why are these needed?
>
> resource\_id: used to uniquely identify the resource selected by the user;\
> display: used to render the resource selected by the user. You can customize how resource names appear using jq.

#### review\_events / review\_objects <a name="setup-review-events-review-objects" />

The `review_events` and `review_objects` sections allow developers to define descriptive and user-friendly text that shows within the review events and review objects steps modal.

> 📘 review\_events and review\_objects are only applicable if the app uses custom objects.
>
> > **The `review_events` and `review_objects` sections are always optional and exist within workflows → setup.**
> > The review\_events and review\_objects sections are only applicable when the app config uses custom objects. Also, depending on the app config the `review_events` might not be needed/used, while `review_objects` could be.

| Key                                      | JSON Type | Required |
| :--------------------------------------- | :-------- | :------- |
| [label](#setup-review-label)             | string    | no       |
| [header](#setup-review-header)           | string    | no       |
| [description](#setup-review-description) | string    | no       |

##### `label` <a name="setup-review-label" />

A user-friendly value used to display as the stepper text in the UI.

##### `header` <a name="setup-review-header" />

A user-friendly value used in the header text within the review modal.

##### `description` <a name="setup-review-description" />

User-friendly descriptive text that explains what the custom objects and events are all about.

##### Example `review_events`:

```json
"review_events": {
  "label": "",
  "header": "",
  "description": ""
}
```

![](https://files.readme.io/4e24235-review_events.jpg)

##### Example `review_objects`:

```json
"review_objects": {
  "label": "",
  "header": "",
  "description": ""
}
```

![](https://files.readme.io/30bdb5e-review_objects.jpg)

#### map <a name="setup-map" />

The map step allows users to map any field in your system to an ActiveCampaign field and vice versa. This mapping info allows data to be transformed properly between the integration and ActiveCampaign. For example, a user may choose to map "Given Name" from your system to "First Name" in ActiveCampaign.\
You need to define fields for both source and target. Depending on the direction of data flow, ActiveCampaign should be either the target (inbound, meaning data flows into ActiveCampaign from your system) or source (outbound, data flows from ActiveCampaign to your system).

> 🆕 Grouped Mapping
>
> Both [`describe_source`](#setup-map-describe-source)  and [`describe_target`](#setup-map-describe-target) can now define multiple sources and targets. This is done with a new key: `group` that can be included on each [`options`](#setup-map-describe-options) object.      Here’s what this looks like when using group keys in combination with contact, deal, and account fields for `describe_target` options:
>
> > ![](https://files.readme.io/07b7b43-image.png)

| JSON Type                                      | Required |     |
| :--------------------------------------------- | :------- | :-- |
| [label](#setup-map-label)                      | string   | yes |
| [describe\_source](#setup-map-describe-source) | object   | yes |
| [describe\_target](#setup-map-describe-target) | object   | yes |

##### `label` <a name="setup-map-label" />

User friendly label to display for this step. For example: "Mapping"

##### `describe_source` <a name="setup-map-describe-source" />

The describe\_source section defines how to populate available data fields of the source.

##### `describe_target` <a name="setup-map-describe-target" />

The describe\_target section defines how to populate available data fields of the target.

Both sections require these two attributes:

| Key                                    | JSON Type | Required |
| :------------------------------------- | :-------- | :------- |
| [label](#setup-map-describe-label)     | string    | yes      |
| [options](#setup-map-describe-options) | object    | yes      |

##### `label` <a name="setup-map-describe-label" />

User friendly label to display for target or source. ActiveCampaign should always be stylized as "ActiveCampaign".

##### `options` <a name="setup-map-describe-options" />

List of available fields to map.\
For ActiveCampaign fields, use the [!resource](https://developers.activecampaign.com/docs/commands-1#resource1) command, for example, "ActiveCampaignContact.fields".\
For external fields, you can either provide a static list or pull from an API using a `!pipe` command.\
The output should be a list of objects with "title", "id" and "required" attributes.

| Key            | Purpose                                                                                        | JSON Type             | Required                            |
| :------------- | :--------------------------------------------------------------------------------------------- | :-------------------- | :---------------------------------- |
| title          | Display value for the option                                                                   | string                | yes                                 |
| id             | Unique ID and value for the option. Will be the value written to the target field if selected. | string **or** integer | yes                                 |
| required       | to indicate if an option must be mapped                                                        | boolean               | no  <br /> default value is `false` |
| group          | define multiple distinct sources or targets                                                    | string                | no                                  |
| schemaId       | for custom object fields                                                                       | string                | only for custom object groups       |
| source\_fields | For describe\_target options only. List of user selectable values that does come from source.  | array\<source\_field> | no                                  |

> 🚧 Required fields in mappings
>
> The "required" attribute only takes effect within "describe\_target". This is to help make sure data can be processed after arriving at the destination:
>
> * Inbound Apps: ActiveCampaign is the target, and the Email field is always required.
> * Outbound Apps: developers are free to declare any field(s) as required, but at least one field mapping must be completed in the "mapping" step.
>
> Our system will indicate this requirement in the UI with an asterisk (\*) as shown below. Users **must** map all required fields before completing the integration setup. Please see the screenshot below.

##### `source_field` <a name="setup-map-describe-source-fields" />

> 🆕 Dynamic Source Selection
>
> Using `source_fields` in a `describe_target.options` allows you to define a user-selectable list of `options` whose values are fixed. When mapped, these fields will not be populated from the source data but will be set to the selected value instead.
>
> This is especially useful when required fields in the target are not present in the expected source data; for example, in ActiveCampaign, deal records need a Stage ID, a number unique to each user that won’t be present in the source. To allow Deals as targets, in our config, we would fetch the users deal stages and organize the result into an array of source\_fields under the deal Stage Field `option`.

| Attribute | Purpose                                                                                               | JSON Type             | Required |
| :-------- | :---------------------------------------------------------------------------------------------------- | :-------------------- | :------- |
| title     | Display value for the option                                                                          | string                | yes      |
| id        | Unique ID and value for the source\_field. Will be the value written to the target field if selected. | string **or** integer | yes      |

![](https://files.readme.io/94f2900-multi.png)

![](https://files.readme.io/be94484-suorce_mapping.png)

View a detailed example [here](https://developers.activecampaign.com/docs/configuration-walkthrough-1#setup-outbound-map-example) to see how mapping options are rendered.

#### Migrating from flat mapping to grouped mapping

A new key `default_group` was introduced to facilitate updating an existing map from flat to grouped mappings. This is **only intended for updating an existing app from flat to grouped mappings**. Users with existing mappings saved flat will see them grouped under the `default_group` key when navigating to the edit mappings page when the new grouped version is published. During processing, given a flat mapping and a `default_group` value, the `data_pipeline` processes the transform as if the mappings are grouped under the `default_group` value. `default_group` is ignored if a user has saved grouped mappings.

| Key            | JSON Type | Required |
| :------------- | :-------- | :------- |
| label          | string    | yes      |
| options        | object    | yes      |
| default\_group | string    | no       |

Shown here is how we migrated our Google Sheets Inbound Workflow from flat to grouped:

![](https://files.readme.io/3ef0864-image.png)

Here is an example of the subsequent `data_pipeline` states when using the `default_group` for this integration:

```json
Mappings are flat
default_group="contact"

data_pipeline.source output
{
    "A": "valueA",
    "B": "valueB",
    "C": "valueC",
    "D": "valueD"
}

===> Transform ===>

data_pipeline.target input

{
"contact":{
  "target_fieldA": "valueA",
  "target_fieldB": "valueB",
  "target_field1": "valueC",
  "target_field2": "valueD"
}
```

### `data_pipeline` Object <a name="data-pipeline" />

| Key                             | JSON Type | Required |
| :------------------------------ | :-------- | :------- |
| [source](#data-pipeline-source) | object    | yes      |
| [target](#data-pipeline-target) | object    | yes      |

This section defines how data is processed. All payloads go through 3 steps in the data pipeline, source, transform, and target. See diagram below:

![Data Pipeline](https://files.readme.io/eae3843-data-pipeline.png)

The "transform" step happens automatically (see details below), but you still need to define `source` and `target`.

#### source <a name="data-pipeline-source" />

When data is received by the integration, it's picked up by the source directly. The source section transforms data received by the integration to the correct format for the next step (transform).

> 📘 Info
>
> If the incoming payload is an ID, this section should contain a command that defines how to retrieve data needed for transformation. It's often a pipe command that consists of an HTTP request which fetches data based on ID, and a JQ transformation that converts data to a flat object if needed.

To transform data using existing field mappings, the integration backend expects data payloads to be valid JSON objects with fields at the root level.\
The responsibility of the `source` section is to make sure data is in the correct format.

For example, if the incoming payload is:

```json
{
  "timestamp": "2020-02-02T00:00:00",
  "data": {
    "Name": "Campy",
    "Age": 18
  }
}
```

It should be converted to:

```json
{
  "Name": "Campy",
  "Age": 18
}
```

To create contacts with custom tags, the output of this step should also include `_tags`, which is an array of strings.

```json
{
  "Name": "Campy",
  "Age": 18,
  "_tags": ["variant-a"]
}
```

#### transform (automatic)

> 📘 Note
>
> The integration automatically applies field mappings, so the output of this section is still a JSON object, whose keys are all mapped to external keys, and values are extracted from the incoming payload. See example below.

Given the output of source is:

```json
{
  "Name": "Campy",
  "Age": 18
}
```

and the field mappings configured by the user are:

```json
{
  "Name": "name_for_account",
  "Age": "age_for_account"
}
```

The expected output from `transform` is:

```json
{
  "name_for_account": "Campy",
  "age_for_account": 18
}
```

#### target <a name="data-pipeline-target" />

The target section should be a command that's responsible for sending the formatted payload to its destination. It's a possibility that you need to further transform the data for the target.

For example, you might want to transform the output from the previous step to the following before sending:

```json
{
  "data": {
    "name_for_account": "Campy",
    "age_for_account": 18
  },
  "action": "update"
}
```

All transformations should be included in this section before sending the payload.\
See [this example](https://developers.activecampaign.com/docs/configuration-walkthrough-1#data-pipeline-outbound-example) for details.

#### Grouped mapping example

Using groups in the `describe_target` section of the `map` step will result in storing mappings in a new format. When passed from the `data_pipeline.source` to the transform, data must be grouped into nested dictionaries under each intended group to see them have grouped mappings applied in the transform step.

The table below outlines the possible combinations for the map step. Depending on the combination, there are different formats the `transform` expects to receive from the output of the `data_pipeline.source` and, similarly, the formatting of the output of the `transform` changes too.

| Combination        | Grouped Target                                                                                                                 | Flat Target                                                                              |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| **Grouped Source** | All data from each source group should be an object of key-value pairs accessible under keys that match the group name.        | Same as grouped source, grouped target, except the output of the transform will be flat. |
| **Flat Source**    | Input should be an object of key-value pairs with no nested values. Transform output will group data under each field's group. | This is the standard flat mapping whose rules are unchanged.                             |