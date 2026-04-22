<!-- Source: https://namespace.so/docs/federation/gcp -->

# Workload Federation with GCP

Namespace relies on Workload Identity Federation to allow Namespace to interact with different systems, instead of relying on pre-shared keys which can be more easily compromised.

## Accessing GCP resources from Namespace

Identity Federation with GCP allows your Namespace workloads to identify
themselves to GCP using short-lived secure credentials.

To enable this federation, create a Workload Identity Pool and Provider for Namespace federation in GCP
and configure service account impersonation.

### Create a Workload Identity Pool and Provider

1. Ensure [IAM](https://console.cloud.google.com/apis/api/iamcredentials.googleapis.com/metrics) is enabled for your GCP project.
2. Create a Workload Identity Pool using `gcloud` CLI:

   ```
   export POOL_ID=namespace-workload-pool
    
   gcloud iam workload-identity-pools create ${POOL_ID} \
       --location="global"
   ```
3. Create an Identity Provider:

   ```
   export PROVIDER_ID=namespace-id-provider
    
   gcloud iam workload-identity-pools providers create-oidc \
       ${PROVIDER_ID} \
       --location="global" \
       --workload-identity-pool=${POOL_ID} \
       --issuer-uri="https://federation.namespaceapis.com" \
       --attribute-mapping="google.subject=assertion.tenant_id"
   ```

### Configure service account impersonation

1. Discover your [GCP Project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). Note, this is different from the [GCP Project ID](https://support.google.com/googleapi/answer/7014113):

   ```
   export PROJECT_NUMBER=$(gcloud projects list \
        --filter="$(gcloud config get-value project)" \
        --format="value(PROJECT_NUMBER)")
    
   echo ${PROJECT_NUMBER}
   ```
2. Open the [Dashboard](https://cloud.namespace.so/workspace/settings) and copy your Workspace ID.
3. Allow external workloads to impersonate the service account by granting the Workload Identity User role `roles/iam.workloadIdentityUser` on the service account:

   ```
   export SERVICE_ACCOUNT=<NAME>@${PROJECT_ID}.iam.gserviceaccount.com
    
   gcloud iam service-accounts add-iam-policy-binding \
       ${SERVICE_ACCOUNT} \
       --project="${PROJECT_ID}" \
       --role="roles/iam.workloadIdentityUser" \
       --member="principal://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${POOL_ID}/subject/<your-workspace-id>"
   ```

### Access GCP resources from a Namespace workload

1. Obtain GCP credentials:

   ```
   nsc gcp impersonate --service_account $SERVICE_ACCOUNT \
       --workload_identity_provider /projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${POOL_ID}/providers/${PROVIDER_ID} \
       --write_creds=gcp-creds.json
   ```
2. Apply the obtained credentials:

   ```
   $

   ```
   export GOOGLE_APPLICATION_CREDENTIALS=gcp-creds.json
   ```
   ```
3. Access GCP resources:

   ```
   $

   ```
   gcloud storage cp test.txt gs://your-bucket-name/test2.txt
   ```
   ```

## Accessing Namespace resources from GCP

Identity Federation with GCP allows your GCP-based workloads (e.g. running in GKE) to identify themselves to Namespace using short-lived secure credentials.
To enable this federation, we rely on GCP's ability to generate OIDC tokens that can be exchanged for Namespace credentials.
See [Permissions](/docs/security/permissions) for the full list of resources and actions available to federated identities.

- **Issuer**: `https://accounts.google.com`
- **Subject Format**: The full resource path of the Google Service Account your workload runs as (format: `projects/PROJECT_NUMBER/serviceAccounts/EMAIL`)

### Ensure your workload has a Google Service Account

Your GCP workload needs a Google Service Account (GSA) that can mint OIDC tokens. If you're running in GKE with [Workload Identity](https://cloud.google.com/kubernetes-engine/docs/concepts/workload-identity), bind your Kubernetes Service Account (KSA) to a GSA:

1. Create a GSA (if you don't already have one):

   ```
   gcloud iam service-accounts create my-nsc-sa --project=${PROJECT_ID}
   ```
2. Bind the KSA to the GSA:

   ```
   gcloud iam service-accounts add-iam-policy-binding \
       my-nsc-sa@${PROJECT_ID}.iam.gserviceaccount.com \
       --role roles/iam.workloadIdentityUser \
       --member "serviceAccount:${PROJECT_ID}.svc.id.goog[${K8S_NAMESPACE}/${KSA_NAME}]"
   ```
3. Annotate the KSA:

   ```
   kubectl annotate serviceaccount ${KSA_NAME} -n ${K8S_NAMESPACE} \
       iam.gke.io/gcp-service-account=my-nsc-sa@${PROJECT_ID}.iam.gserviceaccount.com
   ```

If your workload already runs as a GSA (e.g. on Compute Engine, Cloud Run, or an existing GKE Workload Identity setup), you can skip this step and use that service account directly.

### Configure Trust Relationship

Use the Namespace CLI to establish a trust relationship with your GCP service account:

**For a specific service account:**

```
nsc auth trust-relationships add \
    --issuer "https://accounts.google.com" \
    --subject-match "projects/${PROJECT_NUMBER}/serviceAccounts/my-nsc-sa@${PROJECT_ID}.iam.gserviceaccount.com"
```

**For all service accounts in a GCP project:**

```
nsc auth trust-relationships add \
    --issuer "https://accounts.google.com" \
    --subject-match "projects/${PROJECT_NUMBER}/serviceAccounts/*"
```

By default, a trust relationship grants full access to the workspace. Use the `--grant` flag to restrict the federated identity to specific resources and actions. For example, to only allow creating and managing instances:

```
nsc auth trust-relationships add \
    --issuer "https://accounts.google.com" \
    --subject-match "projects/${PROJECT_NUMBER}/serviceAccounts/my-nsc-sa@${PROJECT_ID}.iam.gserviceaccount.com" \
    --grant '{"resource_type":"instance","resource_id":"*","actions":["create","list","get","destroy"]}' \
    --grant '{"resource_type":"builder","resource_id":"*","actions":["ensure","access"]}'
```

See the [`--grant` flag reference](/docs/reference/cli/auth-trust-relationships-add#--grant-stringarray-optional-can-be-repeated) and [Permissions](/docs/security/permissions) for the full list of available resource types and actions.

### Verify Trust Relationship

List your configured trust relationships to confirm the setup:

```
$

```
nsc auth trust-relationships list
```
```

You should see your GCP trust relationship with the appropriate subject pattern.

### Obtain Namespace credentials from your GCP workload

From your GCP workload (e.g. a GKE pod), obtain and exchange an OIDC token for Namespace credentials:

1. Generate a GCP OIDC token targeting Namespace:

   ```
   $

   ```
   export OIDC_TOKEN=$(gcloud auth print-identity-token --audiences=federation.namespaceapis.com)
   ```
   ```
2. Exchange the OIDC token for Namespace credentials:

   ```
   $

   ```
   nsc auth exchange-oidc-token --token $OIDC_TOKEN --tenant_id <your-workspace-id>
   ```
   ```

   You can find your Workspace ID in the [Dashboard](https://cloud.namespace.so/workspace/settings).

This command should succeed with the name of workspace you've signed in to.
It stores a short-lived token that will be used automatically in subsequent `nsc` calls.

## Related Topics

- [Trust Relationships CLI Reference](/docs/reference/cli/auth-trust-relationships) - Detailed CLI documentation
- [Workspace Access Controls](/docs/workspaces/access) - Overview of authentication and access control

Last updated February 22, 2026
