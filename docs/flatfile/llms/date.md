# Source: https://flatfile.com/docs/plugins/date.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Date Format Normalizer

> Automatically parse and standardize date values during data import, converting various date formats into a consistent output format.

The Date Format Normalizer plugin for Flatfile is designed to automatically parse and standardize date values during the data import process. Its primary purpose is to detect various common date and time formats within specified fields and convert them into a single, consistent output format. This is useful when importing data from different sources that may use different date conventions (e.g., 'MM/DD/YYYY', 'YYYY-MM-DD', 'Jan 15, 2023'). The plugin can be configured to operate on specific fields across one or all sheets, and it can handle both date-only and date-time values. If a date string cannot be parsed, the plugin adds an error to the corresponding cell, alerting the user to the issue.

## Installation

Install the plugin via npm:

```bash  theme={null}
npm install @flatfile/plugin-validate-date
```

## Configuration & Parameters

The plugin accepts a configuration object with the following parameters:

### sheetSlug

* **Type:** `string` (optional)
* **Default:** `'**'` (all sheets)
* **Description:** The slug of the sheet to which the date normalization should be applied. If this option is omitted, the plugin will apply to all sheets in the workbook.

### dateFields

* **Type:** `string[]` (required)
* **Description:** An array of field keys (the column names) that contain date values needing normalization. The plugin will process each field listed in this array for every record.

### outputFormat

* **Type:** `string` (required)
* **Description:** A string defining the desired output format for the dates, following the `date-fns` format patterns (e.g., 'MM/dd/yyyy', 'yyyy-MM-dd HH:mm:ss').

### includeTime

* **Type:** `boolean` (required)
* **Description:** A boolean that determines whether to include the time component in the final output. If set to `false`, any time information from the parsed date will be stripped, leaving only the date part. If `true`, the time will be included as formatted by `outputFormat`.

### locale

* **Type:** `string` (optional)
* **Default:** `'en-US'` (hardcoded)
* **Description:** Specifies the locale for date parsing. Note: Although this option exists in the configuration interface, the current implementation hardcodes the locale to 'en-US' and does not use the value provided in this parameter.

## Usage Examples

### Basic Usage

This example applies date normalization to the 'start\_date' field on all sheets, converting dates to 'YYYY-MM-DD' format.

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener'
  import { validateDate } from '@flatfile/plugin-validate-date'

  export default function (listener) {
    listener.use(
      validateDate({
        dateFields: ['start_date'],
        outputFormat: 'yyyy-MM-dd',
        includeTime: false
      })
    )
  }
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener'
  import { validateDate } from '@flatfile/plugin-validate-date'

  export default function (listener: FlatfileListener) {
    listener.use(
      validateDate({
        dateFields: ['start_date'],
        outputFormat: 'yyyy-MM-dd',
        includeTime: false
      })
    )
  }
  ```
</CodeGroup>

### Configuration Example

This example configures the plugin to run only on the 'contacts' sheet. It normalizes two different date fields, 'birth\_date' and 'registration\_date', to the 'MM/dd/yyyy' format and excludes time.

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener'
  import { validateDate } from '@flatfile/plugin-validate-date'

  export default function (listener) {
    listener.use(
      validateDate({
        sheetSlug: 'contacts',
        dateFields: ['birth_date', 'registration_date'],
        outputFormat: 'MM/dd/yyyy',
        includeTime: false
      })
    )
  }
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener'
  import { validateDate } from '@flatfile/plugin-validate-date'

  export default function (listener: FlatfileListener) {
    listener.use(
      validateDate({
        sheetSlug: 'contacts',
        dateFields: ['birth_date', 'registration_date'],
        outputFormat: 'MM/dd/yyyy',
        includeTime: false
      })
    )
  }
  ```
</CodeGroup>

### Advanced Usage (Including Time)

This example normalizes the 'event\_timestamp' field to a format that includes both date and time.

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener'
  import { validateDate } from '@flatfile/plugin-validate-date'

  export default function (listener) {
    listener.use(
      validateDate({
        sheetSlug: 'event_logs',
        dateFields: ['event_timestamp'],
        outputFormat: 'yyyy-MM-dd HH:mm:ss',
        includeTime: true
      })
    )
  }
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener'
  import { validateDate } from '@flatfile/plugin-validate-date'

  export default function (listener: FlatfileListener) {
    listener.use(
      validateDate({
        sheetSlug: 'event_logs',
        dateFields: ['event_timestamp'],
        outputFormat: 'yyyy-MM-dd HH:mm:ss',
        includeTime: true
      })
    )
  }
  ```
</CodeGroup>

### Error Handling Example

If a date string cannot be parsed, the plugin adds an error to the specific cell. For example, if you try to import a record with `due_date: 'not a real date'`, the plugin will not change the value but will attach an error message.

<CodeGroup>
  ```javascript JavaScript theme={null}
  // Source Record:
  // { due_date: 'not a real date' }

  // After plugin runs, the record in Flatfile will have an error:
  // Field: 'due_date'
  // Value: 'not a real date'
  // Error Message: 'Unable to parse date string'

  import { FlatfileListener } from '@flatfile/listener'
  import { validateDate } from '@flatfile/plugin-validate-date'

  export default function (listener) {
    listener.use(
      validateDate({
        sheetSlug: 'tasks',
        dateFields: ['due_date'],
        outputFormat: 'MM/dd/yyyy',
        includeTime: false
      })
    )
  }
  ```

  ```typescript TypeScript theme={null}
  // Source Record:
  // { due_date: 'not a real date' }

  // After plugin runs, the record in Flatfile will have an error:
  // Field: 'due_date'
  // Value: 'not a real date'
  // Error Message: 'Unable to parse date string'

  import { FlatfileListener } from '@flatfile/listener'
  import { validateDate } from '@flatfile/plugin-validate-date'

  export default function (listener: FlatfileListener) {
    listener.use(
      validateDate({
        sheetSlug: 'tasks',
        dateFields: ['due_date'],
        outputFormat: 'MM/dd/yyyy',
        includeTime: false
      })
    )
  }
  ```
</CodeGroup>

## Troubleshooting

If dates are not being normalized as expected, consider the following:

* **Check Configuration:** Verify that the `sheetSlug` and `dateFields` in the configuration correctly match your workbook setup.
* **Validate Format String:** Ensure that the `outputFormat` string is a valid format recognized by `date-fns`.
* **Locale Issues:** If a valid date is being marked with an error, it may be in a format not recognized by `chrono-node` or it may conflict with the hardcoded 'en-US' locale (e.g., a DD/MM/YYYY format might be misinterpreted as MM/DD/YYYY).

## Notes

### Default Behavior

The plugin hooks into the `commit:created` event. For each committed record, it checks the fields specified in `dateFields`. If a value exists, it attempts to parse it as a date. If successful, it reformats the date according to `outputFormat` and updates the record. If parsing fails, it adds an error message to the cell and leaves the original value unchanged. By default, it operates on all sheets unless a specific `sheetSlug` is provided.

### Special Considerations

* The plugin relies on the `chrono-node` library for date parsing, which supports a wide variety of natural language and standard date formats.
* The plugin hooks into the `commit:created` event, meaning it runs after a user submits their data and before it is finalized.
* The `outputFormat` string must be compatible with the `date-fns` formatting library.

### Limitations

* The `locale` configuration option is not currently implemented. The plugin defaults to using the 'en-US' locale for parsing, regardless of the value passed in the configuration. This may affect parsing of formats where the day and month order are ambiguous (e.g., '01/02/2023').

### Error Handling

The plugin's error handling is simple: if `chrono-node` cannot parse the date string from a given field, the function returns `null`. The plugin then calls `record.addError(field, 'Unable to parse date string')` to flag the cell with an error message in the Flatfile UI. The original, un-parsable value is kept in the cell.
