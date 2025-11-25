# Source: https://docs.comfy.org/api-reference/registry/publish-a-new-version-of-a-node.md

# Publish a new version of a node

## OpenAPI

````yaml https://api.comfy.org/openapi post /publishers/{publisherId}/nodes/{nodeId}/versions
paths:
  path: /publishers/{publisherId}/nodes/{nodeId}/versions
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
        nodeId:
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
              node:
                allOf:
                  - $ref: '#/components/schemas/Node'
              node_version:
                allOf:
                  - $ref: '#/components/schemas/NodeVersion'
              personal_access_token:
                allOf:
                  - type: string
            required: true
            requiredProperties:
              - node
              - node_version
              - personal_access_token
        examples:
          example:
            value:
              node:
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
              node_version:
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
              personal_access_token: <string>
  response:
    '201':
      application/json:
        schemaArray:
          - type: object
            properties:
              node_version:
                allOf:
                  - $ref: '#/components/schemas/NodeVersion'
              signedUrl:
                allOf:
                  - description: The signed URL to upload the node version token.
                    type: string
        examples:
          example:
            value:
              node_version:
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
              signedUrl: <string>
        description: New version published successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: string
              message:
                allOf:
                  - &ref_1
                    type: string
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: &ref_2
              - error
              - message
        examples:
          example:
            value:
              error: <string>
              message: <string>
        description: Bad request, invalid input data.
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
              message:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_2
        examples:
          example:
            value:
              error: <string>
              message: <string>
        description: Forbidden
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
              message:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_2
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
    Node:
      properties:
        author:
          type: string
        banner_url:
          description: URL to the node's banner.
          type: string
        category:
          deprecated: true
          description: >-
            DEPRECATED: The category of the node. Use 'tags' field instead. This
            field will be removed in a future version.
          type: string
        created_at:
          description: The date and time when the node was created
          format: date-time
          type: string
        description:
          type: string
        downloads:
          description: The number of downloads of the node.
          type: integer
        github_stars:
          description: Number of stars on the GitHub repository.
          type: integer
        icon:
          description: URL to the node's icon.
          type: string
        id:
          description: The unique identifier of the node.
          type: string
        latest_version:
          $ref: '#/components/schemas/NodeVersion'
        license:
          description: The path to the LICENSE file in the node's repository.
          type: string
        name:
          description: The display name of the node.
          type: string
        preempted_comfy_node_names:
          description: A list of Comfy node names that are preempted by this node.
          items:
            type: string
          type: array
        publisher:
          $ref: '#/components/schemas/Publisher'
        rating:
          description: The average rating of the node.
          type: number
        repository:
          description: URL to the node's repository.
          type: string
        search_ranking:
          description: >-
            A numerical value representing the node's search ranking, used for
            sorting search results.
          type: integer
        status:
          $ref: '#/components/schemas/NodeStatus'
        status_detail:
          description: The status detail of the node.
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
        translations:
          additionalProperties:
            additionalProperties: true
            type: object
          description: Translations of node metadata in different languages.
          type: object
      type: object
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