# Source: https://docs.avaamo.com/user-guide/how-to/manage-skills-store.md

# Manage skill store

Typically, an enterprise comprises of multiple agents, where each agent is a product on its own that helps users accomplish certain tasks. **Example**: Consider a finance company that handles three products - mutual funds, insurance, and home loans. Correspondingly, for each of these products company can build agents - "Mutual Fund agent",  "Insurance Policy agent", and a "Home Loan agent".

Based on the business requirements, you can build different types of skills in each of your agents. Frequently, the functionality required for some of the skills across agents can be similar. The skills developed in one agent can be re-used in other agents within a company to accelerate the agent development process. Such re-usable skills can be published to **skill store**. See [Publish to skill store](https://docs.avaamo.com/user-guide/how-to/build-skills/manage-skill/publish-skill-to-skills-store), for more information. Once published, you can re-use the skills by importing the skill from skill store to the agent for quickly developing agents, instead of building skills from scratch. See[ Import skill from skill store](https://docs.avaamo.com/user-guide/how-to/build-skills/manage-skill/import-and-re-import-skills), for more information.

**Example**: Considering the finance company agents - "Mutual Fund agent",  "Insurance Policy agent", and a "Home Loan agent", paying a premium requires a similar set of training data, entities, and JavaScript code across all these agents. You can develop a skill "Premium Payment" once in "Mutual Fund agent", publish to skill store, import to "Insurance Policy agent" or "Home Loan agent", and with minimal or no changes re-use in the other agents.

The following is an illustration of how publishing skills and importing skills work in the Avaamo Platform:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LvQGQydpfzEIhKY1Nbu%2F-LvQGtjQpTzTbj9kkiwf%2Fhowto-skill-store-flow.png?alt=media\&token=49d20cdc-be22-4fc0-b0ef-d8cd5fc12cb1)

Hence, **skill store** is a centralized repository of all the published skills across different categories. In the Avaamo Platform UI, click the **Skill store** option in the top menu to view all skills in skill store:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-QB01yCRL6jBEmTpCJ%2F-M-QGzp1l6chYi7Ysca5%2Frn-skill-store.png?alt=media\&token=8c20088d-1ec0-4014-91e4-9c05f9a8ab41)

## Skills in skill store

There are two groups of skills in the skill store:

* **Avaamo skills**: Collection of various in-built skills across certain pre-defined categories already available in the skill store such as Travel, Healthcare, and ServiceDesk. These are pre-trained skills curated and managed by Avaamo. These skills are not specific to a company and available to all the users using the Avaamo Platform.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-QHCR6jhfKFW6fGNa-%2F-M-QI4edSvdhjXjQA7h7%2Fhowto-skill-store-avaamo.png?alt=media\&token=6f6df838-8571-41f1-8ef1-33597bac5363)

* **Company skills**: When you are developing an agent, based on the functionality of the skill, you can choose to publish the skill to the skill store. These skills are specific to your company and available only to the users within the company.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-QHCR6jhfKFW6fGNa-%2F-M-QJSlzrSIxsYVTsREf%2Fhowto-skill-store-company.png?alt=media\&token=13462e0c-7f1c-4322-ba91-d1144f595160)

The following table summarizes the key differences between Avaamo skills and Company skills:

| Avaamo skills                                                                                                     | Company skills                                                                                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Collection of various in-built skills already available in the skill store across certain pre-defined categories. | Collection of all published skills available in your company skills across certain user-defined categories                                                                                                                                                       |
| Curated and managed by Avaamo                                                                                     | Curated and managed by people within your company                                                                                                                                                                                                                |
| Cannot publish skills to Avaamo skill store                                                                       | People within your company with appropriate roles and permissions can publish to the company skill store. See [Publish to skill store](https://docs.avaamo.com/user-guide/how-to/build-skills/manage-skill/publish-skill-to-skills-store), for more information. |
| <p></p><p>Not specific to a company and available to all the users using the Avaamo Platform.</p>                 | <p></p><p>Specific to a company and available only to the users within the company.</p>                                                                                                                                                                          |

{% hint style="success" %}
**Key Points**:

* Before publishing skills to skill store, consider editing the category name in your **Company skills** based on your business model. Click the category in the **Company skills** to edit the category name. See [Publish to skill store](https://docs.avaamo.com/user-guide/how-to/build-skills/manage-skill/publish-skill-to-skills-store), for more information.&#x20;
* Click **+ New category** to add additional categories.
* Only users with the **Settings** role can edit the category name. See [Roles and permissions](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions), for more information.
  {% endhint %}

Click any skill in the skill store, to view the entities, JavaScript files, and document links included in the skill at the time of publishing the skill.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-QHCR6jhfKFW6fGNa-%2F-M-QHd2qqUF5AT_XVJ5j%2Fskills-store-expand.png?alt=media&#x26;token=330cac09-d861-4580-8100-00c00b29b75d" alt=""></div>

## Search skills in skill store

You can search for skills in the Skill store by using the skill name or skill description provided at the time of publishing the skill. Additionally, each published skill also includes a skill version and sample training data of the skill that helps to identify the purpose of the skill.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M89NJT939eZ875WAH75%2F-M89jy1O2OdCP1ox7Wan%2Fskillstore-search.gif?alt=media\&token=28511775-5165-4f66-afe4-c2d342d9f969)

{% hint style="success" %}
**Key Points**:&#x20;

* To aid better search, it is recommended to provide the skill name, description, and intents in a short descriptive way to completely understand what the skill does. This helps to easily search for the required skill in the skill store. See Design skills for more information on some examples and best practices.

* Skill names are not unique.&#x20;
  {% endhint %}

* In the Avaamo Platform UI, click the **Skill store** option in the top menu.

* Navigate to the specific category in **Avaamo skills** or **Company skills** in the left navigation menu.

* By default, all the skills in the skill store within a category are displayed in descending order of the last updated timestamp.

* Search for specific skills in the skill store using the skill name or skill description. All the skills in the skill store that contains the search keyword in either the skill name or skill description are displayed.

## Delete skill from skill store

If a skill is no longer required in the skill store, you can delete the skill from the skill store using the **Delete** option and later publish the skill again from the agent as required.

{% hint style="info" %}
**Note:** Only users with the **Settings** role can delete the skill from the Skill store. See [Roles and permissions](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions), for more information.
{% endhint %}

## Frequently asked questions (FAQs)

The following lists a few commonly asked FAQs about skill store, import, and publish:

### 1. Can all types of skills be published?

Yes, all skills - Dialog, Dynamic Q\&A, Smalltalk, and Answers, can be published to the Skill store.

### 2. I have made some changes to my skill. What happens when I re-import it?

When you re-import a skill from the skill store, the skill in your agent is completely replaced with the skill from the skill store, except for duplicate entities and JS. Hence, all your local skills changes are overwritten. See [Re-import skill](https://docs.avaamo.com/user-guide/how-to/build-skills/manage-skill/import-and-re-import-skills), for more information.

### 3. How can I preserve the local changes in imported skills?

Currently, you can use the following methods to preserve your local changes:

* Use **Make a copy** to create a duplicate copy of your agent. See [Make a copy](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/make-a-copy), for more information.
* Use the **Backup & Export** option to create a backup copy of your agent in your local system. Later, you can use the exported copy and **import** the same to any existing agent in any account.&#x20;

  See [Export and import agents](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/export-and-import-agents), for more information.

You can use the skills from the copied agent or the imported agent to manually compare and merge.

### 4. Can I merge my local skill changes with an updated version of the skill in the skill store?

Currently, you cannot merge the local skill changes with the updated version of the skill in the skill store. When you re-import a skill from the skill store, the skill in your agent is completely replaced with the skill from the skill store, except for duplicate entities and JS. Hence, all your local skills changes are overwritten. See [Re-import skill](https://docs.avaamo.com/user-guide/how-to/build-skills/manage-skill/import-and-re-import-skills), for more information.

### 5. Can I publish a skill that was imported from the skill store?

Yes. If you have appropriate permissions, you can publish a skill imported from the skill store. See [Roles and permissions](applewebdata://CC4E2907-AF33-493E-836D-F82990C2FC5E/@avaamo/s/avaamo/~/drafts/-M5k7GHD45QIIzLybGMd/overview-and-concepts/advanced-concepts/understand-roles-and-permissions), for more information.

### 6. Can I publish multiple versions of skills to the skill store?

No. Only one version of skill published from an agent is available in the skill store.

### 7. Are there any best practices for publishing skills to skill store?

Yes, there are a few best practices that you can follow for publishing a skill to skill store. See [Best practices](https://docs.avaamo.com/user-guide/build-skills/manage-skill/publish-skill-to-skills-store#best-practices), to learn more.

### 8. Can I revert a published skill to the skill store?

You cannot revert a published skill in the skill store. However, a user with the **Settings** role can delete the skill from the skill store and the skill can be published again. See [Delete skill from skill store](#delete-skill-from-skill-store), for more information.
