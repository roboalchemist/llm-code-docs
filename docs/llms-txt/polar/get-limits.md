# Source: https://polar.sh/docs/api-reference/metrics/get-limits.md

# Get Metrics Limits

> Get the interval limits for the metrics endpoint.

**Scopes**: `metrics:read`

## OpenAPI

````yaml get /v1/metrics/limits
paths:
  path: /v1/metrics/limits
  method: get
  servers:
    - url: https://api.polar.sh
      description: Production environment
    - url: https://sandbox-api.polar.sh
      description: Sandbox environment
  request:
    security:
      - title: access token
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                You can generate an **Organization Access Token** from your
                organization's settings.
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: Go (SDK)
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\t\"os\"\n\tpolargo \"github.com/polarsource/polar-go\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := polargo.New(\n        polargo.WithSecurity(os.Getenv(\"POLAR_ACCESS_TOKEN\")),\n    )\n\n    res, err := s.Metrics.Limits(ctx)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.MetricsLimits != nil {\n        // handle response\n    }\n}"
      - label: Python (SDK)
        lang: python
        source: |-
          from polar_sdk import Polar


          with Polar(
              access_token="<YOUR_BEARER_TOKEN_HERE>",
          ) as polar:

              res = polar.metrics.limits()

              # Handle response
              print(res)
      - label: Typescript (SDK)
        lang: typescript
        source: |-
          import { Polar } from "@polar-sh/sdk";

          const polar = new Polar({
            accessToken: process.env["POLAR_ACCESS_TOKEN"] ?? "",
          });

          async function run() {
            const result = await polar.metrics.limits();

            console.log(result);
          }

          run();
      - label: PHP (SDK)
        lang: php
        source: |-
          declare(strict_types=1);

          require 'vendor/autoload.php';

          use Polar;

          $sdk = Polar\Polar::builder()
              ->setSecurity(
                  '<YOUR_BEARER_TOKEN_HERE>'
              )
              ->build();



          $response = $sdk->metrics->limits(

          );

          if ($response->metricsLimits !== null) {
              // handle response
          }
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              min_date:
                allOf:
                  - type: string
                    format: date
                    title: Min Date
                    description: Minimum date to get metrics.
              intervals:
                allOf:
                  - $ref: '#/components/schemas/MetricsIntervalsLimits'
                    description: Limits for each interval.
            title: MetricsLimits
            description: Date limits to get metrics.
            refIdentifier: '#/components/schemas/MetricsLimits'
            requiredProperties:
              - min_date
              - intervals
        examples:
          example:
            value:
              min_date: '2023-12-25'
              intervals:
                hour:
                  max_days: 123
                day:
                  max_days: 123
                week:
                  max_days: 123
                month:
                  max_days: 123
                year:
                  max_days: 123
        description: Successful Response
  deprecated: false
  type: path
components:
  schemas:
    MetricsIntervalLimit:
      properties:
        max_days:
          type: integer
          title: Max Days
          description: Maximum number of days for this interval.
      type: object
      required:
        - max_days
      title: MetricsIntervalLimit
      description: Date interval limit to get metrics for a given interval.
    MetricsIntervalsLimits:
      properties:
        hour:
          $ref: '#/components/schemas/MetricsIntervalLimit'
          description: Limits for the hour interval.
        day:
          $ref: '#/components/schemas/MetricsIntervalLimit'
          description: Limits for the day interval.
        week:
          $ref: '#/components/schemas/MetricsIntervalLimit'
          description: Limits for the week interval.
        month:
          $ref: '#/components/schemas/MetricsIntervalLimit'
          description: Limits for the month interval.
        year:
          $ref: '#/components/schemas/MetricsIntervalLimit'
          description: Limits for the year interval.
      type: object
      required:
        - hour
        - day
        - week
        - month
        - year
      title: MetricsIntervalsLimits
      description: Date interval limits to get metrics for each interval.

````