# Source: https://learn.microsoft.com/en-us/azure/devops/server/admin/admin-quick-ref

Title: What are the administrative tasks? - Azure DevOps

URL Source: https://learn.microsoft.com/en-us/azure/devops/server/admin/admin-quick-ref

Markdown Content:
**Azure DevOps Server |Azure DevOps Server |Azure DevOps Server 2022 | Azure DevOps Server 2020**

Use this index to quickly access information about tasks for managing Azure DevOps on-premises servers.

Install, upgrade, and general admin tasks
-----------------------------------------

*   [Install get started](https://learn.microsoft.com/en-us/azure/devops/server/install/get-started?view=azure-devops-server)
*   [Install SQL Server](https://learn.microsoft.com/en-us/azure/devops/server/install/sql-server/install-sql-server?view=azure-devops-server)
*   [Upgrade get started](https://learn.microsoft.com/en-us/azure/devops/server/upgrade/get-started?view=azure-devops-server)
*   [Upgrade TFS Express](https://learn.microsoft.com/en-us/azure/devops/server/upgrade/express?view=azure-devops-server)
*   [Open the Administration Console](https://learn.microsoft.com/en-us/azure/devops/server/admin/open-admin-console?view=azure-devops-server)

Server-level administrative tasks
---------------------------------

Members of the [Azure DevOps Server Administrators group](https://learn.microsoft.com/en-us/azure/devops/server/admin/add-administrator?view=azure-devops-server) are tasked with server maintenance and configuring resources for all project collections. They also can perform all tasks to administer projects, collections and server instances.

Many tasks are performed from the Azure DevOps Server Administration Console. The main task they perform from the web portal is to [set access levels for a user or security group](https://learn.microsoft.com/en-us/azure/devops/organizations/security/change-access-levels?toc=/azure/devops/server/toc.json&bc=/azure/devops/server/breadcrumb/toc.json).

### Manage users and access

*   [Add administration console users](https://learn.microsoft.com/en-us/azure/devops/server/admin/add-administrator?view=azure-devops-server)
*   [Add server-level administrators](https://learn.microsoft.com/en-us/azure/devops/server/admin/add-administrator?view=azure-devops-server)
*   [Change access levels](https://learn.microsoft.com/en-us/azure/devops/organizations/security/change-access-levels)
*   [Set up groups for use in Azure DevOps deployments](https://learn.microsoft.com/en-us/azure/devops/server/admin/setup-ad-groups?view=azure-devops-server)

### Server configuration

*   [Change cache settings for an application-tier server](https://learn.microsoft.com/en-us/azure/devops/server/admin/change-caching-app-tier?view=azure-devops-server)
*   [Change SSH Settings](https://learn.microsoft.com/en-us/azure/devops/server/admin/websitesettings?view=azure-devops-server)
*   [Configure an SMTP server](https://learn.microsoft.com/en-us/azure/devops/server/admin/setup-customize-alerts?view=azure-devops-server)
*   [Customize email for alerts and feedback requests](https://learn.microsoft.com/en-us/azure/devops/server/admin/setup-customize-alerts?view=azure-devops-server)
*   [View or change the Public URL](https://learn.microsoft.com/en-us/azure/devops/server/admin/open-admin-console?view=azure-devops-server#public-url)

### Server maintenance

*   [Change the service account or password for TFS](https://learn.microsoft.com/en-us/azure/devops/server/admin/change-service-account-password?view=azure-devops-server)
*   [Change cache settings for an application-tier server](https://learn.microsoft.com/en-us/azure/devops/server/admin/change-caching-app-tier?view=azure-devops-server)
*   [Stop and start services, application pools, and websites](https://learn.microsoft.com/en-us/azure/devops/server/admin/stop-start-services-pools?view=azure-devops-server)

### Manage databases

*   [Back up and restore](https://learn.microsoft.com/en-us/azure/devops/server/admin/backup/back-up-restore?view=azure-devops-server)
*   [Configure a backup schedule and plan](https://learn.microsoft.com/en-us/azure/devops/server/admin/backup/config-backup-sched-plan?view=azure-devops-server)
*   [Understand backing up Azure DevOps on-premises](https://learn.microsoft.com/en-us/azure/devops/server/admin/backup/backup-db-architecture?view=azure-devops-server)

Project collection administrative tasks
---------------------------------------

Members of the [Project Collection Administrators group](https://learn.microsoft.com/en-us/azure/devops/security/set-project-collection-level-permissions?toc=/azure/devops/server/toc.json&bc=/azure/devops/server/breadcrumb/toc.json) are tasked with configuring resources for all projects defined for a collection. They also can perform all tasks to add projects, manage projects, and manage permissions for the collection, a project, or an object.

Before you add a a project or project collection, review the information provided in [About projects and scaling your organization](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/about-projects).

### Add and manage project collections

*   [Add a project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/create-project)
*   [Add a project collection](https://learn.microsoft.com/en-us/azure/devops/server/admin/manage-project-collections?view=azure-devops-server)
*   [Delete/detach a project collection](https://learn.microsoft.com/en-us/azure/devops/server/admin/manage-project-collections?view=azure-devops-server)
*   [Add collection-level administrators](https://learn.microsoft.com/en-us/azure/devops/organizations/security/set-project-collection-level-permissions)
*   [Manage collection-level notifications](https://learn.microsoft.com/en-us/azure/devops/organizations/notifications/manage-team-group-global-organization-notifications)
*   [Move a project collection](https://learn.microsoft.com/en-us/azure/devops/server/admin/move-project-collection?view=azure-devops-server)
*   [Open the Administration Console](https://learn.microsoft.com/en-us/azure/devops/server/admin/open-admin-console?view=azure-devops-server)
*   [Split a project collection](https://learn.microsoft.com/en-us/azure/devops/server/admin/split-team-project-collection?view=azure-devops-server)

### Boards/Process and work tracking customizations

*   [Customize your work tracking experience](https://learn.microsoft.com/en-us/azure/devops/reference/customize-work)
*   [On-premises XML process model](https://learn.microsoft.com/en-us/azure/devops/reference/on-premises-xml-process-model)
*   [About process customization and inherited processes](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/work/inheritance-process-model)
*   [Customize a project](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/work/customize-process)
*   [Add and manage processes](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/work/manage-process)

### Analytics

*   [Enable or install Analytics](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/analytics-extension)

### Extensions

*   [Install and manage Marketplace extensions](https://learn.microsoft.com/en-us/azure/devops/marketplace/install-extension)
*   [Approve extensions](https://learn.microsoft.com/en-us/azure/devops/marketplace/approve-extensions)
*   [Assign paid extension access to users](https://learn.microsoft.com/en-us/azure/devops/marketplace/assign-paid-extensions)
*   [Grant permissions to manage extensions](https://learn.microsoft.com/en-us/azure/devops/marketplace/how-to/grant-permissions)
*   [Uninstall or disable extensions](https://learn.microsoft.com/en-us/azure/devops/marketplace/uninstall-disable-extensions)

### Pipelines, Build and release, Agent pools, Deployment pools

*   [Set retention policies](https://learn.microsoft.com/en-us/azure/devops/pipelines/policies/retention)
*   [Set resource limits for pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/licensing/concurrent-pipelines-ts)
*   [Add and manage agent pools](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/pools-queues)
*   [Add and manage deployment pools](https://learn.microsoft.com/en-us/azure/devops/pipelines/release/deployment-groups/index)

Project administrative tasks
----------------------------

Members of the [Project Administrators group](https://learn.microsoft.com/en-us/azure/devops/security/set-project-collection-level-permissions?toc=/azure/devops/server/toc.json&bc=/azure/devops/server/breadcrumb/toc.json) are tasked with configuring resources for a project and managing permissions at the project-level. Members of the Project Collection Administrators group can configure project and team settings as well. See also [Get started as an administrator](https://learn.microsoft.com/en-us/azure/devops/user-guide/project-admin-tutorial?toc=/azure/devops/server/toc.json&bc=/azure/devops/server/breadcrumb/toc.json).

### Manage users and permissions

*   [Add users to a project](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-users-team-project)
*   [Add project administrators](https://learn.microsoft.com/en-us/azure/devops/organizations/security/set-project-collection-level-permissions)
*   [Change access levels to specific functions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/change-access-levels)
*   [Grant or restrict access to select features](https://learn.microsoft.com/en-us/azure/devops/organizations/security/restrict-access)
*   [Set build and release permissions](https://learn.microsoft.com/en-us/azure/devops/pipelines/policies/set-permissions)

### Manage projects

*   [Change service visibility](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-services)
*   [Connect to projects](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/connect-to-projects)
*   [Configure a project portal](https://learn.microsoft.com/en-us/previous-versions/azure/devops/report/sharepoint-dashboards/share-information-using-the-project-portal)
*   [Configure service hooks](https://learn.microsoft.com/en-us/azure/devops/service-hooks/index)
*   [Delete a project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/delete-project)
*   [Rename a project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/rename-project)
*   [Restore a project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/restore-project)
*   [Save project data](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-azdo)

### Manage teams and project configuration

*   [Add a team](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/add-teams)
*   [Add a team administrator](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/add-team-administrator)
*   [Define area paths](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-area-paths)
*   [Define iteration paths or sprints](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-iteration-paths-sprints)
*   [Set default dashboard permissions](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/dashboard-permissions)
*   [Manage project-level notifications](https://learn.microsoft.com/en-us/azure/devops/organizations/notifications/manage-team-group-global-organization-notifications)

### Wiki

*   [Create a wiki for your project](https://learn.microsoft.com/en-us/azure/devops/project/wiki/wiki-create-repo)
*   [Publish a Git repository to a wiki](https://learn.microsoft.com/en-us/azure/devops/project/wiki/publish-repo-to-wiki)
*   [Manage README and Wiki permissions](https://learn.microsoft.com/en-us/azure/devops/project/wiki/manage-readme-wiki-permissions)

### Pipelines, Build and release, Agent Pools

*   [Manage Agent queues and agent pools](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/pools-queues)
*   [Manage service connections](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints)
*   [Manage deployment pools and groups](https://learn.microsoft.com/en-us/azure/devops/pipelines/release/deployment-groups/index)
*   [Set retention policies](https://learn.microsoft.com/en-us/azure/devops/pipelines/policies/retention)

### Repos, Code, version control

*   [Create additional Git repos](https://learn.microsoft.com/en-us/azure/devops/repos/git/creatingrepo)
*   [Manage repository permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/set-git-tfvc-repository-permissions)
*   [Manage branch policies](https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies)
*   [Add TFVC Check-In Policies](https://learn.microsoft.com/en-us/azure/devops/repos/tfvc/add-check-policies)
*   [Manage TFVC file types](https://learn.microsoft.com/en-us/azure/devops/server/admin/manage-file-types?view=azure-devops-server)

### Test plans, Test

*   [Set test retention policies](https://learn.microsoft.com/en-us/azure/devops/test/how-long-to-keep-test-results)
*   [Manage test-related permissions at project level](https://learn.microsoft.com/en-us/azure/devops/organizations/security/set-project-collection-level-permissions)
*   [Set area path-level test permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/set-permissions-access-work-tracking#create-child-nodes-modify-work-items-under-an-area-path)
