# Source: https://docs.datadoghq.com/cloudprem/configure/azure_config.md

---
title: Azure Configuration
description: Learn how to configure Azure for CloudPrem
breadcrumbs: Docs > CloudPrem > Configure CloudPrem > Azure Configuration
source_url: https://docs.datadoghq.com/configure/azure_config/index.html
---

# Azure Configuration

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Before you install CloudPrem on Azure, you must set up a set of supporting infrastructure resources. These components provide the foundational compute, storage, database, and networking services that CloudPrem depends on. This documentation outlines all the resources you must set up in your Azure account before you proceed to the installation steps described in the [Azure AKS Installation Guide](https://docs.datadoghq.com/cloudprem/install/azure_aks).

### Infrastructure Requirements{% #infrastructure-requirements %}

Here are the components you must provision:

- **Azure Kubernetes Service (AKS)**: A running AKS cluster sized for your expected CloudPrem workload.
- **PostgreSQL Flexible Server**: An Azure Database for PostgreSQL instance that CloudPrem will use to store its metadata.
- **Blob Storage container**: An Azure Storage container to hold CloudPrem logs.
- **Client Identity and permissions**: An Azure AD application with read/write access to the storage container.
- **NGINX Ingress Controller**: Installed on the AKS cluster to route external traffic to CloudPrem services.
- **Datadog Agent**: Deployed on the AKS cluster to collect and send logs to CloudPrem.

## Azure Kubernetes Service (AKS){% #azure-kubernetes-service-aks %}

CloudPrem runs entirely on Kubernetes. You need an AKS cluster with sufficient CPU, memory, and disk space configured for your workload. See the Kubernetes cluster sizing recommendations for guidance.

### Deploy the AKS cluster{% #deploy-the-aks-cluster %}

- [Deploy an AKS cluster with the Azure CLI](https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-cli)
- [Deploy an AKS cluster with Terraform](https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-terraform?pivots=development-environment-azure-cli)

### Verify cluster connectivity and health{% #verify-cluster-connectivity-and-health %}

To confirm the cluster is reachable and nodes are in the `Ready` state, run the following command:

```shell
kubectl get nodes -o wide
```

## Azure PostgreSQL Flexible Server{% #azure-postgresql-flexible-server %}

CloudPrem stores its metadata and configuration in a PostgreSQL database. Datadog recommends the Azure Database for PostgreSQL Flexible Server. It must be reachable from the AKS cluster, ideally with private networking enabled. See the Postgres sizing recommendations for details.

### Create the PostgreSQL database{% #create-the-postgresql-database %}

- [Create an Azure Database for PostgreSQL Flexible Server using the Azure CLI](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/quickstart-create-server?tabs=portal-create-flexible%2Cportal-get-connection%2Cportal-delete-resources)
- [Create an Azure Database for PostgreSQL Flexible Server using Terraform](https://learn.microsoft.com/en-us/azure/developer/terraform/deploy-postgresql-flexible-server-database?tabs=azure-cli)

### Verify database connectivity{% #verify-database-connectivity %}

{% alert level="info" %}
For security, create a dedicated database and user for CloudPrem, and grant the user rights only on that database, not cluster-wide.
{% /alert %}

Connect to your PostgreSQL database from within the AKS network using the PostgreSQL client, `psql`. First, start an interactive pod in your Kubernetes cluster using an image that includes `psql`:

```shell
kubectl run psql-client \
  -n <NAMESPACE_NAME> \
  --rm -it \
  --image=bitnami/postgresql:latest \
  --command -- bash
```

Then, run the following command directly from the shell, replacing the placeholder values with your actual values:

```shell
psql "host=<HOST> \
      port=<PORT> \
      dbname=<DATABASE> \
      user=<USERNAME> \
      password=<PASSWORD>"
```

If successful, you should see a prompt similar to:

```shell
psql (15.2)
SSL connection (protocol: TLS...)
Type "help" for help.

<DATABASE>=>
```

## Blob Storage Container{% #blob-storage-container %}

CloudPrem uses Azure Blob Storage to persist logs. Create a dedicated container for this purpose.

### Create a Blob Storage container{% #create-a-blob-storage-container %}

Use a dedicated container per environment (for example, `cloudprem-prod`, `cloudprem-staging`), and assign least-privilege RBAC roles at the container level, rather than at the storage account scope.

- [Create a Blob Storage container using the Azure CLI](https://learn.microsoft.com/en-us/azure/storage/blobs/blob-containers-cli#create-a-container)
- [Create a Blob Storage container using Terraform](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/storage_container)

## Client Identity and permissions{% #client-identity-and-permissions %}

An Azure AD application must be granted read/write access to the Blob Storage container. Register a dedicated application for CloudPrem and assign the corresponding service principal the `Contributor` role on the Blob Storage container created above.

### Register the application{% #register-the-application %}

[Register an application in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app)

### Assign Contributor role{% #assign-contributor-role %}

[Assign an Azure role for access to blob data](https://learn.microsoft.com/en-us/azure/storage/blobs/assign-azure-role-data-access?tabs=portal)

## NGINX Ingress Controller{% #nginx-ingress-controller %}

### Public NGINX Ingress Controller{% #public-nginx-ingress-controller %}

The public ingress is essential for enabling Datadog's control plane and query service to manage and query CloudPrem clusters over the public internet. It provides secure access to the CloudPrem gRPC API through the following mechanisms:

- Creates an internet-facing Azure Load Balancer that accepts traffic from Datadog services
- Implements TLS encryption with termination at the ingress controller level
- Uses HTTP/2 (gRPC) for communication between Datadog and CloudPrem clusters
- Requires mutual TLS (mTLS) authentication where Datadog services must present valid client certificates
- Configures the controller in TLS passthrough mode to forward client certificates to CloudPrem pods with the `ssl-client-cert` header
- Rejects requests that are missing valid client certificates or the certificate header

Use the following `nginx-public.yaml` Helm values file in order to create the public NGINX Ingress Controller:

In the `nginx-public.yaml` file:

```yaml
controller:
  electionID: public-ingress-controller-leader
  ingressClass: nginx-public
  ingressClassResource:
    name: nginx-public
    enabled: true
    default: false
    controllerValue: k8s.io/public-ingress-nginx
  service:
    type: LoadBalancer
    annotations:
      service.beta.kubernetes.io/azure-load-balancer-health-probe-request-path: /healthz
```

Then, install the controller with Helm using the following command:

```shell
helm upgrade --install nginx-public ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace nginx-ingress-public \
  --create-namespace \
  -f nginx-public.yaml
```

Verify that the controller pod is running:

```shell
kubectl get pods -n nginx-ingress-public -l app.kubernetes.io/component=controller
```

Verify that the service exposes an external IP:

```shell
kubectl get svc -n nginx-ingress-public -l app.kubernetes.io/component=controller
```

### Internal NGINX Ingress Controller{% #internal-nginx-ingress-controller %}

The internal ingress enables log ingestion from Datadog Agents and other log collectors within your environment through HTTP. Use the following `nginx-internal.yaml` Helm values file in order to create the public NGINX Ingress Controller:

In the `nginx-internal.yaml` file:

```yaml
controller:
  electionID: internal-ingress-controller-leader
  ingressClass: nginx-internal
  ingressClassResource:
    name: nginx-internal
    enabled: true
    default: false
    controllerValue: k8s.io/internal-ingress-nginx
  service:
    type: LoadBalancer
    annotations:
      service.beta.kubernetes.io/azure-load-balancer-internal: true
      service.beta.kubernetes.io/azure-load-balancer-health-probe-request-path: /healthz
```

Then, install the controller with Helm using the following command:

```shell
helm upgrade --install nginx-internal ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace nginx-ingress-internal \
  --create-namespace \
  -f nginx-internal.yaml
```

Verify that the controller pod is running:

```shell
kubectl get pods -n nginx-ingress-internal -l app.kubernetes.io/component=controller
```

Verify that the service exposes an external IP:

```shell
kubectl get svc -n nginx-ingress-internal -l app.kubernetes.io/component=controller
```

## DNS{% #dns %}

Optionally, you can add a DNS entry pointing to the IP of the public load balancer, so future IP changes won't require updating the configuration on the Datadog side.

## Next steps{% #next-steps %}

After completing the Azure configuration

1. **Install CloudPrem on Azure AKS** - Follow the [Azure AKS Installation Guide](https://docs.datadoghq.com/cloudprem/install/azure_aks) to deploy CloudPrem
1. **Set up log ingestion** - Configure [log ingestion](https://docs.datadoghq.com/cloudprem/ingest_logs/) to start sending logs to CloudPrem

## Further reading{% #further-reading %}

- [Install CloudPrem on Azure AKS](https://docs.datadoghq.com/cloudprem/install/azure_aks/)
- [Configure Log Ingestion](https://docs.datadoghq.com/cloudprem/ingest_logs/)
