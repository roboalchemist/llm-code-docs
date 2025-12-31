# Source: https://docs.zapier.com/powered-by-zapier/zap-templates/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/zap-creation/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/sponsor-user-automation/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/running-actions/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/managing-app-authentication/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/embedding-zapier/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/embedding-zapier-mcp/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/authentication/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/zap-templates/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/zap-creation/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/sponsor-user-automation/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/running-actions/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/managing-app-authentication/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/embedding-zapier/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/embedding-zapier-mcp/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/authentication/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/zap-templates/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/zap-creation/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/sponsor-user-automation/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/running-actions/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/managing-app-authentication/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/embedding-zapier/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/embedding-zapier-mcp/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/authentication/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/zap-templates/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/zap-creation/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/sponsor-user-automation/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/running-actions/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/managing-app-authentication/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/embedding-zapier/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/embedding-zapier-mcp/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/authentication/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/zap-templates/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/zap-creation/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/sponsor-user-automation/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/running-actions/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/managing-app-authentication/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/embedding-zapier/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/embedding-zapier-mcp/getting-started.md

# Source: https://docs.zapier.com/powered-by-zapier/authentication/getting-started.md

# Getting Started

> Authenticate with The Zapier Workflow API

Depending on the endpoints being accessed, there are varying authentication methods that should be used. The documentation for individual endpoints and Powered By Zapier features should guide you to the correct authentication method you should use.

## Authentication Methods

### User Access Token

> Most endpoints use [OAuth 2.0 authentication with the authorization code grant type](https://developer.okta.com/blog/2018/04/10/oauth-authorization-code-grant-type). At the end of the Oauth authentication code flow, you'll get a User Access Token that you'll pass in a header with each API request.
>
> <br />
>
> [View Documentation
> ->](/powered-by-zapier/authentication/methods/user-access-token)

### App Access Token

> While many API endpoints require a user access token to perform actions on behalf of a user, some (ex: [unenrolling a user from a promotion](https://docs.zapier.com/powered-by-zapier/api-reference/promotions/delete-enrollment)) require an App Access Token.
>
> <br />
>
> [View Documentation
> ->](/powered-by-zapier/authentication/methods/app-access-token)

### Client ID

> Most endpoints require app or user access token authentication. However, a smaller number of endpoints require only a valid Client ID in order to be accessed.
>
> <br />
>
> [View Documentation ->](/powered-by-zapier/authentication/methods/client-id)
