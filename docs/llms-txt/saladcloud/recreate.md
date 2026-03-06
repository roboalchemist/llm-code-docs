# Source: https://docs.salad.com/reference/imds/recreate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Recreate Container Instance

> Recreates the current container instance on the same SaladCloud node

*Last Updated: May 10, 2025*


## OpenAPI

````yaml salad-cloud-imds post /v1/recreate
openapi: 3.1.0
info:
  title: SaladCloud IMDS
  description: >-
    The SaladCloud Instance Metadata Service (IMDS). Please refer to the
    [SaladCloud API Documentation](https://docs.salad.com/reference) for more
    details.
  termsOfService: https://salad.com/terms
  contact:
    name: SaladCloud Support
    url: https://salad.com
    email: cloud@salad.com
  license:
    name: MIT
  version: 0.9.0-alpha.2
servers:
  - url: http://169.254.169.254
security: []
tags:
  - name: metadata
    description: Instance Metadata Service
paths:
  /v1/recreate:
    summary: Recreate Container Instance
    description: >-
      Operations to recreate the current container instance on the same
      SaladCloud node
    post:
      tags:
        - metadata
      summary: Recreate Container Instance
      description: Recreates the current container instance on the same SaladCloud node
      operationId: recreate
      parameters:
        - name: Metadata
          in: header
          required: true
          schema:
            type: string
            enum:
              - 'true'
          description: Required header to indicate metadata request
      responses:
        '204':
          $ref: '#/components/responses/204'
        '400':
          $ref: '#/components/responses/400'
        '403':
          $ref: '#/components/responses/403'
        '404':
          $ref: '#/components/responses/404'
        default:
          $ref: '#/components/responses/UnknownError'
      x-codeSamples:
        - source: |-
            from salad_cloud_imds_sdk import SaladCloudImdsSdk

            sdk = SaladCloudImdsSdk(
                timeout=10000
            )

            result = sdk.metadata.recreate()

            print(result)
          lang: Python
        - source: |-
            import com.salad.cloud.imdssdk.SaladCloudImdsSdk;

            public class Main {

              public static void main(String[] args) {
                SaladCloudImdsSdk saladCloudImdsSdk = new SaladCloudImdsSdk();

                saladCloudImdsSdk.metadata.recreate();
              }
            }
          lang: Java
        - source: |-
            using Salad.Cloud.IMDS.SDK;
            using Salad.Cloud.IMDS.SDK.Config;
            using Environment = Salad.Cloud.IMDS.SDK.Http.Environment;

            var config = new SaladCloudImdsSdkConfig{
                Environment = Environment.Default
            };

            var client = new SaladCloudImdsSdkClient(config);

            await client.Metadata.RecreateAsync();
          lang: C#
        - source: >-
            import { SaladCloudImdsSdk } from
            '@saladtechnologies-oss/salad-cloud-imds-sdk';


            (async () => {
              const saladCloudImdsSdk = new SaladCloudImdsSdk({});

              const { data } = await saladCloudImdsSdk.metadata.recreate();

              console.log(data);
            })();
          lang: TypeScript
        - source: |-
            import (
              "fmt"
              "encoding/json"
              "github.com/saladtechnologies/salad-cloud-imds-sdk-go/pkg/saladcloudimdssdkconfig"
              "github.com/saladtechnologies/salad-cloud-imds-sdk-go/pkg/saladcloudimdssdk"

            )

            config := saladcloudimdssdkconfig.NewConfig()
            client := saladcloudimdssdk.NewSaladCloudImdsSdk(config)

            response, err := client.Metadata.Recreate(context.Background())
            if err != nil {
              panic(err)
            }

            fmt.Println(response)
          lang: Go
components:
  responses:
    '204':
      description: No Content
    '400':
      description: Bad Request
      content:
        application/problem+json:
          schema:
            $ref: '#/components/schemas/SaladCloudImdsError'
    '403':
      description: Forbidden
      content:
        application/problem+json:
          schema:
            $ref: '#/components/schemas/SaladCloudImdsError'
    '404':
      description: Not Found
      content:
        application/problem+json:
          schema:
            $ref: '#/components/schemas/SaladCloudImdsError'
    UnknownError:
      description: Unknown Error
      content:
        application/problem+json:
          schema:
            $ref: '#/components/schemas/SaladCloudImdsError'
  schemas:
    SaladCloudImdsError:
      type: object
      description: >-
        An API error. The `code` and `type` uniquely identify the type of the
        error. The `code` is a short value that may be used for programmatic
        error handling. The `type` is an absolute URL that may be resolved for
        more detailed information. Refer to the [SaladCloud IMDS
        reference](https://leaf.salad.com/l/saladcloud-imds-errors) for a list
        of the expected `code` and `type` values. Also, note that all properties
        are optional. Clients should implement robust error handling to account
        for unexpected errors.
      properties:
        code:
          type: string
          description: >-
            The error code that identifies the error type. This is a short value
            that may be used for programmatic error handling.
          examples:
            - container-not-found
          maxLength: 100
          minLength: 1
        detail:
          type: string
          description: >-
            The human-readable explanation specific to this occurrence of the
            error.
          examples:
            - The container instance could not be found.
          maxLength: 10000
          minLength: 1
        errors:
          $ref: '#/components/schemas/SaladCloudImdsPropertyError'
        instance:
          type: string
          format: url
          description: >-
            The URI reference that identifies the specific occurrence of the
            error.
          examples:
            - https://leaf.salad.com/i/5e76d3ae-6660-444e-a7c4-7a3999023fb6
          maxLength: 2048
          minLength: 1
        status:
          type: integer
          format: int32
          description: >-
            The HTTP status code generated by the origin server for this
            occurrence of the error.
          examples:
            - 404
          maximum: 599
          minimum: 100
        title:
          type: string
          description: The short, human-readable summary of the error type.
          examples:
            - Not Found
          maxLength: 10000
          minLength: 1
        type:
          description: The URI reference that identifies the error type.
          type: string
          format: url
          default: about:blank
          examples:
            - https://leaf.salad.com/e/container-group-not-found
          maxLength: 2048
          minLength: 1
    SaladCloudImdsPropertyError:
      type: object
      description: >-
        The contextualized map of human-readable explanations specific to this
        occurrence of the error. This is often used to provide property-specific
        errors, such as validation errors. In these scenarios, the key is the
        property name and the value is an array of human-readable explanations
        specific to this property and this occurrence of the error.
      additionalProperties:
        type: array
        items:
          type: string
          description: >-
            The human-readable explanation specific to this occurrence of the
            error.
          examples:
            - The container instance could not be found.
          maxLength: 10000
          minLength: 1
        maxItems: 200
        minItems: 0
      maxProperties: 200
      minProperties: 0

````