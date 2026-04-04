# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.testmatrixcompleteddata.md.txt

# testLab.TestMatrixCompletedData interface

The data within all Firebase test matrix completed events.

**Signature:**  

    export interface TestMatrixCompletedData 

## Properties

|                                                                                              Property                                                                                              |                                                                             Type                                                                              |                                                Description                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [clientInfo](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.testmatrixcompleteddata.md#testlabtestmatrixcompleteddataclientinfo)                     | [ClientInfo](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.clientinfo.md#testlabclientinfo_interface)          | Information provided by the client that created the test matrix.                                           |
| [createTime](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.testmatrixcompleteddata.md#testlabtestmatrixcompleteddatacreatetime)                     | string                                                                                                                                                        | Time the test matrix was created.                                                                          |
| [invalidMatrixDetails](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.testmatrixcompleteddata.md#testlabtestmatrixcompleteddatainvalidmatrixdetails) | string                                                                                                                                                        | Code that describes why the test matrix is considered invalid. Only set for matrices in the INVALID state. |
| [outcomeSummary](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.testmatrixcompleteddata.md#testlabtestmatrixcompleteddataoutcomesummary)             | [OutcomeSummary](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.md#testlaboutcomesummary)                       | Outcome summary of the test matrix.                                                                        |
| [resultStorage](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.testmatrixcompleteddata.md#testlabtestmatrixcompleteddataresultstorage)               | [ResultStorage](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.resultstorage.md#testlabresultstorage_interface) | Locations where test results are stored.                                                                   |
| [state](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.testmatrixcompleteddata.md#testlabtestmatrixcompleteddatastate)                               | [TestState](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.md#testlabteststate)                                 | State of the test matrix.                                                                                  |
| [testMatrixId](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.testlab.testmatrixcompleteddata.md#testlabtestmatrixcompleteddatatestmatrixid)                 | string                                                                                                                                                        | ID of the test matrix this event belongs to.                                                               |

## testLab.TestMatrixCompletedData.clientInfo

Information provided by the client that created the test matrix.

**Signature:**  

    clientInfo: ClientInfo;

## testLab.TestMatrixCompletedData.createTime

Time the test matrix was created.

**Signature:**  

    createTime: string;

## testLab.TestMatrixCompletedData.invalidMatrixDetails

Code that describes why the test matrix is considered invalid. Only set for matrices in the INVALID state.

**Signature:**  

    invalidMatrixDetails: string;

## testLab.TestMatrixCompletedData.outcomeSummary

Outcome summary of the test matrix.

**Signature:**  

    outcomeSummary: OutcomeSummary;

## testLab.TestMatrixCompletedData.resultStorage

Locations where test results are stored.

**Signature:**  

    resultStorage: ResultStorage;

## testLab.TestMatrixCompletedData.state

State of the test matrix.

**Signature:**  

    state: TestState;

## testLab.TestMatrixCompletedData.testMatrixId

ID of the test matrix this event belongs to.

**Signature:**  

    testMatrixId: string;