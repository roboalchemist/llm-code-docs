# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/export-and-import-agents.md

# Export and import agents

You can create a backup copy of your agent in your local system using the **Backup & Export** option. Later, you can use the exported copy and **import** it into any existing agent in any account. &#x20;

When you export an agent, an exact snapshot of the agent at that point in time is exported to a ZIP file. The following lists a few use cases of this feature:

* Import to an existing agent within the same company
* Import to an existing agent of a different company&#x20;
* Import an agent when you wish to create a new similar agent&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M4wZkp-AIqDEwoNxhIH%2F-M4w_OzHjbdl1ixvUKsa%2Fagent-backup-export.png?alt=media\&token=c0145b08-2cbe-4d63-9edc-d7a54ab1ee91)

{% hint style="info" %}
**Notes:**

* **Backup & export** option is available only in the Development stage of the agent life-cycle and only when you have at least view permission on the agent. See [Roles and permissions](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions), for more information.
* **Import to agent** option is available in the Development stage of the agent life-cycle and only when you have at least edit permission on the agent. See [Roles and permissions](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions), for more information.
* Importing the agent creates an exact copy of the exported agent. Hence, all the existing details in the imported agent are entirely replaced. (except those listed in [What agent details are not imported?](#what-agent-details-are-not-imported))
* Import and export work only in the same version of the platform. This implies that you cannot export your agent in 5.1 and import it in the 5.2 version or you cannot export an agent in 5.2 and import it back to the 5.1 version.
* You can export and import agents upto a maximum size of 4 GB.
  {% endhint %}

## How does it work?

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M4wZkp-AIqDEwoNxhIH%2F-M4w_W0BjZ346qoj1NAF%2Fagent-import-export.gif?alt=media\&token=a7dc952a-9127-425f-95fc-54d98f026d94)

### **Export an agent**

* In the **Agents -> Development** tab, click three ellipse dots in the **Actions** column of the agent to view the extended menu and click **Backup & Export.**&#x20;
* If the agent is getting exported for the first time, then the following pop-up is displayed. Click "Export Zip" to export a fresh copy of the agent.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FEdrXsnAaCW3A0izXE3Uf%2FScreenshot%202025-12-22%20at%2010.52.45%E2%80%AFAM.png?alt=media\&token=8057e54b-3689-4cb2-89ad-81f9e6424acc)

* You can exclude the LLaMB skill from the export by clearing the checkbox.
* If the agent has already been exported before, then in the pop-up message, the following details are displayed:

  * "First name" and "Last name" of the user who last exported the agent
  * Timestamp of when the agent was last exported
  * A link to download the last exported zip file&#x20;

  You can either download the last exported zip file or click "Export Zip" to export the agent.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FLnY0DNbGaoNrE0O6coUt%2FScreenshot%202025-12-22%20at%2010.51.23%E2%80%AFAM.png?alt=media\&token=504c6181-cc9c-417a-b583-ecdea37dddda)

* When you click "Export zip", a zip file of the agent "<\<agent\_name>>\_<\<agent\_id>>\_<\<timestamp>>.zip" is downloaded to your local system. The zip file is a collection of files (JSON, images) of the agent as available at that point in time.&#x20;

### **Import an agent**

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).

* You can import to an agent immediately after creating an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.

* If you wish to edit an agent, then:
  * In the Avaamo Platform UI, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/..#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing.
    {% endhint %}

* In the **Agents -> Skills** page, click **Import to agent** option.

* Browse the exported zip file and click **Open**. In the import message, click **OK** to import.

* An exact copy of the exported agent is created in the agent. See [What agent details are not imported?](#what-agent-details-are-not-imported) for more information.

## What agent details are not imported?

The following lists the agent items or configurations that are not imported from the source to the target agent:

* Answers skill. Also note that if the target agent has answer skills, they are cleared after import.
* Live-agent settings
* Channel configuration
* Permissions
* Notification settings and Personas
* Environment variables: Copied if the target agent does not have any environment variables.
* Details available in Debug, Test, Monitor, and Learning

{% hint style="info" %}
**Notes**: For the items or configurations that are copied from source to target, the existing details in the target agent are cleared out and completely replaced with the details of the source except for a few items such as Web channel and environment variables.
{% endhint %}
