<!-- Source: https://namespace.so/docs/reference/cli/logs -->

# nsc logs

Print the logs for a instance and its workload.

`logs` prints logs for an instance and its workload to the standard output. It
also allows to print real-time logs or logs for the specific period.

**Note**: Printing logs is only supported for Kubernetes instances.

## Usage

```
nsc logs <instance-id> [-n <namespace>] [-p <pod>] [-c <container>] [--since <duration>] [-f] [--raw]
```

### Example

The following example shows how to print logs for `kube-system` Kubernetes
namespace:

```
$ nsc create
Created instance "1lf2ol9ioulce"
 deadline: 2023-04-25T13:24:53Z
 
$ nsc logs 1lf2ol9ioulce -n kube-system
```

To start streaming logs for `kube-system` Kubernetes namespace:

```
$ nsc logs 1lf2ol9ioulce -n kube-system -f
```

## Options

### -n <namespace>

If provided `nsc` prints logs only for the specified Kubernetes namespace.

### -p <pod>

If provided `nsc` prints logs only for the specified Kubernetes pod. If there
are multiple pods are running with the same name (e.g. in different Kubernetes
namespaces) logs of all pods would be printed. Use in combination with `-n` flag
to print the logs for the specific pod.

### -c <container>

If provided `nsc` prints logs only for the specified container in a Kubernetes
pod. If there are multiple containers with the same name (e.g. running in
different Kubernetes pods and/or namespaces) logs of all containers would be
printed. Use in combination with `-n` and/or `-p` flag to print the logs for
the specific container.

### -f

If specified logs would be streamed continuously starting from now.

### --since <duration>

To show logs relative to a timestamp (e.g. 42m for 42 minutes). The flag can't
be used with `-f`.

### --raw

Can be specified to print raw logs - e.g. without namespace/pod/container
labels.

### --source

If specified, display logs from this source. Default: `kubernetes`. Valid options: `kubernetes` or `containerd`

### --all

If specified, output all logs (including Kubernetes system logs).

Last updated July 22, 2025
