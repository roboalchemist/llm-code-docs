# Source: https://flatfile.com/docs/plugins/isbn.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# ISBN Validator Plugin

> A Flatfile plugin that validates and formats International Standard Book Number (ISBN) data during the import process, supporting both ISBN-10 and ISBN-13 standards with automatic formatting and conversion capabilities.

The ISBN Validator plugin for Flatfile is designed to ensure the quality and consistency of International Standard Book Number (ISBN) data during the import process. It automatically validates fields containing ISBNs against both ISBN-10 and ISBN-13 standards, checking for correct structure and valid check digits.

Key features include the ability to automatically format valid ISBNs with hyphens for better readability and to convert ISBNs between formats (e.g., from ISBN-10 to ISBN-13). The plugin provides clear, field-level error messages for invalid ISBNs and informational messages for successful transformations. It is highly configurable, allowing users to specify which sheets and fields to target, making it a flexible tool for any data onboarding workflow involving book information.

## Installation

Install the plugin using npm:

```bash  theme={null}
npm install @flatfile/plugin-validate-isbn
```

## Configuration & Parameters

The plugin accepts a configuration object with the following parameters:

### `sheetSlug`

* **Type:** `string`
* **Default:** `'**'`
* **Description:** The slug of the sheet to apply the validation to. The default `'**'` applies it to all sheets in the workspace.

### `isbnFields`

* **Type:** `string[]`
* **Default:** `['isbn']`
* **Description:** An array of field keys that contain ISBN values to be validated.

### `autoFormat`

* **Type:** `boolean`
* **Default:** `true`
* **Description:** If set to true, the plugin will automatically format valid ISBNs with hyphens (e.g., '9780306406157' becomes '978-0-306-40615-7').

### `format`

* **Type:** `string` (optional)
* **Default:** `undefined`
* **Description:** If specified, the plugin will attempt to convert the ISBN to the given format. Possible values are `'isbn13'`, `'isbn13h'` (with hyphens), `'isbn10'`, and `'isbn10h'` (with hyphens).

## Usage Examples

### Basic Usage

<Tabs>
  <Tab title="JavaScript">
    ```javascript  theme={null}
    import { FlatfileListener } from "@flatfile/listener";
    import validateISBN from "@flatfile/plugin-validate-isbn";

    const listener = new FlatfileListener();

    // Use the plugin with default settings
    // Validates the 'isbn' field on all sheets and auto-formats it.
    listener.use(validateISBN());
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    import { FlatfileListener } from "@flatfile/listener";
    import validateISBN from "@flatfile/plugin-validate-isbn";

    const listener = new FlatfileListener();

    // Use the plugin with default settings
    // Validates the 'isbn' field on all sheets and auto-formats it.
    listener.use(validateISBN());
    ```
  </Tab>
</Tabs>

### Custom Configuration

<Tabs>
  <Tab title="JavaScript">
    ```javascript  theme={null}
    import { FlatfileListener } from "@flatfile/listener";
    import validateISBN from "@flatfile/plugin-validate-isbn";

    const listener = new FlatfileListener();

    // Use the plugin with custom configuration
    listener.use(
      validateISBN({
        sheetSlug: "books",
        isbnFields: ["primary_isbn", "secondary_isbn"],
        autoFormat: true,
        format: "isbn13h", // Convert all valid ISBNs to hyphenated ISBN-13
      })
    );
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    import { FlatfileListener } from "@flatfile/listener";
    import validateISBN from "@flatfile/plugin-validate-isbn";

    const listener = new FlatfileListener();

    // Use the plugin with custom configuration
    listener.use(
      validateISBN({
        sheetSlug: "books",
        isbnFields: ["primary_isbn", "secondary_isbn"],
        autoFormat: true,
        format: "isbn13h", // Convert all valid ISBNs to hyphenated ISBN-13
      })
    );
    ```
  </Tab>
</Tabs>

### Standalone Validation Function

<Tabs>
  <Tab title="JavaScript">
    ```javascript  theme={null}
    // Using the exported utility function for standalone validation
    import { validateAndFormatISBN } from "@flatfile/plugin-validate-isbn";

    const isbnToTest = "0306406152";

    // Validate and convert an ISBN-10 to a hyphenated ISBN-13
    const result = validateAndFormatISBN(isbnToTest, false, "isbn13h");

    if (result.isValid) {
      console.log("Validation successful!");
      console.log("Converted ISBN:", result.convertedISBN); // Output: 978-0-306-40615-7
    } else {
      console.error("Validation failed:", result.message);
    }
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    // Using the exported utility function for standalone validation
    import { validateAndFormatISBN } from "@flatfile/plugin-validate-isbn";

    const isbnToTest = "0306406152";

    // Validate and convert an ISBN-10 to a hyphenated ISBN-13
    const result = validateAndFormatISBN(isbnToTest, false, "isbn13h");

    if (result.isValid) {
      console.log("Validation successful!");
      console.log("Converted ISBN:", result.convertedISBN); // Output: 978-0-306-40615-7
    } else {
      console.error("Validation failed:", result.message);
    }
    ```
  </Tab>
</Tabs>

## Troubleshooting

Common troubleshooting steps include:

1. **Sheet Configuration:** Verify that the `sheetSlug` in the configuration exactly matches the slug of the target sheet in your Flatfile Space.
2. **Field Mapping:** Ensure the strings in the `isbnFields` array match the field keys in your sheet's data model.
3. **Installation:** Confirm that the plugin is correctly installed (`npm install @flatfile/plugin-validate-isbn`) and imported.

## Notes

### Default Behavior

By default, the plugin runs on all sheets, targets the field with the key 'isbn', and automatically formats any valid ISBNs by adding hyphens. It does not perform any format conversion unless the `format` option is explicitly set.

### Dependencies

This plugin has an external dependency on the `isbn3` library, which handles the core validation and conversion logic. The plugin operates using `recordHook`, which is triggered by the `commit:created` event. This means validation runs after a user submits their data but before the commit is finalized.

### Error Handling

The plugin follows standard Flatfile error handling patterns:

* For validation failures, it uses `record.addError(field, message)` to attach a blocking error to the specific field.
* For successful formatting or conversion, it uses `record.addInfo(field, message)` to provide non-blocking feedback to the user.
* If a configured ISBN field is empty or null for a given record, the plugin skips it without adding an error.
