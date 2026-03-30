# Source: https://kueue.sigs.k8s.io/zh-cn/docs/

Title: 文档

URL Source: https://kueue.sigs.k8s.io/zh-cn/docs/

Markdown Content:
文档 | Kueue
===============
[Kueue](https://kueue.sigs.k8s.io/zh-cn/)

*   [文档](https://kueue.sigs.k8s.io/zh-cn/docs/)
*   [演讲和展示](https://kueue.sigs.k8s.io/zh-cn/docs/talks_and_presentations/)
*   [采用者](https://kueue.sigs.k8s.io/zh-cn/docs/adopters/)
*   [GitHub](https://github.com/kubernetes-sigs/kueue)
*   [简体中文](https://kueue.sigs.k8s.io/zh-cn/docs/#)[English](https://kueue.sigs.k8s.io/docs/) 

[简体中文](https://kueue.sigs.k8s.io/zh-cn/docs/#)

[English](https://kueue.sigs.k8s.io/docs/)

*   [文档](https://kueue.sigs.k8s.io/zh-cn/docs/)
    *   - [x] [概览](https://kueue.sigs.k8s.io/zh-cn/docs/overview/) 
    *   - [x] [安装](https://kueue.sigs.k8s.io/zh-cn/docs/installation/) 
    *   - [x] [核心概念](https://kueue.sigs.k8s.io/zh-cn/docs/concepts/) 
        *   - [x] [资源规格（Resource Flavor）](https://kueue.sigs.k8s.io/zh-cn/docs/concepts/resource_flavor/) 
        *   - [x] [集群队列（ClusterQueue）](https://kueue.sigs.k8s.io/zh-cn/docs/concepts/cluster_queue/) 
        *   - [x] [Cohort](https://kueue.sigs.k8s.io/zh-cn/docs/concepts/cohort/) 
        *   - [x] [弹性工作负载](https://kueue.sigs.k8s.io/zh-cn/docs/concepts/elastic_workload/) 
        *   - [x] [本地队列（Local Queue）](https://kueue.sigs.k8s.io/zh-cn/docs/concepts/local_queue/) 
        *   - [x] [工作负载(Workload)](https://kueue.sigs.k8s.io/zh-cn/docs/concepts/workload/) 
        *   - [x] [Topology](https://kueue.sigs.k8s.io/zh-cn/docs/concepts/topology/) 
        *   - [x] [公平共享（Fair Sharing）](https://kueue.sigs.k8s.io/zh-cn/docs/concepts/fair_sharing/) 
        *   - [x] [准入公平分共享（Admission Fair Sharing）](https://kueue.sigs.k8s.io/zh-cn/docs/concepts/admission_fair_sharing/) 
        *   - [x] [准入检查（Admission Check）](https://kueue.sigs.k8s.io/zh-cn/docs/concepts/admission_check/) 
        *   - [x] [拓扑感知调度](https://kueue.sigs.k8s.io/zh-cn/docs/concepts/topology_aware_scheduling/) 
        *   - [x] [Workload 优先级类](https://kueue.sigs.k8s.io/zh-cn/docs/concepts/workload_priority_class/) 
        *   - [x] [抢占（Preemption）](https://kueue.sigs.k8s.io/zh-cn/docs/concepts/preemption/) 
        *   - [x] [MultiKueue](https://kueue.sigs.k8s.io/zh-cn/docs/concepts/multikueue/) 

    *   - [x] [任务](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/) 
        *   - [x] [管理 Kueue](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/manage/) 
            *   - [x] [Kueue 产品化](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/manage/productization/) 
                *   - [x] [配置外部证书管理器](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/manage/productization/cert_manager/) 
                *   - [x] [配置 Prometheus](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/manage/productization/prometheus/) 

            *   - [x] [强制实施 Kueue 对工作负载的管理](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/manage/enforce_job_management/) 
                *   - [x] [设置默认的 LocalQueue](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/manage/enforce_job_management/setup_default_local_queue/) 
                *   - [x] [设置 manageJobsWithoutQueueName](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/manage/enforce_job_management/manage_jobs_without_queue_name/) 
                *   - [x] [制定 Job 准入策略](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/manage/enforce_job_management/setup_job_admission_policy/) 

            *   - [x] [设置 RBAC](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/manage/rbac/) 
            *   - [x] [管理集群配额](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/manage/administer_cluster_quotas/) 
            *   - [x] [Monitor pending Workloads](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/manage/monitor_pending_workloads/ "监控 pending 状态的工作负载") 
                *   - [x] [Pending Workloads on-demand](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/manage/monitor_pending_workloads/pending_workloads_on_demand/) 
                *   - [x] [Grafana 中监控待处理的工作负载](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/manage/monitor_pending_workloads/pending_workloads_in_grafana/) 

            *   - [x] [使用工作负载优先级（`WorkloadPriority`）运行作业（Job）](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/manage/run_job_with_workload_priority/) 
            *   - [x] [使用就绪态 Pod 配置全有或全无调度](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/manage/setup_wait_for_pods_ready/) 
            *   - [x] [设置 MultiKueue 环境](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/manage/setup_multikueue/) 
            *   - [x] [设置 Workload 的垃圾回收](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/manage/setup_object_retention_policy/) 
            *   - [x] [启用 Dashboard（KueueViz）](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/manage/enable_kubeviz/) 

        *   - [x] [Run Workloads](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/) 
            *   - [x] [Kubernetes Job](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/jobs/ "运行 Kubernetes Job") 
            *   - [x] [Kubernetes CronJobs](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/run_cronjobs/ "运行 CronJob") 
            *   - [x] [HAMi vGPU](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/using_hami/ "使用 HAMi") 
            *   - [x] [RayService](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/rayservices/ "运行 RayService") 
            *   - [x] [LeaderWorkerSet](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/leaderworkerset/ "运行 LeaderWorkerSet") 
            *   - [x] [AppWrapper](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/appwrappers/ "运行 AppWrapper") 
            *   - [x] [RayClusters](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/rayclusters/ "运行 RayCluster") 
            *   - [x] [RayJobs](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/rayjobs/ "运行 RayJob") 
            *   - [x] [Deployment](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/deployment/ "运行 Deployment") 
            *   - [x] [StatefulSet](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/statefulset/ "运行 StatefulSet") 
            *   - [x] [普通 Pod](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/plain_pods/ "运行普通 Pod") 
            *   - [x] [Kubeflow Jobs](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/kubeflow/ "运行 Kubeflow") 
                *   - [x] [运行 JAXJob](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/kubeflow/jaxjobs/) 
                *   - [x] [运行 PaddleJob](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/kubeflow/paddlejobs/) 
                *   - [x] [运行 XGBoostJob](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/kubeflow/xgboostjobs/) 
                *   - [x] [运行 TFJob](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/kubeflow/tfjobs/) 
                *   - [x] [运行 PyTorchJob](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/kubeflow/pytorchjobs/) 
                *   - [x] [运行 MPIJob](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/kubeflow/mpijobs/) 

            *   - [x] [Jobsets](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/jobsets/ "运行 JobSet") 
            *   - [x] [Multi-Cluster](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/multikueue/ "Multi-Cluster Job dispatching") 
                *   - [x] [Deployment](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/multikueue/deployment/ "在多集群环境中运行 Deployment") 
                *   - [x] [Plain Pod](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/multikueue/plain_pods/ "在多集群环境中运行普通 Pod") 
                *   - [x] [Kubernetes Job](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/multikueue/job/ "在多集群环境中运行 Job") 
                *   - [x] [AppWrappers](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/multikueue/appwrapper/ "在多集群环境中运行 AppWrappers") 
                *   - [x] [Jobsets](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/multikueue/jobsets/ "在多集群环境中运行 Jobset") 
                *   - [x] [KubeRay](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/multikueue/kuberay/ "在多集群环境中运行 KubeRay Job") 
                *   - [x] [Kubeflow](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/multikueue/kubeflow/ "在多集群环境中运行 Kubeflow Job") 
                *   - [x] [MPIJob](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/multikueue/mpijob/ "在多集群环境中运行 MPIJob") 

            *   - [x] [External Frameworks](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/external_workloads/ "支持外部框架") 
                *   - [x] [Custom Workload](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/external_workloads/wrapped_custom_workload/ "运行包装过的自定义工作负载") 
                *   - [x] [Flux MiniClusters](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/external_workloads/flux_miniclusters/ "运行 Flux MiniCluster") 
                *   - [x] [Argo Workflow](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/external_workloads/argo_workflow/ "运行 Argo Workflow") 
                *   - [x] [Tekton Pipeline](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/external_workloads/tektoncd/ "运行 Tekton Pipeline") 

            *   - [x] [](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/run/python_jobs/) 

        *   - [x] [开发工具](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/dev/) 
            *   - [x] [开启 pprof 端点](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/dev/enabling_pprof_endpoints/) 
            *   - [x] [外部框架](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/dev/external_frameworks/) 
            *   - [x] [将自定义 Job 与 Kueue 集成](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/dev/integrate_a_custom_job/) 
            *   - [x] [开发 AdmissionCheck 控制器](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/dev/develop-acc/) 

        *   - [x] [故障排除](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/troubleshooting/) 
            *   - [x] [Job 故障排除](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/troubleshooting/troubleshooting_jobs/) 
            *   - [x] [队列故障排除](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/troubleshooting/troubleshooting_queues/) 
            *   - [x] [Kueue 中的 Provisioning Request 故障排除](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/troubleshooting/troubleshooting_provreq/) 
            *   - [x] [Pod 故障排除](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/troubleshooting/troubleshooting_pods/) 
            *   - [x] [删除 ClusterQueue 故障排除](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/troubleshooting/troubleshooting_delete_clusterqueue/) 

    *   - [x] [参考](https://kueue.sigs.k8s.io/zh-cn/docs/reference/) 
        *   - [x] [Kubectl Kueue 插件](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/) 
            *   - [x] [Installation](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/installation/) 
            *   - [x] [Commands](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/) 
                *   - [x] [kueuectl](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl/) 
                *   - [x] [kueuectl create](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_create/) 
                    *   - [x] [kueuectl create clusterqueue](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_create/kueuectl_create_clusterqueue/) 
                    *   - [x] [kueuectl create localqueue](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_create/kueuectl_create_localqueue/) 
                    *   - [x] [kueuectl create resourceflavor](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_create/kueuectl_create_resourceflavor/) 

                *   - [x] [kueuectl delete](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_delete/) 
                    *   - [x] [kueuectl delete clusterqueue](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_delete/kueuectl_delete_clusterqueue/) 
                    *   - [x] [kueuectl delete localqueue](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_delete/kueuectl_delete_localqueue/) 
                    *   - [x] [kueuectl delete resourceflavor](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_delete/kueuectl_delete_resourceflavor/) 
                    *   - [x] [kueuectl delete workload](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_delete/kueuectl_delete_workload/) 

                *   - [x] [kueuectl describe](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_describe/) 
                    *   - [x] [kueuectl describe clusterqueue](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_describe/kueuectl_describe_clusterqueue/) 
                    *   - [x] [kueuectl describe localqueue](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_describe/kueuectl_describe_localqueue/) 
                    *   - [x] [kueuectl describe resourceflavor](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_describe/kueuectl_describe_resourceflavor/) 
                    *   - [x] [kueuectl describe workload](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_describe/kueuectl_describe_workload/) 

                *   - [x] [kueuectl edit](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_edit/) 
                    *   - [x] [kueuectl edit clusterqueue](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_edit/kueuectl_edit_clusterqueue/) 
                    *   - [x] [kueuectl edit localqueue](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_edit/kueuectl_edit_localqueue/) 
                    *   - [x] [kueuectl edit resourceflavor](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_edit/kueuectl_edit_resourceflavor/) 
                    *   - [x] [kueuectl edit workload](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_edit/kueuectl_edit_workload/) 

                *   - [x] [kueuectl get](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_get/) 
                    *   - [x] [kueuectl get clusterqueue](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_get/kueuectl_get_clusterqueue/) 
                    *   - [x] [kueuectl get localqueue](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_get/kueuectl_get_localqueue/) 
                    *   - [x] [kueuectl get resourceflavor](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_get/kueuectl_get_resourceflavor/) 
                    *   - [x] [kueuectl get workload](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_get/kueuectl_get_workload/) 

                *   - [x] [kueuectl list](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_list/) 
                    *   - [x] [kueuectl list clusterqueue](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_list/kueuectl_list_clusterqueue/) 
                    *   - [x] [kueuectl list localqueue](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_list/kueuectl_list_localqueue/) 
                    *   - [x] [kueuectl list pods](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_list/kueuectl_list_pods/) 
                    *   - [x] [kueuectl list resourceflavor](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_list/kueuectl_list_resourceflavor/) 
                    *   - [x] [kueuectl list workload](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_list/kueuectl_list_workload/) 

                *   - [x] [kueuectl patch](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_patch/) 
                    *   - [x] [kueuectl patch clusterqueue](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_patch/kueuectl_patch_clusterqueue/) 
                    *   - [x] [kueuectl patch localqueue](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_patch/kueuectl_patch_localqueue/) 
                    *   - [x] [kueuectl patch resourceflavor](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_patch/kueuectl_patch_resourceflavor/) 
                    *   - [x] [kueuectl patch workload](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_patch/kueuectl_patch_workload/) 

                *   - [x] [kueuectl resume](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_resume/) 
                    *   - [x] [kueuectl resume clusterqueue](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_resume/kueuectl_resume_clusterqueue/) 
                    *   - [x] [kueuectl resume localqueue](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_resume/kueuectl_resume_localqueue/) 
                    *   - [x] [kueuectl resume workload](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_resume/kueuectl_resume_workload/) 

                *   - [x] [kueuectl stop](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_stop/) 
                    *   - [x] [kueuectl stop clusterqueue](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_stop/kueuectl_stop_clusterqueue/) 
                    *   - [x] [kueuectl stop localqueue](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_stop/kueuectl_stop_localqueue/) 
                    *   - [x] [kueuectl stop workload](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_stop/kueuectl_stop_workload/) 

                *   - [x] [kueuectl version](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kubectl-kueue/commands/kueuectl_version/) 

        *   - [x] [Labels and Annotations](https://kueue.sigs.k8s.io/zh-cn/docs/reference/labels-and-annotations/) 
        *   - [x] [Prometheus Metrics](https://kueue.sigs.k8s.io/zh-cn/docs/reference/metrics/) 
        *   - [x] [Kueue API](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kueue.v1beta1/) 
        *   - [x] [Kueue Configuration API](https://kueue.sigs.k8s.io/zh-cn/docs/reference/kueue-config.v1beta1/) 

    *   - [x] [准入检查](https://kueue.sigs.k8s.io/zh-cn/docs/admission-check-controllers/) 
        *   - [x] [Provisioning 准入检查控制器](https://kueue.sigs.k8s.io/zh-cn/docs/admission-check-controllers/provisioning/) 

    *   - [x] [演讲和展示](https://kueue.sigs.k8s.io/zh-cn/docs/talks_and_presentations/) 
    *   - [x] [贡献指南](https://kueue.sigs.k8s.io/zh-cn/docs/contribution_guidelines/) 
        *   - [x] [运行测试](https://kueue.sigs.k8s.io/zh-cn/docs/contribution_guidelines/testing/ "运行和调试测试") 

    *   - [x] [采用者](https://kueue.sigs.k8s.io/zh-cn/docs/adopters/) 

[查看此页面](https://github.com/kubernetes-sigs/kueue/tree/main/site/content/zh-CN/docs/_index.md)[编辑此页面](https://github.com/kubernetes-sigs/kueue/edit/main/site/content/zh-CN/docs/_index.md)[创建子页面](https://github.com/kubernetes-sigs/kueue/new/main/site/content/zh-CN/docs?filename=change-me.md&value=---%0Atitle%3A+%22Long+Page+Title%22%0AlinkTitle%3A+%22Short+Nav+Title%22%0Aweight%3A+100%0Adescription%3A+%3E-%0A+++++Page+description+for+heading+and+indexes.%0A---%0A%0A%23%23+Heading%0A%0AEdit+this+template+to+create+your+new+page.%0A%0A%2A+Give+it+a+good+name%2C+ending+in+%60.md%60+-+e.g.+%60getting-started.md%60%0A%2A+Edit+the+%22front+matter%22+section+at+the+top+of+the+page+%28weight+controls+how+its+ordered+amongst+other+pages+in+the+same+directory%3B+lowest+number+first%29.%0A%2A+Add+a+good+commit+message+at+the+bottom+of+the+page+%28%3C80+characters%3B+use+the+extended+description+field+for+more+detail%29.%0A%2A+Create+a+new+branch+so+you+can+preview+your+new+file+and+request+a+review+via+Pull+Request.%0A)[创建问题](https://github.com/kubernetes-sigs/kueue/issues/new?title=%e6%96%87%e6%a1%a3)[创建项目问题](https://github.com/kubernetes-sigs/kueue/issues/new)

1.   文档

文档
==

* * *

##### [概览](https://kueue.sigs.k8s.io/zh-cn/docs/overview/)

为什么选择 Kueue?

##### [安装](https://kueue.sigs.k8s.io/zh-cn/docs/installation/)

将 Kueue 安装到 Kubernetes 集群

##### [核心概念](https://kueue.sigs.k8s.io/zh-cn/docs/concepts/)

Kueue 核心概念

##### [任务](https://kueue.sigs.k8s.io/zh-cn/docs/tasks/)

Doing common Kueue tasks

##### [参考](https://kueue.sigs.k8s.io/zh-cn/docs/reference/)

This section contains the Kueue reference information.

##### [准入检查](https://kueue.sigs.k8s.io/zh-cn/docs/admission-check-controllers/)

本节描述了 Kueue 中包含的准入检查控制器。

##### [演讲和展示](https://kueue.sigs.k8s.io/zh-cn/docs/talks_and_presentations/)

Talks and presentations showcasing Kueue

##### [贡献指南](https://kueue.sigs.k8s.io/zh-cn/docs/contribution_guidelines/)

如何为 Kueue 做出贡献

##### [采用者](https://kueue.sigs.k8s.io/zh-cn/docs/adopters/)

Kueue 的使用场景及使用方式

反馈
--

这个页面有帮助吗？

满意 不满意
Glad to hear it! Please [tell us how we can improve](https://github.com/kubernetes-sigs/kueue/issues/new).

Sorry to hear that. Please [tell us how we can improve](https://github.com/kubernetes-sigs/kueue/issues/new).

最后修改 July 2, 2025: [Cherry-pick website commits from upstream/main (#5825) (cd1b0ecfa)](https://github.com/kubernetes-sigs/kueue/commit/cd1b0ecfa62a7cfb9db93da485321b506dff74af)

*   [](https://groups.google.com/a/kubernetes.io/g/wg-batch)
*   [](https://twitter.com/kubernetesio)
*   [](https://stackoverflow.com/questions/tagged/kubernetes)
*   [](https://kubernetes.slack.com/messages/wg-batch)

© 2026 The Kubernetes Authors | Documentation Distributed under CC BY 4.0

© The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage page](https://www.linuxfoundation.org/legal/trademark-usage).
