# Source: https://docs.acceldata.io/documentation/dataplane-installation-prerequisites.md

# Data Plane Installation Prerequisites

The **Data Plane** is the execution layer of ADOC that connects to your data sources and performs tasks like crawling, profiling, and rule execution, while securely following the access and policies set in the control plane.

Before installing the Acceldata Data Plane, review the following prerequisites. These requirements ensure your infrastructure is ready for a secure, stable, and scalable deployment.

> ADOC Control Plane version **26.2.0** is compatible with Data Plane versions **26.1.0**, **4.10.0**, and **4.9.0**. If you're unsure which versions you're using, contact your Acceldata admin before proceeding.

## 1. User Permissions

Before deploying a Data Plane, ensure your user account in the [ADOC Control Plane](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/adoc-architecture-an-overview#key-components) has the necessary [Tenant Role](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/roles-and-permissions#1-tenant-roles) **permissions** to:

- Register new Data Planes
- Manage existing Data Plane configurations
- Perform installations via automatic or manual methods

These permissions are granted through **Tenant Roles** (platform-wide roles defined in ADOC). For example, a role such as `tenant_admin` or a custom role with Data Plane management privileges must be assigned to your account. Without the correct role-based permissions, you will not be able to create, update, or delete Data Planes from the Control Plane UI, and installation or upgrade tasks will fail.

If you’re unsure which roles provide Data Plane access, contact your ADOC administrator or refer to the **Tenant Roles** section of this guide.

## 2. Kubernetes Cluster Requirements

To deploy the Data Plane, you must have access to a Kubernetes cluster with the following minimum specifications:

| Resource | Minimum Requirement | 
| ---- | ---- | 
| Nodes | 4 | 
| CPU | 4 cores per node | 
| Memory | 32 GB per node | 
| Disk | 80 GB per node | 


These specs ensure Data Plane services (like crawlers, Spark executors, and profiling jobs) have enough compute and memory to run in parallel. Insufficient resources can lead to job failures, long scan durations, or unexpected container restarts.

> For best performance and security, we recommend deploying the Data Plane on a **dedicated Kubernetes cluster**. A dedicated cluster ensures:> > - **Isolation** – ADOC workloads don’t compete with other applications, reducing performance bottlenecks and security risks.> - **Predictable scaling** – Resources like CPU, memory, and storage are fully available for Data Plane tasks such as crawling, profiling, and rule execution.> - **Simplified upgrades** – Version upgrades and configuration changes affect only ADOC components, not unrelated workloads.> > **Using a Shared Cluster** > > While ADOC does support deployment on shared Kubernetes clusters, this approach may require additional considerations:> > - **Custom resource tuning** (quotas, limits, node pools) to avoid contention with other applications.> - **Stronger RBAC and namespace isolation** to ensure ADOC services do not interfere with other tenants.> - **Monitoring overhead** – You may need to track ADOC performance more closely, since external workloads could impact job execution times.> > **How to Decide**> > - Choose a **dedicated cluster** if you are running ADOC in production, handling sensitive data, or expect high data plane workloads.> - A **shared cluster** may be acceptable for proof-of-concept (POC) environments, testing, or smaller teams with limited infrastructure.

**Kubernetes Version Compatibility**

Acceldata supports Kubernetes **versions up to 1.33** for Data Plane deployment. Using unsupported versions may result in failed workloads, broken Helm charts, or Spark driver crashes. Please verify your Kubernetes version before continuing.

## 3. Kubernetes Permissions

The permissions required depend on whether you are deploying the Data Plane **automatically** (via the Control Plane UI) or **manually** (using Helm or YAML manifests).

### Why These Permissions Are Needed

During deployment, the Acceldata deployer must be able to:

- Create and manage **Kubernetes Service Accounts** for ADOC services.
- Deploy and update **Jobs, Deployments, and StatefulSets** for Spark, crawlers, and supporting services.
- Configure **ConfigMaps and Secrets** to securely pass runtime settings and credentials.
- Set up **DaemonSets** for log collection.
- Manage **RBAC Roles and RoleBindings** required for ADOC components to function within their namespace.

Without these permissions, the deployer cannot configure workloads correctly, and automatic installation will fail.

### Automatic Deployment (via Control Plane UI)

If you use the automated deployer, ensure that:

1. The Acceldata Deployer pod is installed and running in your cluster. 
2. The user or service account running the deployer has at least the following Kubernetes roles within the ADOC namespace:
    1. **create, get, list, update, delete** on: 
        1. Pods, Services, Deployments, StatefulSets, Jobs, DaemonSets
        2. ConfigMaps, Secrets, PersistentVolumeClaims
        3. Roles, RoleBindings, ServiceAccounts

    2. **get, list, watch** **on:**
        1. Nodes, Namespaces, Events

In most environments, this is achieved by granting the deployer service account a **namespace-level admin role** or a **cluster role binding** with equivalent permissions. 

**ClusterRole (cluster-resource-manager)**

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: cluster-resource-manager
rules:
  - apiGroups: ["rbac.authorization.k8s.io"]
    resources: ["clusterroles", "clusterrolebindings"]
    verbs: ["get", "list", "watch", "update", "patch"]
```



**Role (resource-manager)**

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: resource-manager
  namespace: <YOUR_NAMESPACE>
rules:
  - apiGroups: [""]
    resources: ["serviceaccounts", "configmaps", "services", "secrets"]
    verbs: ["create", "delete", "get", "list", "patch", "update", "watch"]
  - apiGroups: ["apps"]
    resources: ["deployments"]
    verbs: ["create", "delete", "get", "list", "patch", "update", "watch"]
  - apiGroups: ["batch"]
    resources: ["jobs", "cronjobs"]
    verbs: ["create", "delete", "get", "list", "patch", "update", "watch"]
  - apiGroups: ["rbac.authorization.k8s.io"]
    resources: ["roles", "rolebindings"]
    verbs: ["create", "delete", "get", "list", "patch", "update", "watch"]
```



### Manual Deployment

If you deploy manually (Helm/YAML), you don’t need elevated deployer permissions because you (or your admin team) will apply manifests directly. However, the service accounts created for ADOC services (Spark jobs, crawlers, etc.) must still be granted the same runtime permissions listed above.

If you are using Helm to deploy the Data Plane manually, ensure your account has the following roles:

**Role (helm-installer-role)**

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: helm-installer-role
  namespace: your-namespace
rules:
  - apiGroups: [""]
    resources: ["serviceaccounts", "secrets", "configmaps", "services"]
    verbs: ["create", "get", "list", "watch", "update", "delete"]
  - apiGroups: ["rbac.authorization.k8s.io"]
    resources: ["roles", "rolebindings"]
    verbs: ["create", "get", "list", "watch", "update", "delete"]
  - apiGroups: ["apps"]
    resources: ["deployments"]
    verbs: ["create", "get", "list", "watch", "update", "delete"]
  - apiGroups: ["autoscaling"]
    resources: ["horizontalpodautoscalers"]
    verbs: ["create", "get", "list", "watch", "update", "delete"]
  - apiGroups: ["batch"]
    resources: ["jobs", "cronjobs"]
    verbs: ["create", "get", "list", "watch", "update", "delete"]
  - apiGroups: ["sparkoperator.k8s.io"]
    resources: ["scheduledsparkapplications", "sparkapplications"]
    verbs: ["create", "get", "list", "watch", "update", "delete"]
```



**ClusterRole (helm-installer-clusterrole)**

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: helm-installer-clusterrole
rules:
  - apiGroups: ["apiextensions.k8s.io"]
    resources: ["customresourcedefinitions"]
    verbs: ["create", "get", "list", "watch", "delete"]
  - apiGroups: ["rbac.authorization.k8s.io"]
    resources: ["clusterroles", "clusterrolebindings"]
    verbs: ["create", "get", "list", "watch", "update", "delete"]
```



## 4. Network Connectivity Requirements

The Data Plane relies on outbound connectivity to the Acceldata platform for registration, image pulling, metrics upload, and control messaging. If these domains are blocked, Data Plane services may fail to start, register, or push metadata.

Ensure that the following domains and ports are whitelisted on your cluster:

| Domain | Port | Purpose | 
| ---- | ---- | ---- | 
| accounts.acceldata.app | 443 | For account auth and registration | 
| &lt;tenant&gt;.acceldata.app | 443 | For sending analytics and metadata | 
| dataplane-v2.acceldata.app | 443 | Control flow and command execution | 
| public.ecr.aws | 443 | To fetch containers from public registry | 
| registry.acceldata.app | 443 | New registry for container images | 
| 191579300362.dkr.ecr.us-east-1.amazonaws.com | 443 | Legacy registry endpoint | 


If you are using an HTTP proxy, allow SSL bypass for control flow communication with dataplane.acceldata.app.

> > When configuring the VPC for a Data Plane deployment, ensure that the CIDR range provides sufficient IP addresses to support both installation and ongoing operation. As a minimum, use a **/24 CIDR range** (256 IP addresses). Smaller CIDR ranges (for example, **/26 or /27**) can lead to insufficient IP capacity, which may cause deployment failures or operational issues during scaling or runtime.

## 5. Run Preflight Checks

Acceldata provides a preflight validation tool that checks cluster readiness, network access, and deployment capacity.

This tool validates your cluster before installation to help catch common issues like:

- Missing node resources
- Blocked network routes
- Proxy misconfigurations
- Lacking required permissions

Running this tool early prevents partial installations, deployment errors, and time-consuming debugging later.

What it checks:

- ADOC Control Plane connectivity
- Data source egress (TCP, UDP, HTTP)
- Cluster sizing and namespace quotas

> If the preflight tool returns errors, installation **will not proceed until the issues are resolved**. The output highlights which check failed (e.g., network unreachable, insufficient quota).> > Typical outcomes and next steps:> > - **Network failures** → check firewall, proxy, or security group settings.> - **Quota/resource failures** → request more CPU/memory from your cluster admin or adjust the namespace limits.> - **Permission errors** → verify your Kubernetes role bindings include the required cluster-level permissions (as outlined in the Kubernetes Permissions section).

#### How to Run:

```bash
./dataplane-cli preflight-launcher --config-file=./config.yaml -n <adoc_dp_namespace>
```



### 5.1 Cloud Provider and Spark Compatibility

Before setting up your Data Plane, ensure your cloud provider supports the Spark type you plan to use:

| Cloud Provider | Supported Spark Types | Spark Version | 
| ---- | ---- | ---- | 
| AWS | YuniKorn, Databricks | 3.2.x | 
| Azure | YuniKorn, Databricks | 3.2.x | 
| GCS | YuniKorn, Dataproc | 3.2.x | 


Spark types like Databricks and Dataproc are only supported on certain clouds. Pick the right one to avoid job execution issues later.

## 6. Example Preflight Config File

```yaml
egressTCPConnection: 
  - host: 12.128.0.6
    port: 5120
  - host: 12.128.0.6
    port: 443
egressHttpConnection:
  proxy:
    enabled: false
    host: egress.example.com
    port: 3148
    user: proxyuser
    password: proxypass
  urls:
    - scheme: https
      host: acceldata.acceldata.app
      port: 443
      path: /
quota:
  memory: 20Gi
  cpu: 10
  ephemerial: 100Gi
nodes:
  quantity: 4
  spec:
    cpu: 4
    memory: 32Gi
    disk: 80Gi
```



Note This tool **does not validate credentials or functional access** to data sources. It only checks the environment (network, sizing, and cluster setup). After resolving environment issues, you’ll still need to validate **data source connectivity and authentication** during configuration.