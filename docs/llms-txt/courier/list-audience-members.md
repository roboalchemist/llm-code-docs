# Source: https://www.courier.com/docs/api-reference/audiences/list-audience-members.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List audience members

> Get list of members of an audience.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /audiences/{audience_id}/members
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /audiences/{audience_id}/members:
    get:
      tags:
        - Audiences
      summary: List audience members
      description: Get list of members of an audience.
      operationId: audiences_listMembers
      parameters:
        - name: audience_id
          in: path
          description: A unique identifier representing the audience id
          required: true
          schema:
            type: string
        - name: cursor
          in: query
          description: A unique identifier that allows for fetching the next set of members
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
                $ref: '#/components/schemas/AudienceMemberListResponse'
        '400':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BadRequest'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: |-
            import Courier from '@trycourier/courier';

            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });

            const response = await client.audiences.listMembers('audience_id');

            console.log(response.items);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            response = client.audiences.list_members(
                audience_id="audience_id",
            )
            print(response.items)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tresponse, err := client.Audiences.ListMembers(\n\t\tcontext.TODO(),\n\t\t\"audience_id\",\n\t\tcourier.AudienceListMembersParams{},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", response.Items)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.audiences.AudienceListMembersParams;
            import com.courier.models.audiences.AudienceListMembersResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    AudienceListMembersResponse response = client.audiences().listMembers("audience_id");
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            response = courier.audiences.list_members("audience_id")

            puts(response)
components:
  schemas:
    AudienceMemberListResponse:
      title: AudienceMemberListResponse
      type: object
      properties:
        paging:
          $ref: '#/components/schemas/Paging'
        items:
          type: array
          items:
            $ref: '#/components/schemas/AudienceMember'
      required:
        - paging
        - items
    BadRequest:
      title: BadRequest
      type: object
      properties:
        type:
          type: string
          enum:
            - invalid_request_error
      required:
        - type
      allOf:
        - $ref: '#/components/schemas/BaseError'
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
    AudienceMember:
      title: AudienceMember
      type: object
      properties:
        added_at:
          type: string
        audience_id:
          type: string
        audience_version:
          type: integer
        member_id:
          type: string
        reason:
          type: string
      required:
        - added_at
        - audience_id
        - audience_version
        - member_id
        - reason
    BaseError:
      title: BaseError
      type: object
      properties:
        message:
          type: string
          description: A message describing the error that occurred.
      required:
        - message
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````