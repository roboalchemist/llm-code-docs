# Source: https://docs.avaamo.com/user-guide/recent-releases/release-notes-v8.0/introducing-uat-in-web-channel.md

# Introducing "UAT" in Web channel

In the `Atlas 8` release, a new feature **`UAT`** has been introduced in the web channels.&#x20;

It allows you to set up a pre-defined set of test queries to perform User acceptance testing (UAT) on the agents before deploying the agent in production. This is a crucial step in the agent's life cycle to ensure that the agent meets user requirements, functions correctly in a real-world setting, and provides a high level of quality and satisfaction.&#x20;

Here's a quick demo of the `UAT` feature:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FfFQbC65ToynE8dDTZ6UV%2F8.0-UAT.gif?alt=media&#x26;token=2c0b6294-cc89-4a11-a557-ce76be6fb412" alt=""><figcaption></figcaption></figure>

### Key benefits

The following are some of the key benefits of performing UAT on agents:

* **Validation of requirements**: UAT helps to gather user feedback from UAT users before deploying the agent in the live production environment. Hence it helps to validate that the system aligns with the intended functionality outlined in the initial requirements.&#x20;
* **Quality Assurance:** UAT helps to identify defects, bugs, or discrepancies that may have been overlooked during earlier stages of testing. It helps to ensure a higher level of quality before the agent is made available to a wider audience.
* **Cost-effective:** Identifying and fixing issues during the UAT phase is generally more cost-effective than addressing them after the agent has been deployed in the production environment.&#x20;
* **Accelerates agent deployment**: When you iteratively add more functionality to your agent, the UAT queries can serve as a good test bed to perform quick end-to-end testing of the agents before deploying the agents to production.
* **Collecting effective feedback**: UAT helps to collect feedback from the testers who are subject matter experts with more experience in mimicking the exact production scenarios and hence is a valuable source of information to further improve your agent.

### Who should use UAT?

UAT feature is exclusively built for user acceptance testers who are subject matter experts and are aware of the agent functionality. Testers can use the UAT feature to set up the required test queries, perform UAT on the agent, and provide required feedback.

Developers can then view the feedback provided during UAT testing from the [Monitor -> Analytics](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/analytics#user-feedback) page and also under the [Learning -> User Feedback](https://docs.avaamo.com/user-guide/how-to/build-agents/learning-continuous-improvement/feedback) section. Alternatively, developers can also use the [User Feedback API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/feedback-api) to collect feedback periodically to learn and analyze the experience of the user when they are interacting with your agent.

### Before UAT

* Identify the `categories` of the testing areas. Here, a category can be used to classify your UAT queries into different groups, based on functionalities, modules, or use cases.
* Evaluate what must be accomplished at the end of UAT testing for each category. Have a list of UAT queries that closely mimic the production use cases for each category.

### How does it work?

In the `Channels -> UAT` section, you can add test queries for each category. Here, a category can be used to classify your UAT queries into different groups, based on the say, functionalities, modules, or use cases. `Categories` helps to ensure complete coverage of your test cases.

After configuring the UAT with categories and test queries, you can test the queries using the `View` option in the `Channels -> UAT` section.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FGzUmjSJPvsxV9XQBPdKd%2Fimage.png?alt=media&#x26;token=5f033ef0-26f8-4f0a-8846-2b906b6d6c5c" alt=""><figcaption></figcaption></figure>

In the UAT testing page, the instructions and categories are displayed on the left side of the page. The agent is displayed towards the right. Click the category and corresponding queries to test in the agent widget.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FosG3aOk1SUb3IArXAOn1%2Fimage.png?alt=media&#x26;token=d05dc4c2-cf1f-4346-afc4-83bcd245a8d9" alt=""><figcaption></figcaption></figure>

See [UAT](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/uat), for more information.
