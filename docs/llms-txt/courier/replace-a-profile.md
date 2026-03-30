# Source: https://www.courier.com/docs/api-reference/user-profiles/replace-a-profile.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Replace a profile

> When using `PUT`, be sure to include all the key-value pairs required by the recipient's profile. 
Any key-value pairs that exist in the profile but fail to be included in the `PUT` request will be 
removed from the profile. Remember, a `PUT` update is a full replacement of the data. For partial updates, 
use the [Patch](https://www.courier.com/docs/reference/profiles/patch/) request.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml put /profiles/{user_id}
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
    put:
      tags:
        - User Profiles
      summary: Replace a profile
      description: >-
        When using `PUT`, be sure to include all the key-value pairs required by
        the recipient's profile. 

        Any key-value pairs that exist in the profile but fail to be included in
        the `PUT` request will be 

        removed from the profile. Remember, a `PUT` update is a full replacement
        of the data. For partial updates, 

        use the [Patch](https://www.courier.com/docs/reference/profiles/patch/)
        request.
      operationId: profiles_replace
      parameters:
        - name: user_id
          in: path
          description: >-
            A unique identifier representing the user associated with the
            requested user profile.
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
                $ref: '#/components/schemas/ReplaceProfileResponse'
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


            const response = await client.profiles.replace('user_id', { profile:
            { foo: 'bar' } });


            console.log(response.status);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            response = client.profiles.replace(
                user_id="user_id",
                profile={
                    "foo": "bar"
                },
            )
            print(response.status)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tresponse, err := client.Profiles.Replace(\n\t\tcontext.TODO(),\n\t\t\"user_id\",\n\t\tcourier.ProfileReplaceParams{\n\t\t\tProfile: map[string]any{\n\t\t\t\t\"foo\": \"bar\",\n\t\t\t},\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", response.Status)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.core.JsonValue;
            import com.courier.models.profiles.ProfileReplaceParams;
            import com.courier.models.profiles.ProfileReplaceResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    ProfileReplaceParams params = ProfileReplaceParams.builder()
                        .userId("user_id")
                        .profile(ProfileReplaceParams.Profile.builder()
                            .putAdditionalProperty("foo", JsonValue.from("bar"))
                            .build())
                        .build();
                    ProfileReplaceResponse response = client.profiles().replace(params);
                }
            }
        - lang: Ruby
          source: >-
            require "courier"


            courier = Courier::Client.new(api_key: "My API Key")


            response = courier.profiles.replace("user_id", profile: {foo:
            "bar"})


            puts(response)
components:
  schemas:
    ReplaceProfileResponse:
      title: ReplaceProfileResponse
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