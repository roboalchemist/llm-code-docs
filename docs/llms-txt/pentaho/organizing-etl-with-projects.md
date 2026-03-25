# Source: https://docs.pentaho.com/pdia-data-integration/organizing-etl-with-projects.md

# Organizing ETL with projects

Use projects in Pentaho Data Integration (PDI) to store ETL workflow files and configurations in one place, including transformations, jobs, connections, and supporting content. Projects make ETL workflows easier to organize, share, and move between local systems, the Pentaho Repository, and virtual file systems (VFS). Regardless of PDI client (also called Spoon) configurations or project path variations, all users can consistently access the same files and settings for ETL workflows that are saved as a project. Additionally, because projects are isolated, you can safely reference transformations and jobs from other projects without creating configuration conflicts.

## What is a project?

A project is a self-contained folder that holds everything unique to a specific ETL workflow, which can include one or more of the following items:

* Transformation files (`.ktr`)
* Job files (`.kjb`)
* Variables
* Configurations such as database connections, VFS connections, and run configurations
* Data files used as input, or created as output, for transformations
* Scripts or auxiliary files referenced by jobs or transformations
* Documentation or notes relevant to the project

<figure><img src="https://773338310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYwnJ6Fexn4LZwKRHghPK%2Fuploads%2FFw6VY9FQOkUHw6EFQLuX%2Fimage.png?alt=media&#x26;token=a49abc27-3037-4912-bb57-ae52cec64893" alt="Screenshot of the PDI client that shows the new Projects dropdown list, project files in the View tab, and configurations for a project."><figcaption></figcaption></figure>

<table><thead><tr><th width="114.44439697265625">Item</th><th>Description</th></tr></thead><tbody><tr><td>1</td><td>Use the <strong>Projects</strong> list to switch between recently opened projects. You can also select <strong>&#x3C;No Project></strong> to close the currently open project.</td></tr><tr><td>2</td><td>Use <strong>Project Files</strong> in the <strong>View</strong> tab to manage every file, folder, and subfolder for a project. You can create, rename, delete, or move files and folders, directly from this list.</td></tr><tr><td>3</td><td>Use <strong>Configurations</strong> in the <strong>View</strong> tab to view and manage all of the configurations for the project, such as database connections, VFS connections, and run configurations. Notice that configurations appear shaded when another configuration with the same name and higher priority is active.</td></tr></tbody></table>

### Benefits of projects

When you use projects to manage your ETL workflows, you gain the following benefits and capabilities:

#### Manageability

* **Improved organization:** Consolidate files and configurations for the ETL workflow into a single logical container (the project folder) and use subfolders to organize your workflow.
* **Scalability:** Use multiple projects to segment and modularize integration work, making large ETL workflows easier to manage.
* **Visibility:** In the **View** tab, see **Project Files** and **Configurations** for better visibility and improved management of your project files, connections, schemas, and run configurations.
* **Quick switching:** Switch between all your open projects while you continue to work in the same location or between up to 10 recently opened projects when you change locations in the PDI client.
* **Portability:** Move a project folder (including all files and configurations) without losing the context for the project. You can transfer the project between your local system, a Pentaho Repository, or a VFS.

#### Flexible collaboration

* **Ease of sharing:** Share a project folder with other users and teams that need to review, contribute, or deploy the project. You can share a project folder as a ZIP file, upload it to a Pentaho Repository, save it in a shared VFS, or check it into a version control system.
* **Version control:** Commit the project folder to version control so you can track changes and preserve shared history for the project.

#### Configuration management and security

* **Isolated configurations:** Reduce conflicts by isolating ETL workflows in separate projects with their own unique configurations, connection parameters, and transformation strategies.
* **Enhanced security:** Isolate configurations at the project level to help protect sensitive information (for example, database credentials).
* **Configuration prioritization:** Define configurations at the appropriate level. When a configuration exists in multiple places, the PDI client uses the highest-priority version.
* **Backward compatibility:** Continue working with existing ETL workflow configurations until you are ready to migrate to projects. Projects are an optional feature. You can even execute transformations and jobs with a project context even if the target file lives outside the project.

### Configuration levels

Configurations are automatically applied in priority order to ensure the correct settings are used and to prevent unexpected conflicts. When a configuration exists in multiple locations, the PDI client applies the highest-priority version, reducing duplication and maintaining consistency for shared settings.

When configurations share the same name, the configuration at the highest level is applied. Configurations include connections, schemas, run configurations, slave servers, variables, and parameters.

Configurations are applied in the following priority order, from highest to lowest:

1. **Default:** A default configuration that cannot be edited or removed. **Example:** The **Pentaho local** run configuration.
2. **Project:** A configuration defined in the project that applies only to that project. Project-level configurations are only shown if you have an open project.
3. **System:** A configuration defined for projects in your local system. System-level configurations are not accessible to projects in a repository.
4. **Repository:** A configuration defined for projects in the connected repository. Repository-level configurations are not accessible to projects in your local system.
5. **(Deprecated) File:** File-level configurations have the lowest priority and can no longer be created. File-level configurations can only be edited or deleted. If you move a file with a file-level configuration into the Pentaho Repository, and the repository contains a configuration with the same name, a warning appears to indicate that the file configuration will overwrite the repository configuration.

## Creating projects&#x20;

You can create a project folder in any of the following locations:

* **Local file system:** A folder on your computer.
* **Pentaho Repository:** A folder in a connected Pentaho Repository.
* **VFS:** A folder in a supported VFS\* (for example, cloud storage) that the PDI client can access.&#x20;

  <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> Using folders in a VFS might affect performance.</p></div>

### Create a project

Create a new project when you want to work with all the files and settings for an ETL workflow in a self-contained project folder that you can port to other locations and share with other users.

To create a new project, complete the following steps:

1. Open the PDI client.
2. Click **Project** > **New Project**. The **New project** dialog box opens.
3. Enter a **Name** for the project.
4. To navigate to the **Project Path**, click **Browse**. The **Select a Folder** dialog box opens.
5. Select a folder for your project by taking one of the following actions:
   1. For an existing ETL workflow that you do not need to move, navigate to the root directory that contains every item in your workflow and select it.

      <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> If you have an existing ETL workflow that you want to move to a different location before selecting it as a project, see <a href="#move-a-project">Move a project</a>.</p></div>
   2. To create a new project for a new ETL workflow, navigate to the folder where you want to create the project, click the **Add folder** icon, and in the **Folder Name** dialog box enter a **New Folder Name** and click **OK**.&#x20;
6. Click **Open**.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Notes:</strong></p><ul><li>A project folder can contain only one project.</li><li>It is a recommended best practice to use the same name for the project and project folder.</li></ul></div>
7. In the **New project** dialog box, enter a **Description** for the project.
8. Click **OK**. The project is created and opened in the PDI client.

### Create folders in a project

Create folders within your project to organize transformations, jobs, configurations, and related content, making it easier to manage the project as it becomes more complex.

Create a folder in your project by completing the following steps:

1. Open the PDI client.
2. Click **Project** > **Open Project**. The **Select a Folder** window opens.
3. Search or browse to the project folder and then click **Open**. The project opens.
4. Click the **View** tab.
5. Expand **Project Files** and then navigate to the existing folder in which you want to create your new folder.
6. Right-click the existing folder and select **New Folder**.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> You can create a new folder in the project’s root folder by right-clicking <strong>Project Files</strong>.</p></div>
7. In the **Folder Name** dialog box, enter a folder name.
8. Click **OK**. The folder is created.

{% hint style="info" %}
**Note:** If your project is saved in a repository, you can also use the Repository Explorer to create a folder inside the project folder. For instructions, see [Use the Repository Explorer](https://docs.pentaho.com/pdia-data-integration/redirects/use-the-repository-explorer).
{% endhint %}

### Share a project

Use one of the following options to share your project with other users:

* Create the project in the Pentaho Repository or a shared VFS. See [Create projects](#create-projects).
* Move an existing project into a Pentaho Repository or shared VFS. See [Move a project](#move-a-project).
* Check the project folder into your organization’s version control system.
* Outside of the PDI client, save the project folder as a ZIP file and share it directly with another user. Projects shared as ZIP files can be opened in the recipient's chosen location. After the recipient saves the project to their chosen location, they can open it and then refresh the project by clicking **Project** > **Refresh Project**.

## Editing projects

You can edit a project's name or description, rename or delete folders in the project folder, or move the entire project folder.

### Edit project details

Edit a project details by completing the following steps:

1. Open the PDI client.
2. Click **Project** > **Open Project**. The **Select a Folder** window opens.
3. Search or browse to the project folder and then click **Open**. The project opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> You can have only one project open at a time.</p></div>
4. Click **Project** > **Project Details**. The **Project Details** window opens.
5. Update one or more of the following options:

   * **Name**
   * **Description**

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> You cannot edit the <strong>Project Path</strong>. To change the project path, move the project folder and then open the project from the new location.</p></div>
6. Click **OK**. The details for the project are updated.

### Edit a folder in a project

You can edit a folder in a project to change its name or delete it.

Edit a folder in a project by completing the following steps:

1. Open the PDI client.
2. Click **Project** > **Open Project**. The **Select a Folder** window opens.
3. Search or browse to the project folder and then click **Open**. The project opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> You can have only one project open at a time.</p></div>
4. Edit the folder by taking one of the following actions:
   * **Rename a folder**
     1. Click the **View** tab.
     2. Expand **Project Files** and then navigate to the folder you want to rename.
     3. Right-click the folder and select **Rename**.
     4. In the **Rename** dialog box, enter a new name and click **OK**.
   * **Delete a folder**
     1. Click the **View** tab.
     2. Expand **Project Files** and then navigate to the folder you want to delete.
     3. Right-click the folder and select **Delete**.
     4. Click **Yes** to confirm the deletion.

### Move a project

{% hint style="warning" %}
**Important:**&#x20;

* If you move a project, you must move the entire project and its contents.
* If you move individual files out of a project, such as transformation (.ktr) or job (.kjb) files, any references to other project items, such as database connections, will break.
* Before moving a project, close it in the PDI client.
  {% endhint %}

Projects can be moved between any of the following locations:

* **Local file system:** A folder on your computer.
* **Pentaho Repository:** A folder in a connected Pentaho Repository.
* **VFS:** A folder in a supported VFS (for example, cloud storage) that the PDI client can access.

  <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> Using folders in a VFS might affect performance.</p></div>
* To move a project folder in your local system, use your operating system’s file explorer or command line.
* To move a project folder into or out of the Pentaho Repository, see one of the following topics: [Use the Repository Explorer](https://docs.pentaho.com/pdia-data-integration/redirects/use-the-repository-explorer) or [Upload and download from the Pentaho Repository](https://app.gitbook.com/s/iFWuQjAZNxh1EoQbRnsT/administer/manage-the-pentaho-system/manage-the-pentaho-repository/upload-and-download-from-the-pentaho-repository).
* To move a project into or out of a VFS, use your VFS management tool or file system interface.

After you have moved a project to its new location, open the project and [refresh it](#refresh-project-data).

## Working with projects

You can switch between projects, refresh project data when it is modified outside of the PDI client, close a project, or migrate your existing ETL workflows into a project.

### Switch between projects

You can quickly switch between open or recently opened projects in the PDI client.

To switch projects, above the **View** and **Design** tabs, click the **Projects** list and select the project that you want to switch to.

#### How the Projects list works

* If you work in the same location, on your local system or in a connected repository, you can switch between all open projects.
* If you restart the PDI client or connect to or disconnect from the Pentaho Repository, the 10 most recently opened projects remain in the **Projects** list for each location. The PDI client keeps separate lists of the 10 most recently opened projects for the local system and each user in the Pentaho Repository.
* If a project is open, selecting another project closes the current project and opens the new one. Selecting **\<No Project>** closes the current project.
* If projects have the same name in the **Projects** list, each name shows the full path to help you tell them apart.
* If a project is moved, deleted, or on an inaccessible VFS, it does not appear in the **Projects** list.
* If a project is not in the **Projects** list, you must re-open it. See [Open a project](#open-a-project).

### Refresh project data

Refresh an open project when files are added, removed, or modified outside of the PDI client.

To refresh a project, click **Project** > **Refresh Project**.

To refresh configurations that were edited outside of the PDI client, click the **Refresh** icon.

### Close a project

With a project open, click **Project** > **Close Project**.

A warning is displayed if any open files in the project have unsaved changes.

As long as a project remains in the **Projects** list, its files are automatically restored the next time you open it.

## Project variables

Project variables are a way to store small pieces of information dynamically in a narrower scope than Kettle or environment variables. Project variables are loaded either when a project is opened or when a transformation or job in the project is opened in the PDI client or run in a scheduled task. Use project variables to define variables that apply only to the specific project.

{% hint style="warning" %}
**Important:** When variables are defined in multiple places, the last one applied overrides the others.
{% endhint %}

Variables are applied in the following order:&#x20;

1. Environment variables (JVM `-D` arguments from the JVM process)
2. Variables defined in `kettle.properties`&#x20;
3. Variables defined in `project.properties`&#x20;
4. Variables and parameters defined directly in the PDI client or in a scheduled job.
5. Variables set at runtime by steps such as `Set Variables` and `Set Session Variables`.

{% hint style="info" %}
**Note:** Internal variables are also available for transformations and jobs within a project. For details, see [Internal Variables](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/transforming-data-with-pdi-archive/pdi-run-modifiers/variables/internal-variables).
{% endhint %}

### Set project variables on your local system

To edit project variables for projects saved on your local system, complete the following steps:

1. Open the `project.properties` file in a text editor. By default, the `project.properties` file is stored in the project folder, inside the `.config` folder.
2. Edit the file and save it.
3. (Optional) If the project you set the variables for is open in the PDI client, you must close the project and reopen it for the new variable values to be applied.

### Set project variables in the Pentaho Repository

To edit project variables for projects saved in a Pentaho Repository:

1. Download the `project.properties` file from the project folder in the repository.
2. Open the `project.properties` file in a text editor.
3. Edit the file and save it.
4. Upload the edited `project.properties` file to the repository folder you downloaded it from.

{% hint style="info" %}
**Note:** The `project.properties` file uses the same format as the `kettle.properties` file. For details about `kettle.properties`, see [Kettle Variables](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/transforming-data-with-pdi-archive/pdi-run-modifiers/variables/kettle-variables).
{% endhint %}

### Project run modifier

You can use `-project` argument when executing a transformation or job to specify the path for a project. The path can be to a folder in the Pentaho Repository, in a VFS, or on your local system.
