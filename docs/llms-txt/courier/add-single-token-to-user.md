# Source: https://www.courier.com/docs/api-reference/device-tokens/add-single-token-to-user.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add single token to user

> Adds a single token to a user and overwrites a matching existing token.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml put /users/{user_id}/tokens/{token}
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
    put:
      tags:
        - Device Tokens
      summary: Add single token to user
      description: Adds a single token to a user and overwrites a matching existing token.
      operationId: users_tokens_add
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
              $ref: '#/components/schemas/UsersUserToken'
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

            await client.users.tokens.addSingle('token', {
              user_id: 'user_id',
              body_token: 'token',
              provider_key: 'firebase-fcm',
            });
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            client.users.tokens.add_single(
                path_token="token",
                user_id="user_id",
                body_token="token",
                provider_key="firebase-fcm",
            )
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\terr := client.Users.Tokens.AddSingle(\n\t\tcontext.TODO(),\n\t\t\"token\",\n\t\tcourier.UserTokenAddSingleParams{\n\t\t\tUserID: \"user_id\",\n\t\t\tUserToken: courier.UserTokenParam{\n\t\t\t\tToken:       \"token\",\n\t\t\t\tProviderKey: courier.UserTokenProviderKeyFirebaseFcm,\n\t\t\t},\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.users.tokens.TokenAddSingleParams;
            import com.courier.models.users.tokens.UserToken;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    TokenAddSingleParams params = TokenAddSingleParams.builder()
                        .userId("user_id")
                        .pathToken("token")
                        .userToken(UserToken.builder()
                            .token("token")
                            .providerKey(UserToken.ProviderKey.FIREBASE_FCM)
                            .build())
                        .build();
                    client.users().tokens().addSingle(params);
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            result = courier.users.tokens.add_single(
              "token",
              user_id: "user_id",
              body_token: "token",
              provider_key: :"firebase-fcm"
            )

            puts(result)
components:
  schemas:
    UsersUserToken:
      title: UsersUserToken
      type: object
      properties:
        token:
          type: string
          description: Full body of the token. Must match token in URL path parameter.
        provider_key:
          $ref: '#/components/schemas/UsersProviderKey'
        expiry_date:
          $ref: '#/components/schemas/UsersExpiryDate'
          nullable: true
          description: >-
            ISO 8601 formatted date the token expires. Defaults to 2 months. Set
            to false to disable expiration.
        properties:
          nullable: true
          description: Properties about the token.
        device:
          $ref: '#/components/schemas/UsersDevice'
          nullable: true
          description: Information about the device the token came from.
        tracking:
          $ref: '#/components/schemas/UsersTracking'
          nullable: true
          description: Tracking information about the device the token came from.
      required:
        - provider_key
        - token
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
    UsersProviderKey:
      title: UsersProviderKey
      type: string
      enum:
        - firebase-fcm
        - apn
        - expo
        - onesignal
    UsersExpiryDate:
      title: UsersExpiryDate
      oneOf:
        - type: string
        - type: boolean
    UsersDevice:
      title: UsersDevice
      type: object
      properties:
        app_id:
          type: string
          nullable: true
          description: Id of the application the token is used for
        ad_id:
          type: string
          nullable: true
          description: Id of the advertising identifier
        device_id:
          type: string
          nullable: true
          description: Id of the device the token is associated with
        platform:
          type: string
          nullable: true
          description: The device platform i.e. android, ios, web
        manufacturer:
          type: string
          nullable: true
          description: The device manufacturer
        model:
          type: string
          nullable: true
          description: The device model
    UsersTracking:
      title: usersTracking
      type: object
      properties:
        os_version:
          type: string
          nullable: true
          description: The operating system version
        ip:
          type: string
          nullable: true
          description: The IP address of the device
        lat:
          type: string
          nullable: true
          description: The latitude of the device
        long:
          type: string
          nullable: true
          description: The longitude of the device
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