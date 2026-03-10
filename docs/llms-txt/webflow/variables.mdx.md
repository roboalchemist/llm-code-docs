# Source: https://developers.webflow.com/mcp/reference/designer/variables.mdx

***

title: Variables
description: 'Create and manage design variables for colors, sizes, fonts, and more'
------------------------------------------------------------------------------------

# Variables

Create and manage design variables for colors, sizes, fonts, and other design tokens in the Webflow Designer. Variables function like CSS custom properties and can be linked to styles.

<Warning>
  The MCP Companion App must be open in the Webflow Designer for these tools to function.
</Warning>

## Variable tool

Perform actions like creating variable collections, modes, and variables of different types.

**Tool:** `variable_tool`

**Parameters:**

* `siteId` (required): Unique identifier for the site
* `actions` (required): Array of variable actions

### Create variable collection

Create a new variable collection to organize related variables.

**Action:** `create_variable_collection`

**Parameters:**

* `name` (required): Name of the variable collection

**Returns:** Created collection object with ID

### Create variable mode

Create a new variable mode in a variable collection. Modes allow you to define different values for the same variables (e.g., light/dark themes).

**Action:** `create_variable_mode`

**Parameters:**

* `variable_collection_id` (required): ID of the variable collection
* `name` (required): Name of the variable mode

**Returns:** Created mode object with ID

### Get variable collections

Get all variable collections and their modes.

**Action:** `get_variable_collections`

**Parameters:**

* `query` (required): `"all"` to get all collections, or `"filtered"` for filtered results
* `filter_collections_by_ids` (optional): Array of collection IDs to filter by

**Returns:** Array of variable collection objects with their modes

### Get variables

Get all variables in a variable collection and their modes.

**Action:** `get_variables`

**Parameters:**

* `variable_collection_id` (required): ID of the variable collection
* `include_all_modes` (optional): Whether to include all modes
* `filter_variables_by_ids` (optional): Array of variable IDs to filter by

**Returns:** Array of variable objects with their values across modes

## Create variables

Create variables of different types. All create variable actions share similar parameters.

### Create color variable

Create a new color variable.

**Action:** `create_color_variable`

**Parameters:**

* `variable_collection_id` (required): ID of the variable collection
* `variable_name` (required): Name of the variable
* `value` (required): Value object with:
  * `static_value` (optional): Color value (hex, RGB, etc.)
  * `existing_variable_id` (optional): ID of another variable to bind to

**Returns:** Created variable object

### Create size variable

Create a new size variable with a numeric value and unit.

**Action:** `create_size_variable`

**Parameters:**

* `variable_collection_id` (required): ID of the variable collection
* `variable_name` (required): Name of the variable
* `value` (required): Value object with:
  * `static_value` (optional): Object with `value` (number) and `unit` (string)
  * `existing_variable_id` (optional): ID of another variable to bind to

**Returns:** Created variable object

### Create number variable

Create a new number variable.

**Action:** `create_number_variable`

**Parameters:**

* `variable_collection_id` (required): ID of the variable collection
* `variable_name` (required): Name of the variable
* `value` (required): Value object with:
  * `static_value` (optional): Numeric value
  * `existing_variable_id` (optional): ID of another variable to bind to

**Returns:** Created variable object

### Create percentage variable

Create a new percentage variable.

**Action:** `create_percentage_variable`

**Parameters:**

* `variable_collection_id` (required): ID of the variable collection
* `variable_name` (required): Name of the variable
* `value` (required): Value object with:
  * `static_value` (optional): Percentage value (number)
  * `existing_variable_id` (optional): ID of another variable to bind to

**Returns:** Created variable object

### Create font family variable

Create a new font family variable.

**Action:** `create_font_family_variable`

**Parameters:**

* `variable_collection_id` (required): ID of the variable collection
* `variable_name` (required): Name of the variable
* `value` (required): Value object with:
  * `static_value` (optional): Font family name
  * `existing_variable_id` (optional): ID of another variable to bind to

**Returns:** Created variable object

## Update variables

Update variables of different types. All update variable actions share similar parameters.

### Update color variable

Update a color variable's value.

**Action:** `update_color_variable`

**Parameters:**

* `variable_collection_id` (required): ID of the variable collection
* `variable_id` (required): ID of the variable to update
* `mode_id` (optional): ID of the mode to update (if not provided, updates all modes)
* `value` (required): Value object with `static_value` or `existing_variable_id`

**Returns:** Updated variable confirmation

### Update size variable

Update a size variable's value.

**Action:** `update_size_variable`

**Parameters:**

* `variable_collection_id` (required): ID of the variable collection
* `variable_id` (required): ID of the variable to update
* `mode_id` (optional): ID of the mode to update
* `value` (required): Value object with `static_value` or `existing_variable_id`

**Returns:** Updated variable confirmation

### Update number variable

Update a number variable's value.

**Action:** `update_number_variable`

**Parameters:**

* `variable_collection_id` (required): ID of the variable collection
* `variable_id` (required): ID of the variable to update
* `mode_id` (optional): ID of the mode to update
* `value` (required): Value object with `static_value` or `existing_variable_id`

**Returns:** Updated variable confirmation

### Update percentage variable

Update a percentage variable's value.

**Action:** `update_percentage_variable`

**Parameters:**

* `variable_collection_id` (required): ID of the variable collection
* `variable_id` (required): ID of the variable to update
* `mode_id` (optional): ID of the mode to update
* `value` (required): Value object with `static_value` or `existing_variable_id`

**Returns:** Updated variable confirmation

### Update font family variable

Update a font family variable's value.

**Action:** `update_font_family_variable`

**Parameters:**

* `variable_collection_id` (required): ID of the variable collection
* `variable_id` (required): ID of the variable to update
* `mode_id` (optional): ID of the mode to update
* `value` (required): Value object with `static_value` or `existing_variable_id`

**Returns:** Updated variable confirmation

## Variable binding

Variables can be bound to other variables using `existing_variable_id`. This creates a reference relationship where one variable's value is derived from another. This is useful for creating design systems where related values should stay in sync.

## Example workflow

1. Create a variable collection to organize variables
2. Create variable modes if you need theme variations
3. Create variables of different types (colors, sizes, fonts)
4. Bind variables to other variables as needed
5. Use variables in styles via `variable_as_value` in style properties
6. Update variable values to change them across all uses

## Best practices

* Organize related variables into collections
* Use modes for theme variations (light/dark, etc.)
* Bind related variables to maintain consistency
* Use descriptive names for variables
* Update variables rather than individual style properties when values need to change globally
