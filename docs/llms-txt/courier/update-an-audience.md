# Source: https://www.courier.com/docs/api-reference/audiences/update-an-audience.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update an audience

> Creates or updates audience.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml put /audiences/{audience_id}
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /audiences/{audience_id}:
    put:
      tags:
        - Audiences
      summary: Update an audience
      description: Creates or updates audience.
      operationId: audiences_update
      parameters:
        - name: audience_id
          in: path
          description: A unique identifier representing the audience id
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  nullable: true
                  description: The name of the audience
                description:
                  type: string
                  nullable: true
                  description: A description of the audience
                operator:
                  $ref: '#/components/schemas/LogicalOperator'
                  nullable: true
                  description: The logical operator (AND/OR) for the top-level filter
                filter:
                  $ref: '#/components/schemas/AudienceFilterConfig'
                  nullable: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AudienceUpdateResponse'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: |-
            import Courier from '@trycourier/courier';

            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });

            const audience = await client.audiences.update('audience_id');

            console.log(audience.audience);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            audience = client.audiences.update(
                audience_id="audience_id",
            )
            print(audience.audience)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\taudience, err := client.Audiences.Update(\n\t\tcontext.TODO(),\n\t\t\"audience_id\",\n\t\tcourier.AudienceUpdateParams{},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", audience.Audience)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.audiences.AudienceUpdateParams;
            import com.courier.models.audiences.AudienceUpdateResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    AudienceUpdateResponse audience = client.audiences().update("audience_id");
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            audience = courier.audiences.update("audience_id")

            puts(audience)
components:
  schemas:
    LogicalOperator:
      title: LogicalOperator
      type: string
      enum:
        - AND
        - OR
    AudienceFilterConfig:
      title: AudienceFilterConfig
      type: object
      description: >-
        Filter configuration for audience membership containing an array of
        filter rules
      properties:
        filters:
          type: array
          items:
            $ref: '#/components/schemas/FilterConfig'
          description: Array of filter rules (single conditions or nested groups)
      required:
        - filters
    AudienceUpdateResponse:
      title: AudienceUpdateResponse
      type: object
      properties:
        audience:
          $ref: '#/components/schemas/Audience'
      required:
        - audience
    FilterConfig:
      title: FilterConfig
      type: object
      description: >-
        A filter rule that can be either a single condition (with path/value) or
        a  nested group (with filters array). Use comparison operators (EQ, GT,
        etc.)  for single conditions, and logical operators (AND, OR) for nested
        groups.
      properties:
        operator:
          type: string
          description: >-
            The operator for this filter. Use comparison operators (EQ, GT, LT,
            GTE, LTE,  NEQ, EXISTS, INCLUDES, STARTS_WITH, ENDS_WITH, IS_BEFORE,
            IS_AFTER, OMIT) for  single conditions, or logical operators (AND,
            OR) for nested filter groups.
        path:
          type: string
          description: >-
            The attribute path from the user profile to filter on. Required for
            single  filter conditions, not used for nested filter groups.
        value:
          type: string
          description: >-
            The value to compare against. Required for single filter
            conditions,  not used for nested filter groups.
        filters:
          type: array
          items:
            $ref: '#/components/schemas/FilterConfig'
          description: >-
            Nested filter rules to combine with AND/OR. Required for nested
            filter groups, not used for single filter conditions.
      required:
        - operator
    Audience:
      title: Audience
      type: object
      properties:
        id:
          type: string
          description: A unique identifier representing the audience_id
        name:
          type: string
          description: The name of the audience
        description:
          type: string
          description: A description of the audience
        operator:
          $ref: '#/components/schemas/LogicalOperator'
          description: The logical operator (AND/OR) for the top-level filter
        filter:
          $ref: '#/components/schemas/AudienceFilterConfig'
          nullable: true
        created_at:
          type: string
        updated_at:
          type: string
      required:
        - id
        - name
        - description
        - created_at
        - updated_at
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````