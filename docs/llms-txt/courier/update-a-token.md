# Source: https://www.courier.com/docs/api-reference/device-tokens/update-a-token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a token

> Apply a JSON Patch (RFC 6902) to the specified token.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml patch /users/{user_id}/tokens/{token}
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /users/{user_id}/tokens/{token}:
    patch:
      tags:
        - Device Tokens
      summary: Update a token
      description: Apply a JSON Patch (RFC 6902) to the specified token.
      operationId: users_tokens_update
      parameters:
        - name: user_id
          in: path
          description: The user's ID. This can be any uniquely identifiable string.
          required: true
          schema:
            type: string
        - name: token
          in: path
          description: The full token string.
          required: true
          schema:
            type: string
          x-stainless-param: token_id
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UsersPatchUserTokenOpts'
      responses:
        '204':
          description: ''
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

            await client.users.tokens.update('token', {
              user_id: 'user_id',
              patch: [{ op: 'op', path: 'path' }],
            });
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            client.users.tokens.update(
                token="token",
                user_id="user_id",
                patch=[{
                    "op": "op",
                    "path": "path",
                }],
            )
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\terr := client.Users.Tokens.Update(\n\t\tcontext.TODO(),\n\t\t\"token\",\n\t\tcourier.UserTokenUpdateParams{\n\t\t\tUserID: \"user_id\",\n\t\t\tPatch: []courier.UserTokenUpdateParamsPatch{{\n\t\t\t\tOp:   \"op\",\n\t\t\t\tPath: \"path\",\n\t\t\t}},\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.users.tokens.TokenUpdateParams;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    TokenUpdateParams params = TokenUpdateParams.builder()
                        .userId("user_id")
                        .token("token")
                        .addPatch(TokenUpdateParams.Patch.builder()
                            .op("op")
                            .path("path")
                            .build())
                        .build();
                    client.users().tokens().update(params);
                }
            }
        - lang: Ruby
          source: >-
            require "courier"


            courier = Courier::Client.new(api_key: "My API Key")


            result = courier.users.tokens.update("token", user_id: "user_id",
            patch: [{op: "op", path: "path"}])


            puts(result)
components:
  schemas:
    UsersPatchUserTokenOpts:
      title: UsersPatchUserTokenOpts
      type: object
      properties:
        patch:
          type: array
          items:
            $ref: '#/components/schemas/UsersPatchOperation'
      required:
        - patch
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
    UsersPatchOperation:
      title: UsersPatchOperation
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
          nullable: true
          description: The value for the operation.
      required:
        - op
        - path
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