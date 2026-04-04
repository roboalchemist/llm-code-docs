# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/manage-skill/import-and-re-import-skills.md

# Import and Re-import skills

Instead of creating skills from scratch, you can [import](#import-skill) from any available published skills in the skill store that is closest to your business and then edit the skill as required. Further, once imported to your agent, you can also [re-import skills](#re-import-skills) from the **skill** store to bring the latest copy of the skill from the skill store. See [Manage skill store](https://docs.avaamo.com/user-guide/how-to/manage-skills-store), for more information.

{% hint style="success" %}
**Key Point**: See [Frequently asked questions (FAQs)](https://docs.avaamo.com/user-guide/manage-skills-store#frequently-asked-questions-faqs), for a list of common questions on publishing and re-publishing of skills to skill store.
{% endhint %}

### Pre-requisites

Only users with **Edit, Publish,** or **Owner** permission for the agents can import or re-import a skill from the Skill store. See [Users and Roles](https://docs.avaamo.com/user-guide/manage-platform-settings/users-and-permissions#roles-in-agent-life-cycle) and [Permissions](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/permissions), for more information.

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can import skills from the skill store immediately after creating a new agent. See [Create agent](https://docs.avaamo.com/user-guide/quick-start-tutorials/create-an-agent) and [Add skills to agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills-to-agent), for more information.
* If you wish to edit an agent, then:
  * In the Avaamo Platform UI, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/build-agents/manage-agents#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing and publishing.
    {% endhint %}

### Import skill

* In the **Agent** page, navigate to the **Skills** option in the left navigation menu and click **Import skill**.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-QHCR6jhfKFW6fGNa-%2F-M-QK1H7lFDKwRZO2LfP%2Fhowto-skill-store-import.png?alt=media\&token=41e042ff-9184-48b1-a7af-de0117213685)

* In the **Import skill** pop-up, a list of all the skills that are not already imported in the agent is displayed.
* Search and select a skill. Click **Import to Agent**.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-IzXGjsfZj3ekSuT6X%2F-M-J0NppL0bO9_tKZxee%2Fhowto-skill-import.png?alt=media\&token=85d66bc1-688c-4fdf-af99-deb6a2c29394)

* You can view a copy of the imported skill in the **Custom skills** section.
* **Save** your agent.

{% hint style="success" %}
**Key points**:

1. When you import a skill, an exact independent clone of the skill is created in the agent. Users with the required roles can edit the imported skill in the agent without affecting the skill in the skill store.&#x20;
2. All the entity types and JS files available in the skill from the skill store are imported to the skill in the agent.
3. If you import a skill with duplicate entities and JS files, then a warning message is displayed. Click **Continue** to retain the agent copy.
4. If you have already imported a skill from the skill store, then you can re-import the skill, if required, to get the latest changes of the skill from the skill store. See [Re-Import skills](#re-import-skills), for more information.
5. When importing a skill, only translations of those languages that are supported by the agent are imported. If you wish to import the skill language that is not in the agent, then you must first add the language to the agent and then import the skill.
6. In cases where custom translation for specific sentences or text is available at both the skill level and agent level, the agent-level translation is given priority.
7. Since an imported skill language is considered only when the language is a part of the agent configuration, any node-level translations of the languages that are not a part of the agent are not imported either.
   {% endhint %}

### Re-Import skill

This option is displayed only for those skills in the agent that are already imported from the skill store. &#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Lye-wuK648xmCN9CxQn%2F-Lye0MWztT-jl2segN8l%2Fhowto-reimport-skill.png?alt=media\&token=81a30dc2-74a0-4f79-8719-24ca37c9a1cc)

When you click **Re-import from Skill store**, the skill in your agent is completely replaced with the skill from the skill store, except for duplicate entities and JS. Note the following points on re-import:

* All the entity types and JS files available in the skill from the skill store are imported to the skill in the agent.
* If you re-import a skill with duplicate entities and JS, then a warning message is displayed. Click Continue to retain the agent copy.&#x20;
* Currently, you cannot merge the local skill changes with the skill in the skill store. However, you can use the following methods to preserve your local changes:
  * Use **Make a copy** to create a duplicate copy of your agent. See [Make a copy](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/make-a-copy), for more information.
  * Use **Backup & Export** option to create a backup copy of your agent in your local system. Later, you can use the exported copy and **import** the same to any existing agent in any account. See [Export and import agents](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/export-and-import-agents), for more information.

You can use the skills from the copied agent or the imported agent to manually compare and merge.
