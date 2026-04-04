# Source: https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/integrate-sign-in-with-klarna/openidconnect.md

# OpenIDConnect

## It is possible to integrate directly with Klarna OpenIDConnect.

## 1. Request a new client

Obtain a client with either the `client_secret_basic` or `client_secret_post` authentication methods selected and save the secret. You will need to use it to authenticate requests to the OIDC.

## 2. Choose a right IDP URL

Employ an IDP URL specific to your service's geographic region and run IDP discovery. This step will retrieve the authorization and token endpoints, available scopes and other essential components needed for the standard OAuth flow.

``` markup
EU: https://login.klarna.com
NA: https://login.klarna.com/na/lp/idp
```

To test Sign in with Klarna direct integration on playground, please use the following issuer URLs:

- EU: [<https: login.playground.klarna.com="">](https://login.playground.klarna.com)
- NA: [<https: idp="" login.playground.klarna.com="" lp="" na="">](https://login.playground.klarna.com/na/lp/idp)

## 3. Follow standard OAuth flow

Follow the rest of the OAuth flow according to the standard [<https: datatracker.ietf.org="" doc="" html="" rfc6749="">](https://datatracker.ietf.org/doc/html/rfc6749).</https:></https:></https:>