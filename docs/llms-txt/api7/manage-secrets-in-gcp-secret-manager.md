# Source: https://docs.api7.ai/apisix/how-to-guide/security/secrets-management/manage-secrets-in-gcp-secret-manager.md

# Manage Secrets in GCP Secret Manager

[GCP Secret Manager](https://cloud.google.com/security/products/secret-manager?hl=en) is a fully managed service for storing, managing, and accessing sensitive information such as API keys, passwords, and certificates. It allows you to store secrets centrally with encryption, automate versioning, and control access using Google Cloudâs IAM policies.

This guide will show you how to use GCP Secret Manager to manage user credentials for authentication plugin [`key-auth`](https://docs.api7.ai/hub/key-auth.md) and how to retrieve the secret in APISIX.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker.
* Have a [GCP account](https://cloud.google.com/?hl=en) and enable Secret Manager.

## Create a Secret in GCP Secret Manager[â](#create-a-secret-in-gcp-secret-manager "Direct link to Create a Secret in GCP Secret Manager")

In this section, you will be creating a secret to store the key-auth authentication key for consumer `john`.

Navigate to GCP Secret Manager in the console and create a secret. Fill in the name `apisix-john-key-auth` and the secret `john-key`:

![create a secret for john in GCP secret manager](https://static.api7.ai/uploads/2024/10/16/JNC60Z8O_gcp-step-1.png)

Review the rest of the information and finish secret creation. You should see the secret listed in GCP Secret Manager:

![see the secret listed in the GCP secret manager](https://static.api7.ai/uploads/2024/10/16/WFQQaug5_gcp-step-2.png)

## Obtain GCP Access Credentials[â](#obtain-gcp-access-credentials "Direct link to Obtain GCP Access Credentials")

Follow the [service account credentials](https://developers.google.com/workspace/guides/create-credentials#service-account) doc to create a service account in GCP, assign the account with the **Secret Manager Secret Accessor** role, and create credentials for the account.

You should see a JSON file containing the credentials generated and downloaded to your machine, similar to the following:

```
{
  "type": "service_account",
  "project_id": "apisix-project",
  "private_key_id": "f039bb20b2xxxxxxxxxb43cb7132axxxxxx1f165",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  "client_email": "apisix-secret-manager@apisix-project.iam.gserviceaccount.com",
  "client_id": "115458xxxxxxx68702206",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/apisix-secret-manager%40apisix-project.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
```

## Update Trusted Certificates in APISIX[â](#update-trusted-certificates-in-apisix "Direct link to Update Trusted Certificates in APISIX")

Steps in this section are only required if you use the default configuration with SSL verification. If you wish to disable SSL verification, set `ssl_verify` to `false` in the [next step](#configure-secret-in-apisix).

Update the path to the CA certificates in the [configuration file](https://docs.api7.ai/apisix/reference/configuration-files.md#configyaml-and-configyamlexample):

```
docker exec apisix-quickstart /bin/bash -c "echo '
apisix:
  ssl:
    ssl_trusted_certificate: /etc/ssl/certs/ca-certificates.crt
  enable_control: true
  control:
    ip: "0.0.0.0"
    port: 9092
deployment:
  role: traditional
  role_traditional:
    config_provider: etcd
  admin:
    admin_key_required: false
    allow_admin:
      - 0.0.0.0/0
plugin_attr:
  prometheus:
    export_addr:
      ip: 0.0.0.0
      port: 9091
  ' > /usr/local/apisix/conf/config.yaml"
```

[Reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for configuration changes to take effect:

```
docker exec apisix-quickstart apisix reload
```

## Configure Secret in APISIX[â](#configure-secret-in-apisix "Direct link to Configure Secret in APISIX")

Configure GCP Secret Manager to be a secret provider for john with the access credentials obtained in the [last step](#obtain-gcp-access-credentials):

```
curl "http://127.0.0.1:9180/apisix/admin/secrets/gcp/john" -X PUT -d '
{
  "auth_config": {
    "client_email": "apisix-secret-manager@apisix-project.iam.gserviceaccount.com",
    "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
    "project_id": "apisix-project"
  },
  "ssl_verify": true
}'
```

â¶ Replace with your client email.

â· Replace with your private key.

â¸ Replace with your project ID.

â¹ Enable SSL verification (default).

## Create a Consumer and its Credential[â](#create-a-consumer-and-its-credential "Direct link to Create a Consumer and its Credential")

Create a consumer `john`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT -d '
{
  "username": "john"
}'
```

Configure the `key-auth` credential for consumer `john` to fetch the key from secret provider:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/john/credentials" -X PUT -d '
{
  "id": "cred-john-key-auth",
  "plugins": {
    "key-auth": {
      "key": "$secret://gcp/john/apisix-john-key-auth"
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

Send a request to the route with an invalid credential:

```
curl -i "http://127.0.0.1:9080/anything" -H 'apikey: wrong-key'
```

You should receive an `HTTP/1.1 401 Unauthorized` response.

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have now learned how to configure APISIX to fetch secrets from GCP Secret Manager.

In addition to GCP Secret Manager, APISIX also supports the integration with [HashiCorp Vault](https://docs.api7.ai/apisix/how-to-guide/security/secrets-management/manage-secrets-in-hashicorp-vault.md) and [AWS Secrets Manager](https://docs.api7.ai/apisix/how-to-guide/security/secrets-management/manage-secrets-in-aws.md) for secret management.
