# Source: https://docs.datadoghq.com/agent/configuration/secrets-management.md

---
title: Secrets Management
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Agent > Agent Configuration > Secrets Management
---

# Secrets Management

## Overview{% #overview %}

The Datadog Agent helps you securely manage your secrets by integrating with the following secrets management solutions:

- AWS Secrets Manager
- AWS SSM
- Azure KeyVault
- GCP Secret Manager
- HashiCorp Vault
- File JSON
- File YAML

Instead of hardcoding sensitive values like API keys or passwords in plaintext within configuration files, the Agent can retrieve them dynamically at runtime. To reference a secret in your configuration, use the `ENC[<secret_id>]` notation. The secret is fetched and loaded in memory but is never written to disk or sent to the Datadog backend.

**Note**: You cannot use the `ENC[]` syntax in `secret_*` settings like `secret_backend_command`.

## Options for retrieving secrets{% #options-for-retrieving-secrets %}

### Option 1: Using native Agent support for fetching secrets{% #option-1-using-native-agent-support-for-fetching-secrets %}

**Note**: This option is not available for FIPS-enabled Agents at this time.

Starting in Agent version `7.70`, the Datadog Agent natively supports several secret management solutions. Two new settings have been introduced to `datadog.yaml`: `secret_backend_type` and `secret_backend_config`.

`secret_backend_type` is used to specify which secret management solution to use, and `secret_backend_config` holds additional configuration relevant to that solution.

```yaml
# datadog.yaml

secret_backend_type: <backend_type>
secret_backend_config:
  <KEY_1>: <VALUE_1>
```

More specific setup instructions depend on the backend type used. See the appropriate section below for further information:

{% collapsible-section #id-for-secrets %}
#### AWS Secrets

The following AWS services are supported:

| secret_backend_type value | AWS Service                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------- |
| `aws.secrets`             | [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) |

##### Set up an instance profile{% #set-up-an-instance-profile %}

Datadog recommends using the [instance profile method](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) of retrieving secrets, as AWS handles all environment variables and session profiles for you. More instructions on how to do this can be found at the official [AWS Secrets Manager documentation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html).

##### Configuration example{% #configuration-example %}

{% tab title="Agent YAML file" %}
Configure the Datadog Agent to use AWS Secrets to resolve secrets using the following configuration:

```yaml
# datadog.yaml
secret_backend_type: aws.secrets
secret_backend_config:
  aws_session:
    aws_region: {regionName}
```

When using environment variables, convert the configuration to JSON like so:

```sh
DD_SECRET_BACKEND_TYPE="aws.secrets"
DD_SECRET_BACKEND_CONFIG='{"aws_session":{"aws_region":"<AWS_REGION>"}}'
```

After configuring the Agent to use AWS Secrets, you can reference any secrets in your configurations with `ENC[secretId;secretKey]`.

The ENC notation is composed of:

- `secretId`: either the secret "friendly name" (for example, `/DatadogAgent/Production`) or the ARN (for example, `arn:aws:secretsmanager:us-east-1:123456789012:secret:/DatadogAgent/Production-FOga1K`).
  - **Note**: The full ARN format is required when accessing secrets from a different account where the AWS credential or `sts:AssumeRole` credential is defined.
- `secretKey`: the JSON key from the AWS secret that you want to use.

The AWS Secrets Manager can store multiple key-value pairs within a single secret. A backend configuration using Secrets Manager has access to all the keys defined in a secret.

For example, assuming the secret ID `My-Secrets` contains the following 3 values:

```json
{
    "prodApiKey": "datadog api key to use",
    "anotherSecret1": "value2",
    "anotherSecret2": "value3",
}
```

The following is a complete example of the `datadog.yaml` configuration file using the AWS Secrets to pull its API key from `My-Secrets`:

```yaml
api_key: ENC[My-Secrets;prodApiKey]

secret_backend_type: aws.secrets
secret_backend_config:
  aws_session:
    aws_region: us-east-1
```

{% /tab %}

{% tab title="Helm" %}
Configure the Datadog Agent to use AWS Secrets to resolve secrets in Helm using the following configuration:

##### Integration check{% #integration-check %}

```sh
datadog:
  confd:
  # This is an example
    <INTEGRATION_NAME>.yaml: |-
      ad_identifiers:
        - <SHORT_IMAGE>
      instances:
        - [...]
          password: "ENC[secretId;secretKey]"
  env:
   - name: DD_SECRET_BACKEND_TYPE
     value: "aws.secrets"
   - name: DD_SECRET_BACKEND_CONFIG
     value: '{"aws_session":{"aws_region":"<AWS_REGION>"}}'
agents:
  rbac:
    # IAM role ARN required to grant the Agent permissions to access the AWS secret
    serviceAccountAnnotations:
      eks.amazonaws.com/role-arn: <IAM_ROLE_ARN>
```

{% alert level="info" %}
You must include the `serviceAccountAnnotations` to grant the Agent permissions to access the AWS secret.
{% /alert %}

##### Cluster check: without cluster check runners enabled{% #cluster-check-without-cluster-check-runners-enabled %}

```sh
datadog:
  env:
   - name: DD_SECRET_BACKEND_TYPE
     value: "aws.secrets"
   - name: DD_SECRET_BACKEND_CONFIG
     value: '{"aws_session":{"aws_region":"<AWS_REGION>"}}'
agents:
  rbac:
    # IAM role ARN required to grant the Agent permissions to access the AWS secret
    serviceAccountAnnotations:
      eks.amazonaws.com/role-arn: <IAM_ROLE_ARN>
clusterAgent:
  confd:
    # This is an example
    <INTEGRATION_NAME>.yaml: |-
      cluster_check: true
      instances:
        - [...]
          password: "ENC[secretId;secretKey]"
```

##### Cluster check: with cluster check runners enabled{% #cluster-check-with-cluster-check-runners-enabled %}

```sh
datadog:
  env:
   - name: DD_SECRET_BACKEND_TYPE
     value: "aws.secrets"
   - name: DD_SECRET_BACKEND_CONFIG
     value: '{"aws_session":{"aws_region":"<AWS_REGION>"}}'
clusterAgent:
  confd:
  # This is an example
    <INTEGRATION_NAME>.yaml: |-
      cluster_check: true
      instances:
        - [...]
          password: "ENC[secretId;secretKey]"
clusterChecksRunner:
  enabled: true
  env:
   - name: DD_SECRET_BACKEND_TYPE
     value: "aws.secrets"
   - name: DD_SECRET_BACKEND_CONFIG
     value: '{"aws_session":{"aws_region":"<AWS_REGION>"}}'
  rbac:
    # IAM role ARN required to grant the Agent permissions to access the AWS secret
    serviceAccountAnnotations:
      eks.amazonaws.com/role-arn: <IAM_ROLE_ARN>
```

{% /tab %}

{% tab title="Operator" %}
Configure the Datadog Agent to use AWS Secrets to resolve secrets with the Datadog Operator using the following configuration:

##### Integration check{% #integration-check %}

```sh
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  [...]
  override:
    nodeAgent:
      env:
       - name: DD_SECRET_BACKEND_TYPE
         value: "aws.secrets"
       - name: DD_SECRET_BACKEND_CONFIG
         value: '{"aws_session":{"aws_region":"<AWS_REGION>"}}'
      # IAM role ARN is required to grant the Agent permissions to access the AWS secret
      serviceAccountAnnotations:
        eks.amazonaws.com/role-arn: <IAM_ROLE_ARN>
      extraConfd:
        configDataMap:
        # This is an example
          <INTEGRATION_NAME>.yaml: |-
            ad_identifiers:
              - <SHORT_IMAGE>
            instances:
              - [...]
                 password: "ENC[secretId;secretKey]"
```

{% alert level="info" %}
You must include the `serviceAccountAnnotations` to grant the Agent permissions to access the AWS secret.
{% /alert %}

##### Cluster check: without cluster check runners enabled{% #cluster-check-without-cluster-check-runners-enabled %}

```sh
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  [...]
  override:
    nodeAgent:
      env:
       - name: DD_SECRET_BACKEND_TYPE
         value: "aws.secrets"
       - name: DD_SECRET_BACKEND_CONFIG
         value: '{"aws_session":{"aws_region":"<AWS_REGION>"}}'
      # IAM role ARN required to grant the Agent permissions to access the AWS secret
      serviceAccountAnnotations:
        eks.amazonaws.com/role-arn: <IAM_ROLE_ARN>
    clusterAgent:
      extraConfd:
        configDataMap:
        # This is an example
          <INTEGRATION_NAME>.yaml: |-
            cluster_check: true
            instances:
              - [...]
                password: "ENC[secretId;secretKey]"
```

##### Cluster check: with cluster check runners enabled{% #cluster-check-with-cluster-check-runners-enabled %}

```sh
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  [...]
spec:
  features:
    clusterChecks:
      useClusterChecksRunners: true
  override:
    [...]
    clusterChecksRunner:
      env:
       - name: DD_SECRET_BACKEND_TYPE
         value: "aws.secrets"
       - name: DD_SECRET_BACKEND_CONFIG
         value: '{"aws_session":{"aws_region":"<AWS_REGION>"}}'
      # IAM role ARN required to grant the Agent permissions to access the AWS secret
      serviceAccountAnnotations:
        eks.amazonaws.com/role-arn: <IAM_ROLE_ARN>
    clusterAgent:
      extraConfd:
        configDataMap:
        # This is an example
          <INTEGRATION_NAME>.yaml: |-
            cluster_check: true
            instances:
              - [...]
                password: "ENC[secretId;secretKey]"
```

{% /tab %}

{% /collapsible-section %}

{% collapsible-section #id-for-ssm %}
#### AWS SSM

The following AWS services are supported:

| secret_backend_type value | AWS Service                                                                                                                              |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `aws.ssm`                 | [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) |

##### Set up an instance profile{% #set-up-an-instance-profile-1 %}

Datadog recommends using the [instance profile method](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) of retrieving secrets, as AWS handles all environment variables and session profiles for you. More instructions on how to do this can be found at the official [AWS Secrets Manager documentation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html).

##### Configuration example{% #configuration-example-1 %}

The AWS System Manager Parameter Store supports a hierarchical model. For example, assuming the following AWS System Manager Parameter Store paths:

```sh
/DatadogAgent/Production/ApiKey = <your_api_key>
/DatadogAgent/Production/ParameterKey2 = ParameterStringValue2
/DatadogAgent/Production/ParameterKey3 = ParameterStringValue3
```

The parameters can be fetched like so:

```yaml
# datadog.yaml
secret_backend_type: aws.ssm
secret_backend_config:
  aws_session:
    aws_region: us-east-1

api_key: "ENC[/DatadogAgent/Production/ApiKey]"
property1: "ENC[/DatadogAgent/Production/ParameterKey1]"
property2: "ENC[/DatadogAgent/Production/ParameterKey2]"
```

{% /collapsible-section %}

{% collapsible-section #id-for-azure %}
#### Azure Keyvault Backend

The following Azure services are supported:

| secret_backend_type value | Azure Service                                                                                  |
| ------------------------- | ---------------------------------------------------------------------------------------------- |
| `azure.keyvault`          | [Azure Keyvault](https://docs.microsoft.com/en-us/Azure/key-vault/secrets/quick-create-portal) |

##### Azure authentication{% #azure-authentication %}

Datadog recommends using Managed Identities to authenticate with Azure. This allows you to associate cloud resources with AMI accounts and removes the need to put sensitive information in your `datadog.yaml` configuration file.

##### Managed identity{% #managed-identity %}

To access your Key Vault, create a Managed Identity and assign it to your Virtual Machine. Then, configure the appropriate role assignment on the Key Vault to allow that identity to access its secrets.

##### Configuration example{% #configuration-example-2 %}

The backend configuration for Azure Key Vault secrets is structured as YAML following this schema:

```yaml
# datadog.yaml
secret_backend_type: azure.keyvault
secret_backend_config:
  keyvaulturl: {keyVaultURL}
```

The backend secret is referenced in your Datadog Agent configuration file with `ENC[ ]`. The following is an example where a plain text secret needs to be retrieved:

```yaml
# datadog.yaml

api_key: "ENC[secretKeyNameInKeyVault]"
```

{% /collapsible-section %}

{% collapsible-section #id-for-gcp %}
#### GCP Secret Manager

**Available in Agent version 7.74+**

The following GCP services are supported:

| secret_backend_type value | GCP Service                                                                     |
| ------------------------- | ------------------------------------------------------------------------------- |
| `gcp.secretmanager`       | [GCP Secret Manager](https://cloud.google.com/security/products/secret-manager) |

##### GCP authentication and access policy{% #gcp-authentication-and-access-policy %}

The GCP Secret Manager implementation uses [Application Default Credentials (ADC)](https://cloud.google.com/docs/authentication/application-default-credentials) for authentication with Google.

To interact with GCP Secret Manager, the service account used by the Datadog Agent (such as the VM's service account, a workload identity, or locally activated credentials) requires the `secretmanager.versions.access` permission.

This can be granted with the predefined role **Secret Manager Secret Accessor** (`roles/secretmanager.secretAccessor`) or a custom role with equivalent [access](https://docs.cloud.google.com/secret-manager/docs/access-control).

On GCE or GKE runtimes, ADC is configured automatically through the instance or pod's attached service account. The attached service account needs to have the proper roles to access GCP Secret Manager. In addition, the GCE or GKE runtime requires the `cloud-platform` [OAuth access scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api).

##### GCP configuration example{% #gcp-configuration-example %}

Configure the Datadog Agent to use GCP Secret Manager to resolve secrets with the following configuration:

```yaml
# datadog.yaml
secret_backend_type: gcp.secretmanager
secret_backend_config:
  gcp_session:
    project_id: <PROJECT_ID>
```

After configuring the Agent to use GCP Secret Manager, reference secrets in your configurations with `ENC[secret-name]` or `ENC[secret-name;key;version;]`.

The ENC notation is composed of:

- `secret`: the secret name in GCP Secret Manager (for example, `datadog-api-key`).
- `key`: (optional) the key to extract from a JSON-formatted secret. If you're using plain-text secrets you can ommit this (example: `ENC[secret-name;;version]`).
- `version`: (optional) the secret version number. If not specified, the `latest` version is used.
  - Version syntax examples:
    - `secret-key` - Implicit `latest` version
    - `secret-key;;latest` - Explicit `latest` version
    - `secret-key;;1` - Specific version number

For example, assuming GCP secrets named `datadog-api-key` with two versions and `datadog-app-key`:

```yaml
# datadog.yaml
api_key: ENC[datadog-api-key;;1] # specify the first version of the api key
app_key: ENC[datadog-app-key] # latest version

secret_backend_type: gcp.secretmanager
secret_backend_config:
  gcp_session:
    project_id: <PROJECT_ID>
```

For JSON-formatted secrets, assuming a secret named `datadog-keys` contains:

```json
{
  "api_key": "your_api_key_value",
  "app_key": "your_app_key_value"
}
```

Reference specific keys like this:

```yaml
# datadog.yaml
api_key: ENC[datadog-keys;api_key;1] # specify the first version of the api key
app_key: ENC[datadog-keys;app_key] # latest

secret_backend_type: gcp.secretmanager
secret_backend_config:
  gcp_session:
    project_id: <PROJECT_ID>
```

##### Secret versioning{% #secret-versioning %}

GCP Secret Manager supports secret versions. The Agent implementation also supports secret versioning using the `;` delimiter. If no version is specified, the `latest` version is used.

##### JSON secret support{% #json-secret-support %}

The Datadog Agent supports extracting specific keys from JSON-formatted secrets using the `;` delimiter:

- `datadog;api_key` - Extracts the `api_key` field from the `datadog` secret with an implicit `latest` version
- `datadog;api_key;1` - Extracts the `api_key` field from the `datadog` secret from version `1`

{% /collapsible-section %}

{% collapsible-section #id-for-hashicorp %}
#### HashiCorp Vault Backend

The following HashiCorp services are supported:

| secret_backend_type value | HashiCorp Service                                                                                               |
| ------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `hashicorp.vault`         | [HashiCorp Vault (Secrets Engine Versions 1 and 2)](https://learn.hashicorp.com/tutorials/vault/static-secrets) |

##### How to set up HashiCorp Vault{% #how-to-set-up-hashicorp-vault %}

1. Run your HashiCorp Vault. See the [official HashiCorp Vault documentation](https://developer.hashicorp.com/) for more information.
1. Write a policy that gives the permission to pull secrets from your vault. Create a `*.hcl` file, and include the following permission if using Secrets Engine Version 1:

```
path "<your mount path>/<additional subpath>" {
  capabilities = ["read"]
}
```

If using Secrets Engine Version 2, then the following permissions are needed:

```
path "<your_mount_path>/data/<additional_subpath>" {
  capabilities = ["read"]
}

/*
Datadog needs access to mount information to check the Secrets Engine version
number. If access isn't granted, version 1 is assumed.
*/
path "sys/mounts" {
  capabilities = ["read"]
}
```

Run `vault policy write <policy_name> <path_to_*.hcl_file>`

Choose the method of authenticating to your vault. If using the AWS instance profile method, run `vault auth enable aws`.

##### AWS instance profile instructions{% #aws-instance-profile-instructions %}

Datadog recommends that you authenticate using the [instance profile method](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) if you are running your HashiCorp Vault from an AWS-connected machine.

After this has been set up, write an [authentication-specific vault policy](https://developer.hashicorp.com/vault/docs/auth/aws#iam-authentication-inferences).

##### Configuration example{% #configuration-example-3 %}

In the following example, assume the HashiCorp Vault secret path prefix is `/Datadog/Production` with a parameter key of `apikey`:

```sh
/DatadogAgent/Production/apikey: (SecureString) "<your_api_key>"
```

The following example fetches the API key value from HashiCorp Vault leveraging AWS for authentication.

```yaml
# datadog.yaml
api_key: "ENC[/Datadog/Production;apikey]"

secret_backend_type: hashicorp.vault
secret_backend_config:
  vault_address: http://myvaultaddress.net
  vault_session:
    vault_auth_type: aws
    vault_aws_role: Name-of-IAM-role-attached-to-machine
    aws_region: us-east-1 // this field is optional, and will default to us-east-1 if not set
```

{% /collapsible-section %}

{% collapsible-section #id-for-json-yaml %}
#### JSON or YAML File Secret Backends

| secret_backend_type value | File Service                               |
| ------------------------- | ------------------------------------------ |
| `file.json`               | [JSON](https://en.wikipedia.org/wiki/JSON) |
| `file.yaml`               | [YAML](https://en.wikipedia.org/wiki/YAML) |

##### File permissions{% #file-permissions %}

The file backend only requires **read** permissions for the configured JSON or YAML files. These permissions must be granted to the local Datadog Agent user (`dd-agent` on Linux, `ddagentuser` on Windows).

{% tab title="JSON File Backend" %}
**Note**: Only one level of JSON depth is supported (for example, `{"key": "value"}`)

##### Configuration example{% #configuration-example %}

You can use a JSON file to store secrets locally.

For example, with a JSON file in `/path/to/secret.json` containing the following:

```json
{
  "datadog_api_key": "your_api_key"
}
```

You can use this configuration to pull its secrets:

```yaml
# datadog.yaml
api_key: "ENC[datadog_api_key]"

secret_backend_type: file.json
secret_backend_config:
  file_path: /path/to/secret.json
```

{% /tab %}

{% tab title="YAML File Backend" %}
**Note**: Only one level of YAML depth is supported (for example, `key: value`)

##### Configuration example{% #configuration-example %}

You can use a YAML file to store secrets locally.

As an example if we have a YAML file in `/path/to/secret.yaml` containing:

```yaml
datadog_api_key: your api key
```

You can use the following configuration to pull secrets from it:

```yaml
# datadog.yaml
api_key: "ENC[datadog_api_key]"
secret_backend_type: file.yaml
secret_backend_config:
  file_path: /path/to/secret.yaml
```

{% /tab %}

{% /collapsible-section %}

### Option 2: Using the built-in Script for Kubernetes and Docker{% #option-2-using-the-built-in-script-for-kubernetes-and-docker %}

For containerized environments, the Datadog Agent's container images include a built-in script `/readsecret_multiple_providers.sh` starting with version v7.32.0. This script supports reading secrets from:

- Files: using `ENC[file@/path/to/file]`
- Kubernetes Secrets: using `ENC[k8s_secret@namespace/secret-name/key]`

{% tab title="Datadog Operator" %}
To use this executable with the Datadog Operator, configure it as follows:

```yaml
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  global:
    secretBackend:
      command: "/readsecret_multiple_providers.sh"
```

{% /tab %}

{% tab title="Helm" %}
To use this executable with the Helm chart, set it as the following:

```yaml
datadog:
  [...]
  secretBackend:
    command: "/readsecret_multiple_providers.sh"
```

{% /tab %}

{% tab title="DaemonSet" %}
To use this executable, set the environment variable `DD_SECRET_BACKEND_COMMAND` as follows:

```
DD_SECRET_BACKEND_COMMAND=/readsecret_multiple_providers.sh
```

{% /tab %}

#### Example: Reading from mounted files{% #example-reading-from-mounted-files %}

Kubernetes supports [exposing Secrets as files](https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/#create-a-pod-that-has-access-to-the-secret-data-through-a-volume) inside a pod that the Agent can read to resolve secrets.

In Kubernetes, you can mount a Secret as a volume like this:

```yaml
  containers:
    - name: agent
      #(...)
      volumeMounts:
        - name: secret-volume
          mountPath: /etc/secret-volume
  #(...)
  volumes:
    - name: secret-volume
      secret:
        secretName: test-secret
```

You can then reference the secret like this:

```
password: ENC[file@/etc/secret-volume/password]
```

**Notes**:

- The Secret must exist in the same namespace as the pod it is being mounted in.
- The script is able to access all subfolders, including the sensitive `/var/run/secrets/kubernetes.io/serviceaccount/token`. As such, Datadog recommends using a dedicated folder instead of `/var/run/secrets`.

[Docker swarm secrets](https://docs.docker.com/engine/swarm/secrets/) are mounted in the `/run/secrets` folder. For example, the Docker secret `db_prod_passsword` is located in `/run/secrets/db_prod_password` in the Agent container. This would be referenced in the configuration with `ENC[file@/run/secrets/db_prod_password]`.

#### Example: Reading a Kubernetes secret across namespaces{% #example-reading-a-kubernetes-secret-across-namespaces %}

If you want the Agent to read a Secret from a different namespace, use the `k8s_secret@` prefix. For example:

```
password: ENC[k8s_secret@database/database-secret/password]
```

Configure RBAC to allow the Agent's Service Account to read the Secret. The following Role grants read access to the `database-secret` Secret in the `database` namespace:

{% tab title="Datadog Operator" %}

```yaml
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  global:
    secretBackend:
      command: "/readsecret_multiple_providers.sh"
      roles:
      - namespace: database
        secrets:
        - "database-secret"
```

***Note***: Each namespace in the roles list must also be configured in the `WATCH_NAMESPACE` or `DD_AGENT_WATCH_NAMESPACE` environment variable on the Datadog Operator deployment.
{% /tab %}

{% tab title="Helm" %}

```yaml
datadog:
  (...)
  secretBackend:
    command: "/readsecret_multiple_providers.sh"
    roles:
      - namespace: database
        secrets:
          - database-secret
```

{% /tab %}



Alternatively, you can define RBAC resources directly:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: datadog-secret-reader
  namespace: database
rules:
  - apiGroups: [""]
    resources: ["secrets"]
    resourceNames: ["database-secret"]
    verbs: ["get", "watch", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: datadog-read-secrets
  namespace: database
subjects:
  - kind: ServiceAccount
    name: datadog-agent
    apiGroup: ""
    namespace: default
roleRef:
  kind: Role
  name: datadog-secret-reader
  apiGroup: ""
```

This `Role` gives access to the `Secret: database-secret` in the `Namespace: database`. The `RoleBinding` links up this permission to the `ServiceAccount: datadog-agent` in the `Namespace: default`. This needs to be manually added to your cluster with respect to your resources deployed.

### Option 3: Creating a custom executable{% #option-3-creating-a-custom-executable %}

To retrieve secrets, the Agent uses an external executable that you provide. The executable is used when new secrets are discovered and are cached for the lifecycle of the Agent. If you need to update or rotate a secret, you must restart the Agent to reload it.

This allow you to use any secret management solution and gives you full control on how the Agent accesses secrets.

The Agent sends to this executable a JSON payload over standard input containing a list of secret handles to resolve. Then, your executable fetches each secret and return them in a JSON format through a standard output.

The following example shows what the Agent sends to your executable on STDIN:

```
{
  "version": "1.0",
  "secrets": ["secret1", "secret2"]
}
```

- `version` (string): The format version.
- `secrets` (list of strings): Each string is a handle for a secret to fetch.

The executable responds through the following STDOUT output:

```
{
  "secret1": {"value": "decrypted_value", "error": null},
  "secret2": {"value": null, "error": "could not fetch the secret"}
}
```

- `value` (string): The secret value to be used in the configurations. This can be `null` in the case of an error.
- `error` (string): An error message or `null`.

If a secret fails to be resolved (either by returning a non-zero exit code or a non-null error), the related configuration is ignored by the Agent.

**Never output sensitive information on `stderr`**. If the binary exits with a different status code than `0`, the Agent logs the standard error output of your executable for troubleshooting.

You can also build your own secret retrieval executable using any language. The only requirement is that it follows the input/output format described previously.

Here is a Go example that returns dummy secrets:

```go
package main

import (
  "encoding/json"
  "fmt"
  "io/ioutil"
  "os"
)

type secretsPayload struct {
  Secrets []string `json:secrets`
  Version int      `json:version`
}

func main() {
  data, err := ioutil.ReadAll(os.Stdin)

  if err != nil {
    fmt.Fprintf(os.Stderr, "Could not read from stdin: %s", err)
    os.Exit(1)
  }
  secrets := secretsPayload{}
  json.Unmarshal(data, &secrets)

  res := map[string]map[string]string{}
  for _, handle := range secrets.Secrets {
    res[handle] = map[string]string{
      "value": "decrypted_" + handle,
    }
  }

  output, err := json.Marshal(res)
  if err != nil {
    fmt.Fprintf(os.Stderr, "could not serialize res: %s", err)
    os.Exit(1)
  }
  fmt.Printf(string(output))
}
```

This transforms your configuration:

```yaml
instances:
  - server: db_prod
    user: ENC[db_prod_user]
    password: ENC[db_prod_password]
```

Into the following in memory:

```yaml
instances:
  - server: db_prod
    user: decrypted_db_prod_user
    password: decrypted_db_prod_password
```

You can configure the Agent to use the binary to resolve secrets by adding the following:

```
secret_backend_command: /path/to/binary
```

## Agent security requirements{% #agent-security-requirements %}

The Agent runs the provided executable as a sub-process. The execution patterns differ on Linux and Windows.

{% tab title="Linux" %}
On Linux, your executable must:

- Belong to the same user running the Agent (`dd-agent` by default, or `root` inside a container).
- Have no rights for `group` or `other`.
- Have at least the **execute** right for the owner.

{% /tab %}

{% tab title="Windows" %}
On Windows, your executable must:

- Have **read** or **execute** for `ddagentuser` (the user used to run the Agent).
- Have no rights for any user or group except for the **Administrators** group, the built-in **Local System** account, or the Agent user context (`ddagentuser` by default).
- Be a valid Win32 application so the Agent can execute it (for example, a PowerShell or Python script doesn't work).

{% /tab %}

**Note**: Your executable shares the same environment variables as the Agent.

## Refreshing secrets at runtime{% #refreshing-secrets-at-runtime %}

Starting in Agent v7.67, you can configure the Agent to refresh resolved secrets without requiring a restart.

Set a refresh interval:

```yaml
secret_refresh_interval: 3600  # refresh every hour
```

Or, trigger a refresh manually:

```shell
datadog-agent secret refresh
```

### API/APP key refresh{% #apiapp-key-refresh %}

API/APP keys pulled as secrets support runtime refresh.

You can enable this by setting `secret_refresh_interval` (in seconds) in `datadog.yaml`:

```yaml
api_key: ENC[<secret_handle>]

secret_refresh_interval: 3600  # refresh every hour
```

By default, the Agent randomizes the initial refresh within the `secret_refresh_interval` window to prevent a fleet of Agents from refreshing simultaneously. The key is resolved at startup, then refreshed once within the first interval and every interval thereafter.

To prevent downtime, invalidate old keys only after your entire fleet has pulled the updated keys. You can track key usage on the [Fleet Management](https://app.datadoghq.com/fleet) page.

You can disable this behavior by setting:

```yaml
secret_refresh_scatter: false
```

### Autodiscovery check secrets refresh{% #autodiscovery-check-secrets-refresh %}

Starting in Agent v7.76, scheduled [Autodiscovery](https://docs.datadoghq.com/agent/kubernetes/integrations/) checks can refresh secrets at runtime if the template uses the `ENC[]` syntax.

```yaml
labels:
  tags.datadoghq.com/redis.env: "prod"
  tags.datadoghq.com/redis.service: "my-redis"
  tags.datadoghq.com/redis.version: "6.0.3"
annotations:
  ad.datadoghq.com/redis.checks: |
    {
      "redisdb": {
        "init_config": {},
        "instances": [
          {
            "host": "%%host%%",
            "port":"6379",
            "password":"ENC[<secret_handle>]"
          }
        ]
      }
    }
```

The Agent can then trigger secrets refresh at either the interval set in `secret_refresh_interval` or manually with `datadog-agent secret refresh`.

### Automatic secrets refresh on API key failure / invalidation{% #automatic-secrets-refresh-on-api-key-failure--invalidation %}

Starting in Agent version v7.74, the Agent can automatically refresh secrets when it detects an invalid API key. This happens when the Agent receives a 403 Forbidden response from Datadog or when the periodic health check detects an invalid or expired API key.

To enable this feature, set `secret_refresh_on_api_key_failure_interval` to an interval in minutes in your `datadog.yaml` file. Set to `0` to disable (default).

This interval is the minimum amount of time between 2 refreshes to avoid spamming your secrets management solution when an invalid API key is detected.

```yaml
api_key: ENC[<secret_handle>]

secret_refresh_on_api_key_failure_interval: 10
```

This setting is compatible with `secret_refresh_interval`.

### Enabling DDOT collector refresh{% #enabling-ddot-collector-refresh %}

If you are using [DDOT collector](https://docs.datadoghq.com/opentelemetry/setup/ddot_collector/) and want to enable API/APP refresh you must add the following additional configuration to your `datadog.yaml` file:

```
agent_ipc:
  port: 5051
  config_refresh_interval: 3600
```

This ensures the DDOT collector remains in-sync with the Agent after secrets are refreshed. Similar to how the Agent periodically verifies its configuration state, the DDOT collector uses this setting to regularly check for updated values from the Agent.

## Troubleshooting{% #troubleshooting %}

### Listing detected secrets{% #listing-detected-secrets %}

The `secret` command in the Agent CLI shows any errors related to your setup. For example, if the rights on the executable are incorrect. It also lists all handles found, and where they are located.

On Linux, the command outputs file mode, owner and group for the executable. On Windows, ACL rights are listed.

{% tab title="Linux" %}
Example on Linux:

```sh
datadog-agent secret
=== Checking executable rights ===
Executable path: /path/to/you/executable
Check Rights: OK, the executable has the correct rights

Rights Detail:
file mode: 100700
Owner username: dd-agent
Group name: dd-agent

=== Secrets stats ===
Number of secrets decrypted: 3
Secrets handle decrypted:
- api_key: from datadog.yaml
- db_prod_user: from postgres.yaml
- db_prod_password: from postgres.yaml
```

{% /tab %}

{% tab title="Windows" %}
Example on Windows (from an Administrator PowerShell):

```powershell
PS C:\> & "$env:ProgramFiles\Datadog\Datadog Agent\bin\agent.exe" secret
=== Checking executable rights ===
Executable path: C:\path\to\you\executable.exe
Check Rights: OK, the executable has the correct rights

Rights Detail:
Acl list:
stdout:

Path   : Microsoft.PowerShell.Core\FileSystem::C:\path\to\you\executable.exe
Owner  : BUILTIN\Administrators
Group  : WIN-ITODMBAT8RG\None
Access : NT AUTHORITY\SYSTEM Allow  FullControl
         BUILTIN\Administrators Allow  FullControl
         WIN-ITODMBAT8RG\ddagentuser Allow  ReadAndExecute, Synchronize
Audit  :
Sddl   : O:BAG:S-1-5-21-2685101404-2783901971-939297808-513D:PAI(A;;FA;;;SY)(A;;FA;;;BA)(A;;0x1200
         a9;;;S-1-5-21-2685101404-2783901971-939297808-1001)

=== Secrets stats ===
Number of secrets decrypted: 3
Secrets handle decrypted:
- api_key: from datadog.yaml
- db_prod_user: from sqlserver.yaml
- db_prod_password: from sqlserver.yaml
```

{% /tab %}

### Seeing configurations after secrets were injected{% #seeing-configurations-after-secrets-were-injected %}

To quickly see how the check's configurations are resolved, you can use the `configcheck` command:

```shell
sudo -u dd-agent -- datadog-agent configcheck

=== a check ===
Source: File Configuration Provider
Instance 1:
host: <decrypted_host>
port: <decrypted_port>
password: <obfuscated_password>
~
===

=== another check ===
Source: File Configuration Provider
Instance 1:
host: <decrypted_host2>
port: <decrypted_port2>
password: <obfuscated_password2>
~
===
```

**Note**: The Agent needs to be [restarted](https://docs.datadoghq.com/agent/configuration/agent-commands/#restart-the-agent) to pick up changes on configuration files.

### Debugging your secret_backend_command{% #debugging-your-secret_backend_command %}

To test or debug outside of the Agent, you can mimic how the Agent runs it:

{% tab title="Linux" %}
**Linux**

```bash
sudo -u dd-agent bash -c "echo '{\"version\": \"1.0\", \"secrets\": [\"secret1\", \"secret2\"]}' | /path/to/the/secret_backend_command"
```

The `dd-agent` user is created when you install the Datadog Agent.
{% /tab %}

{% tab title="Windows" %}
##### Rights-related errors{% #rights-related-errors %}

The following errors indicate that something is missing in your setup.

1. If any other group or user than needed has rights on the executable, a similar error to the following is logged:

   ```
   error while decrypting secrets in an instance: Invalid executable 'C:\decrypt.exe': other users/groups than LOCAL_SYSTEM, Administrators or ddagentuser have rights on it
   ```

1. If `ddagentuser` doesn't have read and execute right on the file, a similar error logged:

   ```
   error while decrypting secrets in an instance: could not query ACLs for C:\decrypt.exe
   ```

1. Your executable needs to be a valid Win32 application. If not, the following error is logged:

   ```
   error while running 'C:\decrypt.py': fork/exec C:\decrypt.py: %1 is not a valid Win32 application.
   ```

Datadog has a [Powershell script](https://github.com/DataDog/datadog-agent/blob/master/docs/public/secrets/Set-SecretPermissions.ps1) to help you set the correct permission on your executable. Example on how to use it:

```powershell
.\Set-SecretPermissions.ps1 -SecretBinaryPath C:\secrets\decrypt_secrets.exe
ddagentuser SID: S-1-5-21-3139760116-144564943-2741514060-1076
=== Checking executable permissions ===
Executable path: C:\secrets\decrypt_secrets.exe
Executable permissions: OK, the executable has the correct permissions

Permissions Detail:

stdout:
Path   : Microsoft.PowerShell.Core\FileSystem::C:\secrets\decrypt_secrets.exe
Owner  : BUILTIN\Administrators
Group  : BUILTIN\Administrators
Access : NT AUTHORITY\SYSTEM Allow  FullControl
         BUILTIN\Administrators Allow  FullControl
         DESKTOP-V03BB2P\ddagentuser Allow  ReadAndExecute, Synchronize
Audit  :
Sddl   : O:BAG:BAD:PAI(A;;FA;;;SY)(A;;FA;;;BA)(A;;0x1200a9;;;S-1-5-21-3139760116-144564943-2741514
         060-1076)
stderr:


=== Secrets stats ===
Number of secrets resolved: 0
Secrets handle resolved:
```

##### Testing your executable{% #testing-your-executable %}

Your executable is executed by the Agent when fetching your secrets. The Datadog Agent runs using the `ddagentuser`. This user has no specific rights, but it is part of the `Performance Monitor Users` group. The password for this user is randomly generated at install time and is never saved anywhere.

This means that your executable might work with your default user or development userâbut not when it's run by the Agent, since `ddagentuser` has more restricted rights.

To test your executable in the same conditions as the Agent, update the password of the `ddagentuser` on your dev box. This way, you can authenticate as `ddagentuser` and run your executable in the same context the Agent would.

To do so, follow those steps:

1. Remove `ddagentuser` from the `Local Policies/User Rights Assignement/Deny Log on locally` list in the `Local Security Policy`.
1. Set a new password for `ddagentuser` (since the one generated at install time is never saved anywhere). In PowerShell, run:
   ```powershell
   $user = [ADSI]"WinNT://./ddagentuser";
   $user.SetPassword("a_new_password")
   ```
1. Update the password to be used by `DatadogAgent` service in the Service Control Manager. In PowerShell, run:
   ```powershell
   sc.exe config DatadogAgent password= "a_new_password"
   ```

You can now login as `ddagentuser` to test your executable. Datadog has a [Powershell script](https://github.com/DataDog/datadog-agent/blob/master/docs/public/secrets/secrets_tester.ps1) to help you test your executable as another user. It switches user contexts and mimics how the Agent runs your executable.

Example on how to use it:

```powershell
.\secrets_tester.ps1 -user ddagentuser -password a_new_password -executable C:\path\to\your\executable.exe -payload '{"version": "1.0", "secrets": ["secret_ID_1", "secret_ID_2"]}'
Creating new Process with C:\path\to\your\executable.exe
Waiting a second for the process to be up and running
Writing the payload to Stdin
Waiting a second so the process can fetch the secrets
stdout:
{"secret_ID_1":{"value":"secret1"},"secret_ID_2":{"value":"secret2"}}
stderr: None
exit code:
0
```

{% /tab %}

### Agent refusing to start{% #agent-refusing-to-start %}

The first thing the Agent does on startup is to load `datadog.yaml` and decrypt any secrets in it. This is done before setting up the logging. This means that on platforms like Windows, errors occurring when loading `datadog.yaml` aren't written in the logs, but on `stderr`. This can occur when the executable given to the Agent for secrets returns an error.

If you have secrets in `datadog.yaml` and the Agent refuses to start:

- Try to start the Agent manually to be able to see `stderr`.
- Remove the secrets from `datadog.yaml` and test with secrets in a check configuration file first.

### Testing Kubernetes Permissions{% #testing-kubernetes-permissions %}

When reading Secrets directly from Kubernetes you can double check your permissions with the `kubectl auth` command. The general form of this is:

```
kubectl auth can-i get secret/<SECRET_NAME> -n <SECRET_NAMESPACE> --as system:serviceaccount:<AGENT_NAMESPACE>:<AGENT_SERVICE_ACCOUNT>
```

Consider the previous Kubernetes Secrets example, where the Secret `Secret:database-secret` exists in the `Namespace: database`, and the Service Account `ServiceAccount:datadog-agent` exists in the `Namespace: default`.

In this case, use the following command:

```
kubectl auth can-i get secret/database-secret -n database --as system:serviceaccount:default:datadog-agent
```

This command returns whether the permissions are valid for the Agent to view this Secret.

### Remove trailing line breaks{% #remove-trailing-line-breaks %}

Some secret management tools automatically add a line break when exporting secrets through files. You can remove these line breaks by setting `secret_backend_remove_trailing_line_break: true` in [the datadog.yaml configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/), or use the environment variable `DD_SECRET_BACKEND_REMOVE_TRAILING_LINE_BREAK` to do the same, especially in containerized environments.

### Autodiscovery variables in secret handles{% #autodiscovery-variables-in-secret-handles %}

It is also possible to use [Autodiscovery](https://docs.datadoghq.com/agent/kubernetes/integrations/) variables in secret handles. The Agent resolves these variables before resolving the secret. For example:

```
instances:
  - server: %%host%%
    user: ENC[db_prod_user_%%host%%]
    password: ENC[db_prod_password_%%host%%]
```

## Further Reading{% #further-reading %}

- [Autodiscovery](https://docs.datadoghq.com/agent/autodiscovery/)
