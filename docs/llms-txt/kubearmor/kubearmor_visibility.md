# Source: https://docs.kubearmor.io/kubearmor/documentation/kubearmor_visibility.md

# Control Telemetry/Visibility

KubeArmor currently supports enabling visibility for containers and hosts.

Visibility for hosts is not enabled by default, however it is enabled by default for containers .

The `karmor` tool provides access to both using `karmor logs`.

<details>

<summary>Available visibility options:</summary>

**KubeArmor provides visibility on the following behavior of containers**

* Process
* Files
* Networks

</details>

### Prerequisites

* If you don't have access to a K8s cluster, please follow [this](https://docs.kubearmor.io/kubearmor/quick-links/deployment_guide#prerequisites) to set one up.
* karmor CLI tool: [Download and install karmor-cli](https://docs.kubearmor.io/kubearmor/quick-links/deployment_guide#1-download-and-install-karmor-cli-tool)

### Example: wordpress-mysql

* To deploy [wordpress-mysql](https://github.com/kubearmor/KubeArmor/blob/main/examples/wordpress-mysql/wordpress-mysql-deployment.yaml) app follow [this](https://github.com/kubearmor/KubeArmor/blob/main/examples/wordpress-mysql.md)
* Now we need to deploy some sample policies

```
kubectl apply -f https://raw.githubusercontent.com/kubearmor/KubeArmor/main/examples/wordpress-mysql/security-policies/ksp-wordpress-block-process.yaml
```

This sample policy blocks execution of the `apt` and `apt-get` commands in wordpress pods with label selector `app: wordpress`.

### Getting Container Visibility

* Checking default visibility

  * Container visibility is enabled by default. We can check it using `kubectl describe` and grep `kubearmor-visibility`

  ```
  POD_NAME=$(kubectl get pods -n wordpress-mysql -l app=wordpress -o jsonpath='{.items[0].metadata.name}') && kubectl describe -n wordpress-mysql pod $POD_NAME | grep kubearmor-visibility

  kubearmor-visibility: process, file, network, capabilities
  ```

  * **For pre-existing workloads :** Enable visibility using `kubectl annotate`. Currently KubeArmor supports `process`, `file`, `network`, `capabilities`

  ```
  kubectl annotate pods <pod-name> -n wordpress-mysql "kubearmor-visibility=process,file,network,capabilities"
  ```

* Open up a terminal, and watch logs using the `karmor` cli

  ```
  karmor logs
  ```

* In another terminal, simulate a policy violation . Try `sleep` inside a pod

  ```
  POD_NAME=$(kubectl get pods -n wordpress-mysql -l app=wordpress -o jsonpath='{.items[0].metadata.name}') && kubectl -n wordpress-mysql exec -it $POD_NAME -- bash
  # apt update
  ```

* In the terminal running `karmor logs`, the policy violation along with container visibility is shown, in this case for example
* The logs can also be generated in JSON format using `karmor logs --json`

### Getting Host Visibility

* Host Visibility is not enabled by default . To enable Host Visibility we need to annotate the node using `kubectl annotate node`

```
  kubectl annotate node <node-name> "kubearmor-visibility=process,file,network,capabilities" 
```

* To confirm it use `kubectl describe` and grep `kubearmor-visibility`

```
kubectl describe node <node-name> | grep kubearmor-visibility
```

* Now we can get general telemetry events in the context of the host using `karmor logs` .The logs related to Host Visibility will have type `Type: HostLog`and `Operation: File | Process | Network`

```
karmor logs --logFilter=all
```

<details>

<summary>Click to expand</summary>

```
== Alert / 2023-01-04 04:58:37.689182 ==
== Log / 2023-01-27 14:41:49.017709 ==
ClusterName: default
HostName: kubearmor-dev2
Type: HostLog
Source: /usr/bin/dockerd
Resource: /usr/bin/runc --version
Operation: Process
Data: syscall=SYS_EXECVE
Result: Passed
HostPID: 193088
HostPPID: 914
PID: 193088
PPID: 914
ParentProcessName: /usr/bin/dockerd
ProcessName: /usr/bin/runc
== Log / 2023-01-27 14:41:49.018951 ==
ClusterName: default
HostName: kubearmor-dev2
Type: HostLog
Source: /usr/bin/runc --version
Resource: /lib/x86_64-linux-gnu/libc.so.6
Operation: File
Data: syscall=SYS_OPENAT fd=-100 flags=O_RDONLY|O_CLOEXEC
Result: Passed
HostPID: 193088
HostPPID: 914
PID: 193088
PPID: 914
ParentProcessName: /usr/bin/dockerd
ProcessName: /usr/bin/runc
== Log / 2023-01-27 14:41:49.018883 ==
ClusterName: default
HostName: kubearmor-dev2
Type: HostLog
Source: /usr/bin/runc --version
Resource: /etc/ld.so.cache
Operation: File
Data: syscall=SYS_OPENAT fd=-100 flags=O_RDONLY|O_CLOEXEC
Result: Passed
HostPID: 193088
HostPPID: 914
PID: 193088
PPID: 914
ParentProcessName: /usr/bin/dockerd
ProcessName: /usr/bin/runc
== Log / 2023-01-27 14:41:49.020905 ==
ClusterName: default
HostName: kubearmor-dev2
Type: HostLog
Source: /var/lib/rancher/k3s/data/2949af7261ce923f6a5091396d266a0e9d9436dcee976fcd548edc324eb277bb/bin/k3s
Resource: /var/lib/rancher/k3s/data/2949af7261ce923f6a5091396d266a0e9d9436dcee976fcd548edc324eb277bb/bin/portmap
Operation: Process
Data: syscall=SYS_EXECVE
Result: Passed
HostPID: 193090
HostPPID: 5627
PID: 193090
PPID: 5627
ParentProcessName: /var/lib/rancher/k3s/data/2949af7261ce923f6a5091396d266a0e9d9436dcee976fcd548edc324eb277bb/bin/k3s
ProcessName: /var/lib/rancher/k3s/data/2949af7261ce923f6a5091396d266a0e9d9436dcee976fcd548edc324eb277bb/bin/portmap

```

* The logs can also be generated in JSON format using `karmor logs --logFilter=all --json`

</details>

### Updating Namespace Visibility

KubeArmor has the ability to let the user select what kind of events have to be traced by changing the annotation `kubearmor-visibility` at the namespace.

* Checking Namespace visibility

  * Namespace visibility can be checked using `kubectl describe`.

  ```
  kubectl describe ns wordpress-mysql | grep kubearmor-visibility

  kubearmor-visibility: process, file, network, capabilities
  ```

  * **To update the visibility of namespace :** Now let's update Kubearmor visibility using `kubectl annotate`. Currently KubeArmor supports `process`, `file`, `network`, `capabilities`.\
    Lets try to update visibility for the namespace `wordpress-mysql`

  ```
   kubectl annotate ns wordpress-mysql kubearmor-visibility=network --overwrite
   "namespace/wordpress-mysql annotated"

  ```

  > Note: To turn off the visibility across all aspects, use `kubearmor-visibility=none`. Note that any policy violations or events that results in non-success returns would still be reported in the logs.
* Open up a terminal, and watch logs using the `karmor` cli

  ```
  karmor logs --logFilter=all -n wordpress-mysql

  ```

* In another terminal, let's exec into the pod and run some process commands . Try `ls` inside the pod

  ```
    POD_NAME=$(kubectl get pods -n wordpress-mysql -l app=wordpress -o jsonpath='{.items[0].metadata.name}') && kubectl -n wordpress-mysql exec -it $POD_NAME -- bash
  # ls
  ```

  Now, we can notice that no logs have been generated for the above command and logs with only `Operation: Network` are shown.

  > **Note** If telemetry is disabled, the user wont get audit event even if there is an audit rule.

  > **Note** Only the logs are affected by changing the visibility, we still get all the alerts that are generated.
* Let's simulate a sample policy violation, and see whether we still get alerts or not.

  * **Policy violation :**

  ```
  POD_NAME=$(kubectl get pods -n wordpress-mysql -l app=wordpress -o jsonpath='{.items[0].metadata.name}') && kubectl -n wordpress-mysql exec -it $POD_NAME -- bash
  #apt 
  ```

  Here, note that the alert with `Operation: Process` is reported.
