# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a/debug-dynamic-q-and-a-skill.md

# Debug Dynamic Q\&A skill

In case you are unable to receive the expected response from the **Dynamic Q\&A** skill, you can debug using the following troubleshooting tips:

### **Using local skill testing**

* Use the **Test** in the Dynamic Q\&A page to test the skill locally. See [Test Dynamic Q\&A](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a/test-dynamic-q-and-a-skill), for more information. If you are not receiving the appropriate responses, then check the user query and edit the user intents, if required. See [Edit skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/build-and-manage-dynamic-q-and-a-skill/perform-common-actions#edit-skill), for more information.
* If you are receiving appropriate responses, then test the skill at the agent level. [Use insights](#using-insights) in the agent testing for further debugging.

### **Using Insights**

* Click the **eye icon** below the user query to know the intent mapped to the query.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FHqqmK3fkPEJarX9cjgnY%2Fimage.png?alt=media\&token=599e98c1-bb1f-4d47-ac6a-21ddf12bb7aa)

* In the **Insights** pop-up, you can know if the query is mapped to the required intent type, intent name, skill name, response node, and the language of the query.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FKGET5gMKEOGdYBN9obaH%2Fimage.png?alt=media\&token=bf3858b1-8fee-41fc-9b62-fd40fdd95d08)&#x20;

* Add the query that is not handled \[mapped to unhandled intent] by the agent as inline training data. See [Add Questions and Answers,](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a/build-and-manage-dynamic-q-and-a-skill/add-questions-and-answers) for more information.

### Using Conversation history

You can also check the user query from the [Conversation history](https://docs.avaamo.com/user-guide/build-agents/debug-agents#conversation-history) to know the query for which the expected response is not displayed in the agent.&#x20;

### Using Debug Logs

In case you are receiving a JS error in the Dynamic Q\&A response, check [Debug Log](https://docs.avaamo.com/user-guide/build-agents/debug-agents#debug-log) for more details.
