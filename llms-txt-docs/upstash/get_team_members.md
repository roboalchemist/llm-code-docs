# Source: https://upstash.com/docs/devops/developer-api/teams/get_team_members.md

# Get Team Members

> This endpoint list all members of a team.

## OpenAPI

````yaml devops/developer-api/openapi.yml get /teams/{team_id}
paths:
  path: /teams/{team_id}
  method: get
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
      path:
        team_id:
          schema:
            - type: string
              required: true
              description: ID of the team
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/TeamMember'
        examples:
          example:
            value:
              - team_id: 3423cb72-e50d-43ec-a9c0-f0f359941223
                team_name: test_team_name_2
                member_email: example@upstash.com
                member_role: dev
                copy_cc: true
        description: Team members retrieved successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/teams/get_team_members
components:
  schemas:
    TeamMember:
      type: object
      properties:
        team_id:
          type: string
          description: ID of the team
          example: 3423cb72-e50d-43ec-a9c0-f0f359941223
        team_name:
          type: string
          description: Name of the team
          example: test_team_name_2
        member_email:
          type: string
          description: Email of the team member
          example: example@upstash.com
        member_role:
          type: string
          description: Role of the team member
          enum:
            - owner
            - admin
            - dev
            - finance
          example: dev
        copy_cc:
          type: boolean
          description: >-
            Whether to copy existing credit card information to team member or
            not
          example: true
      xml:
        name: teamMember

````