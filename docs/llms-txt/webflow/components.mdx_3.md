# Source: https://developers.webflow.com/mcp/v1.0.0-beta/reference/designer/components.mdx

***

title: Components
description: Create and manage reusable components in the Webflow Designer.
---------------------------------------------------------------------------

Designer Components tools enable you to create reusable components, insert component instances on pages, and manage component definitions in the Designer.

<Warning>
  Designer tools require the MCP Bridge App to be open in the Webflow Designer. Ensure it's connected before using these tools.
</Warning>

## When to use

Use Designer Components tools to:

* **Create reusable components**: Convert elements into components
* **Insert instances**: Add component instances to pages
* **Edit components**: Open component view for modifications
* **Manage components**: Rename and organize components
* **Check component context**: Verify if you're in component edit mode

## Tool details

**Tool name**: `de_component_tool`

## Available actions

### Check if inside component view

Determine whether you're currently viewing a component for editing.

**Action**: `check_if_inside_component_view`

**Parameters**:

| Parameter | Type   | Required | Description     |
| --------- | ------ | -------- | --------------- |
| `siteId`  | string | Yes      | Site identifier |

**Returns**: Boolean indicating if you're in component view

**Example usage**:

```
Am I currently editing a component?
```

<Tip>
  Use this before performing operations to ensure you're in the correct context (page view vs. component view).
</Tip>

### Transform element to component

Convert an existing element into a reusable component.

**Action**: `transform_element_to_component`

**Parameters**:

| Parameter       | Type   | Required | Description                |
| --------------- | ------ | -------- | -------------------------- |
| `siteId`        | string | Yes      | Site identifier            |
| `elementId`     | string | Yes      | Element to convert         |
| `componentName` | string | Yes      | Name for the new component |

**Example usage**:

```
Transform the selected card element into a reusable "Product Card" component
```

<Note>
  After transformation, the original element becomes a component instance, and a component definition is created.
</Note>

### Insert component instance

Add a component instance to the active page.

**Action**: `insert_component_instance`

**Parameters**:

| Parameter         | Type   | Required | Description                     |
| ----------------- | ------ | -------- | ------------------------------- |
| `siteId`          | string | Yes      | Site identifier                 |
| `parentElementId` | string | Yes      | Parent element for the instance |
| `componentId`     | string | Yes      | Component to instantiate        |
| `position`        | string | Yes      | "append" or "prepend"           |

**Example usage**:

```
Insert a Product Card component instance into the products grid
```

### Open component view

Launch component view to edit a component definition.

**Action**: `open_component_view`

**Parameters**:

| Parameter             | Type   | Required | Description      |
| --------------------- | ------ | -------- | ---------------- |
| `siteId`              | string | Yes      | Site identifier  |
| `componentInstanceId` | string | Yes      | Instance to edit |

**Example usage**:

```
Open the component view to edit this Product Card
```

<Warning>
  Opening component view changes your editing context. All subsequent element operations will affect the component definition, not the page.
</Warning>

### Close component view

Exit component view and return to page view.

**Action**: `close_component_view`

**Parameters**:

| Parameter | Type   | Required | Description     |
| --------- | ------ | -------- | --------------- |
| `siteId`  | string | Yes      | Site identifier |

**Example usage**:

```
Close component view and return to the page
```

### Get all components

Retrieve all available components (requires Webflow Designer connection).

**Action**: `get_all_components`

**Parameters**:

| Parameter | Type   | Required | Description     |
| --------- | ------ | -------- | --------------- |
| `siteId`  | string | Yes      | Site identifier |

**Returns**: List of all components with IDs and metadata

**Example usage**:

```
List all components in this site
```

### Rename component

Change a component's display name.

**Action**: `rename_component`

**Parameters**:

| Parameter     | Type   | Required | Description         |
| ------------- | ------ | -------- | ------------------- |
| `siteId`      | string | Yes      | Site identifier     |
| `componentId` | string | Yes      | Component to rename |
| `name`        | string | Yes      | New component name  |

**Example usage**:

```
Rename component "Card 1" to "Product Card"
```

## Best practices

<Accordion title="Plan component structure first">
  Before creating a component:

  * Identify what elements it needs
  * Determine which values should be properties
  * Consider reusability across pages
  * Plan for variations

  Well-planned components are more useful.
</Accordion>

<Accordion title="Use semantic naming">
  Name components by purpose:

  * ✅ `Navigation-Primary`, `Card-Product`, `Button-CTA`
  * ❌ `Component1`, `Div-Block`, `Element`

  Clear names make components easy to find and use.
</Accordion>

<Accordion title="Keep components focused">
  Each component should have a single, clear purpose:

  * ✅ Product Card (shows product info)
  * ❌ Everything Card (shows products, blog posts, team members)

  Focused components are more maintainable.
</Accordion>

<Accordion title="Verify context before editing">
  Always check if you're in component view before making changes:

  ```
  1. Check if inside component view
  2. If yes, close it first
  3. Open the correct component
  4. Make edits
  5. Close component view
  ```

  This prevents editing the wrong component.
</Accordion>

<Accordion title="Test instances after changes">
  After updating a component definition:

  * Check multiple instances
  * Verify on different pages
  * Test responsive behavior
  * Ensure no layout breaks

  Component changes affect many places.
</Accordion>

## Limitations

* **Context switching**: Opening component view changes editing context
* **Property system**: Limited property configuration via tools
* **Designer required**: Must have Bridge App connection
* **No nested component editing**: Cannot edit nested components directly

<Warning>
  When you open component view, you're editing the component definition. Changes affect ALL instances of that component across your site.
</Warning>

## Related tools

<Cards>
  <Card
    title="Elements"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/PageBuilding.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/PageBuilding.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/v1.0.0-beta/tools/designer/elements"
  >
    Build component structures
  </Card>

  <Card
    title="Styles"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Styles.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Styles.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/v1.0.0-beta/tools/designer/styles"
  >
    Style components
  </Card>

  <Card
    title="Data API Components"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Components.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Components.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/v1.0.0-beta/tools/data/components"
  >
    Manage component content for localization
  </Card>

  <Card
    title="Pages"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Blog.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Blog.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/v1.0.0-beta/tools/designer/pages"
  >
    Add components to pages
  </Card>
</Cards>
