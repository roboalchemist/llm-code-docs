# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/facebook-channel/persona-configuration.md

# Persona Configuration

The Facebook channel integration on the Avaamo platform supports creating new and fun **Personas** for your agent, deployed on your Facebook page. Personas are like the different avatars that you can assign to your agent.

#### **Prerequisites**

Let us create a fun persona for our agent, ensure you have the following:

* Admin access to your Facebook page.
* Images that need to be used as agent avatars.
* Access to the agent to configure personas.

{% hint style="info" %}
**Note**: This persona concept is available only on the Facebook channel.
{% endhint %}

## Configure Persona on Avaamo Platform

You would need to configure the persona for the agent on the Avaamo platform by using javascript code or by selecting the persona option under agent skill's responses.

### Javascript Code

To add Facebook persona feature to your agent using the javascript code, follow the steps below:

* In the **Agent** -> **Configuration -> JS files** tab, click **Add new**.&#x20;
* Specify the name of the JS file and click **Create**.&#x20;
* A new empty JS file is created. In the **Scripts** page, click the JS file and add the code as required.

```
if(!Storage.global.get("Jerry")){
  let Jerry = await(Facebook.findOrCreatePersona({name: "Jerry", profile_picture_url: "https://i.pinimg.com/originals/c0/16/7f/c0167fe13c1217112025cc41ae20abfc.jpg"}));
  Storage.global.set("Jerry", Jerry.id);
}
```

* Click Save.
* In the **Agent** -> **Skills** tab select the required skill.
* In the **Dialog skill** page, click the **Implementation** tab.&#x20;
* Click on the intent and on the user intent window, enable the switch to **Yes** for post-processing.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly-hd2B68sPdOMlOXVb%2F-Ly-iWKfJQSpdm52bhqZ%2Fagent-deploy-fb-persona-2.png?alt=media\&token=1da3b2a1-5c44-4248-85b3-7bb340fd7c29)

* For the Post-processing Script enter the javascript code.

```
Facebook.switchPersona(Storage.global.get("Tom"));
```

* Click on Save to add the javascript code to the agent flow.

### Persona Button

To add the Facebook persona feature to your agent using the persona button, follow the steps below:

* In the **Configuration -> Settings** tab, click on **Add New** in Persona section.
* Enter the name of the persona and upload a persona avatar.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly-hd2B68sPdOMlOXVb%2F-Ly-ivBmJkLvHEh1Hldk%2Fagent-deploy-fb-persona-4.png?alt=media&#x26;token=ddb86677-54c3-4f4a-b221-627f64595367" alt=""></div>

* Click on the dialog designer tab and click on the skill response where you want to add the persona feature. Click on the plus icon and select **Switch Persona** from the list.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-Q91f93zoxIBR-6DFO%2F-M-Q9QDdu0TKuVA1GDJ6%2Fagent-deploy-fb-persona-5.png?alt=media\&token=9167e8b3-e488-4748-ad20-e5d55e418010)

* On the right panel, under persona, select the persona you want your skill to switch.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-Q91f93zoxIBR-6DFO%2F-M-Q9gbOMDCwdxsHPEAS%2Fagent-deploy-fb-persona-6.png?alt=media\&token=55addf0c-c221-4ab4-a0bf-dc9bd19462b0)

## Agent on Facebook

When the agent is deployed on the Facebook channel, the persona will be available to the end-user.\
When the end-user query matches with the ‘User Intent’, then the responding agent persona avatar will change as per the persona configured.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly-hd2B68sPdOMlOXVb%2F-Ly-jCMwE5kSYnz1vGSy%2Fagent-deploy-fb-persona-7.png?alt=media&#x26;token=313b5745-082b-4363-8a98-005cd627a244" alt=""></div>
