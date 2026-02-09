# Source: https://docs.sonarsource.com/sonarqube-server/8.9/project-administration/project-existence.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/project-administration/project-existence.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/project-administration/project-existence.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/project-administration/project-existence.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/project-administration/project-existence.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/project-administration/project-existence.md

# Project existence

Typically, projects are created during their first analysis and never deleted (because old software never dies). For atypical situations, there is the page at **Administration > Projects > Management**, which allows you to manage project existence.

### How do I provision a project before its first analysis? <a href="#how-do-i-provision-a-project-before-its-first-analysis" id="how-do-i-provision-a-project-before-its-first-analysis"></a>

Provisioning a project allows you to declare and configure it (define permissions, set quality profiles, etc.) before running the first analysis. To be able to provision projects, you have to be logged in and be granted the **Provision Projects** permission.

To provision a new project, either go to the **Projects** page and select **Create Project**, or go to **Administration > Projects > Management** and select **Create Project**.

Once the project is provisioned, you can configure it (define permissions, set quality profiles, etc.), and when you’re finished with the configuration, you can simply run the project’s first analysis.

You can also provision and configure projects using the Web API.

### How do I find provisioned projects (that haven’t been analyzed yet)? <a href="#how-do-i-find-provisioned-projects-that-havent-been-analyzed-yet" id="how-do-i-find-provisioned-projects-that-havent-been-analyzed-yet"></a>

The **Projects Management** search interface includes a toggle to allow you to narrow your results on this page to only projects that have never been analyzed. From there you can deal with them on this page as a set, or click through to the individual project homepages for individual attention and administration.

### How do I lock down permissions on a project? (Private vs Public) <a href="#how-do-i-lock-down-permissions-on-a-project-private-vs-public" id="how-do-i-lock-down-permissions-on-a-project-private-vs-public"></a>

By default, any newly created project will be public. It means every SonarQube user, authenticated or not, will be able to:

* **Browse**: Access a project, browse its measures and issues, and perform some issue edits (confirm, assign, comment).
* **See Source Code**: View the project’s source code.

If you want to be sure only a limited list of groups and users can see the project, you need to mark it Private. Once a project is private you will be able to define which groups and users can **Browse** the project or **See Source Code**.

If you want all newly created projects to be private, you can change the default visibility in **Administration > Projects > Management**.

### How do I delete projects? <a href="#how-do-i-delete-projects" id="how-do-i-delete-projects"></a>

A project may be deleted individually from the **Administration** page of the project. See [project-settings](https://docs.sonarsource.com/sonarqube-server/10.2/project-administration/project-settings "mention") for more details. To delete projects in bulk, use **Administration > Projects > Management**. Here you can select the projects to delete. A deleted project is gone for good, there is no way to undo this action.

### How do I find projects that are no longer analyzed? <a href="#how-do-i-find-projects-that-are-no-longer-analyzed" id="how-do-i-find-projects-that-are-no-longer-analyzed"></a>

The **Projects Management** search interface includes a date picker to help you find all projects last analyzed before your specified date. From there you can deal with them on this page as a set, or click through to the individual project homepages for individual attention and administration.

In **Administration** > **Projects** > **Management** search for **Last analysis before** to filter projects not analyzed since a specific date. Then use bulk **Delete** to remove the projects that match your filter.

This can be automated by using the corresponding Web API: `api/projects/bulk_delete?analyzedBefore=YYYY-MM-DD`.

Note that projects that are not analyzed for seven consecutive days are considered inactive, and SonarQube automatically deletes their cached data to free space in the database. See [branch-analysis](https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/branches/branch-analysis "mention") for more information on inactive branches and cached data.
