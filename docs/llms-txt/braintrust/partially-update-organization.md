# Source: https://braintrust.dev/docs/api-reference/organizations/partially-update-organization.md

# Partially update organization

> Partially update an organization object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.



## OpenAPI

````yaml openapi.yaml patch /v1/organization/{organization_id}
openapi: 3.1.1
info:
  version: 1.0.0
  title: Braintrust API
  description: >-
    API specification for the backend data server. The API is hosted globally at

    https://api.braintrust.dev or in your own environment.


    You can access the OpenAPI spec for this API at
    https://github.com/braintrustdata/braintrust-openapi.
  license:
    name: Apache 2.0
servers:
  - url: https://api.braintrust.dev
security:
  - bearerAuth: []
  - {}
paths:
  /v1/organization/{organization_id}:
    patch:
      tags:
        - Organizations
      summary: Partially update organization
      description: >-
        Partially update an organization object. Specify the fields to update in
        the payload. Any object-type fields will be deep-merged with existing
        content. Currently we do not support removing fields or setting them to
        null.
      operationId: patchOrganizationId
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParam'
      requestBody:
        description: Fields to update
        required: false
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchOrganization'
      responses:
        '200':
          description: Returns the organization object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Organization'
        '400':
          description: >-
            The request was unacceptable, often due to missing a required
            parameter
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '401':
          description: No valid API key provided
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '403':
          description: The API key doesn’t have permissions to perform the request
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '429':
          description: >-
            Too many requests hit the API too quickly. We recommend an
            exponential backoff of your requests
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '500':
          description: Something went wrong on Braintrust's end. (These are rare.)
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
      security:
        - bearerAuth: []
        - {}
components:
  parameters:
    OrganizationIdParam:
      schema:
        $ref: '#/components/schemas/OrganizationIdParam'
      required: true
      description: Organization id
      name: organization_id
      in: path
  schemas:
    PatchOrganization:
      type: object
      properties:
        name:
          type: string
          nullable: true
          description: Name of the organization
        api_url:
          type: string
          nullable: true
        is_universal_api:
          type: boolean
          nullable: true
        proxy_url:
          type: string
          nullable: true
        realtime_url:
          type: string
          nullable: true
    Organization:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the organization
        name:
          type: string
          description: Name of the organization
        api_url:
          type: string
          nullable: true
        is_universal_api:
          type: boolean
          nullable: true
        proxy_url:
          type: string
          nullable: true
        realtime_url:
          type: string
          nullable: true
        created:
          type: string
          nullable: true
          format: date-time
          description: Date of organization creation
      required:
        - id
        - name
    OrganizationIdParam:
      type: string
      format: uuid
      description: Organization id
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API key or JWT
      description: >-
        Most Braintrust endpoints are authenticated by providing your API key as
        a header `Authorization: Bearer [api_key]` to your HTTP request. You can
        create an API key in the Braintrust [organization settings
        page](https://www.braintrustdata.com/app/settings?subroute=api-keys).

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt