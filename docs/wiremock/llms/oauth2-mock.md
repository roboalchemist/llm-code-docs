# Source: https://docs.wiremock.io/security/oauth2-mock.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# The OAuth2 / OpenID Connect Mock

> Using the OAuth2 / OpenID Connect Mock

<img src="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/oauth-2-logo.png?fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=575bcf302eaef5ff36ceb83b54cc9598" alt="OAuth2" data-og-width="124" width="124" data-og-height="123" height="123" data-path="images/oauth-2-logo.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/oauth-2-logo.png?w=280&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=84335e14ccca08e66d35ae40f2cdfbc6 280w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/oauth-2-logo.png?w=560&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=e6fb89c1928275b7d5426377d777668e 560w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/oauth-2-logo.png?w=840&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=3747c6a2d70b6dbe0ea3e30cccaa2890 840w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/oauth-2-logo.png?w=1100&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=d40fce3d909e1cdb8e29569c1dcd987b 1100w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/oauth-2-logo.png?w=1650&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=b63b11d167af09206aa59966a0aa539d 1650w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/oauth-2-logo.png?w=2500&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=d96325d0e6edcb33c0bededdefcfb485 2500w" />.    &#x20;

This is a simulation of an **OAuth2** / **OpenID Connect** login service that you can use as a **drop-in replacement** for the real thing during testing. It's free to use, and completely stateless so can accommodate virtually any number of concurrent clients (at least until the server runs out of breath!).

Currently the `authorization_code` (server-side web) OAuth2 flow is supported.

## Using with your app

Start by finding the OAuth2 configuration in your app's server-side component. Where this is located
varies from app to app - sometimes it can be found in a configuration file, other times it is set
directly in code. If you're using an SDK from your login service, you may need to override the defaults this provides.

Set the following values:

* Authorization URI: [`https://oauth.wiremockapi.cloud/oauth/authorize`](https://oauth.wiremockapi.cloud/oauth/authorize)

* Token URI: [`https://oauth.wiremockapi.cloud/oauth/token`](https://oauth.wiremockapi.cloud/oauth/token)

* User info URI: [`https://oauth.wiremockapi.cloud/userinfo`](https://oauth.wiremockapi.cloud/userinfo)

* JWKS URI: [`https://oauth.wiremockapi.cloud/.well-known/jwks.json`](https://oauth.wiremockapi.cloud/.well-known/jwks.json)

You can [see here](https://github.com/wiremock/wiremock-cloud-demo-app/blob/master/src/main/resources/application.yml#L8) how this is done in a Spring Boot application.

After that, when you start the login process from your app you should be sent to
a simulated login page, rather than the one belonging to your real provider. You
can log in with any email address and password you like, real or not.

<img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/Screenshot2025-01-16at10.05.25AM.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=2ae582155118b0764dab691986490fb9" alt="" data-og-width="864" width="864" data-og-height="700" height="700" data-path="Screenshot2025-01-16at10.05.25AM.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/Screenshot2025-01-16at10.05.25AM.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=6496a55de827b2ba0a72479c0fc91f88 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/Screenshot2025-01-16at10.05.25AM.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=c530e7f0c03007cefb82f0e6105f7a32 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/Screenshot2025-01-16at10.05.25AM.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=38d0d7d206bc0a1bc6e68c106cae72a7 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/Screenshot2025-01-16at10.05.25AM.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=e8f31f6b05a4388b6d8466dd356817c6 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/Screenshot2025-01-16at10.05.25AM.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=424a7f4d1d1014828018dd0aebccef26 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/Screenshot2025-01-16at10.05.25AM.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=3d4a5b01bc9ab8032f357ed371318175 2500w" />

## Questions and feedback

If you're not sure how something works or have a suggestion for improving this simulation, please get in touch with us
via [info@wiremock.io](mailto:info@wiremock.io) or the chat widget.
