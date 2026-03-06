# Source: https://io.net/docs/reference/io-explorer/pow-summary.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# PoW Summary

> This PoW Summary endpoint returns information about the Proof of Work challenges for a device.



## OpenAPI

````yaml openapi/io-explorer/pow-summary.json get /v1/io-explorer/devices/{device_id}/pow-summary
openapi: 3.1.0
info:
  title: IO API
  version: '1.0'
servers:
  - url: https://api.io.solutions/
security:
  - sec0: []
paths:
  /v1/io-explorer/devices/{device_id}/pow-summary:
    get:
      summary: PoW Summary
      operationId: pow-summary
      parameters:
        - name: device_id
          in: path
          description: The unique identifier for your device.
          schema:
            type: string
          required: true
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value:
                    data:
                      device_id: dca013fb-5ffa-4134-9b4d-8cb71f953d20
                      last_challenge_status: succeeded
                      pow_jobs_failed: 0
                      pow_jobs_passed: 0
                    status: succeeded
              schema:
                type: object
                properties:
                  data:
                    type: object
                    properties:
                      device_id:
                        type: string
                        example: dca013fb-5ffa-4134-9b4d-8cb71f953d20
                      last_challenge_status:
                        type: string
                        example: succeeded
                      pow_jobs_failed:
                        type: integer
                        example: 0
                        default: 0
                      pow_jobs_passed:
                        type: integer
                        example: 0
                        default: 0
                  status:
                    type: string
                    example: succeeded
        '404':
          description: '404'
          content:
            text/plain:
              examples:
                Result:
                  value: Not found
        '422':
          description: '422'
          content:
            application/json:
              examples:
                Validation Error:
                  value:
                    detail:
                      - loc:
                          - string
                          - 0
                        msg: string
                        type: string
              schema:
                type: object
                properties:
                  detail:
                    type: array
                    items:
                      type: object
                      properties:
                        loc:
                          type: array
                        msg:
                          type: string
                          example: string
                        type:
                          type: string
                          example: string
      deprecated: false
components:
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````