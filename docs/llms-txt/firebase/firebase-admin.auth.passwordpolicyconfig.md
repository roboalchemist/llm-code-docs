# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.passwordpolicyconfig.md.txt

# PasswordPolicyConfig interface

A password policy configuration for a project or tenant

**Signature:**  

    export interface PasswordPolicyConfig 

## Properties

|                                                                              Property                                                                              |                                                                                     Type                                                                                      |                         Description                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| [constraints](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.passwordpolicyconfig.md#passwordpolicyconfigconstraints)                   | [CustomStrengthOptionsConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.customstrengthoptionsconfig.md#customstrengthoptionsconfig_interface) | The constraints that make up the password strength policy    |
| [enforcementState](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.passwordpolicyconfig.md#passwordpolicyconfigenforcementstate)         | [PasswordPolicyEnforcementState](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#passwordpolicyenforcementstate)                                 | Enforcement state of the password policy                     |
| [forceUpgradeOnSignin](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.passwordpolicyconfig.md#passwordpolicyconfigforceupgradeonsignin) | boolean                                                                                                                                                                       | Require users to have a policy-compliant password to sign in |

## PasswordPolicyConfig.constraints

The constraints that make up the password strength policy

**Signature:**  

    constraints?: CustomStrengthOptionsConfig;

## PasswordPolicyConfig.enforcementState

Enforcement state of the password policy

**Signature:**  

    enforcementState?: PasswordPolicyEnforcementState;

## PasswordPolicyConfig.forceUpgradeOnSignin

Require users to have a policy-compliant password to sign in

**Signature:**  

    forceUpgradeOnSignin?: boolean;