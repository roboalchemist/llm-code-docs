# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.allowlistonly.md.txt

# AllowlistOnly interface

Defines a policy of only allowing regions by explicitly adding them to an allowlist.

**Signature:**  

    export interface AllowlistOnly 

## Properties

|                                                                 Property                                                                 |    Type    |                                                                                                       Description                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [allowedRegions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.allowlistonly.md#allowlistonlyallowedregions) | string\[\] | Two letter unicode region codes to allow as defined by https://cldr.unicode.org/ The full list of these region codes is here: https://github.com/unicode-cldr/cldr-localenames-full/blob/master/main/en/territories.json |

## AllowlistOnly.allowedRegions

Two letter unicode region codes to allow as defined by https://cldr.unicode.org/ The full list of these region codes is here: https://github.com/unicode-cldr/cldr-localenames-full/blob/master/main/en/territories.json

**Signature:**  

    allowedRegions: string[];