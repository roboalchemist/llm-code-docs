# Source: https://docs.gitguardian.com/ggmcp-docs/authentication.md

# Source: https://docs.gitguardian.com/api-docs/authentication.md

# Authentication

> How the GitGuardian API authenticates requests using API keys, covering service accounts, personal access tokens, and permission scopes.

The GitGuardian API uses API keys to authenticate requests.

## Creating your API key

There are 2 different types of API keys:
- **[Service accounts](./service-accounts.md):** a special type of token intended to represent a non-human user that needs to authenticate and be authorized for scenarios such as secrets scanning in CI pipelines or batch processing open incidents.
- **[Personal access tokens](./personal-access-tokens.md):** a token intended for the use of the GitGuardian API and command-line application ggshield by individual developers on their local workstations (e.g. pre-commit or pre-push git hooks).

You need to [create an account](https://dashboard.gitguardian.com/auth/signup) in order to get an API key.
Your API key must be kept private and should neither be embedded directly in the code nor versioned in Git.
(Please do not push GitGuardian's API keys to public GitHub repositories ^^).

As in the example below, use the [`/health` endpoint](https://api.gitguardian.com/docs#tag/Status/operation/health_check) to check the validity of your API key.

## Authentication scheme

The GitGuardian API uses `Authorization` header authentication for its requests. The `Authorization` header value must be prefixed with `Token`.

Example request using `curl`:

```sh
curl -H "Authorization: Token ${TOKEN}" \
  https://api.gitguardian.com/v1/health
```

## Scopes

**Scopes are tied to an API key and control the access to resources and scan capability**.

### Dashboard data management scopes

- `incidents`
    - `incidents:share`: grant view, edit and share permissions on the incidents of your GitGuardian workspace.
    - `incidents:write`: grant view and edit permissions on the incidents of your GitGuardian workspace.
    - `incidents:read`: grant view only permission on the incidents of your GitGuardian workspace.
- `sources`
    - `sources:write`: grant view and edit permissions on the sources (code repositories only) of your GitGuardian workspace.
    - `sources:read`: grant view only permission on the sources (code repositories only) of your GitGuardian workspace.
- `honeytokens`
    - `honeytokens:write`: grant view and edit permissions on the honeytokens of your GitGuardian workspace. Available under specific conditions: the honeytoken product must be enabled for the workspace, and for personal access token the role must be minimum "manager".
    - `honeytokens:read`: grant view only permission on the honeytokens of your GitGuardian workspace. Available under specific conditions: the honeytoken product must be enabled for the workspace, and for personal access token the role must be minimum "manager".
- `members`
    - `members:write`: grant view and edit permissions on the members of your GitGuardian workspace.
    - `members:read`: grant view permission on the members of your GitGuardian workspace.
- `teams`
    - `teams:write`: grant view and edit permissions on the teams of your GitGuardian workspace.
    - `teams:read`: grant view permission on the teams of your GitGuardian workspace.
- `api_tokens`
    - `api_tokens:write`: grant view and edit permissions on the api tokens (personal access tokens and service accounts) of your GitGuardian workspace.
    - `api_tokens:read`: grant view permission on the api tokens (personal access tokens and service accounts) of your GitGuardian workspace.
- `audit_logs:read`: grant view permission on the audit logs of your GitGuardian workspace. If you are using personal access tokens, it is only available to Managers.
- `ip_allowlist`
    - `ip_allowlist:write`: grant view and edit permissions on the IP allowlist of your GitGuardian workspace.
    - `ip_allowlist:read`: grant view only permission on the IP allowlist of your GitGuardian workspace.
- `custom_tags`
    - `custom_tags:write`: grant view and edit permissions on the custom tags of your GitGuardian workspace.
    - `custom_tags:read`: grant view only permission on the custom tags of your GitGuardian workspace.
- `secrets`
    - `secrets:write`: grant view and edit permissions on NHI secrets of your GitGuardian workspace.
    - `secrets:read`: grant view only permission on NHI secrets of your GitGuardian workspace.
- `nhi`
    - `nhi:send-inventory`: grant permission to send NHI inventory data to GitGuardian.
    - `nhi:write-vault`: grant permission to receive write instructions from GitGuardian for secret synchronization.
    - `nhi:ownership:write`: grant view and edit permissions on NHI ownership.
    - `nhi:ownership:read`: grant view only permission on NHI ownership.
- `public-perimeter:read`: grant view permission on the public monitoring perimeter of your GitGuardian workspace.

### Scan capability scope

- `scan`: grant permissions to scan any text content for secrets with GitGuardian secrets detection engine. Required to use [ggshield](../ggshield-docs/getting-started).
- `scan:create-incidents`: grant permissions to scan content and create incidents from custom sources. Includes `scan` scope.

> You can even test this capability directly in the [Secrets detection playground section in your dashboard](https://dashboard.gitguardian.com/api/secrets-detection-playground):

![API Secrets detection playground](/img/api/secrets_detection_playground.png)
