# Source: https://www.courier.com/docs/api-reference/automations/invoke-an-ad-hoc-automation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Invoke an Ad Hoc Automation

> Invoke an ad hoc automation run. This endpoint accepts a JSON payload with a series of automation steps. For information about what steps are available, checkout the ad hoc automation guide [here](https://www.courier.com/docs/automations/steps/).



## OpenAPI

````yaml openapi-specs/openapi.documented.yml post /automations/invoke
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /automations/invoke:
    post:
      tags:
        - Automations
      summary: Invoke an Ad Hoc Automation
      description: >-
        Invoke an ad hoc automation run. This endpoint accepts a JSON payload
        with a series of automation steps. For information about what steps are
        available, checkout the ad hoc automation guide
        [here](https://www.courier.com/docs/automations/steps/).
      operationId: automations_invokeAdHocAutomation
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AutomationAdHocInvokeParams'
            examples:
              Example1:
                value:
                  data:
                    name: Foo
                  profile:
                    tenant_id: abc-123
                  recipient: user-yes
                  automation:
                    cancelation_token: delay-send--user-yes--abc-123
                    steps:
                      - action: delay
                        until: 20240408T080910.123
                      - action: send
                        template: 64TP5HKPFTM8VTK1Y75SJDQX9JK0
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AutomationInvokeResponse'
              examples:
                Example1:
                  value:
                    runId: 1-65f240a0-47a6a120c8374de9bcf9f22c
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
            client.automations.invoke.invokeAdHoc({
              automation: {
                cancelation_token: 'delay-send--user-yes--abc-123',
                steps: [
                  { action: 'delay', until: '20240408T080910.123' },
                  { action: 'send', template: '64TP5HKPFTM8VTK1Y75SJDQX9JK0' },
                ],
              },
              data: { name: 'Foo' },
              profile: { tenant_id: 'abc-123' },
              recipient: 'user-yes',
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
            client.automations.invoke.invoke_ad_hoc(
                automation={
                    "cancelation_token": "delay-send--user-yes--abc-123",
                    "steps": [{
                        "action": "delay",
                        "until": "20240408T080910.123",
                    }, {
                        "action": "send",
                        "template": "64TP5HKPFTM8VTK1Y75SJDQX9JK0",
                    }],
                },
                data={
                    "name": "Foo"
                },
                profile={
                    "tenant_id": "abc-123"
                },
                recipient="user-yes",
            )

            print(automation_invoke_response.run_id)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tautomationInvokeResponse, err := client.Automations.Invoke.InvokeAdHoc(context.TODO(), courier.AutomationInvokeInvokeAdHocParams{\n\t\tAutomation: courier.AutomationInvokeInvokeAdHocParamsAutomation{\n\t\t\tCancelationToken: courier.String(\"delay-send--user-yes--abc-123\"),\n\t\t\tSteps: []courier.AutomationInvokeInvokeAdHocParamsAutomationStepUnion{{\n\t\t\t\tOfAutomationDelayStep: &courier.AutomationInvokeInvokeAdHocParamsAutomationStepAutomationDelayStep{\n\t\t\t\t\tAction: \"delay\",\n\t\t\t\t\tUntil:  courier.String(\"20240408T080910.123\"),\n\t\t\t\t},\n\t\t\t}, {\n\t\t\t\tOfAutomationSendStep: &courier.AutomationInvokeInvokeAdHocParamsAutomationStepAutomationSendStep{\n\t\t\t\t\tAction:   \"send\",\n\t\t\t\t\tTemplate: courier.String(\"64TP5HKPFTM8VTK1Y75SJDQX9JK0\"),\n\t\t\t\t},\n\t\t\t}},\n\t\t},\n\t\tData: map[string]any{\n\t\t\t\"name\": \"Foo\",\n\t\t},\n\t\tProfile: map[string]any{\n\t\t\t\"tenant_id\": \"abc-123\",\n\t\t},\n\t\tRecipient: courier.String(\"user-yes\"),\n\t})\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", automationInvokeResponse.RunID)\n}\n"
        - lang: Java
          source: >-
            package com.courier.example;


            import com.courier.client.CourierClient;

            import com.courier.client.okhttp.CourierOkHttpClient;

            import com.courier.models.automations.AutomationInvokeResponse;

            import
            com.courier.models.automations.invoke.InvokeInvokeAdHocParams;


            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    InvokeInvokeAdHocParams params = InvokeInvokeAdHocParams.builder()
                        .automation(InvokeInvokeAdHocParams.Automation.builder()
                            .addStep(InvokeInvokeAdHocParams.Automation.Step.AutomationDelayStep.builder()
                                .action(InvokeInvokeAdHocParams.Automation.Step.AutomationDelayStep.Action.DELAY)
                                .build())
                            .addStep(InvokeInvokeAdHocParams.Automation.Step.AutomationSendStep.builder()
                                .action(InvokeInvokeAdHocParams.Automation.Step.AutomationSendStep.Action.SEND)
                                .build())
                            .build())
                        .build();
                    AutomationInvokeResponse automationInvokeResponse = client.automations().invoke().invokeAdHoc(params);
                }
            }
        - lang: Ruby
          source: >-
            require "courier"


            courier = Courier::Client.new(api_key: "My API Key")


            automation_invoke_response =
            courier.automations.invoke.invoke_ad_hoc(automation: {steps:
            [{action: :delay}, {action: :send}]})


            puts(automation_invoke_response)
components:
  schemas:
    AutomationAdHocInvokeParams:
      title: AutomationAdHocInvokeParams
      type: object
      properties:
        automation:
          $ref: '#/components/schemas/Automation'
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
        - automation
    AutomationInvokeResponse:
      title: AutomationInvokeResponse
      type: object
      properties:
        runId:
          type: string
      required:
        - runId
    Automation:
      title: Automation
      type: object
      properties:
        cancelation_token:
          type: string
          nullable: true
        steps:
          type: array
          items:
            $ref: '#/components/schemas/AutomationStep'
      required:
        - steps
    AutomationStep:
      title: AutomationStep
      oneOf:
        - $ref: '#/components/schemas/AutomationDelayStep'
        - $ref: '#/components/schemas/AutomationSendStep'
        - $ref: '#/components/schemas/AutomationSendListStep'
        - $ref: '#/components/schemas/AutomationUpdateProfileStep'
        - $ref: '#/components/schemas/AutomationCancelStep'
        - $ref: '#/components/schemas/AutomationFetchDataStep'
        - $ref: '#/components/schemas/AutomationInvokeStep'
    AutomationDelayStep:
      title: AutomationDelayStep
      type: object
      properties:
        action:
          type: string
          enum:
            - delay
        duration:
          type: string
          nullable: true
        until:
          type: string
          nullable: true
      required:
        - action
    AutomationSendStep:
      title: AutomationSendStep
      type: object
      properties:
        action:
          type: string
          enum:
            - send
        template:
          type: string
          nullable: true
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
      required:
        - action
    AutomationSendListStep:
      title: AutomationSendListStep
      type: object
      properties:
        action:
          type: string
          enum:
            - send-list
        list:
          type: string
        data:
          type: object
          additionalProperties: true
          nullable: true
        brand:
          type: string
          nullable: true
      required:
        - action
        - list
    AutomationUpdateProfileStep:
      title: AutomationUpdateProfileStep
      type: object
      properties:
        action:
          type: string
          enum:
            - update-profile
        recipient_id:
          type: string
          nullable: true
        merge:
          type: string
          enum:
            - none
            - overwrite
            - soft-merge
            - replace
          nullable: true
        profile:
          type: object
          additionalProperties: true
      required:
        - action
        - profile
    AutomationCancelStep:
      title: AutomationCancelStep
      type: object
      properties:
        action:
          type: string
          enum:
            - cancel
        cancelation_token:
          type: string
      required:
        - action
        - cancelation_token
    AutomationFetchDataStep:
      title: AutomationFetchDataStep
      type: object
      properties:
        action:
          type: string
          enum:
            - fetch-data
        webhook:
          $ref: '#/components/schemas/AutomationWebhookParams'
        merge_strategy:
          type: string
          enum:
            - replace
            - overwrite
            - soft-merge
          nullable: true
      required:
        - action
        - webhook
    AutomationInvokeStep:
      title: AutomationInvokeStep
      type: object
      properties:
        action:
          type: string
          enum:
            - invoke
        template:
          type: string
      required:
        - action
        - template
    AutomationWebhookParams:
      title: AutomationWebhookParams
      type: object
      properties:
        url:
          type: string
        method:
          type: string
          enum:
            - GET
            - POST
            - PUT
            - PATCH
            - DELETE
        headers:
          type: object
          additionalProperties:
            type: string
          nullable: true
        body:
          type: string
          nullable: true
      required:
        - url
        - method
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````