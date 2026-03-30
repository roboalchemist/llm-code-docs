# Source: https://docs.xano.com/xano-features/metadata-api/instance_api/replace_workspace_content_and_configuration_with_imported_archive.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Replace workspace content and configuration with imported archive

> If the file is encrypted, the correct `password` is required to decrypt.



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_instance.json post /workspace/{workspace_id}/import
openapi: 3.0.0
info:
  title: Xano Metadata API (beta)
  description: >-
    The <a href="https://docs.xano.com/xano-features/metadata-api"
    target="_blank">Metadata API</a>

    is currently in <strong>beta</strong> and is the next
      evolution of the Developer API. It provides support
    to programatically manage your Xano instance and uses Access Tokens to

    control access.
  version: 0.0.1
servers:
  - url: https://x8ki-letl-twmt.n7.xano.io/api:meta
security: []
paths:
  /workspace/{workspace_id}/import:
    post:
      tags:
        - workspace
      summary: Replace workspace content and configuration with imported archive
      description: |-
        If the file is encrypted, the correct `password` is required to decrypt.
        <br /><br />
        <b>Required API Scope:</b>
        Instance Workspace: Update
      parameters:
        - name: workspace_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                password:
                  type: string
                  description: ''
                file:
                  type: string
                  format: binary
                  description: ''
              required:
                - file
      responses:
        '200':
          description: Success!
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                    format: int64
                    description: ''
                  name:
                    type: string
                    description: ''
                  description:
                    type: string
                    description: ''
                  branch:
                    type: object
                    properties:
                      id:
                        type: integer
                        format: int64
                        description: ''
                      created_at:
                        type: string
                        format: timestamptz
                        description: ''
                      updated_at:
                        type: string
                        format: timestamptz
                        description: ''
                      description:
                        type: string
                        description: ''
                      label:
                        type: string
                        description: ''
                        nullable: true
                      backup:
                        type: boolean
                        description: ''
                      color:
                        type: string
                        description: ''
                        default: '#ebc346'
                      parent_id:
                        type: integer
                        format: int64
                        description: ''
                      guid:
                        type: string
                        description: ''
                      is_service:
                        type: boolean
                        description: ''
                        nullable: true
                      workspace:
                        type: object
                        properties:
                          id:
                            type: integer
                            format: int64
                            description: ''
                      user:
                        type: object
                        properties:
                          id:
                            type: integer
                            format: int64
                            description: ''
                          name:
                            type: string
                            description: ''
                          email:
                            type: string
                            description: ''
                            format: email
                      history:
                        type: object
                        properties:
                          function_enabled:
                            type: boolean
                            description: ''
                          function_limit:
                            type: integer
                            format: int64
                            description: ''
                            default: 100
                          middleware_enabled:
                            type: boolean
                            description: ''
                          middleware_limit:
                            type: integer
                            format: int64
                            description: ''
                            default: 100
                          query_enabled:
                            type: boolean
                            description: ''
                            default: true
                          query_limit:
                            type: integer
                            format: int64
                            description: ''
                            default: 100
                          task_enabled:
                            type: boolean
                            description: ''
                            default: true
                          task_limit:
                            type: integer
                            format: int64
                            description: ''
                            default: 100
                          tool_enabled:
                            type: boolean
                            description: ''
                            default: true
                          tool_limit:
                            type: integer
                            format: int64
                            description: ''
                            default: 100
                          trigger_enabled:
                            type: boolean
                            description: ''
                          trigger_limit:
                            type: integer
                            format: int64
                            description: ''
                            default: 100
                      middleware:
                        type: object
                        properties:
                          function_pre:
                            type: array
                            items:
                              type: object
                              properties:
                                name:
                                  type: string
                                  description: ''
                                as:
                                  type: string
                                  description: ''
                                context:
                                  type: object
                                  description: ''
                                description:
                                  type: string
                                  description: ''
                                disabled:
                                  type: boolean
                                  description: ''
                                mocks:
                                  type: object
                                  description: ''
                                _xsid:
                                  type: string
                                  description: ''
                                input:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: ''
                                      value:
                                        type: string
                                        description: ''
                                      tag:
                                        type: string
                                        description: ''
                                        enum:
                                          - const
                                          - const:encoded
                                          - const:int
                                          - const:decimal
                                          - const:bool
                                          - const:array
                                          - const:epochms
                                          - const:obj
                                          - const:null
                                          - const:expr
                                          - const:expr:encoded
                                          - const:expr2
                                          - const:expr2:encoded
                                          - input
                                          - reg
                                          - var
                                          - auth
                                          - env
                                          - setting
                                          - col
                                          - output
                                          - response
                                          - trycatch
                                          - toolset
                                          - use_default
                                        default: input
                                      ignore:
                                        type: boolean
                                        description: ''
                                      expand:
                                        type: boolean
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            description: ''
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      filters:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            disabled:
                                              type: boolean
                                              description: ''
                                            arg:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                settings_registry:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: ''
                                      value:
                                        type: string
                                        description: ''
                                      tag:
                                        type: string
                                        description: ''
                                        enum:
                                          - const
                                          - const:encoded
                                          - const:int
                                          - const:decimal
                                          - const:bool
                                          - const:array
                                          - const:epochms
                                          - const:obj
                                          - const:null
                                          - const:expr
                                          - const:expr:encoded
                                          - const:expr2
                                          - const:expr2:encoded
                                          - input
                                          - reg
                                          - var
                                          - auth
                                          - env
                                          - setting
                                          - col
                                          - output
                                          - response
                                          - trycatch
                                          - toolset
                                          - use_default
                                        default: input
                                      ignore:
                                        type: boolean
                                        description: ''
                                      expand:
                                        type: boolean
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            description: ''
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      filters:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            disabled:
                                              type: boolean
                                              description: ''
                                            arg:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                  nullable: true
                                output:
                                  type: object
                                  properties:
                                    customize:
                                      type: boolean
                                      description: ''
                                    filters:
                                      type: array
                                      items:
                                        type: object
                                        properties:
                                          name:
                                            type: string
                                            description: ''
                                          disabled:
                                            type: boolean
                                            description: ''
                                          arg:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                value:
                                                  type: string
                                                  description: ''
                                                tag:
                                                  type: string
                                                  description: ''
                                                  enum:
                                                    - const
                                                    - const:encoded
                                                    - const:int
                                                    - const:decimal
                                                    - const:bool
                                                    - const:array
                                                    - const:epochms
                                                    - const:obj
                                                    - const:null
                                                    - const:expr
                                                    - const:expr:encoded
                                                    - const:expr2
                                                    - const:expr2:encoded
                                                    - input
                                                    - reg
                                                    - var
                                                    - auth
                                                    - env
                                                    - setting
                                                    - col
                                                    - output
                                                    - response
                                                    - trycatch
                                                    - toolset
                                                  default: input
                                                filters:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      disabled:
                                                        type: boolean
                                                        description: ''
                                                      arg:
                                                        type: array
                                                        items:
                                                          type: object
                                                          properties:
                                                            value:
                                                              type: string
                                                              description: ''
                                                            tag:
                                                              type: string
                                                              description: ''
                                                              enum:
                                                                - const
                                                                - const:encoded
                                                                - const:int
                                                                - const:decimal
                                                                - const:bool
                                                                - const:array
                                                                - const:epochms
                                                                - const:obj
                                                                - const:null
                                                                - const:expr
                                                                - const:expr:encoded
                                                                - const:expr2
                                                                - const:expr2:encoded
                                                                - input
                                                                - reg
                                                                - var
                                                                - auth
                                                                - env
                                                                - setting
                                                                - col
                                                                - output
                                                                - response
                                                                - trycatch
                                                                - toolset
                                                              default: input
                                                            filters:
                                                              type: array
                                                              items:
                                                                type: object
                                                                description: ''
                                    items:
                                      type: array
                                      items:
                                        type: object
                                        properties:
                                          name:
                                            type: string
                                            description: ''
                                          children:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                name:
                                                  type: string
                                                  description: ''
                                                children:
                                                  type: array
                                                  items:
                                                    type: object
                                                    description: ''
                                addon:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      id:
                                        type: object
                                        description: ''
                                      offset:
                                        type: string
                                        description: ''
                                      as:
                                        type: string
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            id:
                                              type: object
                                              description: ''
                                            offset:
                                              type: string
                                              description: ''
                                            as:
                                              type: string
                                              description: ''
                                            input:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                      - use_default
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                                  ignore:
                                                    type: boolean
                                                    description: ''
                                                  expand:
                                                    type: boolean
                                                    description: ''
                                                  children:
                                                    type: array
                                                    items:
                                                      type: object
                                                      description: ''
                                            output:
                                              type: object
                                              properties:
                                                customize:
                                                  type: boolean
                                                  description: ''
                                                items:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      children:
                                                        type: array
                                                        items:
                                                          type: object
                                                          description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      input:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                      - use_default
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                                  ignore:
                                                    type: boolean
                                                    description: ''
                                                  expand:
                                                    type: boolean
                                                    description: ''
                                                  children:
                                                    type: array
                                                    items:
                                                      type: object
                                                      description: ''
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              name:
                                                                type: string
                                                                description: ''
                                                              disabled:
                                                                type: boolean
                                                                description: ''
                                                              arg:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  properties:
                                                                    value: {}
                                                                    tag: {}
                                                                    filters: {}
                                      output:
                                        type: object
                                        properties:
                                          customize:
                                            type: boolean
                                            description: ''
                                          items:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                name:
                                                  type: string
                                                  description: ''
                                                children:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      children:
                                                        type: array
                                                        items:
                                                          type: object
                                                          description: ''
                                runtime:
                                  type: object
                                  properties:
                                    mode:
                                      type: string
                                      description: ''
                                      enum:
                                        - disabled
                                        - async-shared
                                        - async-dedicated
                                      default: disabled
                                    cpu:
                                      type: string
                                      description: ''
                                    memory:
                                      type: string
                                      description: ''
                                    max_retry:
                                      type: integer
                                      format: int64
                                      description: ''
                                    timeout:
                                      type: integer
                                      format: int64
                                      description: ''
                                  nullable: true
                          function_post:
                            type: array
                            items:
                              type: object
                              properties:
                                name:
                                  type: string
                                  description: ''
                                as:
                                  type: string
                                  description: ''
                                context:
                                  type: object
                                  description: ''
                                description:
                                  type: string
                                  description: ''
                                disabled:
                                  type: boolean
                                  description: ''
                                mocks:
                                  type: object
                                  description: ''
                                _xsid:
                                  type: string
                                  description: ''
                                input:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: ''
                                      value:
                                        type: string
                                        description: ''
                                      tag:
                                        type: string
                                        description: ''
                                        enum:
                                          - const
                                          - const:encoded
                                          - const:int
                                          - const:decimal
                                          - const:bool
                                          - const:array
                                          - const:epochms
                                          - const:obj
                                          - const:null
                                          - const:expr
                                          - const:expr:encoded
                                          - const:expr2
                                          - const:expr2:encoded
                                          - input
                                          - reg
                                          - var
                                          - auth
                                          - env
                                          - setting
                                          - col
                                          - output
                                          - response
                                          - trycatch
                                          - toolset
                                          - use_default
                                        default: input
                                      ignore:
                                        type: boolean
                                        description: ''
                                      expand:
                                        type: boolean
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            description: ''
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      filters:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            disabled:
                                              type: boolean
                                              description: ''
                                            arg:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                settings_registry:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: ''
                                      value:
                                        type: string
                                        description: ''
                                      tag:
                                        type: string
                                        description: ''
                                        enum:
                                          - const
                                          - const:encoded
                                          - const:int
                                          - const:decimal
                                          - const:bool
                                          - const:array
                                          - const:epochms
                                          - const:obj
                                          - const:null
                                          - const:expr
                                          - const:expr:encoded
                                          - const:expr2
                                          - const:expr2:encoded
                                          - input
                                          - reg
                                          - var
                                          - auth
                                          - env
                                          - setting
                                          - col
                                          - output
                                          - response
                                          - trycatch
                                          - toolset
                                          - use_default
                                        default: input
                                      ignore:
                                        type: boolean
                                        description: ''
                                      expand:
                                        type: boolean
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            description: ''
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      filters:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            disabled:
                                              type: boolean
                                              description: ''
                                            arg:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                  nullable: true
                                output:
                                  type: object
                                  properties:
                                    customize:
                                      type: boolean
                                      description: ''
                                    filters:
                                      type: array
                                      items:
                                        type: object
                                        properties:
                                          name:
                                            type: string
                                            description: ''
                                          disabled:
                                            type: boolean
                                            description: ''
                                          arg:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                value:
                                                  type: string
                                                  description: ''
                                                tag:
                                                  type: string
                                                  description: ''
                                                  enum:
                                                    - const
                                                    - const:encoded
                                                    - const:int
                                                    - const:decimal
                                                    - const:bool
                                                    - const:array
                                                    - const:epochms
                                                    - const:obj
                                                    - const:null
                                                    - const:expr
                                                    - const:expr:encoded
                                                    - const:expr2
                                                    - const:expr2:encoded
                                                    - input
                                                    - reg
                                                    - var
                                                    - auth
                                                    - env
                                                    - setting
                                                    - col
                                                    - output
                                                    - response
                                                    - trycatch
                                                    - toolset
                                                  default: input
                                                filters:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      disabled:
                                                        type: boolean
                                                        description: ''
                                                      arg:
                                                        type: array
                                                        items:
                                                          type: object
                                                          properties:
                                                            value:
                                                              type: string
                                                              description: ''
                                                            tag:
                                                              type: string
                                                              description: ''
                                                              enum:
                                                                - const
                                                                - const:encoded
                                                                - const:int
                                                                - const:decimal
                                                                - const:bool
                                                                - const:array
                                                                - const:epochms
                                                                - const:obj
                                                                - const:null
                                                                - const:expr
                                                                - const:expr:encoded
                                                                - const:expr2
                                                                - const:expr2:encoded
                                                                - input
                                                                - reg
                                                                - var
                                                                - auth
                                                                - env
                                                                - setting
                                                                - col
                                                                - output
                                                                - response
                                                                - trycatch
                                                                - toolset
                                                              default: input
                                                            filters:
                                                              type: array
                                                              items:
                                                                type: object
                                                                description: ''
                                    items:
                                      type: array
                                      items:
                                        type: object
                                        properties:
                                          name:
                                            type: string
                                            description: ''
                                          children:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                name:
                                                  type: string
                                                  description: ''
                                                children:
                                                  type: array
                                                  items:
                                                    type: object
                                                    description: ''
                                addon:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      id:
                                        type: object
                                        description: ''
                                      offset:
                                        type: string
                                        description: ''
                                      as:
                                        type: string
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            id:
                                              type: object
                                              description: ''
                                            offset:
                                              type: string
                                              description: ''
                                            as:
                                              type: string
                                              description: ''
                                            input:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                      - use_default
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                                  ignore:
                                                    type: boolean
                                                    description: ''
                                                  expand:
                                                    type: boolean
                                                    description: ''
                                                  children:
                                                    type: array
                                                    items:
                                                      type: object
                                                      description: ''
                                            output:
                                              type: object
                                              properties:
                                                customize:
                                                  type: boolean
                                                  description: ''
                                                items:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      children:
                                                        type: array
                                                        items:
                                                          type: object
                                                          description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      input:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                      - use_default
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                                  ignore:
                                                    type: boolean
                                                    description: ''
                                                  expand:
                                                    type: boolean
                                                    description: ''
                                                  children:
                                                    type: array
                                                    items:
                                                      type: object
                                                      description: ''
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              name:
                                                                type: string
                                                                description: ''
                                                              disabled:
                                                                type: boolean
                                                                description: ''
                                                              arg:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  properties:
                                                                    value: {}
                                                                    tag: {}
                                                                    filters: {}
                                      output:
                                        type: object
                                        properties:
                                          customize:
                                            type: boolean
                                            description: ''
                                          items:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                name:
                                                  type: string
                                                  description: ''
                                                children:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      children:
                                                        type: array
                                                        items:
                                                          type: object
                                                          description: ''
                                runtime:
                                  type: object
                                  properties:
                                    mode:
                                      type: string
                                      description: ''
                                      enum:
                                        - disabled
                                        - async-shared
                                        - async-dedicated
                                      default: disabled
                                    cpu:
                                      type: string
                                      description: ''
                                    memory:
                                      type: string
                                      description: ''
                                    max_retry:
                                      type: integer
                                      format: int64
                                      description: ''
                                    timeout:
                                      type: integer
                                      format: int64
                                      description: ''
                                  nullable: true
                          query_pre:
                            type: array
                            items:
                              type: object
                              properties:
                                name:
                                  type: string
                                  description: ''
                                as:
                                  type: string
                                  description: ''
                                context:
                                  type: object
                                  description: ''
                                description:
                                  type: string
                                  description: ''
                                disabled:
                                  type: boolean
                                  description: ''
                                mocks:
                                  type: object
                                  description: ''
                                _xsid:
                                  type: string
                                  description: ''
                                input:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: ''
                                      value:
                                        type: string
                                        description: ''
                                      tag:
                                        type: string
                                        description: ''
                                        enum:
                                          - const
                                          - const:encoded
                                          - const:int
                                          - const:decimal
                                          - const:bool
                                          - const:array
                                          - const:epochms
                                          - const:obj
                                          - const:null
                                          - const:expr
                                          - const:expr:encoded
                                          - const:expr2
                                          - const:expr2:encoded
                                          - input
                                          - reg
                                          - var
                                          - auth
                                          - env
                                          - setting
                                          - col
                                          - output
                                          - response
                                          - trycatch
                                          - toolset
                                          - use_default
                                        default: input
                                      ignore:
                                        type: boolean
                                        description: ''
                                      expand:
                                        type: boolean
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            description: ''
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      filters:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            disabled:
                                              type: boolean
                                              description: ''
                                            arg:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                settings_registry:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: ''
                                      value:
                                        type: string
                                        description: ''
                                      tag:
                                        type: string
                                        description: ''
                                        enum:
                                          - const
                                          - const:encoded
                                          - const:int
                                          - const:decimal
                                          - const:bool
                                          - const:array
                                          - const:epochms
                                          - const:obj
                                          - const:null
                                          - const:expr
                                          - const:expr:encoded
                                          - const:expr2
                                          - const:expr2:encoded
                                          - input
                                          - reg
                                          - var
                                          - auth
                                          - env
                                          - setting
                                          - col
                                          - output
                                          - response
                                          - trycatch
                                          - toolset
                                          - use_default
                                        default: input
                                      ignore:
                                        type: boolean
                                        description: ''
                                      expand:
                                        type: boolean
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            description: ''
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      filters:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            disabled:
                                              type: boolean
                                              description: ''
                                            arg:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                  nullable: true
                                output:
                                  type: object
                                  properties:
                                    customize:
                                      type: boolean
                                      description: ''
                                    filters:
                                      type: array
                                      items:
                                        type: object
                                        properties:
                                          name:
                                            type: string
                                            description: ''
                                          disabled:
                                            type: boolean
                                            description: ''
                                          arg:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                value:
                                                  type: string
                                                  description: ''
                                                tag:
                                                  type: string
                                                  description: ''
                                                  enum:
                                                    - const
                                                    - const:encoded
                                                    - const:int
                                                    - const:decimal
                                                    - const:bool
                                                    - const:array
                                                    - const:epochms
                                                    - const:obj
                                                    - const:null
                                                    - const:expr
                                                    - const:expr:encoded
                                                    - const:expr2
                                                    - const:expr2:encoded
                                                    - input
                                                    - reg
                                                    - var
                                                    - auth
                                                    - env
                                                    - setting
                                                    - col
                                                    - output
                                                    - response
                                                    - trycatch
                                                    - toolset
                                                  default: input
                                                filters:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      disabled:
                                                        type: boolean
                                                        description: ''
                                                      arg:
                                                        type: array
                                                        items:
                                                          type: object
                                                          properties:
                                                            value:
                                                              type: string
                                                              description: ''
                                                            tag:
                                                              type: string
                                                              description: ''
                                                              enum:
                                                                - const
                                                                - const:encoded
                                                                - const:int
                                                                - const:decimal
                                                                - const:bool
                                                                - const:array
                                                                - const:epochms
                                                                - const:obj
                                                                - const:null
                                                                - const:expr
                                                                - const:expr:encoded
                                                                - const:expr2
                                                                - const:expr2:encoded
                                                                - input
                                                                - reg
                                                                - var
                                                                - auth
                                                                - env
                                                                - setting
                                                                - col
                                                                - output
                                                                - response
                                                                - trycatch
                                                                - toolset
                                                              default: input
                                                            filters:
                                                              type: array
                                                              items:
                                                                type: object
                                                                description: ''
                                    items:
                                      type: array
                                      items:
                                        type: object
                                        properties:
                                          name:
                                            type: string
                                            description: ''
                                          children:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                name:
                                                  type: string
                                                  description: ''
                                                children:
                                                  type: array
                                                  items:
                                                    type: object
                                                    description: ''
                                addon:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      id:
                                        type: object
                                        description: ''
                                      offset:
                                        type: string
                                        description: ''
                                      as:
                                        type: string
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            id:
                                              type: object
                                              description: ''
                                            offset:
                                              type: string
                                              description: ''
                                            as:
                                              type: string
                                              description: ''
                                            input:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                      - use_default
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                                  ignore:
                                                    type: boolean
                                                    description: ''
                                                  expand:
                                                    type: boolean
                                                    description: ''
                                                  children:
                                                    type: array
                                                    items:
                                                      type: object
                                                      description: ''
                                            output:
                                              type: object
                                              properties:
                                                customize:
                                                  type: boolean
                                                  description: ''
                                                items:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      children:
                                                        type: array
                                                        items:
                                                          type: object
                                                          description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      input:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                      - use_default
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                                  ignore:
                                                    type: boolean
                                                    description: ''
                                                  expand:
                                                    type: boolean
                                                    description: ''
                                                  children:
                                                    type: array
                                                    items:
                                                      type: object
                                                      description: ''
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              name:
                                                                type: string
                                                                description: ''
                                                              disabled:
                                                                type: boolean
                                                                description: ''
                                                              arg:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  properties:
                                                                    value: {}
                                                                    tag: {}
                                                                    filters: {}
                                      output:
                                        type: object
                                        properties:
                                          customize:
                                            type: boolean
                                            description: ''
                                          items:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                name:
                                                  type: string
                                                  description: ''
                                                children:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      children:
                                                        type: array
                                                        items:
                                                          type: object
                                                          description: ''
                                runtime:
                                  type: object
                                  properties:
                                    mode:
                                      type: string
                                      description: ''
                                      enum:
                                        - disabled
                                        - async-shared
                                        - async-dedicated
                                      default: disabled
                                    cpu:
                                      type: string
                                      description: ''
                                    memory:
                                      type: string
                                      description: ''
                                    max_retry:
                                      type: integer
                                      format: int64
                                      description: ''
                                    timeout:
                                      type: integer
                                      format: int64
                                      description: ''
                                  nullable: true
                          query_post:
                            type: array
                            items:
                              type: object
                              properties:
                                name:
                                  type: string
                                  description: ''
                                as:
                                  type: string
                                  description: ''
                                context:
                                  type: object
                                  description: ''
                                description:
                                  type: string
                                  description: ''
                                disabled:
                                  type: boolean
                                  description: ''
                                mocks:
                                  type: object
                                  description: ''
                                _xsid:
                                  type: string
                                  description: ''
                                input:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: ''
                                      value:
                                        type: string
                                        description: ''
                                      tag:
                                        type: string
                                        description: ''
                                        enum:
                                          - const
                                          - const:encoded
                                          - const:int
                                          - const:decimal
                                          - const:bool
                                          - const:array
                                          - const:epochms
                                          - const:obj
                                          - const:null
                                          - const:expr
                                          - const:expr:encoded
                                          - const:expr2
                                          - const:expr2:encoded
                                          - input
                                          - reg
                                          - var
                                          - auth
                                          - env
                                          - setting
                                          - col
                                          - output
                                          - response
                                          - trycatch
                                          - toolset
                                          - use_default
                                        default: input
                                      ignore:
                                        type: boolean
                                        description: ''
                                      expand:
                                        type: boolean
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            description: ''
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      filters:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            disabled:
                                              type: boolean
                                              description: ''
                                            arg:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                settings_registry:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: ''
                                      value:
                                        type: string
                                        description: ''
                                      tag:
                                        type: string
                                        description: ''
                                        enum:
                                          - const
                                          - const:encoded
                                          - const:int
                                          - const:decimal
                                          - const:bool
                                          - const:array
                                          - const:epochms
                                          - const:obj
                                          - const:null
                                          - const:expr
                                          - const:expr:encoded
                                          - const:expr2
                                          - const:expr2:encoded
                                          - input
                                          - reg
                                          - var
                                          - auth
                                          - env
                                          - setting
                                          - col
                                          - output
                                          - response
                                          - trycatch
                                          - toolset
                                          - use_default
                                        default: input
                                      ignore:
                                        type: boolean
                                        description: ''
                                      expand:
                                        type: boolean
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            description: ''
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      filters:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            disabled:
                                              type: boolean
                                              description: ''
                                            arg:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                  nullable: true
                                output:
                                  type: object
                                  properties:
                                    customize:
                                      type: boolean
                                      description: ''
                                    filters:
                                      type: array
                                      items:
                                        type: object
                                        properties:
                                          name:
                                            type: string
                                            description: ''
                                          disabled:
                                            type: boolean
                                            description: ''
                                          arg:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                value:
                                                  type: string
                                                  description: ''
                                                tag:
                                                  type: string
                                                  description: ''
                                                  enum:
                                                    - const
                                                    - const:encoded
                                                    - const:int
                                                    - const:decimal
                                                    - const:bool
                                                    - const:array
                                                    - const:epochms
                                                    - const:obj
                                                    - const:null
                                                    - const:expr
                                                    - const:expr:encoded
                                                    - const:expr2
                                                    - const:expr2:encoded
                                                    - input
                                                    - reg
                                                    - var
                                                    - auth
                                                    - env
                                                    - setting
                                                    - col
                                                    - output
                                                    - response
                                                    - trycatch
                                                    - toolset
                                                  default: input
                                                filters:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      disabled:
                                                        type: boolean
                                                        description: ''
                                                      arg:
                                                        type: array
                                                        items:
                                                          type: object
                                                          properties:
                                                            value:
                                                              type: string
                                                              description: ''
                                                            tag:
                                                              type: string
                                                              description: ''
                                                              enum:
                                                                - const
                                                                - const:encoded
                                                                - const:int
                                                                - const:decimal
                                                                - const:bool
                                                                - const:array
                                                                - const:epochms
                                                                - const:obj
                                                                - const:null
                                                                - const:expr
                                                                - const:expr:encoded
                                                                - const:expr2
                                                                - const:expr2:encoded
                                                                - input
                                                                - reg
                                                                - var
                                                                - auth
                                                                - env
                                                                - setting
                                                                - col
                                                                - output
                                                                - response
                                                                - trycatch
                                                                - toolset
                                                              default: input
                                                            filters:
                                                              type: array
                                                              items:
                                                                type: object
                                                                description: ''
                                    items:
                                      type: array
                                      items:
                                        type: object
                                        properties:
                                          name:
                                            type: string
                                            description: ''
                                          children:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                name:
                                                  type: string
                                                  description: ''
                                                children:
                                                  type: array
                                                  items:
                                                    type: object
                                                    description: ''
                                addon:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      id:
                                        type: object
                                        description: ''
                                      offset:
                                        type: string
                                        description: ''
                                      as:
                                        type: string
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            id:
                                              type: object
                                              description: ''
                                            offset:
                                              type: string
                                              description: ''
                                            as:
                                              type: string
                                              description: ''
                                            input:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                      - use_default
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                                  ignore:
                                                    type: boolean
                                                    description: ''
                                                  expand:
                                                    type: boolean
                                                    description: ''
                                                  children:
                                                    type: array
                                                    items:
                                                      type: object
                                                      description: ''
                                            output:
                                              type: object
                                              properties:
                                                customize:
                                                  type: boolean
                                                  description: ''
                                                items:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      children:
                                                        type: array
                                                        items:
                                                          type: object
                                                          description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      input:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                      - use_default
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                                  ignore:
                                                    type: boolean
                                                    description: ''
                                                  expand:
                                                    type: boolean
                                                    description: ''
                                                  children:
                                                    type: array
                                                    items:
                                                      type: object
                                                      description: ''
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              name:
                                                                type: string
                                                                description: ''
                                                              disabled:
                                                                type: boolean
                                                                description: ''
                                                              arg:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  properties:
                                                                    value: {}
                                                                    tag: {}
                                                                    filters: {}
                                      output:
                                        type: object
                                        properties:
                                          customize:
                                            type: boolean
                                            description: ''
                                          items:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                name:
                                                  type: string
                                                  description: ''
                                                children:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      children:
                                                        type: array
                                                        items:
                                                          type: object
                                                          description: ''
                                runtime:
                                  type: object
                                  properties:
                                    mode:
                                      type: string
                                      description: ''
                                      enum:
                                        - disabled
                                        - async-shared
                                        - async-dedicated
                                      default: disabled
                                    cpu:
                                      type: string
                                      description: ''
                                    memory:
                                      type: string
                                      description: ''
                                    max_retry:
                                      type: integer
                                      format: int64
                                      description: ''
                                    timeout:
                                      type: integer
                                      format: int64
                                      description: ''
                                  nullable: true
                          task_pre:
                            type: array
                            items:
                              type: object
                              properties:
                                name:
                                  type: string
                                  description: ''
                                as:
                                  type: string
                                  description: ''
                                context:
                                  type: object
                                  description: ''
                                description:
                                  type: string
                                  description: ''
                                disabled:
                                  type: boolean
                                  description: ''
                                mocks:
                                  type: object
                                  description: ''
                                _xsid:
                                  type: string
                                  description: ''
                                input:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: ''
                                      value:
                                        type: string
                                        description: ''
                                      tag:
                                        type: string
                                        description: ''
                                        enum:
                                          - const
                                          - const:encoded
                                          - const:int
                                          - const:decimal
                                          - const:bool
                                          - const:array
                                          - const:epochms
                                          - const:obj
                                          - const:null
                                          - const:expr
                                          - const:expr:encoded
                                          - const:expr2
                                          - const:expr2:encoded
                                          - input
                                          - reg
                                          - var
                                          - auth
                                          - env
                                          - setting
                                          - col
                                          - output
                                          - response
                                          - trycatch
                                          - toolset
                                          - use_default
                                        default: input
                                      ignore:
                                        type: boolean
                                        description: ''
                                      expand:
                                        type: boolean
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            description: ''
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      filters:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            disabled:
                                              type: boolean
                                              description: ''
                                            arg:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                settings_registry:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: ''
                                      value:
                                        type: string
                                        description: ''
                                      tag:
                                        type: string
                                        description: ''
                                        enum:
                                          - const
                                          - const:encoded
                                          - const:int
                                          - const:decimal
                                          - const:bool
                                          - const:array
                                          - const:epochms
                                          - const:obj
                                          - const:null
                                          - const:expr
                                          - const:expr:encoded
                                          - const:expr2
                                          - const:expr2:encoded
                                          - input
                                          - reg
                                          - var
                                          - auth
                                          - env
                                          - setting
                                          - col
                                          - output
                                          - response
                                          - trycatch
                                          - toolset
                                          - use_default
                                        default: input
                                      ignore:
                                        type: boolean
                                        description: ''
                                      expand:
                                        type: boolean
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            description: ''
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      filters:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            disabled:
                                              type: boolean
                                              description: ''
                                            arg:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                  nullable: true
                                output:
                                  type: object
                                  properties:
                                    customize:
                                      type: boolean
                                      description: ''
                                    filters:
                                      type: array
                                      items:
                                        type: object
                                        properties:
                                          name:
                                            type: string
                                            description: ''
                                          disabled:
                                            type: boolean
                                            description: ''
                                          arg:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                value:
                                                  type: string
                                                  description: ''
                                                tag:
                                                  type: string
                                                  description: ''
                                                  enum:
                                                    - const
                                                    - const:encoded
                                                    - const:int
                                                    - const:decimal
                                                    - const:bool
                                                    - const:array
                                                    - const:epochms
                                                    - const:obj
                                                    - const:null
                                                    - const:expr
                                                    - const:expr:encoded
                                                    - const:expr2
                                                    - const:expr2:encoded
                                                    - input
                                                    - reg
                                                    - var
                                                    - auth
                                                    - env
                                                    - setting
                                                    - col
                                                    - output
                                                    - response
                                                    - trycatch
                                                    - toolset
                                                  default: input
                                                filters:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      disabled:
                                                        type: boolean
                                                        description: ''
                                                      arg:
                                                        type: array
                                                        items:
                                                          type: object
                                                          properties:
                                                            value:
                                                              type: string
                                                              description: ''
                                                            tag:
                                                              type: string
                                                              description: ''
                                                              enum:
                                                                - const
                                                                - const:encoded
                                                                - const:int
                                                                - const:decimal
                                                                - const:bool
                                                                - const:array
                                                                - const:epochms
                                                                - const:obj
                                                                - const:null
                                                                - const:expr
                                                                - const:expr:encoded
                                                                - const:expr2
                                                                - const:expr2:encoded
                                                                - input
                                                                - reg
                                                                - var
                                                                - auth
                                                                - env
                                                                - setting
                                                                - col
                                                                - output
                                                                - response
                                                                - trycatch
                                                                - toolset
                                                              default: input
                                                            filters:
                                                              type: array
                                                              items:
                                                                type: object
                                                                description: ''
                                    items:
                                      type: array
                                      items:
                                        type: object
                                        properties:
                                          name:
                                            type: string
                                            description: ''
                                          children:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                name:
                                                  type: string
                                                  description: ''
                                                children:
                                                  type: array
                                                  items:
                                                    type: object
                                                    description: ''
                                addon:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      id:
                                        type: object
                                        description: ''
                                      offset:
                                        type: string
                                        description: ''
                                      as:
                                        type: string
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            id:
                                              type: object
                                              description: ''
                                            offset:
                                              type: string
                                              description: ''
                                            as:
                                              type: string
                                              description: ''
                                            input:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                      - use_default
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                                  ignore:
                                                    type: boolean
                                                    description: ''
                                                  expand:
                                                    type: boolean
                                                    description: ''
                                                  children:
                                                    type: array
                                                    items:
                                                      type: object
                                                      description: ''
                                            output:
                                              type: object
                                              properties:
                                                customize:
                                                  type: boolean
                                                  description: ''
                                                items:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      children:
                                                        type: array
                                                        items:
                                                          type: object
                                                          description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      input:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                      - use_default
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                                  ignore:
                                                    type: boolean
                                                    description: ''
                                                  expand:
                                                    type: boolean
                                                    description: ''
                                                  children:
                                                    type: array
                                                    items:
                                                      type: object
                                                      description: ''
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              name:
                                                                type: string
                                                                description: ''
                                                              disabled:
                                                                type: boolean
                                                                description: ''
                                                              arg:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  properties:
                                                                    value: {}
                                                                    tag: {}
                                                                    filters: {}
                                      output:
                                        type: object
                                        properties:
                                          customize:
                                            type: boolean
                                            description: ''
                                          items:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                name:
                                                  type: string
                                                  description: ''
                                                children:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      children:
                                                        type: array
                                                        items:
                                                          type: object
                                                          description: ''
                                runtime:
                                  type: object
                                  properties:
                                    mode:
                                      type: string
                                      description: ''
                                      enum:
                                        - disabled
                                        - async-shared
                                        - async-dedicated
                                      default: disabled
                                    cpu:
                                      type: string
                                      description: ''
                                    memory:
                                      type: string
                                      description: ''
                                    max_retry:
                                      type: integer
                                      format: int64
                                      description: ''
                                    timeout:
                                      type: integer
                                      format: int64
                                      description: ''
                                  nullable: true
                          task_post:
                            type: array
                            items:
                              type: object
                              properties:
                                name:
                                  type: string
                                  description: ''
                                as:
                                  type: string
                                  description: ''
                                context:
                                  type: object
                                  description: ''
                                description:
                                  type: string
                                  description: ''
                                disabled:
                                  type: boolean
                                  description: ''
                                mocks:
                                  type: object
                                  description: ''
                                _xsid:
                                  type: string
                                  description: ''
                                input:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: ''
                                      value:
                                        type: string
                                        description: ''
                                      tag:
                                        type: string
                                        description: ''
                                        enum:
                                          - const
                                          - const:encoded
                                          - const:int
                                          - const:decimal
                                          - const:bool
                                          - const:array
                                          - const:epochms
                                          - const:obj
                                          - const:null
                                          - const:expr
                                          - const:expr:encoded
                                          - const:expr2
                                          - const:expr2:encoded
                                          - input
                                          - reg
                                          - var
                                          - auth
                                          - env
                                          - setting
                                          - col
                                          - output
                                          - response
                                          - trycatch
                                          - toolset
                                          - use_default
                                        default: input
                                      ignore:
                                        type: boolean
                                        description: ''
                                      expand:
                                        type: boolean
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            description: ''
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      filters:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            disabled:
                                              type: boolean
                                              description: ''
                                            arg:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                settings_registry:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: ''
                                      value:
                                        type: string
                                        description: ''
                                      tag:
                                        type: string
                                        description: ''
                                        enum:
                                          - const
                                          - const:encoded
                                          - const:int
                                          - const:decimal
                                          - const:bool
                                          - const:array
                                          - const:epochms
                                          - const:obj
                                          - const:null
                                          - const:expr
                                          - const:expr:encoded
                                          - const:expr2
                                          - const:expr2:encoded
                                          - input
                                          - reg
                                          - var
                                          - auth
                                          - env
                                          - setting
                                          - col
                                          - output
                                          - response
                                          - trycatch
                                          - toolset
                                          - use_default
                                        default: input
                                      ignore:
                                        type: boolean
                                        description: ''
                                      expand:
                                        type: boolean
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            description: ''
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      filters:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            disabled:
                                              type: boolean
                                              description: ''
                                            arg:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                  nullable: true
                                output:
                                  type: object
                                  properties:
                                    customize:
                                      type: boolean
                                      description: ''
                                    filters:
                                      type: array
                                      items:
                                        type: object
                                        properties:
                                          name:
                                            type: string
                                            description: ''
                                          disabled:
                                            type: boolean
                                            description: ''
                                          arg:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                value:
                                                  type: string
                                                  description: ''
                                                tag:
                                                  type: string
                                                  description: ''
                                                  enum:
                                                    - const
                                                    - const:encoded
                                                    - const:int
                                                    - const:decimal
                                                    - const:bool
                                                    - const:array
                                                    - const:epochms
                                                    - const:obj
                                                    - const:null
                                                    - const:expr
                                                    - const:expr:encoded
                                                    - const:expr2
                                                    - const:expr2:encoded
                                                    - input
                                                    - reg
                                                    - var
                                                    - auth
                                                    - env
                                                    - setting
                                                    - col
                                                    - output
                                                    - response
                                                    - trycatch
                                                    - toolset
                                                  default: input
                                                filters:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      disabled:
                                                        type: boolean
                                                        description: ''
                                                      arg:
                                                        type: array
                                                        items:
                                                          type: object
                                                          properties:
                                                            value:
                                                              type: string
                                                              description: ''
                                                            tag:
                                                              type: string
                                                              description: ''
                                                              enum:
                                                                - const
                                                                - const:encoded
                                                                - const:int
                                                                - const:decimal
                                                                - const:bool
                                                                - const:array
                                                                - const:epochms
                                                                - const:obj
                                                                - const:null
                                                                - const:expr
                                                                - const:expr:encoded
                                                                - const:expr2
                                                                - const:expr2:encoded
                                                                - input
                                                                - reg
                                                                - var
                                                                - auth
                                                                - env
                                                                - setting
                                                                - col
                                                                - output
                                                                - response
                                                                - trycatch
                                                                - toolset
                                                              default: input
                                                            filters:
                                                              type: array
                                                              items:
                                                                type: object
                                                                description: ''
                                    items:
                                      type: array
                                      items:
                                        type: object
                                        properties:
                                          name:
                                            type: string
                                            description: ''
                                          children:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                name:
                                                  type: string
                                                  description: ''
                                                children:
                                                  type: array
                                                  items:
                                                    type: object
                                                    description: ''
                                addon:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      id:
                                        type: object
                                        description: ''
                                      offset:
                                        type: string
                                        description: ''
                                      as:
                                        type: string
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            id:
                                              type: object
                                              description: ''
                                            offset:
                                              type: string
                                              description: ''
                                            as:
                                              type: string
                                              description: ''
                                            input:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                      - use_default
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                                  ignore:
                                                    type: boolean
                                                    description: ''
                                                  expand:
                                                    type: boolean
                                                    description: ''
                                                  children:
                                                    type: array
                                                    items:
                                                      type: object
                                                      description: ''
                                            output:
                                              type: object
                                              properties:
                                                customize:
                                                  type: boolean
                                                  description: ''
                                                items:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      children:
                                                        type: array
                                                        items:
                                                          type: object
                                                          description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      input:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                      - use_default
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                                  ignore:
                                                    type: boolean
                                                    description: ''
                                                  expand:
                                                    type: boolean
                                                    description: ''
                                                  children:
                                                    type: array
                                                    items:
                                                      type: object
                                                      description: ''
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              name:
                                                                type: string
                                                                description: ''
                                                              disabled:
                                                                type: boolean
                                                                description: ''
                                                              arg:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  properties:
                                                                    value: {}
                                                                    tag: {}
                                                                    filters: {}
                                      output:
                                        type: object
                                        properties:
                                          customize:
                                            type: boolean
                                            description: ''
                                          items:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                name:
                                                  type: string
                                                  description: ''
                                                children:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      children:
                                                        type: array
                                                        items:
                                                          type: object
                                                          description: ''
                                runtime:
                                  type: object
                                  properties:
                                    mode:
                                      type: string
                                      description: ''
                                      enum:
                                        - disabled
                                        - async-shared
                                        - async-dedicated
                                      default: disabled
                                    cpu:
                                      type: string
                                      description: ''
                                    memory:
                                      type: string
                                      description: ''
                                    max_retry:
                                      type: integer
                                      format: int64
                                      description: ''
                                    timeout:
                                      type: integer
                                      format: int64
                                      description: ''
                                  nullable: true
                          tool_pre:
                            type: array
                            items:
                              type: object
                              properties:
                                name:
                                  type: string
                                  description: ''
                                as:
                                  type: string
                                  description: ''
                                context:
                                  type: object
                                  description: ''
                                description:
                                  type: string
                                  description: ''
                                disabled:
                                  type: boolean
                                  description: ''
                                mocks:
                                  type: object
                                  description: ''
                                _xsid:
                                  type: string
                                  description: ''
                                input:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: ''
                                      value:
                                        type: string
                                        description: ''
                                      tag:
                                        type: string
                                        description: ''
                                        enum:
                                          - const
                                          - const:encoded
                                          - const:int
                                          - const:decimal
                                          - const:bool
                                          - const:array
                                          - const:epochms
                                          - const:obj
                                          - const:null
                                          - const:expr
                                          - const:expr:encoded
                                          - const:expr2
                                          - const:expr2:encoded
                                          - input
                                          - reg
                                          - var
                                          - auth
                                          - env
                                          - setting
                                          - col
                                          - output
                                          - response
                                          - trycatch
                                          - toolset
                                          - use_default
                                        default: input
                                      ignore:
                                        type: boolean
                                        description: ''
                                      expand:
                                        type: boolean
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            description: ''
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      filters:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            disabled:
                                              type: boolean
                                              description: ''
                                            arg:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                settings_registry:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: ''
                                      value:
                                        type: string
                                        description: ''
                                      tag:
                                        type: string
                                        description: ''
                                        enum:
                                          - const
                                          - const:encoded
                                          - const:int
                                          - const:decimal
                                          - const:bool
                                          - const:array
                                          - const:epochms
                                          - const:obj
                                          - const:null
                                          - const:expr
                                          - const:expr:encoded
                                          - const:expr2
                                          - const:expr2:encoded
                                          - input
                                          - reg
                                          - var
                                          - auth
                                          - env
                                          - setting
                                          - col
                                          - output
                                          - response
                                          - trycatch
                                          - toolset
                                          - use_default
                                        default: input
                                      ignore:
                                        type: boolean
                                        description: ''
                                      expand:
                                        type: boolean
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            description: ''
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      filters:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            disabled:
                                              type: boolean
                                              description: ''
                                            arg:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                  nullable: true
                                output:
                                  type: object
                                  properties:
                                    customize:
                                      type: boolean
                                      description: ''
                                    filters:
                                      type: array
                                      items:
                                        type: object
                                        properties:
                                          name:
                                            type: string
                                            description: ''
                                          disabled:
                                            type: boolean
                                            description: ''
                                          arg:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                value:
                                                  type: string
                                                  description: ''
                                                tag:
                                                  type: string
                                                  description: ''
                                                  enum:
                                                    - const
                                                    - const:encoded
                                                    - const:int
                                                    - const:decimal
                                                    - const:bool
                                                    - const:array
                                                    - const:epochms
                                                    - const:obj
                                                    - const:null
                                                    - const:expr
                                                    - const:expr:encoded
                                                    - const:expr2
                                                    - const:expr2:encoded
                                                    - input
                                                    - reg
                                                    - var
                                                    - auth
                                                    - env
                                                    - setting
                                                    - col
                                                    - output
                                                    - response
                                                    - trycatch
                                                    - toolset
                                                  default: input
                                                filters:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      disabled:
                                                        type: boolean
                                                        description: ''
                                                      arg:
                                                        type: array
                                                        items:
                                                          type: object
                                                          properties:
                                                            value:
                                                              type: string
                                                              description: ''
                                                            tag:
                                                              type: string
                                                              description: ''
                                                              enum:
                                                                - const
                                                                - const:encoded
                                                                - const:int
                                                                - const:decimal
                                                                - const:bool
                                                                - const:array
                                                                - const:epochms
                                                                - const:obj
                                                                - const:null
                                                                - const:expr
                                                                - const:expr:encoded
                                                                - const:expr2
                                                                - const:expr2:encoded
                                                                - input
                                                                - reg
                                                                - var
                                                                - auth
                                                                - env
                                                                - setting
                                                                - col
                                                                - output
                                                                - response
                                                                - trycatch
                                                                - toolset
                                                              default: input
                                                            filters:
                                                              type: array
                                                              items:
                                                                type: object
                                                                description: ''
                                    items:
                                      type: array
                                      items:
                                        type: object
                                        properties:
                                          name:
                                            type: string
                                            description: ''
                                          children:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                name:
                                                  type: string
                                                  description: ''
                                                children:
                                                  type: array
                                                  items:
                                                    type: object
                                                    description: ''
                                addon:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      id:
                                        type: object
                                        description: ''
                                      offset:
                                        type: string
                                        description: ''
                                      as:
                                        type: string
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            id:
                                              type: object
                                              description: ''
                                            offset:
                                              type: string
                                              description: ''
                                            as:
                                              type: string
                                              description: ''
                                            input:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                      - use_default
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                                  ignore:
                                                    type: boolean
                                                    description: ''
                                                  expand:
                                                    type: boolean
                                                    description: ''
                                                  children:
                                                    type: array
                                                    items:
                                                      type: object
                                                      description: ''
                                            output:
                                              type: object
                                              properties:
                                                customize:
                                                  type: boolean
                                                  description: ''
                                                items:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      children:
                                                        type: array
                                                        items:
                                                          type: object
                                                          description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      input:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                      - use_default
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                                  ignore:
                                                    type: boolean
                                                    description: ''
                                                  expand:
                                                    type: boolean
                                                    description: ''
                                                  children:
                                                    type: array
                                                    items:
                                                      type: object
                                                      description: ''
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              name:
                                                                type: string
                                                                description: ''
                                                              disabled:
                                                                type: boolean
                                                                description: ''
                                                              arg:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  properties:
                                                                    value: {}
                                                                    tag: {}
                                                                    filters: {}
                                      output:
                                        type: object
                                        properties:
                                          customize:
                                            type: boolean
                                            description: ''
                                          items:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                name:
                                                  type: string
                                                  description: ''
                                                children:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      children:
                                                        type: array
                                                        items:
                                                          type: object
                                                          description: ''
                                runtime:
                                  type: object
                                  properties:
                                    mode:
                                      type: string
                                      description: ''
                                      enum:
                                        - disabled
                                        - async-shared
                                        - async-dedicated
                                      default: disabled
                                    cpu:
                                      type: string
                                      description: ''
                                    memory:
                                      type: string
                                      description: ''
                                    max_retry:
                                      type: integer
                                      format: int64
                                      description: ''
                                    timeout:
                                      type: integer
                                      format: int64
                                      description: ''
                                  nullable: true
                          tool_post:
                            type: array
                            items:
                              type: object
                              properties:
                                name:
                                  type: string
                                  description: ''
                                as:
                                  type: string
                                  description: ''
                                context:
                                  type: object
                                  description: ''
                                description:
                                  type: string
                                  description: ''
                                disabled:
                                  type: boolean
                                  description: ''
                                mocks:
                                  type: object
                                  description: ''
                                _xsid:
                                  type: string
                                  description: ''
                                input:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: ''
                                      value:
                                        type: string
                                        description: ''
                                      tag:
                                        type: string
                                        description: ''
                                        enum:
                                          - const
                                          - const:encoded
                                          - const:int
                                          - const:decimal
                                          - const:bool
                                          - const:array
                                          - const:epochms
                                          - const:obj
                                          - const:null
                                          - const:expr
                                          - const:expr:encoded
                                          - const:expr2
                                          - const:expr2:encoded
                                          - input
                                          - reg
                                          - var
                                          - auth
                                          - env
                                          - setting
                                          - col
                                          - output
                                          - response
                                          - trycatch
                                          - toolset
                                          - use_default
                                        default: input
                                      ignore:
                                        type: boolean
                                        description: ''
                                      expand:
                                        type: boolean
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            description: ''
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      filters:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            disabled:
                                              type: boolean
                                              description: ''
                                            arg:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                settings_registry:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: ''
                                      value:
                                        type: string
                                        description: ''
                                      tag:
                                        type: string
                                        description: ''
                                        enum:
                                          - const
                                          - const:encoded
                                          - const:int
                                          - const:decimal
                                          - const:bool
                                          - const:array
                                          - const:epochms
                                          - const:obj
                                          - const:null
                                          - const:expr
                                          - const:expr:encoded
                                          - const:expr2
                                          - const:expr2:encoded
                                          - input
                                          - reg
                                          - var
                                          - auth
                                          - env
                                          - setting
                                          - col
                                          - output
                                          - response
                                          - trycatch
                                          - toolset
                                          - use_default
                                        default: input
                                      ignore:
                                        type: boolean
                                        description: ''
                                      expand:
                                        type: boolean
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            description: ''
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      filters:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            disabled:
                                              type: boolean
                                              description: ''
                                            arg:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                  nullable: true
                                output:
                                  type: object
                                  properties:
                                    customize:
                                      type: boolean
                                      description: ''
                                    filters:
                                      type: array
                                      items:
                                        type: object
                                        properties:
                                          name:
                                            type: string
                                            description: ''
                                          disabled:
                                            type: boolean
                                            description: ''
                                          arg:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                value:
                                                  type: string
                                                  description: ''
                                                tag:
                                                  type: string
                                                  description: ''
                                                  enum:
                                                    - const
                                                    - const:encoded
                                                    - const:int
                                                    - const:decimal
                                                    - const:bool
                                                    - const:array
                                                    - const:epochms
                                                    - const:obj
                                                    - const:null
                                                    - const:expr
                                                    - const:expr:encoded
                                                    - const:expr2
                                                    - const:expr2:encoded
                                                    - input
                                                    - reg
                                                    - var
                                                    - auth
                                                    - env
                                                    - setting
                                                    - col
                                                    - output
                                                    - response
                                                    - trycatch
                                                    - toolset
                                                  default: input
                                                filters:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      disabled:
                                                        type: boolean
                                                        description: ''
                                                      arg:
                                                        type: array
                                                        items:
                                                          type: object
                                                          properties:
                                                            value:
                                                              type: string
                                                              description: ''
                                                            tag:
                                                              type: string
                                                              description: ''
                                                              enum:
                                                                - const
                                                                - const:encoded
                                                                - const:int
                                                                - const:decimal
                                                                - const:bool
                                                                - const:array
                                                                - const:epochms
                                                                - const:obj
                                                                - const:null
                                                                - const:expr
                                                                - const:expr:encoded
                                                                - const:expr2
                                                                - const:expr2:encoded
                                                                - input
                                                                - reg
                                                                - var
                                                                - auth
                                                                - env
                                                                - setting
                                                                - col
                                                                - output
                                                                - response
                                                                - trycatch
                                                                - toolset
                                                              default: input
                                                            filters:
                                                              type: array
                                                              items:
                                                                type: object
                                                                description: ''
                                    items:
                                      type: array
                                      items:
                                        type: object
                                        properties:
                                          name:
                                            type: string
                                            description: ''
                                          children:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                name:
                                                  type: string
                                                  description: ''
                                                children:
                                                  type: array
                                                  items:
                                                    type: object
                                                    description: ''
                                addon:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      id:
                                        type: object
                                        description: ''
                                      offset:
                                        type: string
                                        description: ''
                                      as:
                                        type: string
                                        description: ''
                                      children:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            id:
                                              type: object
                                              description: ''
                                            offset:
                                              type: string
                                              description: ''
                                            as:
                                              type: string
                                              description: ''
                                            input:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                      - use_default
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                                  ignore:
                                                    type: boolean
                                                    description: ''
                                                  expand:
                                                    type: boolean
                                                    description: ''
                                                  children:
                                                    type: array
                                                    items:
                                                      type: object
                                                      description: ''
                                            output:
                                              type: object
                                              properties:
                                                customize:
                                                  type: boolean
                                                  description: ''
                                                items:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      children:
                                                        type: array
                                                        items:
                                                          type: object
                                                          description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                description: ''
                                      input:
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            name:
                                              type: string
                                              description: ''
                                            value:
                                              type: string
                                              description: ''
                                            tag:
                                              type: string
                                              description: ''
                                              enum:
                                                - const
                                                - const:encoded
                                                - const:int
                                                - const:decimal
                                                - const:bool
                                                - const:array
                                                - const:epochms
                                                - const:obj
                                                - const:null
                                                - const:expr
                                                - const:expr:encoded
                                                - const:expr2
                                                - const:expr2:encoded
                                                - input
                                                - reg
                                                - var
                                                - auth
                                                - env
                                                - setting
                                                - col
                                                - output
                                                - response
                                                - trycatch
                                                - toolset
                                                - use_default
                                              default: input
                                            ignore:
                                              type: boolean
                                              description: ''
                                            expand:
                                              type: boolean
                                              description: ''
                                            children:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  value:
                                                    type: string
                                                    description: ''
                                                  tag:
                                                    type: string
                                                    description: ''
                                                    enum:
                                                      - const
                                                      - const:encoded
                                                      - const:int
                                                      - const:decimal
                                                      - const:bool
                                                      - const:array
                                                      - const:epochms
                                                      - const:obj
                                                      - const:null
                                                      - const:expr
                                                      - const:expr:encoded
                                                      - const:expr2
                                                      - const:expr2:encoded
                                                      - input
                                                      - reg
                                                      - var
                                                      - auth
                                                      - env
                                                      - setting
                                                      - col
                                                      - output
                                                      - response
                                                      - trycatch
                                                      - toolset
                                                      - use_default
                                                    default: input
                                                  filters:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        name:
                                                          type: string
                                                          description: ''
                                                        disabled:
                                                          type: boolean
                                                          description: ''
                                                        arg:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              value:
                                                                type: string
                                                                description: ''
                                                              tag:
                                                                type: string
                                                                description: ''
                                                                enum:
                                                                  - const
                                                                  - const:encoded
                                                                  - const:int
                                                                  - const:decimal
                                                                  - const:bool
                                                                  - const:array
                                                                  - const:epochms
                                                                  - const:obj
                                                                  - const:null
                                                                  - const:expr
                                                                  - const:expr:encoded
                                                                  - const:expr2
                                                                  - const:expr2:encoded
                                                                  - input
                                                                  - reg
                                                                  - var
                                                                  - auth
                                                                  - env
                                                                  - setting
                                                                  - col
                                                                  - output
                                                                  - response
                                                                  - trycatch
                                                                  - toolset
                                                                default: input
                                                              filters:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  description: ''
                                                  ignore:
                                                    type: boolean
                                                    description: ''
                                                  expand:
                                                    type: boolean
                                                    description: ''
                                                  children:
                                                    type: array
                                                    items:
                                                      type: object
                                                      description: ''
                                            filters:
                                              type: array
                                              items:
                                                type: object
                                                properties:
                                                  name:
                                                    type: string
                                                    description: ''
                                                  disabled:
                                                    type: boolean
                                                    description: ''
                                                  arg:
                                                    type: array
                                                    items:
                                                      type: object
                                                      properties:
                                                        value:
                                                          type: string
                                                          description: ''
                                                        tag:
                                                          type: string
                                                          description: ''
                                                          enum:
                                                            - const
                                                            - const:encoded
                                                            - const:int
                                                            - const:decimal
                                                            - const:bool
                                                            - const:array
                                                            - const:epochms
                                                            - const:obj
                                                            - const:null
                                                            - const:expr
                                                            - const:expr:encoded
                                                            - const:expr2
                                                            - const:expr2:encoded
                                                            - input
                                                            - reg
                                                            - var
                                                            - auth
                                                            - env
                                                            - setting
                                                            - col
                                                            - output
                                                            - response
                                                            - trycatch
                                                            - toolset
                                                          default: input
                                                        filters:
                                                          type: array
                                                          items:
                                                            type: object
                                                            properties:
                                                              name:
                                                                type: string
                                                                description: ''
                                                              disabled:
                                                                type: boolean
                                                                description: ''
                                                              arg:
                                                                type: array
                                                                items:
                                                                  type: object
                                                                  properties:
                                                                    value: {}
                                                                    tag: {}
                                                                    filters: {}
                                      output:
                                        type: object
                                        properties:
                                          customize:
                                            type: boolean
                                            description: ''
                                          items:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                name:
                                                  type: string
                                                  description: ''
                                                children:
                                                  type: array
                                                  items:
                                                    type: object
                                                    properties:
                                                      name:
                                                        type: string
                                                        description: ''
                                                      children:
                                                        type: array
                                                        items:
                                                          type: object
                                                          description: ''
                                runtime:
                                  type: object
                                  properties:
                                    mode:
                                      type: string
                                      description: ''
                                      enum:
                                        - disabled
                                        - async-shared
                                        - async-dedicated
                                      default: disabled
                                    cpu:
                                      type: string
                                      description: ''
                                    memory:
                                      type: string
                                      description: ''
                                    max_retry:
                                      type: integer
                                      format: int64
                                      description: ''
                                    timeout:
                                      type: integer
                                      format: int64
                                      description: ''
                                  nullable: true
                      defaults:
                        type: object
                        properties:
                          db_primary_key:
                            type: string
                            description: ''
                            enum:
                              - int
                              - uuid
                    nullable: true
        '400':
          description: Input Error. Check the request payload for issues.
        '401':
          description: Unauthorized
        '403':
          description: >-
            Access denied. Additional privileges are needed access the requested
            resource.
        '404':
          description: Not Found. The requested resource does not exist.
        '429':
          description: Rate Limited. Too many requests.
        '500':
          description: Unexpected error
      security:
        - bearerAuth: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````

Built with [Mintlify](https://mintlify.com).