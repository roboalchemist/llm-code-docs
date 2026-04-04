# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.emailsigninproviderconfig.md.txt

# EmailSignInProviderConfig interface

The email sign in provider configuration.

**Signature:**  

    export interface EmailSignInProviderConfig 

## Properties

|                                                                               Property                                                                               |  Type   |                                                                Description                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------|
| [enabled](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.emailsigninproviderconfig.md#emailsigninproviderconfigenabled)                   | boolean | Whether email provider is enabled.                                                                                                         |
| [passwordRequired](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.emailsigninproviderconfig.md#emailsigninproviderconfigpasswordrequired) | boolean | Whether password is required for email sign-in. When not required, email sign-in can be performed with password or via email link sign-in. |

## EmailSignInProviderConfig.enabled

Whether email provider is enabled.

**Signature:**  

    enabled: boolean;

## EmailSignInProviderConfig.passwordRequired

Whether password is required for email sign-in. When not required, email sign-in can be performed with password or via email link sign-in.

**Signature:**  

    passwordRequired?: boolean;