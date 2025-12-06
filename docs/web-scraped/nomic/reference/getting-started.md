# Nomic Documentation

Source: https://docs.nomic.ai/reference/getting-started/

You can interact with the Nomic Platform API through HTTP requests, our official Python library or NodeJS library.

The Nomic Platform API provides access to Nomic machine learning models and data structuring capabilities.

To install official Python bindings,

```
pip install nomic
```

## Authentication​

The Nomic Platform API provides two methods for authentication: refresh/bearer tokens and API keys.

All API key requests should include your API key in an Authorization HTTP header as follows:

```
Authorization: Bearer NOMIC_API_KEY
```

API keys are tied to specific users in your organization and usage is billed through your Nomic organization.

The Nomic Python Client and NodeJS client will accept a refresh token and handle generating new JWT bearer tokens
on expiration. You can access refresh tokens for use with the Python or NodeJS client in the Atlas Dashboard.

### Enterprise Authentication​

Private deployments of Nomic Platform require specifying a tenant domain during authentication.

```
domain
```

```
nomic login enterprise --domain sterling-cooper-atlas.nomic.ai <refresh_token>
```

or in Python

```
import nomicnomic.cli.login(    token="token",    domain='sterling-cooper-atlas.nomic.ai',    tenant='enterprise')
```

- AuthenticationEnterprise Authentication
- Enterprise Authentication
