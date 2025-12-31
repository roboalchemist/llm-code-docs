# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.resultstorage.md.txt

# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.resultstorage.md.txt

# testLab.ResultStorage interface

Locations where test results are stored.

**Signature:**  

    export interface ResultStorage 

## Properties

|                                                                                    Property                                                                                    |  Type  |                                                                                                                                          Description                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [gcsPath](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.resultstorage.md#testlabresultstoragegcspath)                           | string | Location in Google Cloud Storage where test results are written to. In the form "gs://bucket/path/to/somewhere".                                                                                                                                                                               |
| [resultsUri](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.resultstorage.md#testlabresultstorageresultsuri)                     | string | URI to the test results in the Firebase Web Console.                                                                                                                                                                                                                                           |
| [toolResultsExecution](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.resultstorage.md#testlabresultstoragetoolresultsexecution) | string | Tool Results execution resource containing test results. Format is `projects/{project_id}/histories/{history_id}/executions/{execution_id}`. Optional, can be omitted in erroneous test states. See https://firebase.google.com/docs/test-lab/reference/toolresults/rest for more information. |
| [toolResultsHistory](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.resultstorage.md#testlabresultstoragetoolresultshistory)     | string | Tool Results history resource containing test results. Format is `projects/{project_id}/histories/{history_id}`. See https://firebase.google.com/docs/test-lab/reference/toolresults/rest for more information.                                                                                |

## testLab.ResultStorage.gcsPath

Location in Google Cloud Storage where test results are written to. In the form "gs://bucket/path/to/somewhere".

**Signature:**  

    gcsPath: string;

## testLab.ResultStorage.resultsUri

URI to the test results in the Firebase Web Console.

**Signature:**  

    resultsUri: string;

## testLab.ResultStorage.toolResultsExecution

Tool Results execution resource containing test results. Format is `projects/{project_id}/histories/{history_id}/executions/{execution_id}`. Optional, can be omitted in erroneous test states. See https://firebase.google.com/docs/test-lab/reference/toolresults/rest for more information.

**Signature:**  

    toolResultsExecution: string;

## testLab.ResultStorage.toolResultsHistory

Tool Results history resource containing test results. Format is `projects/{project_id}/histories/{history_id}`. See https://firebase.google.com/docs/test-lab/reference/toolresults/rest for more information.

**Signature:**  

    toolResultsHistory: string;