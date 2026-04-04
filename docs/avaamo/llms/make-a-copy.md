# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/make-a-copy.md

# Make a copy

You can make a copy of your agent using the **Make a copy** option. When you copy an agent an exact clone of the agent is created.&#x20;

{% hint style="info" %}
**Notes**:

* This option is available only when you have at-least edit permission on the agent.
* This option is available only in the Development stage of the agent life-cycle.
* When you "Make a copy" of an agent, the cloned or copied agent is independent and does not have any references to the skills from the original agent. All copies of the skills in the cloned agent are independent copies.&#x20;
  {% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M3b66UFNSY6z8u22peQ%2F-M3b9VheVICre-J2oo1n%2Fagent-make-copy.png?alt=media\&token=14d8ec66-6412-4365-bbae-ac2e03a93a40)

**Make a copy** feature is useful in parallel development, where multiple developers can work on a single agent simultaneously. Avaamo suggests the approach of each developer having their copy of the agent when they have to develop and collaborate on a single agent. See [Best practices - Parallel Development](https://docs.avaamo.com/user-guide/ref/best-practices-parallel-development), for more information.

### How does it work?

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M3dPiC6wvbI9w6F-WDV%2F-M3dSGzbVLIxTpdoHxd3%2Fagent-copy.gif?alt=media\&token=f9290e5b-2c11-4104-9f3e-38017df514be)

* In the **Agents** page, click three ellipse dots in the **Actions** column of the agent to view the extended menu and click **Make a Copy.** &#x20;
* Click **OK** in the confirmation message.&#x20;
* An exact copy of the agent with the name **"**&#x43;opy of <\<agent\_name>>" is created in the **Agents** tab.&#x20;

### What agent details are not copied?

The following lists the items or configurations that are not copied from the original (source) to the copied (target) agent:

* Channel configuration
* Permissions
* Notification settings and Personas
* Environment variables
* Details available in Debug, Test, Monitor, and Learning
