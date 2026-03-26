# Source: https://docs.socket.dev/docs/understanding-act-on-your-behalf-permission.md

# Understanding "Act on Your Behalf" Permission

The "Act on Your Behalf" permission is a requirement from GitHub for third-party apps that utilize GitHub as an Identity Provider (IdP) to verify a user’s identity. This permission may seem broad, but its actual scope is strictly limited to the explicit permissions granted by the user. As clarified in the [GitHub documentation](https://docs.github.com/en/apps/using-github-apps/authorizing-github-apps#about-github-apps-acting-on-your-behalf):

`The GitHub App can only do things that both you and the app have permission to do.`

GitHub requires the "Act on Your Behalf" permission for third-party apps, like Socket, that use GitHub as an Identity Provider (IdP) to verify user identities. This permission is strictly limited to the actions explicitly allowed by the user. Socket requests this to identify active committers within your organization for accurate license compliance tracking but granting it is optional. Without it, open-source contributors may appear in reports. Alternatively, you can avoid using GitHub for authentication by setting up Single Sign-On (SSO) with an identity provider like Okta, as outlined in the [Socket SSO Documentation](https://docs.socket.dev/docs/single-sign-on).