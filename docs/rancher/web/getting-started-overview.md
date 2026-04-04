# Source: https://ranchermanager.docs.rancher.com/getting-started/overview

Title: Overview | Rancher

URL Source: https://ranchermanager.docs.rancher.com/getting-started/overview

Markdown Content:
Rancher is a container management platform built for organizations that deploy containers in production. Rancher makes it easy to run Kubernetes everywhere, meet IT requirements, and empower DevOps teams.

Run Kubernetes Everywhere[​](https://ranchermanager.docs.rancher.com/getting-started/overview#run-kubernetes-everywhere "Direct link to Run Kubernetes Everywhere")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Kubernetes has become the container orchestration standard. Most cloud and virtualization vendors now offer it as standard infrastructure. Rancher users have the choice of creating Kubernetes clusters with Rancher Kubernetes distributions (RKE2/K3s) or cloud Kubernetes services, such as GKE, AKS, and EKS. Rancher users can also import and manage their existing Kubernetes clusters created using any Kubernetes distribution or installer.

Meet IT Requirements[​](https://ranchermanager.docs.rancher.com/getting-started/overview#meet-it-requirements "Direct link to Meet IT Requirements")
----------------------------------------------------------------------------------------------------------------------------------------------------

Rancher supports centralized authentication, access control, and monitoring for all Kubernetes clusters under its control. For example, you can:

*   Use your Active Directory credentials to access Kubernetes clusters hosted by cloud vendors, such as GKE.
*   Setup and enforce access control and security policies across all users, groups, projects, clusters, and clouds.
*   View the health and capacity of your Kubernetes clusters from a single-pane-of-glass.

Empower DevOps Teams[​](https://ranchermanager.docs.rancher.com/getting-started/overview#empower-devops-teams "Direct link to Empower DevOps Teams")
----------------------------------------------------------------------------------------------------------------------------------------------------

Rancher provides an intuitive user interface for DevOps engineers to manage their application workload. The user does not need to have in-depth knowledge of Kubernetes concepts to start using Rancher. Rancher catalog contains a set of useful DevOps tools. Rancher is certified with a wide selection of cloud native ecosystem products, including, for example, security tools, monitoring systems, container registries, and storage and networking drivers.

The following figure illustrates the role Rancher plays in IT and DevOps organizations. Each team deploys their applications on the public or private clouds they choose. IT administrators gain visibility and enforce policies across all users, clusters, and clouds.

![Image 1: Platform](https://ranchermanager.docs.rancher.com/assets/images/platform-9c0c4130a7a0828898dbc7af56f76df7.png)

Features of the Rancher API Server[​](https://ranchermanager.docs.rancher.com/getting-started/overview#features-of-the-rancher-api-server "Direct link to Features of the Rancher API Server")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Rancher API server is built on top of an embedded Kubernetes API server and an etcd database. It implements the following functionalities:

*   **User management:** The Rancher API server [manages user identities](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/authentication-permissions-and-global-configuration/authentication-config) that correspond to external authentication providers like Active Directory or GitHub, in addition to local users.
*   **Authorization:** The Rancher API server manages [access control](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/authentication-permissions-and-global-configuration/manage-role-based-access-control-rbac) and [security](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/authentication-permissions-and-global-configuration/pod-security-standards) standards.

### Working with Kubernetes[​](https://ranchermanager.docs.rancher.com/getting-started/overview#working-with-kubernetes "Direct link to Working with Kubernetes")

*   **Provisioning Kubernetes clusters:** The Rancher API server can [provision Kubernetes](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/kubernetes-clusters-in-rancher-setup) on existing nodes, or perform [Kubernetes upgrades.](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/upgrade-and-roll-back-kubernetes)
*   **Catalog management:** Rancher provides the ability to use a [catalog of Helm charts](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/helm-charts-in-rancher) that make it easy to repeatedly deploy applications.
*   **Managing projects:** A project is a group of multiple namespaces and access control policies within a cluster. A project is a Rancher concept, not a Kubernetes concept, which allows you to manage multiple namespaces as a group and perform Kubernetes operations in them. The Rancher UI provides features for [project administration](https://ranchermanager.docs.rancher.com/how-to-guides/advanced-user-guides/manage-projects) and for [managing applications within projects.](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/kubernetes-resources-setup)
*   **Fleet Continuous Delivery:** Within Rancher, you can leverage [Fleet Continuous Delivery](https://ranchermanager.docs.rancher.com/integrations-in-rancher/fleet) to deploy applications from git repositories, without any manual operation, to targeted downstream Kubernetes clusters.
*   **Istio:** Our [integration with Istio](https://ranchermanager.docs.rancher.com/integrations-in-rancher/istio) is designed so that a Rancher operator, such as an administrator or cluster owner, can deliver Istio to developers. Then developers can use Istio to enforce security policies, troubleshoot problems, or manage traffic for green/blue deployments, canary deployments, or A/B testing.

### Working with Cloud Infrastructure[​](https://ranchermanager.docs.rancher.com/getting-started/overview#working-with-cloud-infrastructure "Direct link to Working with Cloud Infrastructure")

*   **Tracking nodes:** The Rancher API server tracks identities of all the [nodes](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/manage-clusters/nodes-and-node-pools) in all clusters.
*   **Setting up infrastructure:** When configured to use a cloud provider, Rancher can dynamically provision [new nodes](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/launch-kubernetes-with-rancher/use-new-nodes-in-an-infra-provider) and [persistent storage](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/manage-clusters/create-kubernetes-persistent-storage) in the cloud.

### Cluster Visibility[​](https://ranchermanager.docs.rancher.com/getting-started/overview#cluster-visibility "Direct link to Cluster Visibility")

*   **Logging:** Rancher can integrate with a variety of popular logging services and tools that exist outside of your Kubernetes clusters.
*   **Monitoring:** Using Rancher, you can monitor the state and processes of your cluster nodes, Kubernetes components, and software deployments through integration with Prometheus, a leading open-source monitoring solution.
*   **Alerting:** To keep your clusters and applications healthy and driving your organizational productivity forward, you need to stay informed of events occurring in your clusters and projects, both planned and unplanned.

Editing Downstream Clusters with Rancher[​](https://ranchermanager.docs.rancher.com/getting-started/overview#editing-downstream-clusters-with-rancher "Direct link to Editing Downstream Clusters with Rancher")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The options and settings available for an existing cluster change based on the method that you used to provision it.

After a cluster is created with Rancher, a cluster administrator can manage cluster membership or manage node pools, among [other options.](https://ranchermanager.docs.rancher.com/reference-guides/cluster-configuration)

The following table summarizes the options and settings available for each cluster type:

| Action | Rancher Launched Kubernetes Clusters | EKS, GKE and AKS Clusters 1 | Other Hosted Kubernetes Clusters | Non-EKS or GKE Registered Clusters |
| --- | --- | --- | --- | --- |
| [Using kubectl and a kubeconfig file to Access a Cluster](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/manage-clusters/access-clusters/use-kubectl-and-kubeconfig) | ✓ | ✓ | ✓ | ✓ |
| [Managing Cluster Members](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/manage-clusters/access-clusters/add-users-to-clusters) | ✓ | ✓ | ✓ | ✓ |
| [Editing and Upgrading Clusters](https://ranchermanager.docs.rancher.com/reference-guides/cluster-configuration) | ✓ | ✓ | ✓ | ✓2 |
| [Managing Nodes](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/manage-clusters/nodes-and-node-pools) | ✓ | ✓ | ✓ | ✓3 |
| [Managing Persistent Volumes and Storage Classes](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/manage-clusters/create-kubernetes-persistent-storage) | ✓ | ✓ | ✓ | ✓ |
| [Managing Projects, Namespaces and Workloads](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/manage-clusters/projects-and-namespaces) | ✓ | ✓ | ✓ | ✓ |
| [Using App Catalogs](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/helm-charts-in-rancher) | ✓ | ✓ | ✓ | ✓ |
| Configuring Tools ([Alerts, Notifiers, Monitoring](https://ranchermanager.docs.rancher.com/integrations-in-rancher/monitoring-and-alerting), [Logging](https://ranchermanager.docs.rancher.com/integrations-in-rancher/logging), [Istio](https://ranchermanager.docs.rancher.com/integrations-in-rancher/istio)) | ✓ | ✓ | ✓ | ✓ |
| [Running Security Scans](https://ranchermanager.docs.rancher.com/how-to-guides/advanced-user-guides/compliance-scan-guides) | ✓ | ✓ | ✓ | ✓ |
| [Ability to rotate certificates](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/manage-clusters/rotate-certificates) | ✓ | ✓ |  |  |
| Ability to [backup](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/backup-restore-and-disaster-recovery/back-up-rancher-launched-kubernetes-clusters) and [restore](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/backup-restore-and-disaster-recovery/restore-rancher-launched-kubernetes-clusters-from-backup) Rancher-launched clusters | ✓ | ✓ |  | ✓4 |
| [Cleaning Kubernetes components when clusters are no longer reachable from Rancher](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/manage-clusters/clean-cluster-nodes) | ✓ |  |  |  |

1.   Registered EKS, GKE and AKS clusters have the same options available as EKS, GKE and AKS clusters created from the Rancher UI. The difference is that when a registered cluster is deleted from the Rancher UI, it is not destroyed.

2.   Cluster configuration options can't be edited for registered clusters, except for [K3s and RKE2 clusters.](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/kubernetes-clusters-in-rancher-setup/register-existing-clusters)

3.   For registered cluster nodes, the Rancher UI exposes the ability to cordon, drain, and edit the node.

4.   For registered clusters using etcd as a control plane, snapshots must be taken manually outside of the Rancher UI to use for backup and recovery.
