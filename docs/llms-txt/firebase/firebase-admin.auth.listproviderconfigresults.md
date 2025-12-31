# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.listproviderconfigresults.md.txt

# ListProviderConfigResults interface

The response interface for listing provider configs. This is only available when listing all identity providers' configurations via [BaseAuth.listProviderConfigs()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthlistproviderconfigs).

**Signature:**  

    export interface ListProviderConfigResults 

## Properties

|                                                                              Property                                                                              |                                                           Type                                                            |                            Description                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| [pageToken](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.listproviderconfigresults.md#listproviderconfigresultspagetoken)             | string                                                                                                                    | The next page token, if available.                                |
| [providerConfigs](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.listproviderconfigresults.md#listproviderconfigresultsproviderconfigs) | [AuthProviderConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#authproviderconfig)\[\] | The list of providers for the specified type in the current page. |

## ListProviderConfigResults.pageToken

The next page token, if available.

**Signature:**  

    pageToken?: string;

## ListProviderConfigResults.providerConfigs

The list of providers for the specified type in the current page.

**Signature:**  

    providerConfigs: AuthProviderConfig[];