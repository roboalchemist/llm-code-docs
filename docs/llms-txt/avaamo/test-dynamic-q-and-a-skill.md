# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a/test-dynamic-q-and-a-skill.md

# Test Dynamic Q\&A skill

Once the question and answers are created or uploaded successfully to your skill, you can test to ensure the Q\&A provides appropriate responses for user queries.&#x20;

{% hint style="success" %}
**Key point**: If you have added response filters to the skill responses that use user properties, then to test the agent, you can set the custom\_properties\[user\_property\_key]=value in the web channel URL. Example: custom\_properties\[office\_city]=Bangalore. See [Create custom user properties](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/create-custom-user-properties), for more information.
{% endhint %}

{% hint style="info" %}
**Notes**:&#x20;

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can test a skill immediately after creating the skill. See [Create new Dynamic Q\&A skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a/create-a-new-dynamic-q-and-a-skill), for more information.
* If you wish to test skill in an agent, then:
  * Navigate to the Agents tab in the top menu. Search and open the required agent.  See [Search agents](https://docs.avaamo.com/user-guide/build-agents/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * Click Edit to unlock the agent before editing.
  * In the Agent page, navigate to the Skills option in the left navigation menu. Search and open the required skill.&#x20;
    {% endhint %}

You can test the Dynamic Q\&A skill in any of the following ways:

* Using the **Agent simulator** from any page in the skill's left navigation pane&#x20;
* Using the **Test -> Simulator** option in the left navigation menu. This also displays the agent simulator in the bottom right corner.

### **Testing using agent** simulator

* In the agent simulator, select a channel Web or C-IVR in which you wish to test. Note that this option is displayed if you have deployed your agent in both web and C-IVR channels. You can now ask queries and test if you are receiving appropriate responses from user queries.&#x20;
* Note that the questions need not be exact. The variations are automatically handled by the system with appropriate responses.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F14cxVqpmQTt3haRKiNnB%2Fimage.png?alt=media\&token=56786048-e0f5-4897-8b7d-2b4cbdcc6c68)

* Consider that you have [added French language](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-languages) in your agent. When you switch language to say french using [Language.switch](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/language.switch) command and ask any question from the Q\&A skill in French, then the agent detects and responds to the question in French, as applicable:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fk465KvfDMN216AZUXloj%2Fimage.png?alt=media\&token=ec7b55a2-5fcf-4a39-a88a-03b9c72e27f2)
