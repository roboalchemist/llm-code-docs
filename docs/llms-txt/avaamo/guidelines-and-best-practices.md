# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing/guidelines-and-best-practices.md

# Regression testing best practices

Users can interact with your agent in different ways. Some user queries are completely correct grammatical sentences, other user queries can be just phrases, or some user queries can be ambiguous. It is important to test if your agent is trained to handle and respond to all such user queries as desired.&#x20;

This article summarizes a **few essential categories** **of queries** that you must consider when you are preparing to perform regression testing on your agent. It is recommended to have sufficient queries in all these categories to ensure that you have tested your agent with real user queries that can be used to interact with your agent.&#x20;

### Overview

One of the practical ways to build regression testing is by learning how users are interacting with the agent using the Conversation history. You can take a dump of 2-3 months of data to understand the way users interact with your agent. See [Conversation history](https://docs.avaamo.com/user-guide/how-to/debug-agents#using-conversation-history), for more information. A good regression test is the one that tests the skill ability to detect all intents it is expected to handle based on the training data and at the same time does not give wrong answers for questions that it is not trained on.&#x20;

If you are writing regression testing for the first time,

* Review all the best practices for creating the regression test cases. See [Regression testing best practices](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing/guidelines-and-best-practices), for more details.
* Download a sample regression file format and build the regression test cases by evaluating all the best practices. See [Regression test file format](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing/regression-test-file-format), for more details.

If you already have regression testing test cases,

* You can download the latest run of regression test input files. See [Download input CSV](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing/..#download-input-csv), for more details.
* Review all the best practices for augmenting your test cases. See [Regression testing best practices](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing/guidelines-and-best-practices), for more details.
* Build the regression test cases by evaluating all the best practices. See [Regression test file format](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing/regression-test-file-format), for more details.

### Use case

For the purpose of understanding, consider a simple example with the following data:

* "Auto Loan" agent&#x20;
* One Dialog skill "Buy Auto Loan" with invocation intent "I want an auto loan".
* Simple greeting message in the skill that says "Sure. I can help with auto loan."

{% hint style="info" %}
**Notes**:&#x20;

* Examples for all the categories are demonstrated using an agent simulator. The same set of queries can be used for regression testing too. See [Regression test file format](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing/regression-test-file-format), to learn more on how to create a CSV file with test cases.
* It is recommended to have at least 5 queries for an intent. **Example**: If there are 100 intents, then it is recommended to have 500 test queries in the regression file. It is a common practice to have more than 5 queries for each intent.
  {% endhint %}

### 1. Modularize test cases

Consider creating test cases with well-defined boundaries based on your agent implementation. A few examples are listed below:

* If your agent is configured in multiple languages, then consider creating a separate regression file for each language.
* Create separate regression file for each skill. For example, for all Dynamic Q\&A skills in the agent, you can create one regression file.&#x20;
* If you have external integrations, then consider creating a separate regression file with external integration. This enables faster execution of the test cases where external integration is not required.
* It is recommened to create regression file with a maximum of 50000 test cases.

### 2. Well-formed queries

These are the user queries that are completely correct grammatical sentences with proper intents. Very few users interact with the agent using well-formed queries. For example, in the "Auto Loan" agent, you can test with these variations that the users can ask:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M9Y-Mxy3HGCm7Tlmw95%2F-M9Y0Yspm2p_gdTIvFh7%2Fregression-test-eg-1.png?alt=media\&token=df8a7b37-e781-47a8-bdeb-3418511a60ad)

Note that these are not the variations the agent is trained with. Here, the Platform recognizes the intent in the user query accurately and an appropriate response is displayed to the user.&#x20;

### 3. Incomplete/short queries

Most of the user queries are incomplete or short queries usually is the form of two or three phrases that are abstract and not clear. For example, in the "Auto Loan" agent, you can test with these variations that the users can ask:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M9Y1WnAsGDBEUtbXOyF%2F-M9Y26lFSqm4w6c8itfB%2Fregression-test-eg-2.png?alt=media\&token=8ba9424b-7549-4cc1-9333-ef877d3c95d1)

Note that even with minimal user query data, since the Platform is able to recognize a part of the intent, a set of options closely matching the intent is displayed.

### 4. Ambiguous queries

These are the user queries that can be either short phrases or can be complete sentences but the intent is not clear. For example, in the "Auto Loan" agent, you can test with these variations that the users can ask:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M9YOmr3TAfPHv8BJWoB%2F-M9YQGzBgQPSOGxLJHTt%2Fregression-test-eg-6.png?alt=media\&token=51128d8e-d84b-4df4-adf5-4544acf9cbf4)

Note that even with ambiguous user queries, since the Platform is able to recognize a part of the intent, a set of options closely matching the intent is displayed.

### 5. Spelling errors

Most of the user queries also can contain spelling errors. For example, in the "Auto Loan" agent, you can test with these variations that the users can ask:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M9YDXJeIts3E9KmnOzO%2F-M9YF3DEuRFcjDiPYcI4%2Fregression-test-eg-3.png?alt=media\&token=4fffbe23-e403-4ac4-a88e-da2dfcd6ba12)

Note that as long as the Platform is able to reasonably determine the accuracy of the intent from the user query, it is not required to train the agent for all such spelling corrections, as these are automatically handled in the agent.

### 6. Long sentences

There are certain user queries that can contain very long sentences in which the intents are not directly implied or the intent gets combined with multiple sentences. For example, in the "Auto Loan" agent, you can test with these variations that the users can ask:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M9YOmr3TAfPHv8BJWoB%2F-M9YPb-elCko5-rYwGoa%2Fregression-test-eg-5.png?alt=media\&token=41002dc7-e510-4ed5-bfff-0568436d45b0)

Note that even with such long sentences, the Platform is able to recognize the intent and an appropriate response is displayed to the user.&#x20;
