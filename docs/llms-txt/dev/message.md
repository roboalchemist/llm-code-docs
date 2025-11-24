# Source: https://dev.writer.com/components/message.md

# Message

A component that displays a message in various styles, including success, error, warning, and informational.

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/message.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=d524a6480f207b32ea31aea16532b149" data-og-width="1162" width="1162" data-og-height="706" height="706" data-path="framework/public/components/message.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/message.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=2161be2a62bc73e84e4a3c1891e1ab66 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/message.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=fe34b6cbc825952cbc2536b2cc00b14e 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/message.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=a9c3c2f500131c8cdcbc7d0699327bb6 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/message.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=815d1383ac7f245549a12cee19e4378e 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/message.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=87a3a392644c56db555f379a3c15e79f 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/message.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=b931f5f47a7381ebd5faec72cf2e2274 2500w" />

## Overview

The **Message** component displays status messages, notifications, and feedback to users. It uses prefix characters to determine the message type and styling automatically.

Message components support different types (success, error, warning, loading, info) with appropriate styling and can display dynamic content from state variables. They're essential for creating responsive, user-friendly interfaces that keep users informed.

## Common use cases

* **Status updates**: Show progress messages during processing operations
* **Error notifications**: Display validation errors or system failures
* **Success confirmations**: Confirm successful actions or completions
* **Loading states**: Show animated loading messages during operations
* **Form validation**: Display field validation errors and warnings

## How it works

1. **Message content**: Display static text or reference state variables
2. **Prefix-based types**: Use prefix characters to determine message type automatically. For example, `+` makes the message green, `-` makes it red, and `%` provides a dynamic loading icon.
3. **Dynamic updates**: Content updates automatically when state variables change
4. **Visual styling**: Each message type has distinct colors and styling
5. **Conditional display**: Messages can show or hide based on conditions

The component provides immediate feedback to users about the state of their interactions and system operations.

## Configuration options

### Basic settings

* **Message**: The text content to display (supports state variable references)
* **Prefix characters**: Use prefixes to determine message type automatically. For example, `+` in front of the message makes it green: `+Operation completed successfully`.

### Message types and prefixes

* **Success**: Prefix with `+` (for example, `"+Operation completed successfully"`)
* **Error**: Prefix with `-` (for example, `"-An error occurred"`)
* **Warning**: Prefix with `!` (for example, `"!Please check your input"`)
* **Loading**: Prefix with `%` (for example, `"%Processing your request..."`)
* **Info**: No prefix (for example, `"This is an informational message"`)

### Styling options

* **Success color**: Customize success message background color (default: Green3)
* **Error color**: Customize error message background color (default: Orange2)
* **Warning color**: Customize warning message background color (default: #FFE999)
* **Info color**: Customize info message background color (default: Blue2)
* **Loading color**: Customize loading message background color (default: Blue2)
* **Primary text color**: Set the text color
* **Custom CSS classes**: Apply additional styling

## Example

### Processing status updates

Create a workflow that shows different status messages during file processing.

**Interface:**

* File input to upload a file
* Button component to start file processing
* Message component for status updates

**Message configuration:**

* **Message**: `@{status_message}` (with `%` prefix for loading, `+` for success, `-` for errors)

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/components/message-configuration.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=9551475f5c4202ba6800c522ef98a62a" alt="Message configuration" data-og-width="2742" width="2742" data-og-height="1142" height="1142" data-path="images/agent-builder/components/message-configuration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/components/message-configuration.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=be673f15567df8ab5dbfe733dac73bfa 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/components/message-configuration.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=eeca35057f274a72b8428ab9313e4dac 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/components/message-configuration.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=ad3e821f398d53a95580b3e8bb6b6695 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/components/message-configuration.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=4323c66b5e427e8fe74d7f70920970ad 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/components/message-configuration.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=c9d28835e87d0416f7783e1918bdfe8f 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/components/message-configuration.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=86c1e4477b10e3f2eb3d2d79e533f909 2500w" />

## Best practices

1. **Clear messaging**: Use concise, clear language that users can understand immediately
2. **Appropriate types**: Choose the correct message type for the content (info, success, warning, error)
3. **Dynamic content**: Use state variables to show relevant, up-to-date information
4. **Conditional display**: Show messages only when relevant to avoid interface clutter
5. **Consistent styling**: Maintain consistent message styling across your interface
6. **Context**: Provide enough context for users to understand and act on the message

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
      <td>Message</td>
      <td>Text</td>
      <td>Prefix with '+' for a success message, with '-' for error, '!' for warning, '%' for loading. No prefix for info. Leave empty to hide.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Success</td>
      <td>Color</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Error</td>
      <td>Color</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Warning</td>
      <td>Color</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Info</td>
      <td>Color</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Loading</td>
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
      <td>Custom CSS classes</td>
      <td>Text</td>
      <td>CSS classes, separated by spaces. You can define classes in custom stylesheets.</td>

      <td>
        <span>-</span>
      </td>
    </tr>
  </tbody>
</table>
