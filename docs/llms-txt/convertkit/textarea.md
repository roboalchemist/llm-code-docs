# Source: https://developers.kit.com/plugins/component-library/textarea.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Textarea

The textarea component allows creators to enter longer, multi-line text content. It's ideal for collecting descriptions, messages, body content, or any text that requires multiple lines and more space than a single-line input. The textarea provides an expandable interface that accommodates extensive text-based information.

<img width="300" alt="example textarea" src="https://mintcdn.com/kit-314e57c1/lY9TOM1hpqCczZ4S/images/plugins/components/textarea.png?fit=max&auto=format&n=lY9TOM1hpqCczZ4S&q=85&s=6943d8490991cb3daa833dfd7451daf6" data-path="images/plugins/components/textarea.png" />

## Compatibility

| Plugin type    | Availability                 | Additional notes                                                                                                                                    |
| -------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Content blocks | <Icon icon="square-check" /> |                                                                                                                                                     |
| Media source   | <Icon icon="square-check" /> | Available as part of the preset `search` functionality. Check [media source documentation](/plugins/media-source/plugin-settings) for more details. |

## Properties

<ParamField body="type" type="string" required="true">
  `textarea` - the type of the component
</ParamField>

<ParamField body="name" type="string" required="true">
  A unique internal-only identifier that is posted to an app's plugin server to share values inputted by the creator
</ParamField>

<ParamField body="label" type="string" required="true">
  Creator-facing identifier that is shown in the plugin environment (64 character limit)
</ParamField>

<ParamField body="placeholder" type="string">
  Placeholder text displayed in the textarea when empty
</ParamField>

<ParamField body="default" type="string">
  Default value when the component first loads
</ParamField>

<ParamField body="max_length" type="number | null">
  Maximum character limit for the textarea content. Set to `null` for unlimited length
</ParamField>

<ParamField body="required" type="boolean">
  Determines whether the creator must enter text before proceeding
</ParamField>

<ParamField body="help" type="string">
  Brief creator-facing explanation that clarifies the component's purpose and usage (64 character limit)
</ParamField>

<ResponseField name="dependencies" type="object array">
  Allows for the field to be shown conditionally, dependent on other fields. See [dependencies page](/plugins/component-library/dependencies) for more details.

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
      "type": "textarea",
      "name": "feature_description",
      "label": "Feature Description",
      "placeholder": "Describe the feature when enabled", // optional
      "default": "This text describes the feature", // optional
      "max_length": null, // optional - null for unlimited
      "required": false, // optional
      "help": "Only appears when feature toggle is enabled", // optional
      "dependencies": [
        {
            "field": "enable_feature"
            // no value property - shows when enable_feature has any value
        }
      ] // optional
    }
  ```
</RequestExample>

<ResponseExample>
  ```json Example response theme={null}
    {
      "settings": {
        "feature_description": "This feature enables advanced analytics tracking for user interactions, providing detailed insights into engagement patterns and conversion metrics. It includes real-time monitoring, custom event tracking, and comprehensive reporting dashboards."
        // ...additional plugin settings
      }
      // ...plugin-specific additional data
    }
  ```
</ResponseExample>


Built with [Mintlify](https://mintlify.com).