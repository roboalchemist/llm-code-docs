# Source: https://docs.api7.ai/apisix/install/kubernetes/rosa.md

# Install APISIX on ROSA

[Red Hat OpenShift Service on AWS (ROSA)](https://aws.amazon.com/rosa/) is a fully managed service that provides a simplified way to deploy and manage OpenShift clusters on AWS.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Have an AWS account

* Have a Red Hat account

* Follow the [Getting started with ROSA](https://cloud.redhat.com/learn/getting-started-red-hat-openshift-service-aws-rosa) learning path to

  <!-- -->

  * Set up AWS with OpenShift
  * Deploy a cluster
  * Grant the cluster admin rights to a user

* Install [ROSA CLI](https://console.redhat.com/openshift/downloads)

* Install [OpenShift CLI](https://docs.openshift.com/container-platform/4.11/cli_reference/openshift_cli/getting-started-cli.html) and [log in](https://docs.openshift.com/online/pro/cli_reference/get_started_cli.html#basic-setup-and-login) with the credentials of the user with cluster admin rights

* Install [Helm CLI](https://helm.sh/docs/intro/install/)

## Create an OpenShift Project and Service Account[â](#create-an-openshift-project-and-service-account "Direct link to Create an OpenShift Project and Service Account")

Log in OpenShift CLI using the user account with cluster admin rights:

```
oc login <cluster-url> --username <username> --password <password>
```

Create an OpenShift project for APISIX:

```
oc new-project apisix
```

Switch the default project to `apisix`:

```
oc project apisix
```

Create a service account `apisix-sa` for APISIX deployment:

```
oc create sa apisix-sa
```

Add the [security context constraint (SCC)](https://docs.openshift.com/container-platform/4.16/authentication/managing-security-context-constraints.html) `nonroot-v2` to the service account:

```
oc adm policy add-scc-to-user nonroot-v2 -z apisix-sa
```

## Install With Helm[â](#install-with-helm "Direct link to Install With Helm")

Add APISIX Helm repository and update:

```
helm repo add apisix https://apache.github.io/apisix-helm-chart
helm repo update
```

Install the APISIX Helm chart:

```
helm install apisix apisix/apisix \
  --set gateway.type=NodePort \
  --set etcd.podSecurityContext.enabled=false \
  --set etcd.containerSecurityContext.enabled=false \
  --set serviceAccount.name=apisix-sa
```

â¶ Disable `podSecurityContext` and `containerSecurityContext` for etcd to avoid running into [issues related to SCC](https://github.com/bitnami/charts/issues/12215).

â· Deploy with the service account `apisix-sa` to grant APISIX the required permissions.

If successful, you should see a response similar to the following:

```
NAME: apisix
LAST DEPLOYED: Wed May 24 07:56:25 2023
NAMESPACE: apisix
STATUS: deployed
```

## Verify Installation[â](#verify-installation "Direct link to Verify Installation")

Check pod statuses to make sure all pods are up and running:

```
oc get pod
```

The response should be similar to the following with all pods `Running`:

```
NAME                      READY   STATUS    RESTARTS   AGE
apisix-5899557df4-5wgcn   1/1     Running   0          6m33s
apisix-etcd-0             1/1     Running   0          6m33s
apisix-etcd-1             1/1     Running   0          6m33s
apisix-etcd-2             1/1     Running   0          6m33s
```

Send a request to APISIX to verify APISIX is running:

```
oc exec -itq apisix-5899557df4-5wgcn -- curl -I http://127.0.0.1:9080 | grep Server
```

You should see APISIX version in the response:

```
Server: APISIX/3.13.0
```

You have now successfully installed APISIX on ROSA.
