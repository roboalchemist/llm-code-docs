# Source: https://mintlify.com/docs/api/update/status.md

# Get update status

> Get the status of an update from the status ID

## OpenAPI

````yaml GET /project/update-status/{statusId}
paths:
  path: /project/update-status/{statusId}
  method: get
  servers:
    - url: https://api.mintlify.com/v1
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path:
        statusId:
          schema:
            - type: string
              required: true
              description: The status ID of a triggered update.
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              _id:
                allOf:
                  - type: string
                    description: The status ID of the triggered updated.
              projectId:
                allOf:
                  - type: string
                    description: The documentation project ID.
              createdAt:
                allOf:
                  - type: string
                    description: An ISODate with the specified datetime in UTC
              endedAt:
                allOf:
                  - type: string
                    description: An ISODate with the specified datetime in UTC
              status:
                allOf:
                  - type: string
                    enum:
                      - queued
                      - in_progress
                      - success
                      - failure
                    description: The status of the update.
              summary:
                allOf:
                  - type: string
                    description: Summary of the status of the update
              logs:
                allOf:
                  - type: array
                    description: An array of logs.
                    items:
                      type: string
              subdomain:
                allOf:
                  - type: string
                    description: The subdomain of the docs being updated.
              screenshot:
                allOf:
                  - type: string
                    description: A screenshot of the docs.
              screenshotLight:
                allOf:
                  - type: string
                    description: A screenshot of the docs.
              screenshotDark:
                allOf:
                  - type: string
                    description: A screenshot of the docs in dark mode.
              author:
                allOf:
                  - type: string
                    description: The author of the update.
              commit:
                allOf:
                  - type: object
                    description: The commit details
                    properties:
                      sha:
                        type: string
                        description: The SHA of the commit.
                      ref:
                        type: string
                        description: The ref of the commit.
                      message:
                        type: string
                        description: The commit message.
                      filesChanged:
                        type: object
                        description: Details on the changed files.
                        properties:
                          added:
                            type: array
                            description: New files added.
                            items:
                              type: string
                          modified:
                            type: array
                            description: Existing files that were modified.
                            items:
                              type: string
                          removed:
                            type: array
                            description: Files that were removed.
                            items:
                              type: string
              source:
                allOf:
                  - type: string
                    description: The source of the update trigger.
                    enum:
                      - internal
                      - github-app-installation
                      - api
                      - github
                      - dashboard
        examples:
          example:
            value:
              _id: <string>
              projectId: <string>
              createdAt: <string>
              endedAt: <string>
              status: queued
              summary: <string>
              logs:
                - <string>
              subdomain: <string>
              screenshot: <string>
              screenshotLight: <string>
              screenshotDark: <string>
              author: <string>
              commit:
                sha: <string>
                ref: <string>
                message: <string>
                filesChanged:
                  added:
                    - <string>
                  modified:
                    - <string>
                  removed:
                    - <string>
              source: internal
        description: A successful response
  deprecated: false
  type: path
components:
  schemas: {}

````