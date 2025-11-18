# Source: https://flatfile.com/docs/guides/custom-extractors.md

# Custom Extractors

> Build custom file processing plugins to handle unique data formats and transform files into structured data

## What Are Custom Extractors?

Custom extractors are specialized plugins that enable you to handle file formats that aren't natively supported by Flatfile's existing [plugins](/plugins). They process uploaded files, extract structured data, and provide that data for mapping into [Sheets](/core-concepts/sheets) as [Records](/core-concepts/records). This guide covers everything you need to know to build custom extractors.

Common use cases include:

* Legacy system data exports (custom delimited files, fixed-width formats)
* Industry-specific formats (healthcare, finance, manufacturing)
* Multi-format processors (handling various formats in one extractor)
* Binary file handlers (images with metadata, proprietary formats)

## Architecture Overview

### Core Components

Custom extractors are built using the `@flatfile/util-extractor` utility, which provides a standardized framework for file processing:

```javascript
import { Extractor } from "@flatfile/util-extractor";

export const MyCustomExtractor = (options = {}) => {
  return Extractor(".myformat", "custom", myCustomParser, options);
};
```

Once you've created your extractor, you must register it in a [listener](/core-concepts/listeners) to be used. This will ensure that the extractor responds to the `file:created` [event](/reference/events#file%3Acreated) and processes your files.

```javascript
// . . . other imports
import { MyCustomExtractor } from "./my-custom-extractor";

export default function (listener) {
  // . . . other listener setup
  listener.use(MyCustomExtractor());
}
```

### Handling Multiple File Extensions

To support multiple file extensions, use a RegExp pattern:

```javascript
// Support both .pipe and .custom extensions
export const MultiExtensionExtractor = (options = {}) => {
  return Extractor(/\.(pipe|custom)$/i, "pipe", parseCustomFormat, options);
};

// Support JSON variants
export const JSONExtractor = (options = {}) => {
  return Extractor(/\.(json|jsonl|jsonlines)$/i, "json", parseJSONFormat, options);
};
```

### Key Architecture Elements

| Component           | Purpose                                                        | Required |
| ------------------- | -------------------------------------------------------------- | -------- |
| **File Extension**  | String or RegExp of supported file extension(s)                | ✓        |
| **Extractor Type**  | String identifier for the extractor type                       | ✓        |
| **Parser Function** | Core logic that converts file buffer to structured data        | ✓        |
| **Options**         | Configuration for chunking, parallelization, and customization | -        |

### Data Flow

1. **File Upload** → Flatfile receives file with matching extension
2. **Event Trigger** → `file:created` [event](/reference/events#file%3Acreated) fires
3. **Parser Execution** → Your parser function processes the file buffer
4. **Data Structuring** → Raw data is converted to WorkbookCapture format and provided to Flatfile for mapping into [Sheets](/core-concepts/sheets) as [Records](/core-concepts/records)
5. **Job Completion** → Processing status is reported to user

## Getting Started

Remember that custom extractors are powerful tools for handling unique data formats. Start with simple implementations and gradually add complexity as needed.

### Prerequisites

Install the required packages. You may also want to review our [Coding Tutorial](/coding-tutorial/overview) if you haven't created a [Listener](/core-concepts/listeners) yet.

```bash
npm install @flatfile/util-extractor @flatfile/listener @flatfile/api
```

### Basic Implementation

Let's create a simple custom extractor for a pipe-delimited format. This will be used to process files with the `.pipe` or `.psv` extension that look like this:

```psv
name|email|phone
John Doe|john@example.com|123-456-7890
Jane Smith|jane@example.com|098-765-4321
```

```javascript
import { Extractor } from "@flatfile/util-extractor";

// Parser function - converts Buffer to WorkbookCapture
function parseCustomFormat(buffer) {
  const content = buffer.toString('utf-8');
  const lines = content.split('\n').filter(line => line.trim());
  
  if (lines.length === 0) {
    throw new Error('Empty file');
  }
  
  // First line contains headers
  const headers = lines[0].split('|').map(h => h.trim());
  
  // Remaining lines contain data
  const data = lines.slice(1).map(line => {
    const values = line.split('|').map(v => v.trim());
    const record = {};
    
    headers.forEach((header, index) => {
      record[header] = {
        value: values[index] || ''
      };
    });
    
    return record;
  });
  
  return {
    Sheet1: {
      headers,
      data
    }
  };
}

// Create the extractor
export const CustomPipeExtractor = (options = {}) => {
  return Extractor(/\.(pipe|psv)$/i, "pipe", parseCustomFormat, options);
};
```

And now let's import and register it in your [Listener](/core-concepts/listeners).

```javascript
// . . . other imports
import { CustomPipeExtractor } from "./custom-pipe-extractor";

export default function (listener) {
  // . . . other listener setup
  listener.use(CustomPipeExtractor());
}
```

That's it! Your extractor is now registered and will be used to process pipe-delimited files with the `.pipe` or `.psv` extension.

## Advanced Examples

### Multi-Sheet Parser

Let's construct an Extractor to handle files that contain multiple data sections. This will be used to process files with the `.multi` or `.sections` extension that look like this:

```text
---SECTION---
SHEET:Sheet1
name,email,phone
John Doe,john@example.com,123-456-7890
Jane Smith,jane@example.com,098-765-4321
---SECTION---
SHEET:Sheet2
name,email,phone
Jane Doe,jane@example.com,123-456-7891
John Smith,john@example.com,098-765-4322
---SECTION---
```

```javascript
function parseMultiSheetFormat(buffer) {
  const content = buffer.toString('utf-8');
  const sections = content.split('---SECTION---');
  
  const workbook = {};
  
  sections.forEach((section, index) => {
    if (!section.trim()) return;
    
    const lines = section.trim().split('\n');
    const sheetName = lines[0].replace('SHEET:', '').trim() || `Sheet${index + 1}`;
    
    const headers = lines[1].split(',').map(h => h.trim());
    const data = lines.slice(2).map(line => {
      const values = line.split(',').map(v => v.trim());
      const record = {};
      
      headers.forEach((header, idx) => {
        record[header] = {
          value: values[idx] || ''
        };
      });
      
      return record;
    });
    
    workbook[sheetName] = { headers, data };
  });
  
  return workbook;
}

export const MultiSheetExtractor = (options = {}) => {
  return Extractor(/\.(multi|sections)$/i, "multi-sheet", parseMultiSheetFormat, options);
};
```

Now let's register it in your [Listener](/core-concepts/listeners).

```javascript
// . . . other imports
import { MultiSheetExtractor } from "./multi-sheet-extractor";

export default function (listener) {
  // . . . other listener setup
  listener.use(MultiSheetExtractor());
}
```

### Binary Format Handler

This example will be used to process binary files with structured data. This will be used to process binary files with the `.bin` or `.dat` extension. Due to the nature of binary format, we can't easily present a sample import here.

{/* TODO: Add a sample import here. I can't figure out how to get Mintlify to respect asset download links. */}

```javascript
function parseBinaryFormat(buffer) {
  // Example: Custom binary format with header + records
  let offset = 0;
  
  // Read header (first 16 bytes)
  const magic = buffer.readUInt32LE(offset); offset += 4;
  const version = buffer.readUInt16LE(offset); offset += 2;
  const recordCount = buffer.readUInt32LE(offset); offset += 4;
  const fieldCount = buffer.readUInt16LE(offset); offset += 2;
  
  if (magic !== 0xDEADBEEF) {
    throw new Error('Invalid file format');
  }
  
  // Read field definitions
  const headers = [];
  for (let i = 0; i < fieldCount; i++) {
    const nameLength = buffer.readUInt16LE(offset); offset += 2;
    const name = buffer.toString('utf-8', offset, offset + nameLength);
    offset += nameLength;
    const type = buffer.readUInt8(offset); offset += 1;
    
    headers.push(name);
  }
  
  // Read records
  const data = [];
  for (let i = 0; i < recordCount; i++) {
    const record = {};
    
    headers.forEach(header => {
      const valueLength = buffer.readUInt16LE(offset); offset += 2;
      const value = buffer.toString('utf-8', offset, offset + valueLength);
      offset += valueLength;
      
      record[header] = { value };
    });
    
    data.push(record);
  }
  
  return {
    Sheet1: { headers, data }
  };
}

export const BinaryExtractor = (options = {}) => {
  return Extractor(/\.(bin|dat)$/i, "binary", parseBinaryFormat, options);
};
```

And, once again, let's register it in your [Listener](/core-concepts/listeners).

```javascript
// . . . other imports
import { BinaryExtractor } from "./binary-extractor";

export default function (listener) {
  // . . . other listener setup
  listener.use(BinaryExtractor());
}
```

### Configuration-Driven Extractor

Create a flexible extractor that can be configured for different formats. This will be used to process files in a manner that handles different delimiters, line endings, and other formatting options.

```javascript
function createConfigurableParser(config) {
  return function parseConfigurableFormat(buffer) {
    const content = buffer.toString(config.encoding || 'utf-8');
    let lines = content.split(config.lineDelimiter || '\n');
    
    // Skip header lines if specified
    if (config.skipLines) {
      lines = lines.slice(config.skipLines);
    }
    
    // Filter empty lines
    if (config.skipEmptyLines) {
      lines = lines.filter(line => line.trim());
    }
    
    if (lines.length === 0) {
      throw new Error('No data found');
    }
    
    // Extract headers
    let headers;
    let dataStartIndex = 0;
    
    if (config.explicitHeaders) {
      headers = config.explicitHeaders;
    } else {
      headers = lines[0].split(config.fieldDelimiter || ',').map(h => h.trim());
      dataStartIndex = 1;
    }
    
    // Process data
    const data = lines.slice(dataStartIndex).map(line => {
      const values = line.split(config.fieldDelimiter || ',');
      const record = {};
      
      headers.forEach((header, index) => {
        let value = values[index] || '';
        
        // Apply transformations
        if (config.transforms && config.transforms[header]) {
          value = config.transforms[header](value);
        }
        
        // Type conversion
        if (config.typeConversion) {
          if (!isNaN(value) && value !== '') {
            value = Number(value);
          } else if (value.toLowerCase() === 'true' || value.toLowerCase() === 'false') {
            value = value.toLowerCase() === 'true';
          }
        }
        
        record[header] = { value };
      });
      
      return record;
    });
    
    return {
      [config.sheetName || 'Sheet1']: { headers, data }
    };
  };
}

export const ConfigurableExtractor = (userConfig = {}) => {
  const defaultConfig = {
    encoding: 'utf-8',
    lineDelimiter: '\n',
    fieldDelimiter: ',',
    skipLines: 0,
    skipEmptyLines: true,
    typeConversion: false,
    sheetName: 'Sheet1'
  };
  
  const config = { ...defaultConfig, ...userConfig };
  
  return Extractor(
    config.fileExtension || ".txt", 
    "configurable", 
    createConfigurableParser(config),
    {
      chunkSize: config.chunkSize || 10000,
      parallel: config.parallel || 1
    }
  );
};
```

Now let's register two different configurable extractors in our [Listener](/core-concepts/listeners).

The first will be used to process files with the `.custom` extension that look like this, while transforming dates and amount values:

```text
Extraneous text
More extraneous text
name & date & amount
John Doe & 1/1/2021 & 100.00
Jane Smith & 1/2/2021 & 200.00
```

The second will be used to process files with the `.pipe` or `.special` extension that look like this:

```text
Extraneous text
More extraneous text
name|date|amount
John Doe|2021-01-01|100.00
Jane Smith|2021-01-02|200.00
```

```javascript
// . . . other imports
import { ConfigurableExtractor } from "./configurable-extractor";

export default function (listener) {
  // . . . other listener setup

  // Custom extractor with configuration for .custom files
  listener.use(ConfigurableExtractor({
    fileExtension: ".custom",
    fieldDelimiter: " & ",
    skipLines: 2,
    typeConversion: true,
    transforms: {
      'date': (value) => new Date(value).toISOString(),
      'amount': (value) => parseFloat(value).toFixed(2)
    }
  }));

  // Custom extractor with configuration for .pipe and .special files
  listener.use(ConfigurableExtractor({
    fileExtension: /\.(pipe|special)$/i,
    fieldDelimiter: "|",
    skipLines: 2,
    typeConversion: true
  }));
}
```

## Reference

### API

```typescript
function Extractor(
  fileExt: string | RegExp,
  extractorType: string,
  parseBuffer: (
    buffer: Buffer,
    options: any
  ) => WorkbookCapture | Promise<WorkbookCapture>,
  options?: Record<string, any>
): (listener: FlatfileListener) => void
```

| Parameter       | Type                  | Description                                                                |
| --------------- | --------------------- | -------------------------------------------------------------------------- |
| `fileExt`       | `string` or `RegExp`  | File extension to process (e.g., `".custom"` or `/\.(custom\|special)$/i`) |
| `extractorType` | `string`              | Identifier for the extractor type (e.g., "custom", "binary")               |
| `parseBuffer`   | `ParserFunction`      | Function that converts Buffer to WorkbookCapture                           |
| `options`       | `Record<string, any>` | Optional configuration object                                              |

#### Options

| Option      | Type      | Default | Description                            |
| ----------- | --------- | ------- | -------------------------------------- |
| `chunkSize` | `number`  | `5000`  | Records to process per batch           |
| `parallel`  | `number`  | `1`     | Number of concurrent processing chunks |
| `debug`     | `boolean` | `false` | Enable debug logging                   |

#### Parser Function Options

Your `parseBuffer` function receives additional options beyond what you pass to `Extractor`:

| Option                   | Type      | Description                                       |
| ------------------------ | --------- | ------------------------------------------------- |
| `fileId`                 | `string`  | The ID of the file being processed                |
| `fileExt`                | `string`  | The file extension (e.g., ".csv")                 |
| `headerSelectionEnabled` | `boolean` | Whether header selection is enabled for the space |

### Data Structures

#### WorkbookCapture Structure

The parser function must return a `WorkbookCapture` object:

```javascript
const workbookCapture = {
  "SheetName1": {
    headers: ["field1", "field2", "field3"],
    data: [
      {
        field1: { value: "value1" },
        field2: { value: "value2" },
        field3: { value: "value3" }
      },
      // ... more records
    ]
  },
  "SheetName2": {
    headers: ["col1", "col2"],
    data: [
      {
        col1: { value: "data1" },
        col2: { value: "data2" }
      }
    ]
  }
};
```

#### Cell Value Objects

Each cell value should use the `Flatfile.RecordData` format:

```javascript
const recordData = {
  field1: { value: "john@example.com" },
  field2: { value: "John Doe" },
  field3: { 
    value: "invalid-email",
    messages: [
      {
        type: "error",
        message: "Invalid email format"
      }
    ]
  }
};
```

#### Message Types

| Type      | Description           | UI Effect                                                                                    |
| --------- | --------------------- | -------------------------------------------------------------------------------------------- |
| `error`   | Validation error      | Red highlighting, blocks [Actions](/core-concepts/actions) with the `hasAllValid` constraint |
| `warning` | Warning message       | Yellow highlighting, allows submission                                                       |
| `info`    | Informational message | Mouseover tooltip, allows submission                                                         |

### TypeScript Interfaces

```typescript
type ParserFunction = (
  buffer: Buffer,
  options: any
) => WorkbookCapture | Promise<WorkbookCapture>;

type WorkbookCapture = Record<string, SheetCapture>;

type SheetCapture = {
  headers: string[];
  descriptions?: Record<string, string | null> | null;
  data: Flatfile.RecordData[];
  metadata?: { rowHeaders: number[] };
};
```

## Troubleshooting Common Issues

### Files Not Processing

**Symptoms**: Files upload but no extraction occurs

**Solutions**:

* Verify file extension matches `fileExt` configuration
* Check [Listener](/core-concepts/listeners) is properly deployed and running
* Enable debug logging to see processing details

```javascript
const extractor = CustomExtractor({
  debug: true
}); // Make sure file extensions match in the Extractor call
```

### Parser Errors

**Symptoms**: Jobs fail with parsing errors

**Solutions**:

* Add try-catch blocks in parser function
* Validate input data before processing
* Return helpful error messages

```javascript
function parseCustomFormat(buffer) {
  try {
    const content = buffer.toString('utf-8');
    
    if (!content || content.trim() === '') {
      throw new Error('File is empty');
    }
    
    // ... parsing logic
    
  } catch (error) {
    throw new Error(`Parse error: ${error.message}`);
  }
}
```

### Memory Issues

**Symptoms**: Large files cause timeouts or memory errors

**Solutions**:

* Reduce chunk size for large files
* Implement streaming for very large files
* Use parallel processing carefully

```javascript
const extractor = CustomExtractor({
  chunkSize: 1000,  // Smaller chunks
  parallel: 1       // Reduce parallelization
});
```

### Performance Problems

**Symptoms**: Slow processing, timeouts

**Solutions**:

* Optimize parser algorithm
* Use appropriate chunk sizes
* Consider parallel processing for I/O-bound operations

```javascript
// Optimize for large files
const extractor = CustomExtractor({
  chunkSize: 5000,
  parallel: 3
});
```
