# Source: https://docs.baseten.co/reference/management-api/deployments/promote/cancel-promotion.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Cancel model promotion

> Cancels an ongoing promotion to an environment and returns the cancellation status.

<ResponseExample>
  ```json 200 theme={"system"}
  {
    "status": "CANCELED",
    "message": "Promotion to production was successfully canceled."
  }
  ```

  ```json 400 theme={"system"}
  {
    "code": "VALIDATION_ERROR",
    "message": "Environment production has no in progress promotion."
  }
  ```
</ResponseExample>


## OpenAPI

````yaml post /v1/models/{model_id}/environments/{env_name}/cancel_promotion
openapi: 3.1.0
info:
  description: REST API for management of Baseten resources
  title: Baseten management API
  version: 1.0.0
servers:
  - url: https://api.baseten.co
security:
  - ApiKeyAuth: []
paths:
  /v1/models/{model_id}/environments/{env_name}/cancel_promotion:
    parameters:
      - $ref: '#/components/parameters/model_id'
      - $ref: '#/components/parameters/env_name'
    post:
      summary: Cancels a promotion to an environment
      description: >-
        Cancels an ongoing promotion to an environment and returns the
        cancellation status.
      responses:
        '200':
          description: The response to a request to cancel a promotion.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CancelPromotionResponseV1'
components:
  parameters:
    model_id:
      schema:
        type: string
      name: model_id
      in: path
      required: true
    env_name:
      schema:
        type: string
      name: env_name
      in: path
      required: true
  schemas:
    CancelPromotionResponseV1:
      description: The response to a request to cancel a promotion.
      properties:
        status:
          $ref: '#/components/schemas/CancelPromotionStatusV1'
          description: >-
            Status of the request to cancel a promotion. Can be CANCELED or
            RAMPING_DOWN.
        message:
          description: A message describing the status of the request to cancel a promotion
          title: Message
          type: string
      required:
        - status
        - message
      title: CancelPromotionResponseV1
      type: object
    CancelPromotionStatusV1:
      description: The status of a request to cancel a promotion.
      enum:
        - CANCELED
        - RAMPING_DOWN
      title: CancelPromotionStatusV1
      type: string
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Authorization
      description: >-
        You must specify the scheme 'Api-Key' in the Authorization header. For
        example, `Authorization: Api-Key <Your_Api_Key>`

````