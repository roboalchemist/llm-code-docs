# Source: https://flatfile.com/docs/plugins/index.md

# Source: https://flatfile.com/docs/index.md

# Source: https://flatfile.com/docs/plugins/index.md

# Source: https://flatfile.com/docs/index.md

# Source: https://flatfile.com/docs/plugins/index.md

# Source: https://flatfile.com/docs/index.md

# Source: https://flatfile.com/docs/plugins/index.md

# Source: https://flatfile.com/docs/index.md

# Source: https://flatfile.com/docs/plugins/index.md

# Source: https://flatfile.com/docs/index.md

# Source: https://flatfile.com/docs/plugins/index.md

# Overview

> Extend your Flatfile data engine with powerful plugins for extraction, transformation, validation, and integration

Flatfile plugins extend your data processing capabilities with pre-built, reusable modules for common data operations. They handle everything from file extraction and data transformation to validation and external integrations, allowing you to build sophisticated data workflows quickly.

## Open Source

All Flatfile plugins are **open source** and available on GitHub at [github.com/FlatFilers/flatfile-plugins](https://github.com/FlatFilers/flatfile-plugins).

## Plugin Categories

### 🔄 Transform

Plugins for data transformation, validation, and cleaning.

<CardGroup cols={2}>
  <Card title="Record Hook" href="/plugins/record-hook">
    Run custom logic on individual data records in real-time
  </Card>

  <Card title="Autocast" href="/plugins/autocast">
    Automatically cast values to appropriate data types
  </Card>

  <Card title="Constraints" href="/plugins/constraints">
    Extend schemas with external validation constraints
  </Card>

  <Card title="Dedupe" href="/plugins/dedupe">
    Remove duplicate records via sheet-level actions
  </Card>
</CardGroup>

### 📤 Extractors

Plugins for parsing and extracting data from various file formats.

<CardGroup cols={2}>
  <Card title="Delimiter Extractor" href="/plugins/delimiter-extractor">
    Parse delimited files (CSV, TSV, etc.)
  </Card>

  <Card title="XLSX Extractor" href="/plugins/xlsx-extractor">
    Extract data from Excel spreadsheets
  </Card>

  <Card title="JSON Extractor" href="/plugins/json-extractor">
    Parse JSON files and convert to tabular data
  </Card>

  <Card title="PDF Extractor" href="/plugins/pdf-extractor">
    Extract structured data from PDF documents
  </Card>
</CardGroup>

### 📋 Schemas

Plugins for converting external schemas to Flatfile format.

<CardGroup cols={2}>
  <Card title="JSON Schema Converter" href="/plugins/json-schema">
    Convert JSON Schema to Flatfile Blueprint
  </Card>

  <Card title="OpenAPI Schema Converter" href="/plugins/openapi-schema">
    Convert OpenAPI schema to Flatfile Blueprint
  </Card>

  <Card title="SQL DDL Converter" href="/plugins/sql-ddl-converter">
    Convert SQL DDL to Flatfile Blueprint
  </Card>

  <Card title="YAML Schema Converter" href="/plugins/yaml-schema">
    Convert YAML Schema to Flatfile Blueprint
  </Card>
</CardGroup>

### 📤 Export

Plugins for exporting processed data to external systems.

<CardGroup cols={2}>
  <Card title="Export Workbook" href="/plugins/export-workbook">
    Export data from Flatfile to various formats
  </Card>

  <Card title="Webhook Egress" href="/plugins/webhook-egress">
    Send data to external webhooks
  </Card>

  <Card title="Export Delimited ZIP" href="/plugins/delimited-zip">
    Export workbooks as delimited files in ZIP archives
  </Card>

  <Card title="Export Pivot Table" href="/plugins/pivot-table">
    Generate pivot tables from sheet data
  </Card>
</CardGroup>

### 🔧 Core

Essential plugins for Flatfile operations and configuration.

<CardGroup cols={2}>
  <Card title="Space Configure" href="/plugins/space-configure">
    Configure Flatfile spaces with workbooks and settings
  </Card>

  <Card title="Job Handler" href="/plugins/job-handler">
    Handle Flatfile jobs with custom logic
  </Card>

  <Card title="View Mapped" href="/plugins/view-mapped">
    Show only mapped columns in post-mapping view
  </Card>

  <Card title="Rollout" href="/plugins/rollout">
    Automatically roll out workbook changes
  </Card>
</CardGroup>

### ✅ Validation

Specialized validation plugins for data quality.

<CardGroup cols={2}>
  <Card title="Validate Email" href="/plugins/email">
    Comprehensive email address validation
  </Card>

  <Card title="Validate Phone" href="/plugins/phone">
    Phone number formatting and validation
  </Card>

  <Card title="Validate Date" href="/plugins/date">
    Date format normalization and validation
  </Card>

  <Card title="Validate Number" href="/plugins/number">
    Number validation and formatting
  </Card>
</CardGroup>

### 🔗 Enrich

Plugins for data enrichment using external APIs.

<CardGroup cols={2}>
  <Card title="Geocode" href="/plugins/geocode">
    Geocode addresses using Google Maps API
  </Card>

  <Card title="Sentiment Analysis" href="/plugins/sentiment">
    Analyze sentiment of text fields
  </Card>

  <Card title="Text Summarization" href="/plugins/summarize">
    Summarize and extract key phrases from text
  </Card>

  <Card title="What3Words" href="/plugins/what3words">
    Convert What3Words addresses to standard addresses
  </Card>
</CardGroup>

## Getting Started with Plugins

### Installation

Install plugins using npm in your Flatfile project:

```bash
npm install @flatfile/plugin-record-hook @flatfile/plugin-autocast
```

### Basic Usage

Add plugins to your listener:

```typescript
import { FlatfileListener } from '@flatfile/listener'
import { recordHook } from '@flatfile/plugin-record-hook'
import { autocast } from '@flatfile/plugin-autocast'

const listener = FlatfileListener.create(async (client) => {
  // Add autocast for automatic type conversion
  client.use(autocast())
  
  // Add record hook for custom validation
  client.use(
    recordHook('customers', (record) => {
      // Custom record processing logic
      const email = record.get('email')
      if (email && !isValidEmail(email)) {
        record.addError('email', 'Invalid email format')
      }
      return record
    })
  )
})
```

### Plugin Configuration

Most plugins accept configuration options:

```typescript
import { configureSpace } from '@flatfile/plugin-space-configure'
import { dedupePlugin } from '@flatfile/plugin-dedupe'

client.use(
  configureSpace({
    workbooks: [workbookConfig],
    space: {
      name: "Customer Import",
      namespace: "customers"
    }
  })
)

client.use(
  dedupePlugin({
    sheetSlug: 'customers',
    dedupe: {
      key: 'email',
      keep: 'first',
      custom: {
        operation: 'dedupe-customers',
        label: 'Remove Duplicate Customers'
      }
    }
  })
)
```

## Plugin Development

### Creating Custom Plugins

You can create custom plugins for reusable functionality:

```typescript
import { FlatfilePlugin } from '@flatfile/listener'

export function myCustomPlugin(options: any): FlatfilePlugin {
  return (client) => {
    // Plugin initialization logic
    client.filter({ job: 'sheet:myCustomOperation' }, (configure) => {
      configure.on('job:ready', async (event) => {
        // Plugin functionality
        const { jobId } = event.context
        
        try {
          await client.jobs.ack(jobId, {
            info: 'Running custom operation...'
          })
          
          // Your custom logic here
          await performCustomOperation(options)
          
          await client.jobs.complete(jobId, {
            outcome: { message: 'Custom operation completed successfully' }
          })
        } catch (error) {
          await client.jobs.fail(jobId, {
            outcome: { message: `Operation failed: ${error.message}` }
          })
        }
      })
    })
  }
}

// Usage
client.use(myCustomPlugin({ customOption: 'value' }))
```

### Plugin Best Practices

1. **Single Responsibility**: Each plugin should handle one specific functionality
2. **Configuration**: Accept configuration options for flexibility
3. **Error Handling**: Implement robust error handling and logging
4. **Documentation**: Provide clear documentation and examples
5. **Testing**: Include comprehensive tests for your plugin

## Popular Plugin Combinations

### Basic Data Import

```typescript
// Essential plugins for most data import scenarios
client.use(autocast())
client.use(recordHook('sheet-name', validateRecord))
client.use(dedupePlugin({ sheetSlug: 'sheet-name' }))
```

### Advanced Validation

```typescript
// Comprehensive data validation
client.use(autocast())
client.use(recordHook('customers', validateCustomer))
client.use(validateEmail({ sheetSlug: 'customers', fieldKey: 'email' }))
client.use(validatePhone({ sheetSlug: 'customers', fieldKey: 'phone' }))
client.use(validateDate({ sheetSlug: 'customers', fieldKey: 'birthdate' }))
```

### Schema Conversion

```typescript
// Convert external schemas to Flatfile
client.use(convertJsonSchema({ source: 'api-schema.json' }))
client.use(convertOpenApiSchema({ source: 'swagger.yaml' }))
```

### Data Enrichment

```typescript
// Enrich data with external services
client.use(enrichGeocode({ 
  sheetSlug: 'addresses',
  addressField: 'full_address'
}))
client.use(enrichSentiment({
  sheetSlug: 'feedback', 
  textField: 'comments'
}))
```

## Plugin Repository

All Flatfile plugins are open source and available on GitHub:

* **Main Repository**: [github.com/FlatFilers/flatfile-plugins](https://github.com/FlatFilers/flatfile-plugins)
* **NPM Organization**: [@flatfile](https://www.npmjs.com/org/flatfile)
* **Plugin Marketplace**: [flatfile.com/plugins](https://flatfile.com/plugins/)

## Contributing

We welcome contributions to the Flatfile plugin ecosystem:

1. **Bug Reports**: Report issues on the GitHub repository
2. **Feature Requests**: Suggest new plugins or enhancements
3. **Pull Requests**: Contribute code improvements or new plugins
4. **Documentation**: Help improve plugin documentation

## Support

* **Documentation**: Each plugin includes detailed documentation
* **Community**: Join our [Slack community](https://flatfile.com/join-slack/) for support
* **GitHub Issues**: Report bugs or request features on GitHub
* **Professional Support**: Contact our team for enterprise support
