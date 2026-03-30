# Source: https://cert-manager.io/docs/configuration/acme/dns01/google/

Title: Google CloudDNS

URL Source: https://cert-manager.io/docs/configuration/acme/dns01/google/

Markdown Content:
This guide explains how to set up an `Issuer`, or `ClusterIssuer`, to use Google CloudDNS to solve DNS01 ACME challenges. It's advised you read the [DNS01 Challenge Provider](https://cert-manager.io/docs/configuration/acme/dns01/) page first for a more general understanding of how cert-manager handles DNS01 challenges.

This guide assumes that your cluster is hosted on Google Cloud Platform (GCP) and that you already have a domain set up with CloudDNS.

You'll need to be using a **Public DNS Zone**, so that the ACME challenge checker is able to access the DNS records that cert-manager will create.

Set up a Service Account[](https://cert-manager.io/docs/configuration/acme/dns01/google/#set-up-a-service-account)
------------------------------------------------------------------------------------------------------------------

cert-manager needs to be able to add records to CloudDNS in order to solve the DNS01 challenge. To enable this, a GCP service account must be created with the `dns.admin` role.

> Note: For this guide the `gcloud` command will be used to set up the service account. Ensure that `gcloud` is using the correct project and zone before entering the commands. These steps could also be completed using the Cloud Console.

PROJECT_ID=myproject-id

gcloud iam service-accounts create dns01-solver --display-name "dns01-solver"

In the command above, replace `myproject-id` with the ID of your project.

gcloud projects add-iam-policy-binding $PROJECT_ID \

--member serviceAccount:dns01-solver@$PROJECT_ID.iam.gserviceaccount.com \

--role roles/dns.admin

> **Note**: The use of the `dns.admin` role in this example role is for convenience. If you want to ensure cert-manager runs under a least privilege service account, you will need to create a custom role with the following permissions:
> 
> 
> *   `dns.resourceRecordSets.*`
> *   `dns.changes.*`
> *   `dns.managedZones.list`
> 
> 
> In case you do not use the `dns.admin` role, you will also need to make sure that the Service Account used by your GKE cluster (e.g. the Compute Engine default service account) has the `https://www.googleapis.com/auth/cloud-platform` access scope assigned to it. See [Access scopes in GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/access-scopes).

Use Static Credentials[](https://cert-manager.io/docs/configuration/acme/dns01/google/#use-static-credentials)
--------------------------------------------------------------------------------------------------------------

Follow the instructions in the following sections to deploy cert-manager using static credentials for the service account you created. You should rotate these credentials periodically.

### Create a Service Account Secret[](https://cert-manager.io/docs/configuration/acme/dns01/google/#create-a-service-account-secret)

To access this service account, cert-manager uses a key stored in a Kubernetes `Secret`. First, create a key for the service account and download it as a JSON file, then create a `Secret` from this file.

Keep the key file safe and do not share it, as it could be used to gain access access to your cloud resources. The key file can be deleted once it has been used to generate the `Secret`.

If you did not create the service account `dns01-solver` before, you need to create it first.

gcloud iam service-accounts create dns01-solver

Replace instances of `$PROJECT_ID` with the ID of your project.

gcloud iam service-accounts keys create key.json \

--iam-account dns01-solver@$PROJECT_ID.iam.gserviceaccount.com

kubectl create secret generic clouddns-dns01-solver-svc-acct \

--from-file=key.json

> Note: If you have already added the `Secret` but get an error: `...due to error processing: error getting clouddns service account: secret "XXX" not found`, the `Secret` may be in the wrong namespace. If you're configuring a `ClusterIssuer`, move the `Secret` to the `Cluster Resource Namespace` which is `cert-manager` by default. If you're configuring an `Issuer`, the `Secret` should be stored in the same namespace as the `Issuer` resource.

### Create an Issuer That Uses CloudDNS[](https://cert-manager.io/docs/configuration/acme/dns01/google/#create-an-issuer-that-uses-clouddns)

Next, create an `Issuer` (or `ClusterIssuer`) with a `cloudDNS` provider. An example `Issuer` manifest can be seen below with annotations.

apiVersion: cert-manager.io/v1

kind: Issuer

metadata:

name: example-issuer

spec:

acme:

...

solvers:

- dns01:

cloudDNS:

project: $PROJECT_ID

serviceAccountSecretRef:

name: clouddns-dns01-solver-svc-acct

key: key.json

For more information about `Issuers` and `ClusterIssuers`, see [Configuration](https://cert-manager.io/docs/configuration/).

Once an `Issuer` (or `ClusterIssuer`) has been created successfully, a `Certificate` can then be added to verify that everything works.

apiVersion: cert-manager.io/v1

kind: Certificate

metadata:

name: example-com

namespace: default

spec:

secretName: example-com-tls

issuerRef:

name: example-issuer

dnsNames:

- example.com

- www.example.com

For more details about `Certificates`, see [Usage](https://cert-manager.io/docs/usage/).

GKE Workload Identity[](https://cert-manager.io/docs/configuration/acme/dns01/google/#gke-workload-identity)
------------------------------------------------------------------------------------------------------------

If you are deploying cert-manager into a [Google Container Engine (GKE) cluster](https://cloud.google.com/kubernetes-engine/) with workload identity enabled, you can leverage workload identity to avoid creating and managing static service account credentials. The [workload identity how-to](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) provides more detail on how workload identity functions, but briefly workload identity allows you to link a Google service accounts (GSA) to Kubernetes service accounts (KSA). This GSA/KSA linking is two-way, i.e., you must establish the link in GCP _and_ Kubernetes. Once configured, workload identity allows Kubernetes pods running under a KSA to access the GCP APIs with the permissions of the linked GSA. The workload identity how-to also provides detailed instructions on how to enable workload identity in your GKE cluster. The instructions in the following sections assume you are deploying cert-manager to a GKE cluster with workload identity already enabled.

### Enable Ambient Credential Usage[](https://cert-manager.io/docs/configuration/acme/dns01/google/#enable-ambient-credential-usage)

'Ambient Credentials' are credentials drawn from the environment, metadata services, or local files which are not explicitly configured in the ClusterIssuer API object. When this flag is enabled Cert-Manager will access the GKE Metadata server for credentials. By default this is enabled for ClusterIssuer resources but is disabled for Issuer resources. To enable it for Issuer resources set the `--issuer-ambient-credentials` flag.

### Link KSA to GSA in GCP[](https://cert-manager.io/docs/configuration/acme/dns01/google/#link-ksa-to-gsa-in-gcp)

The cert-manager component that needs to modify DNS records is the pod created as part of the cert-manager deployment. The [standard methods for deploying cert-manager to Kubernetes](https://cert-manager.io/docs/installation/) create the cert-manager deployment in the cert-manager namespace and its pod spec specifies it runs under the cert-manager service account. To link the GSA you created above to the cert-manager KSA in the cert-manager namespace in your GKE cluster, run the following command.

gcloud iam service-accounts add-iam-policy-binding \

--role roles/iam.workloadIdentityUser \

--member "serviceAccount:$PROJECT_ID.svc.id.goog[cert-manager/cert-manager]" \

dns01-solver@$PROJECT_ID.iam.gserviceaccount.com

If your cert-manager pods are running under a different service account, replace `goog[cert-manager/cert-manager]` with `goog[NAMESPACE/SERVICE_ACCOUNT]`, where `NAMESPACE` is the namespace of the service account and `SERVICE_ACCOUNT` is the name of the service account.

### Link KSA to GSA in Kubernetes[](https://cert-manager.io/docs/configuration/acme/dns01/google/#link-ksa-to-gsa-in-kubernetes)

After deploying cert-manager, add the proper workload identity annotation to the cert-manager service account.

kubectl annotate serviceaccount --namespace=cert-manager cert-manager \

"iam.gke.io/gcp-service-account=dns01-solver@$PROJECT_ID.iam.gserviceaccount.com"

Again, if your cert-manager pods are running under a different service account, replace `--namespace=cert-manager cert-manager` with `--namespace=NAMESPACE SERVICE_ACCOUNT`, where `NAMESPACE` is the namespace of the service account and `SERVICE_ACCOUNT` is the name of the service account.

If you are deploying cert-manager using its helm chart, you can use the `serviceAccount.annotations` configuration parameter to add the above workload identity annotation to the cert-manager KSA.

### Create an Issuer That Uses CloudDNS[](https://cert-manager.io/docs/configuration/acme/dns01/google/#create-an-issuer-that-uses-clouddns-1)

Next, create an `Issuer` (or `ClusterIssuer`) with a `clouddns` provider. An example `Issuer` manifest can be seen below with annotations. Note that the issuer does not include a `serviceAccountSecretRef` property. Excluding this instructs cert-manager to use the default credentials provided by GKE workload identity.

apiVersion: cert-manager.io/v1

kind: Issuer

metadata:

name: example-issuer

spec:

acme:

...

solvers:

- dns01:

cloudDNS:

project: $PROJECT_ID

For more information about `Issuers` and `ClusterIssuers`, see [Configuration](https://cert-manager.io/docs/configuration/).

Once an `Issuer` (or `ClusterIssuer`) has been created successfully, a `Certificate` can then be added to verify that everything works.

apiVersion: cert-manager.io/v1

kind: Certificate

metadata:

name: example-com

namespace: default

spec:

secretName: example-com-tls

issuerRef:

name: example-issuer

dnsNames:

- example.com

- www.example.com

For more details about `Certificates`, see [Usage](https://cert-manager.io/docs/usage/).
