# Source: https://flatfile.com/docs/plugins/translate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Field Translation using Google Translate API

> Automatically translate text content in specified fields using Google Translate API and create new fields with translated content

The Translate plugin for Flatfile integrates with the Google Translate API to automatically translate the text content of specified fields within a sheet. When records are processed, the plugin takes the values from designated source fields, translates them from a specified source language to a target language, and then adds the translated text into newly created fields. The new fields are automatically named by appending the target language code to the original field name (e.g., 'description' becomes 'description\_es'). This is useful for data localization, preparing multilingual product catalogs, or standardizing user-submitted content into a single language.

## Installation

Install the plugin using npm:

```bash  theme={null}
npm install @flatfile/plugin-convert-translate
```

## Configuration & Parameters

The plugin requires a configuration object with the following properties. All options are required and there are no default values:

| Parameter           | Type       | Description                                                                                                      |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------- |
| `sourceLanguage`    | `string`   | The IETF language code of the source text (e.g., 'en' for English)                                               |
| `targetLanguage`    | `string`   | The IETF language code for the target language (e.g., 'es' for Spanish). This is also used to name the new field |
| `sheetSlug`         | `string`   | The slug of the sheet that the plugin should listen to. Records from other sheets will be ignored                |
| `fieldsToTranslate` | `string[]` | An array of field keys (names) that should be translated. The plugin will only process these fields              |
| `projectId`         | `string`   | Your Google Cloud project ID associated with the Google Translate API                                            |
| `keyFilename`       | `string`   | The absolute or relative path to your Google Cloud service account key file (JSON)                               |

### Default Behavior

By default, the plugin does not do anything until it is configured and registered with a Flatfile listener. Once configured, it will listen for record processing events on the specified `sheetSlug`. For each record, it will read the text from the `fieldsToTranslate`, call the Google Translate API, and write the results to new fields. If a field to be translated is empty or null, it is skipped.

## Usage Examples

### Basic Usage

<Tabs>
  <Tab title="JavaScript">
    ```javascript  theme={null}
    import { FlatfileListener } from '@flatfile/listener';
    import { convertTranslatePlugin } from '@flatfile/plugin-convert-translate';

    export default function (listener) {
      listener.use(
        convertTranslatePlugin({
          sourceLanguage: 'en',
          targetLanguage: 'fr',
          sheetSlug: 'contacts',
          fieldsToTranslate: ['notes', 'comments'],
          projectId: 'your-gcp-project-id',
          keyFilename: './gcp-credentials.json',
        })
      );
    }
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    import { FlatfileListener } from '@flatfile/listener';
    import { convertTranslatePlugin } from '@flatfile/plugin-convert-translate';

    export default function (listener: FlatfileListener) {
      listener.use(
        convertTranslatePlugin({
          sourceLanguage: 'en',
          targetLanguage: 'fr',
          sheetSlug: 'contacts',
          fieldsToTranslate: ['notes', 'comments'],
          projectId: 'your-gcp-project-id',
          keyFilename: './gcp-credentials.json',
        })
      );
    }
    ```
  </Tab>
</Tabs>

### Multiple Language Translation

To translate to multiple languages, use the plugin multiple times with different configurations:

<Tabs>
  <Tab title="JavaScript">
    ```javascript  theme={null}
    import { FlatfileListener } from '@flatfile/listener';
    import { convertTranslatePlugin } from '@flatfile/plugin-convert-translate';

    export default function (listener) {
      // Translate to Spanish
      listener.use(
        convertTranslatePlugin({
          sourceLanguage: 'en',
          targetLanguage: 'es',
          sheetSlug: 'products',
          fieldsToTranslate: ['name', 'description'],
          projectId: 'your-gcp-project-id',
          keyFilename: './gcp-credentials.json',
        })
      );

      // Translate to German
      listener.use(
        convertTranslatePlugin({
          sourceLanguage: 'en',
          targetLanguage: 'de',
          sheetSlug: 'products',
          fieldsToTranslate: ['name', 'description'],
          projectId: 'your-gcp-project-id',
          keyFilename: './gcp-credentials.json',
        })
      );
    }
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    import { FlatfileListener } from '@flatfile/listener';
    import { convertTranslatePlugin } from '@flatfile/plugin-convert-translate';

    export default function (listener: FlatfileListener) {
      // Translate to Spanish
      listener.use(
        convertTranslatePlugin({
          sourceLanguage: 'en',
          targetLanguage: 'es',
          sheetSlug: 'products',
          fieldsToTranslate: ['name', 'description'],
          projectId: 'your-gcp-project-id',
          keyFilename: './gcp-credentials.json',
        })
      );

      // Translate to German
      listener.use(
        convertTranslatePlugin({
          sourceLanguage: 'en',
          targetLanguage: 'de',
          sheetSlug: 'products',
          fieldsToTranslate: ['name', 'description'],
          projectId: 'your-gcp-project-id',
          keyFilename: './gcp-credentials.json',
        })
      );
    }
    ```
  </Tab>
</Tabs>

### Manual Translation with translateRecord

<Tabs>
  <Tab title="JavaScript">
    ```javascript  theme={null}
    import { translateRecord, convertTranslatePlugin } from '@flatfile/plugin-convert-translate';

    const config = {
      sourceLanguage: 'en',
      targetLanguage: 'ja',
      sheetSlug: 'articles',
      fieldsToTranslate: ['title'],
      projectId: 'your-gcp-project-id',
      keyFilename: './gcp-credentials.json',
    };

    // Initialize the client (required for translateRecord to work)
    convertTranslatePlugin(listener, config);

    // Manually process a record
    record.set('title', 'Hello World');
    const { record: updatedRecord, error } = translateRecord(record, config);

    if (error) {
      console.error('Translation failed:', error);
    } else {
      const translatedTitle = updatedRecord.get('title_ja');
      console.log(translatedTitle); // Expected to be the Japanese translation
    }
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    import { FlatfileRecord } from '@flatfile/plugin-record-hook';
    import { translateRecord, convertTranslatePlugin, TranslationConfig } from '@flatfile/plugin-convert-translate';

    const config: TranslationConfig = {
      sourceLanguage: 'en',
      targetLanguage: 'ja',
      sheetSlug: 'articles',
      fieldsToTranslate: ['title'],
      projectId: 'your-gcp-project-id',
      keyFilename: './gcp-credentials.json',
    };

    // Initialize the client (required for translateRecord to work)
    convertTranslatePlugin(listener, config);

    // Manually process a record
    record.set('title', 'Hello World');
    const { record: updatedRecord, error } = translateRecord(record, config);

    if (error) {
      console.error('Translation failed:', error);
    } else {
      const translatedTitle = updatedRecord.get('title_ja');
      console.log(translatedTitle); // Expected to be the Japanese translation
    }
    ```
  </Tab>
</Tabs>

## API Reference

### convertTranslatePlugin

The main entry point for the plugin. This function registers a `recordHook` with the provided Flatfile listener, which will automatically translate specified fields on records belonging to the configured sheet.

**Signature:**

```typescript  theme={null}
convertTranslatePlugin(listener: FlatfileListener, config: TranslationConfig): void
```

**Parameters:**

* `listener`: FlatfileListener - An instance of a Flatfile listener to attach the hook to
* `config`: TranslationConfig - The configuration object for the plugin

**Returns:**
`void` - This function does not return a value. It modifies the listener instance directly.

### translateRecord

A standalone function that applies the translation logic to a single `FlatfileRecord`. It reads values from the fields specified in the config, translates them, and sets the translated values on new fields in the record.

**Signature:**

```typescript  theme={null}
translateRecord(record: FlatfileRecord, config: TranslationConfig): { record: FlatfileRecord; error?: string }
```

**Parameters:**

* `record`: FlatfileRecord - The record to process
* `config`: TranslationConfig - A configuration object specifying languages, fields, and credentials

**Returns:**
An object containing:

* `record`: FlatfileRecord - The record with new fields containing translated text
* `error?`: string - An error message if an issue occurred during processing

## Troubleshooting

### Error Handling

The plugin includes comprehensive error handling:

* **API Errors**: If the Google Translate API call fails, the error is logged to the console and the record won't be updated with translated values
* **Record-level Errors**: If an error occurs during processing of a single record, the plugin will attach a general error message to that specific record using `record.addError()`, making it visible in the Flatfile UI
* **No Text to Translate**: If a record has no text in any of the `fieldsToTranslate`, it is skipped without error

<Tabs>
  <Tab title="JavaScript">
    ```javascript  theme={null}
    // Error handling example
    const { record: updatedRecord, error } = translateRecord(record, config);

    if (error) {
      // This adds the error to the record, which is visible to the user
      updatedRecord.addError('general', error);
    }

    return updatedRecord;
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    // Error handling example
    const { record: updatedRecord, error } = translateRecord(record, config);

    if (error) {
      // This adds the error to the record, which is visible to the user
      updatedRecord.addError('general', error);
    }

    return updatedRecord;
    ```
  </Tab>
</Tabs>

## Notes

### Requirements

* **Google Cloud Account**: A Google Cloud project with the Translate API enabled is required
* **Credentials**: You must provide a valid `projectId` and a path to a service account `keyFilename` with appropriate permissions

### Field Naming Convention

The plugin creates new fields for translated content by appending `_{targetLanguage}` to the original field name (e.g., `name` becomes `name_es`). Ensure this does not conflict with existing fields in your sheet configuration.

### Limitations

* **Field Types**: The plugin is designed to work with `string` fields. Behavior with other field types is undefined
* **Initialization**: The Google Translate client is initialized globally within the plugin's scope when `convertTranslatePlugin` is first called. Subsequent calls with different credentials will re-initialize the client
