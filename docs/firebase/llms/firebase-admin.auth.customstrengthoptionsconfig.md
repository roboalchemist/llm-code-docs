# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.customstrengthoptionsconfig.md.txt

# CustomStrengthOptionsConfig interface

Constraints to be enforced on the password policy

**Signature:**  

    export interface CustomStrengthOptionsConfig 

## Properties

|                                                                                       Property                                                                                       |  Type   |                      Description                       |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|--------------------------------------------------------|
| [maxLength](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.customstrengthoptionsconfig.md#customstrengthoptionsconfigmaxlength)                           | number  | Maximum password length. No default max length         |
| [minLength](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.customstrengthoptionsconfig.md#customstrengthoptionsconfigminlength)                           | number  | Minimum password length. Valid values are from 6 to 30 |
| [requireLowercase](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.customstrengthoptionsconfig.md#customstrengthoptionsconfigrequirelowercase)             | boolean | The password must contain a lower case character       |
| [requireNonAlphanumeric](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.customstrengthoptionsconfig.md#customstrengthoptionsconfigrequirenonalphanumeric) | boolean | The password must contain a non-alphanumeric character |
| [requireNumeric](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.customstrengthoptionsconfig.md#customstrengthoptionsconfigrequirenumeric)                 | boolean | The password must contain a number                     |
| [requireUppercase](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.customstrengthoptionsconfig.md#customstrengthoptionsconfigrequireuppercase)             | boolean | The password must contain an upper case character      |

## CustomStrengthOptionsConfig.maxLength

Maximum password length. No default max length

**Signature:**  

    maxLength?: number;

## CustomStrengthOptionsConfig.minLength

Minimum password length. Valid values are from 6 to 30

**Signature:**  

    minLength?: number;

## CustomStrengthOptionsConfig.requireLowercase

The password must contain a lower case character

**Signature:**  

    requireLowercase?: boolean;

## CustomStrengthOptionsConfig.requireNonAlphanumeric

The password must contain a non-alphanumeric character

**Signature:**  

    requireNonAlphanumeric?: boolean;

## CustomStrengthOptionsConfig.requireNumeric

The password must contain a number

**Signature:**  

    requireNumeric?: boolean;

## CustomStrengthOptionsConfig.requireUppercase

The password must contain an upper case character

**Signature:**  

    requireUppercase?: boolean;