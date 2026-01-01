# Source: https://docs.lunary.ai/docs/api/audit-logs/retrieve-audit-logs.md

# Retrieve audit logs

> Retrieve a list of audit logs for the current organization. Note that this functionality is still under development and the audits logs are not fully exhaustive.



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/audit-logs
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/audit-logs:
    get:
      tags:
        - Audit Logs
      summary: Retrieve audit logs
      description: >-
        Retrieve a list of audit logs for the current organization. Note that
        this functionality is still under development and the audits logs are
        not fully exhaustive.
      parameters:
        - in: query
          name: limit
          description: Number of audit logs to retrieve
          schema:
            type: number
            default: 30
        - in: query
          name: page
          description: Page number for pagination
          schema:
            type: number
            default: 0
      responses:
        '200':
          description: A list of audit logs
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
        '403':
          description: Forbidden - user doesn't have access to this resource
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt