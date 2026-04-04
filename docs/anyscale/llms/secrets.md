# Source: https://docs.anyscale.com/secrets.md

# Secret management on Anyscale

[View Markdown](/secrets.md)

# Secret management on Anyscale

Anyscale leverages secret managers in your cloud provider account to store and use secrets such as API keys, tokens, credentials, and passwords.

Anyscale recommends always using a secrets manager for storing and accessing credentials.

For Anyscale clouds on AWS, see [Configure access to Amazon Secrets Manager](/secrets/aws.md).

For Anyscale clouds on AKS, see [Use secrets from Azure Key Vault](/admin/azure/key-vault.md).

For Anyscale clouds on Google Cloud, see [Configure access to Google Secret Manager](/secrets/google-cloud.md).

note

Anyscale uses the IAM role you configure for your cloud deployment to access the secrets manager in your AWS or Google Cloud account tied to your Anyscale cloud.

If you need to access a secrets manager with a different cloud provider or are using serverless (Anyscale-hosted) clouds, contact [Anyscale support](mailto:support@anyscale.com).

## Use secrets on Anyscale[​](#use-secrets "Direct link to Use secrets on Anyscale")

Anyscale requires a secrets manager to configure credentials when using a private third-party image registry to deploy Ray clusters. The Anyscale console, CLI, and SDK have special built-in behavior to access secrets for external registries. See [Use container images from an external registry](/container-image/image-registry.md).

To reference secrets in your code on Anyscale, use the CLI or Python SDK provided by AWS, Azure, or Google Cloud.

See the following AWS docs pages for working with AWS Secrets Manager:

* [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
* [Secrets Manager examples using AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli_secrets-manager_code_examples.html)
* [Boto3 quickstart](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
* [Boto3 Secrets Manager examples](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/secrets-manager.html)

See the following example for working with Azure Key Vault secrets: [Use secrets from Azure Key Vault in Python](/admin/azure/key-vault.md#use-secrets).

See the following Google Cloud docs pages for working with the Google Secret Manager:

* [Install the gcloud CLI](https://cloud.google.com/sdk/docs/install)
* [gcloud reference for Google Secret Manager](https://cloud.google.com/sdk/gcloud/reference/secrets)
* [Python Client for Secret Manager](https://cloud.google.com/python/docs/reference/secretmanager/latest)
