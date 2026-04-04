# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/cisco-pcce.md

# Cisco PCCE

{% hint style="info" %}
**Note**: You can connect to a channel only if it is enabled for your account or company. If you wish to enable a channel, then contact Avaamo Support for further assistance. Note that only the web channel is enabled by default.
{% endhint %}

Cisco Packaged Contact Center Enterprise (Packaged CCE or PCCE) provides an enterprise-class contact center deployment model that is easy to install, configure, and administer. See [Cisco PCCE](https://developer.cisco.com/docs/packaged-contact-center/), for more information.

The agents developed on the Avaamo platform can be deployed on the **Cisco PCCE** channel. In this article, the following steps are detailed:

1. [ Before you begin](#before-you-begin)
2. [Deploy your agent in Cisco PCCE](#deploy-your-agent-in-nice-incontact)
3. [Manage channel settings](#manage-channel-settings)

## Before you begin

* Get the identifier (or FQDN) of Cisco PCCE SIP. You must configure this in the channel settings. See [Deploy your agent in Cisco PCCE](#deploy-your-agent-in-nice-incontact), for more details.
* Avaamo requires customer source IPs in order to allow traffic to Avaamo SIP. Send a request to Avaamo Support to whitelist the IP addresses.

## Deploy your agent in Cisco PCCE

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can deploy the agent to a channel after creating and building an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.
* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](applewebdata://9AE47367-043D-436A-BAB1-053A8B89E2A1/@avaamo/s/avaamo/~/edit/drafts/-Lsoojy2kKRX1KXPWAZ2/how-to/build-agents/manage-agents#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editin&#x67;**.**
    {% endhint %}

**To configure a Cisco PCCE channel:**

* In the **Agent** page, navigate to the **Configure -> Channels** option in the left navigation menu.
* On the Channels page, click **Connect** in **Cisco PCCE** Channel.
* Specify the following channel setting details:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FYDbPzX4Ma3JV2jnyKLZm%2FCisco-pcce-new-channel.png?alt=media\&token=96cac3ba-a54d-464d-8610-b50b297ae661)

<table><thead><tr><th width="176.94241925087732">Parameter</th><th width="569.8947368421052">Descriptions</th></tr></thead><tbody><tr><td>Name</td><td>Indicates the <strong>Name</strong> used to identify the Cisco PCCE channel. Note that you can have upto 150 characters in the channel name.</td></tr><tr><td>Identifier</td><td>Indicates the identifier (or FQDN) of Cisco PCCE SIP.</td></tr><tr><td><p>Languages and </p><p>Playback Voice for</p></td><td><p>Select the language and configure the voice or the persona to be used by your agent in the interactive phone conversations with the user. </p><p></p><p>Each language has a different set of voice personas that you can choose from. Select the persona from the options provided in the "Playback voice for &#x3C;&#x3C;language>>" section:</p><ul><li>As with any enterprise voice, audio, or video application, each region or country has its own phone number to dial. </li><li>Similarly, in the Cisco PCCE channel, you choose the language of the region or country where you wish to share the configured number. </li><li>If you wish to share the number in multiple regions, then set up the Cisco PCCE channel specific to each language. Note that one Cisco PCCE channel is specific to only one language.</li><li>To hear the voice preview, type any text in the text area and click the play button. You can also download the voice preview if required.</li><li>You can select only those languages for which the agent is configured and those that are supported in the Cisco PCCE channel. If you have switched to a language that is not supported in the Cisco PCCE channel, then the agent responds in the default language.</li></ul><p>See <a href="../add-languages">Add languages</a> and <a href="voice-supported-languages">Supported languages</a>, for more information. </p></td></tr><tr><td>Live agent transfer mode</td><td><p>Select the request mode for Live agent transfer in SIP: </p><ul><li><strong>invite</strong>: Initiate a dialog for establishing a call. The request is sent by a user agent client to a user agent server.</li><li><strong>refer</strong>: Ask the recipient to issue a request for the purpose of call transfer. Note that this is a default method used in the Avaamo Platform and this works for both SIP and PSTN approaches. </li></ul><p>See <a href="../../../../build-skills/create-skill/customize-your-skill/how-to/forward-call-c-ivr-channel#for-refer-transfer-mode">Smartcall.forward</a>, for more information on how to transfer and forward the call in SIP.</p></td></tr><tr><td>Speech timeout</td><td><p>Indicates a maximum wait time of the agent within which a user response is expected. If the user response is not received within the time-out period, then an automated message is rendered back to the user indicating that the agent is awaiting the user response. Currently, this is a standard message and cannot be customized.</p><ul><li>The default value is 1 second.</li><li>Use the up and down arrows to increase or decrease time as required.</li></ul></td></tr></tbody></table>

* Click **Save** to save the SIP channel configuration details.&#x20;
* Click **Download SIP Certificate** to download a "pem" file of the SIP certificate. This must be used to configure Avaamo Platform Cisco PCCE SIP details on the customer's side of the call center stack.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fwwj5WsXKfY8k6Prc0qPY%2FCisco-pcce-new-channel-save.png?alt=media\&token=e41dc6e8-ed64-4320-9d63-b7b04cc183fa)

* Note that Avaamo also requires customer source IPs in order to allow traffic to Avaamo SIP. Send a request to Avaamo Support to whitelist the IP addresses.

## Manage channel settings

After you configure the channel settings, you can view, edit, disconnect and delete the channel settings as per your requirements. See [Manage channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/manage-channel-settings), for more information.
