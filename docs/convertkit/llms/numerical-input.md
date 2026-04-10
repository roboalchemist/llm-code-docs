# Source: https://developers.kit.com/plugins/component-library/numerical-input.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Numerical input

The numerical input allows creators to enter numeric values in a dedicated field with optional currency or unit indicators. It's perfect for collecting prices, quantities, measurements, or any numeric data that benefits from contextual prefixes or suffixes. The input provides a clean interface optimized for numerical data entry.

<img width="300" alt="example numerical input" src="https://mintcdn.com/kit-314e57c1/4EgMrJKlIf0mMyhm/images/plugins/components/numerical_input.png?fit=max&auto=format&n=4EgMrJKlIf0mMyhm&q=85&s=c77c0bb1a603f884a0f30b366481af49" data-path="images/plugins/components/numerical_input.png" />

## Compatibility

| Plugin type    | Availability                 | Additional notes |
| -------------- | ---------------------------- | ---------------- |
| Content blocks | <Icon icon="square-check" /> |                  |
| Media source   | <Icon icon="square-check" /> |                  |

## Properties

<ParamField body="type" type="string" required="true">
  `numericalInput` - the type of the component
</ParamField>

<ParamField body="name" type="string" required="true">
  A unique internal-only identifier that is posted to an app's plugin server to share values inputted by the creator
</ParamField>

<ParamField body="label" type="string" required="true">
  Creator-facing identifier that is shown in the plugin environment
</ParamField>

<ParamField body="prepend" type="string">
  Text or symbol displayed before the input field (e.g., "\$" for currency). Maximum 5 characters. Cannot be used with `append`.
</ParamField>

<ParamField body="append" type="string">
  Text or symbol displayed after the input field (e.g., "lbs" for weight). Maximum 5 characters. Cannot be used with `prepend`.
</ParamField>

<ParamField body="max" type="number">
  Maximum value allowed
</ParamField>

<ParamField body="min" type="number">
  Minimum value allowed
</ParamField>

<ParamField body="required" type="boolean">
  Determines whether the creator must enter a value before proceeding
</ParamField>

<ParamField body="help" type="string">
  Brief creator-facing explanation that clarifies the component's purpose and usage. Maximum 64 characters.
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

## Important Notes

* Either `prepend` or `append` must be provided, but not both
* The placeholder is automatically set to "0" and cannot be customized
* Input accepts decimal numbers and automatically validates numeric format

<RequestExample>
  ```json JSON setting with prepend theme={null}
  {
    "type": "numericalInput",
    "name": "price",
    "label": "Product Price",
    "prepend": "$",
    "max": 200, //optional
    "min": 0, //optional
    "required": true,
    "help": "Enter the price in USD",
    "dependencies": [
      {
        "field": "enable_pricing",
        "value": true
      }
    ]
  }
  ```
</RequestExample>

<ResponseExample>
  ```json Example response theme={null}
  {
    "settings": {
      "price": "99.99",
      "weight": "2.5"
    }
  }
  ```
</ResponseExample>


Built with [Mintlify](https://mintlify.com).