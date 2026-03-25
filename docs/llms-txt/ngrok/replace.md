# Source: https://ngrok.com/docs/api-reference/tlsedgetrafficpolicymodule/replace.md

# Source: https://ngrok.com/docs/api-reference/tlsedgetlsterminationmodule/replace.md

# Source: https://ngrok.com/docs/api-reference/tlsedgemutualtlsmodule/replace.md

# Source: https://ngrok.com/docs/api-reference/tlsedgeiprestrictionmodule/replace.md

# Source: https://ngrok.com/docs/api-reference/tlsedgebackendmodule/replace.md

# Source: https://ngrok.com/docs/api-reference/tcpedgetrafficpolicymodule/replace.md

# Source: https://ngrok.com/docs/api-reference/tcpedgeiprestrictionmodule/replace.md

# Source: https://ngrok.com/docs/api-reference/tcpedgebackendmodule/replace.md

# Source: https://ngrok.com/docs/api-reference/httpsedgetlsterminationmodule/replace.md

# Source: https://ngrok.com/docs/api-reference/httpsedgemutualtlsmodule/replace.md

# Source: https://ngrok.com/docs/api-reference/edgeroutewebsockettcpconvertermodule/replace.md

# Source: https://ngrok.com/docs/api-reference/edgeroutewebhookverificationmodule/replace.md

# Source: https://ngrok.com/docs/api-reference/edgerouteuseragentfiltermodule/replace.md

# Source: https://ngrok.com/docs/api-reference/edgeroutetrafficpolicymodule/replace.md

# Source: https://ngrok.com/docs/api-reference/edgeroutesamlmodule/replace.md

# Source: https://ngrok.com/docs/api-reference/edgerouteresponseheadersmodule/replace.md

# Source: https://ngrok.com/docs/api-reference/edgerouterequestheadersmodule/replace.md

# Source: https://ngrok.com/docs/api-reference/edgerouteoidcmodule/replace.md

# Source: https://ngrok.com/docs/api-reference/edgerouteoauthmodule/replace.md

# Source: https://ngrok.com/docs/api-reference/edgerouteiprestrictionmodule/replace.md

# Source: https://ngrok.com/docs/api-reference/edgeroutecompressionmodule/replace.md

# Source: https://ngrok.com/docs/api-reference/edgeroutecircuitbreakermodule/replace.md

# Source: https://ngrok.com/docs/api-reference/edgeroutebackendmodule/replace.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> Replace or configure the backend module for a specific HTTPS edge route.

# Replace



## OpenAPI

````yaml put /edges/https/{edge_id}/routes/{id}/backend
openapi: 3.0.0
info:
  title: ngrok OpenAPI
  version: 1.0.0
servers:
  - url: https://api.ngrok.com
security:
  - authentication: []
paths:
  /edges/https/{edge_id}/routes/{id}/backend:
    put:
      tags:
        - EdgeRouteBackendModule
      summary: Replace
      operationId: EdgeRouteBackendModuleReplace
      parameters:
        - $ref: '#/components/parameters/ngrokVersion'
        - name: edge_id
          in: path
          required: true
          schema:
            type: string
        - name: id
          in: path
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EdgeRouteBackendReplace'
      responses:
        '200':
          description: n/a
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EndpointBackend'
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
    EdgeRouteBackendReplace:
      type: object
      properties:
        edge_id:
          description: n/a
          type: string
        id:
          description: n/a
          type: string
        module:
          $ref: '#/components/schemas/EndpointBackendMutate'
          description: n/a
    EndpointBackend:
      type: object
      properties:
        enabled:
          description: >
            `true` if the module will be applied to traffic, `false` to disable.
            default `true` if unspecified
          type: boolean
        backend:
          $ref: '#/components/schemas/Ref'
          description: |
            backend to be used to back this endpoint
    EndpointBackendMutate:
      type: object
      properties:
        enabled:
          description: >
            `true` if the module will be applied to traffic, `false` to disable.
            default `true` if unspecified
          type: boolean
        backend_id:
          description: |
            backend to be used to back this endpoint
          type: string
    Ref:
      type: object
      properties:
        id:
          description: |
            a resource identifier
          type: string
        uri:
          description: |
            a uri for locating a resource
          type: string
  securitySchemes:
    authentication:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).