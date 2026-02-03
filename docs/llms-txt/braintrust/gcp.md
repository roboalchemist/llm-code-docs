# Source: https://braintrust.dev/docs/admin/self-hosting/gcp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Self-host on GCP

This guide shows you how to deploy the Braintrust data plane in your Google Cloud project using the Braintrust [Terraform module](https://github.com/braintrustdata/terraform-google-braintrust-data-plane) and [Helm chart](https://github.com/braintrustdata/helm). This is the recommended way to self-host Braintrust on GCP.

## Set up the data plane

Deploy the Braintrust data plane infrastructure in your Google Cloud project.

<Steps>
  <Step title="Configure the Terraform module">
    The Braintrust [Terraform module](https://github.com/braintrustdata/terraform-google-braintrust-data-plane) contains all the necessary resources for a self-hosted Braintrust data plane. A dedicated Google Cloud project for your Braintrust deployment is recommended but not required.

    1. Copy the entire contents of the [`examples/braintrust-data-plane`](https://github.com/braintrustdata/terraform-google-braintrust-data-plane/tree/main/examples/braintrust-data-plane) directory from the [terraform-google-braintrust-data-plane](https://github.com/braintrustdata/terraform-google-braintrust-data-plane) repository into your own repository.

    2. In `provider.tf`, configure your Google Cloud project and region.

    3. In `backend.tf`, set up your remote backend (typically a GCS bucket).

    4. In `main.tf`, customize the Braintrust deployment settings.

       The defaults are for suitable for a large production-sized deployment. Adjust them based on your needs, but keep in mind the [hardware requirements](/admin/self-hosting/index#hardware-requirements).
  </Step>

  <Step title="Enable Google Cloud APIs">
    Before deploying, enable the required Google Cloud services. Run the following in Cloud Shell:

    1. In a Cloud Shell, set the project to deploy Braintrust into:

       ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
       gcloud config set project "your-project-id"
       ```

    2. Enable the required services:

       ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
       gcloud services enable storage-api.googleapis.com \
         storage-component.googleapis.com \
         storage.googleapis.com \
         redis.googleapis.com \
         secretmanager.googleapis.com \
         servicenetworking.googleapis.com \
         logging.googleapis.com \
         monitoring.googleapis.com \
         oslogin.googleapis.com \
         dns.googleapis.com \
         cloudresourcemanager.googleapis.com \
         compute.googleapis.com \
         cloudkms.googleapis.com \
         autoscaling.googleapis.com \
         iam.googleapis.com \
         iamcredentials.googleapis.com \
         vpcaccess.googleapis.com \
         sts.googleapis.com \
         container.googleapis.com \
         sqladmin.googleapis.com \
         artifactregistry.googleapis.com
       ```

    Allow approximately 5 minutes for services to activate.
  </Step>

  <Step title="Deploy the Terraform module">
    Initialize and apply the Terraform configuration:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    terraform init
    terraform apply
    ```

    This will create all necessary GCP resources including:

    * GKE cluster for running Braintrust services
    * Cloud SQL PostgreSQL database
    * Cloud Memorystore Redis cache
    * Cloud Storage buckets
    * VPC network and subnets
    * Cloud KMS key for encryption
  </Step>

  <Step title="Connect to GKE cluster">
    After the Terraform deployment completes, connect to your GKE cluster:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    gcloud auth login
    gcloud config set project "<project-id>"
    gcloud container clusters get-credentials <cluster-name> --region <region>
    ```

    Verify the connection:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    kubectl get nodes
    ```
  </Step>

  <Step title="Create Kubernetes namespace">
    Create the namespace for Braintrust:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    kubectl create namespace braintrust
    ```
  </Step>

  <Step title="Create Kubernetes secrets">
    Create the required Kubernetes secrets for your deployment. The secrets needed depend on your [GCS authentication method](#gcs-authentication-options). See that section below for the specific commands.
  </Step>

  <Step title="Configure Helm values">
    Create a `helm-values.yaml` file for your deployment. Refer to the [Helm chart documentation](https://github.com/braintrustdata/helm) for configuration options.
  </Step>

  <Step title="Deploy Helm chart">
    Deploy the Braintrust Helm chart to your cluster. Refer to the [Helm chart documentation](https://github.com/braintrustdata/helm) for configuration options.

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    helm repo add braintrust oci://public.ecr.aws/braintrust/helm
    helm install braintrust braintrust/braintrust \
      --namespace braintrust \
      --version <version> \
      --values helm-values.yaml
    ```
  </Step>

  <Step title="Get your API URL">
    The dataplane requires a HTTPS connection to the API pods. This connection will require a valid HTTPS certificate that is trusted by the clients connecting to the data plane. Although Google doesn't have a native service, there are several ways to provide a DNS name with a SSL certificate.

    * Use Cloud Run to run a NGINX container to do SSL termination.
    * Use a Load balancer for the API service with a certificate from an internal CA or with Let's Encrypt.

    After setting up your ingress, save the API URL - you'll need it to configure your Braintrust organization.
  </Step>
</Steps>

### GCS authentication options

Braintrust services use different authentication methods for Google Cloud Storage:

* **API**: Can use either native GCS authentication (recommended) or S3 compatibility mode with HMAC keys (legacy)
* **Brainstore**: Always uses native GCS authentication via Workload Identity

#### Workload Identity setup

The Terraform module automatically configures Workload Identity for your GKE cluster and creates service accounts with storage permissions for both the API and Brainstore services.

#### API authentication configuration

Choose one of the following authentication methods for the API service:

<Tabs>
  <Tab title="Native GCS auth (recommended)">
    Native GCS authentication uses the `@google-cloud/storage` SDK and Workload Identity. This is the recommended approach for enhanced security as it eliminates the need to manage service account keys.

    **Requirements:**

    * Helm chart version 3.1.0 or later
    * Workload Identity configured (automatic with Terraform module)

    **Kubernetes secrets:**

    For native GCS authentication, create secrets without GCS credentials:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    kubectl create secret generic braintrust-secrets \
      --from-literal=REDIS_URL="<redis_url>" \
      --from-literal=PG_URL="<pg_url>" \
      --from-literal=FUNCTION_SECRET_KEY="<randomly_generated_secret>" \
      --from-literal=BRAINSTORE_LICENSE_KEY="<brainstore_license_key>" \
      --namespace=braintrust
    ```

    <Note>
      Refer to the Terraform outputs for the connection strings. The Brainstore license key can be found in your Braintrust organization's **Settings** > **Data plane** page.
    </Note>

    **Helm configuration:**

    In your Helm values file, enable native GCS authentication and configure the Google service account:

    ```yaml  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    api:
      serviceAccount:
        googleServiceAccount: "prod-braintrust@your-project-id.iam.gserviceaccount.com"
      enableGcsAuth: true
    ```

    <Note>
      The Terraform module outputs the service account email as `braintrust_service_account`. Run `terraform output braintrust_service_account` to get the full email address.

      The `enableGcsAuth` setting defaults to `false` for backwards compatibility, but will default to `true` in a future release.
    </Note>
  </Tab>

  <Tab title="S3 compatibility mode (legacy)">
    S3 compatibility mode uses HMAC keys to access GCS through the S3-compatible API. This is the legacy authentication method.

    **Kubernetes secrets:**

    For S3 compatibility mode, include HMAC credentials:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    kubectl create secret generic braintrust-secrets \
      --from-literal=REDIS_URL="<redis_url>" \
      --from-literal=PG_URL="<pg_url>" \
      --from-literal=GCS_ACCESS_KEY_ID="<braintrust_hmac_access_id>" \
      --from-literal=GCS_SECRET_ACCESS_KEY="<braintrust_hmac_secret>" \
      --from-literal=FUNCTION_SECRET_KEY="<randomly_generated_secret>" \
      --from-literal=BRAINSTORE_LICENSE_KEY="<brainstore_license_key>" \
      --namespace=braintrust
    ```

    <Note>
      Refer to the Terraform outputs for the connection strings. The Brainstore license key can be found in your Braintrust organization's **Settings** > **Data plane** page.
    </Note>

    **Helm configuration:**

    In your Helm values file, ensure `enableGcsAuth` is not set or set to `false`. Do not configure `googleServiceAccount` when using HMAC keys:

    ```yaml  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    api:
      enableGcsAuth: false  # or omit this line
    ```
  </Tab>
</Tabs>

#### Brainstore configuration

Brainstore always uses native GCS authentication. In your Helm values file, configure the Google service account for Workload Identity:

```yaml  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
brainstore:
  serviceAccount:
    googleServiceAccount: "prod-brainstore@your-project-id.iam.gserviceaccount.com"
```

<Note>
  The Terraform module outputs the service account email as `brainstore_service_account`. Run `terraform output brainstore_service_account` to get the full email address.
</Note>

## Configure your organization

Connect your Braintrust organization to your newly deployed data plane.

<Warning>
  Changing your live organization's API URL can disrupt access for existing users. If you are testing, create a new Braintrust organization for your data plane instead of updating your live environment.
</Warning>

<Steps>
  <Step title="Point your organization to your data plane">
    1. In the Braintrust UI, go to **Settings** > **Data plane**.
    2. In **API URL** area, select **Edit**.
    3. Enter the API URL from the last step.
    4. Leave the other fields blank.
    5. Select **Save**.
  </Step>

  <Step title="Verify the connection">
    The UI will automatically test the connection to your new data plane. Verify that the ping to each endpoint is successful.
  </Step>
</Steps>

## Update the deployment

Updating your GCP deployment involves two steps: updating infrastructure with Terraform and updating services with Helm.

### Update infrastructure (Terraform)

Run `terraform apply` to update infrastructure components (database, Redis, networking, storage, etc.):

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
terraform apply
```

<Warning>
  Carefully review the output of `terraform plan` before applying any changes to your deployment. If you see something unexpected, like deletion of a database or storage bucket, [contact Braintrust](mailto:support@braintrust.dev) for help.
</Warning>

To pin to a specific Terraform module version, add a `?ref=<version>` to the module source:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
module "braintrust-data-plane" {
  source = "github.com/braintrustdata/terraform-google-braintrust-data-plane?ref=vX.Y.Z"

  # ... other configuration ...
}
```

Terraform releases: [GitHub Releases](https://github.com/braintrustdata/terraform-google-braintrust-data-plane/releases)

### Update services (Helm)

After updating infrastructure, upgrade the Helm chart to update service containers and configurations:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
helm upgrade braintrust braintrust/braintrust-data-plane \
  --namespace braintrust \
  --reuse-values \
  --version <version>
```

<Note>
  In some cases, Terraform changes must be applied before Helm upgrades. Check the release notes for any specific upgrade ordering requirements.
</Note>

Helm releases: [GitHub Releases](https://github.com/braintrustdata/helm/releases)
