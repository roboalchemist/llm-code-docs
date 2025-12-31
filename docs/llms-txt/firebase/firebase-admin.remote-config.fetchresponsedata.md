# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.fetchresponsedata.md.txt

# FetchResponseData interface

JSON-serializable representation of evaluated config values. This can be consumed by Remote Config web client SDKs.

**Signature:**  

    export interface FetchResponseData 

## Properties

|                                                                 Property                                                                  |             Type             |                                                                                             Description                                                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [config](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.fetchresponsedata.md#fetchresponsedataconfig) | { \[key: string\]: string; } | Defines the map of parameters returned as "entries" in the fetch response body.                                                                                                                      |
| [eTag](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.fetchresponsedata.md#fetchresponsedataetag)     | string                       | Defines the ETag response header value. Only defined for 200 and 304 responses.This is consistent with Remote Config's server eTag implementation.                                                   |
| [status](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.fetchresponsedata.md#fetchresponsedatastatus) | number                       | The HTTP status, which is useful for differentiating success responses with data from those without.This use of 200 and 304 response codes is consistent with Remote Config's server implementation. |

## FetchResponseData.config

Defines the map of parameters returned as "entries" in the fetch response body.

**Signature:**  

    config?: {
            [key: string]: string;
        };

## FetchResponseData.eTag

Defines the ETag response header value. Only defined for 200 and 304 responses.

This is consistent with Remote Config's server eTag implementation.

**Signature:**  

    eTag?: string;

## FetchResponseData.status

The HTTP status, which is useful for differentiating success responses with data from those without.

This use of 200 and 304 response codes is consistent with Remote Config's server implementation.

**Signature:**  

    status: number;