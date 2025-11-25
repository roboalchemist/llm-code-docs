# Source: https://docs.comfy.org/api-reference/registry/create-a-new-custom-node.md

# Create a new custom node

## OpenAPI

````yaml https://api.comfy.org/openapi post /publishers/{publisherId}/nodes
paths:
  path: /publishers/{publisherId}/nodes
  method: post
  servers:
    - url: https://api.comfy.org
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path:
        publisherId:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              author:
                allOf:
                  - &ref_0
                    type: string
              banner_url:
                allOf:
                  - &ref_1
                    description: URL to the node's banner.
                    type: string
              category:
                allOf:
                  - &ref_2
                    deprecated: true
                    description: >-
                      DEPRECATED: The category of the node. Use 'tags' field
                      instead. This field will be removed in a future version.
                    type: string
              created_at:
                allOf:
                  - &ref_3
                    description: The date and time when the node was created
                    format: date-time
                    type: string
              description:
                allOf:
                  - &ref_4
                    type: string
              downloads:
                allOf:
                  - &ref_5
                    description: The number of downloads of the node.
                    type: integer
              github_stars:
                allOf:
                  - &ref_6
                    description: Number of stars on the GitHub repository.
                    type: integer
              icon:
                allOf:
                  - &ref_7
                    description: URL to the node's icon.
                    type: string
              id:
                allOf:
                  - &ref_8
                    description: The unique identifier of the node.
                    type: string
              latest_version:
                allOf:
                  - &ref_9
                    $ref: '#/components/schemas/NodeVersion'
              license:
                allOf:
                  - &ref_10
                    description: The path to the LICENSE file in the node's repository.
                    type: string
              name:
                allOf:
                  - &ref_11
                    description: The display name of the node.
                    type: string
              preempted_comfy_node_names:
                allOf:
                  - &ref_12
                    description: >-
                      A list of Comfy node names that are preempted by this
                      node.
                    items:
                      type: string
                    type: array
              publisher:
                allOf:
                  - &ref_13
                    $ref: '#/components/schemas/Publisher'
              rating:
                allOf:
                  - &ref_14
                    description: The average rating of the node.
                    type: number
              repository:
                allOf:
                  - &ref_15
                    description: URL to the node's repository.
                    type: string
              search_ranking:
                allOf:
                  - &ref_16
                    description: >-
                      A numerical value representing the node's search ranking,
                      used for sorting search results.
                    type: integer
              status:
                allOf:
                  - &ref_17
                    $ref: '#/components/schemas/NodeStatus'
              status_detail:
                allOf:
                  - &ref_18
                    description: The status detail of the node.
                    type: string
              supported_accelerators:
                allOf:
                  - &ref_19
                    description: >-
                      List of accelerators (e.g. CUDA, DirectML, ROCm) that this
                      node supports
                    items:
                      type: string
                    type: array
              supported_comfyui_frontend_version:
                allOf:
                  - &ref_20
                    description: Supported versions of ComfyUI frontend
                    type: string
              supported_comfyui_version:
                allOf:
                  - &ref_21
                    description: Supported versions of ComfyUI
                    type: string
              supported_os:
                allOf:
                  - &ref_22
                    description: List of operating systems that this node supports
                    items:
                      type: string
                    type: array
              tags:
                allOf:
                  - &ref_23
                    items:
                      type: string
                    type: array
              tags_admin:
                allOf:
                  - &ref_24
                    description: Admin-only tags for security warnings and admin metadata
                    items:
                      type: string
                    type: array
              translations:
                allOf:
                  - &ref_25
                    additionalProperties:
                      additionalProperties: true
                      type: object
                    description: Translations of node metadata in different languages.
                    type: object
            required: true
            refIdentifier: '#/components/schemas/Node'
        examples:
          example:
            value:
              author: <string>
              banner_url: <string>
              category: <string>
              created_at: '2023-11-07T05:31:56Z'
              description: <string>
              downloads: 123
              github_stars: 123
              icon: <string>
              id: <string>
              latest_version:
                changelog: <string>
                comfy_node_extract_status: <string>
                createdAt: '2023-11-07T05:31:56Z'
                dependencies:
                  - <string>
                deprecated: true
                downloadUrl: <string>
                id: <string>
                node_id: <string>
                status: NodeVersionStatusActive
                status_reason: <string>
                supported_accelerators:
                  - <string>
                supported_comfyui_frontend_version: <string>
                supported_comfyui_version: <string>
                supported_os:
                  - <string>
                tags:
                  - <string>
                tags_admin:
                  - <string>
                version: <string>
              license: <string>
              name: <string>
              preempted_comfy_node_names:
                - <string>
              publisher:
                createdAt: '2023-11-07T05:31:56Z'
                description: <string>
                id: <string>
                logo: <string>
                members:
                  - id: <string>
                    role: <string>
                    user:
                      email: <string>
                      id: <string>
                      name: <string>
                name: <string>
                source_code_repo: <string>
                status: PublisherStatusActive
                support: <string>
                website: <string>
              rating: 123
              repository: <string>
              search_ranking: 123
              status: NodeStatusActive
              status_detail: <string>
              supported_accelerators:
                - <string>
              supported_comfyui_frontend_version: <string>
              supported_comfyui_version: <string>
              supported_os:
                - <string>
              tags:
                - <string>
              tags_admin:
                - <string>
              translations: {}
  response:
    '201':
      application/json:
        schemaArray:
          - type: object
            properties:
              author:
                allOf:
                  - *ref_0
              banner_url:
                allOf:
                  - *ref_1
              category:
                allOf:
                  - *ref_2
              created_at:
                allOf:
                  - *ref_3
              description:
                allOf:
                  - *ref_4
              downloads:
                allOf:
                  - *ref_5
              github_stars:
                allOf:
                  - *ref_6
              icon:
                allOf:
                  - *ref_7
              id:
                allOf:
                  - *ref_8
              latest_version:
                allOf:
                  - *ref_9
              license:
                allOf:
                  - *ref_10
              name:
                allOf:
                  - *ref_11
              preempted_comfy_node_names:
                allOf:
                  - *ref_12
              publisher:
                allOf:
                  - *ref_13
              rating:
                allOf:
                  - *ref_14
              repository:
                allOf:
                  - *ref_15
              search_ranking:
                allOf:
                  - *ref_16
              status:
                allOf:
                  - *ref_17
              status_detail:
                allOf:
                  - *ref_18
              supported_accelerators:
                allOf:
                  - *ref_19
              supported_comfyui_frontend_version:
                allOf:
                  - *ref_20
              supported_comfyui_version:
                allOf:
                  - *ref_21
              supported_os:
                allOf:
                  - *ref_22
              tags:
                allOf:
                  - *ref_23
              tags_admin:
                allOf:
                  - *ref_24
              translations:
                allOf:
                  - *ref_25
            refIdentifier: '#/components/schemas/Node'
        examples:
          example:
            value:
              author: <string>
              banner_url: <string>
              category: <string>
              created_at: '2023-11-07T05:31:56Z'
              description: <string>
              downloads: 123
              github_stars: 123
              icon: <string>
              id: <string>
              latest_version:
                changelog: <string>
                comfy_node_extract_status: <string>
                createdAt: '2023-11-07T05:31:56Z'
                dependencies:
                  - <string>
                deprecated: true
                downloadUrl: <string>
                id: <string>
                node_id: <string>
                status: NodeVersionStatusActive
                status_reason: <string>
                supported_accelerators:
                  - <string>
                supported_comfyui_frontend_version: <string>
                supported_comfyui_version: <string>
                supported_os:
                  - <string>
                tags:
                  - <string>
                tags_admin:
                  - <string>
                version: <string>
              license: <string>
              name: <string>
              preempted_comfy_node_names:
                - <string>
              publisher:
                createdAt: '2023-11-07T05:31:56Z'
                description: <string>
                id: <string>
                logo: <string>
                members:
                  - id: <string>
                    role: <string>
                    user:
                      email: <string>
                      id: <string>
                      name: <string>
                name: <string>
                source_code_repo: <string>
                status: PublisherStatusActive
                support: <string>
                website: <string>
              rating: 123
              repository: <string>
              search_ranking: 123
              status: NodeStatusActive
              status_detail: <string>
              supported_accelerators:
                - <string>
              supported_comfyui_frontend_version: <string>
              supported_comfyui_version: <string>
              supported_os:
                - <string>
              tags:
                - <string>
              tags_admin:
                - <string>
              translations: {}
        description: Node created successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_26
                    type: string
              message:
                allOf:
                  - &ref_27
                    type: string
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: &ref_28
              - error
              - message
        examples:
          example:
            value:
              error: <string>
              message: <string>
        description: Bad request, invalid input data.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Unauthorized
        examples: {}
        description: Unauthorized
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_26
              message:
                allOf:
                  - *ref_27
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_28
        examples:
          example:
            value:
              error: <string>
              message: <string>
        description: Internal server error
  deprecated: false
  type: path
components:
  schemas:
    NodeStatus:
      enum:
        - NodeStatusActive
        - NodeStatusDeleted
        - NodeStatusBanned
      type: string
    NodeVersion:
      properties:
        changelog:
          description: Summary of changes made in this version
          type: string
        comfy_node_extract_status:
          description: The status of comfy node extraction process.
          type: string
        createdAt:
          description: The date and time the version was created.
          format: date-time
          type: string
        dependencies:
          description: A list of pip dependencies required by the node.
          items:
            type: string
          type: array
        deprecated:
          description: Indicates if this version is deprecated.
          type: boolean
        downloadUrl:
          description: '[Output Only] URL to download this version of the node'
          type: string
        id:
          type: string
        node_id:
          description: The unique identifier of the node.
          type: string
        status:
          $ref: '#/components/schemas/NodeVersionStatus'
        status_reason:
          type: string
        supported_accelerators:
          description: >-
            List of accelerators (e.g. CUDA, DirectML, ROCm) that this node
            supports
          items:
            type: string
          type: array
        supported_comfyui_frontend_version:
          description: Supported versions of ComfyUI frontend
          type: string
        supported_comfyui_version:
          description: Supported versions of ComfyUI
          type: string
        supported_os:
          description: List of operating systems that this node supports
          items:
            type: string
          type: array
        tags:
          items:
            type: string
          type: array
        tags_admin:
          description: Admin-only tags for security warnings and admin metadata
          items:
            type: string
          type: array
        version:
          description: >-
            The version identifier, following semantic versioning. Must be
            unique for the node.
          type: string
      type: object
    NodeVersionStatus:
      enum:
        - NodeVersionStatusActive
        - NodeVersionStatusDeleted
        - NodeVersionStatusBanned
        - NodeVersionStatusPending
        - NodeVersionStatusFlagged
      type: string
    Publisher:
      properties:
        createdAt:
          description: The date and time the publisher was created.
          format: date-time
          type: string
        description:
          type: string
        id:
          description: >-
            The unique identifier for the publisher. It's akin to a username.
            Should be lowercase.
          type: string
        logo:
          description: URL to the publisher's logo.
          type: string
        members:
          description: A list of members in the publisher.
          items:
            $ref: '#/components/schemas/PublisherMember'
          type: array
        name:
          type: string
        source_code_repo:
          type: string
        status:
          $ref: '#/components/schemas/PublisherStatus'
        support:
          type: string
        website:
          type: string
      type: object
    PublisherMember:
      properties:
        id:
          description: The unique identifier for the publisher member.
          type: string
        role:
          description: The role of the user in the publisher.
          type: string
        user:
          $ref: '#/components/schemas/PublisherUser'
      type: object
    PublisherStatus:
      enum:
        - PublisherStatusActive
        - PublisherStatusBanned
      type: string
    PublisherUser:
      properties:
        email:
          description: The email address for this user.
          type: string
        id:
          description: The unique id for this user.
          type: string
        name:
          description: The name for this user.
          type: string
      type: object

````