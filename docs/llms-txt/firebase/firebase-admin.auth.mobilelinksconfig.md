# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.mobilelinksconfig.md.txt

# MobileLinksConfig interface

Configuration for settings related to univeral links (iOS) and app links (Android).

**Signature:**  

    export interface MobileLinksConfig 

## Properties

|                                                             Property                                                             |                                                        Type                                                         |                                 Description                                 |
|----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [domain](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.mobilelinksconfig.md#mobilelinksconfigdomain) | [MobileLinksDomain](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#mobilelinksdomain) | Use Firebase Hosting or dynamic link domain as the out-of-band code domain. |

## MobileLinksConfig.domain

Use Firebase Hosting or dynamic link domain as the out-of-band code domain.

**Signature:**  

    domain?: MobileLinksDomain;