# Source: https://docs.envzero.com/guides/admin-guide/self-hosted-kubernetes-agent/custom-optional-configuration.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom/Optional Configuration

> Helm values reference for configuring your env zero self-hosted Kubernetes agent

A Helm `values.yml` will be provided by env zero with the configuration env zero provides.\
The customer will need to provide a `values.customer.yml` with the following values (optional), to enable specific features:

## Image & container configuration

### `dockerImage` / `agentImagePullSecret`

* **Description:** Custom Docker image URI and Base64 encoded `.dockerconfigjson` contents
* **Required for feature:** Custom Docker image. See [Using a custom image in an agent](/guides/admin-guide/self-hosted-kubernetes-agent/using-a-custom-image-in-an-agent)
* **Can be provided via a Kubernetes Secret?** No

### `agentImagePullSecretRef`

* **Description:** A reference to a k8s secret name that holds a Docker pull image token
* **Required for feature:** Custom Docker image that is hosted on a private Docker registry
* **Can be provided via a Kubernetes Secret?** No

## Cost estimation & AWS deployment credentials

### `infracostApiKeyEncoded`

* **Description:** Base64 encoded Infracost API key
* **Required for feature:** Cost Estimation
* **Can be provided via a Kubernetes Secret?** Yes:<br />`INFRACOST_API_KEY`

### `assumerKeyIdEncoded` / `assumerSecretEncoded`

* **Description:** Base64 encoded AWS Access Key ID & Secret
* **Required for feature:** AWS Assume role for deploy credentials. Also, see [Authenticating the agent on AWS EKS](/guides/admin-guide/self-hosted-kubernetes-agent/authenticating-the-agent-on-aws-eks)
* **Can be provided via a Kubernetes Secret?** Yes:<br />`ASSUMER_ACCESS_KEY_ID`<br />`ASSUMER_SECRET_ACCESS_KEY`

## Resources & pod scheduling

### `limits.cpu` / `limits.memory`

* **Description:** Container resource limits<br />[Read more about resource allocation](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)<br />Recommended `cpu: 1.5` and `memory: 3Gi`
* **Required for feature:** Custom deployment pod size
* **Can be provided via a Kubernetes Secret?** No

### `requests.cpu` / `requests.memory`

* **Description:** Container resource requests. Recommended `cpu: 1.5` and `memory: 3Gi`
* **Required for feature:** Custom deployment container resources
* **Can be provided via a Kubernetes Secret?** No

### `tolerations`

* **Description:** An array of `toleration` objects to apply to all pods. see [docs](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)
* **Required for feature:** Custom tolerations
* **Can be provided via a Kubernetes Secret?** No

### `deploymentTolerations`

* **Description:** An array of `toleration`objects - targeting the deployment pods. This will override the default `tolerations` for deployment pods.
* **Required for feature:** Custom tolerations
* **Can be provided via a Kubernetes Secret?** No

### `affinity`

* **Description:** Allows you to constrain which nodes env zero pods are eligible to be scheduled on. see [docs](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
* **Required for feature:** Custom node affinity
* **Can be provided via a Kubernetes Secret?** No

### `deploymentAffinity`

* **Description:** Affinity for deployment pods. This will override the default `affinity` for deployment pods.
* **Required for feature:** Custom node affinity
* **Can be provided via a Kubernetes Secret?** No

## Cloud secret managers

### `customerAwsAccessKeyIdEncoded` / `customerAwsSecretAccessKeyEncoded` / `awsSecretsRegion`

* **Description:** Base64 encoded AWS Access Key ID & Secret. Requires the `secretsmanager:GetSecretValue` permission
* **Required for feature:** Using AWS Secrets Manager to store secrets for the agent
* **Can be provided via a Kubernetes Secret?** Yes:<br />`CUSTOMER_AWS_ACCESS_KEY_ID`<br />`CUSTOMER_AWS_SECRET_ACCESS_KEY`

### `customerGoogleProject` / `customerGoogleCredentials`

* **Description:** Base64 encoded GCP project name and JSON service-key contents. Requires the `Secret Manager Secret Access` role.
* **Required for feature:** Using GCP Secret Manager to store secrets for the agent. These credentials are not used for the deployment itself. If `deploymentJobServiceAccountName` is set - Workload identity will override any supplied credentials.
* **Can be provided via a Kubernetes Secret?** Yes:<br />`CUSTOMER_GOOGLE_PROJECT`<br />`CUSTOMER_GOOGLE_CREDENTIALS`

### `customerAzureClientId` / `customerAzureClientSecret` / `customerAzureTenantId`

* **Description:** Base64 encoded Azure Credentials.
* **Required for feature:** Using Azure Key Vault Secrets to store secrets for the agent
* **Can be provided via a Kubernetes Secret?** Yes:<br />`CUSTOMER_AZURE_CLIENT_ID`<br />`CUSTOMER_AZURE_CLIENT_SECRET`<br />`CUSTOMER_AZURE_TENANT_ID`

### `customerOracleCredentials.tenancyOCIDEncoded` / `customerOracleCredentials.userOCIDEncoded` / `customerOracleCredentials.apiKeyFingerprintEncoded` / `customerOracleCredentials.apiKeyPrivateKeyEncoded` / `customerOracleCredentials.secretsRegion`

* **Description:** OCI credentials.<br />All should be defined separately within the same object - `customerOracleCredentials`.<br />Any field that ends with `Encoded` should be Base64 encoded.
* **Required for feature:** Using OCI Vault to store secrets for the agent. These credentials are not used for the deployment itself.
* **Can be provided via a Kubernetes Secret?** Yes:<br />`CUSTOMER_ORACLE_TENANCY_OCID`<br />`CUSTOMER_ORACLE_USER_OCID`<br />`CUSTOMER_ORACLE_API_KEY_FINGERPRINT`<br />`CUSTOMER_ORACLE_API_KEY_PRIVATE_KEY`<br />`ORACLE_SECRETS_REGION`

## HashiCorp Vault

### `customerVaultTokenEncoded` / `customerVaultUrl`

* **Description:** **(Deprecated)** Base64 encoded HCP Vault token, and the Vault's URL (also base64 encoded)
* **Required for feature:** Using HCP Vault to store secrets for the agent
* **Can be provided via a Kubernetes Secret?** Yes:<br />`CUSTOMER_VAULT_TOKEN`<br />`CUSTOMER_VAULT_ADDRESS`

### `vault`

* **Description:** Set HCP Vault authentication.<br />First, set the cluster's URL:<br />`address:` (equivalent to VAULT\_ADDR)<br />`loginPath: "<LoginCustomPath>"` - (Optional)<br />Then, you should choose one of the following login method:<br />- [By Vault token](https://developer.hashicorp.com/vault/docs/auth/token)<br /> `method: "token"`<br /> `encodedToken: "<vault-token>"`<br />- [By Username & Password](https://developer.hashicorp.com/vault/docs/auth/userpass)<br /> `method: "password"`<br /> `username: "<username>"`<br /> `encodedPassword: "<base64Encoded password>"`<br />- [By Certificate](https://developer.hashicorp.com/vault/docs/auth/cert)<br /> `method: "certificate"`<br /> `role: "<certificate name>"`<br /> `clientCertificateSecretName: "<secret-name>"`<br /> \*\* The secret must created in the same namespace with specify keys (client-cert, client-key) for example: `kubectl create secret generic <secret-name> -n env0-agent --from-file=client-key=client.key --from-file=client-cert=client.crt`<br /> `passphraseSecretName: "<secret-name>"` (Optional)<br /> \*\* The secret must created in the same namespace with specify keys (client-cert, client-key) for example: `kubectl create secret generic <secret-name> -n env0-agent --from-literal=passphrase=my-password`<br /> \*\* For Certification Authority (CA) you can choose between:<br /> ^ `caDisable: true`<br /> ^ `caCertificateSecretName: "<secret-name>"`with the key - `ca-cert`<br /> ^ Using CA certificate with `customCertificates`<br />- [By Role & Service Account Token(JWT)](https://developer.hashicorp.com/vault/docs/auth/jwt/oidc-providers/kubernetes)<br /> `method: "service_account"`<br /> `role: "<vault role name>"`<br /> \*\* The JWT is supposed to be supplied by kubernetes in the following path:<br /> `/var/run/secrets/kubernetes.io/serviceaccount/token`<br /> You can read more about service accounts [here](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/). Communication is based on v1 [HTTP API](https://developer.hashicorp.com/vault/api-docs/v1.15.x)
* **Required for feature:** Using HCP Vault to store secrets for the agent
* **Can be provided via a Kubernetes Secret?** No

## VCS & Git configuration

### `bitbucketServerCredentialsEncoded`

* **Description:** Base64 Bitbucket server credentials in the format \`username:token ([using a Personal Access token](https://confluence.atlassian.com/bitbucketserver076/personal-access-tokens-1026534797.html#Personalaccesstokens-usingpersonalaccesstokens))
* **Required for feature:** On-premise Bitbucket Server installation
* **Can be provided via a Kubernetes Secret?** Yes:<br />`BITBUCKET_SERVER_CREDENTIALS`

### `gitlabEnterpriseCredentialsEncoded`

* **Description:** Base64 Gitlab Enterprise credentials in the form of a [Personal Access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token)
* **Required for feature:** On-premise Gitlab Enterprise installation
* **Can be provided via a Kubernetes Secret?** Yes:<br />`GITLAB_ENTERPRISE_CREDENTIALS`

### `gitlabEnterpriseBaseUrlSuffix`

* **Description:** In cases where your GitLab instance base url is not at the root of the url, URL but on a separate path, e.g.,`https://gitlab.acme.com/prod` you should define that added suffix to this value<br />`gitlabEnterpriseBaseUrlSuffix=prod`
* **Required for feature:** On-premise Gitlab Enterprise installation
* **Can be provided via a Kubernetes Secret?** No

### `githubEnterpriseAppId` / `githubEnterpriseAppInstallationId` / `githubEnterpriseAppPrivateKeyEncoded`

* **Description:** [GitHub Enterprise Integration](/guides/admin-guide/templates/github-enterprise-integration) (see step 3)
* **Required for feature:** On-premise GitHub Enterprise installation
* **Can be provided via a Kubernetes Secret?** Yes:<br />`GITHUB_ENTERPRISE_APP_PRIVATE_KEY`

### `allowedVcsUrlRegex`

* **Description:** When set, cloning a git repository will only be permitted if the git url matches the regular expression set.
* **Required for feature:** VCS URL Whitelisting
* **Can be provided via a Kubernetes Secret?** No

## Certificates & TLS

### `customCertificates`

* **Description:** An array of strings. Each represents a name of Kubernetes secret that contains custom CA certificates. Those certificates will be available during deployments.
* **Required for feature:** Custom CA Certificates. More details [here](/guides/admin-guide/self-hosted-kubernetes-agent/custom-ca-certificates)
* **Can be provided via a Kubernetes Secret?** No

### `gitSslNoVerify`

* **Description:** When set to `true`, cloning a git repo will not verify SSL/TLS certs
* **Required for feature:** Ignoring SSL/TLS certs for on-premise git servers
* **Can be provided via a Kubernetes Secret?** No

## Storage & state configuration

### `storageClassName`

* **Description:** Ability to change the default PVC storage class name for env zero self-hosted agent
* **Required for feature:** the default is`env0-state-sc`<br />Please note: When changing this you should also change your [storage class](/guides/admin-guide/self-hosted-kubernetes-agent/#persistent-volumestorage-class-optional) name to match this configuration
* **Can be provided via a Kubernetes Secret?** No

## Agent behavior & security

### `deploymentJobServiceAccountName`

* **Description:** Customize the Kubernetes service account used by the deployment pod. Primarily for pod-level IAM permissions
* **Required for feature:** the default is `default`
* **Can be provided via a Kubernetes Secret?** No

### `jobHistoryLimitFailure` / `jobHistoryLimitSuccess`

* **Description:** The number of successful and failed deployment jobs should be kept in the Kubernetes cluster history
* **Required for feature:** The default is 10 for each value
* **Can be provided via a Kubernetes Secret?** No

### `strictSecurityContext`

* **Description:** When set to `true`, the pod operates under `node` user instead of `root`
* **Required for feature:** Increased agent pod security
* **Can be provided via a Kubernetes Secret?** No

### `env0StateEncryptionKey`

* **Description:** A base64 encoded string (password). When set, deployment state and working directory will be encrypted and persisted on env zero's end
* **Required for feature:** [env zero-Hosted Encrypted State](/guides/admin-guide/self-hosted-kubernetes-agent/env0-hosted-encrypted-state)
* **Can be provided via a Kubernetes Secret?** Yes:<br />`ENV0_STATE_ENCRYPTION_KEY`

### `environmentOutputEncryptionKey`

* **Description:** A base64 encoded string (password). Used to enable the ["Environment Outputs"](/guides/admin-guide/variables/environment-outputs) feature
* **Required for feature:** See notes in [Environment Outputs](/guides/admin-guide/variables/environment-outputs)
* **Can be provided via a Kubernetes Secret?** No

## Logging

### `logger`

* **Description:** Logger config<br />`level` - **debug**/info/warn/error<br />`format` - **json**/cli

### `agentImagePullPolicy`

* **Description:** Set `imagePullPolicy` attribute - **Always**/Never/IfNotPresent

### `agentProxy`

* **Description:** Agent's Proxy pod config:<br />`install` - **true**/false<br />`replicas` - how many replicas of the agent proxy to use. Default is **1**<br />`maxConcurrentRequests` - how many concurrent requests each pod should handle. Default is **500**<br />`limits` - k8s (cpu and memory) limits. Default is **250m** and **500Mi**

### `deploymentPodWarmPoolSize`

* **Description:** A number of deployment pods that should be left "warm" (running & idle) and ready for new deployments

## Environment variables, labels & secrets

### `podAdditionalEnvVars`

* **Description:** Additional Environment variables to be passed to the deployment pods, which will also be passed to the deployment process. These are set as a plain yaml object, i.e.:<br />`"podAdditionalEnvVars":`<br />`"MY_SECRET": akeyless:/K8s/my_k8s_secret"`

### `podAdditionalLabels`

* **Description:** Additional labels to be set on deployment pods. Those are set as a plain yaml object, i.e.:<br />`"podAdditionalLabels":`<br />`"mykey": "myvalue"`

### `podAdditionalAnnotations`

* **Description:** Additional annotations to be set on deployment pods. These are set as a plain yaml object, i.e.:<br />`"podAdditionalAnnotations":`<br />`"mykey": "myvalue"`

### `agentAdditionalEnvVars`

* **Description:** Additional Environment variables to be passed to the agent pods, which will also be passed to the agent proxy / trigger. These are set as a plain yaml object, i.e.:<br />`"agentAdditionalEnvVars":`<br />`"MY_ENV": "MY_VALUE"`

### `agentAdditionalLabels`

* **Description:** Additional annotations to be set on agent (trigger/proxy) pods. These are set as a plain yaml object, i.e.:<br />`"agentAdditionalLabels":`<br />`"mykey": "myvalue"`

### `agentAdditionalAnnotations`

* **Description:** Additional annotations to be set on agent (trigger/proxy) pods. Those are set plain yaml object i.e:<br />`"agentAdditionalAnnotations":`<br />`"mykey": "myvalue"`

### `customSecrets`

* **Description:** `customSecrets:`<br />`- envVarName: MY_SECRET`<br />`secretName: my-secrets-1`<br />`key: db_password`
* **Required for feature:** Mount custom secrets
* **Can be provided via a Kubernetes Secret?** No

### `customSecretMounts`

* **Description:** `customSecretMounts:`<br />`- volumeName: my-secrets-1`<br />`secretName: my-secrets-1`<br />`mountPath: /opt/secret1`
* **Required for feature:** Mount secret files to given a mountPath
* **Can be provided via a Kubernetes Secret?** No

### `env0ConfigSecretName`

* **Description:** A Kubernetes Secret name. Can be used to provide sensitive values listed in this table, instead of providing them in the Helm values files.

### `customRoleForOidcAwsSsm.duration` / `customRoleForOidcAwsSsm.arn`

* **Description:** Custom role for AWS SSM secret fetching, Note: only used when useOidcForAwsSsm=true

### `useOidcForAwsSsm`

* **Description:** When set to`true` the agent will be instructed to authenticate to AWS SSM using env zero OIDC.

## Network & proxy configuration

### `httpProxy` / `httpsProxy` / `noProxy`

* **Description:** Using Internal Proxy for communication with env zero or your self hosted VCS<br />For enable proxy for `http` /`https`requests use<br />`httpProxy: "http://my-http-proxy-address"`<br />`httpsProxy: "https://my-https-proxy-address"`<br />If you want to exclude url from using the proxy use<br />`noProxy: "https://env0.com,https://my-other-vcs"`

## Other advanced configuration

### `env0BlockDestroyAndTaskCommands`

* **Description:** If set to "true", this agent will throw an error when any user tries to destroy any environment or run a custom "task" in it

### `additionalPodConfig`

* **Description:** Additional configurations to be merged with the spec of deployment pods. Can be used to add hostAliases, dnsConfig, etc.<br />Example:<br />`additionalPodConfig:`<br />`hostAliases:`<br />`- ip: "192.168.1.100"`<br />`hostnames:`<br />`- "example.internal"`<br />`- "example.test"`<br />`dnsConfig:`<br />`nameservers:`<br />`- 1.1.1.1`<br />`- 8.8.8.8`

### `additionalAgentConfig`

* **Description:** Additional configurations to be merged with the spec of agent (trigger/proxy) pods. Can be used to add `hostAliases`, `dnsConfig`, etc.<br />Example:<br />`additionalAgentConfig:`<br />`hostAliases:`<br />`- ip: "192.168.1.100"`<br />`hostnames:`<br />`- "example.internal"`<br />`- "example.test"`<br />`dnsConfig:`<br />`nameservers:`<br />`- 1.1.1.1`<br />`- 8.8.8.8`

<Info>
  **Base64 Encoding Values**

  To ensure no additional new line characters are being encoded, please use the following command in your terminal:

  ```bash  theme={null}
  echo -n $VALUE | base64
  ```

</Info>

<Info>
  **Storing Secret Values as Kubernetes Secret**

  Some of the configuration values listed [above](/guides/admin-guide/self-hosted-kubernetes-agent/custom-optional-configuration) are sensitive.

  As an alternative to setting them in your `values.customer.yml`, you can provide sensitive keys and values from your own Kubernetes Secret prior to the agent's installation/upgrade.

  Setting the `env0ConfigSecretName` will instruct the agent to extract the needed values from the given Kubernetes Secret and will override values from the Helm value files.

  The Kubernetes Secret must be accessible from the agent, and sensitive values must be Base64 encoded.
</Info>

Built with [Mintlify](https://mintlify.com).
