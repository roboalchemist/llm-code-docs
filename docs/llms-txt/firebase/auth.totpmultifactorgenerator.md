# Source: https://firebase.google.com/docs/reference/js/auth.totpmultifactorgenerator.md.txt

# TotpMultiFactorGenerator class

Provider for generating a [TotpMultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.totpmultifactorassertion.md#totpmultifactorassertion_interface).

**Signature:**  

    export declare class TotpMultiFactorGenerator 

## Properties

|                                                           Property                                                            | Modifiers |  Type  |                    Description                    |
|-------------------------------------------------------------------------------------------------------------------------------|-----------|--------|---------------------------------------------------|
| [FACTOR_ID](https://firebase.google.com/docs/reference/js/auth.totpmultifactorgenerator.md#totpmultifactorgeneratorfactor_id) | `static`  | 'totp' | The identifier of the TOTP second factor: `totp`. |

## Methods

|                                                                                      Method                                                                                      | Modifiers |                                                                                                                                                                                                  Description                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [assertionForEnrollment(secret, oneTimePassword)](https://firebase.google.com/docs/reference/js/auth.totpmultifactorgenerator.md#totpmultifactorgeneratorassertionforenrollment) | `static`  | Provides a [TotpMultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.totpmultifactorassertion.md#totpmultifactorassertion_interface) to confirm ownership of the TOTP (time-based one-time password) second factor. This assertion is used to complete enrollment in TOTP second factor.                                                                                                  |
| [assertionForSignIn(enrollmentId, oneTimePassword)](https://firebase.google.com/docs/reference/js/auth.totpmultifactorgenerator.md#totpmultifactorgeneratorassertionforsignin)   | `static`  | Provides a [TotpMultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.totpmultifactorassertion.md#totpmultifactorassertion_interface) to confirm ownership of the TOTP second factor. This assertion is used to complete signIn with TOTP as the second factor.                                                                                                                            |
| [generateSecret(session)](https://firebase.google.com/docs/reference/js/auth.totpmultifactorgenerator.md#totpmultifactorgeneratorgeneratesecret)                                 | `static`  | Returns a promise to [TotpSecret](https://firebase.google.com/docs/reference/js/auth.totpsecret.md#totpsecret_class) which contains the TOTP shared secret key and other parameters. Creates a TOTP secret as part of enrolling a TOTP second factor. Used for generating a QR code URL or inputting into a TOTP app. This method uses the auth instance corresponding to the user in the multiFactorSession. |

## TotpMultiFactorGenerator.FACTOR_ID

The identifier of the TOTP second factor: `totp`.

**Signature:**  

    static FACTOR_ID: 'totp';

## TotpMultiFactorGenerator.assertionForEnrollment()

Provides a [TotpMultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.totpmultifactorassertion.md#totpmultifactorassertion_interface) to confirm ownership of the TOTP (time-based one-time password) second factor. This assertion is used to complete enrollment in TOTP second factor.

**Signature:**  

    static assertionForEnrollment(secret: TotpSecret, oneTimePassword: string): TotpMultiFactorAssertion;

#### Parameters

|    Parameter    |                                              Type                                               |                                                                          Description                                                                          |
|-----------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| secret          | [TotpSecret](https://firebase.google.com/docs/reference/js/auth.totpsecret.md#totpsecret_class) | A [TotpSecret](https://firebase.google.com/docs/reference/js/auth.totpsecret.md#totpsecret_class) containing the shared secret key and other TOTP parameters. |
| oneTimePassword | string                                                                                          | One-time password from TOTP App.                                                                                                                              |

**Returns:**

[TotpMultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.totpmultifactorassertion.md#totpmultifactorassertion_interface)

A [TotpMultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.totpmultifactorassertion.md#totpmultifactorassertion_interface) which can be used with [MultiFactorUser.enroll()](https://firebase.google.com/docs/reference/js/auth.multifactoruser.md#multifactoruserenroll).

## TotpMultiFactorGenerator.assertionForSignIn()

Provides a [TotpMultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.totpmultifactorassertion.md#totpmultifactorassertion_interface) to confirm ownership of the TOTP second factor. This assertion is used to complete signIn with TOTP as the second factor.

**Signature:**  

    static assertionForSignIn(enrollmentId: string, oneTimePassword: string): TotpMultiFactorAssertion;

#### Parameters

|    Parameter    |  Type  |                 Description                 |
|-----------------|--------|---------------------------------------------|
| enrollmentId    | string | identifies the enrolled TOTP second factor. |
| oneTimePassword | string | One-time password from TOTP App.            |

**Returns:**

[TotpMultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.totpmultifactorassertion.md#totpmultifactorassertion_interface)

A [TotpMultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.totpmultifactorassertion.md#totpmultifactorassertion_interface) which can be used with [MultiFactorResolver.resolveSignIn()](https://firebase.google.com/docs/reference/js/auth.multifactorresolver.md#multifactorresolverresolvesignin).

## TotpMultiFactorGenerator.generateSecret()

Returns a promise to [TotpSecret](https://firebase.google.com/docs/reference/js/auth.totpsecret.md#totpsecret_class) which contains the TOTP shared secret key and other parameters. Creates a TOTP secret as part of enrolling a TOTP second factor. Used for generating a QR code URL or inputting into a TOTP app. This method uses the auth instance corresponding to the user in the multiFactorSession.

**Signature:**  

    static generateSecret(session: MultiFactorSession): Promise<TotpSecret>;

#### Parameters

| Parameter |                                                            Type                                                             |                                                                        Description                                                                        |
|-----------|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| session   | [MultiFactorSession](https://firebase.google.com/docs/reference/js/auth.multifactorsession.md#multifactorsession_interface) | The [MultiFactorSession](https://firebase.google.com/docs/reference/js/auth.multifactorsession.md#multifactorsession_interface) that the user is part of. |

**Returns:**

Promise\<[TotpSecret](https://firebase.google.com/docs/reference/js/auth.totpsecret.md#totpsecret_class)\>

A promise to [TotpSecret](https://firebase.google.com/docs/reference/js/auth.totpsecret.md#totpsecret_class).