# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/learning-continuous-improvement/query-analyzer-deprecated.md

# Query analyzer (Deprecated)

An agent receives and responds to voluminous amounts of queries. These agent responses are pre-defined with intents and entities in your agent and your agent is trained to respond to the user queries.&#x20;

However, a few queries go unhandled as the agent cannot map them to the predefined intents. By default, for all the user queries that do not get matched to any predefined intents in the agent, the agent has a node within the flow to respond to the user's query with statements like -

*"I am sorry I do not understand."*\
*"I am sorry. I don't have an answer for that."*

These classify as unhandled queries as ideally, the user query goes unanswered.

In certain other cases, when a user's intent does not match a specific intent, the agent responds with a selection of closest intent options, referred to as a disambiguation intent.

In a few others, the agent might respond to the user query but not with the expected results.&#x20;

Overall, in order to improve the accuracy and experience with the agent, it is critical to analyze all these queries and continually improve the agent training data.&#x20;

## What is QA?

The Query Analyzer tool can go through all of the end-user queries and provide suggestions to improve the training data of the agent. The purpose of QA is to:

1. Find out the queries that can be used to train existing intents
2. Find out the queries that can be used to create new skills or intents
3. Find out the words or phrases which can be used to improve entity values&#x20;
4. Find out the words or phrases which can be used to create new entity types

## Why is QA required?

As the agent grows in volume, it is very difficult to analyze the user queries manually and understand why these user queries went unhandled or disambiguation. This effort is tremendous and time-consuming.

QA helps us to accelerate, learn and improve the agent training data by not only analyzing all the queries but also suggesting the required changes in the agent to further improve the accuracy of the agent.

## When to run QA?

It is recommended to run QA in the following scenarios:

1. After Go-live or in the Staging and Production environments.
2. It is recommended that you wait for a good round of testing to complete before running QA.
3. After an agent is in production, it is recommended to wait for at least a week and then run QA.
4. It is not recommended to run QA in Development and Testing environment.

## Enabling QA

Contact Avaamo Support to enable QA for your agent.

## Running QA

{% hint style="info" %}
**Note**: Anyone with at-least view permission on the agent can submit a QA job. See [Permissions](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/permissions), for more information. This is useful in production agents, as typically only read-only permissions are provided to the business users. It helps them to run the QA job to analyze the queries and further improvise the user experience with the agent.&#x20;
{% endhint %}

You can run QA from the **Agent ->** **Learning -> Query analyzer** page.

* Navigate to the **Agents** tab on the top menu.
* Search and click any agent for which you wish to view user feedback. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents#search-agents), for more information.
* In the **Agent's** page, click **Learning -> Query analyzer** and select the following parameters:
  * Start date: Select or specify the start date in dd/mm/yyyy format. By default, the Start date is one month before the current date. The Start date can be upto 6 months before the end date.
  * End date: Select or specify the start date in dd/mm/yyyy format. By default, this is the current date.
  * Types of queries to analyze: Select the types of queries you wish to analyze. By default, Unhandled and Pre-Unhandled are selected.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FY0Pvko6X9myPOwVdyQVq%2FQA-submit-job.png?alt=media\&token=7cef4780-add9-4f1b-a624-426fb627cc40)

* Click **Submit job**. A background job is submitted that run all the selected type of user queries in the specified date range. Note that based on the volume of data, the background job may take upto a few minutes to display the results.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FzmNKLiD0UxPKgCqG19eh%2FScreenshot%202023-03-16%20at%204.55.47%20PM.png?alt=media&#x26;token=09741383-40ec-4c1f-954f-3379c824b037" alt=""><figcaption></figcaption></figure>

* As the job progress, you can view the status in the **Job Pipeline**.
* Click **Cancel Job**, if you wish to cancel the submitted job.
* When the job is completed, the results analyzed are displayed in the respective sections. See [Understanding results](#understanding-results), for more information.

### Understanding results

After the job is completed, the results are displayed in the respective sections. You can learn these results and analyze further on how to further improve your agents.

* Click **Re-run Job** if you wish to perform a fresh run of the QA job.
* Click **Export Job** if you wish to export all the job results into a CSV file. You can also click **Export** from the specific sections. This export the queries and the intent types in a CSV format.&#x20;
* Intent types are classified as follows:
  * **Junk**: Queries that are recognized by the system as not holding any intent/entity. A few examples are listed below:&#x20;
    * Gibberish queries
    * One word or less than 5 chars
    * Command queries, eg reset, #clear
    * Only numbers, no words query
    * When language is not detected as English: If translation or language pack is enabled, then the translated queries are also used. If the translated query is not available but a different language is detected, then it is not used and is classified as Junk.&#x20;
  * **Unclassified**: Queries that do not fall under any existing intent, and are not asked frequently enough to have a new intent.&#x20;
  * **Handled**: Queries that match existing intents if asked again.&#x20;
  * **Duplicate**: If the same query occurs repeatedly, one utterance is maintained for the pipeline and the rest are marked as duplicates.&#x20;
  * **Smalltalk**: Casual conversation such as Greetings and wishes.

### Summary

In the **Summary** tab, the following details are displayed:

* Analyzed Date Range: Indicates the date range for which the current QA job was run.
* Last run of job: Indicates the date of the last QA job.
* Total queries analyzed: Indicates the total number of user queries analyzed by the QA job for the selected date range.
* Queries classified in Existing Intents: Indicates the list of queries where you can enhance training data for existing dialog and QnA intents from unhandled queries
* Matched Queries: Indicates a list of all other queries that are Handled.&#x20;
* Queries Classified in New Intents: Indicates the list of queries for which you can create new intents to improve accuracy.
* Other Queries: Indicates a list of all other queries that are Junk, Unclassified, Duplicate, or Smalltalk.&#x20;
* Click **Export** in each block to export the queries and the intent types in a CSV format. You can use this to further analyze and check if training data can be further improvised.

### Existing intents

In the **Existing intents** tab, you can view a list of queries where you can enhance training data for existing dialog and QnA intents from unhandled queries in the existing intents.

You can click on each intent and view the recommended list where the training data can be enhanced.

### New intents

In the **New intents** tab, you can view a list of queries for which you can create new intents to improve accuracy.

You can click on each intent and view the recommended list where new training data can be created.

## Validating and testing

After you make all the required changes in the agent, you can validate the same by running Regression testing for the newly implemented changes in the agent. You can check if such queries still result in unhandled responses or if the accuracy of the agent has improved. See [Regression testing](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing), for more information.
