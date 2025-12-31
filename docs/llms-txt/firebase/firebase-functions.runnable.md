# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.runnable.md.txt

# Runnable interface

A Runnable has a `run` method which directly invokes the user-defined function - useful for unit testing.

**Signature:**  

    export interface Runnable<T> 

## Properties

|                                                Property                                                |                         Type                          |                Description                 |
|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------|--------------------------------------------|
| [run](https://firebase.google.com/docs/reference/functions/firebase-functions.runnable.md#runnablerun) | (data: T, context: any) =\> PromiseLike\<any\> \| any | Directly invoke the user defined function. |

## Runnable.run

Directly invoke the user defined function.

**Signature:**  

    run: (data: T, context: any) => PromiseLike<any> | any;