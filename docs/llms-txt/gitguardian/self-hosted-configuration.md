# Source: https://docs.gitguardian.com/ggscout-docs/self-hosted-configuration.md

# ggscout for self-hosted installations

> Explains how to deploy and configure ggscout alongside a GitGuardian self-hosted instance using the provided Helm chart.

The GitGuardian Self-Hosted deployment comes with a ready-to-use Helm chart that you can use to deploy ggscout alongside your Self-Hosted instance. The following procedure will help you deploy and configure ggscout.

:::success **No secrets get out of your environment!**

Secrets values will never leave your environment in clear!

Secrets values are hashed using the [HMSL hashing algorithm](https://blog.gitguardian.com/hasmysecretleaked-building-a-trustless-and-secure-protocol/) before they are sent to your GitGuardian self-hosted instance.
Other non-sensitive metadata like the secret names, paths in the vault, creation date, lease time, etc... are also collected to help you in the remediation process.

Find **[instructions on how to run ggscout in audit mode](./what-is-ggscout#keep-full-authority-on-ggscout-execution)** to review what is sent to GitGuardian.
:::

ggscout also works in Airgap mode. Follow the [Airgap documentation](../self-hosting/installation/airgap-installation-existing-cluster-helm) to ensure all necessary images are available in your private registry.

### Helm-based installation

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/hjCNFY0ksM0?controls=0&loop=1" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; fullscreen; encrypted-media; gyroscope; picture-in-picture; web-share; loop" allowFullScreen></iframe>

1. Create a Service Account Token in GitGuardian

    Navigate to **Settings > Service accounts** and generate a token with NHI permissions.
    ![Scout SAT](/img/ggscout/scout-sat.png)

2. Create a kubernetes secret to store the GitGuardian SAT and your sources authentication token (e.g. Hashicorp Vault token, ... )

    To create or update the secrets, you directly use Kubernetes Secrets API.
    Create `secrets.yaml` with the following content (replacing the values with your secrets):

    ```yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: gitguardian-ggscout-secrets
    stringData:
        GITGUARDIAN_API_KEY: "my_gitguardian_api_key"
        HASHICORP_VAULT_TOKEN: "my_vault_token"
    ```

    To apply the secrets to your cluster/namespace, run the following command:
     `kubectl apply -f secrets.yaml -n <namespace>`

3. Configure ggscout in Self-Hosted helm value file

   ggscout is a sub chart of GitGuardian Self-Hosted chart. All the configuration for ggscout happens under `ggscout`. Follow documentation on [https://github.com/GitGuardian/ggscout-helm-charts](https://github.com/GitGuardian/ggscout-helm-charts/tree/main/charts/ggscout/examples).

   The GitGuardian endpoint is automatically computed based on your current instance but you can run it in a different namespace and specify the GitGuardian endpoint. Update your Helm value file with the following configuration steps:

    Use the [examples provided in the Scout GitHub repository](https://github.com/GitGuardian/ggscout-helm-charts/tree/main/charts/ggscout/examples).

    If you deploy over an OpenShift cluster, check [OpenShift installation](../self-hosting/installation/openshift).

    Example with Hashicorp Vault:

    ```yaml
    ggscout:
      enabled: true # to activate the ggscout sub-chart
      inventory:
        config:
          sources:
            hashicorpvault: # example of Hashicorp vault secrets collector
              type: hashicorpvault
              vault_address: https://vault.example.com # Replace with the actual Vault address
              auth:
                auth_mode: "token"
                token: "${HASHICORP_VAULT_TOKEN}"
              fetch_all_versions: false # Fetch all versions of secrets or not
          gitguardian: # Pushes the inventory to the GitGuardian workspace. If the endpoint is empty, it will not push the inventory details.
            endpoint: 'https://<GitGuardian-url>/exposed/v1' # optional; if not specified, the current self-hosted GitGuardian instance URL will be used
            api_token: "${GITGUARDIAN_API_KEY}"
        jobs:
          # Job to fetch defined sources
          fetch:
            enabled: true
            schedule: '*/15 * * * *'
            send: true # send hashed secrets to GitGuardian
          # Job to be able to sync/write secrets from GitGuardian into you vault
          sync:
            enabled: true
            schedule: '* * * * *'
      envFrom:
      - secretRef:
          name: gitguardian-ggscout-secrets
    ```

4. Use the `helm upgrade` command and specify the same version as the one currently installed to prevent unwanted upgrades to the latest version.

    To find the release name and the version currently installed, use `helm ls`:

    ```bash
    helm ls
    NAME             UPDATED             STATUS  	CHART                	APP VERSION
    <release-name>   2025-03-20 12:40    deployed	gitguardian-2025.3.0	2025.3.0
    ```

    Here, the version installed is `2025.3.0`. To install ggscout, you would run the following command, using the version installed in your environment:

    ```bash
    helm upgrade <release-name> -n <namespace> oci://registry.replicated.com/gitguardian/gitguardian --version 2025.3.0 -f local-values.yaml
    ```

    Replace `<release-name>` with the name used during the initial installation. If needed, specify the Kubernetes namespace with `-n` (the default namespace is used if not specified).

### KOTS-based installation

1. Create a Service Account Token in GitGuardian

    Navigate to **Settings > Service accounts** and generate a token with NHI permissions.
    ![Scout SAT](/img/ggscout/scout-sat.png)

2. Enable and configure ggscout in the [KOTS Admin Console](../self-hosting/management/infrastructure-management/admin-console).

    Currently, the only available source is HashiCorp Vault. If you'd like to configure other [sources](https://github.com/GitGuardian/ggscout-helm-charts/tree/main/charts/ggscout/examples), please contact support@gitguardian.com.

    ![Scout KOTS Configuration](/img/ggscout/scout-kots-config.png)
