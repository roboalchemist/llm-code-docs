# Source: https://ngrok.com/docs/api-reference/weightedbackends/delete.md

# Source: https://ngrok.com/docs/api-reference/vaults/delete.md

# Source: https://ngrok.com/docs/api-reference/tunnelgroupbackends/delete.md

# Source: https://ngrok.com/docs/api-reference/tlsedgetrafficpolicymodule/delete.md

# Source: https://ngrok.com/docs/api-reference/tlsedgetlsterminationmodule/delete.md

# Source: https://ngrok.com/docs/api-reference/tlsedgemutualtlsmodule/delete.md

# Source: https://ngrok.com/docs/api-reference/tlsedgeiprestrictionmodule/delete.md

# Source: https://ngrok.com/docs/api-reference/tlsedgebackendmodule/delete.md

# Source: https://ngrok.com/docs/api-reference/tlscertificates/delete.md

# Source: https://ngrok.com/docs/api-reference/tcpedgetrafficpolicymodule/delete.md

# Source: https://ngrok.com/docs/api-reference/tcpedgeiprestrictionmodule/delete.md

# Source: https://ngrok.com/docs/api-reference/tcpedgebackendmodule/delete.md

# Source: https://ngrok.com/docs/api-reference/staticbackends/delete.md

# Source: https://ngrok.com/docs/api-reference/sshusercertificates/delete.md

# Source: https://ngrok.com/docs/api-reference/sshhostcertificates/delete.md

# Source: https://ngrok.com/docs/api-reference/sshcredentials/delete.md

# Source: https://ngrok.com/docs/api-reference/sshcertificateauthorities/delete.md

# Source: https://ngrok.com/docs/api-reference/secrets/delete.md

# Source: https://ngrok.com/docs/api-reference/reserveddomains/delete.md

# Source: https://ngrok.com/docs/api-reference/reservedaddrs/delete.md

# Source: https://ngrok.com/docs/api-reference/iprestrictions/delete.md

# Source: https://ngrok.com/docs/api-reference/ippolicyrules/delete.md

# Source: https://ngrok.com/docs/api-reference/ippolicies/delete.md

# Source: https://ngrok.com/docs/api-reference/httpsedgetlsterminationmodule/delete.md

# Source: https://ngrok.com/docs/api-reference/httpsedgemutualtlsmodule/delete.md

# Source: https://ngrok.com/docs/api-reference/httpresponsebackends/delete.md

# Source: https://ngrok.com/docs/api-reference/failoverbackends/delete.md

# Source: https://ngrok.com/docs/api-reference/eventsubscriptions/delete.md

# Source: https://ngrok.com/docs/api-reference/eventsources/delete.md

# Source: https://ngrok.com/docs/api-reference/eventdestinations/delete.md

# Source: https://ngrok.com/docs/api-reference/endpoints/delete.md

# Source: https://ngrok.com/docs/api-reference/edgestls/delete.md

# Source: https://ngrok.com/docs/api-reference/edgestcp/delete.md

# Source: https://ngrok.com/docs/api-reference/edgeshttpsroutes/delete.md

# Source: https://ngrok.com/docs/api-reference/edgeshttps/delete.md

# Source: https://ngrok.com/docs/api-reference/edgeroutewebsockettcpconvertermodule/delete.md

# Source: https://ngrok.com/docs/api-reference/edgeroutewebhookverificationmodule/delete.md

# Source: https://ngrok.com/docs/api-reference/edgerouteuseragentfiltermodule/delete.md

# Source: https://ngrok.com/docs/api-reference/edgeroutetrafficpolicymodule/delete.md

# Source: https://ngrok.com/docs/api-reference/edgeroutesamlmodule/delete.md

# Source: https://ngrok.com/docs/api-reference/edgerouteresponseheadersmodule/delete.md

# Source: https://ngrok.com/docs/api-reference/edgerouterequestheadersmodule/delete.md

# Source: https://ngrok.com/docs/api-reference/edgerouteoidcmodule/delete.md

# Source: https://ngrok.com/docs/api-reference/edgerouteoauthmodule/delete.md

# Source: https://ngrok.com/docs/api-reference/edgerouteiprestrictionmodule/delete.md

# Source: https://ngrok.com/docs/api-reference/edgeroutecompressionmodule/delete.md

# Source: https://ngrok.com/docs/api-reference/edgeroutecircuitbreakermodule/delete.md

# Source: https://ngrok.com/docs/api-reference/edgeroutebackendmodule/delete.md

# Source: https://ngrok.com/docs/api-reference/credentials/delete.md

# Source: https://ngrok.com/docs/api-reference/certificateauthorities/delete.md

# Source: https://ngrok.com/docs/api-reference/botusers/delete.md

# Source: https://ngrok.com/docs/api-reference/applicationusers/delete.md

# Source: https://ngrok.com/docs/api-reference/applicationsessions/delete.md

# Source: https://ngrok.com/docs/api-reference/apikeys/delete.md

# Source: https://ngrok.com/docs/api-reference/agentingresses/delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> Delete a specific agent ingress configuration by its unique identifier.

# Delete



## OpenAPI

````yaml delete /agent_ingresses/{id}
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
    delete:
      tags:
        - AgentIngresses
      summary: Delete
      description: |
        Delete an Agent Ingress by ID
      operationId: AgentIngressesDelete
      parameters:
        - $ref: '#/components/parameters/ngrokVersion'
        - name: id
          description: |
            a resource identifier
          in: path
          required: true
          schema:
            type: string
      responses:
        '204':
          description: |
            Delete an Agent Ingress by ID
components:
  parameters:
    ngrokVersion:
      name: ngrok-version
      in: header
      required: true
      schema:
        type: integer
        default: 2
  securitySchemes:
    authentication:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).