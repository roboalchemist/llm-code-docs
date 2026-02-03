# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/create-event.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Event

> Partner notifies Vercel of any changes made to an Installation or a Resource. Vercel is expected to use `list-resources` and other read APIs to get the new state.<br/> <br/> `resource.updated` event should be dispatched when any state of a resource linked to Vercel is modified by the partner.<br/> `installation.updated` event should be dispatched when an installation's billing plan is changed via the provider instead of Vercel.<br/> <br/> Resource update use cases: <br/> <br/> - The user renames a database in the partner’s application. The partner should dispatch a `resource.updated` event to notify Vercel to update the resource in Vercel’s datastores.<br/> - A resource has been suspended due to a lack of use. The partner should dispatch a `resource.updated` event to notify Vercel to update the resource's status in Vercel's datastores.<br/>



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/events
openapi: 3.0.3
info:
  title: Vercel REST API & SDK
  description: >-
    The [`@vercel/sdk`](https://www.npmjs.com/package/@vercel/sdk) is a
    type-safe Typescript SDK that allows you to access the resources and methods
    of the Vercel REST API. Learn how to [install
    it](https://vercel.com/docs/rest-api/sdk#installing-vercel-sdk) and
    [authenticate](https://vercel.com/docs/rest-api/sdk#authentication) with a
    Vercel access token.
  contact:
    email: support@vercel.com
    name: Vercel Support
    url: https://vercel.com/support
  version: 0.0.1
servers:
  - url: https://api.vercel.com
    description: Production API
security: []
paths:
  /v1/installations/{integrationConfigurationId}/events:
    post:
      tags:
        - marketplace
      summary: Create Event
      description: >-
        Partner notifies Vercel of any changes made to an Installation or a
        Resource. Vercel is expected to use `list-resources` and other read APIs
        to get the new state.<br/> <br/> `resource.updated` event should be
        dispatched when any state of a resource linked to Vercel is modified by
        the partner.<br/> `installation.updated` event should be dispatched when
        an installation's billing plan is changed via the provider instead of
        Vercel.<br/> <br/> Resource update use cases: <br/> <br/> - The user
        renames a database in the partner’s application. The partner should
        dispatch a `resource.updated` event to notify Vercel to update the
        resource in Vercel’s datastores.<br/> - A resource has been suspended
        due to a lack of use. The partner should dispatch a `resource.updated`
        event to notify Vercel to update the resource's status in Vercel's
        datastores.<br/>
      operationId: create-event
      parameters:
        - name: integrationConfigurationId
          in: path
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - event
              properties:
                event:
                  oneOf:
                    - type: object
                      properties:
                        type:
                          type: string
                          enum:
                            - installation.updated
                        billingPlanId:
                          type: string
                          description: The installation-level billing plan ID
                      required:
                        - type
                      additionalProperties: false
                    - type: object
                      properties:
                        type:
                          type: string
                          enum:
                            - resource.updated
                        productId:
                          type: string
                          description: Partner-provided product slug or id
                        resourceId:
                          type: string
                          description: Partner provided resource ID
                      required:
                        - type
                        - resourceId
                      additionalProperties: false
              additionalProperties: false
        required: true
      responses:
        '201':
          description: ''
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: ''
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````