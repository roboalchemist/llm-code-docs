# Source: https://northflank.com/docs/v1/api/project/services/pause-service.md

# Pause service

Pause the given service.

Required permission: Project > Services > General > Update

**Path parameters:**

{object}
- `projectId`: (string) (required) ID of the project
- `serviceId`: (string) (required) ID of the service

**Response body:**

{object}
- `data`: {object}

## API reference

POST /v1/projects/{projectId}/services/{serviceId}/pause

POST /v1/teams/{teamId}/projects/{projectId}/services/{serviceId}/pause

### Example Response

200 OK: The operation was performed successfully.

```json
{
  "data": {}
}
```

## CLI reference

$ northflank pause service

Options:

- `--projectId <projectId>`: ID of the project

- `--serviceId <serviceId>`: ID of the service

- `--verbose `: Verbose output

- `--quiet `: No console output

- `-o --output <format>`: Output formatting 

### Example Response

 The operation was performed successfully.

```json
{}
```

## JavaScript client reference

### Example request



```javascript
await apiClient.pause.service({
  parameters: {
    "projectId": "default-project",
    "serviceId": "example-service"
  }    
});
```

### Example Response

 The operation was performed successfully.

```json
{
  "data": {},
  "rawResponse": "...",
  "request": "...",
  "error": "..."
}
```

Previous: [Get service metrics](/docs/v1/api//project/services/get-service-metrics)

Next: [Get service ports](/docs/v1/api//project/services/get-service-ports)