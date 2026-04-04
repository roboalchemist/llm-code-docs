# Source: https://docs.vespa.ai/en/operations/kubernetes/installation.html.md

# Install Vespa on Kubernetes

 

The Vespa Operator should be installed using the official Helm chart.  
 The operator depends on the installation of the `VespaSet` [Custom Resource Definition](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) (CRD), which is defined at the Kubernetes cluster scope.  
 Through the Helm Chart, the installation of the CRD and the required RBAC permissions can be simplified. The required permissions are listed in the [Permissions](#permissions) section.

Our container registry is located at `images.ves.pa`.  
 For accessing the required Vespa on Kubernetes container images (and helm chart) you will need to contact us through our support portal, we will provide you with a the authentication id and token.  
**Important:** For production use, we _require_ mirroring these images into your own registry or a well-known internal repository appropriate for your infrastructure!

Our support team will provide you with the required credentials, you will have access to the following:

- the _Vespa on Kubernetes_ image, corresponding to `$OCI_IMAGE_REFERENCE` in this guide,
- the _Vespa Operator_ image, corresponding to `$OCI_IMAGE_REFERENCE_OPERATOR` in this guide,
- the official _Vespa Helm Chart_ OCI, referred to as `$HELM_OCI_CHART_REFERENCE` in this guide.

## Requirements

The following tools are encouraged for a smooth deployment.

- [Helm CLI](https://helm.sh/docs/intro/install/)
- Kubernetes Command Line Tool ([kubectl](https://kubernetes.io/docs/reference/kubectl/))
- [Vespa CLI](https://docs.vespa.ai/en/clients/vespa-cli.html)
- the Vespa on Kubernetes and Vespa Operator images
- the Vespa Helm Chart
- [MiniKube (Optional)](https://minikube.sigs.k8s.io/docs/)
- Podman or Docker

These instructions assume that `kubeconfig` is pointing to an active Kubernetes cluster. Refer to the [Getting Started](https://kubernetes.io/docs/setup/) guide to create a Kubernetes cluster.

## MiniKube Setup

MiniKube allows for simple local testing of Vespa on Kubernetes. Skip to the [Deploy Vespa Operator](#install-helm-chart) section below to directly start installation.

Initialize a Minikube cluster with 8 nodes, 2CPUs and 4GiB memory each ausing the Podman driver. Enable Minikube's image registry add-on to allow the Minikube nodes to access the image.

```
# Start Minikube
minikube start --nodes 8 --cpus 2 --memory 4GiB --driver=podman

# Enable Image Registry add-on
minikube addons enable registry

# Verify MiniKube cluster was created
minikube status
```

```
# Authenticate to the registry
echo $VESPAAI_REGISTRY_TOKEN | podman login images.ves.pa \
  -u "$VESPAAI_REGISTRY_USER" \
  --password-stdin

# Cache the images locally
podman pull images.ves.pa/kubernetes/vespa:$VESPA_VERSION
podman pull images.ves.pa/kubernetes/operator:$VESPA_VERSION
```

Once the Minikube cluster is set up, push the images to the MiniKube registry, to make accessible to the MiniKube nodes. The MiniKube registry is accessible from `$(minikube ip):5000`.

```
# Save the minikube registry endpoint
$MINIKUBE_REGISTRY=$(minikube ip)

# Push the kubernetes/vespa image to the registry
podman tag kubernetes/vespa:$VESPA_VERSION $MINIKUBE_REGISTRY:5000/localhost/kubernetes/vespa:$VESPA_VERSION
podman push --tls-verify=false $MINIKUBE_REGISTRY:5000/localhost/kubernetes/vespa:$VESPA_VERSION

# Push the kubernetes/operator image to the registry
podman tag kubernetes/operator:$VESPA_VERSION $MINIKUBE_REGISTRY:5000/localhost/kubernetes/operator:$VESPA_VERSION
podman push --tls-verify=false $MINIKUBE_REGISTRY:5000/localhost/kubernetes/operator:$VESPA_VERSION
```

The images will now be available to the Minikube nodes from `$MINIKUBE_REGISTRY:5000/localhost/kubernetes/operator:$VESPA_VERSION`.

```
export OCI_IMAGE_REFERENCE=$MINIKUBE_REGISTRY:5000/localhost/kubernetes/vespa
export OCI_IMAGE_REFERENCE_OPERATOR=$MINIKUBE_REGISTRY:5000/localhost/kubernetes/operator
export OCI_IMAGE_TAG=$VESPA_VERSION
```

Then, install the [Local Persistent Volume](https://github.com/kubernetes-sigs/sig-storage-local-static-provisioner) provisioner Helm Chart. This will allow Persistent Volumes to be created in a MiniKube environment. It will automatically create a StorageClass called `local-storage`, which should be used for the next steps.

```
# Clone the local persistent volume static provisioner from the Kubernetes sigs
$ git clone git@github.com:kubernetes-sigs/sig-storage-local-static-provisioner.git

# Deploy onto the Kubernetes cluster
$ helm install -f helm/examples/baremetal-default-storage.yaml local-volume-provisioner --namespace kube-system ./helm/provisioner

# Create several volumes on each Minikube node.
$ for n in minikube minikube-m02 minikube-m03 minikube-m04 minikube-m05 minikube-m06 minikube-m07 minikube-m08; do
  echo "==> $n"
  minikube ssh -n "$n" -- '
    set -e
    for i in 1 2 3 4; do
      sudo mkdir -p /mnt/disks/vol$i
      if ! mountpoint -q /mnt/disks/vol$i; then
        sudo mount --bind /mnt/disks/vol$i /mnt/disks/vol$i
      fi
    done
    echo "Mounted:"
    mount | grep -E "/mnt/disks/vol[1-4]" || true
  '
done
```

## Deploy Vespa Operator

The Helm Chart installs the Vespa Operator and the `Role`, `RoleBinding`, and `ServiceAccount` resources with the necessary permissions to operate Vespa. Optionally, the CRD specification can be installed onto the Kubernetes cluster.

An installation can be performed as follows. This will deploy the Vespa Operator to the `vespa` namespace and apply the `VespaSet` CRD specification to the cluster.

```
$ helm install vespa-operator $HELM_OCI_CHART_REFERENCE --namespace vespa --create-namespace --set image.repository $OCI_IMAGE_REFERENCE_OPERATOR --set image.tag $OCI_IMAGE_TAG
```

If CRDs are managed separately, the CRD installation can be disabled. However, the CRD specification must be manually applied to the cluster before installing the Helm Chart. Our support team can provide this specification if necessary.

```
$ kubectl apply vespasets.k8s.ai.vespa-v1.yaml
$ helm install vespa-operator $HELM_OCI_CHART_REFERENCE --namespace $NAMESPACE --create-namespace --skip-crds --set image.repository $OCI_IMAGE_REFERENCE_OPERATOR --set image.tag $OCI_IMAGE_TAG
```

Ensure that the `Deployment` resource was successfully applied and the operator `Pod` was created. It can be done using the following check.

```
$ kubectl wait --for=condition=available deployment/vespa-operator --timeout=120s -n $NAMESPACE \
&& kubectl get pods -l app=vespa-operator -o wide -n $NAMESPACE
```

The full reference guide for the Helm Chart can be found in the [Helm Reference](helm-reference.html) section.

## Deploy a VespaSet

A `VespaSet` represents a quorum of [ConfigServers](https://docs.vespa.ai/en/operations/self-managed/configuration-server.html) that manage Vespa applications. Several examples of `VespaSet` specifications are provided in the Helm Chart `samples` directory. A sample `VespaSet` resource for [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (EKS) is shown below.

```
# VespaSet configuration for AWS EKS
apiVersion: k8s.ai.vespa/v1
kind: VespaSet
metadata:
  name: vespaset-sample
  namespace: vespa
spec:
  version: $OCI_IMAGE_TAG

  configServer:
    image: "$OCI_IMAGE_REFERENCE"
    storageClass: "gp3"
    generateRbac: false

  application:
    image: "$OCI_IMAGE_REFERENCE"
    storageClass: "gp3"

  ingress:
    endpointType: "NODE_PORT"
```

An example for MiniKube would be as follows.

```
# VespaSet configuration for AWS EKS
apiVersion: k8s.ai.vespa/v1
kind: VespaSet
metadata:
  name: vespaset-sample
  namespace: vespa
spec:
  version: $OCI_IMAGE_TAG

  configServer:
    image: "$OCI_IMAGE_REFERENCE"
    storageClass: "local-storage"
    generateRbac: false

  application:
    image: "$OCI_IMAGE_REFERENCE"
    storageClass: "local-storage"

  ingress:
    endpointType: "NODE_PORT"
```

Note that the `$OCI_IMAGE_REFERENCE` is shared between the ConfigServer and the Vespa Application Pods.

Apply the `VespaSet` resource to the Kubernetes Cluster. The operator will automatically detect the `VespaSet` and create a quorum of ConfigServers.

The ConfigServers will then bootstrap the Vespa infrastructure. This process takes roughly a minute. The bootstrap process is completed once the `VespaSet` shows the status as `RUNNING` for all ConfigServer Pods.

```
$ kubectl describe vespaset vespaset-sample -n vespa
Name: vespaset-sample
Namespace: vespa
Labels: <none>
Annotations: <none>
API Version: k8s.ai.vespa/v1
Kind: VespaSet
Metadata:
  Creation Timestamp: 2026-01-29T21:32:27Z
  Finalizers:
    vespasets.k8s.ai.vespa/finalizer
  Generation: 1
  Resource Version: 121822902
  UID: a70f56e9-6625-4011-acd7-9f7cad29dbc2
Spec:
  Application:
    Image: $OCI_IMAGE_REFERENCE
    Storage Class: gp3
  Config Server:
    Generate Rbac: false
    Image: $OCI_IMAGE_REFERENCE
    Storage Class: gp3
  Ingress:
    Endpoint Type: NODE_PORT
  Version: $OCI_IMAGE_TAG
Status:
  Bootstrap Status:
    Pods:
      cfg-0:
        Last Updated: 2026-01-29T21:38:45Z
        Message: Pod is running
        Phase: RUNNING
      cfg-1:
        Last Updated: 2026-01-29T21:38:09Z
        Message: Pod is running
        Phase: RUNNING
      cfg-2:
        Last Updated: 2026-01-29T21:36:32Z
        Message: Pod is running
        Phase: RUNNING
  Last Transition Time: 2026-01-29T21:33:55Z
  Message: All configservers running
  Phase: RUNNING
Events: <none>
```

The status of the bootstrap process can be easily queried as follows.

```
$ kubectl get vespaset upgradetest-vespaset -n mramdenbourg-upgradetest -o json \
| jq -e '
  .status.bootstrapStatus.pods as $p
  | ($p["cfg-0"].phase == "RUNNING")
  and ($p["cfg-1"].phase == "RUNNING")
  and ($p["cfg-2"].phase == "RUNNING")
'
```

The full reference guide for the VespaSet CRD can be found in the [VespaSet Reference](vespaset-reference.html) section.

## Deploy a Vespa Application

A Vespa application can be deployed once the bootstrap process has completed. Refer to the [Vespa Sample Applications](https://github.com/vespa-engine/sample-apps) to get started. In the following example, we will use the [Album Recommendation](https://github.com/vespa-engine/sample-apps/tree/master/album-recommendation) sample.

Set up the Vespa CLI to download the Album Recommendation sample application to a working directory and use the local endpoints.

```
$ vespa clone album-recommendation myapp && cd myapp
$ vespa config set target local
```

Enable a port-forward of the ConfigServer's ingress port to a port locally.

```
$ kubectl -n mramdenbourg-upgradetest port-forward pod/cfg-0 19071:19071
```

The application can be deployed using the Vespa CLI.

```
$ vespa deploy --wait 600
```

This will create the Container, Content, and Cluster-Controller Pods as specified in the application package. The deployment is considered complete once all Pods are in phase `RUNNING` in the `VespaSet` status. This can be queried as follows.

```
$ kubectl get vespaset upgradetest-vespaset -n mramdenbourg-upgradetest -o json \
| jq -e '
  .status.bootstrapStatus.pods
  | with_entries(
      select(
        .key as $k
        | [
            "cluster-controllers-104",
            "cluster-controllers-105",
            "cluster-controllers-106",
            "default-100",
            "default-101",
            "documentation-102",
            "documentation-103"
          ]
        | index($k) | not
      )
    )
  | all(.phase == "RUNNING")
'
```

Note the names of the Pods may change depending on your specific Application Package configuration.

Port forwarding provides a simple way to access the application locally. For other ingress options, see the [Configuring the External Access Layer](ingress.html) section.

## Feed Documents

Feed documents to the Dataplane entrypoint by port-forwarding to both the Dataplane Pod and the ConfigServer Pod.

```
$ kubectl -n mramdenbourg-upgradetest port-forward pod/cfg-0 19071:19071
$ kubectl -n mramdenbourg-upgradetest port-forward pod/default-100 8080:8080
```

Then, use the Vespa CLI to feed a document.

```
vespa feed dataset/A-Head-Full-of-Dreams.json
```

## Permissions

The Vespa Operator requires the following permissions. These permissions are listed by Kubernetes [API verbs](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) per resource.

| Kubernetes Resource | Required Permissions |
| --- | --- |
| CustomResourceDefinitions | create, get, list, watch |
| VespaSet | get, list, watch, create, update, patch, delete |
| VespaSet Subresources | `vespasets/status`: update, patch  
`vespasets/finalizers`: update |
| ConfigMaps | get, list, watch, create, update, patch, delete |
| Services | get, list, watch, create, update, patch, delete |
| Pods | get, list, watch, create, update, patch, delete |
| Pod Execution | get, create |
| Events | create, patch |
| PersistentVolumeClaims | get, list, watch, create, update, patch, delete |
| ServiceAccounts | get, list, watch, create, update, patch, delete |
| Roles | get, list, watch, create, update, patch, delete |
| RoleBindings | get, list, watch, create, update, patch, delete |

 Copyright © 2026 - [Cookie Preferences](#)

### On this page:

- [Requirements](#)
- [MiniKube Setup](#)
- [Deploy Vespa Operator](#install-helm-chart)
- [Deploy a VespaSet](#)
- [Deploy a Vespa Application](#)
- [Feed Documents](#)
- [Permissions](#permissions)

