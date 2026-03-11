# Source: https://docs.envzero.com/changelogs/2022/08/oidc-support.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🖇️ OpenID Connect (OIDC) Support

> OpenID Connect (OIDC) is a simple identity layer on top of the OAuth 2.0 protocol. It allows clients to verify the identity of a user or an application based on the authentication performed by an Authorization Server. This will enable you to securely interact with 3rd party applications like your cloud provider. Now with env zero, each deployment can have an integration with OIDC and provides an OIDC short-lived token (JWT) for you to authenticate to any other 3rd party application.

OpenID Connect (OIDC) is a simple identity layer on top of the OAuth 2.0 protocol. It allows clients to verify the identity of a user or an application based on the authentication performed by an Authorization Server. This will enable you to securely interact with 3rd party applications like your cloud provider. Now with env zero, each deployment can have an integration with OIDC and provides an OIDC short-lived token (JWT) for you to authenticate to any other 3rd party application.

## ✨ Setup Up OIDC ✨

A JWT token could be available during deployment as an environment variable called `ENV0_OIDC_TOKEN`.\
Organization admins can enable this feature by toggling the related checkbox which exists in the organization's policies tab.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/4i75qYgyhlssLgkA/images/changelogs/2022/08/screen_shot_2022-08-07_at_171544png.png?fit=max&auto=format&n=4i75qYgyhlssLgkA&q=85&s=e510955bbd45c186215dafd45f3b1b9b" alt="Screen Shot 2022-08-07 at 17.15.44.png" width="1404" height="503" data-path="images/changelogs/2022/08/screen_shot_2022-08-07_at_171544png.png" />
</Frame>

To learn more [read more here about this integration](/guides/integrations/oidc-integrations)

> 🚧 For Self-Hosted Agents
>
> If you'd like to enable this feature on your self-hosted agent, please update to the latest version.

Built with [Mintlify](https://mintlify.com).
