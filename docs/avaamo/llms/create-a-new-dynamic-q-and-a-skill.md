# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a/create-a-new-dynamic-q-and-a-skill.md

# Create a new Dynamic Q\&A skill

Based on your requirement, you can either start by creating a new Dynamic Q\&A skill from scratch or by importing from any one of the available skills. See [Import skill](https://docs.avaamo.com/user-guide/how-to/build-skills/manage-skill/import-and-re-import-skills), for more information.

{% hint style="info" %}
**Notes**:&#x20;

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can add skills immediately after creating an agent. See [Create agent](https://docs.avaamo.com/user-guide/quick-start-tutorials/create-an-agent), for more information.
* If you wish to edit an agent, then navigate to the Agents tab in the top menu, search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/build-agents/manage-agents/other-common-actions#search-agents), for more information.&#x20;
* Click Edit to unlock the agent before editing.
* You can apply the Outro messages to the Dynamic Q\&A skill. Refer [Global Outro skill](https://docs.avaamo.com/user-guide/build-agents/add-skills-to-agent#global-outro-skill), for more information.
  {% endhint %}

**To create Dynamic Q\&A skill:**

* In the **Agent** page, navigate to the Skills option in the left navigation menu, click **Add Skill** in the Agent skills page.
* In the **Skill builder** page, select **Dynamic Q\&A** and click **Create**.&#x20;
* Specify the following details and click **Create**:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MZqFBVR5LvFEYHqJ2gY%2F-MZqFicZ9mZ3PrGdx37k%2Fqs-qa-skill-create.png?alt=media\&token=516f7228-92ab-4755-9120-fbfe33bb3e82)

<table><thead><tr><th>Parameters</th><th width="359.299095263438">Description</th><th align="center">Maximum Length</th></tr></thead><tbody><tr><td>Skill name</td><td>Indicates the name of the Q&#x26;A skill, primarily used to identify the skill. The skill name must be less than 50 characters.</td><td align="center">50 characters</td></tr><tr><td>Skill description</td><td>Indicates the description of the skill. Use this to specify the purpose of the skill. The skill description must be less than 200 characters.</td><td align="center">200 characters</td></tr><tr><td>Skill key</td><td><p>Indicates the internal primary key used in the Avaamo Platform for uniquely identifying the skill. </p><p></p><p>Supported characters: Alphanumeric and underscore</p><p></p><p>It is recommended that the key is of at least 3 characters. As you type, the key is automatically converted to Snake Case. See <a href="https://en.wikipedia.org/wiki/Snake_case">Snake Case</a>, for more information. </p><p></p><p>Note that the skill key must be unique in the agent. You can specify the same identifier in the <a href="../customize-your-skill/reference-library/flow-control">flow control statements</a> such as Goto node and in <a href="../../../build-agents/test-agents/regression-testing">regression testing</a>. It helps in easy identification and readability.</p></td><td align="center">20 characters</td></tr><tr><td>Collect Feedback</td><td><p>Indicates if you wish to enable user feedback or not. By default, it is set to false. Use the slider for setting to true. </p><p></p><p>Note that you can also disable feedback at the skill level and add feedback to individual responses using<code>collectFeedback()</code>method. See <a href="../customize-your-skill/how-to/add-feedback">Add feedback (JS)</a>, for more information. </p><p></p><p>Currently, <strong>Collect feedback</strong> functionality is supported only in Web, Android, and iOS channels.</p></td><td align="center">NA</td></tr><tr><td>Mask responses</td><td>Move the slider if you mask all the agent's responses of this skill in the conversation flow. When you enable masking for the skill, all the responses in the skill are masked and cannot be accessed. Note that this option is available only when masking is enabled for an agent. See <a href="../../../../overview-and-concepts/advanced-concepts/information-masking">Information masking</a>, for more information.</td><td align="center">NA</td></tr></tbody></table>

A new empty Dynamic Q\&A skill is created.&#x20;

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-J2JXoR6dNI8YnhRB6%2F-M-J6889gX8h7QSEjW4D%2Fqa-create-new-qa.png?alt=media&#x26;token=05a62a1b-5aec-42d2-aaf1-8d3abbb0728f" alt=""></div>

### Next Steps

You can start by [adding questions and answers ](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a/build-and-manage-dynamic-q-and-a-skill/add-questions-and-answers)to your Dynamic Q\&A skill either manually or by importing a CSV file. Once the Q\&A is added successfully, your Q\&A skill is ready for [testing](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a/test-dynamic-q-and-a-skill). See [Debug Dynamic Q\&A skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a/debug-dynamic-q-and-a-skill), for common troubleshooting tips.

{% hint style="success" %}
**Key Points**:

* If you have imported a skill, ensure to edit the name and description of the skill. See the [Edit skill](https://docs.avaamo.com/user-guide/how-to/manage-skill#edit-skill), for more information.
* Refer to [Design skills](https://docs.avaamo.com/user-guide/how-to/build-skills/design-skill), for best practices and do's and don'ts while building a skill.
  {% endhint %}
