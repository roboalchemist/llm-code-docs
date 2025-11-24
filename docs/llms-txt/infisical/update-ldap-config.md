# Source: https://infisical.com/docs/api-reference/endpoints/organizations/ldap-sso/update-ldap-config.md

# Update LDAP SSO Config

> Update LDAP config

## OpenAPI

````yaml PATCH /api/v1/ldap/config
paths:
  path: /api/v1/ldap/config
  method: patch
  servers:
    - url: https://us.infisical.com
      description: Production server (US)
    - url: https://eu.infisical.com
      description: Production server (EU)
    - url: http://localhost:8080
      description: Local server
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: An access token in Infisical
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              isActive:
                allOf:
                  - type: boolean
                    description: Whether to enable or disable this LDAP configuration.
              url:
                allOf:
                  - type: string
                    description: >-
                      The LDAP server to connect to such as
                      `ldap://ldap.your-org.com`, `ldaps://ldap.myorg.com:636`
                      (for connection over SSL/TLS), etc.
              bindDN:
                allOf:
                  - type: string
                    description: >-
                      The distinguished name of object to bind when performing
                      the user search such as
                      `cn=infisical,ou=Users,dc=acme,dc=com`
              bindPass:
                allOf:
                  - type: string
                    description: >-
                      The password to use along with Bind DN when performing the
                      user search.
              uniqueUserAttribute:
                allOf:
                  - type: string
                    description: >-
                      The attribute to use as the unique identifier of LDAP
                      users such as `sAMAccountName`, `cn`, `uid`, `objectGUID`.
                      If left blank, defaults to uidNumber
              searchBase:
                allOf:
                  - type: string
                    description: >-
                      The base DN to use for the user search such as
                      `ou=Users,dc=acme,dc=com`
              searchFilter:
                allOf:
                  - type: string
                    description: >-
                      The template used to construct the LDAP user search filter
                      such as `(uid={{username}})` uses literal `{{username}}`
                      to have the given username used in the search. The default
                      is `(uid={{username}})` which is compatible with several
                      common directory schemas.
              groupSearchBase:
                allOf:
                  - type: string
                    description: >-
                      LDAP search base to use for group membership search such
                      as `ou=Groups,dc=acme,dc=com`
              groupSearchFilter:
                allOf:
                  - type: string
                    description: >-
                      The template used when constructing the group membership
                      query such as
                      `(&(objectClass=posixGroup)(memberUid={{.Username}}))`.
                      The template can access the following context variables:
                      `[UserDN, UserName]`. The default is
                      `(|(memberUid={{.Username}})(member={{.UserDN}})(uniqueMember={{.UserDN}}))`
                      which is compatible with several common directory schemas.
              caCert:
                allOf:
                  - type: string
                    description: >-
                      The CA certificate to use when verifying the LDAP server
                      certificate.
              organizationId:
                allOf:
                  - type: string
                    description: The ID of the organization to update the LDAP config for.
            required: true
            requiredProperties:
              - organizationId
            additionalProperties: false
        examples:
          example:
            value:
              isActive: true
              url: <string>
              bindDN: <string>
              bindPass: <string>
              uniqueUserAttribute: <string>
              searchBase: <string>
              searchFilter: <string>
              groupSearchBase: <string>
              groupSearchFilter: <string>
              caCert: <string>
              organizationId: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              updatedAt:
                allOf:
                  - type: string
                    format: date-time
              createdAt:
                allOf:
                  - type: string
                    format: date-time
              isActive:
                allOf:
                  - type: boolean
              orgId:
                allOf:
                  - type: string
                    format: uuid
              id:
                allOf:
                  - type: string
                    format: uuid
              url:
                allOf:
                  - type: string
              searchBase:
                allOf:
                  - type: string
              searchFilter:
                allOf:
                  - type: string
                    default: ''
              groupSearchBase:
                allOf:
                  - type: string
                    default: ''
              uniqueUserAttribute:
                allOf:
                  - type: string
                    default: ''
              groupSearchFilter:
                allOf:
                  - type: string
                    default: ''
            requiredProperties:
              - updatedAt
              - createdAt
              - isActive
              - orgId
              - id
              - url
              - searchBase
            additionalProperties: false
        examples:
          example:
            value:
              updatedAt: '2023-11-07T05:31:56Z'
              createdAt: '2023-11-07T05:31:56Z'
              isActive: true
              orgId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              url: <string>
              searchBase: <string>
              searchFilter: ''
              groupSearchBase: ''
              uniqueUserAttribute: ''
              groupSearchFilter: ''
        description: Default Response
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 400
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 400
              message: <string>
              error: <string>
        description: Default Response
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 401
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 401
              message: <string>
              error: <string>
        description: Default Response
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 403
              message:
                allOf:
                  - type: string
              details:
                allOf:
                  - {}
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 403
              message: <string>
              details: <any>
              error: <string>
        description: Default Response
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 404
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 404
              message: <string>
              error: <string>
        description: Default Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 422
              message:
                allOf:
                  - {}
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 422
              message: <any>
              error: <string>
        description: Default Response
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 500
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 500
              message: <string>
              error: <string>
        description: Default Response
  deprecated: false
  type: path
components:
  schemas: {}

````