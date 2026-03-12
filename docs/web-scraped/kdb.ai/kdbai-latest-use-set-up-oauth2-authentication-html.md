# Source: https://code.kx.com/kdbai/latest/use/set-up-oauth2-authentication.html

Title: OAuth 2.0 Authentication and Authorization in KDB.AI

URL Source: https://code.kx.com/kdbai/latest/use/set-up-oauth2-authentication.html

Markdown Content:
_This page explains how to integrate KDB.AI with an external identity provider (IdP) such as Keycloak, Microsoft Entra ID, or Okta to enable OAuth 2.0-based access control. It covers JWT token validation, required environment configuration, tenant and group-based authorization using ACL grants, and Python client integration._

Prerequisites
-------------

Before configuring OAuth 2.0, you need:

*   An IdP that supports OAuth 2.0 and JWTs
*   At least one tenant defined in your IdP
*   An OAuth 2.0 client for each tenant
*   Group membership defined in your IdP
*   Ability to modify environment variables for KDB.AI

How it works
------------

KDB.AI uses the OAuth 2.0 framework to authorize requests based on JWT access tokens issued by your identity provider (IdP). It supports **JWT access tokens only** and validates their signatures using the **RS256** (RSA with SHA-256) algorithm. Public signing keys are retrieved from the issuer’s JWKS endpoint. After signature validation, KDB.AI evaluates the `tenant`, `groups` (with `claim` field names defined by the user), and `aud` claims and matches them against stored ACL grants to determine whether the request is permitted.

Identity provider responsibility

All user management, authentication, and token issuance remain with your IdP. KDB.AI does not manage users, passwords, or sessions, and does not communicate with the IdP beyond fetching JWKS keys for signature verification.

### OAuth 2.0 Authorization Flow (REST API)

**Identity Provider** → issues JWT → **Client** → sends Bearer token → **KDB.AI**

| **Step** | **What happens** |
| --- | --- |
| 1. Token request | Client obtains a JWT token from the IdP. |
| 2. API request | Client sends the JWT as a `Bearer` token in the `Authorization` header of the REST call. |
| 3. Signature check | KDB.AI fetches JWKS keys from the issuer URL and validates the token signature using RS256. |
| 4. Claim validation | KDB.AI checks: `iss` is in the allowed issuers list, `aud` matches the expected app name. |
| 5. Claim extraction | KDB.AI reads the `tenant` and `groups` claims from the token. |
| 6. ACL evaluation | KDB.AI matches (tenant, groups) against stored grants to authorize the request. |

For Python client integration, refer to the [KDB.AI Python Client](https://code.kx.com/kdbai/latest/use/set-up-oauth2-authentication.html#kdbai-python-client) section. You can configure the client to automatically handle OAuth 2.0 token refresh and lifecycle management.

### Example IdP structure

The tenant and group names below are for demo purposes only. Replace them with your own organizational structure. Users are shown for IdP context only.

KDB.AI never sees or stores user identities. It only sees the `tenant` and `groups` claims in the token.

| **Tenant** | **Groups** | **Users (IdP only)** | **Group membership** |
| --- | --- | --- | --- |
| **quants** | `admin`, `trader`, `viewer` | alice | `trader`, `viewer` |
|  |  | bob | `viewer` |
| **risk** | `admin`, `viewer` | charlie | `viewer` |
| **manager** | `admin` | root | `admin` |

Each tenant is an isolated boundary. Groups within a tenant have no inherent meaning on their own – they only gain significance when a KDB.AI **ACL grant** references them (refer to [Group-to-Permission Mapping](https://code.kx.com/kdbai/latest/use/set-up-oauth2-authentication.html#group-to-permission-mapping)).

IdP terminology

How a "tenant" is represented depends on your IdP:

*   In Keycloak, each tenant is a **realm**.
*   In Entra ID, it maps to an **Entra tenant** (identified by `tid`). 
*   In Okta, it could be an **org** or **authorization server**. 

In KDB.AI, the user can configure the `tenant` field name.

### Required JWT claims

The IdP must include the following claims in the access token through **claim mappings** (or equivalent configuration in your IdP). KDB.AI uses these to validate the token and authorize each request.

| **Claim** | **Example value** | **IdP configuration** | **Purpose** |
| --- | --- | --- | --- |
| `iss` | `https://idp.example.com/tenants/quants` | Standard claim (set automatically by the IdP) | Must match one of the [`OAUTH_ISSUERS`](https://code.kx.com/kdbai/latest/use/set-up-oauth2-authentication.html#issuer-url-format) entries. Also used to fetch JWKS keys for signature verification. |
| `aud` | `kdbai-service` | Audience mapper | Must match `OAUTH_APP_NAME`. Prevents tokens intended for other services from being accepted. |
| `tenant` | `quants` | Hardcoded claim mapper | Identifies which tenant the token belongs to. Claim name is configurable using `OAUTH_TENANT_ID`. |
| `groups` | `["trader", "viewer"]` | Group membership mapper | List of group memberships. Matched against ACL grants to determine what operations the token authorizes. Claim name is configurable using `OAUTH_GROUP_ID`. |

Identity provider setup
-----------------------

Regardless of which IdP you use, you need **at least one OAuth 2.0 client per tenant**. Each client gets its own claim mappings with a hardcoded `tenant` value identifying that tenant. A tenant can have multiple clients – for example, a **public client** for interactive users (authorization code, device authorization) and a **confidential client** for machine-to-machine access (client credentials). All clients for the same tenant share the same `tenant` claim value.

For each tenant:

1.   **Create the OAuth 2.0 client** in your IdP.

2.   **Add three claim mappings** to the client:

    *   **Audience** → sets `aud` to your client ID (for example, `kdbai-service`).
    *   **Groups** → emits the user's group memberships as a `groups` claim.
    *   **Tenant** → emits a hardcoded `tenant` claim identifying this specific tenant.

3.   **Create groups** that correspond to the group names you will use in KDB.AI ACL grants.

4.   **Assign users to groups**.

#### Groups and users

Groups in your IdP are the bridge between users and KDB.AI permissions. A group name on its own does nothing – it only gains meaning when a KDB.AI **ACL grant** references that `(tenant, group)` pair.

For example:

*   Creating a group called `trader` in the `quants` tenant does **not** automatically grant any access.
*   Only when a KDB.AI system_admin creates a grant like _"give `trader` in `quants` read access to database `analytics`"_ does the group have an effect.
*   Any user in the `trader` group will then inherit that access.

Create groups in each tenant that reflect the access levels you want to define, then assign users to those groups. A user can belong to multiple groups and will receive the **union** of all matching grants.

KDB.AI configuration
--------------------

The `kdbai‑db` container **requires** the following environment variables to enable OAuth 2.0 token validation and authorization. Without them, the system disables access control and treats all requests as anonymous.

| **Variable** | **Required** | **Example** | **Description** |
| --- | --- | --- | --- |
| `AUTH_TYPE` | Yes | `oauth` | Enables JWT-based authorization |
| `OAUTH_APP_NAME` | Yes | `kdbai-service` | Expected `aud` claim value |
| `OAUTH_TENANT_ID` | Yes | `tenant` | Name of the JWT claim containing the tenant ID |
| `OAUTH_GROUP_ID` | Yes | `groups` | Name of the JWT claim containing the groups |
| `OAUTH_ISSUERS` | Yes | View [format](https://code.kx.com/kdbai/latest/use/set-up-oauth2-authentication.html#issuer-url-format) | **Comma-separated** list of trusted token issuer URLs – one per tenant |
| `ACL_SYSTEM_ADMIN_TENANT` | Yes | `manager` | Tenant whose admin group gets full privileges. Refer to [System admin bootstrap](https://code.kx.com/kdbai/latest/use/set-up-oauth2-authentication.html#system-admin-bootstrap). |
| `ACL_SYSTEM_ADMIN_GROUP` | Yes | `admin` | Group name that grants system admin access. Refer to [System admin bootstrap](https://code.kx.com/kdbai/latest/use/set-up-oauth2-authentication.html#system-admin-bootstrap). |

### ACL data persistence

ACL grants are stored **separately** from VDB data at a different path inside the container. Without a dedicated volume mount, all grants are lost when the container is removed or recreated.

| **Path** | **Volume mount** |
| --- | --- |
| `/tmp/acl` | `./acl-data:/tmp/acl` |

Important

This volume is separate from the VDB data volume (`/tmp/kx/data`). If you mount only the VDB volume and not the ACL volume, your data persists, but the system must recreate all ACL grants after every container restart. In production, you should mount both volumes.

### System admin bootstrap

`ACL_SYSTEM_ADMIN_TENANT` and `ACL_SYSTEM_ADMIN_GROUP` define which `(tenant, group)` pair gets **system_admin** privileges at startup. These values can be anything – `manager` and `admin` are just example names. They must match a real tenant and group in your IdP.

| **Scenario** | **What happens** |
| --- | --- |
| **Both set and match a token's claims** | Any token with that `(tenant, group)` pair gets full admin access: manage grants, bypass all ACL checks, access all resources |
| **Not set (empty or missing)** | Container **fails to start**. The gateway throws: `"need ACL_SYSTEM_TENANT_GROUP env variable value"` |
| **Set to values that don't match any token** | Container starts, but **no token has system_admin access**. No one can call `addGrants` or `deleteGrant`, so you are locked out of ACL management. |

Tip

Always verify that your IdP can issue tokens with the configured tenant and group claims before starting KDB.AI with OAuth enabled. If you get locked out, fix the environment variables and restart – no data is lost.

### Issuer URL format

`OAUTH_ISSUERS` accepts a **comma-separated** list of issuer URLs. Each entry must exactly match the `iss` claim in the tokens issued by that IdP. Add one entry per tenant that should be allowed to authenticate.

Example

```
OAUTH_ISSUERS=https://idp.example.com/tenants/quants,https://idp.example.com/tenants/risk,https://idp.example.com/tenants/manager
```

Important

These URLs must be reachable from the KDB.AI container at runtime. KDB.AI fetches JWKS signing keys from these endpoints to verify token signatures. If a URL is unreachable, tokens from that issuer will fail validation.

### Example configuration

The following Docker Compose example shows all required environment variables and volume mounts. The same configuration applies to any deployment method (for example, Kubernetes, standalone Docker). Adapt the environment variables and volume mounts to your platform.

```
services:
  kdbai-db:
    image: portal.dl.kx.com/kdbai-db:latest
    environment:
      - KDB_LICENSE_B64=${KDB_LICENSE_B64}     # base64 encoded license string
      # --- OAuth (required) ---
      - AUTH_TYPE=oauth
      - OAUTH_APP_NAME=kdbai-service           # must match the "aud" claim in your tokens
      - OAUTH_TENANT_ID=tenant                 # name of the JWT claim that holds the tenant ID
      - OAUTH_GROUP_ID=groups                  # name of the JWT claim that holds the groups ID
      - OAUTH_ISSUERS=https://idp.example.com/tenants/quants,https://idp.example.com/tenants/risk,https://idp.example.com/tenants/manager
      # --- System admin (required, see "System admin bootstrap" above) ---
      - ACL_SYSTEM_ADMIN_TENANT=manager
      - ACL_SYSTEM_ADMIN_GROUP=admin
    volumes:
      - ./kdbai-data:/tmp/kx/data              # kdbai vdb data
      - ./acl-data:/tmp/acl                    # persists ACL grants across restarts
    ports:
      - 8082:8082                              # QIPC port
      - 8081:8081                              # REST port
```

Update the `OAUTH_ISSUERS` to match your IdP configuration. The issuer URL must exactly match the `iss` claim in your tokens. For example:

*   **Keycloak**: `https://<keycloak-host>/realms/<realm>` – one entry per tenant (realm)
*   **Entra ID**: `https://login.microsoftonline.com/<tenant-id>/v2.0`
*   **Okta**: `https://<your-domain>.okta.com/oauth2/<authorization-server-id>`

Group-to-permission mapping
---------------------------

Permissions in KDB.AI are not assigned to individual users. They are assigned to **(tenant, group)** pairs through **grants**. When a request is received, KDB.AI extracts `tenant` and `groups` from the JWT and checks whether any grant matches.

### How groups connect to permissions

You define groups in your IdP and create grants in KDB.AI that reference those same group names. Apart from fetching JWKS keys to verify token signatures, KDB.AI never talks to your IdP - it only reads the group names from the JWT. If a grant exists for that `(tenant, group)` pair, the request is authorized. If not, it is denied.

```
IdP                                              KDB.AI
========================                         ======

Tenant: "quants"                                 ACL Grant:
  Group: "trader"            --- maps to --->      tenant=quants, groups=[trader]
    User: alice                                    database=analytics, actions=[read, write]
    User: dave

Tenant: "quants"                                 ACL Grant:
  Group: "viewer"            --- maps to --->      tenant=quants, groups=[viewer]
    User: alice                                    database=analytics, actions=[read]
    User: bob
```

The group name in the IdP **must exactly match** the group name in the KDB.AI grant. The grant is what gives the group its meaning.

### Access levels

| **Level** | **Includes** | **Allowed operations** |
| --- | --- | --- |
| **system_admin** | everything | Full access: manage grants, bypass all ACL checks, access all resources across all tenants. This level is **not** assigned through grants – it is determined by the `ACL_SYSTEM_ADMIN_TENANT` and `ACL_SYSTEM_ADMIN_GROUP` environment variables (refer to [System admin bootstrap](https://code.kx.com/kdbai/latest/use/set-up-oauth2-authentication.html#system-admin-bootstrap)). Any token whose `tenant` and `groups` claims match these values automatically has system_admin privileges. |
| **delete** | read | Drop table, drop database, delete data |
| **write** | read | Insert data, create table, update data, update indexes |
| **read** | – | Query, search, get table, list tables, get index, list indexes |

Note

`write` includes `read`. `delete` includes `read`. But `delete` does **not** include `write`. These are independent grant actions that happen to share read as a common baseline.

### Grant scopes

Grants can target a **database** (applies to all tables) or a specific **table**:

| **Scope** | **Applies to** | **When to use** |
| --- | --- | --- |
| **database** | All current and future tables in the database | Broad access for a team (for example, "traders can read everything in analytics") |
| **table** | Only the named table | Fine-grained control (for example, "viewers can only query the `prices` table") |

### End-to-end example

This traces how a token with `tenant=quants` and `groups=[trader, viewer]` gets authorized. (In this example, `alice` is the user in the IdP – but KDB.AI only sees the token's claims, not the user identity.)

**1. Token issued by IdP:**

| **Claim** | **Value** |
| --- | --- |
| `iss` | `https://idp.example.com/tenants/quants` |
| `aud` | `kdbai-service` |
| `tenant` | `quants` |
| `groups` | `["trader", "viewer"]` |

**2. KDB.AI validates the token:**

| **Check** | **Result** |
| --- | --- |
| Signature valid (JWKS) | Pass |
| `iss` in `OAUTH_ISSUERS` | Pass |
| `aud` matches `OAUTH_APP_NAME` | Pass |
| Token not expired | Pass |
| `groups` claim is present and not empty | Pass |

**3. KDB.AI evaluates grants for `tenant=quants`, `groups=[trader, viewer]`:**

| **Grant** | **Tenant** | **Groups** | **Database** | **Actions** | **Matches token?** |
| --- | --- | --- | --- | --- | --- |
| #1 | quants | trader | analytics | read | Yes – tenant and group match |
| #2 | quants | trader | analytics | write | Yes – tenant and group match |
| #3 | risk | viewer | analytics | read | No – wrong tenant (risk != quants) |

**4. Result:**

*   Grants #1 and #2 match – the token's `tenant` (`quants`) and one of its `groups` (`trader`) align with the grant. The token gets **read** and **write** access to the `analytics` database.
*   Grant #3 does **not** match – even though the token has a group called `viewer`, the grant is for tenant `risk` and the token is from tenant `quants`. Tenants are strictly isolated.

### Full permission matrix (example setup)

| **Tenant** | **Group** | **User(s)** | **Grants on `analytics` db** | **Effective access** |
| --- | --- | --- | --- | --- |
| quants | `trader` | alice | `read`, `write` | Query, search, insert, create tables. Cannot delete. |
| quants | `viewer` | alice, bob | `read` | Query and search only. Cannot insert or delete. |
| risk | `viewer` | charlie | `read` | Query and search only. Completely isolated from quants grants. |
| manager | `admin` | root | _system\_admin_ (through environment variables) | Full access to everything. Can add/delete grants. Bypasses all ACL checks. |

### Key rules

*   **Grants are never assigned to individual users.** A grant applies to any token whose `tenant` and `groups` claims match.
*   **A token with multiple groups gets combined access.** KDB.AI checks all of the token's groups against all grants. If `trader` has `read` + `write` and `viewer` has `read`, a token in both groups gets `read` + `write`.
*   **Cross-tenant isolation is strict.** A grant for tenant `quants` never applies to a token from tenant `risk`, even if the group name is the same.
*   **`write` implies `read`; `delete` implies `read`; but `delete` does NOT imply `write`.**

Managing grants
---------------

Grant management is restricted to tokens that have `system_admin` privileges (that is, tokens whose `tenant` and `groups` claims match the `ACL_SYSTEM_ADMIN_TENANT` and `ACL_SYSTEM_ADMIN_GROUP` environment variables). Every grant endpoint requires this token in the `Authorization: Bearer` header.

### API endpoints

| **Operation** | **Method** | **Endpoint** |
| --- | --- | --- |
| Add grants | `POST` | `/api/v2/admin/grants` |
| List all grants | `GET` | `/api/v2/admin/grants` |
| Get grant by ID | `GET` | `/api/v2/admin/grants/{id}` |
| Delete grant | `DELETE` | `/api/v2/admin/grants/{id}` |

### Grant parameters

The `POST` body is a JSON **array** of grant objects:

| **Parameter** | **Type** | **Required** | **Notes** |
| --- | --- | --- | --- |
| `resource` | string | Yes | `database`, `table`, or `admin` |
| `databaseName` | string | Yes | Target database name |
| `table` | string | No | Target table (required when resource is `table`) |
| `tenant` | string | Yes | Tenant ID (must match the `tenant` claim in the JWT) |
| `groups` | list of strings | Yes | Group names from the IdP |
| `actions` | list of strings | Yes | `read`, `write`, `delete`, or `system_admin` |

KDBAI Python Client
-------------------

The KDB.AI Python client supports OAuth 2.0 token management with automatic token refresh. It reads the OAuth 2.0 configuration from a YAML file whose path is provided when the session is created.

### OAuth configuration file

The client will read OAuth 2.0 settings from a YAML configuration file that supports three configuration modes, depending on how tokens are obtained:

1.   **Resource owner password** (`grant_type: password`) – obtain a token for a user.

2.   **Client credentials** (`grant_type: client_credentials`) – machine-to-machine authentication.

3.   **Pre-issued tokens** (no `grant_type`) – tokens are acquired externally and supplied to the client.

Create a YAML configuration file containing the following OAuth 2.0 details required by the client:

```
# --- Required ---
token_url: "https://idp.example.com/tenants/quants/protocol/openid-connect/token"
client_id: "kdbai-service"
grant_type: "password"  # or "client_credentials"

# --- Tokens (written by your login script or by the client) ---
access_token: "<your-access-token>"
refresh_token: "<your-refresh-token>"

# --- Optional: confidential client (supports client_credentials grant) ---
client_secret: ""

# --- Optional: resource owner password grant ---
username: ""
password: ""
```

**OAuth 2.0 Configuration Fields**

| **Field** | **Required** | **Description** |
| --- | --- | --- |
| `token_url` | Yes | Your IdP's token endpoint. Required for the client to acquire or refresh tokens. |
| `client_id` | Yes | The OAuth 2.0 client ID registered in your IdP |
| `grant_type` | Yes | The OAuth 2.0 grant type to use (`password` or `client_credentials`) |
| `access_token` | Yes | Current access token |
| `refresh_token` | No | Current refresh token. Enables the client to obtain new access tokens automatically. |
| `client_secret` | No | Client secret for confidential clients. Enables the `client_credentials` grant. |
| `username` | No | Username for `password` grant |
| `password` | No | Password for `password` grant |

From the repository root, run:

```
uv run --with-editable kdbai-python-client --python=3.13 python -c '
import kdbai_client as kdbai

session = kdbai.Session(endpoint="http://localhost:8082", oauth={'enabled':True, 'config_file':"<path to config file>"})
print(session.version())
'
```

### Initial token acquisition

The initial `access_token` and `refresh_token` can be obtained using a login script that performs the appropriate OAuth 2.0 flow against your IdP and writes the tokens to the configuration file in the YAML format shown above. The KDB.AI client then reads these tokens and handles refresh from that point forward.

The client also supports two built-in grant types that can acquire tokens directly, without a separate script:

| **Method** | **Grant type** | **Notes** |
| --- | --- | --- |
| **Client credentials** | `client_credentials` | Requires a confidential client (`client_secret` must be set). Tokens typically do not include a refresh token – the client re-acquires when expired. |
| **Resource owner password** | `password` | Requires `username` and `password`. |

### Token refresh

Once tokens are in the config file, the Python client handles the token lifecycle automatically:

1.   The client sends a request to KDB.AI with the current `access_token`
2.   If the server rejects the token (expired or invalid), this triggers the refresh flow
3.   The client re-acquires a token based on the `grant_type` in the config file
4.   The updated tokens are written back to the config file
5.   If refresh fails, the user must re-run their login script to obtain new tokens
