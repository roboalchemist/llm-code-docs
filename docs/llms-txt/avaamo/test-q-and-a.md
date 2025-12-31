# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-q-and-a-designer/test-q-and-a.md

# Test Q\&A skill

Once the question and answers are created or uploaded successfully to your skill, you can test to ensure the Q\&A provides appropriate responses for user queries.&#x20;

{% hint style="success" %}
**Key point**: If you have added response filters to the skill responses that use user properties, then to test the agent, you can set the custom\_properties\[user\_property\_key]=value in the web channel URL. Example: custom\_properties\[office\_city]=Bangalore. See [Create custom user properties](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/create-custom-user-properties), for more information.
{% endhint %}

{% hint style="info" %}
**Notes**:&#x20;

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* If you wish to test skill in an agent, then:
  * Navigate to the Agents tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/build-agents/manage-agents#search-agents), for more information.&#x20;
  * Click Edit to unlock the agent before editing.
  * In the Agent page, navigate to the Skills option in the left navigation menu. Search and open the required skill.&#x20;
    {% endhint %}

You can test the Q\&A skill in any of the following ways:

* Using the Agent simulator from any page in the skill's left navigation pane&#x20;
* Using the Test -> Simulator option in the left navigation menu. This also displays the agent simulator in the bottom right corner.

### **Testing using agent** simulator

* In the agent simulator, select a channel Web or C-IVR in which you wish to test. Note that this option is displayed if you have deployed your agent in both web and C-IVR channel. You can now ask queries and test if you are receiving appropriate responses from user queries.&#x20;
* Note that the questions need not be exact. The variations are automatically handled by the system with appropriate responses.&#x20;

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-JC1bAWpn2CgL4F5AB%2F-M-JCSA_pJVamQE967To%2Fqa-test-variation.png?alt=media&#x26;token=81b8581e-4ce4-49ce-92cf-06833f3c860c" alt=""></div>

* Consider that you have [added french languag](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-languages)e in your Q\&A skill. When you switch language to say french using [Language.switch](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/language.switch) command and ask any question from the Smalltalk skill in french, then the agent detects and responds to the question in french, as applicable:

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-JC1bAWpn2CgL4F5AB%2F-M-JCqIRMg46yn7F3pfI%2Fqa-test-language.png?alt=media&#x26;token=8635e4a3-3343-4fdc-9974-335a118d7a22" alt=""></div>
