# Source: https://docs.sonarsource.com/sonarqube-server/8.9/instance-administration/project-move.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/instance-administration/project-move.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/project-move.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/instance-administration/project-move.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/instance-administration/project-move.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/instance-administration/project-move.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/project-move.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/project-move.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/project-move.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/project-move.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/project-administration/project-move.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/project-administration/project-move.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/project-administration/project-move.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/project-administration/project-move.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration/project-move.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/project-administration/project-move.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration/project-move.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/maintaining-project/project-move.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/maintaining-project/project-move.md

# Project move

To use **Project Move**, you must have **Administer** permission rights on the project in the source instance and access to the file systems of both instances.

When you move a project from a source to a target instance, all project data are moved except:

* Source code
* Issue assignments
* Security reports

### When to use project move <a href="#when-to-use-project-move" id="when-to-use-project-move"></a>

**Project Move** can help you with the following situations:

* You want to create a central SonarQube Server instance at the enterprise level and you want to keep the history created on instances used previously at the team level.
* You want to consolidate your editions and move projects from a SonarQube Community Build instance to an [Enterprise Edition](https://www.sonarsource.com/plans-and-pricing/enterprise/) instance or above.
* Your company is acquiring another company that already has a central SonarQube Server instance.
* You are at a large company with several SonarQube Server instances and an application is transferred from one team to another.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

* The project to be moved has never been analyzed on the target instance.
* The target instance must be [Enterprise Edition](https://www.sonarsource.com/plans-and-pricing/enterprise/) or above.
* The source instance can be a SonarQuber Server or a SonarQube Community Build instance.
* Both source and target instances must have:
  * If your source instance is a SonarQube Server instance: the exact same SonarQube Server version.
  * The same custom metrics.
  * The same custom rules
* The target instance must have all the plugins of the source instance, with the same versions.\
  If your source instance has plugins that aren’t in your target instance, either remove them and reanalyze your project or add them to your target instance.

### Preliminary step if moving from a SonarQube Community Build instance <a href="#if-moving-from-sonarqube-community-build" id="if-moving-from-sonarqube-community-build"></a>

If your source instance is a SonarQube Community Build instance, a preliminary step is necessary before performing Step 1 to Step 3 below:

* Create a new SonarQube Server Enterprise Edition of the same version as the target instance from the database of your SonarQube Community Build instance (no license is required). This Enterprise Edition instance becomes your source instance.

### Step 1: Export the source project to a ZIP file <a href="#export-to-zip" id="export-to-zip"></a>

On the source instance (if the source instance was originally a SonarQube Community Build instance, go directly to 3.):

1. Review the branches of the project by navigating to **Project Settings** > **Branches & Pull Requests** and enable **Keep when inactive** for each branch you want to keep. Note that pull requests are not saved when exporting a project.
2. Reanalyze the project one last time for each branch that has enabled the **Keep when inactive** option to ensure it is populated with data corresponding to your current SonarQube Server installation.
3. Navigate to the project and at the project level, choose **Project Settings** > **Import / Export**.
4. Click on the **Export** button to generate a ZIP file containing the settings and history of your project (but not the source code). Note that if you need to change the project’s key, you must do it before performing the export.

A zip file containing all project data is generated in a file named:

`<sonarqubeHome>/data/governance/project_dumps/export/<project_key>.zip`

where \<sonarqubeHome>:

* For a ZIP installation: is the location where the SonarQube Server distribution has been unzipped.
* For a Docker installation: is the installation directory of SonarQube Server within your container. This path is stored in the SONARQUBE\_HOME environment variable.

If the source instance is a Data Center Edition instance, the ZIP file is generated on the application node that processed the export. You have to find out which one to copy the ZIP file from there.

### Step 2: Create the target project and import the ZIP file <a href="#import-zip-file" id="import-zip-file"></a>

The procedure is different depending on the target instance edition.

<details>

<summary>Enterprise Edition</summary>

On the target instance:

1\. With a user having the **Administer System** and **Create Projects** permission rights, go to **Administration** > **Projects** > **Management** and create the project using *the same key* the project had in the source instance. See [importing-repo](https://docs.sonarsource.com/sonarqube-server/project-administration/creating-your-project/importing-repo "mention") for more details.

2\. In the Clean as You Code setup step, select **Use the global settings**, the project import will take care of importing your former new code configuration.

3\. Configure the project’s permissions and the quality profiles and quality gate associated with the project.

{% hint style="warning" %}
Do not change anything else on the project’s configuration, otherwise the import might not work.
{% endhint %}

4\. Put the generated ZIP file into the directory `<sonarqubeHome>/data/governance/project_dumps/import/` (create this folder if it does not already exist).

5\. Go to the Project’s Home Page and choose **Project Settings** > **Import / Export**.

6\. Select **Import** to start importing your data.

7\. Monitor the import.

{% hint style="warning" %}
The SonarQube Server application will only read and open ZIP archives with a project key that matches the project key of a brand new, unanalyzed SonarQube Server project. Do not overlook the project key configuration when importing and exporting your project.
{% endhint %}

{% hint style="info" %}
If the import is successful, the ZIP file will automatically be deleted.
{% endhint %}

</details>

<details>

<summary>Data Center Edition</summary>

You can use one of the following methods:

**Scaling down your target instance to one application node**

1. Scale down your SonarQube Server instance to one application node:
   * Scale in the `-app` deployment to 1 replica only.
   * Manually update the replica, mounting it to the appropriate sub-directory.
2. Create and import the project on the target instance as explained above for the Enterprise Edition instance.
3. Scale the application nodes back up to the desired number.

**Importing the file to all application nodes**

Proceed as described above for an Enterprise Edition instance but in step 4, duplicate the export ZIP file onto `data/governance/project_dumps/import` **on all application nodes** of the target instance. Then, import the ZIP file as described in the following steps of the procedure.

{% hint style="info" %}
If the import is successful, one of the ZIP files will automatically be deleted. We recommend that you delete the ZIP files stored on the other application nodes.
{% endhint %}

</details>

### Step 3: Trigger an analysis on the moved project <a href="#trigger-analysis" id="trigger-analysis"></a>

The export ZIP file does not include source code and security reports. Once the import is finished, trigger an analysis to import source files into the new instance and generate security reports.

{% hint style="warning" %}
Note that if the import is done without SCM data, the code will be considered new code and the analysis may provide imprecise results.
{% endhint %}
