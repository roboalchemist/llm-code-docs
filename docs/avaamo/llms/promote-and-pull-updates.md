# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/promote-and-pull-updates.md

# Promote and pull updates

As the agent goes through different stages in its life cycle, you can promote agents from one stage to another using the **Promote** option. See [Promote an agent](#promote-an-agent), for more information.

Similarly, when you make certain changes in the previous stage of the life cycle, you use the **Pull updates** option to pull the updates from the previous stage to the current stage. See [Pull updates](#pull-updates), for more information.

{% hint style="info" %}
**Notes**:

* See [Plan your development process (Agent life cycle)](https://docs.avaamo.com/user-guide/how-to/plan-your-development-process-agent-life-cycle), for more information
* Promote and Pull updates options are specific to the roles and permissions defined for each user. See [Roles and permissions](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions), for more information.
  {% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M3dTeDF4yj4aVklUj6y%2F-M3dUp3DgX5LO9naFJBQ%2Fagent-promote-pull.png?alt=media\&token=0998530a-672d-49af-b92a-62d183ad9673)

### Promote an agent

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M3dbFDzFk01RgyS8E0k%2F-M3ddZMetDgDRn_Wzejv%2Fagent-promote-pull.gif?alt=media\&token=7331b856-9939-402a-b502-3f6bcb4b682a)

* In the **Agents** page, click the **Stage** tab (Development, Testing, Staging) from where you wish to promote the agent.&#x20;
* Click three ellipse dots in the **Actions** column of the agent to view the extended menu and click **Promote.**&#x20;
* If there are users editing the agent, then the following message with a list of the users and the module being edited by the user is displayed. You can review the current changes in progress and decide to either cancel promoting or click **Next** to continue promoting the agent to the next stage.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FnHUtfpUSk7TUFjRaqcko%2F6.3-promote-message.png?alt=media&#x26;token=e21140dd-ac76-407b-a3f0-b2432b443883" alt=""><figcaption></figcaption></figure>

* The following pop-up message is displayed. Type **accept** in the confirmation message box and click **Accept** to complete promoting the agent from the current stage to the next stage. Click **Cancel** if you wish to decline the changes and not proceed with the promotion.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FvByiVtcgBBBNTf9sQkuZ%2Fimage.png?alt=media\&token=c1be4770-3691-4555-a24b-565a07eb0ce4)

* When an agent is promoted to the next stage,
  * The user who promoted the agent is the agent's owner in the promoted stage. As the agent's owner, you can also add other team members as needed.
  * The first step as an owner of the agent in any stage is to configure the agent with variables specific to the environment. See [Define environment variables](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-environment-variables), for more information.
  * An exact clone of the agent is created in the promoted environment. Users with the required roles can work on the agent in the promoted environment without affecting the agent in other stages.&#x20;

{% hint style="info" %}
**Note**: An agent can be promoted from one stage to another only once. Once promoted, you cannot revert the operation. However, you can delete the promoted agent and promote it again from its previous stage.
{% endhint %}

### Pull updates

* In the **Agents** page, click the tab (Testing, Staging, Production) from where you wish to pull updates to the agent.&#x20;
* Click three ellipse dots in the **Actions** column of the agent to view the extended menu and click **Pull updates.**

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fp9WqI5p9gJFT0K5SEDcY%2Fimage.png?alt=media\&token=200e3dc2-0c67-4230-a995-dcdda09f161d)

* If users are editing the agent, a message with a list of users and the module being edited by each user is displayed. You can review the current changes in progress and decide to either cancel pulling the updates or click **Next** to continue to pulling updates from the previous stage.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FHQ0SQpn7kLrT2c7Pox04%2F6.3-pull-message.png?alt=media&#x26;token=7a880772-71d4-45ae-9a22-33d51e41f7d1" alt=""><figcaption></figcaption></figure>

* The **Pulling updates** pop-up window is displayed. In this window, you can view a high-level summary of the agent changes that will be pulled from the previous stage to the current stage.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FG4fr7PqtPOJ1z8qIhwrr%2Fimage.png?alt=media\&token=a92f0311-14ab-4e8e-8eb2-e98abb72ef54)

* Each update is categorized as Created, Updated, or Deleted - to help you easily identify the type of change. Against each category, you can view a count of the updates made.&#x20;
* For [AI agents](https://docs.avaamo.com/user-guide/ai-agent), the [Advanced Options](#advanced-options) section allows you to select from a list of added or modified knowledge skills to pull specific updates.
* Click **Download CSV** to download a detailed summary of the updates in CSV format. This helps you to analyze the changes further.&#x20;
* After verifying all changes, type accept in the confirmation message box, then click Accept to complete pulling updates from the previous stage to the current stage.&#x20;
* &#x20;Click **Cancel** to decline the changes and not proceed with pull updates.

{% hint style="success" %}
**Key points**:&#x20;

* Currently, changes in the following Configuration pages are not displayed in the **Pull updates** window: Settings, Channel, Live chat agent, Persistent menu, and Custom feedback.
* The Pull Updates window provides a summary of changes in the agent between two environments. However, if you wish to audit in-depth details, you can refer to the [Changelog API - V2](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/change-log-apis/changelog-api-v2).
* When you pull changes from the source stage to the current stage, the Auto Sync settings are **not** pulled. For exampl&#x65;**,** If you change the Auto Sync option in the source stage and pull it into the current stage, the current stage’s Auto Sync configuration remains unchanged.
  {% endhint %}

### Advanced options

The `Advanced Options` section provides a detailed list of all added or modified LLaMB content. From this list, you can choose exactly which updates you want to pull, giving you more control over the update process.

The changes are categorized as follows:

* **To be created**: Newly added LLaMB skills
* **To be updated**: Existing LLaMB skills that have been modified

All checkboxes in this section are selected by default during knowledge skill pull updates, reducing manual effort.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FbpLZgAt9NRfEsRJQXS7U%2FScreenshot%202025-11-18%20at%2012.53.44%E2%80%AFPM.png?alt=media&#x26;token=7a6bf50e-3c55-494a-b48e-2fe063cbd173" alt=""><figcaption></figcaption></figure>

### What is not promoted or pulled?

The following lists the items or configurations that are not promoted or pulled from the source to the target agent:

* The agent's name and description are used primarily to identify the agent at a specific stage.
* Channel configuration
* Permissions
* Notification settings and Personas
* Details available in Debug, Test, Monitor, and Learning
* Only the following Live agent Automated messages are pulled:&#x20;
  * Switch to Live Agent Message&#x20;
  * Switch to Agent Message&#x20;
  * Working hours
  * Callback messages

{% hint style="info" %}
**Notes**:&#x20;

* A few items, such as environment variables and web channel configurations, are promoted only the first time, as this helps progress faster through the agent life-cycle stages, rather than recreating them manually. In subsequent pulls, as it can overwrite existing data, certain items may not be pulled from the previous stage.
* When the updates are pulled, for those items that are promoted or pulled from one stage to another, the changes from source agents are copied and overwritten into the target agent.&#x20;
* For the items or configurations that are not promoted or pulled, the changes in the target agent are retained.&#x20;
  {% endhint %}
