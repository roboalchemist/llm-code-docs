# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/manage-channel-settings.md

# Manage channel settings

This article lists certain common actions you can perform after configuring a channel:&#x20;

* [View and edit channel settings](#view-and-edit)
* [Disconnect a channel](#disconnect)
* [Delete a channel](#delete)

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* After creating and building an agent, you can deploy the agent to a channel. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.
* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](applewebdata://9AE47367-043D-436A-BAB1-053A8B89E2A1/@avaamo/s/avaamo/~/edit/drafts/-Lsoojy2kKRX1KXPWAZ2/how-to/build-agents/manage-agents#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing
    {% endhint %}

In the **Agent** page, navigate to the **Configure -> Channels** option in the left navigation menu.

### View and Edit

The following steps describe how to view and edit channel settings:

1. On the **Channels** page, click **View** on the channel you wish to edit.
2. Channel Settings as configured are displayed. Edit the channel settings as required and click **Save** to save the channel settings.

### Disconnect

The following steps describe how to disconnect an agent deployed on a channel:

* On the Channels page, click **Disconnect** in the Channel.
* An alert message is displayed. Click **OK**.&#x20;
* The agent is disconnected and no longer deployed on the corresponding channel. However, note that the configured channel is still available on the Channels page and you can click **Connect** to re-deploy the agent back on the corresponding channel if required.

{% hint style="info" %}
**Note**: Disconnecting the channel also invalidates its end-point URL. Hence, disconnecting a channel must be done with caution, as the end-point URL if used in any other integrations also gets invalidated.
{% endhint %}

### Delete

The following steps describe how to delete custom channel settings:

* On the Channels page, click **Delete** in the Custom Channel.
* An alert message is displayed. Click **OK**.&#x20;
* The configured channel is no longer available on the **Channels** page; hence, the agent is no longer deployed on the corresponding channel.
