# Source: https://docs.ultravox.ai/api-reference/accounts/accounts-me-telephony-config-retrieve.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ultravox.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Telephony Credentials

> Returns the telephony credentials associated with the active account



## OpenAPI

````yaml get /api/accounts/me/telephony_config
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/accounts/me/telephony_config:
    get:
      tags:
        - accounts
      operationId: accounts_me_telephony_config_retrieve
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AccountTelephonyConfigOutput'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    AccountTelephonyConfigOutput:
      type: object
      properties:
        twilio:
          allOf:
            - $ref: '#/components/schemas/TwilioConfigOutput'
          description: Your Twilio configuration.
        telnyx:
          allOf:
            - $ref: '#/components/schemas/TelnyxConfigOutput'
          description: Your Telnyx configuration.
        plivo:
          allOf:
            - $ref: '#/components/schemas/PlivoConfigOutput'
          description: Your Plivo configuration.
    TwilioConfigOutput:
      type: object
      properties:
        callCreationAllowedAgentIds:
          type: array
          items:
            type: string
            format: uuid
          description: >-
            List of agents for whom calls may be directly created by this
            telephony provider to facilitate incoming calls. May not be set if
            callCreationAllowAllAgents is true.
          maxItems: 100
        callCreationAllowAllAgents:
          type: boolean
          default: false
          description: >-
            If true, calls may be directly created by this telephony provider
            for all agents. If false, only agents listed in
            callCreationAllowedAgentIds are allowed.
        requestContextMapping:
          type: object
          additionalProperties:
            type: string
          description: >-
            Maps (dot separated) request fields to (dot separated) context
            fields for incoming call creation.
        accountSid:
          type: string
          description: Your Twilio Account SID.
        authTokenPrefix:
          allOf:
            - $ref: '#/components/schemas/KeyPrefix'
          description: The prefix of your Twilio Auth Token.
      required:
        - accountSid
        - authTokenPrefix
    TelnyxConfigOutput:
      type: object
      properties:
        callCreationAllowedAgentIds:
          type: array
          items:
            type: string
            format: uuid
          description: >-
            List of agents for whom calls may be directly created by this
            telephony provider to facilitate incoming calls. May not be set if
            callCreationAllowAllAgents is true.
          maxItems: 100
        callCreationAllowAllAgents:
          type: boolean
          default: false
          description: >-
            If true, calls may be directly created by this telephony provider
            for all agents. If false, only agents listed in
            callCreationAllowedAgentIds are allowed.
        requestContextMapping:
          type: object
          additionalProperties:
            type: string
          description: >-
            Maps (dot separated) request fields to (dot separated) context
            fields for incoming call creation.
        accountSid:
          type: string
          description: Your Telnyx Account SID.
        apiKeyPrefix:
          allOf:
            - $ref: '#/components/schemas/KeyPrefix'
          description: The prefix of your Telnyx API Key.
        publicKeyPrefix:
          allOf:
            - $ref: '#/components/schemas/KeyPrefix'
          description: The prefix of your Telnyx Public Key.
        applicationSid:
          type: string
          description: Your Telnyx Application SID.
      required:
        - accountSid
        - apiKeyPrefix
        - applicationSid
        - publicKeyPrefix
    PlivoConfigOutput:
      type: object
      properties:
        callCreationAllowedAgentIds:
          type: array
          items:
            type: string
            format: uuid
          description: >-
            List of agents for whom calls may be directly created by this
            telephony provider to facilitate incoming calls. May not be set if
            callCreationAllowAllAgents is true.
          maxItems: 100
        callCreationAllowAllAgents:
          type: boolean
          default: false
          description: >-
            If true, calls may be directly created by this telephony provider
            for all agents. If false, only agents listed in
            callCreationAllowedAgentIds are allowed.
        requestContextMapping:
          type: object
          additionalProperties:
            type: string
          description: >-
            Maps (dot separated) request fields to (dot separated) context
            fields for incoming call creation.
        authId:
          type: string
          description: Your Plivo Auth ID.
        authTokenPrefix:
          allOf:
            - $ref: '#/components/schemas/KeyPrefix'
          description: The prefix of your Plivo Auth Token.
      required:
        - authId
        - authTokenPrefix
    KeyPrefix:
      type: object
      properties:
        prefix:
          type: string
          description: The prefix of the API key.
      required:
        - prefix
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````