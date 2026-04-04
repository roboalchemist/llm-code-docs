# Source: https://docs.avaamo.com/user-guide/llamb/regression-testing/how-to-improve-accuracy.md

# How to improve accuracy?

Ensuring that queries achieve a good correctness score is essential for validating the agent's performance. To improve results, follow these steps:&#x20;

1. **If no ground truth is specified in the regression test input file:**
   * The system generates a ground truth for those queries.
   * Review the generated ground truths, update them to match your expected answers, and rerun the regression test.
2. **If ground truth is specified in the input file:**
   * Modify the ground truth based on the expected answers and rerun the regression test.
3. **If your** [**result files**](https://docs.avaamo.com/user-guide/llamb/regression-testing/understanding-results) **have a status of FAIL:**
   * Check if the added ground truth is present in the ingested content.
   * Improve section headers to enhance content clarity and relevance. Refer [section header](https://docs.avaamo.com/user-guide/get-started/step-2-ingest-enterprise-content/view-and-edit-knowledge#sections), for complete details.
   * Debug the answers by referring to the generated errors and warnings, and refine the input file before re-executing the test. Refer to errors and warnings in [Understanding results](https://docs.avaamo.com/user-guide/llamb/regression-testing/understanding-results), for reference.

By following these steps, you can systematically improve test results and enhance the agent's performance.
