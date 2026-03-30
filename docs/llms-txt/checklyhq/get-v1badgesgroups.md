# Source: https://checklyhq.com/docs/api-reference/badges/get-v1badgesgroups.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get badge for a group

> Get group status badge. You can enable the badges feature in [account settings](https://app.checklyhq.com/settings/account/general)



## OpenAPI

````yaml get /v1/badges/groups/{groupId}
openapi: 3.0.0
info:
  title: Checkly Public API
  version: v1
  description: >-
    These are the docs for the newly released Checkly Public API. If you have
    any questions, please do not hesitate to get in touch with us.
servers:
  - url: https://api.checklyhq.com
security:
  - Bearer: []
tags: []
paths:
  /v1/badges/groups/{groupId}:
    get:
      tags:
        - Badges
      description: >-
        Get group status badge. You can enable the badges feature in [account
        settings](https://app.checklyhq.com/settings/account/general)
      operationId: getV1BadgesGroupsGroupid
      parameters:
        - name: groupId
          in: path
          schema:
            type: integer
            x-constraint:
              sign: positive
          required: true
        - name: style
          in: query
          schema:
            type: string
            default: flat
            enum:
              - flat
              - plastic
              - flat-square
              - for-the-badge
              - social
        - name: theme
          in: query
          schema:
            type: string
            default: default
            enum:
              - light
              - dark
              - default
        - name: responseTime
          in: query
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                type: string
                pattern: (<svg)([^<]*|[^>]*)
components:
  securitySchemes:
    Bearer:
      type: http
      scheme: bearer
      bearerFormat: Bearer
      description: >-
        The Checkly Public API uses API keys to authenticate requests. You can
        get the API Key
        [here](https://app.checklyhq.com/settings/user/api-keys). Your API key
        is like a password:  keep it secure!

        Authentication to the API is performed using the Bearer auth method in
        the Authorization header and using the account ID.

        For example, set **Authorization** header while using cURL: `curl -H
        "Authorization: Bearer [apiKey]" "X-Checkly-Account: [accountId]"` 

````

Built with [Mintlify](https://mintlify.com).