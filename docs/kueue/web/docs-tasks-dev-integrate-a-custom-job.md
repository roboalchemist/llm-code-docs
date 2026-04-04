# Source: https://kueue.sigs.k8s.io/docs/tasks/dev/integrate_a_custom_job/

Title: Integrate a custom Job with Kueue

URL Source: https://kueue.sigs.k8s.io/docs/tasks/dev/integrate_a_custom_job/

Published Time: 2023-07-25T00:00:00+00:00

Markdown Content:
Integrate a custom Job with Kueue | Kueue
===============
[Kueue](https://kueue.sigs.k8s.io/)

*   [Documentation](https://kueue.sigs.k8s.io/docs/)
*   [Talks and presentations](https://kueue.sigs.k8s.io/docs/talks_and_presentations/)
*   [Adopters](https://kueue.sigs.k8s.io/docs/adopters/)
*   [GitHub](https://github.com/kubernetes-sigs/kueue)
*   [English](https://kueue.sigs.k8s.io/docs/tasks/dev/integrate_a_custom_job/#)[简体中文](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/dev/integrate_a_custom_job/) 

[English](https://kueue.sigs.k8s.io/docs/tasks/dev/integrate_a_custom_job/#)

[简体中文](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/dev/integrate_a_custom_job/)

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

[View this page](https://github.com/kubernetes-sigs/kueue/tree/main/site/content/en/docs/tasks/dev/integrate_a_custom_job.md)[Edit this page](https://github.com/kubernetes-sigs/kueue/edit/main/site/content/en/docs/tasks/dev/integrate_a_custom_job.md)[Create child page](https://github.com/kubernetes-sigs/kueue/new/main/site/content/en/docs/tasks/dev?filename=change-me.md&value=---%0Atitle%3A+%22Long+Page+Title%22%0AlinkTitle%3A+%22Short+Nav+Title%22%0Aweight%3A+100%0Adescription%3A+%3E-%0A+++++Page+description+for+heading+and+indexes.%0A---%0A%0A%23%23+Heading%0A%0AEdit+this+template+to+create+your+new+page.%0A%0A%2A+Give+it+a+good+name%2C+ending+in+%60.md%60+-+e.g.+%60getting-started.md%60%0A%2A+Edit+the+%22front+matter%22+section+at+the+top+of+the+page+%28weight+controls+how+its+ordered+amongst+other+pages+in+the+same+directory%3B+lowest+number+first%29.%0A%2A+Add+a+good+commit+message+at+the+bottom+of+the+page+%28%3C80+characters%3B+use+the+extended+description+field+for+more+detail%29.%0A%2A+Create+a+new+branch+so+you+can+preview+your+new+file+and+request+a+review+via+Pull+Request.%0A)[Create issue](https://github.com/kubernetes-sigs/kueue/issues/new?title=Integrate%20a%20custom%20Job%20with%20Kueue)[Create project issue](https://github.com/kubernetes-sigs/kueue/issues/new)

*   [Overview of Requirements](https://kueue.sigs.k8s.io/docs/tasks/dev/integrate_a_custom_job/#overview-of-requirements)
*   [Building a Built-in Integration](https://kueue.sigs.k8s.io/docs/tasks/dev/integrate_a_custom_job/#building-a-built-in-integration)
    *   [Registration](https://kueue.sigs.k8s.io/docs/tasks/dev/integrate_a_custom_job/#registration)
    *   [Job Framework](https://kueue.sigs.k8s.io/docs/tasks/dev/integrate_a_custom_job/#job-framework)
    *   [Developing a mutation and validation webhook](https://kueue.sigs.k8s.io/docs/tasks/dev/integrate_a_custom_job/#developing-a-mutation-and-validation-webhook)
    *   [Adjust build system](https://kueue.sigs.k8s.io/docs/tasks/dev/integrate_a_custom_job/#adjust-build-system)

*   [Building an External Integration](https://kueue.sigs.k8s.io/docs/tasks/dev/integrate_a_custom_job/#building-an-external-integration)
    *   [Registration](https://kueue.sigs.k8s.io/docs/tasks/dev/integrate_a_custom_job/#registration-1)
    *   [Job Framework](https://kueue.sigs.k8s.io/docs/tasks/dev/integrate_a_custom_job/#job-framework-1)

1.   [Documentation](https://kueue.sigs.k8s.io/docs/)
2.   [Tasks](https://kueue.sigs.k8s.io/docs/tasks/)
3.   [Developer Tools](https://kueue.sigs.k8s.io/docs/tasks/dev/)
4.   Integrate a custom Job with Kueue

Integrate a custom Job with Kueue
=================================

Integrate a custom Job with Kueue.

Kueue has built-in integrations for several Job types, including Kubernetes batch Job, MPIJob, RayJob and JobSet.

There are three options for using Kueue to manage Job-like CRDs that lack built-in integrations.

*   Leverage the built-in AppWrapper integration by wrapping instances of the custom Job in an AppWrapper. See [Running a Wrapped Custom Workload](https://kueue.sigs.k8s.io/docs/tasks/run/external_workloads/wrapped_custom_workload/) for details.
*   Build a new integration as part of the Kueue repository.
*   Build a new integration as an external controller.

This guide is for [platform developers](https://kueue.sigs.k8s.io/docs/tasks/#platform-developer) and describes how to build a new integration. Integrations should be built using the APIs provided by Kueue’s `jobframework` package. This will both simplify development and ensure that your controller will be properly structured to become a core built-in integration if your Job type is widely used by the community.

Overview of Requirements [](https://kueue.sigs.k8s.io/docs/tasks/dev/integrate_a_custom_job/#overview-of-requirements)
----------------------------------------------------------------------------------------------------------------------

Kueue uses the [controller-runtime](https://github.com/kubernetes-sigs/controller-runtime). We recommend becoming familiar with it and with [Kubebuilder](https://github.com/kubernetes-sigs/kubebuilder) before starting to build a Kueue integration.

Whether you are building an external or built-in integration, your main tasks are the following:

1.   To work with Kueue, your custom Job CRD should have a suspend-like field, with semantics similar to the [`suspend` field in a Kubernetes Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/#suspending-a-job). The field needs to be in your CRD’s `spec`, not its `status`, to enable its value to be set from a webhook. Your CRD’s primary controller must respond to changes in the value of this field by suspending or unsuspending its owned resources.

2.   You will need to register the GroupVersionKind of your CRD with Kueue as an integration.

3.   You will need to instantiate various pieces of Kueue’s `jobframework` package for your CRD:

    *   You will need to implement Kueue’s `GenericJob` interface for your CRD
    *   You will need to instantiate a `ReconcilerFactory` and register it with the controller runtime.
    *   You will need to add a `+kubebuilder:rbac` directive for your CRD so Kueue will be permitted to manage it.
    *   You will need to register webhooks that set the initial value of the `suspend` field in instances of your CRD and validate Kueue invariants on creation and update operations.
    *   You will need to instantiate a `Workload` indexer for your CRD.

Building a Built-in Integration [](https://kueue.sigs.k8s.io/docs/tasks/dev/integrate_a_custom_job/#building-a-built-in-integration)
------------------------------------------------------------------------------------------------------------------------------------

To get started, add a new folder in `./pkg/controller/jobs/` to host the implementation of the integration.

Here are completed built-in integrations you can learn from:

*   [BatchJob](https://github.com/kubernetes-sigs/kueue/tree/main/pkg/controller/jobs/job)
*   [JobSet](https://github.com/kubernetes-sigs/kueue/tree/main/pkg/controller/jobs/jobset)
*   [MPIJob](https://github.com/kubernetes-sigs/kueue/tree/main/pkg/controller/jobs/mpijob)
*   [RayJob](https://github.com/kubernetes-sigs/kueue/tree/main/pkg/controller/jobs/rayjob)

### Registration [](https://kueue.sigs.k8s.io/docs/tasks/dev/integrate_a_custom_job/#registration)

Add your framework name to `.integrations.frameworks` in [controller_manager_config.yaml](https://github.com/kubernetes-sigs/kueue/blob/main/config/components/manager/controller_manager_config.yaml)

Add RBAC Authorization for your CRD using [kubebuilder marker comments](https://book.kubebuilder.io/reference/markers/rbac.html).

Write a go `func init()` that invokes the jobframework `RegisterIntegration()` function.

### Job Framework [](https://kueue.sigs.k8s.io/docs/tasks/dev/integrate_a_custom_job/#job-framework)

In the `mycrd_controller.go` file in your folder, implement the `GenericJob` interface, and other optional [interfaces defined by the framework](https://github.com/kubernetes-sigs/kueue/blob/main/pkg/controller/jobframework/interface.go).

In the `mycrd_webhook.go` file in your folder, provide the webhook that invokes helper methods in from the jobframework to set the initial suspend status of created jobs and validate invariants.

Add testing files for both the controller and the webhook. You can check the test files in the other subfolders of `./pkg/controller/jobs/` to learn how to implement them.

### Developing a mutation and validation webhook [](https://kueue.sigs.k8s.io/docs/tasks/dev/integrate_a_custom_job/#developing-a-mutation-and-validation-webhook)

Once you have implemented the `GenericJob` interface, you can register a webhook for the type by using the `BaseWebhookFactory` in `pkg/controller/jobframework`. This webhook ensures that a job is created in a suspended state and that queue names don’t change when the job is admitted. You can read the [MPIJob](https://github.com/kubernetes-sigs/kueue/tree/main/pkg/controller/jobs/mpijob) integration as an example.

For certain use cases, you might need to register a dedicated webhook. In this case, you should use Kueue’s `LosslessDefaulter`, which ensures that the defaulter is compatible with future versions of the CRD, under the assumption that the defaulter does **not** remove any fields from the original object. You can read the [BatchJob](https://github.com/kubernetes-sigs/kueue/tree/main/pkg/controller/jobs/job) integration as an example for how to use a `LosslessDefaulter`.

If the suggestions above are incompatible with your use case, beware of potential [problems when using controller-runtime’s CustomDefaulter](https://groups.google.com/a/kubernetes.io/g/wg-batch/c/WAaabCuGCoY).

### Adjust build system [](https://kueue.sigs.k8s.io/docs/tasks/dev/integrate_a_custom_job/#adjust-build-system)

Add required dependencies to compile your code. For example, using `go get github.com/kubeflow/mpi-operator@0.4.0`.

Update the [Makefile](https://github.com/kubernetes-sigs/kueue/blob/main/Makefile) for testing.

*   Add commands which copy the CRD of your custom job to the Kueue project.
*   Add your custom job operator CRD dependencies into `test-integration`.

Building an External Integration [](https://kueue.sigs.k8s.io/docs/tasks/dev/integrate_a_custom_job/#building-an-external-integration)
--------------------------------------------------------------------------------------------------------------------------------------

Building an external integration is similar to building a built-in integration, except that you will instantiate Kueue’s `jobframework` for your CRD in a separate executable. The only change you will make to the primary Kueue manager is a deployment-time configuration change to enable it to recognize that your CRD is being managed by a Kueue-compatible manager.

Here are completed external integrations you can learn from:

*   [AppWrapper](https://github.com/project-codeflare/appwrapper)

### Registration [](https://kueue.sigs.k8s.io/docs/tasks/dev/integrate_a_custom_job/#registration-1)

Configure Kueue by adding your framework’s GroupVersionKind to `.integrations.externalFrameworks` in [controller_manager_config.yaml](https://kueue.sigs.k8s.io/docs/installation/#install-a-custom-configured-released-version).

### Job Framework [](https://kueue.sigs.k8s.io/docs/tasks/dev/integrate_a_custom_job/#job-framework-1)

Make the following changes to an existing controller-runtime based manager for your CRD.

Add a dependency on Kueue to your `go.mod` so you can import `jobframework` as a go library.

In a new `mycrd_workload_controller.go` file, implement the `GenericJob` interface, and other optional [interfaces defined by the framework](https://github.com/kubernetes-sigs/kueue/blob/main/pkg/controller/jobframework/interface.go).

Extend the existing webhook for your CRD to invoke Kueue’s webhook helper methods:

*   Your defaulter should invoke `jobframework.ApplyDefaultForSuspend` in [defaults.go](https://github.com/kubernetes-sigs/kueue/blob/main/pkg/controller/jobframework/defaults.go)
*   Your validator should invoke `jobframework.ValidateJobOnCreate` and `jobframework.ValidateJobOnUpdate` in [validation.go](https://github.com/kubernetes-sigs/kueue/blob/main/pkg/controller/jobframework/validation.go)

Extend your manager’s startup procedure to do the following:

*   Using the `jobframework.NewGenericReconcilerFactory` method, create an instance of Kueue’s JobReconciler for your CRD and register it with the controller-runtime manager.
*   Invoke `jobframework.SetupWorkloadOwnerIndex` to create an indexer for Workloads owned by your CRD.

Extend your existing RBAC Authorizations to include the privileges needed by Kueue’s JobReconciler:

```go
// +kubebuilder:rbac:groups=scheduling.k8s.io,resources=priorityclasses,verbs=list;get;watch
// +kubebuilder:rbac:groups="",resources=events,verbs=create;watch;update;patch
// +kubebuilder:rbac:groups=kueue.x-k8s.io,resources=workloads,verbs=get;list;watch;create;update;patch;delete
// +kubebuilder:rbac:groups=kueue.x-k8s.io,resources=workloads/status,verbs=get;update;patch
// +kubebuilder:rbac:groups=kueue.x-k8s.io,resources=workloads/finalizers,verbs=update
// +kubebuilder:rbac:groups=kueue.x-k8s.io,resources=resourceflavors,verbs=get;list;watch
// +kubebuilder:rbac:groups=kueue.x-k8s.io,resources=workloadpriorityclasses,verbs=get;list;watch
```

Copy

For a concrete example, consult these pieces of the AppWrapper controller:

*   [workload_controller.go](https://github.com/project-codeflare/appwrapper/blob/main/internal/controller/workload/workload_controller.go)
*   [appwrapper_webhook.go](https://github.com/project-codeflare/appwrapper/blob/main/internal/webhook/appwrapper_webhook.go)
*   [setup.go](https://github.com/project-codeflare/appwrapper/blob/main/pkg/controller/setup.go)

Feedback
--------

Was this page helpful?

Yes No
Glad to hear it! Please [tell us how we can improve](https://github.com/kubernetes-sigs/kueue/issues/new).

Sorry to hear that. Please [tell us how we can improve](https://github.com/kubernetes-sigs/kueue/issues/new).

Last modified December 10, 2025: [docs: Fix dead links (#8165) (fe394b921)](https://github.com/kubernetes-sigs/kueue/commit/fe394b921cd084147e62522124c6de734d3b75b0)

*   [](https://groups.google.com/a/kubernetes.io/g/wg-batch)
*   [](https://twitter.com/kubernetesio)
*   [](https://stackoverflow.com/questions/tagged/kubernetes)
*   [](https://kubernetes.slack.com/messages/wg-batch)

© 2026 The Kubernetes Authors | Documentation Distributed under CC BY 4.0

© The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage page](https://www.linuxfoundation.org/legal/trademark-usage).
