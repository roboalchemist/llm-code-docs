# Source: https://docs.avaamo.com/user-guide/llamb/regression-testing/understanding-results.md

# Understanding results

You can download the test results once the test is completed. See [Download Results](https://docs.avaamo.com/user-guide/llamb/run-regression-test#download-results), for more information. The following is a sample regression test input file.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FVJeoBmq8mmzu0cRTChdq%2FScreenshot%202025-04-24%20at%2010.30.02%E2%80%AFAM.png?alt=media&#x26;token=a217017f-d15d-4896-9541-00cde69ff513" alt=""><figcaption></figcaption></figure>

### **How to understand the result file?**

Each query from the input file is evaluated against the ground truth. The result file contains details of all the queries in the following format:

| Column 1 | Column 2     | Column 3        | Column 4         | Column 5 | Column 6 |
| -------- | ------------ | --------------- | ---------------- | -------- | -------- |
| QUESTION | GROUND TRUTH | USER PROPERTIES | GENERATED ANSWER | RESULT   | ERROR    |

* **QUESTION:** This refers to the query asked of the agent. It is the input provided by the user during testing.
* **GROUND TRUTH:** This represents the accurate and meaningfully aligned answer to the query. If the input file does not provide a ground truth, it is generated automatically after the test run.
* **USER PROPERTIES:** These are attributes defined at the user level that may influence the response. See [Document Attributes,](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/document-attributes) for more information.
* **GENERATED ANSWER:** This is the answer produced by the LLaMB in response to the given question. These generated responses contribute to the total number of generations counted in your LLaMB usage. See [LLaMB Usage](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/usage-reports/llamb-usage), for more information.

{% hint style="info" %}
**Note:** The LLaMB regression generation count is an estimate and does not follow a 1:1 mapping. The total count may vary depending on the type of queries and metric evaluations performed, and it can range from **0 to 4**.
{% endhint %}

* **RESULT:**&#x20;
  * The query is considered as PASS, indicating that the generated response is factually correct, contextually appropriate, and aligned with the ground truth.
  * The query is considered as FAIL, indicating that the generated response is either factually incorrect, contextually inappropriate, or not aligned with the ground truth.
* **ERROR:** This indicates the reason why the issue occurred or why LLaMB failed to generate a response. If any errors appear in your result file, contact Avaamo Support for assistance. These are the different types of warnings you can get:

| Types of warnings                                                             | Solution                                                                                  |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Warning: Ground truth data is missing. Please provide it to estimate metrics. | Provide the correct ground truth data in the expected format to enable metric estimation. |
| Warning: No valid chunks found for the input query.                           | Check whether the document contains valid information or the Document Group is disabled.  |
| Warning: All LLaMB skills are currently disabled.                             | Enable the LLaMB skill                                                                    |
