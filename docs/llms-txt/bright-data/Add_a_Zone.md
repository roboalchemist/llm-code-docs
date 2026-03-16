# Source: https://docs.brightdata.com/api-reference/account-management-api/Add_a_Zone.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add a Zone

> Add a new zone

<Warning> **Warning:** This API can modify your account settings, damage your operations or incur charges.</Warning>

<Tip>
  Paste your API key to the authorization field. To get an API key, [Create an account](https://brightdata.com/?hs_signup=1\&utm_source=docs\&utm_campaign=playground) and learn [how to generate an API key](/api-reference/authentication#how-do-i-generate-a-new-api-key%3F)
</Tip>


## OpenAPI

````yaml openapi POST /zone
openapi: 3.0.1
info:
  title: Bright Data API
  description: >-
    Integrate Bright Data APIs to your pipeline and secure high-end scraping
    precision
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /zone:
    post:
      description: Add a new zone
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/NewZoneBody'
      responses:
        '201':
          description: Zone added
components:
  schemas:
    NewZoneBody:
      required:
        - zone
        - plan
      type: object
      properties:
        zone:
          $ref: '#/components/schemas/Zone'
        plan:
          $ref: '#/components/schemas/Plan'
    Zone:
      required:
        - name
      type: object
      properties:
        name:
          description: The name of the zone
          type: string
        type:
          description: Zone Type, e.g. serp, isp, mobile, etc.
          type: string
      example:
        name: zone-name
        type: serp
    Plan:
      required:
        - type
      type: object
      properties:
        type:
          description: type of zone
          type: string
          enum:
            - static
            - resident
            - unblocker
            - browser_api
        domain_whitelist:
          description: Space separated list of allowlisted domains
          type: string
        ips_type:
          description: '`domain_whitelist` is required for `selective`'
          type: string
          enum:
            - shared
            - dedicated
            - selective
        bandwidth:
          description: '`bandwidth`: for bandwidth `unlimited`: enable unlimited bandwidth'
          type: string
          enum:
            - bandwidth
            - unlimited
        ip_alloc_preset:
          description: To set a zone with Shared - Pay per usage type
          type: string
          enum:
            - shared_block
            - shared_res_block
        ips:
          description: Number of static IPs to allocate to the zone
          type: integer
          default: 0
        country:
          description: >-
            Specify which country IP to allocate to the zone, specify this
            parameter when `ips_type=static`
          type: string
          default: any
        country_city:
          description: >-
            Country code followed by city (e.g. “se-stockholm”) - specify which
            City IP to allocate to the zone, specify this parameter when
            `ips_type=static`
          type: string
          default: any
        mobile:
          description: >-
            `true` when adding a Mobile proxy zone, type value must be
            `resident`
          type: boolean
          default: 'false'
        serp:
          description: '`true` when adding a SERP API zone'
          type: boolean
          default: 'false'
        city:
          description: '`true` when enabling City targeting permission'
          type: boolean
          default: 'false'
        asn:
          description: '`true` when enabling ASN targeting permission'
          type: boolean
          default: 'false'
        vip:
          description: '`true` when allocating `gIP` (group of IPs)'
          type: boolean
          default: 'false'
        vips_type:
          description: specify this parameter when adding a Residential or Mobile zone
          type: string
          enum:
            - shared
            - domain
        vips:
          description: Number of `gIP` (group of IPs) to allocate to the zone
          type: integer
          default: '0'
        vip_country:
          description: >-
            Specify which country IP to allocate to the zone, specify this
            parameter when `ips_type=resident` and `vip=true`
          type: string
        vip_country_city:
          description: >-
            Country code followed by city (e.g. “se-stockholm”) - specify which
            City IP to allocate to the zone, specify this parameter when
            `ips_type=resident` and `vip=true`
          type: string
          default: any
        pool_ip_type:
          description: >-
            When `pool_ip_type` is set to `static_res`, the zone will use ISP
            IPs instead of data center IPs.
          type: string
        ub_premium:
          description: When set to `true` will enable access to premium domain.
          type: boolean
          default: false
        solve_captcha_disable:
          description: When set to `true` it will disable captcha solving.
          type: boolean
          default: true
        custom_headers:
          description: >-
            When set to `true`, allows users to include custom headers in their
            requests.
          type: boolean
          default: false
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Use your Bright Data API Key as a Bearer token in the Authorization
        header.


        **How to authenticate:**

        1. Obtain your API Key from the Bright Data account settings at
        https://brightdata.com/cp/setting/users

        2. Include the API Key in the Authorization header of your requests

        3. Format: `Authorization: Bearer YOUR_API_KEY`


        **Example:**

        ```

        Authorization: Bearer
        b5648e1096c6442f60a6c4bbbe73f8d2234d3d8324554bd6a7ec8f3f251f07df

        ```


        Learn how to get your Bright Data API key:
        https://docs.brightdata.com/api-reference/authentication
      bearerFormat: API Key

````