# Source: https://docs.anchorbrowser.io/api-reference/batch-sessions/create-batch-sessions.md

# Create Batch Sessions

> Creates multiple browser sessions in a single batch operation. This endpoint allows you to 
create up to 5,000 browser sessions simultaneously with the same configuration.

The batch will be processed asynchronously, and you can monitor progress using the batch status endpoint.


## OpenAPI

````yaml openapi-mintlify.yaml post /v1/batch-sessions
paths:
  path: /v1/batch-sessions
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              count:
                allOf:
                  - type: integer
                    minimum: 1
                    maximum: 1000
                    description: Number of sessions to create in the batch (1-1000)
              configuration:
                allOf:
                  - $ref: '#/components/schemas/SessionCreateRequestSchema'
                    description: Configuration that applies to all sessions in the batch
              metadata:
                allOf:
                  - type: object
                    additionalProperties: true
                    description: >-
                      Optional batch-level metadata for identification and
                      organization
            required: true
            refIdentifier: '#/components/schemas/BatchSessionRequestSchema'
            requiredProperties:
              - count
        examples:
          small_batch:
            summary: Small batch example
            value:
              count: 10
              configuration:
                browser:
                  headless:
                    active: true
                  viewport:
                    width: 1440
                    height: 900
                session:
                  timeout:
                    idle_timeout: 10
                    max_duration: 300
              metadata:
                project: web-scraping
                environment: production
          large_batch:
            summary: Large batch example (from test snippet)
            value:
              count: 2500
              configuration:
                browser:
                  headless:
                    active: true
                  viewport:
                    width: 1440
                    height: 900
                  recording:
                    active: true
                session:
                  timeout:
                    idle_timeout: 10
                    max_duration: 300
                  tags:
                    - batch-test-comprehensive
              metadata:
                test: true
                description: Comprehensive batch test with 3 sessions
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - $ref: '#/components/schemas/BatchSessionResponseSchema'
        examples:
          example:
            value:
              data:
                batch_id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                status: pending
                total_requests: 123
                created_at: '2023-11-07T05:31:56Z'
        description: Batch created successfully
    '400':
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
          invalid_count:
            summary: Invalid session count
            value:
              error:
                code: 400
                message: Session count must be between 1 and 1000
          invalid_config:
            summary: Invalid configuration
            value:
              error:
                code: 400
                message: CAPTCHA solver requires proxy to be active
        description: Invalid request parameters or configuration
    '402':
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
        description: Payment Required - Insufficient credits for batch creation
    '429':
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
        description: Too many requests - Rate limit exceeded
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
        description: Internal server error
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
    BrowserConfig:
      type: object
      description: Browser-specific configurations.
      properties:
        profile:
          type: object
          description: Options for managing and persisting browser session profiles.
          properties:
            name:
              type: string
              description: The name of the profile to be used during the browser session.
            persist:
              type: boolean
              description: >-
                Indicates whether the browser session profile data should be
                saved when the browser session ends. Defaults to `false`.
        adblock:
          type: object
          description: Configuration for ad-blocking.
          properties:
            active:
              type: boolean
              description: Enable or disable ad-blocking. Defaults to `true`.
        popup_blocker:
          type: object
          description: Configuration for popup blocking.
          properties:
            active:
              type: boolean
              description: >-
                Blocks popups, including ads and CAPTCHA consent banners.
                Requires adblock to be active. Defaults to `true`.
        captcha_solver:
          type: object
          description: Configuration for captcha-solving.
          properties:
            active:
              type: boolean
              description: >-
                Enable or disable captcha-solving. Requires proxy to be active.
                Defaults to `false`.
        headless:
          type: object
          description: Configuration for headless mode.
          properties:
            active:
              type: boolean
              description: >-
                Whether browser should be headless or headful. Defaults to
                `false`.
        viewport:
          type: object
          description: Configuration for the browser's viewport size.
          properties:
            width:
              type: integer
              description: Width of the viewport in pixels. Defaults to `1440`.
            height:
              type: integer
              description: Height of the viewport in pixels. Defaults to `900`.
        fullscreen:
          type: object
          description: Configuration for fullscreen mode.
          properties:
            active:
              type: boolean
              description: >-
                Enable or disable fullscreen mode. When enabled, the browser
                will start in fullscreen mode. Defaults to `false`.
        p2p_download:
          type: object
          description: Configuration for peer-to-peer download capture functionality.
          properties:
            active:
              type: boolean
              description: >-
                Enable or disable P2P downloads. When enabled, the browser will
                capture downloads for direct data extraction, instead of
                uploading them on Anchor's storage. Defaults to `false`.
        extensions:
          type: array
          description: >-
            Array of extension IDs to load in the browser session. Extensions
            must be previously uploaded using the Extensions API.
          items:
            type: string
            format: uuid
        disable_web_security:
          type: object
          description: Configuration for disabling web security features.
          properties:
            active:
              type: boolean
              description: >-
                Whether to disable web security features (CORS, same-origin
                policy, etc.). Allows accessing iframes and resources from
                different origins. Defaults to `false`.
        extra_stealth:
          type: object
          description: >-
            Configuration for extra stealth mode to enhance browser
            fingerprinting protection.
          properties:
            active:
              type: boolean
              description: Enable or disable extra stealth mode.
    SessionCreateRequestSchema:
      type: object
      properties:
        session:
          $ref: '#/components/schemas/SessionConfig'
        browser:
          $ref: '#/components/schemas/BrowserConfig'
        integrations:
          type: array
          description: >-
            Array of integrations to load in the browser session. Integrations
            must be previously created using the Integrations API.
          items:
            $ref: '#/components/schemas/Integration'
          example:
            - id: 550e8400-e29b-41d4-a716-446655440000
              type: 1PASSWORD
              configuration:
                load_mode: all
    BatchSessionResponseSchema:
      type: object
      properties:
        batch_id:
          type: string
          format: uuid
          description: Unique identifier for the batch
        status:
          type: string
          enum:
            - pending
            - processing
            - completed
            - failed
          description: Current status of the batch
        total_requests:
          type: integer
          description: Total number of sessions requested in the batch
        created_at:
          type: string
          format: date-time
          description: Timestamp when the batch was created
    OnePasswordAllSecretsConfig:
      type: object
      required:
        - load_mode
      properties:
        load_mode:
          type: string
          enum:
            - all
          description: Load all secrets from 1Password
    OnePasswordSpecificSecretsConfig:
      type: object
      required:
        - load_mode
        - secrets
      properties:
        load_mode:
          type: string
          enum:
            - specific
          description: Load specific secrets from 1Password
        secrets:
          type: array
          items:
            type: string
          minItems: 1
          description: Array of secret references to load
          example:
            - op://vault/item/field
    OnePasswordConfig:
      oneOf:
        - $ref: '#/components/schemas/OnePasswordAllSecretsConfig'
        - $ref: '#/components/schemas/OnePasswordSpecificSecretsConfig'
    OnePasswordIntegration:
      type: object
      required:
        - id
        - type
        - configuration
      properties:
        id:
          type: string
          format: uuid
          description: Unique integration ID
          example: 550e8400-e29b-41d4-a716-446655440000
        type:
          type: string
          enum:
            - 1PASSWORD
          description: Integration type
        configuration:
          $ref: '#/components/schemas/OnePasswordConfig'
    Integration:
      oneOf:
        - $ref: '#/components/schemas/OnePasswordIntegration'
      discriminator:
        propertyName: type

````