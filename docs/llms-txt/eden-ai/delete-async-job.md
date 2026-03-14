# Source: https://docs.edenai.co/api-reference/universal-ai/delete-async-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Async Job

> Delete an async job by ID.

This permanently removes the job and its results. This action cannot be undone.



## OpenAPI

````yaml openapi/v3-openapi.json delete /v3/universal-ai/async/{job_id}
openapi: 3.1.0
info:
  title: Eden AI API V3
  version: 3.0.0
servers:
  - url: https://api.edenai.run
    description: Production server
security: []
paths:
  /v3/universal-ai/async/{job_id}:
    delete:
      tags:
        - Universal-ai
      summary: Delete Async Job
      description: >-
        Delete an async job by ID.


        This permanently removes the job and its results. This action cannot be
        undone.
      operationId: delete_async_job_v3_universal_ai_async__job_id__delete
      parameters:
        - name: job_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Job ID
            description: The job ID to delete
      responses:
        '204':
          description: Job deleted successfully
        '404':
          description: Job not found
      security:
        - AuthBearer: []
components:
  securitySchemes:
    AuthBearer:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).