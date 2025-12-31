# Source: https://docs.lancedb.com/api-reference/tables/create-table.md

# Create Table

> Create a new table in the database with schema inferred from the provided Arrow data. The table name must be unique within the database and vector columns are automatically detected and optimized for search operations.

**Example curl command:**
```bash
curl --request POST \
  --url https://{db}.{region}.api.lancedb.com/v1/table/{name}/create \
  --header 'Content-Type: application/vnd.apache.arrow.stream' \
  --header 'x-api-key: <api-key>' \
  --data-binary @data.arrow
```




---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lancedb.com/llms.txt