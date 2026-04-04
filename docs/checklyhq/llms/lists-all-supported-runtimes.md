# Source: https://checklyhq.com/docs/api-reference/runtimes/lists-all-supported-runtimes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List all supported runtimes

> Lists all supported runtimes and the included NPM packages for Browser checks and setup & teardown scripts for API checks.



## OpenAPI

````yaml get /v1/runtimes
openapi: 3.0.0
info:
  title: Checkly Public API
  version: v1
  description: >-
    These are the docs for the newly released Checkly Public API. If you have
    any questions, please do not hesitate to get in touch with us.
servers:
  - url: https://api.checklyhq.com
security:
  - Bearer: []
tags: []
paths:
  /v1/runtimes:
    get:
      tags:
        - Runtimes
      summary: Lists all supported runtimes
      description: >-
        Lists all supported runtimes and the included NPM packages for Browser
        checks and setup & teardown scripts for API checks.
      operationId: getV1Runtimes
      parameters:
        - name: x-checkly-account
          in: header
          schema:
            type: string
            description: >-
              Your Checkly account ID, you can find it at
              https://app.checklyhq.com/settings/account/general
            x-format:
              guid: true
          description: >-
            Your Checkly account ID, you can find it at
            https://app.checklyhq.com/settings/account/general
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RuntimeList'
        '429':
          description: Too Many Requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TooManyRequestsError'
components:
  schemas:
    RuntimeList:
      type: array
      items:
        $ref: '#/components/schemas/Runtime'
    TooManyRequestsError:
      type: object
      properties:
        statusCode:
          type: number
          enum:
            - 429
        error:
          $ref: '#/components/schemas/Model2'
        message:
          type: string
          example: Too Many Requests
        attributes:
          $ref: '#/components/schemas/attributes'
      required:
        - statusCode
        - error
    Runtime:
      type: object
      properties:
        name:
          type: string
          description: The unique name of this runtime.
          example: '2025.04'
        multiStepSupport:
          type: boolean
          description: Does this runtime supports multi step checks
        nodeJsVersion:
          type: string
          description: The full Node.js version available in this runtime.
          example: v18.20.3
        stage:
          $ref: '#/components/schemas/stage'
        runtimeEndOfLife:
          type: string
          description: Date which a runtime will be removed from our platform.
          example: 12/31/2022
        description:
          type: string
          description: >-
            A short, human readable description of the main updates in this
            runtime.
          example: Main updates are Playwright 1.51.1
        dependencies:
          $ref: '#/components/schemas/DependenciesList'
      required:
        - name
        - multiStepSupport
        - nodeJsVersion
        - dependencies
    Model2:
      type: string
      enum:
        - Too Many Requests
    attributes:
      type: object
    stage:
      type: string
      description: Current life stage of a runtime.
      example: STABLE
      enum:
        - ALPHA
        - BETA
        - CURRENT
        - DEPRECATED
        - REMOVED
        - STABLE
    DependenciesList:
      type: object
      description: >-
        An object with all dependency package names and versions as in a
        standard package.json.
      example:
        '@playwright/test': 1.51.1
        '@axe-core/playwright': 4.10.1
        '@azure/identity': 4.9.1
        '@azure/keyvault-secrets': 4.9.0
        '@checkly/playwright-helpers': 1.0.4
        '@faker-js/faker': 9.7.0
        '@google-cloud/local-auth': 3.0.1
        '@opentelemetry/api': 1.9.0
        '@opentelemetry/exporter-metrics-otlp-grpc': 0.200.0
        '@opentelemetry/sdk-metrics': 2.0.0
        '@opentelemetry/sdk-trace-base': 2.0.0
        '@t3-oss/env-nextjs': 0.13.0
        '@xmldom/xmldom': 0.9.8
        aws4: 1.13.2
        axios: 0.28.0
        btoa: 1.2.1
        http: 22.11.0
        https: 22.11.0
        crypto-js: 4.2.0
        date-fns: 4.1.0
        date-fns-tz: 3.2.0
        dotenv: 16.5.0
        ethers: 6.13.5
        expect: 29.7.0
        form-data: 4.0.4
        gmail-api-parse-message-ts: 2.2.33
        google-auth-library: 9.15.1
        googleapis: 148.0.0
        graphql: 16.10.0
        graphql-tag: 2.12.6
        jose: 5.10.0
        jsdom: 26.1.0
        jsonwebtoken: 9.0.2
        lodash: 4.17.21
        long: 5.3.2
        moment: 2.30.1
        nice-grpc: 2.1.12
        nice-grpc-client-middleware-deadline: 2.0.15
        nice-grpc-client-middleware-devtools: 1.0.7
        nice-grpc-client-middleware-retry: 3.1.11
        nice-grpc-common: 2.0.2
        nice-grpc-error-details: 0.2.9
        nice-grpc-opentelemetry: 0.1.18
        nice-grpc-prometheus: 0.2.7
        nice-grpc-server-health: 2.0.14
        nice-grpc-server-middleware-terminator: 2.0.14
        nice-grpc-server-reflection: 2.0.14
        nice-grpc-web: 3.3.7
        node-pop3: 0.9.1
        otpauth: 9.4.0
        playwright: 1.51.1
        pdf2json: 3.1.4
        prisma: 6.6.0
        protobufjs: 7.5.0
        tedious: 18.6.1
        twilio: 5.3.0
        uuid: 11.1.0
        ws: 8.18.1
        xml-crypto: 6.1.1
        xml-encryption: 3.1.0
        zod: 3.24.3
        '@clerk/testing': 1.5.1
        mailosaur: 8.8.1
        gaxios: 6.7.1
        '@kubernetes/client-node': 1.1.2
        mysql: 2.18.1
  securitySchemes:
    Bearer:
      type: http
      scheme: bearer
      bearerFormat: Bearer
      description: >-
        The Checkly Public API uses API keys to authenticate requests. You can
        get the API Key
        [here](https://app.checklyhq.com/settings/user/api-keys). Your API key
        is like a password:  keep it secure!

        Authentication to the API is performed using the Bearer auth method in
        the Authorization header and using the account ID.

        For example, set **Authorization** header while using cURL: `curl -H
        "Authorization: Bearer [apiKey]" "X-Checkly-Account: [accountId]"` 

````

Built with [Mintlify](https://mintlify.com).