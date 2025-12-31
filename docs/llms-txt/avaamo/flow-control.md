# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/flow-control.md

# Flow control

You can use goto\_node, goto\_intent, goto\_output, execute\_intent, and idle\_prompt functions in JS to customize the agent flow navigation. See [how-to control skill flow](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/controlling-skill-flow), for a sample scenario.

{% hint style="success" %}
**Key Points**:&#x20;

* Flow control statements are applicable only to Dialog skills. You can transfer only to the Dialog skill nodes or to the main node.
* goto\_node and goto\_output are not supported in Returning User Message Handler JS block.
* goto\_node and goto\_output perform the same functionality and you can use them both interchangeably.
* goto\_intent is not supported in "custom intent" JS sections or in "pre-unhandled" intent.
* execute\_intent works only in post-processing.
* Intents that lead to disambiguation responses are not supported in execute\_intent.
* You can add upto 5 continuous iterations of flow control statements in a single execution. As a best practice, it is recommended to revisit your flow if it requires more than 5 continuous iterations of flow control statements.
  {% endhint %}

### At a glance

The following table summarizes the key points of different flow control statements that can be used in JS to customize the agent flow navigation:

| Flow control                                  |                                                           What?                                                           | Output node | Post-processing | JS intents |
| --------------------------------------------- | :-----------------------------------------------------------------------------------------------------------------------: | :---------: | :-------------: | :--------: |
| goto\_node                                    | Displays and transfers the flow to the skill message configured at the specified intent after executing the current node. |      ✅      |        ✅        |      ❌     |
| goto\_output                                  | Displays and transfers the flow to the skill message configured at the specified intent after executing the current node. |      ✅      |        ✅        |      ❌     |
| execute\_intent                               |                <p>Transfers the flow to the specified intent  </p><p>and executes the specified intent.</p>               |      ❌      |        ✅        |      ❌     |
| <p>goto\_intent </p><p>in post-processing</p> |           Transfers the flow to the specified node and executes the current user query in the transferred node.           |      ❌      |        ✅        |      ❌     |
| goto\_intent in the output node               |   Transfers the flow to the specified intent and waits for the next user query to be executed at the transferred intent.  |      ✅      |        ❌        |      ❌     |

### goto\_node

Displays and transfers the flow to the skill message configured at the specified intent after executing the current node.

```javascript
goto_node('<<skill_key>>.<<intent_key>>') 

Specify only '<<intent_key>>', if you wish to transfer the flow in the current skill
Specify 'main', if you wish to transfer to the main node.
```

| Examples                                                  | Description                                                                                                                                  |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| return goto\_node('starters');                            | Displays the skill message configured at the "starters" intent and correspondingly transfers the flow.                                       |
| return goto\_node('register\_skill.registration\_start'); | Displays the skill message configured at the "registration\_start" intent in "register\_skill" skill and correspondingly transfers the flow. |
| return goto\_node('main');                                | Displays the message configured in the "Greeting skill" or main node and transfers the flow to the main node.                                |

### goto\_intent

goto\_intent behavior is different in the output node and post-processing. When you specify goto\_intent in the output node, you are indicating at which intent the next user query must be evaluated. When you specify goto\_intent in post-processing you are indicating at which node the current user query must be evaluated.&#x20;

#### goto\_intent in output node

goto\_intent in the output node transfers the flow to the specified intent and waits for the next user query. The next user's query is evaluated at the transferred intent. This behavior is similar to the "Goto Intent" option available in the Advanced settings. See [Advanced settings](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/advanced-settings), for more information.&#x20;

```javascript
goto_intent('<<skill_key>>.<<intent_key>>','<<intent>>') 

Specify only '<<intent_key>>', if you wish to transfer the flow in the current skill
Specify 'main', if you wish to transfer to the main node.
```

The following lists a few examples of goto\_intent in the output node:

| Examples                                                    | Description                                                                    |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------ |
| return goto\_intent('starters');                            | Transfers the flow to the specified intent in the current skill.               |
| return goto\_intent('register\_skill.registration\_start'); | Transfers the flow to "registration\_start" intent in "register\_skill" skill. |
| return goto\_intent('main')                                 | Transfers the flow to the first or the main step of the agent.                 |

#### goto\_intent in post-processing

When the goto\_intent is specified in post-processing, the user's intent is still not completely evaluated. The current user query or the intent specified in goto\_intent (if any) is evaluated at the transferred node.

goto\_intent in post-processing transfers the flow to the specified node and executes the current user query in the transferred node (if the intent is not specified in goto\_intent). If you have specified an intent in goto\_intent, then the intent is executed at the transferred node:

* If the query in the transferred node returns true, then the response is delivered by the transferred node.&#x20;
* If the query in the transferred intent returns false, then an unhandled response is delivered.

```javascript
goto_intent('<<skill_key>>.<<intent_key>>','<<intent>>') 

Specify only '<<intent_key>>', if you wish to transfer the flow in the current skill
Specify 'main', if you wish to transfer to the main node.
```

The following lists a few examples of goto\_intent in post-processing:

| Examples                                                        | Description                                                                                                                                               |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| return goto\_intent('starters');                                | Transfers the flow to the specified intent in the current skill and executes the current user query at the transferred node.                              |
| return goto\_intent('register\_skill.registration\_start');     | Transfers the flow to "registration\_start" intent in "register\_skill" skill and executes the current user query at the transferred node.                |
| return goto\_intent('starters', 'I want to get some starters.') | Transfers the flow to the specified intent in the current skill and executes the specified intent 'I want to get some starters.' at the transferred node. |

### goto\_output

Transfers the flow to the specified node number or main and displays the output of the node.

```javascript
goto_output('<<skill_key>>.<<intent_key>>') 

Specify only '<<intent_key>>', if you wish to transfer the flow in the current skill
Specify 'main', if you wish to transfer to the main node.
```

<table><thead><tr><th width="393">Examples</th><th>Description</th></tr></thead><tbody><tr><td>return goto_output('starters');</td><td>Displays the skill message configured at the "starters" intent and correspondingly transfers the flow.</td></tr><tr><td>return goto_output('register_skill.registration_start');</td><td>Displays the skill message configured at the "registration_start" intent in "register_skill" skill and correspondingly transfers the flow.</td></tr><tr><td>return goto_output('main');</td><td>Displays the message configured in the "Greeting skill" or main node and transfers the flow to the main node.</td></tr></tbody></table>

### execute\_intent

Transfers the flow to the specified intent number and executes the specified intent. Since an intent can have multiple nodes, you can use execute\_intent for transferring to different nodes within an intent, based on some condition in the post-processing JavaScript.

```javascript
execute_intent('<<skill_key>>.<<intent_key>>','<<intent>>') 

Specify only '<<intent_key>>', if you wish to transfer the flow in the current skill
Specify 'main', if you wish to transfer to the main node.
```

| Examples                                                          | Description                                                                                                     |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| return execute\_intent(1,'order pizza');                          | Transfers the flow to intent number 1 and executes 'order pizza' intent in the current skill.                   |
| return execute\_intent(2.3,'order pizza');                        | Transfers the flow to intent number 3 in skill number 2 and executes 'order pizza' intent at 2.3                |
| return execute\_intent('main','I want to check my order status'); | Transfers the flow to the main node and executes the intent 'I want to check my order status' at the main node. |

### idle\_prompt

Indicates the response time the agent waits for the user query and post the wait period the skill message configured at the specified intent is displayed.&#x20;

```javascript
idle_prompt(<<time_in_seconds>>,'<<skill_key>>.<<intent_key>>')

Specify only '<<intent_key>>', if you wish to transfer the flow in the current skill
Specify 'main', if you wish to transfer to the main node.
```

**Example**: return idle\_prompt(10,'main');

The agent waits for 10 seconds and then transfers the flow to the main node or the "Greeting skill" and displays a message as configured at the "Greeting skill".

{% hint style="info" %}
**Note**: You can transfer the flow to a greeting node or to a node in the Dialog skill.
{% endhint %}

### Examples

The following Dialog flow is used as a reference for the examples provided in the comparison table:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8tK0XKwP2FE8d3cGtd%2F-M8u7Cnh3J3hJJBbcy3f%2Fdialog-flow.png?alt=media\&token=c250ff6f-10a5-4ed4-bc3d-bb6cced1bdcc)

The following Q\&A skill is used as a reference for the examples provided in the comparison table:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8tK0XKwP2FE8d3cGtd%2F-M8u7QPdlkqKhuByhXPi%2Fqa-flow.png?alt=media\&token=42d73e30-d7c4-4bc2-9f47-e569a4411e9c)

**Example 1**: Consider the execution of the following statement in the **post-processing** script of node 2:

|                                           <p>return goto\_node('4');</p><p>return goto\_output('4');</p><p>return goto\_intent('4','yes'); </p><p>return execute\_intent('3','yes');  </p>                                          |                                                                                                  return execute\_intent('3','no');                                                                                                  |                                                                                                      return goto\_intent('4');                                                                                                      |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8tK0XKwP2FE8d3cGtd%2F-M8tjXz4j_y_1YRRbtO8%2Fflow-example-1.png?alt=media\&token=d80e00f4-0401-4c8c-a377-8e0215e1843c) | ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8tK0XKwP2FE8d3cGtd%2F-M8tjBIEn_afcKuER_iY%2Fflow-example-3.png?alt=media\&token=a7592a8e-84a0-4f2c-8956-1f1f7843bcb8) | ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8tK0XKwP2FE8d3cGtd%2F-M8tkXHKO3XYPdi0fUFh%2Fflow-example-4.png?alt=media\&token=c7934105-5fe6-42b7-968b-e7a88e28ea2a) |

{% hint style="success" %}
**Key point:** Here, note the following point when "return goto\_intent('4');" statement is executed. Since the current user query is "veg" and that is not handled at node number 4, an unhandled response is returned.
{% endhint %}

**Example 2**: Consider the execution of the following statement in the **post-processing** script of node 15:

|                                                                                <p>return goto\_node('main');</p><p>return goto\_output('main'); </p>                                                                                |                                                                                  return execute\_intent('main','Tell me more about reward policy');                                                                                 |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8tK0XKwP2FE8d3cGtd%2F-M8tsTPRlXi45eH0AIXs%2Fflow-example-5.png?alt=media\&token=999206d9-278c-4796-b035-2701ed2bad3b) | ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8tK0XKwP2FE8d3cGtd%2F-M8tt_NGJUshlGXyN_ck%2Fflow-example-6.png?alt=media\&token=bda4215f-2bbd-4186-8e70-cab37923b21d) |

**Example 3**: Consider the execution of the following statement in the **output node** of node 18:

|                                                                                   <p>return goto\_node('10');</p><p>return goto\_output('10');</p>                                                                                   |                                                                                                      return goto\_intent('10');                                                                                                      |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8tK0XKwP2FE8d3cGtd%2F-M8u1eP8Z1M6yscXDr4o%2Fflow-control-11.png?alt=media\&token=5ed8d05d-ad3d-43ea-8622-c4f5392bd61f) | ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8tK0XKwP2FE8d3cGtd%2F-M8u27p15FDA2BduuccO%2Fflow-control-12.png?alt=media\&token=77f1265e-df88-4736-b57c-193716b84b13) |

{% hint style="success" %}
**Key point:** Here, note the following point when the "return goto\_intent('10');" statement is executed. This transfers the execution to intent number 10 and waits for the next user's input. The next user's input is evaluated at intent number 10.
{% endhint %}

**Example 4**: Consider the execution of the following statement in the **output node** of node 15:

|                                                                                        return goto\_node('main');return goto\_output('main');                                                                                        |                                                                                                     return goto\_intent('main');                                                                                                     |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                                                 <p>return goto\_node('main');</p><p>return goto\_output('main'); </p>                                                                                |                                                                                                     return goto\_intent('main');                                                                                                     |
| ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8tK0XKwP2FE8d3cGtd%2F-M8u5G2CJlCTP0Q0t3Z3%2Fflow-control-13.png?alt=media\&token=b94d8edf-55a4-490e-ab4c-aa2b38054388) | ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M8tK0XKwP2FE8d3cGtd%2F-M8u66V35n0c1Wqw7LMK%2Fflow-control-14.png?alt=media\&token=8146a486-dfb4-47f0-98a2-ef7c43ef8b3e) |

{% hint style="success" %}
**Key point:** Here, note the following point when the "return goto\_intent('main');" statement is executed. This transfers the execution to the 'main' node and waits for the next user's input. The next user's input is evaluated at 'main'.
{% endhint %}
