# Source: https://upstash.com/docs/devops/developer-api/teams/delete_team_member.md

# Delete Team Member

> This endpoint deletes a team member from the specified team.

## OpenAPI

````yaml devops/developer-api/openapi.yml delete /teams/member
paths:
  path: /teams/member
  method: delete
  servers:
    - url: https://api.upstash.com/v2
  request:
    security:
      - title: basicAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: basic
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
              team_id:
                allOf:
                  - type: string
                    description: Id of the team to remove the member from
                    example: 95849b27-40d0-4532-8695-d2028847f823
              member_email:
                allOf:
                  - type: string
                    description: Email of the team member to remove
                    example: example@upstash.com
            required: true
            refIdentifier: '#/components/schemas/DeleteTeamMemberRequest'
            requiredProperties:
              - team_id
              - member_email
        examples:
          example:
            value:
              team_id: 95849b27-40d0-4532-8695-d2028847f823
              member_email: example@upstash.com
  response:
    '200':
      application/json:
        schemaArray:
          - type: string
            example: OK
        examples:
          example:
            value: OK
        description: Team member deleted successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/teams/delete_team_member
components:
  schemas: {}

````