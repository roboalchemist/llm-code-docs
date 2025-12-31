# Source: https://docs.avaamo.com/user-guide/quick-start-tutorials/add-dialog-skill.md

# Add Dialog skill

You can start by either creating a new dialog skill in the agent or by importing an existing skill to your agent.

Consider that wish to create an "Order Skill" for "Mac Pizza Restaurant". This article explains how to:

1. [Create a new Dialog skill in the agent](#step-1-create-a-new-dialog-skill-in-the-agent)
2. [Add invocation intent to Dialog skill](#step-2-add-invocation-intent-to-dialog-skill)
3. [Change default greeting message in Dialog skill](#step-3-change-default-greeting-message-in-dialog-skill)
4. [Test Dialog skill](#step-4-test-dialog-skill)

{% embed url="<https://youtu.be/MycJaKrC2MA>" %}

{% hint style="info" %}
**Note**: An invocation intent is an intent or a training phrase that invokes the skill when added to an agent. See [Add invocation intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-invocation-intent), for more information.
{% endhint %}

### Step 1: Create a new Dialog skill in the agent

* In the **Agent** page, navigate to the **Skills** option in the left navigation menu and click **Add skill** in the Agent skills page.
* In the **Skill builder** page, select **Dialog** and click **Create**.&#x20;
* Specify Skill name, Skill description, Skill key, and click **Create**. See [Create a new Dialog skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-dialog-skill), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MZqHaB4vq6WOW41_DQk%2F-MZqIEqiEYPbeKYtz3WS%2Fqs-dialog-skill-create.png?alt=media\&token=84e8b827-f134-4eef-95c8-ace64a639c59)

* A new empty **Dialog skill** is created.&#x20;

### Step 2: Add invocation intent to Dialog skill

* In the **Dialog skill** page, click **Invocation intent** in the left navigation menu. Specify the training phrases required to invoke the skill. See [Add invocation intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-invocation-intent), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-9J0Xf18BKXX4gEW91%2F-M-9LVTyNaseHSwq2wFO%2Fqs-dialog-skill-invocation-intent.png?alt=media\&token=952dcf77-ae2e-4797-9b9b-d1bdc28801c8)

* Save the skill. After creating the invocation intent, the next step is to build a conversational dialog flow. By default, a greeting node and an unhandled node is provided for you. Start by changing the default greeting message; this is the first message displayed to the user after the skill is invoked.

### Step 3: Change default greeting message in Dialog skill

* In the **Dialog skill** page, click the **Implementation** tab.&#x20;
* Click the default greeting message node, in the dialog flow and update the greeting message. See [Change default greeting message](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/change-default-greeting-message) and [Build skill responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses), for more detailed information on different skill responses and **Advanced Settings**.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MOk6m0JMfN2YpuNCPbe%2F-MOk7kctgLJUhtXBzbwU%2Fquick-start-dialog-greeting-message.png?alt=media\&token=827303c1-f095-4625-bad0-4355188eadec)

* Click **Save**. You can now test the skill after adding the invocation intent and updating the greeting message.

### Step 4: Test Dialog skill

You can test the **Dialog skill** in any of the following ways:

* Using the **Agent simulator** from any page in the skill's left navigation pane&#x20;
* Using the **Test -> Simulator** option in the left navigation menu.&#x20;
* Post a user query to invoke this skill. Verify if the greeting message of the skill is displayed in the agent. As you build the flow, you can continue to test and verify your flow incrementally.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FC1FRbNG5vJYQCEORRUNm%2Fimage.png?alt=media\&token=1741b8db-e1b1-4451-ae8e-07288466b63d)

{% hint style="info" %}
**Note**: For extensive and continuous testing, you can use regression testing. See [Regression testing](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing), for more information.&#x20;
{% endhint %}

### Next steps

You can continue to edit the skill by [building dialogs](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill) with user intents and skill responses. Ensure you [test your skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/test-skill) at each step.&#x20;

You can navigate to the [Debug](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/debug-skill) section in the Dialog Studio to troubleshoot your skill if required.&#x20;
