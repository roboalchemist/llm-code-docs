# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-user-properties.md

# User properties

In certain scenarios, the response for the same user intent in an agent can vary based on certain user properties such as location, manager status, or exempt/non-exempt status. You can configure such user properties of an agent in the **Configuration -> User properties** section. Later, you can use these user properties to create response filters that can be used to filter skill responses for the same user intent in an agent. See [Response filters](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-response-filters), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MEzwbySsWqeAW0MdjBS%2F-MEzxbGAEgXVEcg0koRh%2Fadd-user-properties.gif?alt=media\&token=9ed24692-fbec-4081-8ed0-e17424c46113)

Make a note of the following before you add, edit, or delete user properties in agents.

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can add languages to the agent immediately after creating an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.
* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing.
    {% endhint %}

### Add user properties&#x20;

* In the Agent page, navigate to the **Configuration -> User properties** option in the left navigation menu.
* Click **Add user property** and specify the following details:
  * Enter the name of the user property such as city, country
  * Specify the property key. This is an internal primary key used in the Avaamo Platform for uniquely identifying the property. It is recommended that the key is of at least 3 characters. As you type, the key is automatically converted to Snake Case. See[ Snake Case](https://en.wikipedia.org/wiki/Snake_case), for more information.
* Continue adding multiple user properties as required. Note that the user property name must be unique to an agent.&#x20;

### Edit user properties

* In the Agent page, navigate to the **Configuration -> User properties** option in the left navigation menu.
* Click three ellipse dots in the **Actions** column of the agent to view the extended menu and click **Edit.**
* Update the user property name and click **Update**. If the user property is used in Response filters, then the user property name in all the **Response filters** is also updated.&#x20;

### Delete user properties

* In the Agent page, navigate to the **Configuration -> User properties** option in the left navigation menu.
* Click three ellipse dots in the **Actions** column of the agent to view the extended menu and click **Delete.**

{% hint style="info" %}
**Note**: You can only delete a user property that is not used in any response filters. If a user property is used in any response filter, then a warning message is displayed. You must first remove the user property in all the response filters before deleting the user property.
{% endhint %}

### User properties in Response filters

You can use these user properties to create response filters that can be used to filter skill responses for the same user intent in an agent. See [Response filters](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-response-filters), for more information.

### User properties in Query insights export

By default, in the exported query insights CSV file, all the configured user properties in the agent are also exported. If you have deployed your agent in the C-IVR channel, then you can configure the following properties that can help you get better query insights:

* **user\_phone\_number**: Indicates the phone number used by the user for connecting to the C-IVR channel.
* **agent\_phone**: Indicates the phone number used by the agent assigned for connecting to the C-IVR channel. You can view the agent's phone number in the C-IVR channel settings. See [Conversational IVR](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/conversational-ivr-c-ivr-phone), for more information.
* **call\_sid**: Indicates the unique ID for any incoming or outgoing voice call successfully created in the C-IVR channel.

See [Query insights export](https://docs.avaamo.com/user-guide/how-to/monitor-and-analyze/query-insights#export-query-insights-data), for more information.
