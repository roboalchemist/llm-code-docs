# Source: https://ngrok.com/docs/api-reference/weightedbackends/get.md

# Source: https://ngrok.com/docs/api-reference/vaults/get.md

# Source: https://ngrok.com/docs/api-reference/tunnelsessions/get.md

# Source: https://ngrok.com/docs/api-reference/tunnels/get.md

# Source: https://ngrok.com/docs/api-reference/tunnelgroupbackends/get.md

# Source: https://ngrok.com/docs/api-reference/tlsedgetrafficpolicymodule/get.md

# Source: https://ngrok.com/docs/api-reference/tlsedgetlsterminationmodule/get.md

# Source: https://ngrok.com/docs/api-reference/tlsedgemutualtlsmodule/get.md

# Source: https://ngrok.com/docs/api-reference/tlsedgeiprestrictionmodule/get.md

# Source: https://ngrok.com/docs/api-reference/tlsedgebackendmodule/get.md

# Source: https://ngrok.com/docs/api-reference/tlscertificates/get.md

# Source: https://ngrok.com/docs/api-reference/tcpedgetrafficpolicymodule/get.md

# Source: https://ngrok.com/docs/api-reference/tcpedgeiprestrictionmodule/get.md

# Source: https://ngrok.com/docs/api-reference/tcpedgebackendmodule/get.md

# Source: https://ngrok.com/docs/api-reference/staticbackends/get.md

# Source: https://ngrok.com/docs/api-reference/sshusercertificates/get.md

# Source: https://ngrok.com/docs/api-reference/sshhostcertificates/get.md

# Source: https://ngrok.com/docs/api-reference/sshcredentials/get.md

# Source: https://ngrok.com/docs/api-reference/sshcertificateauthorities/get.md

# Source: https://ngrok.com/docs/api-reference/secrets/get.md

# Source: https://ngrok.com/docs/api-reference/reserveddomains/get.md

# Source: https://ngrok.com/docs/api-reference/reservedaddrs/get.md

# Source: https://ngrok.com/docs/api-reference/iprestrictions/get.md

# Source: https://ngrok.com/docs/api-reference/ippolicyrules/get.md

# Source: https://ngrok.com/docs/api-reference/ippolicies/get.md

# Source: https://ngrok.com/docs/api-reference/httpsedgetlsterminationmodule/get.md

# Source: https://ngrok.com/docs/api-reference/httpsedgemutualtlsmodule/get.md

# Source: https://ngrok.com/docs/api-reference/httpresponsebackends/get.md

# Source: https://ngrok.com/docs/api-reference/failoverbackends/get.md

# Source: https://ngrok.com/docs/api-reference/eventsubscriptions/get.md

# Source: https://ngrok.com/docs/api-reference/eventsources/get.md

# Source: https://ngrok.com/docs/api-reference/eventdestinations/get.md

# Source: https://ngrok.com/docs/api-reference/endpoints/get.md

# Source: https://ngrok.com/docs/api-reference/edgestls/get.md

# Source: https://ngrok.com/docs/api-reference/edgestcp/get.md

# Source: https://ngrok.com/docs/api-reference/edgeshttpsroutes/get.md

# Source: https://ngrok.com/docs/api-reference/edgeshttps/get.md

# Source: https://ngrok.com/docs/api-reference/edgeroutewebsockettcpconvertermodule/get.md

# Source: https://ngrok.com/docs/api-reference/edgeroutewebhookverificationmodule/get.md

# Source: https://ngrok.com/docs/api-reference/edgerouteuseragentfiltermodule/get.md

# Source: https://ngrok.com/docs/api-reference/edgeroutetrafficpolicymodule/get.md

# Source: https://ngrok.com/docs/api-reference/edgeroutesamlmodule/get.md

# Source: https://ngrok.com/docs/api-reference/edgerouteresponseheadersmodule/get.md

# Source: https://ngrok.com/docs/api-reference/edgerouterequestheadersmodule/get.md

# Source: https://ngrok.com/docs/api-reference/edgerouteoidcmodule/get.md

# Source: https://ngrok.com/docs/api-reference/edgerouteoauthmodule/get.md

# Source: https://ngrok.com/docs/api-reference/edgerouteiprestrictionmodule/get.md

# Source: https://ngrok.com/docs/api-reference/edgeroutecompressionmodule/get.md

# Source: https://ngrok.com/docs/api-reference/edgeroutecircuitbreakermodule/get.md

# Source: https://ngrok.com/docs/api-reference/edgeroutebackendmodule/get.md

# Source: https://ngrok.com/docs/api-reference/credentials/get.md

# Source: https://ngrok.com/docs/api-reference/certificateauthorities/get.md

# Source: https://ngrok.com/docs/api-reference/botusers/get.md

# Source: https://ngrok.com/docs/api-reference/applicationusers/get.md

# Source: https://ngrok.com/docs/api-reference/applicationsessions/get.md

# Source: https://ngrok.com/docs/api-reference/apikeys/get.md

# Source: https://ngrok.com/docs/api-reference/agentingresses/get.md

# Source: https://ngrok.com/docs/api-reference/abusereports/get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> Retrieve details about a specific abuse report by its unique identifier.

# Get



## OpenAPI

````yaml get /abuse_reports/{id}
openapi: 3.0.0
info:
  title: ngrok OpenAPI
  version: 1.0.0
servers:
  - url: https://api.ngrok.com
security:
  - authentication: []
paths:
  /abuse_reports/{id}:
    get:
      tags:
        - AbuseReports
      summary: Get
      description: |
        Get the detailed status of abuse report by ID.
      operationId: AbuseReportsGet
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
        '200':
          description: |
            Get the detailed status of abuse report by ID.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AbuseReport'
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
    AbuseReport:
      type: object
      properties:
        id:
          description: |
            ID of the abuse report
          type: string
        uri:
          description: |
            URI of the abuse report API resource
          type: string
        created_at:
          description: >
            timestamp that the abuse report record was created in RFC 3339
            format
          type: string
        urls:
          description: |
            a list of URLs containing suspected abusive content
          type: array
          items:
            type: string
        metadata:
          description: >
            arbitrary user-defined data about this abuse report. Optional, max
            4096 bytes.
          type: string
        status:
          description: >
            Indicates whether ngrok has processed the abuse report. one of
            `PENDING`, `PROCESSED`, or `PARTIALLY_PROCESSED`
          type: string
        hostnames:
          description: |
            an array of hostname statuses related to the report
          type: array
          items:
            $ref: '#/components/schemas/AbuseReportHostname'
    AbuseReportHostname:
      type: object
      properties:
        hostname:
          description: >
            the hostname ngrok has parsed out of one of the reported URLs in
            this abuse report
          type: string
        status:
          description: >
            indicates what action ngrok has taken against the hostname. one of
            `PENDING`, `BANNED`, `UNBANNED`, or `IGNORE`
          type: string
  securitySchemes:
    authentication:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).