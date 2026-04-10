# Source: https://docs.convex.dev/deployment-api/convex-deployment-api.md

Version: 1.0.0

# Convex Deployment API

Admin API for interacting with deployments.

## Authentication[​](#authentication "Direct link to Authentication")

* API Key: Deploy Key
* API Key: OAuth Project Token
* API Key: OAuth Team Token
* API Key: Team Token

Deploy keys are used for deployment operations. See [deploy key types](https://docs.convex.dev/cli/deploy-key-types) for more information. Use the `Convex `prefix (e.g., `Convex <deploy_key>`).

| Security Scheme Type:  | apiKey        |
| ---------------------- | ------------- |
| Header parameter name: | Authorization |

Obtained through a [Convex OAuth application](https://docs.convex.dev/management-api) with project scope. Use the `Convex `prefix (e.g., `Convex <oauth_project_token>`).

| Security Scheme Type:  | apiKey        |
| ---------------------- | ------------- |
| Header parameter name: | Authorization |

Obtained through a [Convex OAuth application](https://docs.convex.dev/management-api). Use the `Convex `prefix (e.g., `Convex <oauth_token>`).

| Security Scheme Type:  | apiKey        |
| ---------------------- | ------------- |
| Header parameter name: | Authorization |

Created in the dashboard under team settings for any team you can manage. Use the `Convex `prefix (e.g., `Convex <team_token>`).

| Security Scheme Type:  | apiKey        |
| ---------------------- | ------------- |
| Header parameter name: | Authorization |

### License
