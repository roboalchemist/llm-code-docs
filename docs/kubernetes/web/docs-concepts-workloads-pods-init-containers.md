# Source: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/

Title: Init Containers

URL Source: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/

Markdown Content:
Init Containers | Kubernetes
===============
[Kubernetes](https://kubernetes.io/)

*   [Documentation](https://kubernetes.io/docs/)
*   [Kubernetes Blog](https://kubernetes.io/blog/)
*   [Training](https://kubernetes.io/training/)
*   [Careers](https://kubernetes.io/careers/)
*   [Partners](https://kubernetes.io/partners/)
*   [Community](https://kubernetes.io/community/)
*   [Versions](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#)[Release Information](https://kubernetes.io/releases)[v1.35](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/)[v1.34](https://v1-34.docs.kubernetes.io/docs/concepts/workloads/pods/init-containers/)[v1.33](https://v1-33.docs.kubernetes.io/docs/concepts/workloads/pods/init-containers/)[v1.32](https://v1-32.docs.kubernetes.io/docs/concepts/workloads/pods/init-containers/)[v1.31](https://v1-31.docs.kubernetes.io/docs/concepts/workloads/pods/init-containers/) 
*   [English](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#)[中文 (Chinese)](https://kubernetes.io/zh-cn/docs/concepts/workloads/pods/init-containers/)[Français (French)](https://kubernetes.io/fr/docs/concepts/workloads/pods/init-containers/)[Bahasa Indonesia (Indonesian)](https://kubernetes.io/id/docs/concepts/workloads/pods/init-containers/)[日本語 (Japanese)](https://kubernetes.io/ja/docs/concepts/workloads/pods/init-containers/)[한국어 (Korean)](https://kubernetes.io/ko/docs/concepts/workloads/pods/init-containers/)[Español (Spanish)](https://kubernetes.io/es/docs/concepts/workloads/pods/init-containers/) 

#### ![Image 1](https://kubernetes.io/images/announcements/kccnc-eu-2026-black.svg)[KubeCon + CloudNativeCon Europe 2026](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/?utm_source=kubernetes&utm_medium=homepage&utm_campaign=18269725-KubeCon-EU-2026&utm_content=slim-banner)

Join us for four days of incredible opportunities to collaborate, learn and share with the cloud native community.

[Buy your ticket now! 23 - 26 March | Amsterdam, The Netherlands](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/register/?utm_source=kubernetes&utm_medium=homepage&utm_campaign=18269725-KubeCon-EU-2026&utm_content=slim-banner)

[English](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#)

[বাংলা (Bengali)](https://kubernetes.io/bn/docs/concepts/)[中文 (Chinese)](https://kubernetes.io/zh-cn/docs/concepts/)[Français (French)](https://kubernetes.io/fr/docs/concepts/)[Deutsch (German)](https://kubernetes.io/de/docs/concepts/)[हिन्दी (Hindi)](https://kubernetes.io/hi/docs/concepts/)[Bahasa Indonesia (Indonesian)](https://kubernetes.io/id/docs/concepts/)[Italiano (Italian)](https://kubernetes.io/it/docs/concepts/)[日本語 (Japanese)](https://kubernetes.io/ja/docs/concepts/)[한국어 (Korean)](https://kubernetes.io/ko/docs/concepts/)[Polski (Polish)](https://kubernetes.io/pl/docs/concepts/)[Português (Portuguese)](https://kubernetes.io/pt-br/docs/concepts/)[Русский (Russian)](https://kubernetes.io/ru/docs/concepts/)[Español (Spanish)](https://kubernetes.io/es/docs/concepts/)[Українська (Ukrainian)](https://kubernetes.io/uk/docs/concepts/)[Tiếng Việt (Vietnamese)](https://kubernetes.io/vi/docs/concepts/)

*   [Kubernetes Documentation](https://kubernetes.io/docs/ "Documentation")
    *   - [x] [Documentation](https://kubernetes.io/docs/home/ "Kubernetes Documentation") 
        *   - [x] [Available Documentation Versions](https://kubernetes.io/docs/home/supported-doc-versions/) 

    *   - [x] [Getting started](https://kubernetes.io/docs/setup/) 
        *   - [x] [Learning environment](https://kubernetes.io/docs/setup/learning-environment/) 
        *   - [x] [Production environment](https://kubernetes.io/docs/setup/production-environment/) 
            *   - [x] [Container Runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/) 
            *   - [x] [Installing Kubernetes with deployment tools](https://kubernetes.io/docs/setup/production-environment/tools/) 
                *   - [x] [Bootstrapping clusters with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/) 
                    *   - [x] [Installing kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/) 
                    *   - [x] [Troubleshooting kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/) 
                    *   - [x] [Creating a cluster with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/) 
                    *   - [x] [Customizing components with the kubeadm API](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/control-plane-flags/) 
                    *   - [x] [Options for Highly Available Topology](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/ha-topology/) 
                    *   - [x] [Creating Highly Available Clusters with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/) 
                    *   - [x] [Set up a High Availability etcd Cluster with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm/) 
                    *   - [x] [Configuring each kubelet in your cluster using kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/kubelet-integration/) 
                    *   - [x] [Dual-stack support with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/dual-stack-support/) 

            *   - [x] [Turnkey Cloud Solutions](https://kubernetes.io/docs/setup/production-environment/turnkey-solutions/) 

        *   - [x] [Best practices](https://kubernetes.io/docs/setup/best-practices/) 
            *   - [x] [Considerations for large clusters](https://kubernetes.io/docs/setup/best-practices/cluster-large/) 
            *   - [x] [Running in multiple zones](https://kubernetes.io/docs/setup/best-practices/multiple-zones/) 
            *   - [x] [Validate node setup](https://kubernetes.io/docs/setup/best-practices/node-conformance/) 
            *   - [x] [Enforcing Pod Security Standards](https://kubernetes.io/docs/setup/best-practices/enforcing-pod-security-standards/) 
            *   - [x] [PKI certificates and requirements](https://kubernetes.io/docs/setup/best-practices/certificates/) 

    *   - [x] [Concepts](https://kubernetes.io/docs/concepts/) 
        *   - [x] [Overview](https://kubernetes.io/docs/concepts/overview/) 
            *   - [x] [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/) 
            *   - [x] [Objects In Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/) 
                *   - [x] [Kubernetes Object Management](https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/) 
                *   - [x] [Object Names and IDs](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/) 
                *   - [x] [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) 
                *   - [x] [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) 
                *   - [x] [Annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) 
                *   - [x] [Field Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/) 
                *   - [x] [Finalizers](https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/) 
                *   - [x] [Owners and Dependents](https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/) 
                *   - [x] [Recommended Labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/) 
                *   - [x] [Storage Versions](https://kubernetes.io/docs/concepts/overview/working-with-objects/storage-version/) 

            *   - [x] [The Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/) 

        *   - [x] [Cluster Architecture](https://kubernetes.io/docs/concepts/architecture/) 
            *   - [x] [Nodes](https://kubernetes.io/docs/concepts/architecture/nodes/) 
            *   - [x] [Communication between Nodes and the Control Plane](https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication/) 
            *   - [x] [Controllers](https://kubernetes.io/docs/concepts/architecture/controller/) 
            *   - [x] [Leases](https://kubernetes.io/docs/concepts/architecture/leases/) 
            *   - [x] [Cloud Controller Manager](https://kubernetes.io/docs/concepts/architecture/cloud-controller/) 
            *   - [x] [About cgroup v2](https://kubernetes.io/docs/concepts/architecture/cgroups/) 
            *   - [x] [Kubernetes Self-Healing](https://kubernetes.io/docs/concepts/architecture/self-healing/) 
            *   - [x] [Garbage Collection](https://kubernetes.io/docs/concepts/architecture/garbage-collection/) 
            *   - [x] [Mixed Version Proxy](https://kubernetes.io/docs/concepts/architecture/mixed-version-proxy/) 

        *   - [x] [Containers](https://kubernetes.io/docs/concepts/containers/) 
            *   - [x] [Images](https://kubernetes.io/docs/concepts/containers/images/) 
            *   - [x] [Container Environment](https://kubernetes.io/docs/concepts/containers/container-environment/) 
            *   - [x] [Runtime Class](https://kubernetes.io/docs/concepts/containers/runtime-class/) 
            *   - [x] [Container Lifecycle Hooks](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/) 
            *   - [x] [Container Runtime Interface (CRI)](https://kubernetes.io/docs/concepts/containers/cri/) 

        *   - [x] [Workloads](https://kubernetes.io/docs/concepts/workloads/) 
            *   - [x] [Pods](https://kubernetes.io/docs/concepts/workloads/pods/) 
                *   - [x] [Pod Lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/) 
                *   - [x] [Init Containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) 
                *   - [x] [Sidecar Containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) 
                *   - [x] [Ephemeral Containers](https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/) 
                *   - [x] [Disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) 
                *   - [x] [Pod Hostname](https://kubernetes.io/docs/concepts/workloads/pods/pod-hostname/) 
                *   - [x] [Pod Quality of Service Classes](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/) 
                *   - [x] [Workload Reference](https://kubernetes.io/docs/concepts/workloads/pods/workload-reference/) 
                *   - [x] [User Namespaces](https://kubernetes.io/docs/concepts/workloads/pods/user-namespaces/) 
                *   - [x] [Downward API](https://kubernetes.io/docs/concepts/workloads/pods/downward-api/) 
                *   - [x] [Advanced Pod Configuration](https://kubernetes.io/docs/concepts/workloads/pods/advanced-pod-config/) 

            *   - [x] [Workload API](https://kubernetes.io/docs/concepts/workloads/workload-api/) 
                *   - [x] [Pod Group Policies](https://kubernetes.io/docs/concepts/workloads/workload-api/policies/) 

            *   - [x] [Workload Management](https://kubernetes.io/docs/concepts/workloads/controllers/) 
                *   - [x] [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) 
                *   - [x] [ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) 
                *   - [x] [StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) 
                *   - [x] [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) 
                *   - [x] [Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/) 
                *   - [x] [Automatic Cleanup for Finished Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/ttlafterfinished/) 
                *   - [x] [CronJob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/) 
                *   - [x] [ReplicationController](https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/) 

            *   - [x] [Managing Workloads](https://kubernetes.io/docs/concepts/workloads/management/) 
            *   - [x] [Autoscaling Workloads](https://kubernetes.io/docs/concepts/workloads/autoscaling/) 
            *   - [x] [Horizontal Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/) 
            *   - [x] [Vertical Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/) 

        *   - [x] [Services, Load Balancing, and Networking](https://kubernetes.io/docs/concepts/services-networking/) 
            *   - [x] [Service](https://kubernetes.io/docs/concepts/services-networking/service/) 
            *   - [x] [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) 
            *   - [x] [Ingress Controllers](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/) 
            *   - [x] [Gateway API](https://kubernetes.io/docs/concepts/services-networking/gateway/) 
            *   - [x] [EndpointSlices](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/) 
            *   - [x] [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) 
            *   - [x] [DNS for Services and Pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/) 
            *   - [x] [IPv4/IPv6 dual-stack](https://kubernetes.io/docs/concepts/services-networking/dual-stack/) 
            *   - [x] [Topology Aware Routing](https://kubernetes.io/docs/concepts/services-networking/topology-aware-routing/) 
            *   - [x] [Networking on Windows](https://kubernetes.io/docs/concepts/services-networking/windows-networking/) 
            *   - [x] [Service ClusterIP allocation](https://kubernetes.io/docs/concepts/services-networking/cluster-ip-allocation/) 
            *   - [x] [Service Internal Traffic Policy](https://kubernetes.io/docs/concepts/services-networking/service-traffic-policy/) 

        *   - [x] [Storage](https://kubernetes.io/docs/concepts/storage/) 
            *   - [x] [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/) 
            *   - [x] [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) 
            *   - [x] [Projected Volumes](https://kubernetes.io/docs/concepts/storage/projected-volumes/) 
            *   - [x] [Ephemeral Volumes](https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/) 
            *   - [x] [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/) 
            *   - [x] [Volume Attributes Classes](https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/) 
            *   - [x] [Dynamic Volume Provisioning](https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/) 
            *   - [x] [Volume Snapshots](https://kubernetes.io/docs/concepts/storage/volume-snapshots/) 
            *   - [x] [Volume Snapshot Classes](https://kubernetes.io/docs/concepts/storage/volume-snapshot-classes/) 
            *   - [x] [CSI Volume Cloning](https://kubernetes.io/docs/concepts/storage/volume-pvc-datasource/) 
            *   - [x] [Storage Capacity](https://kubernetes.io/docs/concepts/storage/storage-capacity/) 
            *   - [x] [Node-specific Volume Limits](https://kubernetes.io/docs/concepts/storage/storage-limits/) 
            *   - [x] [Local ephemeral storage](https://kubernetes.io/docs/concepts/storage/ephemeral-storage/) 
            *   - [x] [Volume Health Monitoring](https://kubernetes.io/docs/concepts/storage/volume-health-monitoring/) 
            *   - [x] [Windows Storage](https://kubernetes.io/docs/concepts/storage/windows-storage/) 

        *   - [x] [Configuration](https://kubernetes.io/docs/concepts/configuration/) 
            *   - [x] [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/) 
            *   - [x] [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) 
            *   - [x] [Liveness, Readiness, and Startup Probes](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/) 
            *   - [x] [Resource Management for Pods and Containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) 
            *   - [x] [Organizing Cluster Access Using kubeconfig Files](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/) 
            *   - [x] [Resource Management for Windows nodes](https://kubernetes.io/docs/concepts/configuration/windows-resource-management/) 

        *   - [x] [Security](https://kubernetes.io/docs/concepts/security/) 
            *   - [x] [Cloud Native Security](https://kubernetes.io/docs/concepts/security/cloud-native-security/ "Cloud Native Security and Kubernetes") 
            *   - [x] [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) 
            *   - [x] [Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/) 
            *   - [x] [Service Accounts](https://kubernetes.io/docs/concepts/security/service-accounts/) 
            *   - [x] [Pod Security Policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/) 
            *   - [x] [Security For Linux Nodes](https://kubernetes.io/docs/concepts/security/linux-security/) 
            *   - [x] [Security For Windows Nodes](https://kubernetes.io/docs/concepts/security/windows-security/) 
            *   - [x] [Controlling Access to the Kubernetes API](https://kubernetes.io/docs/concepts/security/controlling-access/) 
            *   - [x] [Role Based Access Control Good Practices](https://kubernetes.io/docs/concepts/security/rbac-good-practices/) 
            *   - [x] [Good practices for Kubernetes Secrets](https://kubernetes.io/docs/concepts/security/secrets-good-practices/) 
            *   - [x] [Multi-tenancy](https://kubernetes.io/docs/concepts/security/multi-tenancy/) 
            *   - [x] [Hardening Guide - Authentication Mechanisms](https://kubernetes.io/docs/concepts/security/hardening-guide/authentication-mechanisms/) 
            *   - [x] [Hardening Guide - Scheduler Configuration](https://kubernetes.io/docs/concepts/security/hardening-guide/scheduler/) 
            *   - [x] [Kubernetes API Server Bypass Risks](https://kubernetes.io/docs/concepts/security/api-server-bypass-risks/) 
            *   - [x] [Linux kernel security constraints for Pods and containers](https://kubernetes.io/docs/concepts/security/linux-kernel-security-constraints/) 
            *   - [x] [Security Checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) 
            *   - [x] [Application Security Checklist](https://kubernetes.io/docs/concepts/security/application-security-checklist/) 

        *   - [x] [Policies](https://kubernetes.io/docs/concepts/policy/) 
            *   - [x] [Limit Ranges](https://kubernetes.io/docs/concepts/policy/limit-range/) 
            *   - [x] [Resource Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/) 
            *   - [x] [Process ID Limits And Reservations](https://kubernetes.io/docs/concepts/policy/pid-limiting/) 
            *   - [x] [Node Resource Managers](https://kubernetes.io/docs/concepts/policy/node-resource-managers/) 

        *   - [x] [Scheduling, Preemption and Eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/) 
            *   - [x] [Kubernetes Scheduler](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/) 
            *   - [x] [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) 
            *   - [x] [Pod Overhead](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-overhead/) 
            *   - [x] [Pod Scheduling Readiness](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-scheduling-readiness/) 
            *   - [x] [Pod Topology Spread Constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/) 
            *   - [x] [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) 
            *   - [x] [Scheduling Framework](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/) 
            *   - [x] [Dynamic Resource Allocation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/) 
            *   - [x] [Gang Scheduling](https://kubernetes.io/docs/concepts/scheduling-eviction/gang-scheduling/) 
            *   - [x] [Scheduler Performance Tuning](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduler-perf-tuning/) 
            *   - [x] [Resource Bin Packing](https://kubernetes.io/docs/concepts/scheduling-eviction/resource-bin-packing/) 
            *   - [x] [Pod Priority and Preemption](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/) 
            *   - [x] [Node-pressure Eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/) 
            *   - [x] [API-initiated Eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/api-eviction/) 
            *   - [x] [Node Declared Features](https://kubernetes.io/docs/concepts/scheduling-eviction/node-declared-features/) 

        *   - [x] [Cluster Administration](https://kubernetes.io/docs/concepts/cluster-administration/) 
            *   - [x] [Node Shutdowns](https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/) 
            *   - [x] [Swap memory management](https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/) 
            *   - [x] [Node Autoscaling](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/) 
            *   - [x] [Certificates](https://kubernetes.io/docs/concepts/cluster-administration/certificates/) 
            *   - [x] [Cluster Networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/) 
            *   - [x] [Observability](https://kubernetes.io/docs/concepts/cluster-administration/observability/) 
            *   - [x] [Admission Webhook Good Practices](https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/) 
            *   - [x] [Good practices for Dynamic Resource Allocation as a Cluster Admin](https://kubernetes.io/docs/concepts/cluster-administration/dra/) 
            *   - [x] [Logging Architecture](https://kubernetes.io/docs/concepts/cluster-administration/logging/) 
            *   - [x] [Compatibility Version For Kubernetes Control Plane Components](https://kubernetes.io/docs/concepts/cluster-administration/compatibility-version/) 
            *   - [x] [Metrics For Kubernetes System Components](https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/) 
            *   - [x] [Metrics for Kubernetes Object States](https://kubernetes.io/docs/concepts/cluster-administration/kube-state-metrics/) 
            *   - [x] [System Logs](https://kubernetes.io/docs/concepts/cluster-administration/system-logs/) 
            *   - [x] [Traces For Kubernetes System Components](https://kubernetes.io/docs/concepts/cluster-administration/system-traces/) 
            *   - [x] [Proxies in Kubernetes](https://kubernetes.io/docs/concepts/cluster-administration/proxies/) 
            *   - [x] [API Priority and Fairness](https://kubernetes.io/docs/concepts/cluster-administration/flow-control/) 
            *   - [x] [Installing Addons](https://kubernetes.io/docs/concepts/cluster-administration/addons/) 
            *   - [x] [Coordinated Leader Election](https://kubernetes.io/docs/concepts/cluster-administration/coordinated-leader-election/) 

        *   - [x] [Windows in Kubernetes](https://kubernetes.io/docs/concepts/windows/) 
            *   - [x] [Windows containers in Kubernetes](https://kubernetes.io/docs/concepts/windows/intro/) 
            *   - [x] [Guide for Running Windows Containers in Kubernetes](https://kubernetes.io/docs/concepts/windows/user-guide/) 

        *   - [x] [Extending Kubernetes](https://kubernetes.io/docs/concepts/extend-kubernetes/) 
            *   - [x] [Compute, Storage, and Networking Extensions](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/) 
                *   - [x] [Network Plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/) 
                *   - [x] [Device Plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/) 

            *   - [x] [Extending the Kubernetes API](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/) 
                *   - [x] [Custom Resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) 
                *   - [x] [Kubernetes API Aggregation Layer](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/) 

            *   - [x] [Operator pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) 

    *   - [x] [Tasks](https://kubernetes.io/docs/tasks/) 
        *   - [x] [Install Tools](https://kubernetes.io/docs/tasks/tools/) 
            *   - [x] [Install and Set Up kubectl on Linux](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/) 
            *   - [x] [Install and Set Up kubectl on macOS](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/) 
            *   - [x] [Install and Set Up kubectl on Windows](https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/) 

        *   - [x] [Administer a Cluster](https://kubernetes.io/docs/tasks/administer-cluster/) 
            *   - [x] [Administration with kubeadm](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/) 
                *   - [x] [Adding Linux worker nodes](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/adding-linux-nodes/) 
                *   - [x] [Adding Windows worker nodes](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/adding-windows-nodes/) 
                *   - [x] [Upgrading kubeadm clusters](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/) 
                *   - [x] [Upgrading Linux nodes](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/upgrading-linux-nodes/) 
                *   - [x] [Upgrading Windows nodes](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/upgrading-windows-nodes/) 
                *   - [x] [Configuring a cgroup driver](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/configure-cgroup-driver/) 
                *   - [x] [Certificate Management with kubeadm](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/) 
                *   - [x] [Reconfiguring a kubeadm cluster](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-reconfigure/) 
                *   - [x] [Changing The Kubernetes Package Repository](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/change-package-repository/) 

            *   - [x] [Overprovision Node Capacity For A Cluster](https://kubernetes.io/docs/tasks/administer-cluster/node-overprovisioning/) 
            *   - [x] [Migrating from dockershim](https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/) 
                *   - [x] [Changing the Container Runtime on a Node from Docker Engine to containerd](https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd/) 
                *   - [x] [Find Out What Container Runtime is Used on a Node](https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use/) 
                *   - [x] [Troubleshooting CNI plugin-related errors](https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/troubleshooting-cni-plugin-related-errors/) 
                *   - [x] [Check whether dockershim removal affects you](https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you/) 
                *   - [x] [Migrating telemetry and security agents from dockershim](https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents/) 

            *   - [x] [Generate Certificates Manually](https://kubernetes.io/docs/tasks/administer-cluster/certificates/) 
            *   - [x] [Manage Memory, CPU, and API Resources](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/) 
                *   - [x] [Configure Default Memory Requests and Limits for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/) 
                *   - [x] [Configure Default CPU Requests and Limits for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/) 
                *   - [x] [Configure Minimum and Maximum Memory Constraints for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/) 
                *   - [x] [Configure Minimum and Maximum CPU Constraints for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/) 
                *   - [x] [Configure Memory and CPU Quotas for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/) 
                *   - [x] [Configure a Pod Quota for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-pod-namespace/) 

            *   - [x] [Install a Network Policy Provider](https://kubernetes.io/docs/tasks/administer-cluster/network-policy-provider/) 
                *   - [x] [Use Antrea for NetworkPolicy](https://kubernetes.io/docs/tasks/administer-cluster/network-policy-provider/antrea-network-policy/) 
                *   - [x] [Use Calico for NetworkPolicy](https://kubernetes.io/docs/tasks/administer-cluster/network-policy-provider/calico-network-policy/) 
                *   - [x] [Use Cilium for NetworkPolicy](https://kubernetes.io/docs/tasks/administer-cluster/network-policy-provider/cilium-network-policy/) 
                *   - [x] [Use Kube-router for NetworkPolicy](https://kubernetes.io/docs/tasks/administer-cluster/network-policy-provider/kube-router-network-policy/) 
                *   - [x] [Romana for NetworkPolicy](https://kubernetes.io/docs/tasks/administer-cluster/network-policy-provider/romana-network-policy/) 
                *   - [x] [Weave Net for NetworkPolicy](https://kubernetes.io/docs/tasks/administer-cluster/network-policy-provider/weave-network-policy/) 

            *   - [x] [Access Clusters Using the Kubernetes API](https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-api/) 
            *   - [x] [Enable Or Disable Feature Gates](https://kubernetes.io/docs/tasks/administer-cluster/configure-feature-gates/) 
            *   - [x] [Advertise Extended Resources for a Node](https://kubernetes.io/docs/tasks/administer-cluster/extended-resource-node/) 
            *   - [x] [Autoscale the DNS Service in a Cluster](https://kubernetes.io/docs/tasks/administer-cluster/dns-horizontal-autoscaling/) 
            *   - [x] [Change the Access Mode of a PersistentVolume to ReadWriteOncePod](https://kubernetes.io/docs/tasks/administer-cluster/change-pv-access-mode-readwriteoncepod/) 
            *   - [x] [Change the default StorageClass](https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/) 
            *   - [x] [Switching from Polling to CRI Event-based Updates to Container Status](https://kubernetes.io/docs/tasks/administer-cluster/switch-to-evented-pleg/) 
            *   - [x] [Change the Reclaim Policy of a PersistentVolume](https://kubernetes.io/docs/tasks/administer-cluster/change-pv-reclaim-policy/) 
            *   - [x] [Cloud Controller Manager Administration](https://kubernetes.io/docs/tasks/administer-cluster/running-cloud-controller/) 
            *   - [x] [Configure a kubelet image credential provider](https://kubernetes.io/docs/tasks/administer-cluster/kubelet-credential-provider/) 
            *   - [x] [Configure Quotas for API Objects](https://kubernetes.io/docs/tasks/administer-cluster/quota-api-object/) 
            *   - [x] [Control CPU Management Policies on the Node](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/) 
            *   - [x] [Control Memory Management Policies on a Node](https://kubernetes.io/docs/tasks/administer-cluster/memory-manager/) 
            *   - [x] [Control Topology Management Policies on a node](https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/) 
            *   - [x] [Customizing DNS Service](https://kubernetes.io/docs/tasks/administer-cluster/dns-custom-nameservers/) 
            *   - [x] [Debugging DNS Resolution](https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/) 
            *   - [x] [Declare Network Policy](https://kubernetes.io/docs/tasks/administer-cluster/declare-network-policy/) 
            *   - [x] [Developing Cloud Controller Manager](https://kubernetes.io/docs/tasks/administer-cluster/developing-cloud-controller-manager/) 
            *   - [x] [Enable Or Disable A Kubernetes API](https://kubernetes.io/docs/tasks/administer-cluster/enable-disable-api/) 
            *   - [x] [Encrypting Confidential Data at Rest](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/) 
            *   - [x] [Decrypt Confidential Data that is Already Encrypted at Rest](https://kubernetes.io/docs/tasks/administer-cluster/decrypt-data/) 
            *   - [x] [Guaranteed Scheduling For Critical Add-On Pods](https://kubernetes.io/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/) 
            *   - [x] [IP Masquerade Agent User Guide](https://kubernetes.io/docs/tasks/administer-cluster/ip-masq-agent/) 
            *   - [x] [Limit Storage Consumption](https://kubernetes.io/docs/tasks/administer-cluster/limit-storage-consumption/) 
            *   - [x] [Migrate Replicated Control Plane To Use Cloud Controller Manager](https://kubernetes.io/docs/tasks/administer-cluster/controller-manager-leader-migration/) 
            *   - [x] [Operating etcd clusters for Kubernetes](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/) 
            *   - [x] [Reserve Compute Resources for System Daemons](https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/) 
            *   - [x] [Running Kubernetes Node Components as a Non-root User](https://kubernetes.io/docs/tasks/administer-cluster/kubelet-in-userns/) 
            *   - [x] [Safely Drain a Node](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/) 
            *   - [x] [Securing a Cluster](https://kubernetes.io/docs/tasks/administer-cluster/securing-a-cluster/) 
            *   - [x] [Set Kubelet Parameters Via A Configuration File](https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/) 
            *   - [x] [Share a Cluster with Namespaces](https://kubernetes.io/docs/tasks/administer-cluster/namespaces/) 
            *   - [x] [Upgrade A Cluster](https://kubernetes.io/docs/tasks/administer-cluster/cluster-upgrade/) 
            *   - [x] [Use Cascading Deletion in a Cluster](https://kubernetes.io/docs/tasks/administer-cluster/use-cascading-deletion/) 
            *   - [x] [Using a KMS provider for data encryption](https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/) 
            *   - [x] [Using CoreDNS for Service Discovery](https://kubernetes.io/docs/tasks/administer-cluster/coredns/) 
            *   - [x] [Using NodeLocal DNSCache in Kubernetes Clusters](https://kubernetes.io/docs/tasks/administer-cluster/nodelocaldns/) 
            *   - [x] [Using sysctls in a Kubernetes Cluster](https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/) 
            *   - [x] [Verify Signed Kubernetes Artifacts](https://kubernetes.io/docs/tasks/administer-cluster/verify-signed-artifacts/) 

        *   - [x] [Configure Pods and Containers](https://kubernetes.io/docs/tasks/configure-pod-container/) 
            *   - [x] [Assign Memory Resources to Containers and Pods](https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/) 
            *   - [x] [Assign CPU Resources to Containers and Pods](https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/) 
            *   - [x] [Assign Devices to Pods and Containers](https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/) 
                *   - [x] [Set Up DRA in a Cluster](https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/set-up-dra-cluster/) 
                *   - [x] [Allocate Devices to Workloads with DRA](https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/allocate-devices-dra/) 

            *   - [x] [Assign Pod-level CPU and memory resources](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pod-level-resources/) 
            *   - [x] [Configure GMSA for Windows Pods and containers](https://kubernetes.io/docs/tasks/configure-pod-container/configure-gmsa/) 
            *   - [x] [Resize CPU and Memory Resources assigned to Containers](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/) 
            *   - [x] [Resize CPU and Memory Resources assigned to Pods](https://kubernetes.io/docs/tasks/configure-pod-container/resize-pod-resources/) 
            *   - [x] [Configure RunAsUserName for Windows pods and containers](https://kubernetes.io/docs/tasks/configure-pod-container/configure-runasusername/) 
            *   - [x] [Create a Windows HostProcess Pod](https://kubernetes.io/docs/tasks/configure-pod-container/create-hostprocess-pod/) 
            *   - [x] [Configure Quality of Service for Pods](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/) 
            *   - [x] [Assign Extended Resources to a Container](https://kubernetes.io/docs/tasks/configure-pod-container/extended-resource/) 
            *   - [x] [Configure a Pod to Use a Volume for Storage](https://kubernetes.io/docs/tasks/configure-pod-container/configure-volume-storage/) 
            *   - [x] [Configure a Pod to Use a PersistentVolume for Storage](https://kubernetes.io/docs/tasks/configure-pod-container/configure-persistent-volume-storage/) 
            *   - [x] [Configure a Pod to Use a Projected Volume for Storage](https://kubernetes.io/docs/tasks/configure-pod-container/configure-projected-volume-storage/) 
            *   - [x] [Configure a Security Context for a Pod or Container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) 
            *   - [x] [Configure Service Accounts for Pods](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) 
            *   - [x] [Pull an Image from a Private Registry](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/) 
            *   - [x] [Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) 
            *   - [x] [Assign Pods to Nodes](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes/) 
            *   - [x] [Assign Pods to Nodes using Node Affinity](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity/) 
            *   - [x] [Configure Pod Initialization](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-initialization/) 
            *   - [x] [Attach Handlers to Container Lifecycle Events](https://kubernetes.io/docs/tasks/configure-pod-container/attach-handler-lifecycle-event/) 
            *   - [x] [Configure a Pod to Use a ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) 
            *   - [x] [Share Process Namespace between Containers in a Pod](https://kubernetes.io/docs/tasks/configure-pod-container/share-process-namespace/) 
            *   - [x] [Use a User Namespace With a Pod](https://kubernetes.io/docs/tasks/configure-pod-container/user-namespaces/) 
            *   - [x] [Use an Image Volume With a Pod](https://kubernetes.io/docs/tasks/configure-pod-container/image-volumes/) 
            *   - [x] [Create static Pods](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/) 
            *   - [x] [Translate a Docker Compose File to Kubernetes Resources](https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/) 
            *   - [x] [Enforce Pod Security Standards by Configuring the Built-in Admission Controller](https://kubernetes.io/docs/tasks/configure-pod-container/enforce-standards-admission-controller/) 
            *   - [x] [Enforce Pod Security Standards with Namespace Labels](https://kubernetes.io/docs/tasks/configure-pod-container/enforce-standards-namespace-labels/) 
            *   - [x] [Migrate from PodSecurityPolicy to the Built-In PodSecurity Admission Controller](https://kubernetes.io/docs/tasks/configure-pod-container/migrate-from-psp/) 

        *   - [x] [Monitoring, Logging, and Debugging](https://kubernetes.io/docs/tasks/debug/) 
            *   - [x] [Logging in Kubernetes](https://kubernetes.io/docs/tasks/debug/logging/) 
            *   - [x] [Monitoring in Kubernetes](https://kubernetes.io/docs/tasks/debug/monitoring/) 
            *   - [x] [Troubleshooting Applications](https://kubernetes.io/docs/tasks/debug/debug-application/) 
                *   - [x] [Debug Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods/) 
                *   - [x] [Debug Services](https://kubernetes.io/docs/tasks/debug/debug-application/debug-service/) 
                *   - [x] [Debug a StatefulSet](https://kubernetes.io/docs/tasks/debug/debug-application/debug-statefulset/) 
                *   - [x] [Determine the Reason for Pod Failure](https://kubernetes.io/docs/tasks/debug/debug-application/determine-reason-pod-failure/) 
                *   - [x] [Debug Init Containers](https://kubernetes.io/docs/tasks/debug/debug-application/debug-init-containers/) 
                *   - [x] [Debug Running Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/) 
                *   - [x] [Get a Shell to a Running Container](https://kubernetes.io/docs/tasks/debug/debug-application/get-shell-running-container/) 

            *   - [x] [Troubleshooting Clusters](https://kubernetes.io/docs/tasks/debug/debug-cluster/) 
                *   - [x] [Troubleshooting kubectl](https://kubernetes.io/docs/tasks/debug/debug-cluster/troubleshoot-kubectl/) 
                *   - [x] [Resource metrics pipeline](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/) 
                *   - [x] [Tools for Monitoring Resources](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-usage-monitoring/) 
                *   - [x] [Monitor Node Health](https://kubernetes.io/docs/tasks/debug/debug-cluster/monitor-node-health/) 
                *   - [x] [Debugging Kubernetes nodes with crictl](https://kubernetes.io/docs/tasks/debug/debug-cluster/crictl/) 
                *   - [x] [Troubleshooting Topology Management](https://kubernetes.io/docs/tasks/debug/debug-cluster/topology/) 
                *   - [x] [Auditing](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/) 
                *   - [x] [Debugging Kubernetes Nodes With Kubectl](https://kubernetes.io/docs/tasks/debug/debug-cluster/kubectl-node-debug/) 
                *   - [x] [Developing and debugging services locally using telepresence](https://kubernetes.io/docs/tasks/debug/debug-cluster/local-debugging/) 
                *   - [x] [Windows debugging tips](https://kubernetes.io/docs/tasks/debug/debug-cluster/windows/) 

        *   - [x] [Manage Kubernetes Objects](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/) 
            *   - [x] [Declarative Management of Kubernetes Objects Using Configuration Files](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/) 
            *   - [x] [Declarative Management of Kubernetes Objects Using Kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/) 
            *   - [x] [Managing Kubernetes Objects Using Imperative Commands](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/imperative-command/) 
            *   - [x] [Imperative Management of Kubernetes Objects Using Configuration Files](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/imperative-config/) 
            *   - [x] [Update API Objects in Place Using kubectl patch](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch/) 
            *   - [x] [Migrate Kubernetes Objects Using Storage Version Migration](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/storage-version-migration/) 

        *   - [x] [Managing Secrets](https://kubernetes.io/docs/tasks/configmap-secret/) 
            *   - [x] [Managing Secrets using kubectl](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kubectl/) 
            *   - [x] [Managing Secrets using Configuration File](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-config-file/) 
            *   - [x] [Managing Secrets using Kustomize](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kustomize/) 

        *   - [x] [Inject Data Into Applications](https://kubernetes.io/docs/tasks/inject-data-application/) 
            *   - [x] [Define a Command and Arguments for a Container](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/) 
            *   - [x] [Define Dependent Environment Variables](https://kubernetes.io/docs/tasks/inject-data-application/define-interdependent-environment-variables/) 
            *   - [x] [Define Environment Variables for a Container](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/) 
            *   - [x] [Define Environment Variable Values Using An Init Container](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-via-file/) 
            *   - [x] [Expose Pod Information to Containers Through Environment Variables](https://kubernetes.io/docs/tasks/inject-data-application/environment-variable-expose-pod-information/) 
            *   - [x] [Expose Pod Information to Containers Through Files](https://kubernetes.io/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/) 
            *   - [x] [Distribute Credentials Securely Using Secrets](https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/) 

        *   - [x] [Run Applications](https://kubernetes.io/docs/tasks/run-application/) 
            *   - [x] [Run a Stateless Application Using a Deployment](https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/) 
            *   - [x] [Run a Single-Instance Stateful Application](https://kubernetes.io/docs/tasks/run-application/run-single-instance-stateful-application/) 
            *   - [x] [Run a Replicated Stateful Application](https://kubernetes.io/docs/tasks/run-application/run-replicated-stateful-application/) 
            *   - [x] [Scale a StatefulSet](https://kubernetes.io/docs/tasks/run-application/scale-stateful-set/) 
            *   - [x] [Delete a StatefulSet](https://kubernetes.io/docs/tasks/run-application/delete-stateful-set/) 
            *   - [x] [Force Delete StatefulSet Pods](https://kubernetes.io/docs/tasks/run-application/force-delete-stateful-set-pod/) 
            *   - [x] [HorizontalPodAutoscaler Walkthrough](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/) 
            *   - [x] [Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) 
            *   - [x] [Accessing the Kubernetes API from a Pod](https://kubernetes.io/docs/tasks/run-application/access-api-from-pod/) 

        *   - [x] [Run Jobs](https://kubernetes.io/docs/tasks/job/) 
            *   - [x] [Running Automated Tasks with a CronJob](https://kubernetes.io/docs/tasks/job/automated-tasks-with-cron-jobs/) 
            *   - [x] [Coarse Parallel Processing Using a Work Queue](https://kubernetes.io/docs/tasks/job/coarse-parallel-processing-work-queue/) 
            *   - [x] [Fine Parallel Processing Using a Work Queue](https://kubernetes.io/docs/tasks/job/fine-parallel-processing-work-queue/) 
            *   - [x] [Indexed Job for Parallel Processing with Static Work Assignment](https://kubernetes.io/docs/tasks/job/indexed-parallel-processing-static/) 
            *   - [x] [Job with Pod-to-Pod Communication](https://kubernetes.io/docs/tasks/job/job-with-pod-to-pod-communication/) 
            *   - [x] [Parallel Processing using Expansions](https://kubernetes.io/docs/tasks/job/parallel-processing-expansion/) 
            *   - [x] [Handling retriable and non-retriable pod failures with Pod failure policy](https://kubernetes.io/docs/tasks/job/pod-failure-policy/) 

        *   - [x] [Access Applications in a Cluster](https://kubernetes.io/docs/tasks/access-application-cluster/) 
            *   - [x] [Deploy and Access the Kubernetes Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/) 
            *   - [x] [Accessing Clusters](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/) 
            *   - [x] [Configure Access to Multiple Clusters](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) 
            *   - [x] [Use Port Forwarding to Access Applications in a Cluster](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/) 
            *   - [x] [Use a Service to Access an Application in a Cluster](https://kubernetes.io/docs/tasks/access-application-cluster/service-access-application-cluster/) 
            *   - [x] [Connect a Frontend to a Backend Using Services](https://kubernetes.io/docs/tasks/access-application-cluster/connecting-frontend-backend/) 
            *   - [x] [Create an External Load Balancer](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/) 
            *   - [x] [List All Container Images Running in a Cluster](https://kubernetes.io/docs/tasks/access-application-cluster/list-all-running-container-images/) 
            *   - [x] [Communicate Between Containers in the Same Pod Using a Shared Volume](https://kubernetes.io/docs/tasks/access-application-cluster/communicate-containers-same-pod-shared-volume/) 
            *   - [x] [Configure DNS for a Cluster](https://kubernetes.io/docs/tasks/access-application-cluster/configure-dns-cluster/) 
            *   - [x] [Access Services Running on Clusters](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster-services/) 

        *   - [x] [Extend Kubernetes](https://kubernetes.io/docs/tasks/extend-kubernetes/) 
            *   - [x] [Configure the Aggregation Layer](https://kubernetes.io/docs/tasks/extend-kubernetes/configure-aggregation-layer/) 
            *   - [x] [Use Custom Resources](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/) 
                *   - [x] [Extend the Kubernetes API with CustomResourceDefinitions](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/) 
                *   - [x] [Versions in CustomResourceDefinitions](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/) 

            *   - [x] [Set up an Extension API Server](https://kubernetes.io/docs/tasks/extend-kubernetes/setup-extension-api-server/) 
            *   - [x] [Configure Multiple Schedulers](https://kubernetes.io/docs/tasks/extend-kubernetes/configure-multiple-schedulers/) 
            *   - [x] [Use an HTTP Proxy to Access the Kubernetes API](https://kubernetes.io/docs/tasks/extend-kubernetes/http-proxy-access-api/) 
            *   - [x] [Use a SOCKS5 Proxy to Access the Kubernetes API](https://kubernetes.io/docs/tasks/extend-kubernetes/socks5-proxy-access-api/) 
            *   - [x] [Set up Konnectivity service](https://kubernetes.io/docs/tasks/extend-kubernetes/setup-konnectivity/) 

        *   - [x] [TLS](https://kubernetes.io/docs/tasks/tls/) 
            *   - [x] [Issue a Certificate for a Kubernetes API Client Using A CertificateSigningRequest](https://kubernetes.io/docs/tasks/tls/certificate-issue-client-csr/) 
            *   - [x] [Configure Certificate Rotation for the Kubelet](https://kubernetes.io/docs/tasks/tls/certificate-rotation/) 
            *   - [x] [Manage TLS Certificates in a Cluster](https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster/) 
            *   - [x] [Manual Rotation of CA Certificates](https://kubernetes.io/docs/tasks/tls/manual-rotation-of-ca-certificates/) 

        *   - [x] [Manage Cluster Daemons](https://kubernetes.io/docs/tasks/manage-daemon/) 
            *   - [x] [Building a Basic DaemonSet](https://kubernetes.io/docs/tasks/manage-daemon/create-daemon-set/) 
            *   - [x] [Perform a Rolling Update on a DaemonSet](https://kubernetes.io/docs/tasks/manage-daemon/update-daemon-set/) 
            *   - [x] [Perform a Rollback on a DaemonSet](https://kubernetes.io/docs/tasks/manage-daemon/rollback-daemon-set/) 
            *   - [x] [Running Pods on Only Some Nodes](https://kubernetes.io/docs/tasks/manage-daemon/pods-some-nodes/) 

        *   - [x] [Networking](https://kubernetes.io/docs/tasks/network/) 
            *   - [x] [Adding entries to Pod /etc/hosts with HostAliases](https://kubernetes.io/docs/tasks/network/customize-hosts-file-for-pods/) 
            *   - [x] [Extend Service IP Ranges](https://kubernetes.io/docs/tasks/network/extend-service-ip-ranges/) 
            *   - [x] [Kubernetes Default ServiceCIDR Reconfiguration](https://kubernetes.io/docs/tasks/network/reconfigure-default-service-ip-ranges/) 
            *   - [x] [Validate IPv4/IPv6 dual-stack](https://kubernetes.io/docs/tasks/network/validate-dual-stack/) 

        *   - [x] [Extend kubectl with plugins](https://kubernetes.io/docs/tasks/extend-kubectl/kubectl-plugins/) 
        *   - [x] [Manage HugePages](https://kubernetes.io/docs/tasks/manage-hugepages/scheduling-hugepages/) 
        *   - [x] [Schedule GPUs](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/) 

    *   - [x] [Tutorials](https://kubernetes.io/docs/tutorials/) 
        *   - [x] [Hello Minikube](https://kubernetes.io/docs/tutorials/hello-minikube/) 
        *   - [x] [Learn Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/) 
            *   - [x] [Create a Cluster](https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/) 
                *   - [x] [Using Minikube to Create a Cluster](https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/cluster-intro/) 

            *   - [x] [Deploy an App](https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/) 
                *   - [x] [Using kubectl to Create a Deployment](https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/) 

            *   - [x] [Explore Your App](https://kubernetes.io/docs/tutorials/kubernetes-basics/explore/) 
                *   - [x] [Viewing Pods and Nodes](https://kubernetes.io/docs/tutorials/kubernetes-basics/explore/explore-intro/) 

            *   - [x] [Expose Your App Publicly](https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/) 
                *   - [x] [Using a Service to Expose Your App](https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/expose-intro/) 

            *   - [x] [Scale Your App](https://kubernetes.io/docs/tutorials/kubernetes-basics/scale/) 
                *   - [x] [Running Multiple Instances of Your App](https://kubernetes.io/docs/tutorials/kubernetes-basics/scale/scale-intro/) 

            *   - [x] [Update Your App](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/) 
                *   - [x] [Performing a Rolling Update](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/) 

        *   - [x] [Configuration](https://kubernetes.io/docs/tutorials/configuration/) 
            *   - [x] [Updating Configuration via a ConfigMap](https://kubernetes.io/docs/tutorials/configuration/updating-configuration-via-a-configmap/) 
            *   - [x] [Configuring Redis using a ConfigMap](https://kubernetes.io/docs/tutorials/configuration/configure-redis-using-configmap/) 
            *   - [x] [Adopting Sidecar Containers](https://kubernetes.io/docs/tutorials/configuration/pod-sidecar-containers/) 

        *   - [x] [Security](https://kubernetes.io/docs/tutorials/security/) 
            *   - [x] [Apply Pod Security Standards at the Cluster Level](https://kubernetes.io/docs/tutorials/security/cluster-level-pss/) 
            *   - [x] [Apply Pod Security Standards at the Namespace Level](https://kubernetes.io/docs/tutorials/security/ns-level-pss/) 
            *   - [x] [Restrict a Container's Access to Resources with AppArmor](https://kubernetes.io/docs/tutorials/security/apparmor/) 
            *   - [x] [Restrict a Container's Syscalls with seccomp](https://kubernetes.io/docs/tutorials/security/seccomp/) 

        *   - [x] [Stateless Applications](https://kubernetes.io/docs/tutorials/stateless-application/) 
            *   - [x] [Exposing an External IP Address to Access an Application in a Cluster](https://kubernetes.io/docs/tutorials/stateless-application/expose-external-ip-address/) 
            *   - [x] [Example: Deploying PHP Guestbook application with Redis](https://kubernetes.io/docs/tutorials/stateless-application/guestbook/) 

        *   - [x] [Stateful Applications](https://kubernetes.io/docs/tutorials/stateful-application/) 
            *   - [x] [StatefulSet Basics](https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/) 
            *   - [x] [Example: Deploying WordPress and MySQL with Persistent Volumes](https://kubernetes.io/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/) 
            *   - [x] [Example: Deploying Cassandra with a StatefulSet](https://kubernetes.io/docs/tutorials/stateful-application/cassandra/) 
            *   - [x] [Running ZooKeeper, A Distributed System Coordinator](https://kubernetes.io/docs/tutorials/stateful-application/zookeeper/) 

        *   - [x] [Cluster Management](https://kubernetes.io/docs/tutorials/cluster-management/) 
            *   - [x] [Running Kubelet in Standalone Mode](https://kubernetes.io/docs/tutorials/cluster-management/kubelet-standalone/) 
            *   - [x] [Configuring swap memory on Kubernetes nodes](https://kubernetes.io/docs/tutorials/cluster-management/provision-swap-memory/) 
            *   - [x] [Install Drivers and Allocate Devices with DRA](https://kubernetes.io/docs/tutorials/cluster-management/install-use-dra/) 
            *   - [x] [Namespaces Walkthrough](https://kubernetes.io/docs/tutorials/cluster-management/namespaces-walkthrough/) 

        *   - [x] [Services](https://kubernetes.io/docs/tutorials/services/) 
            *   - [x] [Connecting Applications with Services](https://kubernetes.io/docs/tutorials/services/connect-applications-service/) 
            *   - [x] [Using Source IP](https://kubernetes.io/docs/tutorials/services/source-ip/) 
            *   - [x] [Explore Termination Behavior for Pods And Their Endpoints](https://kubernetes.io/docs/tutorials/services/pods-and-endpoint-termination-flow/) 

    *   - [x] [Reference](https://kubernetes.io/docs/reference/) 
        *   - [x] [Glossary](https://kubernetes.io/docs/reference/glossary/) 
        *   - [x] [API Overview](https://kubernetes.io/docs/reference/using-api/) 
            *   - [x] [Declarative API Validation](https://kubernetes.io/docs/reference/using-api/declarative-validation/) 
            *   - [x] [Kubernetes API Concepts](https://kubernetes.io/docs/reference/using-api/api-concepts/) 
            *   - [x] [Server-Side Apply](https://kubernetes.io/docs/reference/using-api/server-side-apply/) 
            *   - [x] [Client Libraries](https://kubernetes.io/docs/reference/using-api/client-libraries/) 
            *   - [x] [Common Expression Language in Kubernetes](https://kubernetes.io/docs/reference/using-api/cel/) 
            *   - [x] [Kubernetes Deprecation Policy](https://kubernetes.io/docs/reference/using-api/deprecation-policy/) 
            *   - [x] [Deprecated API Migration Guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/) 
            *   - [x] [Kubernetes API health endpoints](https://kubernetes.io/docs/reference/using-api/health-checks/) 

        *   - [x] [API Access Control](https://kubernetes.io/docs/reference/access-authn-authz/) 
            *   - [x] [Authenticating](https://kubernetes.io/docs/reference/access-authn-authz/authentication/) 
            *   - [x] [Authenticating with Bootstrap Tokens](https://kubernetes.io/docs/reference/access-authn-authz/bootstrap-tokens/) 
            *   - [x] [Authorization](https://kubernetes.io/docs/reference/access-authn-authz/authorization/) 
            *   - [x] [Using RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) 
            *   - [x] [Using Node Authorization](https://kubernetes.io/docs/reference/access-authn-authz/node/) 
            *   - [x] [Webhook Mode](https://kubernetes.io/docs/reference/access-authn-authz/webhook/) 
            *   - [x] [Using ABAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/abac/) 
            *   - [x] [Admission Control](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/ "Admission Control in Kubernetes") 
            *   - [x] [Dynamic Admission Control](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/) 
            *   - [x] [Managing Service Accounts](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/) 
            *   - [x] [User Impersonation](https://kubernetes.io/docs/reference/access-authn-authz/user-impersonation/) 
            *   - [x] [Certificates and Certificate Signing Requests](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/) 
            *   - [x] [Mapping PodSecurityPolicies to Pod Security Standards](https://kubernetes.io/docs/reference/access-authn-authz/psp-to-pod-security-standards/) 
            *   - [x] [Kubelet authentication/authorization](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-authn-authz/) 
            *   - [x] [TLS bootstrapping](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/) 
            *   - [x] [Mutating Admission Policy](https://kubernetes.io/docs/reference/access-authn-authz/mutating-admission-policy/) 
            *   - [x] [Validating Admission Policy](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/) 

        *   - [x] [Well-Known Labels, Annotations and Taints](https://kubernetes.io/docs/reference/labels-annotations-taints/) 
            *   - [x] [Audit Annotations](https://kubernetes.io/docs/reference/labels-annotations-taints/audit-annotations/) 

        *   - [x] [Kubernetes API](https://kubernetes.io/docs/reference/kubernetes-api/) 
            *   - [x] [Workload Resources](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/) 
                *   - [x] [Pod](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/) 
                *   - [x] [Binding](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/binding-v1/) 
                *   - [x] [PodTemplate](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-template-v1/) 
                *   - [x] [ReplicationController](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/replication-controller-v1/) 
                *   - [x] [ReplicaSet](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/) 
                *   - [x] [Deployment](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/deployment-v1/) 
                *   - [x] [StatefulSet](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/stateful-set-v1/) 
                *   - [x] [ControllerRevision](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/controller-revision-v1/) 
                *   - [x] [DaemonSet](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/) 
                *   - [x] [Job](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/job-v1/) 
                *   - [x] [CronJob](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/cron-job-v1/) 
                *   - [x] [HorizontalPodAutoscaler](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/) 
                *   - [x] [HorizontalPodAutoscaler](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v2/) 
                *   - [x] [PriorityClass](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/priority-class-v1/) 
                *   - [x] [DeviceTaintRule v1alpha3](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/device-taint-rule-v1alpha3/) 
                *   - [x] [ResourceClaim](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/resource-claim-v1/) 
                *   - [x] [ResourceClaimTemplate](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/resource-claim-template-v1/) 
                *   - [x] [ResourceSlice](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/resource-slice-v1/) 
                *   - [x] [Workload v1alpha1](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/workload-v1alpha1/) 

            *   - [x] [Service Resources](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/) 
                *   - [x] [Service](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/) 
                *   - [x] [Endpoints](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/endpoints-v1/) 
                *   - [x] [EndpointSlice](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/endpoint-slice-v1/) 
                *   - [x] [Ingress](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/ingress-v1/) 
                *   - [x] [IngressClass](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/ingress-class-v1/) 

            *   - [x] [Config and Storage Resources](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/) 
                *   - [x] [ConfigMap](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/config-map-v1/) 
                *   - [x] [Secret](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/secret-v1/) 
                *   - [x] [CSIDriver](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/csi-driver-v1/) 
                *   - [x] [CSINode](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/csi-node-v1/) 
                *   - [x] [CSIStorageCapacity](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/csi-storage-capacity-v1/) 
                *   - [x] [PersistentVolumeClaim](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/) 
                *   - [x] [PersistentVolume](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-v1/) 
                *   - [x] [StorageClass](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-class-v1/) 
                *   - [x] [StorageVersionMigration v1beta1](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1beta1/) 
                *   - [x] [Volume](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume/) 
                *   - [x] [VolumeAttachment](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/) 
                *   - [x] [VolumeAttributesClass](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attributes-class-v1/) 

            *   - [x] [Authentication Resources](https://kubernetes.io/docs/reference/kubernetes-api/authentication-resources/) 
                *   - [x] [ServiceAccount](https://kubernetes.io/docs/reference/kubernetes-api/authentication-resources/service-account-v1/) 
                *   - [x] [TokenRequest](https://kubernetes.io/docs/reference/kubernetes-api/authentication-resources/token-request-v1/) 
                *   - [x] [TokenReview](https://kubernetes.io/docs/reference/kubernetes-api/authentication-resources/token-review-v1/) 
                *   - [x] [CertificateSigningRequest](https://kubernetes.io/docs/reference/kubernetes-api/authentication-resources/certificate-signing-request-v1/) 
                *   - [x] [ClusterTrustBundle v1beta1](https://kubernetes.io/docs/reference/kubernetes-api/authentication-resources/cluster-trust-bundle-v1beta1/) 
                *   - [x] [SelfSubjectReview](https://kubernetes.io/docs/reference/kubernetes-api/authentication-resources/self-subject-review-v1/) 
                *   - [x] [PodCertificateRequest v1beta1](https://kubernetes.io/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1beta1/) 

            *   - [x] [Authorization Resources](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/) 
                *   - [x] [LocalSubjectAccessReview](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/local-subject-access-review-v1/) 
                *   - [x] [SelfSubjectAccessReview](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/self-subject-access-review-v1/) 
                *   - [x] [SelfSubjectRulesReview](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/self-subject-rules-review-v1/) 
                *   - [x] [SubjectAccessReview](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/subject-access-review-v1/) 
                *   - [x] [ClusterRole](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/cluster-role-v1/) 
                *   - [x] [ClusterRoleBinding](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/cluster-role-binding-v1/) 
                *   - [x] [Role](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/role-v1/) 
                *   - [x] [RoleBinding](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/role-binding-v1/) 

            *   - [x] [Policy Resources](https://kubernetes.io/docs/reference/kubernetes-api/policy-resources/) 
                *   - [x] [FlowSchema](https://kubernetes.io/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/) 
                *   - [x] [LimitRange](https://kubernetes.io/docs/reference/kubernetes-api/policy-resources/limit-range-v1/) 
                *   - [x] [ResourceQuota](https://kubernetes.io/docs/reference/kubernetes-api/policy-resources/resource-quota-v1/) 
                *   - [x] [NetworkPolicy](https://kubernetes.io/docs/reference/kubernetes-api/policy-resources/network-policy-v1/) 
                *   - [x] [PodDisruptionBudget](https://kubernetes.io/docs/reference/kubernetes-api/policy-resources/pod-disruption-budget-v1/) 
                *   - [x] [PriorityLevelConfiguration](https://kubernetes.io/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/) 
                *   - [x] [ValidatingAdmissionPolicy](https://kubernetes.io/docs/reference/kubernetes-api/policy-resources/validating-admission-policy-v1/) 
                *   - [x] [ValidatingAdmissionPolicyBinding](https://kubernetes.io/docs/reference/kubernetes-api/policy-resources/validating-admission-policy-binding-v1/) 
                *   - [x] [MutatingAdmissionPolicy v1beta1](https://kubernetes.io/docs/reference/kubernetes-api/policy-resources/mutating-admission-policy-v1beta1/) 
                *   - [x] [MutatingAdmissionPolicyBinding v1alpha1](https://kubernetes.io/docs/reference/kubernetes-api/policy-resources/mutating-admission-policy-binding-v1alpha1/) 

            *   - [x] [Extend Resources](https://kubernetes.io/docs/reference/kubernetes-api/extend-resources/) 
                *   - [x] [CustomResourceDefinition](https://kubernetes.io/docs/reference/kubernetes-api/extend-resources/custom-resource-definition-v1/) 
                *   - [x] [DeviceClass](https://kubernetes.io/docs/reference/kubernetes-api/extend-resources/device-class-v1/) 
                *   - [x] [MutatingWebhookConfiguration](https://kubernetes.io/docs/reference/kubernetes-api/extend-resources/mutating-webhook-configuration-v1/) 
                *   - [x] [ValidatingWebhookConfiguration](https://kubernetes.io/docs/reference/kubernetes-api/extend-resources/validating-webhook-configuration-v1/) 

            *   - [x] [Cluster Resources](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/) 
                *   - [x] [APIService](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/api-service-v1/) 
                *   - [x] [ComponentStatus](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/component-status-v1/) 
                *   - [x] [Event](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/event-v1/) 
                *   - [x] [IPAddress](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/ip-address-v1/) 
                *   - [x] [Lease](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/lease-v1/) 
                *   - [x] [LeaseCandidate v1beta1](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/lease-candidate-v1beta1/) 
                *   - [x] [Namespace](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/) 
                *   - [x] [Node](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/) 
                *   - [x] [RuntimeClass](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/runtime-class-v1/) 
                *   - [x] [ServiceCIDR](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/) 

            *   - [x] [Common Definitions](https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/) 
                *   - [x] [DeleteOptions](https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/delete-options/) 
                *   - [x] [LabelSelector](https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/label-selector/) 
                *   - [x] [ListMeta](https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/list-meta/) 
                *   - [x] [LocalObjectReference](https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/local-object-reference/) 
                *   - [x] [NodeSelectorRequirement](https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/node-selector-requirement/) 
                *   - [x] [ObjectFieldSelector](https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-field-selector/) 
                *   - [x] [ObjectMeta](https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/) 
                *   - [x] [ObjectReference](https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-reference/) 
                *   - [x] [Patch](https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/patch/) 
                *   - [x] [Quantity](https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/quantity/) 
                *   - [x] [ResourceFieldSelector](https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/resource-field-selector/) 
                *   - [x] [Status](https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/status/) 
                *   - [x] [TypedLocalObjectReference](https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/typed-local-object-reference/) 

            *   - [x] [Other Resources](https://kubernetes.io/docs/reference/kubernetes-api/other-resources/) 
                *   - [x] [MutatingAdmissionPolicyBindingList v1beta1](https://kubernetes.io/docs/reference/kubernetes-api/other-resources/mutating-admission-policy-binding-list-v1beta1/) 

            *   - [x] [Common Parameters](https://kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/) 

        *   - [x] [Instrumentation](https://kubernetes.io/docs/reference/instrumentation/) 
            *   - [x] [Service Level Indicator Metrics](https://kubernetes.io/docs/reference/instrumentation/slis/ "Kubernetes Component SLI Metrics") 
            *   - [x] [CRI Pod & Container Metrics](https://kubernetes.io/docs/reference/instrumentation/cri-pod-container-metrics/) 
            *   - [x] [Node metrics data](https://kubernetes.io/docs/reference/instrumentation/node-metrics/) 
            *   - [x] [Understand Pressure Stall Information (PSI) Metrics](https://kubernetes.io/docs/reference/instrumentation/understand-psi-metrics/) 
            *   - [x] [Kubernetes z-pages](https://kubernetes.io/docs/reference/instrumentation/zpages/) 
            *   - [x] [Kubernetes Metrics Reference](https://kubernetes.io/docs/reference/instrumentation/metrics/) 

        *   - [x] [Kubernetes Issues and Security](https://kubernetes.io/docs/reference/issues-security/) 
            *   - [x] [Kubernetes Issue Tracker](https://kubernetes.io/docs/reference/issues-security/issues/) 
            *   - [x] [Kubernetes Security and Disclosure Information](https://kubernetes.io/docs/reference/issues-security/security/) 
            *   - [x] [CVE feed](https://kubernetes.io/docs/reference/issues-security/official-cve-feed/ "Official CVE Feed") 

        *   - [x] [Node Reference Information](https://kubernetes.io/docs/reference/node/) 
            *   - [x] [Kubelet Checkpoint API](https://kubernetes.io/docs/reference/node/kubelet-checkpoint-api/) 
            *   - [x] [Linux Kernel Version Requirements](https://kubernetes.io/docs/reference/node/kernel-version-requirements/) 
            *   - [x] [Articles on dockershim Removal and on Using CRI-compatible Runtimes](https://kubernetes.io/docs/reference/node/topics-on-dockershim-and-cri-compatible-runtimes/) 
            *   - [x] [Node Labels Populated By The Kubelet](https://kubernetes.io/docs/reference/node/node-labels/) 
            *   - [x] [Local Files And Paths Used By The Kubelet](https://kubernetes.io/docs/reference/node/kubelet-files/) 
            *   - [x] [Kubelet Configuration Directory Merging](https://kubernetes.io/docs/reference/node/kubelet-config-directory-merging/) 
            *   - [x] [Kubelet Device Manager API Versions](https://kubernetes.io/docs/reference/node/device-plugin-api-versions/) 
            *   - [x] [Kubelet Systemd Watchdog](https://kubernetes.io/docs/reference/node/systemd-watchdog/) 
            *   - [x] [Node Status](https://kubernetes.io/docs/reference/node/node-status/) 
            *   - [x] [Seccomp and Kubernetes](https://kubernetes.io/docs/reference/node/seccomp/) 
            *   - [x] [Linux Node Swap Behaviors](https://kubernetes.io/docs/reference/node/swap-behavior/) 

        *   - [x] [Networking Reference](https://kubernetes.io/docs/reference/networking/) 
            *   - [x] [Protocols for Services](https://kubernetes.io/docs/reference/networking/service-protocols/) 
            *   - [x] [Ports and Protocols](https://kubernetes.io/docs/reference/networking/ports-and-protocols/) 
            *   - [x] [Virtual IPs and Service Proxies](https://kubernetes.io/docs/reference/networking/virtual-ips/) 

        *   - [x] [Setup tools](https://kubernetes.io/docs/reference/setup-tools/) 
            *   - [x] [Kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/) 
                *   - [x] [kubeadm init](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/) 
                *   - [x] [kubeadm join](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-join/) 
                *   - [x] [kubeadm upgrade](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-upgrade/) 
                *   - [x] [kubeadm upgrade phases](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-upgrade-phase/) 
                *   - [x] [kubeadm config](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-config/) 
                *   - [x] [kubeadm reset](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-reset/) 
                *   - [x] [kubeadm token](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-token/) 
                *   - [x] [kubeadm version](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-version/) 
                *   - [x] [kubeadm alpha](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-alpha/) 
                *   - [x] [kubeadm certs](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-certs/) 
                *   - [x] [kubeadm init phase](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init-phase/) 
                *   - [x] [kubeadm join phase](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-join-phase/) 
                *   - [x] [kubeadm kubeconfig](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-kubeconfig/) 
                *   - [x] [kubeadm reset phase](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-reset-phase/) 
                *   - [x] [Implementation details](https://kubernetes.io/docs/reference/setup-tools/kubeadm/implementation-details/) 

        *   - [x] [Command line tool (kubectl)](https://kubernetes.io/docs/reference/kubectl/) 
            *   - [x] [Introduction to kubectl](https://kubernetes.io/docs/reference/kubectl/introduction/) 
            *   - [x] [kubectl Quick Reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/) 
            *   - [x] [kubectl reference](https://kubernetes.io/docs/reference/kubectl/generated/) 
                *   - [x] [kubectl](https://kubernetes.io/docs/reference/kubectl/generated/kubectl/) 
                *   - [x] [kubectl alpha](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_alpha/) 
                    *   - [x] [kubectl alpha kuberc](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_alpha/kubectl_alpha_kuberc/) 
                    *   - [x] [kubectl alpha kuberc set](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_alpha/kubectl_alpha_kuberc_set/) 
                    *   - [x] [kubectl alpha kuberc view](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_alpha/kubectl_alpha_kuberc_view/) 

                *   - [x] [kubectl annotate](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_annotate/) 
                *   - [x] [kubectl api-resources](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_api-resources/) 
                *   - [x] [kubectl api-versions](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_api-versions/) 
                *   - [x] [kubectl apply](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/) 
                    *   - [x] [kubectl apply edit-last-applied](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/kubectl_apply_edit-last-applied/) 
                    *   - [x] [kubectl apply set-last-applied](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/kubectl_apply_set-last-applied/) 
                    *   - [x] [kubectl apply view-last-applied](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/kubectl_apply_view-last-applied/) 

                *   - [x] [kubectl attach](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_attach/) 
                *   - [x] [kubectl auth](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_auth/) 
                    *   - [x] [kubectl auth can-i](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_can-i/) 
                    *   - [x] [kubectl auth reconcile](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_reconcile/) 
                    *   - [x] [kubectl auth whoami](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_whoami/) 

                *   - [x] [kubectl autoscale](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_autoscale/) 
                *   - [x] [kubectl certificate](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_certificate/) 
                    *   - [x] [kubectl certificate approve](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_certificate/kubectl_certificate_approve/) 
                    *   - [x] [kubectl certificate deny](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_certificate/kubectl_certificate_deny/) 

                *   - [x] [kubectl cluster-info](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cluster-info/) 
                    *   - [x] [kubectl cluster-info dump](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cluster-info/kubectl_cluster-info_dump/) 

                *   - [x] [kubectl completion](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_completion/) 
                *   - [x] [kubectl config](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/) 
                    *   - [x] [kubectl config current-context](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_current-context/) 
                    *   - [x] [kubectl config delete-cluster](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_delete-cluster/) 
                    *   - [x] [kubectl config delete-context](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_delete-context/) 
                    *   - [x] [kubectl config delete-user](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_delete-user/) 
                    *   - [x] [kubectl config get-clusters](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_get-clusters/) 
                    *   - [x] [kubectl config get-contexts](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_get-contexts/) 
                    *   - [x] [kubectl config get-users](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_get-users/) 
                    *   - [x] [kubectl config rename-context](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_rename-context/) 
                    *   - [x] [kubectl config set](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_set/) 
                    *   - [x] [kubectl config set-cluster](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_set-cluster/) 
                    *   - [x] [kubectl config set-context](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_set-context/) 
                    *   - [x] [kubectl config set-credentials](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_set-credentials/) 
                    *   - [x] [kubectl config unset](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_unset/) 
                    *   - [x] [kubectl config use-context](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_use-context/) 
                    *   - [x] [kubectl config view](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_view/) 

                *   - [x] [kubectl cordon](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cordon/) 
                *   - [x] [kubectl cp](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cp/) 
                *   - [x] [kubectl create](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/) 
                    *   - [x] [kubectl create clusterrole](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_clusterrole/) 
                    *   - [x] [kubectl create clusterrolebinding](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_clusterrolebinding/) 
                    *   - [x] [kubectl create configmap](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_configmap/) 
                    *   - [x] [kubectl create cronjob](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_cronjob/) 
                    *   - [x] [kubectl create deployment](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_deployment/) 
                    *   - [x] [kubectl create ingress](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_ingress/) 
                    *   - [x] [kubectl create job](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_job/) 
                    *   - [x] [kubectl create namespace](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_namespace/) 
                    *   - [x] [kubectl create poddisruptionbudget](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_poddisruptionbudget/) 
                    *   - [x] [kubectl create priorityclass](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_priorityclass/) 
                    *   - [x] [kubectl create quota](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_quota/) 
                    *   - [x] [kubectl create role](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_role/) 
                    *   - [x] [kubectl create rolebinding](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_rolebinding/) 
                    *   - [x] [kubectl create secret](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_secret/) 
                    *   - [x] [kubectl create secret docker-registry](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_secret_docker-registry/) 
                    *   - [x] [kubectl create secret generic](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_secret_generic/) 
                    *   - [x] [kubectl create secret tls](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_secret_tls/) 
                    *   - [x] [kubectl create service](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service/) 
                    *   - [x] [kubectl create service clusterip](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service_clusterip/) 
                    *   - [x] [kubectl create service externalname](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service_externalname/) 
                    *   - [x] [kubectl create service loadbalancer](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service_loadbalancer/) 
                    *   - [x] [kubectl create service nodeport](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service_nodeport/) 
                    *   - [x] [kubectl create serviceaccount](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_serviceaccount/) 
                    *   - [x] [kubectl create token](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_token/) 

                *   - [x] [kubectl debug](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_debug/) 
                *   - [x] [kubectl delete](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_delete/) 
                *   - [x] [kubectl describe](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_describe/) 
                *   - [x] [kubectl diff](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_diff/) 
                *   - [x] [kubectl drain](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_drain/) 
                *   - [x] [kubectl edit](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_edit/) 
                *   - [x] [kubectl events](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_events/) 
                *   - [x] [kubectl exec](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_exec/) 
                *   - [x] [kubectl explain](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_explain/) 
                *   - [x] [kubectl expose](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_expose/) 
                *   - [x] [kubectl get](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_get/) 
                *   - [x] [kubectl kustomize](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_kustomize/) 
                *   - [x] [kubectl label](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_label/) 
                *   - [x] [kubectl logs](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_logs/) 
                *   - [x] [kubectl options](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_options/) 
                *   - [x] [kubectl patch](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_patch/) 
                *   - [x] [kubectl plugin](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_plugin/) 
                    *   - [x] [kubectl plugin list](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_plugin/kubectl_plugin_list/) 

                *   - [x] [kubectl port-forward](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_port-forward/) 
                *   - [x] [kubectl proxy](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_proxy/) 
                *   - [x] [kubectl replace](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_replace/) 
                *   - [x] [kubectl rollout](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/) 
                    *   - [x] [kubectl rollout history](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_history/) 
                    *   - [x] [kubectl rollout pause](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_pause/) 
                    *   - [x] [kubectl rollout restart](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_restart/) 
                    *   - [x] [kubectl rollout resume](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_resume/) 
                    *   - [x] [kubectl rollout status](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_status/) 
                    *   - [x] [kubectl rollout undo](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_undo/) 

                *   - [x] [kubectl run](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_run/) 
                *   - [x] [kubectl scale](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_scale/) 
                *   - [x] [kubectl set](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_set/) 
                    *   - [x] [kubectl set env](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_set/kubectl_set_env/) 
                    *   - [x] [kubectl set image](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_set/kubectl_set_image/) 
                    *   - [x] [kubectl set resources](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_set/kubectl_set_resources/) 
                    *   - [x] [kubectl set selector](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_set/kubectl_set_selector/) 
                    *   - [x] [kubectl set serviceaccount](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_set/kubectl_set_serviceaccount/) 
                    *   - [x] [kubectl set subject](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_set/kubectl_set_subject/) 

                *   - [x] [kubectl taint](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_taint/) 
                *   - [x] [kubectl top](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_top/) 
                    *   - [x] [kubectl top node](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_top/kubectl_top_node/) 
                    *   - [x] [kubectl top pod](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_top/kubectl_top_pod/) 

                *   - [x] [kubectl uncordon](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_uncordon/) 
                *   - [x] [kubectl version](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_version/) 
                *   - [x] [kubectl wait](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_wait/) 

            *   - [x] [kubectl Commands](https://kubernetes.io/docs/reference/kubectl/kubectl-cmds/) 
            *   - [x] [kubectl](https://kubernetes.io/docs/reference/kubectl/kubectl/) 
            *   - [x] [JSONPath Support](https://kubernetes.io/docs/reference/kubectl/jsonpath/) 
            *   - [x] [kubectl for Docker Users](https://kubernetes.io/docs/reference/kubectl/docker-cli-to-kubectl/) 
            *   - [x] [kubectl Usage Conventions](https://kubernetes.io/docs/reference/kubectl/conventions/) 
            *   - [x] [Kubectl user preferences (kuberc)](https://kubernetes.io/docs/reference/kubectl/kuberc/) 

        *   - [x] [Encodings](https://kubernetes.io/docs/reference/encodings/) 
            *   - [x] [KYAML Reference](https://kubernetes.io/docs/reference/encodings/kyaml/) 

        *   - [x] [Component tools](https://kubernetes.io/docs/reference/command-line-tools-reference/) 
            *   - [x] [Feature Gates](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) 
            *   - [x] [Feature Gates (removed)](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates-removed/) 
            *   - [x] [kube-apiserver](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/) 
            *   - [x] [kube-controller-manager](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/) 
            *   - [x] [kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/) 
            *   - [x] [kube-scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/) 
            *   - [x] [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/) 

        *   - [x] [Debug cluster](https://kubernetes.io/docs/reference/debug-cluster/) 
            *   - [x] [Flow control](https://kubernetes.io/docs/reference/debug-cluster/flow-control/) 

        *   - [x] [Configuration APIs](https://kubernetes.io/docs/reference/config-api/) 
            *   - [x] [Client Authentication (v1)](https://kubernetes.io/docs/reference/config-api/client-authentication.v1/) 
            *   - [x] [Client Authentication (v1beta1)](https://kubernetes.io/docs/reference/config-api/client-authentication.v1beta1/) 
            *   - [x] [Event Rate Limit Configuration (v1alpha1)](https://kubernetes.io/docs/reference/config-api/apiserver-eventratelimit.v1alpha1/) 
            *   - [x] [Image Policy API (v1alpha1)](https://kubernetes.io/docs/reference/config-api/imagepolicy.v1alpha1/) 
            *   - [x] [kube-apiserver Admission (v1)](https://kubernetes.io/docs/reference/config-api/apiserver-admission.v1/) 
            *   - [x] [kube-apiserver Audit Configuration (v1)](https://kubernetes.io/docs/reference/config-api/apiserver-audit.v1/) 
            *   - [x] [kube-apiserver Configuration (v1)](https://kubernetes.io/docs/reference/config-api/apiserver-config.v1/) 
            *   - [x] [kube-apiserver Configuration (v1alpha1)](https://kubernetes.io/docs/reference/config-api/apiserver-config.v1alpha1/) 
            *   - [x] [kube-apiserver Configuration (v1beta1)](https://kubernetes.io/docs/reference/config-api/apiserver-config.v1beta1/) 
            *   - [x] [kube-controller-manager Configuration (v1alpha1)](https://kubernetes.io/docs/reference/config-api/kube-controller-manager-config.v1alpha1/) 
            *   - [x] [kube-proxy Configuration (v1alpha1)](https://kubernetes.io/docs/reference/config-api/kube-proxy-config.v1alpha1/) 
            *   - [x] [kube-scheduler Configuration (v1)](https://kubernetes.io/docs/reference/config-api/kube-scheduler-config.v1/) 
            *   - [x] [kubeadm Configuration (v1beta3)](https://kubernetes.io/docs/reference/config-api/kubeadm-config.v1beta3/) 
            *   - [x] [kubeadm Configuration (v1beta4)](https://kubernetes.io/docs/reference/config-api/kubeadm-config.v1beta4/) 
            *   - [x] [kubeconfig (v1)](https://kubernetes.io/docs/reference/config-api/kubeconfig.v1/) 
            *   - [x] [Kubelet Configuration (v1)](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1/) 
            *   - [x] [Kubelet Configuration (v1alpha1)](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1alpha1/) 
            *   - [x] [Kubelet Configuration (v1beta1)](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1beta1/) 
            *   - [x] [Kubelet CredentialProvider (v1)](https://kubernetes.io/docs/reference/config-api/kubelet-credentialprovider.v1/) 
            *   - [x] [kuberc (v1alpha1)](https://kubernetes.io/docs/reference/config-api/kuberc.v1alpha1/) 
            *   - [x] [kuberc (v1beta1)](https://kubernetes.io/docs/reference/config-api/kuberc.v1beta1/) 
            *   - [x] [WebhookAdmission Configuration (v1)](https://kubernetes.io/docs/reference/config-api/apiserver-webhookadmission.v1/) 

        *   - [x] [External APIs](https://kubernetes.io/docs/reference/external-api/) 
            *   - [x] [Kubernetes Custom Metrics (v1beta2)](https://kubernetes.io/docs/reference/external-api/custom-metrics.v1beta2/) 
            *   - [x] [Kubernetes External Metrics (v1beta1)](https://kubernetes.io/docs/reference/external-api/external-metrics.v1beta1/) 
            *   - [x] [Kubernetes Metrics (v1beta1)](https://kubernetes.io/docs/reference/external-api/metrics.v1beta1/) 

        *   - [x] [Scheduling](https://kubernetes.io/docs/reference/scheduling/) 
            *   - [x] [Scheduler Configuration](https://kubernetes.io/docs/reference/scheduling/config/) 
            *   - [x] [Scheduling Policies](https://kubernetes.io/docs/reference/scheduling/policies/) 

        *   - [x] [Other Tools](https://kubernetes.io/docs/reference/tools/) 

    *   - [x] [Contribute](https://kubernetes.io/docs/contribute/ "Contribute to Kubernetes") 
        *   - [x] [Contribute to Kubernetes Documentation](https://kubernetes.io/docs/contribute/docs/) 
        *   - [x] [Contributing to Kubernetes blogs](https://kubernetes.io/docs/contribute/blog/) 
            *   - [x] [Submitting articles to Kubernetes blogs](https://kubernetes.io/docs/contribute/blog/article-submission/) 
            *   - [x] [Blog guidelines](https://kubernetes.io/docs/contribute/blog/guidelines/) 
            *   - [x] [Blog article mirroring](https://kubernetes.io/docs/contribute/blog/article-mirroring/) 
            *   - [x] [Post-release communications](https://kubernetes.io/docs/contribute/blog/release-comms/) 
            *   - [x] [Helping as a blog writing buddy](https://kubernetes.io/docs/contribute/blog/writing-buddy/) 

        *   - [x] [Suggesting content improvements](https://kubernetes.io/docs/contribute/suggesting-improvements/) 
        *   - [x] [Contributing new content](https://kubernetes.io/docs/contribute/new-content/) 
            *   - [x] [Opening a pull request](https://kubernetes.io/docs/contribute/new-content/open-a-pr/) 
            *   - [x] [Previewing locally](https://kubernetes.io/docs/contribute/new-content/preview-locally/) 
            *   - [x] [Documenting for a release](https://kubernetes.io/docs/contribute/new-content/new-features/ "Documenting a feature for a release") 
            *   - [x] [Case studies](https://kubernetes.io/docs/contribute/new-content/case-studies/ "Submitting case studies") 

        *   - [x] [Reviewing changes](https://kubernetes.io/docs/contribute/review/) 
            *   - [x] [Reviewing pull requests](https://kubernetes.io/docs/contribute/review/reviewing-prs/) 
            *   - [x] [For approvers and reviewers](https://kubernetes.io/docs/contribute/review/for-approvers/ "Reviewing for approvers and reviewers") 

        *   - [x] [Localizing Kubernetes documentation](https://kubernetes.io/docs/contribute/localization/) 
        *   - [x] [Participating in SIG Docs](https://kubernetes.io/docs/contribute/participate/) 
            *   - [x] [Roles and responsibilities](https://kubernetes.io/docs/contribute/participate/roles-and-responsibilities/) 
            *   - [x] [Issue Wranglers](https://kubernetes.io/docs/contribute/participate/issue-wrangler/) 
            *   - [x] [PR wranglers](https://kubernetes.io/docs/contribute/participate/pr-wranglers/) 

        *   - [x] [Documentation style overview](https://kubernetes.io/docs/contribute/style/) 
            *   - [x] [Content guide](https://kubernetes.io/docs/contribute/style/content-guide/ "Documentation Content Guide") 
            *   - [x] [Style guide](https://kubernetes.io/docs/contribute/style/style-guide/ "Documentation Style Guide") 
            *   - [x] [Diagram guide](https://kubernetes.io/docs/contribute/style/diagram-guide/ "Diagram Guide") 
            *   - [x] [Writing a new topic](https://kubernetes.io/docs/contribute/style/write-new-topic/) 
            *   - [x] [Page content types](https://kubernetes.io/docs/contribute/style/page-content-types/) 
            *   - [x] [Content organization](https://kubernetes.io/docs/contribute/style/content-organization/) 
            *   - [x] [Custom Hugo Shortcodes](https://kubernetes.io/docs/contribute/style/hugo-shortcodes/) 

        *   - [x] [Updating Reference Documentation](https://kubernetes.io/docs/contribute/generate-ref-docs/) 
            *   - [x] [Quickstart](https://kubernetes.io/docs/contribute/generate-ref-docs/quickstart/ "Reference Documentation Quickstart") 
            *   - [x] [Contributing to the Upstream Kubernetes Code](https://kubernetes.io/docs/contribute/generate-ref-docs/contribute-upstream/) 
            *   - [x] [Generating Reference Documentation for the Kubernetes API](https://kubernetes.io/docs/contribute/generate-ref-docs/kubernetes-api/) 
            *   - [x] [Generating Reference Documentation for kubectl Commands](https://kubernetes.io/docs/contribute/generate-ref-docs/kubectl/) 
            *   - [x] [Generating Reference Documentation for Metrics](https://kubernetes.io/docs/contribute/generate-ref-docs/metrics-reference/) 
            *   - [x] [Generating Reference Pages for Kubernetes Components and Tools](https://kubernetes.io/docs/contribute/generate-ref-docs/kubernetes-components/) 
            *   - [x] [](https://kubernetes.io/docs/contribute/generate-ref-docs/prerequisites-ref-docs/) 

        *   - [x] [Advanced contributing](https://kubernetes.io/docs/contribute/advanced/) 
        *   - [x] [Viewing Site Analytics](https://kubernetes.io/docs/contribute/analytics/) 

    *   - [x] [Docs smoke test page](https://kubernetes.io/docs/test/) 

1.   [Kubernetes Documentation](https://kubernetes.io/docs/)
2.   [Concepts](https://kubernetes.io/docs/concepts/)
3.   [Workloads](https://kubernetes.io/docs/concepts/workloads/)
4.   [Pods](https://kubernetes.io/docs/concepts/workloads/pods/)
5.   [Init Containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/)

Init Containers
===============

This page provides an overview of init containers: specialized containers that run before app containers in a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster."). Init containers can contain utilities or setup scripts not present in an app image.

You can specify init containers in the Pod specification alongside the `containers` array (which describes app containers).

In Kubernetes, a [sidecar container](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) is a container that starts before the main application container and _continues to run_. This document is about init containers: containers that run to completion during Pod initialization.

Understanding init containers
-----------------------------

A [Pod](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.") can have multiple containers running apps within it, but it can also have one or more init containers, which are run before the app containers are started.

Init containers are exactly like regular containers, except:

*   Init containers always run to completion.
*   Each init container must complete successfully before the next one starts.

If a Pod's init container fails, the kubelet repeatedly restarts that init container until it succeeds. However, if the Pod has a `restartPolicy` of Never, and an init container fails during startup of that Pod, Kubernetes treats the overall Pod as failed.

To specify an init container for a Pod, add the `initContainers` field into the [Pod specification](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#PodSpec), as an array of `container` items (similar to the app `containers` field and its contents). See [Container](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#Container) in the API reference for more details.

The status of the init containers is returned in `.status.initContainerStatuses` field as an array of the container statuses (similar to the `.status.containerStatuses` field).

### Differences from regular containers

Init containers support all the fields and features of app containers, including resource limits, [volumes](https://kubernetes.io/docs/concepts/storage/volumes/), and security settings. However, the resource requests and limits for an init container are handled differently, as documented in [Resource sharing within containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#resource-sharing-within-containers).

Regular init containers (in other words: excluding sidecar containers) do not support the `lifecycle`, `livenessProbe`, `readinessProbe`, or `startupProbe` fields. Init containers must run to completion before the Pod can be ready; sidecar containers continue running during a Pod's lifetime, and _do_ support some probes. See [sidecar container](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) for further details about sidecar containers.

If you specify multiple init containers for a Pod, kubelet runs each init container sequentially. Each init container must succeed before the next can run. When all of the init containers have run to completion, kubelet initializes the application containers for the Pod and runs them as usual.

### Differences from sidecar containers

Init containers run and complete their tasks before the main application container starts. Unlike [sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/), init containers are not continuously running alongside the main containers.

Init containers run to completion sequentially, and the main container does not start until all the init containers have successfully completed.

init containers do not support `lifecycle`, `livenessProbe`, `readinessProbe`, or `startupProbe` whereas sidecar containers support all these [probes](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#types-of-probe) to control their lifecycle.

Init containers share the same resources (CPU, memory, network) with the main application containers but do not interact directly with them. They can, however, use shared volumes for data exchange.

Using init containers
---------------------

Because init containers have separate images from app containers, they have some advantages for start-up related code:

*   Init containers can contain utilities or custom code for setup that are not present in an app image. For example, there is no need to make an image `FROM` another image just to use a tool like `sed`, `awk`, `python`, or `dig` during setup.
*   The application image builder and deployer roles can work independently without the need to jointly build a single app image.
*   Init containers can run with a different view of the filesystem than app containers in the same Pod. Consequently, they can be given access to [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/ "Stores sensitive information, such as passwords, OAuth tokens, and ssh keys.") that app containers cannot access.
*   Because init containers run to completion before any app containers start, init containers offer a mechanism to block or delay app container startup until a set of preconditions are met. Once preconditions are met, all of the app containers in a Pod can start in parallel.
*   Init containers can securely run utilities or custom code that would otherwise make an app container image less secure. By keeping unnecessary tools separate you can limit the attack surface of your app container image.

### Examples

Here are some ideas for how to use init containers:

*   Wait for a [Service](https://kubernetes.io/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service.") to be created, using a shell one-line command like:

```shell
for i in {1..100}; do sleep 1; if nslookup myservice; then exit 0; fi; done; exit 1
``` 
*   Register this Pod with a remote server from the downward API with a command like:

```shell
curl -X POST http://$MANAGEMENT_SERVICE_HOST:$MANAGEMENT_SERVICE_PORT/register -d 'instance=$(<POD_NAME>)&ip=$(<POD_IP>)'
``` 
*   Wait for some time before starting the app container with a command like

```shell
sleep 60
``` 
*   Clone a Git repository into a [Volume](https://kubernetes.io/docs/concepts/storage/volumes/ "A directory containing data, accessible to the containers in a pod.")

*   Place values into a configuration file and run a template tool to dynamically generate a configuration file for the main app container. For example, place the `POD_IP` value in a configuration and generate the main app configuration file using Jinja.

#### Init containers in use

This example defines a simple Pod that has two init containers. The first waits for `myservice`, and the second waits for `mydb`. Once both init containers complete, the Pod runs the app container from its `spec` section.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  labels:
    app.kubernetes.io/name: MyApp
spec:
  containers:
  - name: myapp-container
    image: busybox:1.28
    command: ['sh', '-c', 'echo The app is running! && sleep 3600']
  initContainers:
  - name: init-myservice
    image: busybox:1.28
    command: ['sh', '-c', "until nslookup myservice.$(cat /var/run/secrets/kubernetes.io/serviceaccount/namespace).svc.cluster.local; do echo waiting for myservice; sleep 2; done"]
  - name: init-mydb
    image: busybox:1.28
    command: ['sh', '-c', "until nslookup mydb.$(cat /var/run/secrets/kubernetes.io/serviceaccount/namespace).svc.cluster.local; do echo waiting for mydb; sleep 2; done"]
```

You can start this Pod by running:

```shell
kubectl apply -f myapp.yaml
```

The output is similar to this:

```
pod/myapp-pod created
```

And check on its status with:

```shell
kubectl get -f myapp.yaml
```

The output is similar to this:

```
NAME        READY     STATUS     RESTARTS   AGE
myapp-pod   0/1       Init:0/2   0          6m
```

or for more details:

```shell
kubectl describe -f myapp.yaml
```

The output is similar to this:

```
Name:          myapp-pod
Namespace:     default
[...]
Labels:        app.kubernetes.io/name=MyApp
Status:        Pending
[...]
Init Containers:
  init-myservice:
[...]
    State:         Running
[...]
  init-mydb:
[...]
    State:         Waiting
      Reason:      PodInitializing
    Ready:         False
[...]
Containers:
  myapp-container:
[...]
    State:         Waiting
      Reason:      PodInitializing
    Ready:         False
[...]
Events:
  FirstSeen    LastSeen    Count    From                      SubObjectPath                           Type          Reason        Message
  ---------    --------    -----    ----                      -------------                           --------      ------        -------
  16s          16s         1        {default-scheduler }                                              Normal        Scheduled     Successfully assigned myapp-pod to 172.17.4.201
  16s          16s         1        {kubelet 172.17.4.201}    spec.initContainers{init-myservice}     Normal        Pulling       pulling image "busybox"
  13s          13s         1        {kubelet 172.17.4.201}    spec.initContainers{init-myservice}     Normal        Pulled        Successfully pulled image "busybox"
  13s          13s         1        {kubelet 172.17.4.201}    spec.initContainers{init-myservice}     Normal        Created       Created container init-myservice
  13s          13s         1        {kubelet 172.17.4.201}    spec.initContainers{init-myservice}     Normal        Started       Started container init-myservice
```

To see logs for the init containers in this Pod, run:

```shell
kubectl logs myapp-pod -c init-myservice # Inspect the first init container
kubectl logs myapp-pod -c init-mydb      # Inspect the second init container
```

At this point, those init containers will be waiting to discover [Services](https://kubernetes.io/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service.") named `mydb` and `myservice`.

Here's a configuration you can use to make those Services appear:

```yaml
---
apiVersion: v1
kind: Service
metadata:
  name: myservice
spec:
  ports:
  - protocol: TCP
    port: 80
    targetPort: 9376
---
apiVersion: v1
kind: Service
metadata:
  name: mydb
spec:
  ports:
  - protocol: TCP
    port: 80
    targetPort: 9377
```

To create the `mydb` and `myservice` services:

```shell
kubectl apply -f services.yaml
```

The output is similar to this:

```
service/myservice created
service/mydb created
```

You'll then see that those init containers complete, and that the `myapp-pod` Pod moves into the Running state:

```shell
kubectl get -f myapp.yaml
```

The output is similar to this:

```
NAME        READY     STATUS    RESTARTS   AGE
myapp-pod   1/1       Running   0          9m
```

This simple example should provide some inspiration for you to create your own init containers. [What's next](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#what-s-next) contains a link to a more detailed example.

Detailed behavior
-----------------

During Pod startup, the kubelet delays running init containers until the networking and storage are ready. Then the kubelet runs the Pod's init containers in the order they appear in the Pod's spec.

Each init container must exit successfully before the next container starts. If a container fails to start due to the runtime or exits with failure, it is retried according to the Pod `restartPolicy`. However, if the Pod `restartPolicy` is set to Always, the init containers use `restartPolicy` OnFailure.

A Pod cannot be `Ready` until all init containers have succeeded. The ports on an init container are not aggregated under a Service. A Pod that is initializing is in the `Pending` state but should have a condition `Initialized` set to false.

If the Pod [restarts](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#pod-restart-reasons), or is restarted, all init containers must execute again.

Changes to the init container spec are limited to the container image field. Directly altering the `image` field of an init container does _not_ restart the Pod or trigger its recreation. If the Pod has yet to start, that change may have an effect on how the Pod boots up.

For a [pod template](https://kubernetes.io/docs/concepts/workloads/pods/#pod-templates) you can typically change any field for an init container; the impact of making that change depends on where the pod template is used.

Because init containers can be restarted, retried, or re-executed, init container code should be idempotent. In particular, code that writes into any `emptyDir` volume should be prepared for the possibility that an output file already exists.

Init containers have all of the fields of an app container. However, Kubernetes prohibits `readinessProbe` from being used because init containers cannot define readiness distinct from completion. This is enforced during validation.

Use `activeDeadlineSeconds` on the Pod to prevent init containers from failing forever. The active deadline includes init containers. However it is recommended to use `activeDeadlineSeconds` only if teams deploy their application as a Job, because `activeDeadlineSeconds` has an effect even after initContainer finished. The Pod which is already running correctly would be killed by `activeDeadlineSeconds` if you set.

The name of each app and init container in a Pod must be unique; a validation error is thrown for any container sharing a name with another.

### Resource sharing within containers

Given the order of execution for init, sidecar and app containers, the following rules for resource usage apply:

*   The highest of any particular resource request or limit defined on all init containers is the _effective init request/limit_. If any resource has no resource limit specified this is considered as the highest limit.
*   The Pod's _effective request/limit_ for a resource is the higher of:
    *   the sum of all app containers request/limit for a resource
    *   the effective init request/limit for a resource

*   Scheduling is done based on effective requests/limits, which means init containers can reserve resources for initialization that are not used during the life of the Pod.
*   The QoS (quality of service) tier of the Pod's _effective QoS tier_ is the QoS tier for init containers and app containers alike.

Quota and limits are applied based on the effective Pod request and limit.

### Init containers and Linux cgroups

On Linux, resource allocations for Pod level control groups (cgroups) are based on the effective Pod request and limit, the same as the scheduler.

### Pod restart reasons

A Pod can restart, causing re-execution of init containers, for the following reasons:

*   The Pod infrastructure container is restarted. This is uncommon and would have to be done by someone with root access to nodes.
*   All containers in a Pod are terminated while `restartPolicy` is set to Always, forcing a restart, and the init container completion record has been lost due to [garbage collection](https://kubernetes.io/docs/concepts/architecture/garbage-collection/ "A collective term for the various mechanisms Kubernetes uses to clean up cluster resources.").

The Pod will not be restarted when the init container image is changed, or the init container completion record has been lost due to garbage collection. This applies for Kubernetes v1.20 and later. If you are using an earlier version of Kubernetes, consult the documentation for the version you are using.

What's next
-----------

Learn more about the following:

*   [Creating a Pod that has an init container](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-initialization/#create-a-pod-that-has-an-init-container).
*   [Debug init containers](https://kubernetes.io/docs/tasks/debug/debug-application/debug-init-containers/).
*   Overview of [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/) and [kubectl](https://kubernetes.io/docs/reference/kubectl/).
*   [Types of probes](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#types-of-probe): liveness, readiness, startup probe.
*   [Sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/).

Feedback
--------

Was this page helpful?

Yes No
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io/docs/concepts/workloads/pods/init-containers/) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io/docs/concepts/workloads/pods/init-containers/).

Last modified September 18, 2024 at 8:41 AM PST: [38271 - Init Container concept clarity (27779ce888)](https://github.com/kubernetes/website/commit/27779ce8885bdb6cc7ceda6c24740a2fab7bb5ef)

[Edit this page](https://github.com/kubernetes/website/edit/main/content/en/docs/concepts/workloads/pods/init-containers.md)[Create child page](https://github.com/kubernetes/website/new/main/content/en/docs/concepts/workloads/pods/init-containers.md?filename=change-me.md&value=---%0Atitle%3A+%22Long+Page+Title%22%0AlinkTitle%3A+%22Short+Nav+Title%22%0Aweight%3A+100%0Adescription%3A+%3E-%0A+++++Page+description+for+heading+and+indexes.%0A---%0A%0A%23%23+Heading%0A%0AEdit+this+template+to+create+your+new+page.%0A%0A%2A+Give+it+a+good+name%2C+ending+in+%60.md%60+-+e.g.+%60getting-started.md%60%0A%2A+Edit+the+%22front+matter%22+section+at+the+top+of+the+page+%28weight+controls+how+its+ordered+amongst+other+pages+in+the+same+directory%3B+lowest+number+first%29.%0A%2A+Add+a+good+commit+message+at+the+bottom+of+the+page+%28%3C80+characters%3B+use+the+extended+description+field+for+more+detail%29.%0A%2A+Create+a+new+branch+so+you+can+preview+your+new+file+and+request+a+review+via+Pull+Request.%0A)[Create an issue](https://github.com/kubernetes/website/issues/new?title=Init%20Containers)[Print entire section](https://kubernetes.io/docs/concepts/workloads/pods/_print/)

*   [Understanding init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#understanding-init-containers)
    *   [Differences from regular containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#differences-from-regular-containers)
    *   [Differences from sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#differences-from-sidecar-containers)

*   [Using init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#using-init-containers)
    *   [Examples](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#examples)

*   [Detailed behavior](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#detailed-behavior)
    *   [Resource sharing within containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#resource-sharing-within-containers)
    *   [Init containers and Linux cgroups](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#cgroups)
    *   [Pod restart reasons](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#pod-restart-reasons)

*   [What's next](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#what-s-next)

© 2026 The Kubernetes Authors | Documentation Distributed under [CC BY 4.0](https://git.k8s.io/website/LICENSE)

© 2026 The Linux Foundation ®. All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage page](https://www.linuxfoundation.org/trademark-usage)

ICP license: 京ICP备17074266号-3

*   [](https://youtube.com/kubernetescommunity)
*   [](https://discuss.kubernetes.io/)
*   [](https://serverfault.com/questions/tagged/kubernetes)
*   [](https://www.linkedin.com/company/kubernetes/)
*   [](https://bsky.app/profile/kubernetes.io)
*   [](https://x.com/kubernetesio)

*   [](https://k8s.dev/)
*   [](https://github.com/kubernetes/kubernetes)
*   [](https://slack.k8s.io/)
*   [](https://calendar.google.com/calendar/embed?src=calendar%40kubernetes.io)
