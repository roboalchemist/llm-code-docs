# Source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/

Title: Pod Lifecycle

URL Source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/

Markdown Content:
Pod Lifecycle | Kubernetes
===============
[Kubernetes](https://kubernetes.io/)

*   [Documentation](https://kubernetes.io/docs/)
*   [Kubernetes Blog](https://kubernetes.io/blog/)
*   [Training](https://kubernetes.io/training/)
*   [Careers](https://kubernetes.io/careers/)
*   [Partners](https://kubernetes.io/partners/)
*   [Community](https://kubernetes.io/community/)
*   [Versions](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#)[Release Information](https://kubernetes.io/releases)[v1.35](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)[v1.34](https://v1-34.docs.kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)[v1.33](https://v1-33.docs.kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)[v1.32](https://v1-32.docs.kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)[v1.31](https://v1-31.docs.kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/) 
*   [English](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#)[中文 (Chinese)](https://kubernetes.io/zh-cn/docs/concepts/workloads/pods/pod-lifecycle/)[Français (French)](https://kubernetes.io/fr/docs/concepts/workloads/pods/pod-lifecycle/)[Deutsch (German)](https://kubernetes.io/de/docs/concepts/workloads/pods/pod-lifecycle/)[Bahasa Indonesia (Indonesian)](https://kubernetes.io/id/docs/concepts/workloads/pods/pod-lifecycle/)[日本語 (Japanese)](https://kubernetes.io/ja/docs/concepts/workloads/pods/pod-lifecycle/)[한국어 (Korean)](https://kubernetes.io/ko/docs/concepts/workloads/pods/pod-lifecycle/)[Español (Spanish)](https://kubernetes.io/es/docs/concepts/workloads/pods/pod-lifecycle/) 

#### ![Image 1](https://kubernetes.io/images/announcements/kccnc-eu-2026-black.svg)[KubeCon + CloudNativeCon Europe 2026](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/?utm_source=kubernetes&utm_medium=homepage&utm_campaign=18269725-KubeCon-EU-2026&utm_content=slim-banner)

Join us for four days of incredible opportunities to collaborate, learn and share with the cloud native community.

[Buy your ticket now! 23 - 26 March | Amsterdam, The Netherlands](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/register/?utm_source=kubernetes&utm_medium=homepage&utm_campaign=18269725-KubeCon-EU-2026&utm_content=slim-banner)

[English](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#)

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
5.   [Pod Lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)

Pod Lifecycle
=============

This page describes the lifecycle of a Pod. Pods follow a defined lifecycle, starting in the `Pending`[phase](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase), moving through `Running` if at least one of its primary containers starts OK, and then through either the `Succeeded` or `Failed` phases depending on whether any container in the Pod terminated in failure.

Like individual application containers, Pods are considered to be relatively ephemeral (rather than durable) entities. Pods are created, assigned a unique ID ([UID](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids)), and scheduled to run on nodes where they remain until termination (according to restart policy) or deletion. If a [Node](https://kubernetes.io/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") dies, the Pods running on (or scheduled to run on) that node are [marked for deletion](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-garbage-collection). The control plane marks the Pods for removal after a timeout period.

Pod lifetime
------------

Whilst a Pod is running, the kubelet is able to restart containers to handle some kind of faults. Within a Pod, Kubernetes tracks different container [states](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#container-states) and determines what action to take to make the Pod healthy again.

In the Kubernetes API, Pods have both a specification and an actual status. The status for a Pod object consists of a set of [Pod conditions](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions). You can also inject [custom readiness information](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-readiness-gate) into the condition data for a Pod, if that is useful to your application.

Pods are only [scheduled](https://kubernetes.io/docs/concepts/scheduling-eviction/) once in their lifetime; assigning a Pod to a specific node is called _binding_, and the process of selecting which node to use is called _scheduling_. Once a Pod has been scheduled and is bound to a node, Kubernetes tries to run that Pod on the node. The Pod runs on that node until it stops, or until the Pod is [terminated](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination); if Kubernetes isn't able to start the Pod on the selected node (for example, if the node crashes before the Pod starts), then that particular Pod never starts.

You can use [Pod Scheduling Readiness](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-scheduling-readiness/) to delay scheduling for a Pod until all its _scheduling gates_ are removed. For example, you might want to define a set of Pods but only trigger scheduling once all the Pods have been created.

### Pods and fault recovery

If one of the containers in the Pod fails, then Kubernetes may try to restart that specific container. Read [How Pods handle problems with containers](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#container-restarts) to learn more.

Pods can however fail in a way that the cluster cannot recover from, and in that case Kubernetes does not attempt to heal the Pod further; instead, Kubernetes deletes the Pod and relies on other components to provide automatic healing.

If a Pod is scheduled to a [node](https://kubernetes.io/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") and that node then fails, the Pod is treated as unhealthy and Kubernetes eventually deletes the Pod. A Pod won't survive an [eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/ "Process of terminating one or more Pods on Nodes") due to a lack of resources or Node maintenance.

Kubernetes uses a higher-level abstraction, called a [controller](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state."), that handles the work of managing the relatively disposable Pod instances.

A given Pod (as defined by a UID) is never "rescheduled" to a different node; instead, that Pod can be replaced by a new, near-identical Pod. If you make a replacement Pod, it can even have same name (as in `.metadata.name`) that the old Pod had, but the replacement would have a different `.metadata.uid` from the old Pod.

Kubernetes does not guarantee that a replacement for an existing Pod would be scheduled to the same node as the old Pod that was being replaced.

### Associated lifetimes

When something is said to have the same lifetime as a Pod, such as a [volume](https://kubernetes.io/docs/concepts/storage/volumes/ "A directory containing data, accessible to the containers in a pod."), that means that the thing exists as long as that specific Pod (with that exact UID) exists. If that Pod is deleted for any reason, and even if an identical replacement is created, the related thing (a volume, in this example) is also destroyed and created anew.

![Image 2: A multi-container Pod that contains a file puller sidecar and a web server. The Pod uses an ephemeral emptyDir volume for shared storage between the containers.](https://kubernetes.io/images/docs/pod.svg)

#### Figure 1.

A multi-container Pod that contains a file puller [sidecar](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) and a web server. The Pod uses an [ephemeral `emptyDir` volume](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) for shared storage between the containers.

Pod phase
---------

A Pod's `status` field is a [PodStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#podstatus-v1-core) object, which has a `phase` field.

The phase of a Pod is a simple, high-level summary of where the Pod is in its lifecycle. The phase is not intended to be a comprehensive rollup of observations of container or Pod state, nor is it intended to be a comprehensive state machine.

The number and meanings of Pod phase values are tightly guarded. Other than what is documented here, nothing should be assumed about Pods that have a given `phase` value.

Here are the possible values for `phase`:

| Value | Description |
| --- | --- |
| `Pending` | The Pod has been accepted by the Kubernetes cluster, but one or more of the containers has not been set up and made ready to run. This includes time a Pod spends waiting to be scheduled as well as the time spent downloading container images over the network. |
| `Running` | The Pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting. |
| `Succeeded` | All containers in the Pod have terminated in success, and will not be restarted. |
| `Failed` | All containers in the Pod have terminated, and at least one container has terminated in failure. That is, the container either exited with non-zero status or was terminated by the system, and is not set for automatic restarting. |
| `Unknown` | For some reason the state of the Pod could not be obtained. This phase typically occurs due to an error in communicating with the node where the Pod should be running. |

#### Note:

When a pod is failing to start repeatedly, `CrashLoopBackOff` may appear in the `Status` field of some kubectl commands. Similarly, when a pod is being deleted, `Terminating` may appear in the `Status` field of some kubectl commands.

Make sure not to confuse _Status_, a kubectl display field for user intuition, with the pod's `phase`. Pod phase is an explicit part of the Kubernetes data model and of the [Pod API](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/).

```
NAMESPACE               NAME               READY   STATUS             RESTARTS   AGE
  alessandras-namespace   alessandras-pod    0/1     CrashLoopBackOff   200        2d9h
```

A Pod is granted a term to terminate gracefully, which defaults to 30 seconds. You can use the flag `--force` to [terminate a Pod by force](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination-forced).

Since Kubernetes 1.27, the kubelet transitions deleted Pods, except for [static Pods](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/) and [force-deleted Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination-forced) without a finalizer, to a terminal phase (`Failed` or `Succeeded` depending on the exit statuses of the pod containers) before their deletion from the API server.

If a node dies or is disconnected from the rest of the cluster, Kubernetes applies a policy for setting the `phase` of all Pods on the lost node to Failed.

Container states
----------------

As well as the [phase](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase) of the Pod overall, Kubernetes tracks the state of each container inside a Pod. You can use [container lifecycle hooks](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/) to trigger events to run at certain points in a container's lifecycle.

Once the [scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/ "Control plane component that watches for newly created pods with no assigned node, and selects a node for them to run on.") assigns a Pod to a Node, the kubelet starts creating containers for that Pod using a [container runtime](https://kubernetes.io/docs/setup/production-environment/container-runtimes "The container runtime is the software that is responsible for running containers."). There are three possible container states: `Waiting`, `Running`, and `Terminated`.

To check the state of a Pod's containers, you can use `kubectl describe pod <name-of-pod>`. The output shows the state for each container within that Pod.

Each state has a specific meaning:

### `Waiting`

If a container is not in either the `Running` or `Terminated` state, it is `Waiting`. A container in the `Waiting` state is still running the operations it requires in order to complete start up: for example, pulling the container image from a container image registry, or applying [Secret](https://kubernetes.io/docs/concepts/configuration/secret/ "Stores sensitive information, such as passwords, OAuth tokens, and ssh keys.") data. When you use `kubectl` to query a Pod with a container that is `Waiting`, you also see a Reason field to summarize why the container is in that state.

### `Running`

The `Running` status indicates that a container is executing without issues. If there was a `postStart` hook configured, it has already executed and finished. When you use `kubectl` to query a Pod with a container that is `Running`, you also see information about when the container entered the `Running` state.

### `Terminated`

A container in the `Terminated` state began execution and then either ran to completion or failed for some reason. When you use `kubectl` to query a Pod with a container that is `Terminated`, you see a reason, an exit code, and the start and finish time for that container's period of execution.

If a container has a `preStop` hook configured, this hook runs before the container enters the `Terminated` state.

How Pods handle problems with containers
----------------------------------------

Kubernetes manages container failures within Pods using a [`restartPolicy`](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy) defined in the Pod `spec`. This policy determines how Kubernetes reacts to containers exiting due to errors or other reasons, which falls in the following sequence:

1.   **Initial crash**: Kubernetes attempts an immediate restart based on the Pod `restartPolicy`.
2.   **Repeated crashes**: After the initial crash Kubernetes applies an exponential backoff delay for subsequent restarts, described in [`restartPolicy`](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy). This prevents rapid, repeated restart attempts from overloading the system.
3.   **CrashLoopBackOff state**: This indicates that the backoff delay mechanism is currently in effect for a given container that is in a crash loop, failing and restarting repeatedly.
4.   **Backoff reset**: If a container runs successfully for a certain duration (e.g., 10 minutes), Kubernetes resets the backoff delay, treating any new crash as the first one.

In practice, a `CrashLoopBackOff` is a condition or event that might be seen as output from the `kubectl` command, while describing or listing Pods, when a container in the Pod fails to start properly and then continually tries and fails in a loop.

In other words, when a container enters the crash loop, Kubernetes applies the exponential backoff delay mentioned in the [Container restart policy](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy). This mechanism prevents a faulty container from overwhelming the system with continuous failed start attempts.

The `CrashLoopBackOff` can be caused by issues like the following:

*   Application errors that cause the container to exit.
*   Configuration errors, such as incorrect environment variables or missing configuration files.
*   Resource constraints, where the container might not have enough memory or CPU to start properly.
*   Health checks failing if the application doesn't start serving within the expected time.
*   Container liveness probes or startup probes returning a `Failure` result as mentioned in the [probes section](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#container-probes).

To investigate the root cause of a `CrashLoopBackOff` issue, a user can:

1.   **Check logs**: Use `kubectl logs <name-of-pod>` to check the logs of the container. This is often the most direct way to diagnose the issue causing the crashes.
2.   **Inspect events**: Use `kubectl describe pod <name-of-pod>` to see events for the Pod, which can provide hints about configuration or resource issues.
3.   **Review configuration**: Ensure that the Pod configuration, including environment variables and mounted volumes, is correct and that all required external resources are available.
4.   **Check resource limits**: Make sure that the container has enough CPU and memory allocated. Sometimes, increasing the resources in the Pod definition can resolve the issue.
5.   **Debug application**: There might exist bugs or misconfigurations in the application code. Running this container image locally or in a development environment can help diagnose application specific issues.

### Container restarts

When a container in your Pod stops, or experiences failure, Kubernetes can restart it. A restart isn't always appropriate; for example, [init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/ "One or more initialization containers that must run to completion before any app containers run.") run only once (if successful), during Pod startup. You can configure restarts as a policy that applies to all Pods, or using container-level configuration (for example: when you define a [sidecar container](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/ "An auxilliary container that stays running throughout the lifecycle of a Pod.")) or define container-level override.

#### Container restarts and resilience

The Kubernetes project recommends following cloud-native principles, including resilient design that accounts for unannounced or arbitrary restarts. You can achieve this either by failing the Pod and relying on automatic [replacement](https://kubernetes.io/docs/concepts/workloads/controllers/), or you can design for container-level resilience. Either approach helps to ensure that your overall workload remains available despite partial failure.

#### Pod-level container restart policy

The `spec` of a Pod has a `restartPolicy` field with possible values Always, OnFailure, and Never. The default value is Always.

The `restartPolicy` for a Pod applies to [app containers](https://kubernetes.io/docs/reference/glossary/?all=true#term-app-container "A container used to run part of a workload. Compare with init container.") in the Pod and to regular [init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/). [Sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) ignore the Pod-level `restartPolicy` field: in Kubernetes, a sidecar is defined as an entry inside `initContainers` that has its container-level `restartPolicy` set to `Always`. For init containers that exit with an error, the kubelet restarts the init container if the Pod level `restartPolicy` is either `OnFailure` or `Always`:

*   `Always`: Automatically restarts the container after any termination.
*   `OnFailure`: Only restarts the container if it exits with an error (non-zero exit status).
*   `Never`: Does not automatically restart the terminated container.

When the kubelet is handling container restarts according to the configured restart policy, that only applies to restarts that make replacement containers inside the same Pod and running on the same node. After containers in a Pod exit, the kubelet restarts them with an exponential backoff delay (10s, 20s, 40s, …), that is capped at 300 seconds (5 minutes). Once a container has executed for 10 minutes without any problems, the kubelet resets the restart backoff timer for that container. [Sidecar containers and Pod lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/#sidecar-containers-and-pod-lifecycle) explains the behaviour of `init containers` when specify `restartPolicy` field on it.

#### Individual container restart policy and rules

FEATURE STATE:`Kubernetes v1.35 [beta]`(enabled by default)

If your cluster has the feature gate `ContainerRestartRules` enabled, you can specify `restartPolicy` and `restartPolicyRules` on _individual containers_ to override the Pod restart policy. Container restart policy and rules applies to [app containers](https://kubernetes.io/docs/reference/glossary/?all=true#term-app-container "A container used to run part of a workload. Compare with init container.") in the Pod and to regular [init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/).

A Kubernetes-native [sidecar container](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) has its container-level `restartPolicy` set to `Always`.

The container restarts will follow the same exponential backoff as pod restart policy described above. Supported container restart policies:

*   `Always`: Automatically restarts the container after any termination.
*   `OnFailure`: Only restarts the container if it exits with an error (non-zero exit status).
*   `Never`: Does not automatically restart the terminated container.

Additionally, _individual containers_ can specify `restartPolicyRules`. If the `restartPolicyRules` field is specified, then container `restartPolicy`**must** also be specified. The `restartPolicyRules` define a list of rules to apply on container exit. Each rule will consist of a condition and an action. The supported condition is `exitCodes`, which compares the exit code of the container with a list of given values. The supported action is `Restart`, which means the container will be restarted. The rules will be evaluated in order. On the first match, the action will be applied. If none of the rules’ conditions matched, Kubernetes fallback to container’s configured `restartPolicy`.

For example, a Pod with OnFailure restart policy that have a `try-once` container. This allows Pod to only restart certain containers:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: on-failure-pod
spec:
  restartPolicy: OnFailure
  containers:
  - name: try-once-container    # This container will run only once because the restartPolicy is Never.
    image: registry.k8s.io/busybox:1.27.2
    command: ['sh', '-c', 'echo "Only running once" && sleep 10 && exit 1']
    restartPolicy: Never     
  - name: on-failure-container  # This container will be restarted on failure.
    image: registry.k8s.io/busybox:1.27.2
    command: ['sh', '-c', 'echo "Keep restarting" && sleep 1800 && exit 1']
```

A Pod with `Always` restart policy with an init container that only execute once. If the init container fails, the Pod fails. This allows the Pod to fail if the initialization failed, but also keep running once the initialization succeeds:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: fail-pod-if-init-fails
spec:
  restartPolicy: Always
  initContainers:
  - name: init-once      # This init container will only try once. If it fails, the pod will fail.
    image: registry.k8s.io/busybox:1.27.2
    command: ['sh', '-c', 'echo "Failing initialization" && sleep 10 && exit 1']
    restartPolicy: Never
  containers:
  - name: main-container # This container will always be restarted once initialization succeeds.
    image: registry.k8s.io/busybox:1.27.2
    command: ['sh', '-c', 'sleep 1800 && exit 0']
```

A Pod with Never restart policy with a container that ignores and restarts on specific exit codes. This is useful to differentiate between restartable errors and non-restartable errors:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: restart-on-exit-codes
spec:
  restartPolicy: Never
  containers:
  - name: restart-on-exit-codes
    image: registry.k8s.io/busybox:1.27.2
    command: ['sh', '-c', 'sleep 60 && exit 0']
    restartPolicy: Never     # Container restart policy must be specified if rules are specified
    restartPolicyRules:      # Only restart the container if it exits with code 42
    - action: Restart
      exitCodes:
        operator: In
        values: [42]
```

Restart rules can be used for many more advanced lifecycle management scenarios. Note, restart rules are affected by the same inconsistencies as the regular restart policy. The kubelet restarts, container runtime garbage collection, intermitted connectivity issues with the control plane may cause the state loss and containers may be re-run even when you expect a container not to be restarted.

#### Restart All Containers

FEATURE STATE:`Kubernetes v1.35 [alpha]`(disabled by default)

If your cluster has the feature gate `RestartAllContainersOnContainerExits` enabled, you can specify `RestartAllContainers` as an action in `restartPolicyRules` at container level. When a container's exit matches a rule with this action, the entire Pod is terminated and restarted in-place.

This "in-place" restart offers a more efficient way to reset a Pod's state compared to full deletion and recreation. This is especially valuable for workloads where rescheduling is costly, such as batch jobs or AI/ML training tasks.

##### How in-place Pod restarts work

When a `RestartAllContainers` action is triggered, the kubelet performs the following steps:

1.   **Fast Termination**: All running containers in the Pod are terminated. The configured `terminationGracePeriodSeconds` is not respected, and any configured `preStop` hooks are not executed. This ensures a swift shutdown.

2.   **Preservation of Pod Resources**: The Pod's essential resources are preserved:

    *   Pod UID, IP address, and network namespace
    *   Pod sandbox and any attached devices
    *   All volumes, including `emptyDir` and mounted volumes

3.   **Pod Status Update**: The Pod's status is updated with a `PodRestartInPlace` condition set to `True`. This makes the restart process observable.

4.   **Full Restart Sequence**: Once all containers are terminated, the `PodRestartInPlace` condition is set to `False`, and the Pod begins the standard startup process:

    *   **Init containers are re-run** in order.
    *   Sidecar and regular containers are started.

A key aspect of this feature is that **all** containers are restarted, including those that previously completed successfully or failed. The `RestartAllContainers` action overrides any configured container-level or Pod-level `restartPolicy`.

This mechanism is useful in scenarios where a clean slate for all containers is necessary, such as:

*   When an `init` container sets up an environment that can become corrupted, this feature ensures the setup process is re-executed.
*   A sidecar container can monitor the health of a main application and trigger a full Pod restart if the application enters an unrecoverable state.

Consider a workload where a watcher sidecar is responsible for restarting the main application from a known-good state if it encounters an error. The watcher can exit with a specific code to trigger a full, in-place restart of the worker Pod.

[`pods/restart-policy/restart-all-containers.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/restart-policy/restart-all-containers.yaml)![Image 3](https://kubernetes.io/images/copycode.svg)

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: ml-worker
spec:
  restartPolicy: Never # The pod itself should not restart unless explicitly told to.
  initContainers:
  - name: setup-environment
    image: registry.k8s.io/busybox:1.27.2
    command: ['sh', '-c', 'echo "Setting up environment"']
    # This init container runs once to prepare the environment.
    # It will run again after a RestartAllContainers action.
  - name: watcher-sidecar
    image: registry.k8s.io/busybox:1.27.2
    # In a real-world scenario, this would be a dedicated watcher image.
    # This command simulates the watcher exiting with a special code.
    command: ['sh', '-c', 'sleep 60; exit 88']
    restartPolicy: Always
    restartPolicyRules:
    - action: RestartAllContainers
      exitCodes:
        # Exit code 88 triggers a full pod restart.
        operator: In
        values: [88]
  containers:
  - name: main-application
    image: registry.k8s.io/busybox:1.27.2
    command: ['sh', '-c', 'echo "Application is running"; sleep 3600']
```

In this example:

*   The Pod's overall `restartPolicy` is `Never`.
*   The `watcher-sidecar` runs a command and then exits with code `88`.
*   The exit code matches the rule, triggering the `RestartAllContainers` action.
*   The entire Pod, including the `setup-environment` init container and the `main-application` container, is then restarted in-place. The pod keeps its UID, sandbox, IP, and volumes.

### Reduced container restart delay

FEATURE STATE:`Kubernetes v1.33 [alpha]`(disabled by default)

With the alpha feature gate `ReduceDefaultCrashLoopBackOffDecay` enabled, container start retries across your cluster will be reduced to begin at 1s (instead of 10s) and increase exponentially by 2x each restart until a maximum delay of 60s (instead of 300s which is 5 minutes).

If you use this feature along with the alpha feature `KubeletCrashLoopBackOffMax` (described below), individual nodes may have different maximum delays.

### Configurable container restart delay

FEATURE STATE:`Kubernetes v1.35 [beta]`(enabled by default)

With the feature gate `KubeletCrashLoopBackOffMax` enabled, you can reconfigure the maximum delay between container start retries from the default of 300s (5 minutes). This configuration is set per node using kubelet configuration. In your [kubelet configuration](https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/), under `crashLoopBackOff` set the `maxContainerRestartPeriod` field between `"1s"` and `"300s"`. As described above in [Container restart policy](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy), delays on that node will still start at 10s and increase exponentially by 2x each restart, but will now be capped at your configured maximum. If the `maxContainerRestartPeriod` you configure is less than the default initial value of 10s, the initial delay will instead be set to the configured maximum.

See the following kubelet configuration examples:

```yaml
# container restart delays will start at 10s, increasing
# 2x each time they are restarted, to a maximum of 100s
kind: KubeletConfiguration
crashLoopBackOff:
    maxContainerRestartPeriod: "100s"
```

```yaml
# delays between container restarts will always be 2s
kind: KubeletConfiguration
crashLoopBackOff:
    maxContainerRestartPeriod: "2s"
```

If you use this feature along with the alpha feature `ReduceDefaultCrashLoopBackOffDecay` (described above), your cluster defaults for initial backoff and maximum backoff will no longer be 10s and 300s, but 1s and 60s. Per node configuration takes precedence over the defaults set by `ReduceDefaultCrashLoopBackOffDecay`, even if this would result in a node having a longer maximum backoff than other nodes in the cluster.

Pod conditions
--------------

A Pod has a PodStatus, which has an array of [PodConditions](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#podcondition-v1-core) through which the Pod has or has not passed. The kubelet manages the following PodConditions:

*   `PodScheduled`: the Pod has been scheduled to a node.
*   `PodReadyToStartContainers`: (beta feature; enabled by [default](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-has-network)) the Pod sandbox has been successfully created and networking configured.
*   `ContainersReady`: all containers in the Pod are ready.
*   `Initialized`: all [init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) have completed successfully.
*   `Ready`: the Pod is able to serve requests and should be added to the load balancing pools of all matching Services.
*   `DisruptionTarget`: the pod is about to be terminated due to a disruption (such as preemption, eviction or garbage-collection).
*   `PodResizePending`: a pod resize was requested but cannot be applied. See [Pod resize status](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/#pod-resize-status).
*   `PodResizeInProgress`: the pod is in the process of resizing. See [Pod resize status](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/#pod-resize-status).

| Field name | Description |
| --- | --- |
| `type` | Name of this Pod condition. |
| `status` | Indicates whether that condition is applicable, with possible values "`True`", "`False`", or "`Unknown`". |
| `lastProbeTime` | Timestamp of when the Pod condition was last probed. |
| `lastTransitionTime` | Timestamp for when the Pod last transitioned from one status to another. |
| `reason` | Machine-readable, UpperCamelCase text indicating the reason for the condition's last transition. |
| `message` | Human-readable message indicating details about the last status transition. |

### Pod readiness

FEATURE STATE:`Kubernetes v1.14 [stable]`

Your application can inject extra feedback or signals into PodStatus: _Pod readiness_. To use this, set `readinessGates` in the Pod's `spec` to specify a list of additional conditions that the kubelet evaluates for Pod readiness.

Readiness gates are determined by the current state of `status.condition` fields for the Pod. If Kubernetes cannot find such a condition in the `status.conditions` field of a Pod, the status of the condition is defaulted to "`False`".

Here is an example:

```yaml
kind: Pod
...
spec:
  readinessGates:
    - conditionType: "www.example.com/feature-1"
status:
  conditions:
    - type: Ready                              # a built-in PodCondition
      status: "False"
      lastProbeTime: null
      lastTransitionTime: 2018-01-01T00:00:00Z
    - type: "www.example.com/feature-1"        # an extra PodCondition
      status: "False"
      lastProbeTime: null
      lastTransitionTime: 2018-01-01T00:00:00Z
  containerStatuses:
    - containerID: docker://abcd...
      ready: true
...
```

The Pod conditions you add must have names that meet the Kubernetes [label key format](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).

### Status for Pod readiness

The `kubectl patch` command does not support patching object status. To set these `status.conditions` for the Pod, applications and [operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/ "A specialized controller used to manage a custom resource") should use the `PATCH` action. You can use a [Kubernetes client library](https://kubernetes.io/docs/reference/using-api/client-libraries/) to write code that sets custom Pod conditions for Pod readiness.

For a Pod that uses custom conditions, that Pod is evaluated to be ready **only** when both the following statements apply:

*   All containers in the Pod are ready.
*   All conditions specified in `readinessGates` are `True`.

When a Pod's containers are Ready but at least one custom condition is missing or `False`, the kubelet sets the Pod's [condition](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions) to `ContainersReady`.

### Pod network readiness

FEATURE STATE:`Kubernetes v1.29 [beta]`

#### Note:

During its early development, this condition was named `PodHasNetwork`.

After a Pod gets scheduled on a node, it needs to be admitted by the kubelet and to have any required storage volumes mounted. Once these phases are complete, the kubelet works with a container runtime (using [Container Runtime Interface (CRI)](https://kubernetes.io/docs/concepts/architecture/cri "Protocol for communication between the kubelet and the local container runtime.")) to set up a runtime sandbox and configure networking for the Pod. If the `PodReadyToStartContainersCondition`[feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) is enabled (it is enabled by default for Kubernetes 1.35), the `PodReadyToStartContainers` condition will be added to the `status.conditions` field of a Pod.

The `PodReadyToStartContainers` condition is set to `False` by the kubelet when it detects a Pod does not have a runtime sandbox with networking configured. This occurs in the following scenarios:

*   Early in the lifecycle of the Pod, when the kubelet has not yet begun to set up a sandbox for the Pod using the container runtime.
*   Later in the lifecycle of the Pod, when the Pod sandbox has been destroyed due to either:
    *   the node rebooting, without the Pod getting evicted
    *   for container runtimes that use virtual machines for isolation, the Pod sandbox virtual machine rebooting, which then requires creating a new sandbox and fresh container network configuration.

The `PodReadyToStartContainers` condition is set to `True` by the kubelet after the successful completion of sandbox creation and network configuration for the Pod by the runtime plugin. The kubelet can start pulling container images and create containers after `PodReadyToStartContainers` condition has been set to `True`.

For a Pod with init containers, the kubelet sets the `Initialized` condition to `True` after the init containers have successfully completed (which happens after successful sandbox creation and network configuration by the runtime plugin). For a Pod without init containers, the kubelet sets the `Initialized` condition to `True` before sandbox creation and network configuration starts.

Resizing Pods
-------------

FEATURE STATE:`Kubernetes v1.35 [stable]`(enabled by default)

Kubernetes supports changing the CPU and memory resources allocated to Pods after they are created. (For other infrastructure resources, you would need to use different techniques specific to those resources.) There are two main approaches to resizing CPU and memory:

### In-place Pod resize

You can resize a Pod's container-level CPU and memory resources without recreating the Pod. This is also called _in-place Pod vertical scaling_. This allows you to adjust resource allocation for running containers while potentially avoiding application disruption.

To perform an in-place resize, you update the Pod's desired state using the `/resize` subresource. The kubelet then attempts to apply the new resource values to the running containers. The Pod [conditions](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions "A condition represents the current state of a Kubernetes resource, providing information about whether certain aspects of the resource are true.")`PodResizePending` and `PodResizeInProgress` (described in [Pod conditions](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions)) indicate the status of the resize operation. For more details about resize status, see [Container Resize Status](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/#container-resize-status).

Key considerations for in-place resize:

*   Only CPU and memory resources can be resized in-place.
*   The Pod's [Quality of Service (QoS) class](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/) is determined at creation and cannot be changed by resizing.
*   You can configure whether a container restart is required for the resize using `resizePolicy` in the container specification.

For detailed instructions on performing in-place resize, see [Resize CPU and Memory Resources assigned to Containers](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/).

### Resizing by launching replacement Pods

The more cloud native approach to changing a Pod's resources is through the workload resource that manages it (such as a Deployment or StatefulSet). When you update the resource specifications in the Pod template, the workload's controller creates new Pods with the updated resources and terminates the old Pods according to its update strategy.

This approach:

*   Works with any Kubernetes version.
*   Can change any Pod specification, not just resources.
*   Results in Pod replacement, so you should design your workload to handle [planned disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/). Consider using a [PodDisruptionBudget](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) to control availability.
*   Requires that your Pods are managed by a workload resource.

You can also use a [VerticalPodAutoscaler](https://kubernetes.io/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/) to automatically manage Pod resource recommendations and updates.

Container probes
----------------

A _probe_ is a diagnostic performed periodically by the [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/) on a container. To perform a diagnostic, the kubelet either executes code within the container, or makes a network request.

### Check mechanisms

There are four different ways to check a container using a probe. Each probe must define exactly one of these four mechanisms:

`exec`Executes a specified command inside the container. The diagnostic is considered successful if the command exits with a status code of 0.`grpc`Performs a remote procedure call using [gRPC](https://grpc.io/). The target should implement [gRPC health checks](https://grpc.io/grpc/core/md_doc_health-checking.html). The diagnostic is considered successful if the `status` of the response is `SERVING`.`httpGet`Performs an HTTP `GET` request against the Pod's IP address on a specified port and path. The diagnostic is considered successful if the response has a status code greater than or equal to 200 and less than 400.`tcpSocket`Performs a TCP check against the Pod's IP address on a specified port. The diagnostic is considered successful if the port is open. If the remote system (the container) closes the connection immediately after it opens, this counts as healthy.

#### Caution:

Unlike the other mechanisms, `exec` probe's implementation involves the creation/forking of multiple processes each time when executed. As a result, in case of the clusters having higher pod densities, lower intervals of `initialDelaySeconds`, `periodSeconds`, configuring any probe with exec mechanism might introduce an overhead on the cpu usage of the node. In such scenarios, consider using the alternative probe mechanisms to avoid the overhead.

### Probe outcome

Each probe has one of three results:

`Success`The container passed the diagnostic.`Failure`The container failed the diagnostic.`Unknown`The diagnostic failed (no action should be taken, and the kubelet will make further checks).
### Types of probe

The kubelet can optionally perform and react to three kinds of probes on running containers:

`livenessProbe`Indicates whether the container is running. If the liveness probe fails, the kubelet kills the container, and the container is subjected to its [restart policy](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy). If a container does not provide a liveness probe, the default state is `Success`.`readinessProbe`Indicates whether the container is ready to respond to requests. If the readiness probe fails, the [EndpointSlice](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/ "EndpointSlices track the IP addresses of Pods for Services.") controller removes the Pod's IP address from the EndpointSlices of all Services that match the Pod. The default state of readiness before the initial delay is `Failure`. If a container does not provide a readiness probe, the default state is `Success`.`startupProbe`Indicates whether the application within the container is started. All other probes are disabled if a startup probe is provided, until it succeeds. If the startup probe fails, the kubelet kills the container, and the container is subjected to its [restart policy](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy). If a container does not provide a startup probe, the default state is `Success`.
For more information about how to set up a liveness, readiness, or startup probe, see [Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).

#### When should you use a liveness probe?

If the process in your container is able to crash on its own whenever it encounters an issue or becomes unhealthy, you do not necessarily need a liveness probe; the kubelet will automatically perform the correct action in accordance with the Pod's `restartPolicy`.

If you'd like your container to be killed and restarted if a probe fails, then specify a liveness probe, and specify a `restartPolicy` of Always or OnFailure.

#### When should you use a readiness probe?

If you'd like to start sending traffic to a Pod only when a probe succeeds, specify a readiness probe. In this case, the readiness probe might be the same as the liveness probe, but the existence of the readiness probe in the spec means that the Pod will start without receiving any traffic and only start receiving traffic after the probe starts succeeding.

If you want your container to be able to take itself down for maintenance, you can specify a readiness probe that checks an endpoint specific to readiness that is different from the liveness probe.

If your app has a strict dependency on back-end services, you can implement both a liveness and a readiness probe. The liveness probe passes when the app itself is healthy, but the readiness probe additionally checks that each required back-end service is available. This helps you avoid directing traffic to Pods that can only respond with error messages.

If your container needs to work on loading large data, configuration files, or migrations during startup, you can use a [startup probe](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#when-should-you-use-a-startup-probe). However, if you want to detect the difference between an app that has failed and an app that is still processing its startup data, you might prefer a readiness probe.

#### Note:

If you want to be able to drain requests when the Pod is deleted, you do not necessarily need a readiness probe; when the Pod is deleted, the corresponding endpoint in the `EndpointSlice` will update its [conditions](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/#conditions): the endpoint `ready` condition will be set to `false`, so load balancers will not use the Pod for regular traffic. See [Pod termination](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination) for more information about how the kubelet handles Pod deletion.

#### When should you use a startup probe?

Startup probes are useful for Pods that have containers that take a long time to come into service. Rather than set a long liveness interval, you can configure a separate configuration for probing the container as it starts up, allowing a time longer than the liveness interval would allow.

If your container usually starts in more than \( initialDelaySeconds + failureThreshold \times periodSeconds \), you should specify a startup probe that checks the same endpoint as the liveness probe. The default for `periodSeconds` is 10s. You should then set its `failureThreshold` high enough to allow the container to start, without changing the default values of the liveness probe. This helps to protect against deadlocks.

Termination of Pods
-------------------

Because Pods represent processes running on nodes in the cluster, it is important to allow those processes to gracefully terminate when they are no longer needed (rather than being abruptly stopped with a `KILL` signal and having no chance to clean up).

The design aim is for you to be able to request deletion and know when processes terminate, but also be able to ensure that deletes eventually complete. When you request deletion of a Pod, the cluster records and tracks the intended grace period before the Pod is allowed to be forcefully killed. With that forceful shutdown tracking in place, the [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet "An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.") attempts graceful shutdown.

Typically, with this graceful termination of the pod, kubelet makes requests to the container runtime to attempt to stop the containers in the pod by first sending a TERM (aka. SIGTERM) signal, with a grace period timeout, to the main process in each container. The requests to stop the containers are processed by the container runtime asynchronously. There is no guarantee to the order of processing for these requests. Many container runtimes respect the `STOPSIGNAL` value defined in the container image and, if different, send the container image configured STOPSIGNAL instead of TERM. Once the grace period has expired, the KILL signal is sent to any remaining processes, and the Pod is then deleted from the [API Server](https://kubernetes.io/docs/concepts/architecture/#kube-apiserver "Control plane component that serves the Kubernetes API."). If the kubelet or the container runtime's management service is restarted while waiting for processes to terminate, the cluster retries from the start including the full original grace period.

### Stop Signals

The stop signal used to kill the container can be defined in the container image with the `STOPSIGNAL` instruction. If no stop signal is defined in the image, the default signal of the container runtime (SIGTERM for both containerd and CRI-O) would be used to kill the container.

### Defining custom stop signals

FEATURE STATE:`Kubernetes v1.33 [alpha]`(disabled by default)

If the `ContainerStopSignals` feature gate is enabled, you can configure a custom stop signal for your containers from the container Lifecycle. We require the Pod's `spec.os.name` field to be present as a requirement for defining stop signals in the container lifecycle. The list of signals that are valid depends on the OS the Pod is scheduled to. For Pods scheduled to Windows nodes, we only support SIGTERM and SIGKILL as valid signals.

Here is an example Pod spec defining a custom stop signal:

```yaml
spec:
  os:
    name: linux
  containers:
    - name: my-container
      image: container-image:latest
      lifecycle:
        stopSignal: SIGUSR1
```

If a stop signal is defined in the lifecycle, this will override the signal defined in the container image. If no stop signal is defined in the container spec, the container would fall back to the default behavior.

### Pod Termination Flow

Pod termination flow, illustrated with an example:

1.   You use the `kubectl` tool to manually delete a specific Pod, with the default grace period (30 seconds).

2.   The Pod in the API server is updated with the time beyond which the Pod is considered "dead" along with the grace period. If you use `kubectl describe` to check the Pod you're deleting, that Pod shows up as "Terminating". On the node where the Pod is running: as soon as the kubelet sees that a Pod has been marked as terminating (a graceful shutdown duration has been set), the kubelet begins the local Pod shutdown process.

    1.   If one of the Pod's containers has defined a `preStop`[hook](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/) and the `terminationGracePeriodSeconds` in the Pod spec is not set to 0, the kubelet runs that hook inside of the container. The default `terminationGracePeriodSeconds` setting is 30 seconds.

If the `preStop` hook is still running after the grace period expires, the kubelet requests a small, one-off grace period extension of 2 seconds.

#### Note:

If the `preStop` hook needs longer to complete than the default grace period allows, you must modify `terminationGracePeriodSeconds` to suit this.

    1.   The kubelet triggers the container runtime to send a TERM signal to process 1 inside each container.

There is [special ordering](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#termination-with-sidecars) if the Pod has any [sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/ "An auxilliary container that stays running throughout the lifecycle of a Pod.") defined. Otherwise, the containers in the Pod receive the TERM signal at different times and in an arbitrary order. If the order of shutdowns matters, consider using a `preStop` hook to synchronize (or switch to using sidecar containers).

3.   At the same time as the kubelet is starting graceful shutdown of the Pod, the control plane evaluates whether to remove that shutting-down Pod from EndpointSlice objects, where those objects represent a [Service](https://kubernetes.io/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service.") with a configured [selector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/ "Allows users to filter a list of resources based on labels."). [ReplicaSets](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/ "ReplicaSet ensures that a specified number of Pod replicas are running at one time") and other workload resources no longer treat the shutting-down Pod as a valid, in-service replica.

Pods that shut down slowly should not continue to serve regular traffic and should start terminating and finish processing open connections. Some applications need to go beyond finishing open connections and need more graceful termination, for example, session draining and completion.

Any endpoints that represent the terminating Pods are not immediately removed from EndpointSlices, and a status indicating [terminating state](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/#conditions) is exposed from the EndpointSlice API. Terminating endpoints always have their `ready` status as `false` (for backward compatibility with versions before 1.26), so load balancers will not use it for regular traffic.

If traffic draining on terminating Pod is needed, the actual readiness can be checked as a condition `serving`. You can find more details on how to implement connections draining in the tutorial [Pods And Endpoints Termination Flow](https://kubernetes.io/docs/tutorials/services/pods-and-endpoint-termination-flow/)

[](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)
4.   The kubelet ensures the Pod is shut down and terminated

    1.   When the grace period expires, if there is still any container running in the Pod, the kubelet triggers forcible shutdown. The container runtime sends `SIGKILL` to any processes still running in any container in the Pod. The kubelet also cleans up a hidden `pause` container if that container runtime uses one.
    2.   The kubelet transitions the Pod into a terminal phase (`Failed` or `Succeeded` depending on the end state of its containers).
    3.   The kubelet triggers forcible removal of the Pod object from the API server, by setting grace period to 0 (immediate deletion).
    4.   The API server deletes the Pod's API object, which is then no longer visible from any client.

### Forced Pod termination

#### Caution:

Forced deletions can be potentially disruptive for some workloads and their Pods.

By default, all deletes are graceful within 30 seconds. The `kubectl delete` command supports the `--grace-period=<seconds>` option which allows you to override the default and specify your own value.

Setting the grace period to `0` forcibly and immediately deletes the Pod from the API server. If the Pod was still running on a node, that forcible deletion triggers the kubelet to begin immediate cleanup.

Using kubectl, You must specify an additional flag `--force` along with `--grace-period=0` in order to perform force deletions.

When a force deletion is performed, the API server does not wait for confirmation from the kubelet that the Pod has been terminated on the node it was running on. It removes the Pod in the API immediately so a new Pod can be created with the same name. On the node, Pods that are set to terminate immediately will still be given a small grace period before being force killed.

#### Caution:

Immediate deletion does not wait for confirmation that the running resource has been terminated. The resource may continue to run on the cluster indefinitely.

If you need to force-delete Pods that are part of a StatefulSet, refer to the task documentation for [deleting Pods from a StatefulSet](https://kubernetes.io/docs/tasks/run-application/force-delete-stateful-set-pod/).

### Pod shutdown and sidecar containers

If your Pod includes one or more [sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) (init containers with an `Always` restart policy), the kubelet will delay sending the TERM signal to these sidecar containers until the last main container has fully terminated. The sidecar containers will be terminated in the reverse order they are defined in the Pod spec. This ensures that sidecar containers continue serving the other containers in the Pod until they are no longer needed.

This means that slow termination of a main container will also delay the termination of the sidecar containers. If the grace period expires before the termination process is complete, the Pod may enter [forced termination](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination-beyond-grace-period). In this case, all remaining containers in the Pod will be terminated simultaneously with a short grace period.

Similarly, if the Pod has a `preStop` hook that exceeds the termination grace period, emergency termination may occur. In general, if you have used `preStop` hooks to control the termination order without sidecar containers, you can now remove them and allow the kubelet to manage sidecar termination automatically.

### Garbage collection of Pods

For failed Pods, the API objects remain in the cluster's API until a human or [controller](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") process explicitly removes them.

The Pod garbage collector (PodGC), which is a controller in the control plane, cleans up terminated Pods (with a phase of `Succeeded` or `Failed`), when the number of Pods exceeds the configured threshold (determined by `terminated-pod-gc-threshold` in the kube-controller-manager). This avoids a resource leak as Pods are created and terminated over time.

Additionally, PodGC cleans up any Pods which satisfy any of the following conditions:

1.   are orphan Pods - bound to a node which no longer exists,
2.   are unscheduled terminating Pods,
3.   are terminating Pods, bound to a non-ready node tainted with [`node.kubernetes.io/out-of-service`](https://kubernetes.io/docs/reference/labels-annotations-taints/#node-kubernetes-io-out-of-service).

Along with cleaning up the Pods, PodGC will also mark them as failed if they are in a non-terminal phase. Also, PodGC adds a Pod disruption condition when cleaning up an orphan Pod. See [Pod disruption conditions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#pod-disruption-conditions) for more details.

Pod behavior during kubelet restarts
------------------------------------

If you restart the kubelet, Pods (and their containers) continue to run even during the restart. When there are running Pods on a node, stopping or restarting the kubelet on that node does **not** cause the kubelet to stop all local Pods before the kubelet itself stops. To stop the Pods on a node, you can use `kubectl drain`.

### Detection of kubelet restarts

FEATURE STATE:`Kubernetes v1.35 [deprecated]`(disabled by default)

When the kubelet starts, it checks to see if there is already a Node with bound Pods. If the Node's [`Ready` condition](https://kubernetes.io/docs/reference/node/node-status/#condition) remains unchanged, in other words the condition has not transitioned from true to false, Kubernetes detects this a _kubelet restart_. (It's possible to restart the kubelet in other ways, for example to fix a node bug, but in these cases, Kubernetes picks the safe option and treats this as if you stopped the kubelet and then later started it).

When the kubelet restarts, the container statuses are managed differently based on the feature gate setting:

*   By default, the kubelet does not change container statuses after a restart. Containers that were in set to `ready: true` state remain remain ready.

If you stop the kubelet long enough for it to fail a series of [node heartbeat](https://kubernetes.io/docs/concepts/architecture/leases/#node-heart-beats) checks, and then you wait before you start the kubelet again, Kubernetes may begin to evict Pods from that Node. However, even though Pod evictions begin to happen, Kubernetes does not mark the individual containers in those Pods as `ready: false`. The Pod-level eviction happens after the control plane taints the node as `node.kubernetes.io/not-ready` (due to the failed heartbeats).

*   In Kubernetes 1.35 you can opt in to a legacy behavior where the kubelet always modify the containers `ready` value, after a kubelet restart, to be false.

This legacy behavior was the default for a long time, but caused issue for people using Kubernetes, especially in large scale deployments. Althought the feature gate allows reverting to this legacy behavior temporarily, the Kubernetes project recommends that you file a bug report if you encounter problems. The `ChangeContainerStatusOnKubeletRestart`[feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#ChangeContainerStatusOnKubeletRestart) will be removed in the future.

What's next
-----------

*   Get hands-on experience [attaching handlers to container lifecycle events](https://kubernetes.io/docs/tasks/configure-pod-container/attach-handler-lifecycle-event/).

*   Get hands-on experience [configuring Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).

*   Learn more about [container lifecycle hooks](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/).

*   Learn more about [sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/).

*   For detailed information about Pod and container status in the API, see the API reference documentation covering [`status`](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#PodStatus) for Pod.

Feedback
--------

Was this page helpful?

Yes No
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).

Last modified January 15, 2026 at 4:43 PM PST: [Move Resizing Pods section after Pod conditions subsections (70aadb09d6)](https://github.com/kubernetes/website/commit/70aadb09d631ee97e18b2ace6b47042774d9a401)

[Edit this page](https://github.com/kubernetes/website/edit/main/content/en/docs/concepts/workloads/pods/pod-lifecycle.md)[Create child page](https://github.com/kubernetes/website/new/main/content/en/docs/concepts/workloads/pods/pod-lifecycle.md?filename=change-me.md&value=---%0Atitle%3A+%22Long+Page+Title%22%0AlinkTitle%3A+%22Short+Nav+Title%22%0Aweight%3A+100%0Adescription%3A+%3E-%0A+++++Page+description+for+heading+and+indexes.%0A---%0A%0A%23%23+Heading%0A%0AEdit+this+template+to+create+your+new+page.%0A%0A%2A+Give+it+a+good+name%2C+ending+in+%60.md%60+-+e.g.+%60getting-started.md%60%0A%2A+Edit+the+%22front+matter%22+section+at+the+top+of+the+page+%28weight+controls+how+its+ordered+amongst+other+pages+in+the+same+directory%3B+lowest+number+first%29.%0A%2A+Add+a+good+commit+message+at+the+bottom+of+the+page+%28%3C80+characters%3B+use+the+extended+description+field+for+more+detail%29.%0A%2A+Create+a+new+branch+so+you+can+preview+your+new+file+and+request+a+review+via+Pull+Request.%0A)[Create an issue](https://github.com/kubernetes/website/issues/new?title=Pod%20Lifecycle)[Print entire section](https://kubernetes.io/docs/concepts/workloads/pods/_print/)

*   [Pod lifetime](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-lifetime)
    *   [Pods and fault recovery](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-fault-recovery)
    *   [Associated lifetimes](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#associated-lifetimes)

*   [Pod phase](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase)
*   [Container states](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#container-states)
    *   [`Waiting`](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#container-state-waiting)
    *   [`Running`](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#container-state-running)
    *   [`Terminated`](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#container-state-terminated)

*   [How Pods handle problems with containers](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#container-restarts)
    *   [Container restarts](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy)
    *   [Reduced container restart delay](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#reduced-container-restart-delay)
    *   [Configurable container restart delay](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#configurable-container-restart-delay)

*   [Pod conditions](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions)
    *   [Pod readiness](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-readiness-gate)
    *   [Status for Pod readiness](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-readiness-status)
    *   [Pod network readiness](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-has-network)

*   [Resizing Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-resize)
    *   [In-place Pod resize](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-resize-inplace)
    *   [Resizing by launching replacement Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#resizing-by-launching-replacement-pods)

*   [Container probes](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#container-probes)
    *   [Check mechanisms](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#probe-check-methods)
    *   [Probe outcome](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#probe-outcome)
    *   [Types of probe](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#types-of-probe)

*   [Termination of Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination)
    *   [Stop Signals](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination-stop-signals)
    *   [Defining custom stop signals](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#defining-custom-stop-signals)
    *   [Pod Termination Flow](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination-flow)
    *   [Forced Pod termination](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination-forced)
    *   [Pod shutdown and sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#termination-with-sidecars)
    *   [Garbage collection of Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-garbage-collection)

*   [Pod behavior during kubelet restarts](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#kubelet-restarts)
    *   [Detection of kubelet restarts](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#detection-of-kubelet-restarts)

*   [What's next](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#what-s-next)

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
