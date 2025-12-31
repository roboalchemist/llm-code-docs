# Source: https://docs.avaamo.com/user-guide/llamb/regression-testing/run-regression-test.md

# Run regression test

You can run regression testing by uploading a CSV file with regression test data.&#x20;

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/llamb/before-you-begin).
* You can test an agent after creating and adding LLaMB skills to the agent. See [Create agent ](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills)and [Create LLaMB Content skill](https://docs.avaamo.com/user-guide/llamb/get-started/step-1-create-llamb-content-skill) to agent, for more information.
* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/other-common-actions#search-agents), for more information.
  * Click **Edit** to unlock the agent before editing.
    {% endhint %}

## Upload test file

On the `Agent` page, click `Test > Regression Testing` in the left navigation menu.

Click the `Upload test file` option and specify the following details:

{% hint style="danger" %}
**Key Point**: It is recommended to review the regression test file and incorporate all the recommended best practices. See [Regression test best practices](https://docs.avaamo.com/user-guide/llamb/regression-testing/best-practices), for more information.
{% endhint %}

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FF3qUze3GX5SeIqkvVkPw%2FScreenshot%202025-02-26%20at%2011.38.23%E2%80%AFAM.png?alt=media&#x26;token=5db9df8a-731c-4c74-9345-cfe667167061" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="141.90545654296875">Parameters</th><th width="446.460205078125">Description</th><th>Maximum length</th></tr></thead><tbody><tr><td>Test Name</td><td><p>The name of the test suite. Provide a name that helps you to identify the regression testing being performed.</p><p></p><p>Note that the <strong>Test name</strong> must be unique and is mandatory.</p></td><td>100 characters</td></tr><tr><td>CSV file</td><td><p>Click <strong>Browse</strong> to browse a CSV file with regression test cases.</p><p></p><p>You can also click the <strong>Sample test file</strong> to download a sample regression test file. This helps you to know the format required for the regression test file. </p><p></p><p>If you upload a CSV file that is not according to the format required for the regression test, then an appropriate error message with the row number of the first error encountered is displayed.</p></td><td>1000 rows</td></tr></tbody></table>

Click `Submit`. This action starts the regression testing on the agent, based on the test cases in the uploaded file.

* In the **Regression file** column, the `Test name` specified during the time of upload is displayed along with the date and time of the regression test run.
* In the **Status** column, `In Progress` status is displayed indicating that the test run is in progress. Click `Refresh`  to retrieve the latest status. See [View status and results](#view-status-and-results), for more information.
* Click **Download Input CSV** in the **Actions** column, to download the uploaded input test file in CSV format. See [Download Input CSV,](#download-input-csv) for more information.

If you do not wish to upload a test file, click  `Cancel` .

## **View status and results**

In the `Regression testing` page, you can view the status and results of regression testing. You can download the regression testing result file in CSV format.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FfqRxXXY0dPP9WuXMD3XZ%2Fimage%20(6).png?alt=media&#x26;token=8868187f-58f5-410b-a56b-f423d7805bd0" alt=""><figcaption></figcaption></figure>

### **Regression file** <a href="#regression-file" id="regression-file"></a>

The `Regression file` column displays the name of the test file and the time of the test run.

### **Status** <a href="#status" id="status"></a>

The `Status` column displays the status of the regression test along with the date and time of completion. The following values are displayed:

* **In-Progress**: This indicates that the testing is still in progress and that the system is executing the test cases from the uploaded file.
* **Completed**: Indicates that all the test cases are executed. You can also download the result file. See [Actions](#actions), for more information.
* **Failed**: Indicates that there was some failure executing the test cases. In such scenarios, you can [rerun](#run) the test.

### **Result** <a href="#result" id="result"></a>

In the **Results** column, you can view the overall outcomes of the regression testing. The following details are displayed:

* **Total Queries:** Total number of queries present in the input file.
* **Passed:** Number of generated responses that passed the test out of the total queries.
* **Failed:** Number of generated responses that failed the test out of the total queries.

### Language&#x20;

The language in which the regression test is executed. By default, the regression test is executed in English.

### **Actions**

You can perform the following actions:

1. [Run](#run)
2. [Delete](#delete)
3. [Download Results](#download-results)
4. [Download Input CSV](#download-input-csv)

#### Run

You can re-run the regression tests after making any changes to the LLaMB skill, such as updating a document, its attributes, or its group.

To re-run regression test:

* In the `Actions` column, click `Run`**.**

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FPtXlPHlzuFzSIi9SSpN8%2Fimage%20(5)%20copy.png?alt=media&#x26;token=f4093dee-5c4c-4dca-8580-5fbfe177ea0c" alt=""><figcaption></figcaption></figure>

* An alert message is displayed for confirmation. Click `OK`.
* A new run of regression testing is started.
  * In the `Status` column, `In Progress` status is displayed indicating that the test run is in progress. Click `Refresh` to retrieve the latest status. See [View status and results](#view-status-and-results), for more information.
  * Click `Download Input CSV` in the `Actions` column, to download the uploaded input test file in CSV format. See [Download Input CSV](#download-input-csv), for more information.

#### Delete

If the test data is incorrect or you wish to upload another file for regression testing delete the current test file and upload another file.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FunEBqsGVAx9aaqG4MF8L%2Fimage%20(5)%20copy.png?alt=media&#x26;token=fcdbdc9e-eb2c-4cbb-8154-37cbbc43dfe3" alt=""><figcaption></figcaption></figure>

To delete the regression test:

* In the `Actions` column, click `Delete`**.**
* An alert message is displayed for confirmation. Click `OK`.
* The corresponding regression test is deleted.

#### Download Results

You can download the regression testing result in a CSV format.

To download the results of regression testing:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FblkzrJcNc3ElstoiF84F%2Fimage%20(6)%20copy.png?alt=media&#x26;token=cbebfa5d-0924-4a19-bbee-d876a9124e98" alt=""><figcaption></figcaption></figure>

* Click `three dots` (Ellipsis) "…" in the `Actions` column.
* Click `Download Results` to download the results in CSV format.
* A copy of the result file is downloaded to your local machine. See [Understanding Results](https://docs.avaamo.com/user-guide/llamb/regression-testing/understanding-results), for more information on interpreting the regression test results.

#### Download Input CSV

You can download the uploaded input regression test file in CSV format. You can use this for further analysis of the test results.

To download the input CSV file for the regression test:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F08Wlrej4gdLkqYzBpR6A%2Fimage%20(6)%20copy%202.png?alt=media&#x26;token=eaec89de-b1ed-4f9f-869e-c1f0bd9fb6e2" alt=""><figcaption></figcaption></figure>

* Click `three dots` (Ellipsis) "…" in the `Actions` column.
* Click `Download Input CSV` to download the uploaded input test file in CSV format.
* A copy of the input test file is downloaded to your local machine.
