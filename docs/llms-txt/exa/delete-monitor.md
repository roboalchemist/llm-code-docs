# Source: https://docs.exa.ai/websets/api/monitors/delete-monitor.md

# Delete Monitor

> Deletes a monitor.

## OpenAPI

````yaml delete /v0/monitors/{id}
paths:
  path: /v0/monitors/{id}
  method: delete
  servers:
    - url: https://api.exa.ai/websets/
      description: Production
  request:
    security:
      - title: api key
        parameters:
          query: {}
          header:
            x-api-key:
              type: apiKey
              description: Your Exa API key
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              description: The id of the Monitor
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: JavaScript
        lang: javascript
        source: |-
          // npm install exa-js
          import Exa from 'exa-js';
          const exa = new Exa('YOUR_EXA_API_KEY');

          await exa.websets.monitors.delete('monitor_id');

          console.log('Monitor deleted successfully');
      - label: Python
        lang: python
        source: |-
          # pip install exa-py
          from exa_py import Exa
          exa = Exa('YOUR_EXA_API_KEY')

          exa.websets.monitors.delete('monitor_id')

          print('Monitor deleted successfully')
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type:
                      - string
                    description: The unique identifier for the Monitor
              object:
                allOf:
                  - type:
                      - string
                    enum:
                      - monitor
                    description: The type of object
              status:
                allOf:
                  - type:
                      - string
                    enum:
                      - enabled
                      - disabled
                    description: The status of the Monitor
              websetId:
                allOf:
                  - type:
                      - string
                    description: The id of the Webset the Monitor belongs to
              cadence:
                allOf:
                  - type:
                      - object
                    properties:
                      cron:
                        description: >-
                          Cron expression for monitor cadence (must be a valid
                          Unix cron with 5 fields). The schedule must trigger at
                          most once per day.
                        type:
                          - string
                      timezone:
                        description: IANA timezone (e.g., "America/New_York")
                        default: Etc/UTC
                        type:
                          - string
                    required:
                      - cron
                    description: How often the monitor will run
              behavior:
                allOf:
                  - type:
                      - object
                    properties:
                      type:
                        type: string
                        const: search
                        default: search
                      config:
                        type:
                          - object
                        properties:
                          query:
                            type:
                              - string
                            minLength: 2
                            maxLength: 10000
                            description: >-
                              The query to search for. By default, the query
                              from the last search is used.
                          criteria:
                            type:
                              - array
                            items:
                              type:
                                - object
                              properties:
                                description:
                                  type:
                                    - string
                                  minLength: 2
                                  maxLength: 1000
                              required:
                                - description
                            maxItems: 5
                            description: >-
                              The criteria to search for. By default, the
                              criteria from the last search is used.
                          entity:
                            $ref: '#/components/schemas/Entity'
                            title: Entity
                            description: >-
                              The entity to search for. By default, the entity
                              from the last search/import is used.
                          count:
                            type:
                              - number
                            exclusiveMinimum: 0
                            description: The maximum number of results to find
                          behavior:
                            default: append
                            type:
                              - string
                            enum:
                              - override
                              - append
                            description: >-
                              The behaviour of the Search when it is added to a
                              Webset.
                        required:
                          - count
                        description: >-
                          Specify the search parameters for the Monitor.


                          By default, the search parameters (query, entity and
                          criteria) from the last search are used when no
                          parameters are provided.
                    required:
                      - type
                      - config
                    description: Behavior to perform when monitor runs
              lastRun:
                allOf:
                  - type: object
                    $ref: '#/components/schemas/MonitorRun'
                    title: MonitorRun
                    description: The last run of the monitor
                    nullable: true
              nextRunAt:
                allOf:
                  - type: string
                    format: date-time
                    description: Date and time when the next run will occur in
                    nullable: true
              metadata:
                allOf:
                  - description: >-
                      Set of key-value pairs you want to associate with this
                      object.
                    type:
                      - object
                    additionalProperties:
                      type:
                        - string
                      maxLength: 1000
              createdAt:
                allOf:
                  - type:
                      - string
                    format: date-time
                    description: When the monitor was created
              updatedAt:
                allOf:
                  - type:
                      - string
                    format: date-time
                    description: When the monitor was last updated
            refIdentifier: '#/components/schemas/Monitor'
            requiredProperties:
              - id
              - object
              - status
              - websetId
              - cadence
              - behavior
              - lastRun
              - nextRunAt
              - metadata
              - createdAt
              - updatedAt
        examples:
          example:
            value:
              id: <string>
              object: monitor
              status: enabled
              websetId: <string>
              cadence:
                cron: <string>
                timezone: Etc/UTC
              behavior:
                type: search
                config:
                  query: <string>
                  criteria:
                    - description: <string>
                  entity:
                    type: company
                  count: 123
                  behavior: append
              lastRun:
                id: <string>
                object: monitor_run
                status: created
                monitorId: <string>
                type: search
                completedAt: '2023-11-07T05:31:56Z'
                failedAt: '2023-11-07T05:31:56Z'
                failedReason: <string>
                canceledAt: '2023-11-07T05:31:56Z'
                createdAt: '2023-11-07T05:31:56Z'
                updatedAt: '2023-11-07T05:31:56Z'
              nextRunAt: '2023-11-07T05:31:56Z'
              metadata: {}
              createdAt: '2023-11-07T05:31:56Z'
              updatedAt: '2023-11-07T05:31:56Z'
        description: Monitor deleted successfully
  deprecated: false
  type: path
components:
  schemas:
    CompanyEntity:
      type:
        - object
      properties:
        type:
          type: string
          const: company
          default: company
      required:
        - type
      title: Company
    PersonEntity:
      type:
        - object
      properties:
        type:
          type: string
          const: person
          default: person
      required:
        - type
      title: Person
    ArticleEntity:
      type:
        - object
      properties:
        type:
          type: string
          const: article
          default: article
      required:
        - type
      title: Article
    ResearchPaperEntity:
      type:
        - object
      properties:
        type:
          type: string
          const: research_paper
          default: research_paper
      required:
        - type
      title: Research Paper
    CustomEntity:
      type:
        - object
      properties:
        type:
          type: string
          const: custom
          default: custom
        description:
          type:
            - string
          minLength: 2
          maxLength: 200
      required:
        - type
        - description
      title: Custom
    Entity:
      oneOf:
        - type:
            - object
          $ref: '#/components/schemas/CompanyEntity'
        - type:
            - object
          $ref: '#/components/schemas/PersonEntity'
        - type:
            - object
          $ref: '#/components/schemas/ArticleEntity'
        - type:
            - object
          $ref: '#/components/schemas/ResearchPaperEntity'
        - type:
            - object
          $ref: '#/components/schemas/CustomEntity'
    MonitorRun:
      type:
        - object
      properties:
        id:
          type:
            - string
          description: The unique identifier for the Monitor Run
        object:
          type:
            - string
          enum:
            - monitor_run
          description: The type of object
        status:
          type:
            - string
          enum:
            - created
            - running
            - completed
            - canceled
            - failed
          description: The status of the Monitor Run
        monitorId:
          type:
            - string
          description: The monitor that the run is associated with
        type:
          type:
            - string
          enum:
            - search
            - refresh
          description: The type of the Monitor Run
        completedAt:
          type: string
          format: date-time
          description: When the run completed
          nullable: true
        failedAt:
          type: string
          format: date-time
          description: When the run failed
          nullable: true
        failedReason:
          type: string
          description: The reason the run failed
          nullable: true
        canceledAt:
          type: string
          format: date-time
          description: When the run was canceled
          nullable: true
        createdAt:
          type:
            - string
          format: date-time
          description: When the run was created
        updatedAt:
          type:
            - string
          format: date-time
          description: When the run was last updated
      required:
        - id
        - object
        - monitorId
        - status
        - type
        - completedAt
        - failedAt
        - failedReason
        - canceledAt
        - createdAt
        - updatedAt

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt