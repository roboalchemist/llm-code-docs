# Source: https://docs.avaamo.com/user-guide/release-notes/v5.0-to-v5.8.x-releases/whats-new.md

# What's new in v5.0?

The **v5.0** version is a significant revamp of the product. It reduces the number of concepts a new developer has to learn for developing enterprise agents. The dashboard UI and user experience are refreshed to make the development pleasant.&#x20;

To make the navigation around the new features in the **v5.0** easier, they are classified into the following categories:

* Development:
  * [Introduction of enterprise skill ](#introduction-of-enterprise-skill)
  * [Introduction of agent](#introduction-of-agent)
  * [Introduction of skill builders](#introduction-of-skill-builders)
  * [Introduction of Avaamo Answers skill](#introduction-of-avaamo-answers-skill)
  * [Sample agents](#sample-agents)
  * [Terminology changes](#terminology-changes)
* Administration/Management
  * [Introduction of agent life cycle management](#introduction-of-agent-life-cycle-management)
  * [Introduction of fine-grained agent permissions](#introduction-of-fine-grained-agent-permissions)
  * [Introduction of skills store](#introduction-of-skills-store)
  * [Changelogs](#changelogs)

## Development

### Introduction of enterprise skill

The v5.0 version introduces the concept of skill. A skill is specialized to understand and handle a specific task in the user conversation flow. **Example**: Order Pizza skill in a Pizza agent is responsible for taking the user through a conversation to capture the required data to order a pizza.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-QUx3PXYGXy6EvJ-Eh%2F-M-SgkdEHnV6QLITvpMQ%2Fwhats-new-skills.png?alt=media&#x26;token=39647f41-513f-4924-a11e-8e36825b3299" alt=""></div>

At a high level, a skill is similar to a "Conversational Flow Bot" in the previous version. In v5.0, it takes the concept to the next level by including an inlining intent definition to the skill. Broadly, a skill includes two key parts:

* Invocation intent and associated slots
* Implementation

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Lz0tBsV6NHssRCGz0fP%2F-Lz0uduts30WCaNJlG4C%2Fwn-intent.png?alt=media\&token=875ef280-2fbb-4244-85b6-71bb9026f91f)

This combination of intent + implementation (aka fulfillment) provides an optimum level of abstraction to achieve easier reusability and management. See [skill store](#introduction-of-skills-store), for more information on reusing the skills. At a conceptual level, the skill is then defined as

* Something that understands user queries and responds.
* May have one or more intents
* May engage the user in a one-off response or in a multi-turn conversation

With that definition, the old "Conversational Flow Bot" becomes a type of skill. The "Knowledge Pack" becomes another type of skill. The built-in intents from the v4.0 version such as greeting and frustration also become skills in the new version.

See [Build skills](https://docs.avaamo.com/user-guide/how-to/build-skills) and [Dialog Designer](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer), for more information.

### Introduction of agent

An agent is a collection of skills and the container of associated data, such as entity types, JavaScript, channels, languages, environment variables, and so on. When a user posts a query to an agent, the agent understands and classifies the input (both text and voice) and then selects an appropriate skill to engage with the user.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-Sgy7IK2jz2lwPjXZ5%2F-M-ShLolp9KYTJSlQeyE%2Fwn-agent.png?alt=media\&token=514b72a5-78de-4061-b289-b5ee6824a1e8)

See [Agents](https://docs.avaamo.com/user-guide/overview-and-concepts/agents) and [Build agents](https://docs.avaamo.com/user-guide/how-to/build-agents), for more information.

### Introduction of skill builders

The UI wizards used for creating skills are now called **Skill Builders**. There are four types of skill builders in v5.0:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-Sgy7IK2jz2lwPjXZ5%2F-M-Shhlg0L75AkMok-cN%2Frn-skill-builder.png?alt=media\&token=4d6f0762-dde9-47ef-a810-3ce55e8287b2)

<table><thead><tr><th width="201">Builder Name</th><th>Description</th></tr></thead><tbody><tr><td><a href="../../how-to/build-skills/create-skill/using-dialog-designer">Dialog Skill Builder</a></td><td>It helps you create a multi-turn conversation flow that can connect to an enterprise information system for data.</td></tr><tr><td><a href="../../how-to/build-skills/create-skill/using-q-and-a-designer">Q&#x26;A Skill Builder</a></td><td>It helps you create a skill that can provide answers to one-off questions. Typically these are frequently asked questions.</td></tr><tr><td><a href="../../how-to/build-skills/create-skill/using-avaamo-answers-1">Answers Skill Builder</a></td><td>It helps you create a skill to provide answers from your enterprise content via conversations.</td></tr><tr><td><a href="../../how-to/build-skills/create-skill/using-smalltalk">Smalltalk Builder</a></td><td>It helps you create a skill that provides responses to casual user conversations.</td></tr></tbody></table>

See [Build skills](https://docs.avaamo.com/user-guide/how-to/build-skills), for more information.

### Introduction of Avaamo Answers skill

The v5.0 introduces a new skill - **Avaamo Answers** that can provide answers from your enterprise content via conversations.

Using Avaamo Answers, you can create a quick smart conversational knowledge base by importing any PDF document or from any externally accessible URL. In addition, you can iteratively edit and fine-tune the extracted knowledge base in Answers, as required, to provide more accurate responses to user queries.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FJgA07DrWByRvSXLgiCG2%2Fimage.png?alt=media\&token=b794340c-05ec-4bd3-afd9-dbc9352213fc)

See [Build skills using Avaamo Answers](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1), for more information.

{% hint style="success" %}
**Key points**:

* Answers skills do not participate in the agent life cycle.&#x20;
* You cannot publish Answers skill to skills store.
* Make a copy functionality does not apply to Answers skill.&#x20;
  {% endhint %}

### Sample agents

The new version is already available with a few sample agents to help you understand the new and simple ways to build an agent. These agents are curated and managed by Avaamo. For any new user, the following agents are available in the out-of-the-box instance:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-Sgy7IK2jz2lwPjXZ5%2F-M-SjXR8dmfJ1qrjhAjS%2Frn-sample-agents.png?alt=media\&token=9fe989f8-3d9d-4441-8cc4-9eb76e01e017)

You can also make a copy of the agent and start editing the copied agent to explore more. See [Make a Copy](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents#make-a-copy), for more information.

### Terminology changes

The v5.0 release simplifies and streamlines the terminology required to build conversational AI agents. The following table summarizes the terminology changes introduced in v5.0

| 4.x Term                 | 5.0 Term                                                                                                                                                                                                                      |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Composite Bot            | Agent                                                                                                                                                                                                                         |
| Child Bot                | Skill                                                                                                                                                                                                                         |
| Conversational Flow bot  | Dialog Skill                                                                                                                                                                                                                  |
| Knowledge Pack           | Q\&A Skill                                                                                                                                                                                                                    |
| Smalltalk Knowledge Pack | Smalltalk Skill                                                                                                                                                                                                               |
| String Entity            | <p>The string entity is removed.</p><p><br>The string entity types are automatically migrated to Entity Types.</p>                                                                                                            |
| Entity Type              | Entity Type                                                                                                                                                                                                                   |
| Domain                   | The domain is now removed. However, it is available in the older bots in the read-only mode. See [Removal of domain](https://docs.avaamo.com/user-guide/release-notes/release-notes#removal-of-domain), for more information. |
| Domain Intent            | <p>Invocation Intent<br>(Available inside the dialog skill)</p>                                                                                                                                                               |

## Administration/Management

### Introduction of agent life cycle management

The agent life cycle management feature makes the migration of agents from the development stage to the production stage simpler. You can move an agent from one stage to another at the click of a button. The environment-specific variables are retained when an agent is moved from one stage to another.

This helps in a structured release management process and allows different teams to participate and collaborate in different stages of the agent life cycle.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-E1v0tKiEsDCVWTkux%2F-M-ENN7ioY98XDG8l0uc%2Fhowto-agent-life-cycle.png?alt=media\&token=e6d6eb44-ad16-407e-a4d4-b3d0914c8182)

See the [agent life cycle](https://docs.avaamo.com/user-guide/how-to/plan-your-development-process-agent-life-cycle), for more information.

### Introduction of fine-grained agent permissions

This feature makes visibility and access restriction to agents easy. By default, all new agents created are visible only to the creator. The creator can then add additional users with finer permissions such as view, edit, publish, and owner to their agents. This allows team members to collaborate and participate in different stages of an agent life cycle.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Lz0n3QU0y3NS1KJOzKf%2F-Lz0pWkmeURxgTWhez8W%2Fwn-agent-perm.png?alt=media&#x26;token=569b8c43-7c03-480d-839f-844aa4cd0716" alt=""></div>

See [Roles and Permissions](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions), for more information.

### Introduction of skills store

The v5.0 version introduces the skills store feature. The skill store is a repository of skills curated and managed by Avaamo for everybody to use and the skill published by developers within the company.&#x20;

The skills published by developers within your company are shown under the **Company Skills** category. The Avaamo provided skills are shown under the **Avaamo Skills** category. You can import any of the company or **Avaamo skills** into an agent. Skills store allows skill developed in one agent to be re-used in other agents within a company, there-by accelerating the agent development process.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-QB01yCRL6jBEmTpCJ%2F-M-QGzp1l6chYi7Ysca5%2Frn-skill-store.png?alt=media\&token=8c20088d-1ec0-4014-91e4-9c05f9a8ab41)

See the [Manage skills store](https://docs.avaamo.com/user-guide/how-to/manage-skills-store), for more information.

### Changelogs&#x20;

The v5.0 version allows you to track changes of an agent goes in its life cycle using **Changelog API.** This feature helps in better accountability of the users modifying the agent and troubleshooting issues in an agent if any.

See [Changelog API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/change-log-apis/changelog-api), for more information.
