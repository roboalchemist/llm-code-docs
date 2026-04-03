# Source: https://firebase.google.com/docs/reference/js/auth.confirmationresult.md.txt

# ConfirmationResult interface

A result from a phone number sign-in, link, or reauthenticate call.

**Signature:**  

    export interface ConfirmationResult 

## Properties

|                                                          Property                                                           |  Type  |                         Description                          |
|-----------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------|
| [verificationId](https://firebase.google.com/docs/reference/js/auth.confirmationresult.md#confirmationresultverificationid) | string | The phone number authentication operation's verification ID. |

## Methods

|                                                             Method                                                              |                         Description                         |
|---------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| [confirm(verificationCode)](https://firebase.google.com/docs/reference/js/auth.confirmationresult.md#confirmationresultconfirm) | Finishes a phone number sign-in, link, or reauthentication. |

## ConfirmationResult.verificationId

The phone number authentication operation's verification ID.

This can be used along with the verification code to initialize a [PhoneAuthCredential](https://firebase.google.com/docs/reference/js/auth.phoneauthcredential.md#phoneauthcredential_class).

**Signature:**  

    readonly verificationId: string;

## ConfirmationResult.confirm()

Finishes a phone number sign-in, link, or reauthentication.

**Signature:**  

    confirm(verificationCode: string): Promise<UserCredential>;

#### Parameters

|    Parameter     |  Type  |                     Description                     |
|------------------|--------|-----------------------------------------------------|
| verificationCode | string | The code that was sent to the user's mobile device. |

**Returns:**

Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface)\>

### Example

    const confirmationResult = await signInWithPhoneNumber(auth, phoneNumber, applicationVerifier);
    // Obtain verificationCode from the user.
    const userCredential = await confirmationResult.confirm(verificationCode);