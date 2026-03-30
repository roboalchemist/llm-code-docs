# Source: https://docs.api7.ai/ingress-controller/installation/openshift.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/deployment/openshift.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/deployment/openshift.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/deployment/openshift.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/deployment/openshift.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/deployment/openshift.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/deployment/openshift.md

# Source: https://docs.api7.ai/enterprise/3.8.x/deployment/openshift.md

# Source: https://docs.api7.ai/enterprise/3.7.x/deployment/openshift.md

# Source: https://docs.api7.ai/enterprise/3.6.x/deployment/openshift.md

# Source: https://docs.api7.ai/enterprise/3.5.x/deployment/openshift.md

# Source: https://docs.api7.ai/enterprise/3.4.x/deployment/openshift.md

# Source: https://docs.api7.ai/enterprise/3.3.x/deployment/openshift.md

# Install API7 Enterprise on OpenShift

This guide walks you through how to deploy API7 Enterprise on an OpenShift cluster.

## Architecture[â](#architecture "Direct link to Architecture")

### Overview[â](#overview "Direct link to Overview")

API7 Enterprise includes two sets of components:

1. Control Plane: API7 Dashboard, API7 DP Manager, Database (can use RDS instead), Other Components.
2. Data Plane: API7 Gateway

![Architecture overview](https://static.api7.ai/uploads/2024/04/12/jdit8lBM_1.png)

### High Availability Deployment Pattern[â](#high-availability-deployment-pattern "Direct link to High Availability Deployment Pattern")

![high availability deployment architectural diagram](https://static.api7.ai/uploads/2024/04/12/71h8UOEy_2.png)

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

### Deploy an OpenShift Cluster[â](#deploy-an-openshift-cluster "Direct link to Deploy an OpenShift Cluster")

Have a running OpenShift Cluster:

![cluster overview](https://static.api7.ai/uploads/2024/04/12/d0bHSGin_3.png)

![cluster machine pool](https://static.api7.ai/uploads/2024/04/12/HGuUkgnc_4.png)

### Manage Security Context Constraints (SCCs)[â](#manage-security-context-constraints-sccs "Direct link to Manage Security Context Constraints (SCCs)")

[Security Context Constraints (SCCs)](https://docs.openshift.com/container-platform/3.11/architecture/additional_concepts/authorization.html#security-context-constraints) are a set of APIs on OpenShift used to manage security policy constraints for pods.

The SCCs enabled by default in OpenShift are extremely strict and requires the process in the container to be read-only for the file system. Follow the [managing security context constraints](https://docs.openshift.com/dedicated/authentication/managing-security-context-constraints.html) doc to use a more flexible SCC `nonroot-v2` for API7 Enterprise.

### Configure OpenShift CLI[â](#configure-openshift-cli "Direct link to Configure OpenShift CLI")

Install [OpenShift CLI (oc)](https://docs.openshift.com/container-platform/4.12/cli_reference/openshift_cli/getting-started-cli.html#installing-openshift-cli) or download it from the console:

![Download the OpenShift CLI (oc) on the console](https://static.api7.ai/uploads/2024/04/12/HprnNscc_5.png)

Find the login command on the console:

![copy login command from console](https://static.api7.ai/uploads/2024/04/12/r4W6gsFW_6.png)

Log in to the OpenShift Cluster with your token and server address:

```
oc login \
  --token=sha256~pesd0RAyKiKJLkkKJ4Oh2lmy4KSX9b5J6Fc24FYM2EQ \
  --server=https://api.api7.93ew.p1.openshiftapps.com:6443
```

info

Make sure that your user account has the [`cluster-admin` role](https://docs.openshift.com/container-platform/3.11/architecture/additional_concepts/authorization.html#roles) to perform cluster management.

You should see a response similar to the following:

```
Logged into "https://api.api7.93ew.p1.openshiftapps.com:6443" as "admin" using the token provided.

You have access to 102 projects, the list has been suppressed. You can list all projects with 'oc projects'

Using project "default".
```

### Create a Project[â](#create-a-project "Direct link to Create a Project")

Create a project in the console:

![Create a project in the OpenShift console](https://static.api7.ai/uploads/2024/04/12/1lDVSpeZ_7.png)

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

Add the API7 repository `https://charts.api7.ai`:

![Add API7 Helm chart repository](https://static.api7.ai/uploads/2024/04/12/BcInXcFE_8.png)

![Fill in the details of the Helm chart repository](https://static.api7.ai/uploads/2024/04/12/Ks7XziHD_9.png)

### Install Control Plane[â](#install-control-plane "Direct link to Install Control Plane")

Select `Api7ee3` Helm chart and create:

![select the control plane Helm chart](https://static.api7.ai/uploads/2024/04/12/rFu1U2yQ_10.png)

![install the control plane chart](https://static.api7.ai/uploads/2024/04/12/3B6MIiFN_11.png)

Select the chart version:

![select the chart version](https://static.api7.ai/uploads/2024/04/12/DNvpvtXD_12.png)

Paste the following snippet to replace the default values:

```
# adjust the values if needed for additional customizations
postgresql:
  primary:
    podSecurityContext:
      fsGroup: 1001020000
    containerSecurityContext:
      runAsUser: 1001020000
prometheus:
  server:
    podSecurityContext:
      fsGroup: 1001020000
    containerSecurityContext:
      runAsUser: 1001020000
```

Finish by clicking **Create**. You should see the components installed:

![Finished installation](https://static.api7.ai/uploads/2024/04/12/ekJUa3W0_13.png)

See all the created services:

```
kubectl get svc -owide -l app.kubernetes.io/name=api7ee3

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)             AGE   SELECTOR
api7ee3-dashboard    ClusterIP   172.30.249.55   <none>        7080/TCP            28m  app.kubernetes.io/component=dashboard,app.kubernetes.io/instance=api7ee3,app.kubernetes.io/name=api7ee3
api7ee3-dp-manager   ClusterIP   172.30.43.83    <none>        7900/TCP,7943/TCP   28m   app.kubernetes.io/component=dp-manager,app.kubernetes.io/instance=api7ee3,app.kubernetes.io/name=api7ee3
```

### Activate License in the Dashboard[â](#activate-license-in-the-dashboard "Direct link to Activate License in the Dashboard")

Port forward the Dashboard service to `localhost:7443`:

```
kubectl port-forward svc/api7ee3-dashboard 7443:7443
```

If successful, you should be able to visit the dashboard at <https://localhost:7443>.

Log in with `admin` as both the username and the password:

![log in with admin/admin](https://static.api7.ai/uploads/2024/04/13/7OvbvbFZ_14.png)

Then upload your license. If you do not have a license, you can [request a 30-day trial license](https://api7.ai/try?product=enterprise).

![upload license](https://static.api7.ai/uploads/2024/08/09/1V8Tgsw3_generate-licnese-1.png)

Select **Activate**:

![activate the license](https://static.api7.ai/uploads/2024/08/09/zMljBUnq_updated-license.png)

You should now be redirected to the Dashboard main interface.

### Add Control Plane Address[â](#add-control-plane-address "Direct link to Add Control Plane Address")

Before adding more [Gateway instances](https://docs.api7.ai/enterprise/3.3.x/key-concepts/gateway-groups.md), first configure the connection address of the control plane.

In the same cluster, the data plane and control plane follow the format of `https://{service-name}.{namespace}.svc.cluster:7943`, regardless of whether they are deployed under the same namespace.

![add control plane address](https://static.api7.ai/uploads/2024/08/09/Zzgc5aic_20240809-150435.jpeg)

By default, API7 Gateway and control plane will authenticate with mTLS for verification. You should configure `https://{service-name}.{namespace}.svc.cluster:7943` as the control plane address.

### Install Data Plane[â](#install-data-plane "Direct link to Install Data Plane")

#### Configure SCC for API7 Gateway[â](#configure-scc-for-api7-gateway "Direct link to Configure SCC for API7 Gateway")

API7 Gateway needs to generate local files at runtime, including `nginx.conf`, logs, and cached files. The `nonroot-v2` SCC is sufficient with the required permissions.

Create a service account:

```
oc create serviceaccount api7-gateway
```

Create a role with `nonroot-v2` SCC:

```
oc create role api7-gateway \
  --verb=use \
  --resource=scc 
  --resource-name=nonroot-v2
```

Bind the role to the service account:

```
oc create rolebinding api7-gateway \
  --role=api7-gateway
  --serviceaccount=api7-enterprise-project:api7-gateway
```

#### Generate and Run Deployment Script[â](#generate-and-run-deployment-script "Direct link to Generate and Run Deployment Script")

Compared with Apache APISIX, API7 Enterprise introduces an additional logical grouping called [Gateway Group](https://docs.api7.ai/enterprise/3.3.x/key-concepts/gateway-groups.md), where you can manage different sets of Gateway instances with the same API7 Dashboard.

First, you should create or choose the target Gateway Group. In this guide, you will use the `default` gateway group:

![Find the default gateway group in the Dashboard](https://static.api7.ai/uploads/2024/04/12/MtWaiIn5_18.png)

Next, select **Add Gateway Instance**:

![Add gateway instance](https://static.api7.ai/uploads/2024/04/12/aB0zuBWZ_19.png)

Switch to the **Kubernetes** tab and fill out the parameters. Once finished, click **Generate** to see the deployment script.

![Generate deployment script](https://static.api7.ai/uploads/2024/08/09/hCwFcxd0_updated-gateway-script.png)

Copy the generated script and set the additional `securityContext`. The command should be similar to the following:

```
helm repo add api7 https://charts.api7.ai
helm repo update
cat > /tmp/tls.crt <<EOF
-----BEGIN CERTIFICATE-----
MIIBiDCCATqgAwIBAgICBAAwBQYDK2VwMEQxCzAJBgNVBAYTAlVTMRMwEQYDVQQI
EwpDYWxpZm9ybmlhMQ0wCwYDVQQKEwRBUEk3MREwDwYDVQQDEwhBUEk3IEluYzAe
Fw0yNDA4MDkwOTQwNDJaFw0yNTA5MDgwOTQwNDJaMDAxDTALBgNVBAoTBEFQSTcx
HzAdBgNVBAMTFmFwaTdlZTMtYXBpc2l4LWdhdGV3YXkwKjAFBgMrZXADIQBSZVOn
f8Xu63XylUmRi8jvx0G4XUtPQGoYHdSTeyLF36NkMGIwDgYDVR0PAQH/BAQDAgeA
MBMGA1UdJQQMMAoGCCsGAQUFBwMCMC0GA1UdDgQmBCRlOTcwNDRjNy0xZjM2LTQ5
OTYtOTc1NC1hZDY4OTU2Yjk3ZGMwDAYDVR0jBAUwA4ABMDAFBgMrZXADQQAnpSpi
G+X9AgBYUhY3XBe6q9c75RzDjwTf2g9rkmD0VJxYrWVtT95xRwBufiRUsnRh24WE
7NmLI3rE5aGoY0wH
-----END CERTIFICATE-----
EOF
cat > /tmp/tls.key <<EOF
-----BEGIN PRIVATE KEY-----
MC4CAQAwBQYDK2VwBCIEIAokQWsCGewdhhxAKjUFWAyJknZqJWhOCChVbJOXBspi
-----END PRIVATE KEY-----
EOF
cat > /tmp/ca.crt <<EOF
-----BEGIN CERTIFICATE-----
MIIBdTCCASegAwIBAgIQRR8k78lPFZM+mtyAUfz5rjAFBgMrZXAwRDELMAkGA1UE
BhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWExDTALBgNVBAoTBEFQSTcxETAPBgNV
BAMTCEFQSTcgSW5jMB4XDTI0MDgwOTA2MjUxOFoXDTM0MDgwNzA2MjUxOFowRDEL
MAkGA1UEBhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWExDTALBgNVBAoTBEFQSTcx
ETAPBgNVBAMTCEFQSTcgSW5jMCowBQYDK2VwAyEAplXlP4zxS8cq1Qa5Syd7r/ya
SaolzMQBLTMQfcKkb16jLzAtMA4GA1UdDwEB/wQEAwIChDAPBgNVHRMBAf8EBTAD
AQH/MAoGA1UdDgQDBAEwMAUGAytlcANBAJ0ezih/La2Ajc7bi1WdlzIi+T3oIPta
d/l1PkE5rDLxySMzJvowk49earvcz5rVILf2aG/k1YRc7Kc+cmnLlAs=
-----END CERTIFICATE-----
EOF
kubectl create secret generic api7-ee-3-gateway-tls --from-file=tls.crt=/tmp/tls.crt --from-file=tls.key=/tmp/tls.key --from-file=ca.crt=/tmp/ca.crt
helm upgrade --install api7-ee-3-gateway api7/gateway \
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
  --set "apisix.image.tag=3.2.14.4"
  --set "apisix.securityContext.runAsNonRoot=true" \
  --set "apisix.securityContext.runAsUser=636"
```

Install API gateway instances on your cluster.

Navigating back to the `default` gateway group, you should see a healthy gateway instance:

![See an active gateway instance](https://static.api7.ai/uploads/2024/04/12/kWnjDIYf_21.png)

## Verify Installation[â](#verify-installation "Direct link to Verify Installation")

### Create a Sample Service[â](#create-a-sample-service "Direct link to Create a Sample Service")

Create a service `HTTPBIN`:

![Create a service httpbin](https://static.api7.ai/uploads/2024/04/12/f70nEdxx_22.png)

Add a route to `/anything` endpoint and allow only the `GET` method:

![Add a route with GET method](https://static.api7.ai/uploads/2024/04/12/RpMfp0pP_23.png)

You should see the service now shows the created route:

![Dashboard showing the service with the created route](https://static.api7.ai/uploads/2024/04/12/37UQHBZB_24.png)

### Port Forward Gateway Service[â](#port-forward-gateway-service "Direct link to Port Forward Gateway Service")

Before you can send a request to the Gateway, you should first port forward the gateway listening port to localhost.

First, list all Services to check the gateway service name:

```
kubectl get svc
```

The gateway service name is `api7-ee-3-gateway-gateway`:

```
NAME                        TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)             AGE
api7-ee-3-gateway-gateway   NodePort    172.30.211.30   <none>        80:31649/TCP        3m51s
api7-postgresql             ClusterIP   172.30.215.68   <none>        5432/TCP            56m
api7-postgresql-hl          ClusterIP   None            <none>        5432/TCP            56m
api7-prometheus-server      ClusterIP   172.30.3.68     <none>        9090/TCP            56m
api7ee3-dashboard           ClusterIP   172.30.249.55   <none>        7080/TCP            56m
api7ee3-dp-manager          ClusterIP   172.30.43.83    <none>        7900/TCP,7943/TCP   56m
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
    "User-Agent": "curl/8.4.0",
    "X-Amzn-Trace-Id": "Root=1-65fa9071-7506ab7b0e98d7546e3c0845",
    "X-Forwarded-Host": "localhost"
  },
  "json": null,
  "method": "GET",
  "origin": "::1, 3.1.235.149",
  "url": "http://localhost/anything"
}
```

## What's Next[â](#whats-next "Direct link to What's Next")

In addition to publishing services through the Dashboard UI, API7 provides a command line tool that can operate declarative configuration, so you can integrate API7 Operations with internal GitOps. See Managing [APISIX Declaratively with APISIX Declarative CLI (ADC)](https://api7.ai/blog/managing-apisix-declaratively).

See [Getting Started tutorials](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md) to learn more about how to work with ADC.

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
