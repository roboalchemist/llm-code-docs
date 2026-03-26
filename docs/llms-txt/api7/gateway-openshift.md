# Source: https://docs.api7.ai/enterprise/deployment/gateway-openshift.md

# Install API7 Enterprise on OpenShift

This guide walks you through how to deploy API7 Enterprise on an OpenShift cluster.

## Architecture[â](#architecture "Direct link to Architecture")

### Overview[â](#overview "Direct link to Overview")

API7 Enterprise includes two sets of components:

1. Control Plane: API7 Dashboard, API7 DP Manager, Database (can use RDS instead), Other Components.
2. Data Plane: API7 Gateway.

![Architecture overview](https://static.api7.ai/uploads/2024/04/12/jdit8lBM_1.png)

### High Availability Deployment Pattern[â](#high-availability-deployment-pattern "Direct link to High Availability Deployment Pattern")

![high availability deployment architectural diagram](https://static.api7.ai/uploads/2024/04/12/71h8UOEy_2.png)

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

### Deploy an OpenShift Cluster[â](#deploy-an-openshift-cluster "Direct link to Deploy an OpenShift Cluster")

Have a running OpenShift Cluster:

![cluster overview](https://static.api7.ai/uploads/2026/01/21/K8zsBkzg_1-1-create-k8s-cluster.webp)

### Manage Security Context Constraints (SCCs)[â](#manage-security-context-constraints-sccs "Direct link to Manage Security Context Constraints (SCCs)")

[Security Context Constraints (SCCs)](https://docs.openshift.com/container-platform/3.11/architecture/additional_concepts/authorization.html#security-context-constraints) are a set of APIs on OpenShift used to manage security policy constraints for pods.

The SCCs enabled by default in OpenShift are extremely strict and require the process in the container to be read-only for the file system. Follow the [managing security context constraints](https://docs.openshift.com/dedicated/authentication/managing-security-context-constraints.html) doc to use a more flexible SCC `nonroot-v2` for API7 Enterprise.

### Configure OpenShift CLI[â](#configure-openshift-cli "Direct link to Configure OpenShift CLI")

Install [OpenShift CLI (oc)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.12/html/cli_tools/openshift-cli-oc#installing-openshift-cli).

Find the login command on the console:

![Find OpenShift Command Line Tools](https://static.api7.ai/uploads/2026/01/30/ZHStWhtx_1-2-login-command.webp)

![Copy OpenShift Login Command](https://static.api7.ai/uploads/2026/01/30/8PlEpcWk_1-3-copy-command-line.webp)

![Save OpenShift API Token](https://static.api7.ai/uploads/2026/01/21/ukRcUHCC_1-4-save-api-token.webp)

Log in to the OpenShift Cluster with your token and server address:

```
oc login \
  --token=sha256~Jk9gi578fm8tkdCje1qL0IyKc5ntqMOaladPjH3TuAk \
  --server=https://api.v6g2f6c4y1v1q7s.edff.p1.openshiftapps.com:6443
```

info

Make sure that your user account has the [`cluster-admin` role](https://docs.redhat.com/en/documentation/openshift_container_platform/3.11/html/architecture/additional-concepts#roles) to perform cluster management.

You should see a response similar to the following:

```
Logged into "https://api.v6g2f6c4y1v1q7s.edff.p1.openshiftapps.com:6443" as "admin" using the token provided.

You have access to 107 projects, the list has been suppressed. You can list all projects with 'oc projects'

Using project "default".
```

### Create a Project[â](#create-a-project "Direct link to Create a Project")

Create a project in the console:

![Create a project in the OpenShift console](https://static.api7.ai/uploads/2026/01/30/ujAEDe8C_2-1-create-openshift-project.webp)

![Create API7 project in the OpenShift console](https://static.api7.ai/uploads/2026/01/30/crMDxPMq_2-2-create-openshift-project.webp)

Alternatively, you can create a project using the CLI:

```
oc new-project api7-enterprise-project
```

The project name will be used as the Kubernetes namespace.

Switch the default project to `api7-enterprise-project`:

```
oc project api7-enterprise-project
```

## Install API7 Enterprise[â](#install-api7-enterprise "Direct link to Install API7 Enterprise")

### Add API7 Helm Chart Repository[â](#add-api7-helm-chart-repository "Direct link to Add API7 Helm Chart Repository")

Select **Repositories** under the **Helm** tab.

![Add API7 Helm chart repository](https://static.api7.ai/uploads/2026/01/30/6lQvDJ21_2-3-add-helm-charts-repo.webp)

Add the API7 repository `https://charts.api7.ai`.

![Fill in the details of the Helm chart repository](https://static.api7.ai/uploads/2026/01/30/aoSqgXNE_2-4-add-helm-charts-repo.webp)

### Install Control Plane[â](#install-control-plane "Direct link to Install Control Plane")

Select **Releases** under the **Helm** tab to create Helm releases.

![Create Helm Release](https://static.api7.ai/uploads/2026/01/21/fTzEK4Ws_3-4-create-helm-release.webp)

Select **Api7** first and click **Api7ee3** Helm chart to create.

![Select Control Plane Helm Chart](https://static.api7.ai/uploads/2026/01/30/9exLa0rV_2-5-add-control-plane.webp)

![install the API7 control plane chart](https://static.api7.ai/uploads/2026/01/21/XTXhE3hz_3-6-create-helm-release.webp)

Use the default latest chart version and paste the following snippet to replace the default values:

```
# adjust the values if needed for additional customizations
postgresql:
  primary:
    podSecurityContext:
      enabled: false
    containerSecurityContext:
      enabled: false
prometheus:
  server:
    podSecurityContext:
      enabled: false
    containerSecurityContext:
      enabled: false
```

Finish by clicking **Create**.

![Finished Configuration](https://static.api7.ai/uploads/2026/01/30/ombAXlmi_2-6-add-control-plane.webp)

You should see the components installed.

![Finished installation](https://static.api7.ai/uploads/2026/01/30/wOaQFR9p_2-7-add-control-plane.webp)

See all the created services:

```
kubectl get svc -owide -l app.kubernetes.io/name=api7ee3

NAME                       TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)             AGE   SELECTOR
api7ee3-dashboard          ClusterIP   172.30.39.137    <none>        7080/TCP,7443/TCP   35s   app.kubernetes.io/component=dashboard,app.kubernetes.io/instance=api7ee3,app.kubernetes.io/name=api7ee3
api7ee3-developer-portal   ClusterIP   172.30.114.132   <none>        4321/TCP            35s   app.kubernetes.io/component=developer-portal,app.kubernetes.io/instance=api7ee3,app.kubernetes.io/name=api7ee3
api7ee3-dp-manager         ClusterIP   172.30.232.75    <none>        7900/TCP,7943/TCP   35s   app.kubernetes.io/component=dp-manager,app.kubernetes.io/instance=api7ee3,app.kubernetes.io/name=api7ee3
```

### Activate License in the Dashboard[â](#activate-license-in-the-dashboard "Direct link to Activate License in the Dashboard")

Port forward the Dashboard service to `localhost:7443`:

```
kubectl port-forward svc/api7ee3-dashboard 7443:7443
```

If successful, you should be able to visit the dashboard at <https://localhost:7443>.

Log in with `admin` as both the username and the password:

![log in with admin/admin](https://static.api7.ai/uploads/2026/02/03/KXU3kjVD_dashboard-1.webp)

Then upload your license. If you do not have a license, you can [request a 30-day trial license](https://api7.ai/try?product=enterprise).

![upload license](https://static.api7.ai/uploads/2026/02/03/8urD3sVb_dashboard-2.webp)

Select **Activate**:

![activate the license](https://static.api7.ai/uploads/2026/02/03/OHo0UojD_dashboard-3.webp)

You should now be redirected to the Dashboard main interface.

### Add Control Plane Address[â](#add-control-plane-address "Direct link to Add Control Plane Address")

Before adding [Gateway instances](https://docs.api7.ai/enterprise/key-concepts/gateway-groups.md), first configure the connection address of the control plane.

In the same cluster, the data plane and control plane follow the format of `https://{service-name}.{namespace}.svc.cluster.local:7943`, regardless of whether they are deployed under the same namespace.

![Add DP Manager Address](https://static.api7.ai/uploads/2026/01/30/WZOJV7wt_3-1-add-control-plane-address.webp)

By default, API7 Gateway and the control plane will authenticate with mTLS for verification. Configure `https://{service-name}.{namespace}.svc.cluster.local:7943` as the DP manager address.

### Install Data Plane[â](#install-data-plane "Direct link to Install Data Plane")

#### Configure SCC for API7 Gateway[â](#configure-scc-for-api7-gateway "Direct link to Configure SCC for API7 Gateway")

API7 Gateway needs to generate local files at runtime, including `nginx.conf`, logs, and cached files. The `nonroot-v2` SCC is sufficient with the required permissions.

Create a service account:

```
oc create serviceaccount api7-gateway -n api7-enterprise-project
```

Create a role with `nonroot-v2` SCC:

```
oc create role api7-gateway \
  --verb=use \
  --resource=scc \
  --resource-name=nonroot-v2 \
  -n api7-enterprise-project
```

Bind the role to the service account:

```
oc create rolebinding api7-gateway \
  --role=api7-gateway \
  --serviceaccount=api7-enterprise-project:api7-gateway \
  -n api7-enterprise-project
```

#### Generate and Run Deployment Script[â](#generate-and-run-deployment-script "Direct link to Generate and Run Deployment Script")

Compared with Apache APISIX, API7 Enterprise introduces an additional logical grouping called [Gateway Group](https://docs.api7.ai/enterprise/key-concepts/gateway-groups.md), where you can manage different sets of Gateway instances with the same API7 Dashboard.

First, you should create or choose the target Gateway Group. In this guide, you will select the `default` gateway group. Then, select **Gateway Instances** and **Add Gateway Instance**:

![Add gateway instance](https://static.api7.ai/uploads/2026/01/21/zCvaUexE_4-2-deploy-instance.webp)

Switch to the **Kubernetes** tab and fill out the parameters. Once finished, click **Generate** to see the deployment script.

![Generate deployment script](https://static.api7.ai/uploads/2026/01/21/F5L2iuLz_4-3-deploy-instance.webp)

The generated script closes without a backslash (`\`). Ensure the `apisix.image.tag` line ends with `\` and that the additional `securityContext` settings are appended to the end of the Helm command.

The command should be similar to the following:

```
helm repo add api7 https://charts.api7.ai
helm repo update
cat > /tmp/tls.crt <<EOF
-----BEGIN CERTIFICATE-----
MIIBhjCCATigAwIBAgICBAAwBQYDK2VwMEQxCzAJBgNVBAYTAlVTMRMwEQYDVQQI
EwpDYWxpZm9ybmlhMQ0wCwYDVQQKEwRBUEk3MREwDwYDVQQDEwhBUEk3IEluYzAe
Fw0yNTEyMjIwMjQ1MTRaFw0zNjAxMTkwMjQ1MTRaMC4xDTALBgNVBAoTBEFQSTcx
HTAbBgNVBAMTFEdBVEVXQVktQ0EtVkVSU0lPTi0xMCowBQYDK2VwAyEAj7eA6FJM
3TV6J5TfRQ8cyDR53YwoH3i9SHo/yI3UJgajZDBiMA4GA1UdDwEB/wQEAwIHgDAT
BgNVHSUEDDAKBggrBgEFBQcDAjAtBgNVHQ4EJgQkY2I2M2I4MjgtZTAxNC00ZDNh
LTg1YzMtNDk4OTQyZjhkMGE0MAwGA1UdIwQFMAOAATEwBQYDK2VwA0EALyFv3wdZ
inocl8npyQcplqGk9RdLIcSSRaTBWag7fruRnPHMoUJ7WLt0c9LdtNYY65I/l1fi
mKiOgbdJJF4XDQ==
-----END CERTIFICATE-----
EOF
cat > /tmp/tls.key <<EOF
-----BEGIN PRIVATE KEY-----
MC4CAQAwBQYDK2VwBCIEIKeCxj1X5nGbk1DPPOjuHbD4onJnpD1m0FwBvaiN6UR4
-----END PRIVATE KEY-----
EOF
cat > /tmp/ca.crt <<EOF
-----BEGIN CERTIFICATE-----
MIIBeDCCASqgAwIBAgIRAMGXTGlvMme6bPd9BWxagY0wBQYDK2VwMEQxCzAJBgNV
BAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMQ0wCwYDVQQKEwRBUEk3MREwDwYD
VQQDEwhBUEk3IEluYzAgFw0yNTEyMjIwMjE4MzlaGA8yMDg2MDEwNjAyMTgzOVow
RDELMAkGA1UEBhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWExDTALBgNVBAoTBEFQ
STcxETAPBgNVBAMTCEFQSTcgSW5jMCowBQYDK2VwAyEAPCLKi9q/Mwe5HsmzgJyP
hYtvnHDxu15fQJBaoO/LjEujLzAtMA4GA1UdDwEB/wQEAwIChDAPBgNVHRMBAf8E
BTADAQH/MAoGA1UdDgQDBAExMAUGAytlcANBAKZrWTp4fogln52BvMmYr83oYSGU
S3yFz4wi1VW+0r47VSNnFkKSwcAiIpJ4Uu9MNJz4vbK3zDwrmLaMLS/ATAU=
-----END CERTIFICATE-----
EOF
kubectl create namespace api7-enterprise-project --dry-run=client -o yaml | kubectl apply -f -
kubectl create secret generic -n api7-enterprise-project api7-ee-3-gateway-tls --from-file=tls.crt=/tmp/tls.crt --from-file=tls.key=/tmp/tls.key --from-file=ca.crt=/tmp/ca.crt
helm upgrade --install -n api7-enterprise-project --create-namespace api7-ee-3-gateway api7/gateway \
  --set "etcd.auth.tls.enabled=true" \
  --set "etcd.auth.tls.existingSecret=api7-ee-3-gateway-tls" \
  --set "etcd.auth.tls.certFilename=tls.crt" \
  --set "etcd.auth.tls.certKeyFilename=tls.key" \
  --set "etcd.auth.tls.verify=true" \
  --set "gateway.tls.existingCASecret=api7-ee-3-gateway-tls" \
  --set "gateway.tls.certCAFilename=ca.crt" \
  --set "apisix.extraEnvVars[0].name=API7_GATEWAY_GROUP_SHORT_ID" \
  --set "apisix.extraEnvVars[0].value=default" \
  --set "etcd.host[0]=https://api7ee3-dp-manager.api7-enterprise-project.svc.cluster.local:7943" \
  --set "apisix.replicaCount=1" \
  --set "serviceAccount.name=api7-gateway" \
  --set "apisix.image.repository=api7/api7-ee-3-gateway" \
  --set "apisix.image.tag=3.9.2" \
  --set "apisix.securityContext.runAsNonRoot=true" \
  --set "apisix.securityContext.runAsUser=636"
```

â¶ `--set "apisix.securityContext.runAsNonRoot=true"`: Ensures the APISIX pod runs as a non-root user for OpenShift security compliance.

â· `--set "apisix.securityContext.runAsUser=636"`: Specifies the UID (636) for the APISIX pod process, matching OpenShift SCC requirements.

Install API gateway instances on your cluster.

Navigating back to the gateway instance, you should see a healthy gateway instance.

![Active Gateway Instance](https://static.api7.ai/uploads/2026/01/21/nIgpCxdC_4-4-deploy-instance.webp)

## Verify Installation[â](#verify-installation "Direct link to Verify Installation")

### Create a Sample Service[â](#create-a-sample-service "Direct link to Create a Sample Service")

Navigate to the "Published Services" page and add a service manually.

![Add New Service](https://static.api7.ai/uploads/2026/01/21/Axd2D4sD_5-1-create-service.webp)

Create a service `httpbin` and add an upstream node `httpbin.org` with a port `80`. Configure a route to `/anything` endpoint and allow only the `GET` method.

You should see the service now shows the created route:

![Service and Route Configuration](https://static.api7.ai/uploads/2026/01/21/JayJHGZs_5-2-create-service.webp)

### Port Forward Gateway Service[â](#port-forward-gateway-service "Direct link to Port Forward Gateway Service")

Before you can send a request to the Gateway, you should first port forward the gateway listening port to localhost.

First, list all Services to check the gateway service name:

```
kubectl get svc
```

The gateway service name is `api7-ee-3-gateway-gateway`:

```
NAME                        TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
api7-ee-3-gateway-gateway   NodePort    172.30.197.112   <none>        80:30515/TCP,443:31177/TCP   4h58m
api7-postgresql             ClusterIP   172.30.188.65    <none>        5432/TCP                     5h54m
api7-postgresql-hl          ClusterIP   None             <none>        5432/TCP                     5h54m
api7-prometheus-server      ClusterIP   172.30.6.167     <none>        9090/TCP                     5h54m
api7ee3-dashboard           ClusterIP   172.30.39.137    <none>        7080/TCP,7443/TCP            5h54m
api7ee3-developer-portal    ClusterIP   172.30.114.132   <none>        4321/TCP                     5h54m
api7ee3-dp-manager          ClusterIP   172.30.232.75    <none>        7900/TCP,7943/TCP            5h54m
```

Next, forward the gateway port `80` to `localhost:9080`:

```
kubectl port-forward svc/api7-ee-3-gateway-gateway 9080:80
```

### Send a Request[â](#send-a-request "Direct link to Send a Request")

This request receives the correct response, which means the installation is successful.

```
curl "http://127.0.0.1:9080/anything" -i
```

You should receive an `HTTP/1.1 200 OK` response similar to the following:

```
{
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Host": "localhost",
    "User-Agent": "curl/8.7.1",
    "X-Amzn-Trace-Id": "Root=1-697043ec-4be975291786b3e944175f56",
    "X-Forwarded-Host": "localhost"
  },
  "json": null,
  "method": "GET",
  "origin": "127.0.0.1, 3.1.235.149",
  "url": "http://localhost/anything"
}
```

## What's Next[â](#whats-next "Direct link to What's Next")

In addition to publishing services through the Dashboard UI, API7 provides a command line tool that can operate declarative configuration, so you can integrate API7 Operations with internal GitOps. See Managing [APISIX Declaratively with APISIX Declarative CLI (ADC)](https://api7.ai/blog/managing-apisix-declaratively).

See [Getting Started tutorials](https://docs.api7.ai/enterprise/getting-started/install-api7-ee.md) to learn more about how to work with ADC.

## FAQ[â](#faq "Direct link to FAQ")

### How to Connect to Existing PostgreSQL?[â](#how-to-connect-to-existing-postgresql "Direct link to How to Connect to Existing PostgreSQL?")

Configure your database DSN in the [Helm values file](https://github.com/api7/api7-helm-chart/blob/main/charts/api7/values.yaml):

```
dashboard_configuration:
  database:
    dsn: "postgres://api7ee:changeme@api7-postgresql:5432/api7ee"

dp_manager_configuration:
  database:
    dsn: "postgres://api7ee:changeme@api7-postgresql:5432/api7ee"
```
