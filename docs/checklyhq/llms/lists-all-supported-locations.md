# Source: https://checklyhq.com/docs/api-reference/location/lists-all-supported-locations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Lists all supported locations

> Lists all supported locationss.



## OpenAPI

````yaml get /v1/locations
openapi: 3.0.0
info:
  title: Checkly Public API
  version: v1
  description: >-
    These are the docs for the newly released Checkly Public API. If you have
    any questions, please do not hesitate to get in touch with us.
servers:
  - url: https://api.checklyhq.com
security:
  - Bearer: []
tags: []
paths:
  /v1/locations:
    get:
      tags:
        - Location
      summary: Lists all supported locations
      description: Lists all supported locationss.
      operationId: getV1Locations
      parameters:
        - name: x-checkly-account
          in: header
          schema:
            type: string
            description: >-
              Your Checkly account ID, you can find it at
              https://app.checklyhq.com/settings/account/general
            x-format:
              guid: true
          description: >-
            Your Checkly account ID, you can find it at
            https://app.checklyhq.com/settings/account/general
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LocationList'
        '429':
          description: Too Many Requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TooManyRequestsError'
components:
  schemas:
    LocationList:
      type: array
      items:
        $ref: '#/components/schemas/Model223'
    TooManyRequestsError:
      type: object
      properties:
        statusCode:
          type: number
          enum:
            - 429
        error:
          $ref: '#/components/schemas/Model2'
        message:
          type: string
          example: Too Many Requests
        attributes:
          $ref: '#/components/schemas/attributes'
      required:
        - statusCode
        - error
    Model223:
      type: object
      properties:
        region:
          type: string
          description: The unique identifier of this location.
          example: us-east-1
        name:
          type: string
          description: Friendly name of this location.
          example: N. Virginia
      required:
        - region
        - name
    Model2:
      type: string
      enum:
        - Too Many Requests
    attributes:
      type: object
  securitySchemes:
    Bearer:
      type: http
      scheme: bearer
      bearerFormat: Bearer
      description: >-
        The Checkly Public API uses API keys to authenticate requests. You can
        get the API Key
        [here](https://app.checklyhq.com/settings/user/api-keys). Your API key
        is like a password:  keep it secure!

        Authentication to the API is performed using the Bearer auth method in
        the Authorization header and using the account ID.

        For example, set **Authorization** header while using cURL: `curl -H
        "Authorization: Bearer [apiKey]" "X-Checkly-Account: [accountId]"` 

````

Built with [Mintlify](https://mintlify.com).