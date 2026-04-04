# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-response-filters.md

# Response filters

You can configure response filters based on the user properties such as location, manager status, or exempt/non-exempt status. Later, you can use these response filters to filter skill responses for the same user intent in an agent. **Example**: In an HR agent, consider the user query "When is the year-end bonus paid?". Bonus paid for Indian and US employees can be different. You can define multiple responses for an intent based on the user's properties so that agent’s response is different for an Indian user and a US user. See[ Add user properties](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-user-properties), for more information.

This feature helps in:

* Rapid agent development: You can use the same agent and tailor the responses based on different user properties.
* Providing personalized responses for the same user intent, say, for example, based on the location of the user, or department a user belongs to, or time zone.
* Configuring filtered responses completely in the UI without writing any JS code

See the following topics for more information on how to add the response filters to skill responses:

* [Build Dialog skill responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses)
* [Add questions and answers in Q\&A responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-q-and-a-designer/build-and-manage-q-and-a-skill/add-intents-and-languages)
* [Add questions and answers in Smalltalk responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/build-and-manage-smalltalk-skill/add-smalltalk-qa)

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MF-A1gFx7_gO85XIrcU%2F-MF-Om64GfxMi5sE4zIh%2Fadd-response-filters.gif?alt=media\&token=fdd572db-6d0f-4e9a-8cba-746eb9b5af10)

Make a note of the following before you add, edit, or delete response filters in agents.

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can add languages to the agent immediately after creating an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.
* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing.
    {% endhint %}

## Add response filters &#x20;

You can add two types of response filters: User property and Custom code.&#x20;

* In the Agent page, navigate to the **Configuration -> Response filters** option in the left navigation menu.
* Click **Add filter**. Select one of the following options:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MF-PS4TjwPpFPD93KH2%2F-MF-f6gM2ilJ17lWw4ca%2Fconfig-response-filters.png?alt=media\&token=47771aec-fa5d-42ba-a3c8-03d3c88fd039)

<table><thead><tr><th width="174">Filters</th><th width="592">Description</th></tr></thead><tbody><tr><td>User property</td><td><p>Use this to filter responses based on user properties. See <a href="add-user-properties">Add user properties</a>, for more information. Specify the following details:</p><ul><li>Name of the response filter. </li><li>User property for which you wish to define the response filter. </li><li>Enter values for the selected user property and click <strong>Add</strong>. Each value in the filter is an OR condition; the filter is applied even if one of the values match. Note that you can add upto 50 values to a user property. </li></ul></td></tr><tr><td>Custom code</td><td><p>Use this to filter responses based on any other custom condition that cannot be configured using user property. The custom code specified here acts as a response filter. Specify the following details:</p><ul><li>Name of the response filter.</li><li>Enter the custom JS code for defining your filter. The JS must return true or false or a number. The Response filter is applied if the JS code returns true or a number. If the JS code returns 0, then it is considered false and the response filter is not applied in this case. </li></ul></td></tr></tbody></table>

* Click **Add** to add more conditions to the filter. Each condition in the filter is an AND condition; the filter is applied only when all the conditions match. This option is only available for response filters created using user properties. Note that you can add upto 50 conditions in a response filter.&#x20;

## Edit response filters&#x20;

* In the Agent page, navigate to the **Configuration -> Response filters** option in the left navigation menu.
* Update the name, user properties, and values of the required Response filters. Click **Save**. If the response filter is used in the skill responses, then the response filters in the corresponding skill responses are also updated.&#x20;

## Delete response filters&#x20;

* In the Agent page, navigate to the **Configuration -> Response filters** option in the left navigation menu.
* Click **Delete** to delete the filter. You can also click the **Delete** icon to delete values from the response filters.&#x20;

{% hint style="info" %}
**Note**: You can only delete a response filter that is not used in any skill response. If a response filter is used in any skill response, then a warning message is displayed. You must first remove the response filters in all the skill responses before deleting the response filter.
{% endhint %}

## Frequently asked questions (FAQs)

### 1. When multiple conditions are added in a response filter

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MFnIpAWcvr161ZWVcYG%2F-MFnKwFyEjIvP3nZBWck%2Fresp-filter-faq1.png?alt=media\&token=42c7c549-b701-468f-bab4-970e6e6a1c0a)

Each condition in the filter is an AND condition; the filter is applied only when all the conditions match. This option is only available for response filters created using user properties.

### 2. When multiple responses filters are added to a skill response in the user intent

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MFnIpAWcvr161ZWVcYG%2F-MFnLz-OvAiLxcIuSpNV%2Fresp-filter-faq2.png?alt=media\&token=813ae187-80a9-4dc0-9ce9-8bb17b498f1b)

Each response filter is an AND condition; the response is displayed only when all filters match.

### 3. When multiple responses with response filters match the user intent&#x20;

When you add multiple responses to intent, then the responses are evaluated as follows:

* All those responses with no response filters have a return value of 1.
* The response filter with user property matches has a return value of 1.
* The response filter with JS code matches where JS code returns true and has a return value of 1.&#x20;
* If the response filter with the JS code matches and the JS code returns a number, then the number is considered as the return value.
* Among the set that matches, if all of them have an equal return value, then a random response is displayed, else the one that has the highest return value is displayed to the user.

Consider that you have added the following responses with the response filters for an intent (Dialog, Q\&A, or Smalltalk):&#x20;

* Resp1 -> Response filter based on user property
* Resp2 -> Response filter based on user property
* Resp3 -> Response filter using Custom JS code. Returns 2.
* Resp4 -> Response filter using Custom JS code. Returns true.
* Resp5 -> Response filter using Custom JS code. Returns 2.
* Resp6 -> Response filter using Custom JS code. Returns 3.

The following table summarizes the response displayed to the user. The tick mark indicates that the response filter matched:

<table><thead><tr><th width="150" align="center">Scenario</th><th width="150" align="center">Resp1</th><th width="150" align="center">Resp2</th><th width="150" align="center">Resp3</th><th width="150" align="center">Resp4</th><th align="center">Resp5</th><th width="150" align="center">Resp6</th><th align="center">Result</th></tr></thead><tbody><tr><td align="center">a</td><td align="center">✅</td><td align="center">✅</td><td align="center"></td><td align="center"></td><td align="center"></td><td align="center"></td><td align="center">Random</td></tr><tr><td align="center">b</td><td align="center"></td><td align="center"></td><td align="center">✅</td><td align="center">✅</td><td align="center"></td><td align="center"></td><td align="center">Resp3</td></tr><tr><td align="center">c</td><td align="center"></td><td align="center"></td><td align="center">✅</td><td align="center"></td><td align="center">✅</td><td align="center"></td><td align="center">Random</td></tr><tr><td align="center">d</td><td align="center"></td><td align="center"></td><td align="center"></td><td align="center"></td><td align="center">✅</td><td align="center">✅</td><td align="center">Resp6</td></tr><tr><td align="center">e</td><td align="center"></td><td align="center">✅</td><td align="center">✅</td><td align="center"></td><td align="center"></td><td align="center"></td><td align="center">Resp3</td></tr><tr><td align="center">f</td><td align="center"></td><td align="center">✅</td><td align="center"></td><td align="center">✅</td><td align="center"></td><td align="center"></td><td align="center">Random</td></tr></tbody></table>

### 4. When multiple responses are added to an intent without any response filter

If you add multiple responses for an intent without any response filter, then the system picks a random response from the set of multiple responses and displays it to the user.
