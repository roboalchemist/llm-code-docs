# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.testmatrix.md.txt

# testLab.TestMatrix class

TestMatrix captures details about a test run.

**Signature:**  

    export declare class TestMatrix 

## Properties

|                                                                          Property                                                                           | Modifiers |                                                                     Type                                                                     |                                         Description                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [clientInfo](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.testmatrix.md#testlabtestmatrixclientinfo)                     |           | [ClientInfo](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.clientinfo.md#testlabclientinfo_class)          | Information about the client which invoked the test.                                         |
| [createTime](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.testmatrix.md#testlabtestmatrixcreatetime)                     |           | string                                                                                                                                       | When this test matrix was initially created (ISO8601 timestamp).                             |
| [invalidMatrixDetails](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.testmatrix.md#testlabtestmatrixinvalidmatrixdetails) |           | [InvalidMatrixDetails](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.md#testlabinvalidmatrixdetails)       | For 'INVALID' matrices only, describes why the matrix is invalid.                            |
| [outcomeSummary](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.testmatrix.md#testlabtestmatrixoutcomesummary)             |           | [OutcomeSummary](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.md#testlaboutcomesummary)                   | The overall outcome of the test matrix run. Only set when the test matrix state is FINISHED. |
| [resultStorage](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.testmatrix.md#testlabtestmatrixresultstorage)               |           | [ResultStorage](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.resultstorage.md#testlabresultstorage_class) | Where the results for the matrix are located.                                                |
| [state](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.testmatrix.md#testlabtestmatrixstate)                               |           | [TestState](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.md#testlabteststate)                             | Indicates the current progress of the test matrix                                            |
| [testMatrixId](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.testmatrix.md#testlabtestmatrixtestmatrixid)                 |           | string                                                                                                                                       | Unique id set by the service.                                                                |

## testLab.TestMatrix.clientInfo

Information about the client which invoked the test.

**Signature:**  

    clientInfo: ClientInfo;

## testLab.TestMatrix.createTime

When this test matrix was initially created (ISO8601 timestamp).

**Signature:**  

    createTime: string;

## testLab.TestMatrix.invalidMatrixDetails

For 'INVALID' matrices only, describes why the matrix is invalid.

**Signature:**  

    invalidMatrixDetails?: InvalidMatrixDetails;

## testLab.TestMatrix.outcomeSummary

The overall outcome of the test matrix run. Only set when the test matrix state is FINISHED.

**Signature:**  

    outcomeSummary?: OutcomeSummary;

## testLab.TestMatrix.resultStorage

Where the results for the matrix are located.

**Signature:**  

    resultStorage: ResultStorage;

## testLab.TestMatrix.state

Indicates the current progress of the test matrix

**Signature:**  

    state: TestState;

## testLab.TestMatrix.testMatrixId

Unique id set by the service.

**Signature:**  

    testMatrixId: string;