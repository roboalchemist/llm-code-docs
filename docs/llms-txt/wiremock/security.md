# Source: https://docs.wiremock.io/security/security.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# API Security Overview

> WireMock Cloud's simulation and admin API security and how to work with it

WireMock Cloud supports separately configurable authentication on the stub serving
and admin interface for each mock API.

## Admin API security

Every mock API created has its own admin API (think of it as a standalone WireMock server per API), which is used for stubbing, verification, reset and a few other things.
This has the same base URL as your mock API, with a base path of `/__admin` e.g. `https://example.wiremockapi.cloud/__admin`.

By default this is secured using the API token that can be found in [https://app.wiremock.cloud/account/security](https://app.wiremock.cloud/account/security).

The token can either be sent in an Authorization header e.g.

`Authorization:Token 1kj3h98f7sihjfsf`

or as a query parameter e.g.

`https://example.wiremockapi.cloud/__admin/mappings?apiToken=1kj3h98f7sihjfsf`.

It is recommended that you use the header approach where possible as this reduces the risk of the key appearing in log files an browser histories.

### Disabling admin security

Admin API security can be disabled from the Settings page for the API:

<img src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/security-toggle.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=63117d743b761938fd410b3abe5159e5" title="Security toggle" width="50%" data-og-width="512" data-og-height="280" data-path="images/security-toggle.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/security-toggle.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=27b9ba4f79113a945d01d2d7d90f9e21 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/security-toggle.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=9480988429cdd4177c49e246432fd1a0 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/security-toggle.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=64a9c15d186f2101dbcd4f1870aee454 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/security-toggle.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=c7a529f1d689a6507848d4d57c95a04f 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/security-toggle.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=3dea0b5be2a154ff2950bbc7ef9a22f7 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/security-toggle.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=0a214c08f339abfe90e62fa1c033efff 2500w" />

<Note>Admin API security will be disabled by default for APIs created prior to the security feature being released.</Note>

## Mock API security

Mock APIs can optionally be configured to authenticate callers. At present this can
be via HTTP Basic authentication (username + password) or an arbitrary header match,
as well as OpenID Connect authentication for [Enterprise plan users](https://www.wiremock.io/get-pricing).

### HTTP Basic authentication

<img src="https://mintcdn.com/wiremockinc/tOJz-Q8hpPG9i-t9/images/http-basic-auth.png?fit=max&auto=format&n=tOJz-Q8hpPG9i-t9&q=85&s=dc08a6488bed5e2b3469d8be1ce55466" title="HTTP Basic authentication" width="50%" data-og-width="1178" data-og-height="730" data-path="images/http-basic-auth.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/tOJz-Q8hpPG9i-t9/images/http-basic-auth.png?w=280&fit=max&auto=format&n=tOJz-Q8hpPG9i-t9&q=85&s=0c0d1419f2694f1a703ea69a3526aad2 280w, https://mintcdn.com/wiremockinc/tOJz-Q8hpPG9i-t9/images/http-basic-auth.png?w=560&fit=max&auto=format&n=tOJz-Q8hpPG9i-t9&q=85&s=d6bb43f0c54cbc0447ac8eb35590bc2b 560w, https://mintcdn.com/wiremockinc/tOJz-Q8hpPG9i-t9/images/http-basic-auth.png?w=840&fit=max&auto=format&n=tOJz-Q8hpPG9i-t9&q=85&s=44e1fa439c6be56ef9dfe9b05859b4f8 840w, https://mintcdn.com/wiremockinc/tOJz-Q8hpPG9i-t9/images/http-basic-auth.png?w=1100&fit=max&auto=format&n=tOJz-Q8hpPG9i-t9&q=85&s=001713b758fb916d2053fd43622c629d 1100w, https://mintcdn.com/wiremockinc/tOJz-Q8hpPG9i-t9/images/http-basic-auth.png?w=1650&fit=max&auto=format&n=tOJz-Q8hpPG9i-t9&q=85&s=d2018ab5f91b9f03fd980923f825f651 1650w, https://mintcdn.com/wiremockinc/tOJz-Q8hpPG9i-t9/images/http-basic-auth.png?w=2500&fit=max&auto=format&n=tOJz-Q8hpPG9i-t9&q=85&s=cdb42c7cc470137ea63fd335a2b33588 2500w" />

HTTP Basic is a widely supported part of the HTTP standard supporting username/password authentication.
An HTTP resource secured with HTTP Basic will result in a browser prompting the user
with a username/password dialogue box on their initial visit.

Alternatively, an API client can pre-emptively authenticate by sending a header of the form
`Authorization:Basic <base64 encoded username:password>`.

### Header match authentication

<img src="https://mintcdn.com/wiremockinc/tOJz-Q8hpPG9i-t9/images/header-match-auth.png?fit=max&auto=format&n=tOJz-Q8hpPG9i-t9&q=85&s=b4d16c43a0af4254a4b373b9c5434f86" title="Header match authentication" width="50%" data-og-width="1184" data-og-height="858" data-path="images/header-match-auth.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/tOJz-Q8hpPG9i-t9/images/header-match-auth.png?w=280&fit=max&auto=format&n=tOJz-Q8hpPG9i-t9&q=85&s=2b54a5d8e1aa67bccf196a31b23ae4b2 280w, https://mintcdn.com/wiremockinc/tOJz-Q8hpPG9i-t9/images/header-match-auth.png?w=560&fit=max&auto=format&n=tOJz-Q8hpPG9i-t9&q=85&s=2f4c5b853e7b0feb869560321daf41bb 560w, https://mintcdn.com/wiremockinc/tOJz-Q8hpPG9i-t9/images/header-match-auth.png?w=840&fit=max&auto=format&n=tOJz-Q8hpPG9i-t9&q=85&s=5248f347bf33059c722ff6593fc003e0 840w, https://mintcdn.com/wiremockinc/tOJz-Q8hpPG9i-t9/images/header-match-auth.png?w=1100&fit=max&auto=format&n=tOJz-Q8hpPG9i-t9&q=85&s=1ddaad11bb3d4d4241b82349f5a04fac 1100w, https://mintcdn.com/wiremockinc/tOJz-Q8hpPG9i-t9/images/header-match-auth.png?w=1650&fit=max&auto=format&n=tOJz-Q8hpPG9i-t9&q=85&s=6e81657b439be94a2f6a0d97524c20fc 1650w, https://mintcdn.com/wiremockinc/tOJz-Q8hpPG9i-t9/images/header-match-auth.png?w=2500&fit=max&auto=format&n=tOJz-Q8hpPG9i-t9&q=85&s=1dbdf418e6ca11cd4f2523986b5ba9a8 2500w" />

WireMock Cloud can also authenticate requests based on a match expression against any header.
The match expression works in the same way as header matches in the stub creation form,
whereby you specify the header name, predicate and expected value.

### OpenID Connect authentication

<img src="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/oidc-auth.png?fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=338b826848081745da84e7c2b8b581e4" title="OpenID Connect authentication" width="100%" data-og-width="920" data-og-height="440" data-path="images/oidc-auth.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/oidc-auth.png?w=280&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=f8805a855861524db0628bdc085545b9 280w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/oidc-auth.png?w=560&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=35050e300f0b25c729561805633e9b44 560w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/oidc-auth.png?w=840&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=1ee7b6b9d627228fea6edeae9b886aad 840w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/oidc-auth.png?w=1100&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=a3aae69c39147c13e9825340fb09b691 1100w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/oidc-auth.png?w=1650&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=a43deada6d215234263b84701e7e35d1 1650w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/oidc-auth.png?w=2500&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=9b5c5484458ac9df5b95c0f7eddf1985 2500w" />

For [Enterprise plan users](https://www.wiremock.io/get-pricing), WireMock Cloud can authenticate requests via an
OpenID Connect authorization server.
Requests must contain an HTTP header whose value is a [JWT](https://jwt.io) generated by the configured authorization
server.
The value of the Authorization header field must be the name of the HTTP header that will contain the JWT (usually
`Authorization`, but any valid HTTP header name is allowed).
The value of the Issuer URL field must be the base URL of the authorization server.

The authorization server is expected to be configured as per
[the OpenID Connect specification](https://openid.net/specs/openid-connect-discovery-1_0.html).
Specifically `/.well-known/openid-configuration` contains the required configuration information, including the URL to
the JSON Web Key Set (JWKS) that contains the key(s) to verify the JWTs' signatures.

The value of the Audiences field can optionally be a set of required audiences.
If this field's value is non-empty, every JWT's
[`aud` claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.3) must contain all of these audiences for the
JWT to be considered valid.
