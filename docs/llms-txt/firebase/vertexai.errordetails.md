# Source: https://firebase.google.com/docs/reference/js/vertexai.errordetails.md.txt

# ErrorDetails interface

Details object that may be included in an error response.

**Signature:**  

    export interface ErrorDetails 

## Properties

|                                                 Property                                                  |           Type            |             Description              |
|-----------------------------------------------------------------------------------------------------------|---------------------------|--------------------------------------|
| ["@type"](https://firebase.google.com/docs/reference/js/vertexai.errordetails.md#errordetails%22@type%22) | string                    |                                      |
| [domain](https://firebase.google.com/docs/reference/js/vertexai.errordetails.md#errordetailsdomain)       | string                    | The domain where the error occurred. |
| [metadata](https://firebase.google.com/docs/reference/js/vertexai.errordetails.md#errordetailsmetadata)   | Record\<string, unknown\> | Additional metadata about the error. |
| [reason](https://firebase.google.com/docs/reference/js/vertexai.errordetails.md#errordetailsreason)       | string                    | The reason for the error.            |

## ErrorDetails."@type"

**Signature:**  

    '@type'?: string;

## ErrorDetails.domain

The domain where the error occurred.

**Signature:**  

    domain?: string;

## ErrorDetails.metadata

Additional metadata about the error.

**Signature:**  

    metadata?: Record<string, unknown>;

## ErrorDetails.reason

The reason for the error.

**Signature:**  

    reason?: string;