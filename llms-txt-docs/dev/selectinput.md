# Source: https://dev.writer.com/components/selectinput.md

# Select Input

A user input component that allows users to select a single or multiples value(s) from a searchable list of options.

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/selectinput.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=2b485ff4fe89672ae95afdc12024423c" data-og-width="522" width="522" data-og-height="160" height="160" data-path="framework/public/components/selectinput.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/selectinput.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=bb22142e3d49533e21fe7f78f67c8136 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/selectinput.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=d961fe58c374df6cc8ecf760eb119b82 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/selectinput.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=beff7cbaa0fa951e31b51b3d4b2aa8cd 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/selectinput.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=2f135bd67d295cd4852802152f84ecd1 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/selectinput.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=32549e353a37f83b19a5abc38129e7b5 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/selectinput.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=abccf6a0ef3f899b63cd35152c01583a 2500w" />

## Overview

The **Select Input** component provides a dropdown interface for selecting single or multiple values from a searchable list of options. It offers a clean, accessible way to present multiple choices while maintaining a compact interface.

Select inputs are essential for forms and interfaces where users need to choose from predefined options. They provide better user experience than text inputs for categorical data and help ensure data consistency and validation.

## Common use cases

* **Form selections**: Choose options in registration and configuration forms
* **Category filtering**: Filter content by categories or types with single or multiple selections
* **Configuration settings**: Select preferences and settings from predefined options
* **Data entry**: Choose from standardized options for consistent data entry

## How it works

1. **Label**: Provide a clear label for the select input field
2. **Options**: Define available choices as key-value pairs in JSON format
3. **Dropdown**: Display options in a searchable dropdown interface
4. **Selection**: Allow users to select one or multiple options from the list
5. **Binding**: Connect to a state variable to store the selected value
6. **Events**: Trigger workflows when selections change

The component automatically updates the bound state variable when users make selections, and can trigger events for real-time processing or validation.

## Configuration options

### Basic settings

* **Label**: Text label displayed preceding the select input field
* **Allow Multi-select**: Toggle to enable selection of multiple options from the dropdown (default: off)
* **Options**: Key-value object with available options (must be a JSON string or state reference to a dictionary)
* **Placeholder**: Text to display when no options are selected
* **Maximum count**: The maximum allowable number of selected options (set to zero for unlimited) - only available when multi-select is enabled

### Binding settings

* **Link Variable**: Connect the result of this component to a dynamic variable for use across the agent

### Styling options

* **Accent color**: Set the focus and highlight color for the select input
* **Primary text color**: Set the main text color for options and labels
* **Container background color**: Set the background color of the dropdown container
* **Separator color**: Set the border and divider color
* **Custom CSS classes**: Apply additional styling with custom CSS classes (separated by spaces)

### Events

* **wf-option-change**: Triggered when a single option changes (only available when multi-select is off) - payload contains the selected option
* **wf-options-change**: Triggered when multiple options change (only available when multi-select is enabled) - payload contains array of selected options

## Example

### User registration form

This example shows how to create a registration form with select inputs.

**Interface:**

* Text Input components for personal information
* Select Input components for preferences
* Button component for submission

**Select Input configuration:**

* **Label**: "Country," "Account Type," "Time Zone"
* **Options**: Various country, account type, and timezone options
* **Link Variable**: "country," "account," "timezone"

### Multi-select tag management

Create a tag management interface for content categorization.

**Interface:**

* Select Input component with multi-select enabled
* Button component for saving

**Select Input configuration:**

* **Label**: "Content Tags"
* **Allow Multi-select**: Enabled
* **Options**: JSON object with tag categories
* **Placeholder**: "Select tags for your content"
* **Link Variable**: "tags"

## Best practices

1. **Clear labeling**: Use descriptive labels that explain the selection purpose and context
2. **Logical ordering**: Arrange options in logical order (alphabetical, numerical, or by frequency of use)
3. **Option clarity**: Use clear, concise option text that users understand without ambiguity
4. **Accessibility**: Ensure select inputs are keyboard navigable and screen reader friendly

## Fields

<table className="componentFields">
  <thead>
    <th>Name</th>
    <th>Type</th>
    <th class="desc">Description</th>
    <th>Options</th>
  </thead>

  <tbody>
    <tr>
      <td>Label</td>
      <td>Text</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Allow Multi-select</td>
      <td>Boolean</td>
      <td>Select more than one option from the dropdown.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Options</td>
      <td>Key-Value</td>
      <td>Key-value object with options. Must be a JSON string or a state reference to a dictionary.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Placeholder</td>
      <td>Text</td>
      <td>Text to show when no options are selected.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Maximum count</td>
      <td>Number</td>
      <td>The maximum allowable number of selected options. Set to zero for unlimited.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Accent</td>
      <td>Color</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Primary text</td>
      <td>Color</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Chip text</td>
      <td>Color</td>
      <td>The colour of the text in the chips.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Container background</td>
      <td>Color</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Separator</td>
      <td>Color</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Custom CSS classes</td>
      <td>Text</td>
      <td>CSS classes, separated by spaces. You can define classes in custom stylesheets.</td>

      <td>
        <span>-</span>
      </td>
    </tr>
  </tbody>
</table>

## Events

<AccordionGroup>
  <Accordion title="wf-option-change" icon="code">
    Sent when the selected option changes.

    ```python  theme={null}
    def onchange_handler(state, payload):

    # Set the state variable "selected" to the selected option

    state["selected"] = payload
    ```
  </Accordion>

  <Accordion title="wf-options-change" icon="code">
    Sent when the selected options change.

    ```python  theme={null}
    def onchange_handler(state, payload):

    # Set the state variable "selected" to the selected option

    state["selected"] = payload
    ```
  </Accordion>
</AccordionGroup>

<events />
