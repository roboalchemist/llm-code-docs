# Source: https://grafbase.com/docs/gateway/security/access-tokens.md

# Access Tokens

Access tokens grant access to Grafbase services and APIs. Use them to manage your account, organization, and graphs.

## Personal Access Tokens

Use personal access tokens to grant access for the [Grafbase CLI](https://grafbase.com/docs/grafbase-cli.md) and Management API.

These tokens always have the same permissions as the corresponding users. They can be seen as ID tokens.

### Create a Personal Access Token

Create access tokens from your [account settings > access tokens](https://app.grafbase.com/settings/access-tokens) page.

Give your access token a name and select a scope.

You cannot modify or read access tokens after creation. Copy the token to a secure location and never share it with anyone.

### Revoke Access Tokens

Tokens do not expire. Revoke them when you no longer need them.

Revoke tokens anytime from your [account settings > access tokens](https://app.grafbase.com/settings/access-tokens) page.

## Organization Access Tokens

Organization access tokens grant access for the Grafbase Gateway telemetry and Graph Delivery Network. These tokens belong to an organization, so they continue working even if you remove a user from the organization.

### Scopes

Each access token has a specific scope that grants access to certain organization and graph settings.

#### All Graphs

All Graphs tokens let you use the Grafbase Gateway to access all graphs within the organization.

#### Specific Graphs

Use these tokens to limit the Grafbase Gateway to access only certain graphs.

### Create an Organization Access Token

Create access tokens from your `organization settings > access tokens` page.

Give your access token a name and select the graph(s).

You cannot modify or read access tokens after creation. Copy the token to a secure location and never share it with anyone.

### Revoke Access Tokens

Tokens do not expire. Revoke them when you no longer need them.

Revoke tokens anytime from your `organization settings > access tokens` page.