# Source: https://www.traceloop.com/docs/api-reference/organizations/create-a-new-organization.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new organization

> Create a new organization with environments and API keys.



## OpenAPI

````yaml post /v2/organizations
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/organizations:
    post:
      tags:
        - organizations
      summary: Create a new organization
      description: Create a new organization with environments and API keys.
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.CreateOrganizationRequest'
        description: Organization creation request
        required: true
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.CreateOrganizationResponse'
        '400':
          description: Invalid request body or validation error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.ErrorResponse'
        '403':
          description: Not allowed to create organizations
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.ErrorResponse'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.ErrorResponse'
components:
  schemas:
    request.CreateOrganizationRequest:
      properties:
        envs:
          items:
            type: string
          type: array
        org_name:
          type: string
      required:
        - org_name
      type: object
    response.CreateOrganizationResponse:
      properties:
        environments:
          items:
            $ref: '#/components/schemas/response.EnvironmentWithKeyResponse'
          type: array
        org_id:
          type: string
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    response.EnvironmentWithKeyResponse:
      properties:
        api_key:
          type: string
        slug:
          type: string
      type: object

````