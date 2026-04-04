# Source: https://docs.galileo.ai/api-reference/evaluate/cancel-jobs-for-project-run.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Cancel Jobs For Project Run

> Get all jobs for a project and run.

Revoke them from Celery.



## OpenAPI

````yaml https://api.staging.galileo.ai/public/v1/openapi.json put /v1/projects/{project_id}/runs/{run_id}/cancel-jobs
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers:
  - url: https://api.staging.galileo.ai
    description: Galileo Public APIs - staging
security: []
paths:
  /v1/projects/{project_id}/runs/{run_id}/cancel-jobs:
    put:
      tags:
        - evaluate
      summary: Cancel Jobs For Project Run
      description: |-
        Get all jobs for a project and run.

        Revoke them from Celery.
      operationId: >-
        cancel_jobs_for_project_run_v1_projects__project_id__runs__run_id__cancel_jobs_put
      parameters:
        - name: project_id
          in: path
          required: true
          schema:
            type: string
            format: uuid4
            title: Project Id
        - name: run_id
          in: path
          required: true
          schema:
            type: string
            format: uuid4
            title: Run Id
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - APIKeyHeader: []
        - OAuth2PasswordBearer: []
        - HTTPBasic: []
components:
  schemas:
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
  securitySchemes:
    APIKeyHeader:
      type: apiKey
      in: header
      name: Galileo-API-Key
    OAuth2PasswordBearer:
      type: oauth2
      flows:
        password:
          scopes: {}
          tokenUrl: https://api.staging.galileo.ai/login
    HTTPBasic:
      type: http
      scheme: basic

````