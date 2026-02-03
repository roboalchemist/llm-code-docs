# Source: https://flatfile.com/docs/plugins/email.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Email Validation Plugin

> Validate email addresses in Flatfile data imports with format checking, required field validation, and disposable domain blocking

The Email Validation plugin for Flatfile provides a convenient way to validate email addresses in your data. It integrates into the Flatfile Listener as a record hook, automatically checking specified fields on each record. The plugin's core functionalities include validating the email format, checking for required values, and blocking emails from disposable or temporary domains. It is highly configurable, allowing you to specify which fields and sheets to target, provide a custom list of disposable domains, and customize the error messages shown to the user for different validation failures. This is useful for ensuring data quality for contact lists, user sign-ups, and any dataset containing email addresses.

## Installation

Install the plugin using npm:

```bash  theme={null}
npm install @flatfile/plugin-validate-email
```

## Configuration & Parameters

The plugin is configured with a single object passed to the `validateEmail` function.

### sheetSlug

* **Type:** `string`
* **Required:** No
* **Default:** `'**'`
* **Description:** The slug of the sheet to apply the validation to. The default value `'**'` means the plugin will run on all sheets in the workspace.

### emailFields

* **Type:** `string[]`
* **Required:** Yes
* **Description:** An array of strings, where each string is the field key (or column name) that should be validated as an email.

### disposableDomains

* **Type:** `string[]`
* **Required:** No
* **Default:** `[]` (empty array)
* **Description:** A custom list of email domains that should be considered disposable and rejected. The comparison is case-insensitive.

### errorMessages

* **Type:** `object`
* **Required:** No
* **Description:** An object to override the default error messages. The available keys are:
  * `required`: Message for a missing email value. Default: "Email is required"
  * `invalid`: Message for an improperly formatted email. Default: "Invalid email format"
  * `disposable`: Message for an email from a blocked domain. Default: "Disposable email addresses are not allowed"
  * `domain`: Not currently used by the plugin

## Usage Examples

### Basic Usage

This example validates the 'email' field in all sheets with default error messages.

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { validateEmail } from '@flatfile/plugin-validate-email';

  export default function (listener) {
    listener.use(validateEmail({
      emailFields: ['email']
    }));
  }
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { validateEmail } from '@flatfile/plugin-validate-email';

  export default function (listener: FlatfileListener) {
    listener.use(validateEmail({
      emailFields: ['email']
    }));
  }
  ```
</CodeGroup>

### Configuration with Custom Messages

This example validates two email fields, provides custom error messages, and applies the validation only to the 'contacts' sheet.

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { validateEmail } from '@flatfile/plugin-validate-email';

  export default function (listener) {
    listener.use(validateEmail({
      sheetSlug: 'contacts',
      emailFields: ['primary_email', 'secondary_email'],
      errorMessages: {
        required: 'Please enter an email.',
        invalid: 'The email you entered is not valid.',
        disposable: 'Temporary email addresses are not permitted.'
      }
    }));
  }
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { validateEmail } from '@flatfile/plugin-validate-email';

  export default function (listener: FlatfileListener) {
    listener.use(validateEmail({
      sheetSlug: 'contacts',
      emailFields: ['primary_email', 'secondary_email'],
      errorMessages: {
        required: 'Please enter an email.',
        invalid: 'The email you entered is not valid.',
        disposable: 'Temporary email addresses are not permitted.'
      }
    }));
  }
  ```
</CodeGroup>

### Advanced Usage with Disposable Domain Blocking

This example demonstrates using a custom list of disposable domains to block.

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { validateEmail } from '@flatfile/plugin-validate-email';

  export default function (listener) {
    const blockedDomains = ['mailinator.com', 'temp-mail.org', '10minutemail.com'];

    listener.use(validateEmail({
      emailFields: ['email'],
      disposableDomains: blockedDomains,
      errorMessages: {
        disposable: 'This email provider is not allowed. Please use a permanent email address.'
      }
    }));
  }
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { validateEmail } from '@flatfile/plugin-validate-email';

  export default function (listener: FlatfileListener) {
    const blockedDomains = ['mailinator.com', 'temp-mail.org', '10minutemail.com'];

    listener.use(validateEmail({
      emailFields: ['email'],
      disposableDomains: blockedDomains,
      errorMessages: {
        disposable: 'This email provider is not allowed. Please use a permanent email address.'
      }
    }));
  }
  ```
</CodeGroup>

## API Reference

### validateEmail(config)

A factory function that creates a Flatfile record hook. The hook validates specified fields on a record to ensure they are properly formatted and non-disposable email addresses.

**Parameters:**

* `config` (object): A configuration object with the following properties:
  * `sheetSlug` (string, optional): The slug of the sheet to target. Defaults to `'**'` to target all sheets.
  * `emailFields` (string\[], required): An array of field keys to validate.
  * `disposableDomains` (string\[], optional): A list of domains to reject.
  * `errorMessages` (object, optional): An object for custom error messages.

**Return Value:**
Returns a `FlatfileListener` instance configured with the record hook, which can be passed to `listener.use()`.

## Troubleshooting

* **Validation not triggering:** Verify that the `sheetSlug` in the configuration correctly matches the slug of your target Sheet.
* **Fields not being validated:** Ensure the strings in the `emailFields` array exactly match the field keys in your Sheet configuration.
* **Plugin not working:** Confirm that the plugin is correctly registered with a Flatfile listener using `listener.use()`.

## Notes

### Default Behavior

By default, the plugin applies to all sheets. If `errorMessages` are not provided, it uses its own internal messages for required, invalid, and disposable email errors. If `disposableDomains` is not provided, it will not perform any disposable domain checks, only format and presence validation.

### Special Considerations

* This plugin is a "Record Hook" type, meaning it runs on every record as it is processed.
* The validation logic uses a regular expression for format checking. While robust, it may not cover 100% of all edge-case email address formats defined in RFCs.
* The `domain` key within the `errorMessages` configuration object is defined in the type interface but is not currently used in the validation logic.
* The domain check for disposable emails is case-insensitive.

### Error Handling

* The plugin does not throw errors or stop the import process.
* Validation failures are handled by adding an error message to the specific field on the `FlatfileRecord` using the `record.addError()` method.
* This approach allows users to see all data issues inline within the Flatfile interface and correct them before finalizing the import.
