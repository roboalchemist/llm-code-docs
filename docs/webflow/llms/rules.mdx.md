# Source: https://developers.webflow.com/mcp/v1.0.0-beta/reference/utility-tools/rules.mdx

***

title: Rules
description: Essential guidelines and best practices for using Webflow MCP tools correctly.
-------------------------------------------------------------------------------------------

The Rules tool provides comprehensive guidelines for working with Webflow's MCP tools. It should be consulted before performing complex operations to ensure you're following best practices and avoiding common pitfalls.

<Warning>
  Always consult the Rules tool before complex workflows. It helps prevent errors and ensures proper tool usage across Data and Designer APIs.
</Warning>

## When to use

Consult the Rules tool when you need to:

* **Plan complex workflows**: Understand the correct sequence of operations
* **Avoid common mistakes**: Learn about pitfalls before encountering them
* **Understand tool constraints**: Know what each tool can and cannot do
* **Choose the right tool**: Decide between Data API and Designer API tools

## Tool details

**Tool name**: `rules`

**Parameters**: None required

**Returns**: Comprehensive guidelines covering all Webflow MCP tool categories

## Core principles

### Data vs Designer tools

**Data Tools** are REST API calls that work with site content and structure:

* Don't require the Designer to be open
* Work with collections, items, pages, and site metadata
* Changes may not reflect immediately in the Designer

**Designer Tools** are UI tools that manipulate the canvas:

* Require the Designer companion app to be open
* Work with elements, styles, and visual properties
* Changes reflect in real-time in the Designer

### Planning before execution

Always plan your approach before invoking tools:

1. **Understand your goal**: Know exactly what you want to achieve
2. **Identify required tools**: Determine which tools you'll need
3. **Determine the sequence**: Plan the order of operations
4. **Check constraints**: Verify all prerequisites are met

<Tip>
  Invoking tools randomly without planning often leads to errors and unexpected results.
</Tip>

## Element management

### Selection and inspection

**Get the currently selected element:**

```
element_tool > get_selected_element
```

**Select a specific element:**

```
element_tool > select_element
```

Provide the element ID to select it.

**Get all page elements:**

```
element_tool > get_all_elements
```

<Warning>
  Set breakpoint and style flags to `false` to prevent context overflow when retrieving all elements.
</Warning>

### Attributes

**Add or update attributes:**
Only works on elements where `canHaveAttributes: true`. Check element details first.

**Remove attributes:**

```
element_tool > remove_attribute
```

**Update custom IDs:**

```
element_tool > update_id_attribute
```

<Note>
  Don't include the '#' character when updating custom IDs.
</Note>

### Styling

**Apply existing styles:**

```
element_tool > set_style
```

Combo classes are supported.

**Configure links:**
For Button, TextLink, or LinkBlock elements:

```
element_tool > set_link
```

<Warning>
  **Never use CSS shorthand properties**. Always use longhand:

  * ✅ `margin-top`, `margin-bottom`, `margin-left`, `margin-right`
  * ❌ `margin`
</Warning>

### Special elements

**Set image assets:**
For Image elements only:

```
element_tool > set_image_asset
```

Requires a valid `asset_id`.

**Update heading levels:**
For heading elements, set level 1-6:

```
element_tool > set_heading_level
```

## Asset operations

### Creating folders

```
asset_tool > create_folder
```

For nested structures, specify `parent_folder_id`.

### Retrieving assets

```
asset_tool > get_all_assets_and_folders
```

**Query options:**

* `"all"` - Get everything
* `"folders"` - Only folders
* `"assets"` - Only assets

<Tip>
  Use specific queries to limit data retrieval and prevent context overflow.
</Tip>

### Updating assets

```
asset_tool > update_asset
```

Can update:

* Asset name
* Folder location
* Alt text

## Page operations

### Creating pages

```
page_tool > create_page
```

<Note>
  The system automatically switches to the newly created page after creation.
</Note>

### Switching pages

```
page_tool > switch_page
```

Requires `page_id` parameter.

### Creating page folders

```
page_tool > create_page_folder
```

Optional `parent_id` for nested folder structures.

## Style management

### Creating styles

```
style_tool > create_style
```

For combo classes, specify `parent_style_name`.

### Updating styles

```
style_tool > update_style
```

Main breakpoint defaults apply unless specified otherwise.

### Breakpoint hierarchy

Understanding the breakpoint system:

| Breakpoint | Min Width   | Description                |
| ---------- | ----------- | -------------------------- |
| `xxl`      | 1920px+     | Extra extra large displays |
| `xl`       | 1440px+     | Extra large displays       |
| `large`    | 1280px+     | Large displays             |
| `main`     | All devices | Base/desktop styles        |
| `medium`   | ≤991px      | Tablets                    |
| `small`    | ≤767px      | Mobile landscape           |
| `tiny`     | ≤478px      | Mobile portrait            |

<Warning>
  Always use longhand CSS properties, not shorthand, when working with styles.
</Warning>

## Variable system

### Collections and modes

**Create a variable collection:**

```
variable_tool > create_variable_collection
```

**Add modes to a collection:**

```
variable_tool > create_variable_mode
```

### Creating variables

Use type-specific tools for different variable types:

* **Color**: `create_color_variable`
* **Size**: `create_size_variable`
* **Number**: `create_number_variable`
* **Percentage**: `create_percentage_variable`
* **Font Family**: `create_font_family_variable`

<Note>
  Variables function like CSS custom properties and are linked to styles.
</Note>

## CMS operations

### Collections

**Retrieve collections:**

```
cms_tool > get_collection_list
```

**Create collections:**

```
cms_tool > create_collection
```

### Fields

Create fields using appropriate tools based on field type:

* Static fields (text, number, etc.)
* Option fields (dropdown, radio)
* Reference fields (linking to other collections)

### Items

**Create items:**

```
cms_tool > create_collection_item_live
```

**Update items:**

```
cms_tool > update_collection_item_live
```

**Publish items:**
Include collection\_id and proper data structures.

<Tip>
  Use "live" tools to publish changes immediately, or draft tools to stage changes for later publishing.
</Tip>

## Element creation workflow

Follow this workflow when creating elements:

1. **Plan your element structure**
   * Decide on element type
   * Identify required styles
   * Determine necessary attributes

2. **Create styles first** (if needed)
   ```
   style_tool > create_style
   ```

3. **Use element builder**
   ```
   element_builder
   ```
   Provide element type, styles, and attributes.

4. **Select the new element**
   <Warning>
     Newly created elements are NOT automatically selected. You must explicitly select them:

     ```
     element_tool > select_element
     ```
   </Warning>

5. **Add children** (if applicable)
   <Note>
     Only Container, Section, and DivBlock elements support children.
   </Note>

## Best practices

<Accordion title="Check capabilities before operations">
  Before modifying an element, check its capabilities:

  * `canHaveAttributes` - Can accept custom attributes
  * `canHaveChildren` - Can contain child elements
  * `canHaveStyles` - Can have styles applied
</Accordion>

<Accordion title="Use appropriate tool types">
  * **Data API tools**: For content and structure (collections, items, pages)
  * **Designer API tools**: For visual design (elements, styles, assets)
  * **Utility tools**: For guidance and documentation (rules, AI chat)
</Accordion>

<Accordion title="Handle site IDs explicitly">
  Always pass site IDs when required. Don't assume the system will use a default site.
</Accordion>

<Accordion title="Minimize context with filters">
  When retrieving large datasets, use filters and query parameters to limit results:

  * Disable breakpoint data when not needed
  * Disable style data when not needed
  * Use specific asset queries
</Accordion>

## Related tools

<Cards>
  <Card
    title="AI Chat"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Ai.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Ai.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/v1.0.0-beta/tools/utility/ai-chat"
  >
    Ask questions about Webflow APIs
  </Card>

  <Card
    title="Elements"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Elements.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Elements.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/v1.0.0-beta/tools/designer/elements"
  >
    Create and modify elements
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
    Manage styles and classes
  </Card>

  <Card
    title="Variables"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Variables.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Variables.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/v1.0.0-beta/tools/designer/variables"
  >
    Work with design variables
  </Card>

  <Card
    title="CMS Collections"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Collections.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Collections.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/v1.0.0-beta/tools/data/collections"
  >
    Manage CMS collections
  </Card>
</Cards>
