# Source: https://flatfile.com/docs/plugins/autocast.md

# Autocast Plugin

> Automatically convert data in a Flatfile Sheet to match the data types defined in the corresponding Blueprint

The Autocast plugin is an opinionated transformer for Flatfile that automatically converts data in a Sheet to match the data types defined in the corresponding Blueprint (Schema). It operates on the `commit:created` event, meaning it processes records after they have been committed to the sheet.

Its primary purpose is to clean and standardize data by ensuring that values intended to be numbers, booleans, or dates are correctly typed, even if they are imported as strings. For example, it can convert the string "1,000" to the number `1000`, the string "yes" to the boolean `true`, and the string "08/16/2023" to a standardized UTC date string.

This plugin is useful in any scenario where source data may have inconsistent or incorrect data types, saving developers from writing manual data-casting logic.

## Installation

Install the plugin using npm:

```bash
npm install @flatfile/plugin-autocast
```

## Configuration & Parameters

### Main Plugin Function

The `autocast` function accepts the following parameters:

<ParamField path="sheetSlug" type="string" required>
  The slug of the sheet that the plugin should monitor and apply autocasting to.
</ParamField>

<ParamField path="fieldFilters" type="string[]" optional>
  An optional array of field keys. If provided, the plugin will only attempt to cast values in the specified fields.

  **Default Behavior:** If not provided, the plugin will automatically attempt to cast all fields in the sheet that are not of type 'string' in the Blueprint (i.e., it will target number, boolean, and date fields by default).
</ParamField>

<ParamField path="options" type="object" optional>
  Configuration options for performance and debugging:

  <Expandable title="options properties">
    <ParamField path="chunkSize" type="number" default="10000">
      Specifies the number of records to process in each batch. This is passed down to the underlying bulk record hook.
    </ParamField>

    <ParamField path="parallel" type="number" default="1">
      Specifies how many chunks to process in parallel. This is passed down to the underlying bulk record hook.
    </ParamField>

    <ParamField path="debug" type="boolean" default="false">
      An optional flag to enable debug logging.
    </ParamField>
  </Expandable>
</ParamField>

## Usage Examples

### Basic Usage

Apply autocasting to all supported fields on a sheet:

<CodeGroup>
  ```javascript JavaScript
  import { FlatfileListener } from '@flatfile/listener';
  import { autocast } from '@flatfile/plugin-autocast';

  const listener = new FlatfileListener();

  listener.use(autocast('contacts'));

  export default listener;
  ```

  ```typescript TypeScript
  import { FlatfileListener } from '@flatfile/listener';
  import { autocast } from '@flatfile/plugin-autocast';

  const listener = new FlatfileListener();

  listener.use(autocast('contacts'));

  export default listener;
  ```
</CodeGroup>

### Targeted Field Casting

Apply autocasting to only specific fields:

<CodeGroup>
  ```javascript JavaScript
  import { FlatfileListener } from '@flatfile/listener';
  import { autocast } from '@flatfile/plugin-autocast';

  const listener = new FlatfileListener();

  listener.use(autocast('contacts', ['annualRevenue', 'subscribed']));

  export default listener;
  ```

  ```typescript TypeScript
  import { FlatfileListener } from '@flatfile/listener';
  import { autocast } from '@flatfile/plugin-autocast';

  const listener = new FlatfileListener();

  listener.use(autocast('contacts', ['annualRevenue', 'subscribed']));

  export default listener;
  ```
</CodeGroup>

### Advanced Configuration

Configure field filters and adjust performance settings:

<CodeGroup>
  ```javascript JavaScript
  import { FlatfileListener } from '@flatfile/listener';
  import { autocast } from '@flatfile/plugin-autocast';

  const listener = new FlatfileListener();

  listener.use(
    autocast('contacts', ['annualRevenue', 'subscribed'], {
      chunkSize: 5000,
      parallel: 2,
      debug: true,
    })
  );

  export default listener;
  ```

  ```typescript TypeScript
  import { FlatfileListener } from '@flatfile/listener';
  import { autocast } from '@flatfile/plugin-autocast';

  const listener = new FlatfileListener();

  listener.use(
    autocast('contacts', ['annualRevenue', 'subscribed'], {
      chunkSize: 5000,
      parallel: 2,
      debug: true,
    })
  );

  export default listener;
  ```
</CodeGroup>

### Using Utility Functions

The plugin also exports individual casting utility functions:

<CodeGroup>
  ```javascript JavaScript
  import { castNumber, castBoolean, castDate } from '@flatfile/plugin-autocast';

  // Cast numbers (handles commas)
  const num1 = castNumber('1,234.56'); // Returns 1234.56
  const num2 = castNumber(99); // Returns 99

  // Cast booleans
  const bool1 = castBoolean('yes'); // Returns true
  const bool2 = castBoolean(0); // Returns false
  const bool3 = castBoolean('f'); // Returns false

  // Cast dates
  const date1 = castDate('08/16/2023'); // Returns 'Wed, 16 Aug 2023 00:00:00 GMT'
  const date2 = castDate(1692144000000); // Returns 'Wed, 16 Aug 2023 00:00:00 GMT'
  ```

  ```typescript TypeScript
  import { castNumber, castBoolean, castDate, TRecordValue } from '@flatfile/plugin-autocast';

  // Cast numbers (handles commas)
  const num1: number = castNumber('1,234.56'); // Returns 1234.56
  const num2: number = castNumber(99); // Returns 99

  // Cast booleans
  const bool1: boolean = castBoolean('yes'); // Returns true
  const bool2: boolean = castBoolean(0); // Returns false
  const bool3: boolean = castBoolean('f'); // Returns false

  // Cast dates
  const date1: string = castDate('08/16/2023'); // Returns 'Wed, 16 Aug 2023 00:00:00 GMT'
  const date2: string = castDate(1692144000000); // Returns 'Wed, 16 Aug 2023 00:00:00 GMT'
  ```
</CodeGroup>

## Troubleshooting

### Error Handling with Utility Functions

The individual casting utility functions throw errors when values cannot be converted:

<CodeGroup>
  ```javascript JavaScript
  import { castNumber, castBoolean, castDate } from '@flatfile/plugin-autocast';

  try {
    const invalidNum = castNumber('not a number');
  } catch (e) {
    console.error(e.message); // Prints: Invalid number
  }

  try {
    const invalidBool = castBoolean('maybe');
  } catch (e) {
    console.error(e.message); // Prints: Invalid boolean
  }

  try {
    const invalidDate = castDate('not a date');
  } catch (e) {
    console.error(e.message); // Prints: Invalid date
  }
  ```

  ```typescript TypeScript
  import { castNumber, castBoolean, castDate } from '@flatfile/plugin-autocast';

  try {
    const invalidNum = castNumber('not a number');
  } catch (e: any) {
    console.error(e.message); // Prints: Invalid number
  }

  try {
    const invalidBool = castBoolean('maybe');
  } catch (e: any) {
    console.error(e.message); // Prints: Invalid boolean
  }

  try {
    const invalidDate = castDate('not a date');
  } catch (e: any) {
    console.error(e.message); // Prints: Invalid date
  }
  ```
</CodeGroup>

## Notes

### Event Trigger

The plugin is designed to run on the `listener.on('commit:created')` event.

### Plugin Order

This plugin runs on the same event as `recordHook` and `bulkRecordHook`. The order in which you `.use()` the plugins in your listener matters, as they will execute sequentially.

### Error Handling Pattern

The main `autocast` plugin does not throw errors. Instead, if a value cannot be cast, it attaches an error message directly to the record's cell using `record.addError()`. This makes the errors visible to the user in the Flatfile UI. The individual `cast*` utility functions, however, do throw an `Error` on failure.

### Supported Types

The plugin automatically targets fields of type `number`, `boolean`, and `date` as defined in the Sheet's Blueprint. It does not attempt to cast `string` fields by default.

### Boolean Casting

* **Truthy values:** `'1'`, `'yes'`, `'true'`, `'on'`, `'t'`, `'y'`, and `1`
* **Falsy values:** `'-1'`, `'0'`, `'no'`, `'false'`, `'off'`, `'f'`, `'n'`, `0`, and `-1`

### Date Casting

All parsed dates are converted to a standardized UTC string format. ISO 8601 formats like `YYYY-MM-DD` are treated as UTC, while other formats like `MM/DD/YYYY` are assumed to be local time and are converted to UTC.
