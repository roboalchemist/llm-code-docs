# Source: https://flatfile.com/docs/guides/egress.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Data Egress

> Get data out of Flatfile using various transmission methods and file formats

After your customers have imported and validated their data in Flatfile, you need to get that data to its final destination. Data egress refers to the process of extracting and transmitting data from Flatfile to external systems, files, or destinations.

## Egress Methods

Since Flatfile listeners run in TypeScript/JavaScript environments, you can egress data using any mechanism available in the language ecosystem. This includes direct API calls, file generation, database connections, message queues, or any custom integration pattern your application requires.

### API Transmission

Send data directly to external systems via HTTP requests to REST APIs, GraphQL endpoints, streaming services, or database APIs. Use any HTTP client library or built-in fetch to POST data to your existing endpoints.

### File Generation & Download

Build files in any format - CSV, XLSX, XML, JSON, PDF, or custom formats - using the appropriate TypeScript libraries. Generate formatted reports, structured documents, or data exports that users can download directly.

### File Transfer

Transmit generated files to external destinations like cloud storage, FTP servers, email attachments, or content delivery networks using the corresponding SDK or protocol library.

## Example: API Egress with Workbook Actions

The following example demonstrates egressing data via HTTP POST when users complete a workbook. This pattern listens for a workbook action and sends the data to an external webhook endpoint.

### Implementation

The example listener responds to `workbook:submitActionFg` events, retrieves all sheets and records from the workbook, and posts the data to a configured webhook URL. It uses the `event.secrets()` method to securely access the destination URL.

### Testing with webhook.site

To test this pattern:

1. Navigate to [webhook.site](https://webhook.site) and copy your unique URL
2. Add the URL as a Flatfile secret named `WEBHOOK_SITE_URL`
3. Configure a workbook action in your blueprint to trigger the egress
4. The listener will POST the workbook data to your webhook.site URL where you can inspect the payload

### Example Projects

* [TypeScript implementation](https://github.com/FlatFilers/flatfile-docs-kitchen-sink/blob/main/typescript/egress/index.ts)
* [JavaScript implementation](https://github.com/FlatFilers/flatfile-docs-kitchen-sink/blob/main/javascript/egress/index.js)

## Example: File Export with Export Workbook Plugin

For file generation and download, Flatfile provides the Export Workbook Plugin that generates Excel files from workbook data. This plugin handles the entire process of extracting data, formatting it into Excel sheets, and making it available for download.

### Installation

```bash  theme={null}
npm install @flatfile/plugin-export-workbook
```

### Implementation

```javascript  theme={null}
import { FlatfileListener } from "@flatfile/listener";
import { exportWorkbookPlugin } from "@flatfile/plugin-export-workbook";

export default function (listener) {
  listener.use(
    exportWorkbookPlugin({
      // Only export validated records
      recordFilter: 'valid',
      // Automatically trigger download
      autoDownload: true,
      // Custom filename
      filename: 'exported-data',
      // Transform column names for readability
      columnNameTransformer: (columnName) => {
        return columnName.replace(/([A-Z])/g, ' $1').replace(/^./, str => str.toUpperCase());
      }
    })
  );
}
```

### Workbook Configuration

Add a download action to your workbook to trigger the export:

```javascript  theme={null}
{
  name: "Customer Data",
  actions: [
    {
      operation: "downloadWorkbook",
      mode: "foreground", 
      label: "Download Excel File",
      description: "Export all data as Excel spreadsheet",
      primary: true
    }
  ],
  sheets: [
    // your sheet definitions
  ]
}
```

When users click the download action, the plugin generates an Excel file containing all workbook data and either triggers an automatic download or directs users to the Files page to download manually.

For complete configuration options and advanced usage, see the [Export Workbook Plugin documentation](/plugins/export-workbook).

## Example: Custom XML File Generation

For custom file formats, you can build files programmatically using any TypeScript library. This example demonstrates creating XML files using the `xml2js` library to generate structured data exports.

### Installation

```bash  theme={null}
npm install xml2js
npm install @types/xml2js --save-dev
```

### Implementation

```javascript  theme={null}
import api from "@flatfile/api";
import { FlatfileListener } from "@flatfile/listener";
import { Builder } from 'xml2js';
import fs from 'fs';

export default function (listener) {
  listener.on(
    "job:ready",
    { job: "workbook:downloadXML" },
    async ({ context: { jobId, workbookId } }) => {
      try {
        await api.jobs.ack(jobId, {
          info: "Starting XML generation...",
          progress: 10,
        });

        // Get workbook and find the target sheet
        const workbook = await api.workbooks.get(workbookId);
        const sheet = workbook?.data.sheets?.find(sheet => sheet.slug === "customers");
        const records = await api.records.get(sheet?.id || "");

        await api.jobs.ack(jobId, {
          info: "Processing records...",
          progress: 30,
        });

        // Initialize XML builder
        const builder = new Builder({
          xmldec: { version: '1.0', encoding: 'UTF-8' }
        });

        // Transform records to structured data
        const customers = records.data.records.map(record => {
          const values = record.values;
          return {
            id: values.id?.value || '',
            name: values.name?.value || '',
            email: values.email?.value || '',
            phone: values.phone?.value || '',
            address: {
              street: values.street?.value || '',
              city: values.city?.value || '',
              state: values.state?.value || '',
              zip: values.zip?.value || ''
            }
          };
        });

        // Create XML structure
        const xmlObj = {
          export: {
            $: { 
              generated: new Date().toISOString(),
              recordCount: customers.length 
            },
            customers: {
              customer: customers
            }
          }
        };

        // Generate XML string
        const xml = builder.buildObject(xmlObj);

        await api.jobs.ack(jobId, {
          info: "Creating XML file...",
          progress: 70,
        });

        // Write XML to temporary file
        const fileName = `customer_export_${new Date().toISOString().split('T')[0]}.xml`;
        fs.writeFileSync(fileName, xml);

        // Upload file to Flatfile
        const file = fs.createReadStream(fileName);
        const fileUpload = await api.files.upload(file, {
          spaceId: workbook.data.spaceId,
          environmentId: workbook.data.environmentId,
        });

        // Complete job with download link
        await api.jobs.complete(jobId, {
          outcome: {
            message: "XML file generated successfully",
            next: {
              type: "files",
              label: "Download XML",
              files: [{ fileId: fileUpload?.data?.id }],
            },
          },
        });

        // Clean up temporary file
        fs.unlinkSync(fileName);

      } catch (error) {
        await api.jobs.fail(jobId, {
          outcome: {
            message: `Failed to generate XML: ${error.message}`,
          },
        });
      }
    }
  );
}
```

### Workbook Configuration

Add an XML download action to trigger the export:

```javascript  theme={null}
{
  name: "Customer Data",
  actions: [
    {
      operation: "downloadXML",
      mode: "foreground",
      label: "Download XML",
      description: "Export data as XML file",
      primary: false
    }
  ],
  sheets: [
    {
      name: "Customers",
      slug: "customers",
      fields: [
        { key: "id", type: "string", label: "Customer ID" },
        { key: "name", type: "string", label: "Name" },
        { key: "email", type: "string", label: "Email" },
        { key: "phone", type: "string", label: "Phone" },
        { key: "street", type: "string", label: "Street" },
        { key: "city", type: "string", label: "City" },
        { key: "state", type: "string", label: "State" },
        { key: "zip", type: "string", label: "ZIP Code" }
      ]
    }
  ]
}
```

This pattern can be adapted for any file format by substituting the appropriate library and transformation logic. The key steps remain the same: fetch data, transform it, generate the file, upload it to Flatfile, and provide a download link to users.
