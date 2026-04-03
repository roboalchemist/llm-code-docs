# Source: https://firebase.google.com/docs/reference/js/auth.applicationverifier.md.txt

# ApplicationVerifier interface

A verifier for domain verification and abuse prevention.

Currently, the only implementation is [RecaptchaVerifier](https://firebase.google.com/docs/reference/js/auth.recaptchaverifier.md#recaptchaverifier_class).

**Signature:**  

    export interface ApplicationVerifier 

## Properties

|                                                 Property                                                  |  Type  |                           Description                           |
|-----------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------|
| [type](https://firebase.google.com/docs/reference/js/auth.applicationverifier.md#applicationverifiertype) | string | Identifies the type of application verifier (e.g. "recaptcha"). |

## Methods

|                                                     Method                                                      |            Description             |
|-----------------------------------------------------------------------------------------------------------------|------------------------------------|
| [verify()](https://firebase.google.com/docs/reference/js/auth.applicationverifier.md#applicationverifierverify) | Executes the verification process. |

## ApplicationVerifier.type

Identifies the type of application verifier (e.g. "recaptcha").

**Signature:**  

    readonly type: string;

## ApplicationVerifier.verify()

Executes the verification process.

**Signature:**  

    verify(): Promise<string>;

**Returns:**

Promise\<string\>

A Promise for a token that can be used to assert the validity of a request.