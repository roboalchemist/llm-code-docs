# Source: https://www.courier.com/docs/api-reference/device-tokens/delete-user-token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete User Token



## OpenAPI

````yaml openapi-specs/openapi.documented.yml delete /users/{user_id}/tokens/{token}
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
    delete:
      tags:
        - Device Tokens
      summary: Delete User Token
      operationId: users_tokens_delete
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

            await client.users.tokens.delete('token', { user_id: 'user_id' });
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            client.users.tokens.delete(
                token="token",
                user_id="user_id",
            )
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\terr := client.Users.Tokens.Delete(\n\t\tcontext.TODO(),\n\t\t\"token\",\n\t\tcourier.UserTokenDeleteParams{\n\t\t\tUserID: \"user_id\",\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.users.tokens.TokenDeleteParams;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    TokenDeleteParams params = TokenDeleteParams.builder()
                        .userId("user_id")
                        .token("token")
                        .build();
                    client.users().tokens().delete(params);
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            result = courier.users.tokens.delete("token", user_id: "user_id")

            puts(result)
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````