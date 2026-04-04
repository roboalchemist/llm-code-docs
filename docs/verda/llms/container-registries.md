<!-- Source: https://docs.verda.com/containers/container-registries.md -->

# Container Registries

Verda Containers service supports any container registry that allows authentication using the standard Docker `config.json` format. In addition to that, we support the custom authentication methods for Docker Hub, GitHub Container Registry, and GCP Artifacts.

## Docker Hub

Use your Docker Hub username and access token (dckr\_pat\_xxxxx)

## GitHub Container Registry

Use your GitHub access token (ghp\_xxxx)

## GCP Artifacts

Use your GCP service account key file (json format)

## AWS ECR

Use your AWS credentials (access\_key\_id and secret\_access\_key). It's recommended to create a new IAM user and a keypair for it.

{% hint style="warning" %}
Ensure you assign the `ecr:GetAuthorizationToken` permission to the IAM role, or our platform will not be able to refresh the token, and container pulls will fail after 12 hours when the token expires.
{% endhint %}

## Custom Registries

Other registries can be authenticated using the keys in `config.json`.

Here is a sample key in this format:

```json
{
  "auths": {
    "my-private-registry.com": {
      "auth": "bXlwYXNzd29yZA=="
    }
  }
}
```
