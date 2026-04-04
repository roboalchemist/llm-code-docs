# Source: https://docs.avaamo.com/user-guide/configuration/channels/webex.md

# Webex

## Webex channel integration

The Avaamo Conversational AI Platform now supports `Webex` as a communication channel, enabling AI agents to interact seamlessly with users directly within the Webex collaboration environment. This integration allows organizations to leverage existing workflows while providing AI-powered assistance, making conversations more interactive and context-aware.

{% hint style="info" %}
Note: This channel only supports AI agents.
{% endhint %}

### What is Webex channel integration?

The Webex channel integration allows AI agents to engage users within Webex teams and spaces, eliminating the need to switch platforms for information or support. Users can interact with AI agents via `text messages` and `adaptive cards`, enabling a smooth conversational experience within the enterprise collaboration environment.

This integration is handy for:

* Internal employee support and queries
* Customer engagement through Webex collaboration spaces
* Automating routine tasks, such as approvals, reminders, and notifications

### Before you begin

Before connecting your Webex channel to Avaamo, you must **create a Webex bot** and obtain the following details:

* **Bot Username**
* **Access Token**
* **Bot ID**

These details are necessary to connect your Webex bot to the Avaamo platform. Refer to [Create Webex Bot](https://developer.webex.com/messaging/docs/bots) for detailed instructions.

### Benefits of Webex channel integration

* **Enhanced user experience:** Users can interact with AI agents without switching platforms.
* **Faster task completion:** Interactive cards and contextual AI responses streamline workflows.
* **Enterprise-ready:** Securely integrates with corporate Webex accounts while maintaining compliance and auditability.
* **Scalable deployment:** Supports multiple AI agents and Webex spaces, enabling broad adoption across teams or departments.

### Deploy your agent to Webex channel

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can deploy the agent to a channel after creating and building an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.
* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing the agent.
    {% endhint %}

1. Navigate to the **Agent** page and go to **Configuration > Channels** in the left navigation menu.
2. On the **Channels** page, click **Connect** under the Webex channel.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FG8IT9VuyAsWWPp8NUtVD%2Fimage.png?alt=media&#x26;token=58453ff9-acb9-4658-8e64-47a8ad4b5324" alt=""><figcaption></figcaption></figure>

3. Specify the following details and click Save.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FvM2tEy3LtI117YQhZ76t%2FScreenshot%202025-10-24%20at%202.00.14%E2%80%AFPM.png?alt=media&#x26;token=ff47d372-b3e1-44ec-859e-ab8b0355b407" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="140.25">Parameter </th><th>Description</th><th>Mandatory</th></tr></thead><tbody><tr><td>Name</td><td>Indicates the <strong>Name</strong> used to identify the Webex channel.</td><td>Yes</td></tr><tr><td>Bot Username</td><td>Name of your Webex bot as it will appear in Webex and Webex App Hub.</td><td>Yes</td></tr><tr><td>Access Token</td><td>Access token for your Webex bot.</td><td>Yes</td></tr><tr><td>Bot ID</td><td>Unique system-generated ID for your Webex bot.</td><td>Yes</td></tr></tbody></table>

Now you can view the AI agent in your [Webex messaging](https://web.webex.com/sign-in) space. Start sending and receiving messages with AI agents directly in Webex.
