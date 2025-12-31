# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/create-universal-agent/manage-member-agents.md

# Manage member agents

In the **Agents** -> **Member agents** section, you can perform the following actions for each Member agent as per your requirement:

* [View member agent](#view-member-agent)
* [View member details](#view-member-details)
* [Delete](#delete-member-agent)
* [Disable](#disable-member-agent)

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FP9XxCTWPbQSIild7T8wj%2Fmanage-member-agents.png?alt=media\&token=0d287d8b-ca65-4563-9d35-009c6c3ea25b)

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can perform all these actions immediately after adding member agents to the Universal agent. See [Create universal agent](https://docs.avaamo.com/user-guide/how-to/build-agents/overview-get-started#create-a-universal-agent) and [Add member agents](https://docs.avaamo.com/user-guide/how-to/build-agents/create-universal-agent/add-member-agents), for more information.
* If you wish to edit an agent, then:
  * In the Avaamo Platform UI, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing and publishing.
    {% endhint %}

### View member agent

Since a Universal agent is a "group of individual member agents", during Universal agent development it is helpful if the user can view the member agent implementation.

{% hint style="info" %}
**Note**: Viewing the member agent is based on the permissions provided to the user at the member agent level. See[ roles and permission](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions#agent-permissions) for information on permissions.
{% endhint %}

1. Click the 3 dots in the box of the member agent that you wish to open.
2. Select **View member agent**. The member agent opens in a separate tab if the user has sufficient permissions, else the unauthorized message is displayed.

### View member details

The basic details of the member agent such as UUID, owner, and member agent access token can be viewed:

1. Click the 3 dots in the box of the member agent - whose basic details you wish to view.
2. Select **View member details**. A pop-up box with the details of the member agent is displayed.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FdbNhfX0ZYYJNYirObzAl%2Fview-member-agent-details.png?alt=media\&token=9bafc86a-7db0-486b-919c-b367f57bc620)

### Delete member agent

You can delete a member agent from the Universal agent if it is no longer required.

* Click the 3 dots in the box of the member agent that you wish to delete.
* Select **Delete** and provide confirmation in the pop-u&#x70;**.** The member agent is deleted from the Universal agent. To add the deleted member agent back, you must provide the member agent's UUID and access token. See [add member agents](https://docs.avaamo.com/user-guide/how-to/build-agents/create-universal-agent/add-member-agents) for more information.

### Disable member agent

You can disable a member agent from the Universal agent as required. When you disable a member agent, the Universal agent does not use the member agent to respond to queries. When any user query is posted to the Universal agent with a disabled member agent, a corresponding error message is displayed in the JS error indicating the same. See [JS errors](https://docs.avaamo.com/user-guide/how-to/debug-agents#using-js-errors), for more information.

**To disable a member agent**:

* Click the 3 dots in the box of the member agent that you wish to disable.
* Select **Disable** and provide confirmation in the pop-u&#x70;**.** The member agent is disabled from the Universal agent. You can always enable a disabled member agent at any time by clicking the 3 dots in the box of the member agent and selecting **Enable.**
