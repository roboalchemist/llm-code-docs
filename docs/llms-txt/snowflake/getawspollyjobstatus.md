# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/getawspollyjobstatus.md

# GetAwsPollyJobStatus 2025.10.9.21

## Bundle

org.apache.nifi | nifi-aws-nar

## Description

Retrieves the current status of an AWS Polly job.

## Tags

AWS, Amazon, ML, Machine Learning, Polly

## Input Requirement

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| AWS Credentials Provider service | The Controller Service that is used to obtain AWS credentials provider |
| AWS Task ID |  |
| Communications Timeout |  |
| Endpoint Override URL | Endpoint URL to use instead of the AWS default including scheme, host, port, and path. The AWS libraries select an endpoint URL based on the AWS region, but this property overrides the selected endpoint URL, allowing use with other S3-compatible endpoints. |
| Region |  |
| SSL Context Service | Specifies an optional SSL Context Service that, if provided, will be used to create connections |
| proxy-configuration-service | Specifies the Proxy Configuration Controller Service to proxy network requests. |

## Relationships

| Name | Description |
| --- | --- |
| failure | The job failed, the original FlowFile will be routed to this relationship. |
| original | Upon successful completion, the original FlowFile will be routed to this relationship. |
| running | The job is currently still being processed |
| success | Job successfully finished. FlowFile will be routed to this relation. |

## Writes attributes

| Name | Description |
| --- | --- |
| PollyS3OutputBucket | The bucket name where polly output will be located. |
| filename | Object key of polly output. |
| outputLocation | S3 path-style output location of the result. |

## See also

* [org.apache.nifi.processors.aws.ml.polly.StartAwsPollyJob](startawspollyjob.md)
