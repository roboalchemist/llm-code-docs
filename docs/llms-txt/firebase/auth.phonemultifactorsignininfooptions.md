# Source: https://firebase.google.com/docs/reference/js/auth.phonemultifactorsignininfooptions.md.txt

# PhoneMultiFactorSignInInfoOptions interface

Options used for signing in with a second factor.

**Signature:**  

    export interface PhoneMultiFactorSignInInfoOptions 

## Properties

|                                                                          Property                                                                           |                                                            Type                                                             |                                                                                                                                                          Description                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [multiFactorHint](https://firebase.google.com/docs/reference/js/auth.phonemultifactorsignininfooptions.md#phonemultifactorsignininfooptionsmultifactorhint) | [MultiFactorInfo](https://firebase.google.com/docs/reference/js/auth.multifactorinfo.md#multifactorinfo_interface)          | The [MultiFactorInfo](https://firebase.google.com/docs/reference/js/auth.multifactorinfo.md#multifactorinfo_interface) obtained via [MultiFactorResolver.hints](https://firebase.google.com/docs/reference/js/auth.multifactorresolver.md#multifactorresolverhints).One of `multiFactorHint` or `multiFactorUid` is required. |
| [multiFactorUid](https://firebase.google.com/docs/reference/js/auth.phonemultifactorsignininfooptions.md#phonemultifactorsignininfooptionsmultifactoruid)   | string                                                                                                                      | The uid of the second factor.One of `multiFactorHint` or `multiFactorUid` is required.                                                                                                                                                                                                                                        |
| [session](https://firebase.google.com/docs/reference/js/auth.phonemultifactorsignininfooptions.md#phonemultifactorsignininfooptionssession)                 | [MultiFactorSession](https://firebase.google.com/docs/reference/js/auth.multifactorsession.md#multifactorsession_interface) | The [MultiFactorSession](https://firebase.google.com/docs/reference/js/auth.multifactorsession.md#multifactorsession_interface) obtained via [MultiFactorResolver.session](https://firebase.google.com/docs/reference/js/auth.multifactorresolver.md#multifactorresolversession).                                             |

## PhoneMultiFactorSignInInfoOptions.multiFactorHint

The [MultiFactorInfo](https://firebase.google.com/docs/reference/js/auth.multifactorinfo.md#multifactorinfo_interface) obtained via [MultiFactorResolver.hints](https://firebase.google.com/docs/reference/js/auth.multifactorresolver.md#multifactorresolverhints).

One of `multiFactorHint` or `multiFactorUid` is required.

**Signature:**  

    multiFactorHint?: MultiFactorInfo;

## PhoneMultiFactorSignInInfoOptions.multiFactorUid

The uid of the second factor.

One of `multiFactorHint` or `multiFactorUid` is required.

**Signature:**  

    multiFactorUid?: string;

## PhoneMultiFactorSignInInfoOptions.session

The [MultiFactorSession](https://firebase.google.com/docs/reference/js/auth.multifactorsession.md#multifactorsession_interface) obtained via [MultiFactorResolver.session](https://firebase.google.com/docs/reference/js/auth.multifactorresolver.md#multifactorresolversession).

**Signature:**  

    session: MultiFactorSession;