# Source: https://flatfile.com/docs/plugins/pdf-extractor.md

# PDF Extractor Plugin

> Extract tabular data from PDF files and convert them to CSV format using the pdftables.com service

The PDF Extractor plugin is designed to process PDF files uploaded to Flatfile. Its main purpose is to extract tabular data from a PDF document and make it available for import. When a user uploads a PDF file, this plugin automatically sends the file to the external `pdftables.com` service, which converts the data into a CSV format. The resulting CSV file is then uploaded back into the same Flatfile Space as a new file, ready to be mapped and imported. This is useful for workflows where source data is provided in PDF reports or documents instead of standard spreadsheet formats.

## Installation

Install the plugin using npm:

```bash
npm install @flatfile/plugin-pdf-extractor
```

## Configuration & Parameters

The `pdfExtractorPlugin` function accepts a configuration object with the following options:

| Parameter | Type      | Required | Default | Description                                |
| --------- | --------- | -------- | ------- | ------------------------------------------ |
| `apiKey`  | `string`  | Yes      | -       | Your API key from `pdftables.com` service  |
| `debug`   | `boolean` | No       | `false` | Enable verbose logging for troubleshooting |

### Default Behavior

By default, the plugin operates with debugging messages turned off. It will listen for any `.pdf` file uploaded in `import` mode. If a matching file is detected, it will attempt the conversion process. If the required `apiKey` is not provided, the plugin will log an error and fail silently.

## Usage Examples

<Tabs>
  <Tab title="JavaScript">
    ```javascript
    // listener.js
    import { pdfExtractorPlugin } from "@flatfile/plugin-pdf-extractor";

    export default function (listener) {
      // A pdftables.com API key is required
      listener.use(pdfExtractorPlugin({ 
        apiKey: "YOUR_PDFTABLES_API_KEY" 
      }));
    }
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript
    // listener.ts
    import { FlatfileListener } from "@flatfile/listener";
    import { pdfExtractorPlugin } from "@flatfile/plugin-pdf-extractor";

    export default function (listener: FlatfileListener) {
      // A pdftables.com API key is required
      listener.use(pdfExtractorPlugin({ 
        apiKey: "YOUR_PDFTABLES_API_KEY" 
      }));
    }
    ```
  </Tab>
</Tabs>

### Configuration with Debug Mode

<Tabs>
  <Tab title="JavaScript">
    ```javascript
    // listener.js
    import { pdfExtractorPlugin } from "@flatfile/plugin-pdf-extractor";

    export default function (listener) {
      // Using the plugin with debug option enabled for detailed logging
      listener.use(
        pdfExtractorPlugin({
          apiKey: "YOUR_PDFTABLES_API_KEY",
          debug: true,
        })
      );
    }
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript
    // listener.ts
    import { FlatfileListener } from "@flatfile/listener";
    import { pdfExtractorPlugin } from "@flatfile/plugin-pdf-extractor";

    export default function (listener: FlatfileListener) {
      // Using the plugin with debug option enabled for detailed logging
      listener.use(
        pdfExtractorPlugin({
          apiKey: "YOUR_PDFTABLES_API_KEY",
          debug: true,
        })
      );
    }
    ```
  </Tab>
</Tabs>

## Troubleshooting

If the plugin is not working properly, follow these troubleshooting steps:

1. **Check API Key**: Ensure that a valid `apiKey` has been provided in the configuration
2. **Enable Debug Mode**: Set `debug: true` in the plugin configuration to get detailed logs in your listener's console output
3. **Network Access**: Ensure the listener environment has network access to `pdftables.com`

### Error Handling

The plugin has built-in error handling and will log errors to the console. Common errors include:

* "Found invalid API key"
* "Failed to convert PDF on pdftables.com"
* "Error writing file to disk"
* "Failed to upload PDF->CSV file"

<Tabs>
  <Tab title="JavaScript">
    ```javascript
    // Enable debug mode to see detailed error messages
    listener.use(
      pdfExtractorPlugin({
        apiKey: "YOUR_PDFTABLES_API_KEY",
        debug: true, // This will log errors from the API call or file upload
      })
    );
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript
    // Enable debug mode to see detailed error messages
    listener.use(
      pdfExtractorPlugin({
        apiKey: "YOUR_PDFTABLES_API_KEY",
        debug: true, // This will log errors from the API call or file upload
      })
    );
    ```
  </Tab>
</Tabs>

## Notes

### Requirements and Limitations

* **External Dependency**: This plugin requires a subscription and a valid API key from the third-party service `pdftables.com`
* **File Scope**: The plugin only processes files with a `.pdf` extension that are uploaded in `import` mode. It will ignore all other files
* **Environment**: This plugin is intended to be run in a server-side listener environment (e.g., Node.js) as it interacts with the file system

### Processing Details

* **Asynchronous Processing**: The PDF conversion and re-upload process is asynchronous. After a user uploads a PDF, the new converted CSV file will appear in the "Files" list in the Flatfile Space a few moments later
* **File Naming**: The converted file will be named based on the original, with ` (Converted PDF)-{timestamp}.csv` appended to it
