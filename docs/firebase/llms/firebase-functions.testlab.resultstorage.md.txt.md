# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.resultstorage.md.txt

# testLab.ResultStorage class

Locations where the test results are stored.

**Signature:**

    export declare class ResultStorage 

## Properties

| Property | Modifiers | Type | Description |
|---|---|---|---|
| [gcsPath](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.resultstorage.md#testlabresultstoragegcspath) |   | string | A storage location within Google Cloud Storage (GCS) for the test artifacts. |
| [resultsUrl](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.resultstorage.md#testlabresultstorageresultsurl) |   | string | URL to test results in Firebase Console. |
| [toolResultsExecutionId](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.resultstorage.md#testlabresultstoragetoolresultsexecutionid) |   | string | Id of the ToolResults execution that the detailed TestMatrix results are written to. |
| [toolResultsHistoryId](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.resultstorage.md#testlabresultstoragetoolresultshistoryid) |   | string | Id of the ToolResults History containing these results. |

## testLab.ResultStorage.gcsPath

A storage location within Google Cloud Storage (GCS) for the test artifacts.

**Signature:**

    gcsPath?: string;

## testLab.ResultStorage.resultsUrl

URL to test results in Firebase Console.

**Signature:**

    resultsUrl?: string;

## testLab.ResultStorage.toolResultsExecutionId

Id of the ToolResults execution that the detailed TestMatrix results are written to.

**Signature:**

    toolResultsExecutionId?: string;

## testLab.ResultStorage.toolResultsHistoryId

Id of the ToolResults History containing these results.

**Signature:**

    toolResultsHistoryId?: string;