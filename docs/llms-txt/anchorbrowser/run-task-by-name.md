# Source: https://docs.anchorbrowser.io/api-reference/tasks/run-task-by-name.md

# Run Task by Name

> Executes a task by its name, always using the latest version. This is a convenience endpoint
for running tasks without needing to know the task ID.


## OpenAPI

````yaml openapi-mintlify.yaml post /v1/task/run/{taskName}
paths:
  path: /v1/task/run/{taskName}
  method: post
  servers:
    - url: https://api.anchorbrowser.io
      description: API server
  request:
    security:
      - title: api key header
        parameters:
          query: {}
          header:
            anchor-api-key:
              type: apiKey
              description: API key passed in the header
          cookie: {}
    parameters:
      path:
        taskName:
          schema:
            - type: string
              required: true
              description: The name of the task to run
              example: web-scraper
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              async:
                allOf:
                  - type: boolean
                    description: Whether to run the task asynchronously
              overrideBrowserConfiguration:
                allOf:
                  - $ref: '#/components/schemas/SessionConfig'
                    description: Override browser configuration for this execution
              inputs:
                allOf:
                  - type: object
                    additionalProperties:
                      type: string
                    patternProperties:
                      ^ANCHOR_.*$:
                        type: string
                    description: >-
                      Environment variables for task execution (keys must start
                      with ANCHOR_)
            required: true
            refIdentifier: '#/components/schemas/RunTaskByNameRequest'
        examples:
          example:
            value:
              async: true
              overrideBrowserConfiguration:
                initial_url: <string>
                recording:
                  active: true
                proxy:
                  active: true
                  type: anchor_proxy
                  country_code: af
                  region: <string>
                  city: <string>
                timeout:
                  max_duration: 123
                  idle_timeout: 123
                live_view:
                  read_only: true
              inputs: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: object
                    properties:
                      success:
                        type: boolean
                        description: Whether the task executed successfully
                      async:
                        type: boolean
                        description: Whether the task was executed asynchronously
                      message:
                        type: string
                        description: Execution result message
                      taskId:
                        type: string
                        format: uuid
                        description: Task identifier
                      executionTime:
                        type: number
                        description: >-
                          Execution duration in milliseconds (only present in
                          sync mode)
                      output:
                        type: string
                        description: Task execution output (only present in sync mode)
                      error:
                        type: string
                        description: >-
                          Error message if execution failed (only present in
                          sync mode)
                      executionResultId:
                        type: string
                        format: uuid
                        description: >-
                          Execution result identifier for tracking and polling
                          (present in async mode)
                    required:
                      - success
                      - async
                      - message
                      - taskId
            refIdentifier: '#/components/schemas/RunTaskResponse'
        examples:
          example:
            value:
              data:
                success: true
                async: true
                message: <string>
                taskId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                executionTime: 123
                output: <string>
                error: <string>
                executionResultId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
        description: Task executed successfully
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: object
                    properties:
                      code:
                        type: integer
                      message:
                        type: string
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              error:
                code: 123
                message: <string>
        description: Task not found
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              error:
                code: 123
                message: <string>
        description: Task execution failed
  deprecated: false
  type: path
components:
  schemas:
    ProxyConfig:
      description: |
        Proxy Documentation available at [Proxy Documentation](/advanced/proxy)
      type: object
      oneOf:
        - $ref: '#/components/schemas/AnchorProxy'
        - $ref: '#/components/schemas/CustomProxy'
    AnchorProxy:
      title: Anchor Proxy
      type: object
      properties:
        active:
          type: boolean
        type:
          type: string
          description: |
            **On change make sure to update the country_code.**
          oneOf:
            - enum:
                - anchor_proxy
                - anchor_residential
                - anchor_mobile
                - anchor_gov
              title: anchor_residential
              description: >-
                Create a session with a residential proxy to access websites as
                if you're browsing from a computer in that country.
            - enum:
                - anchor_proxy
                - anchor_residential
                - anchor_mobile
                - anchor_gov
              description: >-
                Create a session with a mobile proxy to access websites as if
                you're browsing from a mobile device in that country.
              title: anchor_mobile
            - enum:
                - anchor_proxy
                - anchor_residential
                - anchor_mobile
                - anchor_gov
              description: >-
                Create your session with a residential proxy to access websites
                as if you're browsing from a computer in that country. This
                option reduces the chance of being blocked by governmental
                websites.
              title: anchor_gov
            - enum:
                - anchor_proxy
                - anchor_residential
                - anchor_mobile
                - anchor_gov
              description: >-
                Create a session with a proxy to access websites as if you're
                browsing from a computer in that country.
              title: anchor_proxy
        country_code:
          oneOf:
            - $ref: '#/components/schemas/AnchorProxyCountryCode'
            - $ref: '#/components/schemas/ResidentialCountryCode'
            - $ref: '#/components/schemas/MobileCountryCode'
            - $ref: '#/components/schemas/GovCountryCode'
          description: |
            Supported country codes ISO 2 lowercase

            **On change make sure to update the Proxy type.**
        region:
          type: string
          description: |
            Region code for more specific geographic targeting.
            The city parameter can only be used when region is also provided.
        city:
          type: string
          description: >
            City name for precise geographic targeting. Supported for
            anchor_proxy only.

            Can only be used when region is also provided.
      required:
        - active
    CustomProxy:
      title: Custom Proxy
      type: object
      properties:
        type:
          type: string
          enum:
            - custom
        server:
          type: string
          description: Proxy server address
        username:
          type: string
          description: Proxy username
        password:
          type: string
          description: Proxy password
        active:
          type: boolean
      required:
        - type
        - server
        - username
        - password
        - active
    ResidentialCountryCode:
      type: string
      title: anchor_residential
      enum:
        - af
        - al
        - dz
        - ad
        - ao
        - ag
        - ar
        - am
        - aw
        - au
        - at
        - az
        - bs
        - bh
        - bd
        - bb
        - by
        - be
        - bz
        - bj
        - bm
        - bo
        - ba
        - bw
        - br
        - bn
        - bg
        - bf
        - bi
        - kh
        - cm
        - ca
        - cv
        - td
        - cl
        - cn
        - co
        - cg
        - cr
        - ci
        - hr
        - cu
        - cy
        - cz
        - dk
        - dj
        - dm
        - do
        - ec
        - eg
        - sv
        - gq
        - ee
        - sz
        - et
        - fj
        - fi
        - fr
        - pf
        - ga
        - gm
        - ge
        - de
        - gh
        - gr
        - gd
        - gt
        - gn
        - gy
        - ht
        - hn
        - hk
        - hu
        - is
        - in
        - id
        - ir
        - iq
        - ie
        - il
        - it
        - jm
        - jp
        - jo
        - kz
        - ke
        - kw
        - kg
        - la
        - lv
        - lb
        - ls
        - lr
        - ly
        - lt
        - lu
        - mk
        - mg
        - mw
        - my
        - mv
        - ml
        - mt
        - mr
        - mx
        - md
        - mn
        - me
        - ma
        - mz
        - mm
        - na
        - np
        - nl
        - nc
        - nz
        - ni
        - ne
        - ng
        - 'no'
        - om
        - pk
        - pa
        - pg
        - py
        - pe
        - ph
        - pl
        - pt
        - pr
        - qa
        - ro
        - ru
        - rw
        - lc
        - ws
        - sm
        - sa
        - sn
        - rs
        - sl
        - sg
        - sk
        - si
        - so
        - za
        - kr
        - ss
        - es
        - lk
        - sd
        - sr
        - se
        - ch
        - sy
        - st
        - tw
        - tj
        - tz
        - th
        - tl
        - tr
        - tg
        - tt
        - tn
        - tm
        - ug
        - ua
        - gb
        - us
        - uy
        - uz
        - vu
        - ve
        - vn
        - ye
        - zm
        - zw
      default: us
    MobileCountryCode:
      type: string
      title: anchor_mobile
      enum:
        - af
        - al
        - dz
        - ao
        - ag
        - ar
        - am
        - au
        - at
        - az
        - bs
        - bh
        - bd
        - bb
        - be
        - bz
        - bj
        - bt
        - bo
        - ba
        - bw
        - br
        - bg
        - bf
        - kh
        - cm
        - ca
        - cv
        - cl
        - cn
        - co
        - cg
        - ci
        - hr
        - cu
        - cy
        - cz
        - dk
        - do
        - ec
        - eg
        - sv
        - ee
        - et
        - fj
        - fi
        - fr
        - ga
        - gm
        - ge
        - de
        - gh
        - gr
        - gt
        - gw
        - gy
        - ht
        - hn
        - hu
        - is
        - in
        - id
        - iq
        - ie
        - il
        - it
        - jm
        - jp
        - jo
        - kz
        - ke
        - kw
        - kg
        - la
        - lv
        - lb
        - lr
        - ly
        - lt
        - mk
        - mw
        - my
        - mv
        - ml
        - mt
        - mu
        - mx
        - md
        - mn
        - me
        - ma
        - mz
        - np
        - nl
        - nc
        - nz
        - na
        - ni
        - ng
        - 'no'
        - om
        - pk
        - pa
        - py
        - pe
        - ph
        - pl
        - pt
        - qa
        - ro
        - ru
        - rw
        - sa
        - sn
        - rs
        - sl
        - sg
        - sk
        - si
        - za
        - kr
        - es
        - lk
        - sd
        - se
        - ch
        - sy
        - tw
        - tj
        - tz
        - th
        - tg
        - tt
        - tn
        - tr
        - ug
        - ua
        - ae
        - gb
        - us
        - uy
        - uz
        - ve
        - vn
        - ye
        - zm
        - zw
      default: us
    GovCountryCode:
      type: string
      title: anchor_gov
      enum:
        - af
        - al
        - dz
        - ad
        - ao
        - as
        - ag
        - ar
        - am
        - aw
        - au
        - at
        - az
        - bs
        - bh
        - bb
        - by
        - be
        - bz
        - bj
        - bm
        - bo
        - ba
        - br
        - bg
        - bf
        - cm
        - ca
        - cv
        - td
        - cl
        - co
        - cg
        - cr
        - ci
        - hr
        - cu
        - cy
        - cz
        - dk
        - dm
        - do
        - ec
        - eg
        - sv
        - ee
        - et
        - fo
        - fi
        - fr
        - gf
        - pf
        - ga
        - gm
        - ge
        - de
        - gh
        - gi
        - gr
        - gd
        - gp
        - gt
        - gg
        - gn
        - gw
        - gy
        - ht
        - hn
        - hu
        - is
        - in
        - ir
        - iq
        - ie
        - il
        - it
        - jm
        - jp
        - jo
        - kz
        - kw
        - kg
        - lv
        - lb
        - ly
        - li
        - lt
        - lu
        - mk
        - ml
        - mt
        - mq
        - mr
        - mx
        - md
        - mc
        - me
        - ma
        - nl
        - nz
        - ni
        - ng
        - 'no'
        - pk
        - pa
        - py
        - pe
        - ph
        - pl
        - pt
        - pr
        - qa
        - ro
        - lc
        - sm
        - sa
        - sn
        - rs
        - sc
        - sl
        - sk
        - si
        - so
        - za
        - kr
        - es
        - sr
        - se
        - ch
        - sy
        - st
        - tw
        - tj
        - tg
        - tt
        - tn
        - tr
        - tc
        - ua
        - ae
        - us
        - uy
        - uz
        - ve
        - ye
      default: us
    AnchorProxyCountryCode:
      type: string
      title: anchor_proxy
      enum:
        - af
        - al
        - dz
        - ad
        - ao
        - as
        - ag
        - ar
        - am
        - aw
        - au
        - at
        - az
        - bs
        - bh
        - bb
        - by
        - be
        - bz
        - bj
        - bm
        - bo
        - ba
        - br
        - bg
        - bf
        - cm
        - ca
        - cv
        - td
        - cl
        - co
        - cg
        - cr
        - ci
        - hr
        - cu
        - cy
        - cz
        - dk
        - dm
        - do
        - ec
        - eg
        - sv
        - ee
        - et
        - fo
        - fi
        - fr
        - gf
        - pf
        - ga
        - gm
        - ge
        - de
        - gh
        - gi
        - gr
        - gd
        - gp
        - gt
        - gg
        - gn
        - gw
        - gy
        - ht
        - hn
        - hu
        - is
        - in
        - ir
        - iq
        - ie
        - il
        - it
        - jm
        - jp
        - jo
        - kz
        - kw
        - kg
        - lv
        - lb
        - ly
        - li
        - lt
        - lu
        - mk
        - ml
        - mt
        - mq
        - mr
        - mx
        - md
        - mc
        - me
        - ma
        - nl
        - nz
        - ni
        - ng
        - 'no'
        - pk
        - pa
        - py
        - pe
        - ph
        - pl
        - pt
        - pr
        - qa
        - ro
        - lc
        - sm
        - sa
        - sn
        - rs
        - sc
        - sl
        - sk
        - si
        - so
        - za
        - kr
        - es
        - sr
        - se
        - ch
        - sy
        - st
        - tw
        - tj
        - tg
        - tt
        - tn
        - tr
        - tc
        - ua
        - ae
        - us
        - uy
        - uz
        - ve
        - ye
      default: us
    SessionConfig:
      type: object
      description: Session-related configurations.
      properties:
        initial_url:
          type: string
          format: uri
          description: >-
            The URL to navigate to when the browser session starts. If not
            provided, the browser will load an empty page.
        recording:
          type: object
          description: Configuration for session recording.
          properties:
            active:
              type: boolean
              description: >-
                Enable or disable video recording of the browser session.
                Defaults to `true`.
        proxy:
          $ref: '#/components/schemas/ProxyConfig'
        timeout:
          type: object
          description: Timeout configurations for the browser session.
          properties:
            max_duration:
              type: integer
              description: >-
                Maximum amount of time (in minutes) for the browser to run
                before terminating. Defaults to `20`.
            idle_timeout:
              type: integer
              description: >-
                The amount of time (in minutes) the browser session waits for
                new connections after all others are closed before stopping.
                Defaults to `5`.
        live_view:
          type: object
          description: Configuration for live viewing the browser session.
          properties:
            read_only:
              type: boolean
              description: >-
                Enable or disable read-only mode for live viewing. Defaults to
                `false`.

````