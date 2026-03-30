# Source: https://kubernetes.io/docs/concepts/services-networking/service/

Title: Service

URL Source: https://kubernetes.io/docs/concepts/services-networking/service/

Markdown Content:
Service | Kubernetes
===============
[Kubernetes](https://kubernetes.io/)

*   [Documentation](https://kubernetes.io/docs/)
*   [Kubernetes Blog](https://kubernetes.io/blog/)
*   [Training](https://kubernetes.io/training/)
*   [Careers](https://kubernetes.io/careers/)
*   [Partners](https://kubernetes.io/partners/)
*   [Community](https://kubernetes.io/community/)
*   [Versions](https://kubernetes.io/docs/concepts/services-networking/service/#)[Release Information](https://kubernetes.io/releases)[v1.35](https://kubernetes.io/docs/concepts/services-networking/service/)[v1.34](https://v1-34.docs.kubernetes.io/docs/concepts/services-networking/service/)[v1.33](https://v1-33.docs.kubernetes.io/docs/concepts/services-networking/service/)[v1.32](https://v1-32.docs.kubernetes.io/docs/concepts/services-networking/service/)[v1.31](https://v1-31.docs.kubernetes.io/docs/concepts/services-networking/service/) 
*   [English](https://kubernetes.io/docs/concepts/services-networking/service/#)[中文 (Chinese)](https://kubernetes.io/zh-cn/docs/concepts/services-networking/service/)[Français (French)](https://kubernetes.io/fr/docs/concepts/services-networking/service/)[Deutsch (German)](https://kubernetes.io/de/docs/concepts/services-networking/service/)[Bahasa Indonesia (Indonesian)](https://kubernetes.io/id/docs/concepts/services-networking/service/)[日本語 (Japanese)](https://kubernetes.io/ja/docs/concepts/services-networking/service/)[한국어 (Korean)](https://kubernetes.io/ko/docs/concepts/services-networking/service/)[Português (Portuguese)](https://kubernetes.io/pt-br/docs/concepts/services-networking/service/)[Español (Spanish)](https://kubernetes.io/es/docs/concepts/services-networking/service/) 

#### ![Image 1](https://kubernetes.io/images/announcements/kccnc-eu-2026-black.svg)[KubeCon + CloudNativeCon Europe 2026](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/?utm_source=kubernetes&utm_medium=homepage&utm_campaign=18269725-KubeCon-EU-2026&utm_content=slim-banner)

Join us for four days of incredible opportunities to collaborate, learn and share with the cloud native community.

[Buy your ticket now! 23 - 26 March | Amsterdam, The Netherlands](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/register/?utm_source=kubernetes&utm_medium=homepage&utm_campaign=18269725-KubeCon-EU-2026&utm_content=slim-banner)

[English](https://kubernetes.io/docs/concepts/services-networking/service/#)

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
3.   [Services, Load Balancing, and Networking](https://kubernetes.io/docs/concepts/services-networking/)
4.   [Service](https://kubernetes.io/docs/concepts/services-networking/service/)

Service
=======

Expose an application running in your cluster behind a single outward-facing endpoint, even when the workload is split across multiple backends.

In Kubernetes, a Service is a method for exposing a network application that is running as one or more [Pods](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.") in your cluster.

A key aim of Services in Kubernetes is that you don't need to modify your existing application to use an unfamiliar service discovery mechanism. You can run code in Pods, whether this is a code designed for a cloud-native world, or an older app you've containerized. You use a Service to make that set of Pods available on the network so that clients can interact with it.

If you use a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/ "Manages a replicated application on your cluster.") to run your app, that Deployment can create and destroy Pods dynamically. From one moment to the next, you don't know how many of those Pods are working and healthy; you might not even know what those healthy Pods are named. Kubernetes [Pods](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.") are created and destroyed to match the desired state of your cluster. Pods are ephemeral resources (you should not expect that an individual Pod is reliable and durable).

Each Pod gets its own IP address (Kubernetes expects network plugins to ensure this). For a given Deployment in your cluster, the set of Pods running in one moment in time could be different from the set of Pods running that application a moment later.

This leads to a problem: if some set of Pods (call them "backends") provides functionality to other Pods (call them "frontends") inside your cluster, how do the frontends find out and keep track of which IP address to connect to, so that the frontend can use the backend part of the workload?

Enter _Services_.

Services in Kubernetes
----------------------

The Service API, part of Kubernetes, is an abstraction to help you expose groups of Pods over a network. Each Service object defines a logical set of endpoints (usually these endpoints are Pods) along with a policy about how to make those pods accessible.

For example, consider a stateless image-processing backend which is running with 3 replicas. Those replicas are fungible—frontends do not care which backend they use. While the actual Pods that compose the backend set may change, the frontend clients should not need to be aware of that, nor should they need to keep track of the set of backends themselves.

The Service abstraction enables this decoupling.

The set of Pods targeted by a Service is usually determined by a [selector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/ "Allows users to filter a list of resources based on labels.") that you define. To learn about other ways to define Service endpoints, see [Services _without_ selectors](https://kubernetes.io/docs/concepts/services-networking/service/#services-without-selectors).

If your workload speaks HTTP, you might choose to use an [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) to control how web traffic reaches that workload. Ingress is not a Service type, but it acts as the entry point for your cluster. An Ingress lets you consolidate your routing rules into a single resource, so that you can expose multiple components of your workload, running separately in your cluster, behind a single listener.

The [Gateway](https://gateway-api.sigs.k8s.io/#what-is-the-gateway-api) API for Kubernetes provides extra capabilities beyond Ingress and Service. You can add Gateway to your cluster - it is a family of extension APIs, implemented using [CustomResourceDefinitions](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/ "Custom code that defines a resource to add to your Kubernetes API server without building a complete custom server.") - and then use these to configure access to network services that are running in your cluster.

### Cloud-native service discovery

If you're able to use Kubernetes APIs for service discovery in your application, you can query the [API server](https://kubernetes.io/docs/concepts/architecture/#kube-apiserver "Control plane component that serves the Kubernetes API.") for matching EndpointSlices. Kubernetes updates the EndpointSlices for a Service whenever the set of Pods in a Service changes.

For non-native applications, Kubernetes offers ways to place a network port or load balancer in between your application and the backend Pods.

Either way, your workload can use these [service discovery](https://kubernetes.io/docs/concepts/services-networking/service/#discovering-services) mechanisms to find the target it wants to connect to.

Defining a Service
------------------

A Service is an [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects "An entity in the Kubernetes system, representing part of the state of your cluster.") (the same way that a Pod or a ConfigMap is an object). You can create, view or modify Service definitions using the Kubernetes API. Usually you use a tool such as `kubectl` to make those API calls for you.

For example, suppose you have a set of Pods that each listen on TCP port 9376 and are labelled as `app.kubernetes.io/name=MyApp`. You can define a Service to publish that TCP listener:

[`service/simple-service.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/service/simple-service.yaml)![Image 2](https://kubernetes.io/images/copycode.svg)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app.kubernetes.io/name: MyApp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376
```

Applying this manifest creates a new Service named "my-service" with the default ClusterIP [service type](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types). The Service targets TCP port 9376 on any Pod with the `app.kubernetes.io/name: MyApp` label.

Kubernetes assigns this Service an IP address (the _cluster IP_), that is used by the virtual IP address mechanism. For more details on that mechanism, read [Virtual IPs and Service Proxies](https://kubernetes.io/docs/reference/networking/virtual-ips/).

The controller for that Service continuously scans for Pods that match its selector, and then makes any necessary updates to the set of EndpointSlices for the Service.

The name of a Service object must be a valid [RFC 1035 label name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#rfc-1035-label-names).

#### Note:

A Service can map _any_ incoming `port` to a `targetPort`. By default and for convenience, the `targetPort` is set to the same value as the `port` field.

### Relaxed naming requirements for Service objects

FEATURE STATE:`Kubernetes v1.34 [alpha]`(disabled by default)

The `RelaxedServiceNameValidation` feature gate allows Service object names to start with a digit. When this feature gate is enabled, Service object names must be valid [RFC 1123 label names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-label-names).

### Port definitions

Port definitions in Pods have names, and you can reference these names in the `targetPort` attribute of a Service. For example, we can bind the `targetPort` of the Service to the Pod port in the following way:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app.kubernetes.io/name: proxy
  ports:
  - name: name-of-service-port
    protocol: TCP
    port: 80
    targetPort: http-web-svc

---
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    app.kubernetes.io/name: proxy
spec:
  containers:
  - name: nginx
    image: nginx:stable
    ports:
      - containerPort: 80
        name: http-web-svc
```

This works even if there is a mixture of Pods in the Service using a single configured name, with the same network protocol available via different port numbers. This offers a lot of flexibility for deploying and evolving your Services. For example, you can change the port numbers that Pods expose in the next version of your backend software, without breaking clients.

The default protocol for Services is [TCP](https://kubernetes.io/docs/reference/networking/service-protocols/#protocol-tcp); you can also use any other [supported protocol](https://kubernetes.io/docs/reference/networking/service-protocols/).

Because many Services need to expose more than one port, Kubernetes supports [multiple port definitions](https://kubernetes.io/docs/concepts/services-networking/service/#multi-port-services) for a single Service. Each port definition can have the same `protocol`, or a different one.

### Services without selectors

Services most commonly abstract access to Kubernetes Pods thanks to the selector, but when used with a corresponding set of [EndpointSlices](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/ "EndpointSlices track the IP addresses of Pods for Services.") objects and without a selector, the Service can abstract other kinds of backends, including ones that run outside the cluster.

For example:

*   You want to have an external database cluster in production, but in your test environment you use your own databases.
*   You want to point your Service to a Service in a different [Namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces "An abstraction used by Kubernetes to support isolation of groups of resources within a single cluster.") or on another cluster.
*   You are migrating a workload to Kubernetes. While evaluating the approach, you run only a portion of your backends in Kubernetes.

In any of these scenarios you can define a Service _without_ specifying a selector to match Pods. For example:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 9376
```

Because this Service has no selector, the corresponding EndpointSlice objects are not created automatically. You can map the Service to the network address and port where it's running, by adding an EndpointSlice object manually. For example:

```yaml
apiVersion: discovery.k8s.io/v1
kind: EndpointSlice
metadata:
  name: my-service-1 # by convention, use the name of the Service
                     # as a prefix for the name of the EndpointSlice
  labels:
    # You should set the "kubernetes.io/service-name" label.
    # Set its value to match the name of the Service
    kubernetes.io/service-name: my-service
addressType: IPv4
ports:
  - name: http # should match with the name of the service port defined above
    appProtocol: http
    protocol: TCP
    port: 9376
endpoints:
  - addresses:
      - "10.4.5.6"
  - addresses:
      - "10.1.2.3"
```

#### Custom EndpointSlices

When you create an [EndpointSlice](https://kubernetes.io/docs/concepts/services-networking/service/#endpointslices) object for a Service, you can use any name for the EndpointSlice. Each EndpointSlice in a namespace must have a unique name. You link an EndpointSlice to a Service by setting the `kubernetes.io/service-name`[label](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels "Tags objects with identifying attributes that are meaningful and relevant to users.") on that EndpointSlice.

#### Note:

The endpoint IPs _must not_ be: loopback (127.0.0.0/8 for IPv4, ::1/128 for IPv6), or link-local (169.254.0.0/16 and 224.0.0.0/24 for IPv4, fe80::/64 for IPv6).

The endpoint IP addresses cannot be the cluster IPs of other Kubernetes Services, because [kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/ "kube-proxy is a network proxy that runs on each node in the cluster.") doesn't support virtual IPs as a destination.

For an EndpointSlice that you create yourself, or in your own code, you should also pick a value to use for the label [`endpointslice.kubernetes.io/managed-by`](https://kubernetes.io/docs/reference/labels-annotations-taints/#endpointslicekubernetesiomanaged-by). If you create your own controller code to manage EndpointSlices, consider using a value similar to `"my-domain.example/name-of-controller"`. If you are using a third party tool, use the name of the tool in all-lowercase and change spaces and other punctuation to dashes (`-`). If people are directly using a tool such as `kubectl` to manage EndpointSlices, use a name that describes this manual management, such as `"staff"` or `"cluster-admins"`. You should avoid using the reserved value `"controller"`, which identifies EndpointSlices managed by Kubernetes' own control plane.

#### Accessing a Service without a selector

Accessing a Service without a selector works the same as if it had a selector. In the [example](https://kubernetes.io/docs/concepts/services-networking/service/#services-without-selectors) for a Service without a selector, traffic is routed to one of the two endpoints defined in the EndpointSlice manifest: a TCP connection to 10.1.2.3 or 10.4.5.6, on port 9376.

#### Note:

The Kubernetes API server does not allow proxying to endpoints that are not mapped to pods. Actions such as `kubectl port-forward service/<service-name> forwardedPort:servicePort` where the service has no selector will fail due to this constraint. This prevents the Kubernetes API server from being used as a proxy to endpoints the caller may not be authorized to access.

An `ExternalName` Service is a special case of Service that does not have selectors and uses DNS names instead. For more information, see the [ExternalName](https://kubernetes.io/docs/concepts/services-networking/service/#externalname) section.

### EndpointSlices

FEATURE STATE:`Kubernetes v1.21 [stable]`

[EndpointSlices](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/) are objects that represent a subset (a _slice_) of the backing network endpoints for a Service.

Your Kubernetes cluster tracks how many endpoints each EndpointSlice represents. If there are so many endpoints for a Service that a threshold is reached, then Kubernetes adds another empty EndpointSlice and stores new endpoint information there. By default, Kubernetes makes a new EndpointSlice once the existing EndpointSlices all contain at least 100 endpoints. Kubernetes does not make the new EndpointSlice until an extra endpoint needs to be added.

See [EndpointSlices](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/) for more information about this API.

### Endpoints (deprecated)

FEATURE STATE:`Kubernetes v1.33 [deprecated]`

The EndpointSlice API is the evolution of the older [Endpoints](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/endpoints-v1/) API. The deprecated Endpoints API has several problems relative to EndpointSlice:

*   It does not support dual-stack clusters.
*   It does not contain information needed to support newer features, such as [trafficDistribution](https://kubernetes.io/docs/concepts/services-networking/service/#traffic-distribution).
*   It will truncate the list of endpoints if it is too long to fit in a single object.

Because of this, it is recommended that all clients use the EndpointSlice API rather than Endpoints.

#### Over-capacity endpoints

Kubernetes limits the number of endpoints that can fit in a single Endpoints object. When there are over 1000 backing endpoints for a Service, Kubernetes truncates the data in the Endpoints object. Because a Service can be linked with more than one EndpointSlice, the 1000 backing endpoint limit only affects the legacy Endpoints API.

In that case, Kubernetes selects at most 1000 possible backend endpoints to store into the Endpoints object, and sets an [annotation](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations "A key-value pair that is used to attach arbitrary non-identifying metadata to objects.") on the Endpoints: [`endpoints.kubernetes.io/over-capacity: truncated`](https://kubernetes.io/docs/reference/labels-annotations-taints/#endpoints-kubernetes-io-over-capacity). The control plane also removes that annotation if the number of backend Pods drops below 1000.

Traffic is still sent to backends, but any load balancing mechanism that relies on the legacy Endpoints API only sends traffic to at most 1000 of the available backing endpoints.

The same API limit means that you cannot manually update an Endpoints to have more than 1000 endpoints.

### Application protocol

FEATURE STATE:`Kubernetes v1.20 [stable]`

The `appProtocol` field provides a way to specify an application protocol for each Service port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. The value of this field is mirrored by the corresponding Endpoints and EndpointSlice objects.

This field follows standard Kubernetes label syntax. Valid values are one of:

*   [IANA standard service names](https://www.iana.org/assignments/service-names).

*   Implementation-defined prefixed names such as `mycompany.com/my-custom-protocol`.

*   Kubernetes-defined prefixed names:

| Protocol | Description |
| --- | --- |
| `kubernetes.io/h2c` | HTTP/2 over cleartext as described in [RFC 7540](https://www.rfc-editor.org/rfc/rfc7540) |
| `kubernetes.io/ws` | WebSocket over cleartext as described in [RFC 6455](https://www.rfc-editor.org/rfc/rfc6455) |
| `kubernetes.io/wss` | WebSocket over TLS as described in [RFC 6455](https://www.rfc-editor.org/rfc/rfc6455) |

### Multi-port Services

For some Services, you need to expose more than one port. Kubernetes lets you configure multiple port definitions on a Service object. When using multiple ports for a Service, you must give all of your ports names so that these are unambiguous. For example:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app.kubernetes.io/name: MyApp
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 9376
    - name: https
      protocol: TCP
      port: 443
      targetPort: 9377
```

#### Note:

As with Kubernetes [names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names "A client-provided string that refers to an object in a resource URL, such as /api/v1/pods/some-name.") in general, names for ports must only contain lowercase alphanumeric characters and `-`. Port names must also start and end with an alphanumeric character.

For example, the names `123-abc` and `web` are valid, but `123_abc` and `-web` are not.

Service type
------------

For some parts of your application (for example, frontends) you may want to expose a Service onto an external IP address, one that's accessible from outside of your cluster.

Kubernetes Service types allow you to specify what kind of Service you want.

The available `type` values and their behaviors are:

[`ClusterIP`](https://kubernetes.io/docs/concepts/services-networking/service/#type-clusterip)Exposes the Service on a cluster-internal IP. Choosing this value makes the Service only reachable from within the cluster. This is the default that is used if you don't explicitly specify a `type` for a Service. You can expose the Service to the public internet using an [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) or a [Gateway](https://gateway-api.sigs.k8s.io/).[`NodePort`](https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport)Exposes the Service on each Node's IP at a static port (the `NodePort`). To make the node port available, Kubernetes sets up a cluster IP address, the same as if you had requested a Service of `type: ClusterIP`.[`LoadBalancer`](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer)Exposes the Service externally using an external load balancer. Kubernetes does not directly offer a load balancing component; you must provide one, or you can integrate your Kubernetes cluster with a cloud provider.[`ExternalName`](https://kubernetes.io/docs/concepts/services-networking/service/#externalname)Maps the Service to the contents of the `externalName` field (for example, to the hostname `api.foo.bar.example`). The mapping configures your cluster's DNS server to return a `CNAME` record with that external hostname value. No proxying of any kind is set up.
The `type` field in the Service API is designed as nested functionality - each level adds to the previous. However there is an exception to this nested design. You can define a `LoadBalancer` Service by [disabling the load balancer `NodePort` allocation](https://kubernetes.io/docs/concepts/services-networking/service/#load-balancer-nodeport-allocation).

### `type: ClusterIP`

This default Service type assigns an IP address from a pool of IP addresses that your cluster has reserved for that purpose.

Several of the other types for Service build on the `ClusterIP` type as a foundation.

If you define a Service that has the `.spec.clusterIP` set to `"None"` then Kubernetes does not assign an IP address. See [headless Services](https://kubernetes.io/docs/concepts/services-networking/service/#headless-services) for more information.

#### Choosing your own IP address

You can specify your own cluster IP address as part of a `Service` creation request. To do this, set the `.spec.clusterIP` field. For example, if you already have an existing DNS entry that you wish to reuse, or legacy systems that are configured for a specific IP address and difficult to re-configure.

The IP address that you choose must be a valid IPv4 or IPv6 address from within the `service-cluster-ip-range` CIDR range that is configured for the API server. If you try to create a Service with an invalid `clusterIP` address value, the API server will return a 422 HTTP status code to indicate that there's a problem.

Read [avoiding collisions](https://kubernetes.io/docs/reference/networking/virtual-ips/#avoiding-collisions) to learn how Kubernetes helps reduce the risk and impact of two different Services both trying to use the same IP address.

### `type: NodePort`

If you set the `type` field to `NodePort`, the Kubernetes control plane allocates a port from a range specified by `--service-node-port-range` flag (default: 30000-32767). Each node proxies that port (the same port number on every Node) into your Service. Your Service reports the allocated port in its `.spec.ports[*].nodePort` field.

Using a NodePort gives you the freedom to set up your own load balancing solution, to configure environments that are not fully supported by Kubernetes, or even to expose one or more nodes' IP addresses directly.

For a node port Service, Kubernetes additionally allocates a port (TCP, UDP or SCTP to match the protocol of the Service). Every node in the cluster configures itself to listen on that assigned port and to forward traffic to one of the ready endpoints associated with that Service. You'll be able to contact the `type: NodePort` Service, from outside the cluster, by connecting to any node using the appropriate protocol (for example: TCP), and the appropriate port (as assigned to that Service).

#### Choosing your own port

If you want a specific port number, you can specify a value in the `nodePort` field. The control plane will either allocate you that port or report that the API transaction failed. This means that you need to take care of possible port collisions yourself. You also have to use a valid port number, one that's inside the range configured for NodePort use.

Here is an example manifest for a Service of `type: NodePort` that specifies a NodePort value (30007, in this example):

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  type: NodePort
  selector:
    app.kubernetes.io/name: MyApp
  ports:
    - port: 80
      # By default and for convenience, the `targetPort` is set to
      # the same value as the `port` field.
      targetPort: 80
      # Optional field
      # By default and for convenience, the Kubernetes control plane
      # will allocate a port from a range (default: 30000-32767)
      nodePort: 30007
```

#### Reserve Nodeport ranges to avoid collisions

The policy for assigning ports to NodePort services applies to both the auto-assignment and the manual assignment scenarios. When a user wants to create a NodePort service that uses a specific port, the target port may conflict with another port that has already been assigned.

To avoid this problem, the port range for NodePort services is divided into two bands. Dynamic port assignment uses the upper band by default, and it may use the lower band once the upper band has been exhausted. Users can then allocate from the lower band with a lower risk of port collision.

When using the default NodePort range 30000-32767, the bands are partitioned as follows:

*   Static band: 30000-30085
*   Dynamic band: 30086-32767

See [Avoid Collisions Assigning Ports to NodePort Services](https://kubernetes.io/blog/2023/05/11/nodeport-dynamic-and-static-allocation/) for more details on how the static and dynamic bands are calculated.

#### Custom IP address configuration for `type: NodePort` Services

You can set up nodes in your cluster to use a particular IP address for serving node port services. You might want to do this if each node is connected to multiple networks (for example: one network for application traffic, and another network for traffic between nodes and the control plane).

If you want to specify particular IP address(es) to proxy the port, you can set the `--nodeport-addresses` flag for kube-proxy or the equivalent `nodePortAddresses` field of the [kube-proxy configuration file](https://kubernetes.io/docs/reference/config-api/kube-proxy-config.v1alpha1/) to particular IP block(s).

This flag takes a comma-delimited list of IP blocks (e.g. `10.0.0.0/8`, `192.0.2.0/25`) to specify IP address ranges that kube-proxy should consider as local to this node.

For example, if you start kube-proxy with the `--nodeport-addresses=127.0.0.0/8` flag, kube-proxy only selects the loopback interface for NodePort Services. The default for `--nodeport-addresses` is an empty list. This means that kube-proxy should consider all available network interfaces for NodePort. (That's also compatible with earlier Kubernetes releases.)

#### Note:

This Service is visible as `<NodeIP>:spec.ports[*].nodePort` and `.spec.clusterIP:spec.ports[*].port`. If the `--nodeport-addresses` flag for kube-proxy or the equivalent field in the kube-proxy configuration file is set, `<NodeIP>` would be a filtered node IP address (or possibly IP addresses).

### `type: LoadBalancer`

On cloud providers which support external load balancers, setting the `type` field to `LoadBalancer` provisions a load balancer for your Service. The actual creation of the load balancer happens asynchronously, and information about the provisioned balancer is published in the Service's `.status.loadBalancer` field. For example:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app.kubernetes.io/name: MyApp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376
  clusterIP: 10.0.171.239
  type: LoadBalancer
status:
  loadBalancer:
    ingress:
    - ip: 192.0.2.127
```

Traffic from the external load balancer is directed at the backend Pods. The cloud provider decides how it is load balanced.

To implement a Service of `type: LoadBalancer`, Kubernetes typically starts off by making the changes that are equivalent to you requesting a Service of `type: NodePort`. The cloud-controller-manager component then configures the external load balancer to forward traffic to that assigned node port.

You can configure a load balanced Service to [omit](https://kubernetes.io/docs/concepts/services-networking/service/#load-balancer-nodeport-allocation) assigning a node port, provided that the cloud provider implementation supports this.

Some cloud providers allow you to specify the `loadBalancerIP`. In those cases, the load-balancer is created with the user-specified `loadBalancerIP`. If the `loadBalancerIP` field is not specified, the load balancer is set up with an ephemeral IP address. If you specify a `loadBalancerIP` but your cloud provider does not support the feature, the `loadbalancerIP` field that you set is ignored.

#### Note:

The`.spec.loadBalancerIP` field for a Service was deprecated in Kubernetes v1.24.

This field was under-specified and its meaning varies across implementations. It also cannot support dual-stack networking. This field may be removed in a future API version.

If you're integrating with a provider that supports specifying the load balancer IP address(es) for a Service via a (provider specific) annotation, you should switch to doing that.

If you are writing code for a load balancer integration with Kubernetes, avoid using this field. You can integrate with [Gateway](https://gateway-api.sigs.k8s.io/) rather than Service, or you can define your own (provider specific) annotations on the Service that specify the equivalent detail.

#### Node liveness impact on load balancer traffic

Load balancer health checks are critical to modern applications. They are used to determine which server (virtual machine, or IP address) the load balancer should dispatch traffic to. The Kubernetes APIs do not define how health checks have to be implemented for Kubernetes managed load balancers, instead it's the cloud providers (and the people implementing integration code) who decide on the behavior. Load balancer health checks are extensively used within the context of supporting the `externalTrafficPolicy` field for Services.

#### Load balancers with mixed protocol types

FEATURE STATE:`Kubernetes v1.26 [stable]`(enabled by default)

By default, for LoadBalancer type of Services, when there is more than one port defined, all ports must have the same protocol, and the protocol must be one which is supported by the cloud provider.

The feature gate `MixedProtocolLBService` (enabled by default for the kube-apiserver as of v1.24) allows the use of different protocols for LoadBalancer type of Services, when there is more than one port defined.

#### Note:

The set of protocols that can be used for load balanced Services is defined by your cloud provider; they may impose restrictions beyond what the Kubernetes API enforces.

#### Disabling load balancer NodePort allocation

FEATURE STATE:`Kubernetes v1.24 [stable]`

You can optionally disable node port allocation for a Service of `type: LoadBalancer`, by setting the field `spec.allocateLoadBalancerNodePorts` to `false`. This should only be used for load balancer implementations that route traffic directly to pods as opposed to using node ports. By default, `spec.allocateLoadBalancerNodePorts` is `true` and type LoadBalancer Services will continue to allocate node ports. If `spec.allocateLoadBalancerNodePorts` is set to `false` on an existing Service with allocated node ports, those node ports will **not** be de-allocated automatically. You must explicitly remove the `nodePorts` entry in every Service port to de-allocate those node ports.

#### Specifying class of load balancer implementation

FEATURE STATE:`Kubernetes v1.24 [stable]`

For a Service with `type` set to `LoadBalancer`, the `.spec.loadBalancerClass` field enables you to use a load balancer implementation other than the cloud provider default.

By default, `.spec.loadBalancerClass` is not set and a `LoadBalancer` type of Service uses the cloud provider's default load balancer implementation if the cluster is configured with a cloud provider using the `--cloud-provider` component flag.

If you specify `.spec.loadBalancerClass`, it is assumed that a load balancer implementation that matches the specified class is watching for Services. Any default load balancer implementation (for example, the one provided by the cloud provider) will ignore Services that have this field set. `spec.loadBalancerClass` can be set on a Service of type `LoadBalancer` only. Once set, it cannot be changed. The value of `spec.loadBalancerClass` must be a label-style identifier, with an optional prefix such as "`internal-vip`" or "`example.com/internal-vip`". Unprefixed names are reserved for end-users.

#### Load balancer IP address mode

For a Service of `type: LoadBalancer`, a controller can set `.status.loadBalancer.ingress.ipMode`. The `.status.loadBalancer.ingress.ipMode` specifies how the load-balancer IP behaves. It may be specified only when the `.status.loadBalancer.ingress.ip` field is also specified.

There are two possible values for `.status.loadBalancer.ingress.ipMode`: "VIP" and "Proxy". The default value is "VIP" meaning that traffic is delivered to the node with the destination set to the load-balancer's IP and port. There are two cases when setting this to "Proxy", depending on how the load-balancer from the cloud provider delivers the traffics:

*   If the traffic is delivered to the node then DNATed to the pod, the destination would be set to the node's IP and node port;
*   If the traffic is delivered directly to the pod, the destination would be set to the pod's IP and port.

Service implementations may use this information to adjust traffic routing.

#### Internal load balancer

In a mixed environment it is sometimes necessary to route traffic from Services inside the same (virtual) network address block.

In a split-horizon DNS environment you would need two Services to be able to route both external and internal traffic to your endpoints.

To set an internal load balancer, add one of the following annotations to your Service depending on the cloud service provider you're using:

*   [Default](https://kubernetes.io/docs/concepts/services-networking/service/#service-tabs-0)
*   [GCP](https://kubernetes.io/docs/concepts/services-networking/service/#service-tabs-1)
*   [AWS](https://kubernetes.io/docs/concepts/services-networking/service/#service-tabs-2)
*   [Azure](https://kubernetes.io/docs/concepts/services-networking/service/#service-tabs-3)
*   [IBM Cloud](https://kubernetes.io/docs/concepts/services-networking/service/#service-tabs-4)
*   [OpenStack](https://kubernetes.io/docs/concepts/services-networking/service/#service-tabs-5)
*   [Baidu Cloud](https://kubernetes.io/docs/concepts/services-networking/service/#service-tabs-6)
*   [Tencent Cloud](https://kubernetes.io/docs/concepts/services-networking/service/#service-tabs-7)
*   [Alibaba Cloud](https://kubernetes.io/docs/concepts/services-networking/service/#service-tabs-8)
*   [OCI](https://kubernetes.io/docs/concepts/services-networking/service/#service-tabs-9)

Select one of the tabs.

```yaml
metadata:
  name: my-service
  annotations:
    networking.gke.io/load-balancer-type: "Internal"
```

```yaml
metadata:
  name: my-service
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-scheme: "internal"
```

```yaml
metadata:
  name: my-service
  annotations:
    service.beta.kubernetes.io/azure-load-balancer-internal: "true"
```

```yaml
metadata:
  name: my-service
  annotations:
    service.kubernetes.io/ibm-load-balancer-cloud-provider-ip-type: "private"
```

```yaml
metadata:
  name: my-service
  annotations:
    service.beta.kubernetes.io/openstack-internal-load-balancer: "true"
```

```yaml
metadata:
  name: my-service
  annotations:
    service.beta.kubernetes.io/cce-load-balancer-internal-vpc: "true"
```

```yaml
metadata:
  annotations:
    service.kubernetes.io/qcloud-loadbalancer-internal-subnetid: subnet-xxxxx
```

```yaml
metadata:
  annotations:
    service.beta.kubernetes.io/alibaba-cloud-loadbalancer-address-type: "intranet"
```

```yaml
metadata:
  name: my-service
  annotations:
    service.beta.kubernetes.io/oci-load-balancer-internal: true
```

### `type: ExternalName`

Services of type ExternalName map a Service to a DNS name, not to a typical selector such as `my-service` or `cassandra`. You specify these Services with the `spec.externalName` parameter.

This Service definition, for example, maps the `my-service` Service in the `prod` namespace to `my.database.example.com`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
  namespace: prod
spec:
  type: ExternalName
  externalName: my.database.example.com
```

#### Note:

A Service of `type: ExternalName` accepts an IPv4 address string, but treats that string as a DNS name comprised of digits, not as an IP address (the internet does not however allow such names in DNS). Services with external names that resemble IPv4 addresses are not resolved by DNS servers.

If you want to map a Service directly to a specific IP address, consider using [headless Services](https://kubernetes.io/docs/concepts/services-networking/service/#headless-services).

When looking up the host `my-service.prod.svc.cluster.local`, the cluster DNS Service returns a `CNAME` record with the value `my.database.example.com`. Accessing `my-service` works in the same way as other Services but with the crucial difference that redirection happens at the DNS level rather than via proxying or forwarding. Should you later decide to move your database into your cluster, you can start its Pods, add appropriate selectors or endpoints, and change the Service's `type`.

#### Caution:

You may have trouble using ExternalName for some common protocols, including HTTP and HTTPS. If you use ExternalName then the hostname used by clients inside your cluster is different from the name that the ExternalName references.

For protocols that use hostnames this difference may lead to errors or unexpected responses. HTTP requests will have a `Host:` header that the origin server does not recognize; TLS servers will not be able to provide a certificate matching the hostname that the client connected to.

Headless Services
-----------------

Sometimes you don't need load-balancing and a single Service IP. In this case, you can create what are termed _headless Services_, by explicitly specifying `"None"` for the cluster IP address (`.spec.clusterIP`).

You can use a headless Service to interface with other service discovery mechanisms, without being tied to Kubernetes' implementation.

For headless Services, a cluster IP is not allocated, kube-proxy does not handle these Services, and there is no load balancing or proxying done by the platform for them.

A headless Service allows a client to connect to whichever Pod it prefers, directly. Services that are headless don't configure routes and packet forwarding using [virtual IP addresses and proxies](https://kubernetes.io/docs/reference/networking/virtual-ips/); instead, headless Services report the endpoint IP addresses of the individual pods via internal DNS records, served through the cluster's [DNS service](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/). To define a headless Service, you make a Service with `.spec.type` set to ClusterIP (which is also the default for `type`), and you additionally set `.spec.clusterIP` to None.

The string value None is a special case and is not the same as leaving the `.spec.clusterIP` field unset.

How DNS is automatically configured depends on whether the Service has selectors defined:

### With selectors

For headless Services that define selectors, the endpoints controller creates EndpointSlices in the Kubernetes API, and modifies the DNS configuration to return A or AAAA records (IPv4 or IPv6 addresses) that point directly to the Pods backing the Service.

### Without selectors

For headless Services that do not define selectors, the control plane does not create EndpointSlice objects. However, the DNS system looks for and configures either:

*   DNS CNAME records for [`type: ExternalName`](https://kubernetes.io/docs/concepts/services-networking/service/#externalname) Services.
*   DNS A / AAAA records for all IP addresses of the Service's ready endpoints, for all Service types other than `ExternalName`.
    *   For IPv4 endpoints, the DNS system creates A records.
    *   For IPv6 endpoints, the DNS system creates AAAA records.

When you define a headless Service without a selector, the `port` must match the `targetPort`.

Discovering services
--------------------

For clients running inside your cluster, Kubernetes supports two primary modes of finding a Service: environment variables and DNS.

### Environment variables

When a Pod is run on a Node, the kubelet adds a set of environment variables for each active Service. It adds `{SVCNAME}_SERVICE_HOST` and `{SVCNAME}_SERVICE_PORT` variables, where the Service name is upper-cased and dashes are converted to underscores.

For example, the Service `redis-primary` which exposes TCP port 6379 and has been allocated cluster IP address 10.0.0.11, produces the following environment variables:

```shell
REDIS_PRIMARY_SERVICE_HOST=10.0.0.11
REDIS_PRIMARY_SERVICE_PORT=6379
REDIS_PRIMARY_PORT=tcp://10.0.0.11:6379
REDIS_PRIMARY_PORT_6379_TCP=tcp://10.0.0.11:6379
REDIS_PRIMARY_PORT_6379_TCP_PROTO=tcp
REDIS_PRIMARY_PORT_6379_TCP_PORT=6379
REDIS_PRIMARY_PORT_6379_TCP_ADDR=10.0.0.11
```

#### Note:

When you have a Pod that needs to access a Service, and you are using the environment variable method to publish the port and cluster IP to the client Pods, you must create the Service _before_ the client Pods come into existence. Otherwise, those client Pods won't have their environment variables populated.

If you only use DNS to discover the cluster IP for a Service, you don't need to worry about this ordering issue.

Kubernetes also supports and provides variables that are compatible with Docker Engine's "_[legacy container links](https://docs.docker.com/network/links/)_" feature. You can read [`makeLinkVariables`](https://github.com/kubernetes/kubernetes/blob/dd2d12f6dc0e654c15d5db57a5f9f6ba61192726/pkg/kubelet/envvars/envvars.go#L72) to see how this is implemented in Kubernetes.

### DNS

You can (and almost always should) set up a DNS service for your Kubernetes cluster using an [add-on](https://kubernetes.io/docs/concepts/cluster-administration/addons/).

A cluster-aware DNS server, such as CoreDNS, watches the Kubernetes API for new Services and creates a set of DNS records for each one. If DNS has been enabled throughout your cluster then all Pods should automatically be able to resolve Services by their DNS name.

For example, if you have a Service called `my-service` in a Kubernetes namespace `my-ns`, the control plane and the DNS Service acting together create a DNS record for `my-service.my-ns`. Pods in the `my-ns` namespace should be able to find the service by doing a name lookup for `my-service` (`my-service.my-ns` would also work).

Pods in other namespaces must qualify the name as `my-service.my-ns`. These names will resolve to the cluster IP assigned for the Service.

Kubernetes also supports DNS SRV (Service) records for named ports. If the `my-service.my-ns` Service has a port named `http` with the protocol set to `TCP`, you can do a DNS SRV query for `_http._tcp.my-service.my-ns` to discover the port number for `http`, as well as the IP address.

The Kubernetes DNS server is the only way to access `ExternalName` Services. You can find more information about `ExternalName` resolution in [DNS for Services and Pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/).

[[[[[[[Virtual IP addressing mechanism ------------------------------- Read [Virtual IPs and Service Proxies](https://kubernetes.io/docs/reference/networking/virtual-ips/) explains the mechanism Kubernetes provides to expose a Service with a virtual IP address. ### Traffic policies You can set the `.spec.internalTrafficPolicy` and `.spec.externalTrafficPolicy` fields to control how Kubernetes routes traffic to healthy (“ready”) backends. See [Traffic Policies](https://kubernetes.io/docs/reference/networking/virtual-ips/#traffic-policies) for more details. ### Traffic distribution control The `.spec.trafficDistribution` field provides another way to influence traffic routing within a Kubernetes Service. While traffic policies focus on strict semantic guarantees, traffic distribution allows you to express _preferences_ (such as routing to topologically closer endpoints). This can help optimize for performance, cost, or reliability. In Kubernetes 1.35, the following values are supported: `PreferSameZone`Indicates a preference for routing traffic to endpoints that are in the same zone as the client.`PreferSameNode`Indicates a preference for routing traffic to endpoints that are on the same node as the client.`PreferClose` (deprecated)This is an older alias for `PreferSameZone` that is less clear about the semantics. If the field is not set, the implementation will apply its default routing strategy. See [Traffic Distribution](https://kubernetes.io/docs/reference/networking/virtual-ips/#traffic-distribution) for more details ### Session stickiness If you want to make sure that connections from a particular client are passed to the same Pod each time, you can configure session affinity based on the client's IP address. Read [session affinity](https://kubernetes.io/docs/reference/networking/virtual-ips/#session-affinity) to learn more. External IPs ------------ If there are external IPs that route to one or more cluster nodes, Kubernetes Services can be exposed on those `externalIPs`. When network traffic arrives into the cluster, with the external IP (as destination IP) and the port matching that Service, rules and routes that Kubernetes has configured ensure that the traffic is routed to one of the endpoints for that Service. When you define a Service, you can specify `externalIPs` for any [service type](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types). In the example below, the Service named `"my-service"` can be accessed by clients using TCP, on `"198.51.100.32:80"` (calculated from `.spec.externalIPs[]` and `.spec.ports[].port`). ```yaml apiVersion: v1 kind: Service metadata: name: my-service spec: selector: app.kubernetes.io/name: MyApp ports: - name: http protocol: TCP port: 80 targetPort: 49152 externalIPs: - 198.51.100.32 ``` #### Note: Kubernetes does not manage allocation of `externalIPs`; these are the responsibility of the cluster administrator. API Object ---------- Service is a top-level resource in the Kubernetes REST API. You can find more details about the [Service API object](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#service-v1-core). What's next ----------- Learn more about Services and how they fit into Kubernetes: * Follow the [Connecting Applications with Services](https://kubernetes.io/docs/tutorials/services/connect-applications-service/) tutorial. * Read about [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/), which exposes HTTP and HTTPS routes from outside the cluster to Services within your cluster. * Read about [Gateway](https://kubernetes.io/docs/concepts/services-networking/gateway/), an extension to Kubernetes that provides more flexibility than Ingress. For more context, read the following: * [Virtual IPs and Service Proxies](https://kubernetes.io/docs/reference/networking/virtual-ips/) * [EndpointSlices](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/) * [Service API reference](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/) * [EndpointSlice API reference](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/endpoint-slice-v1/) * [Endpoint API reference (legacy)](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/endpoints-v1/)](https://kubernetes.io/docs/concepts/services-networking/service/)](https://kubernetes.io/docs/concepts/services-networking/service/)](https://kubernetes.io/docs/concepts/services-networking/service/)](https://kubernetes.io/docs/concepts/services-networking/service/)](https://kubernetes.io/docs/concepts/services-networking/service/)](https://kubernetes.io/docs/concepts/services-networking/service/)](https://kubernetes.io/docs/concepts/services-networking/service/)

Feedback
--------

Was this page helpful?

Yes No
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).

Last modified January 07, 2026 at 4:12 AM PST: [Fix ordering of Service and Pod in Port definitions example (854aaf863c)](https://github.com/kubernetes/website/commit/854aaf863c572486e8998060294c4d858dc74101)

[Service API reference](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/)[Edit this page](https://github.com/kubernetes/website/edit/main/content/en/docs/concepts/services-networking/service.md)[Create child page](https://github.com/kubernetes/website/new/main/content/en/docs/concepts/services-networking/service.md?filename=change-me.md&value=---%0Atitle%3A+%22Long+Page+Title%22%0AlinkTitle%3A+%22Short+Nav+Title%22%0Aweight%3A+100%0Adescription%3A+%3E-%0A+++++Page+description+for+heading+and+indexes.%0A---%0A%0A%23%23+Heading%0A%0AEdit+this+template+to+create+your+new+page.%0A%0A%2A+Give+it+a+good+name%2C+ending+in+%60.md%60+-+e.g.+%60getting-started.md%60%0A%2A+Edit+the+%22front+matter%22+section+at+the+top+of+the+page+%28weight+controls+how+its+ordered+amongst+other+pages+in+the+same+directory%3B+lowest+number+first%29.%0A%2A+Add+a+good+commit+message+at+the+bottom+of+the+page+%28%3C80+characters%3B+use+the+extended+description+field+for+more+detail%29.%0A%2A+Create+a+new+branch+so+you+can+preview+your+new+file+and+request+a+review+via+Pull+Request.%0A)[Create an issue](https://github.com/kubernetes/website/issues/new?title=Service)[Print entire section](https://kubernetes.io/docs/concepts/services-networking/_print/)

*   [Services in Kubernetes](https://kubernetes.io/docs/concepts/services-networking/service/#services-in-kubernetes)
    *   [Cloud-native service discovery](https://kubernetes.io/docs/concepts/services-networking/service/#cloud-native-service-discovery)

*   [Defining a Service](https://kubernetes.io/docs/concepts/services-networking/service/#defining-a-service)
    *   [Relaxed naming requirements for Service objects](https://kubernetes.io/docs/concepts/services-networking/service/#relaxed-naming-requirements-for-service-objects)
    *   [Port definitions](https://kubernetes.io/docs/concepts/services-networking/service/#field-spec-ports)
    *   [Services without selectors](https://kubernetes.io/docs/concepts/services-networking/service/#services-without-selectors)
    *   [EndpointSlices](https://kubernetes.io/docs/concepts/services-networking/service/#endpointslices)
    *   [Endpoints (deprecated)](https://kubernetes.io/docs/concepts/services-networking/service/#endpoints)
    *   [Application protocol](https://kubernetes.io/docs/concepts/services-networking/service/#application-protocol)
    *   [Multi-port Services](https://kubernetes.io/docs/concepts/services-networking/service/#multi-port-services)

*   [Service type](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types)
    *   [`type: ClusterIP`](https://kubernetes.io/docs/concepts/services-networking/service/#type-clusterip)
    *   [`type: NodePort`](https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport)
    *   [`type: LoadBalancer`](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer)
    *   [`type: ExternalName`](https://kubernetes.io/docs/concepts/services-networking/service/#externalname)

*   [Headless Services](https://kubernetes.io/docs/concepts/services-networking/service/#headless-services)
    *   [With selectors](https://kubernetes.io/docs/concepts/services-networking/service/#with-selectors)
    *   [Without selectors](https://kubernetes.io/docs/concepts/services-networking/service/#without-selectors)

*   [Discovering services](https://kubernetes.io/docs/concepts/services-networking/service/#discovering-services)
    *   [Environment variables](https://kubernetes.io/docs/concepts/services-networking/service/#environment-variables)
    *   [DNS](https://kubernetes.io/docs/concepts/services-networking/service/#dns)

*   [Virtual IP addressing mechanism](https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ip-addressing-mechanism)
    *   [Traffic policies](https://kubernetes.io/docs/concepts/services-networking/service/#traffic-policies)
    *   [Traffic distribution control](https://kubernetes.io/docs/concepts/services-networking/service/#traffic-distribution)
    *   [Session stickiness](https://kubernetes.io/docs/concepts/services-networking/service/#session-stickiness)

*   [External IPs](https://kubernetes.io/docs/concepts/services-networking/service/#external-ips)
*   [API Object](https://kubernetes.io/docs/concepts/services-networking/service/#api-object)
*   [What's next](https://kubernetes.io/docs/concepts/services-networking/service/#what-s-next)

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
