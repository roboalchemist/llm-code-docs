# Source: https://firebase.google.com/docs/functions/1st-gen/test-lab-events-1st.md.txt

<br />

| **Note:** The 1st-gen functionality described in this page is also supported inCloud Functions(2nd gen) with improved features and performance. For more information about 2nd gen, see the[version comparison](https://firebase.google.com/docs/functions/version-comparison). To go directly to the 2nd gen guide for this feature, see[Test Lab triggers](https://firebase.google.com/docs/functions/test-lab-events).

## Trigger a function on TestMatrix completion

Create a new function that triggers when a TestMatrix completes with the event handler`functions.testLab.testMatrix().onComplete()`:  

    exports.sendEmailNotification = functions.testLab.testMatrix().onComplete((testMatrix) => {
      // ...
    });

## Handle test states and outcomes

Each execution of your function is passed a[`TestMatrix`](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.testmatrix)which includes the final state of the matrix and details to help understand problems.  

    exports.handleTestMatrixCompletion = functions.testLab.testMatrix().onComplete(testMatrix => {
      const matrixId = testMatrix.testMatrixId;
      switch (testMatrix.state) {
        case 'FINISHED':
          console.log(`TestMatrix ${matrixId} finished with outcome: ${testMatrix.outcomeSummary}`);
          break;
        case 'INVALID':
          console.log(`TestMatrix ${matrixId} was marked as invalid: ${testMatrix.invalidMatrixDetails}`);
          break;
        default:
          console.log(`TestMatrix ${matrixId} completed with state ${testMatrix.state}`);
      }
      return null;
    });

## Access client details

Test matrices may be created from different sources or workflows. It is therefore often desirable to create functions that perform different actions based on the source or other important context of the test. To help with this,`gcloud`allows you to pass arbitrary information when starting a test that can be accessed later in your function. For example:  

    gcloud beta firebase test android run \
        --app=path/to/app.apk \
        --client-details testType=pr,link=https://path/to/pull-request

Example function:  

    exports.notifyOnPullRequestFailure = functions.testLab.testMatrix().onComplete(testMatrix => {
      if (testMatrix.clientInfo.details['testType'] != 'pr') {
        // Not a pull request
        return null;
      }

      if (testMatrix.state == 'FINISHED' && testMatrix.outcomeSummary == 'SUCCESS') {
        // No failure
        return null;
      }

      const link = testMatrix.clientInfo.details['link'];
      let message = `Test Lab validation for pull request ${link} failed. `;

      if (!!testMatrix.resultStorage.resultsUrl) {
        message += `Test results available at ${testMatrix.resultStorage.resultsUrl}. `;
      }

      // Send notification here ...
    });