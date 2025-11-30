# Source: https://docs.exa.ai/websets/api/monitors/runs/get-monitor-run.md

# Get Monitor Run

> Gets a specific monitor run.

## OpenAPI

````yaml get /v0/monitors/{monitor}/runs/{id}
paths:
  path: /v0/monitors/{monitor}/runs/{id}
  method: get
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
        monitor:
          schema:
            - type: string
              required: true
              description: The id of the Monitor to get the run for
        id:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: JavaScript
        lang: javascript
        source: >-
          // npm install exa-js

          import Exa from 'exa-js';

          const exa = new Exa('YOUR_EXA_API_KEY');


          const run = await exa.websets.monitors.runs.get('monitor_id',
          'run_id');


          console.log(`Monitor run: ${run.id} - ${run.status}`);
      - label: Python
        lang: python
        source: |-
          # pip install exa-py
          from exa_py import Exa
          exa = Exa('YOUR_EXA_API_KEY')

          run = exa.websets.monitors.runs.get('monitor_id', 'run_id')

          print(f'Monitor run: {run.id} - {run.status}')
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
                    description: The unique identifier for the Monitor Run
              object:
                allOf:
                  - type:
                      - string
                    enum:
                      - monitor_run
                    description: The type of object
              status:
                allOf:
                  - type:
                      - string
                    enum:
                      - created
                      - running
                      - completed
                      - canceled
                      - failed
                    description: The status of the Monitor Run
              monitorId:
                allOf:
                  - type:
                      - string
                    description: The monitor that the run is associated with
              type:
                allOf:
                  - type:
                      - string
                    enum:
                      - search
                      - refresh
                    description: The type of the Monitor Run
              completedAt:
                allOf:
                  - type: string
                    format: date-time
                    description: When the run completed
                    nullable: true
              failedAt:
                allOf:
                  - type: string
                    format: date-time
                    description: When the run failed
                    nullable: true
              failedReason:
                allOf:
                  - type: string
                    description: The reason the run failed
                    nullable: true
              canceledAt:
                allOf:
                  - type: string
                    format: date-time
                    description: When the run was canceled
                    nullable: true
              createdAt:
                allOf:
                  - type:
                      - string
                    format: date-time
                    description: When the run was created
              updatedAt:
                allOf:
                  - type:
                      - string
                    format: date-time
                    description: When the run was last updated
            refIdentifier: '#/components/schemas/MonitorRun'
            requiredProperties:
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
        examples:
          example:
            value:
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
        description: Monitor run details
  deprecated: false
  type: path
components:
  schemas: {}

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt