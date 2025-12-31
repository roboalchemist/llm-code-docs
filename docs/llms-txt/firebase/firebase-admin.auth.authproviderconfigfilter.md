# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.authproviderconfigfilter.md.txt

# AuthProviderConfigFilter interface

The filter interface used for listing provider configurations. This is used when specifying how to list configured identity providers via [BaseAuth.listProviderConfigs()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthlistproviderconfigs).

**Signature:**  

    export interface AuthProviderConfigFilter 

## Properties

|                                                                        Property                                                                        |       Type       |                                                                                 Description                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [maxResults](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.authproviderconfigfilter.md#authproviderconfigfiltermaxresults) | number           | The maximum number of results to return per page. The default and maximum is 100.                                                                                            |
| [pageToken](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.authproviderconfigfilter.md#authproviderconfigfilterpagetoken)   | string           | The next page token. When not specified, the lookup starts from the beginning of the list.                                                                                   |
| [type](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.authproviderconfigfilter.md#authproviderconfigfiltertype)             | 'saml' \| 'oidc' | The Auth provider configuration filter. This can be either `saml` or `oidc`. The former is used to look up SAML providers only, while the latter is used for OIDC providers. |

## AuthProviderConfigFilter.maxResults

The maximum number of results to return per page. The default and maximum is 100.

**Signature:**  

    maxResults?: number;

## AuthProviderConfigFilter.pageToken

The next page token. When not specified, the lookup starts from the beginning of the list.

**Signature:**  

    pageToken?: string;

## AuthProviderConfigFilter.type

The Auth provider configuration filter. This can be either `saml` or `oidc`. The former is used to look up SAML providers only, while the latter is used for OIDC providers.

**Signature:**  

    type: 'saml' | 'oidc';