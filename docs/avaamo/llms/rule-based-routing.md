# Source: https://docs.avaamo.com/user-guide/live-agent-console/supervisor/rule-based-routing.md

# Rule-based routing

Rule-based routing is a mechanism used in live agent systems to direct customer inquiries to the most suitable agents based on their skills and expertise.&#x20;

In the `Avaamo Live Agent Console`, by default, all the live agent requests are routed to the default team. If you wish to route any specific live agent requests to another team, then you can use routing rules. Supervisors can create teams with live agents having specific skills or areas of expertise to handle certain kinds of requests. These skills can include product knowledge, language proficiency, technical expertise, or specialized training. See [Teams](https://docs.avaamo.com/user-guide/live-agent-console/supervisor/teams), for more information.&#x20;

Rule-based routing rules enable Supervisors to create rules in the live agent system to automatically route the live agent requests to specific teams based on their area of expertise.&#x20;

### How does Rule-based routing help?&#x20;

The following are a few points that list the benefits of having rule-based routing in your organization:

* **Improved Customer Experience**: Rule-based routing ensures that customer inquiries are directed to agents who possess the necessary skills and expertise to address their specific needs. This leads to faster and more accurate resolutions, reducing the need for customers to be transferred or bounced between teams.&#x20;
* **Enhanced First Contact Resolution**: By routing inquiries to agents with the appropriate skills, rule-based routing increases the likelihood of resolving customer issues during the initial interaction.&#x20;
* **Efficient Resource Utilization**: Rule-based routing optimizes resource allocation within the live agent system. It ensures that agents are assigned inquiries that align with their skills, preventing them from receiving inquiries outside their expertise.&#x20;
* **Reduced Average Handling Time (AHT)**: Routing inquiries to agents with the required skills can significantly reduce the average handling time per interaction. Agents who are familiar with the specific area of inquiry can quickly understand customer issues and provide efficient solutions, minimizing unnecessary back-and-forth or transfers.&#x20;
* **Increased Agent Satisfaction and Retention**: Rule-based routing contributes to agent satisfaction by ensuring they are assigned inquiries that match their skills and interests.&#x20;

### View all rules

* Click `Settings -> Avaamo Live Agent` in the Avaamo dashboard home page to view the Supervisor interface.
* Click `Settings icon -> Routing Rules` page in the left navigation pane of the Supervisor interface to view all the routing rules in your organization.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Ff1OARLFm6ba4RriPYUzO%2Fimage.png?alt=media&#x26;token=4cdd36c3-2ee6-42cf-985b-e6af842a6440" alt=""><figcaption></figcaption></figure>

* By default, the page displays all the enabled rules first and followed by disabled rules. Within each status category, the rules are listed in descending order based on their creation time, which implies that the last created rule appears first in the list.&#x20;
* Each row in the list provides essential information about a routing rule, including the rule name, the rule status (Enabled or Disabled), the team to which the rule is routed, the updated timestamp, and the user who last updated the routing rule.

### Create a new rule

* Click `Settings -> Avaamo Live Agent` in the Avaamo dashboard home page to view the Supervisor interface.
* Click `Settings icon -> Routing Rules` page in the left navigation pane of the Supervisor interface to view all the routing rules in your organization.
* In the `Routing Rules` page, click `Create Rule` and specify the following details:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FHV5LX455jPx7YTjqoxWR%2Fimage.png?alt=media&#x26;token=654d035b-7c16-4a67-b44d-930b37bf8697" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="146.44475920679886">Parameters</th><th width="468.798167959476">Description</th><th align="center">Maximum length</th></tr></thead><tbody><tr><td>Rule name</td><td>Indicates the name of the rule. Specify a name that clearly identifies the rule, making it easier to associate the teams with the rules.</td><td align="center">50 characters</td></tr><tr><td>Rule description</td><td>Indicates the description of the rule. Use this to specify the purpose of the rule. </td><td align="center">200 characters</td></tr><tr><td>Conditions  </td><td><p>Add conditions or rules when met, transfers the live agent request to the corresponding team. </p><ul><li>Use the <code>Agent.setContext</code> to set the required context before transferring to a live agent. You can set the context in any JS block in the Avaamo Platform before transferring the live agent request. For example, you can set in the <code>Before transfer</code> callback. See <a href="../../how-to/build-skills/create-skill/customize-your-skill/reference-library/agent.setcontext">Agent.setContext</a>, for more information.</li><li>Use the same key from the <code>Agent.setContext</code> and set the condition in the routing rule which when met, transfers the live agent request to the corresponding team in the following format:</li></ul><p><code>[{"key":"&#x3C;&#x3C;key_name>>","value":"&#x3C;&#x3C;value>>"},...]</code></p><p><code>... -> Indicates that you can specify multiple key-value pairs that must be satisfied for the rule to trigger</code></p><ul><li>If you have set multiple conditions, then all conditions must match for the rule to execute.</li><li>See <a href="#example-routing-rule-based-on-user-location">Example: Routing rule based on location</a>, for a sample demonstration.</li></ul></td><td align="center">NA</td></tr><tr><td>Enabled</td><td>Indicates if the rule is enabled or disabled.</td><td align="center">NA</td></tr><tr><td>Team</td><td>Indicates the team to which the live agent requests are set if the condition is met.</td><td align="center">NA</td></tr></tbody></table>

* Click **Create** to complete the creation of the new rule. Currently, the platform offers the ability to create an unlimited number of rules for an account.

### How are rules executed?

Note the following points applicable to rule execution:

* Only enabled rules are considered for rule execution.
* If there are multiple enabled rules matching the criteria, then the rule is picked based on their creation time, which implies that only the recently created rule is picked for execution. The rest of the rules are ignored.

### Example: Routing rule based on user location

Consider that you wish to transfer all the live requests from Indian users to a specific team - `Team India.`

* Get the user location from the custom user properties and set the agent context in the `Agent.setContext` method in the `Before transfer` callback section of the live agent settings. See [Before transfer](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/switch-to-live-agent/pre-built-live-agent#callbacks) and [Agent.setContext](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/agent.setcontext), for more information.

In the following illustration, it is set manually, however, you can either use an API call to get details or you can use custom user properties and then set the agent context.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FIYN7jYzxFjCoGXB1c8KX%2FScreenshot%2003-07-2023%20at%2012.30%20(1).png?alt=media&#x26;token=1d4c87e1-8883-459f-8a04-ebdd1e3bfa11" alt=""><figcaption></figcaption></figure>

* In the `Teams` page of the Supervisor interface, create the required team to whom you wish to route this request. See [Create a new team](https://docs.avaamo.com/user-guide/live-agent-console/teams#create-a-new-team), for more information.
* In the `Routing rules` page of the Supervisor interface, create a new rule, and use the location key to set the condition that triggers the rule and transfers the request to the respective team. See [Create a new rule](#create-a-new-rule), for more information.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FI9SzbNyTQHOuVK6Zvsvr%2Fimage.png?alt=media&#x26;token=fafdf3e9-3a3e-4d5f-8498-e83fea2723c9" alt=""><figcaption></figcaption></figure>

### Edit rule

You can edit the rule details such as the name, description, conditions, and teams, or make the rule enabled or disabled based on your requirement.

* Click `Settings -> Avaamo Live Agent` in the Avaamo dashboard home page to view the Supervisor interface.
* Click `Settings icon -> Routing Rules` page in the left navigation pane of the Supervisor interface to view all the routing rules in your organization.
* Search for the rule you wish to edit. See [Search rules](#search-rules), for more information.
* Click three ellipse dots in the `Actions` column of the rule to view the extended menu and click `Edit` against the rule you wish to edit.
* You can edit details such as name, description, or condition of the routing rule. You can also assign the rule to a different team or check/uncheck the `Enable checkbox.`

{% hint style="info" %}
**Note**: When a rule is enabled or disabled or say when it is assigned to a different team, any ongoing conversations where the rule is triggered or where the team is currently handling continue to operate without any interruption until they reach completion.&#x20;
{% endhint %}

### Delete a rule

A supervisor can delete a rule in a live agent system for various reasons. A few examples can be&#x20;

* When the rule is no longer required or serves no purpose. Deleting such rules helps to maintain a more manageable and organized structure within the live agent system.
* When there is a need to restructure the rules within the organization by merging, reassigning, or consolidating rules.&#x20;

**To delete a rule**:

* Click `Settings -> Avaamo Live Agent` in the Avaamo dashboard home page to view the Supervisor interface.
* Click `Settings icon -> Routing Rules` page in the left navigation pane of the Supervisor interface to view all the routing rules in your organization.
* Search for the rule you wish to delete. See [Search rules](#search-rules), for more information.
* Click three ellipse dots in the `Actions` column of the team to view the extended menu and click `Delete`**.** Click `OK` in the confirmation message to delete the rule.&#x20;

{% hint style="info" %}
**Note**: When a rule is deleted from the account, any ongoing conversations with the live agents of the team that are already triggered before deletion continue to operate without any interruption until they reach completion.&#x20;
{% endhint %}

### Search rules

You can search for routing rules using the search icon in the `Routing Rules` page. To search for a rule, enter the desired text in the `Search text box` and press enter.
