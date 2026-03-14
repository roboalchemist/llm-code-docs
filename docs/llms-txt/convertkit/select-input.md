# Source: https://developers.kit.com/plugins/component-library/select-input.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Select input

The select input provides creators with a dropdown menu containing predefined options. It's ideal for scenarios where you need to present a fixed set of choices such as categories, sizes, or configuration options. The selected value is hidden from creators but passed to your plugin for processing.

<Note>If you want to generate dynamic options, please use a [search input](/plugins/component-library/search-input) instead.</Note>

<img width="300" alt="example select input" src="https://mintcdn.com/kit-314e57c1/ohR8KbVxvspIDffR/images/plugins/components/select_input.png?fit=max&auto=format&n=ohR8KbVxvspIDffR&q=85&s=844c16d0bc291da2d9b5bd5eda48a60c" data-path="images/plugins/components/select_input.png" />

## Compatibility

| Plugin type    | Availability                 | Additional notes                                                                                                                                                     |
| -------------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Content blocks | <Icon icon="square-check" /> |                                                                                                                                                                      |
| Media source   | <Icon icon="square-check" /> | Available as part of the preset `filter` and `sort` group functionality. Check [media source documentation](/plugins/media-source/plugin-settings) for more details. |

## Properties

<ParamField body="type" type="string" required="true">
  `select` - the type of the component
</ParamField>

<ParamField body="name" type="string" required="true">
  A unique internal-only identifier that is posted to an app's plugin server to share values inputted by the creator
</ParamField>

<ParamField body="label" type="string" required="true">
  Creator-facing identifier that is shown in the plugin environment
</ParamField>

<ParamField body="options" type="array" required="true">
  Array of objects containing label-value pairs for the dropdown options
</ParamField>

<ParamField body="placeholder" type="string">
  Placeholder text displayed when no option is selected
</ParamField>

<ParamField body="required" type="boolean">
  Determines whether the creator must make a selection before proceeding
</ParamField>

<ParamField body="help" type="string">
  Brief creator-facing explanation that clarifies the component's purpose and usage
</ParamField>

<ResponseField name="dependencies" type="object array">
  Allows for the field to be shown conditionally. dependent on other fields. See [dependencies page](/plugins/component-library/dependencies) for more details.

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
      "type": "select",
      "name": "favorite_food",
      "label": "Favorite food",
      "options": [
        {
          "label": "French fries",
          "value": "food-id-1"
        },
        {
          "label": "Hash browns",
          "value": "food-id-2"
        },
        {
          "label": "Potato chips",
          "value": "food-id-3"
        }
      ],
      "placeholder": "Select a food...", // optional
      "required": true, // optional
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
        "favorite_food": "food-id-2"
        // ...additional plugin settings
      }
      // ...plugin-specific additional data
    }
  ```
</ResponseExample>


Built with [Mintlify](https://mintlify.com).