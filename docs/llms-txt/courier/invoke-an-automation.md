# Source: https://www.courier.com/docs/api-reference/automations/invoke-an-automation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Invoke an Automation

> Invoke an automation run from an automation template.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml post /automations/{templateId}/invoke
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /automations/{templateId}/invoke:
    post:
      tags:
        - Automations
      summary: Invoke an Automation
      description: Invoke an automation run from an automation template.
      operationId: automations_invokeAutomationTemplate
      parameters:
        - name: templateId
          in: path
          description: >-
            A unique identifier representing the automation template to be
            invoked. This could be the Automation Template ID or the Automation
            Template Alias.
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AutomationInvokeParams'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AutomationInvokeResponse'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: >-
            import Courier from '@trycourier/courier';


            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });


            const automationInvokeResponse = await
            client.automations.invoke.invokeByTemplate('templateId', {
              recipient: 'recipient',
            });


            console.log(automationInvokeResponse.runId);
        - lang: Python
          source: >-
            import os

            from courier import Courier


            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )

            automation_invoke_response =
            client.automations.invoke.invoke_by_template(
                template_id="templateId",
                recipient="recipient",
            )

            print(automation_invoke_response.run_id)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tautomationInvokeResponse, err := client.Automations.Invoke.InvokeByTemplate(\n\t\tcontext.TODO(),\n\t\t\"templateId\",\n\t\tcourier.AutomationInvokeInvokeByTemplateParams{\n\t\t\tRecipient: courier.String(\"recipient\"),\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", automationInvokeResponse.RunID)\n}\n"
        - lang: Java
          source: >-
            package com.courier.example;


            import com.courier.client.CourierClient;

            import com.courier.client.okhttp.CourierOkHttpClient;

            import com.courier.models.automations.AutomationInvokeResponse;

            import
            com.courier.models.automations.invoke.InvokeInvokeByTemplateParams;


            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    InvokeInvokeByTemplateParams params = InvokeInvokeByTemplateParams.builder()
                        .templateId("templateId")
                        .recipient("recipient")
                        .build();
                    AutomationInvokeResponse automationInvokeResponse = client.automations().invoke().invokeByTemplate(params);
                }
            }
        - lang: Ruby
          source: >-
            require "courier"


            courier = Courier::Client.new(api_key: "My API Key")


            automation_invoke_response =
            courier.automations.invoke.invoke_by_template("templateId",
            recipient: "recipient")


            puts(automation_invoke_response)
components:
  schemas:
    AutomationInvokeParams:
      title: AutomationInvokeParams
      type: object
      properties:
        brand:
          type: string
          nullable: true
        data:
          type: object
          additionalProperties: true
          nullable: true
        profile:
          type: object
          additionalProperties: true
          nullable: true
        recipient:
          type: string
          nullable: true
        template:
          type: string
          nullable: true
      required:
        - recipient
    AutomationInvokeResponse:
      title: AutomationInvokeResponse
      type: object
      properties:
        runId:
          type: string
      required:
        - runId
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````