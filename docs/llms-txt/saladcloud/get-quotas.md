# Source: https://docs.salad.com/reference/saladcloud-api/organizations/get-quotas.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Quotas

> Gets the organization quotas

*Last Updated: July 1, 2025*


## OpenAPI

````yaml api-specs/salad-cloud.yaml get /organizations/{organization_name}/quotas
openapi: 3.1.0
info:
  title: SaladCloud API
  description: >-
    The SaladCloud REST API. Please refer to the [SaladCloud API
    Documentation](https://docs.salad.com/api-reference) for more details.
  termsOfService: https://salad.com/terms
  contact:
    name: SaladCloud Support
    url: https://salad.com
    email: cloud@salad.com
  license:
    name: MIT License
    identifier: MIT
  version: 0.9.0-alpha.16
servers:
  - url: https://api.salad.com/api/public
security:
  - ApiKeyAuth: []
tags:
  - name: container_groups
    description: Container Groups
  - name: inference_endpoints
    description: Inference Endpoints
  - name: organization_data
    description: Auxiliary organization data and info
  - name: queues
    description: Job Queues
  - name: quotas
    description: quotas
  - name: system_logs
    description: System Logs
  - name: webhook_secret_key
    description: Webhook Secret Key
  - name: logs
    description: Platform and Application Log Entries
paths:
  /organizations/{organization_name}/quotas:
    summary: Quotas
    description: Operations for quotas
    parameters:
      - $ref: '#/components/parameters/organization_name'
    get:
      tags:
        - quotas
      summary: Get Quotas
      description: Gets the organization quotas
      operationId: get_quotas
      responses:
        '200':
          $ref: '#/components/responses/GetQuotas'
        '404':
          $ref: '#/components/responses/404'
        '429':
          $ref: '#/components/responses/429'
        default:
          $ref: '#/components/responses/UnknownError'
      x-codeSamples:
        - source: |-
            from salad_cloud_sdk import SaladCloudSdk

            sdk = SaladCloudSdk(
                api_key="YOUR_API_KEY",
                api_key_header="YOUR_API_KEY_HEADER",
                timeout=10000
            )

            result = sdk.quotas.get_quotas(organization_name="acme-corp")

            print(result)
          lang: Python
        - source: |-
            using Salad.Cloud.SDK;
            using Salad.Cloud.SDK.Config;

            var config = new SaladCloudSdkConfig{};

            var client = new SaladCloudSdkClient(config);

            var response = await client.Quotas.GetQuotasAsync("acme-corp");

            Console.WriteLine(response);
          lang: C#
        - source: >-
            import (
              "fmt"
              "encoding/json"
              "context"
              "github.com/saladtechnologies/salad-cloud-sdk-go/pkg/saladcloudsdkconfig"
              "github.com/saladtechnologies/salad-cloud-sdk-go/pkg/saladcloudsdk"

            )


            config := saladcloudsdkconfig.NewConfig()

            config.SetApiKey("API_KEY")

            client := saladcloudsdk.NewSaladCloudSdk(config)


            response, err := client.Quotas.GetQuotas(context.Background(),
            "acme-corp")

            if err != nil {
              panic(err)
            }


            fmt.Println(response)
          lang: Go
        - source: >-
            import { SaladCloudSdk } from
            '@saladtechnologies-oss/salad-cloud-sdk';


            (async () => {
              const saladCloudSdk = new SaladCloudSdk({
                apiKey: 'YOUR_API_KEY',
              });

              const { data } = await saladCloudSdk.quotas.getQuotas('acme-corp');

              console.log(data);
            })();
          lang: TypeScript
        - source: |-
            import com.salad.cloud.sdk.SaladCloudSdk;
            import com.salad.cloud.sdk.config.ApiKeyAuthConfig;
            import com.salad.cloud.sdk.config.SaladCloudSdkConfig;
            import com.salad.cloud.sdk.models.Quotas;

            public class Main {

              public static void main(String[] args) {
                SaladCloudSdkConfig config = SaladCloudSdkConfig.builder()
                  .apiKeyAuthConfig(ApiKeyAuthConfig.builder().apiKey("YOUR_API_KEY").build())
                  .build();

                SaladCloudSdk saladCloudSdk = new SaladCloudSdk(config);

                Quotas response = saladCloudSdk.quotas.getQuotas("acme-corp");

                System.out.println(response);
              }
            }
          lang: Java
components:
  parameters:
    organization_name:
      name: organization_name
      in: path
      description: >-
        Your organization name. This identifies the billing context for the API
        operation and represents a security boundary for SaladCloud resources.
        The organization must be created before using the API, and you must be a
        member of the organization.
      required: true
      schema:
        $ref: '#/components/schemas/OrganizationName'
  responses:
    '404':
      description: Not Found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ProblemDetails'
    '429':
      description: Too Many Requests
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ProblemDetails'
    GetQuotas:
      description: OK
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Quotas'
    UnknownError:
      description: Unknown Error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ProblemDetails'
  schemas:
    OrganizationName:
      description: The organization name.
      type: string
      examples:
        - acme-corp
      maxLength: 63
      minLength: 2
      pattern: ^[a-z][a-z0-9-]{0,61}[a-z0-9]$
      title: Organization Name
    Quotas:
      description: Represents the organization quotas
      type: object
      properties:
        container_groups_quotas:
          $ref: '#/components/schemas/ContainerGroupsQuotas'
        create_time:
          description: The time the resource was created
          type: string
          format: date-time
        update_time:
          description: The time the resource was last updated
          type: string
          format: date-time
      required:
        - container_groups_quotas
    ProblemDetails:
      description: Represents an API error
      type: object
      properties:
        type:
          description: The URI reference that identifies the error type.
          type: string
          format: url
          default: about:blank
          examples:
            - https://example.com/errors/invalid-request
          maxLength: 2048
          minLength: 1
        title:
          description: The short, human-readable summary of the error type.
          type: string
          examples:
            - Not Found
          maxLength: 2000
          minLength: 1
        status:
          description: >-
            The HTTP status code generated by the origin server for this
            occurrence of the error.
          type: integer
          format: int32
          examples:
            - 404
          maximum: 599
          minimum: 100
        detail:
          description: >-
            The human-readable explanation specific to this occurrence of the
            error.
          type: string
          examples:
            - The container group could not be found.
          maxLength: 2000
          minLength: 1
        instance:
          description: >-
            The URI reference that identifies the specific occurrence of the
            error.
          type: string
          format: url
          examples:
            - https://example.com/error-instances/12345
          maxLength: 2048
          minLength: 1
    ContainerGroupsQuotas:
      description: Represents the organization quotas for container groups
      type: object
      properties:
        container_replicas_quota:
          description: >-
            The maximum number of replicas that can be created for a container
            group
          type: integer
          format: int32
          examples:
            - 500
          maximum: 2147483647
          minimum: 0
        container_replicas_used:
          description: The number of replicas that are currently in use
          type: integer
          format: int32
          examples:
            - 10
          maximum: 2147483647
          minimum: 0
        max_container_group_reallocations_per_minute:
          description: The maximum number of container group reallocations per minute
          type: integer
          format: int32
          examples:
            - 10
          maximum: 2147483647
          minimum: 0
        max_container_group_recreates_per_minute:
          description: The maximum number of container group recreates per minute
          type: integer
          format: int32
          examples:
            - 10
          maximum: 2147483647
          minimum: 0
        max_container_group_restarts_per_minute:
          description: The maximum number of container group restarts per minute
          type: integer
          format: int32
          examples:
            - 10
          maximum: 2147483647
          minimum: 0
      required:
        - container_replicas_quota
        - container_replicas_used
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Salad-Api-Key

````