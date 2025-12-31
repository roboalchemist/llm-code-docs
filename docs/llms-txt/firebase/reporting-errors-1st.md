# Source: https://firebase.google.com/docs/functions/1st-gen/reporting-errors-1st.md.txt

<br />

| **Note:** The 1st-gen functionality described in this page is also supported inCloud Functions(2nd gen) with improved features and performance. For more information about 2nd gen, see the[version comparison](https://firebase.google.com/docs/functions/version-comparison). To go directly to the 2nd gen guide for this feature, see[Report errors](https://firebase.google.com/docs/functions/reporting-errors).

## Automatically reporting errors

You can emit an error from a function to[Error Reporting](https://cloud.google.com/error-reporting/docs)as shown below:  

    // These WILL be reported to Error Reporting
    throw new Error('I failed you'); // Will cause a cold start if not caught

If you would like more fine-grained error reporting, you can use the[Error Reporting client libraries](https://cloud.google.com/error-reporting/docs/reference/libraries).

You can view the reported errors in[Error Reporting](https://console.cloud.google.com/errors)in the Google Cloud console. You can also see the errors reported from a particular function when you select it from the[list of functions](https://console.cloud.google.com/functions)in the Google Cloud console.

Uncaught exceptions produced by your function will appear in Error Reporting. Note that some types of uncaught exceptions (such as those thrown asynchronously) will cause a[cold start](https://cloud.google.com/functions/docs/bestpractices/tips)to occur upon a future function invocation. This increases the amount of time your function will take to run.

## Manually reporting errors

### Importing dependencies

To report an error to[Error Reporting](https://cloud.google.com/error-reporting/docs)from a function, import the`error`function from the Cloud Functions[logger](https://firebase.google.com/docs/reference/functions/firebase-functions.logger)SDK:  

    // All available logging functions
    const {
      log,
      info,
      debug,
      warn,
      error,
      write,
    } = require("firebase-functions/logger");  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/monitor-cloud-logging/functions/index.js#L23-L31

### Sending toCloud Logging

The`error`function from the Cloud Functions[logger](https://firebase.google.com/docs/reference/functions/firebase-functions.logger)SDK will report errors to bothCloud Loggingand[Error Reporting](https://cloud.google.com/error-reporting/docs). To include more context from the error as[structured data](https://cloud.google.com/logging/docs/structured-logging), pass an error object as the second argument:  

     } catch (err) {
      // Attach an error object as the second argument
      error("Unable to read quote from Firestore, sending default instead",
          err);  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/monitor-cloud-logging/functions/index.js#L83-L86