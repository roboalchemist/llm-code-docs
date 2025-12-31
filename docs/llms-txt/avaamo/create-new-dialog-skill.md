# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-dialog-skill.md

# Create a new Dialog skill

Based on your requirement, you can either start by creating a new Dialog skill or by importing from any one of the available skills. See [Import skill](https://docs.avaamo.com/user-guide/how-to/build-skills/manage-skill/import-and-re-import-skills), for more information.

{% hint style="info" %}
**Notes**:&#x20;

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can add skills immediately after creating an agent. See [Create agent](https://docs.avaamo.com/user-guide/quick-start-tutorials/create-an-agent), for more information.
* If you wish to edit an agent, then navigate to the Agents tab in the top menu, search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/build-agents/manage-agents/other-common-actions#search-agents), for more information.&#x20;
* Click Edit to unlock the agent before editing.
* You can apply the Outro messages to the Dialog skill. Refer [Global Outro skill](https://docs.avaamo.com/user-guide/build-agents/add-skills-to-agent#global-outro-skill), for more information.
  {% endhint %}

**To create Dialog skill:**

* In the **Agent** page, navigate to the **Skills** option in the left navigation menu and click **Add skill**.
* In the **Skill builder** page, select **Dialog skill** and click **Create**.
* Specify the following details and click **Create**:&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mc9CHg9Drju-ZvNM-cM%2F-Mc9CgN3677LANlNdCHM%2F5.7-create-dialog-skill.png?alt=media\&token=1ba60359-4265-4f93-88a9-05d6410b0dcc)

<table><thead><tr><th width="189.44475920679886">Parameters</th><th width="359.798167959476">Description</th><th align="center">Maximum length</th></tr></thead><tbody><tr><td>Skill name</td><td>Indicates the name of the dialog skill. </td><td align="center">50 characters</td></tr><tr><td>Skill description</td><td>Indicates the description of the dialog skill. Use this to specify the purpose of the skill. </td><td align="center">200 characters</td></tr><tr><td>Skill key</td><td><p>Indicates the internal primary key used in the Avaamo Platform for uniquely identifying the skill. By default, a key is provided when you create a skill. You can change it to any user-friendly identifier. </p><p></p><p>Supported characters: Alphanumeric and underscore</p><p></p><p>It is recommended that the key is of at least 3 characters. As you type, the key is automatically converted to Snake Case. See <a href="https://en.wikipedia.org/wiki/Snake_case">Snake Case</a>, for more information. </p><p></p><p>Note that the skill key must be unique in the agent. You can specify the same identifier in the <a href="../customize-your-skill/reference-library/flow-control">flow control statements</a> such as Goto node and in <a href="../../../build-agents/test-agents/regression-testing">regression testing</a>. It helps in easy identification and readability.</p></td><td align="center">20 characters</td></tr><tr><td>Mask responses</td><td>Move the slider if you mask all the agent's responses of this skill in the conversation flow. When you enable masking for the skill, all the responses in the skill are masked and cannot be accessed. Note that this option is available only when masking is enabled for an agent. See <a href="../../../../overview-and-concepts/advanced-concepts/information-masking">Information masking</a>, for more information.</td><td align="center">NA</td></tr></tbody></table>

* Save your agent.

A new empty Dialog skill is created. See the [Next steps](#next-steps), for more information on how to continue building dialogs.

### Next steps

You can start by adding an [invocation intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-invocation-intent) to your skill. This is the intent that invokes this skill when added to an agent.&#x20;

You can then continue to edit the skill by [building dialogs](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill) with user intents and skill responses. Ensure to [test your skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/test-skill) at each step. You can navigate to the [Debug](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/debug-skill) section in the Dialog skill to troubleshoot your skill if required.&#x20;

{% hint style="success" %}
**Key Points**:

* If you have imported a skill, ensure to edit the name and description of the skill. See [Edit skill](https://docs.avaamo.com/user-guide/how-to/manage-skill#edit-skill), for more information.
* Refer to [Design skill](https://docs.avaamo.com/user-guide/how-to/build-skills/design-skill), for best practices and do's and don'ts while building a skill.
  {% endhint %}
