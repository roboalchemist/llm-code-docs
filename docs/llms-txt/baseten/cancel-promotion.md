# Source: https://docs.baseten.co/reference/management-api/deployments/promote/cancel-promotion.md

# Cancel model promotion

> Cancels an ongoing promotion to an environment and returns the cancellation status.

## OpenAPI

````yaml post /v1/models/{model_id}/environments/{env_name}/cancel_promotion
paths:
  path: /v1/models/{model_id}/environments/{env_name}/cancel_promotion
  method: post
  servers:
    - url: https://api.baseten.co
  request:
    security:
      - title: ApiKeyAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: apiKey
              description: >-
                You must specify the scheme 'Api-Key' in the Authorization
                header. For example, `Authorization: Api-Key <Your_Api_Key>`
          cookie: {}
    parameters:
      path:
        model_id:
          schema:
            - type: string
              required: true
        env_name:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - lang: bash
        source: >
          curl --request POST \

          --url
          https://api.baseten.co/v1/models/{model_id}/environments/{env_name}/cancel_promotion
          \

          --header "Authorization: Api-Key $BASETEN_API_KEY"
      - lang: python
        source: >-
          import requests

          import os

          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

          url =
          "https://api.baseten.co/v1/models/{model_id}/environments/{env_name}/cancel_promotion"


          headers = {"Authorization": f"Api-Key {API_KEY}"}


          response = requests.request(
              "POST",
              url,
              headers=headers,
              json={}
          )


          print(response.text)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - $ref: '#/components/schemas/CancelPromotionStatusV1'
                    description: >-
                      Status of the request to cancel a promotion. Can be
                      CANCELED or RAMPING_DOWN.
              message:
                allOf:
                  - description: >-
                      A message describing the status of the request to cancel a
                      promotion
                    title: Message
                    type: string
            title: CancelPromotionResponseV1
            description: The response to a request to cancel a promotion.
            refIdentifier: '#/components/schemas/CancelPromotionResponseV1'
            requiredProperties:
              - status
              - message
        examples:
          example:
            value:
              status: CANCELED
              message: <string>
        description: The response to a request to cancel a promotion.
  deprecated: false
  type: path
components:
  schemas:
    CancelPromotionStatusV1:
      description: The status of a request to cancel a promotion.
      enum:
        - CANCELED
        - RAMPING_DOWN
      title: CancelPromotionStatusV1
      type: string

````