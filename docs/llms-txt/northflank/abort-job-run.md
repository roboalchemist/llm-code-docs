# Source: https://northflank.com/docs/v1/api/project/jobs/abort-job-run.md

# Abort job run

Aborts the given job run

Required permission: Project > Jobs > Deployment > Deploy Build

**Path parameters:**

{object}
- `projectId`: (string) (required) ID of the project
- `jobId`: (string) (required) ID of the job
- `runId`: (string) (required) ID of the job run

**Response body:**

{object}
- `data`: {object}

## API reference

DELETE /v1/projects/{projectId}/jobs/{jobId}/runs/{runId}

DELETE /v1/teams/{teamId}/projects/{projectId}/jobs/{jobId}/runs/{runId}

### Example Response

200 OK: The operation was performed successfully.

```json
{
  "data": {}
}
```

## CLI reference

$ northflank abort job run

Options:

- `--projectId <projectId>`: ID of the project

- `--jobId <jobId>`: ID of the job

- `--runId <runId>`: ID of the job run

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
await apiClient.abort.job.run({
  parameters: {
    "projectId": "default-project",
    "jobId": "example-job",
    "runId": "d34582a4-35bd-4c71-8e7c-e36999b88723"
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

Previous: [Get run details](/docs/v1/api//project/jobs/get-run-details)

Next: [Create cron job](/docs/v1/api//project/jobs/create-cron-job)