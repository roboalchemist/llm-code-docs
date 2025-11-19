# Source: https://docs.meshconnect.com/advanced/mesh-managed-tokens.md

# Mesh Managed Tokens (MMT)

> This guide explains how to implement Mesh Managed Tokens (MMT), our recommended approach for handling user authentication to create a secure and seamless return user experience.

# Overview

Mesh’s Managed Tokens system (MMT) is a service designed to simplify how clients manage user authentication tokens. Rather than requiring clients to handle the lifecycle of access and refresh tokens for each integration, MMT securely stores and manages tokens on behalf of the client. Clients receive a persistent `TokenId` that can be used to interact with exchange brokers via Mesh APIs without needing to refresh or re-authenticate.

***

## Benefits

* **Simplified Token Lifecycle**: Clients do not need to handle the storage or refresh logic for tokens directly.
* **Streamlined UX**: End-users can skip repetitive authentication steps, enhancing the embedded experience.
* **Persistent Access** (where supported): For broker integrations that provide long-lived or refreshable tokens (e.g., Coinbase), the same `TokenId` remains valid indefinitely. For integrations with expiring tokens (e.g., Binance), users may still need to re-authenticate, but the `TokenId` remains unchanged, allowing clients to reuse it without needing to update backend storage.
* **Seamless Re-authentication**: When a token expires (e.g., Binance), Mesh Link will prompt the user to re-authenticate. Once complete, the same `TokenId` is revalidated and continues to work as before—reducing backend complexity for clients.
* **Integration-Agnostic**: Works across different auth methods (OAuth, credentials-based) with no added client-side complexity.

***

## Security Considerations

While MMT streamlines token handling and unlocks powerful functionality, it also requires thoughtful security practices given its expanded role in managing user access. Mesh has designed the system with robust safeguards to ensure token integrity and data protection, including:

* **Encrypted Storage**: All tokens are encrypted at rest using modern encryption standards.
* **Scoped Access**: Each `TokenId` is tied to the permission scope (read or write) associated with the API key. Unauthorized operations (e.g., calling a write endpoint with a read-scoped token) will be rejected.
* **Client-Level Isolation**: Each `TokenId` is also scoped to a specific `clientId`. Even if the same end user connects the same integration account across multiple client apps, the tokens are isolated and not shared across clients.
* **User-Level Isolation**: Each `TokenId` is unique to a specific `EndUserId` and integration.
* **Token Revocation**: Clients can revoke a `TokenId`, permanently disabling access and triggering a secure deletion process. There is no path to restore a revoked token.

***

# How to Implement MMT

## 1. Enable Token Management for Your Client

Ensure MMT is enabled for your `clientId` by contacting your Mesh Customer Success representative.

Once enabled, all authentication flows will return a `TokenId` in place of a raw access token.

***

## 2. Obtain a `TokenId`

When a user authenticates with their exchange or wallet account, you will receive the SDK event `integrationConnected`, which contains an object like this:

```json  theme={null}

{
  "accountTokens": [
    {
      "account": {
        "accountName": "Coinbase wallets",
        "fund": 0.90
      },
      "tokenId": "dc16b40f-746c-4701-xxxx-ac37eccc766d"
    }
  ]
}

```

Save the `tokenId` for future use with Mesh APIs.

***

## 3. Reuse TokenIds with Mesh SDK

You can pass existing `TokenId` (or multiple, if available) into the Mesh Link SDK to skip re-authentication and launch users directly into the transfer or portfolio flow.

**SDK Setup Example:**

```jsx  theme={null}
javascript
CopyEdit
const link = new MeshLink({
  clientId: "<your-client-id>",
  linkToken: "<link-token>",
  accountTokens: [
    {
      tokenId: "dc16b40f-746c-4701-xxxx-ac37eccc766d",
      type: "Coinbase"
    }
  ]
});

```

This enables seamless repeat usage without forcing the user to re-authenticate.

If the associated token is still valid, users will skip auth and land in the desired experience. If the token has expired (e.g., Binance), Link will prompt the user to re-authenticate and automatically reactivate the same `TokenId` upon success.

***

### 4. Token Lifecycle and Behavior

| Scenario                                                           | Result                                                                                                              |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| **Same user reconnects with same integration**                     | Returns same `TokenId`                                                                                              |
| **Different user connects to same integration**                    | Returns a new `TokenId`                                                                                             |
| **Same user connects with different scopes (e.g., read vs write)** | Returns distinct `TokenId`s per scope                                                                               |
| **Write endpoint called using read-only `TokenId`**                | API returns a scope mismatch error                                                                                  |
| **Token revoked by client**                                        | Associated access is permanently disabled and Mesh also deletes the token physically, without any way to restore it |

***

## Supported Integrations (as of today)

* **Coinbase** (OAuth)
* **Binance** (Username/Password)
* *Note: connections with self-custody wallets are maintained on subsequent sessions without the need for handling tokens (unless the user actively kills the connection in their wallet app). This means the same smooth return user journey is achieved for wallet transactions.*

For testing with sandbox accounts, see [our sandbox guide](https://docs.meshconnect.com/guides/digital-asset-managed-transfers-with-sdk-integration-guide).

***

## Key Takeaways

* The `TokenId` is a powerful abstraction. It should be stored and transmitted securely.
* MMT is backward-compatible with all Mesh API endpoints that accept `AuthToken`.
* Always ensure scope consistency when re-using a `TokenId`.

***
