# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.listversionsoptions.md.txt

# ListVersionsOptions interface

Interface representing options for Remote Config list versions operation.

**Signature:**  

    export interface ListVersionsOptions 

## Properties

|                                                                             Property                                                                              |       Type       |                                                               Description                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [endTime](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.listversionsoptions.md#listversionsoptionsendtime)                   | Date \| string   | Specifies the latest update time to include in the results. Any entries updated on or after this time are omitted.                      |
| [endVersionNumber](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.listversionsoptions.md#listversionsoptionsendversionnumber) | string \| number | Specifies the newest version number to include in the results. If specified, must be greater than zero. Defaults to the newest version. |
| [pageSize](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.listversionsoptions.md#listversionsoptionspagesize)                 | number           | The maximum number of items to return per page.                                                                                         |
| [pageToken](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.listversionsoptions.md#listversionsoptionspagetoken)               | string           | The `nextPageToken` value returned from a previous list versions request, if any.                                                       |
| [startTime](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.listversionsoptions.md#listversionsoptionsstarttime)               | Date \| string   | Specifies the earliest update time to include in the results. Any entries updated before this time are omitted.                         |

## ListVersionsOptions.endTime

Specifies the latest update time to include in the results. Any entries updated on or after this time are omitted.

**Signature:**  

    endTime?: Date | string;

## ListVersionsOptions.endVersionNumber

Specifies the newest version number to include in the results. If specified, must be greater than zero. Defaults to the newest version.

**Signature:**  

    endVersionNumber?: string | number;

## ListVersionsOptions.pageSize

The maximum number of items to return per page.

**Signature:**  

    pageSize?: number;

## ListVersionsOptions.pageToken

The `nextPageToken` value returned from a previous list versions request, if any.

**Signature:**  

    pageToken?: string;

## ListVersionsOptions.startTime

Specifies the earliest update time to include in the results. Any entries updated before this time are omitted.

**Signature:**  

    startTime?: Date | string;