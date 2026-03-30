# Source: https://www.courier.com/docs/api-reference/notification-templates/put-notifications-checks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Put notifications checks



## OpenAPI

````yaml openapi-specs/openapi.documented.yml put /notifications/{id}/{submissionId}/checks
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /notifications/{id}/{submissionId}/checks:
    put:
      tags:
        - Notification Templates
      operationId: notifications_replaceSubmissionChecks
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
        - name: submissionId
          in: path
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
                checks:
                  type: array
                  items:
                    $ref: '#/components/schemas/BaseCheck'
              required:
                - checks
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SubmissionChecksReplaceResponse'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: >-
            import Courier from '@trycourier/courier';


            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });


            const check = await
            client.notifications.checks.update('submissionId', {
              id: 'id',
              checks: [
                {
                  id: 'id',
                  status: 'RESOLVED',
                  type: 'custom',
                },
              ],
            });


            console.log(check.checks);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            check = client.notifications.checks.update(
                submission_id="submissionId",
                id="id",
                checks=[{
                    "id": "id",
                    "status": "RESOLVED",
                    "type": "custom",
                }],
            )
            print(check.checks)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tcheck, err := client.Notifications.Checks.Update(\n\t\tcontext.TODO(),\n\t\t\"submissionId\",\n\t\tcourier.NotificationCheckUpdateParams{\n\t\t\tID: \"id\",\n\t\t\tChecks: []courier.BaseCheckParam{{\n\t\t\t\tID:     \"id\",\n\t\t\t\tStatus: courier.BaseCheckStatusResolved,\n\t\t\t\tType:   courier.BaseCheckTypeCustom,\n\t\t\t}},\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", check.Checks)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.notifications.BaseCheck;
            import com.courier.models.notifications.checks.CheckUpdateParams;
            import com.courier.models.notifications.checks.CheckUpdateResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    CheckUpdateParams params = CheckUpdateParams.builder()
                        .id("id")
                        .submissionId("submissionId")
                        .addCheck(BaseCheck.builder()
                            .id("id")
                            .status(BaseCheck.Status.RESOLVED)
                            .type(BaseCheck.Type.CUSTOM)
                            .build())
                        .build();
                    CheckUpdateResponse check = client.notifications().checks().update(params);
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            check = courier.notifications.checks.update(
              "submissionId",
              id: "id",
              checks: [{id: "id", status: :RESOLVED, type: :custom}]
            )

            puts(check)
components:
  schemas:
    BaseCheck:
      title: BaseCheck
      type: object
      properties:
        id:
          type: string
        status:
          $ref: '#/components/schemas/CheckStatus'
        type:
          type: string
          enum:
            - custom
      required:
        - id
        - status
        - type
    SubmissionChecksReplaceResponse:
      title: SubmissionChecksReplaceResponse
      type: object
      properties:
        checks:
          type: array
          items:
            $ref: '#/components/schemas/Check'
      required:
        - checks
    CheckStatus:
      title: CheckStatus
      type: string
      enum:
        - RESOLVED
        - FAILED
        - PENDING
    Check:
      title: Check
      type: object
      properties:
        updated:
          type: integer
          format: int64
      required:
        - updated
      allOf:
        - $ref: '#/components/schemas/BaseCheck'
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````