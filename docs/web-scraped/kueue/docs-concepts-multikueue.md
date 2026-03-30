# Source: https://kueue.sigs.k8s.io/docs/concepts/multikueue/

Title: MultiKueue

URL Source: https://kueue.sigs.k8s.io/docs/concepts/multikueue/

Published Time: 2024-11-11T00:00:00+00:00

Markdown Content:
MultiKueue | Kueue
===============
[Kueue](https://kueue.sigs.k8s.io/)

*   [Documentation](https://kueue.sigs.k8s.io/docs/)
*   [Talks and presentations](https://kueue.sigs.k8s.io/docs/talks_and_presentations/)
*   [Adopters](https://kueue.sigs.k8s.io/docs/adopters/)
*   [GitHub](https://github.com/kubernetes-sigs/kueue)
*   [English](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#)[简体中文](https://kueue.sigs.k8s.io/zh-cn/docs/concepts/multikueue/) 

[English](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#)

[简体中文](https://kueue.sigs.k8s.io/zh-cn/docs/concepts/multikueue/)

*   [Documentation](https://kueue.sigs.k8s.io/docs/)
    *   - [x] [Overview](https://kueue.sigs.k8s.io/docs/overview/) 
    *   - [x] [Installation](https://kueue.sigs.k8s.io/docs/installation/) 
    *   - [x] [Concepts](https://kueue.sigs.k8s.io/docs/concepts/) 
        *   - [x] [Resource Flavor](https://kueue.sigs.k8s.io/docs/concepts/resource_flavor/) 
        *   - [x] [Cluster Queue](https://kueue.sigs.k8s.io/docs/concepts/cluster_queue/) 
        *   - [x] [Cohort](https://kueue.sigs.k8s.io/docs/concepts/cohort/) 
        *   - [x] [Elastic Workloads](https://kueue.sigs.k8s.io/docs/concepts/elastic_workload/) 
        *   - [x] [Local Queue](https://kueue.sigs.k8s.io/docs/concepts/local_queue/) 
        *   - [x] [Workload](https://kueue.sigs.k8s.io/docs/concepts/workload/) 
        *   - [x] [Topology](https://kueue.sigs.k8s.io/docs/concepts/topology/) 
        *   - [x] [Admission Fair Sharing](https://kueue.sigs.k8s.io/docs/concepts/admission_fair_sharing/) 
        *   - [x] [Fair Sharing](https://kueue.sigs.k8s.io/docs/concepts/fair_sharing/) 
        *   - [x] [Admission Check](https://kueue.sigs.k8s.io/docs/concepts/admission_check/) 
            *   - [x] [ProvisioningRequest](https://kueue.sigs.k8s.io/docs/concepts/admission_check/provisioning_request/) 
            *   - [x] [Multikueue](https://kueue.sigs.k8s.io/docs/concepts/admission_check/multikueue/) 

        *   - [x] [Topology Aware Scheduling](https://kueue.sigs.k8s.io/docs/concepts/topology_aware_scheduling/) 
        *   - [x] [Workload Priority Class](https://kueue.sigs.k8s.io/docs/concepts/workload_priority_class/) 
        *   - [x] [Preemption](https://kueue.sigs.k8s.io/docs/concepts/preemption/) 
        *   - [x] [MultiKueue](https://kueue.sigs.k8s.io/docs/concepts/multikueue/) 
        *   - [x] [Admission](https://kueue.sigs.k8s.io/docs/concepts/admission/) 

    *   - [x] [Tasks](https://kueue.sigs.k8s.io/docs/tasks/) 
        *   - [x] [Manage Kueue](https://kueue.sigs.k8s.io/docs/tasks/manage/) 
            *   - [x] [Productionization of Kueue](https://kueue.sigs.k8s.io/docs/tasks/manage/productization/) 
                *   - [x] [Configure external cert-manager](https://kueue.sigs.k8s.io/docs/tasks/manage/productization/cert_manager/) 
                *   - [x] [Configure Prometheus with TLS](https://kueue.sigs.k8s.io/docs/tasks/manage/productization/prometheus/) 

            *   - [x] [Enforce Kueue Management of Workloads](https://kueue.sigs.k8s.io/docs/tasks/manage/enforce_job_management/) 
                *   - [x] [Setup default LocalQueue](https://kueue.sigs.k8s.io/docs/tasks/manage/enforce_job_management/setup_default_local_queue/) 
                *   - [x] [Setup a Job Admission Policy](https://kueue.sigs.k8s.io/docs/tasks/manage/enforce_job_management/setup_job_admission_policy/) 
                *   - [x] [Setup manageJobsWithoutQueueName](https://kueue.sigs.k8s.io/docs/tasks/manage/enforce_job_management/manage_jobs_without_queue_name/) 
                *   - [x] [Opt-in Namespace Management](https://kueue.sigs.k8s.io/docs/tasks/manage/enforce_job_management/opt_in_namespace_management/) 

            *   - [x] [Setup RBAC](https://kueue.sigs.k8s.io/docs/tasks/manage/rbac/) 
            *   - [x] [Administer Cluster Quotas](https://kueue.sigs.k8s.io/docs/tasks/manage/administer_cluster_quotas/) 
            *   - [x] [Share Quotas](https://kueue.sigs.k8s.io/docs/tasks/manage/share_quotas_across_flavors/ "Share Quotas Across Resource Flavors") 
            *   - [x] [Monitor pending Workloads](https://kueue.sigs.k8s.io/docs/tasks/manage/monitor_pending_workloads/) 
                *   - [x] [Pending Workloads on-demand](https://kueue.sigs.k8s.io/docs/tasks/manage/monitor_pending_workloads/pending_workloads_on_demand/) 
                *   - [x] [Pending Workloads in Grafana](https://kueue.sigs.k8s.io/docs/tasks/manage/monitor_pending_workloads/pending_workloads_in_grafana/) 

            *   - [x] [Run job with WorkloadPriority](https://kueue.sigs.k8s.io/docs/tasks/manage/run_job_with_workload_priority/) 
            *   - [x] [Observability](https://kueue.sigs.k8s.io/docs/tasks/manage/observability/) 
                *   - [x] [Setup Prometheus](https://kueue.sigs.k8s.io/docs/tasks/manage/observability/setup_prometheus/) 
                *   - [x] [Common Grafana Queries](https://kueue.sigs.k8s.io/docs/tasks/manage/observability/common_grafana_queries/) 

            *   - [x] [Setup All-or-nothing with ready Pods](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_wait_for_pods_ready/) 
            *   - [x] [Setup a MultiKueue environment](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/) 
            *   - [x] [Setup garbage-collection of workload](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_object_retention_policy/) 
            *   - [x] [Setup failure recovery](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_failure_recovery/) 
            *   - [x] [Enable KueueViz](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/) 

        *   - [x] [Run Workloads](https://kueue.sigs.k8s.io/docs/tasks/run/) 
            *   - [x] [Kubernetes Jobs](https://kueue.sigs.k8s.io/docs/tasks/run/jobs/ "Run A Kubernetes Job") 
            *   - [x] [Kubernetes CronJobs](https://kueue.sigs.k8s.io/docs/tasks/run/run_cronjobs/ "Run A CronJob") 
            *   - [x] [HAMi vGPU](https://kueue.sigs.k8s.io/docs/tasks/run/using_hami/ "Using HAMi") 
            *   - [x] [LeaderWorkerSet](https://kueue.sigs.k8s.io/docs/tasks/run/leaderworkerset/ "Run LeaderWorkerSet") 
            *   - [x] [AppWrappers](https://kueue.sigs.k8s.io/docs/tasks/run/appwrappers/ "Run An AppWrapper") 
            *   - [x] [TrainJobs](https://kueue.sigs.k8s.io/docs/tasks/run/trainjobs/ "Run A TrainJob") 
            *   - [x] [Deployment](https://kueue.sigs.k8s.io/docs/tasks/run/deployment/ "Run Deployment") 
            *   - [x] [StatefulSet](https://kueue.sigs.k8s.io/docs/tasks/run/statefulset/ "Run StatefulSet") 
            *   - [x] [Plain Pods](https://kueue.sigs.k8s.io/docs/tasks/run/plain_pods/ "Run Plain Pods") 
            *   - [x] [Kubeflow Jobs (v1)](https://kueue.sigs.k8s.io/docs/tasks/run/kubeflow/) 
                *   - [x] [Run a JAXJob](https://kueue.sigs.k8s.io/docs/tasks/run/kubeflow/jaxjobs/) 
                *   - [x] [Run a PaddleJob](https://kueue.sigs.k8s.io/docs/tasks/run/kubeflow/paddlejobs/) 
                *   - [x] [Run a XGBoostJob](https://kueue.sigs.k8s.io/docs/tasks/run/kubeflow/xgboostjobs/) 
                *   - [x] [Run a TFJob](https://kueue.sigs.k8s.io/docs/tasks/run/kubeflow/tfjobs/) 
                *   - [x] [Run a PyTorchJob](https://kueue.sigs.k8s.io/docs/tasks/run/kubeflow/pytorchjobs/) 
                *   - [x] [Run a MPIJob](https://kueue.sigs.k8s.io/docs/tasks/run/kubeflow/mpijobs/) 

            *   - [x] [Python](https://kueue.sigs.k8s.io/docs/tasks/run/python_jobs/ "Run Jobs Using Python") 
            *   - [x] [Jobsets](https://kueue.sigs.k8s.io/docs/tasks/run/jobsets/ "Run A JobSet") 
            *   - [x] [Multi-Cluster](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/ "Multi-Cluster Job dispatching") 
                *   - [x] [Deployment](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/deployment/ "Run Deployment in Multi-Cluster") 
                *   - [x] [Plain Pod](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/plain_pods/ "Run Plain Pod in Multi-Cluster") 
                *   - [x] [StatefulSet](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/statefulset/ "Run StatefulSet in Multi-Cluster") 
                *   - [x] [Kubernetes Job](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/job/ "Run Kubernetes Job in Multi-Cluster") 
                *   - [x] [TrainJob](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/trainjob/ "Run TrainJobs in Multi-Cluster") 
                *   - [x] [AppWrappers](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/appwrapper/ "Run AppWrappers in Multi-Cluster") 
                *   - [x] [Jobsets](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/jobsets/ "Run Jobsets in Multi-Cluster") 
                *   - [x] [KubeRay](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/kuberay/ "Run KubeRay Jobs in Multi-Cluster") 
                *   - [x] [Kubeflow (v1)](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/kubeflow/ "Run Kubeflow Jobs (v1) in Multi-Cluster") 
                *   - [x] [External Framework Jobs](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/external-frameworks/ "Run External Framework Jobs in Multi-Cluster") 
                *   - [x] [MPIJob](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/mpijob/ "Run MPIJobs in Multi-Cluster") 

            *   - [x] [External Frameworks](https://kueue.sigs.k8s.io/docs/tasks/run/external_workloads/ "Supporting External Frameworks") 
                *   - [x] [Custom Workload](https://kueue.sigs.k8s.io/docs/tasks/run/external_workloads/wrapped_custom_workload/ "Run A Wrapped Custom Workload") 
                *   - [x] [Flux MiniClusters](https://kueue.sigs.k8s.io/docs/tasks/run/external_workloads/flux_miniclusters/ "Run A Flux MiniCluster") 
                *   - [x] [Argo Workflow](https://kueue.sigs.k8s.io/docs/tasks/run/external_workloads/argo_workflow/ "Run An Argo Workflow") 
                *   - [x] [Tekton Pipeline](https://kueue.sigs.k8s.io/docs/tasks/run/external_workloads/tektoncd/ "Run A Tekton Pipeline") 

            *   - [x] [RayServices](https://kueue.sigs.k8s.io/docs/tasks/run/rayservices/ "Run A RayService") 
            *   - [x] [RayClusters](https://kueue.sigs.k8s.io/docs/tasks/run/rayclusters/ "Run A RayCluster") 
            *   - [x] [RayJobs](https://kueue.sigs.k8s.io/docs/tasks/run/rayjobs/ "Run A RayJob") 

        *   - [x] [Developer Tools](https://kueue.sigs.k8s.io/docs/tasks/dev/) 
            *   - [x] [Enabling pprof endpoints](https://kueue.sigs.k8s.io/docs/tasks/dev/enabling_pprof_endpoints/) 
            *   - [x] [Setup Dev Monitoring](https://kueue.sigs.k8s.io/docs/tasks/dev/setup_dev_monitoring/) 
            *   - [x] [Setup MultiKueue Development Environment](https://kueue.sigs.k8s.io/docs/tasks/dev/setup_multikueue_development_environment/) 
            *   - [x] [External Frameworks](https://kueue.sigs.k8s.io/docs/tasks/dev/external_frameworks/) 
            *   - [x] [Integrate a custom Job with Kueue](https://kueue.sigs.k8s.io/docs/tasks/dev/integrate_a_custom_job/) 
            *   - [x] [Develop an AdmissionCheck Controller](https://kueue.sigs.k8s.io/docs/tasks/dev/develop-acc/) 

        *   - [x] [Troubleshooting](https://kueue.sigs.k8s.io/docs/tasks/troubleshooting/) 
            *   - [x] [Troubleshooting Jobs](https://kueue.sigs.k8s.io/docs/tasks/troubleshooting/troubleshooting_jobs/) 
            *   - [x] [Troubleshooting Queues](https://kueue.sigs.k8s.io/docs/tasks/troubleshooting/troubleshooting_queues/) 
            *   - [x] [Troubleshooting Provisioning Request in Kueue](https://kueue.sigs.k8s.io/docs/tasks/troubleshooting/troubleshooting_provreq/) 
            *   - [x] [Troubleshooting Pods](https://kueue.sigs.k8s.io/docs/tasks/troubleshooting/troubleshooting_pods/) 
            *   - [x] [Troubleshooting delete ClusterQueue](https://kueue.sigs.k8s.io/docs/tasks/troubleshooting/troubleshooting_delete_clusterqueue/) 

    *   - [x] [Reference](https://kueue.sigs.k8s.io/docs/reference/) 
        *   - [x] [Kubectl Kueue Plugin](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/) 
            *   - [x] [Installation](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/installation/) 
            *   - [x] [Commands](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/) 
                *   - [x] [kueuectl](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl/) 
                *   - [x] [kueuectl create](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_create/) 
                    *   - [x] [kueuectl create clusterqueue](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_create/kueuectl_create_clusterqueue/) 
                    *   - [x] [kueuectl create localqueue](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_create/kueuectl_create_localqueue/) 
                    *   - [x] [kueuectl create resourceflavor](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_create/kueuectl_create_resourceflavor/) 

                *   - [x] [kueuectl delete](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_delete/) 
                    *   - [x] [kueuectl delete clusterqueue](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_delete/kueuectl_delete_clusterqueue/) 
                    *   - [x] [kueuectl delete localqueue](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_delete/kueuectl_delete_localqueue/) 
                    *   - [x] [kueuectl delete resourceflavor](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_delete/kueuectl_delete_resourceflavor/) 
                    *   - [x] [kueuectl delete workload](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_delete/kueuectl_delete_workload/) 

                *   - [x] [kueuectl describe](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_describe/) 
                    *   - [x] [kueuectl describe clusterqueue](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_describe/kueuectl_describe_clusterqueue/) 
                    *   - [x] [kueuectl describe localqueue](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_describe/kueuectl_describe_localqueue/) 
                    *   - [x] [kueuectl describe resourceflavor](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_describe/kueuectl_describe_resourceflavor/) 
                    *   - [x] [kueuectl describe workload](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_describe/kueuectl_describe_workload/) 

                *   - [x] [kueuectl edit](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_edit/) 
                    *   - [x] [kueuectl edit clusterqueue](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_edit/kueuectl_edit_clusterqueue/) 
                    *   - [x] [kueuectl edit localqueue](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_edit/kueuectl_edit_localqueue/) 
                    *   - [x] [kueuectl edit resourceflavor](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_edit/kueuectl_edit_resourceflavor/) 
                    *   - [x] [kueuectl edit workload](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_edit/kueuectl_edit_workload/) 

                *   - [x] [kueuectl get](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_get/) 
                    *   - [x] [kueuectl get clusterqueue](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_get/kueuectl_get_clusterqueue/) 
                    *   - [x] [kueuectl get localqueue](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_get/kueuectl_get_localqueue/) 
                    *   - [x] [kueuectl get resourceflavor](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_get/kueuectl_get_resourceflavor/) 
                    *   - [x] [kueuectl get workload](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_get/kueuectl_get_workload/) 

                *   - [x] [kueuectl list](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_list/) 
                    *   - [x] [kueuectl list clusterqueue](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_list/kueuectl_list_clusterqueue/) 
                    *   - [x] [kueuectl list localqueue](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_list/kueuectl_list_localqueue/) 
                    *   - [x] [kueuectl list pods](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_list/kueuectl_list_pods/) 
                    *   - [x] [kueuectl list resourceflavor](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_list/kueuectl_list_resourceflavor/) 
                    *   - [x] [kueuectl list workload](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_list/kueuectl_list_workload/) 

                *   - [x] [kueuectl patch](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_patch/) 
                    *   - [x] [kueuectl patch clusterqueue](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_patch/kueuectl_patch_clusterqueue/) 
                    *   - [x] [kueuectl patch localqueue](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_patch/kueuectl_patch_localqueue/) 
                    *   - [x] [kueuectl patch resourceflavor](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_patch/kueuectl_patch_resourceflavor/) 
                    *   - [x] [kueuectl patch workload](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_patch/kueuectl_patch_workload/) 

                *   - [x] [kueuectl resume](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_resume/) 
                    *   - [x] [kueuectl resume clusterqueue](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_resume/kueuectl_resume_clusterqueue/) 
                    *   - [x] [kueuectl resume localqueue](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_resume/kueuectl_resume_localqueue/) 
                    *   - [x] [kueuectl resume workload](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_resume/kueuectl_resume_workload/) 

                *   - [x] [kueuectl stop](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_stop/) 
                    *   - [x] [kueuectl stop clusterqueue](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_stop/kueuectl_stop_clusterqueue/) 
                    *   - [x] [kueuectl stop localqueue](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_stop/kueuectl_stop_localqueue/) 
                    *   - [x] [kueuectl stop workload](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_stop/kueuectl_stop_workload/) 

                *   - [x] [kueuectl version](https://kueue.sigs.k8s.io/docs/reference/kubectl-kueue/commands/kueuectl_version/) 

        *   - [x] [Component tools](https://kueue.sigs.k8s.io/docs/reference/components-tools/) 
            *   - [x] [Feature Gates (removed)](https://kueue.sigs.k8s.io/docs/reference/components-tools/feature-gate-removed/) 

        *   - [x] [Labels and Annotations](https://kueue.sigs.k8s.io/docs/reference/labels-and-annotations/) 
        *   - [x] [Prometheus Metrics](https://kueue.sigs.k8s.io/docs/reference/metrics/) 
        *   - [x] [Kueue Configuration v1beta1 API](https://kueue.sigs.k8s.io/docs/reference/kueue-config.v1beta1/) 
        *   - [x] [Kueue Configuration v1beta2 API](https://kueue.sigs.k8s.io/docs/reference/kueue-config.v1beta2/) 
        *   - [x] [Kueue v1beta1 API](https://kueue.sigs.k8s.io/docs/reference/kueue.v1beta1/) 
        *   - [x] [Kueue v1beta2 API](https://kueue.sigs.k8s.io/docs/reference/kueue.v1beta2/) 

    *   - [x] [Talks and presentations](https://kueue.sigs.k8s.io/docs/talks_and_presentations/) 
    *   - [x] [Contribution Guidelines](https://kueue.sigs.k8s.io/docs/contribution_guidelines/) 
        *   - [x] [Running tests](https://kueue.sigs.k8s.io/docs/contribution_guidelines/testing/ "Running and debugging tests") 

    *   - [x] [Adopters](https://kueue.sigs.k8s.io/docs/adopters/) 

[View this page](https://github.com/kubernetes-sigs/kueue/tree/main/site/content/en/docs/concepts/multikueue.md)[Edit this page](https://github.com/kubernetes-sigs/kueue/edit/main/site/content/en/docs/concepts/multikueue.md)[Create child page](https://github.com/kubernetes-sigs/kueue/new/main/site/content/en/docs/concepts?filename=change-me.md&value=---%0Atitle%3A+%22Long+Page+Title%22%0AlinkTitle%3A+%22Short+Nav+Title%22%0Aweight%3A+100%0Adescription%3A+%3E-%0A+++++Page+description+for+heading+and+indexes.%0A---%0A%0A%23%23+Heading%0A%0AEdit+this+template+to+create+your+new+page.%0A%0A%2A+Give+it+a+good+name%2C+ending+in+%60.md%60+-+e.g.+%60getting-started.md%60%0A%2A+Edit+the+%22front+matter%22+section+at+the+top+of+the+page+%28weight+controls+how+its+ordered+amongst+other+pages+in+the+same+directory%3B+lowest+number+first%29.%0A%2A+Add+a+good+commit+message+at+the+bottom+of+the+page+%28%3C80+characters%3B+use+the+extended+description+field+for+more+detail%29.%0A%2A+Create+a+new+branch+so+you+can+preview+your+new+file+and+request+a+review+via+Pull+Request.%0A)[Create issue](https://github.com/kubernetes-sigs/kueue/issues/new?title=MultiKueue)[Create project issue](https://github.com/kubernetes-sigs/kueue/issues/new)

*   [Cluster Roles](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#cluster-roles)
    *   [Manager Cluster](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#manager-cluster)
    *   [Worker Cluster](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#worker-cluster)
    *   [Using manager to run workloads](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#using-manager-to-run-workloads)

*   [Job Flow](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#job-flow)
*   [Workload Dispatching](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#workload-dispatching)
    *   [AllAtOnce (Default Mode):](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#allatonce-default-mode)
    *   [Incremental:](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#incremental)
    *   [External (Custom implementation):](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#external-custom-implementation)

*   [Supported Job Types](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#supported-job-types)
*   [Submitting Jobs](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#submitting-jobs)
*   [What’s Next?](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#whats-next)
*   [Limitation](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#limitation)

1.   [Documentation](https://kueue.sigs.k8s.io/docs/)
2.   [Concepts](https://kueue.sigs.k8s.io/docs/concepts/)
3.   MultiKueue

MultiKueue
==========

Multi-cluster job dispatching with Kueue.

Feature state beta since Kueue v0.9

#### Note

`MultiKueue` is currently a beta feature and is enabled by default.

You can disable it by editing the `MultiKueue` feature gate. Refer to the [Installation guide](https://kueue.sigs.k8s.io/docs/installation/#change-the-feature-gates-configuration) for instructions on configuring feature gates.

A MultiKueue setup is composed of a manager cluster and at least one worker cluster.

Cluster Roles [](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#cluster-roles)
-----------------------------------------------------------------------------------

### Manager Cluster [](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#manager-cluster)

The manager cluster is responsible for:

*   Establishing and maintaining connections with worker clusters.
*   Creating and monitoring remote objects (Workloads or Jobs) while keeping the local ones in sync.

The **MultiKueue Admission Check Controller** runs in the manager cluster. It maintains the `Active` status of AdmissionChecks managed by MultiKueue.

The quota set for the flavors of a ClusterQueue determines how many jobs are eligible for dispatching at a given time. Ideally, the quota in the manager cluster should equal the total quota available in all worker clusters:

*   If the manager’s quota is **significantly lower**, worker clusters may remain underutilized.
*   If the manager’s quota is **significantly higher**, it may dispatch and monitor workloads that are unlikely to be admitted in the worker clusters.

### Worker Cluster [](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#worker-cluster)

The worker cluster acts like a standalone Kueue cluster. The **MultiKueue Admission Check Controller**, running in the manager cluster, creates and deletes Workloads and Jobs in the worker clusters as needed.

### Using manager to run workloads [](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#using-manager-to-run-workloads)

MultiKueue supports running regular Jobs regular Jobs on the manager when using a dedicated ClusterQueue. However, we do not support currently role sharing where the manager cluster is also one of workers for itself, see [limitations](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#limitations)

Job Flow [](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#job-flow)
-------------------------------------------------------------------------

To enable multi-cluster dispatching, you need to assign a Job to a ClusterQueue configured with a MultiKueue `AdmissionCheck`.

The dispatching flow works as follows:

1.   When the Job’s Workload obtains a `QuotaReservation` in the manager cluster, the dispatcher determines the worker clusters where the Workload should be created. Depending on the configured dispatching algorithm (e.g., AllAtOnce, Incremental, or a custom approach), the Workload may be created in all configured worker clusters or in a subset of them.
2.   When a worker cluster admits one of these remote Workloads:
    *   The manager deletes the Workloads from the other clusters.
    *   The manager creates a copy of the Job in the selected worker cluster and labels it with `kueue.x-k8s.io/prebuilt-workload-name` to link it to the admitted Workload.

3.   The manager monitors the remote Workload and Job, and synchronizes their status with the corresponding local objects.
4.   Once the remote Workload is marked `Finished`:
    *   The manager performs a final status sync.
    *   It then deletes the corresponding objects from the worker cluster.

Feature state beta since Kueue v0.16

#### Note

By default, Workloads are only deleted from non-selected worker clusters after a Workload is fully admitted (quota reserved AND all admission checks satisfied). This allows parallel ProvisioningRequests across worker clusters. To revert to the previous behavior where Workloads are deleted immediately upon quota reservation, disable the `MultiKueueWaitForWorkloadAdmitted` feature gate.

Workload Dispatching [](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#workload-dispatching)
-------------------------------------------------------------------------------------------------

#### Note

The MultiKueue Dispatcher mechanism is available since Kueue v0.13.

Provides a flexible way to control how workloads are distributed across worker clusters by allowing users to choose between built-in dispatching algorithms or implement custom ones. This mechanism ensures efficient workload placement while minimizing resource contention and preemptions across clusters.
The `status.nominatedClusterNames` field lists the worker clusters currently being considered for scheduling the Workload, as determined by the dispatching algorithm, and is updated while the Workload is pending admission.

The `status.clusterName` field specifies the worker cluster where the Workload has been successfully admitted. Once the field is set, it becomes immutable and the `status.nominatedClusterNames` field is reset, and it is no longer possible to set it.

This ensures that the Workload’s cluster assignment is finalized and prevents further nomination of clusters.

### AllAtOnce (Default Mode): [](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#allatonce-default-mode)

In this mode, the Workload is copied to all available worker clusters as soon as it obtains a QuotaReservation in the manager cluster. This approach ensures the fastest possible admission by allowing all clusters to compete for the Workload simultaneously.

### Incremental: [](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#incremental)

This mode introduces a gradual dispatching strategy where clusters are nominated in rounds. Initially, all worker clusters are sorted in dictionary order, and a subset of up to 3 clusters is selected from the sorted list. The Workload is copied only to these nominated clusters. If none of the nominated clusters admit the Workload within a fixed duration (5 minutes), an additional up to 3 clusters are incrementally added in subsequent rounds, following the same dictionary order.

### External (Custom implementation): [](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#external-custom-implementation)

In this mode, the selection of worker clusters is delegated to an external controller. The external controller is responsible for setting the `.status.nominatedClusterNames` field in the Workload to specify the clusters where it should be copied.

The MultiKueue Workload Controller synchronizes the Workload with the nominated clusters.

Known Limitation:

#### Warning

For the external controller to patch the `.status.nominatedClusterNames` field there are 2 options:

*   Use the `kueue-admission` field manager, because the kueue-admission field manager is responsible for managing updates to the `.status.nominatedClusterNames` field.
*   [Enable `WorkloadRequestUseMergePatch` feature gate](https://kueue.sigs.k8s.io/docs/concepts/workload/#workload-updates-by-kueue) that drops the `kueue-admission` field manager from the `.status.nominatedClusterNames`.

Without this, the Kueue is not able to admit the MultiKueue workloads.

Supported Job Types [](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#supported-job-types)
-----------------------------------------------------------------------------------------------

MultiKueue supports a wide variety of workloads. You can learn how to:

*   [Dispatch a Kueue managed Deployment](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/deployment/).
*   [Dispatch a Kueue managed batch/Job](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/job/).
*   [Dispatch a Kueue managed JobSet](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/jobsets/).
*   [Dispatch a Kueue managed Kubeflow Jobs](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/kubeflow/).
*   [Dispatch a Kueue managed KubeRay workloads](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/kuberay/).
*   [Dispatch a Kueue managed MPIJob](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/mpijob/).
*   [Dispatch a Kueue managed AppWrapper](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/appwrapper/).
*   [Dispatch a Kueue managed plain Pod](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/plain_pods/).
*   [Dispatch a Kueue managed StatefulSet](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/statefulset/).
*   [Dispatch a Kueue managed External Framework Job](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/external-frameworks/)

Submitting Jobs [](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#submitting-jobs)
---------------------------------------------------------------------------------------

In a [properly configured MultiKueue environment](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/), you can submit any supported Job to the **manager cluster**, targeting a ClusterQueue configured for MultiKueue.

Kueue handles delegation to the appropriate worker cluster without requiring any additional changes to your job specification.

What’s Next? [](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#whats-next)
-------------------------------------------------------------------------------

*   [Set up a MultiKueue environment](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/)
*   [Run Jobs in a MultiKueue environment](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/)

Limitation [](https://kueue.sigs.k8s.io/docs/concepts/multikueue/#limitation)
-----------------------------------------------------------------------------

*   we do not support currently running manager cluster as one of workers for itself.

Feedback
--------

Was this page helpful?

Yes No
Glad to hear it! Please [tell us how we can improve](https://github.com/kubernetes-sigs/kueue/issues/new).

Sorry to hear that. Please [tell us how we can improve](https://github.com/kubernetes-sigs/kueue/issues/new).

Last modified January 22, 2026: [Add documentation for manager cluster to run workloads (#8747) (874199560)](https://github.com/kubernetes-sigs/kueue/commit/874199560e71b1af76815e8649a48d3c9f447082)

*   [](https://groups.google.com/a/kubernetes.io/g/wg-batch)
*   [](https://twitter.com/kubernetesio)
*   [](https://stackoverflow.com/questions/tagged/kubernetes)
*   [](https://kubernetes.slack.com/messages/wg-batch)

© 2026 The Kubernetes Authors | Documentation Distributed under CC BY 4.0

© The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage page](https://www.linuxfoundation.org/legal/trademark-usage).
