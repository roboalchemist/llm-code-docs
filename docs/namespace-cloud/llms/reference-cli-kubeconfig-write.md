<!-- Source: https://namespace.so/docs/reference/cli/kubeconfig-write -->

# nsc kubeconfig write

Generate a kubeconfig to connect to a instance.

`kubeconfig write` generates a kubeconfig that allows connecting `kubectl` to an instance.
The config is written to a temporary file. When running `kubectl`, the created kubeconfig
[can be selected](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/)
by setting the `KUBECONFIG` environment variable or by setting the `--kubeconfig` flag.

To skip writing the config and run a configured kubectl directly, see [`nsc kubectl`](/docs/reference/cli/kubectl)

## Usage

```
nsc kubeconfig write [instance-id]
```

### Example

The following example shows how to generate a kubeconfig and use it to deploy an application into an instance:

```
$ nsc create
Created instance "1lf2ol9ioulce"
 deadline: 2023-04-25T13:24:53Z
 
$ nsc kubeconfig write 1lf2ol9ioulce
Wrote Kubeconfig for instance 1lf2ol9ioulce to ~/.cache/ns/tmp/kubeconfig/2342545987.yaml.
 
Start using it by setting:
  export KUBECONFIG=~/.cache/ns/tmp/kubeconfig/2342545987.yaml
 
$ export KUBECONFIG=~/.cache/ns/tmp/kubeconfig/2342545987.yaml
$ kubectl apply -f https://k8s.io/examples/application/nginx-app.yaml
service/my-nginx-svc created
deployment.apps/my-nginx created
```

## Options

### --output\_to <path>

Write the *config path* to file. If file already exists, it will get overwritten.

Last updated July 4, 2025
