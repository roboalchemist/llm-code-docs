# Source: https://docs.avaamo.com/user-guide/live-agent-console/supervisor/teams.md

# Teams

In the context of a live agent system, teams refer to groups or departments within an organization that is responsible for handling specific tasks or providing support in distinct areas. Teams in live agent systems are designed to streamline and organize agent workflows by assigning agents to specific teams based on their expertise or responsibilities.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FMPEB2IFav9e2BoFAXPKX%2Fimage.png?alt=media&#x26;token=65384dec-dfcd-4975-8c00-343bfb39d4cc" alt=""><figcaption></figcaption></figure>

### How do teams help?

The following are a few points that list the benefits of having teams in your organization:

* **Structure and Organization**: Teams help categorize and group live agents based on their roles, skills, or functional areas. For example, there might be separate teams for technical support, sales, billing, or customer service. This structure allows for the efficient assignment of tasks and ensures that customer inquiries are directed to the appropriate team.
* **Collaboration and Communication**: Teams facilitate collaboration among agents who belong to the same group. Agents within a team can share information, communicate internally, and collaborate on resolving customer issues. This improves efficiency and coordination within the team.
* **Rule-Based Routing**: Teams are often used in conjunction with skill-based routing, where customer inquiries are automatically routed to the most suitable team or agent based on predefined criteria. Skill-based routing ensures that customer requests are directed to agents who possess the necessary expertise to handle them effectively. See [Rule-based routing](https://docs.avaamo.com/user-guide/live-agent-console/supervisor/rule-based-routing), for more information.
* **Reporting**: Supervisors can assess the workload of specific teams, monitor metrics, and make informed decisions regarding resource allocation and training needs.

### Default team

When you start a new setup of the Avaamo live agent console, a default team is already available for you to get started. You can edit the team to rename and add live agents to the default team. See [Edit team details](#edit-team-details), for more information.

{% hint style="success" %}
**Key points**:

* By default, newly added live agents are not added to any team. It is the responsibility of the supervisor within the account to associate a newly added live agent with a team. This ensures that the live agent is properly assigned and aligned with a specific team's responsibilities and tasks.
* By default, all the live agent requests are routed to the default team. If you wish to route any specific live agent requests to another team, then you can use routing rules. See [Rule-based routing](https://docs.avaamo.com/user-guide/live-agent-console/supervisor/rule-based-routing), for more information.
  {% endhint %}

It is mandatory to have one team as the default team. A supervisor has the option to set any team as the default team.&#x20;

**To set a default team:**

* Click `Settings -> Avaamo Live Agent` in the Avaamo dashboard home page to view the Supervisor interface.
* Click `Settings icon -> Teams` page in the left navigation pane of the Supervisor interface to view all the teams in your organization.
* Search the team you wish to set as default. See [Search teams](#search-teams), for more information.
* Click three ellipse dots in the `Actions` column of the team to view the extended menu and click `Make Default` against the team that you wish to set as default.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F2zz3szcvWb0EhAfGdVwX%2Fimage.png?alt=media&#x26;token=d09e6bb1-5cf3-410a-b870-b50cc3b1a405" alt=""><figcaption></figcaption></figure>

### View all teams

* Click `Settings -> Avaamo Live Agent` in the Avaamo dashboard home page to view the Supervisor interface.
* Click `Settings icon -> Teams` page in the left navigation pane of the Supervisor interface to view all the teams in your organization.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FMPEB2IFav9e2BoFAXPKX%2Fimage.png?alt=media&#x26;token=65384dec-dfcd-4975-8c00-343bfb39d4cc" alt=""><figcaption></figcaption></figure>

* By default, the teams are displayed in descending order, organized according to their creation time, which implies that the last created team appears first in the list.
* Each row in the list provides essential information about a team, including the team name, the number of live agents assigned to the team, and the timestamp indicating the last update made to the team.

{% hint style="info" %}
**Note**: Before accepting any requests, a supervisor within the account must associate a newly added live agent with a team. This ensures that the live agent is properly assigned and aligned with a specific team's responsibilities and tasks.
{% endhint %}

### Create a new team

* Click `Settings -> Avaamo Live Agent` in the Avaamo dashboard home page to view the Supervisor interface.
* Click `Settings icon -> Teams` page in the left navigation pane of the Supervisor interface to view all the teams in your organization.
* Supervisors can create new teams from the `Teams` page. In the `Teams` page, click `Create New Team` and specify the following details:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fcx2Z86ZoEdCQ7jSwVcHs%2Fimage.png?alt=media&#x26;token=31c1e6cc-1102-4416-bcda-3e96cd409a56" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="189.44475920679886">Parameters</th><th width="359.798167959476">Description</th><th align="center">Maximum length</th></tr></thead><tbody><tr><td>Team name</td><td><p>Indicates the name of the team. Specify a name that clearly identifies the team, making it easier to associate and add new live agents to the team. </p><p></p><p>Supported characters: Team name must start with an alphabet and must contain only Alphabets, Numbers, or Underscore.</p></td><td align="center">50 characters</td></tr><tr><td>Team description</td><td>Indicates the description of the team. Use this to specify the purpose of the team. </td><td align="center">200 characters</td></tr><tr><td>Live agents </td><td><p>Add live agents to the team. Begin by entering the name of the live agent. The list is automatically filtered out based on the entered text. In case there are multiple live agents with the same name, you can utilize the associated email ID to differentiate and select the desired live agents for the team.</p><p></p><p>As you add the live agents, the updated list is displayed at the bottom. If you need to remove a live agent from the team, click "Cancel" next to their name. </p><p></p><p>Currently, the platform offers the ability to add an unlimited number of live agents to a team.</p></td><td align="center">NA</td></tr></tbody></table>

* Click `Create` to complete the creation of the new team. Currently, the platform offers the ability to create an unlimited number of teams for an account.

### Edit team details

You can edit the name, and description, or add/remove live agents in the team.

* Click `Settings -> Avaamo Live Agent` in the Avaamo dashboard home page to view the Supervisor interface.
* Click `Settings icon -> Teams` page in the left navigation pane of the Supervisor interface to view all the teams in your organization.
* Search for the team you wish to edit. See [Search teams](#search-teams), for more information.
* Click three ellipse dots in the `Actions` column of the team to view the extended menu and click `Edit` against the team you wish to edit.
* You can edit details such as name and description of the team. You can also add or remove the live agents from the team, say for example, during the restructuring process or when the live agent is no longer associated with the account.&#x20;

{% hint style="info" %}
**Note**: When a live agent is removed from a team, any ongoing conversations with the live agents of the team continue to operate without any interruption until they reach completion.&#x20;
{% endhint %}

### Delete a team

A supervisor can delete a team in a live agent system for various reasons. A few examples can be&#x20;

* When the team is no longer required or serves no purpose. Deleting such teams helps to maintain a more manageable and organized structure within the live agent system.
* When there is a need to restructure the teams within the organization by merging, reassigning, or consolidating teams, this can enhance collaboration, simplify workflows, and ensures accurate and up-to-date team assignments.

**To delete a team**:

* Click `Settings -> Avaamo Live Agent` in the Avaamo dashboard home page to view the Supervisor interface.
* Click `Settings icon -> Teams` page in the left navigation pane of the Supervisor interface to view all the teams in your organization.
* Search the team you wish to delete. See [Search teams](#search-teams), for more information.
* Click three ellipse dots in the `Actions` column of the team to view the extended menu and click `Delete`**.** Click `OK` in the confirmation message to delete the team.&#x20;

{% hint style="info" %}
**Notes**:&#x20;

* When a team is deleted from the account, any ongoing conversations with the live agents of the team continue to operate without any interruption until they reach completion.&#x20;
* Supervisors can delete all teams except the default team.
  {% endhint %}

### Search teams

You can search for teams using the search icon in the `Teams` page. To search a team, enter the desired text in the `Search text box` and press enter.
