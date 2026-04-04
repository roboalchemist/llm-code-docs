# Source: https://www.courier.com/docs/api-reference/notification-templates/get-notifications-checks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get notifications checks



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /notifications/{id}/{submissionId}/checks
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
    get:
      tags:
        - Notification Templates
      operationId: notifications_getSubmissionChecks
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
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SubmissionChecksGetResponse'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: >-
            import Courier from '@trycourier/courier';


            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });


            const checks = await
            client.notifications.checks.list('submissionId', { id: 'id' });


            console.log(checks.checks);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            checks = client.notifications.checks.list(
                submission_id="submissionId",
                id="id",
            )
            print(checks.checks)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tchecks, err := client.Notifications.Checks.List(\n\t\tcontext.TODO(),\n\t\t\"submissionId\",\n\t\tcourier.NotificationCheckListParams{\n\t\t\tID: \"id\",\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", checks.Checks)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.notifications.checks.CheckListParams;
            import com.courier.models.notifications.checks.CheckListResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    CheckListParams params = CheckListParams.builder()
                        .id("id")
                        .submissionId("submissionId")
                        .build();
                    CheckListResponse checks = client.notifications().checks().list(params);
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            checks = courier.notifications.checks.list("submissionId", id: "id")

            puts(checks)
components:
  schemas:
    SubmissionChecksGetResponse:
      title: SubmissionChecksGetResponse
      type: object
      properties:
        checks:
          type: array
          items:
            $ref: '#/components/schemas/Check'
      required:
        - checks
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
    CheckStatus:
      title: CheckStatus
      type: string
      enum:
        - RESOLVED
        - FAILED
        - PENDING
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````