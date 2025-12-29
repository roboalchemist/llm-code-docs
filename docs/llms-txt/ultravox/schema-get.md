# Source: https://docs.ultravox.ai/api-reference/other/schema-get.md

# Get OpenAPI Schema

> Gets the OpenAPI schema for the Ultravox REST API

Format can be selected via content negotiation.

* YAML: application/vnd.oai.openapi
* JSON: application/vnd.oai.openapi+json


## OpenAPI

````yaml get /api/schema/
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/schema/:
    get:
      tags:
        - schema
      description: >-
        OpenApi3 schema for this API. Format can be selected via content
        negotiation.


        - YAML: application/vnd.oai.openapi

        - JSON: application/vnd.oai.openapi+json
      operationId: schema_retrieve
      parameters:
        - in: query
          name: format
          schema:
            type: string
            enum:
              - json
              - yaml
        - in: query
          name: lang
          schema:
            type: string
            enum:
              - af
              - ar
              - ar-dz
              - ast
              - az
              - be
              - bg
              - bn
              - br
              - bs
              - ca
              - ckb
              - cs
              - cy
              - da
              - de
              - dsb
              - el
              - en
              - en-au
              - en-gb
              - eo
              - es
              - es-ar
              - es-co
              - es-mx
              - es-ni
              - es-ve
              - et
              - eu
              - fa
              - fi
              - fr
              - fy
              - ga
              - gd
              - gl
              - he
              - hi
              - hr
              - hsb
              - hu
              - hy
              - ia
              - id
              - ig
              - io
              - is
              - it
              - ja
              - ka
              - kab
              - kk
              - km
              - kn
              - ko
              - ky
              - lb
              - lt
              - lv
              - mk
              - ml
              - mn
              - mr
              - ms
              - my
              - nb
              - ne
              - nl
              - nn
              - os
              - pa
              - pl
              - pt
              - pt-br
              - ro
              - ru
              - sk
              - sl
              - sq
              - sr
              - sr-latn
              - sv
              - sw
              - ta
              - te
              - tg
              - th
              - tk
              - tr
              - tt
              - udm
              - ug
              - uk
              - ur
              - uz
              - vi
              - zh-hans
              - zh-hant
      responses:
        '200':
          content:
            application/vnd.oai.openapi:
              schema:
                type: object
                additionalProperties: {}
            application/yaml:
              schema:
                type: object
                additionalProperties: {}
            application/vnd.oai.openapi+json:
              schema:
                type: object
                additionalProperties: {}
            application/json:
              schema:
                type: object
                additionalProperties: {}
          description: ''
      security:
        - {}

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.ultravox.ai/llms.txt