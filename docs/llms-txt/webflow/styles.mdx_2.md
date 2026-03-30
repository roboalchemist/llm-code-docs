# Source: https://developers.webflow.com/mcp/reference/designer/styles.mdx

***

title: Styles
description: 'Create and manage styles, classes, and CSS properties in the Webflow Designer'
--------------------------------------------------------------------------------------------

Create and manage styles, classes, and CSS properties in the Webflow Designer using the Styles tools. These tools let you create new styles, update existing ones, and manage style properties across breakpoints.

<Warning>
  The MCP Companion App must be open in the Webflow Designer for these tools to function.
</Warning>

***

## Style tool

Create and manage classes and CSS properties in the Webflow Designer using the Style tool.

**Tool:** `style_tool`

<Card>
  <ParamField path="siteId" type="string" required={true}>
    Unique identifier for the site.
  </ParamField>

  <ParamField path="actions" type="array" required={true}>
    An array of style actions to perform. See action examples below.
  </ParamField>
</Card>

***

### Create style

Create a new style with specified properties.

<Card>
  <ParamField path="name" type="string" required={true}>
    The name of the new style.
  </ParamField>

  <ParamField path="properties" type="array" required={true}>
    An array of property objects.

    <Accordion title="+ Show Property Properties">
      <ParamField path="property_name" type="string" required={true}>
        The CSS property name (use longhand, e.g., `margin-top`).
      </ParamField>

      <ParamField path="property_value" type="string" required={false}>
        The static value for the property.
      </ParamField>

      <ParamField path="variable_as_value" type="string" required={false}>
        The ID of a variable to use as the value.
      </ParamField>
    </Accordion>
  </ParamField>

  <ParamField path="parent_style_name" type="string" required={false}>
    The name of a parent style to create a combo class.
  </ParamField>
</Card>

<CodeGroup>
  ```json {{ title: 'Action Example' }}
  {
    "actions": [
      {
        "create_style": {
          "name": "Primary Button",
          "properties": [
            { "property_name": "background-color", "property_value": "#007bff" }
          ]
        }
      }
    ]
  }
  ```
</CodeGroup>

### Get styles

Retrieve a list of styles from the site.

<Card>
  <ParamField path="query" type="'all' | 'filtered'" required={true}>
    Specify "all" to get all styles or "filtered" to use `filter_ids`.
  </ParamField>

  <ParamField path="skip_properties" type="boolean" required={false}>
    If true, the response will not include style properties.
  </ParamField>

  <ParamField path="include_all_breakpoints" type="boolean" required={false}>
    If true, includes styles from all breakpoints (can be data-intensive).
  </ParamField>

  <ParamField path="filter_ids" type="array" required={false}>
    An array of style IDs to retrieve when `query` is "filtered."
  </ParamField>
</Card>

<CodeGroup>
  ```json {{ title: 'Action Example' }}
  {
    "actions": [
      {
        "get_styles": {
          "query": "all",
          "skip_properties": true
        }
      }
    ]
  }
  ```
</CodeGroup>

### Update style

Update a style's properties for a specific breakpoint and pseudo-class.

<Card>
  <ParamField path="style_name" type="string" required={true}>
    The name of the style to update.
  </ParamField>

  <ParamField path="breakpoint_id" type="string" required={false}>
    The breakpoint to target (e.g., `main`, `medium`, `tiny`). Defaults to `main`.
  </ParamField>

  <ParamField path="pseudo" type="string" required={false}>
    The pseudo-class to target (e.g., `hover`, `focus`). Defaults to `noPseudo`.
  </ParamField>

  <ParamField path="properties" type="array" required={false}>
    An array of property objects to add or update.
  </ParamField>

  <ParamField path="remove_properties" type="array" required={false}>
    An array of property names to remove.
  </ParamField>
</Card>

<CodeGroup>
  ```json {{ title: 'Action Example' }}
  {
    "actions": [
      {
        "update_style": {
          "style_name": "Primary Button",
          "pseudo": "hover",
          "properties": [
            { "property_name": "background-color", "property_value": "#0056b3" }
          ]
        }
      }
    ]
  }
  ```
</CodeGroup>

***

## Learn about Webflow styles and supported CSS properties

A tool, that when called, will get a list of all CSS properties supported by the Webflow Designer.

**Tool:** `de_learn_more_about_styles`
