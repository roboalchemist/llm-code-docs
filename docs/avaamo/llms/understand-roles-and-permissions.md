# Source: https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions.md

# Roles and permissions

Avaamo Platform allows you to create and associate users and groups to different out-of-the-box roles based on the user's responsibility in the company. A user or group can also be assigned to multiple roles as required. Broadly, roles can be categorized as follows:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fk90O2JZjz34kItHW0vnP%2Fimage.png?alt=media&#x26;token=511a4919-f1e8-40ea-8a43-3d7a64df6888" alt=""><figcaption></figcaption></figure>

* **Agent Settings**: Typically, any agent goes through different stages in its life cycle from inception to production - **Development, Testing, Staging, and Production**. You can create users or groups with different roles for collaborating in each stage of the agent life cycle. This allows teams to develop, test, stage, and then deploy the agents in different environments within the Avaamo Conversation AI Platform, thereby providing the required compliance. See [Agent Settings](#agent-settings), for more information.
* **Campaign Settings**: Avaamo Platform allows you to create and associate users and groups with different out-of-the-box campaign roles based on the user's responsibility in the company.&#x20;

  See [Campaign Permissions](https://docs.avaamo.com/user-guide/outreach/before-you-begin#campaign-permissions), for more information on different roles available for an outreach campaign.&#x20;
* **Live Agent Settings**: Avaamo Platform allows you to create and associate users and groups with different out-of-the-box live agent roles based on the user's responsibility in the company.&#x20;

  See [Live Agent Roles](https://docs.avaamo.com/user-guide/live-agent-console/before-you-begin#live-agent-roles), for more information on different roles available in the Avaamo Live Agent system.
* **Global settings**: For managing users, groups, and roles, specifying privacy, and identity provider's details. These are not related to the agent life cycle. See [Global settings](#global-settings), for more information.

## Roles - At a glance

The following table summarizes the actions and the corresponding roles applicable to each action:

{% hint style="info" %}
**Note**: Roles can be assigned to individual users and also to groups. When a role is assigned to a group, it is applicable to all the users of a group. See [Users and Groups](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/users-and-permissions), for more information on managing users and groups in the Avaamo Platform.&#x20;

If a user belongs to multiple groups, then the roles applicable to a user are a union of all the roles from individual groups.&#x20;

**Example**: Consider the following scenario:

* Group 1 is associated with the Development role
* Group 2 is associated with the Testing role
* User John Miller is added to Group 1 and Group 2.

Roles applicable to John Miller -> Roles from Group 1 + Roles from Group 2. Hence, John Miller has both Development and Testing roles.
{% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FLSFbIiBwqFISTikdqSfo%2FUntitled%20design%20\(4\).png?alt=media\&token=49d81ad9-0ca9-4a99-b973-3d9ad7bf1923)

## Agent settings

The following roles are available in the Avaamo Platform to facilitate the collaboration between teams in the agent life-cycle:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LupsguuyOxN7dHAgdMS%2F-LupvMjQYhH0DV_nnqZT%2Fhowto-agent-life-cycle-flow.png?alt=media\&token=8dd1c9ae-a99a-4b92-8014-60156a56efaf)

### **Development**

Users with development roles gather requirements, configure the development environment, start designing and developing agents and skills (create an agent, edit the agent, add skills to the agent, make a copy of the agent), and finally prepare the agent for testing by the testing team. They are also responsible for fixing the issues reported by different teams. In parallel, they also continue with further development as required by the business.

### **Testing**

Users with a testing role can promote agents from development to testing environment, configure the testing environment, test the agent's functionality, report bugs, and issues. Correspondingly, they can also pull updates from development to testing for re-testing the issues fixed. Once testing is completed, they notify the staging users to promote the agent from testing to staging.

### **Staging**

Users with a staging role can promote agents from testing to the staging environment, configure the staging environment, test the agent's functionality by replicating production instances, report bugs and issues. Correspondingly, they can also pull updates from testing to staging for re-testing the issues fixed. Once testing is completed, they notify the staging users to promote the agent from staging to production.

### **Production**

Users with a production role can promote agents from staging to the production environment, configure the production environment, and report bugs and issues in the live production instance. Correspondingly, they can also pull updates from staging to production for the issues fixed. Minor defects can be fixed as hotfixes in the production instance. Production users must notify the issues and hot-fixes to the development team.

See [Users and Groups](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/users-and-permissions), for more information on how to manage users and groups with roles. Also see the [agent life cycle](https://docs.avaamo.com/user-guide/how-to/plan-your-development-process-agent-life-cycle#stages-in-agent-life-cycle), for more information on life cycle stages.

## Campaign settings

Avaamo Platform allows you to create and associate users and groups with different out-of-the-box campaign roles based on the user's responsibility in the company.&#x20;

See [Campaign Permissions](https://docs.avaamo.com/user-guide/outreach/before-you-begin#campaign-permissions), for more information on different roles available for an outreach campaign.&#x20;

## Live agent settings

Avaamo Platform allows you to create and associate users and groups with different out-of-the-box live agent roles based on the user's responsibility in the company.&#x20;

See [Live Agent Roles](https://docs.avaamo.com/user-guide/live-agent-console/before-you-begin#live-agent-roles), for more information on different roles available in the Avaamo Live Agent system.

## Global settings

### Settings

Users with this role are responsible for managing users and groups and roles, specifying privacy, providing identity provider details. They can also access `Usage reports` for LLaMB, SMS, and Voice based on what is enabled for their account. See [Manage settings](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings), for more information.

Also, only users with the Settings role can edit the category name in the Skills store and delete skills from the Skills store. See the [Manage skill store](https://docs.avaamo.com/user-guide/how-to/manage-skills-store), for more information.

## Agent permissions

By default, when you create an agent, you are the **owner** of the agent. Additionally, when a user promotes an agent, the user who promoted the agent is automatically the owner of the agent in the promoted stage. As an owner of the agent, you can assign permissions to different people within your company for your agent as required.&#x20;

Permissions can be assigned to individual users and also to groups. When permissions are assigned to a group, it is applicable to all the users of a group. See [Users and Groups](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/users-and-permissions), for more information on managing users and groups in the Avaamo Platform.&#x20;

{% hint style="info" %}
**Note**: If a user belongs to multiple groups and each group is assigned different permissions on the agent, then the permission applicable to a user is a union of all the permissions from individual groups.&#x20;

**Example**: Consider the following scenario:

* User 1 belongs to Group 1 and Group 2
* Group 1 has View permission on the agent
* Group 2 has Edit permission on the agent

Hence, User 1 has both View and Edit permission on the agent.
{% endhint %}

There are four types of permissions available for an agent:

* **View**: Users can only view the agent but cannot edit the agent. Note that with this permission the user can still submit an Unhandled Query Analyzer (UQA) job. See [Unhandled Query Analyzer](https://docs.avaamo.com/user-guide/how-to/build-agents/learning-continuous-improvement/query-analyzer-deprecated), for more information.
* **Edit**: Users can view and edit the agent.
* **Publish**: Users can view agents, edit agents, and publish skills from the agent to the skill store.&#x20;
* **Owner**: Full access to the agent. Users can view agents, edit agents, publish skills from the agent to the skill store, and edit agent permissions.

The following table summarizes the actions and the corresponding agent permissions applicable for each action:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LzwNMOffvON93b_JOd5%2F-M-8VqSXn3_RMhruJUe-%2Fqs-agent-permission.png?alt=media\&token=7959ebf6-3d8c-4e14-a9a7-49779569c3ff)

{% hint style="success" %}
**Key Points**:&#x20;

* To view the agent, and get data from the agent using an API, a user must have at least read permission on the agent.&#x20;
* To make any data modifications on the agent in the UI or via API, the user must have at least edit permission on the agent.
* Only an owner of the agent can delete the agent and configure the permissions of an agent.
  {% endhint %}

See [Permissions](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/permissions), for more information.
