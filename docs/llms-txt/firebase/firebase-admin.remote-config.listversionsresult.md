# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.listversionsresult.md.txt

# ListVersionsResult interface

Interface representing a list of Remote Config template versions.

**Signature:**  

    export interface ListVersionsResult 

## Properties

|                                                                         Property                                                                          |                                                              Type                                                              |                                          Description                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [nextPageToken](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.listversionsresult.md#listversionsresultnextpagetoken) | string                                                                                                                         | Token to retrieve the next page of results, or empty if there are no more results in the list. |
| [versions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.listversionsresult.md#listversionsresultversions)           | [Version](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.version.md#version_interface)\[\] | A list of version metadata objects, sorted in reverse chronological order.                     |

## ListVersionsResult.nextPageToken

Token to retrieve the next page of results, or empty if there are no more results in the list.

**Signature:**  

    nextPageToken?: string;

## ListVersionsResult.versions

A list of version metadata objects, sorted in reverse chronological order.

**Signature:**  

    versions: Version[];