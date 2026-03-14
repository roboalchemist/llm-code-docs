# Source: https://developers.kit.com/plugins/component-library/radio-group.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Radio group

The radio group component allows creators to choose from mutually exclusive options presented as individual selectable buttons. It's ideal for settings where only one choice can be made at a time, such as text alignment, layout options, or display modes. The visual button interface makes selection clear and intuitive for creators.

<img width="400" alt="example radio button" src="https://mintcdn.com/kit-314e57c1/lY9TOM1hpqCczZ4S/images/plugins/components/radio-group.png?fit=max&auto=format&n=lY9TOM1hpqCczZ4S&q=85&s=31b7f89c8fcc10a679a8db9fa706b4f8" data-path="images/plugins/components/radio-group.png" />

<Note>
  To get the most out of dependency with radio-groups utilize the `value` option whereby a field only shows when the corresponding value is selected, using the following syntax:

  ```json  theme={null}
    {
      "name": "text_alignment",
      "label": "Text Alignment",
      "type": "radioGroup",
      // ...additional component-specific settings
      "dependencies": [
        {
          "field": "field_name",
          "value": "expected_value"
        }
      ]
    }
  ```

  A typical use case for this would be to create three pre-defined options and a final `Custom` button, that exposes more granular functionality.
</Note>

## Compatibility

| Plugin type    | Availability                 | Additional notes |
| -------------- | ---------------------------- | ---------------- |
| Content blocks | <Icon icon="square-check" /> |                  |
| Media source   | <Icon icon="square-xmark" /> |                  |

## Properties

<ParamField body="type" type="string" required="true">
  `radioGroup` - the type of the component
</ParamField>

<ParamField body="name" type="string" required="true">
  A unique internal-only identifier that is posted to an app's plugin server to share values inputted by the creator
</ParamField>

<ParamField body="label" type="string" required="true">
  Creator-facing identifier that is shown in the plugin environment (64 character limit)
</ParamField>

<ResponseField name="options" type="array" required="true">
  Array of objects containing label-value pairs for the radio button options

  <Expandable title="properties">
    <ResponseField name="value" type="string" required="true">
      A unique internal-only identifier that is posted to an app's plugin server to share values from the specific button selected by the creator
    </ResponseField>

    <ResponseField name="label" type="string" required="true">
      Creator-facing identifier that is shown on the button (character length across all labels in the component cannot exceed 28 characters)
    </ResponseField>
  </Expandable>
</ResponseField>

<ParamField body="default" type="string">
  Default option value that is pre-selected when the component first loads
</ParamField>

<ParamField body="required" type="boolean">
  Determines whether the creator must make a selection before proceeding (defaults to false)
</ParamField>

<ParamField body="help" type="string">
  Brief creator-facing explanation that clarifies the component's purpose and usage (64 character limit)
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
      "name": "text_alignment",
      "label": "Text Alignment",
      "required": false, // optional - defaults to false
      "help": "Choose how text should be aligned", // optional
      "type": "radioGroup",
      "default": "left", // optional
      "options": [
        {
          "label": "Left",
          "value": "left"
        },
        {
          "label": "Center",
          "value": "center"
        },
        {
          "label": "Right",
          "value": "right"
        }
      ],
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
        "radio_group": "center"
        // ...additional plugin settings
      }
      // ...plugin-specific additional data
    }
  ```
</ResponseExample>


Built with [Mintlify](https://mintlify.com).