# Source: https://upstash.com/docs/devops/developer-api/teams/add_team_member.md

# Add Team Member

> This endpoint adds a new team member to the specified team.

## OpenAPI

````yaml devops/developer-api/openapi.yml post /teams/member
paths:
  path: /teams/member
  method: post
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
                    description: Id of the team to add the member to
                    example: 95849b27-40d0-4532-8695-d2028847f823
              member_email:
                allOf:
                  - type: string
                    description: Email of the new team member
                    example: example@upstash.com
              member_role:
                allOf:
                  - type: string
                    description: Role of the new team member
                    enum:
                      - admin
                      - dev
                      - finance
                    example: dev
            required: true
            refIdentifier: '#/components/schemas/AddTeamMemberRequest'
            requiredProperties:
              - team_id
              - member_email
              - member_role
        examples:
          example:
            value:
              team_id: 95849b27-40d0-4532-8695-d2028847f823
              member_email: example@upstash.com
              member_role: dev
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              team_id:
                allOf:
                  - type: string
                    description: ID of the team
                    example: 3423cb72-e50d-43ec-a9c0-f0f359941223
              team_name:
                allOf:
                  - type: string
                    description: Name of the team
                    example: test_team_name_2
              member_email:
                allOf:
                  - type: string
                    description: Email of the team member
                    example: example@upstash.com
              member_role:
                allOf:
                  - type: string
                    description: Role of the team member
                    enum:
                      - owner
                      - admin
                      - dev
                      - finance
                    example: dev
              copy_cc:
                allOf:
                  - type: boolean
                    description: >-
                      Whether to copy existing credit card information to team
                      member or not
                    example: true
            refIdentifier: '#/components/schemas/TeamMember'
        examples:
          example:
            value:
              team_id: 3423cb72-e50d-43ec-a9c0-f0f359941223
              team_name: test_team_name_2
              member_email: example@upstash.com
              member_role: dev
              copy_cc: true
        description: Team member added successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/teams/add_team_member
components:
  schemas: {}

````