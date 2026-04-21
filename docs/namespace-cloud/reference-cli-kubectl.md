<!-- Source: https://namespace.so/docs/reference/cli/kubectl -->

# nsc kubectl

Run kubectl commands on a instance.

`kubectl` downloads a pinned kubectl binary and configures it inline to connect to your Namespace instance.
It allows you to quickly query Kubernetes resources in your instance with no setup.

To export the kubeconfig instead, see [`nsc kubeconfig write`](/docs/reference/cli/kubeconfig-write)

## Usage

```
nsc kubectl <instance-id> <kubectl arguments>
```

### Example

The following example shows how to get pods from all namespaces:

```
$ nsc create
Created instance "1lf2ol9ioulce"
 deadline: 2023-04-25T13:24:53Z
 
$ nsc kubectl 1lf2ol9ioulce get pods -A
NAMESPACE        NAME                                      READY   STATUS    RESTARTS   AGE
kube-system      coredns-5c6b6c5476-zh7rq                  1/1     Running   0          9s
kube-system      local-path-provisioner-5d56847996-lz8nd   1/1     Running   0          9s
metallb-system   controller-bdf98b979-qfwxr                0/1     Running   0          9s
metallb-system   speaker-rwxqr                             0/1     Running   0          9s
```

## Options

Please refer to the
[kubectl reference](https://kubernetes.io/docs/reference/kubectl/)
for a list of all possible arguments.

Last updated July 4, 2025
