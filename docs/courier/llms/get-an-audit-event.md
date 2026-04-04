# Source: https://www.courier.com/docs/api-reference/audit-events/get-an-audit-event.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get an audit event

> Fetch a specific audit event by ID.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /audit-events/{audit-event-id}
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /audit-events/{audit-event-id}:
    get:
      tags:
        - Audit Events
      summary: Get an audit event
      description: Fetch a specific audit event by ID.
      operationId: auditEvents_get
      parameters:
        - name: audit-event-id
          in: path
          description: >-
            A unique identifier associated with the audit event you wish to
            retrieve
          required: true
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AuditEvent'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: >-
            import Courier from '@trycourier/courier';


            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });


            const auditEvent = await
            client.auditEvents.retrieve('audit-event-id');


            console.log(auditEvent.actor);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            audit_event = client.audit_events.retrieve(
                "audit-event-id",
            )
            print(audit_event.actor)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tauditEvent, err := client.AuditEvents.Get(context.TODO(), \"audit-event-id\")\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", auditEvent.Actor)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.auditevents.AuditEvent;
            import com.courier.models.auditevents.AuditEventRetrieveParams;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    AuditEvent auditEvent = client.auditEvents().retrieve("audit-event-id");
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            audit_event = courier.audit_events.retrieve("audit-event-id")

            puts(audit_event)
components:
  schemas:
    AuditEvent:
      title: AuditEvent
      type: object
      properties:
        auditEventId:
          type: string
        actor:
          $ref: '#/components/schemas/Actor'
        target:
          type: string
        source:
          type: string
        timestamp:
          type: string
        type:
          type: string
      required:
        - auditEventId
        - actor
        - target
        - source
        - timestamp
        - type
    Actor:
      title: Actor
      type: object
      properties:
        id:
          type: string
        email:
          type: string
          nullable: true
      required:
        - id
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````