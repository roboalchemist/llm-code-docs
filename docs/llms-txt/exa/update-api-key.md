# Source: https://exa.ai/docs/reference/team-management/update-api-key.md

> ## Documentation Index

> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt

> Use this file to discover all available pages before exploring further.

# Update API Key

> Update the name and rate limit of an existing API key.

<Card title="Get your Exa API key" icon="key" horizontal href="https://dashboard.exa.ai/api-keys" />

## Overview

The Update API Key endpoint allows you to modify an existing API key

## Path Parameters

* **id**: The unique identifier of the API key to update (UUID format)

## Optional Parameters

* **name**: New descriptive name for the API key
* **rateLimit**: New rate limit in requests per minute


## OpenAPI

````yaml put /api-keys/{id}
openapi: 3.1.0
info:
  version: 1.0.0
  title: Team Management API
  description: >-
    API for managing API keys within teams. Provides CRUD operations for
    creating, listing, updating, and deleting API keys with team-based access
    controls.
servers:
  - url: https://admin-api.exa.ai/team-management
security:
  - apikey: []
paths:
  /api-keys/{id}:
    put:
      tags:
        - Team Management
      summary: Update API Key
      description: >-
        Updates an existing API key's name and/or rate limit. Only API keys
        belonging to the authenticated team can be updated.
      operationId: update-api-key
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
          description: The unique identifier of the API key to update
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: Optional new name for the API key
                  example: Updated Production Key
                rateLimit:
                  type: integer
                  description: Optional new rate limit for the API key
                  example: 2000
              additionalProperties: false
      responses:
        '200':
          description: API key updated successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  apiKey:
                    type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      name:
                        type: string
                      rateLimit:
                        type: integer
                        nullable: true
                      teamId:
                        type: string
                        format: uuid
                      userId:
                        type: string
                        format: uuid
                      createdAt:
                        type: string
                        format: date-time
                      updatedAt:
                        type: string
                        format: date-time
        '400':
          description: Bad Request - Invalid parameters
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    examples:
                      - api_key_id is required
                      - Invalid API key ID format. Must be a valid UUID.
        '401':
          description: Unauthorized - Invalid or missing service key
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Unauthorized
        '403':
          description: Forbidden - API key belongs to a different team
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: You do not have permission to access this API key
        '404':
          description: Not Found - API key does not exist
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: API key not found
      security:
        - apikey: []
components:
  securitySchemes:
    apikey:
      type: apiKey
      in: header
      name: x-api-key
      description: Service API key for team authentication

````