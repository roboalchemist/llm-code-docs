# Source: https://polar.sh/docs/api-reference/events/ingest.md

# Ingest Events

> Ingest batch of events.

**Scopes**: `events:write`

## OpenAPI

````yaml post /v1/events/ingest
paths:
  path: /v1/events/ingest
  method: post
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              events:
                allOf:
                  - items:
                      anyOf:
                        - $ref: '#/components/schemas/EventCreateCustomer'
                        - $ref: '#/components/schemas/EventCreateExternalCustomer'
                    type: array
                    title: Events
                    description: List of events to ingest.
            required: true
            title: EventsIngest
            refIdentifier: '#/components/schemas/EventsIngest'
            requiredProperties:
              - events
        examples:
          example:
            value:
              events:
                - timestamp: '2023-11-07T05:31:56Z'
                  name: <string>
                  organization_id: 1dbfc517-0bbf-4301-9ba8-555ca42b9737
                  metadata: {}
                  customer_id: <string>
    codeSamples:
      - label: Go (SDK)
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\t\"os\"\n\tpolargo \"github.com/polarsource/polar-go\"\n\t\"github.com/polarsource/polar-go/models/components\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := polargo.New(\n        polargo.WithSecurity(os.Getenv(\"POLAR_ACCESS_TOKEN\")),\n    )\n\n    res, err := s.Events.Ingest(ctx, components.EventsIngest{\n        Events: []components.Events{},\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.EventsIngestResponse != nil {\n        // handle response\n    }\n}"
      - label: Python (SDK)
        lang: python
        source: |-
          from polar_sdk import Polar


          with Polar(
              access_token="<YOUR_BEARER_TOKEN_HERE>",
          ) as polar:

              res = polar.events.ingest(request={
                  "events": [],
              })

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
            const result = await polar.events.ingest({
              events: [],
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

          $sdk = Polar\Polar::builder()
              ->setSecurity(
                  '<YOUR_BEARER_TOKEN_HERE>'
              )
              ->build();

          $request = new Components\EventsIngest(
              events: [],
          );

          $response = $sdk->events->ingest(
              request: $request
          );

          if ($response->eventsIngestResponse !== null) {
              // handle response
          }
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              inserted:
                allOf:
                  - type: integer
                    title: Inserted
                    description: Number of events inserted.
            title: EventsIngestResponse
            refIdentifier: '#/components/schemas/EventsIngestResponse'
            requiredProperties:
              - inserted
        examples:
          example:
            value:
              inserted: 123
        description: Successful Response
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
    CostMetadata-Input:
      properties:
        amount:
          anyOf:
            - type: number
            - type: string
              pattern: >-
                ^(?!^[-+.]*$)[+-]?0*(?:\d{0,5}|(?=[\d.]{1,18}0*$)\d{0,5}\.\d{0,12}0*$)
          title: Amount
          description: The amount in cents.
        currency:
          type: string
          pattern: usd
          title: Currency
          description: The currency. Currently, only `usd` is supported.
      type: object
      required:
        - amount
        - currency
      title: CostMetadata
    EventCreateCustomer:
      properties:
        timestamp:
          type: string
          format: date-time
          title: Timestamp
          description: The timestamp of the event.
        name:
          type: string
          title: Name
          description: The name of the event.
        organization_id:
          anyOf:
            - type: string
              format: uuid4
              description: The organization ID.
              examples:
                - 1dbfc517-0bbf-4301-9ba8-555ca42b9737
              x-polar-selector-widget:
                displayProperty: name
                resourceName: Organization
                resourceRoot: /v1/organizations
            - type: 'null'
          title: Organization Id
          description: >-
            The ID of the organization owning the event. **Required unless you
            use an organization token.**
        metadata:
          $ref: '#/components/schemas/EventMetadataInput'
          description: >-
            Key-value object allowing you to store additional information about
            the event. Some keys like `_llm` are structured data that are
            handled specially by Polar.


            The key must be a string with a maximum length of **40 characters**.

            The value must be either:


            * A string with a maximum length of **500 characters**

            * An integer

            * A floating-point number

            * A boolean


            You can store up to **50 key-value pairs**.
        customer_id:
          type: string
          format: uuid4
          title: Customer Id
          description: >-
            ID of the customer in your Polar organization associated with the
            event.
      type: object
      required:
        - name
        - customer_id
      title: EventCreateCustomer
    EventCreateExternalCustomer:
      properties:
        timestamp:
          type: string
          format: date-time
          title: Timestamp
          description: The timestamp of the event.
        name:
          type: string
          title: Name
          description: The name of the event.
        organization_id:
          anyOf:
            - type: string
              format: uuid4
              description: The organization ID.
              examples:
                - 1dbfc517-0bbf-4301-9ba8-555ca42b9737
              x-polar-selector-widget:
                displayProperty: name
                resourceName: Organization
                resourceRoot: /v1/organizations
            - type: 'null'
          title: Organization Id
          description: >-
            The ID of the organization owning the event. **Required unless you
            use an organization token.**
        metadata:
          $ref: '#/components/schemas/EventMetadataInput'
          description: >-
            Key-value object allowing you to store additional information about
            the event. Some keys like `_llm` are structured data that are
            handled specially by Polar.


            The key must be a string with a maximum length of **40 characters**.

            The value must be either:


            * A string with a maximum length of **500 characters**

            * An integer

            * A floating-point number

            * A boolean


            You can store up to **50 key-value pairs**.
        external_customer_id:
          type: string
          title: External Customer Id
          description: ID of the customer in your system associated with the event.
      type: object
      required:
        - name
        - external_customer_id
      title: EventCreateExternalCustomer
    EventMetadataInput:
      additionalProperties:
        anyOf:
          - type: string
            maxLength: 500
            minLength: 1
          - type: integer
          - type: number
          - type: boolean
          - $ref: '#/components/schemas/CostMetadata-Input'
          - $ref: '#/components/schemas/LLMMetadata'
      type: object
      title: EventMetadataInput
    LLMMetadata:
      properties:
        vendor:
          type: string
          title: Vendor
          description: The vendor of the event.
        model:
          type: string
          title: Model
          description: The model used for the event.
        prompt:
          anyOf:
            - type: string
            - type: 'null'
          title: Prompt
          description: The LLM prompt used for the event.
        response:
          anyOf:
            - type: string
            - type: 'null'
          title: Response
          description: The LLM response used for the event.
        input_tokens:
          type: integer
          title: Input Tokens
          description: The number of LLM input tokens used for the event.
        cached_input_tokens:
          type: integer
          title: Cached Input Tokens
          description: The number of LLM cached tokens that were used for the event.
        output_tokens:
          type: integer
          title: Output Tokens
          description: The number of LLM output tokens used for the event.
        total_tokens:
          type: integer
          title: Total Tokens
          description: The total number of LLM tokens used for the event.
      type: object
      required:
        - vendor
        - model
        - input_tokens
        - output_tokens
        - total_tokens
      title: LLMMetadata
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