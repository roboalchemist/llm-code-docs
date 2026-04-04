# Source: https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions/use-case-dedicated-platform-team-with-azure-saml.md

# Use case - Dedicated platform team with Azure SAML

Avaamo Platform allows you to create and associate users and groups to different out-of-the-box roles based on the user's responsibility in the company. Roles focus on platform-level access. At the agent level, access can be controlled by the owner of the agent using permissions. See [Roles and permissions](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions), for more information.

### Use case

Consider the following use-case:

* Avaamo platform is integrated with MS Azure. See [SAML Support - MS Azure](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/identity-providers/saml-support-ms-azure), for more information.
* A particular line of business who wants to build an agent puts up a proposal to the Platform owner.
* The Platform owner creates an agent for the team.&#x20;
* The agent modification is owned by the Business Development team.&#x20;
* The agent permissions are controlled by the Platform team.

Here, there is a dedicated Platform team to support multiple business units. Platform Owner group has the company level highest access on the platform. In the current use case, Platform Owner group hold the responsibility for all platform-level changes. This includes:

1. Creating a new agent
2. Provisioning of new and existing agent
3. Making copies of agent
4. Promotion of the agent
5. Pulling updates from lower to a higher instance
6. Deletion of the agent
7. Backup and export copy
8. Import an agent
9. Publishing to skill store

The Business Development team of the agent can be either

1. One for each business unit
2. One for multiple business units
3. Combination of the above

For example, consider, each business unit with its own developers. The HR business unit wants to build an agent with help of its developers. Let us see the groups suggestion for such a case below.

### MS-Azure setup

Based on the above use-case, groups in MS Azure can be created. The groups are for logical separation only with only user access in Azure app roles.&#x20;

* User access allows the group members to log in to the platform only.&#x20;
* For each agent, one-time access to the respective groups is provided.

| AD Group       | Azure App Role                                                   |
| -------------- | ---------------------------------------------------------------- |
| Platform Owner | development, testing, staging, production, live\_agent, settings |
| Live Agent     | live\_agent                                                      |
| Developer      | user                                                             |

Apart from the SAML setup, there is a one time per agent permission control to be setup.

### Avaamo Platform with AD Group <a href="#id-58khfjxrpom0" id="id-58khfjxrpom0"></a>

For the HR agent, the permissions can be distributed as follows:

| Agent Stage | AD Group  | Agent Permission |
| ----------- | --------- | ---------------- |
| Development | Developer | Publish          |
| Testing     | Developer | View             |
| Staging     | Developer | View             |
| Production  | Developer | View             |

{% hint style="info" %}
**Notes**:

* During a first-time promotion for an agent. Group to be added in permission for the agent on the promoted instance as listed above.
* In case of deletion of the agent and promotion again, the same permission must be replicated.
  {% endhint %}

### Avaamo Platform with AD Group with Edit <a href="#lgt4h8am5to3" id="lgt4h8am5to3"></a>

* Publish access is only available in the Development stage which offers publish to skill store. At a higher stage, it is equivalent to edit access.&#x20;

{% hint style="info" %}
**Note**: To publish to Skill store, development role access is required. As the development role is removed, the ownership to publish to the skill store is with Platform owners.
{% endhint %}

* In case, you wish to offer Developers access on a higher stage, edit permission can be granted.
* In a setup where the Platform team need full control and wishes to keep the same agent in sync across the stages, edit access on a higher stage is best avoided. Platform teams are advised to own changes on a higher instance especially on Production.

| **Agent Stage** | **AD Group** | **Agent Permission** |
| --------------- | ------------ | -------------------- |
| Development     | Developer    | Publish              |
| Testing         | Developer    | Edit                 |
| Staging         | Developer    | Edit                 |
| Production      | Developer    | View                 |
