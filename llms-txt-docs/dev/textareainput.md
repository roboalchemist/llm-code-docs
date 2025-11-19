# Source: https://dev.writer.com/components/textareainput.md

# Text area Input

A user input component that allows users to enter multi-line text values.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/textareainput.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=7d78bb7c819b5751d77d38bff4e6ea8e" data-og-width="970" width="970" data-og-height="271" height="271" data-path="framework/public/components/textareainput.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/textareainput.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=0b0bb9331a2cabdaf2b61ddce23608bf 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/textareainput.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=e3d14b572fcecfeb1c3723b618b3e017 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/textareainput.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=5858cdd3659dd85c39ee7f19505c1bd7 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/textareainput.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=60df41a7e524f01626d9b3ff277ebe76 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/textareainput.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=7d28444d2b6c5387d28c64dca95eb45e 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/textareainput.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=a9f7f1eb8c78305a8ff73baa3b752fb7 2500w" />

## Overview

The **Text area Input** component allows users to enter multi-line text values. It's designed for longer text content like descriptions, comments, reviews, or any content that requires multiple lines.

## Common use cases

* **Long-form content**: Collect essays, articles, or detailed descriptions
* **User feedback**: Gather reviews, comments, or support requests
* **Data entry**: Allow users to paste large amounts of text or data
* **Configuration**: Collect complex configuration settings or parameters

## How it works

1. **Multi-line input**: Users can enter text across multiple lines
2. **Manual resizing**: Users can resize the text area by dragging the bottom corner
3. **State binding**: Content automatically saves to the specified state variable
4. **Real-time events**: Triggers events as users type or finish editing
5. **Configurable rows**: Set the initial number of rows to display

The component provides a familiar text editing experience with manual resizing for longer content entry.

## Configuration options

### Basic settings

* **Label**: Text label displayed above the input field
* **Placeholder**: Hint text shown when the field is empty
* **Rows**: Number of rows to display (default: `5`)
* **Link variable**: The name of the state variable that stores the input value

### Styling options

* **Custom CSS classes**: Apply additional styling

### Events

* **wf-change**: Triggered as users type (real-time) - payload contains the text area content
* **wf-change-finish**: Triggered when users finish editing (on blur) - payload contains the text area content

## Example

### Customer feedback form

This example shows how to create a customer feedback form with a text area for detailed comments.

**Interface:**

* Text Input for customer name
* Text area Input for feedback details
* Button to submit the form

**Text area Input configuration:**

* Label: "Your feedback"
* Placeholder: "Please share your experience with our product..."
* State element: `customer_feedback`
* Rows: 4

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/components/textareainput-configuration.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=d00e7359cce0d8fefcdf2818f0229bf8" alt="Text area Input configuration" data-og-width="2704" width="2704" data-og-height="1558" height="1558" data-path="images/agent-builder/components/textareainput-configuration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/components/textareainput-configuration.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=f4ca02fb2d434a79f98f041d2c198350 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/components/textareainput-configuration.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=8059197a31c3ab6a1b059183624e506a 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/components/textareainput-configuration.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=f596032cce0fa5e61546c318a07619a8 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/components/textareainput-configuration.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=25cf82ae60fe3310e4b1fba8b0de8ab6 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/components/textareainput-configuration.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=528730a9b19f68332f52a41d9a23ba9e 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/components/textareainput-configuration.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=d6ce6cc3b2ad0331eebe118784b34daf 2500w" />

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
      <td>Placeholder</td>
      <td>Text</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Rows</td>
      <td>Number</td>
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
