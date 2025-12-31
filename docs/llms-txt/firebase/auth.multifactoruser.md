# Source: https://firebase.google.com/docs/reference/js/auth.multifactoruser.md.txt

# MultiFactorUser interface

An interface that defines the multi-factor related properties and operations pertaining to a [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface).

**Signature:**  

    export interface MultiFactorUser 

## Properties

|                                                        Property                                                         |                                                          Type                                                          |                      Description                      |
|-------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| [enrolledFactors](https://firebase.google.com/docs/reference/js/auth.multifactoruser.md#multifactoruserenrolledfactors) | [MultiFactorInfo](https://firebase.google.com/docs/reference/js/auth.multifactorinfo.md#multifactorinfo_interface)\[\] | Returns a list of the user's enrolled second factors. |

## Methods

|                                                            Method                                                             |                                                                                         Description                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [enroll(assertion, displayName)](https://firebase.google.com/docs/reference/js/auth.multifactoruser.md#multifactoruserenroll) | Enrolls a second factor as identified by the [MultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.multifactorassertion.md#multifactorassertion_interface) for the user. |
| [getSession()](https://firebase.google.com/docs/reference/js/auth.multifactoruser.md#multifactorusergetsession)               | Returns the session identifier for a second factor enrollment operation. This is used to identify the user trying to enroll a second factor.                                                 |
| [unenroll(option)](https://firebase.google.com/docs/reference/js/auth.multifactoruser.md#multifactoruserunenroll)             | Unenrolls the specified second factor.                                                                                                                                                       |

## MultiFactorUser.enrolledFactors

Returns a list of the user's enrolled second factors.

**Signature:**  

    readonly enrolledFactors: MultiFactorInfo[];

## MultiFactorUser.enroll()

Enrolls a second factor as identified by the [MultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.multifactorassertion.md#multifactorassertion_interface) for the user.

On resolution, the user tokens are updated to reflect the change in the JWT payload. Accepts an additional display name parameter used to identify the second factor to the end user. Recent re-authentication is required for this operation to succeed. On successful enrollment, existing Firebase sessions (refresh tokens) are revoked. When a new factor is enrolled, an email notification is sent to the user's email.

**Signature:**  

    enroll(assertion: MultiFactorAssertion, displayName?: string | null): Promise<void>;

#### Parameters

|  Parameter  |                                                               Type                                                                |                Description                 |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| assertion   | [MultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.multifactorassertion.md#multifactorassertion_interface) | The multi-factor assertion to enroll with. |
| displayName | string \| null                                                                                                                    | The display name of the second factor.     |

**Returns:**

Promise\<void\>

### Example

    const multiFactorUser = multiFactor(auth.currentUser);
    const multiFactorSession = await multiFactorUser.getSession();

    // Send verification code.
    const phoneAuthProvider = new PhoneAuthProvider(auth);
    const phoneInfoOptions = {
      phoneNumber: phoneNumber,
      session: multiFactorSession
    };
    const verificationId = await phoneAuthProvider.verifyPhoneNumber(phoneInfoOptions, appVerifier);

    // Obtain verification code from user.
    const phoneAuthCredential = PhoneAuthProvider.credential(verificationId, verificationCode);
    const multiFactorAssertion = PhoneMultiFactorGenerator.assertion(phoneAuthCredential);
    await multiFactorUser.enroll(multiFactorAssertion);
    // Second factor enrolled.

## MultiFactorUser.getSession()

Returns the session identifier for a second factor enrollment operation. This is used to identify the user trying to enroll a second factor.

**Signature:**  

    getSession(): Promise<MultiFactorSession>;

**Returns:**

Promise\<[MultiFactorSession](https://firebase.google.com/docs/reference/js/auth.multifactorsession.md#multifactorsession_interface)\>

The promise that resolves with the [MultiFactorSession](https://firebase.google.com/docs/reference/js/auth.multifactorsession.md#multifactorsession_interface).

### Example

    const multiFactorUser = multiFactor(auth.currentUser);
    const multiFactorSession = await multiFactorUser.getSession();

    // Send verification code.
    const phoneAuthProvider = new PhoneAuthProvider(auth);
    const phoneInfoOptions = {
      phoneNumber: phoneNumber,
      session: multiFactorSession
    };
    const verificationId = await phoneAuthProvider.verifyPhoneNumber(phoneInfoOptions, appVerifier);

    // Obtain verification code from user.
    const phoneAuthCredential = PhoneAuthProvider.credential(verificationId, verificationCode);
    const multiFactorAssertion = PhoneMultiFactorGenerator.assertion(phoneAuthCredential);
    await multiFactorUser.enroll(multiFactorAssertion);

## MultiFactorUser.unenroll()

Unenrolls the specified second factor.

To specify the factor to remove, pass a [MultiFactorInfo](https://firebase.google.com/docs/reference/js/auth.multifactorinfo.md#multifactorinfo_interface) object (retrieved from [MultiFactorUser.enrolledFactors](https://firebase.google.com/docs/reference/js/auth.multifactoruser.md#multifactoruserenrolledfactors)) or the factor's UID string. Sessions are not revoked when the account is unenrolled. An email notification is likely to be sent to the user notifying them of the change. Recent re-authentication is required for this operation to succeed. When an existing factor is unenrolled, an email notification is sent to the user's email.

**Signature:**  

    unenroll(option: MultiFactorInfo | string): Promise<void>;

#### Parameters

| Parameter |                                                             Type                                                             |             Description              |
|-----------|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| option    | [MultiFactorInfo](https://firebase.google.com/docs/reference/js/auth.multifactorinfo.md#multifactorinfo_interface) \| string | The multi-factor option to unenroll. |

**Returns:**

Promise\<void\>

- A `Promise` which resolves when the unenroll operation is complete.

### Example

    const multiFactorUser = multiFactor(auth.currentUser);
    // Present user the option to choose which factor to unenroll.
    await multiFactorUser.unenroll(multiFactorUser.enrolledFactors[i])