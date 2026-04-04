# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.testmatrixbuilder.md.txt

# testLab.TestMatrixBuilder class

Builder used to create Cloud Functions for Test Lab test matrices events.

**Signature:**  

    export declare class TestMatrixBuilder 

## Methods

|                                                                             Method                                                                             | Modifiers |                     Description                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------|
| [onComplete(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.testmatrixbuilder.md#testlabtestmatrixbuilderoncomplete) |           | Handle a TestMatrix that reached a final test state. |

## testLab.TestMatrixBuilder.onComplete()

Handle a TestMatrix that reached a final test state.

**Signature:**  

    onComplete(handler: (testMatrix: TestMatrix, context: EventContext) => PromiseLike<any> | any): CloudFunction<TestMatrix>;

### Parameters

| Parameter |                                                                                                                                                           Type                                                                                                                                                           | Description |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| handler   | (testMatrix: [TestMatrix](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.testmatrix.md#testlabtestmatrix_class), context: [EventContext](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontext_interface)) =\> PromiseLike\<any\> \| any |             |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[TestMatrix](https://firebase.google.com/docs/reference/functions/firebase-functions.testlab.testmatrix.md#testlabtestmatrix_class)\>