# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/test-skill.md

# Test Dialog skill

You can test your skill using the agent simulator from any page available in the skill's left navigation pane without navigating back to the main agent page.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8o1bYqJmdWfIpU0KsZ%2F-M8o2xzfcdo5YRhtPvda%2Ftest-dialog-invocation.gif?alt=media\&token=1c21dab2-8023-48fb-9918-312ca1fb8a40)

From any page in the Dialog skill click the **agent simulator** in the bottom right corner. Select a channel Web or C-IVR in which you wish to test. Note that this option is displayed if you have deployed your agent in both web and C-IVR channels. You can now ask queries and test if you are receiving appropriate responses from user queries.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MNCAhiv8MAGxLADKNUQ%2F-MND-Jxt7a6_c3g8ybf-%2Fc-ivr-dialog-simulator.png?alt=media\&token=b908adce-5a62-457f-a895-7422e3189469)

{% hint style="info" %}
**Note**: If you have added response filters to the skill responses that use user properties, then to test the agent, you can set the custom\_properties\[user\_property\_key]=value in the web channel URL. Example: custom\_properties\[office\_city]=Bangalore. See [Create custom user properties](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/create-custom-user-properties), for more information.
{% endhint %}

**Few important examples are listed below**:

* You can add new invocation intents to your **Dialog** skill and test agent using the agent simulator from the **Invocation intent** page itself without navigating back to the main agent page.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8RJJ1a8MLRWISRp5wZ%2F-M8RLyyjGDV_rptqoYih%2Fwn-agent-chat-dialog.png?alt=media\&token=d0fb696e-44c3-4a40-95df-b2ba4d2dfa14)

* You can build a multi-turn conversational flow in your **Dialog** skill and test agent using the agent simulator from the **Dialog Designer** page itself without navigating back to the main agent page.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MF4Xy27vjfwSVcnJlHk%2F-MF4ZT69s8pvHcL4ATVL%2Fagent-chat-dialog-flow.png?alt=media\&token=d6af72f3-dd03-47d1-bbff-2c4bbdf68026)
