# Source: https://firebase.google.com/docs/reference/js/auth.phonemultifactorgenerator.md.txt

# PhoneMultiFactorGenerator class

Provider for generating a [PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.phonemultifactorassertion.md#phonemultifactorassertion_interface).

**Signature:**  

    export declare class PhoneMultiFactorGenerator 

## Properties

|                                                            Property                                                             | Modifiers |  Type  |                     Description                     |
|---------------------------------------------------------------------------------------------------------------------------------|-----------|--------|-----------------------------------------------------|
| [FACTOR_ID](https://firebase.google.com/docs/reference/js/auth.phonemultifactorgenerator.md#phonemultifactorgeneratorfactor_id) | `static`  | string | The identifier of the phone second factor: `phone`. |

## Methods

|                                                                   Method                                                                    | Modifiers |                                                                                                 Description                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [assertion(credential)](https://firebase.google.com/docs/reference/js/auth.phonemultifactorgenerator.md#phonemultifactorgeneratorassertion) | `static`  | Provides a [PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.phonemultifactorassertion.md#phonemultifactorassertion_interface) to confirm ownership of the phone second factor. |

## PhoneMultiFactorGenerator.FACTOR_ID

The identifier of the phone second factor: `phone`.

**Signature:**  

    static FACTOR_ID: string;

## PhoneMultiFactorGenerator.assertion()

Provides a [PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.phonemultifactorassertion.md#phonemultifactorassertion_interface) to confirm ownership of the phone second factor.

This method does not work in a Node.js environment.

**Signature:**  

    static assertion(credential: PhoneAuthCredential): PhoneMultiFactorAssertion;

#### Parameters

| Parameter  |                                                            Type                                                            | Description |
|------------|----------------------------------------------------------------------------------------------------------------------------|-------------|
| credential | [PhoneAuthCredential](https://firebase.google.com/docs/reference/js/auth.phoneauthcredential.md#phoneauthcredential_class) |             |

**Returns:**

[PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.phonemultifactorassertion.md#phonemultifactorassertion_interface)

A [PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.phonemultifactorassertion.md#phonemultifactorassertion_interface) which can be used with [MultiFactorResolver.resolveSignIn()](https://firebase.google.com/docs/reference/js/auth.multifactorresolver.md#multifactorresolverresolvesignin)