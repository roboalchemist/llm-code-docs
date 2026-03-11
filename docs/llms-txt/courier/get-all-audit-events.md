# Source: https://www.courier.com/docs/api-reference/audit-events/get-all-audit-events.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all audit events

> Fetch the list of audit events



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /audit-events
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /audit-events:
    get:
      tags:
        - Audit Events
      summary: Get all audit events
      description: Fetch the list of audit events
      operationId: auditEvents_list
      parameters:
        - name: cursor
          in: query
          description: >-
            A unique identifier that allows for fetching the next set of audit
            events.
          required: false
          schema:
            type: string
            nullable: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListAuditEventsResponse'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: |-
            import Courier from '@trycourier/courier';

            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });

            const auditEvents = await client.auditEvents.list();

            console.log(auditEvents.paging);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            audit_events = client.audit_events.list()
            print(audit_events.paging)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tauditEvents, err := client.AuditEvents.List(context.TODO(), courier.AuditEventListParams{})\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", auditEvents.Paging)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.auditevents.AuditEventListParams;
            import com.courier.models.auditevents.AuditEventListResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    AuditEventListResponse auditEvents = client.auditEvents().list();
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            audit_events = courier.audit_events.list

            puts(audit_events)
components:
  schemas:
    ListAuditEventsResponse:
      title: ListAuditEventsResponse
      type: object
      properties:
        paging:
          $ref: '#/components/schemas/Paging'
        results:
          type: array
          items:
            $ref: '#/components/schemas/AuditEvent'
      required:
        - paging
        - results
    Paging:
      title: Paging
      type: object
      properties:
        cursor:
          type: string
          nullable: true
        more:
          type: boolean
      required:
        - more
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