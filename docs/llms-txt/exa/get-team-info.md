# Source: https://exa.ai/docs/websets/api/teams/get-team-info.md


> ## Documentation Index
>
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Team Info

> Retrieve information about your team including concurrency usage and limits.

## Overview

The Get Team Info endpoint returns information about the authenticated team, including the team's current concurrency usage and configured limits. This is useful for monitoring your Websets API usage and understanding your rate limits.

## Response

The response includes:

* **object**: Always "team"
* **id**: Your team's unique identifier
* **name**: Your team's name
* **concurrency**: Current usage showing active and queued requests
* **limits**: Your team's concurrency limits

### Concurrency Fields

The `concurrency` object shows your current request state:

* **active**: Number of requests currently being processed
* **queued**: Number of requests waiting to be processed

### Limits Fields

The `limits` object shows your team's configured limits:

* **maxConcurrent**: Maximum number of requests that can be processed simultaneously (null means unlimited)
* **maxQueued**: Maximum number of requests that can wait in the queue (null means unlimited)


## OpenAPI

````yaml websets-spec get /v0/teams/me
openapi: 3.1.0
info:
  title: Websets
  description: ''
  version: '0'
  contact: {}
servers:
  - url: https://api.exa.ai/websets/
    description: Production
security: []
tags: []
paths:
  /v0/teams/me:
    get:
      tags:
        - Teams
      summary: Get Team Info
      description: >-
        Returns information about the authenticated team, including current
        concurrency usage and limits.
      operationId: teams-me-get
      responses:
        '200':
          description: Team information retrieved successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  object:
                    type: string
                    example: team
                    description: The object type, always "team"
                  id:
                    type: string
                    description: Unique identifier for the team
                    example: team-abc123
                  name:
                    type: string
                    description: Name of the team
                    example: My Team
                  concurrency:
                    type: object
                    description: Current concurrency usage
                    properties:
                      active:
                        type: integer
                        description: Number of requests currently being processed
                        example: 5
                      queued:
                        type: integer
                        description: Number of requests currently queued
                        example: 2
                  limits:
                    type: object
                    description: Concurrency limits for the team
                    properties:
                      maxConcurrent:
                        type: integer
                        nullable: true
                        description: >-
                          Maximum number of concurrent requests allowed (null =
                          unlimited)
                        example: 10
                      maxQueued:
                        type: integer
                        nullable: true
                        description: >-
                          Maximum number of queued requests allowed (null =
                          unlimited)
                        example: 50
        '401':
          description: Unauthorized - Invalid or missing API key
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Unauthorized
      security:
        - api_key: []
components:
  securitySchemes:
    api_key:
      type: apiKey
      in: header
      name: x-api-key
      description: Your Exa API key

````