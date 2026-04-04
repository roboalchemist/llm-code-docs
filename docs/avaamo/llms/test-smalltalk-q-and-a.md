# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/test-smalltalk-q-and-a.md

# Test Smalltalk skill

Once the **Smalltalk** is created or uploaded successfully to your skill, you can test to ensure the skill provides appropriate responses for user queries.&#x20;

{% hint style="success" %}
**Key Point**: If you have added response filters to the skill responses that use user properties, then to test the agent, you can set the custom\_properties\[user\_property\_key]=value in the web channel URL. Example: custom\_properties\[office\_city]=Bangalore. See [Create custom user properties](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/create-custom-user-properties), for more information.
{% endhint %}

{% hint style="info" %}
**Notes**:&#x20;

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can test a skill immediately after creating the skill. See [Create new Smalltalk skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/create-new-knowledge-base), for more information.
* If you wish to test skill in an agent, then:
  * Navigate to the Agents tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/build-agents/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * In the Agent page, navigate to the Skills option in the left navigation menu. Search and open the required skill.&#x20;
    {% endhint %}

You can test the Smalltalk skill in any of the following ways:

* Using the **Agent simulator** from any page in the skill's left navigation pane&#x20;
* Using the **Test -> Simulator** option in the left navigation menu. This also displays the agent simulator in the bottom right corner.

### **Test using agent** simulator

* In the agent simulator, select a channel Web or C-IVR in which you wish to test. Note that this option is displayed if you have deployed your agent in both web and C-IVR channels. You can now ask queries and test if you are receiving appropriate responses from user queries.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-IxFY804it_ciH5Zui%2F-M-Iz7FMVzJqmnSh3zDf%2Fsmalltalk-test-result.png?alt=media\&token=d9508262-6322-4c07-9682-9d3b6d9105d7)

* Consider that you have [added French language](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-languages) in your agent. When you switch language to say French using [Language.switch](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/language.switch) command and ask any question from the Smalltalk skill in French, then the agent detects and responds to the question in French, as applicable:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F0q80SLDKLev0Xfic8m3R%2Fimage.png?alt=media\&token=b5f340a2-510a-43cc-8567-bf8743c6bc5b)

{% hint style="info" %}
**Note**: Smalltalk response is displayed only when the user query (including punctuations) exactly matches the training data provided in the Smalltalk.
{% endhint %}
