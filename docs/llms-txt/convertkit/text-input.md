# Source: https://developers.kit.com/plugins/component-library/text-input.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Text input

The text input allows creators to enter short snippets of text in a single-line field. It's perfect for collecting titles, names, URLs, or any brief text content that doesn't require multiple lines. The input provides a clean, straightforward interface for essential text-based information.

<img width="300" alt="example text input" src="https://mintcdn.com/kit-314e57c1/ohR8KbVxvspIDffR/images/plugins/components/text_input.png?fit=max&auto=format&n=ohR8KbVxvspIDffR&q=85&s=452f57dfe41cc010c2656cf91d92ddd5" data-path="images/plugins/components/text_input.png" />

## Compatibility

| Plugin type    | Availability                 | Additional notes                                                                                                                                    |
| -------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Content blocks | <Icon icon="square-check" /> |                                                                                                                                                     |
| Media source   | <Icon icon="square-check" /> | Available as part of the preset `search` functionality. Check [media source documentation](/plugins/media-source/plugin-settings) for more details. |

## Properties

<ParamField body="type" type="string" required="true">
  `text` - the type of the component
</ParamField>

<ParamField body="name" type="string" required="true">
  A unique internal-only identifier that is posted to an app's plugin server to share values inputted by the creator
</ParamField>

<ParamField body="label" type="string" required="true">
  Creator-facing identifier that is shown in the plugin environment
</ParamField>

<ParamField body="placeholder" type="string">
  Placeholder text displayed in the input field when empty
</ParamField>

<ParamField body="required" type="boolean">
  Determines whether the creator must enter text before proceeding
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
      "type": "text",
      "name": "title",
      "label": "Title",
      "placeholder": "Enter a title...", // optional
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
        "title": "My Amazing Email Campaign"
        // ...additional plugin settings
      }
      // ...plugin-specific additional data
    }
  ```
</ResponseExample>


Built with [Mintlify](https://mintlify.com).