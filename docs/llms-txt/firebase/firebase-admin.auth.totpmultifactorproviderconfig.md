# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.totpmultifactorproviderconfig.md.txt

# TotpMultiFactorProviderConfig interface

Interface representing configuration settings for TOTP second factor auth.

**Signature:**  

    export interface TotpMultiFactorProviderConfig 

## Properties

|                                                                                    Property                                                                                    |  Type  |                                                Description                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------|
| [adjacentIntervals](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.totpmultifactorproviderconfig.md#totpmultifactorproviderconfigadjacentintervals) | number | The allowed number of adjacent intervals that will be used for verification to compensate for clock skew. |

## TotpMultiFactorProviderConfig.adjacentIntervals

The allowed number of adjacent intervals that will be used for verification to compensate for clock skew.

**Signature:**  

    adjacentIntervals?: number;