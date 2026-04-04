# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.createrequest.md.txt

# CreateRequest interface

Interface representing the properties to set on a new user record to be created.

**Signature:**  

    export interface CreateRequest extends UpdateRequest 

**Extends:** [UpdateRequest](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updaterequest.md#updaterequest_interface)

## Properties

|                                                              Property                                                              |                                                                                  Type                                                                                   |                 Description                 |
|------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| [multiFactor](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.createrequest.md#createrequestmultifactor) | [MultiFactorCreateSettings](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorcreatesettings.md#multifactorcreatesettings_interface) | The user's multi-factor related properties. |
| [uid](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.createrequest.md#createrequestuid)                 | string                                                                                                                                                                  | The user's `uid`.                           |

## CreateRequest.multiFactor

The user's multi-factor related properties.

**Signature:**  

    multiFactor?: MultiFactorCreateSettings;

## CreateRequest.uid

The user's `uid`.

**Signature:**  

    uid?: string;