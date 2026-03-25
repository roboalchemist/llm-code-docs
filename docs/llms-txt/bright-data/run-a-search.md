# Source: https://docs.brightdata.com/api-reference/archive-api/run-a-search.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run a Search

> To initiate a search of our Archive, use the following `/search` endpoint.

<Danger>
  **Mandatory**:\
  Either use `max_age` OR a combination of `min_date` + `max_date`
</Danger>

<Note>
  If the search takes longer than 30 seconds, the response returns only a `search_id` and you should poll the status asynchronously. If the search completes within 30 seconds, the response returns the full search result object (same as `GET /webarchive/search/<search_id>`).
</Note>

<Note>
  You can run up to 100 searches per day without triggering a dump.
  Once you trigger a dump, that search no longer count against your limit.
</Note>

<Accordion title="LIKE vs Regex Filters">
  * Use LIKE filters (`domain_like_*`, `url_like_*`) for simple pattern matching with `%` (any sequence) and `_` (single character).
  * LIKE patterns are case-insensitive and often faster than regex for simple prefix/suffix matching like `%.com` or `amazon%`.
  * Use regex filters (`domain_regex_*`, `url_regex_*`) for complex patterns requiring full regex syntax. LIKE patterns use backslash escaping: `\%` for literal `%`, `\_` for literal `_`.
</Accordion>


## OpenAPI

````yaml POST /webarchive/search
openapi: 3.1.0
info:
  title: BrightData Web Archive API
  version: 1.0.0
  description: API to search and retrieve archived web pages.
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /webarchive/search:
    post:
      summary: Run a search
      description: >-
        To initiate a search of our Archive, use the following `/search`
        endpoint.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                filters:
                  type: object
                  description: The filters used for this search (echoed back)
                  properties:
                    max_age:
                      type: string
                      description: >-
                        Limits results to records collected within a specified
                        time range. 


                        > **Mandatory**:  Either use `max_age` OR a combination
                        of `min_date` + `max_date`
                    min_date:
                      description: >-
                        Returns records collected on or after the specified
                        date. 


                        > **Mandatory**:  Either use `max_age` OR a combination
                        of `min_date` + `max_date`
                      type: string
                      format: date
                    max_date:
                      description: >-
                        Returns records collected on or before the specified
                        date. 


                        > **Mandatory**:  Either use `max_age` OR a combination
                        of `min_date` + `max_date`
                      type: string
                      format: date
                    domain_whitelist:
                      description: >-
                        Includes results only from listed domains. 


                        > **Tip**:  Either use `domain_whitelist` OR
                        `domain_blacklist` for best results.
                      type: array
                      items:
                        type: string
                    domain_blacklist:
                      description: >-
                        Excludes results from listed domains. 


                        > **Tip**:  Either use `domain_whitelist` OR
                        `domain_blacklist` for best results.
                      type: array
                      items:
                        type: string
                    domain_regex_whitelist:
                      description: >-
                        Includes results only matching the specified domain
                        regex pattern.
                      type: array
                      items:
                        type: string
                    domain_regex_blacklist:
                      description: >-
                        Excludes results matching the specified domain regex
                        pattern.
                      type: array
                      items:
                        type: string
                    domain_like_whitelist:
                      description: >-
                        Includes domains matching LIKE pattern (% = any chars, _
                        = single char). Case-insensitive.
                      type: array
                      items:
                        type: string
                    domain_like_blacklist:
                      description: >-
                        Excludes domains matching LIKE pattern.
                        Case-insensitive.
                      type: array
                      items:
                        type: string
                    category_whitelist:
                      description: Includes results only from specified categories.
                      type: array
                      items:
                        type: string
                    category_blacklist:
                      description: Excludes results from specified categories.
                      type: array
                      items:
                        type: string
                    url_regex_whitelist:
                      description: >-
                        Includes results only matching the specified URL regex
                        pattern.
                      type: array
                      items:
                        type: string
                    url_regex_blacklist:
                      description: >-
                        Excludes results matching the specified URL regex
                        pattern.
                      type: array
                      items:
                        type: string
                    url_like_whitelist:
                      description: >-
                        Includes URLs matching LIKE pattern (% = any chars, _ =
                        single char). Case-insensitive.
                      type: array
                      items:
                        type: string
                    url_like_blacklist:
                      description: Excludes URLs matching LIKE pattern. Case-insensitive.
                      type: array
                      items:
                        type: string
                    language_whitelist:
                      description: >-
                        Includes results only for specific language codes (ISO
                        639-3).
                      type: array
                      items:
                        type: string
                    language_blacklist:
                      description: Excludes results for specific language codes.
                      type: array
                      items:
                        type: string
                    ip_country_whitelist:
                      description: >-
                        Includes results collected through IPs or peers only
                        from specified countries.
                      type: array
                      items:
                        type: string
                    ip_country_blacklist:
                      description: >-
                        Excludes results collected through IPs or peers from
                        specified countries.
                      type: array
                      items:
                        type: string
                    captcha:
                      description: Return only results with captcha triggered
                      type: boolean
                    robots_block:
                      description: Return only results with robots block
                      type: boolean
                  required:
                    - max_age
              example:
                filters:
                  max_age: Duration
                  min_date: YYYY-MM-DD
                  max_date: YYYY-MM-DD
                  domain_whitelist:
                    - example.com
                  domain_blacklist:
                    - example.com
                  domain_regex_whitelist:
                    - .*example..*
                  domain_regex_blacklist:
                    - .*example..*
                  domain_like_whitelist:
                    - '%.example.%'
                    - example%
                  domain_like_blacklist:
                    - '%.example.ca'
                  category_whitelist:
                    - Automotive
                  category_blacklist:
                    - Automotive
                  url_regex_whitelist:
                    - .*/products/.*
                  url_regex_blacklist:
                    - .*/products/.*
                  url_like_whitelist:
                    - '%/products/%'
                    - '%/search%'
                  url_like_blacklist:
                    - '%/review/%'
                  language_whitelist:
                    - eng
                  language_blacklist:
                    - eng
                  ip_country_whitelist:
                    - us
                    - ie
                    - in
                  ip_country_blacklist:
                    - mx
                    - ae
                    - ca
                  captcha: true
                  robots_block: true
      responses:
        '200':
          description: Search initiated successfully
          content:
            application/json:
              schema:
                oneOf:
                  - title: Async (Still Running)
                    type: object
                    properties:
                      search_id:
                        type: string
                        description: Returned if search is async
                        example: ucd_abc123xyz
                    example:
                      search_id: ucd_abc123xyz
                  - title: Completed within 30s
                    type: object
                    properties:
                      search_id:
                        type: string
                        description: Unique identifier for the search
                      status:
                        type: string
                        description: 'Current status: `in_progress`, `done`, or `failed`'
                      filters:
                        type: object
                        description: The filters used for this search (echoed back)
                      files_count:
                        type: integer
                        description: Total number of matching files found
                      estimate_batch_count:
                        type: integer
                        description: Estimated number of batches for the dump
                      estimate_batch_size:
                        type: integer
                        description: Estimated total size in bytes
                      dump_cost_usd:
                        type: number
                        description: Estimated total cost to create a dump
                      cost_breakdown:
                        type: object
                        description: Breakdown of costs between cache and archive pages
                        properties:
                          archive_pages_count:
                            type: integer
                          archive_pages_cost:
                            type: number
                          cache_pages_count:
                            type: integer
                          cache_pages_cost:
                            type: number
                      estimate_dump_duration_sec:
                        type: integer
                        description: Estimated time to complete the dump in seconds
                      duration:
                        type: string
                        description: How long the search took to complete
                      error:
                        type: string
                        description: Error message (only present when status is `failed`)
                    example:
                      search_id: ucd_abc123xyz
                      status: done
                      filters:
                        domain_whitelist:
                          - example.com
                          - www.example.com
                        max_age: 1d
                        min_date: '2026-02-05T10:00:00.000Z'
                      files_count: 12341294
                      estimate_batch_count: 130
                      estimate_batch_size: 1073679195
                      dump_cost_usd: 2468.26
                      cost_breakdown:
                        archive_pages_count: 0
                        archive_pages_cost: 0
                        cache_pages_count: 12341294
                        cache_pages_cost: 2468.26
                      estimate_dump_duration_sec: 13000
                      duration: 4s210ms
              examples:
                Async (Still Running):
                  summary: 200 OK (async, search still running)
                  value:
                    search_id: ucd_abc123xyz
                Completed within 30s:
                  summary: 200 OK (completed within 30s)
                  value:
                    search_id: ucd_abc123xyz
                    status: done
                    filters:
                      domain_whitelist:
                        - example.com
                        - www.example.com
                      max_age: 1d
                      min_date: '2026-02-05T10:00:00.000Z'
                    files_count: 12341294
                    estimate_batch_count: 130
                    estimate_batch_size: 1073679195
                    dump_cost_usd: 2468.26
                    cost_breakdown:
                      archive_pages_count: 0
                      archive_pages_cost: 0
                      cache_pages_count: 12341294
                      cache_pages_cost: 2468.26
                    estimate_dump_duration_sec: 13000
                    duration: 4s210ms
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: >-
                      domain_blacklist cannot be used along with
                      domain_whitelist
components:
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