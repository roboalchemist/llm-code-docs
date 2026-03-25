# Source: https://docs.anyscale.com/container-image/image-registry.md

# Use container images from an external registry

[View Markdown](/container-image/image-registry.md)

# Use container images from an external registry

You can configure Anyscale to access external image registries to launch Ray clusters with images built by external workflows or tools, such as CI/CD artifacts or local Docker builds. The following is an overview of the requirements to use images from an external registry:

* Define and build an Anyscale-compatible image. See [Anyscale-compatible custom images](/container-image/custom-image.md#compatibility).
* Upload your image to an image registry. See [Supported external image registries](#external-registries).
* If necessary, store login credentials in a secret manager. See [Store credentials for a private image registry](#creds).

You can then use your image by following one of the following flows:

* Register your external image to the Anyscale container image registry. See [Register a custom image](#register).
* Specify the image URI and credentials when configuring your Anyscale workload. See [Launch a cluster with an image from an external registry](#use-image).

For an example workflow using a local Docker build and a public Docker Hub repository, see [Tutorial: Build a custom container image](/container-image/build-image-tutorial.md).

## Register a custom image[​](#register "Direct link to Register a custom image")

You can use the Anyscale console, CLI, or SDK to register custom images from an external image registry to your Anyscale organization. When you register an image, it becomes available to all users in your Anyscale organization.

Once you've registered an image to Anyscale, you can use it the same way you use a custom image built on Anyscale. The Anyscale URI for registered images uses the following format:

```
anyscale/image/<image-name>:<version>
```

note

Unlike the custom images built on Anyscale that appear in the Anyscale image registry, registering a custom image from an external registry doesn't store the built image in the Anyscale control plane.

After accessing your image from an external registry, Anyscale builds and caches an optimized version of your image in the object storage configured for the Anyscale cloud in which your job, service, or workspace runs. Anyscale uses the cached image to deploy all nodes in your Ray cluster.

You can use images from external image registries without registering them to your organization. See [Use container images from an external registry](/container-image/image-registry.md).

The following table describes the fields you must configure when registering an image:

| Field                 | Description                                                                                                                                                                                                                                                                                                                                  |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                  | The name used to register the image in the Anyscale container image registry. If you reuse an existing name, registering an image creates a new version.                                                                                                                                                                                     |
| Image URI             | The URI for the image in your external registry.                                                                                                                                                                                                                                                                                             |
| Ray version           | The version of Ray in the image.                                                                                                                                                                                                                                                                                                             |
| Registry login secret | The name of the secret that contains the login credentials to your registry. Required unless the image registry is public or accessible through the IAM role of your Anyscale cloud. You must configure a secret to store login credentials. See [Store credentials for a private image registry](/container-image/image-registry.md#creds). |

important

If you're using a serverless Anyscale cloud (also called an Anyscale-hosted cloud), you can only use images in external registries that are publicly accessible.

To register an image from an external registry, complete the following steps:

* Anyscale console
* CLI
* SDK

note

The Anyscale console doesn't include the option to specify a registry login secret. Use the CLI or SDK if you need to access a private registry outside your cloud provider account.

1. Navigate to the Anyscale console.
2. From the console home screen, select **Advanced > Container images**.
3. Click **+ Build**.
4. In the **Name** field, provide a unique name for the image.
   <!-- -->
   * The URI of the image generates automatically. Use this URI to reference this image when you create a workspace, job, or service.
5. Under **Build step**, select **Use an image from an external registry**.
6. Enter the URI for the image in your external registry in the **Image URI** field.
7. For the **Ray version** option, select the version that corresponds to your image.
8. Click **Build**.

Run the following command from the Anyscale CLI, substituting the correct values for each placeholder value in the example syntax:

```
anyscale image register --image-uri <image-registry>:<image-tag> \
    --name <anyscale-image-name> \
    --ray-version <version> \
    --registry-login-secret <secret-name>
```

When you register an image, the SDK returns the URI identifying the image in the Anyscale container image registry.

Use the following command to register an image from the SDK, substituting the correct values for each placeholder value in the example syntax:

```
import anyscale

image_uri = anyscale.image.register(
    image_uri = "<image-registry>:<image-tag>", 
    name="<anyscale-image-name>",
    ray_version="<version>",
    registry_login_secret="<secret_name>"
    )
```

## Launch a cluster with an image from an external registry[​](#use-image "Direct link to Launch a cluster with an image from an external registry")

Workspaces, jobs, and services support launching Ray clusters using images from external image registries. You specify the following options to use an image from an external registry:

| Option                | Description                                                                                                                                 |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Image URI             | The URI for the image in your external registry.                                                                                            |
| Ray version           | The version of Ray in the image.                                                                                                            |
| Registry login secret | The name of the secret that contains the login credentials to your registry. See [Use registry login secrets on Anyscale](#registry-login). |

The Anyscale console has a dedicated flow for using images in external registries when creating a workspace. Select **Use an image from an external registry** in the **Container image > Select image** field to view the configuration.

See the following sections in the CLI and SDK reference for details on using external registries with Anyscale workspace, jobs, and services:

| Cluster type | CLI                                                                                     | SDK                                                                             | Config YAML                                                   |
| ------------ | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Workspace    | [`anyscale workspace_v2 create`](/reference/workspaces.md#anyscale-workspace_v2-create) | [`anyscale.workspace.create`](/reference/workspaces.md#anyscaleworkspacecreate) | [`WorkspaceConfig`](/reference/workspaces.md#workspaceconfig) |
| Job          | [`anyscale job submit`](/reference/job-api.md#anyscale-job-submit)                      | [`anyscale.job.submit`](/reference/job-api.md#anyscalejobsubmit)                | [`JobConfig`](/reference/job-api.md#jobconfig)                |
| Service      | [`anyscale service deploy`](/reference/service-api.md#anyscale-service-deploy)          | [`anyscale.service.deploy`](/reference/service-api.md#anyscaleservicedeploy)    | [`ServiceConfig`](/reference/service-api.md#serviceconfig)    |

## Supported external image registries[​](#external-registries "Direct link to Supported external image registries")

The following table describes common external image registries supported on Anyscale:

| Image registry                   | Description                                                                                                                                                                                                                                                                                                                    |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Azure Container Registry (ACR)   | ACR is a managed image registry on Azure. Use ACR when you're using an Anyscale cloud deployed on AKS. An Azure admin must configure access from AKS to ACR, then you can use fully qualified image URIs without passing additional credentials. See [Configure Azure Container Registry](/admin/azure/container-registry.md). |
| Elastic Container Registry (ECR) | ECR is a managed image registry on AWS. Use ECR when you're using an Anyscale cloud deployed on AWS. Configure access through your cloud IAM role. See [Access Amazon ECR](/administration/cloud-deployment/aws-ecr.md).                                                                                                       |
| Artifact Registry                | Artifact Registry is a managed image registry on Google Cloud. Use Artifact Registry when you're using an Anyscale cloud deployed on Google Cloud. Configure access through the Google Cloud service account used by your Anyscale cloud.                                                                                      |
| Private registries               | Many CI/CD tools use private artifact registries to store built images. You must configure a secret containing login credentials to use other private registries, for example Docker Hub or JFrog Artifactory. See [Store credentials for a private image registry](#creds).                                                   |
| Public registries                | Public registries typically contain images intended for general use and don't require authorization to pull images. For example, Anyscale shares base images through a [public Docker Hub registry](https://hub.docker.com/r/anyscale/ray).                                                                                    |

## Store credentials for a private image registry[​](#creds "Direct link to Store credentials for a private image registry")

Anyscale requires login credentials to pull images from private image registries. You must store these credentials in a secrets manager accessible in your Anyscale cloud.

note

If you're using a managed image registry, configure secure access using IAM features in your cloud provider.

* For Anyscale clouds on AWS, see [Configure access to Amazon Secrets Manager](/secrets/aws.md).
* For Anyscale clouds on Google Cloud, see [Configure access to Google Secret Manager](/secrets/google-cloud.md).
* For Anyscale clouds on AKS, see [Use secrets from Azure Key Vault](/admin/azure/key-vault.md).

Anyscale uses the same credentials as the `docker login` CLI command.

important

When available, Anyscale recommends using an access token with read-only credentials instead of your personal username and password. For example, Docker Hub recommends using organization access tokens to manage access permissions for integrated services. See [Docker Hub docs on organization access tokens](https://docs.docker.com/security/for-admins/access-tokens/).

Create a new secret in your secrets manager and add your login credentials using the following JSON format:

```
{
    "username": "<username>",
    "password": "<password>",
    "server": "<server>"
}
```

| Value        | Description                                                                                                                                                                                                                                                                    |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `<username>` | The login username for a user or service account with read privileges on the image registry.                                                                                                                                                                                   |
| `<password>` | The password or token used by the configured username.                                                                                                                                                                                                                         |
| `<server>`   | The URL for the server containing the private registry. For example, the server for Docker Hub is `registry.hub.docker.com`. Other registry providers might have a custom server for each customer. For example, JFrog Artifactory uses the pattern `<company-name>.jfrog.io`. |

## Use registry login secrets on Anyscale[​](#registry-login "Direct link to Use registry login secrets on Anyscale")

Use the `registry_login_secret` option when referring to images in private external image registries on Anyscale.

When you use this secret on Anyscale with the `registry_login_secret` option, Anyscale compares the server name configured with your secret to the server specified by the image URI. If the servers don't match, Anyscale doesn't submit your credentials to attempt to log in.

For Anyscale clouds on AWS, you can either specify the name of your secret or the full ARN. If you use the secret name, Anyscale uses the secret in the same account and region as the instance. To access secrets across accounts or regions, use the full ARN.

For Anyscale clouds on Google Cloud, you can either specify the name of your secret or the full identifier (`/projects/<project-id>/secrets/<secret-name>/versions/<version>`). If you use the secret name, Anyscale uses the latest version of the secret in the same project containing your Anyscale cloud. To access secrets across projects or specific versions, use the full identifier.
