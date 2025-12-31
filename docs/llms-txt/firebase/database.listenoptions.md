# Source: https://firebase.google.com/docs/reference/js/database.listenoptions.md.txt

# ListenOptions interface

An options objects that can be used to customize a listener.

**Signature:**  

    export declare interface ListenOptions 

## Properties

|                                                 Property                                                  |  Type   |                        Description                         |
|-----------------------------------------------------------------------------------------------------------|---------|------------------------------------------------------------|
| [onlyOnce](https://firebase.google.com/docs/reference/js/database.listenoptions.md#listenoptionsonlyonce) | boolean | Whether to remove the listener after its first invocation. |

## ListenOptions.onlyOnce

Whether to remove the listener after its first invocation.

**Signature:**  

    readonly onlyOnce?: boolean;