# Source: https://docs.asapp.com/apis/generativeagent/get-generativeagent-state.md

# Get GenerativeAgent state

> This API provides the current state of the generative agent for a given conversation.


## OpenAPI

````yaml api-specs/generativeagent.yaml get /generativeagent/v1/state
paths:
  path: /generativeagent/v1/state
  method: get
  servers:
    - url: https://api.sandbox.asapp.com
  request:
    security:
      - title: API ID & API Secret
        parameters:
          query: {}
          header:
            asapp-api-id:
              type: apiKey
            asapp-api-secret:
              type: apiKey
          cookie: {}
    parameters:
      path: {}
      query:
        criteria:
          schema:
            - type: object
              properties:
                externalId:
                  allOf:
                    - type: string
                      description: >-
                        External conversation identifier from your external chat
                        / voice system
              description: Search criteria
              additionalProperties: false
              minProperties: 1
          style: form
          explode: true
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              state:
                allOf:
                  - type: string
                    enum:
                      - ready
                      - processing
                      - waitingForConfirmation
                      - waitingForAuth
                      - transferredToAgent
                      - transferredToSystem
                    description: |
                      The last status of the conversation:
                        * `ready` - GenerativeAgent is ready to respond to requests
                        * `processing` - GenerativeAgent is actively processing the conversation
                        * `waitingForConfirmation` - GenerativeAgent is expecting an explicit confirmation on the next message
                        * `waitingForAuth` - GenerativeAgent is waiting for the user to login before proceeding
                        * `transferredToAgent` - GenerativeAgent is no longer able to provide meaningful responses and has 
                                                 requested the conversation be transferred to a human agent
                        * `transferredToSystem` - GenerativeAgent has transferred control of this conversation back to the
                                                  caller system. However, it will respond if new analyze requests are made
              lastGenerativeAgentMessageId:
                allOf:
                  - type: string
                    description: >-
                      ULID identifier of the last asynchronous response that was
                      sent to the customer
              currentTaskName:
                allOf:
                  - type: string
                    description: Current task TaskBot is executing
              inputVariables:
                allOf:
                  - type: object
                    description: Last input variables
            example:
              state: ready
              lastGenerativeAgentMessageId: 01HWXSGMT91HCS18BV0CRGEKY8
              currentTaskName: PaymentDetails
              inputVariables:
                input-context: >-
                  Customer chatted in to check the details of their last
                  payment.
                last-customer-purchase: '2024-05-07'
        examples:
          example:
            value:
              state: ready
              lastGenerativeAgentMessageId: 01HWXSGMT91HCS18BV0CRGEKY8
              currentTaskName: PaymentDetails
              inputVariables:
                input-context: >-
                  Customer chatted in to check the details of their last
                  payment.
                last-customer-purchase: '2024-05-07'
        description: Successfully fetched state of generative agent for a conversation
  deprecated: false
  type: path
components:
  schemas: {}

````