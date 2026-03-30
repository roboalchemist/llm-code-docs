# Source: https://docs.knock.app/api-reference/bulk_operations/schemas/bulk_operation.md

### BulkOperation

A bulk operation entity.

#### Attributes

- **__typename** (string) *required* - The typename of the schema.
- **completed_at** (string) - Timestamp when the bulk operation was completed.
- **error_count** (integer) - The number of failed operations.
- **error_items** (array) - A list of items that failed to be processed.
- **estimated_total_rows** (integer) *required* - The estimated total number of rows to process.
- **failed_at** (string) - Timestamp when the bulk operation failed.
- **id** (string) *required* - Unique identifier for the bulk operation.
- **inserted_at** (string) *required* - Timestamp when the resource was created.
- **name** (string) *required* - The name of the bulk operation.
- **processed_rows** (integer) *required* - The number of rows processed so far.
- **progress_path** (string) - The URI to the bulk operation's progress.
- **started_at** (string) - Timestamp when the bulk operation was started.
- **status** (string) *required* - The status of the bulk operation.
- **success_count** (integer) *required* - The number of successful operations.
- **updated_at** (string) *required* - The timestamp when the resource was last updated.

#### Example

```json
{
  "__typename": "BulkOperation",
  "completed_at": null,
  "error_count": 0,
  "error_items": [],
  "estimated_total_rows": 1000,
  "failed_at": null,
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "inserted_at": "2024-05-22T12:00:00Z",
  "name": "Bulk operation name",
  "processed_rows": 0,
  "progress_path": "https://api.switchboard.com/v1/bulk_operations/123e4567-e89b-12d3-a456-426614174000",
  "started_at": null,
  "status": "processing",
  "success_count": 0,
  "updated_at": "2024-05-22T12:00:00Z"
}
```

