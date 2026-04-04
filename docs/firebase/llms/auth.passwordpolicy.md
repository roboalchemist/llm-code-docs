# Source: https://firebase.google.com/docs/reference/js/auth.passwordpolicy.md.txt

# PasswordPolicy interface

A structure specifying password policy requirements.

**Signature:**  

    export interface PasswordPolicy 

## Properties

|                                                                        Property                                                                         |                                                                                                                                  Type                                                                                                                                   |                                Description                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| [allowedNonAlphanumericCharacters](https://firebase.google.com/docs/reference/js/auth.passwordpolicy.md#passwordpolicyallowednonalphanumericcharacters) | string                                                                                                                                                                                                                                                                  | List of characters that are considered non-alphanumeric during validation. |
| [customStrengthOptions](https://firebase.google.com/docs/reference/js/auth.passwordpolicy.md#passwordpolicycustomstrengthoptions)                       | { readonly minPasswordLength?: number; readonly maxPasswordLength?: number; readonly containsLowercaseLetter?: boolean; readonly containsUppercaseLetter?: boolean; readonly containsNumericCharacter?: boolean; readonly containsNonAlphanumericCharacter?: boolean; } | Requirements enforced by this password policy.                             |
| [enforcementState](https://firebase.google.com/docs/reference/js/auth.passwordpolicy.md#passwordpolicyenforcementstate)                                 | string                                                                                                                                                                                                                                                                  | The enforcement state of the policy. Can be 'OFF' or 'ENFORCE'.            |
| [forceUpgradeOnSignin](https://firebase.google.com/docs/reference/js/auth.passwordpolicy.md#passwordpolicyforceupgradeonsignin)                         | boolean                                                                                                                                                                                                                                                                 | Whether existing passwords must meet the policy.                           |

## PasswordPolicy.allowedNonAlphanumericCharacters

List of characters that are considered non-alphanumeric during validation.

**Signature:**  

    readonly allowedNonAlphanumericCharacters: string;

## PasswordPolicy.customStrengthOptions

Requirements enforced by this password policy.

**Signature:**  

    readonly customStrengthOptions: {
            readonly minPasswordLength?: number;
            readonly maxPasswordLength?: number;
            readonly containsLowercaseLetter?: boolean;
            readonly containsUppercaseLetter?: boolean;
            readonly containsNumericCharacter?: boolean;
            readonly containsNonAlphanumericCharacter?: boolean;
        };

## PasswordPolicy.enforcementState

The enforcement state of the policy. Can be 'OFF' or 'ENFORCE'.

**Signature:**  

    readonly enforcementState: string;

## PasswordPolicy.forceUpgradeOnSignin

Whether existing passwords must meet the policy.

**Signature:**  

    readonly forceUpgradeOnSignin: boolean;