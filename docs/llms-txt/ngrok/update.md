# Source: https://ngrok.com/docs/k8s/installation/update.md

# Source: https://ngrok.com/docs/api-reference/weightedbackends/update.md

# Source: https://ngrok.com/docs/api-reference/vaults/update.md

# Source: https://ngrok.com/docs/api-reference/tunnelsessions/update.md

# Source: https://ngrok.com/docs/api-reference/tunnelgroupbackends/update.md

# Source: https://ngrok.com/docs/api-reference/tlscertificates/update.md

# Source: https://ngrok.com/docs/api-reference/staticbackends/update.md

# Source: https://ngrok.com/docs/api-reference/sshusercertificates/update.md

# Source: https://ngrok.com/docs/api-reference/sshhostcertificates/update.md

# Source: https://ngrok.com/docs/api-reference/sshcredentials/update.md

# Source: https://ngrok.com/docs/api-reference/sshcertificateauthorities/update.md

# Source: https://ngrok.com/docs/api-reference/secrets/update.md

# Source: https://ngrok.com/docs/api-reference/reserveddomains/update.md

# Source: https://ngrok.com/docs/api-reference/reservedaddrs/update.md

# Source: https://ngrok.com/docs/api-reference/iprestrictions/update.md

# Source: https://ngrok.com/docs/api-reference/ippolicyrules/update.md

# Source: https://ngrok.com/docs/api-reference/ippolicies/update.md

# Source: https://ngrok.com/docs/api-reference/httpresponsebackends/update.md

# Source: https://ngrok.com/docs/api-reference/failoverbackends/update.md

# Source: https://ngrok.com/docs/api-reference/eventsubscriptions/update.md

# Source: https://ngrok.com/docs/api-reference/eventsources/update.md

# Source: https://ngrok.com/docs/api-reference/eventdestinations/update.md

# Source: https://ngrok.com/docs/api-reference/endpoints/update.md

# Source: https://ngrok.com/docs/api-reference/edgestls/update.md

# Source: https://ngrok.com/docs/api-reference/edgestcp/update.md

# Source: https://ngrok.com/docs/api-reference/edgeshttpsroutes/update.md

# Source: https://ngrok.com/docs/api-reference/edgeshttps/update.md

# Source: https://ngrok.com/docs/api-reference/credentials/update.md

# Source: https://ngrok.com/docs/api-reference/certificateauthorities/update.md

# Source: https://ngrok.com/docs/api-reference/botusers/update.md

# Source: https://ngrok.com/docs/api-reference/apikeys/update.md

# Source: https://ngrok.com/docs/api-reference/agentingresses/update.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> Update an existing agent ingress configuration with new settings or parameters.

# Update



## OpenAPI

````yaml patch /agent_ingresses/{id}
openapi: 3.0.0
info:
  title: ngrok OpenAPI
  version: 1.0.0
servers:
  - url: https://api.ngrok.com
security:
  - authentication: []
paths:
  /agent_ingresses/{id}:
    patch:
      tags:
        - AgentIngresses
      summary: Update
      description: |
        Update attributes of an Agent Ingress by ID.
      operationId: AgentIngressesUpdate
      parameters:
        - $ref: '#/components/parameters/ngrokVersion'
        - name: id
          in: path
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AgentIngressUpdate'
      responses:
        '200':
          description: |
            Update attributes of an Agent Ingress by ID.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AgentIngress'
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
    AgentIngressUpdate:
      type: object
      properties:
        id:
          description: n/a
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
        certificate_management_policy:
          $ref: '#/components/schemas/AgentIngressCertPolicy'
          description: >
            configuration for automatic management of TLS certificates for this
            domain, or null if automatic management is disabled. Optional.
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