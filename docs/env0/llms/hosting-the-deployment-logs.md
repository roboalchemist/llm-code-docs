# Source: https://docs.envzero.com/guides/admin-guide/self-hosted-kubernetes-agent/hosting-the-deployment-logs.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Hosting Deployment Logs

> Store env zero deployment logs in your own AWS DynamoDB table instead of the default location

By default, the deployment logs are stored in env zero, in a dedicated DynamoDB table per customer.\
If you'd like, you can store the logs in your own AWS account.

The following page will explain how to do so.

## AWS - Hosting the Deployment Logs in DynamoDB

1. Contact the env zero sales team, and supply them with the region and AWS account ID in which the logs should be stored
2. Once your self-hosted configuration is prepared, you will be able to download a `values.yaml` file from the agents tab on the organization settings page. This file contains values necessary for the agent installation. One of those values is `alternativeLogLocation.dynamoWriterExternalIdEncoded`. This is a base64 encoded externalID that env zero will use when reading and storing the deployment logs. Base64 decode the external ID, you will need it for the next step
3. On your AWS account, deploy the [env zero log table terraform module](https://github.com/env0/k8s-modules/tree/main/log-storage/aws/dynamodb). This module creates the table on your account and the role that env zero will assume when reading and writing the logs. For the variables, make sure to add the following data:

* external\_id - The base64 decoded external ID from the previous step
* agent\_key - The unique env zero agent identifier supplied to you

1. Now you are done creating the necessary resources for hosting the deployment logs in your own DynamoDB table. Once you finish your Kubernetes agent installation, the deployment logs will be written there

Built with [Mintlify](https://mintlify.com).
