# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.allowbydefault.md.txt

# AllowByDefault interface

Defines a policy of allowing every region by default and adding disallowed regions to a disallow list.

**Signature:**  

    export interface AllowByDefault 

## Properties

|                                                                     Property                                                                     |    Type    |                                                                                                         Description                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [disallowedRegions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.allowbydefault.md#allowbydefaultdisallowedregions) | string\[\] | Two letter unicode region codes to disallow as defined by https://cldr.unicode.org/ The full list of these region codes is here: https://github.com/unicode-cldr/cldr-localenames-full/blob/master/main/en/territories.json |

## AllowByDefault.disallowedRegions

Two letter unicode region codes to disallow as defined by https://cldr.unicode.org/ The full list of these region codes is here: https://github.com/unicode-cldr/cldr-localenames-full/blob/master/main/en/territories.json

**Signature:**  

    disallowedRegions: string[];