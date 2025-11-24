# Source: https://flatfile.com/docs/core-concepts/records.md

# Records

> Individual data rows that represent your imported data in Flatfile

Records in Flatfile represent individual rows of data within your import workflows. They are instances of data that conform to the [field](/core-concepts/fields) definitions in your [blueprints](/core-concepts/blueprints), containing the actual values that users import, validate, and transform.

## What are Records?

A Record is a data instance that:

* **Contains Data Values** - Stores the actual imported data for each [field](/core-concepts/fields)
* **Maintains State** - Tracks validation status, errors, and processing history
* **Supports Transformation** - Allows data modification and enrichment

Records are the fundamental data units that flow through your import pipelines, from initial upload through final export.

## Record Structure

### Basic Record Anatomy

This is an example JSON response from the Flatfile API. For working with Records in your language, see our [API Reference](/api-reference) documentation

```json
{
  "data": {
    "records": [
      {
        "id": "us_rc_YOUR_ID",
        "values": {
          "firstName": {
            "messages": [],
            "updatedAt": "2023-11-20T16:59:40.286Z",
            "valid": true,
            "value": "John"
          },
          "lastName": {
            "messages": [],
            "updatedAt": "2023-11-20T16:59:40.286Z",
            "valid": true,
            "value": "Smith"
          },
          "email": {
            "messages": [],
            "updatedAt": "2023-11-20T16:59:40.286Z",
            "valid": true,
            "value": "john.smith@example.com"
          }
        },
        "valid": true,
        "metadata": {},
        "config": {}
      }
    ],
    "success": true,
    "commitId": "us_vr_YOUR_ID",
    "counts": {
      "total": 1000,
      "valid": 1000,
      "error": 0
    },
    "versionId": "us_vr_YOUR_ID"
  }
}
```
