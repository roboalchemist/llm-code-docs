# Source: https://flatfile.com/docs/plugins/boolean.md

# Boolean Validator

> Comprehensive boolean validation plugin for Flatfile that handles various representations of boolean values with multi-language support and flexible configuration options.

The Boolean Validator plugin for Flatfile provides comprehensive boolean validation for specified fields. It is designed to handle various representations of boolean values, not just `true` and `false`. Key features include two main validation modes: 'strict' (only accepts true/false boolean types) and 'truthy' (accepts values like 'yes', 'no', 'y', 'n', etc.). The plugin offers multi-language support for these truthy values (English, Spanish, French, German) and allows for custom mappings. It is highly configurable, with options to control case sensitivity, how null/undefined values are handled, and whether to automatically convert non-boolean values.

## Installation

Install the plugin using npm:

```bash
npm install @flatfile/plugin-validate-boolean
```

## Configuration & Parameters

The plugin is configured with a single object, `BooleanValidatorConfig`, containing the following options:

### Required Parameters

**`fields`** `string[]`

* An array of field keys (column names) to which the boolean validation should be applied.

**`validationType`** `'strict' | 'truthy'`

* The type of validation to perform:
  * `'strict'`: Only allows `true` and `false` boolean values
  * `'truthy'`: Allows string representations like 'yes', 'no', etc.

### Optional Parameters

**`sheetSlug`** `string`

* The slug of a specific sheet to apply the validation to
* Default: `'**'` (all sheets)

**`language`** `'en' | 'es' | 'fr' | 'de'`

* Specifies the language for predefined 'truthy' mappings
* Default: `'en'`

**`customMapping`** `Record<string, boolean>`

* Custom string-to-boolean mappings that override language-specific mappings
* Example: `{ 'ja': true, 'nein': false }`

**`caseSensitive`** `boolean`

* Controls case sensitivity for string comparisons during 'truthy' validation
* Default: `false`

**`handleNull`** `'error' | 'false' | 'true' | 'skip'`

* Defines how to handle `null` or `undefined` values:
  * `'error'`: Adds an error to the record
  * `'false'`: Converts the value to `false`
  * `'true'`: Converts the value to `true`
  * `'skip'`: Ignores the value without adding an error
* Default: `'skip'`

**`convertNonBoolean`** `boolean`

* Attempts to convert non-boolean values using JavaScript's `Boolean()` casting
* Default: `false`

**`defaultValue`** `boolean | 'skip'`

* Default value for invalid inputs instead of adding an error
* Default: `undefined` (raises an error)

**`customErrorMessages`** `object`

* Custom error messages for validation failures
* Properties: `invalidBoolean`, `invalidTruthy`, `nullValue`

## Usage Examples

<CodeGroup>
  ```javascript JavaScript
  import { FlatfileListener } from '@flatfile/listener';
  import { validateBoolean } from '@flatfile/plugin-validate-boolean';

  export default function(listener) {
    // Basic strict validation
    listener.use(
      validateBoolean({
        fields: ['isActive'],
        validationType: 'strict',
      })
    );
  }
  ```

  ```typescript TypeScript
  import { FlatfileListener } from '@flatfile/listener';
  import { validateBoolean } from '@flatfile/plugin-validate-boolean';

  export default function(listener: FlatfileListener) {
    // Basic strict validation
    listener.use(
      validateBoolean({
        fields: ['isActive'],
        validationType: 'strict',
      })
    );
  }
  ```
</CodeGroup>

### Advanced Configuration

<CodeGroup>
  ```javascript JavaScript
  import { FlatfileListener } from '@flatfile/listener';
  import { validateBoolean } from '@flatfile/plugin-validate-boolean';

  export default function(listener) {
    listener.use(
      validateBoolean({
        sheetSlug: 'contacts',
        fields: ['hasSubscription', 'isPremium'],
        validationType: 'truthy',
        language: 'es', // Use Spanish mappings: 'sí', 'no'
        handleNull: 'false', // Treat null/undefined as false
        defaultValue: false, // Set invalid values to false instead of erroring
        customErrorMessages: {
          nullValue: 'El campo no puede estar vacío.',
        },
      })
    );
  }
  ```

  ```typescript TypeScript
  import { FlatfileListener } from '@flatfile/listener';
  import { validateBoolean } from '@flatfile/plugin-validate-boolean';

  export default function(listener: FlatfileListener) {
    listener.use(
      validateBoolean({
        sheetSlug: 'contacts',
        fields: ['hasSubscription', 'isPremium'],
        validationType: 'truthy',
        language: 'es', // Use Spanish mappings: 'sí', 'no'
        handleNull: 'false', // Treat null/undefined as false
        defaultValue: false, // Set invalid values to false instead of erroring
        customErrorMessages: {
          nullValue: 'El campo no puede estar vacío.',
        },
      })
    );
  }
  ```
</CodeGroup>

### Using Helper Functions

<CodeGroup>
  ```javascript JavaScript
  import { validateBooleanField } from '@flatfile/plugin-validate-boolean';

  const myValue = 'Y';
  const result = validateBooleanField(myValue, {
    fields: ['customField'],
    validationType: 'truthy',
    language: 'en', // 'y' is a valid mapping in English
  });

  if (result.error) {
    console.error(`Validation failed: ${result.error}`);
  } else {
    console.log(`Validated value: ${result.value}`); // Outputs: Validated value: true
  }
  ```

  ```typescript TypeScript
  import { validateBooleanField } from '@flatfile/plugin-validate-boolean';

  const myValue = 'Y';
  const result = validateBooleanField(myValue, {
    fields: ['customField'],
    validationType: 'truthy',
    language: 'en', // 'y' is a valid mapping in English
  });

  if (result.error) {
    console.error(`Validation failed: ${result.error}`);
  } else {
    console.log(`Validated value: ${result.value}`); // Outputs: Validated value: true
  }
  ```
</CodeGroup>

## API Reference

### validateBoolean

The main entry point for the plugin that configures and returns a Flatfile listener.

**Signature:**

```typescript
validateBoolean(config: BooleanValidatorConfig): (listener: FlatfileListener) => void
```

**Parameters:**

* `config` - Configuration object for the validator

**Returns:**
A function that can be passed to `listener.use()` to register the plugin.

### validateBooleanField

A utility function that runs the complete validation logic for a single value.

**Signature:**

```typescript
validateBooleanField(value: any, config: BooleanValidatorConfig): { value: boolean | null; error: string | null }
```

**Parameters:**

* `value` - The value to validate
* `config` - The configuration object

**Returns:**
Object with `value` (validated boolean or null) and `error` (error message or null)

### validateStrictBoolean

Validates that a value is strictly a boolean `true` or `false`.

**Signature:**

```typescript
validateStrictBoolean(value: any, config: BooleanValidatorConfig): { value: boolean | null; error: string | null }
```

### validateTruthyBoolean

Validates that a value corresponds to a "truthy" or "falsy" representation.

**Signature:**

```typescript
validateTruthyBoolean(value: any, config: BooleanValidatorConfig): { value: boolean | null; error: string | null }
```

### handleNullValue

Processes a `null` or `undefined` value according to the `handleNull` configuration.

**Signature:**

```typescript
handleNullValue(value: any, config: BooleanValidatorConfig): { value: boolean | null; error: string | null }
```

### handleInvalidValue

Processes a value that has been identified as invalid.

**Signature:**

```typescript
handleInvalidValue(value: any, config: BooleanValidatorConfig): { value: boolean | null; error: string | null }
```

## Troubleshooting

### Validation Not Applied

* Ensure the `fields` array contains the correct field keys
* Verify the `sheetSlug` (if used) matches the target sheet

### Case Sensitivity Issues

For 'truthy' validation, if values like 'YES' aren't being validated correctly, check the `caseSensitive` option. It defaults to `false`, but if set to `true`, the case must match exactly.

### Unexpected Results

Remember the order of operations:

1. Null handling is checked first
2. Specific validation type ('strict' or 'truthy') is applied
3. `defaultValue` is used as a final fallback for invalid values

## Notes

### Default Behavior

If only the required `fields` and `validationType` options are provided, the plugin will apply validation to the specified fields on all sheets. For 'truthy' validation, it uses case-insensitive English mappings ('yes'/'no'). Null or undefined values are skipped by default.

### Special Considerations

* The plugin supports built-in truthy/falsy mappings for English ('en'), Spanish ('es'), French ('fr'), and German ('de')
* Custom mappings (`customMapping`) take precedence over language-based default mappings
* The `sheetSlug` option allows applying different validation rules to different sheets within the same workbook

### Error Handling Patterns

* The main plugin does not throw exceptions; it adds errors directly to Flatfile records
* When a `defaultValue` is provided, the plugin corrects invalid values and adds an informational message for auditing
* Helper functions return a consistent `{ value, error }` object pattern for easy error checking
