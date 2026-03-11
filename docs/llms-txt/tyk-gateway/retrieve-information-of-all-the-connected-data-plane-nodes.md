# Source: https://tyk.io/docs/api-reference/data-planes/retrieve-information-of-all-the-connected-data-plane-nodes.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve information of all the connected data plane nodes

> Provides a list of all the data plane nodes connected to MDCB. Data plane nodes are Tyk Gateways that make your APIs available to your consumers. MDCB offers centralised management of your data plane nodes. This endpoint offers metadata and status for all connected data plane nodes, allowing for monitoring and troubleshooting.

## OpenAPI

````yaml swagger/5.8/mdcb-swagger.yml get /dataplanes
openapi: 3.0.0
info:
  contact:
    email: support@tyk.io
    name: Tyk Technologies
    url: https://tyk.io/contact
  version: 1.0.0
  title: MDCB Data Planes and Diagnostics API
  description: >
    This API provides operations for monitoring Data Planes connected to MDCB
    and accessing diagnostic data.  It includes endpoints for retrieving
    connected data plane details, performing health checks,  and accessing Go's
    built-in pprof diagnostics for advanced performance profiling.
servers:
  - url: https://{tenant}
    variables:
      tenant:
        default: localhost:8181
        description: Your MDCB host
security:
  - api_key: []
tags:
  - name: Data Planes
    description: Operations related to data plane management and information
  - name: Health
    description: Endpoints for checking system health and status
  - name: Debug
    description: Diagnostic and profiling endpoints
  - name: Configuration
    description: Configuration and environment variable management
paths:
  /dataplanes:
    get:
      tags:
        - Data Planes
      summary: Retrieve information of all the connected data plane nodes.
      description: >-
        Provides a list of all the data plane nodes connected to MDCB. Data
        plane nodes are Tyk Gateways that make your APIs available to your
        consumers. MDCB offers centralised management of your data plane nodes.
        This endpoint offers metadata and status for all connected data plane
        nodes, allowing for monitoring and troubleshooting.
      operationId: dataplanesGet
      parameters:
        - in: header
          name: x-tyk-authorization
          description: Secret value set in sink.conf
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful retrieval of the connected data planes.
          content:
            application/json:
              schema:
                type: object
                additionalProperties:
                  type: array
                  items:
                    $ref: '#/components/schemas/Node'
        '401':
          description: Forbidden access due to invalid or missing administrative key.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    Node:
      type: object
      properties:
        node_id:
          type: string
          example: solo-uid
        api_key:
          type: string
          example: c5e9b9ed8dee42fb668f81cef7f905bb
        group_id:
          type: string
          example: Redis Cluster Slave 1
        node_version:
          type: string
          example: v5.3.0-dev
        ttl:
          type: integer
          example: 10
        tags:
          type: array
          items:
            type: string
          example:
            - tag1
            - tag2
        health:
          $ref: '#/components/schemas/Health'
        stats:
          $ref: '#/components/schemas/Stats'
        host_details:
          $ref: '#/components/schemas/HostDetails'
    Error:
      type: object
      properties:
        error:
          type: string
          example: Attempted administrative access with invalid or missing key!
    Health:
      type: object
      properties:
        redis:
          $ref: '#/components/schemas/ComponentStatus'
        rpc:
          $ref: '#/components/schemas/ComponentStatus'
    Stats:
      type: object
      properties:
        apis_count:
          type: integer
          example: 1
        policies_count:
          type: integer
          example: 0
    HostDetails:
      type: object
      properties:
        Hostname:
          type: string
          example: Peter-MacBook-Pro.local
        PID:
          type: integer
          example: 62663
        Address:
          type: string
          example: 203.0.113.0
    ComponentStatus:
      type: object
      properties:
        status:
          type: string
          example: pass
        componentType:
          type: string
          example: datastore
        time:
          type: string
          format: date-time
          example: '2024-02-23T08:51:23-03:00'
  securitySchemes:
    api_key:
      in: header
      name: X-Tyk-Authorization
      type: apiKey

````

Built with [Mintlify](https://mintlify.com).
