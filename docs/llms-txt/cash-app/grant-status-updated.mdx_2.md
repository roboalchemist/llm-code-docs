# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/grants-cash-app-afterpay/grant-status-updated.mdx

# Grant status updated

POST 

Webhook notification sent when a grant's status changes

Reference: https://developers.cash.app/cash-app-afterpay/api-reference/reference/grants-cash-app-afterpay/grant-status-updated

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths: {}
webhooks:
  grant-status-updated:
    post:
      operationId: grant-status-updated
      summary: Grant status updated
      description: Webhook notification sent when a grant's status changes
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/OnFileGrantStatusUpdated'
components:
  schemas:
    OnFileGrantStatusUpdatedDataType:
      type: string
      enum:
        - ON_FILE_GRANT
      title: OnFileGrantStatusUpdatedDataType
    GrantType:
      type: string
      enum:
        - ON_FILE
      description: Type of grant
      title: GrantType
    GrantStatus:
      type: string
      enum:
        - ACTIVE
        - CANCELLED
      description: Current status of the grant
      title: GrantStatus
    Grant:
      type: object
      properties:
        id:
          type: string
          description: Unique id identifying the grant
        type:
          $ref: '#/components/schemas/GrantType'
          description: Type of grant
        status:
          $ref: '#/components/schemas/GrantStatus'
          description: Current status of the grant
        created:
          type: string
          format: date-time
          description: Timestamp when the grant was created
        merchantReference:
          type:
            - string
            - 'null'
          description: Merchant's reference for this grant
        cancelled:
          type: string
          format: date-time
          description: If present, indicates when the grant was cancelled
        expires:
          type: string
          format: date-time
          description: >-
            If present, indicates when the grant's status will become EXPIRED,
            preventing a client from using it to create payments
        consumerReference:
          type:
            - string
            - 'null'
          description: Reference identifier for the consumer
        email:
          type:
            - string
            - 'null'
          description: Masked email address of the consumer
        requestId:
          type:
            - string
            - 'null'
          description: If present, unique identifier for the request
      required:
        - id
        - type
        - status
        - created
      title: Grant
    OnFileGrantStatusUpdatedDataObject:
      type: object
      properties:
        grant:
          $ref: '#/components/schemas/Grant'
      title: OnFileGrantStatusUpdatedDataObject
    OnFileGrantStatusUpdatedData:
      type: object
      properties:
        id:
          type: string
        type:
          $ref: '#/components/schemas/OnFileGrantStatusUpdatedDataType'
        object:
          $ref: '#/components/schemas/OnFileGrantStatusUpdatedDataObject'
      required:
        - id
        - type
        - object
      title: OnFileGrantStatusUpdatedData
    OnFileGrantStatusUpdated:
      type: object
      properties:
        type:
          type: string
        eventId:
          type: string
          format: uuid
        createdAt:
          type: string
          format: date-time
        data:
          $ref: '#/components/schemas/OnFileGrantStatusUpdatedData'
      required:
        - type
        - eventId
        - createdAt
        - data
      title: OnFileGrantStatusUpdated

```