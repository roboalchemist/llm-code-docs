# Source: https://www.courier.com/docs/api-reference/authentication/create-a-jwt.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a JWT

> Returns a new access token.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml post /auth/issue-token
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /auth/issue-token:
    post:
      tags:
        - Authentication
      summary: Create a JWT
      description: Returns a new access token.
      operationId: authTokens_issueToken
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                scope:
                  type: string
                  description: >-
                    Available scopes:

                    - `user_id:<user-id>` - Defines which user the token will be
                    scoped to. Multiple can be listed if needed. Ex
                    `user_id:pigeon user_id:bluebird`.

                    - `read:messages` - Read messages.

                    - `read:user-tokens` - Read user push tokens.

                    - `write:user-tokens` - Write user push tokens.

                    - `read:brands[:<brand_id>]` - Read brands, optionally
                    restricted to a specific brand_id. Examples `read:brands`,
                    `read:brands:my_brand`.

                    - `write:brands[:<brand_id>]` - Write brands, optionally
                    restricted to a specific brand_id. Examples `write:brands`,
                    `write:brands:my_brand`.

                    - `inbox:read:messages` - Read inbox messages.

                    - `inbox:write:events` - Write inbox events, such as mark
                    message as read.

                    - `read:preferences` - Read user preferences.

                    - `write:preferences` - Write user preferences.

                    Example: `user_id:user123 write:user-tokens
                    inbox:read:messages inbox:write:events read:preferences
                    write:preferences read:brands`
                expires_in:
                  type: string
                  description: |-
                    Duration for token expiration. Accepts various time formats:
                    - "2 hours" - 2 hours from now
                    - "1d" - 1 day
                    - "3 days" - 3 days
                    - "10h" - 10 hours
                    - "2.5 hrs" - 2.5 hours
                    - "1m" - 1 minute
                    - "5s" - 5 seconds
                    - "1y" - 1 year
              required:
                - scope
                - expires_in
            examples:
              InboxExample:
                value:
                  scope: >-
                    user_id:$YOUR_USER_ID write:user-tokens inbox:read:messages
                    inbox:write:events read:preferences write:preferences
                    read:brands
                  expires_in: $YOUR_NUMBER days
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/IssueTokenResponse'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: |-
            import Courier from '@trycourier/courier';

            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });

            const response = await client.auth.issueToken({
              expires_in: '$YOUR_NUMBER days',
              scope:
                'user_id:$YOUR_USER_ID write:user-tokens inbox:read:messages inbox:write:events read:preferences write:preferences read:brands',
            });

            console.log(response.token);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            response = client.auth.issue_token(
                expires_in="$YOUR_NUMBER days",
                scope="user_id:$YOUR_USER_ID write:user-tokens inbox:read:messages inbox:write:events read:preferences write:preferences read:brands",
            )
            print(response.token)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tresponse, err := client.Auth.IssueToken(context.TODO(), courier.AuthIssueTokenParams{\n\t\tExpiresIn: \"$YOUR_NUMBER days\",\n\t\tScope:     \"user_id:$YOUR_USER_ID write:user-tokens inbox:read:messages inbox:write:events read:preferences write:preferences read:brands\",\n\t})\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", response.Token)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.auth.AuthIssueTokenParams;
            import com.courier.models.auth.AuthIssueTokenResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    AuthIssueTokenParams params = AuthIssueTokenParams.builder()
                        .expiresIn("$YOUR_NUMBER days")
                        .scope("user_id:$YOUR_USER_ID write:user-tokens inbox:read:messages inbox:write:events read:preferences write:preferences read:brands")
                        .build();
                    AuthIssueTokenResponse response = client.auth().issueToken(params);
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            response = courier.auth.issue_token(
              expires_in: "$YOUR_NUMBER days",
              scope: "user_id:$YOUR_USER_ID write:user-tokens inbox:read:messages inbox:write:events read:preferences write:preferences read:brands"
            )

            puts(response)
components:
  schemas:
    IssueTokenResponse:
      title: IssueTokenResponse
      type: object
      properties:
        token:
          type: string
      required:
        - token
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````