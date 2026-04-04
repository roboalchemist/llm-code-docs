# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/create-custom-html-web-views.md

# Create custom HTML web views

You can create custom HTML web views on **Web Channel** and **Facebook** for the skill responses configured using a card, carousel, or list view. See [Build Skill Response](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses) and [Web Channe](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel)l, for more information on creating custom HTML web views for a **card, carousel, and list view**.

Consider that you wish to create a **custom HTML web view** that displays more details on how pizzas are prepared in the **Order Skill** of **Mac Pizza Agent** via a "Know more.." button.

**To create a custom HTML web view**:

* Click the skill response where you wish to custom HTML web view.&#x20;
* Add a button, select **Webview (HTML)**.&#x20;
* Add HTML code and select a view such as **Compact**, **Tall**, and **Full**.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LwWh2zZZs52k7uwGwH0%2F-LwWlP0_BtxUDZ3ngdhZ%2Fjs-webview-types.png?alt=media&#x26;token=9db7cef9-51cc-45bd-9028-79b67a639119" alt=""></div>

* Click **OK** and **Save** the skill.
* In the **Skill** page, click the agent icon in the bottom right corner. Either you can use **goto\_node\_<\<node number>>** to directly test the node or specify intents that navigate to that node.
* Click the link that is configured to display the web view. The custom web view HTML as specified in the response is displayed.

{% hint style="info" %}
**Notes**:&#x20;

* Currently, Compact, Tall, and Full view are not supported in the Microsoft Teams channel due to the limitations on the channel's side. See [Microsoft Teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams), for more information on deploying your agent in the MS Teams channel.
* If the agent response contains sensitive PII data such as name, account number, password, then it is recommended to mask the agent responses to protect user privacy. See [Agent response masking](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/information-masking#masking-agent-responses), for more information.
  {% endhint %}
