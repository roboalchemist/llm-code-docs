# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing/regression-test-file-format.md

# Source: https://docs.avaamo.com/user-guide/llamb/regression-testing/regression-test-file-format.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing/regression-test-file-format.md

# Source: https://docs.avaamo.com/user-guide/llamb/regression-testing/regression-test-file-format.md

# Regression test file format

A regression test file contains a set of questions, the actual answer to each question, which is the ground truth, and any user properties specific to that answer.&#x20;

{% hint style="success" %}
**Key point:** Collaborate with Subject Matter Experts to build a regression test file in the Discovery phase itself.
{% endhint %}

### File format

The following is a sample regression test input file.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FNRvsxQqNntTrmIFCVTxn%2FScreenshot%202025-04-15%20at%2011.13.40%E2%80%AFAM.png?alt=media&#x26;token=72085f99-9bde-4439-ab64-6ab93d05aefc" alt=""><figcaption></figcaption></figure>

Your regression test file must be in CSV format. Each row of the CSV file is a test case to execute. The following are the details of the format:

<table><thead><tr><th width="141.544677734375">Column 1</th><th width="233.3463134765625"> Column 2</th><th>Column 3</th></tr></thead><tbody><tr><td>QUESTION</td><td>GROUND TRUTH</td><td>USER PROPERTIES</td></tr></tbody></table>

* **Question** – The query or input provided by a user to the agent. Only up to 1000 questions are supported per file.

{% hint style="info" %}
**Note:** You can run a maximum of 1,000 questions per day. Contact Avaamo Support to request a change to the daily limit configuration.
{% endhint %}

* **Ground Truth** – The expected answer for a given query serves as the reference point to evaluate whether the agent’s response is accurate and meaningfully aligned with the query’s intent. This field is optional and is used for comparison to evaluate the accuracy of the agent’s response. If left blank, the system generates the ground truth for all queries after the test is completed.
* **User Properties** – [Attributes](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/document-attributes) or metadata assigned at the user level, which can influence personalization and response generation. This field is optiona&#x6C;**.**&#x20;
