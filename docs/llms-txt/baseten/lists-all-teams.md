# Source: https://docs.baseten.co/reference/management-api/teams/lists-all-teams.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# List all teams

> Returns a list of all teams the authenticated user has access to.



## OpenAPI

````yaml get /v1/teams
openapi: 3.1.0
info:
  description: REST API for management of Baseten resources
  title: Baseten management API
  version: 1.0.0
servers:
  - url: https://api.baseten.co
security:
  - ApiKeyAuth: []
paths:
  /v1/teams:
    get:
      summary: Lists all teams
      description: Returns a list of all teams the authenticated user has access to.
      responses:
        '200':
          description: A list of teams.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TeamsV1'
components:
  schemas:
    TeamsV1:
      description: A list of teams.
      properties:
        teams:
          description: A list of teams
          items:
            $ref: '#/components/schemas/TeamV1'
          title: Teams
          type: array
      required:
        - teams
      title: TeamsV1
      type: object
    TeamV1:
      description: A team.
      properties:
        id:
          description: Unique identifier of the team
          title: Id
          type: string
        name:
          description: Name of the team
          title: Name
          type: string
        default:
          type: boolean
          description: Whether this is the default team for the organization
          title: Default
        created_at:
          description: Time the team was created in ISO 8601 format
          format: date-time
          title: Created At
          type: string
      required:
        - id
        - name
        - default
        - created_at
      title: TeamV1
      type: object
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Authorization
      description: >-
        You must specify the scheme 'Api-Key' in the Authorization header. For
        example, `Authorization: Api-Key <Your_Api_Key>`

````