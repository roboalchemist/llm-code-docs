# Source: https://docs.kubearmor.io/kubearmor/contribution/development_guide.md

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
