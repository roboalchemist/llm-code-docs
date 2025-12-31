# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/manage-skill/publish-skill-to-skills-store.md

# Publish and Re-publish skills

Based on the business requirements, you can build different types of skills in each of your agents. Frequently, the functionality required for some of the skills across agents can be similar. The skills developed in one agent can be re-used in other agents within a company to accelerate the agent development process. Such re-usable skills can be published to **skill store**. See [Manage skill store](https://docs.avaamo.com/user-guide/how-to/manage-skills-store), for more information.

{% hint style="success" %}
**Key Points**:&#x20;

* See [Best practices](#best-practices) that you can follow for publishing a skill to skill store.
* See [Frequently asked questions (FAQs)](https://docs.avaamo.com/user-guide/manage-skills-store#frequently-asked-questions-faqs), for a list of common questions on publishing and re-publishing.
  {% endhint %}

### Pre-requisites

Only **Development** role users and with **Publish** or **Owner** permission for the agents can publish, re-publish skill to skill store. See [Users and Roles](https://docs.avaamo.com/user-guide/manage-platform-settings/users-and-permissions#roles-in-agent-life-cycle) and [Permissions](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/permissions), for more information.

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can publish skills to skill store immediately after creating skills in the agent. See [Create agent](https://docs.avaamo.com/user-guide/quick-start-tutorials/create-an-agent) and [Add skills to agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills-to-agent), for more information.
* If you wish to edit an agent, then:
  * In the Avaamo Platform UI, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/build-agents/manage-agents#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing and publishing.
    {% endhint %}

### Publish skill

To re-use the skill across multiple agents in your account, you can publish skills to skill store:

* In the **Agent -> Skills** page, click **Publish to skill store** in the overflow menu icon for the skill you wish to publish.
* In the **Publish skill -> Skill details**, specify the following details that help to identify the skill in the skill store:

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LydcAUYJFgOl9tqQyv9%2F-Lyde4pt3HxgoWiI7j0j%2Fhowto-publish-skill.png?alt=media&#x26;token=02fe14d9-3e00-4048-ab4f-86c0ceae1227" alt=""></div>

| Fields             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Skill name         | The skill name is automatically populated from the current name of the skill. This is the name that is used to identify the skill in the skill store. However, you can also change the name, if required. Use a combination of verb + noun to name your skill. **Example**: Instead of naming the skill as "ResetPassword", consider adding a noun, "ResetPassword - AWS".                                                                                            |
| Description        | The description is automatically populated from the current description of the skill. However, you can also change the description, if required. Keep the description succinct and short while mentioning the purpose of the skill.                                                                                                                                                                                                                                   |
| Things you can say | List the top three queries the skill can respond to. This must help to easily demonstrate the understanding capability of the skill.                                                                                                                                                                                                                                                                                                                                  |
| Category           | Select the category under which you wish to publish the skill in the skill store. Before publishing skills to skill store, consider editing the category name in your **Company skills** based on your business model. Click the category in the **Company skills** to edit the category name. See [Manage skill store](https://docs.avaamo.com/user-guide/how-to/manage-skills-store), for more information.                                                         |
| Version            | <p>Specify the version of the skill. It is recommended that you increment the version as you publish successive versions of skill to skill store. Note that only one version of the skill is retained in the skill store.</p><p></p><p>You can also communicate the availability of the new version to the developers. Currently, this communication is manual, there is no automatic notification to developers when a skill is re-published with a new version.</p> |
| Document link      | Any external document link that contains more details about the skill. You can use this to explain the skill details that the developers can learn about before importing the skill from the skill store.                                                                                                                                                                                                                                                             |
| What's new         | Briefly describe new changes or updates to the skill before publishing or re-publishing. This helps developers to understand the changes if they wish to re-import a skill from skill store to their agent.                                                                                                                                                                                                                                                           |

* In the **Publish skill -> Entity types**, a list of all the entity types in the agent is displayed. The entities used in the skill is automatically selected and displayed to you. Additionally, you can select the other entity types as required before publishing your skill.&#x20;
* In the **Publish skill -> Javascript**, a list of all the JS files used by the agent is displayed. You can select the ones used by your skill before publishing. See [Add JS files](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-js-files), for more information.
* Click **Publish**. The skill is now published to the company skill store under the selected category.

{% hint style="success" %}
**Key Points**:&#x20;

* The skills published in the skill store are independent clones with all required data needed for it.
* You can only publish to the skill store under your **Company skills**. You cannot publish to **Avaamo skills**.
* Currently, Answers skill cannot be published to skill store.
  {% endhint %}

### Republish skill&#x20;

After you publish the skill to the Skill store, you can continue to work on the skill independently in your agent and later re-publish the skills again to the skill store.&#x20;

{% hint style="success" %}
**Key points**:&#x20;

* Republishing a skill from an agent is a complete replacement of that skill in the skill store. Only one version of the skill published from an agent is available in the skill store.

* There is no restriction on the number of times you can re-publish a skill from an agent to the skill store.
  {% endhint %}

* In the **Agent -> Skills** page, click **Re-publish to skill store** in the overflow menu icon for the skill you wish to re-publish.

* In the **Publish** skill pop-up, specify the details required for publishing. See [How to publish?](#how-to-publish) for more information.

### Best practices

The following lists a few best practices that you can follow for publishing a skill to skill store:

* When you start designing an agent, consider defining the functionality of the agent in well-defined tasks. For each specific task, you can build skills and choose to publish the skill to your company skill store for re-usability. See [Design skills](https://docs.avaamo.com/user-guide/how-to/build-skills/design-skill), for more information.
* When you start creating skills, the name the skill in such a way that helps you easily identify the skill and its functionality. Use a combination of verb + noun to name your skill. **Example**: Instead of naming the skill as "ResetPassword", consider adding a noun, "ResetPassword - AWS".
* When you publish a skill, ensure that in **Things you can say** section, you list the top three queries the skill can respond to. This must help to easily demonstrate the understanding capability of the skill.
* Increment the version as you publish successive versions of skill to skill store. You can also communicate the availability of the new version to the developers.&#x20;
* Maintain a document with the skill details and update the document as and when you re-publish the skill with a new version. Currently, this communication is manual, there is no automatic notification to developers when a new skill version is re-published with a new version.
* You cannot revert a published skill in the skill store. However, a user with the **Settings** role can delete the skill from the skill store and the skill can be published again. See [Delete skill from skill store](https://docs.avaamo.com/user-guide/manage-skills-store#delete-skill-from-skill-store), for more information.
