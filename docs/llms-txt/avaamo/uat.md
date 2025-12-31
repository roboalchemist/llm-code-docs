# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/uat.md

# UAT

User acceptance testing (UAT) is a crucial step before deploying your agents to the production environment. It helps to ensure that the agent meets user requirements, functions correctly in a real-world setting, and provides a high level of quality and satisfaction.

Here's a quick demo of the **`UAT`** feature:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FfFQbC65ToynE8dDTZ6UV%2F8.0-UAT.gif?alt=media&#x26;token=2c0b6294-cc89-4a11-a557-ce76be6fb412" alt=""><figcaption></figcaption></figure>

### Why UAT of agents?

Some of the key benefits include:

* **Validation of requirements**: UAT helps to gather user feedback from UAT users before deploying the agent in the live production environment. Hence it helps to validate that the system aligns with the intended functionality outlined in the initial requirements.&#x20;
* **Quality Assurance:** UAT helps to identify defects, bugs, or discrepancies that may have been overlooked during earlier stages of testing. It helps to ensure a higher level of quality before the agent is made available to a wider audience.
* **Cost-effective:** Identifying and fixing issues during the UAT phase is generally more cost-effective than addressing them after the agent has been deployed in the production environment.&#x20;
* **Accelerates agent deployment**: When you iteratively add more functionality to your agent, the UAT queries can serve as a good test bed to perform quick end-to-end testing if the agents before deploying the agents to production.

### Who should use UAT?

UAT feature is exclusively built for user acceptance testers who are subject matter experts and are aware of the agent functionality. Testers can use the UAT feature to set up the required test queries, perform UAT on the agent, and provide required feedback.

Developers can then view the feedback provided during UAT testing from the [Monitor -> Analytics](https://docs.avaamo.com/user-guide/how-to/monitor-and-analyze/analytics#user-feedback) page and also under [Learning -> User Feedback](https://docs.avaamo.com/user-guide/how-to/build-agents/learning-continuous-improvement/feedback) section. Alternatively, developers can also use the [User Feedback API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/feedback-api) to collect feedback periodically to learn and analyze the experience of the user when they are interacting with your agent.

### Before UAT

* Identify the `categories` of the testing areas. Here, a category can be used to classify your UAT queries into different groups, based on functionalities, modules, or use cases. Categories help to maintain the UAT queries effectively.
* Evaluate what must be accomplished at the end of UAT testing for each category. Have a list of UAT queries that closely mimic the production use cases for each category.

{% hint style="info" %}
**Before configuring UAT section in the web channel**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can deploy the agent to a channel after creating and building an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.
* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing the agent.
    {% endhint %}

### Add UAT queries

In the Avaamo Conversational AI Platform, the `UAT` option is available in the Web channel. It allows you to set up a pre-defined set of test queries to conduct UAT on the agents before deploying the agent in production.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FGzUmjSJPvsxV9XQBPdKd%2Fimage.png?alt=media&#x26;token=5f033ef0-26f8-4f0a-8846-2b906b6d6c5c" alt=""><figcaption></figcaption></figure>

**To add UAT test queries**:

* On the `Agent -> Channels` page, click `View` on the Web Channel.
* In the `Channels -> UAT` section, you can add test queries for each category.&#x20;
  * By default, three categories are already available in the UAT page.
  * Click `Add new category` to add a new category of queries.
  * Click the extended menu on the category to edit the category name or delete the category.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FODzqMWKSvKkGWVlDYbJx%2Fimage.png?alt=media&#x26;token=392f7871-3c38-4e90-8d68-c2d748dd3bd4" alt=""><figcaption></figcaption></figure>

* For each category, type the query in the `Type in your query` textbox and click `Add` to add new UAT queries.&#x20;
* Click `Save` to save the UAT categories and queries.

{% hint style="info" %}
**Notes**:

* Currently, there is no limit on the number of categories to add in the UAT page. However, it is recommended to keep the categories close to the number of functionalities or modules that you wish to test.&#x20;
* Currently, there is no limit on the number of queries to add. It is recommended to add at least 50 UAT queries for each category for a thorough evaluation.
* A Category name can be up to 191 characters and must be unique
* The query within the same category must be unique.
  {% endhint %}

### Perform UAT

After configuring the UAT, click the `View` option in the `Channels -> UAT` section to test the queries.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FGzUmjSJPvsxV9XQBPdKd%2Fimage.png?alt=media&#x26;token=5f033ef0-26f8-4f0a-8846-2b906b6d6c5c" alt=""><figcaption></figcaption></figure>

The UAT link is displayed in the new tab. The instructions and categories are displayed on the left side of the page. The agent is displayed towards the right.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F5opQda8GFLccEJ70eHma%2Fimage.png?alt=media&#x26;token=ace345fe-eeaa-488f-9059-172d623c4158" alt=""><figcaption></figcaption></figure>

* Click the `Category` to view the queries corresponding to each category.
* Click the query in the `Category`, the query is displayed in the agent widget, executed in the agent widget and the response corresponding to the query is displayed.&#x20;
* Click the thumbs up and thumbs down option to provide feedback.
* In the thumbs-down option, you can specify more granular details that can help in tuning the agent for a better user experience.&#x20;

If you are using a `Mercury` theme, the feedback collected on the thumbs-down option from the UAT users differs from what is collected from the production users. In the `Mercury` theme, the feedback collected at the UAT stage aims towards collecting more specific details since UAT users are subject matter experts and testers within the account who are more aware of the agent and what is built into it when compared to the production users. See [Mercury theme](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/theme#mercury-theme), for more information.

The following illustration depicts the feedback collected on the thumbs-down option in the `Mercury` theme:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FlRDGC8n6z3foJ5Lm247Q%2Fimage.png?alt=media&#x26;token=c0660609-f3de-4fd2-afb2-042719c68133" alt=""><figcaption></figcaption></figure>

The following illustration depicts the feedback collected on the thumbs-down option in the `Messenger` theme:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FUpTydhVJTcTneGFUAHVT%2Fimage.png?alt=media&#x26;token=879dc43a-e39c-4de0-8aa1-48b686b4c809" alt=""><figcaption></figcaption></figure>

### Reviewing UAT feedback

Developers can view the user feedback from the [Monitor -> Analytics](https://docs.avaamo.com/user-guide/how-to/monitor-and-analyze/analytics#user-feedback) page and also under [Learning -> User Feedback](https://docs.avaamo.com/user-guide/how-to/build-agents/learning-continuous-improvement/feedback) section.&#x20;

The following is an illustration of the `User feedback` section in the [Monitor -> Analytics](https://docs.avaamo.com/user-guide/how-to/monitor-and-analyze/analytics#user-feedback) page:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbL2mIO2DxF7v2-VJ6S%2F-MbL3u_tkYxXauRUuQK2%2F5.7-analytics-user-feedback.png?alt=media&#x26;token=e97bf97d-fd2b-436f-a41b-d813956440a8" alt=""><figcaption></figcaption></figure>

Alternatively, Developers can also use the [User Feedback API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/feedback-api) to collect feedback periodically to learn and analyze the experience of the user when they are interacting with your agent.

### Key points

The following are some of the key points to note in the UAT feature:

* Since the primary audience of this feature is UAT users, message insights for the responses are not displayed in the agent widget.
* UAT queries and responses are available in the Conversation history for further review and debugging is required. See [Conversation history](https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents/conversation-history), for more information.
* UAT link is similar to the link generated when you click `Test` option in the web channel. If the agent is publically accessible, then the UAT link is also publically accessible and can be shared with the UAT users for testing.
* All the Web channel configurations apply for the agent in the UAT environment. For example, if the web channel theme is `Messenger`, then the agent widget in the UAT link uses the `Messenger` theme.&#x20;
