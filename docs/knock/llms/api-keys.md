# Source: https://docs.knock.app/developer-tools/api-keys.md

# Source: https://docs.knock.app/api-reference/overview/api-keys.md

# API keys

Knock authenticates your API requests using your account's API keys. API requests made without authentication or using an incorrect key will return a 401 error. Requests using a valid key but with insufficient permissions will return a 403 error.

You can view and manage your API keys in the dashboard. You can create any number of API keys per environment, and there are two types of keys:

- Public keys are only meant to identify your account with Knock. They aren't secret, and can safely be made public in any of your client-side code. Publishable keys are prefixed with `pk_*`.

- Secret keys can perform any API request to Knock and should be kept secure and private. Be sure to prevent secret keys from being made publicly accessible, such as in client-side code, GitHub, unsecured S3 buckets, and so forth. Secret keys are prefixed with `sk_*`.

Each environment in your account can have any number of publishable and secret keys. API requests will be scoped to the provided key's environment. You can create and revoke keys at any time from the [API keys page](/developer-tools/api-keys) in your dashboard.
