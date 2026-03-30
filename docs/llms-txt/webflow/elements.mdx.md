# Source: https://developers.webflow.com/mcp/reference/designer/elements.mdx

***

title: Elements
description: Create and manipulate elements on the Webflow Designer canvas
--------------------------------------------------------------------------

Create and manipulate elements on the Webflow Designer canvas using the Elements tools. These tools work with the live Designer interface to build and modify page layouts.

<Warning>
  The MCP Companion App must be open in the Webflow Designer for these tools to function.
</Warning>

***

## Element Builder

Use the Element Builder to create nested elements on the current page. Each action supports up to three levels of nesting. For more complex layouts, make multiple calls to `element_builder` to construct the element tree incrementally.

<Note>
  After an element is created, it is not automatically selected. Use the `element_tool` with the `select_element` action to select and inspect it.
</Note>

**Tool:** `element_builder`

<Card>
  <ParamField path="siteId" type="string" required={true}>
    Unique identifier for the site.
  </ParamField>

  <ParamField path="actions" type="array" required={true}>
    An array of element creation actions.

    <Accordion title="+ Show Action Properties">
      <ParamField path="parentElementId" type="object" required={true}>
        Object containing the `component` and `element` IDs of the parent.
      </ParamField>

      <ParamField path="creationPosition" type="'append' | 'prepend'" required={true}>
        Position to create the new element relative to the parent.
      </ParamField>

      <ParamField path="elementSchema" type="object" required={true}>
        The definition of the element to create.

        <Accordion title="+ Show Schema Properties">
          <ParamField path="type" type="string" required={true}>
            The element type (e.g., "div," "section," "h1," "p").
          </ParamField>

          <ParamField path="children" type="array" required={false}>
            An array of nested child `elementSchema` objects.
            <Note>Only container-type elements like `div`, `section`, and `container` can have children. Element nesting is limited to 3 levels deep.</Note>
          </ParamField>
        </Accordion>
      </ParamField>
    </Accordion>
  </ParamField>
</Card>

<CodeGroup>
  ```json Request Example
  {
    "siteId": "628f4b034872242526c8f62a",
    "actions": [
      {
        "parentElementId": { "component": "...", "element": "..." },
        "creationPosition": "append",
        "elementSchema": {
          "type": "div",
          "children": [
            { "type": "h1", "children": [{ "type": "text", "text": "Hello World" }] }
          ]
        }
      }
    ]
  }
  ```
</CodeGroup>

***

## Element Tool

The element tool supports multiple actions on elements, such as reading properties, selecting, and updating.

**Tool:** `element_tool`

<Card>
  <ParamField path="siteId" type="string" required={true}>
    Unique identifier for the site.
  </ParamField>

  <ParamField path="actions" type="array" required={true}>
    An array of element actions to perform. See action examples below.
  </ParamField>
</Card>

### Actions

#### Get All Elements

Get a list of all elements on the current page.

<Card>
  <ParamField path="query" type="'all'" required={true}>
    Set to "all" to retrieve all elements.
  </ParamField>

  <ParamField path="includeStyleProperties" type="boolean" required={false}>
    Whether to include style properties in the response.
  </ParamField>

  <ParamField path="includeAllBreakpointStyles" type="boolean" required={false}>
    Whether to include styles for all breakpoints.
  </ParamField>
</Card>

<CodeGroup>
  ```json title="Action Example"
  {
    "actions": [
      {
        "getAllElements": {
          "query": "all",
          "includeStyleProperties": false
        }
      }
    ]
  }
  ```
</CodeGroup>

#### Get Selected Element

Get detailed information about the currently selected element.

<CodeGroup>
  ```json title="Action Example"
  {
    "actions": [
      { "getSelectedElement": true }
    ]
  }
  ```
</CodeGroup>

#### Select Element

Select an element on the canvas by its ID.

<Card>
  <ParamField path="component" type="string" required={true}>
    Component ID.
  </ParamField>

  <ParamField path="element" type="string" required={true}>
    Element ID.
  </ParamField>
</Card>

<CodeGroup>
  ```json title="Action Example"
  {
    "actions": [
      {
        "selectElement": {
          "component": "...",
          "element": "..."
        }
      }
    ]
  }
  ```
</CodeGroup>

#### Add or Update Attributes

Add or update attributes on an element.

<Card>
  <ParamField path="component" type="string" required={true}>
    Component ID.
  </ParamField>

  <ParamField path="element" type="string" required={true}>
    Element ID.
  </ParamField>

  <ParamField path="attributes" type="array" required={true}>
    An array of attribute objects, each with a `name` and `value`.
  </ParamField>
</Card>

<Note>
  This action is only valid if the element's metadata shows 

  `canHaveAttributes: true`

  .
</Note>

<CodeGroup>
  ```json title="Action Example"
  {
    "actions": [
      {
        "addOrUpdateAttribute": {
          "component": "...",
          "element": "...",
          "attributes": [{ "name": "data-custom", "value": "123" }]
        }
      }
    ]
  }
  ```
</CodeGroup>

#### Set Text

Set the text content for a text-based element (e.g., "p," "h1," "span").

<Card>
  <ParamField path="component" type="string" required={true}>
    Component ID.
  </ParamField>

  <ParamField path="element" type="string" required={true}>
    Element ID.
  </ParamField>

  <ParamField path="text" type="string" required={true}>
    The text content to set.
  </ParamField>
</Card>

<CodeGroup>
  ```json title="Action Example"
  {
    "actions": [
      {
        "setText": {
          "component": "...",
          "element": "...",
          "text": "New Heading Text"
        }
      }
    ]
  }
  ```
</CodeGroup>

#### Remove Attribute

Remove one or more attributes from an element.

<Card>
  <ParamField path="component" type="string" required={true}>
    Component ID.
  </ParamField>

  <ParamField path="element" type="string" required={true}>
    Element ID.
  </ParamField>

  <ParamField path="attribute_names" type="array" required={true}>
    An array of attribute names to remove.
  </ParamField>
</Card>

<Note>
  This action is only valid if the element's metadata shows 

  `canHaveAttributes: true`

  .
</Note>

<CodeGroup>
  ```json title="Action Example"
  {
    "actions": [
      {
        "remove_attribute": {
          "component": "...",
          "element": "...",
          "attribute_names": ["data-custom"]
        }
      }
    ]
  }
  ```
</CodeGroup>

#### Update ID Attribute

Update the HTML `id` attribute of an element.

<Card>
  <ParamField path="component" type="string" required={true}>
    Component ID.
  </ParamField>

  <ParamField path="element" type="string" required={true}>
    Element ID.
  </ParamField>

  <ParamField path="new_id" type="string" required={true}>
    The new ID to set.
  </ParamField>
</Card>

<Note>
  Do not include the 

  `#`

   character in the 

  `new_id`

   string.
</Note>

<CodeGroup>
  ```json title="Action Example"
  {
    "actions": [
      {
        "update_id_attribute": {
          "component": "...",
          "element": "...",
          "new_id": "my-unique-id"
        }
      }
    ]
  }
  ```
</CodeGroup>

#### Set Link

Set the link for an element like a `Link Block`, `Button`, or `Text Link`.

<Card>
  <ParamField path="component" type="string" required={true}>
    Component ID.
  </ParamField>

  <ParamField path="element" type="string" required={true}>
    Element ID.
  </ParamField>

  <ParamField path="linkType" type="'url' | 'file' | 'page' | 'element' | 'email' | 'phone'" required={true}>
    The type of link to set.
  </ParamField>

  <ParamField path="link" type="string" required={true}>
    The link destination. The format depends on `linkType`.
  </ParamField>
</Card>

<CodeGroup>
  ```json title="Action Example"
  {
    "actions": [
      {
        "set_link": {
          "component": "...",
          "element": "...",
          "linkType": "url",
          "link": "https://webflow.com"
        }
      }
    ]
  }
  ```
</CodeGroup>

#### Set Heading Level

Change the heading level of a `Heading` element (e.g., from `h2` to `h3`).

<Card>
  <ParamField path="component" type="string" required={true}>
    Component ID.
  </ParamField>

  <ParamField path="element" type="string" required={true}>
    Element ID.
  </ParamField>

  <ParamField path="heading_level" type="1 | 2 | 3 | 4 | 5 | 6" required={true}>
    The heading level to apply (1-6).
  </ParamField>
</Card>

<CodeGroup>
  ```json title="Action Example"
  {
    "actions": [
      {
        "set_heading_level": {
          "component": "...",
          "element": "...",
          "heading_level": 2
        }
      }
    ]
  }
  ```
</CodeGroup>

#### Set Style

Apply one or more existing styles to an element.

<Card>
  <ParamField path="component" type="string" required={true}>
    Component ID.
  </ParamField>

  <ParamField path="element" type="string" required={true}>
    Element ID.
  </ParamField>

  <ParamField path="styleNames" type="array" required={true}>
    An array of style names to apply.
  </ParamField>
</Card>

<Note>
  This action replaces all existing styles on the element. To create styles, use the 

  `style_tool`

  .
</Note>

<CodeGroup>
  ```json title="Action Example"
  {
    "actions": [
      {
        "setStyle": {
          "component": "...",
          "element": "...",
          "styleNames": ["Button", "Primary-Button"]
        }
      }
    ]
  }
  ```
</CodeGroup>

#### Set Image Asset

Set the image source for an `Image` element.

<Card>
  <ParamField path="component" type="string" required={true}>
    Component ID.
  </ParamField>

  <ParamField path="element" type="string" required={true}>
    Element ID of the Image.
  </ParamField>

  <ParamField path="imageAssetId" type="string" required={true}>
    The ID of the asset to use.
  </ParamField>
</Card>

<Note>
  Retrieve available asset IDs using 

  `asset_tool`

  .
</Note>

<CodeGroup>
  ```json title="Action Example"
  {
    "actions": [
      {
        "setImageAsset": {
          "component": "...",
          "element": "...",
          "imageAssetId": "628f4b034872242526c8f65c"
        }
      }
    ]
  }
  ```
</CodeGroup>
