# Source: https://docs.promptlayer.com/reference/delete-reports-by-name.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Reports by Name

This endpoint archives all reports with the specified name within the workspace associated with the provided API key.


## OpenAPI

````yaml DELETE /reports/name/{report_name}
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /reports/name/{report_name}:
    delete:
      tags:
        - reports
      summary: Delete Reports by Name
      operationId: deleteReportsByName
      parameters:
        - name: report_name
          in: path
          required: true
          schema:
            type: string
          description: Name of the report to archive.
        - name: X-API-KEY
          in: header
          required: true
          schema:
            type: string
          description: API key to authorize the operation.
      responses:
        '200':
          description: Successful Operation
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  message:
                    type: string
                required:
                  - success
                  - message
        '401':
          description: Unauthorized
        '404':
          description: Report not found

````