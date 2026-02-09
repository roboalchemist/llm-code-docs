# Source: https://docs.ultravox.ai/api-reference/sip/sip-get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ultravox.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Account SIP configuration

> Returns the SIP configuration for your account



## OpenAPI

````yaml get /api/sip
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/sip:
    get:
      tags:
        - sip
      operationId: sip_retrieve
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SipConfig'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    SipConfig:
      type: object
      properties:
        allowedCidrRanges:
          type: array
          items:
            type: string
            format: ipv4-cidr
          description: >-
            The list of IPv4 CIDR ranges from which incoming SIP calls will be
            accepted.
        allowAllAgents:
          type: boolean
          default: false
          description: >-
            If true, adds an implicit allowance for requests matching
            agent_<agent_id>@<anydomain> for any of your agents.
        allowedAgents:
          type: array
          items:
            $ref: '#/components/schemas/AgentAllowance'
          description: >-
            Calls must match a pattern for one of these agents (or the global
            agent pattern if allowAllAgents is true) to be accepted.
          maxItems: 20
        domain:
          type: string
          readOnly: true
          description: The domain used for SIP invites for your account.
      required:
        - allowedAgents
        - domain
    AgentAllowance:
      type: object
      properties:
        agentId:
          type: string
          format: uuid
          description: The ID of the agent to allow.
        toUserPattern:
          type: string
          description: >-
            A pattern to apply to the to user part of the URI of any incoming
            sip INVITE that determines how this agent can be reached. Defaults
            to ^agent_<agent_id>$ if not specified.
          maxLength: 200
      required:
        - agentId
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````