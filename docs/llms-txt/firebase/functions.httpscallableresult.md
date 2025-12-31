# Source: https://firebase.google.com/docs/reference/js/functions.httpscallableresult.md.txt

# HttpsCallableResult interface

An `HttpsCallableResult` wraps a single result from a function call.

**Signature:**  

    export interface HttpsCallableResult<ResponseData = unknown> 

## Properties

|                                                    Property                                                    |     Type     |              Description              |
|----------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------|
| [data](https://firebase.google.com/docs/reference/js/functions.httpscallableresult.md#httpscallableresultdata) | ResponseData | Data returned from callable function. |

## HttpsCallableResult.data

Data returned from callable function.

**Signature:**  

    readonly data: ResponseData;