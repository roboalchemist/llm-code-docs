# Source: https://www.courier.com/docs/api-reference/notification-templates/delete-notifications-checks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete notifications checks



## OpenAPI

````yaml openapi-specs/openapi.documented.yml delete /notifications/{id}/{submissionId}/checks
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
    delete:
      tags:
        - Notification Templates
      operationId: notifications_cancelSubmission
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
        '204':
          description: ''
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: >-
            import Courier from '@trycourier/courier';


            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });


            await client.notifications.checks.delete('submissionId', { id: 'id'
            });
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            client.notifications.checks.delete(
                submission_id="submissionId",
                id="id",
            )
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\terr := client.Notifications.Checks.Delete(\n\t\tcontext.TODO(),\n\t\t\"submissionId\",\n\t\tcourier.NotificationCheckDeleteParams{\n\t\t\tID: \"id\",\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.notifications.checks.CheckDeleteParams;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    CheckDeleteParams params = CheckDeleteParams.builder()
                        .id("id")
                        .submissionId("submissionId")
                        .build();
                    client.notifications().checks().delete(params);
                }
            }
        - lang: Ruby
          source: >-
            require "courier"


            courier = Courier::Client.new(api_key: "My API Key")


            result = courier.notifications.checks.delete("submissionId", id:
            "id")


            puts(result)
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````