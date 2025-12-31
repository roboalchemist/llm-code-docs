# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-dictionaries.md

# Dictionaries

A dictionary, in the agent, is a collection of words or phrases that holds a specific meaning to your business. The following lists a few use-cases:

* **HR agent:** You are creating an HR agent regarding the employee bonus policies. Here, EB (Employee bonus), QEB (Quarterly Employee Bonus), and such terminologies can be added to the dictionary.
* **SSN agent:** In the United States, a Social Security number (SSN) is a nine-digit number issued to U.S. citizens, permanent residents, and temporary (working) residents. You are creating an agent that helps to apply SSN, change, and get details of an SSN. Here, SSN can be a dictionary word.
* **MLS:** A multiple listing service (MLS) is a marketing database, set up by a group of co-operating real estate brokers to provide accurate and structured data about properties for sale. You are creating an agent that helps to list your property in MLS and update the MLS details. Here, MLS or MLSListing can dictionary words.

These words once added to the agent dictionary are considered differently when understanding user queries. One such consideration is spelling correction. The system does not attempt spelling correction when it encounters these words in user queries. You can also specify alternate values to these dictionary entries. The alternate values are considered equivalent to the original word or phrase. **Example**: Alternate values for "MLS" can be "multiple listing service", "mlslisting".

When you are creating dictionaries, you can also configure dictionaries using these response filters, if required. This is useful when the business terminology varies based on user properties such as location. Example: PTO in US => Vacation. PTO in India => Leave. See [Add response filters](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-response-filters), for more information.

{% hint style="success" %}
**Key Point**: When you create multiple dictionaries, as a best practice, it is recommended to add a dictionary value only in one dictionary. Avoid adding the same dictionary value in multiple dictionaries.
{% endhint %}

### Quick overview

A dictionary in the Avaamo Platform is very similar to the dictionary feature in Microsoft Word.

In MS Word, when you type any word that is not recognized, the word gets highlighted either due to a spelling error or due to the word not being in the MS Word dictionary. You can then choose to correct the spelling error or add the word to the MS Word dictionary.

Similar to the way you add words not recognized by MS word to the MS Word dictionary, you can also add words or phrases that hold specific meaning to your business to the Avaamo Platform dictionary.

### Create a new dictionary

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M4wbC1zCjTVZbX7Wiuw%2F-M4wbGf7jcoyJHzS0MX3%2Fagent-dic.gif?alt=media\&token=16c0b9c3-9016-4285-9764-93ed80e40b95)

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).

* You can add languages to the agent immediately after creating an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.

* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing.
    {% endhint %}

* In the **Agent** page, navigate to the **Configure -> Dictionaries** option in the left navigation menu.

* In the **Create new dictionary** pop-up, specify the name, description, and select the response filter (if any). Click **Create**.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MFTiQ18mRrgKKJZ-6Gr%2F-MFTkFcKeLN9s2HhWsni%2Fconfig-add-dictionary.png?alt=media\&token=8fddf263-169f-45bd-b162-3eb43da01271)

* In the **Dictionaries** page, enter the word and click **Add.** For each word, enter the alternate value in the **Alternate value** text box and click **Add**, if required.

You can also export, import, edit, and delete words, as required from this page similar to entity values. See [Manage entity values](https://docs.avaamo.com/user-guide/how-to/build-agents/add-entity-types-to-agent/manage-entity-types), for more information.

{% hint style="success" %}
**Key point**: You can also right-click and open the dictionaries in a new browser tab or window. This reduces the number of clicks and helps you to work with your skills parallelly as you view or modify the dictionary values.&#x20;
{% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M88uF46_NmooNkh_d-8%2F-M89B3KoshEX1RdWFCU_%2Fwhatsnew-dictionaries.png?alt=media\&token=9b394a3e-0710-4f85-8962-ef5eba2b41d9)

### Examples

* Consider the following skills in an agent - Update MLS Listing and SSN FAQ.
* Invocation intent in Update MLS Listing:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M4wbC1zCjTVZbX7Wiuw%2F-M4wbTIjrtcyKjeuacKZ%2Fagent-dic-mls.png?alt=media\&token=9944ef3d-e6fe-471a-aa81-fbe8f56da090)

* Q\&A in SSN FAQ:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M4wbC1zCjTVZbX7Wiuw%2F-M4wbaT_9Tw_BHk68ULD%2Fagent-dic-ssn.png?alt=media\&token=4ab48f08-d8fa-4d26-bbfb-7406e00f3cf1)

* **User Query**: *What is SSN?, What is social security number?*

| Without Dictionary                                                                                                                                                                    | With Dictionary                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fv5%2F-M4wbC1zCjTVZbX7Wiuw%2F-M4wcKRQkvh6L_HXrCVQ%2F4.png?generation=1586933881614926\&alt=media) | ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fv5%2F-M4wbC1zCjTVZbX7Wiuw%2F-M4wcKRRSo4GddgVJcGa%2F5.png?generation=1586933881699808\&alt=media) |

* **User Query**: *I want to update details of my mls, I want to update details of my mlslisting*

| Without Dictionary                                                                                                                                                                    | With Dictionary                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fv5%2F-M4wbC1zCjTVZbX7Wiuw%2F-M4wcKRSU--JeeJctLbk%2F6.png?generation=1586933881597284\&alt=media) | ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fv5%2F-M4wbC1zCjTVZbX7Wiuw%2F-M4wcKRTPwMAu8upkQ8A%2F7.png?generation=1586933881615167\&alt=media) |
