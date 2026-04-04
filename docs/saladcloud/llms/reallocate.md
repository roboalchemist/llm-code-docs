# Source: https://docs.salad.com/reference/imds/reallocate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Reallocate Container Instance

> Reallocates the current container instance to another SaladCloud node

*Last Updated: May 10, 2025*


## OpenAPI

````yaml salad-cloud-imds post /v1/reallocate
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
  /v1/reallocate:
    summary: Reallocate Container Instance
    description: >-
      Operations to reallocate the current container instance to another
      SaladCloud node
    post:
      tags:
        - metadata
      summary: Reallocate Container Instance
      description: Reallocates the current container instance to another SaladCloud node
      operationId: reallocate
      parameters:
        - name: Metadata
          in: header
          required: true
          schema:
            type: string
            enum:
              - 'true'
          description: Required header to indicate metadata request
      requestBody:
        $ref: '#/components/requestBodies/Reallocate'
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
            from salad_cloud_imds_sdk.models import ReallocatePrototype

            sdk = SaladCloudImdsSdk(
                timeout=10000
            )

            request_body = ReallocatePrototype(
                reason="Insufficient VRAM"
            )

            result = sdk.metadata.reallocate(request_body=request_body)

            print(result)
          lang: Python
        - source: |-
            import com.salad.cloud.imdssdk.SaladCloudImdsSdk;
            import com.salad.cloud.imdssdk.models.ReallocatePrototype;

            public class Main {

              public static void main(String[] args) {
                SaladCloudImdsSdk saladCloudImdsSdk = new SaladCloudImdsSdk();

                ReallocatePrototype reallocatePrototype = ReallocatePrototype.builder().reason("Insufficient VRAM").build();

                saladCloudImdsSdk.metadata.reallocate(reallocatePrototype);
              }
            }
          lang: Java
        - source: |-
            using Salad.Cloud.IMDS.SDK;
            using Salad.Cloud.IMDS.SDK.Config;
            using Salad.Cloud.IMDS.SDK.Models;
            using Environment = Salad.Cloud.IMDS.SDK.Http.Environment;

            var config = new SaladCloudImdsSdkConfig{
                Environment = Environment.Default
            };

            var client = new SaladCloudImdsSdkClient(config);

            var input = new ReallocatePrototype("Insufficient VRAM");

            await client.Metadata.ReallocateAsync(input);
          lang: C#
        - source: >-
            import { ReallocatePrototype, SaladCloudImdsSdk } from
            '@saladtechnologies-oss/salad-cloud-imds-sdk';


            (async () => {
              const saladCloudImdsSdk = new SaladCloudImdsSdk({});

              const reallocatePrototype: ReallocatePrototype = {
                reason: 'Insufficient VRAM',
              };

              const { data } = await saladCloudImdsSdk.metadata.reallocate(reallocatePrototype);

              console.log(data);
            })();
          lang: TypeScript
        - source: >-
            import (
              "fmt"
              "encoding/json"
              "github.com/saladtechnologies/salad-cloud-imds-sdk-go/pkg/saladcloudimdssdkconfig"
              "github.com/saladtechnologies/salad-cloud-imds-sdk-go/pkg/saladcloudimdssdk"
              "github.com/saladtechnologies/salad-cloud-imds-sdk-go/pkg/util"
              "github.com/saladtechnologies/salad-cloud-imds-sdk-go/pkg/metadata"
            )


            config := saladcloudimdssdkconfig.NewConfig()

            client := saladcloudimdssdk.NewSaladCloudImdsSdk(config)



            request := metadata.ReallocatePrototype{
              Reason: util.ToPointer("Reason"),
            }


            response, err := client.Metadata.Reallocate(context.Background(),
            request)

            if err != nil {
              panic(err)
            }


            fmt.Println(response)
          lang: Go
components:
  requestBodies:
    Reallocate:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ReallocatePrototype'
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
    ReallocatePrototype:
      description: >-
        Represents a request to reallocate the current container instance to
        another SaladCloud node.
      type: object
      properties:
        reason:
          description: >-
            The reason for reallocating the current container instance. This
            value is reported to SaladCloud support for quality assurance
            purposes of SaladCloud nodes.
          type: string
          examples:
            - Insufficient VRAM
          maxLength: 1000
          minLength: 1
      required:
        - reason
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