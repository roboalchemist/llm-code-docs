# Source: https://docs.ox.security/secure-runtime/ox-inspector.md

# OX K8s Inspector

> **Note:** This capability is currently in Early Access (EA) and is not generally available. To request access, please contact OX technical support.

OX K8s Inspector is a lightweight data collection tool that enables secure extraction of Kubernetes cluster data without requiring external access to the Kubernetes API server.

OX K8s Inspector runs as a Kubernetes CronJob inside your cluster, collecting configuration and activity data at regular intervals and securely sending it to the OX platform for analysis.

This solution is designed for environments where the Kubernetes API server is not exposed publicly. The setup adheres to security best practices that minimize the cluster's attack surface.

By operating entirely within the cluster and using outbound communication, K8s Inspector avoids the need for direct access from external systems while still providing full visibility into Kubernetes environments.

## OX Inspector architecture

OX K8s Inspector components:

* **Inspector CronJob:** Runs inside your Kubernetes cluster, collects relevant data, and securely transmits it to OX.
* **OX Backend:** Authenticates the Inspector, handles secure data transfer, and processes the data to produce insights.

OX K8s Inspector data flow:

1. The K8s Inspector CronJob runs inside your Kubernetes cluster as a scheduled task.
2. Using a configured API key, the CronJob authenticates with the OX backend.
3. The CronJob collects relevant data by querying the Kubernetes API server.
4. All collected data is encrypted locally within the cluster.
5. The encrypted data is then securely uploaded to the OX backend.
6. The OX platform analyzes the uploaded data during scans and presents insights in the user interface.

## Installing OX K8s Inspector

To allow K8s Inspector to communicate with the OX platform, you need to create an API key, and then go to your cluster and start the installation. Here are the required installation steps:

1. [Create an API key.](#creating-a-new-api-key)
2. Make sure that the cluster has access to: `api.cloud.ox.security`
3. [Push API keys to Kubernetes secrets.](#pushing-api-keys-to-kubernetes-secrets)
4. [Install OX K8s Inspector with Helm](#installing-ox-inspector-with-helm).
5. [Connect to OX K8s Inspector.](#connecting-to-ox-k8s-inspector)

### Creating a new API key

1. From the left pane of **OX dashboard**, select **Settings > API Key Settings**.
2. In the **API Key Settings** window, select **CREATE API KEY**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-45bc3c861b9afded39a32a23722fbc5fc33b035e%2FK8%20API%20key.png?alt=media" alt="" width="358"><figcaption></figcaption></figure>

1. In the **Create API Key** box, set the following and select **CREATE**:

* **API Key Name:** Add a meaningful name that is easy to identify. It is good practice to include the key's intended purpose in the name.
* **API Key Type:** Select **K8s Inspector Integration**.
* **Expiration Date:** Until when you can use this key.

1. Copy the key that appears and save the key it in a safe location. This is the only time when you can see and copy the actual key.
2. Select **CLOSE**. The new key appears in the **API Key Settings** page.

### Pushing API keys to Kubernetes Secrets

1. To create a Kubernetes secret named `ox-inspector-secret` with your API key, run:

```
kubectl create secret generic ox-inspector-secret --from-literal=api-key=<your-api-key-value>
```

Replace `<your-api-key-value>` with the [API key](#creating-a-new-api-key) you previously generated.

### Installing OX Inspector with Helm

```
helm repo add ox-inspector-repo https://charts.cloud.ox.security 

helm repo update
helm install ox-inspector ox-inspector-repo/ox-inspector \
  --set-string oxInspector.cluster.cloud_provider="<CLOUD_PROVIDER>" \
  --set-string oxInspector.cluster.account_id="<ACCOUNT_ID>" \
  --set-string oxInspector.cluster.region="<REGION>" \
  --set-string oxInspector.cluster.name="<CLUSTER_NAME>"
```

| Placeholder        | Description                                                                                  |
| ------------------ | -------------------------------------------------------------------------------------------- |
| `<CLOUD_PROVIDER>` | Cloud provider where the cluster is running (EKS, GKE, OpenShift, or AKS)                    |
| `<ACCOUNT_ID>`     | Cloud provider account identifier (AWS Account ID, Azure Subscription ID, or GCP Project ID) |
| `<REGION>`         | Cloud provider region where the cluster is deployed (e.g., "us-west-2", "eu-west-1")         |
| `<CLUSTER_NAME>`   | Name of the Kubernetes cluster where OX Inspector will run                                   |

**Additional Values:**

* `oxInspector.cluster.is_on_prem` :Whether you are an OX on-premises customer (true) or OX SaaS customer (false). Default: false
* wheather your an OX SaaS customer or an OX onprem customer
* `oxInspector.schedule` : Cron schedule expression for the Inspector job. Default: "0 12 \* \* " (runs daily at 12:00 PM)
* `oxInspector.proxy_url` : A value you can set to route all traffic from Inspector through your proxy server.

## Connecting to OX K8s Inspector

> **Note:** Before connecting, a DevOps team member must ensure that the CronJob is running in your environment.

1. In the OX platform, go to the **Connectors** page.
2. Select **Add Connector** and search for **OX** **K8s Inspector**.
3. In the **Configure your OX K8s Inspector credentials** dialog, select **CONNECT**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-4300be51d6781de20685c54e4a5b64f3d09b5f42%2FK8s%20Inspector%20connect.png?alt=media" alt="" width="360"><figcaption></figcaption></figure>

1. To select specific clusters for scanning by the OX platform, select the gear icon next to **DELETE**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-07f73b8b0e9278c5539a519850d40be46afae27e%2Fgear_icon.png?alt=media" alt="" width="321"><figcaption></figcaption></figure>

1. Select the clusters you want to protect.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2f724f79cebc1b533567fbc3ca8465dafc144fff%2FK8s%20Inspector%20cluster%20selection.png?alt=media" alt="" width="279"><figcaption></figcaption></figure>

1. Select **SAVE**.
