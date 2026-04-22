<!-- Source: https://namespace.so/docs/reference/github-actions/nscloud-cluster-action -->

# namespacelabs/nscloud-cluster-action

namespacelabs/nscloud-cluster-action@v0

[namespacelabs/nscloud-cluster-action](https://github.com/namespacelabs/nscloud-cluster-action)
is a GitHub action that creates an ephemeral Kubernetes Cluster.
It also downloads and configures `kubectl` to grant access to the new cluster.

## Prerequisites

In order to use `nscloud-cluster-action`, you need to have access to Namespace.
The easiest way to ensure access is to run [namespacelabs/nscloud-setup](/docs/reference/github-actions/nscloud-setup) beforehand.

## Example

```
jobs:
  deploy:
    name: Ephemeral cluster
    runs-on: ubuntu-latest
    # These permissions are needed to interact with GitHub's OIDC Token endpoint.
    permissions:
      id-token: write
      contents: read
    steps:
      - uses: actions/checkout@v4
      - uses: namespacelabs/nscloud-setup@v0
      - name: Create a Namespace cluster
        uses: namespacelabs/nscloud-cluster-action@v0
      - name: Apply configurations
        run: |
          kubectl apply -f foo/bar.yaml
```

## Options

### preview

If set to `true`, the cluster created will *not* be destroyed at the end.
The default is `false`.

### wait-kube-system

If set to `true`, wait for `coredns` and `local-path-provisioner` to be ready.
The default is `true`.

### platform

Select the platform to run on. Valid options: `linux/amd64`, `linux/arm64` and `macos/arm64`. The default is `linux/amd64`

### machine-shape:

Specify the machine shape as `<cpu>x<mem>`. E.g. `2x8` starts a 2 vCPU 8GB RAM instance.

### duration

If set, specifies how long the cluster should live for. E.g. `10m`.

### unique-tag

If set, assign a unique tag to the instance. If there is already an instance with this tag, reuse it.

### ingress

Configures the ingress of this instance. Valid options: `wildcard`.

### kubernetes-version

Which Kubernetes cluster version to deploy in the instance. E.g. `1.31`.

## Outputs

### registry-address

Endpoint address of your workspace's private [Namespace Container Registry](/docs/architecture/storage/container-registry).

### instance-id

Identifier of the Namespace Instance hosting the created cluster.

### instance-url

Namespace App URL to manage and observe the created cluster.

### kubeconfig

Plain text version of the kubeconfig used to access the cluster.

Last updated February 13, 2026
