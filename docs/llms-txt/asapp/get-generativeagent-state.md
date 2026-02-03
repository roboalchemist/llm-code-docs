# Source: https://docs.asapp.com/apis/generativeagent/get-generativeagent-state.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get GenerativeAgent state

> This API provides the current state of the generative agent for a given conversation.




## OpenAPI

````yaml api-specs/generativeagent.yaml get /generativeagent/v1/state
openapi: 3.0.1
info:
  title: GenerativeAgent API
  description: >
    GenerativeAgent API allows customers to interact with a chat / voice
    automation bot leveraging LLMs by sending messages and receiving responses
    asynchronously through webhooks
  contact:
    email: api-info@asapp.com
  license:
    name: ASAPP Software License
    url: https://api.asapp.com/LICENSE
  version: '0.1'
servers:
  - url: https://api.sandbox.asapp.com
security:
  - API-ID: []
    API-Secret: []
tags:
  - name: GenerativeAgent
    description: >-
      Operations to send messages and trigger GenerativeAgent to respond or
      query the current state
paths:
  /generativeagent/v1/state:
    get:
      tags:
        - GenerativeAgent
      summary: Get GenerativeAgent state
      description: >
        This API provides the current state of the generative agent for a given
        conversation.
      operationId: getState
      parameters:
        - in: query
          name: criteria
          description: Search criteria
          style: form
          explode: true
          schema:
            type: object
            properties:
              externalId:
                type: string
                description: >-
                  External conversation identifier from your external chat /
                  voice system
            additionalProperties: false
            minProperties: 1
      responses:
        '200':
          description: Successfully fetched state of generative agent for a conversation
          content:
            application/json:
              schema:
                type: object
                properties:
                  state:
                    type: string
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
                    type: string
                    description: >-
                      ULID identifier of the last asynchronous response that was
                      sent to the customer
                  currentTaskName:
                    type: string
                    description: Current task TaskBot is executing
                  inputVariables:
                    type: object
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
components:
  securitySchemes:
    API-ID:
      type: apiKey
      in: header
      name: asapp-api-id
    API-Secret:
      type: apiKey
      in: header
      name: asapp-api-secret

````