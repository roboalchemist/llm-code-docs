# Source: https://firebase.google.com/docs/reference/js/functions.httpscallableoptions.md.txt

# HttpsCallableOptions interface

An interface for metadata about how calls should be executed.

**Signature:**  

    export interface HttpsCallableOptions 

## Properties

|                                                                         Property                                                                         |  Type   |                                                                                                                                                         Description                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [limitedUseAppCheckTokens](https://firebase.google.com/docs/reference/js/functions.httpscallableoptions.md#httpscallableoptionslimiteduseappchecktokens) | boolean | If set to true, uses a limited-use App Check token for callable function requests from this instance of [Functions](https://firebase.google.com/docs/reference/js/functions.functions.md#functions_interface). You must use limited-use tokens to call functions with replay protection enabled. By default, this is false. |
| [timeout](https://firebase.google.com/docs/reference/js/functions.httpscallableoptions.md#httpscallableoptionstimeout)                                   | number  | Time in milliseconds after which to cancel if there is no response. Default is 70000.                                                                                                                                                                                                                                       |

## HttpsCallableOptions.limitedUseAppCheckTokens

If set to true, uses a limited-use App Check token for callable function requests from this instance of [Functions](https://firebase.google.com/docs/reference/js/functions.functions.md#functions_interface). You must use limited-use tokens to call functions with replay protection enabled. By default, this is false.

**Signature:**  

    limitedUseAppCheckTokens?: boolean;

## HttpsCallableOptions.timeout

Time in milliseconds after which to cancel if there is no response. Default is 70000.

**Signature:**  

    timeout?: number;