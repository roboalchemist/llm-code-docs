# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing/regression-test-file-format-1.md

# Regression test file format - V2

This article describes the new and improved version of the regression test file format referred to as "Version 2 (V2)" and how to understand results after executing the regression test using the V2 format.&#x20;

* [File format](#file-format)
* [Understanding results](#understanding-results)

## Why Version 2 format?

Version 2 file format of regression testing is a new improved version. The basic principle of writing the test case differs in V1 and V2 formats and the improved format in V2 addresses certain shortcomings of the V1 format.&#x20;

* Regression test - V1 format file, is a long list of comma-separated flows with skill and intent keys, along with the responses of each node in an additional column required to test multi-turn conversations. See [Regression test file format - V1](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-test-file-format#file-format), for more information.
* Regression test - V2 format file, is based on test identifiers. Each step in the flow is a row and hence, there are no additional columns of response nodes are required in the V2 format to test multi-turn conversations. Based on the way the test identifiers are defined, the platform infers the flow and the sequence of execution. See [Regression test file format - V2](#file-format), for more information.&#x20;

The following table summarizes a few key differences and improvements of the Regression test - V2 format file:

<table><thead><tr><th width="162.33333333333331">Areas</th><th>Regression test file format - V1</th><th>Regression test file format - V2</th></tr></thead><tbody><tr><td>Ease-of-use</td><td><p>Understanding and writing test cases is a time-consuming process. </p><p></p><p></p></td><td><p>Test identifiers make it easier to write test cases. </p><p></p><p></p></td></tr><tr><td>Multi-turn conversation flow testing</td><td>Requires a long list of comma-separated flows with skill and intent keys and many additional columns with responses for each node.</td><td>Requires the developers to write the test cases with proper test identifiers, each in a separate row. The rest of the inference of grouping and executing the test cases is done by the Platform.</td></tr><tr><td>Scalability and Maintainability </td><td><p>With the comma-separated list, it is not easy to scale and maintain new test cases or to augment the existing test cases.</p><p></p><p>Troubleshooting any error in the test case is time-consuming.</p></td><td><p>Helps to enhance the existing test case flow just by adding new identifiers. </p><p></p><p>Troubleshooting any error is easier since each row is a separate test case in a flow. </p></td></tr><tr><td>Flow control testing </td><td>A limitation of the V1 format, as it is only based on the skill key and intent key. </td><td>Allows complete test coverage of the flow control statements as it offers a combination of both intent and response node matching. </td></tr></tbody></table>

## File format

The regression test file must be in CSV format. The following are the details of the format:

<table><thead><tr><th width="191" align="center">ID</th><th width="163">QUERY</th><th width="205">TYPE</th><th align="center">EXPECTED_VALUE</th></tr></thead><tbody><tr><td align="center">&#x3C;&#x3C;unique_id-&#x3C;&#x3C;sequence_id>></td><td>&#x3C;&#x3C;test Query>></td><td>&#x3C;&#x3C;response_source>></td><td align="center">&#x3C;&#x3C;skill_key>>.&#x3C;&#x3C;intent_key>></td></tr></tbody></table>

* **ID:**  Unique identifier of each test case. The identifier must be in the format - `<<unique_id>>-<<sequence_id>>,` for all cases except when the conversation is not multi-turn. Although, it is recommended to provide the full format, in such cases, only a unique identifier is sufficient. For example, If you wish to test Smalltalk or Q\&A response, then the ID can be "PizzaFAQ"  instead of "PizzaFAQ-1".  Each row of the CSV file is a test case to execute.&#x20;
  * `unique_id` can be any user-defined value.&#x20;
  * `sequence_id` must be numbers such as 1,2,3.&#x20;
  * `unique_id` and `sequence_id` must be separated by a hyphen.
  * A multi-turn conversation flow is grouped by `unique_id` and executed in the sequence as mentioned by `sequence_id`. In simple terms, a group of rows with the same `unique_id` represents a flow to be executed according to the sequence in the `sequence_id`.&#x20;
  * See [Dialog skill](#dialog-skill), for more an example and more information.
* **QUERY:** The user query to be executed.
* **TYPE:** Indicates the response source that specifies where the user query is executed. For example, if the user query must match an intent or a response node in the Dialog skill. See [Type - Response source](#type-response-source), for more information and supported values.
* **EXPECTED\_VALUE:** Indicates the skill and intent key where the user query execution is expected to match.

{% hint style="info" %}
**Note**: The column headers are in capital case separated by an underscore.&#x20;
{% endhint %}

## Type - Response source

You can specify the following response types in the regression test file:

<table><thead><tr><th width="197.33333333333331">TYPE</th><th width="190">EXPECTED_VALUE</th><th>Description</th></tr></thead><tbody><tr><td><code>intent</code> </td><td><code>&#x3C;&#x3C;skill_key>>.&#x3C;&#x3C;intent_key>></code></td><td><p>Response source is an intent in the Dialog skill, Q&#x26;A, or Smalltalk. This is to test the query against a respective skill intent match. </p><p></p><p>See <a href="#dialog-skill-intent-match">Dialog skill - intent match</a>, for an example. </p><p></p><p>See <a href="#dialog-skill-response-node-match">Q&#x26;A</a>, for an example. </p></td></tr><tr><td><code>response_node</code> </td><td><code>&#x3C;&#x3C;skill_key>>.&#x3C;&#x3C;intent_key>></code></td><td><p>Response source is a response node in the Dialog skill designer. This is to test the query against a Dialog skill response node match. Useful when,</p><ul><li>The same intent match has different responses from different nodes based on the use case. </li><li>Test flow control scenarios such as Goto_node. </li></ul><p></p><p>See <a href="#dialog-skill-response-node-match">Dialog skill - response node match</a>, for an example. </p></td></tr><tr><td><code>intent</code></td><td><code>agent_request</code> </td><td><p>Test if the query triggers a live agent. </p><p></p><p>See <a href="#live-agent">Live agent</a>, for an example.</p></td></tr><tr><td><code>intent</code></td><td><code>agent_transfer</code></td><td><p>Expected value is <code>agent_transfer</code> when the live agent is triggered and transferred using <code>#talk to agent</code> command.</p><p></p><p>See <a href="#live-agent">Live agent</a>, for an example.</p></td></tr><tr><td><code>intent</code></td><td><code>agent_terminate</code></td><td><p>Expected value is <code>agent_terminate</code> when the live agent is terminated using <code>#end agent</code> command.</p><p></p><p>See <a href="#live-agent">Live agent</a>, for an example.</p></td></tr><tr><td><code>intent</code></td><td><code>unhandled</code></td><td><p>The agent must not give a valid response to this query. It must be an unhandled response. </p><p></p><p>See <a href="#unhandled">Unhandled</a>, for an example.</p></td></tr><tr><td><code>intent</code></td><td><code>smalltalk</code></td><td>Test if the agent replies with a system Smalltalk response.</td></tr><tr><td><code>disambiguation</code> </td><td><code>disambiguation</code></td><td><p>Test if the agent replies with the disambiguation response for the given intent. </p><p></p><p>See <a href="#disambiguation">Disambiguation</a>, for an example.</p></td></tr><tr><td><code>disambiguation</code> </td><td><code>&#x3C;&#x3C;skill_key>>.&#x3C;&#x3C;intent_key>>|&#x3C;&#x3C;skill_key>>.&#x3C;&#x3C;intent_key>></code></td><td>Test if the agent responds with the disambiguation options specified in the pipe-separated list. See <a href="#understanding-results">Result</a>, for more information on understanding how the disambiguation results are evaluated.</td></tr></tbody></table>

{% hint style="info" %}
**Notes**: Ensure that there is no space before or after any separators such as "I" in the regression test file.
{% endhint %}

{% hint style="success" %}
**Key points**: To get the skill key and the intent key,&#x20;

* In the desired conversational flow, post the query you wish to test in the agent chat widget at the bottom-right corner.&#x20;
* Click the eye icon to view the message insights.&#x20;
* From the message insights, you can get the skill key and the intent key. Use this to specify the expected intent match in the Regression test file:

<img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mg4cHwa3n5WPZduAtq-%2F-Mg508gMHo6a4KuM2h-5%2F5.7-regression-testing-insights.png?alt=media&#x26;token=a4e9f3b7-1e2c-42c1-889c-7487ccc3229b" alt="" data-size="original">&#x20;

* &#x20;It is not required to specify system intents such as "None of these", "#end agent" when you are testing a flow. You can omit such system intents during testing.
  {% endhint %}

## Use case

Consider the following conversation flow in the Order Pizza skill with the skill key as "macpizza\_order".

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F3PjiQPu75WwWasT7wWyT%2F6.4-regression-testing-order-skill-example.png?alt=media&#x26;token=11c2d70e-74eb-47a1-8e40-ad63ddad2fc3" alt=""><figcaption></figcaption></figure>

The following is an example of different response types in the regression test file:

<table><thead><tr><th width="241">ID</th><th width="136">QUERY</th><th width="158">TYPE</th><th>EXPECTED VALUE</th></tr></thead><tbody><tr><td>OrderPizza-1</td><td>I want to order pizza</td><td>intent</td><td>macpizza_order.1</td></tr><tr><td>OrderPizza-2</td><td>veg</td><td>intent</td><td>macpizza_order.2</td></tr><tr><td>OrderPizza-3</td><td>cheese</td><td>intent</td><td>macpizza_order.4</td></tr><tr><td>OrderPizzaStarter-1</td><td>I want to order pizza</td><td>intent</td><td>macpizza_order.1</td></tr><tr><td>OrderPizzaStarter-2</td><td>veg</td><td>intent</td><td>macpizza_order.2</td></tr><tr><td>OrderPizzaStarter-3</td><td>cheese</td><td>response_node</td><td>macpizza_order.starters</td></tr><tr><td>PizzaLiveAgent</td><td>I want to talk to an agent</td><td>intent</td><td>agent_request</td></tr><tr><td>StoreFAQ</td><td>where is your store?</td><td>intent</td><td>mac_pizza_faqs.store_faqs</td></tr><tr><td>Unhandled</td><td>do you use organic ingredients?</td><td>intent</td><td>unhandled</td></tr><tr><td>OrderFAQDisambiguation</td><td>order</td><td>disambiguation</td><td>macpizza_order.1|mac_pizza_faqs.order_faq</td></tr><tr><td>Disambiguation</td><td>order</td><td>disambiguation</td><td>disambiguation</td></tr></tbody></table>

### Dialog skill - intent match

The pizza placing order flow in the above diagram can be tested as follows:

<table><thead><tr><th width="161">ID</th><th width="205">QUERY</th><th width="88">TYPE</th><th width="318">EXPECTED_VALUE</th></tr></thead><tbody><tr><td>OrderPizza-1</td><td>I want to order pizza</td><td>intent</td><td>macpizza_order.1</td></tr><tr><td>OrderPizza-2</td><td>veg</td><td>intent</td><td>macpizza_order.2</td></tr><tr><td>OrderPizza-3</td><td>cheese</td><td>intent</td><td>macpizza_order.4</td></tr></tbody></table>

{% hint style="info" %}
**Note**: Since all the unique identifiers are the same, they are grouped and executed in the following order `OrderPizza-1 -> OrderPizza-2 -> OrderPizza-3` based on the sequence identifier.
{% endhint %}

### Dialog skill - response node match

Consider the following conversation flow in the Order Pizza skill with the skill key as "macpizza\_order".

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F3PjiQPu75WwWasT7wWyT%2F6.4-regression-testing-order-skill-example.png?alt=media&#x26;token=11c2d70e-74eb-47a1-8e40-ad63ddad2fc3" alt=""><figcaption></figcaption></figure>

The pizza placing order flow in the above diagram can be tested as follows:

<table><thead><tr><th width="211">ID</th><th width="139">QUERY</th><th width="150">TYPE</th><th>EXPECTED_VALUE</th></tr></thead><tbody><tr><td>OrderPizzaStarter-1</td><td>I want to order pizza</td><td>intent</td><td>macpizza_order.1</td></tr><tr><td>OrderPizzaStarter-2</td><td>veg</td><td>intent</td><td>macpizza_order.2</td></tr><tr><td>OrderPizzaStarter-3</td><td>cheese</td><td>response_node</td><td>macpizza_order.starters</td></tr></tbody></table>

{% hint style="info" %}
**Notes:**&#x20;

* Since all the unique identifiers are the same, they are grouped and executed in the following order `OrderPizzaStarter-1 -> OrderPizzaStarter-2 -> OrderPizzaStarter-3` based on the sequence identifier.
* Node 4 has a flow control statement and the response is from the `starters` node. `OrderPizzaStarter-3` test case is to evaluate the response from the flow control statement.
  {% endhint %}

### Live agent

Consider that in the MacPizza agent, you have enabled live agent interaction. See [Switch to live agent](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/switch-to-live-agent), for more information. You can test the transfer to the live agent using the following regression test case:

<table><thead><tr><th width="169">ID</th><th width="225">QUERY</th><th width="149">TYPE</th><th>EXPECTED_VALUE</th></tr></thead><tbody><tr><td>PizzaLiveAgent</td><td>I want to talk to an agent</td><td>intent</td><td>agent_request</td></tr><tr><td>TalktoAgent</td><td>#transfer to agent</td><td>intent</td><td>agent_transfer</td></tr><tr><td>TerminateAgent</td><td>#end agent</td><td>intent</td><td>agent_terminate</td></tr></tbody></table>

### Q\&A

Consider the following Q\&A skill:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mb5VnymYt7rBdi8JKHI%2F-Mb5XR7h0ngmveWbG3hA%2F5.7-regression-test-qa.png?alt=media\&token=9e5d70be-ec3b-48e4-8301-ab56a37f1cda)

You can test the Q\&A skill using the following regression test case:

<table><thead><tr><th width="150">ID</th><th width="225">QUERY</th><th width="90">TYPE</th><th>EXPECTED_VALUE</th></tr></thead><tbody><tr><td>StoreFAQ</td><td>where is your store?</td><td>intent</td><td>mac_pizza_faqs.store_faqs</td></tr></tbody></table>

### Unhandled

Consider that in the MacPizza agent, the query "*do you use organic ingredients?*", goes to an unhandled query. You can test the unhandled case using the following regression test case:

You can test the Q\&A skill using the following regression test case:

<table><thead><tr><th width="134">ID</th><th width="225">QUERY</th><th width="102">TYPE</th><th>EXPECTED_VALUE</th></tr></thead><tbody><tr><td>Unhandled</td><td>do you use organic ingredients?</td><td>intent</td><td>unhandled</td></tr></tbody></table>

### Disambiguation

Consider that in the MacPizza agent, the query "order", goes to disambiguation with options from a dialog skill "Order pizza" and from a Dynamic Q\&A skill "MacPizza FAQs". You can test the disambiguation case using the following regression test case:

You can test the Q\&A skill using the following regression test case:

<table><thead><tr><th width="262">ID</th><th width="92">QUERY</th><th width="167">TYPE</th><th>EXPECTED_VALUE</th></tr></thead><tbody><tr><td>Disambiguation</td><td>order</td><td>disambiguation</td><td>disambiguation</td></tr><tr><td>OrderDisambiguation</td><td>order</td><td>disambiguation</td><td>macpizza_order.1</td></tr><tr><td>OrderFAQDisambiguation</td><td>order</td><td>disambiguation</td><td>macpizza_order.1|mac_pizza_faqs.order_faq</td></tr></tbody></table>

Test if the agent responds with the disambiguation options specified in the pipe-separated list. See [Result](#understanding-results), for more information on understanding how the disambiguation results are evaluated.

### Card responses

If you have card responses in your agent, then you specify the card response in the regression file using the following format:

```javascript
{
  "card_response": {
    "<<field_id>>": "<<value>>"
  }
}
```

* **field\_id**: Identifier of the form element in the card. See [Add form elements](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/add-form-elements), for more information
* **value**: Value of the form element. This can be a simple string or can be an array of values based on the form element.&#x20;

Example 1 (for form elements with an array of values: Checklist): Consider the following Card response in a Dialog skill node:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MV0zw_yGggmiVECZCfM%2F-MV16kOm-zLVQJMush05%2Fregression-testing-card-response.png?alt=media\&token=3d8ddc3c-2acc-49e7-b93c-0f9edd11249d)

You can specify the "Expected value" in the regression test file as follows:

```javascript
{
  "card_response": {
    "d61ac4": [
      "India",
      "United States",
      "Pakistan",
      "Bangladesh"
    ]
  }
}
```

Example 2 (for a simple string input such as single-line element, multi-line element, date, number, rating, poll, and picklist): The following is an example of a single-line element card response that can be used in the regression file:&#x20;

```javascript
{
  "card_response": {
    "ea6432": "This is single line input"
  }
}
```

## **Understanding results**

For each row,  in addition to ID, QUERY, and TYPE, the following columns are displayed in the results CSV:

* EXPECTED\_VALUE: Indicates the expected value to be matched during the regression test run.
* MATCHED\_VALUE: Indicates the actual value that matched during the regression test run.
* RESULT: If the Expected value and Matched value are the same, the result is PASSED, else it is marked as FAILED. In a flow, if one row fails execution, then the subsequent rows in the flow are skipped from execution. Such cases are marked as SKIPPED.
* INSIGHTS:  Insights on how the query was analyzed are available in JSON format. You can use this for further analysis and debugging. See [context.insights](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context/insights), for more information.
