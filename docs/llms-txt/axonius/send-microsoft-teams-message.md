# Source: https://docs.axonius.com/docs/send-microsoft-teams-message.md

# Microsoft Teams - Send Message

**Microsoft Teams - Send Message** posts a message to a Microsoft Teams channel for assets returned by the selected query, or assets selected on the relevant asset page.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Webhook URL** - The incoming Webhook URL that Microsoft Teams generates for sending messages to a channel. See [Generating the Microsoft Teams Incoming Webhook URL](#generating-the-microsoft-teams-incoming-webhook-url) below on how to generate and add an incoming Webhook URL to a Microsoft Teams channel.

* **Title** - A title for the message. If you do not give a title, the title will be Send Microsoft Teams Message + 'for Query:' + \[query name].

## Additional Fields

* **Subtitle** - A title for the message. If you do not give a title, the title will be *Send Microsoft Teams Message + 'for Query:' + \[query name]*.

* **Title for current number of assets in message body** - Enter a title to describe the current number of assets in the message body. The default title is *Current Number of Assets*.

* **Title for previous number of assets in message body** - Enter a title to describe the previous number of assets in the message body. The default title is *Previous Number of Assets*.

* **Additional text in message body** - Choose how to use the text added to the default message:
  * **Prepend Message Body** - Adds the entered text before the default message.
  * **Append Message Body** - Add the entered text after the default message.
  * **Replace Message Body**  - Replace the default message with the entered text.

* **Create list of predefined responses** - This field is only available in an action that is added to a Workflow. Enter a list of response buttons to be shown in the Microsoft Teams message in the order that they are added into this field. Click **Add** to add each possible response to the list. When a response button is clicked in a Microsoft Teams message that is sent, the workflow continues based on that button. Use Microsoft Power Automate to configure what happens when a response button is clicked.

* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

## Generating the Microsoft Teams Incoming Webhook URL

**To add an incoming webhook to a Microsoft Teams channel and acquire the correct webhook URL:**

1. Sign into *teams.microsoft.com* with a user that has permissions to the channel you want to use for notifications.
2. From the left hand menu, click **View more apps** and select **Workflows**.
3. Select **+ New flow**.
4. In the **Create** tab, from the **Templates** menu, select the tile of **Post to a channel when a webhook request is received**.

<Image alt="Teams-1" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Teams-1.png" />

6. In the **Create a flow** dialog for the selected template, enter a **Flow name** and click **Next**.

7. Select a **Microsoft Teams Team** and a **Microsoft Teams Channel**.

8. Click **Create flow.**

9. A message appears notifying you that your workflow was created. Click **Done**.

10. The URL is generated. Click the copy icon to copy the URL and then click **Done** again.
    ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Teams-2.png)

11. Paste the copied URL into the **Webhook URL** field in this EC action. This is the endpoint URL that you require to send data to Microsoft Teams.

<Callout icon="💡" theme="warn">
  Legacy Webhook Procedure

  You can also add a webhook to a Microsoft Teams channel using the following procedure. However, note that this option **will be deprecated by Microsoft  by the end of 2024**.

  1. Sign into *teams.microsoft.com* with a user that has permissions to the channel you want to use for notifications. You add the incoming webhook to this channel.
  2. In Teams, select **Settings `>` Member permissions `>` Allow members to create, update, and remove connectors**, so that you  can add, modify, or delete a connector.
  3. Open the channel, click the 3-dot menu in the upper-right corner, and select **Connectors**.
  4. In the **Connectors** dialog that opens, type *incoming webhook* in the **Search** bar.
  5. Near **Incoming Webhook**, click **Add**, and in the screen that opens, click **Add** again to install the app.
  6. Near **Incoming Webhook**, click **Configure**, and name your webhook with a name, in our case, *Axonius*. Optionally, click **Upload Image** to upload a different image.
  7. Click **Create**.
  8. Your Incoming Webhook named *Axonius* has been created and it has been integrated with the Microsoft Teams channel you have chosen. The webhook URL is displayed in the box.
  9. Paste the URL into the **Webhook URL** field in this EC action. This is the endpoint URL that you require to send data to Microsoft Teams.
  10. Click **Done**. The webhook is now available in the Microsoft Teams channel.
</Callout>

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).