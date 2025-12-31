# Source: https://firebase.google.com/docs/reference/js/auth.phonemultifactorenrollinfooptions.md.txt

# PhoneMultiFactorEnrollInfoOptions interface

Options used for enrolling a second factor.

**Signature:**  

    export interface PhoneMultiFactorEnrollInfoOptions 

## Properties

|                                                                      Property                                                                       |                                                            Type                                                             |                                                                                                                                  Description                                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [phoneNumber](https://firebase.google.com/docs/reference/js/auth.phonemultifactorenrollinfooptions.md#phonemultifactorenrollinfooptionsphonenumber) | string                                                                                                                      | Phone number to send a verification code to.                                                                                                                                                                                                                                  |
| [session](https://firebase.google.com/docs/reference/js/auth.phonemultifactorenrollinfooptions.md#phonemultifactorenrollinfooptionssession)         | [MultiFactorSession](https://firebase.google.com/docs/reference/js/auth.multifactorsession.md#multifactorsession_interface) | The [MultiFactorSession](https://firebase.google.com/docs/reference/js/auth.multifactorsession.md#multifactorsession_interface) obtained via [MultiFactorUser.getSession()](https://firebase.google.com/docs/reference/js/auth.multifactoruser.md#multifactorusergetsession). |

## PhoneMultiFactorEnrollInfoOptions.phoneNumber

Phone number to send a verification code to.

**Signature:**  

    phoneNumber: string;

## PhoneMultiFactorEnrollInfoOptions.session

The [MultiFactorSession](https://firebase.google.com/docs/reference/js/auth.multifactorsession.md#multifactorsession_interface) obtained via [MultiFactorUser.getSession()](https://firebase.google.com/docs/reference/js/auth.multifactoruser.md#multifactorusergetsession).

**Signature:**  

    session: MultiFactorSession;