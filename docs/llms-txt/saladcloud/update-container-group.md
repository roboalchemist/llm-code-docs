# Source: https://docs.salad.com/reference/saladcloud-api/container-groups/update-container-group.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Container Group

> Updates a container group

*Last Updated: July 1, 2025*


## OpenAPI

````yaml api-specs/salad-cloud.yaml patch /organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}
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
  /organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}:
    summary: Container Group
    description: Operations for a container group
    parameters:
      - $ref: '#/components/parameters/organization_name'
      - $ref: '#/components/parameters/project_name'
      - $ref: '#/components/parameters/container_group_name'
    patch:
      tags:
        - container_groups
      summary: Update Container Group
      description: Updates a container group
      operationId: update_container_group
      requestBody:
        $ref: '#/components/requestBodies/UpdateContainerGroup'
      responses:
        '200':
          $ref: '#/components/responses/UpdateContainerGroup'
        '400':
          $ref: '#/components/responses/400'
        '403':
          $ref: '#/components/responses/403'
        '404':
          $ref: '#/components/responses/404'
        '429':
          $ref: '#/components/responses/429'
        default:
          $ref: '#/components/responses/UnknownError'
      x-codeSamples:
        - source: |-
            from salad_cloud_sdk import SaladCloudSdk
            from salad_cloud_sdk.models import ContainerGroupPatch

            sdk = SaladCloudSdk(
                api_key="YOUR_API_KEY",
                api_key_header="YOUR_API_KEY_HEADER",
                timeout=10000
            )

            request_body = ContainerGroupPatch(
                display_name="ZJjdnvu",
                container={
                    "command": [
                        "command"
                    ],
                    "environment_variables": {},
                    "image": "image",
                    "image_caching": True,
                    "logging": {
                        "axiom": {
                            "host": "host",
                            "api_token": "api_token",
                            "dataset": "dataset"
                        },
                        "datadog": {
                            "host": "host",
                            "api_key": "api_key",
                            "tags": [
                                {
                                    "name": "name",
                                    "value": "value"
                                }
                            ]
                        },
                        "http": {
                            "host": "host",
                            "port": 55354,
                            "user": "user",
                            "password": "password",
                            "path": "path",
                            "format": "json",
                            "headers": [
                                {
                                    "name": "name",
                                    "value": "value"
                                }
                            ],
                            "compression": "none"
                        },
                        "new_relic": {
                            "host": "host",
                            "ingestion_key": "ingestion_key"
                        },
                        "splunk": {
                            "host": "host",
                            "token": "token"
                        },
                        "tcp": {
                            "host": "host",
                            "port": 44671
                        }
                    },
                    "priority": "high",
                    "registry_authentication": {
                        "aws_ecr": {
                            "access_key_id": "access_key_id",
                            "secret_access_key": "secret_access_key"
                        },
                        "basic": {
                            "username": "username",
                            "password": "password"
                        },
                        "docker_hub": {
                            "username": "username",
                            "personal_access_token": "personal_access_token"
                        },
                        "gcp_gar": {
                            "service_key": "service_key"
                        },
                        "gcp_gcr": {
                            "service_key": "service_key"
                        }
                    },
                    "resources": {
                        "cpu": 1013,
                        "memory": 352043675,
                        "gpu_classes": [
                            "gpu_classes"
                        ],
                        "storage_amount": 1032076497908566.1,
                        "shm_size": 64
                    }
                },
                replicas=56,
                country_codes=[
                    "af"
                ],
                networking={
                    "port": 13142
                },
                liveness_probe={
                    "exec_": {
                        "command": [
                            "command"
                        ]
                    },
                    "failure_threshold": 3,
                    "grpc": {
                        "port": 37648,
                        "service": "service"
                    },
                    "http": {
                        "headers": [
                            {
                                "name": "name",
                                "value": "value"
                            }
                        ],
                        "path": "path",
                        "port": 29069,
                        "scheme": "http"
                    },
                    "initial_delay_seconds": 670,
                    "period_seconds": 10,
                    "success_threshold": 1,
                    "tcp": {
                        "port": 13817
                    },
                    "timeout_seconds": 30
                },
                readiness_probe={
                    "exec_": {
                        "command": [
                            "command"
                        ]
                    },
                    "failure_threshold": 3,
                    "grpc": {
                        "port": 37648,
                        "service": "service"
                    },
                    "http": {
                        "headers": [
                            {
                                "name": "name",
                                "value": "value"
                            }
                        ],
                        "path": "path",
                        "port": 29069,
                        "scheme": "http"
                    },
                    "initial_delay_seconds": 262,
                    "period_seconds": 1,
                    "success_threshold": 1,
                    "tcp": {
                        "port": 13817
                    },
                    "timeout_seconds": 1
                },
                startup_probe={
                    "exec_": {
                        "command": [
                            "command"
                        ]
                    },
                    "failure_threshold": 15,
                    "grpc": {
                        "port": 37648,
                        "service": "service"
                    },
                    "http": {
                        "headers": [
                            {
                                "name": "name",
                                "value": "value"
                            }
                        ],
                        "path": "path",
                        "port": 29069,
                        "scheme": "http"
                    },
                    "initial_delay_seconds": 1106,
                    "tcp": {
                        "port": 13817
                    },
                    "period_seconds": 3,
                    "success_threshold": 2,
                    "timeout_seconds": 10
                },
                queue_autoscaler={
                    "desired_queue_length": 53,
                    "max_replicas": 291,
                    "max_downscale_per_minute": 65,
                    "max_upscale_per_minute": 100,
                    "min_replicas": 54,
                    "polling_period": 140
                }
            )

            result = sdk.container_groups.update_container_group(
                request_body=request_body,
                organization_name="acme-corp",
                project_name="dev-env",
                container_group_name="mandlebrot"
            )

            print(result)
          lang: Python
        - source: >-
            using Salad.Cloud.SDK;

            using Salad.Cloud.SDK.Config;

            using Salad.Cloud.SDK.Models;


            var config = new SaladCloudSdkConfig{};


            var client = new SaladCloudSdkClient(config);


            var command = new List<string>() { "command" };

            var axiom = new AxiomLoggingConfiguration("host", "api_token",
            "dataset");

            var tagsItem = new DatadogTagForContainerLogging("name", "value");

            var tags = new List<DatadogTagForContainerLogging>() { tagsItem };

            var datadog = new DatadogLoggingConfiguration("host", "api_key",
            tags);

            var headersItem = new ContainerLoggingHttpHeader("name", "value");

            var headers = new List<ContainerLoggingHttpHeader>() { headersItem
            };

            var http = new ContainerLoggingConfigurationHttp1("host", 55354,
            ContainerLoggingHttpFormat.Json, headers,
            ContainerLoggingHttpCompression.None, "user", "password", "path");

            var newRelic = new NewRelicLoggingConfiguration("host",
            "ingestion_key");

            var splunk = new ContainerLoggingSplunkConfiguration("host",
            "token");

            var tcp = new TcpLoggingConfiguration("host", 44671);

            var logging = new UpdateContainerLogging(axiom, datadog, http,
            newRelic, splunk, tcp);

            var awsEcr = new
            ContainerRegistryAuthenticationAwsEcr("access_key_id",
            "secret_access_key");

            var basic = new ContainerRegistryAuthenticationBasic("username",
            "password");

            var dockerHub = new
            ContainerRegistryAuthenticationDockerHub("username",
            "personal_access_token");

            var gcpGar = new
            ContainerRegistryAuthenticationGcpGar("service_key");

            var gcpGcr = new
            ContainerRegistryAuthenticationGcpGcr("service_key");

            var registryAuthentication = new
            ContainerRegistryAuthentication(awsEcr, basic, dockerHub, gcpGar,
            gcpGcr);

            var gpuClasses = new List<string>() { "gpu_classes" };

            var resources = new ContainerResourceUpdateSchema(1013, 352043675,
            gpuClasses, 1032076497908566.1, 64);

            var container = new UpdateContainer(command, new object(), "image",
            true, logging, ContainerGroupPriority.High, registryAuthentication,
            resources);

            var countryCodes = new List<CountryCode>() { CountryCode.Af };

            var networking = new UpdateContainerGroupNetworking(13142);

            var command = new List<string>() { "command" };

            var exec = new ContainerGroupProbeExec(command);

            var grpc = new ContainerGroupGRpcProbe(37648, "service");

            var headersItem = new ContainerGroupProbeHttpHeader("name",
            "value");

            var headers = new List<ContainerGroupProbeHttpHeader>() {
            headersItem };

            var http = new ContainerGroupHttpProbeConfiguration(headers, "path",
            29069, HttpScheme.Http);

            var tcp = new ContainerGroupTcpProbe(13817);

            var livenessProbe = new ContainerGroupLivenessProbe(3, 670, 10, 1,
            30, exec, grpc, http, tcp);

            var command = new List<string>() { "command" };

            var exec = new ContainerGroupProbeExec(command);

            var grpc = new ContainerGroupGRpcProbe(37648, "service");

            var headersItem = new ContainerGroupProbeHttpHeader("name",
            "value");

            var headers = new List<ContainerGroupProbeHttpHeader>() {
            headersItem };

            var http = new ContainerGroupHttpProbeConfiguration(headers, "path",
            29069, HttpScheme.Http);

            var tcp = new ContainerGroupTcpProbe(13817);

            var readinessProbe = new ContainerGroupReadinessProbe(3, 262, 1, 1,
            1, exec, grpc, http, tcp);

            var command = new List<string>() { "command" };

            var exec = new ContainerGroupProbeExec(command);

            var grpc = new ContainerGroupGRpcProbe(37648, "service");

            var headersItem = new ContainerGroupProbeHttpHeader("name",
            "value");

            var headers = new List<ContainerGroupProbeHttpHeader>() {
            headersItem };

            var http = new ContainerGroupHttpProbeConfiguration(headers, "path",
            29069, HttpScheme.Http);

            var tcp = new ContainerGroupTcpProbe(13817);

            var startupProbe = new ContainerGroupStartupProbe(15, 1106, 3, 2,
            10, exec, grpc, http, tcp);

            var queueAutoscaler = new QueueBasedAutoscalerConfiguration(53, 291,
            54, 65, 100, 140);

            var input = new ContainerGroupPatch("ZJjdnvu", container, 56,
            countryCodes, networking, livenessProbe, readinessProbe,
            startupProbe, queueAutoscaler);


            var response = await
            client.ContainerGroups.UpdateContainerGroupAsync(input, "acme-corp",
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
              "github.com/saladtechnologies/salad-cloud-sdk-go/pkg/util"
              "github.com/saladtechnologies/salad-cloud-sdk-go/pkg/containergroups"
            )


            config := saladcloudsdkconfig.NewConfig()

            config.SetApiKey("API_KEY")

            client := saladcloudsdk.NewSaladCloudSdk(config)



            axiomLoggingConfiguration := shared.AxiomLoggingConfiguration{
              Host: util.ToPointer("host"),
              ApiToken: util.ToPointer("api_token"),
              Dataset: util.ToPointer("dataset"),
            }



            datadogTagForContainerLogging :=
            shared.DatadogTagForContainerLogging{
              Name: util.ToPointer("name"),
              Value: util.ToPointer("value"),
            }


            datadogLoggingConfiguration := shared.DatadogLoggingConfiguration{
              Host: util.ToPointer("host"),
              ApiKey: util.ToPointer("api_key"),
              Tags: []shared.DatadogTagForContainerLogging{datadogTagForContainerLogging},
            }


            containerLoggingHttpFormat :=
            shared.CONTAINER_LOGGING_HTTP_FORMAT_JSON



            containerLoggingHttpHeader := shared.ContainerLoggingHttpHeader{
              Name: util.ToPointer("name"),
              Value: util.ToPointer("value"),
            }


            containerLoggingHttpCompression :=
            shared.CONTAINER_LOGGING_HTTP_COMPRESSION_NONE


            containerLoggingConfigurationHttp1 :=
            shared.ContainerLoggingConfigurationHttp1{
              Host: util.ToPointer("host"),
              Port: util.ToPointer(int64(55354)),
              User: util.ToPointer(util.Nullable[string]{ Value: "user" }),
              Password: util.ToPointer(util.Nullable[string]{ Value: "password" }),
              Path: util.ToPointer(util.Nullable[string]{ Value: "path" }),
              Format: &containerLoggingHttpFormat,
              Headers: []shared.ContainerLoggingHttpHeader{containerLoggingHttpHeader},
              Compression: &containerLoggingHttpCompression,
            }



            newRelicLoggingConfiguration := shared.NewRelicLoggingConfiguration{
              Host: util.ToPointer("host"),
              IngestionKey: util.ToPointer("ingestion_key"),
            }



            containerLoggingSplunkConfiguration :=
            shared.ContainerLoggingSplunkConfiguration{
              Host: util.ToPointer("host"),
              Token: util.ToPointer("token"),
            }



            tcpLoggingConfiguration := shared.TcpLoggingConfiguration{
              Host: util.ToPointer("host"),
              Port: util.ToPointer(int64(44671)),
            }


            updateContainerLogging := containergroups.UpdateContainerLogging{
              Axiom: &axiomLoggingConfiguration,
              Datadog: &datadogLoggingConfiguration,
              Http: &containerLoggingConfigurationHttp1,
              NewRelic: &newRelicLoggingConfiguration,
              Splunk: &containerLoggingSplunkConfiguration,
              Tcp: &tcpLoggingConfiguration,
            }


            containerGroupPriority := shared.CONTAINER_GROUP_PRIORITY_HIGH



            containerRegistryAuthenticationAwsEcr :=
            containergroups.ContainerRegistryAuthenticationAwsEcr{
              AccessKeyId: util.ToPointer("access_key_id"),
              SecretAccessKey: util.ToPointer("secret_access_key"),
            }



            containerRegistryAuthenticationBasic :=
            containergroups.ContainerRegistryAuthenticationBasic{
              Username: util.ToPointer("username"),
              Password: util.ToPointer("password"),
            }



            containerRegistryAuthenticationDockerHub :=
            containergroups.ContainerRegistryAuthenticationDockerHub{
              Username: util.ToPointer("username"),
              PersonalAccessToken: util.ToPointer("personal_access_token"),
            }



            containerRegistryAuthenticationGcpGar :=
            containergroups.ContainerRegistryAuthenticationGcpGar{
              ServiceKey: util.ToPointer("service_key"),
            }



            containerRegistryAuthenticationGcpGcr :=
            containergroups.ContainerRegistryAuthenticationGcpGcr{
              ServiceKey: util.ToPointer("service_key"),
            }


            containerRegistryAuthentication :=
            containergroups.ContainerRegistryAuthentication{
              AwsEcr: &containerRegistryAuthenticationAwsEcr,
              Basic: &containerRegistryAuthenticationBasic,
              DockerHub: &containerRegistryAuthenticationDockerHub,
              GcpGar: &containerRegistryAuthenticationGcpGar,
              GcpGcr: &containerRegistryAuthenticationGcpGcr,
            }



            containerResourceUpdateSchema :=
            containergroups.ContainerResourceUpdateSchema{
              Cpu: util.ToPointer(util.Nullable[int64]{ Value: int64(1013) }),
              Memory: util.ToPointer(util.Nullable[int64]{ Value: int64(352043675) }),
              GpuClasses: []string{},
              StorageAmount: util.ToPointer(util.Nullable[int64]{ Value: int64(1032076497908566.1) }),
              ShmSize: util.ToPointer(util.Nullable[int64]{ Value: int64(64) }),
            }


            updateContainer := containergroups.UpdateContainer{
              Command: []string{},
              EnvironmentVariables: map[string]string{},
              Image: util.ToPointer(util.Nullable[string]{ Value: "image" }),
              ImageCaching: util.ToPointer(true),
              Logging: &updateContainerLogging,
              Priority: &containerGroupPriority,
              RegistryAuthentication: &containerRegistryAuthentication,
              Resources: &containerResourceUpdateSchema,
            }


            countryCode := shared.COUNTRY_CODE_AF



            updateContainerGroupNetworking :=
            containergroups.UpdateContainerGroupNetworking{
              Port: util.ToPointer(util.Nullable[int64]{ Value: int64(13142) }),
            }



            containerGroupProbeExec := shared.ContainerGroupProbeExec{
              Command: []string{},
            }



            containerGroupGRpcProbe := shared.ContainerGroupGRpcProbe{
              Port: util.ToPointer(int64(37648)),
              Service: util.ToPointer("service"),
            }



            containerGroupProbeHttpHeader :=
            shared.ContainerGroupProbeHttpHeader{
              Name: util.ToPointer("name"),
              Value: util.ToPointer("value"),
            }


            httpScheme := shared.HTTP_SCHEME_HTTP


            containerGroupHttpProbeConfiguration :=
            shared.ContainerGroupHttpProbeConfiguration{
              Headers: []shared.ContainerGroupProbeHttpHeader{containerGroupProbeHttpHeader},
              Path: util.ToPointer("path"),
              Port: util.ToPointer(int64(29069)),
              Scheme: &httpScheme,
            }



            containerGroupTcpProbe := shared.ContainerGroupTcpProbe{
              Port: util.ToPointer(int64(13817)),
            }


            containerGroupLivenessProbe := shared.ContainerGroupLivenessProbe{
              Exec: &containerGroupProbeExec,
              FailureThreshold: util.ToPointer(int64(3)),
              Grpc: &containerGroupGRpcProbe,
              Http: &containerGroupHttpProbeConfiguration,
              InitialDelaySeconds: util.ToPointer(int64(670)),
              PeriodSeconds: util.ToPointer(int64(10)),
              SuccessThreshold: util.ToPointer(int64(1)),
              Tcp: &containerGroupTcpProbe,
              TimeoutSeconds: util.ToPointer(int64(30)),
            }



            containerGroupProbeExec := shared.ContainerGroupProbeExec{
              Command: []string{},
            }



            containerGroupGRpcProbe := shared.ContainerGroupGRpcProbe{
              Port: util.ToPointer(int64(37648)),
              Service: util.ToPointer("service"),
            }



            containerGroupProbeHttpHeader :=
            shared.ContainerGroupProbeHttpHeader{
              Name: util.ToPointer("name"),
              Value: util.ToPointer("value"),
            }


            httpScheme := shared.HTTP_SCHEME_HTTP


            containerGroupHttpProbeConfiguration :=
            shared.ContainerGroupHttpProbeConfiguration{
              Headers: []shared.ContainerGroupProbeHttpHeader{containerGroupProbeHttpHeader},
              Path: util.ToPointer("path"),
              Port: util.ToPointer(int64(29069)),
              Scheme: &httpScheme,
            }



            containerGroupTcpProbe := shared.ContainerGroupTcpProbe{
              Port: util.ToPointer(int64(13817)),
            }


            containerGroupReadinessProbe := shared.ContainerGroupReadinessProbe{
              Exec: &containerGroupProbeExec,
              FailureThreshold: util.ToPointer(int64(3)),
              Grpc: &containerGroupGRpcProbe,
              Http: &containerGroupHttpProbeConfiguration,
              InitialDelaySeconds: util.ToPointer(int64(262)),
              PeriodSeconds: util.ToPointer(int64(1)),
              SuccessThreshold: util.ToPointer(int64(1)),
              Tcp: &containerGroupTcpProbe,
              TimeoutSeconds: util.ToPointer(int64(1)),
            }



            containerGroupProbeExec := shared.ContainerGroupProbeExec{
              Command: []string{},
            }



            containerGroupGRpcProbe := shared.ContainerGroupGRpcProbe{
              Port: util.ToPointer(int64(37648)),
              Service: util.ToPointer("service"),
            }



            containerGroupProbeHttpHeader :=
            shared.ContainerGroupProbeHttpHeader{
              Name: util.ToPointer("name"),
              Value: util.ToPointer("value"),
            }


            httpScheme := shared.HTTP_SCHEME_HTTP


            containerGroupHttpProbeConfiguration :=
            shared.ContainerGroupHttpProbeConfiguration{
              Headers: []shared.ContainerGroupProbeHttpHeader{containerGroupProbeHttpHeader},
              Path: util.ToPointer("path"),
              Port: util.ToPointer(int64(29069)),
              Scheme: &httpScheme,
            }



            containerGroupTcpProbe := shared.ContainerGroupTcpProbe{
              Port: util.ToPointer(int64(13817)),
            }


            containerGroupStartupProbe := shared.ContainerGroupStartupProbe{
              Exec: &containerGroupProbeExec,
              FailureThreshold: util.ToPointer(int64(15)),
              Grpc: &containerGroupGRpcProbe,
              Http: &containerGroupHttpProbeConfiguration,
              InitialDelaySeconds: util.ToPointer(int64(1106)),
              Tcp: &containerGroupTcpProbe,
              PeriodSeconds: util.ToPointer(int64(3)),
              SuccessThreshold: util.ToPointer(int64(2)),
              TimeoutSeconds: util.ToPointer(int64(10)),
            }



            queueBasedAutoscalerConfiguration :=
            shared.QueueBasedAutoscalerConfiguration{
              DesiredQueueLength: util.ToPointer(int64(53)),
              MaxReplicas: util.ToPointer(int64(291)),
              MaxDownscalePerMinute: util.ToPointer(int64(65)),
              MaxUpscalePerMinute: util.ToPointer(int64(100)),
              MinReplicas: util.ToPointer(int64(54)),
              PollingPeriod: util.ToPointer(int64(140)),
            }


            request := containergroups.ContainerGroupPatch{
              DisplayName: util.ToPointer(util.Nullable[string]{ Value: "ZJjdnvu" }),
              Container: &updateContainer,
              Replicas: util.ToPointer(util.Nullable[int64]{ Value: int64(56) }),
              CountryCodes: []shared.CountryCode{countryCode},
              Networking: &updateContainerGroupNetworking,
              LivenessProbe: &containerGroupLivenessProbe,
              ReadinessProbe: &containerGroupReadinessProbe,
              StartupProbe: &containerGroupStartupProbe,
              QueueAutoscaler: &queueBasedAutoscalerConfiguration,
            }


            response, err :=
            client.ContainerGroups.UpdateContainerGroup(context.Background(),
            "acme-corp", "dev-env", "mandlebrot", request)

            if err != nil {
              panic(err)
            }


            fmt.Println(response)
          lang: Go
        - source: |-
            import {
              AxiomLoggingConfiguration,
              ContainerGroupGRpcProbe,
              ContainerGroupHttpProbeConfiguration,
              ContainerGroupLivenessProbe,
              ContainerGroupPatch,
              ContainerGroupPriority,
              ContainerGroupProbeExec,
              ContainerGroupProbeHttpHeader,
              ContainerGroupReadinessProbe,
              ContainerGroupStartupProbe,
              ContainerGroupTcpProbe,
              ContainerLoggingConfigurationHttp1,
              ContainerLoggingHttpCompression,
              ContainerLoggingHttpFormat,
              ContainerLoggingHttpHeader,
              ContainerLoggingSplunkConfiguration,
              ContainerRegistryAuthentication,
              ContainerRegistryAuthenticationAwsEcr,
              ContainerRegistryAuthenticationBasic,
              ContainerRegistryAuthenticationDockerHub,
              ContainerRegistryAuthenticationGcpGar,
              ContainerRegistryAuthenticationGcpGcr,
              ContainerResourceUpdateSchema,
              CountryCode,
              DatadogLoggingConfiguration,
              DatadogTagForContainerLogging,
              HttpScheme,
              NewRelicLoggingConfiguration,
              QueueBasedAutoscalerConfiguration,
              SaladCloudSdk,
              TcpLoggingConfiguration,
              UpdateContainer,
              UpdateContainerGroupNetworking,
              UpdateContainerLogging,
            } from '@saladtechnologies-oss/salad-cloud-sdk';

            (async () => {
              const saladCloudSdk = new SaladCloudSdk({
                apiKey: 'YOUR_API_KEY',
              });

              const axiomLoggingConfiguration: AxiomLoggingConfiguration = {
                host: 'host',
                apiToken: 'api_token',
                dataset: 'dataset',
              };

              const datadogTagForContainerLogging: DatadogTagForContainerLogging = {
                name: 'name',
                value: 'value',
              };

              const datadogLoggingConfiguration: DatadogLoggingConfiguration = {
                host: 'host',
                apiKey: 'api_key',
                tags: [datadogTagForContainerLogging],
              };

              const containerLoggingHttpFormat = ContainerLoggingHttpFormat.JSON;

              const containerLoggingHttpHeader: ContainerLoggingHttpHeader = {
                name: 'name',
                value: 'value',
              };

              const containerLoggingHttpCompression = ContainerLoggingHttpCompression.NONE;

              const containerLoggingConfigurationHttp1: ContainerLoggingConfigurationHttp1 = {
                host: 'host',
                port: 55354,
                user: 'user',
                password: 'password',
                path: 'path',
                format: containerLoggingHttpFormat,
                headers: [containerLoggingHttpHeader],
                compression: containerLoggingHttpCompression,
              };

              const newRelicLoggingConfiguration: NewRelicLoggingConfiguration = {
                host: 'host',
                ingestionKey: 'ingestion_key',
              };

              const containerLoggingSplunkConfiguration: ContainerLoggingSplunkConfiguration = {
                host: 'host',
                token: 'token',
              };

              const tcpLoggingConfiguration: TcpLoggingConfiguration = {
                host: 'host',
                port: 44671,
              };

              const updateContainerLogging: UpdateContainerLogging = {
                axiom: axiomLoggingConfiguration,
                datadog: datadogLoggingConfiguration,
                http: containerLoggingConfigurationHttp1,
                newRelic: newRelicLoggingConfiguration,
                splunk: containerLoggingSplunkConfiguration,
                tcp: tcpLoggingConfiguration,
              };

              const containerGroupPriority = ContainerGroupPriority.HIGH;

              const containerRegistryAuthenticationAwsEcr: ContainerRegistryAuthenticationAwsEcr = {
                accessKeyId: 'access_key_id',
                secretAccessKey: 'secret_access_key',
              };

              const containerRegistryAuthenticationBasic: ContainerRegistryAuthenticationBasic = {
                username: 'username',
                password: 'password',
              };

              const containerRegistryAuthenticationDockerHub: ContainerRegistryAuthenticationDockerHub = {
                username: 'username',
                personalAccessToken: 'personal_access_token',
              };

              const containerRegistryAuthenticationGcpGar: ContainerRegistryAuthenticationGcpGar = {
                serviceKey: 'service_key',
              };

              const containerRegistryAuthenticationGcpGcr: ContainerRegistryAuthenticationGcpGcr = {
                serviceKey: 'service_key',
              };

              const containerRegistryAuthentication: ContainerRegistryAuthentication = {
                awsEcr: containerRegistryAuthenticationAwsEcr,
                basic: containerRegistryAuthenticationBasic,
                dockerHub: containerRegistryAuthenticationDockerHub,
                gcpGar: containerRegistryAuthenticationGcpGar,
                gcpGcr: containerRegistryAuthenticationGcpGcr,
              };

              const containerResourceUpdateSchema: ContainerResourceUpdateSchema = {
                cpu: 1013,
                memory: 352043675,
                gpuClasses: ['gpu_classes'],
                storageAmount: 1032076497908566.1,
                shmSize: 64,
              };

              const updateContainer: UpdateContainer = {
                command: ['command'],
                environmentVariables: [],
                image: 'image',
                imageCaching: true,
                logging: updateContainerLogging,
                priority: containerGroupPriority,
                registryAuthentication: containerRegistryAuthentication,
                resources: containerResourceUpdateSchema,
              };

              const countryCode = CountryCode.AF;

              const updateContainerGroupNetworking: UpdateContainerGroupNetworking = {
                port: 13142,
              };

              const containerGroupProbeExec: ContainerGroupProbeExec = {
                command: ['command'],
              };

              const containerGroupGRpcProbe: ContainerGroupGRpcProbe = {
                port: 37648,
                service: 'service',
              };

              const containerGroupProbeHttpHeader: ContainerGroupProbeHttpHeader = {
                name: 'name',
                value: 'value',
              };

              const httpScheme = HttpScheme.HTTP;

              const containerGroupHttpProbeConfiguration: ContainerGroupHttpProbeConfiguration = {
                headers: [containerGroupProbeHttpHeader],
                path: 'path',
                port: 29069,
                scheme: httpScheme,
              };

              const containerGroupTcpProbe: ContainerGroupTcpProbe = {
                port: 13817,
              };

              const containerGroupLivenessProbe: ContainerGroupLivenessProbe = {
                exec: containerGroupProbeExec,
                failureThreshold: 3,
                grpc: containerGroupGRpcProbe,
                http: containerGroupHttpProbeConfiguration,
                initialDelaySeconds: 670,
                periodSeconds: 10,
                successThreshold: 1,
                tcp: containerGroupTcpProbe,
                timeoutSeconds: 30,
              };

              const containerGroupReadinessProbe: ContainerGroupReadinessProbe = {
                exec: containerGroupProbeExec,
                failureThreshold: 3,
                grpc: containerGroupGRpcProbe,
                http: containerGroupHttpProbeConfiguration,
                initialDelaySeconds: 262,
                periodSeconds: 1,
                successThreshold: 1,
                tcp: containerGroupTcpProbe,
                timeoutSeconds: 1,
              };

              const containerGroupStartupProbe: ContainerGroupStartupProbe = {
                exec: containerGroupProbeExec,
                failureThreshold: 15,
                grpc: containerGroupGRpcProbe,
                http: containerGroupHttpProbeConfiguration,
                initialDelaySeconds: 1106,
                tcp: containerGroupTcpProbe,
                periodSeconds: 3,
                successThreshold: 2,
                timeoutSeconds: 10,
              };

              const queueBasedAutoscalerConfiguration: QueueBasedAutoscalerConfiguration = {
                desiredQueueLength: 53,
                maxReplicas: 291,
                maxDownscalePerMinute: 65,
                maxUpscalePerMinute: 100,
                minReplicas: 54,
                pollingPeriod: 140,
              };

              const containerGroupPatch: ContainerGroupPatch = {
                displayName: 'ZJjdnvu',
                container: updateContainer,
                replicas: 56,
                countryCodes: [countryCode],
                networking: updateContainerGroupNetworking,
                livenessProbe: containerGroupLivenessProbe,
                readinessProbe: containerGroupReadinessProbe,
                startupProbe: containerGroupStartupProbe,
                queueAutoscaler: queueBasedAutoscalerConfiguration,
              };

              const { data } = await saladCloudSdk.containerGroups.updateContainerGroup(
                'acme-corp',
                'dev-env',
                'mandlebrot',
                containerGroupPatch,
              );

              console.log(data);
            })();
          lang: TypeScript
        - source: "import com.salad.cloud.sdk.SaladCloudSdk;\nimport com.salad.cloud.sdk.config.ApiKeyAuthConfig;\nimport com.salad.cloud.sdk.config.SaladCloudSdkConfig;\nimport com.salad.cloud.sdk.models.AxiomLoggingConfiguration;\nimport com.salad.cloud.sdk.models.ContainerGroup;\nimport com.salad.cloud.sdk.models.ContainerGroupGRpcProbe;\nimport com.salad.cloud.sdk.models.ContainerGroupHttpProbeConfiguration;\nimport com.salad.cloud.sdk.models.ContainerGroupLivenessProbe;\nimport com.salad.cloud.sdk.models.ContainerGroupPatch;\nimport com.salad.cloud.sdk.models.ContainerGroupPriority;\nimport com.salad.cloud.sdk.models.ContainerGroupProbeExec;\nimport com.salad.cloud.sdk.models.ContainerGroupProbeHttpHeader;\nimport com.salad.cloud.sdk.models.ContainerGroupReadinessProbe;\nimport com.salad.cloud.sdk.models.ContainerGroupStartupProbe;\nimport com.salad.cloud.sdk.models.ContainerGroupTcpProbe;\nimport com.salad.cloud.sdk.models.ContainerLoggingConfigurationHttp1;\nimport com.salad.cloud.sdk.models.ContainerLoggingHttpCompression;\nimport com.salad.cloud.sdk.models.ContainerLoggingHttpFormat;\nimport com.salad.cloud.sdk.models.ContainerLoggingHttpHeader;\nimport com.salad.cloud.sdk.models.ContainerLoggingSplunkConfiguration;\nimport com.salad.cloud.sdk.models.ContainerRegistryAuthentication;\nimport com.salad.cloud.sdk.models.ContainerRegistryAuthenticationAwsEcr;\nimport com.salad.cloud.sdk.models.ContainerRegistryAuthenticationBasic;\nimport com.salad.cloud.sdk.models.ContainerRegistryAuthenticationDockerHub;\nimport com.salad.cloud.sdk.models.ContainerRegistryAuthenticationGcpGar;\nimport com.salad.cloud.sdk.models.ContainerRegistryAuthenticationGcpGcr;\nimport com.salad.cloud.sdk.models.ContainerResourceUpdateSchema;\nimport com.salad.cloud.sdk.models.CountryCode;\nimport com.salad.cloud.sdk.models.DatadogLoggingConfiguration;\nimport com.salad.cloud.sdk.models.DatadogTagForContainerLogging;\nimport com.salad.cloud.sdk.models.HttpScheme;\nimport com.salad.cloud.sdk.models.NewRelicLoggingConfiguration;\nimport com.salad.cloud.sdk.models.QueueBasedAutoscalerConfiguration;\nimport com.salad.cloud.sdk.models.TcpLoggingConfiguration;\nimport com.salad.cloud.sdk.models.UpdateContainer;\nimport com.salad.cloud.sdk.models.UpdateContainerGroupNetworking;\nimport com.salad.cloud.sdk.models.UpdateContainerLogging;\nimport java.util.Arrays;\nimport java.util.HashMap;\nimport java.util.List;\n\npublic class Main {\n    public static void main(String[] args) {\n\t\tSaladCloudSdkConfig config = SaladCloudSdkConfig.builder()\n\t\t\t.apiKeyAuthConfig(\n\t\t\t\tApiKeyAuthConfig.builder()\n\t\t\t\t\t.apiKey(\"YOUR_API_KEY\")\n\t\t\t\t\t.build()\n\t\t\t)\n\t\t\t.build();\n\n\t\tSaladCloudSdk saladCloudSdk = new SaladCloudSdk(config);\n\n\t\tList<String> commandList = Arrays.asList(\"command\");\n\n\t\tAxiomLoggingConfiguration axiomLoggingConfiguration = AxiomLoggingConfiguration.builder()\n\t\t\t.host(\"host\")\n\t\t\t.apiToken(\"api_token\")\n\t\t\t.dataset(\"dataset\")\n\t\t\t.build();\n\n\t\tDatadogTagForContainerLogging datadogTagForContainerLogging = DatadogTagForContainerLogging.builder()\n\t\t\t.name(\"name\")\n\t\t\t.value(\"value\")\n\t\t\t.build();\n\n\t\tList<DatadogTagForContainerLogging> tagsList = Arrays.asList(datadogTagForContainerLogging);\n\n\t\tDatadogLoggingConfiguration datadogLoggingConfiguration = DatadogLoggingConfiguration.builder()\n\t\t\t.host(\"host\")\n\t\t\t.apiKey(\"api_key\")\n\t\t\t.tags(tagsList)\n\t\t\t.build();\n\n\t\tContainerLoggingHttpHeader containerLoggingHttpHeader = ContainerLoggingHttpHeader.builder()\n\t\t\t.name(\"name\")\n\t\t\t.value(\"value\")\n\t\t\t.build();\n\n\t\tList<ContainerLoggingHttpHeader> headersList = Arrays.asList(containerLoggingHttpHeader);\n\n\t\tContainerLoggingConfigurationHttp1 containerLoggingConfigurationHttp1 = ContainerLoggingConfigurationHttp1.builder()\n\t\t\t.host(\"host\")\n\t\t\t.port(55354L)\n\t\t\t.user(\"user\")\n\t\t\t.password(\"password\")\n\t\t\t.path(\"path\")\n\t\t\t.format(ContainerLoggingHttpFormat.JSON)\n\t\t\t.headers(headersList)\n\t\t\t.compression(ContainerLoggingHttpCompression.NONE)\n\t\t\t.build();\n\n\t\tNewRelicLoggingConfiguration newRelicLoggingConfiguration = NewRelicLoggingConfiguration.builder()\n\t\t\t.host(\"host\")\n\t\t\t.ingestionKey(\"ingestion_key\")\n\t\t\t.build();\n\n\t\tContainerLoggingSplunkConfiguration containerLoggingSplunkConfiguration = ContainerLoggingSplunkConfiguration.builder()\n\t\t\t.host(\"host\")\n\t\t\t.token(\"token\")\n\t\t\t.build();\n\n\t\tTcpLoggingConfiguration tcpLoggingConfiguration = TcpLoggingConfiguration.builder()\n\t\t\t.host(\"host\")\n\t\t\t.port(44671L)\n\t\t\t.build();\n\n\t\tUpdateContainerLogging updateContainerLogging = UpdateContainerLogging.builder()\n\t\t\t.axiom(axiomLoggingConfiguration)\n\t\t\t.datadog(datadogLoggingConfiguration)\n\t\t\t.http(containerLoggingConfigurationHttp1)\n\t\t\t.newRelic(newRelicLoggingConfiguration)\n\t\t\t.splunk(containerLoggingSplunkConfiguration)\n\t\t\t.tcp(tcpLoggingConfiguration)\n\t\t\t.build();\n\n\t\tContainerRegistryAuthenticationAwsEcr containerRegistryAuthenticationAwsEcr = ContainerRegistryAuthenticationAwsEcr.builder()\n\t\t\t.accessKeyId(\"access_key_id\")\n\t\t\t.secretAccessKey(\"secret_access_key\")\n\t\t\t.build();\n\n\t\tContainerRegistryAuthenticationBasic containerRegistryAuthenticationBasic = ContainerRegistryAuthenticationBasic.builder()\n\t\t\t.username(\"username\")\n\t\t\t.password(\"password\")\n\t\t\t.build();\n\n\t\tContainerRegistryAuthenticationDockerHub containerRegistryAuthenticationDockerHub = ContainerRegistryAuthenticationDockerHub.builder()\n\t\t\t.username(\"username\")\n\t\t\t.personalAccessToken(\"personal_access_token\")\n\t\t\t.build();\n\n\t\tContainerRegistryAuthenticationGcpGar containerRegistryAuthenticationGcpGar = ContainerRegistryAuthenticationGcpGar.builder()\n\t\t\t.serviceKey(\"service_key\")\n\t\t\t.build();\n\n\t\tContainerRegistryAuthenticationGcpGcr containerRegistryAuthenticationGcpGcr = ContainerRegistryAuthenticationGcpGcr.builder()\n\t\t\t.serviceKey(\"service_key\")\n\t\t\t.build();\n\n\t\tContainerRegistryAuthentication containerRegistryAuthentication = ContainerRegistryAuthentication.builder()\n\t\t\t.awsEcr(containerRegistryAuthenticationAwsEcr)\n\t\t\t.basic(containerRegistryAuthenticationBasic)\n\t\t\t.dockerHub(containerRegistryAuthenticationDockerHub)\n\t\t\t.gcpGar(containerRegistryAuthenticationGcpGar)\n\t\t\t.gcpGcr(containerRegistryAuthenticationGcpGcr)\n\t\t\t.build();\n\n\t\tList<String> gpuClassesList = Arrays.asList(\"gpu_classes\");\n\n\t\tContainerResourceUpdateSchema containerResourceUpdateSchema = ContainerResourceUpdateSchema.builder()\n\t\t\t.cpu(1013L)\n\t\t\t.memory(352043675L)\n\t\t\t.gpuClasses(gpuClassesList)\n\t\t\t.storageAmount(1032076497908566.1L)\n\t\t\t.shmSize(64L)\n\t\t\t.build();\n\n\t\tUpdateContainer updateContainer = UpdateContainer.builder()\n\t\t\t.command(commandList)\n\t\t\t.environmentVariables(new HashMap())\n\t\t\t.image(\"image\")\n\t\t\t.imageCaching(true)\n\t\t\t.logging(updateContainerLogging)\n\t\t\t.priority(ContainerGroupPriority.HIGH)\n\t\t\t.registryAuthentication(containerRegistryAuthentication)\n\t\t\t.resources(containerResourceUpdateSchema)\n\t\t\t.build();\n\n\t\tList<CountryCode> countryCodesList = Arrays.asList(CountryCode.AF);\n\n\t\tUpdateContainerGroupNetworking updateContainerGroupNetworking = UpdateContainerGroupNetworking.builder()\n\t\t\t.port(13142L)\n\t\t\t.build();\n\n\t\tList<String> commandList1 = Arrays.asList(\"command\");\n\n\t\tContainerGroupProbeExec containerGroupProbeExec = ContainerGroupProbeExec.builder()\n\t\t\t.command(commandList1)\n\t\t\t.build();\n\n\t\tContainerGroupGRpcProbe containerGroupGRpcProbe = ContainerGroupGRpcProbe.builder()\n\t\t\t.port(37648L)\n\t\t\t.service(\"service\")\n\t\t\t.build();\n\n\t\tContainerGroupProbeHttpHeader containerGroupProbeHttpHeader = ContainerGroupProbeHttpHeader.builder()\n\t\t\t.name(\"name\")\n\t\t\t.value(\"value\")\n\t\t\t.build();\n\n\t\tList<ContainerGroupProbeHttpHeader> headersList1 = Arrays.asList(containerGroupProbeHttpHeader);\n\n\t\tContainerGroupHttpProbeConfiguration containerGroupHttpProbeConfiguration = ContainerGroupHttpProbeConfiguration.builder()\n\t\t\t.headers(headersList1)\n\t\t\t.path(\"path\")\n\t\t\t.port(29069L)\n\t\t\t.scheme(HttpScheme.HTTP)\n\t\t\t.build();\n\n\t\tContainerGroupTcpProbe containerGroupTcpProbe = ContainerGroupTcpProbe.builder()\n\t\t\t.port(13817L)\n\t\t\t.build();\n\n\t\tContainerGroupLivenessProbe containerGroupLivenessProbe = ContainerGroupLivenessProbe.builder()\n\t\t\t.exec(containerGroupProbeExec)\n\t\t\t.failureThreshold(3L)\n\t\t\t.grpc(containerGroupGRpcProbe)\n\t\t\t.http(containerGroupHttpProbeConfiguration)\n\t\t\t.initialDelaySeconds(670L)\n\t\t\t.periodSeconds(10L)\n\t\t\t.successThreshold(1L)\n\t\t\t.tcp(containerGroupTcpProbe)\n\t\t\t.timeoutSeconds(30L)\n\t\t\t.build();\n\n\t\tContainerGroupReadinessProbe containerGroupReadinessProbe = ContainerGroupReadinessProbe.builder()\n\t\t\t.exec(containerGroupProbeExec)\n\t\t\t.failureThreshold(3L)\n\t\t\t.grpc(containerGroupGRpcProbe)\n\t\t\t.http(containerGroupHttpProbeConfiguration)\n\t\t\t.initialDelaySeconds(262L)\n\t\t\t.periodSeconds(1L)\n\t\t\t.successThreshold(1L)\n\t\t\t.tcp(containerGroupTcpProbe)\n\t\t\t.timeoutSeconds(1L)\n\t\t\t.build();\n\n\t\tContainerGroupStartupProbe containerGroupStartupProbe = ContainerGroupStartupProbe.builder()\n\t\t\t.exec(containerGroupProbeExec)\n\t\t\t.failureThreshold(15L)\n\t\t\t.grpc(containerGroupGRpcProbe)\n\t\t\t.http(containerGroupHttpProbeConfiguration)\n\t\t\t.initialDelaySeconds(1106L)\n\t\t\t.tcp(containerGroupTcpProbe)\n\t\t\t.periodSeconds(3L)\n\t\t\t.successThreshold(2L)\n\t\t\t.timeoutSeconds(10L)\n\t\t\t.build();\n\n\t\tQueueBasedAutoscalerConfiguration queueBasedAutoscalerConfiguration = QueueBasedAutoscalerConfiguration.builder()\n\t\t\t.desiredQueueLength(53L)\n\t\t\t.maxReplicas(291L)\n\t\t\t.maxDownscalePerMinute(65L)\n\t\t\t.maxUpscalePerMinute(100L)\n\t\t\t.minReplicas(54L)\n\t\t\t.pollingPeriod(140L)\n\t\t\t.build();\n\n\t\tContainerGroupPatch containerGroupPatch = ContainerGroupPatch.builder()\n\t\t\t.displayName(\"ZJjdnvu\")\n\t\t\t.container(updateContainer)\n\t\t\t.replicas(56L)\n\t\t\t.countryCodes(countryCodesList)\n\t\t\t.networking(updateContainerGroupNetworking)\n\t\t\t.livenessProbe(containerGroupLivenessProbe)\n\t\t\t.readinessProbe(containerGroupReadinessProbe)\n\t\t\t.startupProbe(containerGroupStartupProbe)\n\t\t\t.queueAutoscaler(queueBasedAutoscalerConfiguration)\n\t\t\t.build();\n\n\t\tContainerGroup response = saladCloudSdk.containerGroups.updateContainerGroup(\"acme-corp\", \"dev-env\", \"mandlebrot\", containerGroupPatch);\n\n\t\tSystem.out.println(response);\n    }\n}"
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
  requestBodies:
    UpdateContainerGroup:
      required: true
      content:
        application/merge-patch+json:
          schema:
            $ref: '#/components/schemas/ContainerGroupPatch'
  responses:
    '400':
      description: Bad Request
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ProblemDetails'
    '403':
      description: Forbidden
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ProblemDetails'
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
    UpdateContainerGroup:
      description: OK
      content:
        application/merge-patch+json:
          schema:
            $ref: '#/components/schemas/ContainerGroup'
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
    ContainerGroupPatch:
      description: Represents a request to update a container group
      type: object
      properties:
        display_name:
          description: >-
            The display name for the container group. If null is provided, the
            display name will be set to the container group name.
          type:
            - string
            - 'null'
          maxLength: 63
          minLength: 2
          pattern: ^[ ,-.0-9A-Za-z]+$
        container:
          $ref: '#/components/schemas/UpdateContainer'
        replicas:
          description: The desired number of instances for your container group deployment.
          type:
            - integer
            - 'null'
          maximum: 500
          minimum: 0
        country_codes:
          description: >-
            List of countries nodes must be located in. Remove this field to
            permit nodes from any country.
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/CountryCode'
          maxItems: 500
          minItems: 1
        networking:
          $ref: '#/components/schemas/UpdateContainerGroupNetworking'
        liveness_probe:
          $ref: '#/components/schemas/ContainerGroupLivenessProbe'
        readiness_probe:
          $ref: '#/components/schemas/ContainerGroupReadinessProbe'
        startup_probe:
          $ref: '#/components/schemas/ContainerGroupStartupProbe'
        queue_autoscaler:
          $ref: '#/components/schemas/ContainerGroupQueueAutoscaler'
    ContainerGroup:
      description: >-
        A container group definition that represents a scalable set of identical
        containers running as a distributed service
      type: object
      properties:
        autostart_policy:
          description: >-
            Defines whether containers in this group should automatically start
            when deployed (true) or require manual starting (false)
          type: boolean
        container:
          $ref: '#/components/schemas/Container'
        country_codes:
          description: >-
            List of country codes where container instances are permitted to
            run. When not specified or empty, containers may run in any
            available region.
          type: array
          items:
            $ref: '#/components/schemas/CountryCode'
          maxItems: 500
          minItems: 0
        create_time:
          description: ISO 8601 timestamp when this container group was initially created
          type: string
          format: date-time
        current_state:
          $ref: '#/components/schemas/ContainerGroupState'
        display_name:
          $ref: '#/components/schemas/DisplayName'
        id:
          $ref: '#/components/schemas/ContainerGroupId'
        liveness_probe:
          $ref: '#/components/schemas/ContainerGroupLivenessProbe'
        name:
          $ref: '#/components/schemas/ContainerGroupName'
        networking:
          $ref: '#/components/schemas/ContainerGroupNetworking'
        organization_name:
          $ref: '#/components/schemas/OrganizationName'
        pending_change:
          description: >-
            Indicates whether a configuration change has been requested but not
            yet applied to all containers in the group
          type: boolean
        priority:
          $ref: '#/components/schemas/ContainerGroupPriority'
        project_name:
          $ref: '#/components/schemas/ProjectName'
        queue_autoscaler:
          $ref: '#/components/schemas/ContainerGroupQueueAutoscaler'
        queue_connection:
          $ref: '#/components/schemas/ContainerGroupQueueConnection'
        readiness_probe:
          $ref: '#/components/schemas/ContainerGroupReadinessProbe'
        readme:
          type: string
          maxLength: 65000
          minLength: 2
        replicas:
          $ref: '#/components/schemas/ContainerGroupReplicas'
        restart_policy:
          $ref: '#/components/schemas/ContainerRestartPolicy'
        startup_probe:
          $ref: '#/components/schemas/ContainerGroupStartupProbe'
        update_time:
          description: ISO 8601 timestamp when this container group was last updated
          type: string
          format: date-time
        version:
          description: >-
            Incremental version number that increases with each configuration
            change to the container group
          type: integer
          format: int32
          maximum: 2147483647
          minimum: 1
      required:
        - autostart_policy
        - container
        - country_codes
        - create_time
        - current_state
        - display_name
        - id
        - name
        - organization_name
        - pending_change
        - priority
        - project_name
        - replicas
        - restart_policy
        - update_time
        - version
      title: Container Group
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
    UpdateContainer:
      description: Represents an update container object
      type:
        - object
        - 'null'
      properties:
        command:
          description: >-
            Pass a command (and optional arguments) to override the ENTRYPOINT
            and CMD of a container image.
          type:
            - array
            - 'null'
          items:
            type: string
            pattern: ^.*$
            minLength: 1
            maxLength: 1024
          maxItems: 100
          minItems: 0
        environment_variables:
          description: Environment variables to set in the container.
          type: object
          additionalProperties:
            type: string
            minLength: 1
            maxLength: 1000
            pattern: ^.*$
        image:
          description: The container image to use.
          type:
            - string
            - 'null'
          maxLength: 1024
          minLength: 1
          pattern: ^.*$
        image_caching:
          $ref: '#/components/schemas/ContainerImageCaching'
        logging:
          $ref: '#/components/schemas/UpdateContainerLogging'
        priority:
          $ref: '#/components/schemas/ContainerGroupPriority'
        registry_authentication:
          $ref: '#/components/schemas/ContainerRegistryAuthentication'
        resources:
          $ref: '#/components/schemas/UpdateContainerResources'
    CountryCode:
      description: ISO 3166-1 alpha-2 country codes
      type: string
      enum:
        - af
        - al
        - dz
        - as
        - ad
        - ao
        - ai
        - aq
        - ag
        - ar
        - am
        - aw
        - au
        - at
        - az
        - bs
        - bh
        - bd
        - bb
        - by
        - be
        - bz
        - bj
        - bm
        - bt
        - bo
        - bq
        - ba
        - bw
        - bv
        - br
        - io
        - bn
        - bg
        - bf
        - bi
        - cv
        - kh
        - cm
        - ca
        - ky
        - cf
        - td
        - cl
        - cn
        - cx
        - cc
        - co
        - km
        - cd
        - cg
        - ck
        - cr
        - hr
        - cu
        - cw
        - cy
        - cz
        - ci
        - dk
        - dj
        - dm
        - do
        - ec
        - eg
        - sv
        - gq
        - er
        - ee
        - sz
        - et
        - fk
        - fo
        - fj
        - fi
        - fr
        - gf
        - pf
        - tf
        - ga
        - gm
        - ge
        - de
        - gh
        - gi
        - gr
        - gl
        - gd
        - gp
        - gu
        - gt
        - gg
        - gn
        - gw
        - gy
        - ht
        - hm
        - va
        - hn
        - hk
        - hu
        - is
        - in
        - id
        - ir
        - iq
        - ie
        - im
        - il
        - it
        - jm
        - jp
        - je
        - jo
        - kz
        - ke
        - ki
        - kp
        - kr
        - kw
        - kg
        - la
        - lv
        - lb
        - ls
        - lr
        - ly
        - li
        - lt
        - lu
        - mo
        - mg
        - mw
        - my
        - mv
        - ml
        - mt
        - mh
        - mq
        - mr
        - mu
        - yt
        - mx
        - fm
        - md
        - mc
        - mn
        - me
        - ms
        - ma
        - mz
        - mm
        - na
        - nr
        - np
        - nl
        - nc
        - nz
        - ni
        - ne
        - ng
        - nu
        - nf
        - mp
        - 'no'
        - om
        - pk
        - pw
        - ps
        - pa
        - pg
        - py
        - pe
        - ph
        - pn
        - pl
        - pt
        - pr
        - qa
        - mk
        - ro
        - ru
        - rw
        - re
        - bl
        - sh
        - kn
        - lc
        - mf
        - pm
        - vc
        - ws
        - sm
        - st
        - sa
        - sn
        - rs
        - sc
        - sl
        - sg
        - sx
        - sk
        - si
        - sb
        - so
        - za
        - gs
        - ss
        - es
        - lk
        - sd
        - sr
        - sj
        - se
        - ch
        - sy
        - tw
        - tj
        - tz
        - th
        - tl
        - tg
        - tk
        - to
        - tt
        - tn
        - tr
        - tm
        - tc
        - tv
        - ug
        - ua
        - ae
        - gb
        - um
        - us
        - uy
        - uz
        - vu
        - ve
        - vn
        - vg
        - vi
        - wf
        - eh
        - ye
        - zm
        - zw
        - ax
      title: Country Code
    UpdateContainerGroupNetworking:
      description: Represents update container group networking parameters
      type: object
      properties:
        port:
          description: The port number to expose on the container group
          type:
            - integer
            - 'null'
          maximum: 65535
          minimum: 1
    ContainerGroupLivenessProbe:
      description: >-
        Defines a liveness probe for container groups that determines when to
        restart a container if it becomes unhealthy
      type:
        - object
        - 'null'
      properties:
        exec:
          $ref: '#/components/schemas/ContainerGroupProbeExec'
        failure_threshold:
          description: >-
            Number of consecutive failures required to consider the probe as
            failed
          type: integer
          format: int32
          default: 3
          maximum: 20
          minimum: 1
        grpc:
          $ref: '#/components/schemas/ContainerGroupProbeGrpc'
        http:
          $ref: '#/components/schemas/ContainerGroupProbeHttp'
        initial_delay_seconds:
          description: >-
            Number of seconds to wait after container start before initiating
            liveness probes
          type: integer
          format: int32
          default: 0
          maximum: 1200
          minimum: 0
        period_seconds:
          description: Frequency in seconds at which the probe should be executed
          type: integer
          format: int32
          default: 10
          maximum: 120
          minimum: 1
        success_threshold:
          description: >-
            Number of consecutive successes required to consider the probe
            successful
          type: integer
          format: int32
          default: 1
          maximum: 10
          minimum: 1
        tcp:
          $ref: '#/components/schemas/ContainerGroupProbeTcp'
        timeout_seconds:
          description: >-
            Number of seconds after which the probe times out if no response is
            received
          type: integer
          format: int32
          default: 30
          maximum: 60
          minimum: 1
      required:
        - failure_threshold
        - initial_delay_seconds
        - period_seconds
        - success_threshold
        - timeout_seconds
    ContainerGroupReadinessProbe:
      description: >-
        Defines how to check if a container is ready to serve traffic. The
        readiness probe determines whether the container's application is ready
        to accept traffic. If the readiness probe fails, the container is
        considered not ready and traffic will not be sent to it.
      type:
        - object
        - 'null'
      properties:
        exec:
          $ref: '#/components/schemas/ContainerGroupProbeExec'
        failure_threshold:
          description: >-
            The number of consecutive failures required to consider the probe
            failed. After this many consecutive failures, the container is
            marked as not ready.
          type: integer
          format: int32
          default: 3
          maximum: 20
          minimum: 1
        grpc:
          $ref: '#/components/schemas/ContainerGroupProbeGrpc'
        http:
          $ref: '#/components/schemas/ContainerGroupProbeHttp'
        initial_delay_seconds:
          description: >-
            The time in seconds to wait after the container starts before
            initiating the first probe. This allows time for the application to
            initialize before being tested.
          type: integer
          format: int32
          default: 0
          maximum: 1200
          minimum: 0
        period_seconds:
          description: >-
            How frequently (in seconds) the probe should be executed during the
            container's lifetime. Specifies the interval between consecutive
            probe executions.
          type: integer
          format: int32
          default: 1
          maximum: 120
          minimum: 1
        success_threshold:
          description: >-
            The minimum consecutive successes required to consider the probe
            successful after it has failed. Defines how many successful probe
            results are needed to transition from failure to success.
          type: integer
          format: int32
          default: 1
          maximum: 10
          minimum: 1
        tcp:
          $ref: '#/components/schemas/ContainerGroupProbeTcp'
        timeout_seconds:
          description: >-
            The maximum time in seconds that the probe has to complete. If the
            probe doesn't return a result before the timeout, it's considered
            failed.
          type: integer
          format: int32
          default: 1
          maximum: 60
          minimum: 1
      required:
        - failure_threshold
        - initial_delay_seconds
        - period_seconds
        - success_threshold
        - timeout_seconds
    ContainerGroupStartupProbe:
      description: >-
        Defines a probe that checks if a container application has started
        successfully. Startup probes help prevent applications from being
        prematurely marked as unhealthy during initialization. The probe can use
        HTTP requests, TCP connections, gRPC calls, or shell commands to
        determine startup status.
      type:
        - object
        - 'null'
      properties:
        exec:
          $ref: '#/components/schemas/ContainerGroupProbeExec'
        failure_threshold:
          description: >-
            Number of times the probe must fail before considering the container
            not started
          type: integer
          format: int32
          default: 15
          maximum: 20
          minimum: 1
        grpc:
          $ref: '#/components/schemas/ContainerGroupProbeGrpc'
        http:
          $ref: '#/components/schemas/ContainerGroupProbeHttp'
        initial_delay_seconds:
          description: >-
            Number of seconds to wait after container startup before the first
            probe is executed
          type: integer
          format: int32
          default: 0
          maximum: 1200
          minimum: 0
        tcp:
          $ref: '#/components/schemas/ContainerGroupProbeTcp'
        period_seconds:
          description: How frequently (in seconds) to perform the probe
          type: integer
          format: int32
          default: 3
          maximum: 120
          minimum: 1
        success_threshold:
          description: >-
            Minimum consecutive successes required for the probe to be
            considered successful
          type: integer
          format: int32
          default: 2
          maximum: 10
          minimum: 1
        timeout_seconds:
          description: >-
            Maximum time (in seconds) to wait for a probe response before
            considering it failed
          type: integer
          format: int32
          default: 10
          maximum: 60
          minimum: 1
      required:
        - failure_threshold
        - initial_delay_seconds
        - period_seconds
        - success_threshold
        - timeout_seconds
      title: Container Group Startup Probe
    ContainerGroupQueueAutoscaler:
      description: >-
        Defines configuration for automatically scaling container instances
        based on queue length. The autoscaler monitors a queue and adjusts the
        number of running replicas to maintain the desired queue length.
      type: object
      properties:
        desired_queue_length:
          description: >-
            The target number of items in the queue that the autoscaler attempts
            to maintain by scaling the containers up or down
          type: integer
          format: int32
          maximum: 100
          minimum: 1
        max_replicas:
          description: The maximum number of instances the container can scale up to
          type: integer
          format: int32
          maximum: 500
          minimum: 1
        max_downscale_per_minute:
          description: >-
            The maximum number of instances that can be removed per minute to
            prevent rapid downscaling
          type: integer
          format: int32
          maximum: 100
          minimum: 1
        max_upscale_per_minute:
          description: >-
            The maximum number of instances that can be added per minute to
            prevent rapid upscaling
          type: integer
          format: int32
          maximum: 100
          minimum: 1
        min_replicas:
          description: >-
            The minimum number of instances the container can scale down to,
            ensuring baseline availability
          type: integer
          format: int32
          maximum: 100
          minimum: 0
        polling_period:
          description: >-
            The period (in seconds) in which the autoscaler checks the queue
            length and applies the scaling formula
          type: integer
          format: int32
          maximum: 1800
          minimum: 15
      required:
        - desired_queue_length
        - max_replicas
        - min_replicas
      title: Queue-based Autoscaler Configuration
    Container:
      description: Represents a container with its configuration and resource requirements.
      type: object
      properties:
        command:
          description: >-
            List of commands to run inside the container. Each command is a
            string representing a command-line instruction.
          type:
            - 'null'
            - array
          items:
            type: string
            pattern: ^.*$
            minLength: 1
            maxLength: 2048
          maxItems: 100
          minItems: 0
        environment_variables:
          description: Environment variables to set in the container.
          type: object
          additionalProperties:
            type: string
            description: Key-value pairs of environment variables to set in the container.
            pattern: ^.*$
            minLength: 0
            maxLength: 2048
        hash:
          description: SHA-256 hash (64-character hexadecimal string)
          type: string
          maxLength: 135
          minLength: 47
          pattern: ^sha\d{1,3}:[a-fA-F0-9]{40,135}$
        image:
          $ref: '#/components/schemas/ContainerImage'
        image_caching:
          $ref: '#/components/schemas/ContainerImageCaching'
        logging:
          $ref: '#/components/schemas/ContainerLogging'
        resources:
          $ref: '#/components/schemas/ContainerResourceRequirements'
        size:
          description: Size of the container in bytes.
          type: integer
          format: int64
          maximum: 9223372036854776000
          minimum: 0
      required:
        - command
        - image
        - resources
    ContainerGroupState:
      description: >-
        Represents the operational state of a container group during its
        lifecycle, including timing information, status, and instance
        distribution metrics. This state captures the current execution status,
        start and finish times, and provides visibility into the operational
        health across instances.
      type: object
      properties:
        description:
          description: >-
            Optional textual description or notes about the current state of the
            container group
          type:
            - string
            - 'null'
          maxLength: 1000
          minLength: 0
          pattern: ^.*$
        finish_time:
          description: >-
            Timestamp when the container group execution finished or is expected
            to finish
          type: string
          format: date-time
        instance_status_counts:
          $ref: '#/components/schemas/ContainerGroupInstanceStatusCount'
        start_time:
          description: Timestamp when the container group execution started
          type: string
          format: date-time
        status:
          $ref: '#/components/schemas/ContainerGroupStatus'
      required:
        - finish_time
        - instance_status_counts
        - start_time
        - status
      title: Container Group State
    DisplayName:
      description: The display-friendly name of the resource.
      type: string
      examples:
        - Name
      maxLength: 63
      minLength: 2
      pattern: ^[ ,-.0-9A-Za-z]+$
    ContainerGroupId:
      description: The container group identifier.
      type: string
      format: uuid
      examples:
        - ab3a4591-efc3-46c0-b06a-3d820c0ec100
      title: Container Group ID
    ContainerGroupNetworking:
      description: >-
        Network configuration for container groups that defines connectivity,
        routing, and access control settings
      type: object
      properties:
        auth:
          description: >-
            Whether authentication is required for network access to the
            container group
          type: boolean
        client_request_timeout:
          $ref: '#/components/schemas/ContainerGroupNetworkingClientRequestTimeout'
        dns:
          description: >-
            Domain name or URL endpoint for the container group's network
            interface
          type: string
          format: url
          maxLength: 253
          minLength: 1
          pattern: ^([a-z][a-z0-9-]{0,61}[a-z0-9]\.)*[a-z][a-z0-9-]{0,61}[a-z0-9]$
        load_balancer:
          $ref: '#/components/schemas/ContainerGroupNetworkingLoadBalancer'
        port:
          $ref: '#/components/schemas/ContainerGroupNetworkingPort'
        protocol:
          $ref: '#/components/schemas/ContainerNetworkingProtocol'
        server_response_timeout:
          $ref: '#/components/schemas/ContainerGroupNetworkingServerResponseTimeout'
        single_connection_limit:
          $ref: '#/components/schemas/ContainerGroupNetworkingSingleConnectionLimit'
      required:
        - auth
        - dns
        - load_balancer
        - port
        - protocol
      title: Container Group Networking Configuration
    ContainerGroupPriority:
      description: >-
        Specifies the priority level for container group execution, which
        determines resource allocation and scheduling precedence.
      type:
        - string
        - 'null'
      enum:
        - high
        - medium
        - low
        - batch
      title: Container Group Priority
    ContainerGroupQueueConnection:
      description: >-
        Configuration for connecting a container group to a message queue
        system, enabling asynchronous communication between services.
      type: object
      properties:
        path:
          description: >-
            The endpoint path for accessing the queue service, relative to the
            base URL of the queue server.
          type: string
          maxLength: 1024
          minLength: 1
          pattern: ^.*$
        port:
          description: >-
            The network port number used to connect to the queue service. Must
            be a valid TCP/IP port between 1 and 65535.
          type: integer
          format: int32
          maximum: 65535
          minimum: 1
        queue_name:
          description: >-
            Unique identifier for the queue. Must start with a lowercase letter,
            can contain lowercase letters, numbers, and hyphens, and must end
            with a letter or number.
          type: string
          maxLength: 63
          minLength: 2
          pattern: ^[a-z][a-z0-9-]{0,61}[a-z0-9]$
      required:
        - path
        - port
        - queue_name
    ContainerGroupReplicas:
      description: The container group replicas.
      type: integer
      format: int32
      examples:
        - 50
      maximum: 500
      minimum: 0
      title: Container Group Replicas
    ContainerRestartPolicy:
      description: Specifies the policy for restarting containers when they exit or fail.
      type: string
      enum:
        - always
        - on_failure
        - never
      title: Container Restart Policy
    ContainerImageCaching:
      description: The container image caching.
      type: boolean
      examples:
        - true
      title: Container Image Caching
    UpdateContainerLogging:
      description: >-
        Configuration options for directing container logs to a logging
        provider. This schema enables you to specify a single logging
        destination for container output, supporting monitoring, debugging, and
        analytics use cases. Each provider has its own configuration parameters
        defined in the referenced schemas. Only one logging provider can be
        selected at a time.
      type:
        - object
        - 'null'
      properties:
        axiom:
          $ref: '#/components/schemas/ContainerLoggingAxiom'
        datadog:
          $ref: '#/components/schemas/ContainerLoggingDatadog'
        http:
          $ref: '#/components/schemas/ContainerLoggingHttp'
        new_relic:
          $ref: '#/components/schemas/ContainerLoggingNewRelic'
        splunk:
          $ref: '#/components/schemas/ContainerLoggingSplunk'
        tcp:
          $ref: '#/components/schemas/ContainerLoggingTcp'
      title: Container Logging Configuration
    ContainerRegistryAuthentication:
      description: >-
        Authentication configuration for various container registry types,
        including AWS ECR, Docker Hub, GCP GAR, GCP GCR, and basic
        authentication.
      type: object
      properties:
        aws_ecr:
          $ref: '#/components/schemas/ContainerRegistryAuthenticationAwsEcr'
        basic:
          $ref: '#/components/schemas/ContainerRegistryAuthenticationBasic'
        docker_hub:
          $ref: '#/components/schemas/ContainerRegistryAuthenticationDockerHub'
        gcp_gar:
          $ref: '#/components/schemas/ContainerRegistryAuthenticationGcpGar'
        gcp_gcr:
          $ref: '#/components/schemas/ContainerRegistryAuthenticationGcpGcr'
      title: Container Registry Authentication
    UpdateContainerResources:
      description: >-
        Defines the resource specifications that can be modified for a container
        group, including CPU, memory, GPU classes, and storage allocations.
      type:
        - object
        - 'null'
      properties:
        cpu:
          description: >-
            The number of CPU cores to allocate to the container (between 1 and
            1024).
          type:
            - integer
            - 'null'
          maximum: 1024
          minimum: 1
        memory:
          description: >-
            The amount of memory to allocate to the container in megabytes
            (between 1024 and 1073741824).
          type:
            - integer
            - 'null'
          maximum: 1073741824
          minimum: 1024
        gpu_classes:
          description: >-
            List of GPU class identifiers that the container can use, specified
            as UUIDs.
          type:
            - array
            - 'null'
          items:
            type: string
            format: uuid
          maxItems: 100
          minItems: 0
        storage_amount:
          description: >-
            The amount of storage to allocate to the container in bytes (between
            1 GB and 1 PB).
          type:
            - integer
            - 'null'
          format: int64
          maximum: 1125899906842624
          minimum: 1073741824
        shm_size:
          description: >-
            The amount of shared memory to allocate to the container via
            `/dev/shm` in megabytes (between 64 and 1073741824). If not
            specified, defaults to 64 MB.
          type:
            - integer
            - 'null'
          format: int32
          default: 64
          maximum: 1073741824
          minimum: 64
      title: Container Resource Update Schema
    ContainerGroupProbeExec:
      description: >-
        Defines the exec action for a probe in a container group. This is used
        to execute a command inside a container for health checks.
      type: object
      properties:
        command:
          description: >-
            The command to execute inside the container. Exit status of 0 is
            considered successful, any other exit status is considered failure.
          type: array
          items:
            type: string
            description: Individual component of the command to be run.
            pattern: ^.*$
            minLength: 1
            maxLength: 2048
          maxItems: 100
          minItems: 1
      required:
        - command
      title: Container Group Probe Exec
    ContainerGroupProbeGrpc:
      description: >-
        Configuration for gRPC-based health probes in container groups, used to
        determine container health status.
      type: object
      properties:
        port:
          description: The port number on which the gRPC health check service is exposed.
          type: integer
          format: int32
          maximum: 65536
          minimum: 0
        service:
          description: >-
            The name of the gRPC service that implements the health check
            protocol.
          type: string
          maxLength: 1024
          minLength: 0
          pattern: ^.*$
      required:
        - port
        - service
      title: Container Group gRPC Probe
    ContainerGroupProbeHttp:
      description: >-
        Defines HTTP probe configuration for container health checks within a
        container group.
      type: object
      properties:
        headers:
          $ref: '#/components/schemas/ContainerGroupProbeHttpHeaders'
        path:
          description: The HTTP path that will be probed to check container health.
          type: string
          maxLength: 2048
          minLength: 1
          pattern: ^.*$
        port:
          description: The TCP port number to which the HTTP request will be sent.
          type: integer
          format: int32
          maximum: 65536
          minimum: 0
        scheme:
          $ref: '#/components/schemas/ContainerProbeHttpScheme'
      required:
        - headers
        - path
        - port
        - scheme
      title: Container Group HTTP Probe Configuration
    ContainerGroupProbeTcp:
      description: >-
        Configuration for a TCP probe used to check container health via network
        connectivity.
      type: object
      properties:
        port:
          description: >-
            The TCP port number that the probe should connect to. Must be a
            valid port number between 0 and 65535.
          type: integer
          format: int32
          maximum: 65535
          minimum: 0
      required:
        - port
      title: Container Group TCP Probe
    ContainerImage:
      description: The container image.
      type: string
      examples:
        - acme/:latest
      maxLength: 2048
      minLength: 1
      pattern: ^.*$
      title: Container Image
    ContainerLogging:
      description: >-
        Configuration options for directing container logs to a logging
        provider. This schema enables you to specify a single logging
        destination for container output, supporting monitoring, debugging, and
        analytics use cases. Each provider has its own configuration parameters
        defined in the referenced schemas. Only one logging provider can be
        selected at a time.
      type: object
      properties:
        axiom:
          $ref: '#/components/schemas/ContainerLoggingAxiom'
        datadog:
          $ref: '#/components/schemas/ContainerLoggingDatadog'
        http:
          $ref: '#/components/schemas/ContainerLoggingHttp'
        new_relic:
          $ref: '#/components/schemas/ContainerLoggingNewRelic'
        splunk:
          $ref: '#/components/schemas/ContainerLoggingSplunk'
        tcp:
          $ref: '#/components/schemas/ContainerLoggingTcp'
      title: Container Logging Configuration
    ContainerResourceRequirements:
      description: Specifies the resource requirements for a container.
      type: object
      properties:
        cpu:
          description: >-
            The number of CPU cores required by the container. Must be between 1
            and 16.
          type: integer
          format: int32
          maximum: 1024
          minimum: 1
        memory:
          description: >-
            The amount of memory (in MB) required by the container. Must be
            between 1024 MB and 61440 MB.
          type: integer
          format: int32
          maximum: 1073741824
          minimum: 1024
        gpu_classes:
          description: >-
            A list of GPU class UUIDs required by the container. Can be null if
            no GPU is required.
          type: array
          items:
            type: string
            format: uuid
          maxItems: 100
          minItems: 0
        storage_amount:
          description: >-
            The amount of storage (in bytes) required by the container. Must be
            between 1 GB (1073741824 bytes) and 250 GB (268435456000 bytes).
          type: integer
          format: int64
          maximum: 1125899906842624
          minimum: 1073741824
        shm_size:
          description: >-
            The size of the shared memory (/dev/shm) in MB. If not specified,
            defaults to 1024MB.
          type: integer
          format: int32
          default: 64
          maximum: 1073741824
          minimum: 64
      required:
        - cpu
        - memory
        - gpu_classes
    ContainerGroupInstanceStatusCount:
      description: >-
        A summary of container group instances categorized by their current
        lifecycle status
      type: object
      properties:
        allocating_count:
          description: >-
            The number of container instances that are currently being allocated
            resources
          type: integer
          format: int32
          maximum: 2147483647
          minimum: 0
        creating_count:
          description: >-
            The number of container instances that are in the process of being
            created
          type: integer
          format: int32
          maximum: 2147483647
          minimum: 0
        running_count:
          description: >-
            The number of container instances that are currently running and
            operational
          type: integer
          format: int32
          maximum: 2147483647
          minimum: 0
        stopping_count:
          description: >-
            The number of container instances that are in the process of
            stopping
          type: integer
          format: int32
          maximum: 2147483647
          minimum: 0
      required:
        - allocating_count
        - creating_count
        - running_count
        - stopping_count
    ContainerGroupStatus:
      description: >-
        Represents the current operational state of a container group within the
        Salad platform.
      type: string
      enum:
        - pending
        - running
        - stopped
        - succeeded
        - failed
        - deploying
      title: ContainerGroupStatus
    ContainerGroupNetworkingClientRequestTimeout:
      description: The container group networking client request timeout.
      type: integer
      format: int32
      default: 100000
      examples:
        - 100000
      maximum: 100000
      minimum: 1
      title: Container Group Networking Client Request Timeout
    ContainerGroupNetworkingLoadBalancer:
      description: The container group networking load balancer.
      type: string
      default: round_robin
      enum:
        - round_robin
        - least_number_of_connections
      title: The Container Group Networking Load Balancer
    ContainerGroupNetworkingPort:
      description: The container group networking port.
      type: integer
      format: int32
      examples:
        - 60000
      maximum: 65535
      minimum: 1
      title: Container Group Networking Port
    ContainerNetworkingProtocol:
      description: >-
        Defines the communication protocol used for network traffic between
        containers or external systems. Currently supports HTTP protocol for
        web-based communication.
      type: string
      enum:
        - http
      title: Container Networking Protocol
    ContainerGroupNetworkingServerResponseTimeout:
      description: The container group networking server response timeout.
      type: integer
      format: int32
      default: 100000
      examples:
        - 100000
      maximum: 100000
      minimum: 1
      title: Container Group Networking Server Response Timeout
    ContainerGroupNetworkingSingleConnectionLimit:
      description: The container group networking single connection limit flag.
      type: boolean
      default: false
      examples:
        - false
      title: Container Group Networking Single Connection Limit
    ContainerLoggingAxiom:
      description: >-
        Configuration settings for integrating container logs with the Axiom
        logging service. When specified, container logs will be forwarded to the
        Axiom instance defined by these parameters.
      type: object
      properties:
        host:
          description: The Axiom host URL where logs will be sent (e.g. logs.axiom.co)
          type: string
          maxLength: 1000
          minLength: 1
          pattern: ^.*$
        api_token:
          description: >-
            Authentication token for the Axiom API with appropriate write
            permissions
          type: string
          maxLength: 1000
          minLength: 1
          pattern: ^.*$
        dataset:
          description: >-
            Name of the Axiom dataset where the container logs will be stored
            and indexed
          type: string
          maxLength: 1000
          minLength: 1
          pattern: ^.*$
      required:
        - host
        - api_token
        - dataset
      title: Axiom Logging Configuration
    ContainerLoggingDatadog:
      description: >-
        Configuration for forwarding container logs to Datadog monitoring
        service.
      type: object
      properties:
        host:
          description: The Datadog intake server host URL where logs will be sent.
          type: string
          maxLength: 1000
          minLength: 1
          pattern: ^.*$
        api_key:
          description: The Datadog API key used for authentication when sending logs.
          type: string
          maxLength: 1000
          minLength: 1
          pattern: ^.*$
        tags:
          description: >-
            Optional metadata tags to attach to logs for filtering and
            categorization in Datadog.
          items:
            $ref: '#/components/schemas/ContainerLoggingDatadogTag'
          maxItems: 1000
          minItems: 0
          type:
            - array
            - 'null'
      required:
        - host
        - api_key
        - tags
      title: Datadog Logging Configuration
    ContainerLoggingHttp:
      description: >-
        Configuration for sending container logs to an HTTP endpoint. Defines
        how logs are formatted, compressed, and transmitted.
      type: object
      properties:
        host:
          description: The hostname or IP address of the HTTP logging endpoint
          type: string
          maxLength: 1000
          minLength: 1
          pattern: ^.*$
        port:
          description: The port number of the HTTP logging endpoint (1-65535)
          type: integer
          format: int32
          maximum: 65535
          minimum: 1
        user:
          description: Optional username for HTTP authentication
          type:
            - string
            - 'null'
          maxLength: 1000
          minLength: 1
          pattern: ^.*$
        password:
          description: Optional password for HTTP authentication
          type:
            - string
            - 'null'
          maxLength: 1000
          minLength: 1
          pattern: ^.*$
        path:
          description: Optional URL path for the HTTP endpoint
          type:
            - string
            - 'null'
          maxLength: 1000
          minLength: 1
          pattern: ^.*$
        format:
          $ref: '#/components/schemas/ContainerLoggingHttpFormat'
        headers:
          description: Optional HTTP headers to include in log transmission requests
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/ContainerLoggingHttpHeader'
          maxItems: 1000
          minItems: 0
        compression:
          $ref: '#/components/schemas/ContainerLoggingHttpCompression'
      required:
        - headers
        - host
        - port
        - format
        - compression
      title: Container HTTP Logging Configuration
    ContainerLoggingNewRelic:
      description: >-
        Configuration for sending container logs to New Relic's log management
        platform.
      type: object
      properties:
        host:
          description: >-
            The New Relic endpoint host for log ingestion (e.g.,
            log-api.newrelic.com).
          type: string
          maxLength: 1000
          minLength: 1
          pattern: ^.*$
        ingestion_key:
          description: >-
            The New Relic license or ingestion key used for authentication and
            data routing.
          type: string
          maxLength: 1000
          minLength: 1
          pattern: ^.*$
      required:
        - host
        - ingestion_key
      title: New Relic Logging Configuration
    ContainerLoggingSplunk:
      description: >-
        Configuration settings for forwarding container logs to a Splunk
        instance.
      type: object
      properties:
        host:
          description: The URL of the Splunk HTTP Event Collector (HEC) endpoint.
          type: string
          maxLength: 1000
          minLength: 1
          pattern: ^.*$
        token:
          description: >-
            The authentication token required to send data to the Splunk HEC
            endpoint.
          type: string
          maxLength: 1000
          minLength: 1
          pattern: ^.*$
      required:
        - host
        - token
      title: Container Logging Splunk Configuration
    ContainerLoggingTcp:
      description: Configuration for forwarding container logs to a remote TCP endpoint
      type: object
      properties:
        host:
          description: The hostname or IP address of the remote TCP logging endpoint
          type: string
          maxLength: 1000
          minLength: 1
          pattern: ^.*$
        port:
          description: The port number on which the TCP logging endpoint is listening
          type: integer
          format: int32
          maximum: 65535
          minimum: 1
      required:
        - host
        - port
      title: TCP Logging Configuration
    ContainerRegistryAuthenticationAwsEcr:
      description: Authentication details for AWS Elastic Container Registry (ECR)
      type:
        - object
        - 'null'
      properties:
        access_key_id:
          description: AWS access key ID used for ECR authentication
          type: string
          maxLength: 10000
          minLength: 1
          pattern: ^.*$
        secret_access_key:
          description: AWS secret access key used for ECR authentication
          type: string
          maxLength: 10000
          minLength: 1
          pattern: ^.*$
      required:
        - access_key_id
        - secret_access_key
    ContainerRegistryAuthenticationBasic:
      description: >-
        Basic username and password authentication for generic container
        registries
      type: object
      properties:
        username:
          description: Username for registry authentication
          type: string
          maxLength: 10000
          minLength: 1
          pattern: ^.*$
        password:
          description: Password for registry authentication
          type: string
          maxLength: 10000
          minLength: 1
          pattern: ^.*$
      required:
        - username
        - password
    ContainerRegistryAuthenticationDockerHub:
      description: Authentication details for Docker Hub registry
      type: object
      properties:
        username:
          description: Docker Hub username
          type: string
          maxLength: 10000
          minLength: 1
          pattern: ^.*$
        personal_access_token:
          description: Docker Hub personal access token (PAT)
          type: string
          maxLength: 10000
          minLength: 1
          pattern: ^.*$
      required:
        - username
        - personal_access_token
    ContainerRegistryAuthenticationGcpGar:
      description: Authentication details for Google Artifact Registry (GAR)
      type: object
      properties:
        service_key:
          description: GCP service account key in JSON format for GAR authentication
          type: string
          maxLength: 10000
          minLength: 1
      required:
        - service_key
    ContainerRegistryAuthenticationGcpGcr:
      description: Authentication details for Google Container Registry (GCR)
      type: object
      properties:
        service_key:
          description: GCP service account key in JSON format for GCR authentication
          type: string
          maxLength: 10000
          minLength: 1
      required:
        - service_key
    ContainerGroupProbeHttpHeaders:
      description: >-
        A collection of HTTP header name-value pairs used for configuring
        requests and responses in container group endpoints. Each header
        consists of a name and its corresponding value.
      type: array
      items:
        $ref: '#/components/schemas/ContainerGroupProbeHttpHeader'
      maxItems: 50
      minItems: 1
      title: HTTP Headers
    ContainerProbeHttpScheme:
      description: >-
        The protocol scheme used for HTTP probe requests in container health
        checks.
      type:
        - string
        - 'null'
      enum:
        - http
        - https
      title: HTTP Scheme
    ContainerLoggingDatadogTag:
      description: Represents a Datadog tag used for container logging metadata.
      type: object
      properties:
        name:
          description: The name of the metadata tag.
          type: string
          maxLength: 1000
          minLength: 1
          pattern: ^.*$
        value:
          description: The value of the metadata tag.
          type: string
          maxLength: 1000
          minLength: 1
          pattern: ^.*$
      required:
        - name
        - value
      title: Datadog Tag for Container Logging
    ContainerLoggingHttpFormat:
      description: The format in which logs will be delivered
      type: string
      enum:
        - json
        - json_lines
    ContainerLoggingHttpHeader:
      description: Represents an HTTP header used for container logging configuration.
      type: object
      properties:
        name:
          description: The name of the HTTP header
          type: string
          maxLength: 1000
          minLength: 1
          pattern: ^.*$
        value:
          description: The value of the HTTP header
          type: string
          maxLength: 1000
          minLength: 1
          pattern: ^.*$
      required:
        - name
        - value
      title: Container Logging Http Header
    ContainerLoggingHttpCompression:
      description: The compression algorithm to apply to logs before transmission
      type: string
      enum:
        - none
        - gzip
    ContainerGroupProbeHttpHeader:
      type: object
      properties:
        name:
          description: The name of the HTTP header
          type: string
          maxLength: 256
          minLength: 1
          pattern: ^.*$
        value:
          description: The value associated with the HTTP header
          type: string
          maxLength: 1024
          minLength: 1
          pattern: ^.*$
      required:
        - name
        - value
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Salad-Api-Key

````