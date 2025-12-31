# Source: https://flatfile.com/docs/plugins/phone.md

# Phone Number Validation and Formatting Plugin

> Validates and formats phone numbers in Flatfile using country-specific validation with libphonenumber-js library

This plugin validates phone numbers in a specified field against a corresponding country code from another field. It leverages the `libphonenumber-js` library for robust, country-specific validation. The primary use case is to ensure that phone number data ingested into Flatfile is correctly formatted and valid. It can automatically correct and reformat phone numbers into various standard formats (e.g., NATIONAL, INTERNATIONAL, E164) or simply add an error to the record if the number is invalid.

## Installation

Install the plugin using npm:

```bash
npm install @flatfile/plugin-validate-phone
```

## Configuration & Parameters

The plugin accepts a configuration object with the following parameters:

| Parameter       | Type    | Required | Default      | Description                                                                                 |
| --------------- | ------- | -------- | ------------ | ------------------------------------------------------------------------------------------- |
| `phoneField`    | string  | Yes      | -            | The API key (name) of the field containing the phone number to validate                     |
| `countryField`  | string  | Yes      | -            | The API key (name) of the field containing the country code (e.g., 'US', 'GB')              |
| `sheetSlug`     | string  | No       | `'**'`       | The slug of the sheet to apply the validation to. Defaults to all sheets                    |
| `autoConvert`   | boolean | No       | `true`       | If true, automatically updates the phone number field with the correctly formatted version  |
| `format`        | string  | No       | `'NATIONAL'` | The desired output format: 'NATIONAL', 'INTERNATIONAL', 'E164', 'RFC3966', or 'SIGNIFICANT' |
| `concurrency`   | number  | No       | `10`         | Number of records to process concurrently                                                   |
| `debug`         | boolean | No       | `false`      | Enables verbose debug logging in the console                                                |
| `formatOptions` | object  | No       | -            | Additional formatting options for libphonenumber-js library                                 |

## Usage Examples

### Basic Usage

<CodeGroup>
  ```javascript JavaScript
  import { FlatfileListener } from '@flatfile/listener';
  import validatePhone from '@flatfile/plugin-validate-phone';

  export default function (listener) {
    listener.use(validatePhone({
      phoneField: 'phone',
      countryField: 'country',
      autoConvert: false
    }));
  }
  ```

  ```typescript TypeScript
  import { FlatfileListener } from '@flatfile/listener';
  import validatePhone from '@flatfile/plugin-validate-phone';

  export default function (listener: FlatfileListener) {
    listener.use(validatePhone({
      phoneField: 'phone',
      countryField: 'country',
      autoConvert: false
    }));
  }
  ```
</CodeGroup>

This example validates the 'phone' field using the 'country' field in all sheets. It will add errors for invalid numbers but will not automatically reformat them.

### Configuration Example

<CodeGroup>
  ```javascript JavaScript
  import { FlatfileListener } from '@flatfile/listener';
  import validatePhone from '@flatfile/plugin-validate-phone';

  export default function (listener) {
    listener.use(validatePhone({
      sheetSlug: 'contacts',
      phoneField: 'phone_number',
      countryField: 'country_code',
      autoConvert: true,
      format: 'INTERNATIONAL',
      debug: true
    }));
  }
  ```

  ```typescript TypeScript
  import { FlatfileListener } from '@flatfile/listener';
  import validatePhone from '@flatfile/plugin-validate-phone';

  export default function (listener: FlatfileListener) {
    listener.use(validatePhone({
      sheetSlug: 'contacts',
      phoneField: 'phone_number',
      countryField: 'country_code',
      autoConvert: true,
      format: 'INTERNATIONAL',
      debug: true
    }));
  }
  ```
</CodeGroup>

This example validates and formats phone numbers in the "contacts" sheet using the 'phone\_number' and 'country\_code' fields. Valid numbers are automatically converted to INTERNATIONAL format.

### Advanced Usage with Format Options

<CodeGroup>
  ```javascript JavaScript
  import { FlatfileListener } from '@flatfile/listener';
  import validatePhone from '@flatfile/plugin-validate-phone';

  export default function (listener) {
    listener.use(validatePhone({
      sheetSlug: 'my-sheet',
      phoneField: 'phone_number',
      countryField: 'country_code',
      format: 'INTERNATIONAL',
      formatOptions: { formatExtension: 'national' }
    }));
  }
  ```

  ```typescript TypeScript
  import { FlatfileListener } from '@flatfile/listener';
  import validatePhone from '@flatfile/plugin-validate-phone';

  export default function (listener: FlatfileListener) {
    listener.use(validatePhone({
      sheetSlug: 'my-sheet',
      phoneField: 'phone_number',
      countryField: 'country_code',
      format: 'INTERNATIONAL',
      formatOptions: { formatExtension: 'national' }
    }));
  }
  ```
</CodeGroup>

This example demonstrates using the formatOptions parameter to provide more specific formatting rules from the underlying libphonenumber-js library.

## Troubleshooting

If validation is not working as expected:

1. **Check field names**: Ensure that the `phoneField` and `countryField` values in the configuration exactly match the field keys in your Sheet template.

2. **Verify country codes**: Ensure the `countryField` in your data contains valid two-letter ISO 3166-1 alpha-2 country codes (e.g., "US", "GB", "DE").

3. **Enable debug logging**: Set the `debug` option to `true` in the configuration to see more detailed logging output in your environment's console, which can help diagnose issues.

## Notes

### Default Behavior

* By default, the plugin applies to all sheets (`sheetSlug: '**'`)
* Phone numbers are automatically converted to the specified format when `autoConvert` is `true` (default)
* The default format is 'NATIONAL'
* Records are processed with a concurrency of 10

### Error Handling

The plugin adds errors to specific fields rather than throwing exceptions:

* **Empty phone number**: "Phone number is required"
* **Empty country field**: "Country is required for phone number formatting"
* **Invalid phone number**: "Invalid phone number format for \[country]"

### Requirements and Limitations

* This plugin has an external dependency on `libphonenumber-js`
* The `countryField` must contain a valid two-letter ISO 3166-1 alpha-2 country code
* The plugin operates as a listener on the `commit:created` event, processing records in batches
* While the documentation mentions specific support for US, UK, India, Germany, France, and Brazil, the underlying library supports a wider range of countries
