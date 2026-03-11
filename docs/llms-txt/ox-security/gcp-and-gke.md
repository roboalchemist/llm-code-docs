# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/cloud-security/gcp-and-gke.md

# GCP and GKE

## Google Kubernetes Engine (GKE)

Google Kubernetes Engine (GKE) is a managed Kubernetes service that simplifies the deployment, scaling, and management of containerized applications in Google Cloud. It abstracts infrastructure management while providing flexibility and control over Kubernetes clusters.

Integrating OX Security with GKE gives your security team real-time visibility into what’s running in your clusters and improves workload protection, as follows:

* **Workload-Level Scanning:** OX identifies which container images are actively running in Kubernetes workloads, such as deployments and pods, and scans those confirmed to be in use. This improves precision and reduces unnecessary overhead.
* **Runtime Context**\
  OX enriches security findings across your environment with runtime metadata. When a vulnerability is found in code or an image that is deployed and running, the issue is flagged with additional severity context to support informed triage and decision-making.
* **Risk Prioritization Support**\
  You can prioritize issues based on runtime status, filter findings by whether they are actively running, or create custom policies that adjust severity accordingly.

For a description of the supported Kubernetes connection models, including direct cloud integration and Inspector-based access, see [Kubernetes Reachability](https://docs.ox.security/ox-integrations/3rd-party-integrations/cloud-security/kubernetes-reachability).

## Google Cloud Platform (GCP) support for GKE

To support GKE integration, OX also connects to Google Cloud Platform (GCP). The GCP connector is required to enable GKE connectivity and provides cloud-level context for Kubernetes workloads.

The GCP connector is used to:

* Authenticate access to your Google Cloud project as a prerequisite for connecting GKE.
* Enrich Kubernetes data with cloud-level information, including whether deployed workloads are internet exposed.
* Generate a cloud-based bill of materials (Cloud BOM) that reflects assets deployed in your cloud environment.

## Prerequisites

* A Google Cloud project with IAM permissions to:
  * Create service accounts
  * Manage service account keys
* Enable required APIs (e.g., Compute Engine API, IAM API, Kubernetes Engine API).
* Optional: `gcloud` CLI installed and configured.
* A running GKE cluster in the selected GCP project, with Kubernetes API enabled.
* Authorized OX static IP address to access your GKE: 108.128.213.11, 34.247.61.212.

## Step 1: Create a new service account \[Google]

1. Log in to the [Google Cloud Console](https://console.cloud.google.com).
2. Select your GKE project.
3. Navigate to **IAM & Admin**.
4. Select **Service Accounts**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-621c63fddb71f312c62da8c695affd764764577e%2FService_Account.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Select **+ Create Service Account**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-008a5338932ea7d0fb11a5b9f5dc8383b352c90a%2FGCP_Create_SA.png?alt=media" alt="" width="430"><figcaption></figcaption></figure>

1. Add a meaningful name and an optional description.
2. Select **Create and Continue**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-ff10e6b449203542004554433247a3ee942d18c0%2FGrant_SA.png?alt=media" alt="" width="418"><figcaption></figcaption></figure>

1. Grant the **Viewer** role to the new service account and select **Done**. The new service account appears in the **Service accounts** table.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2f92b296af2ab5c1630e2931c4f91f05e57b686e%2Fgcp_connector_result.png?alt=media" alt=""><figcaption></figcaption></figure>

1. In the **Actions** column, select the newly created service account, click the three dot menu related to it, and select **Manage keys**.
2. In the **Keys** pane, select **Add key > Create new key**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-ae77d8d54d42d59f513a7208d522033d6c683e28%2FGCP_connector__create_key.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Select **JSON** and then select **Create**. The file is automatically downloaded to your system.
2. Securely store the JSON key file.
3. To encode the Key File in Base64:

* On **macOS/Linux**, run: `base64 <filename>.json`
* On **Windows**, use a tool or plugin to convert the JSON to a one-line Base64 string.

> **Note:** The Base64 encoding ensures multi-line keys are compacted into a single string.

1. To enable required Google Cloud APIs, in the **Google Cloud Console**:
    1. Navigate to **APIs & Services**.
    2. In the left pane, select **Library**.
    3. Search for and enable the following APIs:

       * Compute Engine API (compute.googleapis.com)
       * Kubernetes Engine API (container.googleapis.com)
       * Cloud Resource Manager API (cloudresourcemanager.googleapis.com)

       <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-01c799b58b5eddec595b9365826d0347175c9ef4%2FAPI_enable.png?alt=media" alt="" width="544"><figcaption></figcaption></figure>
    4. Alternatively, use the gcloud CLI to enable all the required APIs at once:

```
gcloud services enable compute.googleapis.com \
    apikeys.googleapis.com \
    artifactregistry.googleapis.com \
    bigquery.googleapis.com \
    sqladmin.googleapis.com \
    storage.googleapis.com \
    dns.googleapis.com \
    containerregistry.googleapis.com \
    container.googleapis.com \
    iam.googleapis.com \
    dataproc.googleapis.com \
    cloudkms.googleapis.com \
    logging.googleapis.com \
    cloudresourcemanager.googleapis.com
```

e. To verify the APIs were enabled, run:

```
gcloud services list --enabled

```

## Step 2: Connect to GCP

1. In the **Google Cloud Console**, locate the ID of the project in which you have created a service account.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-87af824d6471a1b83cb8357dc5f9b3153d5ece8a%2Fproject%20in%20GCP.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

1. In the **OX Security** platform, go to **Connectors** and search for **GCP**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3aa20953fd8b1bf48a861ec22ac4072cabef8894%2FGCP_icon.png?alt=media" alt="" width="155"><figcaption></figcaption></figure>

1. Select **GCP** and set the following parameters in the **Configure your GCP credentials** dialog.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2818c1a890efa33b88bc2bc6b70b00b52f5f106f%2FGCP_connect.png?alt=media" alt="" width="539"><figcaption></figcaption></figure>

| Parameter         | Description                    |
| ----------------- | ------------------------------ |
| **Project ID**    | Copy the value from the step 1 |
| **API** **Token** | Base64-encoded key             |

1. Select **CONNECT**. A success message appears.

## Multi-project access

**To reuse one service account across multiple GCP projects:**

1. [Create a new service account](#creating-a-new-service-account).
2. In the source project, copy the email of the service account.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-66ed90b3ea66193f1abfd2ec50745794c18f51c7%2Fgcp_connector_result_email.png?alt=media" alt=""><figcaption></figcaption></figure>

1. For each target project, navigate to **IAM & Admin** and select **Grant Access**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-0b659975e096c899980ed903ff56f6be142b1467%2FMulti_project_grant_perm.png?alt=media" alt="" width="453"><figcaption></figcaption></figure>

1. In the **New principals** box, add the copied email address.
2. In the **Role** box, select **Viewer** and then click **Save**.
3. In the **OX Security** platform, go to **Connectors** and search for **GCP**.
4. Select **GCP** and set the following parameters in the **Configure your GCP credentials** dialog.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2818c1a890efa33b88bc2bc6b70b00b52f5f106f%2FGCP_connect%20(1).png?alt=media" alt="" width="539"><figcaption></figcaption></figure>

| Parameter         | Description        |
| ----------------- | ------------------ |
| **Project ID**    | Add \*             |
| **API** **Token** | Base64-encoded key |

1. Select **CONNECT**. A success message appears.

## Step 3: Connect to GKE

After you configure the GCP connector, you can connect your GKE clusters. The GKE connector does not require separate credentials. Instead, it automatically uses the credentials you created for GCP, because both connectors rely on the same authentication format and access scope within your Google Cloud project.

Configuring GKE is a short process. Once the GCP connector is active and the required services are enabled in your Google Cloud project, you only need to select your cluster and complete the connection.

When you connect GKE, OX retrieves metadata from your Kubernetes clusters and enriches your environment with workload-level and runtime insights.

**To connect to GKE:**

1. In the **OX Security** platform, go to **Connectors** and search for **GKE**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-97852b228bdde0619c7adcc4165fdf45023b6830%2FGKE_icon%20(1).png?alt=media" alt="" width="135"><figcaption></figcaption></figure>

1. Select **GKE**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-7159edcbd85c81c2767d36287b1c50104b4d65b2%2FGKE_connect_new.png?alt=media" alt="" width="537"><figcaption></figcaption></figure>

1. Select **Connect**.
2. To select specific clusters for scanning by OX platform, select the gear icon next to **DELETE**.
3. Select the clusters you want to protect.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-8e8a4fb0187ade4190bf7f814d64d3d2fb9dceba%2FGKE_clusters_selection.png?alt=media" alt="" width="337"><figcaption></figcaption></figure>

1. Select **SAVE**.

After connecting your cluster, OX begins collecting Kubernetes metadata, such as deployed workloads, image versions, and runtime status. This information enriches your Applications, Issues, Attack Path, and Artifact BOM pages with cloud-native context.
