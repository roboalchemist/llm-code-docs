# Source: https://www.courier.com/docs/api-reference/automations/list-automations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Automations

> Get the list of automations.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /automations
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /automations:
    get:
      tags:
        - Automations
      summary: List Automations
      description: Get the list of automations.
      operationId: automations_list
      parameters:
        - name: cursor
          in: query
          description: >-
            A cursor token for pagination. Use the cursor from the previous
            response to fetch the next page of results.
          required: false
          schema:
            type: string
        - name: version
          in: query
          description: >-
            The version of templates to retrieve. Accepted values are published
            (for published templates) or draft (for draft templates). Defaults
            to published.
          required: false
          schema:
            type: string
            enum:
              - published
              - draft
            default: published
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AutomationTemplateListResponse'
              examples:
                Example1:
                  value:
                    templates:
                      - name: Welcome Email Automation
                        id: abc-123-def-456
                        version: published
                        createdAt: '2024-01-01T00:00:00Z'
                        updatedAt: '2024-01-02T00:00:00Z'
                      - name: Order Confirmation
                        id: xyz-789-ghi-012
                        version: published
                        createdAt: '2024-01-03T00:00:00Z'
                        updatedAt: '2024-01-04T00:00:00Z'
                    cursor: eyJpZCI6InRlbXBsYXRlLTIifQ==
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
              examples:
                InvalidVersion:
                  value:
                    message: >-
                      Invalid version parameter "invalid". Accepted values are:
                      published (for published templates) or draft (for draft
                      templates)
                InvalidCursor:
                  value:
                    message: Invalid cursor format
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: >-
            import Courier from '@trycourier/courier';


            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });


            const automationTemplateListResponse = await
            client.automations.list();


            console.log(automationTemplateListResponse.cursor);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            automation_template_list_response = client.automations.list()
            print(automation_template_list_response.cursor)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tautomationTemplateListResponse, err := client.Automations.List(context.TODO(), courier.AutomationListParams{})\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", automationTemplateListResponse.Cursor)\n}\n"
        - lang: Java
          source: >-
            package com.courier.example;


            import com.courier.client.CourierClient;

            import com.courier.client.okhttp.CourierOkHttpClient;

            import com.courier.models.automations.AutomationListParams;

            import
            com.courier.models.automations.AutomationTemplateListResponse;


            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    AutomationTemplateListResponse automationTemplateListResponse = client.automations().list();
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            automation_template_list_response = courier.automations.list

            puts(automation_template_list_response)
components:
  schemas:
    AutomationTemplateListResponse:
      title: AutomationTemplateListResponse
      type: object
      properties:
        templates:
          type: array
          items:
            $ref: '#/components/schemas/AutomationTemplate'
        cursor:
          type: string
          description: >-
            A cursor token for pagination. Present when there are more results
            available.
    AutomationTemplate:
      title: AutomationTemplate
      type: object
      properties:
        name:
          type: string
          description: The name of the automation template.
        id:
          type: string
          description: The unique identifier of the automation template.
        version:
          type: string
          description: The version of the template published or drafted.
          enum:
            - published
            - draft
        createdAt:
          type: string
          format: date-time
          description: ISO 8601 timestamp when the template was created.
        updatedAt:
          type: string
          format: date-time
          description: ISO 8601 timestamp when the template was last updated.
      required:
        - name
        - id
        - version
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````