# Source: https://flatfile.com/docs/plugins/xml-extractor.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# XML Extractor

> A Flatfile plugin for parsing XML files, flattening nested structures and attributes, and converting them into tabular format for easy import into Flatfile Sheets.

The XML Extractor plugin processes .xml files uploaded to Flatfile by parsing XML data, flattening its nested structure and attributes, and converting it into a tabular format. The plugin automatically detects the main collection of records within the XML file and transforms each record into a row, making it ideal for importing structured XML data from legacy systems, APIs, or data exports.

## Installation

Install the XML Extractor plugin using npm:

```bash  theme={null}
npm install @flatfile/plugin-xml-extractor
```

## Configuration & Parameters

The XML Extractor accepts the following configuration options:

| Parameter         | Type     | Default     | Description                                                           |
| ----------------- | -------- | ----------- | --------------------------------------------------------------------- |
| `separator`       | string   | `"/"`       | Character used to separate keys when flattening nested XML elements   |
| `attributePrefix` | string   | `"#"`       | Prefix added to keys derived from XML element attributes              |
| `transform`       | function | `undefined` | Function to transform each parsed data row before passing to Flatfile |
| `chunkSize`       | number   | `10000`     | Number of records to process in each batch                            |
| `parallel`        | number   | `1`         | Number of chunks to process concurrently                              |
| `debug`           | boolean  | `false`     | Enable verbose logging for debugging                                  |

### Default Behavior

By default, the plugin:

* Flattens nested elements using `"/"` as a separator (e.g., `<country><name>USA</name></country>` becomes `"country/name"`)
* Prefixes attributes with `"#"` (e.g., `<country code="US">` becomes `"country#code"`)
* Processes files in chunks of 10,000 records with sequential processing
* Automatically infers headers from all unique keys found across records

## Usage Examples

### Basic Usage

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { listener } from '@flatfile/listener';
  import { XMLExtractor } from '@flatfile/plugin-xml-extractor';

  export default listener.on('file:created', (event) => {
    // Only handle .xml files
    if (event.context.file.ext !== 'xml') {
      return;
    }
    return XMLExtractor()(event);
  });
  ```

  ```typescript TypeScript theme={null}
  import { listener } from '@flatfile/listener';
  import { XMLExtractor } from '@flatfile/plugin-xml-extractor';
  import type { FlatfileEvent } from '@flatfile/listener';

  export default listener.on('file:created', (event: FlatfileEvent) => {
    // Only handle .xml files
    if (event.context.file.ext !== 'xml') {
      return;
    }
    return XMLExtractor()(event);
  });
  ```
</CodeGroup>

### Custom Configuration

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { listener } from '@flatfile/listener';
  import { XMLExtractor } from '@flatfile/plugin-xml-extractor';

  export default listener.on('file:created', (event) => {
    if (event.context.file.ext !== 'xml') {
      return;
    }
    return XMLExtractor({
      separator: '_',
      attributePrefix: '@',
      transform: (row) => {
        if (row.age) {
          row.age = parseInt(row.age, 10);
        }
        return row;
      },
      chunkSize: 5000,
      parallel: 2,
    })(event);
  });
  ```

  ```typescript TypeScript theme={null}
  import { listener } from '@flatfile/listener';
  import { XMLExtractor } from '@flatfile/plugin-xml-extractor';
  import type { FlatfileEvent } from '@flatfile/listener';

  export default listener.on('file:created', (event: FlatfileEvent) => {
    if (event.context.file.ext !== 'xml') {
      return;
    }
    return XMLExtractor({
      separator: '_',
      attributePrefix: '@',
      transform: (row: Record<string, any>) => {
        if (row.age) {
          row.age = parseInt(row.age, 10);
        }
        return row;
      },
      chunkSize: 5000,
      parallel: 2,
    })(event);
  });
  ```
</CodeGroup>

### Using the Standalone Parser

<CodeGroup>
  ```javascript JavaScript theme={null}
  import * as fs from 'fs';
  import { xmlParser } from '@flatfile/plugin-xml-extractor';

  const xmlBuffer = fs.readFileSync('path/to/your/file.xml');
  const workbookData = xmlParser(xmlBuffer, { separator: '.' });

  console.log(workbookData.Sheet1.headers);
  console.log(workbookData.Sheet1.data[0]);
  ```

  ```typescript TypeScript theme={null}
  import * as fs from 'fs';
  import { xmlParser } from '@flatfile/plugin-xml-extractor';

  const xmlBuffer: Buffer = fs.readFileSync('path/to/your/file.xml');
  const workbookData = xmlParser(xmlBuffer, { separator: '.' });

  console.log(workbookData.Sheet1.headers);
  console.log(workbookData.Sheet1.data[0]);
  ```
</CodeGroup>

### Error Handling

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { xmlParser } from '@flatfile/plugin-xml-extractor';

  try {
    const emptyXml = Buffer.from('<?xml version="1.0"?>');
    xmlParser(emptyXml);
  } catch (e) {
    console.error(e.message); // "No root xml object found"
  }
  ```

  ```typescript TypeScript theme={null}
  import { xmlParser } from '@flatfile/plugin-xml-extractor';

  try {
    const emptyXml: Buffer = Buffer.from('<?xml version="1.0"?>');
    xmlParser(emptyXml);
  } catch (e: any) {
    console.error(e.message); // "No root xml object found"
  }
  ```
</CodeGroup>

## Troubleshooting

### Fields Not Appearing as Expected

Check the `separator` and `attributePrefix` configuration. The default flattening behavior might not match your desired output format.

### Handling Repeated Tags

If tags within a record are repeated (e.g., multiple `<email>` tags), the extractor creates indexed headers. The first email tag becomes the `email` field, the second becomes `email/0`, the third `email/1`, and so on.

### Debugging Row Data

Use the `transform` function to inspect intermediate parsed output:

<CodeGroup>
  ```javascript JavaScript theme={null}
  XMLExtractor({
    transform: (row) => {
      console.log(row);
      return row;
    }
  })
  ```

  ```typescript TypeScript theme={null}
  XMLExtractor({
    transform: (row: Record<string, any>) => {
      console.log(row);
      return row;
    }
  })
  ```
</CodeGroup>

## Notes

* The plugin is designed for server-side environments and should be used in Flatfile listeners deployed on the Platform
* XML files must have a single root element containing an array of similar child elements (records)
* Not suitable for arbitrary or document-style XML with highly irregular structures
* Headers are automatically inferred from all unique keys found across all records
* The primary error condition is invalid XML structure - if no root element containing records is found, the parser throws "No root xml object found"
