# Source: https://docs.runpod.io/api-reference/templates/POST/templates.md

# Source: https://docs.runpod.io/api-reference/templates/GET/templates.md

# Source: https://docs.runpod.io/api-reference/templates/POST/templates.md

# Source: https://docs.runpod.io/api-reference/templates/GET/templates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.runpod.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List templates

> Returns a list of templates.



## OpenAPI

````yaml GET /templates
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
  /templates:
    get:
      tags:
        - templates
      summary: List templates
      description: Returns a list of templates.
      operationId: ListTemplates
      parameters:
        - name: includeEndpointBoundTemplates
          in: query
          schema:
            type: boolean
            default: false
            example: true
            description: Include templates bound to Serverless endpoints in the response.
        - name: includePublicTemplates
          in: query
          schema:
            type: boolean
            default: false
            example: true
            description: Include community-made public templates in the response.
        - name: includeRunpodTemplates
          in: query
          schema:
            type: boolean
            default: false
            example: true
            description: Include official Runpod templates in the response.
      responses:
        '200':
          description: Successful operation.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Templates'
        '400':
          description: Invalid ID supplied.
        '404':
          description: Template not found.
components:
  schemas:
    Templates:
      type: array
      items:
        $ref: '#/components/schemas/Template'
    Template:
      type: object
      properties:
        category:
          type: string
          example: NVIDIA
          description: >-
            The category of the template. The category can be used to filter
            templates in the Runpod UI. Current categories are NVIDIA, AMD, and
            CPU.
        containerDiskInGb:
          type: integer
          example: 50
          description: >-
            The amount of disk space, in gigabytes (GB), to allocate on the
            container disk for a Pod or worker. The data on the container disk
            is wiped when the Pod or worker restarts. To persist data across
            restarts, set volumeInGb to configure the local network volume.
        containerRegistryAuthId:
          type: string
        dockerEntrypoint:
          type: array
          items:
            type: string
          example: []
          description: >-
            If specified, overrides the ENTRYPOINT for the Docker image run on a
            Pod or worker. If [], uses the ENTRYPOINT defined in the image.
        dockerStartCmd:
          type: array
          items:
            type: string
          example: []
          description: >-
            If specified, overrides the start CMD for the Docker image run on a
            Pod or worker. If [], uses the start CMD defined in the image.
        earned:
          type: number
          example: 100
          description: >-
            The amount of Runpod credits earned by the creator of a template by
            all Pods or workers created from the template.
        env:
          type: object
          items:
            type: string
          example:
            ENV_VAR: value
          default: {}
        id:
          type: string
          example: 30zmvf89kd
          description: A unique string identifying a template.
        imageName:
          type: string
          example: runpod/pytorch:2.1.0-py3.10-cuda11.8.0-devel-ubuntu22.04
          description: >-
            The image tag for the container run on Pods or workers created from
            a template.
        isPublic:
          type: boolean
          example: false
          description: >-
            Set to true if a template is public and can be used by any Runpod
            user. Set to false if a template is private and can only be used by
            the creator.
        isRunpod:
          type: boolean
          example: true
          description: If true, a template is an official template managed by Runpod.
        isServerless:
          type: boolean
          example: true
          description: >-
            If true, instances created from a template are Serverless workers.
            If false, instances created from a template are Pods.
        name:
          type: string
          example: my template
          description: A user-defined name for a template. The name needs to be unique.
        ports:
          type: array
          items:
            type: string
          example:
            - 8888/http
            - 22/tcp
          description: >-
            A list of ports exposed on a Pod or worker. Each port is formatted
            as [port number]/[protocol]. Protocol can be either http or tcp.
        readme:
          type: string
          description: >-
            A string of markdown-formatted text that describes a template. The
            readme is displayed in the Runpod UI when a user selects the
            template.
        runtimeInMin:
          type: integer
        volumeInGb:
          type: integer
          example: 20
          description: >-
            The amount of disk space, in gigabytes (GB), to allocate on the
            local network volume for a Pod or worker. The data on the local
            network volume is persisted across restarts. To persist data so that
            future Pods and workers can access it, create a network volume and
            set networkVolumeId to attach it to the Pod or worker.
        volumeMountPath:
          type: string
          example: /workspace
          description: >-
            If a local network volume or network volume is attached to a Pod or
            worker, the absolute path where the network volume is mounted in the
            filesystem.
  securitySchemes:
    ApiKey:
      type: http
      scheme: bearer
      bearerFormat: Bearer

````