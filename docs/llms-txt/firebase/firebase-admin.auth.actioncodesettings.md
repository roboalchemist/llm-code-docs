# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.actioncodesettings.md.txt

# ActionCodeSettings interface

This is the interface that defines the required continue/state URL with optional Android and iOS bundle identifiers.

**Signature:**  

    export interface ActionCodeSettings 

## Properties

|                                                                         Property                                                                         |                                  Type                                   |                                                                                                                                                                                                                                                                    Description                                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [android](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.actioncodesettings.md#actioncodesettingsandroid)                     | { packageName: string; installApp?: boolean; minimumVersion?: string; } | Defines the Android package name. This will try to open the link in an android app if it is installed. If `installApp` is passed, it specifies whether to install the Android app if the device supports it and the app is not already installed. If this field is provided without a `packageName`, an error is thrown explaining that the `packageName` must be provided in conjunction with this field. If `minimumVersion` is specified, and an older version of the app is installed, the user is taken to the Play Store to upgrade the app. |
| [dynamicLinkDomain](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.actioncodesettings.md#actioncodesettingsdynamiclinkdomain) | string                                                                  | Defines the dynamic link domain to use for the current link if it is to be opened using Firebase Dynamic Links, as multiple dynamic link domains can be configured per project. This field provides the ability to explicitly choose configured per project. This fields provides the ability explicitly choose one. If none is provided, the oldest domain is used by default.                                                                                                                                                                    |
| [handleCodeInApp](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.actioncodesettings.md#actioncodesettingshandlecodeinapp)     | boolean                                                                 | Whether to open the link via a mobile app or a browser. The default is false. When set to true, the action code link is sent as a Universal Link or Android App Link and is opened by the app if installed. In the false case, the code is sent to the web widget first and then redirects to the app if installed.                                                                                                                                                                                                                                |
| [iOS](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.actioncodesettings.md#actioncodesettingsios)                             | { bundleId: string; }                                                   | Defines the iOS bundle ID. This will try to open the link in an iOS app if it is installed.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [linkDomain](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.actioncodesettings.md#actioncodesettingslinkdomain)               | string                                                                  | Defines the custom Firebase Hosting domain to use when the link is to be opened via a specified mobile app, This is a replacement of Firebase Dynamic Link. If none is provided, a default hosting domain will be used (for example, `example.firebaseapp.com`)                                                                                                                                                                                                                                                                                    |
| [url](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.actioncodesettings.md#actioncodesettingsurl)                             | string                                                                  | Defines the link continue/state URL, which has different meanings in different contexts: - When the link is handled in the web action widgets, this is the deep link in the `continueUrl` query parameter. - When the link is handled in the app directly, this is the `continueUrl` query parameter in the deep link of the Dynamic Link.                                                                                                                                                                                                         |

## ActionCodeSettings.android

Defines the Android package name. This will try to open the link in an android app if it is installed. If `installApp` is passed, it specifies whether to install the Android app if the device supports it and the app is not already installed. If this field is provided without a `packageName`, an error is thrown explaining that the `packageName` must be provided in conjunction with this field. If `minimumVersion` is specified, and an older version of the app is installed, the user is taken to the Play Store to upgrade the app.

**Signature:**  

    android?: {
            packageName: string;
            installApp?: boolean;
            minimumVersion?: string;
        };

## ActionCodeSettings.dynamicLinkDomain

> | **Warning:** This API is now obsolete.
>
> use `linkDomain` instead

Defines the dynamic link domain to use for the current link if it is to be opened using Firebase Dynamic Links, as multiple dynamic link domains can be configured per project. This field provides the ability to explicitly choose configured per project. This fields provides the ability explicitly choose one. If none is provided, the oldest domain is used by default.

**Signature:**  

    dynamicLinkDomain?: string;

## ActionCodeSettings.handleCodeInApp

Whether to open the link via a mobile app or a browser. The default is false. When set to true, the action code link is sent as a Universal Link or Android App Link and is opened by the app if installed. In the false case, the code is sent to the web widget first and then redirects to the app if installed.

**Signature:**  

    handleCodeInApp?: boolean;

## ActionCodeSettings.iOS

Defines the iOS bundle ID. This will try to open the link in an iOS app if it is installed.

**Signature:**  

    iOS?: {
            bundleId: string;
        };

## ActionCodeSettings.linkDomain

Defines the custom Firebase Hosting domain to use when the link is to be opened via a specified mobile app, This is a replacement of Firebase Dynamic Link. If none is provided, a default hosting domain will be used (for example, `example.firebaseapp.com`)

**Signature:**  

    linkDomain?: string;

## ActionCodeSettings.url

Defines the link continue/state URL, which has different meanings in different contexts:

- When the link is handled in the web action widgets, this is the deep link in the `continueUrl` query parameter.
- When the link is handled in the app directly, this is the `continueUrl` query parameter in the deep link of the Dynamic Link.

<br />

**Signature:**  

    url: string;