# Source: https://docs.runpod.io/api-reference/container-registry-auths/POST/containerregistryauth.md

# Source: https://docs.runpod.io/api-reference/container-registry-auths/GET/containerregistryauth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.runpod.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List container registry auths

> Returns a list of container registry auths.



## OpenAPI

````yaml GET /containerregistryauth
openapi: 3.0.3
info:
  title: Runpod API
  description: Public Rest API for managing Runpod programmatically.
  version: 0.1.0
  contact:
    name: help
    url: https://contact.runpod.io/hc/requests/new
    email: help@runpod.io
servers:
  - url: https://rest.runpod.io/v1
security:
  - ApiKey: []
tags:
  - name: docs
    description: This documentation page.
  - name: pods
    description: Manage Pods.
  - name: endpoints
    description: Manage Serverless endpoints.
  - name: network volumes
    description: Manage Runpod network volumes.
  - name: templates
    description: Manage Pod and Serverless templates.
  - name: container registry auths
    description: >-
      Manage authentication for container registries such as dockerhub to use
      private images.
  - name: billing
    description: Retrieve billing history for your Runpod account.
externalDocs:
  description: Find out more about Runpod.
  url: https://runpod.io
paths:
  /containerregistryauth:
    get:
      tags:
        - container registry auths
      summary: List container registry auths
      description: Returns a list of container registry auths.
      operationId: ListContainerRegistryAuths
      responses:
        '200':
          description: Successful operation.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ContainerRegistryAuths'
        '400':
          description: Invalid ID supplied.
        '404':
          description: Container registry auth not found.
components:
  schemas:
    ContainerRegistryAuths:
      type: array
      items:
        $ref: '#/components/schemas/ContainerRegistryAuth'
    ContainerRegistryAuth:
      type: object
      properties:
        id:
          type: string
          example: clzdaifot0001l90809257ynb
          description: A unique string identifying a container registry authentication.
        name:
          type: string
          example: my creds
          description: >-
            A user-defined name for a container registry authentication. The
            name must be unique.
  securitySchemes:
    ApiKey:
      type: http
      scheme: bearer
      bearerFormat: Bearer

````