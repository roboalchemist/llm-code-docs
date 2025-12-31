# Source: https://docs.exa.ai/websets/api/monitors/runs/list-monitor-runs.md

# List Monitor Runs

> Lists all runs for the Monitor.

## OpenAPI

````yaml get /v0/monitors/{monitor}/runs
paths:
  path: /v0/monitors/{monitor}/runs
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
              description: The id of the Monitor to list runs for
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

          const runs = await exa.websets.monitors.runs.list('monitor_id');

          console.log(`Found ${runs.data.length} monitor runs`);
          runs.data.forEach(run => {
            console.log(`- ${run.id}: ${run.status}`);
          });
      - label: Python
        lang: python
        source: |-
          # pip install exa-py
          from exa_py import Exa
          exa = Exa('YOUR_EXA_API_KEY')

          runs = exa.websets.monitors.runs.list('monitor_id')

          print(f'Found {len(runs.data)} monitor runs')
          for run in runs.data:
              print(f'- {run.id}: {run.status}')
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type:
                      - array
                    items:
                      type:
                        - object
                      $ref: '#/components/schemas/MonitorRun'
                    description: The list of monitor runs
              hasMore:
                allOf:
                  - type:
                      - boolean
                    description: Whether there are more results to paginate through
              nextCursor:
                allOf:
                  - type: string
                    description: The cursor to paginate through the next set of results
                    nullable: true
            refIdentifier: '#/components/schemas/ListMonitorRunsResponse'
            requiredProperties:
              - data
              - hasMore
              - nextCursor
        examples:
          example:
            value:
              data:
                - id: <string>
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
              hasMore: true
              nextCursor: <string>
        description: List of monitor runs
  deprecated: false
  type: path
components:
  schemas:
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