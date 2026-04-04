# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/create-universal-agent/add-member-agents.md

# Add member agents

Member agents are independent agents that are connected to a universal agent. See [Universal agent](https://docs.avaamo.com/user-guide/how-to/build-agents/overview-get-started#create-a-universal-agent), for more information. There are two steps for adding a member agent to a Universal agent.

**Step 1:** [Generate the member agent's UUID and access token](#generate-the-member-agents-uuid-and-access-token)

**Step 2:** [Add member agent to the universal agent](#add-member-agent-to-the-universal-agent)

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can add member agents to a Universal agent immediately after creating the Universal agent. See [Create Universal agent](https://docs.avaamo.com/user-guide/how-to/build-agents/overview-get-started#create-a-universal-agent), for more information.
* If you wish to edit an agent, then:
  * In the Avaamo Platform UI, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing.
  * In the **Universal** **Agent** page, navigate to the **Member agents** option in the left navigation menu to add the Member agents.&#x20;
    {% endhint %}

### Generate the member agent's UUID and access token

A member agent can be connected with a Universal agent only using the UUID and access token of the member agent. Hence, it is necessary to generate a UUID and access token for the member agent and provide this information to those who are in charge of the Universal agent - so that they can establish a connection to the member agent.

See[ Configure universal agent](https://docs.avaamo.com/user-guide/how-to/configure-agents/deploy/universal-agent#configure-universal-agent) to understand the steps to generate a UUID and access token for the member agent:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FCFReVG0EPpg27hAXNNRb%2FScreenshot%202022-04-08%20at%207.03.57%20PM.png?alt=media\&token=6e9f985c-17a5-4260-a08a-806e17099f78)

### Add member agent to the Universal agent

A connection can be established to a member agent only after you receive the UUID and access token of the member agent. See [Generating UUID and access token](#generate-the-member-agents-uuid-and-access-token), for more information.

* In the **Agent -> Member Agents** page, click **Add Member Agent**.
* Currently, you can add only Avaamo agents. Hence, select the platform type **Avaamo.**
* Enter the generated UUID and Access token in the **Member UUID** and **Member Access token** fields respectively. See [Generating UUID and access token](#generate-the-member-agents-uuid-and-access-token), for more information.
* Enter a unique key for this member agent in the **Member key** field and click **Next**. The **Add Member Agent** pop-up box is displayed with the details of the member agent.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FTFuAdKJ5vKnY2fS6Z2gU%2Fadd-member-agent.png?alt=media\&token=89c5e92d-c8eb-4d3c-a1d0-cf692ff96254)

* Click **Add.** The member agent is added to the Universal agent in the **Agent -> Member agents** page. Each member agent displays the member agent name, key, skills, and last updated date that helps to identify the member agent.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F6ATCIXZ6jVWaQXwQJ35x%2Fmember-agents.png?alt=media\&token=889a1edc-3939-4bd3-b6ed-3e2a030d013f)

{% hint style="info" %}
**Note**: The member agent can always disable its connection with the universal agent. See [Disconnecting from the universal agent](https://docs.avaamo.com/user-guide/how-to/configure-agents/deploy/universal-agent#disconnecting-from-the-universal-agent), for more information.
{% endhint %}

See [Manage member agents](https://docs.avaamo.com/user-guide/how-to/build-agents/create-universal-agent/manage-member-agents), for more information on how to delete, disable, and view member agents.
