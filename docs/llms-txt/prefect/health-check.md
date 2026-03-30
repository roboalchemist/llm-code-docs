# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/root/health-check.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Health Check



## OpenAPI

````yaml get /health
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /health:
    get:
      tags:
        - Root
      summary: Health Check
      operationId: health_check_health_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: boolean
                title: Response Health Check Health Get

````

Built with [Mintlify](https://mintlify.com).