# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/connect/list-secure-compute-networks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# List Secure Compute networks

> Allows to list Secure Compute networks.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/connect/networks
openapi: 3.0.3
info:
  title: Vercel REST API & SDK
  description: >-
    The [`@vercel/sdk`](https://www.npmjs.com/package/@vercel/sdk) is a
    type-safe Typescript SDK that allows you to access the resources and methods
    of the Vercel REST API. Learn how to [install
    it](https://vercel.com/docs/rest-api/sdk#installing-vercel-sdk) and
    [authenticate](https://vercel.com/docs/rest-api/sdk#authentication) with a
    Vercel access token.
  contact:
    email: support@vercel.com
    name: Vercel Support
    url: https://vercel.com/support
  version: 0.0.1
servers:
  - url: https://api.vercel.com
    description: Production API
security: []
paths:
  /v1/connect/networks:
    get:
      tags:
        - connect
      summary: List Secure Compute networks
      description: Allows to list Secure Compute networks.
      operationId: listNetworks
      parameters:
        - name: includeHostedZones
          description: Whether to include Hosted Zones in the response
          in: query
          schema:
            type: boolean
            description: Whether to include Hosted Zones in the response
            default: true
        - name: includePeeringConnections
          description: Whether to include VPC Peering connections in the response
          in: query
          schema:
            type: boolean
            description: Whether to include VPC Peering connections in the response
            default: true
        - name: includeProjects
          description: Whether to include projects in the response
          in: query
          schema:
            type: boolean
            description: Whether to include projects in the response
            default: true
        - name: search
          description: The query to use as a filter for returned networks
          in: query
          schema:
            type: string
            description: The query to use as a filter for returned networks
            maxLength: 255
        - description: The Team identifier to perform the request on behalf of.
          in: query
          name: teamId
          schema:
            type: string
            example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        - description: The Team slug to perform the request on behalf of.
          in: query
          name: slug
          schema:
            type: string
            example: my-team-url-slug
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                items:
                  $ref: '#/components/schemas/Network'
                type: array
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
      security:
        - bearerToken: []
components:
  schemas:
    Network:
      properties:
        awsAccountId:
          type: string
          description: The ID of the AWS Account in which the network exists.
        awsAvailabilityZoneIds:
          items:
            type: string
          type: array
          description: >-
            The IDs of the AWS Availability Zones in which the network exists,
            if specified during creation.
        awsRegion:
          type: string
          description: The AWS Region in which the network exists.
        cidr:
          type: string
          description: The CIDR range of the Network.
        createdAt:
          type: number
          description: >-
            The date at which the Network was created, represented as a UNIX
            timestamp since EPOCH.
        egressIpAddresses:
          items:
            type: string
          type: array
        hostedZones:
          properties:
            count:
              type: number
              description: >-
                The number of AWS Route53 Hosted Zones associated with the
                Network.
          required:
            - count
          type: object
          description: >-
            Metadata about any AWS Route53 Hosted Zones associated with the
            Network.
        id:
          type: string
          description: The unique identifier of the Network.
        name:
          type: string
          description: The name of the network.
        peeringConnections:
          properties:
            count:
              type: number
              description: >-
                The number of AWS Route53 Hosted Zones associated with the
                Network.
          required:
            - count
          type: object
          description: >-
            Metadata about any AWS Route53 Hosted Zones associated with the
            Network.
        projects:
          properties:
            count:
              type: number
            ids:
              items:
                type: string
              type: array
          required:
            - count
            - ids
          type: object
          description: Metadata about any projects associated with the Network.
        region:
          type: string
          description: The Vercel region in which the Network exists.
        status:
          type: string
          enum:
            - create_in_progress
            - delete_in_progress
            - error
            - ready
          description: The status of the Network.
        teamId:
          type: string
          description: The unique identifier of the Team that owns the Network.
        vpcId:
          type: string
          description: The ID of the VPC which hosts the network.
      required:
        - awsAccountId
        - awsRegion
        - cidr
        - createdAt
        - id
        - name
        - status
        - teamId
      type: object
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````