# Source: https://docs.anyscale.com/admin/cloud/create-gke-cloud.md

# Deploy Anyscale on Google Kubernetes Engine (GKE)

[View Markdown](/admin/cloud/create-gke-cloud.md)

## 1. Install Anyscale's python client package[​](#1-install-anyscales-python-client-package "Direct link to 1. Install Anyscale's python client package")

```
pip install -U "anyscale[gcp]"
anyscale login # authenticate
```

## 2. Configure your Cloud Provider account[​](#2-configure-your-cloud-provider-account "Direct link to 2. Configure your Cloud Provider account")

* Prepare a Google Cloud project for Anyscale to use.
* Follow the Google Cloud [instructions](https://cloud.google.com/sdk/docs/install) on installing gcloud CLI if you haven't.

note

Before you continue to the next step, make sure your GCP credentials have the following permissions ([learn more](/admin/cloud/configure-google-cloud.md)):

* Has owner role on the GCP project you want Anyscale to use

## 3. Terraform your GCP Project to create a GKE cluster[​](#3-terraform-your-gcp-project-to-create-a-gke-cluster "Direct link to 3. Terraform your GCP Project to create a GKE cluster")

note

If you wish to use an existing GKE cluster, follow [this example](https://github.com/anyscale/terraform-kubernetes-anyscale-foundation-modules/tree/main/examples/gcp/gke-existing_cluster) or explore [the Anyscale Operator documentation](/admin/cloud/kubernetes.md) and the [Anyscale Terraform Github](https://github.com/anyscale/terraform-kubernetes-anyscale-foundation-modules) repository.

**Enter information about where you want to deploy your GKE cluster.**

GCP Project IDmy-rayturbo-project

Anyscale Cloud Namemy-gke-cloud

GCP Regionus-central1

GKE cluster namemy-gke-cluster

Run the following commands to create an Anyscale Cloud with a basic GKE cluster.

```
git clone https://github.com/anyscale/terraform-kubernetes-anyscale-foundation-modules
cd terraform-kubernetes-anyscale-foundation-modules/examples/gcp/gke-new_cluster/
```

Create and populate the Terraform variable file with your Anyscale organization ID and other variables (automatically populated).

```
cat <<EOF > terraform.tfvars
google_project_id = "<your_google_project_id>"
google_region = "<your_google_region>"
gke_cluster_name = "<your_gke_cluster_name>"
EOF
```

Apply the Terraform and wait for resources to be created. This may take a couple minutes.

```
terraform init
terraform plan
terraform apply
```

*Note: You may need to enable some GCP APIs in order for the Terraform to apply successfully.*

note

The Terraform output provides an example Cloud registration command. Take note of the following outputs:

* The Availability Zones for the GKE cluster
* The Anyscale Operator service account email
* The name of the GCS bucket

**Provide information from the Terraform output:**

Availability Zonesus-central1-a,us-central1-b

Operator Service Account Emailanyscale-gke-nodes@\<your\_google\_project\_id>.iam.gserviceaccount.com

Storage Bucket Nameanyscale-1234

## 4. Install an nginx ingress controller[​](#4-install-an-nginx-ingress-controller "Direct link to 4. Install an nginx ingress controller")

Connect your terminal to the GKE cluster, replacing the cluster name if it has been modified.

```
gcloud container clusters get-credentials <your_gke_cluster_name> --region <your_google_region> --project <your_google_project_id>
```

*Note: You may need to install the gke-gcloud-auth-plugin if not already installed.*

Run the following commands to install the nginx ingress controller for externally facing load balancing. For more information about customizing ingress, refer to the [Anyscale Terraform Github](https://github.com/anyscale/terraform-kubernetes-anyscale-foundation-modules) repository.

```
helm repo add nginx https://kubernetes.github.io/ingress-nginx
```

```
helm upgrade ingress-nginx nginx/ingress-nginx \
  --version 4.12.1 \
  --namespace ingress-nginx \
  --values sample-values_nginx_gke_public.yaml \
  --create-namespace \
  --install
```

## 5. Install the Anyscale Operator Helm chart[​](#5-install-the-anyscale-operator-helm-chart "Direct link to 5. Install the Anyscale Operator Helm chart")

Run the following command to install and update the Helm chart for the Anyscale Operator.

```
helm repo add anyscale https://anyscale.github.io/helm-charts
helm repo update anyscale
```

If you wish to customize the Helm chart to add custom Patches or additional pod shapes follow [these instructions](/k8s/configure-helm.md) in the documentation. To enable TPU support, follow the guide for [leveraging TPUs on GKE](/administration/cloud-deployment/leverage-cloud-tpus-on-kubernetes.md).

## 6. Register the Anyscale Cloud resources[​](#6-register-the-anyscale-cloud-resources "Direct link to 6. Register the Anyscale Cloud resources")

Run the command produced by the Terraform script. The command should look similar to the commands below. Verify all variables are entered correctly.

```
anyscale cloud register --name <your_cloud_name> \
  --provider gcp \
  --region <your_google_region> \
  --compute-stack k8s \
  --kubernetes-zones us-central1-a,us-central1-b \
  --anyscale-operator-iam-identity anyscale-gke-nodes@<your_google_project_id>.iam.gserviceaccount.com \
  --cloud-storage-bucket-name gs://<your_storage_bucket_name>
```

note

Take note of the Cloud Deployment ID in the output.

**Record the cloud resource ID:**

Cloud Resource IDcldrsrc\_1234

## 7. Deploy the Anyscale Operator on your GKE cluster[​](#7-deploy-the-anyscale-operator-on-your-gke-cluster "Direct link to 7. Deploy the Anyscale Operator on your GKE cluster")

Run the following commands to deploy the Anyscale Operator with your Cloud Deployment ID. Verify all variables are entered correctly. The release name and namespace are up to you to define.

```
helm upgrade <your_cloud_name>-v0 anyscale/anyscale-operator \
  --set-string global.cloudDeploymentId=<your_cloud_deployment_id> \
  --set-string global.cloudProvider=gcp \
  --set-string global.auth.iamIdentity=anyscale-gke-nodes@<your_google_project_id>.iam.gserviceaccount.com \
  --set-string workloads.serviceAccount.name=anyscale-operator \
  --namespace <your_cloud_name> \
  --create-namespace \
  -i
```

Run the following command to bind the Anyscale Operator service account to the operator.

```
gcloud iam service-accounts add-iam-policy-binding anyscale-gke-nodes@<your_google_project_id>.iam.gserviceaccount.com \
  --role roles/iam.workloadIdentityUser \
  --member "serviceAccount:<your_google_project_id>.svc.id.goog[<your_cloud_name>/anyscale-operator]" \
  --project <your_google_project_id>
```

It may take several minutes for your Anyscale Cloud to be ready to use. You can watch the deployment status using the following command.

```
kubectl get deployments anyscale-operator -n <your_cloud_name> -w
```

## 8. Verify your Anyscale Cloud[​](#8-verify-your-anyscale-cloud "Direct link to 8. Verify your Anyscale Cloud")

It may take several minutes for your Anyscale Cloud to be ready to use. Run the following command to verify that your newly created Anyscale Cloud is fully functional and ready to use.

```
anyscale job submit --cloud <your_cloud_name> --working-dir https://github.com/anyscale/docs_examples/archive/refs/heads/main.zip -- python hello_world.py
```
