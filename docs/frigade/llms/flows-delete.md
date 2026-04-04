# Source: https://docs.frigade.com/api-reference/flows/flows-delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Flow

> Delete a Flow

Deleting a Flow will remove all the data associated with it, including the Flow itself, its responses, and any other related data. This operation is irreversible.

<Warning>Only call this endpoint from your backend code.</Warning>

### Obtaining the numeric ID of a Flow

To obtain the numeric ID of a Flow, you should make a [GET request](/api-reference/flows/flows-get) to get the Flow you are looking to change. The numeric ID is a number and is different from the slug (e.g. `flow_GzXC2fHz`). The reason for this is that different [versions](/platform/versioning) of the Flow share the same slug but have different numeric IDs to differentiate them.


## OpenAPI

````yaml delete /v1/flows/{numericFlowId}
openapi: 3.0.0
info:
  title: Frigade API
  description: Official Frigade API documentation
  version: '1.0'
  contact: {}
servers: []
security: []
tags: []
paths:
  /v1/flows/{numericFlowId}:
    delete:
      tags:
        - flows
      description: Delete a Flow
      operationId: FlowsController_delete
      parameters: []
      responses:
        '204':
          description: The Flow has been successfully deleted.
      security:
        - bearer: []
components:
  securitySchemes:
    bearer:
      scheme: bearer
      bearerFormat: JWT
      type: http
      description: >-
        Authentication header of the form `Bearer: <token>`, where `<token>` is
        either your public or private API key. [See when to use
        which](/v2/api-reference/authorization)

````