# Source: https://docs.api7.ai/apisix/how-to-guide/security/secrets-management/manage-secrets-in-aws.md

# Manage Secrets in AWS Secrets Manager

[AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) is a fully managed service that you can integrate with APISIX to securely store, manage, and retrieve sensitive information such as API keys, passwords, and other types of credentials. It allows automatic rotation of secrets, reducing the risk of credentials being exposed over time.

This guide will show you how to use AWS Secrets Manager to manage user credentials for the [`key-auth`](https://docs.api7.ai/hub/key-auth.md) plugin and how to retrieve the secret in APISIX.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker.
* Have an [AWS account](https://aws.amazon.com).

## Create a Secret in AWS Secrets Manager[â](#create-a-secret-in-aws-secrets-manager "Direct link to Create a Secret in AWS Secrets Manager")

In this section, you will be creating a secret to store the [`key-auth`](https://docs.api7.ai/hub/key-auth.md) authentication key for user `john`.

Navigate to AWS Secrets Manager in the console and create a secret. Choose **Other type of secret** as the secret type and enter the name of the key `john-key-auth` and the credential `john-key` in the key-value pairs:

![create a secret in AWS step 1](https://static.api7.ai/uploads/2024/10/15/cE5VB3JE_aws-step-1-secret.png)

In the next step, configure the name of the secret to be `apisix-secrets` and optionally add a description:

![create a secret in AWS step 2](https://static.api7.ai/uploads/2024/12/12/XuDtH9cL_aws_Step_2.png)

Review the rest of the information and finish secret creation. You should see the secret listed in AWS Secrets Manager:

![finish secret creation in AWS](https://static.api7.ai/uploads/2024/12/12/9pQHpijS_aws_final.png)

## Obtain IAM Access Key ID and Secret Access Key[â](#obtain-iam-access-key-id-and-secret-access-key "Direct link to Obtain IAM Access Key ID and Secret Access Key")

Obtain the [IAM user access key and secret access key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey), which will be configured in APISIX in the next step to access AWS Secrets Manager.

Alternatively, you can also create a [temporary security credential](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) and configure the credential in the APISIX secret's `session_token`. See [Admin API](https://docs.api7.ai/apisix/reference/admin-api/.md#tag/Secret/paths/~1apisix~1admin~1secrets~1%7Bsecretmanager%7D~1%7Bid%7D/put) for configuration reference.

## Configure Secret in APISIX[â](#configure-secret-in-apisix "Direct link to Configure Secret in APISIX")

Configure AWS Secrets Manager to be a secret provider for `john` and specify the AWS region, access key ID, and secret access key:

```
curl "http://127.0.0.1:9180/apisix/admin/secrets/aws/john" -X PUT -d '
{
  "region": "ap-southeast-2",
  "access_key_id": "AKIAIOSFODNN7EXAMPLE",
  "secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
}'
```

## Create a Consumer and its Credential[â](#create-a-consumer-and-its-credential "Direct link to Create a Consumer and its Credential")

Create a consumer `john`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT -d '
{
  "username": "john"
}'
```

Configure the `key-auth` credential for consumer `john` to fetch the key from the secret provider:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/john/credentials" -X PUT -d '
{
  "id": "cred-john-key-auth",
  "plugins": {
    "key-auth": {
      "key": "$secret://aws/john/apisix-secrets/john-key-auth"
    }
  }
}'
```

## Create a Route with Authentication[â](#create-a-route-with-authentication "Direct link to Create a Route with Authentication")

Create a sample route and enable the `key-auth` plugin:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "key-auth-route",
  "uri": "/anything",
  "plugins": {
    "key-auth": {}
  },
  "upstream" : {
    "nodes": {
    "httpbin.org": 1
    }
  }
}'
```

## Verify[â](#verify "Direct link to Verify")

Send a request to the route with the valid credential:

```
curl -i "http://127.0.0.1:9080/anything" -H 'apikey: john-key'
```

You should receive an `HTTP/1.1 200 OK` response.

tip

If you are receiving a `401 Unauthorized` response with the `unable to get local issuer certificate` error in the error log, please add the path to the certificate manually to the configuration file:

conf/config.yaml

```
apisix:
  ssl:
    ssl_trusted_certificate: /etc/ssl/certs/ca-certificates.crt
```

Then [reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for configuration changes to take effect:

```
docker exec apisix-quickstart apisix reload
```

Send a request to the route with an invalid credential:

```
curl -i "http://127.0.0.1:9080/anything" -H 'apikey: wrong-key'
```

You should receive an `HTTP/1.1 401 Unauthorized` response.

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have now learned how to configure APISIX to fetch secrets from AWS Secrets Manager.

In addition to AWS Secrets Manager, APISIX also supports the integration with [HashiCorp Vault](https://docs.api7.ai/apisix/how-to-guide/security/secrets-management/manage-secrets-in-hashicorp-vault.md) and [GCP Secret Manager](https://docs.api7.ai/apisix/how-to-guide/security/secrets-management/manage-secrets-in-gcp-secret-manager.md) for secret management.
