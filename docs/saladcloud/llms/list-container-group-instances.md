# Source: https://docs.salad.com/reference/saladcloud-api/container-groups/list-container-group-instances.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Container Group Instances

> Gets the list of container group instances

*Last Updated: July 1, 2025*


## OpenAPI

````yaml api-specs/salad-cloud.yaml get /organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/instances
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
  /organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/instances:
    summary: Container Group Instances
    description: Operations for container group instances
    parameters:
      - $ref: '#/components/parameters/organization_name'
      - $ref: '#/components/parameters/project_name'
      - $ref: '#/components/parameters/container_group_name'
    get:
      tags:
        - container_groups
      summary: List Container Group Instances
      description: Gets the list of container group instances
      operationId: list_container_group_instances
      responses:
        '200':
          $ref: '#/components/responses/ListContainerGroupInstances'
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

            result = sdk.container_groups.list_container_group_instances(
                organization_name="acme-corp",
                project_name="dev-env",
                container_group_name="mandlebrot"
            )

            print(result)
          lang: Python
        - source: >-
            using Salad.Cloud.SDK;

            using Salad.Cloud.SDK.Config;


            var config = new SaladCloudSdkConfig{};


            var client = new SaladCloudSdkClient(config);


            var response = await
            client.ContainerGroups.ListContainerGroupInstancesAsync("acme-corp",
            "dev-env", "mandlebrot");


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


            response, err :=
            client.ContainerGroups.ListContainerGroupInstances(context.Background(),
            "acme-corp", "dev-env", "mandlebrot")

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

              const { data } = await saladCloudSdk.containerGroups.listContainerGroupInstances(
                'acme-corp',
                'dev-env',
                'mandlebrot',
              );

              console.log(data);
            })();
          lang: TypeScript
        - source: |-
            import com.salad.cloud.sdk.SaladCloudSdk;
            import com.salad.cloud.sdk.config.ApiKeyAuthConfig;
            import com.salad.cloud.sdk.config.SaladCloudSdkConfig;
            import com.salad.cloud.sdk.models.ContainerGroupInstanceCollection;

            public class Main {

              public static void main(String[] args) {
                SaladCloudSdkConfig config = SaladCloudSdkConfig.builder()
                  .apiKeyAuthConfig(ApiKeyAuthConfig.builder().apiKey("YOUR_API_KEY").build())
                  .build();

                SaladCloudSdk saladCloudSdk = new SaladCloudSdk(config);

                ContainerGroupInstanceCollection response = saladCloudSdk.containerGroups.listContainerGroupInstances(
                  "acme-corp",
                  "dev-env",
                  "mandlebrot"
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
    container_group_name:
      in: path
      name: container_group_name
      description: The unique container group name
      required: true
      schema:
        $ref: '#/components/schemas/ContainerGroupName'
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
    ListContainerGroupInstances:
      description: OK
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ContainerGroupInstanceCollection'
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
    ContainerGroupName:
      description: The container group name.
      type: string
      examples:
        - mandlebrot
      maxLength: 63
      minLength: 2
      pattern: ^[a-z][a-z0-9-]{0,61}[a-z0-9]$
      title: Container Group Name
    ContainerGroupInstanceCollection:
      description: >-
        A collection of container group instances returned as part of a
        paginated response or batch operation result.
      type: object
      properties:
        instances:
          description: >-
            An array of container group instances, each representing a deployed
            container group with its current state and configuration
            information.
          type: array
          items:
            $ref: '#/components/schemas/ContainerGroupInstance'
          maxItems: 1000
          minItems: 0
      required:
        - instances
      title: Container Group Instance Collection
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
    ContainerGroupInstance:
      description: >-
        A Container Group Instance represents a running instance of a container
        group on a specific machine. It provides information about the execution
        state, readiness, and version of the deployed container group.
      type: object
      properties:
        id:
          $ref: '#/components/schemas/ContainerGroupInstanceId'
        machine_id:
          $ref: '#/components/schemas/ContainerGroupMachineId'
        ssh_ip:
          $ref: '#/components/schemas/ContainerGroupInstanceSshIp'
        ssh_port:
          $ref: '#/components/schemas/ContainerGroupInstanceSshPort'
        ssh_host_key_fingerprint:
          $ref: '#/components/schemas/ContainerGroupInstanceSshHostKeyFingerprint'
        state:
          $ref: '#/components/schemas/ContainerGroupInstanceState'
        update_time:
          description: >-
            The UTC timestamp when the container group instance last changed its
            state. This helps track the lifecycle and state transitions of the
            instance.
          type: string
          format: date-time
        version:
          description: >-
            The version of the container group definition currently running on
            this instance. Used to track deployment and update progress across
            the container group fleet.
          type: integer
          format: int32
          maximum: 2147483647
          minimum: 1
        ready:
          description: >-
            Indicates whether the container group instance is currently passing
            its readiness checks and is able to receive traffic or perform its
            intended function. If no readiness probe is defined, this will be
            true once the instance is fully started.
          type: boolean
        started:
          description: >-
            Indicates whether the container group instance has successfully
            completed its startup sequence and passed any configured startup
            probes. This will always be true when no startup probe is defined
            for the container group.
          type: boolean
        deletion_cost:
          description: The cost of deleting the container group instance
          type: integer
          default: 0
          maximum: 100000
          minimum: 0
      required:
        - id
        - machine_id
        - state
        - update_time
        - version
    ContainerGroupInstanceId:
      description: The container group instance identifier.
      type: string
      format: uuid
      examples:
        - db3a4591-efc3-46c0-b06a-3d820c0ec100
      title: Container Group Instance ID
    ContainerGroupMachineId:
      description: The container group machine identifier.
      type: string
      format: uuid
      examples:
        - eb3a4591-efc3-46c0-b06a-3d820c0ec100
      title: Container Group Machine ID
    ContainerGroupInstanceSshIp:
      description: The SSH IP address of the container group instance
      type: string
      format: ipv4
      example: 192.168.1.100
    ContainerGroupInstanceSshPort:
      description: The SSH port of the container group instance
      type: integer
      format: int32
      default: 22
      maximum: 65535
      minimum: 1
    ContainerGroupInstanceSshHostKeyFingerprint:
      description: The SSH host key fingerprint of the container group instance
      type: string
      example: SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8
      maxLength: 256
      minLength: 1
    ContainerGroupInstanceState:
      description: The state of the container group instance
      type: string
      enum:
        - allocating
        - downloading
        - creating
        - running
        - stopping
      title: The Container Group Instance State
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Salad-Api-Key

````