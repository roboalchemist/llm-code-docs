# Source: https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/

Title: Enable KueueViz

URL Source: https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/

Published Time: 2025-07-18T00:00:00+00:00

Markdown Content:
Enable KueueViz | Kueue
===============
[Kueue](https://kueue.sigs.k8s.io/)

*   [Documentation](https://kueue.sigs.k8s.io/docs/)
*   [Talks and presentations](https://kueue.sigs.k8s.io/docs/talks_and_presentations/)
*   [Adopters](https://kueue.sigs.k8s.io/docs/adopters/)
*   [GitHub](https://github.com/kubernetes-sigs/kueue)
*   [English](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#) 

[English](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#)

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

[View this page](https://github.com/kubernetes-sigs/kueue/tree/main/site/content/en/docs/tasks/manage/enable_kueueviz.md)[Edit this page](https://github.com/kubernetes-sigs/kueue/edit/main/site/content/en/docs/tasks/manage/enable_kueueviz.md)[Create child page](https://github.com/kubernetes-sigs/kueue/new/main/site/content/en/docs/tasks/manage?filename=change-me.md&value=---%0Atitle%3A+%22Long+Page+Title%22%0AlinkTitle%3A+%22Short+Nav+Title%22%0Aweight%3A+100%0Adescription%3A+%3E-%0A+++++Page+description+for+heading+and+indexes.%0A---%0A%0A%23%23+Heading%0A%0AEdit+this+template+to+create+your+new+page.%0A%0A%2A+Give+it+a+good+name%2C+ending+in+%60.md%60+-+e.g.+%60getting-started.md%60%0A%2A+Edit+the+%22front+matter%22+section+at+the+top+of+the+page+%28weight+controls+how+its+ordered+amongst+other+pages+in+the+same+directory%3B+lowest+number+first%29.%0A%2A+Add+a+good+commit+message+at+the+bottom+of+the+page+%28%3C80+characters%3B+use+the+extended+description+field+for+more+detail%29.%0A%2A+Create+a+new+branch+so+you+can+preview+your+new+file+and+request+a+review+via+Pull+Request.%0A)[Create issue](https://github.com/kubernetes-sigs/kueue/issues/new?title=Enable%20KueueViz)[Create project issue](https://github.com/kubernetes-sigs/kueue/issues/new)

*   [Before you begin](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#before-you-begin)
*   [Installation with Kueue](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#installation-with-kueue)
*   [Enable KueueViz (Kueue is already installed)](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#enable-kueueviz-kueue-is-already-installed)
    *   [Enable KueueViz by Helm](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#enable-kueueviz-by-helm)
    *   [Enable KueueViz by YAML](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#enable-kueueviz-by-yaml)

*   [Accessing the Dashboard](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#accessing-the-dashboard)
    *   [Port Forwarding (Only for development)](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#port-forwarding-only-for-development)
    *   [Ingress](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#ingress)
    *   [LoadBalancer](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#loadbalancer)

*   [Upgrade](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#upgrade)
    *   [Upgrade by Helm](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#upgrade-by-helm)
    *   [Upgrade by YAML](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#upgrade-by-yaml)

*   [Uninstall](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#uninstall)
*   [What’s next](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#whats-next)

1.   [Documentation](https://kueue.sigs.k8s.io/docs/)
2.   [Tasks](https://kueue.sigs.k8s.io/docs/tasks/)
3.   [Manage Kueue](https://kueue.sigs.k8s.io/docs/tasks/manage/)
4.   Enable KueueViz

Enable KueueViz
===============

Installing and configuring KueueViz, a web-based visualization tool for Kueue workload monitoring.

#### Note

For a streamlined installation and simplified upgrades, we recommend deploying Kueue using Helm.

You can customize the deployment with a local `values.yaml` file to fit your environment.

See the [Helm chart installation guide](https://kueue.sigs.k8s.io/docs/installation/#install-by-helm) for full instructions.

KueueViz is a web-based visualization tool that provides real-time monitoring of Kueue workloads, queues, and resource allocation. It offers an intuitive dashboard for observing job queue status, resource utilization, and workload progression.

This page shows how to install and configure KueueViz in your cluster.

The page is intended for [batch administrators](https://kueue.sigs.k8s.io/docs/tasks/#batch-administrator).

Before you begin [](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#before-you-begin)
--------------------------------------------------------------------------------------------------

Make sure the following conditions are met:

*   A Kubernetes cluster is running
*   The kubectl command-line tool has communication with your cluster
*   The Helm command-line tool is installed
*   Kueue is installed in your cluster
*   (Optional) An ingress controller for external access (e.g. Nginx Ingress Controller)

KueueViz can be installed using Helm (recommended), or kubectl. Choose the method that best fits your workflow.

Installation with Kueue [](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#installation-with-kueue)
----------------------------------------------------------------------------------------------------------------

To install KueueViz as part of a new Kueue installation:

```bash
helm install kueue oci://registry.k8s.io/kueue/charts/kueue \
  --version=0.16.2 \
  --namespace kueue-system \
  --create-namespace \
  --wait --timeout 300s \
  --set enableKueueViz=true # enable KueueViz
```

Copy

For more information on installing Kueue, please refer to [Installation](https://kueue.sigs.k8s.io/docs/installation/).

Enable KueueViz (Kueue is already installed) [](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#enable-kueueviz-kueue-is-already-installed)
--------------------------------------------------------------------------------------------------------------------------------------------------------

If Kueue is already installed, you can enable KueueViz by Helm or kubectl.

### Enable KueueViz by Helm [](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#enable-kueueviz-by-helm)

To enable KueueViz on an existing Kueue installation by Helm:

```bash
helm upgrade kueue oci://registry.k8s.io/kueue/charts/kueue \
  --version=0.16.2 \
  --namespace kueue-system \
  --set enableKueueViz=true # enable KueueViz
```

Copy

### Enable KueueViz by YAML [](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#enable-kueueviz-by-yaml)

To enable KueueViz on an existing Kueue installation by YAML:

```bash
kubectl apply --server-side -f https://github.com/kubernetes-sigs/kueue/releases/download/v0.16.2/kueueviz.yaml
```

Copy

Accessing the Dashboard [](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#accessing-the-dashboard)
----------------------------------------------------------------------------------------------------------------

### Port Forwarding (Only for development) [](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#port-forwarding-only-for-development)

For quick access during development or testing(had tested by Docker Desktop):

```bash
kubectl port-forward svc/kueue-kueueviz-frontend -n kueue-system 8080
kubectl port-forward svc/kueue-kueueviz-backend  -n kueue-system 8081:8080
```

Copy

Edit the kueue-viz-frontend Deployment to set env `REACT_APP_WEBSOCKET_URL=ws://localhost:8081`.

Then access the dashboard at [http://localhost:8080](http://localhost:8080/).

### Ingress [](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#ingress)

For production deployments, configure an Ingress resource:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: kueueviz-ingress
  namespace: kueue-system
spec:
  rules:
    - host: kueueviz.example.com
      http:
        paths:
          - path: /api(/|$)(.*)
            pathType: Prefix
            backend:
              service:
                name: kueue-kueueviz-backend
                port:
                  number: 8080
          - path: /
            pathType: Prefix
            backend:
              service:
                name: kueue-kueueviz-frontend
                port:
                  number: 8080
  tls:
    - hosts:
        - kueueviz.example.com # replace with your domain
      secretName: kueueviz-tls # you need to create a TLS secret at first
```

Copy

### LoadBalancer [](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#loadbalancer)

For cloud environments with LoadBalancer support:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: kueueviz-loadbalancer
  namespace: kueue-system
spec:
  type: LoadBalancer
  ports:
    - name: http
      port: 80
      targetPort: 8080
      protocol: TCP
  selector:
    app.kubernetes.io/name: kueue
    app.kubernetes.io/component: kueueviz-frontend
```

Copy

Upgrade [](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#upgrade)
--------------------------------------------------------------------------------

### Upgrade by Helm [](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#upgrade-by-helm)

To upgrade KueueViz by Helm:

```bash
helm upgrade kueue oci://registry.k8s.io/kueue/charts/kueue \
  --version=0.16.2 \
  --namespace kueue-system \
  --set enableKueueViz=true
```

Copy

### Upgrade by YAML [](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#upgrade-by-yaml)

To upgrade KueueViz by YAML:

```bash
kubectl apply --server-side -f https://github.com/kubernetes-sigs/kueue/releases/download/v0.16.2/kueueviz.yaml
```

Copy

Uninstall [](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#uninstall)
------------------------------------------------------------------------------------

**Note:** Be sure to uninstall KueueViz, and not to accidentally uninstall Kueue instead.

To uninstall KueueViz components:

```bash
kubectl delete -f https://github.com/kubernetes-sigs/kueue/releases/download/v0.16.2/kueueviz.yaml
```

Copy

What’s next [](https://kueue.sigs.k8s.io/docs/tasks/manage/enable_kueueviz/#whats-next)
---------------------------------------------------------------------------------------

*   Explore more [Tasks](https://kueue.sigs.k8s.io/docs/tasks/)
*   Learn about [Concepts](https://kueue.sigs.k8s.io/docs/concepts/)

Feedback
--------

Was this page helpful?

Yes No
Glad to hear it! Please [tell us how we can improve](https://github.com/kubernetes-sigs/kueue/issues/new).

Sorry to hear that. Please [tell us how we can improve](https://github.com/kubernetes-sigs/kueue/issues/new).

Last modified December 9, 2025: [[website] Document the failure recovery mechanism (#8147) (6611ea161)](https://github.com/kubernetes-sigs/kueue/commit/6611ea161db143110a4d1abc0766049fb2e62224)

*   [](https://groups.google.com/a/kubernetes.io/g/wg-batch)
*   [](https://twitter.com/kubernetesio)
*   [](https://stackoverflow.com/questions/tagged/kubernetes)
*   [](https://kubernetes.slack.com/messages/wg-batch)

© 2026 The Kubernetes Authors | Documentation Distributed under CC BY 4.0

© The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage page](https://www.linuxfoundation.org/legal/trademark-usage).
