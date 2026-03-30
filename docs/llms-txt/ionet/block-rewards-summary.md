# Source: https://io.net/docs/reference/io-explorer/block-rewards-summary.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Block Rewards Summary

> The Block Rewards Summary endpoint returns insight on the block rewards associated with a specific device. This includes, but is not limited to, successful rewards, failed and missed rewards, and an earnings summary - given a specific date range. 



## OpenAPI

````yaml openapi/io-explorer/block-rewards-summary.json get /v1/io-blocks/devices/{device_id}/block-rewards-summary/{from_date}/{to_date}
openapi: 3.1.0
info:
  title: IO API
  version: '1.0'
servers:
  - url: https://api.io.solutions/
security:
  - sec0: []
paths:
  /v1/io-blocks/devices/{device_id}/block-rewards-summary/{from_date}/{to_date}:
    get:
      summary: Block Rewards Summary
      operationId: block-rewards-summary
      parameters:
        - name: device_id
          in: path
          description: Unique identifier for your device.
          schema:
            type: string
          required: true
        - name: from_date
          in: path
          description: The start date for the block reward info (YYYY-MM-DD).
          schema:
            type: string
          required: true
        - name: to_date
          in: path
          description: The end date for the block reward info (YYYY-MM-DD).
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
                    device_id: 00fd3995-9bf3-4371-87fd-91237a8248ed
                    total_block_rewards: 0
                    total_blocks_earned: 0
                    total_blocks_failed: 0
                    total_blocks_missed: 0
                    datewise_earnings_summary: []
              schema:
                type: object
                properties:
                  device_id:
                    type: string
                    example: 00fd3995-9bf3-4371-87fd-91237a8248ed
                  total_block_rewards:
                    type: integer
                    example: 0
                    default: 0
                  total_blocks_earned:
                    type: integer
                    example: 0
                    default: 0
                  total_blocks_failed:
                    type: integer
                    example: 0
                    default: 0
                  total_blocks_missed:
                    type: integer
                    example: 0
                    default: 0
                  datewise_earnings_summary:
                    type: array
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