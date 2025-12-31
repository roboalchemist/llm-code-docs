# Source: https://flatfile.com/docs/plugins/stored-constraints.md

# Stored Constraints Plugin

> Automatically applies server-side validation rules to records during the data import process using reusable JavaScript functions defined at the App level.

The Stored Constraints plugin automatically applies server-side validation rules to records during the data import process. These rules, called "stored constraints," are defined as reusable JavaScript functions at the App level within your Flatfile account. You can then apply these constraints to specific fields in your Sheet configurations.

When a user submits data, this plugin triggers. It fetches the stored constraint functions from the Flatfile API, finds the corresponding fields in the submitted data, and executes the validation logic for each record.

This plugin is ideal for enforcing complex or reusable business logic, such as validating a SKU against an external database, checking for valid country-state combinations, or implementing custom data quality rules that are shared across multiple Sheets or Blueprints.

## Installation

Install the plugin using npm:

```bash
npm install @flatfile/plugin-stored-constraints
```

## Configuration & Parameters

The `storedConstraint()` function itself does not accept any configuration parameters. The plugin's behavior is configured entirely within the Flatfile platform.

Configuration is managed in two places in Flatfile:

### App Constraints

* **Location**: In your Flatfile App's settings
* **Purpose**: This is where you define the reusable validation logic. Each stored constraint consists of a unique name (the "validator") and a JavaScript function body (the "function")
* **Example**: You could create a constraint named "is-valid-email" with the function body `(value, key, { record }) => { if (!/\S+@\S+\.\S+/.test(value)) { record.addError(key, 'Invalid email format.') } }`

### Sheet Field Constraints

* **Location**: In your Sheet or Blueprint configuration
* **Purpose**: You apply a stored constraint to a specific field by adding a constraint of type "stored" and referencing its name
* **`validator`** (string): The name of the App-level constraint to apply (e.g., "is-valid-email")
* **`config`** (object, optional): An arbitrary configuration object that gets passed to your validation function. This allows you to make a single stored constraint adaptable to different contexts

### Default Behavior

By default, the plugin does nothing if no fields in a Sheet are configured with a `type: 'stored'` constraint. When such constraints are present, the plugin will automatically trigger on every data submission (`commit:created` event) for all sheets and execute the corresponding validation logic.

## Usage Examples

### Basic Usage

<CodeGroup>
  ```javascript JavaScript
  // listener.js
  import { storedConstraint } from '@flatfile/plugin-stored-constraints';

  export default function (listener) {
    // Registers the plugin to run on data submission
    listener.use(storedConstraint());
  }
  ```

  ```typescript TypeScript
  // listener.ts
  import type { FlatfileListener } from "@flatfile/listener";
  import { storedConstraint } from '@flatfile/plugin-stored-constraints';

  export default function (listener: FlatfileListener) {
    // Registers the plugin to run on data submission
    listener.use(storedConstraint());
  }
  ```
</CodeGroup>

### Configuration Example

<CodeGroup>
  ```javascript JavaScript
  // In your Flatfile Sheet/Blueprint configuration (JSON or UI):
  /*
  {
    "key": "email",
    "label": "Email",
    "constraints": [
      {
        "type": "stored",
        "validator": "is-valid-email-domain",
        "config": {
          "allowedDomain": "example.com"
        }
      }
    ]
  }
  */

  // In your Flatfile App's Stored Constraints section (UI):
  /*
    Validator Name: "is-valid-email-domain"
    Function:
    function(value, key, { record, config }) {
      if (!value.endsWith('@' + config.allowedDomain)) {
        record.addError(key, 'Email must be from the ' + config.allowedDomain + ' domain.');
      }
    }
  */

  // Your listener code remains simple:
  // listener.js
  import { storedConstraint } from '@flatfile/plugin-stored-constraints';

  export default function (listener) {
    listener.use(storedConstraint());
  }
  ```

  ```typescript TypeScript
  // In your Flatfile Sheet/Blueprint configuration (JSON or UI):
  /*
  {
    "key": "email",
    "label": "Email",
    "constraints": [
      {
        "type": "stored",
        "validator": "is-valid-email-domain",
        "config": {
          "allowedDomain": "example.com"
        }
      }
    ]
  }
  */

  // In your Flatfile App's Stored Constraints section (UI):
  /*
    Validator Name: "is-valid-email-domain"
    Function:
    function(value, key, { record, config }) {
      if (!value.endsWith('@' + config.allowedDomain)) {
        record.addError(key, 'Email must be from the ' + config.allowedDomain + ' domain.');
      }
    }
  */

  // Your listener code remains simple:
  // listener.ts
  import type { FlatfileListener } from "@flatfile/listener";
  import { storedConstraint } from '@flatfile/plugin-stored-constraints';

  export default function (listener: FlatfileListener) {
    listener.use(storedConstraint());
  }
  ```
</CodeGroup>

### Advanced Usage with Dependencies

Stored constraint functions have access to a `deps` object containing helpful libraries. This example shows a constraint using the `validator` library to check for a valid email format.

<CodeGroup>
  ```javascript JavaScript
  // In your Flatfile App's Stored Constraints section (UI):
  /*
    Validator Name: "is-valid-email-advanced"
    Function:
    function(value, key, { record, deps }) {
      // Access the 'validator' library from the deps object
      if (!deps.validator.isEmail(value)) {
        record.addError(key, 'Please enter a valid email address.');
      }
    }
  */

  // Your listener code does not change:
  // listener.js
  import { storedConstraint } from '@flatfile/plugin-stored-constraints';

  export default function (listener) {
    listener.use(storedConstraint());
  }
  ```

  ```typescript TypeScript
  // In your Flatfile App's Stored Constraints section (UI):
  /*
    Validator Name: "is-valid-email-advanced"
    Function:
    function(value, key, { record, deps }) {
      // Access the 'validator' library from the deps object
      if (!deps.validator.isEmail(value)) {
        record.addError(key, 'Please enter a valid email address.');
      }
    }
  */

  // Your listener code does not change:
  // listener.ts
  import type { FlatfileListener } from "@flatfile/listener";
  import { storedConstraint } from '@flatfile/plugin-stored-constraints';

  export default function (listener: FlatfileListener) {
    listener.use(storedConstraint());
  }
  ```
</CodeGroup>

### Error Handling Examples

#### User-facing Error

```javascript
// Stored constraint function defined in the Flatfile App UI
function(value, key, { record }) {
  if (value === null || value === '') {
    // This adds an error to the cell in the UI
    record.addError(key, 'This field is required.');
  }
}
```

#### Server-side Error

```javascript
// Stored constraint function defined in the Flatfile App UI
function(value, key, { record }) {
  // This will throw an exception because 'badProperty' does not exist
  const x = null;
  x.badProperty = 'test';
}

// When the above constraint runs, the plugin will catch the TypeError
// and log a message like "Error executing constraint: Cannot set properties of null..."
// to the server console. No error will appear in the Flatfile UI.
```

## Troubleshooting

If your constraints are not running, verify that:

1. The `storedConstraint()` plugin is registered in your listener
2. The field in your Sheet configuration has a constraint with `type: 'stored'`
3. The `validator` name in the Sheet constraint exactly matches the name of a Stored Constraint defined in your App
4. The listener's environment has a valid Flatfile API key with sufficient permissions

If you see "Error executing constraint" in your server logs, check the corresponding stored constraint function for runtime errors.

## Notes

### Security Considerations

* The plugin uses `eval()` to execute the function strings stored in your App constraints. This means the constraint logic is executed dynamically. Ensure that only trusted administrators can create or edit stored constraint functions to avoid security risks.

### Requirements

* The plugin requires an active connection to the Flatfile API to fetch sheet configurations and app-level constraint definitions. Ensure your listener environment is configured with a valid Flatfile API key.
* The plugin triggers on the `commit:created` event, which runs server-side after a user submits their data.

### Error Handling

* The plugin includes a `try...catch` block around the execution of each constraint. If a constraint function throws an unhandled exception, the error is logged to the server-side console, and processing continues with the next record or field.
* For user-facing validation errors, the constraint function logic itself is responsible for calling `record.addError(fieldKey, 'Your error message')`. The plugin does not automatically convert thrown exceptions into record errors.
