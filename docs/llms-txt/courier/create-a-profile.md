# Source: https://www.courier.com/docs/api-reference/user-profiles/create-a-profile.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a profile

> Merge the supplied values with an existing profile or create a new profile if one doesn't already exist.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml post /profiles/{user_id}
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /profiles/{user_id}:
    post:
      tags:
        - User Profiles
      summary: Create a profile
      description: >-
        Merge the supplied values with an existing profile or create a new
        profile if one doesn't already exist.
      operationId: profiles_create
      parameters:
        - name: user_id
          in: path
          description: >-
            A unique identifier representing the user associated with the
            requested profile.
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
                profile:
                  type: object
                  additionalProperties: true
              required:
                - profile
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MergeProfileResponse'
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
          source: >-
            import Courier from '@trycourier/courier';


            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });


            const profile = await client.profiles.create('user_id', { profile: {
            foo: 'bar' } });


            console.log(profile.status);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            profile = client.profiles.create(
                user_id="user_id",
                profile={
                    "foo": "bar"
                },
            )
            print(profile.status)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tprofile, err := client.Profiles.New(\n\t\tcontext.TODO(),\n\t\t\"user_id\",\n\t\tcourier.ProfileNewParams{\n\t\t\tProfile: map[string]any{\n\t\t\t\t\"foo\": \"bar\",\n\t\t\t},\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", profile.Status)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.core.JsonValue;
            import com.courier.models.profiles.ProfileCreateParams;
            import com.courier.models.profiles.ProfileCreateResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    ProfileCreateParams params = ProfileCreateParams.builder()
                        .userId("user_id")
                        .profile(ProfileCreateParams.Profile.builder()
                            .putAdditionalProperty("foo", JsonValue.from("bar"))
                            .build())
                        .build();
                    ProfileCreateResponse profile = client.profiles().create(params);
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            profile = courier.profiles.create("user_id", profile: {foo: "bar"})

            puts(profile)
components:
  schemas:
    MergeProfileResponse:
      title: MergeProfileResponse
      type: object
      properties:
        status:
          type: string
          enum:
            - SUCCESS
      required:
        - status
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