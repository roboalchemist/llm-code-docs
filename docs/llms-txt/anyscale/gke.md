# Source: https://docs.anyscale.com/iam/gke.md

# Configure service accounts for clusters on Anyscale on GKE

[View Markdown](/iam/gke.md)

# Configure service accounts for clusters on Anyscale on GKE

This page describes how to use and manage service accounts for Anyscale clouds deployed on Google Kubernetes Engine (GKE).

## What is the IAM model for Anyscale on GKE?[​](#iam-model "Direct link to What is the IAM model for Anyscale on GKE?")

The Anyscale control plane interacts with GKE service accounts through the Anyscale operator. You manage all identity and access management (IAM) for Anyscale workloads on GKE through Kubernetes service accounts that map to Google Cloud service accounts.

GKE uses Workload Identity Federation to map IAM permissions from Google Cloud service accounts onto Kubernetes service accounts. See the following Google Cloud docs for more details:

* [About service accounts in GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/service-accounts)
* [Workload Identity Federation for GKE](https://cloud.google.com/kubernetes-engine/docs/concepts/workload-identity)

For the best performance, Anyscale recommends the following:

* Configure your GKE cluster to use Workload Identity Federation.
* Create Google Cloud service accounts with appropriate IAM permissions.
* Map a single Google Cloud service account to each Kubernetes service account in your GKE cluster used by Anyscale.

important

You provide a Google Cloud service account to Anyscale when registering a new cloud resource backed by GKE. The Anyscale operator uses that service account to get a token from GKE. The Anyscale control plane uses the registered service account to validate the identity used by the Anyscale operator and returns a token for secure communication with the control plane.

## GKE service accounts used by Anyscale[​](#service-accounts "Direct link to GKE service accounts used by Anyscale")

You annotate GKE service accounts to add a trust relationship with a Google Cloud service account. This annotation provides Ray nodes in your Anyscale cluster access to resources in your Google Cloud account, such as the default Cloud Storage bucket configured during your cloud deployment.

The following table describes the service accounts you need to configure for Anyscale:

| Term                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Anyscale operator service account | When you deploy an Anyscale cloud on GKE, you configure a Kubernetes service account for the Anyscale operator that maps to a Google Cloud service account.The permissions in this service account govern all actions that the Anyscale operator can take in your GKE cluster. The Anyscale operator is responsible for processing all instructions from the Anyscale control plane to deploy nodes for Ray clusters in your GKE cluster.                                                                                                                                                                              |
| Cluster service account           | When you configure the Anyscale operator for your Anyscale cloud on GKE, you configure a default Kubernetes service account that maps to a Google Cloud service account. When the Anyscale operator deploys a new cluster or autoscales to add worker nodes, the Pods use this service account and assume the Google Cloud service account to gain access to necessary resources in your Google Cloud account.You must define a Kubernetes service account and Google Cloud service account for each unique set of IAM permissions you want to assign to a given user, workload, or project through cloud IAM mapping. |

## View cluster service account[​](#view "Direct link to View cluster service account")

Run the following commands to find the Kubernetes service account in use for Pods in your Anyscale cluster:

```
# Define your GKE namespace.
NAMESPACE="<your-gke-namespace>"

# Get all Pods and manually identify your Pod.
kubectl get pods -n ${NAMESPACE} | grep k-

# Define a variable for your Pod name.
POD_NAME="<your-pod-name>"

# Get the Kubernetes service account name used by your Pod.
kubectl get pod ${POD_NAME} -n ${NAMESPACE} -o jsonpath='{.spec.serviceAccountName}'
```

To see the Google Cloud service account used by your Kubernetes service account, run the following command:

```
kubectl get serviceaccount "<your-kubernetes-service-account>" -n "${NAMESPACE}" \
  -o jsonpath='{.metadata.annotations.iam\.gke\.io/gcp-service-account}{"\n"}'
```

## Create and map a GKE cluster service account[​](#create-account "Direct link to Create and map a GKE cluster service account")

To create a new cluster service account, you annotate a Kubernetes service account with a Google Cloud service account. You add IAM roles to the Google Cloud service account to grant access to additional resources in your Google Cloud account, such as Cloud Storage buckets.

note

Use cloud IAM mapping to control how Anyscale assigns cluster service accounts based on user identity, workload type, or project.

You must create and annotate a Kubernetes service account for each unique Google Cloud service account you need to assign to Anyscale clusters. See [Anyscale cloud IAM mapping](/iam/cloud-iam-mapping.md).

Complete the following steps to annotate a GKE service account.

### Requirements[​](#requirements "Direct link to Requirements")

The following instructions assume the following:

* You have created a GKE cluster and registered it as an Anyscale cloud resource.
* You have installed and authenticated the Google Cloud CLI.
* You have installed and configured `kubectl` for your GKE cluster.
* You have enabled Workload Identity Federation on your GKE cluster. See [Enable Workload Identity Federation for GKE on your cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable).

### Step 0: Identify or create a Google Cloud service account[​](#step-0 "Direct link to Step 0: Identify or create a Google Cloud service account")

Identify or create the Google Cloud service account you need to attach to your GKE cluster.

For Anyscale to operate correctly, your service account must have permissions to interact with the Cloud Storage bucket configured as default storage for your Anyscale cloud resource. See [Minimum privileges for Anyscale cluster service accounts](/iam/google-cloud.md#minimum).

important

You use the email address for the Google Cloud service account to configure the trust relationship with GKE.

You define your service account name as a variable in the next step and use it to construct the email address.

### Step 1: Configure variables[​](#step-1 "Direct link to Step 1: Configure variables")

The following commands configure variables that describe your Google Cloud account, GKE cluster, and Anyscale account. Replace the variables denoted with `<>` before running these commands. For example, replace `<your-gke-cluster-name>` with the name of your GKE cluster.

note

You can save and run these commands as a `.sh` script, or run each command sequentially from the command line.

```
#!/bin/bash

# Specify the namespace for Anyscale in your GKE cluster.
# Anyscale uses 'anyscale-operator' as the default GKE namespace.
export NAMESPACE="<your-anyscale-namespace>"

# Specify the Google Cloud region, project ID, and name of your GKE cluster.
export PROJECT_ID="<your-google-cloud-project-id>"
export GKE_REGION="<your-gke-region>"
export GKE_CLUSTER_NAME="<your-gke-cluster-name>"

# Define the name for a new GKE service account.
export SERVICE_ACCOUNT_NAME="<your-service-account-name>"

# Define a variable for the name of your Google Cloud service account.
# Use variables to format the email address for the Google Cloud service account.
export GOOGLE_SERVICE_ACCOUNT_NAME="<your-google-service-account-name>"
export GOOGLE_SERVICE_ACCOUNT_EMAIL="${GOOGLE_SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"
```

### Step 2: Show current service accounts[​](#step-2 "Direct link to Step 2: Show current service accounts")

Run the following commands to connect to your GKE cluster and list all service accounts present in your namespace:

```
gcloud container clusters get-credentials "${GKE_CLUSTER_NAME}" \
    --region "${GKE_REGION}" \
    --project "${PROJECT_ID}"
kubectl get serviceaccounts -n ${NAMESPACE}
```

note

You can review service accounts currently registered for Anyscale cloud IAM mapping in the Anyscale console or using the CLI. See [Anyscale cloud IAM mapping](/iam/cloud-iam-mapping.md).

### Step 3: Create a Kubernetes service account[​](#step-3 "Direct link to Step 3: Create a Kubernetes service account")

Run the following command to create a Kubernetes service account in the namespace of your GKE cluster:

```
kubectl create serviceaccount "${SERVICE_ACCOUNT_NAME}" -n "${NAMESPACE}" \
  --dry-run=client -o yaml | kubectl apply -f -
```

### Step 4: Annotate the Kubernetes service account[​](#step-4 "Direct link to Step 4: Annotate the Kubernetes service account")

Run the following command to annotate the GKE service account with the Google Cloud service account email:

```
kubectl annotate serviceaccount "${SERVICE_ACCOUNT_NAME}" -n "${NAMESPACE}" \
  iam.gke.io/gcp-service-account="${GOOGLE_SERVICE_ACCOUNT_EMAIL}" --overwrite
```

### Step 5: Bind the Kubernetes service account to the Google Cloud service account[​](#step-5 "Direct link to Step 5: Bind the Kubernetes service account to the Google Cloud service account")

Create an IAM policy binding that allows the Kubernetes service account to impersonate the Google Cloud service account. This step establishes the trust relationship between your GKE cluster and the Google Cloud service account.

Run the following command to add the IAM policy binding:

```
gcloud iam service-accounts add-iam-policy-binding "${GOOGLE_SERVICE_ACCOUNT_EMAIL}" \
    --role roles/iam.workloadIdentityUser \
    --member "serviceAccount:${PROJECT_ID}.svc.id.goog[${NAMESPACE}/${SERVICE_ACCOUNT_NAME}]"
```

See [Configure applications to use Workload Identity Federation for GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#authenticating_to) for more details.

### Step 6: Verify the annotation[​](#step-6 "Direct link to Step 6: Verify the annotation")

Run the following command to display the annotation field of your service account:

```
kubectl get serviceaccount "${SERVICE_ACCOUNT_NAME}" -n "${NAMESPACE}" \
  -o jsonpath='{.metadata.annotations.iam\.gke\.io/gcp-service-account}{"\n"}'
```

The Google Cloud service account email you assigned to the GKE service account displays.

### Step 7: Register the service account with Anyscale[​](#step-7 "Direct link to Step 7: Register the service account with Anyscale")

Each Anyscale cloud resource has a default service account used by all clusters. To use your new service account as the default, update the `workloads.serviceAccount.name` setting in your Helm chart with the name of your service account and upgrade your Anyscale operator.

Anyscale recommends using cloud IAM mapping to scope service accounts to users, projects, and workloads for more fine-grained access controls. Cloud owners can define cloud IAM mapping rules in the Anyscale console or using the CLI. See [Anyscale cloud IAM mapping](/iam/cloud-iam-mapping.md).
