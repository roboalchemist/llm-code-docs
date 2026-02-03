# Source: https://docs.anchorbrowser.io/api-reference/tasks/get-latest-task-version.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Latest Task Version

> Retrieves the latest version of a task, including the full code content.




## OpenAPI

````yaml openapi-mintlify.yaml get /v1/task/{taskId}/latest
openapi: 3.1.0
info:
  title: AnchorBrowser API
  version: 1.0.0
  description: APIs to manage all browser-related actions and configuration.
servers:
  - url: https://api.anchorbrowser.io
    description: API server
security: []
paths:
  /v1/task/{taskId}/latest:
    get:
      tags:
        - Tasks
      summary: Get Latest Task Version
      description: |
        Retrieves the latest version of a task, including the full code content.
      parameters:
        - name: taskId
          in: path
          required: true
          description: The ID of the task
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Latest task version retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskVersionResponse'
        '404':
          description: Task or version not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to retrieve task version
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    TaskVersionResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/TaskVersion'
    ErrorResponse:
      type: object
      properties:
        error:
          type: object
          properties:
            code:
              type: integer
            message:
              type: string
    TaskVersion:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the task version
        taskId:
          type: string
          format: uuid
          description: Parent task identifier
        version:
          type: string
          description: Version identifier (draft, latest, or version number)
        code:
          type: string
          description: Base64 encoded task code
        language:
          type: string
          enum:
            - typescript
          description: Programming language for the task
        description:
          type: string
          maxLength: 1000
          description: Optional description of the version
        browserConfiguration:
          $ref: '#/components/schemas/SessionConfig'
          description: Browser configuration for task execution
        deleted:
          type: boolean
          description: Whether the version is soft deleted
        createdAt:
          type: string
          format: date-time
          description: Version creation timestamp
        updatedAt:
          type: string
          format: date-time
          description: Version last update timestamp
      required:
        - id
        - taskId
        - version
        - code
        - deleted
        - createdAt
        - updatedAt
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
        tags:
          type: array
          items:
            type: string
          description: >-
            Custom labels to categorize and identify browser sessions. Useful
            for filtering, organizing, and tracking sessions across your
            workflows.
          example:
            - production
            - scraping
            - customer-123
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
                Maximum time (in minutes) the session can run before
                automatically terminating. Defaults to `20`. Set to `-1` to
                disable this limit.
            idle_timeout:
              type: integer
              description: >-
                Time (in minutes) the session waits for new connections after
                all others are closed before stopping. Defaults to `5`. Set to
                `-1` to disable this limit.
        live_view:
          type: object
          description: Configuration for live viewing the browser session.
          properties:
            read_only:
              type: boolean
              description: >-
                Enable or disable read-only mode for live viewing. Defaults to
                `false`.
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
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````