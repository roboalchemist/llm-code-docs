# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/create-new-knowledge-base.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/create-new-knowledge-base.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/create-new-knowledge-base.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/create-new-knowledge-base.md

# Create a new Smalltalk skill

Based on your requirement, you can either start by creating a new Smalltalk skill from scratch or by importing from any one of the available skills. See [Import skill](#import-skill), for more information.

{% hint style="info" %}
**Notes**:&#x20;

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can add skills immediately after creating an agent. See [Create agent](https://docs.avaamo.com/user-guide/quick-start-tutorials/create-an-agent), for more information.
* If you wish to edit an agent, then navigate to the Agents tab in the top menu, search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/build-agents/manage-agents/other-common-actions#search-agents), for more information.&#x20;
* Click Edit to unlock the agent before editing.
  {% endhint %}

**To create a Smalltalk skill:**

* In the **Agent** page, navigate to the Skills option in the left navigation menu, click **Add Skill** in the **Agent skills** page.
* In the **Skill builder** page, select **Smalltalk** and click **Create**.&#x20;
* Specify the following details and click **Create**:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MZqGQFGpO9rpWbUCaIX%2F-MZqGszZ0z60C22rZFhd%2Fsmalltalk-create-skill.png?alt=media\&token=83739ab1-d3ca-4244-8f62-81659041ef49)

<table><thead><tr><th width="150.33333333333331">Parameters</th><th width="390.09153627905783">Description</th><th align="center">Maximum length</th></tr></thead><tbody><tr><td>Skill name</td><td>Indicates the name of the Smalltalk skill, primarily used to identify the skill. </td><td align="center">50 characters</td></tr><tr><td>Description</td><td>Indicates the description of the skill. Use this to specify the purpose of the skill. </td><td align="center">200 characters</td></tr><tr><td>Skill key</td><td><p>Indicates the internal primary key used in the Avaamo Platform for uniquely identifying the skill. </p><p></p><p>Supported characters: Alphanumeric and underscore</p><p></p><p>It is recommended that the key is of at least 3 characters. As you type, the key is automatically converted to Snake Case. See <a href="https://en.wikipedia.org/wiki/Snake_case">Snake Case</a>, for more information. </p><p></p><p>Note that the skill key must be unique in the agent. You can specify the same identifier in the <a href="../customize-your-skill/reference-library/flow-control">flow control statements</a> such as Goto node and in <a href="../../../build-agents/test-agents/regression-testing">regression testing</a>. It helps in easy identification and readability.</p></td><td align="center">20 characters</td></tr><tr><td>Mask responses</td><td>Move the slider if you mask all the agent's responses of this skill in the conversation flow. When you enable masking for the skill, all the responses in the skill are masked and cannot be accessed. Note that this option is available only when masking is enabled for an agent. See <a href="../../../../overview-and-concepts/advanced-concepts/information-masking">Information masking</a>, for more information.</td><td align="center">NA</td></tr></tbody></table>

A new empty Smalltalk skill is created. The next step is to [add questions and answers](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/build-and-manage-smalltalk-skill/add-smalltalk-qa) to the Smalltalk skill.

### Next steps

You can start by [adding questions and answers](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/build-and-manage-smalltalk-skill/add-smalltalk-qa) to your Smalltalk skill either manually or by importing a CSV file. Once the Smalltalk is uploaded successfully, your skill is ready for [testing](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/test-smalltalk-q-and-a). See [Debug Smalltalk](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/troubleshooting-tips), for common troubleshooting tips.

{% hint style="success" %}
**Key Points**:

* If you have imported a skill, ensure to edit the name and description of the skill. See [Edit skill](https://docs.avaamo.com/user-guide/how-to/manage-skill#edit-skill), for more information.
* Refer to [Design skills](https://docs.avaamo.com/user-guide/how-to/build-skills/design-skill), for best practices and do's and don'ts while building a skill.
  {% endhint %}
