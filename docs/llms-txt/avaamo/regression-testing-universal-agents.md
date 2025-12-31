# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing-universal-agents.md

# Regression testing - Universal agents

{% hint style="info" %}
**Note**: See [Universal agent](https://docs.avaamo.com/user-guide/how-to/build-agents/create-universal-agent), for more information on what a Universal agent is and how to use it.&#x20;
{% endhint %}

You can test Universal agents using Regression testing. Regression testing in Universal agents allows you to test queries with its member agents.

The process of running the regression testing and viewing the status and its results remains the same as with the independent agents. See [Regression testing](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing), for more information.&#x20;

The only difference between the Regression testing in the independent agents and the Regression testing in the Universal agents is the Regression testing file format. A sample Regression testing file format can be downloaded in the **Upload test file** pop-up window. You can use this as a reference to build the test cases that you wish to execute in the Universal agents.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FHy605JRIRl7HfKbdQNcc%2Funiversal-agent-regression-testing-sample-file.png?alt=media\&token=ddb1ee77-ba07-443f-8f08-efd813965a75)

{% hint style="info" %}
**Notes**:&#x20;

* Currently, Universal agents are supported only in the English language. Hence, you can execute regression testing of Universal agents only in the English language.&#x20;
* Regression testing for [disabled](https://docs.avaamo.com/user-guide/how-to/create-universal-agent/manage-member-agents#disable-member-agent) or[ invalid credentials](https://docs.avaamo.com/user-guide/how-to/configure-agents/deploy/universal-agent#regenerate-credentials) or [deleted member agent](https://docs.avaamo.com/user-guide/how-to/create-universal-agent/manage-member-agents#delete-member-agent) fails and returns false.&#x20;
  {% endhint %}

### Regression testing file format

Your regression test file must be in CSV format. Each row of the CSV file is a test case to execute. The following are the details of the format:

|  Column 1 |  Column 2  |
| :-------: | :--------: |
| <\<Flow>> | <\<Query>> |

* **Flow**: Indicates the expected flow in which the user query is tested. This can be a comma-separated list of the expected flow sequence if you wish to test a multi-turn conversation.
* **Query**: Indicates sample query. In case you wish to test a multi-turn conversation, then you can add responses of each node in an additional column.

You can specify the following response types can be specified in the regression test file:

<table><thead><tr><th>Response source</th><th>Format</th><th width="360.3333333333333">Description</th></tr></thead><tbody><tr><td>A response from the member agent</td><td><code>&#x3C;&#x3C;member_key>></code></td><td><p>Test the query against a Member agent intent match. </p><p></p><p>You can get the member_key in the Agent -> Member agent page. See <a href="../../create-universal-agent/add-member-agents#add-member-agent-to-the-universal-agent">Add member agent</a>, for more information. </p><p></p><p>See <a href="#member-agent">Member agent</a>, for an example.</p></td></tr><tr><td>Unhandled</td><td><code>unhandled</code></td><td><p>The agent must not give a valid response to this query. It must be an unhandled response.  This is similar to testing an unhandled scenario with independent agents.</p><p></p><p>See <a href="../regression-testing/regression-test-file-format#unhandled">Unhandled</a>, for an example.</p></td></tr><tr><td>Disambiguation</td><td><code>disambiguation</code></td><td><p>Test if the agent replies with the disambiguation response for the given intent. </p><p></p><p>See <a href="#disambiguation">Disambiguation</a>, for an example.</p></td></tr><tr><td></td><td><code>disambiguation:&#x3C;&#x3C;member_key>>|&#x3C;&#x3C;member_key>></code></td><td><p>Test if the agent responds with the disambiguation options specified in the pipe-separated list. </p><p></p><p>See <a href="../regression-testing#result">Result</a>, for more information on understanding how the disambiguation results are evaluated.</p></td></tr><tr><td>Built-in Smalltalk</td><td><code>smalltalk</code></td><td>Test if the agent replies with a system Smalltalk response. This is similar to testing an unhandled scenario with independent agents.</td></tr></tbody></table>

{% hint style="info" %}
**Notes**:&#x20;

* Currently, the regression testing format in Universal agents has only information about which member agent to execute. Within the member agents, the further path of execution is not available in the test file. Hence, partial path execution (for example: 1.3,1.5) which can be performed with normal agents cannot be executed in Universal agent regression testing.&#x20;
* Ensure that there is no space before or after any separators such as comma or "I" in the regression test file.
  {% endhint %}

### Example: Scenario

Consider the following Universal agent example Acme Enterprise with three member agents - Acme Finance, Acme HR, and Acme IT.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F6ATCIXZ6jVWaQXwQJ35x%2Fmember-agents.png?alt=media\&token=889a1edc-3939-4bd3-b6ed-3e2a030d013f)

### Member agent

Consider the following sample user conversation flow:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FVwa4QhlJp7N3v4KsgRUj%2FScreenshot%202022-04-22%20at%204.39.49%20PM.png?alt=media\&token=9018a916-666c-4c9a-b023-8f9e237a4527)

You can test the same flow in the Regression testing using the following format:

<table><thead><tr><th width="200.47978436657684" align="center">Column 1</th><th width="159" align="center">Column 2</th><th align="center">Column 3</th><th align="center">Column 4</th></tr></thead><tbody><tr><td align="center">1,acme_hr,acme_it,acme_finance</td><td align="center">When is the bonus paid this year?</td><td align="center">Oh my official email Id is not configured yet. Can you help me?</td><td align="center">Okay, also, need to declare the income tax for this year. Can you help me?</td></tr></tbody></table>

### Disambiguation

Consider the following sample user conversation flow that results in disambiguation:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FhHU05NkYp2uf9diTfEXw%2Fua-disambiguation.png?alt=media\&token=d975fd61-6269-4031-b92f-a6348ef2e692)

You can test the same flow in the Regression testing using the following format:

|                 Column 1                 |    Column 2    |
| :--------------------------------------: | :------------: |
| 1,disambiguation:acme\_hr\|acme\_finance | update details |
