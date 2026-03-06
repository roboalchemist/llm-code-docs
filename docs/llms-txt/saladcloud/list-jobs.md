# Source: https://docs.salad.com/reference/saladcloud-api/queues/list-jobs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Jobs

> Gets the list of jobs in a queue

*Last Updated: July 1, 2025*


## OpenAPI

````yaml api-specs/salad-cloud.yaml get /organizations/{organization_name}/projects/{project_name}/queues/{queue_name}/jobs
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
  /organizations/{organization_name}/projects/{project_name}/queues/{queue_name}/jobs:
    summary: Jobs in a Queue
    description: Operations for jobs in a queue
    parameters:
      - $ref: '#/components/parameters/organization_name'
      - $ref: '#/components/parameters/project_name'
      - $ref: '#/components/parameters/queue_name'
    get:
      tags:
        - queues
      summary: List Jobs
      description: Gets the list of jobs in a queue
      operationId: list_queue_jobs
      parameters:
        - $ref: '#/components/parameters/Page'
        - $ref: '#/components/parameters/PageSize'
      responses:
        '200':
          $ref: '#/components/responses/ListQueueJobs'
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

            result = sdk.queues.list_queue_jobs(
                organization_name="acme-corp",
                project_name="dev-env",
                queue_name="fifo-queue",
                page=1,
                page_size=1
            )

            print(result)
          lang: Python
        - source: >-
            using Salad.Cloud.SDK;

            using Salad.Cloud.SDK.Config;


            var config = new SaladCloudSdkConfig{};


            var client = new SaladCloudSdkClient(config);


            var response = await client.Queues.ListQueueJobsAsync("acme-corp",
            "dev-env", "fifo-queue", 1, 1);


            Console.WriteLine(response);
          lang: C#
        - source: >-
            import (
              "fmt"
              "encoding/json"
              "context"
              "github.com/saladtechnologies/salad-cloud-sdk-go/pkg/saladcloudsdkconfig"
              "github.com/saladtechnologies/salad-cloud-sdk-go/pkg/saladcloudsdk"
              "github.com/saladtechnologies/salad-cloud-sdk-go/pkg/util"
              "github.com/saladtechnologies/salad-cloud-sdk-go/pkg/queues"
            )


            config := saladcloudsdkconfig.NewConfig()

            config.SetApiKey("API_KEY")

            client := saladcloudsdk.NewSaladCloudSdk(config)



            params := queues.ListQueueJobsRequestParams{
              Page: util.ToPointer(int64(1)),
              PageSize: util.ToPointer(int64(1)),
            }


            response, err := client.Queues.ListQueueJobs(context.Background(),
            "acme-corp", "dev-env", "fifo-queue", params)

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

              const { data } = await saladCloudSdk.queues.listQueueJobs('acme-corp', 'dev-env', 'fifo-queue', {
                page: 1,
                pageSize: 1,
              });

              console.log(data);
            })();
          lang: TypeScript
        - source: |-
            import com.salad.cloud.sdk.SaladCloudSdk;
            import com.salad.cloud.sdk.config.ApiKeyAuthConfig;
            import com.salad.cloud.sdk.config.SaladCloudSdkConfig;
            import com.salad.cloud.sdk.models.ListQueueJobsParameters;
            import com.salad.cloud.sdk.models.QueueJobCollection;

            public class Main {

              public static void main(String[] args) {
                SaladCloudSdkConfig config = SaladCloudSdkConfig.builder()
                  .apiKeyAuthConfig(ApiKeyAuthConfig.builder().apiKey("YOUR_API_KEY").build())
                  .build();

                SaladCloudSdk saladCloudSdk = new SaladCloudSdk(config);

                ListQueueJobsParameters requestParameters = ListQueueJobsParameters.builder().page(1L).pageSize(1L).build();

                QueueJobCollection response = saladCloudSdk.queues.listQueueJobs(
                  "acme-corp",
                  "dev-env",
                  "fifo-queue",
                  requestParameters
                );

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
    project_name:
      name: project_name
      in: path
      description: >-
        Your project name. This represents a collection of related SaladCloud
        resources. The project must be created before using the API.
      required: true
      schema:
        $ref: '#/components/schemas/ProjectName'
    queue_name:
      in: path
      name: queue_name
      required: true
      schema:
        type: string
        examples:
          - fifo-queue
        maxLength: 63
        minLength: 2
        pattern: ^[a-z][a-z0-9-]{0,61}[a-z0-9]$
      description: The queue name.
    Page:
      in: query
      name: page
      description: The page number.
      schema:
        $ref: '#/components/schemas/Page'
    PageSize:
      in: query
      name: page_size
      description: The maximum number of items per page.
      schema:
        $ref: '#/components/schemas/PageSize'
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
    ListQueueJobs:
      description: OK
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/QueueJobCollection'
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
    ProjectName:
      description: The project name.
      type: string
      examples:
        - dev-env
      maxLength: 63
      minLength: 2
      pattern: ^[a-z][a-z0-9-]{0,61}[a-z0-9]$
    Page:
      description: The page number.
      type: integer
      format: int32
      examples:
        - 1
      maximum: 2147483647
      minimum: 1
    PageSize:
      description: The maximum number of items per page.
      type: integer
      format: int32
      examples:
        - 1
      maximum: 100
      minimum: 1
    QueueJobCollection:
      description: Represents a Queue Job Collection
      type: object
      properties:
        items:
          description: The list of queue jobs
          type: array
          items:
            $ref: '#/components/schemas/QueueJob'
          maxItems: 100
          minItems: 0
      required:
        - items
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
    QueueJob:
      description: Represents a queue job
      type: object
      properties:
        id:
          description: The job identifier
          type: string
          format: uuid
        input:
          $ref: '#/components/schemas/QueueJobInput'
        metadata:
          $ref: '#/components/schemas/QueueJobMetadata'
        webhook:
          description: The webhook URL to notify when the job completes
          type: string
          format: url
          maxLength: 27
          minLength: 20
          pattern: >-
            ^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[+-]\\d{2}:\\d{2})$
        status:
          description: The job status
          type: string
          enum:
            - pending
            - running
            - succeeded
            - cancelled
            - failed
        events:
          description: The job events
          type: array
          items:
            $ref: '#/components/schemas/QueueJobEvent'
          maxItems: 1000
          minItems: 0
        output:
          $ref: '#/components/schemas/QueueJobOutput'
        create_time:
          description: The job creation time
          type: string
          format: date-time
        update_time:
          description: The job update time
          type: string
          format: date-time
      required:
        - id
        - input
        - status
        - events
        - create_time
        - update_time
    QueueJobInput:
      description: The job input. May be any valid JSON.
    QueueJobMetadata:
      description: Additional metadata for the job
      type: object
      maxProperties: 20
    QueueJobEvent:
      description: Represents an event for queue job
      type: object
      properties:
        action:
          description: The action that was taken on the queue job
          type: string
          enum:
            - created
            - started
            - succeeded
            - cancelled
            - failed
        time:
          description: The time the action was taken on the queue job
          type: string
          format: date-time
      required:
        - action
        - time
    QueueJobOutput:
      description: The job output. May be any valid JSON.
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Salad-Api-Key

````