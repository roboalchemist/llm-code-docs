# Source: https://docs.sandboxes.cloud/docs/kubernetes-setup.md

# Setup for Kubernetes

This section will walk you through how to setup Crafting for empowering your developers with the simplest experience to boost the productivity on day-to-day Kubernetes related development tasks. For the user guide on how a developer to use this setup to develop on Kubernetes, please see [Develop on Kubernetes](https://docs.sandboxes.cloud/docs/kubernetes-dev). Specifically, the outline of this page:

* [How Crafting Works with Kubernetes](#how-crafting-works-with-kubernetes)
* [Setup Guide](#setup-guide)
  * [Connect a Kubernetes cluster](#connect-a-kubernetes-cluster)
  * [Setup Kubernetes access in the sandboxes](#setup-kubernetes-access-in-the-sandboxes)
  * [Orchestrate deployment of per-dev namespace from sandbox](#orchestrate-deployment-of-per-dev-namespace-from-sandbox)
  * [Access Kubernetes deployment using sandbox endpoint](#access-kubernetes-deployment-using-sandbox-endpoint)
  * [Use sandbox endpoint for conditional interception](#use-sandbox-endpoint-for-conditional-interception)
  * [Share with developers](#share-with-developers)
* [Additional Information](#additional-information)
  * [Features](#features)
  * [Supported Kubernetes clusters](#supported-kubernetes-clusters)
  * [Setup video](#setup-video)

## How Crafting Works with Kubernetes

Crafting Kubernetes Development Experience augments an existing Kubernetes cluster with rich development capabilities integrated with the Crafting system by installing the Crafting Kubernetes agent in the cluster. The agent takes care of communicating and collaborating with the Crafting system, regardless where your Kubernetes cluster is hosted (any location, any cloud provider), as long as it's able to connect to the Crafting system (including SaaS, self-hosted, and Express).

![](https://files.readme.io/3273f58-K8sDebug.png)

## Setup Guide

### Connect a Kubernetes cluster

A Kubernetes cluster can be connected to the Crafting system using a single command. Before that:

* Make sure your Kubernetes cluster is [supported](#supported-kubernetes-clusters);
* Make sure you are in a terminal with `kubectl` and `helm` installed, and `kubectl` is able to access the Kubernetes cluster with full access (e.g. `cluster-admin` equivalent privilege);
* The Crafting CLI `cs` is downloaded and installed, and has admin permission to access the Crafting system.

Run the following command:

```shell shell
$ cs infra kubernetes connect
```

The command prompts for a name of the cluster (it's a name used on the Crafting system side, not necessary to be the exact name of the cluster) and installs the `Crafting Kubernetes Agent` using `helm` in its own namespace and enables the following development capabilities:

* Direct in-cluster network access (Pod IPs, Service IPs, Service DNS) from Crafting sandboxes;
* Traffic interception and reroute (conditionally or unconditionally) incoming traffic to a Crafting sandbox;
* Direct Kubernetes API server access from Crafting sandboxes (without additional access setup in the Crafting sandboxes and/or from the cloud provider).

Please checkout [Features](#features) for the details.

> 🚧 If Kubernetes NetworkPolicy is used
>
> Kubernetes NetworkPolicy may prevent the Crafting Kubernetes Agent from communicating with workloads deployed in the other namespaces, and some of the above features may not work properly. In a cluster for development, please refer to [Kubernetes NetworkPolicy](#kubernetes-networkpolicy) for how to enable communication between Crafting Kubernetes Agent and other workloads.

The command will perform preflight checks and attempt auto-detection of Kubernetes in-cluster network setup. In most cases, it will be able to detect in-cluster CIDRs of Pod network and Service network. However, it may fail for some clusters, and it will ask you to enter the CIDRs.

> 📘 AWS EKS Specific
>
> As EKS clusters are using VPC subnet CIDRs directly for Kubernetes Services, the `cs` command will not be able to detect the Service subnet. In this case, you can enter the full VPC subnet CIDR directly, or individual CIDRs of the subnets in the VPC.

This information is required for Direct in-cluster network access to work properly.

Once the agent is installed successfully, the cluster will show up from the Crafting Web Console:

![](https://files.readme.io/3919dbb-ConnectedK8s.png)

### Setup Kubernetes access in the sandboxes

As the next step, setting up the `kubeconfig` file in the sandboxes allows the developers to access the cluster directly using `kubectl`. This is optional if sandboxes don't orchestrate an automated deployment in the cluster and the developers don't need to access the cluster directly. Features like direct in-cluster network access and traffic interception don't need Kubernetes access from sandboxes.

#### Direct Kubernetes API server access

If Direct Kubernetes API server access is enabled during agent installation, the following file can be used (as `~/.kube/config` or any file pointed by the environment variable `KUBECONFIG`, assuming the name of the cluster used during installation is `example`):

```yaml
apiVersion: v1
clusters:
- cluster:
    server: http://example.k8s.g.sandbox
  name: example
contexts:
- context:
    cluster: example
  name: example
current-context: example
```

The DNS name `example.k8s.g.sandbox` is specially registered inside each of the Crafting sandbox, proxied to the Kubernetes API server on the cluster connected under the name `example`.

There are a few ways to save this `kubeconfig` file

* As a [Secret](https://docs.sandboxes.cloud/docs/secrets), and add the env `KUBECONFIG` to the sandbox template. For example, the shared organizational secret is named `example-kubeconfig` and then the env `KUBECONFIG=/run/sandbox/fs/secrets/shared/example-kubeconfig`;
* Directly write to `~/.kube/config` and include that file in a [home snapshot](https://docs.sandboxes.cloud/docs/workspaces-setup#home-snapshots);
* Use a setup script (`/etc/sandbox.d/setup` or `~/.sandbox/setup`) to generate `~/.kube/config` every time a sandbox starts.

#### Through Cloud Provider

This is the alternative way if Direct Kubernetes API server access is disabled or special control is needed via the cloud provider:

* \[ ] Follow [Cloud Access Setup](https://docs.sandboxes.cloud/docs/cloud-resources-setup#access-setup) to make sure the developer can access the cloud provider from the sandbox using the corresponding CLI tools (e.g. `gcloud`, `aws` etc.);
* \[ ] Generate the `kubeconfig` file according to the cloud provider. Similar to above, find a way to save and share the file with sandboxes. Specific to GKE, please follow [Cloud Access Setup](https://docs.sandboxes.cloud/docs/cloud-resources-setup#access-setup) and modify the generated `kubeconfig` file.

#### Fine-grained Access Control

On the Kubernetes clusters supporting external OIDC provider, the native Kubernetes RBAC can be used to control fine-grained access to Crafting users when accessing from the workspaces.

##### AWS EKS

AWS EKS supports external OIDC providers. Add Crafting as one of the entry (the following example is using Terraform) to the cluster (make sure the EKS endpoint can be accessed from the Crafting workspaces):

```
variable "cluster_name" {
  description = "Name of the cluster"
}

variables "crafting_org" {
  description = "Org name in Crafting sandbox system"
}

resource "aws_eks_identity_provider_config" "crafting" {
  cluster_name = var.cluster_name

  oidc {
    client_id                     = var.crafting_org
    identity_provider_config_name = "crafting"
    issuer_url                    = "https://sandboxes.cloud"
  }
}
```

In the Crafting workspaces, prepare a `kubeconfig` file with `user` like:

```yaml
users:
- name: crafting
  user:
    tokenFile: /run/sandbox/fs/metadata/owner/token
```

A full example if `kubeconfig` can be (the rest part can be the same as generated from `aws eks update-kubeconfig ...`):

```yaml
apiVersion: v1
kind: Config
clusters:
- name: eks-cluster
  cluster:
    certificate-authority-data: <BASE64-OF-CLUSTER-CA-PEM>
    server: https://EKS-ENDPOINT.eks.amazonaws.com
contexts:
- name: crafting
  context:
    cluster: eks-cluster
    user: crafting
current-context: crafting
users:
- name: crafting
  user:
    tokenFile: /run/sandbox/fs/metadata/owner/token
```

Then create `RoleBinding` or `ClusterRoleBinding` in the Kubernetes for fine-grained access control. The *subject* should be `User` with name like `https://sandboxes.cloud#EMAIL`. For example:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: crafting-user-foo
subjects:
- kind: User
  name: 'https://sandboxes.cloud#foo@gmail.com'
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: bar-cluster-role
  apiGroup: rbac.authorization.k8s.io
```

### Orchestrate deployment of per-dev namespace from sandbox

By leveraging `resource` in a sandbox, a developer is able to have a namespace-isolated, per-sandbox deployment automatically and starts development without dealing with any Kubernetes related tasks. Define the following in a Sandbox Template:

```Text YAML
env:
  - APP_NS=${SANDBOX_APP}-${SANDBOX_NAME}-${SANDBOX_ID}
workspaces:
  - name: dev
    checkouts:
    - path: src
      ...
  ...
resources:
  - name: kubernetes
    brief: The deployment in the Kubernetes cluster
    handlers:
      on_create:
        use_workspace:
          name: dev
          run:
            cmd: |
              # Create the namespace if not exists.
              kubectl create ns "$APP_NS" || true
              kubectl -n "$APP_NS" apply -f deploy/kubernetes.yaml
            dir: src
      on_delete:
        use_workspace:
          name: dev
          run:
            cmd: kubectl delete ns "$APP_NS"
            dir: src
      on_suspend:
        max_retries: 1
        use_workspace:
          name: dev
          run:
            cmd: kubectl -n "$APP_NS" scale --replicas=0 --all deploy
            dir: src
      on_resume:
        use_workspace:
          name: dev
          run:
            cmd: kubectl -n "$APP_NS" scale --replicas=1 --all deploy
            dir: src
```

### Access Kubernetes deployment using sandbox endpoint

Per-sandbox deployment can be accessed using a sandbox Endpoint as it's more convenient and resource efficient compared to creating an Ingress or Load Balancer Service in the deployment (often these take long to provision, incur additional cost, and difficult to use - with direct IP or long, generated DNS, and no access control). A sandbox Endpoint can be easily clicked from the Web Console with additional access control feature which protects in-progress work from being accessed from public.

First, add the Endpoint to the definition and use a workspace as its backend:

```yaml
endpoints:
- name: k8sapp
  http:
    routes:
    - path_prefix: /
      backend:
        target: dev # This references the following workspace
        port: k8s-forward # This reference the port in the workspace
 workspaces:
 - name: dev
   ports:
   - name: k8s-forward
     port: 8888
     protocol: HTTP/TCP
...
```

With the above config, the Endpoint `k8sapp` is forwarding traffic to the workspace `dev` on port `8888`. Now add a daemon in the workspace to forward the traffic to a workload in the Kubernetes cluster, in the [Repo Manifest](https://docs.sandboxes.cloud/docs/repo-manifest):

```yaml
daemons:
  k8s-forward:
    run:
      cmd: cs k8s forward 8888:appsvc.${APP_NS}:8888
```

The above configuration leverages the env `APP_NS` as the namespace of the per-sandbox deployment. Where `appsvc` is the name of the Kubernetes Service as the entry of the deployment. The second port `8888` must be the port defined in the Service.

> 📘 Why not kubectl port-forward?
>
> The above command can be replaced with `kubectl port-forward ...` however, the command `kubectl port-forward` is unstable and often gets disconnected for unknown reason. Once that happened, the whole command must be restarted before it can forward new connections.

### Use sandbox endpoint for conditional interception

The [Traffic Intercept and Reroute](#traffic-intercept-and-reroute) provided by the Crafting Kubernetes agent supports conditional rerouting based on special HTTP headers. Once configured, only HTTP requests with specified headers are rerouted to sandboxes, thus allowing multiple developers to intercept the same deployment simultaneously without interfere with each other.

As the conditional rerouting relies on special HTTP headers, it has the following requirements before the feature is able to work properly:

* The application itself must support HTTP header propagation. For a specific service, the relationship between incoming and outgoing requests is determined by the application specific logic. The service must propagate special headers from incoming requests to the outgoing ones, so the complete end-to-end transaction of requests can be correctly rerouted;
* The first incoming request must carry the designated special HTTP headers.

The first requirement must be fulfilled by the application itself. Regarding the second one, the sandbox endpoint has the capability of injecting HTTP headers with special values. Please read [Develop on Kubernetes](https://docs.sandboxes.cloud/docs/kubernetes-dev#conditional-interception) for more details.

Note that GPRC protocol uses HTTP/2, so it is also supported for conditional routing if headers are configured properly.

### Share with developers

Once the setup is done, including the Template for sandboxes, related snapshots, share the Template with developers. The developers are able to have ready-to-use Kubernetes development environments by simply creating sandboxes from the template.

## Additional Information

### Features

#### Direct in-cluster Network Access

When the `Kubernetes Interception` is enabled on a sandbox, the full Kubernetes in-cluster can be accessed from the sandbox. For example, directly access a Pod using its IP address, resolving and accessing using a Kubernetes Service DNS.

This helps the outgoing communication from an in-development service (launched from a workspace in the sandbox) to talk to other dependencies in the cluster using the same way (e.g. using Kubernetes Service DNS names) as in a production deployment.

This feature doesn't require Kubernetes access from the sandbox.

#### Traffic Intercept and Reroute

The incoming traffic to any Pods in the cluster can be intercepted (either on HTTP level or TCP level) and rerouted to a workload in the sandbox. This helps quickly validate the change of a service without building and re-deploying it.

For HTTP interception, the interception can run conditionally based on special HTTP headers and their values. This allows multiple developers intercepting the same deployed service and validate individual changes without conflict.

#### Direct Kubernetes API server access

This feature provides the convenience to provide developers access to the connected Kubernetes cluster without additional access setup for the cloud providers. The *Crafting Kubernetes Agent* proxies the connection from sandbox to the API server and automatically injects the access token of the preconfigured service account (bound to a ClusterRole, default is *cluster-admin*).

On the sandbox side, the special DNS name `<CLUSTER-NAME>.k8s.g.sandbox` can be used to access the API server of the cluster connected under the name `CLUSTER-NAME`.

### Supported Kubernetes clusters

The *Crafting Kubernetes Agent* requires the deployment of `privilged` pods in the cluster, and it will be able to perform operations on node level. Nodeless clusters (e.g. EKS based on Fargate profiles, Autpilot GKE clusters) are not supported.

The minimum supported (tested) Kubernetes version is `1.21`. Old clusters or clusters running without `containerd` or docker-shim as the container runtime (CRI implementation) are not supported.

### Kubernetes NetworkPolicy

When Kubernetes NetworkPolicy resources are deployed, it's likely the Crafting Kubernetes agent can't communicate with other workloads. The features like [Direct in-cluster Network Access](#direct-in-cluster-network-access), [Traffic Intercept and Reroute](#traffic-intercept-and-reroute) won't work properly. If that's the case, please apply the following *NetworkPolicy* to the target namespace:

```yaml YAML
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-crafting
spec:
  podSelector: {}
  policyTypes:
    - Ingress
  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: crafting-sandbox
```

### Setup video

The steps to setup are also described in our video demo [here](https://youtu.be/J8LbuUVP_Do?t=271)

<Embed url="https://www.youtube.com/watch?v=J8LbuUVP_Do" title="Crafting Demo - Kubernetes" favicon="https://www.google.com/favicon.ico" image="https://i.ytimg.com/vi/J8LbuUVP_Do/hqdefault.jpg" provider="youtube.com" href="https://www.youtube.com/watch?v=J8LbuUVP_Do" typeOfEmbed="youtube" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252FJ8LbuUVP_Do%253Fstart%253D271%2526feature%253Doembed%2526start%253D271%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DJ8LbuUVP_Do%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252FJ8LbuUVP_Do%252Fhqdefault.jpg%26key%3D7788cb384c9f4d5dbbdbeffd9fe4b92f%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />