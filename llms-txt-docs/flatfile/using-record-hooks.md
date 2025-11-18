# Source: https://flatfile.com/docs/guides/using-record-hooks.md

# Using Record Hooks

> Process data with Record Hooks

**Hooks** are concise functions that automatically **re-format**, **correct**, **validate**, and **enrich** data during the data import process. These hooks can be executed on a complete record, or row, of data using methods on the `FlatfileRecord` class.

Record-level hooks have access to all fields in a row and should be utilized for operations that require access to multiple fields or when creating a new field.

## Getting started

The `FlatfileRecord` class provides methods to manipulate and interact with a record in the Flatfile format, including setting values, retrieving values, adding information messages, performing computations, validating fields, and converting the record to JSON format.

Use the [Record Hook plugin](/plugins/record-hook) to listen for updates to data records and respond with three types of record hooks: `compute`, `computeIfPresent`, and `validate`. These hooks are available as methods on the `FlatfileRecord` class.

For complete installation instructions, configuration options, and detailed examples, see the [Record Hook plugin documentation](/plugins/record-hook).

## Record Hook Types

Record hooks provide three main operations for data processing:

### `compute`

Transforms field values based on the original value or other fields in the record. Always runs, even when no initial value is set. Use this for generating new values or creating computed fields.

### `computeIfPresent`

Similar to `compute`, but only runs when the field has an initial value. Ideal for transformations that might fail on empty values, such as string operations or mathematical calculations.

### `validate`

Validates field values against custom conditions and marks fields as invalid with error messages when they fail validation. Use this for complex validation rules beyond built-in field constraints.

For detailed syntax, parameters, and implementation examples of these record hooks, see the [Record Hook plugin documentation](/plugins/record-hook).

## Record Messages

The `FlatfileRecord` class provides methods to attach contextual messages to fields:

* **`addInfo()`**: Adds informational messages in a tooltip to help users understand transformations or provide context
* **`addWarning()`**: Adds warning messages to alert users of potential issues
* **`addError()`**: Marks fields as invalid with error messages, blocks [Actions](/core-concepts/actions) with the `hasAllValid` constraint

These methods accept either a single field name or an array of field names, along with a message string. For detailed syntax and examples, see the [Record Hook plugin documentation](/plugins/record-hook).

## Accessing External APIs

Record hooks can integrate with external APIs to enrich, validate, or transform data in real-time. This is useful for:

* **Data Enrichment**: Fetching additional information from external services
* **Real-time Validation**: Verifying data against external systems
* **Data Transformation**: Using external services to process or format data
* **Webhook Integration**: Sending processed data to external systems

### Common Use Cases

* **GET Requests**: Retrieve data from external APIs to enrich records
* **POST Requests**: Send record data to webhooks or external systems for processing
* **Authentication**: Validate credentials or tokens against external services
* **Geocoding**: Convert addresses to coordinates using mapping services

For complete examples of API integration patterns, including error handling and async processing, see the [Record Hook plugin documentation](/plugins/record-hook).

## getLinks

The `getLinks` method is a feature of the FlatfileRecord class. When a field in your record is of the Reference Field type and links to another record, getLinks can fetch those linked fields for you.

### Usage

When processing a record, you may find references to a related record. To retrieve the fields from the related record, use the `getLinks` method. Provide the field key of the Reference Field type, the part of the record that holds the reference to the other records, like this:

```javascript
const relatedRecords = record.getLinks("referenceFieldKey");
```

The getLinks method will then return an array containing all fields from the linked record associated with the provided 'referenceFieldKey'. If there is not a linked record associated with this field, an empty array will be returned.

### Benefits

Using `getLinks` provides access to all related information. It's particularly useful when you want to perform operations similar to VLOOKUPs in spreadsheets, or when you need to compare data across referenced fields.

For instance, you could use `getLinks` to fetch all the fields related to a particular record and enrich your data, or compare the related records for validation.

With `getLinks`, processing related datasets becomes much more manageable in Flatfile. This method provides you with an effective way to navigate, enrich, and validate your data.

## Deleting records

There are primarily two use cases for deleting records:

1. Deleting a subset of records
2. Deleting all records in a sheet

### Deleting a subset of records

To delete a subset of records first import the `@flatfile/api` package, then use the `api.records.delete()` helper method. This method takes in an array of record IDs and deletes them from the sheet.

```javascript
await api.records.delete(sheetId, { ids: [...] });
```

### Deleting all records in a sheet

For clearing an entire sheet of its records, set up a bulk delete job. This task will comprehensively wipe out every record on the specified sheet. Check out our [jobs documentation](/core-concepts/jobs).

```javascript
await api.jobs.create({
  type: "workbook",
  operation: "delete-records",
  trigger: "immediate",
  source: workbookId,
  config: {
    sheet: sheetId,
    filter: "all",
  },
});
```

* [Clone the Handling Data example in Typescript](https://github.com/FlatFilers/flatfile-docs-kitchen-sink/blob/main/typescript/handling-data/index.ts)
* [Clone the Handling Data example in Javascript](https://github.com/FlatFilers/flatfile-docs-kitchen-sink/blob/main/javascript/handling-data/index.js)
