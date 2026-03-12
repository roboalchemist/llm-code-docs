# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/root/server-version.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Server Version



## OpenAPI

````yaml get /version
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /version:
    get:
      tags:
        - Root
      summary: Server Version
      operationId: server_version_version_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: string
                title: Response Server Version Version Get

````

Built with [Mintlify](https://mintlify.com).