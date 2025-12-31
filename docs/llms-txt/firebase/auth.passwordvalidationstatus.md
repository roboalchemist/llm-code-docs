# Source: https://firebase.google.com/docs/reference/js/auth.passwordvalidationstatus.md.txt

# PasswordValidationStatus interface

A structure indicating which password policy requirements were met or violated and what the requirements are.

**Signature:**  

    export interface PasswordValidationStatus 

## Properties

|                                                                                  Property                                                                                   |                                                      Type                                                       |                                        Description                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [containsLowercaseLetter](https://firebase.google.com/docs/reference/js/auth.passwordvalidationstatus.md#passwordvalidationstatuscontainslowercaseletter)                   | boolean                                                                                                         | Whether the password contains a lowercase letter, or undefined if not required.           |
| [containsNonAlphanumericCharacter](https://firebase.google.com/docs/reference/js/auth.passwordvalidationstatus.md#passwordvalidationstatuscontainsnonalphanumericcharacter) | boolean                                                                                                         | Whether the password contains a non-alphanumeric character, or undefined if not required. |
| [containsNumericCharacter](https://firebase.google.com/docs/reference/js/auth.passwordvalidationstatus.md#passwordvalidationstatuscontainsnumericcharacter)                 | boolean                                                                                                         | Whether the password contains a numeric character, or undefined if not required.          |
| [containsUppercaseLetter](https://firebase.google.com/docs/reference/js/auth.passwordvalidationstatus.md#passwordvalidationstatuscontainsuppercaseletter)                   | boolean                                                                                                         | Whether the password contains an uppercase letter, or undefined if not required.          |
| [isValid](https://firebase.google.com/docs/reference/js/auth.passwordvalidationstatus.md#passwordvalidationstatusisvalid)                                                   | boolean                                                                                                         | Whether the password meets all requirements.                                              |
| [meetsMaxPasswordLength](https://firebase.google.com/docs/reference/js/auth.passwordvalidationstatus.md#passwordvalidationstatusmeetsmaxpasswordlength)                     | boolean                                                                                                         | Whether the password meets the maximum password length, or undefined if not required.     |
| [meetsMinPasswordLength](https://firebase.google.com/docs/reference/js/auth.passwordvalidationstatus.md#passwordvalidationstatusmeetsminpasswordlength)                     | boolean                                                                                                         | Whether the password meets the minimum password length, or undefined if not required.     |
| [passwordPolicy](https://firebase.google.com/docs/reference/js/auth.passwordvalidationstatus.md#passwordvalidationstatuspasswordpolicy)                                     | [PasswordPolicy](https://firebase.google.com/docs/reference/js/auth.passwordpolicy.md#passwordpolicy_interface) | The policy used to validate the password.                                                 |

## PasswordValidationStatus.containsLowercaseLetter

Whether the password contains a lowercase letter, or undefined if not required.

**Signature:**  

    readonly containsLowercaseLetter?: boolean;

## PasswordValidationStatus.containsNonAlphanumericCharacter

Whether the password contains a non-alphanumeric character, or undefined if not required.

**Signature:**  

    readonly containsNonAlphanumericCharacter?: boolean;

## PasswordValidationStatus.containsNumericCharacter

Whether the password contains a numeric character, or undefined if not required.

**Signature:**  

    readonly containsNumericCharacter?: boolean;

## PasswordValidationStatus.containsUppercaseLetter

Whether the password contains an uppercase letter, or undefined if not required.

**Signature:**  

    readonly containsUppercaseLetter?: boolean;

## PasswordValidationStatus.isValid

Whether the password meets all requirements.

**Signature:**  

    readonly isValid: boolean;

## PasswordValidationStatus.meetsMaxPasswordLength

Whether the password meets the maximum password length, or undefined if not required.

**Signature:**  

    readonly meetsMaxPasswordLength?: boolean;

## PasswordValidationStatus.meetsMinPasswordLength

Whether the password meets the minimum password length, or undefined if not required.

**Signature:**  

    readonly meetsMinPasswordLength?: boolean;

## PasswordValidationStatus.passwordPolicy

The policy used to validate the password.

**Signature:**  

    readonly passwordPolicy: PasswordPolicy;