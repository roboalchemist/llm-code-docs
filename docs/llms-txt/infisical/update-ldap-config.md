# Source: https://infisical.com/docs/api-reference/endpoints/organizations/ldap-sso/update-ldap-config.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update LDAP SSO Config

> Update LDAP config



## OpenAPI

````yaml PATCH /api/v1/ldap/config
openapi: 3.0.3
info:
  title: Infisical API
  description: List of all available APIs that can be consumed
  version: 0.0.1
servers:
  - url: https://us.infisical.com
    description: Production server (US)
  - url: https://eu.infisical.com
    description: Production server (EU)
  - url: http://localhost:8080
    description: Local server
security: []
paths:
  /api/v1/ldap/config:
    patch:
      tags:
        - LDAP SSO
      description: Update LDAP config
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                isActive:
                  type: boolean
                  description: Whether to enable or disable this LDAP configuration.
                url:
                  type: string
                  description: >-
                    The LDAP server to connect to such as
                    `ldap://ldap.your-org.com`, `ldaps://ldap.myorg.com:636`
                    (for connection over SSL/TLS), etc.
                bindDN:
                  type: string
                  description: >-
                    The distinguished name of object to bind when performing the
                    user search such as `cn=infisical,ou=Users,dc=acme,dc=com`
                bindPass:
                  type: string
                  description: >-
                    The password to use along with Bind DN when performing the
                    user search.
                uniqueUserAttribute:
                  type: string
                  description: >-
                    The attribute to use as the unique identifier of LDAP users
                    such as `sAMAccountName`, `cn`, `uid`, `objectGUID`. If left
                    blank, defaults to uidNumber
                searchBase:
                  type: string
                  description: >-
                    The base DN to use for the user search such as
                    `ou=Users,dc=acme,dc=com`
                searchFilter:
                  type: string
                  description: >-
                    The template used to construct the LDAP user search filter
                    such as `(uid={{username}})` uses literal `{{username}}` to
                    have the given username used in the search. The default is
                    `(uid={{username}})` which is compatible with several common
                    directory schemas.
                groupSearchBase:
                  type: string
                  description: >-
                    LDAP search base to use for group membership search such as
                    `ou=Groups,dc=acme,dc=com`
                groupSearchFilter:
                  type: string
                  description: >-
                    The template used when constructing the group membership
                    query such as
                    `(&(objectClass=posixGroup)(memberUid={{.Username}}))`. The
                    template can access the following context variables:
                    `[UserDN, UserName]`. The default is
                    `(|(memberUid={{.Username}})(member={{.UserDN}})(uniqueMember={{.UserDN}}))`
                    which is compatible with several common directory schemas.
                caCert:
                  type: string
                  description: >-
                    The CA certificate to use when verifying the LDAP server
                    certificate.
                organizationId:
                  type: string
                  description: The ID of the organization to update the LDAP config for.
              required:
                - organizationId
              additionalProperties: false
        required: true
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  updatedAt:
                    type: string
                    format: date-time
                  createdAt:
                    type: string
                    format: date-time
                  isActive:
                    type: boolean
                  orgId:
                    type: string
                    format: uuid
                  id:
                    type: string
                    format: uuid
                  url:
                    type: string
                  searchBase:
                    type: string
                  searchFilter:
                    type: string
                    default: ''
                  groupSearchBase:
                    type: string
                    default: ''
                  uniqueUserAttribute:
                    type: string
                    default: ''
                  groupSearchFilter:
                    type: string
                    default: ''
                required:
                  - updatedAt
                  - createdAt
                  - isActive
                  - orgId
                  - id
                  - url
                  - searchBase
                additionalProperties: false
        '400':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 400
                  message:
                    type: string
                  error:
                    type: string
                  details: {}
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '401':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 401
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '403':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 403
                  message:
                    type: string
                  details: {}
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '404':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 404
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '422':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 422
                  message: {}
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - error
                additionalProperties: false
        '500':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 500
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
      security:
        - bearerAuth: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: An access token in Infisical

````