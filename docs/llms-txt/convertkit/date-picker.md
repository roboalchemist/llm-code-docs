# Source: https://developers.kit.com/plugins/component-library/date-picker.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Date picker

The date picker allows creators to select specific dates for time-sensitive content such as event announcements, promotional campaigns, or content scheduling. All dates are standardized and returned in UTC ISO8601 format to ensure consistent handling across different time zones and applications.

<img width="300" alt="example date picker" src="https://mintcdn.com/kit-314e57c1/ohR8KbVxvspIDffR/images/plugins/components/date_picker.png?fit=max&auto=format&n=ohR8KbVxvspIDffR&q=85&s=fb49d13b3e1a9a2c71b948635ca6b2f3" data-path="images/plugins/components/date_picker.png" />

## Compatibility

| Plugin type    | Availability                 | Additional notes |
| -------------- | ---------------------------- | ---------------- |
| Content blocks | <Icon icon="square-check" /> |                  |
| Media source   | <Icon icon="square-xmark" /> |                  |

## Properties

<ParamField body="type" type="string" required="true">
  `date` - the type of the component
</ParamField>

<ParamField body="name" type="string" required="true">
  A unique internal-only identifier that is posted to an app's plugin server to share values inputted by the creator
</ParamField>

<ParamField body="label" type="string" required="true">
  Creator-facing identifier that is shown in the plugin environment
</ParamField>

<ParamField body="required" type="boolean">
  Determines whether the creator must select a date before proceeding
</ParamField>

<ParamField body="help" type="string">
  Brief creator-facing explanation that clarifies the component's purpose and usage.
</ParamField>

<ResponseField name="dependencies" type="object array">
  Allows for the field to be shown conditionally. Dependent on other fields. See [dependencies page](/plugins/component-library/dependencies) for more details.

  <Expandable title="properties">
    <ResponseField name="field" type="string" required="true">
      Name of the dependent field
    </ResponseField>

    <ResponseField name="value" type="string">
      Value for the dependent field required to show this field. To show when any value is inputted, leave out this property.
    </ResponseField>
  </Expandable>
</ResponseField>

<RequestExample>
  ```json JSON setting theme={null}
    {
      "type": "date",
      "name": "start_date",
      "label": "Start date",
      "required": false, // optional
      "help": "help text shown in tooltip to creator while editing", // optional
      "dependencies": [
        {
            "field": "dependent_field",
            "value": "dependent_value" //optional
        }
      ] // optional
    }
  ```
</RequestExample>

<ResponseExample>
  ```json Example response theme={null}
    {
      "settings": {
        "start_date": "2024-10-03T07:00:00.000Z"
        // ...additional plugin settings
      }
      // ...plugin-specific additional data
    }
  ```
</ResponseExample>


Built with [Mintlify](https://mintlify.com).