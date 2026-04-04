# Source: https://docs.sonarsource.com/sonarqube-server/8.9/project-administration/managing-applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/project-administration/managing-applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/project-administration/managing-applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/project-administration/managing-applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/project-administration/managing-applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/project-administration/managing-applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/project-administration/managing-applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/project-administration/managing-applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/project-administration/managing-applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/project-administration/managing-applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/project-administration/managing-applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/project-administration/managing-applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/project-administration/managing-applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/project-administration/managing-applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration/managing-applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/project-administration/managing-applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration/managing-applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/managing-applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/managing-applications.md

# Managing applications

### Permissions <a href="#permissions" id="permissions"></a>

#### Creating applications <a href="#creating-applications" id="creating-applications"></a>

Both users with the **Create Applications** permission and global administrators can create applications:

* **Create Applications permission** – Users with the **Create Applications** permission (granted at the global level at **Administration** > **Security** > **Global Permissions**) can create applications by clicking the **Create Application** button in the upper-right corner of the **Projects** homepage.
* **Global Administrators** – In addition to creating applications from the **Projects** homepage, global administrators (with the global **Administer System** permission granted at **Administration** > **Security** > **Global Permissions**) can create applications from the overall portfolio administration interface at **Administration** > **Configuration** > **Portfolios**.

#### Editing Applications <a href="#editing-applications" id="editing-applications"></a>

Users need to have either **Administer** permissions for any applications that they want to edit (set on the specific application’s page at **Application Settings** > **Permissions**) or the global **Administer System** permission.

{% hint style="info" %}
Users with **Administer** permissions for an application can see the list of projects that make up the application even if they don’t have browse permissions for those projects.
{% endhint %}

#### Changing the PDF report frequency <a href="#changing-the-pdf-report-frequency" id="changing-the-pdf-report-frequency"></a>

As an application administrator, you can change the PDF report subscription frequency of the application:

1. Retrieve the application.
2. Select **Application Settings** > **Application Report Settings**, and select an option from the **Application Reports Frequency** drop-down menu.

You have the following options for subscription frequency:

* **Daily**
* **Weekly**
* **Monthly (default)**

### Populating applications <a href="#populating-applications" id="populating-applications"></a>

Once your application exists, you can populate it with manually selected projects. By default, the configuration interface shows the list of projects currently selected for the application. To add additional projects, choose the **Unselected** or **All** filter.

### Creating Application Branches <a href="#creating-application-branches" id="creating-application-branches"></a>

Once your application is populated with projects, you can create application branches by choosing branches from the application’s component projects. This option is available in the application’s **Application Settings** > **Edit Definition** interface or from the global administration interface.

### Calculation <a href="#calculation" id="calculation"></a>

By default, applications are queued to be recalculated after each analysis of an included project. For each relevant application, a **Background Task** is created, and you can follow the progress on each in the **Administration** > **Projects** > **Background Tasks** by looking at the logs available for each item.

### Reindexing <a href="#reindexing" id="reindexing"></a>

During Elasticsearch reindexing due to disaster recovery or upgrading, applications become available as they are indexed. See [reindexing](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/maintenance/reindexing "mention") for more information.
