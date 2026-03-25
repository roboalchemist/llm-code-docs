# Source: https://docs.airbyte.com/platform/enterprise-setup/multi-region.md

# Source: https://docs.airbyte.com/platform/2.0/enterprise-setup/multi-region.md

# Source: https://docs.airbyte.com/platform/1.8/enterprise-setup/multi-region.md

# Source: https://docs.airbyte.com/platform/1.7/enterprise-setup/multi-region.md

# Source: https://docs.airbyte.com/platform/1.6/enterprise-setup/multi-region.md

# Multiple region deployments

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

Self-Managed Enterprise customers can use Airbyte's public API to define regions and create independent data planes that operate in those regions. This ensures you're satisfying your data residency and governance requirements with a single Airbyte deployment, and it can help you reduce data egress costs with cloud providers.

![Stylized diagram showing a control plane above multiple data planes in different global regions](/assets/images/data-planes-3942e06a2d769bdcfb98bf0041eee697.png)

## How it works[​](#how-it-works "Direct link to How it works")

If you're not familiar with Kubernetes, think of the control plane as the brain and data planes as the muscles doing work the brain tells them to do.

* The control plane is responsible for Airbyte's user interface, APIs, Terraform provider, and orchestrating work.
* The data plane initiates jobs, syncs data, completes jobs, and reports its status back to the control plane.

This separation of duties is what allows a single Airbyte deployment to ensure your data remains segregated and compliant.

By default, Airbyte has a single data plane that any workspace in the organization can access, and it's automatically tied to the default workspace when Airbyte first starts. To configure additional data planes and regions, complete these steps.

1. [Create a region](#step-1).
2. [Create a data plane](#step-2) in that region.
3. [Associate your data plane to an Airbyte workspace](#step-3). You can tie each workspace to exactly one region.
4. [Configure Kubernetes secrets](#step-4).
5. [Create your values.yaml file](#step-5).
6. [Deploy your data plane](#step-6).

Once you complete these steps, jobs in your workspace move data exclusively using the data plane mapped to that region.

### Limitations and considerations[​](#limitations-and-considerations "Direct link to Limitations and considerations")

While data planes process data in their respective regions, some metadata remains in the control plane.

* Airbyte stores Cursor and Primary Key data in the control plane regardless of data plane location. If you have data that you can't store in the control plane, don't use it as a cursor or primary key.

* The Connector Builder processes all data through the control plane, regardless of workspace settings. This limitation applies to the development and testing phase only; published connectors respect workspace data residency settings during syncs.

* If you're using a secrets manager, the secrets manager used by the control plane is the one used by the data plane.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before you begin, make sure you've completed the following.

* Deploy your Self-Managed Enterprise version of Airbyte as described in the [implementation guide](/platform/1.6/enterprise-setup/implementation-guide.md).

* You must be an Instance Administrator to manage regions and data planes.

* You need a Kubernetes cluster on which your data plane can run. For example, if your Airbyte control plane already runs on an EKS cluster on `us-west-2`, and you want your data plane to run on `eu-west-1`, create an EKS cluster on `eu-west-1`.

* If you haven't already, get access to Airbyte's API by creating an application and generating an access token. For help, see [Configuring API access](/platform/1.6/enterprise-setup/api-access-config.md).

## 1. Create a region[​](#step-1 "Direct link to 1. Create a region")

The first step is to create a region. Regions are objects that contain data planes, and which you associate to workspaces.

Request

Send a POST request to /v1/regions/.

```
curl --request POST \
  --url https://example.com/api/public/v1/regions \
  --header 'authorization: Bearer $TOKEN' \
  --header 'content-type: application/json' \
  --data '{
  "name": "aws-us-east-1",
  "organizationId": "00000000-0000-0000-0000-000000000000"
}'
```

Include the following parameters in your request.

| Body parameter   | Required? | Description                                                                                                                              |
| ---------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `name`           | Required  | The name of your region in Airbyte. For simplicity, you might want to make this the same as the actual cloud region this region runs on. |
| `organizationId` | Required  | Your Airbyte organization ID. In most cases, this is `00000000-0000-0000-0000-000000000000`.                                             |
| `enabled`        | Optional  | Defaults to true. Set this to `false` if you don't want this region enabled.                                                             |

For additional request examples, see [the API reference](https://reference.airbyte.com/reference/regions#/).

Response

Make note of your `regionId`. You need it to create a data plane.

200 Successful operation

```
{
  "regionId": "uuid-string",
  "name": "region-name",
  "organizationId": "org-uuid-string",
  "enabled": true,
  "createdAt": "timestamp-string",
  "updatedAt": "timestamp-string"
}
```

## 2. Create a data plane[​](#step-2 "Direct link to 2. Create a data plane")

Once you have a region, you create a data plane within it.

Request

Send a POST request to /v1/dataplanes.

```
curl -X POST https://example.com/api/public/v1/dataplanes \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -d '{
    "name": "My Data Plane"
    "regionId": "780d5bd9-a8a0-43cf-8b35-cc2061ad8319"
  }'
```

Include the following parameters in your request.

| Body parameter | Required? | Description                                                                                                         |
| -------------- | --------- | ------------------------------------------------------------------------------------------------------------------- |
| `name`         | Required  | The name of your data plane. For simplicity, you might want to name it based on the region in which you created it. |
| `regionId`     | Optional  | The region this data plane belongs to.                                                                              |

For additional request examples, see [the API reference](https://reference.airbyte.com/reference/dataplanes#/).

Response

Make note of your `dataplaneId`, `clientId` and `clientSecret`. You need these values later to deploy your data plane on Kubernetes.

200 Successful operation

```
json
{
  "dataplaneId": "uuid-string",
  "clientId": "client-id-string",
  "clientSecret": "client-secret-string"
}
```

## 3. Associate a region to a workspace[​](#step-3 "Direct link to 3. Associate a region to a workspace")

One you have a region and a data plane, you need to associate that region to your workspace. You can associate a workspace with a region when you create that workspace or later, after it exists.

note

You can only associate each workspace with one region.

### When creating a new workspace[​](#when-creating-a-new-workspace "Direct link to When creating a new workspace")

Request

Send a POST request to /v1/workspaces/

```
curl -X POST "https://example.com/api/public/v1/workspaces" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My New Workspace",
    "dataResidency": "auto"
  }'
```

Include the following parameters in your request.

| Body parameter  | Description                                               |
| --------------- | --------------------------------------------------------- |
| `name`          | The name of your workspace in Airbyte.                    |
| `dataResidency` | A string with a region identifier you received in step 1. |

For additional request examples, see [the API reference](https://reference.airbyte.com/reference/workspaces#/).

Response

```
{
  "workspaceId": "uuid-string",
  "name": "workspace-name",
  "dataResidency": "auto",
  "notifications": {
    "failure": {},
    "success": {}
  }
}
```

### When updating a workspace[​](#when-updating-a-workspace "Direct link to When updating a workspace")

Request

Send a PATCH request to /v1/workspaces/`{workspaceId}`

```
curl -X PATCH "https://example.com/api/public/v1/workspaces/{workspaceId}" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Workspace Name",
    "dataResidency": "us-west"
  }'
```

Include the following parameters in your request.

| Body parameter  | Description                                               |
| --------------- | --------------------------------------------------------- |
| `name`          | The name of your workspace in Airbyte.                    |
| `dataResidency` | A string with a region identifier you received in step 1. |

For additional request examples, see [the API reference](https://reference.airbyte.com/reference/workspaces#/).

Response

```
{
  "workspaceId": "uuid-string",
  "name": "updated-workspace-name",
  "dataResidency": "region-identifier",
  "notifications": {
    "failure": {},
    "success": {}
  }
}
```

## 4. Configure Kubernetes Secrets[​](#step-4 "Direct link to 4. Configure Kubernetes Secrets")

Your data plane relies on Kubernetes secrets to identify itself with the control plane.

In the next step, you create a values.yaml file that references this Kubernetes secret store and these secret keys. Configure all required secrets before deploying your data plane.

You may apply your Kubernetes secrets by applying the example manifests below to your cluster, or using kubectl directly. If your Kubernetes cluster already has permissions to make requests to an external entity via an instance profile, credentials aren't required. For example, if your Amazon EKS cluster has a sufficient AWS IAM role to make requests to AWS S3, you don't need to specify access keys.

### Creating a Kubernetes secret[​](#creating-a-kubernetes-secret "Direct link to Creating a Kubernetes secret")

While you can set the name of the secret to whatever you prefer, you need to set that name in your values.yaml file. For this reason it's easiest to keep the name of airbyte-config-secrets unless you have a reason to change it.

airbyte-config-secrets

* S3
* GCS

```
apiVersion: v1
kind: Secret
metadata:
  name: airbyte-config-secrets
type: Opaque
data:
  # Enterprise License Key
  license-key: your-airbyte-license-key

  # Insert the data plane credentials received in step 2
  DATA_PLANE_CLIENT_ID: your-data-plane-client-id
  DATA_PLANE_CLIENT_SECRET: your-data-plane-client-id

  # Only set these values if they are also set on your control plane
  AWS_SECRET_MANAGER_ACCESS_KEY_ID: your-aws-secret-manager-access-key
  AWS_SECRET_MANAGER_SECRET_ACCESS_KEY: your-aws-secret-manager-secret-key
  S3_ACCESS_KEY_ID: your-s3-access-key
  S3_SECRET_ACCESS_KEY: your-s3-secret-key
```

Apply your secrets manifest in your command-line tool with `kubectl`: `kubectl apply -f <file>.yaml -n <namespace>`.

You can also use `kubectl` to create the secret directly from the command-line tool:

```
kubectl create secret generic airbyte-config-secrets \
  --from-literal=license-key='' \
  --from-literal=data_plane_client_id='' \
  --from-literal=data_plane_client_secret='' \
  --from-literal=s3-access-key-id='' \
  --from-literal=s3-secret-access-key='' \
  --from-literal=aws-secret-manager-access-key-id='' \
  --from-literal=aws-secret-manager-secret-access-key='' \
  --namespace airbyte
```

First, create a new file `gcp.json` containing the credentials JSON blob for the service account you are looking to assume.

```
apiVersion: v1
kind: Secret
metadata:
  name: airbyte-config-secrets
type: Opaque
stringData:
  # Enterprise License Key
  license-key: your-airbyte-license-key

  # Insert the data plane credentials received in step 2
  DATA_PLANE_CLIENT_ID: your-data-plane-client-id
  DATA_PLANE_CLIENT_SECRET: your-data-plane-client-id

  # Only set these values if they are also set on your control plane
  AWS_SECRET_MANAGER_ACCESS_KEY_ID: your-aws-secret-manager-access-key
  AWS_SECRET_MANAGER_SECRET_ACCESS_KEY: your-aws-secret-manager-secret-key
  S3_ACCESS_KEY_ID: your-s3-access-key
  S3_SECRET_ACCESS_KEY: your-s3-secret-key

  # GCP Secrets
  gcp.json: <CREDENTIALS_JSON_BLOB>
```

Apply your secrets manifest in your command-line tool with `kubectl`: `kubectl apply -f <file>.yaml -n <namespace>`.

You can also use `kubectl` to create the secret directly from the command-line tool:

```
kubectl create secret generic airbyte-config-secrets \
  --from-literal=license-key='' \
  --from-literal=data_plane_client_id='' \
  --from-literal=data_plane_client_secret='' \
  --from-literal=s3-access-key-id='' \
  --from-literal=s3-secret-access-key='' \
  --from-literal=aws-secret-manager-access-key-id='' \
  --from-literal=aws-secret-manager-secret-access-key='' \
  --from-file=gcp.json
  --namespace airbyte
```

## 5. Create your deployment values[​](#step-5 "Direct link to 5. Create your deployment values")

Add the following overrides to a new `values.yaml` file.

values.yaml

```
airbyteUrl: https://airbyte.example.com # Base URL for the control plane so Airbyte knows where to authenticate

edition: enterprise # Required for Self-Managed Enterprise

# Logging:
#  level: DEBUG

dataPlane:
  # Used to render the data plane creds secret into the Helm chart.
  secretName: airbyte-config-secrets
  id: "preview-data-plane"

  # Describe secret name and key where each of the client ID and secret are stored
  clientIdSecretName: airbyte-config-secrets
  clientIdSecretKey: "DATA_PLANE_CLIENT_ID"
  clientSecretSecretName: airbyte-config-secrets
  clientSecretSecretKey: "DATA_PLANE_CLIENT_SECRET"

# Describe the secret name and key where the Airbyte license key is found
enterprise:
  secretName: airbyte-config-secrets
  licenseKeySecretKey: AIRBYTE_LICENSE_KEY

# S3 bucket secrets/config
# Only set this section if the control plane has also set these values.
storage:
  secretName: airbyte-config-secrets
  type: "s3"
  bucket:
    log: my-bucket-name
    state: my-bucket-name
    workloadOutput: my-bucket-name
  s3:
    region: "us-west-2"
    authenticationType: credentials
    accessKeyIdSecretKey: S3_ACCESS_KEY_ID
    secretAccessKeySecretKey: S3_SECRET_ACCESS_KEY

# Secret manager secrets/config
# Only set this section if the control plane has also set these values.
secretsManager:
  secretName: airbyte-config-secrets
  type: AWS_SECRET_MANAGER
  awsSecretManager:
    region: us-west-2
    authenticationType: credentials
    accessKeyIdSecretKey: AWS_SECRET_MANAGER_ACCESS_KEY_ID
    secretAccessKeySecretKey: AWS_SECRET_MANAGER_SECRET_ACCESS_KEY
```

## 6. Deploy your data plane[​](#step-6 "Direct link to 6. Deploy your data plane")

In your command-line tool, deploy the data plane using `helm upgrade`. The examples here may not reflect your actual Airbyte version and namespace conventions, so make sure you use the settings that are appropriate for your environment.

Example using the default namespace in your cluster

```
helm upgrade --install airbyte-enterprise airbyte/airbyte-data-plane --version 1.6.0 --values values.yaml
```

Example using or creating a namespace called 'airbyte-dataplane'

```
helm upgrade --install airbyte-enterprise airbyte/airbyte-data-plane --version 1.6.0 -n airbyte-dataplane --create-namespace --values values.yaml
```

## Check which region your workspaces use[​](#check-which-region-your-workspaces-use "Direct link to Check which region your workspaces use")

### From Airbyte's UI[​](#from-airbytes-ui "Direct link to From Airbyte's UI")

You can see a list of your workspaces and the region associated to each from Airbyte's organization settings.

1. In Airbyte's user interface, click **Settings**.

2. Click **General**.

Airbyte displays your workspaces and each workspace region under **Regions**.

![Multiple regions displayed in Airbyte\&#39;s General Organization settings](/assets/images/multiple-regions-in-airbyte-99a13c3e654ceed1f6be4b6225ef7390.png)

### From Airbyte's API[​](#from-airbytes-api "Direct link to From Airbyte's API")

Request:

```
bash
curl -X GET "https://example.com/api/public/v1/workspaces/{workspaceId}" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

Response:

```
{
  "workspaceId": "18dccc91-0ab1-4f72-9ed7-0b8fc27c5826",
  "name": "Acme Company",
  "dataResidency": "auto"
}
```
