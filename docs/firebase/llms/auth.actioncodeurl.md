# Source: https://firebase.google.com/docs/reference/js/auth.actioncodeurl.md.txt

# ActionCodeURL class

A utility class to parse email action URLs such as password reset, email verification, email link sign in, etc.

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `ActionCodeURL` class.

**Signature:**  

    export declare class ActionCodeURL 

## Properties

|                                                   Property                                                    | Modifiers |      Type      |                                                                                             Description                                                                                              |
|---------------------------------------------------------------------------------------------------------------|-----------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [apiKey](https://firebase.google.com/docs/reference/js/auth.actioncodeurl.md#actioncodeurlapikey)             |           | string         | The API key of the email action link.                                                                                                                                                                |
| [code](https://firebase.google.com/docs/reference/js/auth.actioncodeurl.md#actioncodeurlcode)                 |           | string         | The action code of the email action link.                                                                                                                                                            |
| [continueUrl](https://firebase.google.com/docs/reference/js/auth.actioncodeurl.md#actioncodeurlcontinueurl)   |           | string \| null | The continue URL of the email action link. Null if not provided.                                                                                                                                     |
| [languageCode](https://firebase.google.com/docs/reference/js/auth.actioncodeurl.md#actioncodeurllanguagecode) |           | string \| null | The language code of the email action link. Null if not provided.                                                                                                                                    |
| [operation](https://firebase.google.com/docs/reference/js/auth.actioncodeurl.md#actioncodeurloperation)       |           | string         | The action performed by the email action link. It returns from one of the types from [ActionCodeInfo](https://firebase.google.com/docs/reference/js/auth.actioncodeinfo.md#actioncodeinfo_interface) |
| [tenantId](https://firebase.google.com/docs/reference/js/auth.actioncodeurl.md#actioncodeurltenantid)         |           | string \| null | The tenant ID of the email action link. Null if the email action is from the parent project.                                                                                                         |

## Methods

|                                                    Method                                                     | Modifiers |                                                                                                Description                                                                                                |
|---------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [parseLink(link)](https://firebase.google.com/docs/reference/js/auth.actioncodeurl.md#actioncodeurlparselink) | `static`  | Parses the email action link string and returns an [ActionCodeURL](https://firebase.google.com/docs/reference/js/auth.actioncodeurl.md#actioncodeurl_class) if the link is valid, otherwise returns null. |

## ActionCodeURL.apiKey

The API key of the email action link.

**Signature:**  

    readonly apiKey: string;

## ActionCodeURL.code

The action code of the email action link.

**Signature:**  

    readonly code: string;

## ActionCodeURL.continueUrl

The continue URL of the email action link. Null if not provided.

**Signature:**  

    readonly continueUrl: string | null;

## ActionCodeURL.languageCode

The language code of the email action link. Null if not provided.

**Signature:**  

    readonly languageCode: string | null;

## ActionCodeURL.operation

The action performed by the email action link. It returns from one of the types from [ActionCodeInfo](https://firebase.google.com/docs/reference/js/auth.actioncodeinfo.md#actioncodeinfo_interface)

**Signature:**  

    readonly operation: string;

## ActionCodeURL.tenantId

The tenant ID of the email action link. Null if the email action is from the parent project.

**Signature:**  

    readonly tenantId: string | null;

## ActionCodeURL.parseLink()

Parses the email action link string and returns an [ActionCodeURL](https://firebase.google.com/docs/reference/js/auth.actioncodeurl.md#actioncodeurl_class) if the link is valid, otherwise returns null.

**Signature:**  

    static parseLink(link: string): ActionCodeURL | null;

#### Parameters

| Parameter |  Type  |          Description          |
|-----------|--------|-------------------------------|
| link      | string | The email action link string. |

**Returns:**

[ActionCodeURL](https://firebase.google.com/docs/reference/js/auth.actioncodeurl.md#actioncodeurl_class) \| null

The [ActionCodeURL](https://firebase.google.com/docs/reference/js/auth.actioncodeurl.md#actioncodeurl_class) object, or null if the link is invalid.