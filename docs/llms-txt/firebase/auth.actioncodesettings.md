# Source: https://firebase.google.com/docs/reference/js/auth.actioncodesettings.md.txt

# ActionCodeSettings interface

An interface that defines the required continue/state URL with optional Android and iOS bundle identifiers.

**Signature:**  

    export interface ActionCodeSettings 

## Properties

|                                                             Property                                                              |                                  Type                                   |                                                                                                                            Description                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [android](https://firebase.google.com/docs/reference/js/auth.actioncodesettings.md#actioncodesettingsandroid)                     | { installApp?: boolean; minimumVersion?: string; packageName: string; } | Sets the Android package name.                                                                                                                                                                                                                                     |
| [dynamicLinkDomain](https://firebase.google.com/docs/reference/js/auth.actioncodesettings.md#actioncodesettingsdynamiclinkdomain) | string                                                                  | When multiple custom dynamic link domains are defined for a project, specify which one to use when the link is to be opened via a specified mobile app (for example, `example.page.link`).                                                                         |
| [handleCodeInApp](https://firebase.google.com/docs/reference/js/auth.actioncodesettings.md#actioncodesettingshandlecodeinapp)     | boolean                                                                 | When set to true, the action code link will be be sent as a Universal Link or Android App Link and will be opened by the app if installed.                                                                                                                         |
| [iOS](https://firebase.google.com/docs/reference/js/auth.actioncodesettings.md#actioncodesettingsios)                             | { bundleId: string; }                                                   | Sets the iOS bundle ID.                                                                                                                                                                                                                                            |
| [linkDomain](https://firebase.google.com/docs/reference/js/auth.actioncodesettings.md#actioncodesettingslinkdomain)               | string                                                                  | The optional custom Firebase Hosting domain to use when the link is to be opened via a specified mobile app. The domain must be configured in Firebase Hosting and owned by the project. This cannot be a default Hosting domain (`web.app` or `firebaseapp.com`). |
| [url](https://firebase.google.com/docs/reference/js/auth.actioncodesettings.md#actioncodesettingsurl)                             | string                                                                  | Sets the link continue/state URL.                                                                                                                                                                                                                                  |

## ActionCodeSettings.android

Sets the Android package name.

This will try to open the link in an Android app if it is installed.

**Signature:**  

    android?: {
            installApp?: boolean;
            minimumVersion?: string;
            packageName: string;
        };

## ActionCodeSettings.dynamicLinkDomain

> | **Warning:** This API is now obsolete.
>
> Firebase Dynamic Links is deprecated and will be shut down as early as August 2025. Instead, use [ActionCodeSettings.linkDomain](https://firebase.google.com/docs/reference/js/auth.actioncodesettings.md#actioncodesettingslinkdomain) to set a custom domain for mobile links. Learn more in the [Dynamic Links deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq).

When multiple custom dynamic link domains are defined for a project, specify which one to use when the link is to be opened via a specified mobile app (for example, `example.page.link`).

**Signature:**  

    dynamicLinkDomain?: string;

## ActionCodeSettings.handleCodeInApp

When set to true, the action code link will be be sent as a Universal Link or Android App Link and will be opened by the app if installed.

In the false case, the code will be sent to the web widget first and then on continue will redirect to the app if installed.

**Signature:**  

    handleCodeInApp?: boolean;

## ActionCodeSettings.iOS

Sets the iOS bundle ID.

This will try to open the link in an iOS app if it is installed.

**Signature:**  

    iOS?: {
            bundleId: string;
        };

## ActionCodeSettings.linkDomain

The optional custom Firebase Hosting domain to use when the link is to be opened via a specified mobile app. The domain must be configured in Firebase Hosting and owned by the project. This cannot be a default Hosting domain (`web.app` or `firebaseapp.com`).

**Signature:**  

    linkDomain?: string;

## ActionCodeSettings.url

Sets the link continue/state URL.

This has different meanings in different contexts: - When the link is handled in the web action widgets, this is the deep link in the `continueUrl` query parameter. - When the link is handled in the app directly, this is the `continueUrl` query parameter in the deep link of the Dynamic Link or Hosting link.

**Signature:**  

    url: string;