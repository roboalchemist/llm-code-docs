# Source: https://developers.kit.com/plugins/component-library/toggle.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Toggle

The toggle allows creators to enable or disable specific features through a simple boolean switch interface. It's perfect for optional configurations like custom descriptions, showing or hiding elements, applying filters, or turning functionality on and off. The toggle provides clear visual feedback about the current state of the setting.

<img width="400" alt="example toggle" src="https://mintcdn.com/kit-314e57c1/lY9TOM1hpqCczZ4S/images/plugins/components/toggle.png?fit=max&auto=format&n=lY9TOM1hpqCczZ4S&q=85&s=7c16411113ec0a8eb01bf5838b0b8ff5" data-path="images/plugins/components/toggle.png" />

<Note>
  Fields dependent on toggles will only show when the toggle is switched on (i.e. has a value `true`).
</Note>

## Compatibility

| Plugin type    | Availability                 | Additional notes |
| -------------- | ---------------------------- | ---------------- |
| Content blocks | <Icon icon="square-check" /> |                  |
| Media source   | <Icon icon="square-xmark" /> |                  |

## Properties

<ParamField body="type" type="string" required="true">
  `toggle` - the type of the component
</ParamField>

<ParamField body="name" type="string" required="true">
  A unique internal-only identifier that is posted to an app's plugin server to share values inputted by the creator
</ParamField>

<ParamField body="label" type="string" required="true">
  Creator-facing identifier that is shown in the plugin environment (64 character limit)
</ParamField>

<ParamField body="default" type="boolean">
  Default state of the toggle when the component first loads
</ParamField>

<ParamField body="required" type="boolean">
  Determines whether the creator must interact with the toggle before proceeding
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
      "type": "toggle",
      "name": "optional_toggle",
      "label": "Optional Toggle",
      "default": false, // optional
      "required": false, // optional
      "help": "Helping you understand what this toggle does", //optional
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
        "optional_toggle": true
        // ...additional plugin settings
      }
      // ...plugin-specific additional data
    }
  ```
</ResponseExample>


Built with [Mintlify](https://mintlify.com).