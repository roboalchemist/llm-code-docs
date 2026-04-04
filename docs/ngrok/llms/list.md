# Source: https://ngrok.com/docs/api-reference/weightedbackends/list.md

# Source: https://ngrok.com/docs/api-reference/vaults/list.md

# Source: https://ngrok.com/docs/api-reference/tunnelsessions/list.md

# Source: https://ngrok.com/docs/api-reference/tunnels/list.md

# Source: https://ngrok.com/docs/api-reference/tunnelgroupbackends/list.md

# Source: https://ngrok.com/docs/api-reference/tlscertificates/list.md

# Source: https://ngrok.com/docs/api-reference/staticbackends/list.md

# Source: https://ngrok.com/docs/api-reference/sshusercertificates/list.md

# Source: https://ngrok.com/docs/api-reference/sshhostcertificates/list.md

# Source: https://ngrok.com/docs/api-reference/sshcredentials/list.md

# Source: https://ngrok.com/docs/api-reference/sshcertificateauthorities/list.md

# Source: https://ngrok.com/docs/api-reference/secrets/list.md

# Source: https://ngrok.com/docs/api-reference/reserveddomains/list.md

# Source: https://ngrok.com/docs/api-reference/reservedaddrs/list.md

# Source: https://ngrok.com/docs/api-reference/iprestrictions/list.md

# Source: https://ngrok.com/docs/api-reference/ippolicyrules/list.md

# Source: https://ngrok.com/docs/api-reference/ippolicies/list.md

# Source: https://ngrok.com/docs/api-reference/httpresponsebackends/list.md

# Source: https://ngrok.com/docs/api-reference/failoverbackends/list.md

# Source: https://ngrok.com/docs/api-reference/eventsubscriptions/list.md

# Source: https://ngrok.com/docs/api-reference/eventsources/list.md

# Source: https://ngrok.com/docs/api-reference/eventdestinations/list.md

# Source: https://ngrok.com/docs/api-reference/endpoints/list.md

# Source: https://ngrok.com/docs/api-reference/edgestls/list.md

# Source: https://ngrok.com/docs/api-reference/edgestcp/list.md

# Source: https://ngrok.com/docs/api-reference/edgeshttps/list.md

# Source: https://ngrok.com/docs/api-reference/credentials/list.md

# Source: https://ngrok.com/docs/api-reference/certificateauthorities/list.md

# Source: https://ngrok.com/docs/api-reference/botusers/list.md

# Source: https://ngrok.com/docs/api-reference/applicationusers/list.md

# Source: https://ngrok.com/docs/api-reference/applicationsessions/list.md

# Source: https://ngrok.com/docs/api-reference/apikeys/list.md

# Source: https://ngrok.com/docs/api-reference/agentingresses/list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> List all agent ingress configurations in your ngrok account with optional filtering and pagination.

# List



## OpenAPI

````yaml get /agent_ingresses
openapi: 3.0.0
info:
  title: ngrok OpenAPI
  version: 1.0.0
servers:
  - url: https://api.ngrok.com
security:
  - authentication: []
paths:
  /agent_ingresses:
    get:
      tags:
        - AgentIngresses
      summary: List
      description: |
        List all Agent Ingresses owned by this account
      operationId: AgentIngressesList
      parameters:
        - $ref: '#/components/parameters/ngrokVersion'
        - name: before_id
          description: >
            Expects a resource ID as its input. Returns earlier entries in the
            result set, sorted by ID.
          in: query
          required: false
          schema:
            type: string
        - name: limit
          description: >
            Constrains the number of results in the dataset. See the [API
            Overview](https://ngrok.com/docs/api/index#pagination) for details.
          in: query
          required: false
          schema:
            type: string
        - name: filter
          description: >
            A CEL expression to filter the list results. Supports logical and
            comparison operators to match on fields such as `id`, `metadata`,
            `created_at`, and more. See ngrok API Filtering for syntax and field
            details: https://ngrok.com/docs/api/api-filtering.
          in: query
          required: false
          schema:
            type: string
      responses:
        '200':
          description: |
            List all Agent Ingresses owned by this account
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AgentIngressList'
components:
  parameters:
    ngrokVersion:
      name: ngrok-version
      in: header
      required: true
      schema:
        type: integer
        default: 2
  schemas:
    AgentIngressList:
      type: object
      properties:
        ingresses:
          description: |
            the list of Agent Ingresses owned by this account
          type: array
          items:
            $ref: '#/components/schemas/AgentIngress'
        uri:
          description: |
            URI of the Agent Ingress list API resource
          type: string
        next_page_uri:
          description: |
            URI of the next page, or null if there is no next page
          type: string
    AgentIngress:
      type: object
      properties:
        id:
          description: |
            unique Agent Ingress resource identifier
          type: string
        uri:
          description: |
            URI to the API resource of this Agent ingress
          type: string
        description:
          description: >
            human-readable description of the use of this Agent Ingress.
            optional, max 255 bytes.
          type: string
        metadata:
          description: >
            arbitrary user-defined machine-readable data of this Agent Ingress.
            optional, max 4096 bytes
          type: string
        domain:
          description: >
            the domain that you own to be used as the base domain name to
            generate regional agent ingress domains.
          type: string
        ns_targets:
          description: >
            a list of target values to use as the values of NS records for the
            domain property these values will delegate control over the domain
            to ngrok
          type: array
          items:
            type: string
        region_domains:
          description: >
            a list of regional agent ingress domains that are subdomains of the
            value of domain this value may increase over time as ngrok adds more
            regions
          type: array
          items:
            type: string
        created_at:
          description: |
            timestamp when the Agent Ingress was created, RFC 3339 format
          type: string
        certificate_management_policy:
          $ref: '#/components/schemas/AgentIngressCertPolicy'
          description: >
            configuration for automatic management of TLS certificates for this
            domain, or null if automatic management is disabled
        certificate_management_status:
          $ref: '#/components/schemas/AgentIngressCertStatus'
          description: >
            status of the automatic certificate management for this domain, or
            null if automatic management is disabled
    AgentIngressCertPolicy:
      type: object
      properties:
        authority:
          description: >
            certificate authority to request certificates from. The only
            supported value is letsencrypt.
          type: string
        private_key_type:
          description: >
            type of private key to use when requesting certificates. Defaults to
            rsa, can be either rsa or ecdsa.
          type: string
    AgentIngressCertStatus:
      type: object
      properties:
        renews_at:
          description: |
            timestamp when the next renewal will be requested, RFC 3339 format
          type: string
        provisioning_job:
          $ref: '#/components/schemas/AgentIngressCertJob'
          description: >
            status of the certificate provisioning job, or null if the
            certificiate isn't being provisioned or renewed
    AgentIngressCertJob:
      type: object
      properties:
        error_code:
          description: >
            if present, an error code indicating why provisioning is failing. It
            may be either a temporary condition (INTERNAL_ERROR), or a permanent
            one the user must correct (DNS_ERROR).
          type: string
        msg:
          description: |
            a message describing the current status or error
          type: string
        started_at:
          description: |
            timestamp when the provisioning job started, RFC 3339 format
          type: string
        retries_at:
          description: |
            timestamp when the provisioning job will be retried
          type: string
  securitySchemes:
    authentication:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).