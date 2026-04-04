# Source: https://docs.avaamo.com/user-guide/llamb/get-started/step-3-test-your-agent.md

# Step 3: Test your agent

If you are starting to explore LLaMB for the first time, then the best way to test a sample query is using the [Agent Simulator](#using-agent-simulator).&#x20;

As you iteratively build the agent with LLaMB, you can further use the [UAT option in the Web channel](#using-uat-option-in-web-channel) to perform more comprehensive testing.&#x20;

{% hint style="success" %}
**Key points**:&#x20;

* `Mercury` theme is the recommended theme for LLaMB. See [Mercury theme](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/theme), for more information.
* You can test LLaMB content through Regression Testing. Refer [Regression Testing](https://docs.avaamo.com/user-guide/llamb/regression-testing), for more details.
* User inputs and agent responses can be in multiple languages. However, Documents can only be ingested in **en-US**.
  {% endhint %}

### Using Agent Simulator

* On the Agent page, navigate to the`Test -> Simulator` option in the left navigation menu. Alternatively, you can test using the agent icon in the bottom right corner.
* You can now ask queries and test if you receive appropriate responses from user queries.&#x20;

<div align="left"><figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fv6uMzwuYtJA5ZxgsD3M5%2Fimage.png?alt=media&#x26;token=c7b06149-c80a-4848-8740-28e151fa4725" alt="" width="375"><figcaption></figcaption></figure></div>

* Click on the `source citations` to view the actual source of the agent's response. This allows you to see the details of the `data chunk` used to answer the user's query. Refer [Query context](#query-context) for more information.

### Query context

You can gain deeper visibility into how LLaMB generates responses with the new `Query Context` feature in `Message insights`.&#x20;

This helps you understand how different parts of your data contribute to the response—making it easier to debug, optimize, and trust the results. Some of the key benefits include:

* Enhanced visibility into the chunks used to generate responses
* Chunk-based responses show how queries are matched with relevant data
* Improved debugging with traceable chunk information for better optimization
* Greater transparency into how LLaMB builds and delivers answers

<div align="left"><figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FnbQc0foGKgUzcnhG4ItA%2FScreenshot%202025-03-21%20at%2012.32.37%E2%80%AFPM.png?alt=media&#x26;token=d16a8601-076c-4950-9e70-5b676cf0fdd5" alt="" width="375"><figcaption></figcaption></figure></div>

Click `Query Context` to view all the chunks involved in the response creation.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FzCdkOp41KhhI5WYJ6z9p%2FScreenshot%202025-03-21%20at%2012.43.19%E2%80%AFPM.png?alt=media&#x26;token=8bd1a190-4647-46e5-a9ed-e79bf34b15d7" alt=""><figcaption></figcaption></figure>

You can also view the label `Strong match` which means the chunks that were deemed **most relevant** to the question and contributed **significantly** to generating the answer.

Click any `chunk` to view detailed information.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FmACgjxx8wHJdSjlPe21n%2FScreenshot%2025-03-2025%20at%2013.57%20(1).png?alt=media&#x26;token=598c7714-9034-414e-be87-9cd9252aba1e" alt=""><figcaption></figcaption></figure>

* **Document Name**: The name of the document from which the chunk was derived.
* **Intent Key**: The specific intent used in response generation.
* **URL:** The source of the document, as specified during ingestion.
* **Document Attributes:** Attributes assigned to the document during ingestion.
* **User custom properties:** The custom properties set by the user are displayed here.
* **Descriptions**: Additional contextual information about the chunk.

### Using the UAT option in the Web channel

User Acceptance Testing (UAT) option in the Web channel allows you to set up a pre-defined set of test queries to conduct UAT on the agents before deploying the agent in production.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FGzUmjSJPvsxV9XQBPdKd%2Fimage.png?alt=media&#x26;token=5f033ef0-26f8-4f0a-8846-2b906b6d6c5c" alt=""><figcaption></figcaption></figure>

You can use these queries to quickly test your agent as you iteratively build the agent with LLaMB. User Acceptance Testing is crucial because it acts as a final validation step, ensuring that the agent meets user expectations and is ready for deployment into the production environment.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F5opQda8GFLccEJ70eHma%2Fimage.png?alt=media&#x26;token=ace345fe-eeaa-488f-9059-172d623c4158" alt=""><figcaption></figcaption></figure>

See [UAT](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/uat), for more information.

### Regression testing

Regression testing is a tool for verifying that an agent's responses are accurate and consistent with previous versions. It helps ensure that queries and their corresponding responses remain correct even as the underlying models and AI tools evolve.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fl1gCwkf8H3HhTAPNOqpE%2Fimage%20(5).png?alt=media&#x26;token=df38f644-427d-4b08-b33a-fe5b9fa77bf3" alt=""><figcaption></figcaption></figure>

Refer [Regression Testing](https://docs.avaamo.com/user-guide/llamb/regression-testing), for more details.
