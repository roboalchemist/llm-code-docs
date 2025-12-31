# Source: https://polar.sh/docs/api-reference/meters/get-quantities.md

# Get Meter Quantities

> Get quantities of a meter over a time period.

**Scopes**: `meters:read` `meters:write`

## OpenAPI

````yaml get /v1/meters/{id}/quantities
paths:
  path: /v1/meters/{id}/quantities
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
      path:
        id:
          schema:
            - type: string
              required: true
              title: Id
              description: The meter ID.
              format: uuid4
      query:
        start_timestamp:
          schema:
            - type: string
              required: true
              title: Start Timestamp
              description: Start timestamp.
              format: date-time
        end_timestamp:
          schema:
            - type: string
              required: true
              title: End Timestamp
              description: End timestamp.
              format: date-time
        interval:
          schema:
            - type: enum<string>
              enum:
                - year
                - month
                - week
                - day
                - hour
              required: true
              title: TimeInterval
              description: Interval between two timestamps.
        customer_id:
          schema:
            - type: string
              required: false
              title: CustomerID Filter
              description: |-
                Filter by customer ID.
                The customer ID.
              format: uuid4
            - type: array
              items:
                allOf:
                  - type: string
                    format: uuid4
                    description: The customer ID.
              required: false
              title: CustomerID Filter
              description: Filter by customer ID.
            - type: 'null'
              required: false
              title: CustomerID Filter
              description: Filter by customer ID.
        external_customer_id:
          schema:
            - type: string
              required: false
              title: ExternalCustomerID Filter
              description: Filter by external customer ID.
            - type: array
              items:
                allOf:
                  - type: string
              required: false
              title: ExternalCustomerID Filter
              description: Filter by external customer ID.
            - type: 'null'
              required: false
              title: ExternalCustomerID Filter
              description: Filter by external customer ID.
        customer_aggregation_function:
          schema:
            - type: enum<string>
              enum:
                - count
                - sum
                - max
                - min
                - avg
                - unique
              required: false
              title: AggregationFunction
              description: >-
                If set, will first compute the quantities per customer before
                aggregating them using the given function. If not set, the
                quantities will be aggregated across all events.
              refIdentifier: '#/components/schemas/AggregationFunction'
            - type: 'null'
              required: false
              title: Customer Aggregation Function
              description: >-
                If set, will first compute the quantities per customer before
                aggregating them using the given function. If not set, the
                quantities will be aggregated across all events.
        metadata:
          schema:
            - type: object
              properties: {}
              required: false
              title: MetadataQuery
              description: >-
                Filter by metadata key-value pairs. It uses the `deepObject`
                style, e.g. `?metadata[key]=value`.
              additionalProperties:
                allOf:
                  - anyOf:
                      - type: string
                      - type: integer
                      - type: boolean
                      - type: array
                        items:
                          type: string
                      - type: array
                        items:
                          type: integer
                      - type: array
                        items:
                          type: boolean
            - type: 'null'
              required: false
              title: MetadataQuery
              description: >-
                Filter by metadata key-value pairs. It uses the `deepObject`
                style, e.g. `?metadata[key]=value`.
          style: deepObject
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: Go (SDK)
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\t\"os\"\n\tpolargo \"github.com/polarsource/polar-go\"\n\t\"github.com/polarsource/polar-go/types\"\n\t\"github.com/polarsource/polar-go/models/components\"\n\t\"github.com/polarsource/polar-go/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := polargo.New(\n        polargo.WithSecurity(os.Getenv(\"POLAR_ACCESS_TOKEN\")),\n    )\n\n    res, err := s.Meters.Quantities(ctx, operations.MetersQuantitiesRequest{\n        ID: \"<value>\",\n        StartTimestamp: types.MustTimeFromString(\"2025-11-25T04:37:16.823Z\"),\n        EndTimestamp: types.MustTimeFromString(\"2025-11-26T17:06:00.727Z\"),\n        Interval: components.TimeIntervalDay,\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.MeterQuantities != nil {\n        // handle response\n    }\n}"
      - label: Python (SDK)
        lang: python
        source: |-
          import polar_sdk
          from polar_sdk import Polar
          from polar_sdk.utils import parse_datetime


          with Polar(
              access_token="<YOUR_BEARER_TOKEN_HERE>",
          ) as polar:

              res = polar.meters.quantities(id="<value>", start_timestamp=parse_datetime("2025-11-25T04:37:16.823Z"), end_timestamp=parse_datetime("2025-11-26T17:06:00.727Z"), interval=polar_sdk.TimeInterval.DAY)

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
            const result = await polar.meters.quantities({
              id: "<value>",
              startTimestamp: new Date("2025-11-25T04:37:16.823Z"),
              endTimestamp: new Date("2025-11-26T17:06:00.727Z"),
              interval: "day",
            });

            console.log(result);
          }

          run();
      - label: PHP (SDK)
        lang: php
        source: |-
          declare(strict_types=1);

          require 'vendor/autoload.php';

          use Polar;
          use Polar\Models\Components;
          use Polar\Models\Operations;
          use Polar\Utils;

          $sdk = Polar\Polar::builder()
              ->setSecurity(
                  '<YOUR_BEARER_TOKEN_HERE>'
              )
              ->build();

          $request = new Operations\MetersQuantitiesRequest(
              id: '<value>',
              startTimestamp: Utils\Utils::parseDateTime('2025-11-25T04:37:16.823Z'),
              endTimestamp: Utils\Utils::parseDateTime('2025-11-26T17:06:00.727Z'),
              interval: Components\TimeInterval::Day,
          );

          $response = $sdk->meters->quantities(
              request: $request
          );

          if ($response->meterQuantities !== null) {
              // handle response
          }
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              quantities:
                allOf:
                  - items:
                      $ref: '#/components/schemas/MeterQuantity'
                    type: array
                    title: Quantities
              total:
                allOf:
                  - type: number
                    title: Total
                    description: The total quantity for the period.
                    examples:
                      - 100
            title: MeterQuantities
            refIdentifier: '#/components/schemas/MeterQuantities'
            requiredProperties:
              - quantities
              - total
        examples:
          example:
            value:
              quantities:
                - timestamp: '2023-11-07T05:31:56Z'
                  quantity: 10
              total: 100
        description: Successful Response
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    const: ResourceNotFound
                    title: Error
                    examples:
                      - ResourceNotFound
              detail:
                allOf:
                  - type: string
                    title: Detail
            title: ResourceNotFound
            refIdentifier: '#/components/schemas/ResourceNotFound'
            requiredProperties:
              - error
              - detail
        examples:
          example:
            value:
              error: ResourceNotFound
              detail: <string>
        description: Meter not found.
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ValidationError'
                    type: array
                    title: Detail
            title: HTTPValidationError
            refIdentifier: '#/components/schemas/HTTPValidationError'
        examples:
          example:
            value:
              detail:
                - loc:
                    - <string>
                  msg: <string>
                  type: <string>
        description: Validation Error
  deprecated: false
  type: path
components:
  schemas:
    MeterQuantity:
      properties:
        timestamp:
          type: string
          format: date-time
          title: Timestamp
          description: The timestamp for the current period.
        quantity:
          type: number
          title: Quantity
          description: The quantity for the current period.
          examples:
            - 10
      type: object
      required:
        - timestamp
        - quantity
      title: MeterQuantity
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````