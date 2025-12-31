# Source: https://herd.laravel.com/docs/macos/advanced-usage/social-auth.md

# Social Authentication

# Implementing Social Authentication

When implementing social authentication in your Laravel application, you may face the issue that Herd's `.test`
domain is not recognized by the social authentication providers. This is because they often require a public top-level
domain (TLD) for their callback URLs. Herd does not support changing the `.test` domain to a public TLD, because
that would introduce serious security issues to your machine – but we can work around this.

## Using the fwd.host Webservice

We've created a web service that acts as a proxy for your redirects and does not store any data. You can use this service
to handle social authentication callbacks by setting your callback URLs to `https://fwd.host/http://your-herd-site.test/auth/callback`.

This way, the social authentication provider will redirect to `fwd.host`, which will then forward the request to your Herd site.

You can see the setup in the following screenshot:

<img src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/google-oauth-setup.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=814d601ef3ce2050cd09c3df58f1c007" alt="Social Authentication Setup" data-og-width="2302" width="2302" data-og-height="1720" height="1720" data-path="images/docs/google-oauth-setup.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/google-oauth-setup.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=9d21f517f270cbadd29aa0a7a08aff48 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/google-oauth-setup.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=e2dd9f8392d3f66562d04da1f9516304 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/google-oauth-setup.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=791c0988a80fac5a566615ceaa1a1b3b 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/google-oauth-setup.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=ed193bb809eee279eb3963e8c9033eb1 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/google-oauth-setup.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=81b69d62297bb67c4ccb12c77889e98b 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/google-oauth-setup.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=dfcdc0dca72961bb443efeb5030c8369 2500w" />

The `fwd.host` service will forward the request to your Herd site, allowing you to handle the social authentication as usual.
For security reasons, the redirects are limited to Herd sites with `.test` domains only, so you cannot use this service to redirect to any other site.
