# Source: https://flatfile.com/docs/plugins/string.md

# String Validator Plugin

> A comprehensive plugin for validating and transforming string data during the Flatfile import process with configurable validation rules, pattern matching, and automatic data corrections.

The String Validator plugin for Flatfile provides a comprehensive way to validate and transform string data during the import process. It allows you to configure multiple validation rules for specified fields in a single, easy-to-use configuration object.

Its main purpose is to enforce data quality and consistency for string-based fields. Key features include validating strings against regular expression patterns (both common predefined patterns like email and URL, and custom ones), enforcing length constraints (min, max, or exact), and ensuring proper casing (lowercase, uppercase, or titlecase). The plugin can also automatically trim leading or trailing whitespace.

Use cases include cleaning user-submitted data, ensuring identifiers match a specific format (e.g., 'ABC-123'), validating contact information like emails and phone numbers, and standardizing the case of names or categories before they are imported into a system. If a value doesn't meet a validation rule but can be corrected (e.g., wrong case, extra whitespace), the plugin will automatically transform the value and notify the user of the change.

## Installation

Install the plugin using npm:

```bash
npm install @flatfile/plugin-validate-string
```

## Configuration & Parameters

The plugin is configured with a single `StringValidationConfig` object with the following properties:

### Required Parameters

<ParamField path="fields" type="string[]" required>
  An array of field keys (column names) to which the validation rules should be applied.
</ParamField>

### Optional Parameters

<ParamField path="sheetSlug" type="string" default="**">
  The slug of a specific sheet to apply the validations to. Defaults to '\*\*' (applies to all sheets in the workbook).
</ParamField>

<ParamField path="pattern" type="'email' | 'phone' | 'url' | RegExp">
  A regular expression to validate the string against. You can use one of the predefined string keys for common patterns ('email', 'phone', 'url') or provide your own custom RegExp object.
</ParamField>

<ParamField path="minLength" type="number">
  The minimum allowed length for the string.
</ParamField>

<ParamField path="maxLength" type="number">
  The maximum allowed length for the string.
</ParamField>

<ParamField path="exactLength" type="number">
  The exact required length for the string.
</ParamField>

<ParamField path="caseType" type="'lowercase' | 'uppercase' | 'titlecase'">
  Enforces a specific character case. If the input string does not match, it will be transformed, and a validation message will be added.
</ParamField>

<ParamField path="trim" type="{ leading?: boolean, trailing?: boolean }">
  An object to control whitespace trimming. If `leading` is true, it trims whitespace from the start. If `trailing` is true, it trims from the end. If the string is trimmed, the value is transformed, and a message is added.
</ParamField>

<ParamField path="emptyStringAllowed" type="boolean" default="false">
  Controls whether an empty string is considered a valid value. By default, empty strings will generate a "Field cannot be empty" error.
</ParamField>

<ParamField path="errorMessages" type="{ pattern?: string, length?: string, case?: string, trim?: string }">
  An object to provide custom error messages for different validation types, overriding the default messages. The plugin provides default messages for each validation type (e.g., "Invalid format", "Minimum length is X").
</ParamField>

## Usage Examples

### Basic Usage

<CodeGroup>
  ```javascript JavaScript
  import { FlatfileListener } from '@flatfile/listener';
  import { validateString } from '@flatfile/plugin-validate-string';

  const listener = new FlatfileListener();

  listener.use(validateString({
    fields: ['firstName', 'lastName'],
    minLength: 2,
    maxLength: 50,
    caseType: 'titlecase'
  }));
  ```

  ```typescript TypeScript
  import { FlatfileListener } from '@flatfile/listener';
  import { validateString } from '@flatfile/plugin-validate-string';

  const listener = new FlatfileListener();

  listener.use(validateString({
    fields: ['firstName', 'lastName'],
    minLength: 2,
    maxLength: 50,
    caseType: 'titlecase'
  }));
  ```
</CodeGroup>

### Email Validation

<CodeGroup>
  ```javascript JavaScript
  import { FlatfileListener } from '@flatfile/listener';
  import { validateString } from '@flatfile/plugin-validate-string';

  const listener = new FlatfileListener();

  listener.use(validateString({
    fields: ['email'],
    pattern: 'email',
    emptyStringAllowed: false,
    errorMessages: {
      pattern: 'Please provide a valid email address.',
      length: 'The email address is too long.'
    }
  }));
  ```

  ```typescript TypeScript
  import { FlatfileListener } from '@flatfile/listener';
  import { validateString } from '@flatfile/plugin-validate-string';

  const listener = new FlatfileListener();

  listener.use(validateString({
    fields: ['email'],
    pattern: 'email',
    emptyStringAllowed: false,
    errorMessages: {
      pattern: 'Please provide a valid email address.',
      length: 'The email address is too long.'
    }
  }));
  ```
</CodeGroup>

### Advanced Custom Pattern Validation

<CodeGroup>
  ```javascript JavaScript
  import { FlatfileListener } from '@flatfile/listener';
  import { validateString } from '@flatfile/plugin-validate-string';

  const listener = new FlatfileListener();

  // Example: Validate a product SKU that must be in the format 'SKU-12345'
  listener.use(validateString({
    fields: ['product_sku'],
    pattern: /^SKU-\d{5}$/,
    caseType: 'uppercase',
    errorMessages: {
      pattern: 'SKU must be in the format SKU-XXXXX, where X is a digit.',
      case: 'SKU must be in uppercase.'
    }
  }));
  ```

  ```typescript TypeScript
  import { FlatfileListener } from '@flatfile/listener';
  import { validateString } from '@flatfile/plugin-validate-string';

  const listener = new FlatfileListener();

  // Example: Validate a product SKU that must be in the format 'SKU-12345'
  listener.use(validateString({
    fields: ['product_sku'],
    pattern: /^SKU-\d{5}$/,
    caseType: 'uppercase',
    errorMessages: {
      pattern: 'SKU must be in the format SKU-XXXXX, where X is a digit.',
      case: 'SKU must be in uppercase.'
    }
  }));
  ```
</CodeGroup>

### Using the Utility Function

<CodeGroup>
  ```javascript JavaScript
  import { validateAndTransformString } from '@flatfile/plugin-validate-string';

  const config = {
    fields: ['email'],
    pattern: 'email'
  };

  const result1 = validateAndTransformString('test@example.com', config);
  // result1 -> { value: 'test@example.com', error: null }

  const result2 = validateAndTransformString('not-an-email', config);
  // result2 -> { value: 'not-an-email', error: 'Invalid format' }
  ```

  ```typescript TypeScript
  import { validateAndTransformString } from '@flatfile/plugin-validate-string';

  const config = {
    fields: ['email'],
    pattern: 'email'
  };

  const result1 = validateAndTransformString('test@example.com', config);
  // result1 -> { value: 'test@example.com', error: null }

  const result2 = validateAndTransformString('not-an-email', config);
  // result2 -> { value: 'not-an-email', error: 'Invalid format' }
  ```
</CodeGroup>

### Error Handling Example

<CodeGroup>
  ```javascript JavaScript
  import { validateAndTransformString } from '@flatfile/plugin-validate-string';

  const config = {
    fields: ['code'],
    exactLength: 5
  };

  const result = validateAndTransformString('ABC', config);
  if (result.error) {
    console.log(`Validation failed: ${result.error}`);
    // Logs: "Validation failed: Exact length must be 5"
  }
  ```

  ```typescript TypeScript
  import { validateAndTransformString } from '@flatfile/plugin-validate-string';

  const config = {
    fields: ['code'],
    exactLength: 5
  };

  const result = validateAndTransformString('ABC', config);
  if (result.error) {
    console.log(`Validation failed: ${result.error}`);
    // Logs: "Validation failed: Exact length must be 5"
  }
  ```
</CodeGroup>

## API Reference

### validateString(config)

The main entry point for the plugin. It configures and registers a `recordHook` that listens for new commits and applies the specified string validations to each record.

**Parameters:**

* `config` (StringValidationConfig): An object that defines the validation and transformation rules.

**Returns:** A function that takes a `FlatfileListener` instance and attaches the validation logic to it.

### validateAndTransformString(value, config)

An exported utility function that runs the validation and transformation logic on a single string value. It is used internally by the plugin but can be used for custom validation logic if needed.

**Parameters:**

* `value` (string): The input string to validate and transform.
* `config` (StringValidationConfig): The configuration object defining the rules to apply.

**Returns:** An object of type `ValidationResult` with two properties:

* `value` (string): The original or transformed string value.
* `error` (string | null): An error message string if any validation fails, otherwise `null`.

## Notes

### Default Behavior

* **Empty strings**: By default, empty strings are considered invalid. To allow them, you must explicitly set `emptyStringAllowed: true` in the configuration.
* **Sheet targeting**: When no `sheetSlug` is specified, the plugin applies to all sheets in the workbook using the default value '\*\*'.
* **Error messages**: The plugin provides default error messages for each validation type (e.g., "Invalid format", "Minimum length is X") which can be customized using the `errorMessages` configuration option.

### Important Considerations

* The plugin operates using the `@flatfile/plugin-record-hook`, which is a dependency. It processes records individually during the `commit:created` event.
* The plugin can modify data. When a transformation is applied (e.g., changing case or trimming whitespace), the record's value is updated with `record.set()`.
* By default, when a transformation is applied, the plugin also adds a validation message to the cell (e.g., "Field value must be in titlecase"). This informs the user that their original data was automatically corrected.
* The plugin handles `null` and `undefined` values by simply skipping them. Validation is only applied to defined string values.
* The plugin does not throw exceptions. Instead, it captures validation failures and adds them as errors to the corresponding record and field using `record.addError(field, message)`. These errors are then visible to the user in the Flatfile UI.
