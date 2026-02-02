# Source: https://docs.runpod.io/api-reference/container-registry-auths/GET/containerregistryauth/containerRegistryAuthId.md

# Source: https://docs.runpod.io/api-reference/container-registry-auths/DELETE/containerregistryauth/containerRegistryAuthId.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.runpod.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a container registry auth

> Delete a container registry auth.



## OpenAPI

````yaml DELETE /containerregistryauth/{containerRegistryAuthId}
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
  /containerregistryauth/{containerRegistryAuthId}:
    delete:
      tags:
        - container registry auths
      summary: Delete a container registry auth
      description: Delete a container registry auth.
      operationId: DeleteContainerRegistryAuth
      parameters:
        - name: containerRegistryAuthId
          in: path
          description: Container registry auth ID to delete.
          required: true
          schema:
            type: string
      responses:
        '204':
          description: Container registry auth successfully deleted.
        '400':
          description: Invalid container registry auth ID.
        '401':
          description: Unauthorized.
components:
  securitySchemes:
    ApiKey:
      type: http
      scheme: bearer
      bearerFormat: Bearer

````