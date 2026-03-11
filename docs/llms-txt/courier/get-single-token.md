# Source: https://www.courier.com/docs/api-reference/device-tokens/get-single-token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get single token

> Get single token available for a `:token`



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /users/{user_id}/tokens/{token}
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
    get:
      tags:
        - Device Tokens
      summary: Get single token
      description: Get single token available for a `:token`
      operationId: users_tokens_get
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
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UsersGetUserTokenResponse'
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


            const token = await client.users.tokens.retrieve('token', { user_id:
            'user_id' });


            console.log(token);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            token = client.users.tokens.retrieve(
                token="token",
                user_id="user_id",
            )
            print(token)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\ttoken, err := client.Users.Tokens.Get(\n\t\tcontext.TODO(),\n\t\t\"token\",\n\t\tcourier.UserTokenGetParams{\n\t\t\tUserID: \"user_id\",\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", token)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.users.tokens.TokenRetrieveParams;
            import com.courier.models.users.tokens.TokenRetrieveResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    TokenRetrieveParams params = TokenRetrieveParams.builder()
                        .userId("user_id")
                        .token("token")
                        .build();
                    TokenRetrieveResponse token = client.users().tokens().retrieve(params);
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            token = courier.users.tokens.retrieve("token", user_id: "user_id")

            puts(token)
components:
  schemas:
    UsersGetUserTokenResponse:
      title: UsersGetUserTokenResponse
      type: object
      properties:
        status:
          $ref: '#/components/schemas/UsersTokenStatus'
          nullable: true
        status_reason:
          type: string
          nullable: true
          description: The reason for the token status.
      allOf:
        - $ref: '#/components/schemas/UsersUserToken'
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
    UsersTokenStatus:
      title: UsersTokenStatus
      type: string
      enum:
        - active
        - unknown
        - failed
        - revoked
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
    BaseError:
      title: BaseError
      type: object
      properties:
        message:
          type: string
          description: A message describing the error that occurred.
      required:
        - message
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
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````