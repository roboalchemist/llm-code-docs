# Source: https://flatfile.com/docs/plugins/number.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Number Validation Plugin

> Comprehensive validation for numeric data during the Flatfile import process with support for ranges, formats, and special number types.

The Number Validation Plugin for Flatfile provides comprehensive validation for numeric data during the import process. It attaches to the `commit:created` listener event to analyze and validate data from specified fields.

Its main purpose is to ensure that numeric data conforms to a wide range of rules before being accepted into the system. Use cases include:

* Enforcing value ranges (e.g., age must be between 18 and 65)
* Validating data formats like integers, currency, or numbers with specific precision and scale
* Ensuring numbers follow specific rules, such as being a multiple of a certain value (step validation)
* Checking for special numeric properties like being even, odd, or prime
* Automatically cleaning up number formats by handling thousands separators and decimal points
* Optionally rounding or truncating numbers before validation

The plugin modifies records by setting the cleaned, parsed numeric value and attaching any validation errors or warnings directly to the relevant field.

## Installation

Install the plugin using npm:

```bash  theme={null}
npm install @flatfile/plugin-validate-number
```

## Configuration & Parameters

The `validateNumber` function accepts a single configuration object with the following properties:

### Required Parameters

| Parameter | Type       | Description                                                                           |
| --------- | ---------- | ------------------------------------------------------------------------------------- |
| `fields`  | `string[]` | An array of field keys (column names) to which the validation rules should be applied |

### Optional Parameters

| Parameter            | Type       | Default   | Description                                                                                          |
| -------------------- | ---------- | --------- | ---------------------------------------------------------------------------------------------------- |
| `sheetSlug`          | `string`   | `'**'`    | The slug of the sheet to apply the validation to. Defaults to all sheets                             |
| `min`                | `number`   | undefined | The minimum allowed value for the number                                                             |
| `max`                | `number`   | undefined | The maximum allowed value for the number                                                             |
| `inclusive`          | `boolean`  | `false`   | Determines if the `min` and `max` values are inclusive                                               |
| `integerOnly`        | `boolean`  | `false`   | If true, the value must be an integer (no decimal part)                                              |
| `precision`          | `number`   | undefined | The total maximum number of digits allowed (requires `scale` to be set)                              |
| `scale`              | `number`   | undefined | The maximum number of digits allowed after the decimal point (requires `precision` to be set)        |
| `currency`           | `boolean`  | `false`   | If true, validates that the number is a valid currency format, allowing up to two decimal places     |
| `step`               | `number`   | undefined | The value must be a multiple of this number                                                          |
| `thousandsSeparator` | `string`   | `','`     | The character used as a thousands separator in the input string                                      |
| `decimalPoint`       | `string`   | `'.'`     | The character used as the decimal point in the input string                                          |
| `specialTypes`       | `string[]` | undefined | An array of special number types to validate against. Supported values: `'prime'`, `'even'`, `'odd'` |
| `round`              | `boolean`  | `false`   | If true, the number is rounded to the nearest integer before validation                              |
| `truncate`           | `boolean`  | `false`   | If true, the decimal part of the number is removed before validation                                 |

## Usage Examples

### Basic Usage

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { validateNumber } from '@flatfile/plugin-validate-number';

  const listener = new FlatfileListener();

  listener.use(
    validateNumber({
      fields: ['quantity'],
      integerOnly: true,
    })
  );
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { validateNumber } from '@flatfile/plugin-validate-number';

  const listener = new FlatfileListener();

  listener.use(
    validateNumber({
      fields: ['quantity'],
      integerOnly: true,
    })
  );
  ```
</CodeGroup>

### Currency Validation

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { validateNumber } from '@flatfile/plugin-validate-number';

  const listener = new FlatfileListener();

  listener.use(
    validateNumber({
      sheetSlug: 'products',
      fields: ['price'],
      min: 0,
      max: 1000000,
      inclusive: true,
      currency: true,
      precision: 9, // 7 digits before decimal, 2 after
      scale: 2,
      thousandsSeparator: ',',
      decimalPoint: '.',
    })
  );
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { validateNumber } from '@flatfile/plugin-validate-number';

  const listener = new FlatfileListener();

  listener.use(
    validateNumber({
      sheetSlug: 'products',
      fields: ['price'],
      min: 0,
      max: 1000000,
      inclusive: true,
      currency: true,
      precision: 9, // 7 digits before decimal, 2 after
      scale: 2,
      thousandsSeparator: ',',
      decimalPoint: '.',
    })
  );
  ```
</CodeGroup>

### Direct Validation Function

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { validateNumberField } from '@flatfile/plugin-validate-number';

  const customValidation = () => {
    const inputValue = '1,234.56';
    const config = { thousandsSeparator: ',', decimalPoint: '.' };

    const result = validateNumberField(inputValue, config);

    if (result.errors.length > 0) {
      console.error('Validation Errors:', result.errors);
    } else if (result.warnings.length > 0) {
      console.warn('Validation Warnings:', result.warnings);
    } else {
      console.log('Validated Value:', result.value); // Outputs: 1234.56
    }
  };
  ```

  ```typescript TypeScript theme={null}
  import { validateNumberField } from '@flatfile/plugin-validate-number';

  const customValidation = (): void => {
    const inputValue = '1,234.56';
    const config = { thousandsSeparator: ',', decimalPoint: '.' };

    const result = validateNumberField(inputValue, config);

    if (result.errors.length > 0) {
      console.error('Validation Errors:', result.errors);
    } else if (result.warnings.length > 0) {
      console.warn('Validation Warnings:', result.warnings);
    } else {
      console.log('Validated Value:', result.value); // Outputs: 1234.56
    }
  };
  ```
</CodeGroup>

## API Reference

### validateNumber

The main plugin entry point that returns a function for use with `listener.use()`.

**Parameters:**

* `config` (object): Configuration object containing validation rules and target fields

**Returns:**
A function of type `(listener: FlatfileListener) => void` that registers the validation hook.

**Example:**

<CodeGroup>
  ```javascript JavaScript theme={null}
  listener.use(
    validateNumber({
      fields: ['score'],
      min: 0,
      max: 100,
      inclusive: true,
    })
  );
  ```

  ```typescript TypeScript theme={null}
  listener.use(
    validateNumber({
      fields: ['score'],
      min: 0,
      max: 100,
      inclusive: true,
    })
  );
  ```
</CodeGroup>

### validateNumberField

A standalone utility function that validates a single value against validation rules.

**Parameters:**

* `value` (string | number): The input value to validate
* `config` (NumberValidationConfig): Configuration object with validation rules

**Returns:**
`NumberValidationResult` object with:

* `value` (number | null): The parsed numeric value or null if parsing failed
* `errors` (string\[]): Array of error messages for fundamental parsing failures
* `warnings` (string\[]): Array of warning messages for validation rule violations

**Error Handling Example:**

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { validateNumberField } from '@flatfile/plugin-validate-number';

  const result = validateNumberField('not-a-number', {});
  console.log(result.errors); // Outputs: ['Must be a number']
  console.log(result.value); // Outputs: null

  const result2 = validateNumberField('99.99', { integerOnly: true });
  console.log(result2.warnings); // Outputs: ['Must be an integer']
  console.log(result2.value); // Outputs: 99.99
  ```

  ```typescript TypeScript theme={null}
  import { validateNumberField } from '@flatfile/plugin-validate-number';

  const result = validateNumberField('not-a-number', {});
  console.log(result.errors); // Outputs: ['Must be a number']
  console.log(result.value); // Outputs: null

  const result2 = validateNumberField('99.99', { integerOnly: true });
  console.log(result2.warnings); // Outputs: ['Must be an integer']
  console.log(result2.value); // Outputs: 99.99
  ```
</CodeGroup>

### isPrime

A helper function to check if a number is prime. Used internally when `specialTypes: ['prime']` is configured.

**Parameters:**

* `num` (number): The number to check

**Returns:**
`boolean` - True if the number is prime, false otherwise

## Troubleshooting

* **Validation not working**: Check the `fields` and `sheetSlug` configuration to ensure the plugin is targeting the correct data
* **Unexpected number formats**: Verify the `thousandsSeparator` and `decimalPoint` settings match your data format
* **Reference examples**: The test file `src/validate.number.plugin.spec.ts` provides clear examples of expected outcomes for every configuration option

## Notes

### Default Behavior

* The `min`/`max` validation is **exclusive by default**. To include boundary values, set `inclusive: true`
* Default `thousandsSeparator` is `','` and `decimalPoint` is `'.'`
* If both `round` and `truncate` are true, rounding occurs first, then truncation

### Special Considerations

* The plugin operates on the `commit:created` event, running after user submission but before data finalization
* The plugin modifies `FlatfileRecord` in place, overwriting original values with parsed numeric values
* Fundamental parsing failures (e.g., "abc" as a number) result in "errors"
* Rule violations (e.g., number outside min/max range) result in "warnings"
* The plugin follows standard Flatfile patterns by adding errors/warnings to records rather than throwing exceptions
