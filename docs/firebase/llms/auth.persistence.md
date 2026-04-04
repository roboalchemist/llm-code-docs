# Source: https://firebase.google.com/docs/reference/js/auth.persistence.md.txt

# Persistence interface

An interface covering the possible persistence mechanism types.

**Signature:**  

    export interface Persistence 

## Properties

|                                         Property                                          |                    Type                    |                                                                                                                                                   Description                                                                                                                                                   |
|-------------------------------------------------------------------------------------------|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [type](https://firebase.google.com/docs/reference/js/auth.persistence.md#persistencetype) | 'SESSION' \| 'LOCAL' \| 'NONE' \| 'COOKIE' | Type of Persistence. - 'SESSION' is used for temporary persistence such as `sessionStorage`. - 'LOCAL' is used for long term persistence such as `localStorage` or `IndexedDB`. - 'NONE' is used for in-memory, or no persistence. - 'COOKIE' is used for cookie persistence, useful for server-side rendering. |

## Persistence.type

Type of Persistence. - 'SESSION' is used for temporary persistence such as `sessionStorage`. - 'LOCAL' is used for long term persistence such as `localStorage` or `IndexedDB`. - 'NONE' is used for in-memory, or no persistence. - 'COOKIE' is used for cookie persistence, useful for server-side rendering.

**Signature:**  

    readonly type: 'SESSION' | 'LOCAL' | 'NONE' | 'COOKIE';