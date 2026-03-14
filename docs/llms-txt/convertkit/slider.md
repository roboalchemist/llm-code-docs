# Source: https://developers.kit.com/plugins/component-library/slider.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Slider

The slider provides creators with an intuitive way to select numerical values through a visual slider interface combined with a numerical input box. It's perfect for precise control over design properties like corner radius, border width, pixel dimensions, or quantities. The dual interface allows creators to either drag the slider for quick adjustments or type exact values for precision.

<img width="400" alt="example slider" src="https://mintcdn.com/kit-314e57c1/LcH6W0paa0rAEiec/images/plugins/components/slider.png?fit=max&auto=format&n=LcH6W0paa0rAEiec&q=85&s=24a40b924fd1609871cc5886e86dfb14" data-path="images/plugins/components/slider.png" />

<Note>
  Fields cannot be dependent on sliders as they always have a value.
</Note>

## Compatibility

| Plugin type    | Availability                 | Additional notes |
| -------------- | ---------------------------- | ---------------- |
| Content blocks | <Icon icon="square-check" /> |                  |
| Media source   | <Icon icon="square-xmark" /> |                  |

## Properties

<ParamField body="type" type="string" required="true">
  `slider` - the type of the component
</ParamField>

<ParamField body="name" type="string" required="true">
  A unique internal-only identifier that is posted to an app's plugin server to share values inputted by the creator
</ParamField>

<ParamField body="label" type="string" required="true">
  Creator-facing identifier that is shown in the plugin environment (64 character limit)
</ParamField>

<ParamField body="max" type="number" required="true">
  Maximum value allowed on the slider
</ParamField>

<ParamField body="min" type="number" required="true">
  Minimum value allowed on the slider
</ParamField>

<ParamField body="step" type="number" required="true">
  Increment value for slider movement and input validation
</ParamField>

<ParamField body="default" type="number" required="true">
  Default value when the component first loads
</ParamField>

<ParamField body="required" type="boolean">
  Determines whether the creator must set a value before proceeding, defaults to `false`
</ParamField>

<ParamField body="help" type="string">
  Brief creator-facing explanation that clarifies the component's purpose and usage (64 character limit)
</ParamField>

<ParamField body="suffix" type="string">
  Unit or label displayed after the value (3 character limit, defaults to null). If `null` or absent, the suffix won't show
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
      "name": "border_width",
      "label": "Border Width",
      "required": false, // optional
      "help": "Set the border width in pixels", // optional
      "type": "slider",
      "max": 20,
      "min": 0,
      "step": 1,
      "default": 2,
      "suffix": "px", // optional
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
        "border_width": 5
        // ...additional plugin settings
      }
      // ...plugin-specific additional data
    }
  ```
</ResponseExample>


Built with [Mintlify](https://mintlify.com).