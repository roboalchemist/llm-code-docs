<!-- Source: https://namespace.so/docs/reference/github-actions/nscloud-expose-kubernetes-action -->

# namespacelabs/nscloud-expose-kubernetes-action

namespacelabs/nscloud-expose-kubernetes-action@v0

[namespacelabs/nscloud-expose-kubernetes-action](https://github.com/namespacelabs/nscloud-expose-kubernetes-action)
is a GitHub action that exposes a Kubernetes application from Namespace.
It also generates a bearer token to access the authenticated preview via HTTP.

## Prerequisites

In order to use `nscloud-expose-kubernetes-action`, you need to have access to Namespace.
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
      - name: Create Cluster
        id: create-cluster
        uses: namespacelabs/nscloud-cluster-action@v0
      - name: Deploy NGINX
        run: |
          kubectl run nginx --image=nginx
          kubectl expose pod nginx --type=LoadBalancer --port=80
      - name: Expose application
        uses: namespacelabs/nscloud-expose-kubernetes-action@v0
        with:
          instance-id: ${{ steps.create-cluster.outputs.instance-id }}
          namespace: default
          service: nginx
```

## Options

### instance-id

Identifier of the Namespace Instance that hosts the Kubernetes application.

### namespace

Namespace of the service load balancer to expose.

### service

Name of the service load balancer to expose.

### port

Which exported Load Balancer port to expose.
This parameter can be skipped if there is a single exposed port for the service.

### name

If specified, set the name of the exposed ingress.

### ingress

Specify additional rules per ingress. The following effects can be set per
route:

- `noauth`: Disables authentication on the route.

Rules are defined by specifying method, path regex, using one of the following schemes:

- `<effect>`: Applies effect to any method or path.
- `<path_regex>:<effect>`: Applies effect to paths that match `path_regex` (the full path without the query is using for matching.).
- `<method>[,<method>,...]:<path_regex>:<effect>`: In addition to matching path, also matches against the HTTP method used.

### wildcard

Expose the service load balancer under a wildcard ingress.
The hosting instance needs to be configured to support wildcard ingresses.

## Outputs

### preview-url

URL of the exposed preview.

### access-token

Bearer token to access the exposed preview from HTTP.

Last updated September 1, 2025
