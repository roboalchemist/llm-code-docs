# Source: https://docs.redwoodjs.com/docs/auth/azure

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Authentication](/docs/authentication)
-   [Azure]

[Version: 8.8]

On this page

<div>

# Azure Active Directory Authentication

</div>

To get started, run the setup command:

``` 
yarn rw setup auth azure-active-directory
```

This installs all the packages, writes all the files, and makes all the code modifications you need. For a detailed explanation of all the api- and web-side changes that aren\'t exclusive to Azure, see the top-level [Authentication](/docs/authentication) doc. For now, let\'s focus on Azure\'s side of things.

Follow the steps in [Single-page application: App registration](https://docs.microsoft.com/en-us/azure/active-directory/develop/scenario-spa-app-registration). After registering your app, you\'ll be redirected to its \"Overview\" section. We\'re interested in two credentials here, \"Application (client) ID\" and \"Directory (tenant) ID\". Go ahead and copy \"Application (client) ID\" to your `.env` file as `AZURE_ACTIVE_DIRECTORY_CLIENT_ID`. But \"Directory (tenant) ID\" needs a bit more explanation.

Azure has an option called \"Authority\". It\'s a URL that specifies a directory that MSAL (Microsoft Authentication Library) can request tokens from. You can read more about it [here](https://docs.microsoft.com/en-us/azure/active-directory/develop/msal-client-application-configuration#authority), but to cut to the chase, you probably want `https://login.microsoftonline.com/$` as your Authority, where `tenantId` is \"Directory (tenant) ID\".

After substituting your app\'s \"Directory (tenant) ID\" in the URL, add it to your `.env` file as `AZURE_ACTIVE_DIRECTORY_AUTHORITY`. All together now:

.env

``` 
AZURE_ACTIVE_DIRECTORY_CLIENT_ID="..."
# Where `tenantId` is your app's "Directory (tenant) ID"
AZURE_ACTIVE_DIRECTORY_AUTHORITY="https://login.microsoftonline.com/$"
```

Ok, back to [Single-page application: App registration](https://docs.microsoft.com/en-us/azure/active-directory/develop/scenario-spa-app-registration). At the end, it says\...

> Next, configure the app registration with a Redirect URI to specify where the Microsoft identity platform should redirect the client along with any security tokens. Use the steps appropriate for the version of MSAL.js you\'re using in your application:
>
> -   MSAL.js 2.0 with auth code flow (recommended)
> -   MSAL.js 1.0 with implicit flow

Redwood uses [MSAL.js 2.0 with auth code flow](https://learn.microsoft.com/en-us/azure/active-directory/develop/scenario-spa-app-registration#redirect-uri-msaljs-20-with-auth-code-flow), so follow the steps there next. When it asks you for a Redirect URI, enter `http://localhost:8910` and `http://localhost:8910/login`, and copy these into your `.env` file as `AZURE_ACTIVE_DIRECTORY_REDIRECT_URI` and `AZURE_ACTIVE_DIRECTORY_LOGOUT_REDIRECT_URI`:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]Can\'t add multiple URI\'s?

Configure one, then you\'ll be able to configure another.

.env

``` 
AZURE_ACTIVE_DIRECTORY_CLIENT_ID="..."
# Where `tenantId` is your app's "Directory (tenant) ID"
AZURE_ACTIVE_DIRECTORY_AUTHORITY="https://login.microsoftonline.com/$"
AZURE_ACTIVE_DIRECTORY_REDIRECT_URI="http://localhost:8910"
AZURE_ACTIVE_DIRECTORY_LOGOUT_REDIRECT_URI="http://localhost:8910/login"
```

That\'s it for .env vars. Don\'t forget to include them in the `includeEnvironmentVariables` array in `redwood.toml`:

redwood.toml

``` 
[web]
  # ...
  includeEnvironmentVariables = [
    "AZURE_ACTIVE_DIRECTORY_CLIENT_ID",
    "AZURE_ACTIVE_DIRECTORY_AUTHORITY",
    "AZURE_ACTIVE_DIRECTORY_REDIRECT_URI",
    "AZURE_ACTIVE_DIRECTORY_LOGOUT_REDIRECT_URI",
  ]
```

Now let\'s make sure everything works: if this is a brand new project, generate a home page. There we\'ll try to sign up by destructuring `signUp` from the `useAuth` hook (import that from `'src/auth'`). We\'ll also destructure and display `isAuthenticated` to see if it worked:

``` 
yarn rw g page home /
```

web/src/pages/HomePage.tsx

``` 
import  from 'src/auth'

const HomePage = () =>  = useAuth()

  return (
    <>
      

      <p>)}</p>
      <button onClick=>Sign Up</button>
    </>
  )
}
```

## Roles[​](#roles "Direct link to Roles") 

To add roles exposed via the `roles` claim, follow [Add app roles to your application and receive them in the token](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-add-app-roles-in-azure-ad-apps).

## `logIn` Options[​](#login-options "Direct link to login-options") 

`options` in `logIn(options?)` is of type [RedirectRequest](https://azuread.github.io/microsoft-authentication-library-for-js/ref/types/_azure_msal_browser.RedirectRequest.html) and is a good place to pass in optional [scopes](https://docs.microsoft.com/en-us/graph/permissions-reference#user-permissions) to be authorized. By default, MSAL sets `scopes` to [/.default](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent#the-default-scope) which is built in for every application that refers to the static list of permissions configured on the application registration. Furthermore, MSAL will add `openid`, `profile` and `offline_access` to all requests. In the example below we explicit include `User.Read.All` in the login scope.

``` 
await logIn()
```

See [loginRedirect](https://azuread.github.io/microsoft-authentication-library-for-js/ref/classes/_azure_msal_browser.PublicClientApplication.html#loginRedirect), [PublicClientApplication](https://azuread.github.io/microsoft-authentication-library-for-js/ref/classes/_azure_msal_browser.PublicClientApplication.html) class and [Scopes Behavior](https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/msal-lts/lib/msal-core/docs/scopes.md#scopes-behavior) for more documentation.

## `getToken` Options[​](#gettoken-options "Direct link to gettoken-options") 

`options` in `getToken(options?)` is of type [RedirectRequest](https://azuread.github.io/microsoft-authentication-library-for-js/ref/types/_azure_msal_browser.RedirectRequest.html). By default, `getToken` will be called with scope `['openid', 'profile']`. Since Azure Active Directory applies [incremental consent](https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-browser/docs/resources-and-scopes.md#dynamic-scopes-and-incremental-consent), we can extend the permissions from the login example by including another scope, for example `Mail.Read`:

``` 
await getToken()
```

See [acquireTokenSilent](https://azuread.github.io/microsoft-authentication-library-for-js/ref/classes/_azure_msal_browser.PublicClientApplication.html#acquireTokenSilent), [Resources and Scopes](https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-browser/docs/resources-and-scopes.md#resources-and-scopes) or [full class documentation](https://pub.dev/documentation/msal_js/latest/msal_js/PublicClientApplication-class.html#constructors) for more.

## Azure Active Directory B2C-specific configuration[​](#azure-active-directory-b2c-specific-configuration "Direct link to Azure Active Directory B2C-specific configuration") 

You can design your own auth flow with Azure Active Directory B2C using [hosted user flows](https://docs.microsoft.com/en-us/azure/active-directory-b2c/add-sign-up-and-sign-in-policy?pivots=b2c-user-flow). Using it requires two extra settings.

#### Update the .env file:[​](#update-the-env-file "Direct link to Update the .env file:") 

.env

``` 
AZURE_ACTIVE_DIRECTORY_AUTHORITY=https://.b2clogin.com/}.onmicrosoft.com/}
AZURE_ACTIVE_DIRECTORY_JWT_ISSUER=https://}.b2clogin.com/}/v2.0/
AZURE_ACTIVE_DIRECTORY_KNOWN_AUTHORITY=https://}.b2clogin.com
```

Here\'s an example:

.env.example

``` 
AZURE_ACTIVE_DIRECTORY_AUTHORITY=https://rwauthtestb2c.b2clogin.com/rwauthtestb2c.onmicrosoft.com/B2C_1_signupsignin1
AZURE_ACTIVE_DIRECTORY_JWT_ISSUER=https://rwauthtestb2c.b2clogin.com/775527ef-8a37-4307-8b3d-cc311f58d922/v2.0/
AZURE_ACTIVE_DIRECTORY_KNOWN_AUTHORITY=https://rwauthtestb2c.b2clogin.com
```

And don\'t forget to add `AZURE_ACTIVE_DIRECTORY_KNOWN_AUTHORITY` to the `includeEnvironmentVariables` array in `redwood.toml`. (`AZURE_ACTIVE_DIRECTORY_JWT_ISSUER` is only used on the API side. But more importantly, it\'s sensitive---do *not* include it in the web side.)

#### Update `activeDirectoryClient` instance[​](#update-activedirectoryclient-instance "Direct link to update-activedirectoryclient-instance") 

This lets the MSAL web-side client know about our new B2C authority:

web/src/auth.

``` 
const azureActiveDirectoryClient = new PublicClientApplication(,
})
```

Now you can call the `logIn` and `logOut` functions from `useAuth()`, and everything should just work.

Here\'s a few more links to relevant documentation for reference:

-   [Overview of tokens in Azure Active Directory B2C](https://docs.microsoft.com/en-us/azure/active-directory-b2c/tokens-overview)
-   [Working with MSAL.js and Azure AD B2C](https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-browser/docs/working-with-b2c.md)

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/auth/azure.md)