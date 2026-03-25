# Source: https://www.courier.com/docs/api-reference/user-profiles/update-a-profile.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a profile



## OpenAPI

````yaml openapi-specs/openapi.documented.yml patch /profiles/{user_id}
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
    patch:
      tags:
        - User Profiles
      summary: Update a profile
      operationId: profiles_mergeProfile
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
              $ref: '#/components/schemas/ProfileUpdateRequest'
      responses:
        '204':
          description: ''
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: |-
            import Courier from '@trycourier/courier';

            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });

            await client.profiles.update('user_id', {
              patch: [
                {
                  op: 'op',
                  path: 'path',
                  value: 'value',
                },
              ],
            });
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            client.profiles.update(
                user_id="user_id",
                patch=[{
                    "op": "op",
                    "path": "path",
                    "value": "value",
                }],
            )
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\terr := client.Profiles.Update(\n\t\tcontext.TODO(),\n\t\t\"user_id\",\n\t\tcourier.ProfileUpdateParams{\n\t\t\tPatch: []courier.ProfileUpdateParamsPatch{{\n\t\t\t\tOp:    \"op\",\n\t\t\t\tPath:  \"path\",\n\t\t\t\tValue: \"value\",\n\t\t\t}},\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.profiles.ProfileUpdateParams;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    ProfileUpdateParams params = ProfileUpdateParams.builder()
                        .userId("user_id")
                        .addPatch(ProfileUpdateParams.Patch.builder()
                            .op("op")
                            .path("path")
                            .value("value")
                            .build())
                        .build();
                    client.profiles().update(params);
                }
            }
        - lang: Ruby
          source: >-
            require "courier"


            courier = Courier::Client.new(api_key: "My API Key")


            result = courier.profiles.update("user_id", patch: [{op: "op", path:
            "path", value: "value"}])


            puts(result)
components:
  schemas:
    ProfileUpdateRequest:
      title: ProfileUpdateRequest
      type: object
      properties:
        patch:
          type: array
          items:
            $ref: '#/components/schemas/UserProfilePatch'
          description: List of patch operations to apply to the profile.
      required:
        - patch
    UserProfilePatch:
      title: UserProfilePatch
      type: object
      properties:
        op:
          type: string
          description: The operation to perform.
        path:
          type: string
          description: The JSON path specifying the part of the profile to operate on.
        value:
          type: string
          description: The value for the operation.
      required:
        - op
        - path
        - value
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````