# Source: https://ngrok.com/docs/api-reference/weightedbackends/create.md

# Source: https://ngrok.com/docs/api-reference/vaults/create.md

# Source: https://ngrok.com/docs/api-reference/tunnelgroupbackends/create.md

# Source: https://ngrok.com/docs/api-reference/tlscertificates/create.md

# Source: https://ngrok.com/docs/api-reference/staticbackends/create.md

# Source: https://ngrok.com/docs/api-reference/sshusercertificates/create.md

# Source: https://ngrok.com/docs/api-reference/sshhostcertificates/create.md

# Source: https://ngrok.com/docs/api-reference/sshcredentials/create.md

# Source: https://ngrok.com/docs/api-reference/sshcertificateauthorities/create.md

# Source: https://ngrok.com/docs/api-reference/secrets/create.md

# Source: https://ngrok.com/docs/api-reference/reserveddomains/create.md

# Source: https://ngrok.com/docs/api-reference/reservedaddrs/create.md

# Source: https://ngrok.com/docs/api-reference/iprestrictions/create.md

# Source: https://ngrok.com/docs/api-reference/ippolicyrules/create.md

# Source: https://ngrok.com/docs/api-reference/ippolicies/create.md

# Source: https://ngrok.com/docs/api-reference/httpresponsebackends/create.md

# Source: https://ngrok.com/docs/api-reference/failoverbackends/create.md

# Source: https://ngrok.com/docs/api-reference/eventsubscriptions/create.md

# Source: https://ngrok.com/docs/api-reference/eventsources/create.md

# Source: https://ngrok.com/docs/api-reference/eventdestinations/create.md

# Source: https://ngrok.com/docs/api-reference/endpoints/create.md

# Source: https://ngrok.com/docs/api-reference/edgestls/create.md

# Source: https://ngrok.com/docs/api-reference/edgestcp/create.md

# Source: https://ngrok.com/docs/api-reference/edgeshttpsroutes/create.md

# Source: https://ngrok.com/docs/api-reference/edgeshttps/create.md

# Source: https://ngrok.com/docs/api-reference/credentials/create.md

# Source: https://ngrok.com/docs/api-reference/certificateauthorities/create.md

# Source: https://ngrok.com/docs/api-reference/botusers/create.md

# Source: https://ngrok.com/docs/api-reference/apikeys/create.md

# Source: https://ngrok.com/docs/api-reference/agentingresses/create.md

# Source: https://ngrok.com/docs/api-reference/abusereports/create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> Create a new abuse report to report suspicious or malicious activity on your ngrok endpoints.

# Create



## OpenAPI

````yaml post /abuse_reports
openapi: 3.0.0
info:
  title: ngrok OpenAPI
  version: 1.0.0
servers:
  - url: https://api.ngrok.com
security:
  - authentication: []
paths:
  /abuse_reports:
    post:
      tags:
        - AbuseReports
      summary: Create
      description: >
        Creates a new abuse report which will be reviewed by our system and
        abuse response team. This API is only available to authorized accounts.
        Contact abuse@ngrok.com to request access
      operationId: AbuseReportsCreate
      parameters:
        - $ref: '#/components/parameters/ngrokVersion'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AbuseReportCreate'
      responses:
        '201':
          description: >
            Creates a new abuse report which will be reviewed by our system and
            abuse response team. This API is only available to authorized
            accounts. Contact abuse@ngrok.com to request access
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
    AbuseReportCreate:
      type: object
      required:
        - urls
      properties:
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