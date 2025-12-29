# Source: https://docs.ultravox.ai/api-reference/accounts/accounts-me-telephony-config-partial-update.md

# Set Telephony Credentials

> Allows adding or updating telephony provider credentials to an account



## OpenAPI

````yaml patch /api/accounts/me/telephony_config
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
    patch:
      tags:
        - accounts
      operationId: accounts_me_telephony_config_partial_update
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchedAccountTelephonyConfig'
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
    PatchedAccountTelephonyConfig:
      type: object
      properties:
        twilio:
          allOf:
            - $ref: '#/components/schemas/TwilioConfig'
          nullable: true
          description: Your Twilio configuration. See https://console.twilio.com/
        telnyx:
          allOf:
            - $ref: '#/components/schemas/TelnyxConfig'
          nullable: true
          description: Your Telnyx configuration. See https://portal.telnyx.com/
        plivo:
          allOf:
            - $ref: '#/components/schemas/PlivoConfig'
          nullable: true
          description: Your Plivo configuration. See https://console.plivo.com/dashboard/
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
    TwilioConfig:
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
        authToken:
          type: string
          description: Your Twilio Auth Token.
      required:
        - accountSid
        - authToken
    TelnyxConfig:
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
          description: >-
            Your Telnyx Account SID. See
            https://portal.telnyx.com/#/account/general
        apiKey:
          type: string
          description: Your Telnyx API Key. See https://portal.telnyx.com/#/api-keys
        publicKey:
          type: string
          description: >-
            Your Telnyx Public Key. See
            https://portal.telnyx.com/#/api-keys/public-key
        applicationSid:
          type: string
          description: >-
            Your Telnyx Application SID. This must be configured with an
            Outbound Voice Profile that allows calls to your destination. See
            https://portal.telnyx.com/#/call-control/texml
          maxLength: 40
      required:
        - accountSid
        - apiKey
        - applicationSid
        - publicKey
    PlivoConfig:
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
        authToken:
          type: string
          description: Your Plivo Auth Token.
      required:
        - authId
        - authToken
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.ultravox.ai/llms.txt