# Source: https://developers.kit.com/plugins/component-library/font-picker.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Font picker

The font picker allows creators to select typography that matches their brand identity and enhances readability. It provides access to email-safe font families with their appropriate fallbacks, along with font weight options to create visual hierarchy and emphasis in email content.

<img width="300" alt="example font picker" src="https://mintcdn.com/kit-314e57c1/ohR8KbVxvspIDffR/images/plugins/components/font_picker.png?fit=max&auto=format&n=ohR8KbVxvspIDffR&q=85&s=40c80868fec427beff79599afa2921cd" data-path="images/plugins/components/font_picker.png" />

## Compatibility

| Plugin type    | Availablity                  | Additional notes |
| -------------- | ---------------------------- | ---------------- |
| Content blocks | <Icon icon="square-check" /> |                  |
| Media source   | <Icon icon="square-xmark" /> |                  |

## Properties

<ParamField body="type" type="string" required="true">
  `fontFamily` - the type of the component
</ParamField>

<ParamField body="name" type="string" required="true">
  A unique internal-only identifier that is posted to an app's plugin server to share values inputted by the creator
</ParamField>

<ParamField body="label" type="string" required="true">
  Creator-facing identifier that is shown in the plugin environment
</ParamField>

<ParamField body="required" type="boolean">
  Determines whether the creator must select a font before proceeding
</ParamField>

<ParamField body="help" type="string">
  Brief creator-facing explanation that clarifies the component's purpose and usage.
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

## Best practices

### Automatic styling

When using the `font picker` for content blocks, alongside the settings object, Kit also shares data on the styles used within the email template - allowing your plugin to assume the styling of the email automatically, to make it feel as native as possible.

Details on the style data available can be found below:

<AccordionGroup>
  <Accordion title="Supported HTML elements">
    * p
    * h1
    * h2
    * h3
    * h4
    * h5
    * h6
    * ol
    * ul
    * blockquote
    * a
  </Accordion>

  <Accordion title="Shared styles">
    * "color",
    * "font-family",
    * "font-size",
    * "font-weight",
    * "letter-spacing",
    * "line-height",
    * "text-align",
    * "text-transform",
    * "margin-top",
    * "margin-right",
    * "margin-bottom",
    * "margin-left",
    * "padding-top",
    * "padding-right",
    * "padding-bottom",
    * "padding-left"
  </Accordion>

  <Accordion title="Example request">
    ```json  theme={null}
      {
        "settings": {
            "postId": "default-to-generosity-id-123",
            "favoriteColor": "#ff0000"
        },
        "styles": {
            "p": {
                "color": "rgb(45, 45, 47)",
                "font-family": "Charter, Georgia, Times, \"Times New Roman\", serif",
                "font-size": "18px",
                "font-weight": "400",
                "letter-spacing": "normal",
                "line-height": "27px",
                "text-align": "start",
                "text-transform": "none",
                "margin-top": "18px",
                "margin-right": "0px",
                "margin-bottom": "18px",
                "margin-left": "0px",
                "padding-top": "0px",
                "padding-right": "0px",
                "padding-bottom": "0px",
                "padding-left": "0px"
            },
            "h1": {
                "color": "rgb(0, 0, 0)",
                "font-family": "-apple-system, \"system-ui\", \"Segoe UI\", Roboto, Oxygen-Sans, Ubuntu, Cantarell, \"Helvetica Neue\", sans-serif",
                "font-size": "28px",
                "font-weight": "700",
                "letter-spacing": "normal",
                "line-height": "42px",
                "text-align": "start",
                "text-transform": "none",
                "margin-top": "0px",
                "margin-right": "0px",
                "margin-bottom": "0px",
                "margin-left": "0px",
                "padding-top": "0px",
                "padding-right": "0px",
                "padding-bottom": "0px",
                "padding-left": "0px"
            },
            "h2": {
                "color": "rgb(0, 0, 0)",
                "font-family": "-apple-system, \"system-ui\", \"Segoe UI\", Roboto, Oxygen-Sans, Ubuntu, Cantarell, \"Helvetica Neue\", sans-serif",
                "font-size": "21px",
                "font-weight": "700",
                "letter-spacing": "normal",
                "line-height": "31.5px",
                "text-align": "start",
                "text-transform": "none",
                "margin-top": "21px",
                "margin-right": "0px",
                "margin-bottom": "21px",
                "margin-left": "0px",
                "padding-top": "0px",
                "padding-right": "0px",
                "padding-bottom": "0px",
                "padding-left": "0px"
            },
            "h3": {
                "color": "rgb(0, 0, 0)",
                "font-family": "-apple-system, \"system-ui\", \"Segoe UI\", Roboto, Oxygen-Sans, Ubuntu, Cantarell, \"Helvetica Neue\", sans-serif",
                "font-size": "16.38px",
                "font-weight": "700",
                "letter-spacing": "normal",
                "line-height": "24.57px",
                "text-align": "start",
                "text-transform": "none",
                "margin-top": "16.38px",
                "margin-right": "0px",
                "margin-bottom": "16.38px",
                "margin-left": "0px",
                "padding-top": "0px",
                "padding-right": "0px",
                "padding-bottom": "0px",
                "padding-left": "0px"
            },
            "h4": {
                "color": "rgb(0, 0, 0)",
                "font-family": "-apple-system, \"system-ui\", \"Segoe UI\", Roboto, Oxygen-Sans, Ubuntu, Cantarell, \"Helvetica Neue\", sans-serif",
                "font-size": "14px",
                "font-weight": "700",
                "letter-spacing": "normal",
                "line-height": "21px",
                "text-align": "start",
                "text-transform": "none",
                "margin-top": "0px",
                "margin-right": "0px",
                "margin-bottom": "0px",
                "margin-left": "0px",
                "padding-top": "0px",
                "padding-right": "0px",
                "padding-bottom": "0px",
                "padding-left": "0px"
            },
            "h5": {
                "color": "rgb(0, 0, 0)",
                "font-family": "-apple-system, \"system-ui\", \"Segoe UI\", Roboto, Oxygen-Sans, Ubuntu, Cantarell, \"Helvetica Neue\", sans-serif",
                "font-size": "14px",
                "font-weight": "700",
                "letter-spacing": "normal",
                "line-height": "15.4px",
                "text-align": "start",
                "text-transform": "none",
                "margin-top": "0px",
                "margin-right": "0px",
                "margin-bottom": "0px",
                "margin-left": "0px",
                "padding-top": "0px",
                "padding-right": "0px",
                "padding-bottom": "0px",
                "padding-left": "0px"
            },
            "h6": {
                "color": "rgb(0, 0, 0)",
                "font-family": "-apple-system, \"system-ui\", \"Segoe UI\", Roboto, Oxygen-Sans, Ubuntu, Cantarell, \"Helvetica Neue\", sans-serif",
                "font-size": "14px",
                "font-weight": "400",
                "letter-spacing": "normal",
                "line-height": "21px",
                "text-align": "start",
                "text-transform": "none",
                "margin-top": "0px",
                "margin-right": "0px",
                "margin-bottom": "0px",
                "margin-left": "0px",
                "padding-top": "0px",
                "padding-right": "0px",
                "padding-bottom": "0px",
                "padding-left": "0px"
            },
            "ol": {
                "color": "rgb(45, 45, 47)",
                "font-family": "Charter, Georgia, Times, \"Times New Roman\", serif",
                "font-size": "18px",
                "font-weight": "400",
                "letter-spacing": "normal",
                "line-height": "27px",
                "text-align": "start",
                "text-transform": "none",
                "margin-top": "18px",
                "margin-right": "0px",
                "margin-bottom": "18px",
                "margin-left": "18px",
                "padding-top": "0px",
                "padding-right": "0px",
                "padding-bottom": "0px",
                "padding-left": "0px"
            },
            "ul": {
                "color": "rgb(45, 45, 47)",
                "font-family": "Charter, Georgia, Times, \"Times New Roman\", serif",
                "font-size": "18px",
                "font-weight": "400",
                "letter-spacing": "normal",
                "line-height": "27px",
                "text-align": "start",
                "text-transform": "none",
                "margin-top": "18px",
                "margin-right": "0px",
                "margin-bottom": "18px",
                "margin-left": "18px",
                "padding-top": "0px",
                "padding-right": "0px",
                "padding-bottom": "0px",
                "padding-left": "0px"
            },
            "blockquote": {
                "color": "rgb(55, 63, 69)",
                "font-family": "\"open sans\", \"helvetica neue\", Helvetica, Arial, sans-serif",
                "font-size": "17.5px",
                "font-weight": "400",
                "letter-spacing": "normal",
                "line-height": "25px",
                "text-align": "start",
                "text-transform": "none",
                "margin-top": "17.5px",
                "margin-right": "0px",
                "margin-bottom": "17.5px",
                "margin-left": "0px",
                "padding-top": "10px",
                "padding-right": "20px",
                "padding-bottom": "10px",
                "padding-left": "20px"
            },
            "a": {
                "color": "rgb(32, 177, 150)",
                "font-family": "\"open sans\", \"helvetica neue\", Helvetica, Arial, sans-serif",
                "font-size": "14px",
                "font-weight": "400",
                "letter-spacing": "normal",
                "line-height": "20px",
                "text-align": "start",
                "text-transform": "none",
                "margin-top": "0px",
                "margin-right": "0px",
                "margin-bottom": "0px",
                "margin-left": "0px",
                "padding-top": "0px",
                "padding-right": "0px",
                "padding-bottom": "0px",
                "padding-left": "0px"
            }
        }
    }
    ```
  </Accordion>
</AccordionGroup>

<RequestExample>
  ```json JSON setting theme={null}
    {
      "type": "fontFamily",
      "name": "paragraph_font",
      "label": "Paragraph font",
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
        "paragraph_font": {
          "fontFamily": "'Courier New', Courier, monospace",
          "fontWeight": 400
        }
        // ...additional plugin settings
      }
      // ...plugin-specific additional data
    }
  ```
</ResponseExample>


Built with [Mintlify](https://mintlify.com).