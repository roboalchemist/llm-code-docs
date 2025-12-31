# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent/faqs.md

# Source: https://docs.avaamo.com/user-guide/llamb/regression-testing/faqs.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent/faqs.md

# Source: https://docs.avaamo.com/user-guide/llamb/regression-testing/faqs.md

# FAQ's

**1. What happens if an incorrect input file is uploaded for testing?**

An incorrect input file may contain **syntax errors, incorrect entries, or invalid data**, leading to errors and abnormal metric values in the results.

**2. What should be done if the results are showing as FAIL?**

A **FAIL** indicates that the generated response is either factually incorrect, contextually inappropriate, or not aligned with the ground truth. Further debugging is required to identify the root cause and address any underlying issues.

**3. How do you analyze the results of a regression test?**

Once the regression test is completed:

* The UI displays the total number of queries along with a breakdown of passed and failed queries. This offers a directional analysis of the uploaded file's quality.

Refer [Understanding results](https://docs.avaamo.com/user-guide/llamb/regression-testing/understanding-results), for complete details about this.

**4. What should be done after conducting a regression test?**

After running a regression test, [analyze the results file](https://docs.avaamo.com/user-guide/llamb/regression-testing/understanding-results) to identify any discrepancies or failures. If the test results do not meet expectations or fail to generate the correct responses, review the data and make necessary adjustments to [improve accuracy](https://docs.avaamo.com/user-guide/llamb/regression-testing/how-to-improve-accuracy).

**5. What do the different columns in the input and results files represent?**

Refer [Regression test file format](https://docs.avaamo.com/user-guide/llamb/regression-testing/regression-test-file-format) and [Understanding results](https://docs.avaamo.com/user-guide/llamb/regression-testing/understanding-results), for complete details about this.

#### **6. What happens if the input regression file does not specify any user properties, but the ingested document includes them?**

If the input regression file does not define any `user_properties`, but the ingested document is associated with specific document properties, the regression results are still generated without filtering based on those properties.

#### 7. How to test soft unhandled queries during regression testing

To verify soft unhandled responses, include the marker `<avm-stream-aborted>` in either the `ground_truth` or `generated_answer` fields. This helps identify cases where the system gracefully aborted the stream without triggering a hard failure.
