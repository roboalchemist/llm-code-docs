# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorsettings.md.txt

# MultiFactorSettings class

The multi-factor related user settings.

**Signature:**  

    export declare class MultiFactorSettings 

## Properties

|                                                                        Property                                                                        | Modifiers |                                                                   Type                                                                    |                                                    Description                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [enrolledFactors](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorsettings.md#multifactorsettingsenrolledfactors) |           | [MultiFactorInfo](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorinfo.md#multifactorinfo_class)\[\] | List of second factors enrolled with the current user. Currently only phone and TOTP second factors are supported. |

## Methods

|                                                                 Method                                                                 | Modifiers |                               Description                               |
|----------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------------------------|
| [toJSON()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorsettings.md#multifactorsettingstojson) |           | Returns a JSON-serializable representation of this multi-factor object. |

## MultiFactorSettings.enrolledFactors

List of second factors enrolled with the current user. Currently only phone and TOTP second factors are supported.

**Signature:**  

    enrolledFactors: MultiFactorInfo[];

## MultiFactorSettings.toJSON()

Returns a JSON-serializable representation of this multi-factor object.

**Signature:**  

    toJSON(): object;

**Returns:**

object

A JSON-serializable representation of this multi-factor object.