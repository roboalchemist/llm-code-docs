# Source: https://dev.writer.com/components/textinput.md

# Text Input

A user input component that allows users to enter single-line text values.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/textinput.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=aa0cc5b8fd4e316f7dc7a9f13fb2dbf4" data-og-width="967" width="967" data-og-height="162" height="162" data-path="framework/public/components/textinput.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/textinput.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=e136a0d242a01200fd4127f245bce1bb 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/textinput.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=ae717601ccca263b3f4c9268737b1252 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/textinput.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=3e31b5cc138e5724fb7681dab698761c 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/textinput.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=d6f70106873a8936edd567db9d597baf 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/textinput.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=9b17199a890971d90cd194d6933325de 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/textinput.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=eb366deaefe983b8e1da51644adbbf0f 2500w" />

## Overview

The **Text Input** component allows users to enter single-line text values. It's the most basic form of user input and is essential for collecting information from users in your agent.

Text inputs automatically bind to state variables, making it easy to capture and use user input in your blueprint workflows. They support various styling options and can be configured for different use cases, including password fields.

## Common use cases

* **User information**: Collect names, emails, phone numbers, and other personal data
* **Search queries**: Allow users to search through data or content
* **Configuration values**: Let users set preferences or parameters
* **Form fields**: Collect data as part of larger forms
* **Password entry**: Secure input for sensitive information

## How it works

1. **Label**: Provide a clear label for the input field
2. **Placeholder**: Add helpful placeholder text to guide users
3. **Binding**: Connect to a state variable to store the input value
4. **Events**: Trigger workflows when users type or finish editing
5. **Styling**: Customize appearance with colors and CSS classes, and add a password mode for sensitive information

The component automatically updates the bound state variable as users type, and can trigger events for real-time processing or validation.

## Configuration options

### Basic settings

* **Label**: The field label displayed above the input
* **Placeholder**: Hint text shown when the field is empty
* **Link variable**: The name of the state variable that stores the input value

### Styling options

* **Password mode**: Toggle to hide input for sensitive data (default is disabled)
* **Accent color**: Set the focus color for the input field
* **Custom CSS classes**: Apply additional styling

### Events

* **wf-change**: Triggered as users type (real-time) - payload contains the input value
* **wf-change-finish**: Triggered when users finish editing (on blur) - payload contains the input value

## Example

### Search interface

This example shows how to create a search interface with a text input. The search query is stored in the `search_query` state variable. For the blueprint workflow, you can access the `search_query` state variable to see the user's query.

**Interface:**

* Text Input component for the search query
* Button component to trigger the search
* Results container to display matches

**Search text input configuration:**

* **Label**: "Search"
* **Placeholder**: "Enter search terms..."
* **Link variable**: `search_query`

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/components/textinput-configuration.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=bcac6a24540b4f8833d2af0b5d35ad61" alt="Text Input configuration" data-og-width="2710" width="2710" data-og-height="1284" height="1284" data-path="images/agent-builder/components/textinput-configuration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/components/textinput-configuration.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=1af9d36224cd816a31a88fc47e630e94 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/components/textinput-configuration.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=cfd74fb2afb05c660e94a21c6113f653 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/components/textinput-configuration.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=2ff264fd25dc429864edede82367354e 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/components/textinput-configuration.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=6dc5c31246a96a8639248e95f2c1c7dc 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/components/textinput-configuration.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=73bd4e578e4e1a7dfefc97bd11da2b0e 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/components/textinput-configuration.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=6a3ad974308a801a1b3eb66813846a4a 2500w" />

## Best practices

1. **Clear labels**: Use descriptive labels that clearly indicate what information is needed
2. **Helpful placeholders**: Provide examples or guidance in placeholder text
3. **Appropriate validation**: Validate input on both client and server side
4. **Real-time feedback**: Use the `wf-change` event for immediate user feedback
5. **Password security**: Use password mode for sensitive information

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
      <td>Password mode</td>
      <td>Boolean</td>
      <td>-</td>

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
      <td>Custom CSS classes</td>
      <td>Text</td>
      <td>CSS classes, separated by spaces. You can define classes in custom stylesheets.</td>

      <td>
        <span>-</span>
      </td>
    </tr>
  </tbody>
</table>
