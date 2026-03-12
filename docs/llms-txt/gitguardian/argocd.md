# Source: https://docs.gitguardian.com/self-hosting/installation/argocd.md

# Install using Argo CD

> Install GitGuardian self-hosted on an existing Kubernetes cluster using ArgoCD for GitOps-based deployment.

## Introduction

Using the GitGuardian Helm repository, you can easily install GitGuardian on your existing Kubernetes cluster with [Argo CD](https://argo-cd.readthedocs.io/en/stable/).

:::caution Requirements
Before starting the installation, ensure to review the **[system](../system-requirements)** and **[network](../network-requirements)** requirements.
:::

## Add GitGuardian Helm repository

First, you need to add the GitGuardian Helm repository to Argo CD using the following settings:

```yaml
name: gitguardian
type: helm
enableOCI: 'true'
url: registry.replicated.com/gitguardian
username: <your.name@yourcompany.com>
password: <your.password>
```

The GitGuardian team will provide you the username and the password.

You can follow the [official documentation](https://argo-cd.readthedocs.io/en/stable/user-guide/private-repositories/) and choose from the following methods:

1. [Declarative setup](https://argo-cd.readthedocs.io/en/stable/operator-manual/declarative-setup/#repositories)

Create the following Argo CD repository secret using `kubectl`:

You need to set the username and the password before.

```shell
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Secret
metadata:
  name: replicated-repo
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: repository
stringData:
  name: replicated
  type: helm
  enableOCI: "true"
  url: registry.replicated.com
  username: <your.name@yourcompany.com>
  password: <your.password>
EOF
```

2. [Argo CD CLI](https://argo-cd.readthedocs.io/en/stable/cli_installation/)

:::caution Requirements
You must first authenticate on your Argo CD server by using the command: `argocd login <server_url>`
:::

Set your username/password and run this command:

```shell
argocd repo add registry.replicated.com \
  --name replicated \
  --type helm \
  --enable-oci \
  --username <your.name@yourcompany.com> \
  --password <your.password>
```

3. [Argo CD UI](https://argo-cd.readthedocs.io/en/stable/user-guide/private-repositories/#https-username-and-password-credential)

Navigate to `Settings/Repositories` and add the GitGuardian Helm repository:
![UI - add repository](/img/self-hosting/installation/installation_argocd_repository_1.png)

:::caution Requirements
Ensure to enable OCI
:::
![UI - enable OCI](/img/self-hosting/installation/installation_argocd_repository_2.png)

Once added, you should see the GitGuardian Helm repository:
![UI - repository list](/img/self-hosting/installation/installation_argocd_repository_3.png)

The connection status must be `successful`.

## Configure GitGuardian Application

You can configure GitGuardian application by providing custom Helm values, follow the [Helm instructions](./installation-existing-cluster-helm) to proceed.

We highly recommend managing secrets on your own and referencing them via `existingSecret` Helm parameters (See [Helm Secrets Management](./helm-secrets#existing-secret) page). We also suggest visiting the [Argo CD Secret Management page](https://argo-cd.readthedocs.io/en/stable/operator-manual/secret-management/) to efficiently manage your secrets.

## Create encryption secret

When using Argo CD, you must pre-create the application encryption secret before deploying.

Generate a random key and create the secret:

<Tabs>
<TabItem value="linux-macos" label="Linux / macOS" default>

```shell
kubectl create secret generic gitguardian-encryption \
  --namespace <namespace> \
  --from-literal=django-secret-key="$(openssl rand -hex 32)"
```

</TabItem>
<TabItem value="windows-powershell" label="Windows (PowerShell)">

```powershell
$key = -join ((1..32) | ForEach-Object { '{0:x2}' -f (Get-Random -Maximum 256) })
kubectl create secret generic gitguardian-encryption `
  --namespace <namespace> `
  --from-literal=django-secret-key=$key
```

</TabItem>
</Tabs>

Then reference it in your `values.yaml`:

```yaml
miscEncryption:
  existingSecret: 'gitguardian-encryption'
  existingSecretKeys:
    djangoSecretKey: 'django-secret-key'
```

:::tip
This secret is managed outside of Argo CD and will persist across syncs and upgrades.
:::

## Install GitGuardian Application

After creating the Helm value file `values.yaml` following above instructions, you can create the GitGuardian application using Argo CD CLI by running the following command:

```shell
argocd app create gitguardian \
  --dest-server <cluster> \
  --dest-namespace <namespace> \
  --repo registry.replicated.com/gitguardian \
  --helm-chart gitguardian \
  --revision 2025.x.y \
  --values-literal-file values.yaml \
  --self-heal \
  --auto-prune \
  --sync-option PruneLast=true
```

If `autoscaling` is enabled, you must configure the Argo application to ignore changes made to the number of replicas for all deployments:

```shell
argocd app patch gitguardian \
  --patch '{"spec": {"ignoreDifferences": [{"group": "apps", "kind": "Deployment", "jsonPointers": ["/spec/replicas"]}]}}' \
  --type merge
```

:::tip Missing status on MinIO bucket-init job
If the MinIO bucket-init job appears with a **Missing** status in Argo CD, add the following annotations in your `values.yaml` to let Argo CD properly track the job:

```yaml
loki-minio:
  bucketInitJob:
    annotations:
      argocd.argoproj.io/hook: Sync
      argocd.argoproj.io/hook-delete-policy: BeforeHookCreation
```
:::

## Upgrade GitGuardian Application

:::caution
Prior to upgrading, ensure you back up your PostgreSQL database. For detailed instructions, refer to the **[Backup](../management/infrastructure-management/backup.md)** page.
:::

To upgrade GitGuardian, you need first to update the Helm chart version using Argo CD CLI by running the following command:

```shell
argocd app patch gitguardian \
  --patch '{"spec": { "source": { "targetRevision": "2024.x.y" } }}' \
  --type merge
```

Sync the GitGuardian app:

```shell
argocd app sync gitguardian
```
