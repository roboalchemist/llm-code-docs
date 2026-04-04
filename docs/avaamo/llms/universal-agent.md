# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/universal-agent.md

# Universal agent

Avaamo Platform allows you to connect different individual agents into one central agent referred to as the **Universal agent**. Here, each individual agent of the Universal agent is called a Member agent. See [Universal agent](https://docs.avaamo.com/user-guide/how-to/build-agents/create-universal-agent), for more information.

{% hint style="info" %}
**Note**: You can connect to a channel only if it is enabled for your account or company. If you wish to enable a channel, then contact Avaamo Support for further assistance. Note that only the web channel is enabled by default.
{% endhint %}

The first step for a member agent to connect to a Universal agent is generating its own UUID and access token. This allows the Universal agent to establish a communication channel with the corresponding member agent.&#x20;

### Configure Universal agent&#x20;

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can deploy the agent to a channel after creating and building an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.
* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing.
    {% endhint %}

**To configure a Universal agent channel:**

* In the **Agent** page, navigate to the **Configure -> Channels** option in the left navigation menu.
* On the Channels page, click **Connect** in Universal agent.&#x20;
* Enter the name of the connector that helps you to identify the Universal agent it is connecting to. As a recommended practice, you can provide the name of the Universal agent here. Click **Save**.
* The **UUID** and **Access Token** are generated. Make a note of the generated UUID and Access Token. You must specify these when adding a member agent to the Universal agent. See [Add member agents](https://docs.avaamo.com/user-guide/how-to/create-universal-agent/add-member-agents#adding-the-member-agents-to-the-universal-agent), for more information.

### Manage channel settings

After you configure the channel settings, you can view, edit, disconnect and delete the channel settings as per your requirements.&#x20;

You can also deploy a member agent in different Universal agents as required. On the Channels page, click **Connect** in the Universal agent and follow the steps in [Configure Universal agent](#configure-universal-agent) to complete the setup.

### Disconnecting from the Universal agent

The member agent's connection with the Universal agent can be disconnected at any time from the Configuration -> Channel page of the member agents. This provides owners of member agents complete control over their agents while at the same time being able to lend their agents to be used by Universal agents.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FVTokiO6i2fnHSG2jQg5V%2Fdisconnect-member-agent.png?alt=media\&token=3349a0e3-d15e-46ea-9d40-541bc94d8e6e)

Once disconnected from a Universal agent, the Universal agent cannot use the member agent. This implies that when a user query is posted to the Universal agent, it probes only those member agents that are enabled and connected. When any user query is posted to the Universal agent with a disconnected member agent, a corresponding error message is displayed in the JS error indicating the same. See [JS errors](https://docs.avaamo.com/user-guide/how-to/debug-agents#using-js-errors), for more information.&#x20;

You can always connect again to the Universal agent by clicking **Connect** in the universal agent channel box. See [Manage channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/manage-channel-settings), for more information.

### Regenerate credentials

Click **Regenerate credentials** to generate a new access token and UUID. You can use this option if you suspect that the credentials are compromised, or as a regular routine.

{% hint style="success" %}
**Key points**:

* Once you regenerate the credentials of a member agent that is linked to a Universal agent, then the member agent is disconnected from the Universal agent. When any user query is posted to the Universal agent with a disconnected member agent, a corresponding error message is displayed in the JS error indicating the same. See [JS errors](https://docs.avaamo.com/user-guide/how-to/debug-agents#using-js-errors), for more information.
* If you wish to link the member agent again, then you must first [delete the member agent](https://docs.avaamo.com/user-guide/how-to/create-universal-agent/manage-member-agents#deleting-or-disabling-member-agents) from the Universal agent and add the member agent back with the regenerated credentials. See [Add member agents](https://docs.avaamo.com/user-guide/how-to/build-agents/create-universal-agent/add-member-agents), for more information.
* Analytics for member agents is displayed in the Universal agents -> Monitor -> Analytics page even if credentials are invalid or the member agent is deleted. See [Analytics - Universal agents](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/analytics-universal-agent), for more information
* Regression testing for disabled or invalid credentials or deleted member agent fails and returns false. See [Regression testing - Universal agents](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing-universal-agents), for more information.
  {% endhint %}
