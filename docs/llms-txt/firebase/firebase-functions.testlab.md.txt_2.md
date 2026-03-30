# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.md.txt

# testLab namespace

## Functions

| Function | Description |
|---|---|
| [onTestMatrixCompleted(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.md#testlabontestmatrixcompleted) | Event handler which triggers when a Firebase test matrix completes. |
| [onTestMatrixCompleted(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.md#testlabontestmatrixcompleted) | Event handler which triggers when a Firebase test matrix completes. |

## Interfaces

| Interface | Description |
|---|---|
| [ClientInfo](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.clientinfo.md#testlabclientinfo_interface) | Information about the client which invoked the test. |
| [ResultStorage](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.resultstorage.md#testlabresultstorage_interface) | Locations where test results are stored. |
| [TestMatrixCompletedData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.testmatrixcompleteddata.md#testlabtestmatrixcompleteddata_interface) | The data within all Firebase test matrix completed events. |

## Type Aliases

| Type Alias | Description |
|---|---|
| [OutcomeSummary](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.md#testlaboutcomesummary) | Outcome summary for a finished test matrix. |
| [TestState](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.md#testlabteststate) | Possible test states for a test matrix. |

## testLab.onTestMatrixCompleted()

Event handler which triggers when a Firebase test matrix completes.

**Signature:**

    export declare function onTestMatrixCompleted(handler: (event: CloudEvent<TestMatrixCompletedData>) => any | Promise<any>): CloudFunction<CloudEvent<TestMatrixCompletedData>>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| handler | (event: [CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<[TestMatrixCompletedData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.testmatrixcompleteddata.md#testlabtestmatrixcompleteddata_interface)\>) =\> any \| Promise\<any\> | Event handler which is run every time a Firebase test matrix completes. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<[TestMatrixCompletedData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.testmatrixcompleteddata.md#testlabtestmatrixcompleteddata_interface)\>\>

A Cloud Function that you can export and deploy.

## testLab.onTestMatrixCompleted()

Event handler which triggers when a Firebase test matrix completes.

**Signature:**

    export declare function onTestMatrixCompleted(opts: EventHandlerOptions, handler: (event: CloudEvent<TestMatrixCompletedData>) => any | Promise<any>): CloudFunction<CloudEvent<TestMatrixCompletedData>>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| opts | [EventHandlerOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventhandleroptions.md#eventhandleroptions_interface) | Options that can be set on an individual event-handling function. |
| handler | (event: [CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<[TestMatrixCompletedData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.testmatrixcompleteddata.md#testlabtestmatrixcompleteddata_interface)\>) =\> any \| Promise\<any\> | Event handler which is run every time a Firebase test matrix completes. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<[TestMatrixCompletedData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.testmatrixcompleteddata.md#testlabtestmatrixcompleteddata_interface)\>\>

A Cloud Function that you can export and deploy.

## testLab.OutcomeSummary

Outcome summary for a finished test matrix.

**Signature:**

    export type OutcomeSummary = 
    /** The default value. This value is used if the state is omitted. */
    "OUTCOME_SUMMARY_UNSPECIFIED"
    /**
     * The test matrix run was successful, for instance:
     * - All test cases passed.
     * - No crash of the application under test was detected.
     */
     | "SUCCESS"
    /**
     * A run failed, for instance:
     * - One or more test case failed.
     * - A test timed out.
     * - The application under test crashed.
     */
     | "FAILURE"
    /**
     * Something unexpected happened. The test run should still be considered
     * unsuccessful but this is likely a transient problem and re-running the
     * test might be successful.
     */
     | "INCONCLUSIVE"
    /** All tests were skipped. */
     | "SKIPPED";

## testLab.TestState

Possible test states for a test matrix.

**Signature:**

    export type TestState = 
    /** The default value. This value is used if the state is omitted. */
    "TEST_STATE_UNSPECIFIED"
    /** The test matrix is being validated. */
     | "VALIDATING"
    /** The test matrix is waiting for resources to become available. */
     | "PENDING"
    /** The test matrix has completed normally. */
     | "FINISHED"
    /** The test matrix has completed because of an infrastructure failure. */
     | "ERROR"
    /** The test matrix was not run because the provided inputs are not valid. */
     | "INVALID";