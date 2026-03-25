# Drip Documentation

Source: https://docs.drip.re/llms-full.txt

---

# Find Account

Source: https://docs.drip.re/api-reference/accounts/find-account

https://api.drip.re/docs/json get /api/v1/accounts/find
Find any DRIP user their ID by their username, email, wallet address, or twitter/discord id

# Get App Authorized Realms

Source: https://docs.drip.re/api-reference/apps/get-app-authorized-realms

https://api.drip.re/docs/json get /api/v1/apps/{appId}/authorized-realms
Get the realms that an app is authorized to access. Can only be used by the app itself.

# Get App Installs

Source: https://docs.drip.re/api-reference/apps/get-app-installs

https://api.drip.re/docs/json get /api/v1/realms/{realmId}/apps/{appId}/installs
Get paginated list of realms that have installed this app

# Search App Authorized Realms

Source: https://docs.drip.re/api-reference/apps/search-app-authorized-realms

https://api.drip.re/docs/json get /api/v1/apps/{appId}/authorized-realms/search
Search for realms that an app is authorized to access. Can only be used by the app itself.

# Authentication

Source: https://docs.drip.re/api-reference/authentication

Learn how to authenticate with the DRIP API using API keys and bearer tokens

The DRIP API uses API key authentication. You'll need to include your API key in the Authorization header of every request.

## Getting Your API Key

1. Log into your DRIP dashboard
2. Navigate to **Settings** > **API Keys**
3. Click **Generate New API Key**
4. Copy and securely store your API key

<Warning>
  Keep your API keys secure and never expose them in client-side code. Treat them like passwords.
</Warning>

## Authentication Header

Include your API key in the `Authorization` header using the Bearer token format:

```bash theme={"dark"}
Authorization: Bearer YOUR_API_KEY_HERE
```

## Example Request

<CodeGroup>
  ```bash cURL theme={"dark"}
  curl -X GET "https://api.drip.re/api/v1/realms/YOUR_REALM_ID" \
    -H "Authorization: Bearer YOUR_API_KEY_HERE" \
    -H "Content-Type: application/json"
  ```

  ```javascript JavaScript theme={"dark"}
  const response = await fetch('https://api.drip.re/api/v1/realms/YOUR_REALM_ID', {
    headers: {
      'Authorization': 'Bearer YOUR_API_KEY_HERE',
      'Content-Type': 'application/json'
    }
  });
  ```

  ```python Python theme={"dark"}
  import requests

  headers = {
      'Authorization': 'Bearer YOUR_API_KEY_HERE',
      'Content-Type': 'application/json'
  }

  response = requests.get('https://api.drip.re/api/v1/realms/YOUR_REALM_ID', headers=headers)
  ```

</CodeGroup>

## API Key Permissions

API keys inherit the permissions of the user who created them. Ensure your account has the necessary permissions for the operations you want to perform:

* **Read permissions**: View realm data, member information, point balances
* **Write permissions**: Update member balances, create quests, manage store items
* **Admin permissions**: Full realm management capabilities

## Testing Authentication

You can test your authentication by making a simple request to get your realm information:

```bash theme={"dark"}
curl -X GET "https://api.drip.re/api/v1/realms/YOUR_REALM_ID" \
  -H "Authorization: Bearer YOUR_API_KEY_HERE"
```

A successful response will return your realm data. An authentication error will return a `401 Unauthorized` status.

## Security Best Practices

<CardGroup>
  <Card title="Environment Variables" icon="shield-check">
    Store API keys in environment variables, never in your source code
  </Card>

  <Card title="Rotate Keys" icon="arrows-rotate">
    Regularly rotate your API keys and revoke unused ones
  </Card>

  <Card title="Scope Permissions" icon="lock">
    Use accounts with minimal necessary permissions for API operations
  </Card>

  <Card title="Monitor Usage" icon="chart-line">
    Monitor API key usage to detect unauthorized access
  </Card>
</CardGroup>

# Batch update point balances for multiple credentials by their identifiers

Source: https://docs.drip.re/api-reference/credentials-balances/batch-update-point-balances-for-multiple-credentials-by-their-identifiers

https://api.drip.re/docs/json patch /api/v1/realms/{realmId}/credentials/transaction
Batch update point balances for multiple credentials by their identifiers

# Transfer points from one credential to another by their identifiers

Source: https://docs.drip.re/api-reference/credentials-balances/transfer-points-from-one-credential-to-another-by-their-identifiers

https://api.drip.re/docs/json patch /api/v1/realms/{realmId}/credentials/transfer
Transfer points from one credential to another by their identifiers

# Update point balance for a credential by its identifier (email, wallet, discord ID, etc)

Source: https://docs.drip.re/api-reference/credentials-balances/update-point-balance-for-a-credential-by-its-identifier-email-wallet-discord-id-etc

https://api.drip.re/docs/json patch /api/v1/realms/{realmId}/credentials/balance
Update point balance for a credential by its identifier (email, wallet, discord ID, etc)

# Create a social credential

Source: https://docs.drip.re/api-reference/credentials/create-a-social-credential

https://api.drip.re/docs/json post /api/v1/realms/{realmId}/credentials/social
Create a social credential (Twitter, Discord, etc.) - can be unlinked or linked to an account

# Create a wallet credential

Source: https://docs.drip.re/api-reference/credentials/create-a-wallet-credential

https://api.drip.re/docs/json post /api/v1/realms/{realmId}/credentials/wallet
Create a wallet credential - can be unlinked or linked to an account

# Delete a non-verified credential (linked or unlinked, only if no balances exist)

Source: https://docs.drip.re/api-reference/credentials/delete-a-non-verified-credential-linked-or-unlinked-only-if-no-balances-exist

https://api.drip.re/docs/json delete /api/v1/realms/{realmId}/credentials/
Delete a non-verified credential (linked or unlinked, only if no balances exist)

# Find non-verified credential by type and value (twitter-id uses oauthAccountId, wallet uses address, email uses email)

Source: https://docs.drip.re/api-reference/credentials/find-non-verified-credential-by-type-and-value-twitter-id-uses-oauthaccountid-wallet-uses-address-email-uses-email

https://api.drip.re/docs/json get /api/v1/realms/{realmId}/credentials/find
Find non-verified credential by type and value (twitter-id uses oauthAccountId, wallet uses address, email uses email)

# Link a credential to an account (transfers balances)

Source: https://docs.drip.re/api-reference/credentials/link-a-credential-to-an-account-transfers-balances

https://api.drip.re/docs/json post /api/v1/realms/{realmId}/credentials/link
Link a credential to an account (transfers balances)

# Update custom metadata for a ghost credential by identifier

Source: https://docs.drip.re/api-reference/credentials/update-custom-metadata-for-a-ghost-credential-by-identifier

https://api.drip.re/docs/json patch /api/v1/realms/{realmId}/credentials/metadata
Update custom metadata for a ghost credential by identifier

# Archive Currency

Source: https://docs.drip.re/api-reference/currencies/archive-currency

https://api.drip.re/docs/json delete /api/v1/realms/{realmId}/currencies/{currencyId}
Archive a currency

# Create Currency

Source: https://docs.drip.re/api-reference/currencies/create-currency

https://api.drip.re/docs/json post /api/v1/realms/{realmId}/currencies
Create a new currency in a realm

# Get Currencies

Source: https://docs.drip.re/api-reference/currencies/get-currencies

https://api.drip.re/docs/json get /api/v1/realms/{realmId}/currencies
Get all currencies in a realm with pagination, search, filtering, and sorting

# Get Currency

Source: https://docs.drip.re/api-reference/currencies/get-currency

https://api.drip.re/docs/json get /api/v1/realms/{realmId}/currencies/{currencyId}
Get a currency by id

# Unarchive Currency

Source: https://docs.drip.re/api-reference/currencies/unarchive-currency

https://api.drip.re/docs/json post /api/v1/realms/{realmId}/currencies/{currencyId}/unarchive
Unarchive a currency

# Update Currency

Source: https://docs.drip.re/api-reference/currencies/update-currency

https://api.drip.re/docs/json patch /api/v1/realms/{realmId}/currencies/{currencyId}
Update a currency in a realm

# Update Currency Metadata

Source: https://docs.drip.re/api-reference/currencies/update-currency-metadata

https://api.drip.re/docs/json patch /api/v1/realms/{realmId}/currencies/{currencyId}/metadata
Update the metadata of a currency

# API Introduction

Source: https://docs.drip.re/api-reference/introduction

Welcome to the DRIP API documentation. Learn about our current and legacy APIs.

# DRIP API Introduction

Welcome to the DRIP API documentation! DRIP provides powerful APIs to help you build engaging community experiences with points, quests, games, and Web3 integrations.

## Current API (Recommended)

Our **current API** is the modern, feature-complete solution for integrating with the DRIP platform. It provides:

* ✅ **Full Feature Set** - Access to all DRIP platform capabilities
* ✅ **Modern Architecture** - RESTful design with comprehensive OpenAPI documentation
* ✅ **Active Development** - Regular updates and new features
* ✅ **Better Performance** - Optimized endpoints and response times
* ✅ **Enhanced Security** - Latest authentication and authorization methods
* ✅ **Comprehensive Documentation** - Interactive API playground and detailed examples

**Base URL:** `https://api.drip.re/api/v1`

## Legacy API (Deprecated)

Our **legacy API** is maintained for backward compatibility but is scheduled for deprecation:

* ⚠️ **Deprecated** - No new features will be added
* ⚠️ **Limited Support** - Bug fixes only, no feature enhancements
* ⚠️ **No Assistance** - We do not provide help with implementing the legacy API
* ⚠️ **Scheduled Removal** - Will be discontinued in the future
* ⚠️ **Migration Required** - Please migrate to the current API

<Warning>
  The legacy API will be discontinued in the future. Please migrate your applications to the current API to avoid service disruption. We will provide advance notice before discontinuation.
</Warning>

## Getting Started

### 1. Read the Developer Guide

Before diving into the API reference, we recommend reading our comprehensive [Developer Guide](/developer/quickstart) which covers:

* [Quick Start](/developer/quickstart) - Get up and running in minutes
* [Authentication](/developer/authentication) - Learn about API keys and security
* [Core Concepts](/developer/core-concepts) - Understand DRIP's data model
* [API Clients](/developer/api-clients) - Manage your API credentials
* [Best Practices](/developer/best-practices) - Tips for optimal integration

### 2. Choose Your API

* **New Projects**: Use the [Current API](#current-api-recommended) for all new integrations
* **Existing Projects**: Plan your [migration from Legacy API](#migration-guide) to Current API

### 3. Get Your API Key

1. Visit the [DRIP Dashboard](https://app.drip.re)
2. Navigate to your realm settings
3. Generate an API client in the [API Clients](/developer/api-clients) section
4. Copy your API key and keep it secure

## Migration Guide

If you're currently using the legacy API, here's how to migrate:

### Step 1: Review Changes

* Compare legacy endpoints with current API equivalents
* Update authentication method to use Bearer tokens
* Review response format changes

### Step 2: Update Base URL

```diff theme={"dark"}
- https://legacy-api.drip.re/v1
+ https://api.drip.re/api/v1
```

### Step 3: Update Authentication

```diff theme={"dark"}
- X-API-Key: your-api-key
+ Authorization: Bearer your-api-key
```

### Step 4: Test & Deploy

* Test all endpoints in our interactive playground
* Update error handling for new response formats
* Deploy and monitor your integration

<Tip>
  Need help with migration? Check out our [migration examples](/developer/examples) or reach out to our [support team](https://discord.gg/dripchain).
</Tip>

## Support & Community

* 📚 **Documentation**: Browse our complete [Developer Guide](/developer/quickstart)
* 💬 **Discord**: Join our [community Discord](https://discord.gg/dripchain) for support
* 🎮 **Interactive Playground**: Test endpoints directly in the API reference
* 📧 **Contact**: Reach out through our support channels

## What's Next?

Ready to start building? Here are your next steps:

1. **Explore the API**: Browse the complete API reference below
2. **Try the Playground**: Test endpoints interactively
3. **Build Something Amazing**: Create engaging experiences with DRIP

# Batch Update Member Balance Of A Currency

Source: https://docs.drip.re/api-reference/realm-members-balances/batch-update-member-balance-of-a-currency

https://api.drip.re/docs/json patch /api/v1/realms/{realmId}/members/transaction
Batch update the balances of multiple DRIP users in a realm by their drip ids and currency id. All updates are applied in a single transaction, so if any update fails, the entire batch will fail.

# Transfer Member Balance Of A Currency

Source: https://docs.drip.re/api-reference/realm-members-balances/transfer-member-balance-of-a-currency

https://api.drip.re/docs/json patch /api/v1/realms/{realmId}/members/{dripId}/transfer
Transfer points from one DRIP user to another in a realm by their drip ids and currency id

# Update Member Balance Of A Currency

Source: https://docs.drip.re/api-reference/realm-members-balances/update-member-balance-of-a-currency

https://api.drip.re/docs/json patch /api/v1/realms/{realmId}/members/{dripId}/balance
Update the balance of a DRIP user in a realm by their drip id and currency id

# Get Realm Member Leaderboard

Source: https://docs.drip.re/api-reference/realm-members/get-realm-member-leaderboard

https://api.drip.re/docs/json get /api/v1/realms/{realmId}/members/leaderboard
Get the leaderboard of a realm by their currency id

# List Realm Members

Source: https://docs.drip.re/api-reference/realm-members/list-realm-members

https://api.drip.re/docs/json get /api/v1/realms/{realmId}/members/
List members of a realm with optional pagination, search, and sorting.

# Search Realm Member

Source: https://docs.drip.re/api-reference/realm-members/search-realm-member

https://api.drip.re/docs/json get /api/v1/realms/{realmId}/members/search
Search for a DRIP user in a realm by their drip id, twitter id, discord id, wallet address, email, or username

# Update Member Metadata

Source: https://docs.drip.re/api-reference/realm-members/update-member-metadata

https://api.drip.re/docs/json patch /api/v1/realms/{realmId}/members/{dripId}/metadata
Update custom metadata for a realm member

# Get Realm

Source: https://docs.drip.re/api-reference/realms/get-realm

https://api.drip.re/docs/json get /api/v1/realms/{realmId}
Get a realm by id

# Accept a pending shared currency

Source: https://docs.drip.re/api-reference/shared-currency/accept-a-pending-shared-currency

https://api.drip.re/docs/json post /api/v1/realms/{realmId}/currencies/{currencyId}/share/accept
Accept a pending shared currency

# Get all the pending requests for a realm (not by currency)

Source: https://docs.drip.re/api-reference/shared-currency/get-all-the-pending-requests-for-a-realm-not-by-currency

https://api.drip.re/docs/json get /api/v1/realms/{realmId}/shares/pending
Get all the pending requests for a realm (not by currency)

# List all child realms that use a parent's currency

Source: https://docs.drip.re/api-reference/shared-currency/list-all-child-realms-that-use-a-parents-currency

https://api.drip.re/docs/json get /api/v1/realms/{realmId}/currencies/{currencyId}/shares
List all child realms that use a parent's currency

# Reject a pending shared currency

Source: https://docs.drip.re/api-reference/shared-currency/reject-a-pending-shared-currency

https://api.drip.re/docs/json post /api/v1/realms/{realmId}/currencies/{currencyId}/share/reject
Reject a pending shared currency

# Remove a shared currency from a child realm

Source: https://docs.drip.re/api-reference/shared-currency/remove-a-shared-currency-from-a-child-realm

https://api.drip.re/docs/json delete /api/v1/realms/{realmId}/currencies/{currencyId}/remove
Remove a shared currency from a child realm

# Share a currency with another realm

Source: https://docs.drip.re/api-reference/shared-currency/share-a-currency-with-another-realm

https://api.drip.re/docs/json post /api/v1/realms/{realmId}/currencies/{currencyId}/share
Share a currency with another realm

# Un-share a currency from a child realm

Source: https://docs.drip.re/api-reference/shared-currency/un-share-a-currency-from-a-child-realm

https://api.drip.re/docs/json delete /api/v1/realms/{realmId}/currencies/{currencyId}/shares/{childRealmId}
Un-share a currency from a child realm

# Add a new config to an existing activation

Source: https://docs.drip.re/api-reference/web3-activations-configs/add-a-new-config-to-an-existing-activation

https://api.drip.re/docs/json post /api/v1/realms/{realmId}/web3/activations/{activationId}/configs
Add a new config to an existing WEB3 activation

# Delete a config from an activation

Source: https://docs.drip.re/api-reference/web3-activations-configs/delete-a-config-from-an-activation

https://api.drip.re/docs/json delete /api/v1/realms/{realmId}/web3/activations/{activationId}/configs/{configId}
Delete a config from an existing WEB3 activation

# Get all configs for a given activation

Source: https://docs.drip.re/api-reference/web3-activations-configs/get-all-configs-for-a-given-activation

https://api.drip.re/docs/json get /api/v1/realms/{realmId}/web3/activations/{activationId}/configs
Get all configs for a given WEB3 activation

# Update an existing config on an activation

Source: https://docs.drip.re/api-reference/web3-activations-configs/update-an-existing-config-on-an-activation

https://api.drip.re/docs/json patch /api/v1/realms/{realmId}/web3/activations/{activationId}/configs/{configId}
Update an existing config on an existing WEB3 activation

# Claim Web3 Balance

Source: https://docs.drip.re/api-reference/web3-activations-members/claim-web3-balance

https://api.drip.re/docs/json post /api/v1/realms/{realmId}/web3/members/{dripId}/claim
Claim Web3 Balance of a specific member of a specific activation

# Get member web3 balances data

Source: https://docs.drip.re/api-reference/web3-activations-members/get-member-web3-balances-data

https://api.drip.re/docs/json get /api/v1/realms/{realmId}/web3/members/{dripId}/balances
Get member web3 balances data by a specific member of a specific activation

# Get user ERC721 NFTs

Source: https://docs.drip.re/api-reference/web3-activations-members/get-user-erc721-nfts

https://api.drip.re/docs/json get /api/v1/realms/{realmId}/web3/members/{dripId}/nfts
Get user ERC721 NFTs with pagination by a specific member of a specific activation

# Link NFTs

Source: https://docs.drip.re/api-reference/web3-activations-members/link-nfts

https://api.drip.re/docs/json post /api/v1/realms/{realmId}/web3/members/{dripId}/nfts/link
Link NFTs of a specific member of a specific activation to another activation

# Unlink NFTs

Source: https://docs.drip.re/api-reference/web3-activations-members/unlink-nfts

https://api.drip.re/docs/json post /api/v1/realms/{realmId}/web3/members/{dripId}/nfts/unlink
Unlink NFTs of a specific member of a specific activation from another activation

# Create an activation

Source: https://docs.drip.re/api-reference/web3-activations/create-an-activation

https://api.drip.re/docs/json post /api/v1/realms/{realmId}/web3/activations
Create a WEB3 activation for a realm

# Credit NFTs

Source: https://docs.drip.re/api-reference/web3-activations/credit-nfts

https://api.drip.re/docs/json post /api/v1/realms/{realmId}/web3/activations/{activationId}/credit
Credit NFTs of a specific activation by a specific currency

# Delete an activation

Source: https://docs.drip.re/api-reference/web3-activations/delete-an-activation

https://api.drip.re/docs/json delete /api/v1/realms/{realmId}/web3/activations/{activationId}
Delete a WEB3 activation of a realm

# Get all activations

Source: https://docs.drip.re/api-reference/web3-activations/get-all-activations

https://api.drip.re/docs/json get /api/v1/realms/{realmId}/web3/activations
Get all WEB3activations for a realm

# Get an activation by ID

Source: https://docs.drip.re/api-reference/web3-activations/get-an-activation-by-id

https://api.drip.re/docs/json get /api/v1/realms/{realmId}/web3/activations/{activationId}
Get a WEB3 activation by ID

# Get balance for a single NFT

Source: https://docs.drip.re/api-reference/web3-activations/get-balance-for-a-single-nft

https://api.drip.re/docs/json get /api/v1/realms/{realmId}/web3/activations/{activationId}/nfts/{tokenId}/balance
Get balance for a single NFT of a specific activation

# Link collections

Source: https://docs.drip.re/api-reference/web3-activations/link-collections

https://api.drip.re/docs/json post /api/v1/realms/{realmId}/web3/activations/{sourceActivationId}/link
Link collections of a specific activation to another activation

# Re-sync an activation

Source: https://docs.drip.re/api-reference/web3-activations/re-sync-an-activation

https://api.drip.re/docs/json post /api/v1/realms/{realmId}/web3/activations/{activationId}/sync
Re-sync a WEB3 activation for a realm, which will re-sync all the NFT data and ownership

# Unlink collections

Source: https://docs.drip.re/api-reference/web3-activations/unlink-collections

https://api.drip.re/docs/json post /api/v1/realms/{realmId}/web3/activations/{sourceActivationId}/unlink
Unlink collections of a specific activation from another activation

# Get details for a specific NFT

Source: https://docs.drip.re/api-reference/web3-data-collections/get-details-for-a-specific-nft

https://api.drip.re/docs/json get /api/v1/web3-data/collections/{contractAddress}/nfts/{tokenId}
Get details for a specific NFT by its contract address and token id

# Get listings for a collection

Source: https://docs.drip.re/api-reference/web3-data-collections/get-listings-for-a-collection

https://api.drip.re/docs/json get /api/v1/web3-data/collections/{contractAddress}/listings
Get listings for a collection by its contract address

# Get listings for a NFT

Source: https://docs.drip.re/api-reference/web3-data-collections/get-listings-for-a-nft

https://api.drip.re/docs/json get /api/v1/web3-data/collections/{contractAddress}/nfts/{tokenId}/listings
Get listings for a NFT by its contract address and token id

# Get metadata for a collection

Source: https://docs.drip.re/api-reference/web3-data-collections/get-metadata-for-a-collection

https://api.drip.re/docs/json get /api/v1/web3-data/collections/{contractAddress}
Get metadata for a collection by its contract address

# Get NFTs in a collection

Source: https://docs.drip.re/api-reference/web3-data-collections/get-nfts-in-a-collection

https://api.drip.re/docs/json get /api/v1/web3-data/collections/{contractAddress}/nfts
Get all NFTs in a collection by their contract address

# Get metadata for a token

Source: https://docs.drip.re/api-reference/web3-data-tokens/get-metadata-for-a-token

https://api.drip.re/docs/json get /api/v1/web3-data/tokens/{tokenAddress}
Get metadata for a token by its address

# Get ERC1155 NFTs owned by a wallet

Source: https://docs.drip.re/api-reference/web3-data-wallets/get-erc1155-nfts-owned-by-a-wallet

https://api.drip.re/docs/json get /api/v1/web3-data/wallets/{walletAddress}/nfts
Get ERC1155 NFTs owned by a wallet by its address

# Get listings for a wallet

Source: https://docs.drip.re/api-reference/web3-data-wallets/get-listings-for-a-wallet

https://api.drip.re/docs/json get /api/v1/web3-data/wallets/{walletAddress}/listings
Get listings for a wallet by its address

# Get token balances for a wallet

Source: https://docs.drip.re/api-reference/web3-data-wallets/get-token-balances-for-a-wallet

https://api.drip.re/docs/json get /api/v1/web3-data/wallets/{walletAddress}/token-balances
Get token balances for a wallet by its address

# Overview

Source: https://docs.drip.re/apps/overview

Understand the DRIP apps ecosystem and how apps fit into your workspace

Apps extend DRIP with modular capabilities that you can install into one or more realms. Each app runs independently, requests specific permissions, and interacts with DRIP services through stable APIs.

* Apps can be built by DRIP or third‑party developers
* You control which realms an app is installed to
* Permissions are scoped per app and per realm
* Multiple apps can work together to create end‑to‑end workflows

<Info>
  Think of apps as building blocks: install what you need, where you need it, and keep everything permissioned and auditable.
</Info>

## Install apps

<Steps>
  <Step title="Open the App Store">
    Browse available apps maintained by DRIP and third parties. Use categories and search to find what you need.
  </Step>

  <Step title="Review details and permissions">
    Check the app description, capabilities, and requested scopes. Confirm it supports your target realm(s).
  </Step>

  <Step title="Install to realm(s)">
    Choose one or more realms for installation. You can adjust permissions per realm during setup.
  </Step>

  <Step title="Configure settings">
    Complete any required configuration (permissions, channels, roles, webhooks, etc.). Test in a staging realm when possible.
  </Step>

  <Step title="Maintain, update, or uninstall">
    Keep apps up to date. If an app is no longer needed, uninstall it from specific realms or globally.
  </Step>
</Steps>

<Info>
  Tip: Start with a single realm to validate configuration, then roll out to additional realms.
</Info>

## Build your own

Build custom functionality that integrates with DRIP using our APIs and app model. Your app chooses its scopes, installs to specific realms, and can be published for others to use.

<CardGroup>
  <Card title="App Development" icon="rocket" href="/developer/app-development">
    Concepts, capabilities, and lifecycle of DRIP apps.
  </Card>

  <Card title="Multi‑Realm Apps" icon="globe" href="/developer/multi-realm-apps">
    Patterns for building apps that span multiple realms.
  </Card>

  <Card title="App Store Publishing" icon="cart-shopping" href="/developer/app-store">
    Requirements, assets, and submission process.
  </Card>
</CardGroup>

<Info>
  For implementation details, see authentication, API clients, rate limits, and examples in the developer docs.
</Info>

## DRIP Official Apps

First‑party apps built and maintained by DRIP. They follow the same installation and permissions model, with opinionated defaults and deep product integration.

<CardGroup>
  <Card title="Discord Bot" icon="discord" href="/bot-documentation/home">
    Moderation, quests, points, and community engagement features.
  </Card>

  <Card title="Burn Ghosts Activity" icon="ghost" href="/burn-ghosts-activity/home">
    Competitive tournaments with 9 mini-games and token rewards.
  </Card>
</CardGroup>

# Overview

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard

Navigate the Admin Dashboard to make changes to your community and get Drip support

The Admin dashboard can be found in the `#🛠┆admin` channel and is used to make changes to Drip Rewards in your community. You can also access the Drip Support Discord and Documentation via the dashboard. Click on the various buttons in the embed to use the dashboard:

* ⚡️**Create Channels:** This will create some starter channels for the bot. You will also get to choose which channels you want to create.

* 🔍 **Manage Points:** Lookup information about a community member held by Drip Rewards. You can also add or remove points from members this way.

* ⚙️ **Settings:** This will open the settings menu for the bot where you can edit the settings for your server.

* **Feedback:** Submit feedback directly to the Drip Rewards team via a form

* 📣 **Get Support:** This will send you to our support server where you can ask questions or give feedback.

* 📚 **View Docs:** This will send you to our support documentation where you can read more about Drip Rewards

<Frame>
  <img />
</Frame>

# Overview

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings

Settings is where you can configure the bot to your server needs

## Accessing Settings

You can access Settings for your community by clicking the `⚙️ Settings` option in the `🛠┆admin` channel

<Frame>
  <img />
</Frame>

The following embed will appear:

<Frame>
  <img />
</Frame>

If you don't have an `🛠┆admin` channel yet, type [`/start`](/).

## Using the Settings

Drip Rewards has many settings to play with, all can used without having to leave Discord. Here is a small overview of the many features.

<CardGroup>
  <Card title="✨ Points Settings">
    Brand your servers Points or mass credit
  </Card>

  <Card title="📈">View stats about your server</Card>

  <Card title="🎲 Game Settings">Edit settings for the casino</Card>

  <Card title="🗺">Edit the Quest settings for your community</Card>

  <Card title="🔒">
    Delegate access to trusted members by setting up some roles
  </Card>

  <Card title="👥 Member Roles">Assign roles for member achievements</Card>

  <Card title="🔥 WEB3 Settings">Set up WEB3 features</Card>

  <Card title="🏳️ White Label">Customize the bot to suit your brand</Card>

  <Card title="🔌 Developer API">
    Extend your server's Points beyond Discord
  </Card>
</CardGroup>

# Overview

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/admin-permissions

Delegate access to trusted members by setting up some roles

## Retrieve Server Permissions

You can view your server permissions by clicking the `⚙️ Permissions` option in the [settings menu](/admin-settings/admin-dashboard/admin-settings).

If you have opened the **Permissions**, you will see an embed where all different roles are displayed.

### Available Roles

* 👑 **Co-Admin**: Assign a role to access critical bot settings.

* ✨ **Magic Embeds**: Assign role to create and edit Magic Embeds

* 📦 **Store Items**: Assign role to create and edit Store Items.

* 🎁 **Prizes**: Assign role to create and edit Prizes.

* 💰 **Economy**: Assign role to give or take Points in Magic Embeds.

* 🗳️ **Voting**: Assign role to create and edit Voting Embeds.

* 🏹 **Admin Quests:** Assign role to create admin quests.

<Frame>
  <img />
</Frame>

## Assign Roles

For each of the [available roles](/admin-settings/admin-dashboard/admin-settings/admin-permissions#available-roles), you can set a Discord role. This means that a member needs that role to perform that action.

There are 2 options for assigning roles: you can use the default roles or you can create your own.

### Default Roles

To use the default roles, you can use the `🔨 Create Roles` button to create the default roles if they do not already exist.

<Frame>
  <img />
</Frame>

### Custom Roles

To assign a custom role to the action, use the select menu to select the action you want to set the role for.

<Frame>
  <img />
</Frame>

After you click on the action, you will see that the message has been updated and there is a new drop-down menu. Use this drop-down menu to choose the role you want to use.

<Frame>
  <img />
</Frame>

# Discord Limitations

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/admin-permissions/discord-limitations

This is how to properly integrate roles created by Drip Rewards into your Discord

Drip Rewards allows communities to create roles or delegate custom roles to team members, allowing them to use features such as the `/create` command. However, you must "tell" Discord that Drip is allowed to do this within Discord Integration Settings.

If you haven't done so already, be sure to assign/create admin [Admin Permissions](/admin-settings/admin-dashboard/admin-settings/admin-permissions) as seen below:

<Frame>
  <img />
</Frame>

### Integrating Admin Roles

Navigate to Server Settings in your Discord community by choosing `Server Settings` in the dropdown menu at the top of your channels list

<Frame>
  <img />
</Frame>

Click on `Integrations` in the Apps category then navigate to Drip and click on `Manage`

<Frame>
  <img />
</Frame>

Click on `/create` to override which roles can use this command

<Frame>
  <img />
</Frame>

Add the roles that should be able to use this permission by clicking the `Add Roles or Members` button

<Frame>
  <img />
</Frame>

<Check>Be sure to save your settings and you are all set!</Check>

# Overview

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/game-settings

Edit the settings for various Games in your community

### Accessing Game Settings

You can access Game Settings by clicking the `🎲 Game Settings` option in the [settings menu](/admin-settings/admin-dashboard/admin-settings).

<Frame>
  <img />
</Frame>

There are two different options in Game Settings, choose which you would like to edit from the dropdown menu:

* 🃏**Casino Branding:** Configure the casino branding for your server

* 🎲 **Casino Games:** Configure the games

<Frame>
  <img />
</Frame>

<CardGroup>
  <Card title="🃏Configure the casino branding for your server" />

  <Card title="🎲 Configure the games" />
</CardGroup>

# Casino Branding

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/game-settings/casino-branding

Configure the casino branding for your server

<Warning>This feature is only available for Custom Plans</Warning>

After selecting `🃏``Casino Branding` \*\*\*\*from the dropdown in [Game Settings,](/admin-settings/admin-dashboard/admin-settings/game-settings) you will see one option. Choose this option from the dropdown menu to edit:

* 📷 **Casino Images:** Configure the casino images for your server

<Frame>
  <img />
</Frame>

A new embed will appear and should look something like this unless the media has already been changed:

<Frame>
  <img />
</Frame>

Drip Rewards comes with its own Casino branding but you can change the various media by clicking the blue arrows at the bottom of the embed and then selecting `Edit Image.` A form will appear for you to edit the URL for the media you would like to use

<Frame>
  <img />
</Frame>

After clicking submit, your new media should appear! You can reset the media by clicking the green `Reset` button

<Frame>
  <img />
</Frame>

# Casino Games

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/game-settings/casino-games

Configure the various games for your community

After selecting `🎲 Casino Games` from the dropdown in [Game Settings](/admin-settings/admin-dashboard/admin-settings/game-settings), there will be two different options. Choose which you would like to edit from the dropdown menu:

* 💰 **Bet Amount:** Configure the bet amounts for the games

* 🎲 **Game Status:** Disable or enable the games for your server

<Frame>
  <img />
</Frame>

<Tabs>
  <Tab title="💰 Bet Amount">
    After selecting `💰 Bet Amount` from the dropdown menu in Casino Games Settings, select the game you would like to edit.

    <Frame>
      <img />
    </Frame>

    After choosing the game you would like to edit, a new embed will appear with the current bet amounts for the selected game.

    <Frame>
      <img />
    </Frame>

    Click on the bet amount that you would like to edit then enter the new bet amount in the form that appears then click submit.

    <Frame>
      <img />
    </Frame>
  </Tab>

  <Tab title="🎲 Game Status">
    After selecting `🎲 Game Status` from the dropdown menu in Casino Games Settings, select the game you would like to edit.

    <Frame>
      <img />
    </Frame>

    After choosing the game you would like to edit, a new embed will appear with the current status of the selected game. Click on disable/enable to change the status of the game for your community.

    <Frame>
      <img />
    </Frame>
  </Tab>
</Tabs>

# Member Roles

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/member-roles

Assign roles for member achievements

## Retrieve Server Permissions

You can view your server achievements by clicking the `👤Special Roles` option in the [settings menu](/admin-settings/admin-dashboard/admin-settings).

If you have opened the **Special Roles**, you will see an embed where all different roles are displayed.

### Available Roles

* 👑 **Big Tipper**: The role that will be given to the member who tips over x amount of Points.

* 🔗 **Linked Role**: The role that will be given to people who link their wallet to your server.

* 📈 **Exclude from leaderboard**: These roles won't be considered when showing the leaderboard (such as team or mods).

* 🏹 **Allow Quest Creation:** These roles will be able to create quests

<Frame>
  <img />
</Frame>

## Assign Roles

For each of the [available roles](/admin-settings/admin-dashboard/admin-settings/member-roles#available-roles), you can set a Discord role.

To assign a role to the achievement, use the select menu to select the action you want to set the role for.

<Frame>
  <img />
</Frame>

After you click on the achievement, you will see that the message has been updated and there is a new drop-down menu. Use this drop-down menu to choose the role you want to use.

<Frame>
  <img />
</Frame>

## Extra

### Set Big Tipper Amount

The Big Tipper role is a role given to a member who tips x number of Points. Each server can choose this option for itself.

To change this this amount, follow the steps in [Assign Roles](/admin-settings/admin-dashboard/admin-settings/member-roles#assign-roles) and select the `👑Big Tipper` role in the menu. Now you will see the option to select a role, but also a button `💰 Set Tip Amount`.

<Frame>
  <img />
</Frame>

Use the `💰 Set Tip Amount` button to set an amount. Now you will get a form where you can enter the amount:

<Frame>
  <img />
</Frame>

# Overview

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/points-settings

Customize and manage your points for your server

<Warning>
  Points created by Drip Rewards are off-chain tokens that do not have any
  monetary value. Points cannot be directly converted to Cryptocurrency or
  on-chain tokens.
</Warning>

You can access the Points Settings by clicking the `💰 Points Settings` option in the [Settings Menu](/admin-settings/admin-dashboard).

<Frame>
  <img />
</Frame>

You can choose from the following settings:

* ✨ **Branded Points:** Customize the name and appearance of Points

* **💰 Mass Credit:** Mass Credit NFT's or users

* 🪵 **Transaction Logs:** View transaction logs for your server

* 💸 **Tip Logs:** View tip logs for your server

* 🏆 L**eaderboard Settings**: Enable or Disable Leaderboard

### Learn More About

<CardGroup>
  <Card title="✨">
    Customize the name and appearance of Points
  </Card>

  <Card title="💰 Mass Credit">Mass Credit NFT's or users</Card>

  <Card title="🪵">View transaction logs for your server</Card>

  <Card title="💸">
    View tip logs for your server
  </Card>
</CardGroup>

# Branded Points

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/points-settings/branded-points

Customize the name and appearance of Points

The Branded Points allows you to edit the name and emoji of your Points.

<Frame>
  <img />
</Frame>

## Change Points

You can change the Points by using the `Change Token` button. Once you click the button, a form will open:

<Frame>
  <img />
</Frame>

Here you can enter both the name of your points and the emoji. Click `Submit` when you're done!

<Warning>
  **Custom Emojis Disclaimer**

  To use custom emojis they must be part of this server. To use the emoji enter ***only*** the emoji name without the colons. Example: `:goldcoin:` would be `goldcoin.`
</Warning>

<Warning>You can only change your token name and emoji **once a day**</Warning>

# Mass Credit Points

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/points-settings/mass-credit-points

Mass Credit NFT's or users

The **Mass Credit** feature allows you to credit points to users or NFTs

<Frame>
  <img />
</Frame>

## Credit Users

### Credit Specific Users

To credit specific users, use the `Credit users` button. Once you clicked the button, you will get a menu where you can select all the users you want to credit.

<Frame>
  <img />
</Frame>

Once you have selected the users you want to credit, you will be presented with a form where you must enter the number of points you want to award to all selected members.

<Frame>
  <img />
</Frame>

### Credit All Users

To credit all users, use the `Credit all users` button. Once you clicked the button, you will be presented with a form where you must enter the number of points you want to award to all members. Once you click `Submit`, it will credit the Points.

<Frame>
  <img />
</Frame>

## Credit NFTs

### Credit Specific NFTs

To credit specific NFTs, use the `Credit list of NFTs` button. Once you have clicked on the button, you will get a form where you have to enter the number of points you want to credit and all the ids of the NFTs, separated by a comma.

<Frame>
  <img />
</Frame>

### Credit All NFTs

To credit all NFTs, use the `Credit all NFTs` button. Once you have clicked the button, you will be presented with a form where you must enter the number of points you want to award to all NFTs. Once you click `Submit`, it will credit the Points.

<Frame>
  <img />
</Frame>

<Info>You can also use negative numbers to remove points from users</Info>

# Overview

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/quest-settings

In this section, you can edit the Quest settings for your community

# Insta-Quest

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/quest-settings/insta-quest

Automate your quests (Pro Feature)

After selecting `⚡Insta-Quest` from the dropdown menu in [Quest Settings](/admin-settings/admin-dashboard/admin-settings/quest-settings), a new embed will appear:

<Frame>
  <img />
</Frame>

Click on `📍 Add Account`**. This will open a popup which you can input the Twitter account handle in.**

<Frame>
  <img />
</Frame>

Once you have the Twitter account added you will be greeted by a new embed.

<Frame>
  <img />
</Frame>

Click on the `🔍 Set Filter` button to add specific words that will allow the bot to use Twitter posts as Insta-Quests. A form will appear for you to enter words to allow DRIP to pick up .

<Frame>
  <img />
</Frame>

<Warning>
  Simply selecting a Channel and Template without adding a filter will post
  every Twitter post from your account as a quest.
</Warning>

*Keywords: insta-quest, insta quest, quest filter, filter*

# Member Active Quest Limit

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/quest-settings/member-active-quest-limit

Change the limit on quests per regular member, per day (Pro Feature)

After selecting `🔢 ``Member Active Quest Limit` \*\*\*\*from the dropdown menu in [Quest Settings](/admin-settings/admin-dashboard/admin-settings/quest-settings), a new embed will appear:

<Frame>
  <img />
</Frame>

Click on the `🔢 Change Limit` button to change the number of Member Active Quests that can be active at a single time. A form will appear for you to enter a limit, enter "0" for unlimited member Quests or click the `🚫 No Member Active Quest Limit` button.

<Frame>
  <img />
</Frame>

*Keywords: member quests limit, change limit*

# Project Handle

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/quest-settings/project-handle

Set the project handle(s) for quests

After selecting `🪪 Project Handle` from the dropdown menu in [Quest Settings](/admin-settings/admin-dashboard/admin-settings/quest-settings), a new embed will appear:

<Frame>
  <img />
</Frame>

To add a project handle, click on Twitter from the dropdown menu:

<Frame>
  <img />
</Frame>

A form will appear for you to enter the project's Twitter handle

<Frame>
  <img />
</Frame>

*Keywords: project handle, twitter handle*

# Quests Channel

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/quest-settings/quests-channel

Change the channel that quests are sent in once created

After selecting `📍 Quests Channel` \*\*\*\*from the dropdown menu in [Quest Settings](/admin-settings/admin-dashboard/admin-settings/quest-settings), a new embed will appear:

<Frame>
  <img />
</Frame>

From here, you can choose where Main Quests (any quest sent by an Admin or Quest Master) and Side Quests (any Quest sent by allowed roles) will be sent using the two dropdown menus.

*Keywords: quests channel, main quests, side quests*

# Quests Duration

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/quest-settings/quests-duration

Change the default duration for quests in your community

After selecting `⏳ Quests Duration` \*\*\*\*from the dropdown menu in [Quest Settings](/admin-settings/admin-dashboard/admin-settings/quest-settings), a new embed will appear:

<Frame>
  <img />
</Frame>

Choose the fitting option from the dropdown menu.

<Frame>
  <img />
</Frame>

Choosing the custom option will open a form for you to enter a custom time:

<Frame>
  <img />
</Frame>

*Keywords: quests duration, custom time*

# Quests Limit

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/quest-settings/quests-limit

Change the amount of active quests allowed at one time

After selecting `✋ Quests Limit` \*\*\*\*from the dropdown menu in [Quest Settings](/admin-settings/admin-dashboard/admin-settings/quest-settings), a new embed will appear:

<Frame>
  <img />
</Frame>

Click on the `🔢 Change Limit` button to change the number of Quests that can be active at a single time. A form will appear for you to enter a limit, enter "0" for unlimited Quests.

<Frame>
  <img />
</Frame>

*Keywords: quests limit, change limit*

# Sharing Reward

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/quest-settings/sharing-reward

Set the rewards for sharing quests results

After selecting `💸 Sharing Reward` from the dropdown menu in [Quest Settings](/admin-settings/admin-dashboard/admin-settings/quest-settings), a new embed will appear:

<Frame>
  <img />
</Frame>

Click on the `💸 Change Rewards` button to change the amount of points given to a user when they share a quest reward on Twitter. A form will appear for you to enter a reward, enter "0" for no rewards or click `🔒``Disable Sharing`.

<Frame>
  <img />
</Frame>

*Keywords: sharing reward*

# Server Stats

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/server-stats

In this section you can view the statistics of your server

## Retrieve Server Statistics

You can view your server stats by clicking the `📊 Server Stats` option in the [settings menu](/admin-settings/admin-dashboard/admin-settings).

If you have opened the server statistics, you will see some general statistics. To choose another category, use the drop-down menu.

You can choose from the following categories:

* 📊 General

* 🕹️ Games

* 🏪 Store

* 🎁 Prizes

* 💰 Token Drops

* 💸 Tipping

* ✨ Magic Embed

<Frame>
  <img />
</Frame>

# Overview

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/web3-settings

Activate and edit Web3 features for your community

You can access the WEB3 Settings by clicking the `🔥WEB3 Settings` option in the [settings menu](/admin-settings/admin-dashboard/admin-settings).

<Frame>
  <img />
</Frame>

There are four different options in the Web3 Settings Menu, choose which you would like to edit from the dropdown menu:

* 🔥 **Manage Activations:** Reward NFT or Token holders with daily points

* 🤑 **NFT Sales Tracker:** Publicly track sales for NFT Collections

* 🖼 **Meme Maker:** Set up the meme maker for your collection(s)

* 🛒 **Preferred Marketplace:** Set your preferred marketplace

<CardGroup>
  <Card title="🔥 Reward NFT or Token holders with daily points" href="/admin-settings/admin-dashboard/admin-settings/web3-settings/manage-activations" />

  <Card title="🤑 Publicly track sales for NFT Collections" href="/admin-settings/admin-dashboard/admin-settings/web3-settings/nft-sales-tracker" />

  <Card title="🖼 Set up the meme maker for your collection(s)" href="/admin-settings/admin-dashboard/admin-settings/web3-settings/meme-maker" />

  <Card title="🛒 Set your preferred marketplace" href="/admin-settings/admin-dashboard/admin-settings/web3-settings/preferred-marketplace" />
</CardGroup>

# Advanced Collection Settings

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/web3-settings/advanced-collection-settings

There are various Advanced Settings available for Generator and Multiplier Collections

Advanced Collection Settings can be accessed via the [`🔥 Manage Activations`](/admin-settings/admin-dashboard/admin-settings/web3-settings/manage-activations) Menu

<Tabs>
  <Tab title="Attribute Override (Generators & Multipliers)">
    Generators and multipliers can be edited in even more detail. You can have generators with a particular attribute generate more or fewer tokens than others. Or you can make multipliers with a specific attribute have a greater effect on your generators.

    1. Click `📝 Attribute Override`

    <Frame>
      <img />
    </Frame>

    2. A new embed will appear, click on `📝 Add Property`

    <Frame>
      <img />
    </Frame>

    3. A new embed will appear, choose the property you want to edit from the dropdown menu.

    <Frame>
      <img />
    </Frame>

    4. Choose an attribute to edit from the dropdown menu

    <Frame>
      <img />
    </Frame>

    5. A new form will appear, enter the new value for the attribute override

    <Frame>
      <img />
    </Frame>

    The attribute override will now appear in the Advanced Attribute Settings Menu

    <Frame>
      <img />
    </Frame>
  </Tab>

  <Tab title="Set Max Balance (Generators)">
    To set a maximum balance that an NFT can generate, click on the `📝 Set Max Balance` button

    <Frame>
      <img />
    </Frame>

    A new form will appear, enter the new collection max balance

    <Frame>
      <img />
    </Frame>
  </Tab>

  <Tab title="Re-Sync">
    This allows you to update collections in case of changes to metadata, collection size, etc. To do so, click on the `🔄 Re-Sync` button

    <Frame>
      <img />
    </Frame>

    A new embed will appear for you to confirm a Re-Sync. You can do so by clicking the `🔄 Re-Sync` button again. This can only be done once a day.

    <Frame>
      <img />
    </Frame>
  </Tab>
</Tabs>

# EVM Chains

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/web3-settings/evm-chains

Activate ERC-721 NFTs, ERC-1155 NFTs, and ERC-20 Tokens on EVM Chains

### Add an Activation

After selecting an EVM Chain from the dropdown in the [`🔥 Manage Activations`](/admin-settings/admin-dashboard/admin-settings/web3-settings/manage-activations) menu, a new embed will appear:

<Frame>
  <img />
</Frame>

Select the type of NFT/Token you would like to add from the dropdown menu

<Frame>
  <img />
</Frame>

### NFT & Token Types

<Tabs>
  <Tab title="ERC-721">
    After selecting the ERC-721 from the dropdown menu, a form will appear for you to enter the contract address and custom name

    <Frame>
      <img />
    </Frame>

    After the collection has been imported the following embed will appear, select the collection type from the dropdown menu

    <Frame>
      <img />
    </Frame>

    #### **No Effect - Collection will only appear in the Dashboard for users**

    <Frame>
      <img />
    </Frame>

    #### **Generator -** Generate daily points for NFTs

    <Frame>
      <img />
    </Frame>

    <Frame>
      <img />
    </Frame>

    #### Multiplier - Multiply the daily points your Generators give

    <Frame>
      <img />
    </Frame>

    You can always change/edit collections via the Collection Settings Menu after it is activated

    <Frame>
      <img />
    </Frame>
  </Tab>

  <Tab title="ERC-1155">
    After selecting the ERC-1155 from the dropdown menu, a form will appear for you to enter the contract address and custom name

    <Frame>
      <img />
    </Frame>

    After the collection has been imported the following embed will appear. ERC-1155 NFTs may only be used as Generators or a No Effect by inputting "0" into the custom field

    <Frame>
      <img />
    </Frame>

    You can always change/edit collections via the Collection Settings Menu after it is activated

    <Frame>
      <img />
    </Frame>
  </Tab>

  <Tab title="ERC-20">
    After selecting the ERC-20 from the dropdown menu, a form will appear for you to enter the contract address, custom name, and generation ratio

    <Frame>
      <img />
    </Frame>

    You can always change/edit ERC-20 Tokens via the Collection Settings Menu after they are activated by selecting them from the dropdown menu

    <Frame>
      <img />
    </Frame>
  </Tab>
</Tabs>

### Remove an Activation

To remove a collection, go to the **Collection Setting Menu** and click the `🗑️ Remove A Collection` option.

<Frame>
  <img />
</Frame>

Now select the collection you would like to remove from the dropdown menu

<Frame>
  <img />
</Frame>

A new embed will appear, click on `🗑 Confirm Removal` \*\*\*\*to remove the collection. \*\*This cannot be undone\*\*!

<Frame>
  <img />
</Frame>

# Manage Activations

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/web3-settings/manage-activations

Reward NFT or Token holders with daily points

After selecting `🔥 Manage On-Chain Activations` \*\*\*\*from the dropdown menu in [Web3 Settings](/admin-settings/admin-dashboard/admin-settings/web3-settings), a new embed will appear:

<Frame>
  <img />
</Frame>

### New Activation

To add a new collection, select `✨ New Activation` from the dropdown menu

<Frame>
  <img />
</Frame>

Then select the chain of the collection from the dropdown menu

<Frame>
  <img />
</Frame>

Drip Rewards currently supports activations on the following [EVM Chains](/admin-settings/admin-dashboard/admin-settings/web3-settings/evm-chains):

* **Ethereum:** ERC-721 NFTs, ERC-1155 NFTs, ERC-20 Tokens

* **Polygon:** ERC-721 NFTs, ERC-1155 NFTs, ERC-20 Tokens

* **Binance:** ERC-721 NFTs, ERC-1155 NFTs, ERC-20 Tokens

* **SEI (v2):** ERC-721 NFTs, ERC-1155 NFTs

* **Avalanche:** ERC-721 NFTs, ERC-1155 NFTs, ERC-20 Tokens

* **Fantom:** ERC-721 NFTs, ERC-1155 NFTs, ERC-20 Tokens

* **Cronos:** ERC-20 Tokens

* **Arbitrum:** ERC-721 NFTs, ERC-1155 NFTs, ERC-20 Tokens

* **Base:** ERC-721 NFTs, ERC-1155 NFTs

* **Blast:** ERC-721 NFTs, ERC-1155 NFTs

* **Polygon ZK-EVM:** ERC-721 NFTs, ERC-1155 NFTs

* **Optimism:** ERC-721 NFTs, ERC-1155 NFTs

* **Gnosis:** ERC-721 NFTs, ERC-1155 NFTs

* **Celo:** ERC-721 NFTs, ERC-1155 NFTs

Drip Rewards also currently supports [Solana](/admin-settings/admin-dashboard/admin-settings/web3-settings/solana-activation):

* **Solana:** Solana NFT, Solana Token

### Edit Activations

To edit a Web3 Activation, click on the dropdown menu in the Manage Activations Menu and select the collection you would like to edit

<Frame>
  <img />
</Frame>

A new embed will appear that allows you to edit collection settings

<Frame>
  <img />
</Frame>

<Check>
  The buttons from the above embed have become a dropdown menu to keep the UI
  tidy and to add "Listing Penalty".
</Check>

<img alt="" />

# Meme Maker

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/web3-settings/meme-maker

Set up the meme maker for your collection(s)

## Set Up a Meme

To create a new meme, add the collection you want to create a new meme from. To do this, click the `⚡ Add a New Collection` option.

<Frame>
  <img />
</Frame>

Select the collection you want to use next.

<Frame>
  <img />
</Frame>

Now click the `Set Attribute` button and select the attribute you want to use to base your memes on.

<Frame>
  <img />
</Frame>

<Frame>
  <img />
</Frame>

After picking the correct attribute, you can now create a new meme. Do this by clicking `Create a new meme` from the dropdown menu at the bottom of the embed. A pop-up will appear asking you to enter the name of the new meme.

<Frame>
  <img />
</Frame>

<Frame>
  <img />
</Frame>

Then choose a property you want to set and fill in the URL to the overlay.

<Frame>
  <img />
</Frame>

<Frame>
  <img />
</Frame>

<Info>
  The overlay should be a PNG with all the right dimensions to fit the NFT image
</Info>

<Warning>
  We suggest using an external image host, like[
  https://imgtr.ee/](https://imgtr.ee/) or
  [https://imgur.com](https://imgur.com) for hosting images
</Warning>

## Remove a Meme

To remove a meme, click the `🗑️ Remove` button.

<Frame>
  <img />
</Frame>

To be safe, another confirmation will be shown if you still want to delete the meme. Then click the `Confirm` button.

<Frame>
  <img />
</Frame>

## Send Meme Maker

To send the **Meme Maker** message, use the `📤 Send Meme Maker` button.

<Frame>
  <img />
</Frame>

This opens a new drop-down menu where you must choose the channel to which the message should be sent.

<Frame>
  <img />
</Frame>

## Use the Meme Maker

To use the meme maker, use the `Create Meme` button.

<Frame>
  <img />
</Frame>

If multiple collections are activated, you will see multiple options. Click on the collection you want to use.

<Frame>
  <img />
</Frame>

Now choose the NFT for which you want to create a meme.

<Frame>
  <img />
</Frame>

As a final step, select the meme you want to create.

<Frame>
  <img />
</Frame>

After a few seconds, your meme is ready to use

<img alt="" />

# NFT Sales Tracker

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/web3-settings/nft-sales-tracker

Set up a sales tracker for your NFT Collections so you never miss a sale again!

You can access the **NFT Sales Tracker** settings by clicking the `🤑 NFT Sales Tracker` option in the [Web3 Settings](/admin-settings/admin-dashboard/admin-settings/web3-settings) menu.

When you click on the option, you will see the following menu:

<Frame>
  <img />
</Frame>

## Add New Tracker

To add a new tracker, click the `New Tracker` button. This will open up a new menu where you configure your sales tracker.

<Frame>
  <img />
</Frame>

1. Click the `Choose Collection` button, you will see a dropdown menu appear. Select the collection you want to set up the Sales Tracker for.

<Frame>
  <img />
</Frame>

1. Now click the `Choose Channel` button, you will see a dropdown menu appear. Select the channel you want the sales to be posted.

<Frame>
  <img />
</Frame>

1. Once it is configured as desired, click the `✅ Save Tracker` button to save the Sales Tracker and now you will see the confirmation message:

<Frame>
  <img />
</Frame>

## Edit Tracker

To add a new tracker, click the `Manage Tracker` button. This will open a new menu where you can see all active sales trackers and a dropdown menu where you can select them.

1. To edit a Sales Tracker, pick the Sales Tracker you want to edit in the drop-down menu.

<Frame>
  <img />
</Frame>

1. Now you will get some option for you to edit. Pick the option you want to edit.

<Frame>
  <img />
</Frame>

**2.1** **Edit Channel**

Click `📝 Edit Channel` to edit the channel to which sales are sent. You will get the option to choose a new channel. Pick the channel in the drop-down menu.

<Frame>
  <img />
</Frame>

**2.2 Toggle Linked Only**

Click `🔗Toggle Linked Only`to send only sales from linked accounts in the server.

## **Remove Tracker**

To remove a tracker, use the `Manage Trackers` button, **select** the sales tracker you want to delete and click the `🗑️ Delete Tracker` button to delete the tracker.

<Frame>
  <img />
</Frame>

<Warning>Sales Trackers are only available for imported collections</Warning>

# Preferred Marketplace

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/web3-settings/preferred-marketplace

Set your preferred marketplace for the NFT Sales Tracker

After selecting `🛒 Preferred Marketplace` \*\*\*\*from the dropdown menu in [Web3 Settings](/admin-settings/admin-dashboard/admin-settings/web3-settings), a new embed will appear:

<Frame>
  <img />
</Frame>

Drip Rewards currently supports the following marketplaces:

* OpenSea

* X2Y2

* Magic Eden

* Blur

* Aura Exchange

* Alpha Shares

* Snag

<Info>
  Preferred Marketplaces are first selected by chain

  <img alt="" />
</Info>

Select your preferred marketplace from the dropdown menu

<Frame>
  <img />
</Frame>

# Solana Activation

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/web3-settings/solana-activation

Activate Solana NFTs, and Tokens

### Add an Activation

After selecting `Solana` from the dropdown in the [`🔥 Manage Activations`](/admin-settings/admin-dashboard/admin-settings/web3-settings/manage-activations) menu, a new embed will appear:

<Frame>
  <img />
</Frame>

Select the type of NFT/Token you would like to add from the dropdown menu

<Frame>
  <img />
</Frame>

### NFTs & Tokens

<Tabs>
  <Tab title="Solana NFT">
    After selecting Solana NFT from the dropdown menu, a form will appear for you to enter the contract address and custom name

    <Frame>
      <img />
    </Frame>

    After the collection has been imported the following embed will appear, select the collection type from the dropdown menu

    <Frame>
      <img />
    </Frame>

    #### **No Effect - Collection will only appear in the Dashboard for users**

    <Frame>
      <img />
    </Frame>

    #### **Generator -** Generate daily points for NFTs

    <Frame>
      <img />
    </Frame>

    #### Multiplier - Multiply the daily points your Generators give

    <Frame>
      <img />
    </Frame>

    You can always change/edit collections via the Collection Settings Menu after it is activated

    <Frame>
      <img />
    </Frame>
  </Tab>

  <Tab title="Solana Token">
    After selecting Solana Token from the dropdown menu, a form will appear for you to enter the contract address and custom name

    <Frame>
      <img />
    </Frame>

    You can always change/edit Solana Tokens via the Collection Settings Menu after they are activated by selecting them from the dropdown menu

    <Frame>
      <img />
    </Frame>

    You can always change/edit collections via the Collection Settings Menu after it is activated
  </Tab>
</Tabs>

### Remove an Activation

To remove a collection, go to the **Collection Setting Menu** and click the `🗑️ Remove A Collection` option

<Frame>
  <img />
</Frame>

Now select the collection you would like to remove from the dropdown menu

<Frame>
  <img />
</Frame>

A new embed will appear, click on `🗑 Confirm Removal` to remove the collection. **This cannot be undone**!

<Frame>
  <img />
</Frame>

# Overview

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/white-label-settings

White Labeling is a feature that allows you to turn DRIP into your own branded experience

You can access the White Label Settings by clicking the `🏳️ White Label Settings` option in the [settings menu](/admin-settings/admin-dashboard/admin-settings).

You can choose from the following settings:

* 🔗 **Wallet Connect**: Customize your wallet connect page

* **🤖 Bot Status**: Customize the status of your bot

* ✔️ **Marketplace Bio:** Customize the Marketplace bio code for your server

* 🖼️ **Bot Avatar:** Customize the bot avaatar

<Frame>
  <img />
</Frame>

## Learn More About

<CardGroup>
  <Card title="✨ Custom Bot Status">
    Customize the status of your bot
  </Card>

  <Card title="⚡️ White-Labelled Wallet Connect">
    Customize your own wallet connect page
  </Card>

  <Card title="🎨">
    Customize the colors of your bots embeds

    *Coming Soon*
  </Card>

  <Card title="🃏 Custom Casino Dealer Graphics">
    Use custom images in the casino
  </Card>

  <Card title="🏳️ White Label">
    Turn the Bear Bot into your own branded experience
  </Card>
</CardGroup>

# Bot Status

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/white-label-settings/bot-status

Customize the status of your bot

# Setup White Label

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/admin-settings/white-label-settings/setup-white-label

White Labelling is a feature that allows you to turn Drip Rewards into your own branded experience

**Here's what you get with the Custom Plan:**

* 📝 Custom Bot Name

* 😎 Custom Bot Avatar

* ✨ Custom Bot Status

* ⚡️ White-Labelled Wallet Connect

* 🚀 Dedicated Speed & Performance

* 🎨 Bot-Wide Color Scheme

* 🃏 Custom Casino Dealer Graphics

* 📊 Discord User Analytics

* 🔌 Extended API (Coming Soon)

## Learn More About

<CardGroup>
  <Card title="✨ Custom Bot Status">
    Customize the status of your bot
  </Card>

  <Card title="⚡️ White-Labelled Wallet Connect">
    Customize your own wallet connect page
  </Card>

  <Card title="🎨">
    Customize the colors of your bots embeds

    *Coming Soon*
  </Card>

  <Card title="🃏 Custom Casino Dealer Graphics">
    Use custom images in the casino
  </Card>
</CardGroup>

a

# Create Channels

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/create-channels

Have Drip Rewards create starter channels for your Discord Community

Drip Rewards can create some starter channels for your Discord community if you would like. To Create Channels, navigate to the Admin Dashboard then click on the `Create Channels` button.

<Frame>
  <img />
</Frame>

After clicking the button, a new embed will appear with three different options for creating channels for your community:

* ⚡️ **Create All:** Create all of the basic channels that come with the Drip Rewards template (dashboard, lootbox, games, store, and prizes)

* ⚙️ **Create Specific:** Create a specific channel from the Drip Rewards template

* 📄 **Use Template:** Create channels from a template that works best for your community

<Frame>
  <img />
</Frame>

<Tabs>
  <Tab title="⚡️ Create All">
    To create all of the basic channels provided by Drip Rewards, click on the `Create All` button

    <Frame>
      <img />
    </Frame>

    This will create the 6 basic channels used by Drip Rewards as seen below:

    <Frame>
      <img />
    </Frame>
  </Tab>

  <Tab title="⚙️ Create Specific">
    To create specific channels offered by Drip Rewards, click on the `Create Specific` button

    <Frame>
      <img />
    </Frame>

    You can then pick the channels you would like to create from the dropdown menu that appears

    <Frame>
      <img />
    </Frame>
  </Tab>

  <Tab title="📄 Use Template">
    To create channels based on a template included with Drip Rewards, click on the `Use Template` button

    <Frame>
      <img />
    </Frame>

    You can then pick the template you would like to create from the dropdown menu that appears

    <Frame>
      <img />
    </Frame>

    These templates will create multiple categories, channels, and roles for your community to get started.

    <Info>
      You will still need to edit permissions for these various categories, channels, and roles to ensure your Discord is properly set up.
    </Info>
  </Tab>
</Tabs>

# Manage Points

Source: https://docs.drip.re/bot-documentation/admin-settings/admin-dashboard/manage-points

Lookup information about members in your community

Drip Rewards keeps various information about members of your community that you can access by clicking the `🔍 Manage Points` button.

<Frame>
  <img />
</Frame>

After pressing the `🔍 Manage Points` button a new embed will appear

<Frame>
  <img />
</Frame>

Choose a member you would like to lookup by selecting their username from the dropdown menu

<Frame>
  <img />
</Frame>

After selecting a member, information kept by Drip Rewards will appear in a new embed. You can add/remove points from this embed and select a new member to view as you wish

<Frame>
  <img />
</Frame>

# Overview

Source: https://docs.drip.re/bot-documentation/drip-academy/economy-101-balancing-your-discord-economy-with-drip

In this course, we'll explore the best practices for setting up your economy, managing points, and ensuring a balanced system that engages and rewards your members. 4 to 5 minute read.

### Understanding Supply and Demand

Creating a thriving micro-economy within your Discord community using Drip requires careful consideration of supply and demand. In the context of a Discord economy, **supply** refers to how your members can earn points, while **demand** represents ways members can spend or enjoy those points. It's crucial to strike a balance between the two to prevent inflation and maintain a healthy economy.

<Tabs>
  <Tab title="Creating Demand">
    To stimulate the usage of points and keep your members engaged, you must provide valuable ways for them to spend their points. Some options include:

    * Setting up a [store item](/drip-features/store) with attractive rewards
    * Organizing [raffles/prizes](/drip-features/prizes)
    * Integration of external platforms using [Drip API](/api/extended-api)
    * Offering a diverse range of rewards for member's preferences & interests
    * Including exclusive or limited-edition items to create scarcity and demand
    * Collaborating with other brands to provide additional rewards and experiences
  </Tab>

  <Tab title="Managing Supply">
    Points can be earned through various means, such as completing [quests](/drip-features/quests), holding on-chain assets like [tokens or NFTs](/drip-features/web3-features), or receiving [tips](/drip-features/slash-commands) from other members. However, it's essential to be mindful of the amount of points introduced to the economy by administrators. Any points given via [Member Lookup](/admin-settings/admin-dashboard/manage-points) or creating unlimited amounts in Quests/Drops will increase the supply.
  </Tab>

  <Tab title="Balancing Web3 Activations">
    When using NFTs and Tokens as a source of point generation, be cautious of the potential for inflation. Consider the following measures:

    * Limit the daily points generated by NFTs and Tokens
    * Implement a maximum balance for NFTs, requiring users to claim points before the NFT can continue generating more
    * Start with low point generation rates and adjust as needed
  </Tab>

  <Tab title="Resetting the Economy">
    If inflation becomes a concern, you can reset the economy by creating a high-value raffle with no point limit. Offer desirable prizes such as exclusive NFTs or merchandise to encourage participation and drain excess points from the system.
  </Tab>
</Tabs>

### Additional Tips for Creating a Balanced Economy

1. **Regularly Monitor and Analyze the Economy:** Keep track of the total points in circulation and the rate at which they are being earned and spent using [Server Stats](/admin-settings/admin-dashboard/admin-settings/server-stats). This will also allow you to identify any imbalances or trends in the economy. Adjust point generation rates, quest rewards, and store prices to maintain balance.

2. **Encourage Active Participation:** Create engaging [quests](/drip-features/quests) and challenges that require effort and skill, rewarding users with points for their achievements. Regularly update and rotate the available quests to keep things fresh and exciting. Implement game [leaderboard](/drip-features/games#casino-leaderboard) tournaments to foster friendly competition and motivate users to earn and spend points.

3. **Implement Sinks and Drains:** Introduce mechanisms that remove points from circulation to counteract inflation. Offer high-value, limited-quantity [store items](/drip-features/store) or experiences that require significant amounts of points to obtain, effectively draining points from the economy.

4. **Communicate and Educate:** Clearly explain the mechanics of your economy to your community members, including how points are earned, spent, and valued. Provide guides, tutorials, or FAQs to help users understand ways to participate in the economy and maximize their rewards. Regularly communicate any changes or updates to the economy, and seek feedback from your community to ensure their needs and preferences are met.

### Conclusion

Building a balanced Discord economy with Drip requires careful planning and ongoing monitoring. By providing valuable ways to spend points, managing supply, implementing safeguards against inflation, and incorporating additional strategies like encouraging active participation, implementing sinks and drains, and communicating effectively, you can create an engaging and rewarding experience for your community members. Remember to start small, experiment, and adapt as you go to ensure the long-term success of your micro-economy.

# Overview

Source: https://docs.drip.re/bot-documentation/drip-features/games

Bet your hard-earned token for a chance to win in Blackjack or Poker!

# Blackjack

Source: https://docs.drip.re/bot-documentation/drip-features/games/blackjack

A card game where players aim to achieve a hand value closest to 21 without exceeding it, competing against the dealer.

<Warning>
  *We strictly prohibit the usage of casino features if your Points can be
  purchased or sold for real-world value.*
</Warning>

### Start a Blackjack game

To start a Blackjack game, go to the `🎲 Casino` channel and click the `Start` button. Now click `🃏New Blackjack Table.`

<Frame>
  <img />
</Frame>

Once your table is started, a Discord thread will created and you will be mentioned in the thread. In this thread you will see the following message:

<Frame>
  <img />
</Frame>

Your game is ready! Invite your friends by mentioning them in the thread, or not, and enjoy!

### Join a Blackjack game

To join an active Blackjack table, go to the `🎲 Casino` channel and click the `Start` button. If there are any active tables, they will be displayed there.

<img alt="" />

Once you have found a table you want to join, click on the table to be listed in the table thread. Now click the `Join Game` button to join the table and wait for the game to be started by the **👑 Game Master**.

<Frame>
  <img />
</Frame>

### Blackjack table settings

The **👑 Game Master** can update some settings of the table, these are the options:

* **💻 Manage Players:**

  * **👟 Remove Player:** Kick a player from the game

* **👀 Manage Game Visibility:**

  * **🙌 Make Game Public:** Anyone can view and join the table

  * **🔒 Make Game Private:** Only mentioned members can view and join the table

<Frame>
  <img />
</Frame>

### Play a Blackjack game

<Info>
  If you don't know the Texas Hold'em house rules, read them first before
  proceeding. You can find them [Blackjack House
  Rules](/drip-features/games/blackjack#blackjack-house-rules)
</Info>

To play a game, the [👑 Game Master](/drip-features/games/blackjack#keywords) needs to start the round by clicking the `👑Start Round` button.

Once the game is started, it proceeds according to the[Rules](/drip-features/games/blackjack#rules).

Players will have to choose in turn, if they take too long they will automatically stand their hand.

<Frame>
  <img />
</Frame>

### Blackjack House Rules

#### Rules

1. Players and the dealer are dealt two cards each; players can see one of the dealer's cards.

2. The goal is to have a hand value closest to 21 without going over. Face cards are worth 10, Aces are 1 or 11, and number cards are their face value.

3. Players can 'hit' to take additional cards or 'stand' to maintain their total.

4. If a player's total exceeds 21, they 'bust' and lose the round.

5. The dealer reveals the hidden card and must hit until their cards total 17 or higher.

6. Players win by having a higher total than the dealer without busting or by the dealer busting.

<Frame>
  <img />
</Frame>

#### Keywords

* 👑**Game Master ->** Member who created the table or the member who has been in the game the longest after the Game Master has left.

# Crash

Source: https://docs.drip.re/bot-documentation/drip-features/games/crash

A strategic game where players bet on a multiplying value aiming to cash-out before the multiplier crashes

<Warning>
  *We strictly prohibit the usage of casino features if your Points can be
  purchased or sold for real-world value.*
</Warning>

### Creating a new Crash Game

To start a Crash game, go to the `🎲 Casino` channel and click the `Start` button. Now click `🚀 New Crash Game` from the dropdown menu

<Frame>
  <img />
</Frame>

Once your game is started, a Discord thread will be created and you will be mentioned. In this thread you will see the following embed:

<Frame>
  <img />
</Frame>

You can mention other community members in the thread to play as multiplayer or you can use Crash as a single-player game.

<Info>
  Get invited to a game? Click on the `Join Game` button then wait for the Game Master to start the game.

  <img alt="" />
</Info>

### Starting a Crash Game

To begin a new round of Crash, click on the `Start Round` button.

<Frame>
  <img />
</Frame>

Choose the amount of points you would like to bet in the game.

<Frame>
  <img />
</Frame>

The Game Master can start the game once all players have selected a bet amount.

The embed seen below will be sent in the thread and the multiplier GIF in the top right corner will begin to count upwards.

To cash out, click the `Cash Out` button before the multiplier crashes.

<Frame>
  <img />
</Frame>

A message will appear showing you your winnings when you cash out

<Frame>
  <img />
</Frame>

# Poker

Source: https://docs.drip.re/bot-documentation/drip-features/games/poker

A strategic card game involving betting and individual play, where players wager on the best hand according to game-specific rankings.

<Warning>
  *We strictly prohibit the usage of casino features if your Points can be
  purchased or sold for real-world value.*
</Warning>

### Start a Poker game

To start a Poker game, go to the `🎲 Casino` channel and click the `Start` button. Now click `🪙 New Poker Table.`

<Frame>
  <img />
</Frame>

Once your table is started, a Discord thread will created and you will be mentioned in the thread. In this thread you will see the following message:

<Frame>
  <img />
</Frame>

Select your small blind for your game, you won't be able to change this anymore.

<Frame>
  <img />
</Frame>

Your game is set, invite your friends and enjoy!

### Join a Poker game

To join an active Poker table, go to the `🎲 Casino` channel and click the `Start` button. If there are any active tables, they will be displayed there.

<Frame>
  <img />
</Frame>

Once you have found a table you want to join, click on the table and you will be listed in the corresponding Discord thread. Now click the `Join Game` button to join the table and wait for the game to be started by the **👑 Game Master**.

<Frame>
  <img />
</Frame>

### Poker table settings

The **👑 Game Master** can update some settings of the table, these are the options:

* **💻 Manage Players:**

  * **👟 Remove Player:** Kick a player from the game

* **👀 Manage Game Visibility:**

  * **🙌 Make Game Public:** Anyone can view and join the table

  * **🔒 Make Game Private:** Only mentioned members can view and join the table

<Frame>
  <img />
</Frame>

### Play a Poker game

<Info>
  If you don't know the Texas Hold'em house rules, read them first before
  proceeding. You can find them in
  [#poker-house-rules-and-keywords](/drip-features/games/poker#poker-house-rules-and-keywords).
</Info>

To play a game, the [👑Game Master](/drip-features/games/poker#keywords) needs to start the round by clicking the `👑Start Round` button.

Once the game is started, it proceeds according to the [Rules](/drip-features/games/poker#rules).

Players can check their cards by using the `👀 View My Cards` button.

<img alt="" />

### Poker house rules and terminology

#### Rules

1. Players are dealt two private cards (hole cards) that belong to them alone.

2. Five community cards are dealt face-up on the board.

3. Players use the best combination of five cards to form their hand.

4. Betting rounds occur before the flop (first three community cards), after the flop, after the turn (fourth community card), and after the river (fifth community card).

5. Players can check, bet, raise, or fold in each betting round.

6. If a player can't or doesn't want to match a bet, they can fold, but any money they've already bet stays in the pot. When other players go above the original bet, this creates a side pot that the original player isn't eligible to win.

7. The best hand, according to traditional hand rankings, wins the pot. If multiple pots (main and side pots) are present, they are awarded based on hand strength and betting participation.

8. If a player does not play in time, their hand is folded and they are removed from the game.

<Frame>
  <img />
</Frame>

#### Keywords

* 👑**Game Master ->** Member who created the table or the member who has been in the game the longest after the Game Master has left.

# Magic Embed Builder

Source: https://docs.drip.re/bot-documentation/drip-features/magic-embed-builder

Build embeds on any device directly inside of Discord and add buttons with dynamic functionality.

# Overview

Source: https://docs.drip.re/bot-documentation/drip-features/magic-embed-builder/components

All interactive elements associated with the message.

## Get Started

To edit the embed components, use the command `/create type:✨ Magic Embed` and select the `👆 Edit Components` option.

<Frame>
  <img />
</Frame>

After clicking the option, you will get some different options depending on your already existing components.

### 📝 Add Component

You can add a new component by clicking the option `📝Add Component`

<Frame>
  <img />
</Frame>

After clicking the option, a form will open where you can fill in the context of your button:

* Name of the button *(Required)*

* Emoji of the button

<Frame>
  <img />
</Frame>

When you submit the information, you should now see all the possible modifications, each of which is explained in[Components Options](/drip-features/magic-embed-builder/components#components-options)

<Info>
  Due to Discord limitations a Magic Embed can only have a **maximum** of 5
  buttons.
</Info>

### ✏️ Edit Component

If you have already created a component, you can now edit it by clicking on the option with the values of the button you want to edit. After clicking you should now see all the possible modifications, each of which is explained in[Components Options](/drip-features/magic-embed-builder/components#components-options)

<Frame>
  <img />
</Frame>

## Components Options

<CardGroup>
  <Card title="✏️" href="/drip-features/magic-embed-builder/components/edit-component">
    Edit the label of the button
  </Card>

  <Card title="🎨" href="/drip-features/magic-embed-builder/components/edit-style">
    Style the button
  </Card>

  <Card title="🔗" href="/drip-features/magic-embed-builder/components/add-link">
    Redirect members to a website
  </Card>

  <Card title="✨" href="/drip-features/magic-embed-builder/components/give-take-points">
    Give/take points from a member
  </Card>

  <Card title="✨" href="/drip-features/magic-embed-builder/components/give-take-role">
    Give/take a role from a member
  </Card>

  <Card title="✨ Role Restrictions" href="/drip-features/magic-embed-builder/components/role-restrictions">
    Restrict button interaction based on roles
  </Card>

  <Card title="⌛" href="/drip-features/magic-embed-builder/components/time-restricions">
    Restrict button interaction based on time
  </Card>

  <Card title="👩‍💻 Password Restrictions" href="/drip-features/magic-embed-builder/components/password-restrictions">
    Add a required code to the button
  </Card>

  <Card title="🗨️" href="/drip-features/magic-embed-builder/components/attach-message">
    Add a message to the button
  </Card>

  <Card title="🗨️" href="/drip-features/magic-embed-builder/components/attach-embed">
    Add an embed to the button
  </Card>

  <Card title="♻️" href="/drip-features/magic-embed-builder/components/reset-functionality">
    Reset/remove a functionality of the button
  </Card>

  <Card title="🗑️" href="/drip-features/magic-embed-builder/components/remove-component">
    Remove the button
  </Card>
</CardGroup>

*Keywords: components, add component, edit component, component options*

# Add Link

Source: https://docs.drip.re/bot-documentation/drip-features/magic-embed-builder/components/add-link

Redirect members to a website

With this option, you can make the button refer members when they interact with it. Clicking on the option will open a form where you can enter the following:

* URL to redirect to

<Frame>
  <img />
</Frame>

Once you submit the information, the embed is updated and link added.

<Frame>
  <img />
</Frame>

When a member now presses the button, they will get the following response:

<Frame>
  <img />
</Frame>

<Warning>
  Please be aware due to Discord limitations, a link button can not have other features attached to it. If you wish to add feature to this button, please remove it and add it back.

  If you wish to remove the link button, use the `🔗Remove Link` option.

  <img alt="" />
</Warning>

*Keywords: add link, button link, remove link*

# Attach Embed

Source: https://docs.drip.re/bot-documentation/drip-features/magic-embed-builder/components/attach-embed

Add an embed to the button

This option allows you to add an embed to the button. This embed will be sent as a reply.

When you click on the option, a form opens where you have to enter the **link of the embed** you want to send as a reply.

<Frame>
  <img />
</Frame>

Once you submit the embed, the embed is updated. As of now, members who press the button will get the embed as a reply.

<Frame>
  <img />
</Frame>

<Info>✨ This feature is only available for the Core Tier</Info>

*Keywords: attach embed*

# Attach Message

Source: https://docs.drip.re/bot-documentation/drip-features/magic-embed-builder/components/attach-message

Add a message to the button

This option allows you to add a message to the button. This message will be sent as a reply. When you click on the option, a form opens in which you have to enter the message.

<Frame>
  <img />
</Frame>

Once you submit the text, the embed is updated. As of now, members who press the button will get the message as a reply.

<Frame>
  <img />
</Frame>

*Keywords: attach message*

# Edit Component

Source: https://docs.drip.re/bot-documentation/drip-features/magic-embed-builder/components/edit-component

Edit the label of the button

This option allows you to edit the label of the button. When clicking the option, a form will be opened where you can fill in the following:

* Title of the label *(Required)*

* Emoji

<Frame>
  <img />
</Frame>

*Keywords: edit component, title of label, emoji*

# Edit Style

Source: https://docs.drip.re/bot-documentation/drip-features/magic-embed-builder/components/edit-style

Style the button

This option allows you to style the button. When clicking the option, different options will be displayed:

* Color of The Button

* Disabled/Enabled

<Frame>
  <img />
</Frame>

Once you save the component, the button style is updated.

<Frame>
  <img />
</Frame>

<Info>✨ This feature is only available for the Pro Tier</Info>

*Keywords: edit style, color of button, colour of button, button color, button colour, disable/enable*

# Give/Take Points

Source: https://docs.drip.re/bot-documentation/drip-features/magic-embed-builder/components/give-take-points

Give/Take points from a member

This option allows you to give/take points from a member when they interact with it. If you click on the option, multiple options will be displayed:

* Give/Take Points -> Click on the option that applies

* Number of Points to give/take

* Time Restriction -> How frequent can they use the button

<Frame>
  <img />
</Frame>

Once you submit the information, the embed is updated. When a member now presses the button, they will get the following response:

<Frame>
  <img />
</Frame>

<Warning>
  Give/Take points is restricted to Administrators and users with the [Economy ](/admin-settings/admin-dashboard/admin-settings/admin-permissions)permission.

  <img alt="" />
</Warning>

*Keywords: give/take points, number of points, time restriction*

# Give/Take Role

Source: https://docs.drip.re/bot-documentation/drip-features/magic-embed-builder/components/give-take-role

Give/Take a role from a member

This option allows you to give/take a role from a member when they interact with it. If you click on the option, multiple options will be displayed:

* Give/Take Role -> Click on the option that applies

* The role to give/take

<Frame>
  <img />
</Frame>

Once you submit the information, the embed is updated. When a member now presses the button, they will get the following response:

<Frame>
  <img />
</Frame>

*Keywords: give/take role, select role, give role, take role*

# Give/Take Variable Points

Source: https://docs.drip.re/bot-documentation/drip-features/magic-embed-builder/components/give-take-variable-points

Give/Take a variable amount of points from a member

If you choose to add this option to a component, a form will be displayed for you to enter:

* **Points Amount Min Value:** The minimum amount of points that will be given/taken by the embed

* **Points Amount Max Value:** The maximum amount of points that will be given/taken by the embed

* **Add or Remove:** Choose whether the embed will give (add) or take (remove) variable amounts of points

<Frame>
  <img />
</Frame>

<Info>Minimum value must be less than Maximum value</Info>

<Frame>
  <img />
</Frame>

Now, when a member presses this button they will get/lose an amount of points between the minimum and maximum values

<Frame>
  <img />
</Frame>

<Warning>
  Give/Take points is restricted to Administrators and users with the [Economy](/admin-settings/admin-dashboard/admin-settings/admin-permissions)[ ](/admin-settings/admin-dashboard/admin-settings/admin-permissions)permission.

  <img alt="" />
</Warning>

*Keywords: give/take variable points, minimum value, maximum value, random points*

# Password Restrictions

Source: https://docs.drip.re/bot-documentation/drip-features/magic-embed-builder/components/password-restrictions

Add a required code to the button

This option allows you to add a required code to the button. When you click on the option, a form will open where you have to enter the code.

<Warning>This code is **case sensitive**!</Warning>

<Frame>
  <img />
</Frame>

Once you submit the code, the embed will be updated. From now on, members who press the button must enter the code you submitted. If they don't, they can't use the button.

<Frame>
  <img />
</Frame>

<Frame>
  <img />
</Frame>

<Info>✨ This feature is only available for the Pro Tier</Info>

*Keywords: password restrictions, code restrictions*

# Remove Component

Source: https://docs.drip.re/bot-documentation/drip-features/magic-embed-builder/components/remove-component

Remove the component

This option allows you to remove the button.

<Warning>This option is **irreversible**</Warning>

*Keywords: remove component, remove button*

# Reset Functionality

Source: https://docs.drip.re/bot-documentation/drip-features/magic-embed-builder/components/reset-functionality

Reset/remove a functionality of the button

# Role Restrictions

Source: https://docs.drip.re/bot-documentation/drip-features/magic-embed-builder/components/role-restrictions

Restrict button interaction based on roles

This option allows you to restrict button interaction based on a users roles. Use the 2 selection menus to choose the appropriate roles. Options:

* Required role to interact

* Exclude a role from interacting

<Frame>
  <img />
</Frame>

Once you click the `Done` button, the embed is updated. When a member now presses the button, they will get one of the following responses:

<Frame>
  <img />
</Frame>

<Frame>
  <img />
</Frame>

*Keywords: role restrictions, role requirements, exclude roles*

# Time Restricions

Source: https://docs.drip.re/bot-documentation/drip-features/magic-embed-builder/components/time-restricions

Restrict button interaction based on time

This option allows you to restrict button interaction based on time. Choose the fitting option from the dropdown menu.

<Frame>
  <img />
</Frame>

Choosing the **Custom Time Limit** will open a form where you can enter the time **in minutes**. If you want to use a tool to calculate the time, you can use [this site](https://www.inchcalculator.com/time-to-minutes-calculator/).

Once you choose the fitting **Time Restriction** option, the embed is updated. If a member presses the button now, they cannot interact with the button again until the limited time has passed. If they click the button before this time is up, they will get the following response:

<Frame>
  <img />
</Frame>

*Keywords: time restrictions, custom time limit*

# Overview

Source: https://docs.drip.re/bot-documentation/drip-features/magic-embed-builder/embeds

The embed is the main body of the message

### Get Started

To edit the embed content, use the command `/create type:✨ Magic Embed` and select the `📝Edit Embed` option.

<Frame>
  <img />
</Frame>

Now you see all the possible customizations, each of which is explained in [#embed-customizations-options](/drip-features/magic-embed-builder/embeds#embed-customizations-options)

## ✏️ Embed Customization Options

<CardGroup>
  <Card title="✏️" href="/drip-features/magic-embed-builder/embeds/edit-text-above-embed">
    Set a text that will be displayed above the embed
  </Card>

  <Card title="📝" href="/drip-features/magic-embed-builder/embeds/edit-embed-content">
    Set the text that will be displayed in the embed
  </Card>

  <Card title="🙍‍♂️ Edit Author" href="/drip-features/magic-embed-builder/embeds/edit-author">
    Set the author of the embed
  </Card>

  <Card title="👞" href="/drip-features/magic-embed-builder/embeds/edit-footer">
    Set the footer of the embed
  </Card>

  <Card title="🖼️" href="/drip-features/magic-embed-builder/embeds/edit-media">
    Set the images of the embed
  </Card>

  <Card title="✨" href="/drip-features/magic-embed-builder/embeds/edit-fields">
    Set the fields in the embed
  </Card>

  <Card title="🎨" href="/drip-features/magic-embed-builder/embeds/edit-color">
    Set the color of the embed
  </Card>
</CardGroup>

## ♻️ Delete Embed

This option allows you to remove the embed from the message.

<Frame>
  <img />
</Frame>

Once you click the option, the embed is removed from the message.

<Frame>
  <img />
</Frame>

<Warning>
  Removing the embed is irreversible, all modifications will be lost
</Warning>

<Info>
  After you remove the embed, a new option is displayed to add a new embed. This will create the default embed.

  <img alt="" />
</Info>

*Keywords: embed customization, delete embed*

# Edit Author

Source: https://docs.drip.re/bot-documentation/drip-features/magic-embed-builder/embeds/edit-author

Set the author of the embed

This option allows you to set the author of the embed. When clicking the option, a form will be opened where you can fill in the following:

* Author Name

* URL that redirects users when they click on the author

* URL for the icon that will be displayed next to the author

<Frame>
  <img />
</Frame>

Once you submit the information, the embed is updated.

<Frame>
  <img />
</Frame>

<Info>✨ This feature is only available for the Pro Tier</Info>

*Keywords: edit author, author name*

# Edit Color

Source: https://docs.drip.re/bot-documentation/drip-features/magic-embed-builder/embeds/edit-color

Set the color of the embed

This option allows you to set the color of the embed. The color is visible on the left side of the embed. When you click the option, you will get a select menu with different options like:

* Preset colors (Red, Green, ...)

* Custom Hex Code

<Frame>
  <img />
</Frame>

### 🔴 Preset Color

If you want to set one of the preset colors as your color, click on the desired color option and your embed will be updated.

### ⚙️ Custom Hex Code

This option allows you to set the color of the embed to a custom color. When you click the option, you will get a form where you need to fill in the HEX code of the color.

You can find the HEX code of a color on [this site](https://redketchup.io/color-picker).

<Frame>
  <img />
</Frame>

Once you submit the information, the embed is updated.

<Frame>
  <img />
</Frame>

*Keywords: edit color, preset color, custom hex, colour, preset colour*

# Edit Embed Content

Source: https://docs.drip.re/bot-documentation/drip-features/magic-embed-builder/embeds/edit-embed-content

Set the text that will be displayed in the embed

This option allows you to set the text that will be displayed in the embed. When clicking the option, a form will be opened where you can fill in the following:

* Title of the embed

* URL that redirects users when they click on the title

* Description of the embed

<Frame>
  <img />
</Frame>

Once you submit the information, the embed is updated.

<Frame>
  <img />
</Frame>

*Keywords: embed content, title, description*

# Edit Fields

Source: https://docs.drip.re/bot-documentation/drip-features/magic-embed-builder/embeds/edit-fields

Set the fields in the embed

This option allows you to set the fields in the embed. "Fields" in an embed feature to provide structure and detail, allowing segmented information within the layout of the embed. They are essentially subsections within the embed content, often used to display a title-value pair for greater clarity.

When clicking the option, you will see different options:

* 📝 Add Field -> Add a new field

* 🗑️ Remove Field -> Remove a field from the embed if any

* ✏️ Edit a Specific Field -> Edit a certain field

<Frame>
  <img />
</Frame>

### Add Field

This option allows you to set the values of the field. When clicking the option, a form will be opened where you can fill in the following:

* Name -> 'Title' of the field

* Value -> Displayed under the name

* Is Inline -> Type yes/ no whether you want the field inline. Inline determines whether the field will be displayed in-line with other fields. If set to 'yes', multiple fields can be shown side by side (given space constraints), otherwise, they'll be displayed one below the other.

<Frame>
  <img />
</Frame>

Once you submit the information, the embed is updated.

<Frame>
  <img />
</Frame>

### Remove Field

This option allows you to remove a field from the embed. When you click on the option, a form opens where you can select the field you want to remove. You can remove it by selecting it.

<Frame>
  <img />
</Frame>

### Edit a Specific Field

This option allows you to edit the values of a specific field. When clicking the option, all the existing fields will be listed. Select the one you want to edit. Once you clicked the field that you want to update, it will update a form similar to [Add Field](/drip-features/magic-embed-builder/embeds/edit-fields#add-field).

<Frame>
  <img />
</Frame>

*Keywords: edit fields, add field, remove field*

# Edit Footer

Source: https://docs.drip.re/bot-documentation/drip-features/magic-embed-builder/embeds/edit-footer

Set the footer of the embed

This option allows you to set the author of the embed. When clicking the option, a form will be opened where you can fill in the following:

* Footer Name

* URL for the icon that will be displayed in the footer

<Frame>
  <img />
</Frame>

Once you submit the information, the embed is updated.

<Frame>
  <img />
</Frame>

<Info>✨ This feature is only available for the Pro Tier</Info>

*Keywords: edit footer, footer name*

# Edit Media

Source: https://docs.drip.re/bot-documentation/drip-features/magic-embed-builder/embeds/edit-media

Set the images of the embed

This option allows you to set the images of the embed. When clicking the option, a form will be opened where you can fill in the following:

* Image URL -> Image at the bottom of the embed (Green box)

* Thumbnail URL -> Image in the upper right corner next to the text (Pink Box)

<Frame>
  <img />
</Frame>

Once you submit the information, the embed is updated.

<Frame>
  <img />
</Frame>

*Keywords: edit media, image URL, thumbnail URL*

# Edit Text Above Embed

Source: https://docs.drip.re/bot-documentation/drip-features/magic-embed-builder/embeds/edit-text-above-embed

Set a text that will be displayed above the embed

This option allows you to set a text that will be displayed above the embed. When clicking the option, a form will be opened where you can fill in the text that you want to be displayed.

<Frame>
  <img />
</Frame>

Once you click submit, you will see your text on top of the embed.

<Frame>
  <img />
</Frame>

*Keywords: text above embed*

# Prizes

Source: https://docs.drip.re/bot-documentation/drip-features/prizes

Create raffles for your members to spend tokens on!

### Creating a Prize

To create a Prize, use the command `/create` and select `🎁 Prize`.

<Frame>
  <img />
</Frame>

#### Edit Giveaway

This option allows you to edit the embed with the information of your Giveaway. You can edit the following:

* Giveaway Title

* Giveaway Description

* Giveaway Image

* Giveaway Thumbnail

* More Info Link

<Frame>
  <img />
</Frame>

### Edit Settings

Here you can configure the settings of your item:

* Entry Limit in Points

* Min entry in Points *(Leave blank if no minimum)*

* The number of winners

<Frame>
  <img />
</Frame>

#### Edit End Time

Here you can set the end time of your giveaway. There are some preset options you can use or you can set a custom time.

<Frame>
  <img />
</Frame>

If you would like to set a custom end date, there are 2 options:

<Tabs>
  <Tab title="Relative Time Format">
    To set a custom end date by using the **Relative Time Format**, scroll down in the select menu and click the option `⚙️Custom`.

    Once you click the option, enter the time in the correct format and click `Submit`.

    Time format options:

    * 'y' for years
    * 'M' for months (Capital)
    * 'w' for weeks
    * 'd' for days
    * 'h' for hours
    * 'm' for minutes (Lowercase)

    <Frame>
      <img />
    </Frame>
  </Tab>

  <Tab title="Custom Timestamp">
    <Frame>
      <img />
    </Frame>

    A custom timestamp gives you absolute control over when your giveaway ends down to the second.

    **How to get the timestamp?**

    Go to [this website](https://timestampgenerator.com/), and select the date and time you want your giveaway to end. Then, click `Submit`. In `Common Date Formats`, copy the `timestamp`. Now click `Enter Timestamp` below and paste it into the form.

    <Frame>
      <img />
    </Frame>
  </Tab>
</Tabs>

#### Role Settings

This option allows you to limit who can enter the Giveaway by role. Use the 2 selects to choose the fitting roles:

* Required role to enter

* Exclude a role from entering

<Frame>
  <img />
</Frame>

#### Publish the Giveaway

To publish, click the green `🚀Publish` button, this will send your Giveaway in the current channel.

<Frame>
  <img />
</Frame>

### Copy Giveaway

To copy an already existing Giveaway, copy the message ID from the Giveaway you want to duplicate.

<Frame>
  <img />
</Frame>

<Info>
  If you don't see the option to copy the message ID, enable Developer Mode
  under Settings -> Advanced -> Developer Mode
</Info>

Now use the `/create` command and select `🎁 Prize`. Click the `💾Copy Existing` button and paste the ID from the message you copied earlier.

<Frame>
  <img />
</Frame>

Now you see that the entire configuration of the Giveaway is copied.

### Edit Giveaway

To edit an already existing Store Item: **right-click the message** -> **Apps** -> **Edit**

<Frame>
  <img />
</Frame>

When clicking **Edit**, you will now be able to edit the message. For details, follow the steps in [Creating a Prize](/drip-features/prizes#creating-a-prize).

### Entering a Giveaway

To enter a giveaway, click `🎁 Enter` -> Amount of Points you want to enter

<Frame>
  <img />
</Frame>

### Draw Prize

A prize can only be drawn by a **prize master** or **administrator.** To do this go to the Prize, click `🎉Draw Prize.`

<Frame>
  <img />
</Frame>

Once you have confirmed, the bot will choose a winner from the members who have entered. Each entry is a chance to win, the more they enter the greater their chance of winning.

<Frame>
  <img />
</Frame>

Once a winner is chosen, the message will be updated.

<Frame>
  <img />
</Frame>

<Info>
  A prize can always be redrawn by following the exact same steps from above.
</Info>

# Overview

Source: https://docs.drip.re/bot-documentation/drip-features/quests

Create Quests for community members to engage with Social Media Posts

<Info>
  The Drip Rewards Free Forever plan allows 3 active quests at one time. For
  unlimited quests, upgrade to the Drip Rewards Pro plan.
</Info>

### Creating a Quest

To create a Quest, use the `/drop` command

<Frame>
  <img />
</Frame>

After typing the command and clicking enter, the following embed will be sent to the channel

<Frame>
  <img />
</Frame>

There are currently three different categories of Quests:

* **X Quests:** Create a Quest for members to engage with a post or profile on X

* Discord Quests: Create a Quest for members to engage in the Discord community

* **Custom Quests:** Create a custom Quest for members to engage with almost anything

Choose the type of Quest you would like to create from the dropdown menu

<Frame>
  <img />
</Frame>

<Info>
  Discord Quests can only be created by users with the Admin, Co-Admin, or Quest
  Master roles
</Info>

<CardGroup>
  <Card title="❌" href="/drip-features/quests/x-quests">
    Create Quests for member to engage with a post or profile on X
  </Card>

  <Card title="💬 Discord Quests" href="/drip-features/quests/discord-quests">
    Create a Quest for members to engage in the Discord community
  </Card>

  <Card title="✨" href="/drip-features/quests/custom-quests">
    Create a custom Quest for members to engage with almost anything
  </Card>
</CardGroup>

<Warning>Share Quest Rewards are no longer used</Warning>

<Accordion title="Share Quest Rewards">
  **Depreciated!**

  You have the option to share Quest rewards on Twitter after completing a Quest in your community. To do this, complete an active quest by clicking on the `Verify` button.

  <img alt="Complete a Quest and click on the Verify button" />

  After clicking this button, Drip Rewards will check to see if you completed all of the requirements before rewarding you points. To share your reward on Twitter, click on the `Share` button

  <img alt="Click on the Share button" />

  After clicking this button, a drafted Twitter post will show up. Click on the `Tweet Now` button and Drip Rewards will post your Quest rewards to Twitter for you!

  <img alt="Click on the Tweet Now button" />

  Check your Twitter profile to see the Quest Rewards post

  ![Shared Quest](https://docs.drip.re/~gitbook/image?url=https%3A%2F%2F2728597434-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxUaE8LDXTeS85PkKxJJa%252Fuploads%252FDSS6fItCYTjg9FdBGOQB%252F%289%29%2520Shlig%2520on%2520X%2520I%2520just%2520earned%252025%2520HUNNY%2520for%2520completing%2520a%2520Quest%2520at%2520%2540badbearsio%2520t.co3uio694Eo2%2520X%25202024-02-24%2520at%252010.02.42%2520AM.jpg%3Falt%3Dmedia%26token%3Dcd62fe61-603d-46e6-b1e5-a666b3b48a68\&width=300\&dpr=4\&quality=100\&sign=9c9b4952\&sv=1)
</Accordion>

*Keywords: quest, /drop, share*

# Overview

Source: https://docs.drip.re/bot-documentation/drip-features/quests/custom-quests

Create a Quest that requires members to perform an action of your choosing

### Creating a Custom Quest

To create a Custom Quest, click on `✨ Custom Quests` from the dropdown menu

<Frame>
  <img />
</Frame>

A form will appear for you to enter information about the custom quest.

<Frame>
  <img />
</Frame>

This information will now appear in the Quest embed

<Frame>
  <img />
</Frame>

After adding requirements to the Custom Quest, you can modify different components:

* ✨ Reward&#x73;**:** Modify the total budget and amount of points per claim. You can also select a role to reward upon completion of the quest

<Info>
  Custom Quests have the ability to give "Custom Rewards"

  <img alt="" />
</Info>

* ✨ Reward&#x73;**:** Modify the total budget and amount of points per claim. You can also choose a role to reward, or apply a multiplier for future points earned

* ⏱ **Time:** Change the expiry limit of the Quest (leave blank for no expiry)

* 🔔 Role&#x73;**:** Select roles to mention in the Quest

* ✏️ **Customize:** Customize how the Quest looks

* 📄 **Templates:** Create or Select a Quest template

<Frame>
  <img />
</Frame>

Click the publish button to send the Quest when finished. A thread will also be created for the creator of the Quest to [verify entries](/drip-features/quests/custom-quests/verify-entries).

<Frame>
  <img />
</Frame>

<Frame>
  <img />
</Frame>

# Verify Entries

Source: https://docs.drip.re/bot-documentation/drip-features/quests/custom-quests/verify-entries

When an entry is submitted on a Custom Quest, it must be verified by the Quest Creator

When a Custom Quest is published, a new thread will be created for entries to be verified

<Frame>
  <img />
</Frame>

When a new entry for the Custom Quest is submitted, it will be sent in this thread as seen below:

<Frame>
  <img />
</Frame>

After reviewing the submission, you can choose to **Approve, Deny, and/or Tip Extra** to verify

# Discord Quests

Source: https://docs.drip.re/bot-documentation/drip-features/quests/discord-quests

Create a Quest for members to engage in the Discord community

<Info>
  Discord Quests can only be created by users with the Admin, Co-Admin, or Quest
  Master roles
</Info>

### Creating a Discord Quest

To create an Discord Quest, click on `Discord Quests` from the dropdown menu

<Frame>
  <img />
</Frame>

Discord Quests come with six different options for engagement:

* 💸 **Total Tipped in Server:** Reward members for tipping a certain number of points

* 🔗 **Wallet Linked:** Reward members for linking their wallet(s) to Drip Rewards

* 📅 **Days in Server:** Reward members for being in the community a certain number of days

* 🚀 **Boosted Server:** Reward members for boosting the Discord server

* 💌 **Invited User To Discord:** Reward members for inviting users to the Discord server

* 🎉 **Participate In Event:** Reward members for participating in a Discord event

Choose which type(s) of engagement you want from the dropdown menu

<Frame>
  <img />
</Frame>

After choosing engagement option(s) you can modify different components of the quest:

* ✨ Reward&#x73;**:** Modify the total budget and amount of points per claim. You can also choose a role to reward, or apply a multiplier for future points earned

* ⏱ **Time:** Change the expiry limit of the Quest (leave blank for no expiry)

* 🔔 Role&#x73;**:** Select roles to mention in the Quest

* ✏️ **Customize:** Customize how the Quest looks

* 📄 **Templates:** Create or Select a Quest template

<Frame>
  <img />
</Frame>

Click the publish button to send the Quest when finished

<Frame>
  <img />
</Frame>

# Overview

Source: https://docs.drip.re/bot-documentation/drip-features/slash-commands

Commands that can be used

Drip Rewards comes with several slash commands allowing users easy interaction with the bot. To send a slash command, type / in the message box followed by the command you want to send.

## Commands

<CardGroup>
  <Card title="💸">
    Tip your fellow members with your Points
  </Card>

  <Card title="🏦">Check your Points balance</Card>

  <Card title="🌧️ Drop">
    Make it rain Points that can be claimed by members
  </Card>
</CardGroup>

# Balance

Source: https://docs.drip.re/bot-documentation/drip-features/slash-commands/balance

Displays your Points balance

To use this command type `/balance` in the message box:

<Frame>
  <img />
</Frame>

Once you have entered the command, click enter and you will see the following message with your balance displayed:

<Frame>
  <img />
</Frame>

# Tip

Source: https://docs.drip.re/bot-documentation/drip-features/slash-commands/tip

Tip your fellow members with your Points

To use this command type `/tip user: name amount: 999 note: Note` in the message box where U**ser** is the user you want to tip, **Amount** is the number of Points you want to tip and **Note** is an optional message you want to add.

<Frame>
  <img />
</Frame>

Once you have entered the command, click enter and you will see the following message:

<Frame>
  <img />
</Frame>

Click the `✔️ Confirm` button to confirm and send your tip. Now your tip will appear in the channel:

<Frame>
  <img />
</Frame>

<Accordion title="Dedicate a Tip Channel">
  Don't want all of your community member's tips being sent in random channels? Dedicate a specific channel for tips to be sent in when they are created! To do this, navigate to `Settings > Point settings` then click on `Tip Logs` from the dropdown menu

  <img alt="" />

  Then select which channel you would like tips to be sent in from the dropdown menu or have Drip create one for you!

  <img alt="" />

  Now when members send a tip, the embed will be sent to a dedicated channel
</Accordion>

# Overview

Source: https://docs.drip.re/bot-documentation/drip-features/store

Create buyable items for your members to spend tokens on!

### Creating a Store Item

To create a Store Item, use the `/create` command and choose `📦 Store Item`.

<Frame>
  <img />
</Frame>

After typing the command and clicking enter, the following embed will be sent to the channel

<Frame>
  <img />
</Frame>

Choose the option you would like to edit by clicking one of the buttons or selecting from the dropdown menu

<Tabs>
  <Tab title="Edit Store Item">
    To edit a store item click on the `Edit Store Item` button

    <Frame>
      <img />
    </Frame>

    A form will appear for you to edit the item name, description, thumbnail, and image displayed in the embed

    <Frame>
      <img />
    </Frame>
  </Tab>

  <Tab title="Edit Settings">
    To edit store item settings click on the `Edit Settings` button

    <Frame>
      <img />
    </Frame>

    A form will appear for you to edit the price, max per person, and stock of the item

    <Frame>
      <img />
    </Frame>
  </Tab>

  <Tab title="Role Settings">
    To edit store item role settings click on the `Role Settings` button

    <Frame>
      <img />
    </Frame>

    Use the 3 dropdown menus to choose the fitting roles to be rewarded, excluded, or required to purchase the item

    <Frame>
      <img />
    </Frame>
  </Tab>

  <Tab title="🧵 Create Thread on Purchase">
    Use the dropdown menu and select `🧵 Create Thread on Purchase` to edit whether a Thread is created when an item is purchased

    <Frame>
      <img />
    </Frame>

    A green ✅ will appear next to the menu item when the feature is enabled

    <Frame>
      <img />
    </Frame>
  </Tab>

  <Tab title="💰 Require Buyer Input">
    Use the dropdown menu and select `💰 Require Buyer Input` to require buyers to select a wallet or input custom text before purchasing an item

    <Frame>
      <img />
    </Frame>

    Now you can select the type of input required of a user before they can purchase the store item. You can choose from the following options:

    * 💰 **Wallet:** Require the buyer to input their wallet before purchasing
    * 🔧 **Custom:** Require the buyer to input something custom before purchasing

    <Frame>
      <img />
    </Frame>
  </Tab>
</Tabs>

To publish, click the green `🚀Publish` button. This will send your Store Item to the current channel

<Frame>
  <img />
</Frame>

# Copying Store Items

Source: https://docs.drip.re/bot-documentation/drip-features/store/copying-store-items

You can copy a store item to send in a different channel

To copy an already existing Store Item, right-click the store item you want to duplicate and copy the message ID.

<Frame>
  <img />
</Frame>

<Info>
  If you don't see the option to copy the message ID, enable Developer Mode
  under Settings -> Advanced -> Developer Mode
</Info>

Now use the `/create type: 📦 Store Item` command. Click the `💾Copy Existing` button and paste the ID from the message you copied earlier

<Frame>
  <img />
</Frame>

Now you will see that the entire configuration of the Store item is copied to that embed

<Frame>
  <img />
</Frame>

# Editing Store Items

Source: https://docs.drip.re/bot-documentation/drip-features/store/editing-store-items

You can make changes to store items after they have been published

To edit an already existing Store Item, right-click the store item you want to edit and select edit from the menu

<Frame>
  <img />
</Frame>

After clicking edit from the menu, you will be able to edit the store item. For details, follow the steps in[Creating a Store Item](/drip-features/store#creating-a-store-item)

# Retrieving a CSV File

Source: https://docs.drip.re/bot-documentation/drip-features/store/retrieving-a-csv-file

Get a CSV File containing information about the sales of a store item

Members with the role of Store Manager and/or administrators can request a CSV file containing all sales of an item. To do this click `🎒 My Backpack` -> `📖 Export Sheets`.

CSV files are exported to Google Sheets and include:

* User Name

* User ID

* Price

* Quantity

* Selected Wallet

# User Dashboard

Source: https://docs.drip.re/bot-documentation/drip-features/user-dashboard

The Dashboard is a central place for your community to manage points.

Creating the Dashboard

<Info>Only an administrator can create the dashboard</Info>

1. **Creating the Dashboard:** Visit the `#🛠┆admin` channel and click `Create Channels > Create Specific` and select "Dashboard".

<Frame>
  <img />

  `#🛠┆admin`
</Frame>

<Frame>
  <img />
</Frame>

1. You can create the dashboard Magic Embed in a channel directly by using the command `/dashboard ChannelName` - This can also be used to reset the Dashboard embed.

<Frame>
  <img />
</Frame>

### Using the Dashboard

<Frame>
  <img />
</Frame>

#### Buttons on the Main Embed

* **⚡My Dashboard:** Navigate to your dashboard with details about points, NFTs, and more.

* **🏆 Leaderboard:** See other community members with the highest point counts.

* **🔎 Check NFT Balance:** Check the balance of specific NFTs from activated collections.

* **Support:** Join the Drip Discord for support and follow us on Twitter for the latest updates

<Info>
  **Pro Feature:** Right-click the embed then use `App > Edit` to change various features of your community dashboard including image, embed title, description, and color.

  ![](https://docs.drip.re/~gitbook/image?url=https%3A%2F%2F2728597434-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxUaE8LDXTeS85PkKxJJa%252Fuploads%252F33dxKeYBDYc3Zr0KLKOx%252F%2523%25E3%2580%258C%25E2%259A%25A1%25E3%2580%258Ddashboard%2520%2524WOJAK%2520x%2520Anonthology%2520-%2520Discord%25202024-02-24%2520at%25203.06.43%2520PM.jpg%3Falt%3Dmedia%26token%3D1a495dcc-d879-44e5-85ec-7104cb79db1d\&width=300\&dpr=4\&quality=100\&sign=be15c07d\&sv=1)
</Info>

### Detailed Features

<Tabs>
  <Tab title="⚡️ My Dashboard">
    Displays an overview of your account:

    * Points balance
    * Daily points generation (yield)
    * Time remaining until your next claim
    * The number of NFTs you own from the server's activated collection(s).

    <Frame>
      <img />
    </Frame>

    **Dashboard Buttons:**

    1. **Claim Tokens:** Harvest all the Points from your NFTs.
    2. **🔗 Pair/Unpair NFTs:** These buttons are visible only when the server has a multiplier. Use them to pair or unpair NFTs.
    3. **🔎 Browse NFTs:** Navigate through your NFTs from activated collections. Check details and harvest tokens from generator NFTs. [Read More](/drip-features/user-dashboard/browse-nfts)
    4. **⚙️ Settings:** Manage your Twitter account and Web3 Wallets – adding or removing them. [Read More](/drip-features/user-dashboard/user-settings/wallet-settings)
  </Tab>

  <Tab title="🏆 Leaderboard">
    Displays community members with the highest point counts:

    <Frame>
      <img />
    </Frame>

    You can exclude certain roles from appearing in the Leaderboard. [Read more](/admin-settings/admin-dashboard/admin-settings/member-roles)

    Admins can enable/disable the Leaderboard. [Read more](/admin-settings/admin-dashboard/admin-settings/points-settings)
  </Tab>

  <Tab title="🔎 Check NFT Balance">
    Enter the NFT ID of your choice from an activated collection to see how many points it holds.

    <Frame>
      <img />
    </Frame>
  </Tab>
</Tabs>

### Learn More About

<CardGroup>
  <Card title="🔎" href="/drip-features/user-dashboard/browse-nfts">
    The browse NFTs is the way for users to check their NFTs from imported collections and harvest generators.
  </Card>

  <Card title="💰" href="/drip-features/user-dashboard/user-settings/wallet-settings">
    The wallets section in the dashboard is the place to manage all of your wallets.
  </Card>
</CardGroup>

*Keywords: dashboard, leaderboard, points balance, claim points, pair/unpair NFTs, browse NFTs*

# Browse NFTs

Source: https://docs.drip.re/bot-documentation/drip-features/user-dashboard/browse-nfts

View NFTs you hold from the server's activated collections.

### Browse NFTs

Go to your [Dashboard](/drip-features/user-dashboard) and click the `🔎 Browse NFTs` button.

<Frame>
  <img />
</Frame>

Choose an activated collection you want to browse.

<Frame>
  <img />
</Frame>

Once you make a selection, all owned NFTs in that collection are displayed from your connected wallets. When the collection type is a `🔥 ``Generator`, it will also display the points balance the NFT currently holds.

<Frame>
  <img />
</Frame>

If you click on an NFT, you will get a display similar to the one below depending on the type of NFT effect:

<Tabs>
  <Tab title="🙂 No Effect">
    * Link to [Preferred Marketplace](/admin-settings/admin-dashboard/admin-settings/web3-settings/preferred-marketplace)
    * ID + Name of the NFT
    * Image of the NFT

    <Frame>
      <img />
    </Frame>
  </Tab>

  <Tab title="🔥 Generator">
    * Link to [Preferred Marketplace](/admin-settings/admin-dashboard/admin-settings/web3-settings/preferred-marketplace)
    * ID + Name of the NFT
    * Image of the NFT
    * Current points balance
    * Number of daily points it is generating (yield)
    * Paired NFTs
    * Button to claim the points of this individual NFT

    <Frame>
      <img />
    </Frame>
  </Tab>

  <Tab title="⚡️ Multiplier">
    * Link to [Preferred Marketplace](/admin-settings/admin-dashboard/admin-settings/web3-settings/preferred-marketplace)
    * ID + Name of the NFT
    * Image
    * Multiplier amount
    * Paired NFTs

    <Frame>
      <img />
    </Frame>
  </Tab>
</Tabs>

*Keywords: browse NFTs, connected wallet, no effect, generator, multiplier*

# Overview

Source: https://docs.drip.re/bot-documentation/drip-features/user-dashboard/user-settings

Manage your Twitter account and Web3 Wallets

You can access user settings by clicking the Settings button in the user [dashboard](/drip-features/user-dashboard#my-dashboard).

<Frame>
  <img />
</Frame>

A new embed will appear with the following options:

* [⚙️ **Wallet Settings:**](/drip-features/user-dashboard/user-settings/wallet-settings) Change your wallet settings

* [**𝕏 X Settings:**](/drip-features/user-dashboard/user-settings/x-settings) Link your X/Twitter account

<Frame>
  <img />
</Frame>

# Wallet Settings

Source: https://docs.drip.re/bot-documentation/drip-features/user-dashboard/user-settings/wallet-settings

Manage and link your Web3 wallets

### Open wallet settings

<Frame>
  <img />
</Frame>

After clicking on the `✨ My Dashboard` button, click the `⚙️ Wallet Settings` \*\*\*\*button.

<Frame>
  <img />
</Frame>

### Adding a new wallet

You can add up to 10 wallets. To add a wallet use the green `➕` button.

<Frame>
  <img />
</Frame>

After using the button, you will get 2 options to add a wallet.

<Frame>
  <img />
</Frame>

* Link wallet using a traditional wallet connect via a message signature

* Link wallet using an Marketplace bio verification system **(most secure)**

### Traditional Wallet Linking

If you choose the Traditional `Link Wallet` option, the following message is displayed:

<Frame>
  <img />
</Frame>

Use the Link Wallet button to go to the Wallet Connect page:

<Frame>
  <img />
</Frame>

Click the Link Wallet button and choose the right wallet option.

Then, return to this page and use the `Link Wallet` button again. Check if the message matches the message from Discord. Sign only if it does.

Now your wallet is connected to your Discord account.

### Marketplace Bio Verification

Marketplace `Bio Verification` is the most secure linking option available because the signing happens on a website many people trust. For this example we will use OpenSea. If you choose this method, you will get the following window where you must enter your Marketplace username OR wallet address:

<Frame>
  <img />
</Frame>

Once you click **Submit**, you will be given a secret code to paste into your Marketplace bio.

<Frame>
  <img />
</Frame>

Now go to your OpenSea profile and click the 3 dots on the right side of your screen.

<Frame>
  <img />
</Frame>

Paste the code into the bio text field and click **save**.

<Frame>
  <img />
</Frame>

Now go back to your discord and click the ✅**Verify** button. A message similar to the one below should be displayed.

<Frame>
  <img />
</Frame>

### Unlinking a Wallet

To unlink a wallet, use the "Select the wallet you want to use" dropdown menu to choose the wallet you want to unlink.

<Frame>
  <img />
</Frame>

You will see that your message has been edited and displays the wallet you selected:

<Frame>
  <img />
</Frame>

Click the ❌ button to unlink the selected wallet from your account.

### Setting Primary Wallet

The primary wallet is the wallet that is visible to server admins when they need to send out a prize or a purchased store item.

To set a wallet as your primary wallet, use the "Select the wallet you want to use" dropdown menu to choose the wallet you want to set as your primary wallet.

<Frame>
  <img />
</Frame>

You will see that your message has been edited and displays the wallet you selected:

<Frame>
  <img />
</Frame>

Click the ⭐ button to set the selected wallet as your primary wallet.

<Info>
  If a member has only 1 wallet, this will automatically be their primary
  wallet.
</Info>

*Keywords: wallets, manage wallets, link wallets, wallet settings, marketplace verification, bio verification, opensea verification, primary wallet*

# X Settings

Source: https://docs.drip.re/bot-documentation/drip-features/user-dashboard/user-settings/x-settings

Link your X/Twitter account

After clicking on the `X Settings` button in [User Settings](/drip-features/user-dashboard/user-settings), a new embed will appear

<Frame>
  <img />
</Frame>

To link an X Account, click on the `Link X` button, a new embed will appear

<Frame>
  <img />
</Frame>

Click on the `Link X` button again to be redirected to the landing page and connect your Twitter

<Frame>
  <img />
</Frame>

Click on `Authorize App` \*\*\*\*to link your X Account to Drip Rewards/ For more information about permissions. required, you can [read our FAQ](/faq/what-twitter-permissions-are-required-by-drip). Your Twitter Settings Menu will now appear something like this:

<Frame>
  <img />
</Frame>

*Keywords: link x, link twitter, x account, twitter account, x permissions, twitter permissions*

# Web3 Features

Source: https://docs.drip.re/bot-documentation/drip-features/web3-features

Activate rewards for your NFT or Crypto communities!

Web3 is available for communities that are subscribed to the Pro or Custom Plans. Web3 comes with a multitude of highly customizable features:

* 🔥 **Manage Activations:** Reward NFT or Token holders with different collection effects

<Tabs>
  <Tab title="🙂 No Effect">
    This feature lets users view their NFTs/Tokens in the [User Dashboard](/drip-features/user-dashboard#my-dashboard) and does not result in any point generation or multipliers
  </Tab>

  <Tab title="🔥 Generator Effect">
    Collections with the **Generator Effect** generate tokens daily; you can set
    the number of tokens by importing the collection and selecting the amount you
    would like
  </Tab>

  <Tab title="Multiplier">
    Collections with the **Multiplier Effect** allow your holders to multiply the number of points their Generators make daily. You can **pair up to 2 generators** per multiplier. For example, say you have Bad Bears NFT Collection making 5 tokens per day as the Generator. You can activate the Bad Cubs NFT Collection to have a 3x Multiplier, and now your paired Bad Bears NFTs are making 15 tokens per day.
  </Tab>
</Tabs>

Collections with the **Generator Effect** generate tokens daily; you can set the number of tokens by importing the collection and selecting the amount you would like

Collections with the **Multiplier Effect** allow your holders to multiply the number of points their Generators make daily. You can **pair up to 2 generators** per multiplier. For example, say you have Bad Bears NFT Collection making 5 tokens per day as the Generator. You can activate the Bad Cubs NFT Collection to have a 3x Multiplier, and now your paired Bad Bears NFTs are making 15 tokens per day.

* 💰 **NFT Sales Tracker:** Track the sales of NFT Collections for community members

* 🐸 **NFT Meme Maker:** Allow community members to create mems of their NFTs

* 🛒 **Preferred Marketplace:** Set your preferred marketplace

Learn more in the [Web3 Settings Module](/admin-settings/admin-dashboard/admin-settings/web3-settings)

# Join us on Discord

Source: https://docs.drip.re/bot-documentation/external-link-0

# Follow us on X

Source: https://docs.drip.re/bot-documentation/external-link-2

# Overview

Source: https://docs.drip.re/bot-documentation/faq/how-do-i-contact-support

Our friendly support team is here to help. Learn what information to share and when can you an expect a response.

You can contact us by opening a ticket on our [Discord](https://discord.gg/dripchain) server.

### What information should I share?

To help *us* help *you* as efficiently as possible, you must send us all the relevant information:

* Describe the steps you took, what happens when you take those steps, and what you expect to happen instead.

* If you encounter an error message, please provide the full error message.

* Can you send us a screenshot to show us what you see? Or can you send us a short video to show us the steps you take? These are very helpful!

## When will I get a response?

We try to reply to every message within 1 business day. During busy times this may not be possible, but we will always get back to you as soon as possible! In the meantime, make sure to read through our documentation at [https://docs.drip.re](https://docs.drip.re).

# How do I whitelist Drip with Wick Bot?

Source: https://docs.drip.re/bot-documentation/faq/how-do-i-whitelist-drip-with-wick-bot

How to prevent Drip Rewards from being kicked by Wick Bot

The Wick Bot is a great tool for Discord security and is notorious for "wrongfully" kicking verified members/bots from servers if whitelist roles are not properly configured. Here is how you can set the Wick Bot to work together with Drip Rewards:

<Info>
  This is not a tutorial for the entire setup of the Wick Bot. If you have not
  properly set up certain components, the whitelist may not work. Please refer
  to Wick Bot documentation/support for initial setup and any ongoing issues.
</Info>

### Types of Whitelist

The Wick Bot has 4 different types of whitelists, each allowing different members/roles to do different things without risk of consequence. It is your choice to whitelist Drip Rewards for the various categories that fit your needs best.

* **Spam Whitelist:** Allows members/roles to send multiple messages at a time and walls of text

* **Mentions Whitelist:** Allows members/roles to repeatedly mention other members and roles

* **Invite Links Whitelist:** Allows members/roles to post invite links to other Discord servers

* **@Everyone Whitelist:** Allows members/roles to mention @everyone and other public roles

The process for whitelisting a member/role with the Wick Bot is the same for all 4 types. For this example, we will be showing you how to give Drip Reward the Mentions Whitelist.

### How to Whitelist Drip Rewards

<Warning>
  If using Wick Premium, you must ensure Anti-Nuke Protection is disabled before
  installing or setting up Drip Rewards
</Warning>

Navigate to your server's Wick Dashboard and click on Whitelist in the Auto Mod category. Ensure Auto Mod is properly set up beforehand.

<Frame>
  <img />
</Frame>

Click on the Mention tab to modify whitelist permissions

<Frame>
  <img />
</Frame>

Click on the dropdown menu under Roles and select the Drip role to whitelist Drip Rewards

<Frame>
  <img />
</Frame>

<Frame>
  <img />
</Frame>

Be sure to save your changes!

Drip Rewards should now be able to mention members without consequence from the Wick Bot. The process is the same for the other 3 categories.

# What Discord permissions does Drip need?

Source: https://docs.drip.re/bot-documentation/faq/what-discord-permissions-does-drip-need

These are the permissions that Drip Rewards needs to function properly in your community

Drip Rewards requires admins to give it certain permissions that allow it to run properly in the community. Each permission plays a vital role in the functionality of Drip. Below are the required permissions as well as explanations to help you better understand how they are used by Drip.

<Frame>
  <img />
</Frame>

### Discord Permissions

* **Manage Roles**

  * The magic embed builder can [Give/Take Role](/drip-features/magic-embed-builder/components/give-take-role) when users click a button

  * Allows Drip to assign to team members for tasks such as creating store items, prizes, or admin quests

* **Manage Channels**

  * Drip Rewards can automatically set up channels when [Getting Started](/)

* **Read Messages**

  * This is an essential permission that allows Drip to see when users are using commands such as `/tip` or `/create`

* **Send Messages**

  * This is an essential permission that allows Drip to send messages and embeds in the community

* **Send Messages in Threads, Create Public/Private Threads, & Manage Threads**

  * This allows Drip to create and send messages in threads for features such as the [Games](/drip-features/games)and [Store](/drip-features/store)

* **Embed Links**

  * Links to external platforms are embedded for interactive features like [Quests](/drip-features/quests)

* **Attach Files**

  * This is an essential permission that allows Drip to include images in embeds it sends

* **Read Message History**

  * This is used for an upcoming AI feature that allows Drip to summarize daily conversations and create a sentiment analysis for admins

* **Add Reactions**

  * This is an essential permission for various interactive elements that Drip uses throughout the community

* **Use External Emoji**

  * This is an essential permission that allows Drip to use emojis from its server for branding and to enhance your community interaction

# Getting Started

Source: https://docs.drip.re/bot-documentation/home

This is a basic guide to help get Drip Rewards installed in your community

<AccordionGroup>
  <Accordion title="Step 1: Install Drip Rewards">
    Visit [this link](https://discord.com/oauth2/authorize?client_id=1047256251320520705\&permissions=395405806672\&scope=bot%20applications.commands) to invite Drip Rewards into your Discord Server. If you have a Custom Plan with white label, you will receive a separate link.

    **Do you have Wick Installed?**

    Please refer to [Whitelisting with Wick](/faq/how-do-i-whitelist-drip-with-wick-bot) to make sure Drip can perform all necessary functions.
  </Accordion>

  <Accordion title="Step 2: Initial setup">
    Click the "Let's Go!" button in the `#🛠┆admin` channel after installation to open the initial setup for Drip Rewards.
  </Accordion>

  <Accordion title="Step 3: Create Channels">
    *(optional)*[](#step-3-create-channels-optional)

    Click the "Create Channels" button to create the base channels that your community needs to start using Drip right away. Edit the permissions in individual channels to allow other users to see them, and you're good to go!
  </Accordion>

  <Accordion title="Step 4: Activate WEB3">
    *(optional)*[](#step-4-activate-web3-optional)

    In the `#🛠┆admin` channel visit `Settings > WEB3 Setup` to turn on [Web3 features](/drip-features/web3-features).
  </Accordion>
</AccordionGroup>

After you have completed the initial setup, you can begin playing with more settings, or go ahead and open up the newly made channels to your community.

*Keywords: getting started, install, initial setup, create channels, activate web3*

# Admin Setup

Source: https://docs.drip.re/burn-ghosts-activity/admin-setup

Essential Discord slash commands for server administrators to configure Burn Ghosts Activity

## Overview

Server administrators must run two essential slash commands to enable full functionality of the Burn Ghosts Activity. These are **one-time setup commands** that connect your server to the DRIP Rewards system and configure tournament management permissions.

<Warning>
  Both commands require **Administrator** Discord permissions to execute.
</Warning>

## Discord Slash Commands

### `/authorize` (Admin Only)

Connects your Discord server to the DRIP Rewards system for token reward distribution.

<Card title="Purpose" icon="link">
  Links your Discord server to DRIP Rewards so tournament prizes can be distributed as tokens
</Card>

**What it does:**

* Generates a DRIP authorization link for your server
* Provides DRIP bot install button if not already installed
* Links server to a DRIP realm for automatic reward distribution
* Enables token balance viewing and transactions

**When to use:**

* **Required first** before hosting tournaments with token rewards
* Must be run once during initial setup
* Re-run if you need to re-authorize or change DRIP realm connection

<Steps>
  <Step title="Run the command">
    Type `/authorize` in any channel where you have permissions
  </Step>

  <Step title="Click authorization link">
    Follow the generated link to connect to DRIP
  </Step>

  <Step title="Install DRIP bot (if needed)">
    If prompted, install the DRIP bot to your server
  </Step>

  <Step title="Complete authorization">
    Confirm the connection in the DRIP interface
  </Step>
</Steps>

### `/set_master_role` (Admin Only)

Configures which Discord role can access tournament management features in the activity.

<Card title="Purpose" icon="user-shield">
  Determines who can create and manage tournaments in the admin panel
</Card>

**What it does:**

* Takes a Discord role as a parameter
* Grants admin panel access to members with the specified role
* Allows tournament creation, editing, and management
* Controls access to game configuration

**When to use:**

* After running `/authorize` command
* When setting up tournament organizers
* When changing which role manages tournaments

<Steps>
  <Step title="Create a role (if needed)">
    Create a Discord role for tournament managers (e.g., "Tournament Admin")
  </Step>

  <Step title="Run the command">
    Type `/set_master_role` in any channel
  </Step>

  <Step title="Select the role">
    Choose the role from the dropdown parameter
  </Step>

  <Step title="Confirm">
    Members with this role now have admin access in the activity
  </Step>
</Steps>

## Setup Checklist

<AccordionGroup>
  <Accordion title="Step 1: Initial Authorization">
    * Run `/authorize` command
    * Complete DRIP authorization flow
    * Verify DRIP bot is installed
    * Confirm server is linked to DRIP realm
  </Accordion>

  <Accordion title="Step 2: Configure Admin Access">
    * Create or identify the admin role
    * Run `/set_master_role` with chosen role
    * Assign role to tournament managers
    * Verify admin panel access in activity
  </Accordion>

  <Accordion title="Step 3: Test Configuration">
    * Launch Burn Ghosts Activity
    * Check admin panel visibility (admins only)
    * Verify token balances are visible
    * Test creating a sample tournament
  </Accordion>
</AccordionGroup>

## Important Notes

<Info>
  **Setup Order Matters**: Always run `/authorize` before `/set_master_role` to ensure proper functionality.
</Info>

<Warning>
  **Regular Users Don't Need These Commands**: These are server setup commands for administrators only. Regular players can start playing immediately after setup is complete.
</Warning>

### Who Needs What?

| User Type          | Needs /authorize | Needs /set\_master\_role | Can Play |
| ------------------ | ---------------- | ------------------------ | -------- |
| Server Admin       | ✅ Must run       | ✅ Must run               | ✅ Yes    |
| Tournament Manager | ❌ No             | ❌ No (assigned role)     | ✅ Yes    |
| Regular Player     | ❌ No             | ❌ No                     | ✅ Yes    |

## Troubleshooting Commands

### Re-authorizing

If token rewards stop working:

1. Run `/authorize` again
2. Complete the authorization flow
3. Verify connection in DRIP dashboard

### Changing Master Role

To change who can manage tournaments:

1. Run `/set_master_role` with new role
2. Previous role loses admin access
3. New role members gain admin access immediately

### Verification

To verify setup is complete:

* ✅ DRIP bot is present in server
* ✅ `/authorize` completed successfully
* ✅ `/set_master_role` configured with appropriate role
* ✅ Admin panel visible to role members
* ✅ Token balances displaying correctly

<Tip>
  Test your setup with a free tournament first to ensure everything works before creating tournaments with entry fees!
</Tip>

*Keywords: admin setup, slash commands, authorize, set master role, configuration, server setup, discord commands*

# Available Games

Source: https://docs.drip.re/burn-ghosts-activity/games

Explore the 9 exciting mini-games available in Burn Ghosts Activity

The Burn Ghosts Activity features 9 exciting mini-games, each with unique mechanics and scoring systems. Your goal is to achieve the highest score possible!

## Game Library

<CardGroup>
  <Card title="Slaygrounds" icon="helmet-battle">
    Action-packed arena combat
  </Card>

  <Card title="Pinball" icon="gamepad-modern">
    Classic pinball with a twist
  </Card>

  <Card title="Hologon" icon="cube">
    Futuristic puzzle challenges
  </Card>

  <Card title="Vendetta" icon="sword">
    Strategic combat game
  </Card>

  <Card title="Mageboy" icon="hat-wizard">
    Magical adventure platformer
  </Card>

  <Card title="Perch" icon="fish">
    Fishing and collection game
  </Card>

  <Card title="Blockbreak" icon="block-brick">
    Modern brick-breaker arcade
  </Card>

  <Card title="Hyperjump" icon="rocket">
    High-speed jumping challenges
  </Card>

  <Card title="Ghostrun" icon="ghost">
    Spooky endless runner
  </Card>
</CardGroup>

## Game Controls

* Each mini-game has its own control scheme
* Controls are typically explained when you start each game
* Most games use keyboard and/or mouse controls

<Info>
  Each game has unique mechanics and scoring systems. Practice multiple times to learn the best strategies!
</Info>

*Keywords: mini-games, slaygrounds, pinball, hologon, vendetta, mageboy, perch, blockbreak, hyperjump, ghostrun*

# Getting Started

Source: https://docs.drip.re/burn-ghosts-activity/home

Complete guide to participating in tournaments, earning rewards, and having fun with Burn Ghosts Activity mini-games

Welcome to the **Burn Ghosts Activity** on Discord! This is your complete guide to participating in tournaments, earning rewards, and having fun with mini-games.

## 🚀 Getting Started

### Accessing the Activity

<Steps>
  <Step title="Join a Discord server">
    Join a Discord server that has the Burn Ghosts Activity enabled
  </Step>

  <Step title="Look for the activity">
    Find the activity in voice channels or activity launcher
  </Step>

  <Step title="Launch the activity">
    Click to launch the Burn Ghosts Activity
  </Step>

  <Step title="Automatic authentication">
    The activity will automatically authenticate you with your Discord account
  </Step>
</Steps>

### First Time Setup

**For Players:**

* No setup required! The activity automatically connects to your Discord account
* Your progress and rewards are tied to your Discord identity
* Make sure you're in a server that has DRIP Rewards integration for token rewards

**For Server Administrators:**

* Server admins must run setup commands to enable full functionality
* See [Admin Setup](/burn-ghosts-activity/admin-setup) for required Discord slash commands
* Commands include `/authorize` (connect to DRIP) and `/set_master_role` (tournament management)

## 🎯 Understanding Tournaments

### What are Tournaments?

Tournaments are competitive events where players compete in mini-games to win prizes. Each tournament has:

* **🎮 Featured Game**: One specific mini-game for the tournament
* **⏰ Time Limit**: Start and end dates for participation
* **💰 Prize Pool**: Total rewards to be distributed
* **🎫 Entry Fee**: Cost to participate (may be free or require tokens)
* **👥 Participants**: Other players competing for prizes

### Tournament Status Types

* **🟢 Active**: Currently running - you can join and play
* **🟡 Upcoming**: Scheduled to start soon - you can join but not play yet
* **🔴 Ended**: Tournament finished - rewards have been distributed

### Entry Methods

* **Per Tournament**: Pay once to join, play unlimited games during the tournament
* **Per Game**: Pay each time you want to play a game in the tournament

*Keywords: burn ghosts, tournaments, mini-games, discord activity, getting started*

# Navigation & Controls

Source: https://docs.drip.re/burn-ghosts-activity/navigation

Learn how to navigate the activity interface and control games

## 🧭 Sidebar Navigation

The sidebar provides quick access to all major features of the activity:

### Main Navigation Icons

<CardGroup>
  <Card title="Home" icon="house">
    Return to the tournament list and activity homepage
  </Card>

  <Card title="Help" icon="circle-question">
    View guides, tips, and access support resources
  </Card>

  <Card title="Invite" icon="paper-plane">
    Send Discord invites to friends to join your server
  </Card>

  <Card title="Leaderboard" icon="chart-simple">
    View live tournament rankings during active games
  </Card>

  <Card title="Admin" icon="shield-halved">
    Tournament management panel (administrators only)
  </Card>
</CardGroup>

## 🎮 Game Controls

### General Information

* Each mini-game has its own unique control scheme
* Controls are explained when you start each game
* Most games use keyboard and/or mouse controls
* Some games may support gamepad controllers

### Common Control Patterns

<AccordionGroup>
  <Accordion title="Keyboard Controls">
    * Arrow keys or WASD for movement
    * Spacebar for jump or action
    * Number keys for special abilities
    * ESC for pause menu
  </Accordion>

  <Accordion title="Mouse Controls">
    * Click to select or activate
    * Drag for movement or aiming
    * Right-click for secondary actions
    * Scroll wheel for zoom or selection
  </Accordion>

  <Accordion title="Combination Controls">
    Many games use both keyboard and mouse together for optimal gameplay
  </Accordion>
</AccordionGroup>

<Info>
  Pay attention to the control instructions when each game loads. They're designed to help you get started quickly!
</Info>

## 📱 Interface Elements

### Tournament Cards

Each tournament card displays:

* Game name and icon
* Tournament status (Active, Upcoming, Ended)
* Time remaining
* Prize pool amount
* Entry fee (if applicable)
* Current participant count
* Join/Play buttons

### Leaderboard Display

The leaderboard shows:

* Player rankings (1st, 2nd, 3rd, etc.)
* Player names
* High scores
* Your current position (highlighted)
* Prize distribution preview

### Token Balance Indicator

* Displayed in the top corner
* Shows your current DRIP token balance
* Updates automatically after transactions

<Tip>
  Bookmark frequently played tournaments for quick access from the home screen!
</Tip>

*Keywords: navigation, controls, sidebar, interface, game controls, leaderboard, ui*

# How to Participate

Source: https://docs.drip.re/burn-ghosts-activity/participating

Learn how to join tournaments, play games, and track your progress

## 🏆 Joining a Tournament

<Steps>
  <Step title="Browse Active Tournaments">
    Navigate to the home screen and browse available tournaments
  </Step>

  <Step title="Select a Tournament">
    Click on a tournament you want to join
  </Step>

  <Step title="Review the Details">
    Check the entry fee (if any), prize pool and distribution, time remaining, and current participants
  </Step>

  <Step title="Join Tournament">
    Click "Join Tournament" if you meet the requirements
  </Step>

  <Step title="Pay Entry Fee">
    If required, the entry fee will be deducted from your token balance
  </Step>
</Steps>

## 🎮 Playing Games

<Steps>
  <Step title="Join an Active Tournament">
    You must join a tournament before you can play
  </Step>

  <Step title="Click Play">
    Click the "Play" button on the tournament card
  </Step>

  <Step title="Game Launch">
    The mini-game will launch in a new window/frame
  </Step>

  <Step title="Play Your Best">
    Play to achieve your best score
  </Step>

  <Step title="Automatic Submission">
    Your score is automatically submitted when you finish
  </Step>

  <Step title="Keep Improving">
    Play multiple times to improve your ranking (if entry method allows)
  </Step>
</Steps>

## 📊 Checking Your Progress

### Live Leaderboard

Click the chart icon 📊 during games to see real-time rankings and your current position among competitors.

### Tournament Rankings

View your position among all participants in the tournament page. Track how you stack up against the competition.

### Score History

Track your improvement over multiple plays. See your best scores and progression over time.

<Tip>
  Play multiple times to improve your ranking! If the tournament allows unlimited plays per entry, take advantage of it to climb the leaderboard.
</Tip>

*Keywords: join tournament, play games, leaderboard, rankings, progress tracking*

# Rewards & Economy

Source: https://docs.drip.re/burn-ghosts-activity/rewards

Understand prize distribution methods and the token economy

## 💰 Prize Distribution Methods

### 🏆 Top Heavy (Default)

The default distribution favors top performers:

* **1st Place**: 50% of prize pool
* **2nd Place**: 30% of prize pool
* **3rd Place**: 20% of prize pool

### ⚖️ Even Split

Equal opportunity for top three finishers:

* **1st, 2nd, 3rd Place**: Equal share (33.3% each)

### 👑 Winner Takes All

All or nothing competition:

* **1st Place**: 100% of prize pool
* **2nd & 3rd Place**: No rewards

<Info>
  The prize distribution method is set by the tournament organizer when creating the tournament.
</Info>

## 🎁 When Rewards are Distributed

* **Automatically** when tournaments end
* **Instantly credited** to your DRIP token balance
* **No manual claiming** required

## 💎 Token Balance

Your token balance is integrated with the DRIP Rewards system:

* View your current balance in supported servers
* Tokens are managed through the DRIP Rewards system
* Use tokens to pay entry fees for premium tournaments
* Win tokens by placing in tournaments

<Tip>
  Start with free tournaments to build up your token balance before entering premium tournaments with entry fees!
</Tip>

## 📋 Tips for Managing Your Tokens

<AccordionGroup>
  <Accordion title="Start with Free Tournaments">
    Build up your token balance by participating in free tournaments before spending on premium ones.
  </Accordion>

  <Accordion title="Budget Wisely">
    Don't spend all your tokens on one tournament. Diversify your entries to maximize your chances.
  </Accordion>

  <Accordion title="High Risk, High Reward">
    Premium tournaments with entry fees often have bigger prize pools. Assess your skill level before entering.
  </Accordion>

  <Accordion title="Track Your ROI">
    Monitor if your winnings exceed your entry fees over time. Adjust your strategy accordingly.
  </Accordion>
</AccordionGroup>

*Keywords: rewards, prize pool, token economy, prize distribution, winnings*

# Tips for Success

Source: https://docs.drip.re/burn-ghosts-activity/tips

Strategies to maximize your scores and win more tournaments

## 🎯 Maximize Your Scores

### Practice Makes Perfect

<Steps>
  <Step title="Learn the Mechanics">
    Play games multiple times to understand the scoring system and controls
  </Step>

  <Step title="Join Early">
    Enter tournaments early to have more time for attempts
  </Step>

  <Step title="Focus on Strengths">
    Concentrate on games you're naturally good at
  </Step>

  <Step title="Consistent Improvement">
    Steady improvement often beats lucky high scores in the long run
  </Step>
</Steps>

## 🏆 Tournament Strategy

### Before Joining

<Card title="Review Tournament Details" icon="magnifying-glass">
  * Check entry fees and ensure you have enough tokens
  * Read the prize distribution method
  * Review time limits and plan your gaming sessions
  * Watch current leaderboard scores to gauge competition
</Card>

### During Competition

<Card title="Active Participation" icon="gamepad">
  * Monitor the leaderboard regularly
  * Don't wait until the last minute to play
  * Take breaks between games to maintain focus
  * Adjust strategy based on scores needed to place
</Card>

## 💡 Advanced Strategies

### Game Selection

Choose tournaments featuring games that match your skills:

* **Reaction-based games**: Good for players with quick reflexes
* **Strategy games**: Better for thoughtful, calculated players
* **Puzzle games**: Great for problem-solvers
* **Action games**: Perfect for competitive, high-energy players

### Risk Management

<AccordionGroup>
  <Accordion title="Low-Risk Strategy">
    Participate in free or low entry fee tournaments to build experience and tokens safely.
  </Accordion>

  <Accordion title="Medium-Risk Strategy">
    Mix free and paid tournaments, entering premium tournaments only for games you excel at.
  </Accordion>

  <Accordion title="High-Risk Strategy">
    Focus on high entry fee tournaments with large prize pools. Only recommended for experienced players.
  </Accordion>
</AccordionGroup>

### Time Management

<Card title="Optimize Your Gaming Time" icon="clock">
  * Join tournaments with longer durations for more flexibility
  * Practice during low-stakes tournaments
  * Save your best performances for high-stakes competitions
  * Don't overcommit to too many tournaments at once
</Card>

<Tip>
  The best players combine skill, strategy, and consistency. Focus on improving in all three areas!
</Tip>

*Keywords: tips, strategy, tournament strategy, winning tips, game tips, score optimization*

# Troubleshooting

Source: https://docs.drip.re/burn-ghosts-activity/troubleshooting

Solutions to common issues and how to get help

## ❓ Common Issues

### "Not enough balance" Error

<AccordionGroup>
  <Accordion title="Problem">
    You see an error message saying you don't have enough tokens for the entry fee.
  </Accordion>

  <Accordion title="Solution">
    * Participate in free tournaments first to earn tokens
    * Check your token balance before joining paid tournaments
    * Win tournaments to build up your token reserves
  </Accordion>
</AccordionGroup>

### Game Won't Load

<AccordionGroup>
  <Accordion title="Problem">
    The mini-game doesn't launch or shows a blank screen.
  </Accordion>

  <Accordion title="Solution">
    * Check your internet connection
    * Try refreshing the Discord activity
    * Make sure your browser allows pop-ups/new windows
    * Clear browser cache and try again
    * Try using a different browser
  </Accordion>
</AccordionGroup>

### Score Not Submitting

<AccordionGroup>
  <Accordion title="Problem">
    Your score doesn't appear on the leaderboard after playing.
  </Accordion>

  <Accordion title="Solution">
    * Complete the full game session without closing early
    * Don't close the game window before score submission
    * Check your internet connection during gameplay
    * Contact server admins if the issue persists
  </Accordion>
</AccordionGroup>

### Can't Join Tournament

<AccordionGroup>
  <Accordion title="Problem">
    Unable to join a tournament you want to participate in.
  </Accordion>

  <Accordion title="Solution">
    * Verify the tournament is still active (not ended or full)
    * Check if you meet any entry requirements
    * Confirm you have enough tokens for the entry fee
    * Try refreshing the page
  </Accordion>
</AccordionGroup>

## 🆘 Getting Help

### In-App Help

Use the **❓ Help** button in the sidebar to access:

* Quick reference guides
* Game instructions
* Contact information

### Server Support

<Card title="Contact Server Administrators" icon="user-headset">
  * Report technical issues to server admins
  * Ask questions in server support channels
  * Check server announcements for known issues
</Card>

### Discord Support

<Card title="DRIP Support Server" icon="discord">
  For issues with the activity integration or DRIP Rewards system, join the official DRIP Discord server.
</Card>

<Warning>
  If you experience repeated issues with score submission or token transactions, document the issue with screenshots and contact support immediately.
</Warning>

## 🔧 System Requirements

### Recommended Setup

* **Browser**: Latest version of Chrome, Firefox, or Edge
* **Internet**: Stable connection with at least 5 Mbps
* **Discord**: Desktop or web app (mobile may have limited functionality)
* **Pop-ups**: Enabled for game windows

<Tip>
  For the best experience, use Discord desktop app with a stable internet connection and latest browser.
</Tip>

*Keywords: troubleshooting, common issues, help, support, problems, errors, game issues*

# Changelog

Source: https://docs.drip.re/changelog

Product updates and announcements for DRIP platform

# Changelog

Stay up to date with the latest improvements, features, and updates to the DRIP platform.

<Update label="August 20, 2025" description="v2.2.0">
  ## User Authentication & OAuth Flow

  We're excited to introduce a secure OAuth-like authentication flow that enables apps to access user data with explicit consent.

### 🔐 New Authentication Features

* **OAuth Consent Flow**: Users can now securely authorize apps to access their DRIP profile data
* **Consent Page**: Beautiful authorization page at `app.drip.re/oauth/authorize` where users review and approve app permissions
* **Secure Authorization Codes**: Short-lived (5-minute) single-use codes for maximum security
* **Minimal Data Exposure**: Apps only receive the user's DRIP ID, protecting sensitive information

### 🚀 Developer Benefits

* **Works for All App Types**: Supports both single-realm and multi-realm applications
* **Simple Integration**: Standard OAuth 2.0-like flow that developers already know
* **Public Client Info API**: Apps can display their verification status and information transparently
* **Comprehensive Documentation**: Full implementation guides with examples in multiple languages

### 🔧 API Endpoints

* `GET /oauth/authorize` - User consent page (browser)
* `POST /api/v1/auth/oauth/token` - Exchange authorization code for user's DRIP ID
* `GET /api/v1/auth/oauth/client` - Fetch public app information

### 📚 Documentation

* New comprehensive guide at [User Authentication & OAuth](/developer/user-authentication)
* Code examples in JavaScript, Python, and TypeScript
* Complete server implementation examples
* Error handling and troubleshooting guides

  This update makes it easier than ever for developers to build secure, user-consented integrations with the DRIP platform while maintaining user privacy and control.
</Update>

<Update label="August 15, 2025" description="v2.1.0">
  ## Documentation Rework

  We've completely revamped our documentation to provide a better developer experience:

### ✨ New Features

* **Enhanced API Reference**: Restructured API documentation with clear separation between current and legacy APIs
* **Expanded Developer Guide**: Added comprehensive guides for authentication, core concepts, and app development
* **Interactive Navigation**: Implemented dropdown navigation for better content organization
* **Dark Mode Optimization**: Full black background theme for improved readability

### 🔧 Improvements

* **Better Search Experience**: Enhanced search functionality with contextual prompts
* **Mobile-Responsive Design**: Optimized documentation layout for all devices
* **Auto-Expanding Accordions**: API reference sections now automatically expand for easier navigation
* **RSS Feed Support**: Subscribe to changelog updates via RSS

### 📚 Additional Content

* **Migration Guidance**: Clear instructions for transitioning from legacy to current API
* **Code Examples**: More comprehensive examples across all endpoints
* **Developer Resources**: Enhanced reference materials for rate limits, errors, and best practices

  The new documentation structure makes it easier than ever to integrate with DRIP's powerful rewards and engagement platform.
</Update>

# AI Coding Assistants

Source: https://docs.drip.re/developer/ai-assistants

Use DRIP docs with AI tools (MCP, llms.txt, Markdown export) for faster development

Accelerate development by connecting your favorite AI coding assistants to the DRIP docs and API. This page shows the fastest, safest ways to give AI the right context.

<Warning>
  Never paste secrets into public chats. When AI tools ask for API keys, provide them securely via the tool’s secret manager or environment settings.
</Warning>

## Model Context Protocol (MCP)

The Model Context Protocol lets AI tools query and call APIs directly against the DRIP docs.

* Install the DRIP MCP server:

```bash theme={"dark"}
npx mint-mcp add driprewards
```

* Reference: [Model Context Protocol](https://mintlify.com/docs/ai/model-context-protocol)

### Use with Cursor

1. Run the install command above.
2. Open the command palette → “Open MCP settings” and confirm “driprewards” is listed.
3. In chat, ask: “What tools do you have available?” You should see the DRIP docs search tool and any exposed endpoints.

### Use with Claude

* From any docs page, use the contextual menu → “Open in Claude” to start a conversation with this page as context.
* Alternatively, add the DRIP docs MCP server using Claude’s Connectors flow if your workspace supports it.

## llms.txt and llms-full.txt

llms files help AI index your docs efficiently.

* **Mintlify guide**: [llms.txt](https://mintlify.com/docs/ai/llmstxt)
* DRIP docs expose:
  * `https://docs.drip.re/llms.txt` (site map for LLMs)
  * `https://docs.drip.re/llms-full.txt` (entire docs in one file)

How to use:

* Add one of the above URLs in your AI editor’s settings so it can index DRIP docs for context-aware answers.
* In tools that support it, reference docs explicitly in prompts (e.g., “Use DRIP docs for this task”).

## Markdown export

Get clean Markdown versions of any page for better AI ingestion.

* **Mintlify guide**: [Markdown export](https://mintlify.com/docs/ai/markdown-export)
* Add `.md` to any page URL on these docs (e.g., `https://docs.drip.re/developer/app-development.md`).
* Many tools have a shortcut to copy a page as Markdown (Command + C in Mintlify).

## Recommended workflows

* **Quick search + call generation**: Ask your AI to “Find the points balance update endpoint in DRIP, generate Node/TS code using fetch with retries.”
* **Fix missing scopes**: “Given this error, which scopes are required and how do I request reauthorization?”
* **Docs-first answer**: “Summarize app authorization flow from DRIP docs, then produce a checklist for publishing.”

<Info>
  If you expose API tools via MCP, the AI will prompt you for your DRIP API key at call time. The key is handled by the client tool, not stored in the docs system.
</Info>

# API Client Types

Source: https://docs.drip.re/developer/api-clients

Understanding Realm vs App clients and how to manage them

DRIP supports two distinct types of API clients, each designed for different use cases. Understanding the difference is crucial for choosing the right approach for your integration.

## Client Type Overview

<CardGroup>
  <Card title="Realm Clients" icon="castle">
    **Purpose**: Direct access to your own realm\
    **Scope**: Single realm only\
    **Authorization**: Automatic access to your realm\
    **Best for**: Internal tools, custom dashboards, automation
  </Card>

  <Card title="App Clients" icon="globe">
    **Purpose**: Multi-realm applications\
    **Scope**: Multiple realms with explicit authorization\
    **Authorization**: Publish + per-realm authorization\
    **Best for**: Third-party integrations, marketplace apps
  </Card>
</CardGroup>

## When to Use Each Type

### Use Realm Clients When

* Building tools for your own community only
* Creating internal dashboards or analytics
* Automating tasks within your realm
* Developing custom member management tools
* You need immediate access without approval processes

### Use App Clients When

* Building apps for multiple communities
* Creating marketplace applications
* Developing SaaS tools for DRIP communities
* Building integrations that other realms can install
* You want to distribute your app publicly

## Creating API Clients

### Creating a Realm Client

<Steps>
  <Step title="Access Developer Portal">
    Navigate to **Admin** → **Developer** in your DRIP dashboard
  </Step>

  <Step title="Go to Project API">
    Click the **Project API** tab
  </Step>

  <Step title="Create Client">
    Click **Create API Client** and configure:

    * **Name**: Descriptive name for your integration
    * **Scopes**: Select the permissions you need
  </Step>

  <Step title="Save Credentials">
    Copy and securely store your **Client Secret** (this is your API key)
  </Step>
</Steps>

### Creating an App Client

<Steps>
  <Step title="Access Developer Portal">
    Navigate to **Admin** → **Developer** in your DRIP dashboard
  </Step>

  <Step title="Go to DRIP Apps">
    Click the **DRIP Apps** tab
  </Step>

  <Step title="Set up New App">
    In the **Listing** section, you can set up your app metadata (name, description, logo)
  </Step>

  <Step title="Get App Client">
    In the **App Client** section, you can set up your app client credentials
  </Step>

  <Step title="Submit App">
    Once your app is ready, you can publish it to the DRIP Apps marketplace
  </Step>

  <Step title="Wait for Approval">
    DRIP reviews your app for security and compliance
  </Step>
</Steps>

## Scope Management

### Understanding Scopes

Scopes define what your client can access and modify.

<Info>
  For apps: you select the scopes your app needs. Realms/projects grant those scopes when they authorize your app. If you later change your app’s requested scopes, realms must reauthorize for the new scopes to take effect.
</Info>

#### Basic Scopes

```javascript theme={"dark"}
const basicScopes = [
  'realm:read',           // Read realm information
  'members:read',         // Read member profiles
  'quests:read',          // Read quest data
  'store:read',           // Read store items
];
```

#### Advanced Scopes

```javascript theme={"dark"}
const advancedScopes = [
  'members:write',        // Modify member data
  'points:write',         // Award/deduct points
  'quests:write',         // Create/modify quests
  'store:write',          // Manage store items
];
```

### Scope Selection Best Practices

<AccordionGroup>
  <Accordion title="Principle of Least Privilege">
    Only request scopes you actually need. This improves security and increases approval chances.

    ```javascript theme={"dark"}
    // ❌ Bad: Requesting unnecessary scopes
    const badScopes = ['realm:read', 'members:read', 'members:write', 'admin:read'];

    // ✅ Good: Only what you need
    const goodScopes = ['realm:read', 'members:read']; // For read-only analytics
    ```
  </Accordion>

  <Accordion title="Start Small, Expand Later">
    Begin with basic scopes and add more as your app grows.

    ```javascript theme={"dark"}
    // Phase 1: Read-only analytics
    const phase1Scopes = ['realm:read', 'members:read'];

    // Phase 2: Add point management
    const phase2Scopes = [...phase1Scopes, 'points:write'];

    // Phase 3: Add quest creation
    const phase3Scopes = [...phase2Scopes, 'quests:write'];
    ```
  </Accordion>
</AccordionGroup>

## Authorization Flows

### Realm Client Flow

```mermaid theme={"dark"}
sequenceDiagram
    participant Dev as Developer
    participant Portal as DRIP Portal
    participant API as DRIP API
    participant Realm as Your Realm
    
    Dev->>Portal: Create Realm Client
    Portal->>Dev: API Key Generated
    Dev->>API: Request with API Key
    API->>Realm: Access Your Realm Data
    Realm->>API: Return Data
    API->>Dev: Response
```

**Characteristics:**

* ✅ Immediate access
* ✅ No approval delays
* ✅ Full permissions within your realm
* ❌ Limited to single realm
* ❌ Can't be distributed to other realms

### App Client Flow

```mermaid theme={"dark"}
sequenceDiagram
    participant Dev as Developer
    participant Platform as DRIP Platform
    participant RealmAdmin as Realm Admin
    participant API as DRIP API
    participant Realm as Target Realm
    
    Dev->>Platform: Submit App
    Platform->>Platform: Review & Approve
    Platform->>Dev: App Client Credentials
    RealmAdmin->>Platform: Authorize App
    Platform->>RealmAdmin: Grant Access
    Dev->>API: Request with App Client
    API->>Realm: Access Authorized Data
    Realm->>API: Return Data
    API->>Dev: Response
```

**Characteristics:**

* ✅ Multi-realm capability
* ✅ Can be distributed publicly
* ✅ Scalable business model
* ❌ Requires platform approval
* ❌ Each realm must authorize separately
* ❌ Limited to approved scopes only

## Managing Multiple Clients

### Client Organization

```javascript theme={"dark"}
class DripClientManager {
  constructor() {
    this.clients = new Map();
  }

  // Add a realm client
  addRealmClient(name, apiKey, realmId) {
    this.clients.set(name, {
      type: 'realm',
      client: new DripClient(apiKey, realmId),
      realmId
    });
  }

  // Add an app client
  addAppClient(name, appClientSecret) {
    this.clients.set(name, {
      type: 'app',
      client: new DripAppClient(appClientSecret),
      authorizedRealms: []
    });
  }

  // Get client by name
  getClient(name) {
    return this.clients.get(name);
  }

  // List all clients
  listClients() {
    return Array.from(this.clients.entries()).map(([name, config]) => ({
      name,
      type: config.type,
      realmId: config.realmId || 'multiple'
    }));
  }
}

// Usage
const manager = new DripClientManager();
manager.addRealmClient('analytics', 'realm_api_key', 'realm_id');
manager.addAppClient('marketplace-app', 'app_client_secret');
```

### Environment-Based Configuration

```javascript theme={"dark"}
// config/clients.js
const clients = {
  development: {
    realm: {
      apiKey: process.env.DEV_REALM_API_KEY,
      realmId: process.env.DEV_REALM_ID
    },
    app: {
      clientSecret: process.env.DEV_APP_CLIENT_SECRET
    }
  },
  production: {
    realm: {
      apiKey: process.env.PROD_REALM_API_KEY,
      realmId: process.env.PROD_REALM_ID
    },
    app: {
      clientSecret: process.env.PROD_APP_CLIENT_SECRET
    }
  }
};

const env = process.env.NODE_ENV || 'development';
export const realmClient = new DripClient(
  clients[env].realm.apiKey,
  clients[env].realm.realmId
);
export const appClient = new DripAppClient(
  clients[env].app.clientSecret
);
```

## Security Best Practices

### API Key Management

<CardGroup>
  <Card title="Secure Storage" icon="vault">
    * Store keys in environment variables
    * Use secure key management services
    * Never commit keys to version control
    * Rotate keys regularly
  </Card>

  <Card title="Access Control" icon="lock">
    * Use least-privilege scopes
    * Monitor API key usage
    * Set up usage alerts
    * Revoke unused keys immediately
  </Card>
</CardGroup>

### Code Examples

```javascript theme={"dark"}
// ✅ Good: Environment variables
const client = new DripClient(
  process.env.DRIP_API_KEY,
  process.env.DRIP_REALM_ID
);

// ❌ Bad: Hardcoded keys
const client = new DripClient(
  'drip_1234567890abcdef',
  '507f1f77bcf86cd799439011'
);

// ✅ Good: Key rotation support
class SecureDripClient extends DripClient {
  async rotateKey(newApiKey) {
    // Test new key first
    const testClient = new DripClient(newApiKey, this.realmId);
    await testClient.request('GET', `/realms/${this.realmId}`);
    
    // If successful, update
    this.apiKey = newApiKey;
    console.log('API key rotated successfully');
  }
}
```

## Monitoring and Analytics

### Usage Tracking

```javascript theme={"dark"}
class MonitoredDripClient extends DripClient {
  constructor(apiKey, realmId) {
    super(apiKey, realmId);
    this.stats = {
      requests: 0,
      errors: 0,
      lastUsed: null
    };
  }

  async request(method, endpoint, data) {
    this.stats.requests++;
    this.stats.lastUsed = new Date();
    
    try {
      const result = await super.request(method, endpoint, data);
      return result;
    } catch (error) {
      this.stats.errors++;
      throw error;
    }
  }

  getStats() {
    return {
      ...this.stats,
      errorRate: this.stats.errors / this.stats.requests,
      isActive: Date.now() - this.stats.lastUsed < 300000 // 5 minutes
    };
  }
}
```

## Migration Strategies

### From Realm to App Client

If you started with a realm client and want to expand to multiple realms:

<Steps>
  <Step title="Create App">
    Submit your app through the DRIP Apps portal
  </Step>

  <Step title="Parallel Development">
    Develop app client integration alongside existing realm client
  </Step>

  <Step title="Testing">
    Test app client with your own realm first
  </Step>

  <Step title="Gradual Migration">
    Migrate features one by one from realm client to app client
  </Step>

  <Step title="Deprecation">
    Once fully migrated, deprecate the realm client
  </Step>
</Steps>

### Code Migration Example

```javascript theme={"dark"}
// Before: Realm client
class RealmIntegration {
  constructor(apiKey, realmId) {
    this.client = new DripClient(apiKey, realmId);
  }

  async getLeaderboard() {
    return this.client.getLeaderboard();
  }
}

// After: App client supporting multiple realms
class AppIntegration {
  constructor(appClientSecret) {
    this.client = new DripAppClient(appClientSecret);
    this.authorizedRealms = new Map();
  }

  async getLeaderboard(realmId) {
    if (!this.authorizedRealms.has(realmId)) {
      throw new Error('Not authorized for this realm');
    }
    return this.client.getLeaderboard(realmId);
  }

  async loadAuthorizedRealms() {
    const realms = await this.client.getAuthorizedRealms();
    realms.forEach(realm => {
      this.authorizedRealms.set(realm.realmId, realm);
    });
  }
}
```

## Next Steps

<CardGroup>
  <Card title="Build Your First App" icon="rocket" href="/developer/first-app">
    Create a simple application using your API client
  </Card>

  <Card title="Multi-Realm Apps" icon="globe" href="/developer/multi-realm-apps">
    Learn to build apps that work across multiple communities
  </Card>

  <Card title="Authentication Guide" icon="key" href="/developer/authentication">
    Deep dive into authentication and security
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference">
    Complete documentation of all available endpoints
  </Card>
</CardGroup>

# App Development

Source: https://docs.drip.re/developer/app-development

Build apps and integrations for your own realm. Compare client types and get started quickly with a Realm API Client. For multi-realm app keys and scopes, see Multi-Realm Apps.

Learn how to build applications and integrations on DRIP for your own realm. This guide covers the general development flow for Realm Clients and links out to multi-realm app development when you need it.

## Overview

DRIP supports two types of integrations:

### Realm Clients (Direct Integration)

* **Purpose**: Direct access to your own realm's data
* **Scope**: Single realm only
* **Use case**: Custom dashboards, internal tools, automation scripts
* **Authorization**: Scoped to your realm automatically

### App Clients (Multi-Realm Apps)

* **Purpose**: Build applications that can be used by multiple communities
* **Scope**: Can access multiple realms with their permission
* **Use case**: Third-party integrations, marketplace apps, SaaS tools
* **Authorization**: Each realm must explicitly authorize your app

<Info>
  This guide focuses on **Realm Clients** for single-realm development. For app keys, cross-realm authorization, and scopes, see [Multi-Realm Apps](/developer/multi-realm-apps).
</Info>

## Using a Realm API Client

For most internal tools and single-realm integrations, use a Realm API Client. It has immediate access to your own realm and is the fastest way to build.

<Steps>
  <Step title="Create a Realm Client">
    Go to **Admin** > **Developer** > **Project API** and create an API client. Select only the scopes you need (e.g., `realm:read`, `members:read`).
  </Step>

  <Step title="Find Your Realm (Project) ID">
    When a project is selected in the dashboard, the Realm/Project ID appears in the header.
  </Step>

  <Step title="Make Your First Call">
    Use your API key (Client Secret) to call the API for your realm.
  </Step>
</Steps>

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  const API_BASE = 'https://api.drip.re/api/v1';
  const API_KEY = process.env.DRIP_API_KEY; // Store securely
  const REALM_ID = process.env.DRIP_REALM_ID;

  async function getMembers() {
    const res = await fetch(`${API_BASE}/realm/${REALM_ID}/members/search?type=drip-id&values=all`, {
      headers: {
        Authorization: `Bearer ${API_KEY}`,
        'Content-Type': 'application/json'
      }
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    return data.data;
  }

  ```

  ```python Python theme={"dark"}
  import os, requests
  API_BASE = 'https://api.drip.re/api/v1'
  API_KEY = os.environ['DRIP_API_KEY']
  REALM_ID = os.environ['DRIP_REALM_ID']

  def get_members():
      url = f"{API_BASE}/realm/{REALM_ID}/members/search?type=drip-id&values=all"
      r = requests.get(url, headers={
          'Authorization': f'Bearer {API_KEY}',
          'Content-Type': 'application/json'
      })
      r.raise_for_status()
      return r.json()['data']
  ```

</CodeGroup>

<Warning>
  Never expose your API key in client-side code. Use server-side calls or a secure proxy; store keys in environment variables.
</Warning>

<Info>
  Building a multi-realm app instead? See the full guide: [Multi-Realm Apps](/developer/multi-realm-apps).
</Info>

## API Client Types Explained

### Realm Client Workflow

```mermaid theme={"dark"}
sequenceDiagram
    participant Dev as Developer
    participant Dashboard as DRIP Dashboard
    participant API as DRIP API
    participant Realm as Your Realm
    
    Dev->>Dashboard: Create Realm Client
    Dashboard->>Dev: API Key Generated
    Dev->>API: Request with API Key
    API->>Realm: Access Your Realm Data
    Realm->>API: Return Data
    API->>Dev: Response
```

**Characteristics:**

* Immediate access to your realm
* No approval process needed
* Scoped to single realm
* Full permissions within your realm

### App Clients (overview)

Use App Clients to build multi-realm applications that can be authorized by multiple communities (realms). Key differences vs. Realm Clients:

* Authorization: publish your app, then each realm grants authorization
* Credentials: use an app client secret (not a realm API key)
* Scopes: your app selects `requestedScopes`; scopes are granted per realm

For app creation, cross-realm authorization, and scopes, see [Multi-Realm Apps](/developer/multi-realm-apps).

## App Clients

See [Multi-Realm Apps](/developer/multi-realm-apps) for app creation, scopes, and authorization flow.

## Development Best Practices

### 1. Scope Minimization

Only request scopes you actually need:

```javascript theme={"dark"}
// ❌ Bad: Requesting unnecessary scopes
const badScopes = [
  'realm:read',
  'members:read',
  'members:write',  // Not needed for read-only analytics
  'points:write',   // Not needed for analytics
  'admin:read',     // Overly broad
  'webhooks:write'  // Not needed
];

// ✅ Good: Minimal necessary scopes
const goodScopes = [
  'realm:read',     // Need realm info
  'members:read'    // Need member data for analytics
];
```

## Next Steps

<CardGroup>
  <Card title="Multi-Realm Apps" icon="globe" href="/developer/multi-realm-apps">
    Building for multiple realms? Learn app creation, scopes, and authorization
  </Card>

  <Card title="Examples" icon="code" href="/developer/examples">
    Copy-paste snippets for common tasks
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference">
    Complete API documentation
  </Card>

  <Card title="Support Community" icon="discord" href="https://discord.gg/dripchain">
    Get help from other developers
  </Card>
</CardGroup>

# App Store Submission

Source: https://docs.drip.re/developer/app-store

Get your app published in the DRIP App Store 🏪

Learn how to submit your application to the DRIP App Store, navigate the review process, and successfully distribute your app to the DRIP ecosystem.

## Overview

The DRIP App Store is the official marketplace where realm administrators can discover, install, and manage applications for their communities. Getting your app published opens up your integration to thousands of DRIP communities.

<Info>
  Draft apps can create API clients and work only in your own realm. To enable other realms to authorize and use your app, you must publish it. App Store listing follows manual verification via email to [dev@drip.re](mailto:dev@drip.re).
</Info>

### Temporary Submission Process (Manual)

* Until the submission portal is live, email [dev@drip.re](mailto:dev@drip.re) to request App Store listing.
* Publishing your app enables cross-realm authorization immediately; store listing follows manual verification.

#### What to include in your email

* App name and App ID
* Website and contact email
* Short description (1-2 sentences)
* Scopes requested (list)
* Why each scope is needed (1-2 bullets per scope)
* Data handling summary (what you store/process)
* Screenshots/logo links
* Testing instructions or install link
* Expected usage/rate-limit profile (if relevant)

#### Email template

```text theme={"dark"}
To: dev@drip.re
Subject: DRIP App Store Listing Request - <Your App Name>

App name: <Your App Name>
App ID: <app_id>
Website: <https://...>
Contact email: <you@company.com>

Short description:
<one or two sentences>

Requested scopes:
- scope.one — why needed
- scope.two — why needed

Data handling summary:
<what data you store/process and where>

Screenshots/logo:
<links>

Testing/install:
<link or instructions>

Expected usage:
<notes on expected traffic if any>
```

<Info>
  All scopes are granted per realm at authorization; there are no public scopes available across realms. At this time, there is no separate platform scope approval.
</Info>

## Submission Requirements

### Technical Requirements

<CardGroup>
  <Card title="Functionality" icon="gear">
    * App must work as described
    * Proper error handling implemented
    * No critical bugs or crashes
    * Respects rate limits and API guidelines
  </Card>

  <Card title="Security" icon="shield">
    * Secure API key management
    * No unauthorized data collection
    * Proper scope usage
    * Data privacy compliance
  </Card>

  <Card title="Performance" icon="clock">
    * Reasonable response times
    * Efficient API usage
    * Proper caching implementation
    * Handles high load gracefully
  </Card>

  <Card title="Integration" icon="puzzle-piece">
    * Clean integration with DRIP
    * Follows DRIP design patterns
    * Proper webhook handling
    * Multi-realm support (if applicable)
  </Card>
</CardGroup>

### Content Requirements

Your app submission must include:

#### App Metadata

```json theme={"dark"}
{
  "name": "Your App Name",
  "tagline": "Brief one-line description",
  "description": "Detailed description of what your app does",
  "category": "productivity", // analytics, gaming, productivity, social, utility
  "version": "1.0.0",
  "website": "https://yourapp.com",
  "supportUrl": "https://yourapp.com/support",
  "privacyPolicy": "https://yourapp.com/privacy",
  "termsOfService": "https://yourapp.com/terms"
}
```

#### Visual Assets

* **App Icon**: 512x512 PNG, clean and professional
* **Screenshots**: 3-5 high-quality screenshots showing key features
* **Banner Image**: 1200x630 for store listings (optional)

#### Documentation

* **Setup Instructions**: Clear installation and configuration steps
* **User Guide**: How to use your app's features
* **API Documentation**: If your app exposes APIs
* **Changelog**: Version history and updates

### Scope Justification

Clearly explain why your app needs each requested scope:

<Tabs>
  <Tab title="Good Example">
    ```json theme={"dark"}
    {
      "requestedScopes": ["realm:read", "members:read", "points:write"],
      "scopeJustification": {
        "realm:read": "Display realm name and branding in analytics dashboard",
        "members:read": "Generate engagement analytics and member insights",
        "points:write": "Award points for completing external challenges and tasks"
      },
      "dataUsage": "Member data is used only for analytics generation and is not stored permanently or shared with third parties"
    }
    ```
  </Tab>

  <Tab title="Bad Example">
    ```json theme={"dark"}
    {
      "requestedScopes": ["realm:read", "members:read", "members:write", "admin:read"],
      "scopeJustification": {
        "realm:read": "Need realm info",
        "members:read": "For analytics",
        "members:write": "Might need this later",
        "admin:read": "Just in case"
      }
    }
    ```
  </Tab>
</Tabs>

## Submission Process

### Step 1: Prepare Your Submission

<Steps>
  <Step title="Complete Your App">
    Ensure your app is fully functional and tested across multiple realms
  </Step>

  <Step title="Gather Assets">
    Prepare all required visual assets and documentation
  </Step>

  <Step title="Test Thoroughly">
    Test your app with different realm configurations and permission sets
  </Step>

  <Step title="Review Guidelines">
    Double-check that your app meets all technical and content requirements
  </Step>
</Steps>

### Step 2: Submit Through Developer Portal

1. **Access Developer Portal**
   * Navigate to **Admin** → **Developer** in your DRIP dashboard
   * Go to the **DRIP Apps** tab

2. **Create New Submission**
   * Click **Submit New App**
   * Fill out the app information form
   * Upload your visual assets

3. **Configure Scopes**
   * Select required scopes
   * Provide detailed justification for each scope
   * Explain your data usage policies

4. **Submit for Review**
   * Review all information for accuracy
   * Submit your app for platform review

### Step 3: Review Process

```mermaid theme={"dark"}
graph TB
    A[App Submitted] --> B[Automated Checks]
    B --> C{Pass Basic Tests?}
    C -->|No| D[Rejection with Feedback]
    C -->|Yes| E[Manual Security Review]
    E --> F{Security Approved?}
    F -->|No| G[Security Feedback]
    F -->|Yes| H[Functionality Testing]
    H --> I{Functionality OK?}
    I -->|No| J[Functionality Feedback]
    I -->|Yes| K[Final Approval]
    
    D --> L[Fix Issues & Resubmit]
    G --> L
    J --> L
    L --> A
    
    K --> M[Published to Store]
```

#### Review Timeline

* **Automated Checks**: 5-10 minutes
* **Security Review**: 2-3 business days
* **Functionality Testing**: 3-5 business days
* **Total Time**: Usually 5-8 business days

## Review Criteria

### Automated Checks

Your app will be automatically tested for:

<AccordionGroup>
  <Accordion title="Technical Validation">
    * Valid app metadata format
    * Required fields completed
    * Image assets meet specifications
    * Links are accessible and valid
    * Privacy policy and terms exist
  </Accordion>

  <Accordion title="Basic Functionality">
    * App responds to basic API calls
    * Authentication works correctly
    * No immediate crashes or errors
    * Handles missing permissions gracefully
  </Accordion>
</AccordionGroup>

### Manual Review

Human reviewers will evaluate:

<AccordionGroup>
  <Accordion title="Security Assessment">
    * Scope usage is appropriate and justified
    * No unauthorized data collection
    * Secure handling of API keys and tokens
    * Proper data encryption and storage
    * Compliance with privacy regulations
  </Accordion>

  <Accordion title="User Experience">
    * App works as described
    * Clear and intuitive interface
    * Proper error handling and feedback
    * Good performance under normal load
    * Professional presentation
  </Accordion>

  <Accordion title="Content Review">
    * App description is accurate
    * Screenshots represent actual functionality
    * No misleading claims or features
    * Appropriate for all audiences
    * Follows DRIP brand guidelines
  </Accordion>
</AccordionGroup>

## Common Rejection Reasons

### Technical Issues

<CardGroup>
  <Card title="Scope Overreach" icon="exclamation-triangle">
    **Problem**: Requesting more permissions than needed

    **Solution**: Only request scopes your app actually uses and provide clear justification
  </Card>

  <Card title="Poor Error Handling" icon="bug">
    **Problem**: App crashes or shows unclear errors

    **Solution**: Implement comprehensive error handling with user-friendly messages
  </Card>

  <Card title="Security Concerns" icon="shield-exclamation">
    **Problem**: Insecure data handling or API key exposure

    **Solution**: Follow security best practices and never expose sensitive data
  </Card>

  <Card title="Performance Issues" icon="clock">
    **Problem**: Slow response times or excessive API usage

    **Solution**: Optimize performance and implement proper caching
  </Card>
</CardGroup>

### Content Issues

<CardGroup>
  <Card title="Misleading Description" icon="file-x">
    **Problem**: App functionality doesn't match description

    **Solution**: Ensure description accurately reflects your app's features
  </Card>

  <Card title="Poor Quality Assets" icon="image">
    **Problem**: Low-quality screenshots or unprofessional icon

    **Solution**: Create high-quality, professional visual assets
  </Card>

  <Card title="Missing Documentation" icon="book-x">
    **Problem**: Insufficient setup or usage instructions

    **Solution**: Provide comprehensive documentation and support resources
  </Card>

  <Card title="Policy Violations" icon="gavel">
    **Problem**: Violates DRIP's app store policies

    **Solution**: Review and comply with all platform policies
  </Card>
</CardGroup>

## After Approval

### App Store Listing

Once approved, your app will appear in the DRIP App Store with:

* **App tile** with your icon and basic info
* **Detailed page** with screenshots and full description
* **Installation button** for realm administrators
* **Ratings and reviews** from users
* **Support links** and contact information

### Managing Your App

<Tabs>
  <Tab title="Updates">
    ```javascript theme={"dark"}
    // Submitting app updates
    const updateData = {
      version: "1.1.0",
      changelog: [
        "Added new analytics dashboard",
        "Fixed member search bug",
        "Improved performance"
      ],
      newFeatures: ["Advanced filtering", "Export functionality"],
      bugFixes: ["Fixed memory leak", "Resolved auth issues"]
    };
    ```

    **Update Process:**

    1. Submit update through developer portal
    2. Automated testing of new version
    3. Review of changes (faster for minor updates)
    4. Deployment to app store
  </Tab>

  <Tab title="Analytics">
    Track your app's performance:

    * **Installation metrics**: How many realms have installed your app
    * **Usage statistics**: API call volume and patterns
    * **User feedback**: Ratings, reviews, and support requests
    * **Revenue tracking**: If your app has paid features
  </Tab>

  <Tab title="Support">
    Provide ongoing support:

    * **Monitor reviews**: Respond to user feedback promptly
    * **Handle support requests**: Provide timely assistance
    * **Release updates**: Fix bugs and add new features
    * **Maintain documentation**: Keep guides current
  </Tab>
</Tabs>

## Marketing Your App

### App Store Optimization

<AccordionGroup>
  <Accordion title="Compelling Description">
    Write a description that clearly explains your app's value:

    ```markdown theme={"dark"}
    # Good Example
    **Community Analytics Pro** gives realm administrators deep insights into member engagement, activity patterns, and growth trends. 

    Key Features:
    - Real-time engagement dashboards
    - Member activity heatmaps  
    - Custom report generation
    - Automated insights and recommendations

    Perfect for community managers who want to understand and grow their communities with data-driven decisions.
    ```
  </Accordion>

  <Accordion title="High-Quality Screenshots">
    Show your app in action:

    * Use actual data (anonymized)
    * Highlight key features
    * Show different use cases
    * Include mobile views if applicable
  </Accordion>

  <Accordion title="Keywords and Categories">
    Choose the right category and keywords:

    * **Analytics**: Data, insights, reporting, metrics
    * **Productivity**: Automation, management, efficiency
    * **Gaming**: Leaderboards, competitions, rewards
    * **Social**: Community, engagement, interaction
  </Accordion>
</AccordionGroup>

### Promoting Your App

<CardGroup>
  <Card title="Community Engagement" icon="users">
    * Share in DRIP Discord community
    * Write blog posts about your app
    * Create tutorial videos
    * Engage with potential users
  </Card>

  <Card title="Content Marketing" icon="megaphone">
    * Case studies from early users
    * Feature comparisons
    * Integration tutorials
    * Best practices guides
  </Card>

  <Card title="Partnerships" icon="handshake">
    * Partner with popular realms
    * Collaborate with other developers
    * Sponsor community events
    * Offer exclusive features
  </Card>

  <Card title="Social Proof" icon="star">
    * Collect user testimonials
    * Showcase success stories
    * Display usage statistics
    * Highlight positive reviews
  </Card>
</CardGroup>

## Monetization Strategies

### Pricing Models

<Tabs>
  <Tab title="Freemium">
    ```javascript theme={"dark"}
    const pricingTiers = {
      free: {
        price: 0,
        features: ['Basic analytics', 'Up to 100 members', 'Standard support'],
        limitations: ['Limited data retention', 'Basic reporting only']
      },
      pro: {
        price: 9.99,
        features: ['Advanced analytics', 'Unlimited members', 'Custom reports', 'Priority support'],
        limitations: []
      }
    };
    ```
  </Tab>

  <Tab title="Per-Realm">
    ```javascript theme={"dark"}
    const perRealmPricing = {
      basePrice: 4.99, // Per realm per month
      discounts: {
        multiRealm: 0.15, // 15% off for 3+ realms
        annual: 0.20      // 20% off for annual billing
      }
    };
    ```
  </Tab>

  <Tab title="Usage-Based">
    ```javascript theme={"dark"}
    const usagePricing = {
      freeQuota: 1000, // Free API calls per month
      overageRate: 0.01, // $0.01 per additional call
      memberTiers: {
        small: { max: 500, price: 5.99 },
        medium: { max: 2000, price: 19.99 },
        large: { max: 10000, price: 49.99 }
      }
    };
    ```
  </Tab>
</Tabs>

## App Store Policies

### Prohibited Content

Apps cannot:

* Collect unnecessary personal data
* Spam users or communities
* Violate intellectual property rights
* Contain malicious code or security vulnerabilities
* Mislead users about functionality
* Compete directly with core DRIP features

### Content Guidelines

Apps must:

* Provide clear value to communities
* Respect user privacy and data
* Follow accessibility best practices
* Use appropriate and professional language
* Comply with applicable laws and regulations

### Technical Policies

Apps must:

* Use APIs as intended and documented
* Respect rate limits and quotas
* Handle errors gracefully
* Provide adequate user support
* Maintain reasonable uptime and performance

## Support and Resources

<CardGroup>
  <Card title="Developer Support" icon="headphones">
    Get help with your submission:

    * Email: [dev@drip.re](mailto:dev@drip.re)
    * Discord: #app-developers channel
    * Office hours: Fridays 2-4 PM PST
  </Card>

  <Card title="Documentation" icon="book">
    Additional resources:

    * App Store Guidelines (full document)
    * Technical Requirements Checklist
    * Design Guidelines
    * Marketing Best Practices
  </Card>

  <Card title="Community" icon="users">
    Connect with other developers:

    * Developer Discord community
    * Monthly developer meetups
    * App showcase events
    * Beta testing programs
  </Card>

  <Card title="Tools" icon="wrench">
    Development tools:

    * App submission checklist
    * Testing frameworks
    * Analytics SDKs
    * Design templates
  </Card>
</CardGroup>

## App Installation & Configuration

Once your app is approved and published, you need to properly configure it for realm installations.

### 1. Prepare Your App

Before inviting realms to authorize your app, make sure your app is properly configured:

<Steps>
  <Step title="Fill in Required Information">
    * Go to the **Overview** tab in the app configuration
    * Provide key details such as **App Name**, **Description**, **Website URL**, **Support URL**, etc.
    * Upload logos or graphics as needed
  </Step>

  <Step title="Create an App Client & Specify Scopes">
    * Navigate to the **Client Settings** (or **App Client** section, depending on your UI)
    * Generate or retrieve your client credentials
    * Specify the appropriate **scopes** you need for your app to function correctly
    * Save your changes
  </Step>
</Steps>

### 2. Publish Your App

When you're ready for others to use your app:

<Steps>
  <Step title="Go to the Overview Page">
    * In the app settings, open the **Overview** tab again
    * Review all of your app details to ensure accuracy
  </Step>

  <Step title="Publish the App">
    * Click the **Publish** button (or "Make Public") to make your app available
    * Confirm any prompts to finalize the publishing process
  </Step>
</Steps>

<Info>
  **Note:** Publishing means that realms (communities) can now add and authorize your app.
</Info>

### 3. Invite Realms

After your app is published, you can share an **Invite Link** with realms who want to install or authorize the app.

<Steps>
  <Step title="Locate the Invite (Install) Link">
    * Go to the **Help & Resources** page (or "Help" tab)
    * Look for the **Installation** or **Invite** link builder
  </Step>

  <Step title="Customize (Optional)">
    * You can add query parameters such as `platformType` or `platformId` to keep track of your integrations
    * You will be able to search authorized realms by these parameters using the API
    * Copy the link when you're done
  </Step>

  <Step title="Share the Link">
    * Send it to any realm or community you wish to onboard
    * When they visit the link, they'll be prompted to grant permission for your app
  </Step>
</Steps>

### 4. Manage Future Updates

<AccordionGroup>
  <Accordion title="Updating App Information">
    If you need to revise your app's description, images, or settings:

    * Return to the **Overview** tab
    * Make your changes and save
  </Accordion>

  <Accordion title="Managing Scopes">
    If you need additional scopes or wish to remove some:

    * Revisit the **Client Settings**
    * Realms may need to re-authorize your app to grant newly requested scopes
    * This can be done by clicking the "Re-authorize" button in the app settings of their realm
  </Accordion>

  <Accordion title="Unpublishing">
    If you need to temporarily hide your app from new realms:

    * Use the **Unpublish** feature in the app settings
  </Accordion>
</AccordionGroup>

## Next Steps

<Steps>
  <Step title="Prepare Your App">
    Ensure your app meets all requirements and is thoroughly tested
  </Step>

  <Step title="Gather Materials">
    Create all required documentation, screenshots, and assets
  </Step>

  <Step title="Submit for Review">
    Submit through the developer portal and wait for review feedback
  </Step>

  <Step title="Launch and Promote">
    Once approved, actively promote your app to the DRIP community
  </Step>
</Steps>

<Info>
  **Ready to submit?** Make sure to review our [Best Practices](/developer/best-practices) guide and test your app thoroughly before submission. Good luck! 🚀
</Info>

# Authentication Guide

Source: https://docs.drip.re/developer/authentication

Complete guide to authenticating with the DRIP API

This guide covers everything you need to know about authenticating with the DRIP API, managing API keys, and handling authentication in your applications.

## Overview

The DRIP API uses **Bearer token authentication** with API keys. Every request must include a valid API key in the `Authorization` header.

## Managing API Keys

### Creating API Keys

<Steps>
  <Step title="Access Developer Portal">
    Navigate to your DRIP dashboard and go to **Admin** > **Developer**
  </Step>

  <Step title="Create API Client">
    Go to the **Project API** tab and click **Create API Client**. Choose appropriate scopes and provide a descriptive name
  </Step>

  <Step title="Copy and Store">
    Copy the API key immediately - you won't be able to see it again
  </Step>

  <Step title="Test the Key">
    Make a test API call to verify the key works correctly
  </Step>
</Steps>

## Implementation Examples

### Environment Variables

Store your API keys securely using environment variables:

<Info>
  **Finding your Realm (Project) ID:** It's displayed in the dashboard header when you select your project.
</Info>

<CodeGroup>
  ```bash .env theme={"dark"}
  DRIP_API_KEY=your_api_key_here
  DRIP_REALM_ID=your_realm_id_here
  DRIP_BASE_URL=https://api.drip.re/api/v1
  ```

  ```javascript JavaScript theme={"dark"}
  // Load from environment
  const DRIP_API_KEY = process.env.DRIP_API_KEY;
  const DRIP_REALM_ID = process.env.DRIP_REALM_ID;

  // Create headers
  const headers = {
    'Authorization': `Bearer ${DRIP_API_KEY}`,
    'Content-Type': 'application/json'
  };
  ```

  ```python Python theme={"dark"}
  import os

  # Load from environment
  DRIP_API_KEY = os.getenv('DRIP_API_KEY')
  DRIP_REALM_ID = os.getenv('DRIP_REALM_ID')

  # Create headers
  headers = {
      'Authorization': f'Bearer {DRIP_API_KEY}',
      'Content-Type': 'application/json'
  }
  ```

</CodeGroup>

### API Client Class

Create a reusable client class for your applications:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  class DripClient {
    constructor(apiKey, realmId) {
      this.apiKey = apiKey;
      this.realmId = realmId;
      this.baseUrl = 'https://api.drip.re/api/v1';
    }

    async request(method, endpoint, data = null) {
      const url = `${this.baseUrl}${endpoint}`;
      const options = {
        method,
        headers: {
          'Authorization': `Bearer ${this.apiKey}`,
          'Content-Type': 'application/json'
        }
      };

      if (data) {
        options.body = JSON.stringify(data);
      }

      const response = await fetch(url, options);
      
      if (!response.ok) {
        throw new Error(`API Error: ${response.status} ${response.statusText}`);
      }

      return response.json();
    }

    // Helper methods
    async getRealm() {
      return this.request('GET', `/realms/${this.realmId}`);
    }

    async searchMembers(type, values) {
      return this.request('GET', `/realm/${this.realmId}/members/search?type=${type}&values=${values}`);
    }
  }

  // Usage
  const client = new DripClient(process.env.DRIP_API_KEY, process.env.DRIP_REALM_ID);

  ```

  ```python Python theme={"dark"}
  import requests
  import json

  class DripClient:
      def __init__(self, api_key, realm_id):
          self.api_key = api_key
          self.realm_id = realm_id
          self.base_url = 'https://api.drip.re/api/v1'
          self.headers = {
              'Authorization': f'Bearer {api_key}',
              'Content-Type': 'application/json'
          }

      def request(self, method, endpoint, data=None):
          url = f"{self.base_url}{endpoint}"
          
          response = requests.request(
              method=method,
              url=url,
              headers=self.headers,
              json=data if data else None
          )
          
          response.raise_for_status()
          return response.json()

      def get_realm(self):
          return self.request('GET', f'/realms/{self.realm_id}')

      def search_members(self, search_type, values):
          return self.request('GET', f'/realm/{self.realm_id}/members/search?type={search_type}&values={values}')

  # Usage
  client = DripClient(os.getenv('DRIP_API_KEY'), os.getenv('DRIP_REALM_ID'))
  ```

</CodeGroup>

## Error Handling

Handle authentication errors gracefully:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function handleApiCall(apiCall) {
    try {
      return await apiCall();
    } catch (error) {
      if (error.status === 401) {
        console.error('Authentication failed - check your API key');
        // Redirect to re-authenticate or refresh key
      } else if (error.status === 403) {
        console.error('Insufficient permissions for this operation');
      } else {
        console.error('API call failed:', error.message);
      }
      throw error;
    }
  }
  ```

  ```python Python theme={"dark"}
  def handle_api_call(api_call):
      try:
          return api_call()
      except requests.exceptions.HTTPError as e:
          if e.response.status_code == 401:
              print("Authentication failed - check your API key")
              # Handle re-authentication
          elif e.response.status_code == 403:
              print("Insufficient permissions for this operation")
          else:
              print(f"API call failed: {e}")
          raise
  ```

</CodeGroup>

## Security Best Practices

<CardGroup>
  <Card title="Secure Storage" icon="vault">
    * Store API keys in environment variables
    * Use secure key management services in production
    * Never commit keys to version control
  </Card>

  <Card title="Key Rotation" icon="arrows-rotate">
    * Rotate API keys regularly (monthly/quarterly)
    * Have a process for emergency key rotation
    * Revoke unused or compromised keys immediately
  </Card>

  <Card title="Network Security" icon="shield">
    * Always use HTTPS for API requests
    * Implement request signing for extra security
    * Use IP allowlisting when possible
  </Card>

  <Card title="Monitoring" icon="chart-line">
    * Monitor API key usage patterns
    * Set up alerts for unusual activity
    * Log authentication failures for security analysis
  </Card>
</CardGroup>

## Testing Authentication

Use this simple test to verify your authentication setup:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function testAuth() {
    try {
      const response = await fetch(`https://api.drip.re/api/v1/realms/${DRIP_REALM_ID}`, {
        headers: {
          'Authorization': `Bearer ${DRIP_API_KEY}`
        }
      });

      if (response.ok) {
        const realm = await response.json();
        console.log('✅ Authentication successful!');
        console.log(`Connected to realm: ${realm.name}`);
      } else {
        console.log('❌ Authentication failed');
      }
    } catch (error) {
      console.error('Error testing authentication:', error);
    }
  }

  ```

  ```python Python theme={"dark"}
  def test_auth():
      try:
          response = requests.get(
              f'https://api.drip.re/api/v1/realms/{DRIP_REALM_ID}',
              headers={'Authorization': f'Bearer {DRIP_API_KEY}'}
          )
          
          if response.ok:
              realm = response.json()
              print("✅ Authentication successful!")
              print(f"Connected to realm: {realm['name']}")
          else:
              print("❌ Authentication failed")
              
      except Exception as e:
          print(f"Error testing authentication: {e}")
  ```

  ```bash cURL theme={"dark"}
  # Test authentication
  curl -X GET "https://api.drip.re/api/v1/realms/YOUR_REALM_ID" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -w "\nStatus: %{http_code}\n"
  ```

</CodeGroup>

## Troubleshooting

Common authentication issues and solutions:

<AccordionGroup>
  <Accordion title="401 Unauthorized">
    **Causes:**

    * Invalid or expired API key
    * Missing Authorization header
    * Incorrect Bearer token format

    **Solutions:**

    * Verify API key is correct and active
    * Check header format: `Authorization: Bearer YOUR_KEY`
    * Generate a new API key if needed
  </Accordion>

  <Accordion title="403 Forbidden">
    **Causes:**

    * API key lacks required permissions
    * Trying to access resources outside your realm
    * Account permissions changed

    **Solutions:**

    * Check your account permissions in the dashboard
    * Ensure you're accessing the correct realm
    * Contact an admin to update permissions
  </Accordion>

  <Accordion title="Rate Limiting">
    **Causes:**

    * Too many requests in a short time
    * Exceeding API quotas

    **Solutions:**

    * Implement exponential backoff
    * Check rate limit headers in responses
    * Optimize request frequency
  </Accordion>
</AccordionGroup>

# Best Practices

Source: https://docs.drip.re/developer/best-practices

Production-ready patterns and tips for DRIP API development 🚀

Build robust, scalable, and secure DRIP integrations with these battle-tested best practices from the community.

## Security First 🔒

### API Key Management

<CardGroup>
  <Card title="Environment Variables" icon="key">
    ```javascript theme={"dark"}
    // ✅ Good
    const client = new DripClient(
      process.env.DRIP_API_KEY,
      process.env.DRIP_REALM_ID
    );

    // ❌ Never do this
    const client = new DripClient(
      'drip_1234567890abcdef',
      '507f1f77bcf86cd799439011'
    );
    ```
  </Card>

  <Card title="Key Rotation" icon="arrows-rotate">
    ```javascript theme={"dark"}
    // Implement key rotation
    class SecureDripClient {
      async rotateApiKey(newKey) {
        // Test new key first
        const testClient = new DripClient(newKey, this.realmId);
        await testClient.getRealm();

        // If successful, update
        this.apiKey = newKey;
        console.log('✅ API key rotated');
      }
    }
    ```
  </Card>
</CardGroup>

### Scope Minimization

Only request the scopes you actually need:

```javascript theme={"dark"}
// ✅ Good: Minimal scopes for analytics app
const analyticsScopes = [
  'realm:read',
  'members:read'
];

// ❌ Bad: Requesting unnecessary permissions
const badScopes = [
  'realm:read',
  'members:read',
  'members:write',  // Don't need this for analytics
  'admin:read',     // Way too broad
  'webhooks:write'  // Not needed
];
```

## Performance Optimization ⚡

### Batch Operations

Use batch endpoints whenever possible:

<Tabs>
  <Tab title="JavaScript">
    ```javascript theme={"dark"}
    // ❌ Slow: Individual requests
    for (const member of members) {
      await updateMemberBalance(realmId, member.id, 10);
    }
    // 100 members = 100 API calls = slow

    // ✅ Fast: Batch request
    const updates = members.map(m => ({ 
      memberId: m.id, 
      tokens: 10 
    }));
    await batchUpdateBalances(realmId, updates);
    // 100 members = 1 API call = fast
    ```
  </Tab>

  <Tab title="Python">
    ```python theme={"dark"}
    # ❌ Slow: Individual requests
    for member in members:
        update_member_balance(realm_id, member['id'], 10)
    # 100 members = 100 API calls

    # ✅ Fast: Batch request
    updates = [
        {'memberId': member['id'], 'tokens': 10}
        for member in members
    ]
    batch_update_balances(realm_id, updates)
    # 100 members = 1 API call
    ```
  </Tab>
</Tabs>

### Caching Strategy

Implement smart caching to reduce API calls:

```javascript theme={"dark"}
class CachedDripClient extends DripClient {
  constructor(apiKey, realmId, cacheTtl = 300000) { // 5 minutes
    super(apiKey, realmId);
    this.cache = new Map();
    this.cacheTtl = cacheTtl;
  }

  async cachedRequest(cacheKey, requestFn) {
    const cached = this.cache.get(cacheKey);
    
    if (cached && Date.now() - cached.timestamp < this.cacheTtl) {
      return cached.data;
    }

    const data = await requestFn();
    this.cache.set(cacheKey, {
      data,
      timestamp: Date.now()
    });

    return data;
  }

  async getRealm() {
    return this.cachedRequest(
      `realm:${this.realmId}`,
      () => super.getRealm()
    );
  }

  async searchMembers(type, values) {
    // Don't cache member searches as they change frequently
    return super.searchMembers(type, values);
  }
}
```

### Request Optimization

<AccordionGroup>
  <Accordion title="Parallel Requests">
    Run independent requests in parallel:

    ```javascript theme={"dark"}
    // ❌ Slow: Sequential requests
    const realm = await client.getRealm();
    const members = await client.searchMembers('drip-id', 'all');
    const points = await client.getRealmPoints();

    // ✅ Fast: Parallel requests
    const [realm, members, points] = await Promise.all([
      client.getRealm(),
      client.searchMembers('drip-id', 'all'),
      client.getRealmPoints()
    ]);
    ```
  </Accordion>

  <Accordion title="Request Queuing">
    Implement request queuing to avoid rate limits:

    ```javascript theme={"dark"}
    class QueuedDripClient extends DripClient {
      constructor(apiKey, realmId, maxConcurrent = 5) {
        super(apiKey, realmId);
        this.queue = [];
        this.running = 0;
        this.maxConcurrent = maxConcurrent;
      }

      async queueRequest(requestFn) {
        return new Promise((resolve, reject) => {
          this.queue.push({ requestFn, resolve, reject });
          this.processQueue();
        });
      }

      async processQueue() {
        if (this.running >= this.maxConcurrent || this.queue.length === 0) {
          return;
        }

        this.running++;
        const { requestFn, resolve, reject } = this.queue.shift();

        try {
          const result = await requestFn();
          resolve(result);
        } catch (error) {
          reject(error);
        } finally {
          this.running--;
          setTimeout(() => this.processQueue(), 100); // Small delay
        }
      }
    }
    ```
  </Accordion>
</AccordionGroup>

## Error Handling 🛡️

### Comprehensive Error Handling

```javascript theme={"dark"}
class RobustDripClient extends DripClient {
  async safeRequest(method, endpoint, data, options = {}) {
    const { retries = 3, retryDelay = 1000 } = options;
    
    for (let attempt = 0; attempt <= retries; attempt++) {
      try {
        return await this.request(method, endpoint, data);
      } catch (error) {
        const isLastAttempt = attempt === retries;
        
        // Don't retry client errors (4xx) except rate limits
        if (error.status >= 400 && error.status < 500 && error.status !== 429) {
          throw error;
        }
        
        // Handle rate limits
        if (error.status === 429) {
          const retryAfter = error.retryAfter || 60;
          if (!isLastAttempt) {
            console.log(`Rate limited. Retrying in ${retryAfter}s...`);
            await this.sleep(retryAfter * 1000);
            continue;
          }
        }
        
        // Retry server errors with exponential backoff
        if (error.status >= 500 && !isLastAttempt) {
          const delay = retryDelay * Math.pow(2, attempt);
          console.log(`Server error. Retrying in ${delay}ms...`);
          await this.sleep(delay);
          continue;
        }
        
        // If we get here, we've exhausted retries
        throw error;
      }
    }
  }
}
```

### Error Recovery Patterns

<Tabs>
  <Tab title="Circuit Breaker">
    ```javascript theme={"dark"}
    class CircuitBreaker {
      constructor(threshold = 5, timeout = 60000) {
        this.failureCount = 0;
        this.threshold = threshold;
        this.timeout = timeout;
        this.state = 'CLOSED'; // CLOSED, OPEN, HALF_OPEN
        this.nextAttempt = Date.now();
      }

      async call(fn) {
        if (this.state === 'OPEN') {
          if (Date.now() < this.nextAttempt) {
            throw new Error('Circuit breaker is OPEN');
          }
          this.state = 'HALF_OPEN';
        }

        try {
          const result = await fn();
          this.onSuccess();
          return result;
        } catch (error) {
          this.onFailure();
          throw error;
        }
      }

      onSuccess() {
        this.failureCount = 0;
        this.state = 'CLOSED';
      }

      onFailure() {
        this.failureCount++;
        if (this.failureCount >= this.threshold) {
          this.state = 'OPEN';
          this.nextAttempt = Date.now() + this.timeout;
        }
      }
    }
    ```
  </Tab>

  <Tab title="Fallback Values">
    ```javascript theme={"dark"}
    async function getMembersWithFallback(client) {
      try {
        return await client.searchMembers('drip-id', 'all');
      } catch (error) {
        console.error('Failed to fetch members, using cached data');
        return getCachedMembers(); // Fallback to cache
      }
    }

    async function getLeaderboardWithFallback(client) {
      try {
        return await client.getLeaderboard();
      } catch (error) {
        console.error('API unavailable, showing static leaderboard');
        return getStaticLeaderboard(); // Fallback to static data
      }
    }
    ```
  </Tab>
</Tabs>

## Code Organization 🏗️

### Modular Architecture

Organize your code into focused modules:

```javascript theme={"dark"}
// services/drip.js
export class DripService {
  constructor(apiKey, realmId) {
    this.client = new DripClient(apiKey, realmId);
  }

  async getRealmInfo() {
    return this.client.getRealm();
  }
}

// services/members.js
export class MemberService extends DripService {
  async findMember(type, value) {
    const result = await this.client.searchMembers(type, value);
    return result.data?.[0] || null;
  }

  async awardPoints(memberId, points) {
    return this.client.updateMemberBalance(memberId, points);
  }
}

// services/analytics.js
export class AnalyticsService extends DripService {
  async getTopMembers(limit = 10) {
    const members = await this.client.searchMembers('drip-id', 'all');
    return members.data
      .sort((a, b) => (b.pointBalances[0]?.balance || 0) - (a.pointBalances[0]?.balance || 0))
      .slice(0, limit);
  }
}
```

### Configuration Management

Centralize your configuration:

```javascript theme={"dark"}
// config/drip.js
export const dripConfig = {
  development: {
    apiKey: process.env.DEV_DRIP_API_KEY,
    realmId: process.env.DEV_DRIP_REALM_ID,
    baseUrl: 'https://api.drip.re/api/v1',
    rateLimit: {
      maxConcurrent: 3,
      delay: 200
    }
  },
  production: {
    apiKey: process.env.PROD_DRIP_API_KEY,
    realmId: process.env.PROD_DRIP_REALM_ID,
    baseUrl: 'https://api.drip.re/api/v1',
    rateLimit: {
      maxConcurrent: 10,
      delay: 50
    }
  }
};

export const getConfig = () => {
  const env = process.env.NODE_ENV || 'development';
  return dripConfig[env];
};
```

## Monitoring and Observability 📊

### Logging Best Practices

```javascript theme={"dark"}
import winston from 'winston';

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  transports: [
    new winston.transports.File({ filename: 'drip-api.log' })
  ]
});

class LoggedDripClient extends DripClient {
  async request(method, endpoint, data) {
    const startTime = Date.now();
    const requestId = Math.random().toString(36).substring(7);
    
    logger.info('API request started', {
      requestId,
      method,
      endpoint,
      timestamp: new Date().toISOString()
    });

    try {
      const result = await super.request(method, endpoint, data);
      const duration = Date.now() - startTime;
      
      logger.info('API request completed', {
        requestId,
        duration,
        status: 'success'
      });
      
      return result;
    } catch (error) {
      const duration = Date.now() - startTime;
      
      logger.error('API request failed', {
        requestId,
        duration,
        status: 'error',
        error: error.message,
        stack: error.stack
      });
      
      throw error;
    }
  }
}
```

### Metrics Collection

```javascript theme={"dark"}
class MetricsDripClient extends DripClient {
  constructor(apiKey, realmId) {
    super(apiKey, realmId);
    this.metrics = {
      requests: 0,
      errors: 0,
      totalDuration: 0,
      endpoints: new Map()
    };
  }

  async request(method, endpoint, data) {
    const startTime = Date.now();
    this.metrics.requests++;
    
    try {
      const result = await super.request(method, endpoint, data);
      this.recordSuccess(endpoint, Date.now() - startTime);
      return result;
    } catch (error) {
      this.recordError(endpoint, Date.now() - startTime);
      throw error;
    }
  }

  recordSuccess(endpoint, duration) {
    this.metrics.totalDuration += duration;
    this.updateEndpointMetrics(endpoint, duration, true);
  }

  recordError(endpoint, duration) {
    this.metrics.errors++;
    this.metrics.totalDuration += duration;
    this.updateEndpointMetrics(endpoint, duration, false);
  }

  updateEndpointMetrics(endpoint, duration, success) {
    if (!this.metrics.endpoints.has(endpoint)) {
      this.metrics.endpoints.set(endpoint, {
        requests: 0,
        errors: 0,
        totalDuration: 0
      });
    }
    
    const endpointMetrics = this.metrics.endpoints.get(endpoint);
    endpointMetrics.requests++;
    endpointMetrics.totalDuration += duration;
    if (!success) endpointMetrics.errors++;
  }

  getMetrics() {
    return {
      ...this.metrics,
      averageResponseTime: this.metrics.totalDuration / this.metrics.requests,
      errorRate: this.metrics.errors / this.metrics.requests,
      endpoints: Object.fromEntries(this.metrics.endpoints)
    };
  }
}
```

## Testing Strategies 🧪

### Unit Testing

```javascript theme={"dark"}
// tests/drip-client.test.js
import { jest } from '@jest/globals';
import { DripClient } from '../src/drip-client.js';

describe('DripClient', () => {
  let client;
  let mockFetch;

  beforeEach(() => {
    mockFetch = jest.fn();
    global.fetch = mockFetch;
    client = new DripClient('test-key', 'test-realm');
  });

  test('should search members successfully', async () => {
    const mockResponse = {
      data: [{ id: '123', name: 'Test User' }]
    };

    mockFetch.mockResolvedValueOnce({
      ok: true,
      json: async () => mockResponse
    });

    const result = await client.searchMembers('discord-id', '123456789');
    
    expect(mockFetch).toHaveBeenCalledWith(
      expect.stringContaining('/members/search'),
      expect.objectContaining({
        headers: expect.objectContaining({
          'Authorization': 'Bearer test-key'
        })
      })
    );
    
    expect(result).toEqual(mockResponse);
  });

  test('should handle API errors gracefully', async () => {
    mockFetch.mockResolvedValueOnce({
      ok: false,
      status: 404,
      json: async () => ({ error: 'Not found' })
    });

    await expect(
      client.searchMembers('discord-id', 'invalid')
    ).rejects.toThrow('API Error: 404');
  });
});
```

### Integration Testing

```javascript theme={"dark"}
// tests/integration.test.js
describe('DRIP API Integration', () => {
  let client;

  beforeAll(() => {
    client = new DripClient(
      process.env.TEST_DRIP_API_KEY,
      process.env.TEST_DRIP_REALM_ID
    );
  });

  test('should fetch realm information', async () => {
    const realm = await client.getRealm();
    
    expect(realm).toHaveProperty('id');
    expect(realm).toHaveProperty('name');
    expect(realm.id).toBe(process.env.TEST_DRIP_REALM_ID);
  });

  test('should handle member operations', async () => {
    // Create test member (if not exists)
    const testMemberId = 'test-member-123';
    
    // Award points
    const result = await client.updateMemberBalance(testMemberId, 100);
    expect(result).toHaveProperty('id');
    
    // Verify balance
    const members = await client.searchMembers('drip-id', testMemberId);
    expect(members.data[0].pointBalances[0].balance).toBeGreaterThanOrEqual(100);
  });
});
```

## Deployment Patterns 🚀

### Environment Configuration

```javascript theme={"dark"}
// .env.example
DRIP_API_KEY=your_api_key_here
DRIP_REALM_ID=your_realm_id_here
NODE_ENV=production
LOG_LEVEL=info
CACHE_TTL=300000
RATE_LIMIT_MAX_CONCURRENT=10
```

### Health Checks

```javascript theme={"dark"}
// health.js
export async function healthCheck() {
  const client = new DripClient(
    process.env.DRIP_API_KEY,
    process.env.DRIP_REALM_ID
  );

  try {
    // Simple API call to verify connectivity
    await client.getRealm();
    
    return {
      status: 'healthy',
      timestamp: new Date().toISOString(),
      services: {
        drip_api: 'up'
      }
    };
  } catch (error) {
    return {
      status: 'unhealthy',
      timestamp: new Date().toISOString(),
      services: {
        drip_api: 'down'
      },
      error: error.message
    };
  }
}
```

## Community Best Practices 🌟

### Code Reviews

When reviewing DRIP API code, check for:

* [ ] API keys not hardcoded
* [ ] Proper error handling
* [ ] Rate limit considerations
* [ ] Batch operations used where possible
* [ ] Appropriate scopes requested
* [ ] Caching implemented for static data
* [ ] Logging for debugging
* [ ] Tests covering happy and error paths

### Documentation

Document your integrations:

```javascript theme={"dark"}
/**
 * Awards points to a member for completing a task
 * 
 * @param {string} memberId - The DRIP member ID
 * @param {number} points - Points to award (positive) or deduct (negative)
 * @param {string} reason - Reason for the point change (for logging)
 * @returns {Promise<Object>} Updated member balance
 * 
 * @example
 * await awardTaskPoints('member123', 50, 'Completed daily quest');
 */
async function awardTaskPoints(memberId, points, reason) {
  logger.info('Awarding points', { memberId, points, reason });
  
  try {
    return await client.updateMemberBalance(memberId, points);
  } catch (error) {
    logger.error('Failed to award points', { memberId, points, error });
    throw error;
  }
}
```

## Quick Checklist ✅

Before deploying your DRIP integration:

* [ ] API keys stored securely (environment variables)
* [ ] Error handling implemented with retries
* [ ] Rate limiting respected (batch operations, delays)
* [ ] Caching implemented for static data
* [ ] Logging and monitoring set up
* [ ] Tests written and passing
* [ ] Documentation updated
* [ ] Health checks implemented
* [ ] Minimal scopes requested and justified

<Info>
  **Need help?** Join our [Discord community](https://discord.gg/dripchain) to get advice from other developers and share your own best practices! 🚀
</Info>

# Core Concepts

Source: https://docs.drip.re/developer/core-concepts

Understanding DRIP's data model, relationships, and key concepts

This guide explains the fundamental concepts and data model that power the DRIP ecosystem. Understanding these concepts is essential for building effective integrations.

<Info>
  Terminology: In the dashboard UI, a "Realm" is sometimes labeled as "Project". They refer to the same thing.
</Info>

## API Client Types

DRIP supports two distinct types of API clients:

### Realm Clients

**Purpose**: Direct integration with your own realm\
**Scope**: Single realm access\
**Authorization**: Automatic access to your realm\
**Use Cases**: Custom dashboards, internal automation, realm-specific tools

### App Clients

**Purpose**: Multi-realm applications for the broader ecosystem\
**Scope**: Multiple realm access with explicit authorization\
**Authorization**: Platform approval + individual realm authorization\
**Use Cases**: Third-party integrations, marketplace apps, SaaS tools

<Info>
  The type of client determines your authorization flow and available permissions. Choose based on whether you're building for your own realm or the broader DRIP ecosystem.
</Info>

## Data Model Overview

DRIP's architecture is built around these core entities:

```mermaid theme={"dark"}
graph TB
    Realm[Realm] --> Member[Realm Members]
    Realm --> Points[Realm Points]
    Realm --> Quest[Quests]
    Realm --> Store[Store Items]
    Realm --> GhostCred[Ghost Credentials]
    
    Member --> Balance[Point Balances]
    Member --> Progress[Quest Progress]
    Member --> Purchase[Purchases]
    
    GhostCred --> GhostBalance[Ghost Balances]
    GhostCred -.->|link| Member
    
    Quest --> Task[Tasks]
    Task --> Trigger[Triggers]
    Task --> Action[Actions]
    Task --> Condition[Conditions]
    
    Points --> Balance
    Points --> GhostBalance
    Store --> Purchase
```

## Realms

A **Realm** (or Project) represents your community or server - it's the top-level container for all resources.

### Key Properties

* **ID**: Unique identifier for the realm
* **Name**: Display name of your community
* **Subdomain**: Custom subdomain (e.g., `yourname.drip.re`)
* **Settings**: Configuration for features, branding, permissions
* **Members**: All users who have joined the realm

### Example Realm Object

```json theme={"dark"}
{
  "id": "507f1f77bcf86cd799439011",
  "name": "My Gaming Community",
  "description": "The best gaming community on Discord",
  "subdomain": "mygaming",
  "serverId": "123456789012345678",
  "ownerId": "507f1f77bcf86cd799439012",
  "level": 5,
  "premiumLevel": 2,
  "published": true,
  "verified": true
}
```

<Info>
  Most API operations are scoped to a specific realm. You'll need your Realm ID for nearly every API call.
</Info>

## Members

**Realm Members** represent users who have joined your community and can earn points, complete quests, and make purchases.

### Key Properties

* **ID**: Unique identifier for the member's account
* **Realm Membership**: Specific membership details for this realm
* **Point Balances**: Current balances for each point type
* **Credentials**: Connected accounts (Discord, Twitter, wallets)
* **Activity**: Join date, last visit, engagement metrics

### Member Search Types

You can search for members using different identifiers:

| Search Type  | Description             | Example                         |
| ------------ | ----------------------- | ------------------------------- |
| `drip-id`    | Internal DRIP member ID | `507f1f77bcf86cd799439013`      |
| `discord-id` | Discord user ID         | `123456789012345678`            |
| `twitter-id` | Twitter/X user ID       | `987654321`                     |
| `wallet`     | Crypto wallet address   | `0x742d35Cc6634C0532925a3b8D23` |
| `email`      | Email address           | `user@example.com`              |
| `username`   | Display username        | `gamerpro123`                   |

### Example Member Object

```json theme={"dark"}
{
  "id": "507f1f77bcf86cd799439013",
  "realmMemberId": "507f1f77bcf86cd799439014",
  "username": "gamerpro123",
  "displayName": "Gamer Pro",
  "imageUrl": "https://cdn.drip.re/avatars/123.png",
  "joinedAt": "2024-01-15T10:30:00Z",
  "lastVisit": "2024-01-20T14:22:00Z",
  "pointBalances": [
    {
      "balance": 1500,
      "realmPoint": {
        "id": "507f1f77bcf86cd799439015",
        "name": "XP",
        "emoji": "⭐"
      }
    }
  ]
}
```

## Points (Currencies)

**Realm Points** are customizable currencies that members can earn, spend, and transfer within your community.

### Point Types

* **Primary Currency**: Main point system (e.g., XP, Coins)
* **Secondary Currencies**: Additional point types (e.g., Gems, Tokens)
* **Event Points**: Temporary currencies for special events
* **Branded Points**: Custom-branded currencies with logos

### Key Operations

* **Award Points**: Add points to a member's balance
* **Deduct Points**: Remove points (for purchases, penalties)
* **Transfer Points**: Move points between members
* **Batch Updates**: Update multiple balances at once

### Example Point Balance Update

```json theme={"dark"}
{
  "tokens": 100,
  "realmPointId": "507f1f77bcf86cd799439015"
}
```

<Warning>
  Point operations are atomic - they either succeed completely or fail completely. This prevents double-spending and ensures data consistency.
</Warning>

## Ghost Credentials

**Ghost Credentials** are non-verified identity records that can accumulate points before being linked to an account. They enable pre-crediting users who haven't yet connected to your realm.

### Key Characteristics

* **Non-verified**: Created by your app/realm, not verified by the user
* **Realm-scoped**: Each credential belongs to a specific realm
* **Independent balances**: Can hold point balances without being linked to an account
* **Linkable**: When linked to an account, balances transfer automatically

### Supported Types

| Type         | Description                   |
| ------------ | ----------------------------- |
| `twitter-id` | Twitter/X user ID             |
| `discord-id` | Discord user ID               |
| `wallet`     | Blockchain wallet address     |
| `email`      | Email address                 |
| `custom`     | Custom identifier with source |

### Use Cases

* Pre-credit Twitter followers before they join
* Track wallet activity before users connect
* Award points to email addresses before signup
* Migrate users from external systems

<Info>
  When a ghost credential is linked to an account, all accumulated balances are atomically transferred to the account's point balances. See the [Ghost Credentials guide](/developer/credentials) for details.
</Info>

## Quests

**Quests** are gamified task systems that engage members through challenges, rewards, and progression.

### Quest Structure

```mermaid theme={"dark"}
graph LR
    Quest --> Task1[Task 1]
    Quest --> Task2[Task 2]
    Quest --> Task3[Task 3]
    
    Task1 --> Trigger1[Triggers]
    Task1 --> Action1[Actions]
    Task1 --> Condition1[Conditions]
    
    Task2 --> Trigger2[Triggers]
    Task2 --> Action2[Actions]
    Task2 --> Condition2[Conditions]
```

### Components

| Component     | Purpose                          | Examples                                 |
| ------------- | -------------------------------- | ---------------------------------------- |
| **Quest**     | Overall challenge container      | "Weekly Challenges", "Onboarding"        |
| **Task**      | Individual steps within quest    | "Join Discord", "Make 5 Posts"           |
| **Trigger**   | Events that activate tasks       | Message sent, reaction added             |
| **Action**    | What happens when task completes | Award points, assign role                |
| **Condition** | Requirements to complete task    | Minimum message length, specific channel |

### Quest States

* **Draft**: Being created, not yet active
* **Active**: Running and accepting completions
* **Paused**: Temporarily stopped
* **Completed**: Finished, no longer accepting new participants
* **Archived**: Historical record, not visible to users

## Store Items

**Store Items** allow members to spend their points on rewards, perks, and digital goods.

### Item Types

* **Digital Rewards**: Exclusive content, early access
* **Role Upgrades**: Special Discord roles and permissions
* **Physical Items**: Merchandise, gift cards (with shipping)
* **Experiences**: Events, meetings, consultations

### Key Properties

```json theme={"dark"}
{
  "id": "507f1f77bcf86cd799439016",
  "name": "VIP Discord Role",
  "description": "Get exclusive VIP access and perks",
  "price": 1000,
  "realmPointId": "507f1f77bcf86cd799439015",
  "category": "roles",
  "inventory": 50,
  "purchaseLimit": 1,
  "active": true
}
```

## Relationships and Workflows

### Common Integration Patterns

<AccordionGroup>
  <Accordion title="Member Onboarding">
    1. Member joins Discord server
    2. DRIP creates realm member record
    3. Welcome quest automatically starts
    4. Member completes onboarding tasks
    5. Points awarded for completion
  </Accordion>

  <Accordion title="Activity Rewards">
    1. Member performs action (message, reaction, etc.)
    2. Webhook triggers DRIP API call
    3. Points awarded based on activity type
    4. Member balance updated in real-time
    5. Leaderboards automatically refresh
  </Accordion>

  <Accordion title="Store Purchase">
    1. Member browses store items
    2. Selects item and confirms purchase
    3. Points deducted from member balance
    4. Item delivered (role, access, etc.)
    5. Transaction recorded for analytics
  </Accordion>

  <Accordion title="Quest Completion">
    1. Member starts quest
    2. Completes required tasks
    3. Conditions verified automatically
    4. Rewards distributed via actions
    5. Progress tracked and displayed
  </Accordion>
</AccordionGroup>

## Data Consistency

DRIP ensures data consistency through:

* **Atomic Operations**: All-or-nothing transactions
* **Validation**: Input validation and business rule enforcement
* **Audit Trails**: Complete history of all changes
* **Rate Limiting**: Prevents abuse and ensures system stability

## Best Practices

<CardGroup>
  <Card title="Efficient Queries" icon="gauge-high">
    * Use specific search parameters
    * Implement pagination for large datasets
    * Cache frequently accessed data
    * Batch operations when possible
  </Card>

  <Card title="Error Handling" icon="shield-exclamation">
    * Always check response status codes
    * Implement retry logic with backoff
    * Log errors for debugging
    * Provide meaningful user feedback
  </Card>

  <Card title="Security" icon="lock">
    * Validate all user inputs
    * Use least-privilege API keys
    * Implement rate limiting
    * Monitor for unusual activity
  </Card>

  <Card title="Performance" icon="rocket">
    * Use webhooks for real-time updates
    * Implement efficient caching strategies
    * Optimize database queries
    * Monitor API response times
  </Card>
</CardGroup>

## Next Steps

Now that you understand DRIP's core concepts, explore these integration guides:

<CardGroup>
  <Card title="Managing Members" icon="users" href="/developer/guides/managing-members">
    Learn to search, update, and manage community members
  </Card>

  <Card title="Point Systems" icon="coins" href="/developer/guides/point-systems">
    Implement reward systems and point management
  </Card>

  <Card title="Quest Management" icon="map" href="/developer/guides/quest-management">
    Create and manage gamified experiences
  </Card>

  <Card title="Webhooks" icon="webhook" href="/developer/guides/webhooks">
    Set up real-time event notifications
  </Card>
</CardGroup>

# Ghost Credentials

Source: https://docs.drip.re/developer/credentials

Pre-credit users before they connect with ghost credentials

Ghost credentials allow you to create identity records and assign points to users before they've connected to your realm. This is powerful for pre-seeding rewards, running off-platform campaigns, or migrating users from external systems.

## Overview

A **ghost credential** is a non-verified identity record (Twitter ID, wallet address, email, etc.) that can accumulate point balances independently. When the user eventually connects that identity to your realm, the ghost credential is linked to their account and all accumulated balances are transferred.

<Info>
  Ghost credentials are realm-specific. The same Twitter ID can exist as separate ghost credentials in different realms, each with their own point balances.
</Info>

### Use Cases

<CardGroup>
  <Card title="Pre-Credit Campaigns" icon="bullhorn">
    Award points to Twitter followers or wallet holders before they join your community
  </Card>

  <Card title="Off-Platform Activity" icon="arrow-up-right-from-square">
    Track and reward activity that happens outside your realm (external events, partnerships)
  </Card>

  <Card title="User Migration" icon="arrows-rotate">
    Import users from external systems with their pre-existing point balances
  </Card>

  <Card title="Email Onboarding" icon="envelope">
    Assign welcome bonuses to email addresses before users complete signup
  </Card>
</CardGroup>

## Credential Types

Ghost credentials support multiple identity formats:

| Type         | Description                           | Example Value                                |
| ------------ | ------------------------------------- | -------------------------------------------- |
| `twitter-id` | Twitter/X user ID                     | `1234567890`                                 |
| `discord-id` | Discord user ID                       | `123456789012345678`                         |
| `wallet`     | Blockchain wallet address             | `0x742d35Cc6634C0532925a3b844Bc454e4438f44e` |
| `email`      | Email address                         | `user@example.com`                           |
| `custom`     | Custom identifier (requires `source`) | `customer_12345`                             |

## Creating Credentials

### Social Credentials

Create credentials for social platform identities like Twitter or Discord:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function createTwitterCredential(realmId, twitterId, username) {
    const response = await fetch(
      `https://api.drip.re/api/v1/realms/${realmId}/credentials/social`,
      {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          provider: 'twitter',
          providerId: twitterId,
          username: username
        })
      }
    );

    return response.json();
  }

  // Create a ghost credential for a Twitter user
  const credential = await createTwitterCredential(
    'YOUR_REALM_ID',
    '1234567890',
    'twitter_handle'
  );

  ```

  ```python Python theme={"dark"}
  import requests
  import os

  def create_twitter_credential(realm_id, twitter_id, username):
      url = f"https://api.drip.re/api/v1/realms/{realm_id}/credentials/social"
      
      headers = {
          'Authorization': f'Bearer {os.getenv("DRIP_API_KEY")}',
          'Content-Type': 'application/json'
      }
      
      data = {
          'provider': 'twitter',
          'providerId': twitter_id,
          'username': username
      }
      
      response = requests.post(url, headers=headers, json=data)
      return response.json()

  # Create a ghost credential for a Twitter user
  credential = create_twitter_credential(
      'YOUR_REALM_ID',
      '1234567890',
      'twitter_handle'
  )
  ```

  ```bash cURL theme={"dark"}
  curl -X POST "https://api.drip.re/api/v1/realms/YOUR_REALM_ID/credentials/social" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "provider": "twitter",
      "providerId": "1234567890",
      "username": "twitter_handle"
    }'
  ```

</CodeGroup>

### Wallet Credentials

Create credentials for blockchain wallet addresses:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function createWalletCredential(realmId, address, chain) {
    const response = await fetch(
      `https://api.drip.re/api/v1/realms/${realmId}/credentials/wallet`,
      {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          address: address,
          chain: chain
        })
      }
    );

    return response.json();
  }

  // Create a ghost credential for an Ethereum wallet
  const credential = await createWalletCredential(
    'YOUR_REALM_ID',
    '0x742d35Cc6634C0532925a3b844Bc454e4438f44e',
    'ethereum'
  );

  ```

  ```python Python theme={"dark"}
  def create_wallet_credential(realm_id, address, chain):
      url = f"https://api.drip.re/api/v1/realms/{realm_id}/credentials/wallet"
      
      headers = {
          'Authorization': f'Bearer {os.getenv("DRIP_API_KEY")}',
          'Content-Type': 'application/json'
      }
      
      data = {
          'address': address,
          'chain': chain
      }
      
      response = requests.post(url, headers=headers, json=data)
      return response.json()

  # Create a ghost credential for an Ethereum wallet
  credential = create_wallet_credential(
      'YOUR_REALM_ID',
      '0x742d35Cc6634C0532925a3b844Bc454e4438f44e',
      'ethereum'
  )
  ```

  ```bash cURL theme={"dark"}
  curl -X POST "https://api.drip.re/api/v1/realms/YOUR_REALM_ID/credentials/wallet" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "address": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
      "chain": "ethereum"
    }'
  ```

</CodeGroup>

## Finding Credentials

Look up existing ghost credentials by their identifier:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function findCredential(realmId, type, value) {
    const params = new URLSearchParams({ type, value });

    const response = await fetch(
      `https://api.drip.re/api/v1/realms/${realmId}/credentials/find?${params}`,
      {
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`
        }
      }
    );
    
    if (response.status === 404) {
      return null; // Credential doesn't exist
    }
    
    return response.json();
  }

  // Find by Twitter ID
  const twitterCred = await findCredential('YOUR_REALM_ID', 'twitter-id', '1234567890');

  // Find by wallet address
  const walletCred = await findCredential('YOUR_REALM_ID', 'wallet', '0x742d35Cc...');

  // Find by email
  const emailCred = await findCredential('YOUR_REALM_ID', 'email', 'user@example.com');

  ```

  ```python Python theme={"dark"}
  def find_credential(realm_id, cred_type, value):
      url = f"https://api.drip.re/api/v1/realms/{realm_id}/credentials/find"
      
      headers = {
          'Authorization': f'Bearer {os.getenv("DRIP_API_KEY")}'
      }
      
      params = {
          'type': cred_type,
          'value': value
      }
      
      response = requests.get(url, headers=headers, params=params)
      
      if response.status_code == 404:
          return None
      
      return response.json()

  # Find by Twitter ID
  twitter_cred = find_credential('YOUR_REALM_ID', 'twitter-id', '1234567890')
  ```

  ```bash cURL theme={"dark"}
  # Find by Twitter ID
  curl -X GET "https://api.drip.re/api/v1/realms/YOUR_REALM_ID/credentials/find?type=twitter-id&value=1234567890" \
    -H "Authorization: Bearer YOUR_API_KEY"

  # Find by wallet
  curl -X GET "https://api.drip.re/api/v1/realms/YOUR_REALM_ID/credentials/find?type=wallet&value=0x742d35Cc..." \
    -H "Authorization: Bearer YOUR_API_KEY"
  ```

</CodeGroup>

## Managing Balances

### Update Balance

Award or deduct points from a ghost credential:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function updateCredentialBalance(realmId, type, value, amount, realmPointId = null) {
    const params = new URLSearchParams({ type, value });

    const body = { amount };
    if (realmPointId) {
      body.realmPointId = realmPointId;
    }
    
    const response = await fetch(
      `https://api.drip.re/api/v1/realms/${realmId}/credentials/balance?${params}`,
      {
        method: 'PATCH',
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
      }
    );
    
    return response.json();
  }

  // Award 100 points to a Twitter user (uses default currency)
  await updateCredentialBalance('YOUR_REALM_ID', 'twitter-id', '1234567890', 100);

  // Deduct 50 points from a wallet
  await updateCredentialBalance('YOUR_REALM_ID', 'wallet', '0x742d35Cc...', -50);

  // Award 200 of a specific currency
  await updateCredentialBalance('YOUR_REALM_ID', 'email', 'user@example.com', 200, 'CURRENCY_ID');

  ```

  ```python Python theme={"dark"}
  def update_credential_balance(realm_id, cred_type, value, amount, realm_point_id=None):
      url = f"https://api.drip.re/api/v1/realms/{realm_id}/credentials/balance"
      
      headers = {
          'Authorization': f'Bearer {os.getenv("DRIP_API_KEY")}',
          'Content-Type': 'application/json'
      }
      
      params = {
          'type': cred_type,
          'value': value
      }
      
      data = {'amount': amount}
      if realm_point_id:
          data['realmPointId'] = realm_point_id
      
      response = requests.patch(url, headers=headers, params=params, json=data)
      return response.json()

  # Award 100 points to a Twitter user
  update_credential_balance('YOUR_REALM_ID', 'twitter-id', '1234567890', 100)
  ```

  ```bash cURL theme={"dark"}
  # Award 100 points to a Twitter user
  curl -X PATCH "https://api.drip.re/api/v1/realms/YOUR_REALM_ID/credentials/balance?type=twitter-id&value=1234567890" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"amount": 100}'
  ```

</CodeGroup>

<Info>
  If `realmPointId` is not specified, the realm's default currency is used.
</Info>

### Batch Updates

Update multiple credentials in a single request:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function batchUpdateBalances(realmId, updates) {
    const response = await fetch(
      `https://api.drip.re/api/v1/realms/${realmId}/credentials/transaction`,
      {
        method: 'PATCH',
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ updates })
      }
    );

    return response.json();
  }

  // Batch award points to multiple credentials
  const result = await batchUpdateBalances('YOUR_REALM_ID', [
    { type: 'twitter-id', value: '1234567890', amount: 100 },
    { type: 'twitter-id', value: '9876543210', amount: 150 },
    { type: 'wallet', value: '0x742d35Cc...', amount: 200 },
    { type: 'email', value: 'user@example.com', amount: 75 }
  ]);

  console.log(`Success: ${result.results.length}, Errors: ${result.errors.length}`);

  ```

  ```python Python theme={"dark"}
  def batch_update_balances(realm_id, updates):
      url = f"https://api.drip.re/api/v1/realms/{realm_id}/credentials/transaction"
      
      headers = {
          'Authorization': f'Bearer {os.getenv("DRIP_API_KEY")}',
          'Content-Type': 'application/json'
      }
      
      data = {'updates': updates}
      
      response = requests.patch(url, headers=headers, json=data)
      return response.json()

  # Batch award points
  result = batch_update_balances('YOUR_REALM_ID', [
      {'type': 'twitter-id', 'value': '1234567890', 'amount': 100},
      {'type': 'twitter-id', 'value': '9876543210', 'amount': 150},
      {'type': 'wallet', 'value': '0x742d35Cc...', 'amount': 200}
  ])
  ```

  ```bash cURL theme={"dark"}
  curl -X PATCH "https://api.drip.re/api/v1/realms/YOUR_REALM_ID/credentials/transaction" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "updates": [
        {"type": "twitter-id", "value": "1234567890", "amount": 100},
        {"type": "twitter-id", "value": "9876543210", "amount": 150},
        {"type": "wallet", "value": "0x742d35Cc...", "amount": 200}
      ]
    }'
  ```

</CodeGroup>

### Transfer Points

Transfer points between two credentials:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function transferPoints(realmId, from, to, amount, realmPointId = null) {
    const params = new URLSearchParams({
      fromType: from.type,
      fromValue: from.value,
      toType: to.type,
      toValue: to.value
    });

    const body = { amount };
    if (realmPointId) {
      body.realmPointId = realmPointId;
    }
    
    const response = await fetch(
      `https://api.drip.re/api/v1/realms/${realmId}/credentials/transfer?${params}`,
      {
        method: 'PATCH',
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
      }
    );
    
    return response.json();
  }

  // Transfer 50 points from one Twitter user to another
  await transferPoints(
    'YOUR_REALM_ID',
    { type: 'twitter-id', value: '1234567890' },
    { type: 'twitter-id', value: '9876543210' },
    50
  );

  // Transfer points from a wallet to an email
  await transferPoints(
    'YOUR_REALM_ID',
    { type: 'wallet', value: '0x742d35Cc...' },
    { type: 'email', value: 'user@example.com' },
    100
  );

  ```

  ```bash cURL theme={"dark"}
  curl -X PATCH "https://api.drip.re/api/v1/realms/YOUR_REALM_ID/credentials/transfer?fromType=twitter-id&fromValue=1234567890&toType=twitter-id&toValue=9876543210" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"amount": 50}'
  ```

</CodeGroup>

## Linking to Accounts

When a user connects their identity to your realm, you can link the ghost credential to their account. This transfers all accumulated balances to their account.

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function linkCredentialToAccount(realmId, type, value, accountId) {
    const params = new URLSearchParams({ type, value, accountId });

    const response = await fetch(
      `https://api.drip.re/api/v1/realms/${realmId}/credentials/link?${params}`,
      {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`
        }
      }
    );
    
    if (response.status === 204) {
      return { success: true };
    }
    
    return response.json();
  }

  // Link a Twitter credential to a user's account
  await linkCredentialToAccount(
    'YOUR_REALM_ID',
    'twitter-id',
    '1234567890',
    'ACCOUNT_ID'
  );

  ```

  ```python Python theme={"dark"}
  def link_credential_to_account(realm_id, cred_type, value, account_id):
      url = f"https://api.drip.re/api/v1/realms/{realm_id}/credentials/link"
      
      headers = {
          'Authorization': f'Bearer {os.getenv("DRIP_API_KEY")}'
      }
      
      params = {
          'type': cred_type,
          'value': value,
          'accountId': account_id
      }
      
      response = requests.post(url, headers=headers, params=params)
      return response.status_code == 204

  # Link a Twitter credential to a user's account
  link_credential_to_account(
      'YOUR_REALM_ID',
      'twitter-id',
      '1234567890',
      'ACCOUNT_ID'
  )
  ```

  ```bash cURL theme={"dark"}
  curl -X POST "https://api.drip.re/api/v1/realms/YOUR_REALM_ID/credentials/link?type=twitter-id&value=1234567890&accountId=ACCOUNT_ID" \
    -H "Authorization: Bearer YOUR_API_KEY"
  ```

</CodeGroup>

<Warning>
  Linking is a one-way operation. Once linked, ghost balances are transferred to the account and the credential cannot be unlinked. The credential will still exist but future balance updates will go directly to the account.
</Warning>

### What Happens When Linking

1. Ghost credential is found by identifier
2. All `GhostCredentialPointBalance` records are transferred to `AccountPointBalance`
3. Ghost balance records are deleted
4. Credential gets `accountId` set
5. If the account has a verified credential with the same identity, the ghost credential can auto-upgrade to verified

## Metadata

Store custom data on credentials for your application's needs:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function updateCredentialMetadata(realmId, type, value, metadata) {
    const params = new URLSearchParams({ type, value });

    const response = await fetch(
      `https://api.drip.re/api/v1/realms/${realmId}/credentials/metadata?${params}`,
      {
        method: 'PATCH',
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ metadata })
      }
    );
    
    return response.status === 204;
  }

  // Store custom metadata
  await updateCredentialMetadata(
    'YOUR_REALM_ID',
    'twitter-id',
    '1234567890',
    {
      source: 'airdrop_campaign_2024',
      tier: 'gold',
      referredBy: 'partner_xyz'
    }
  );

  ```

  ```bash cURL theme={"dark"}
  curl -X PATCH "https://api.drip.re/api/v1/realms/YOUR_REALM_ID/credentials/metadata?type=twitter-id&value=1234567890" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "metadata": {
        "source": "airdrop_campaign_2024",
        "tier": "gold",
        "referredBy": "partner_xyz"
      }
    }'
  ```

</CodeGroup>

<Info>
  Metadata is returned when finding credentials and can be used to track campaign attribution, user segments, or any custom data your application needs.
</Info>

## Deleting Credentials

Remove ghost credentials that are no longer needed:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function deleteCredential(realmId, type, value) {
    const params = new URLSearchParams({ type, value });

    const response = await fetch(
      `https://api.drip.re/api/v1/realms/${realmId}/credentials?${params}`,
      {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`
        }
      }
    );
    
    return response.status === 204;
  }

  // Delete a ghost credential
  await deleteCredential('YOUR_REALM_ID', 'twitter-id', '1234567890');

  ```

  ```bash cURL theme={"dark"}
  curl -X DELETE "https://api.drip.re/api/v1/realms/YOUR_REALM_ID/credentials?type=twitter-id&value=1234567890" \
    -H "Authorization: Bearer YOUR_API_KEY"
  ```

</CodeGroup>

<Warning>
  You cannot delete credentials that have non-zero point balances. Zero out the balance first or link the credential to transfer the balance.
</Warning>

## Custom Credential Types

For identifiers that don't fit the standard types, use the `custom` type with a `source` parameter:

```javascript theme={"dark"}
// Create a custom credential (e.g., Shopify customer ID)
const response = await fetch(
  `https://api.drip.re/api/v1/realms/${realmId}/credentials/social`,
  {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${process.env.DRIP_API_KEY}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      provider: 'shopify',  // Your custom source
      providerId: 'customer_12345',
      username: 'Customer Name'
    })
  }
);

// Find by custom type
const credential = await findCredential('YOUR_REALM_ID', 'custom', 'customer_12345');
// Note: For custom types, include source parameter:
// ?type=custom&value=customer_12345&source=shopify
```

## Best Practices

<CardGroup>
  <Card title="Batch Operations" icon="layer-group">
    Use batch endpoints when updating multiple credentials to reduce API calls and improve performance
  </Card>

  <Card title="Idempotent Creates" icon="repeat">
    Creating a credential that already exists returns a 409 Conflict - check first or handle the error
  </Card>

  <Card title="Track Attribution" icon="tag">
    Use metadata to track where credentials came from (campaigns, partners, events)
  </Card>

  <Card title="Clean Up" icon="broom">
    Periodically review and delete unused credentials with zero balances
  </Card>
</CardGroup>

## Error Handling

Common errors and how to handle them:

| Error                             | Cause                                | Solution                                     |
| --------------------------------- | ------------------------------------ | -------------------------------------------- |
| `409 Conflict`                    | Credential already exists            | Find existing credential instead of creating |
| `404 Not Found`                   | Credential doesn't exist             | Create the credential first                  |
| `400 INSUFFICIENT_BALANCE`        | Trying to deduct more than available | Check balance before deducting               |
| `400 CANNOT_DELETE_WITH_BALANCES` | Credential has non-zero balance      | Zero out balance or link first               |

## Next Steps

<CardGroup>
  <Card title="Member Management" icon="users" href="/developer/managing-members">
    Learn how to manage verified realm members
  </Card>

  <Card title="Point Systems" icon="coins" href="/developer/point-systems">
    Design effective point economies
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference">
    Explore the complete API documentation
  </Card>
</CardGroup>

# Error Handling

Source: https://docs.drip.re/developer/errors

Complete guide to API errors, status codes, and troubleshooting

This guide covers all aspects of error handling when working with the DRIP API, including common error scenarios, proper error handling techniques, and troubleshooting steps.

## Error Response Format

All DRIP API errors follow a consistent format:

```json theme={"dark"}
{
  "error": "ValidationError",
  "message": "Invalid request parameters",
  "details": {
    "field": "tokens",
    "issue": "Must be a positive integer"
  },
  "requestId": "req_1234567890abcdef",
  "timestamp": "2024-01-20T15:30:00Z"
}
```

### Error Response Fields

| Field       | Description                               |
| ----------- | ----------------------------------------- |
| `error`     | Error type identifier                     |
| `message`   | Human-readable error description          |
| `details`   | Additional error context (when available) |
| `requestId` | Unique request identifier for support     |
| `timestamp` | When the error occurred                   |

## HTTP Status Codes

The DRIP API uses standard HTTP status codes:

### 2xx Success

* **200 OK**: Request successful
* **201 Created**: Resource created successfully
* **204 No Content**: Request successful, no response body

### 4xx Client Errors

* **400 Bad Request**: Invalid request format or parameters
* **401 Unauthorized**: Missing or invalid authentication
* **403 Forbidden**: Valid authentication but insufficient permissions
* **404 Not Found**: Requested resource doesn't exist
* **409 Conflict**: Request conflicts with current resource state
* **422 Unprocessable Entity**: Valid format but business logic error
* **429 Too Many Requests**: Rate limit exceeded

### 5xx Server Errors

* **500 Internal Server Error**: Unexpected server error
* **502 Bad Gateway**: Upstream service error
* **503 Service Unavailable**: Temporary service outage
* **504 Gateway Timeout**: Upstream service timeout

## Common Error Types

### Authentication Errors

<AccordionGroup>
  <Accordion title="401 Unauthorized - Invalid API Key">
    ```json theme={"dark"}
    {
      "error": "Unauthorized",
      "message": "Invalid API key provided"
    }
    ```

    **Causes:**

    * API key is incorrect or malformed
    * API key has been revoked
    * Missing Authorization header

    **Solutions:**

    * Verify your API key is correct
    * Generate a new API key if needed
    * Ensure proper header format: `Authorization: Bearer YOUR_KEY`
  </Accordion>

  <Accordion title="403 Forbidden - Insufficient Permissions">
    ```json theme={"dark"}
    {
      "error": "Forbidden",
      "message": "Insufficient permissions to access this resource"
    }
    ```

    **Causes:**

    * API key lacks required permissions
    * Trying to access another realm's resources
    * Account permissions have been changed

    **Solutions:**

    * Check your account permissions in the dashboard
    * Ensure you're using the correct realm ID
    * Contact an admin to update permissions
  </Accordion>
</AccordionGroup>

### Validation Errors

<AccordionGroup>
  <Accordion title="400 Bad Request - Invalid Parameters">
    ```json theme={"dark"}
    {
      "error": "ValidationError",
      "message": "Invalid request parameters",
      "details": {
        "tokens": "Must be a number between -1000000 and 1000000",
        "realmPointId": "Must be a valid ObjectId"
      }
    }
    ```

    **Common Issues:**

    * Invalid data types (string instead of number)
    * Missing required fields
    * Values outside allowed ranges
    * Malformed IDs

    **Solutions:**

    * Validate input data before sending requests
    * Check API documentation for required fields and formats
    * Use proper data types in your requests
  </Accordion>

  <Accordion title="422 Unprocessable Entity - Business Logic Error">
    ```json theme={"dark"}
    {
      "error": "InsufficientBalance",
      "message": "Member does not have enough points for this operation",
      "details": {
        "currentBalance": 50,
        "requestedAmount": 100,
        "memberId": "507f1f77bcf86cd799439013"
      }
    }
    ```

    **Common Scenarios:**

    * Insufficient point balance for transfers
    * Duplicate resource creation
    * Quest already completed
    * Store item out of stock

    **Solutions:**

    * Check resource state before operations
    * Implement proper business logic validation
    * Handle edge cases gracefully
  </Accordion>
</AccordionGroup>

### Resource Errors

<AccordionGroup>
  <Accordion title="404 Not Found - Resource Missing">
    ```json theme={"dark"}
    {
      "error": "NotFound",
      "message": "Realm member not found",
      "details": {
        "realmId": "507f1f77bcf86cd799439011",
        "memberId": "507f1f77bcf86cd799439013"
      }
    }
    ```

    **Common Causes:**

    * Incorrect resource IDs
    * Resource has been deleted
    * Member hasn't joined the realm
    * Typos in endpoint URLs

    **Solutions:**

    * Verify resource IDs are correct
    * Check if resources exist before operations
    * Handle missing resources gracefully
  </Accordion>

  <Accordion title="409 Conflict - Resource State Conflict">
    ```json theme={"dark"}
    {
      "error": "ConflictError",
      "message": "Quest is already completed and cannot be modified",
      "details": {
        "questId": "507f1f77bcf86cd799439015",
        "currentStatus": "completed"
      }
    }
    ```

    **Common Scenarios:**

    * Modifying completed quests
    * Creating duplicate resources
    * Concurrent modification conflicts

    **Solutions:**

    * Check resource state before modifications
    * Implement proper concurrency handling
    * Use appropriate HTTP methods (PUT vs PATCH)
  </Accordion>
</AccordionGroup>

### Rate Limiting Errors

<AccordionGroup>
  <Accordion title="429 Too Many Requests">
    ```json theme={"dark"}
    {
      "error": "RateLimitExceeded",
      "message": "Too many requests. Try again in 60 seconds.",
      "details": {
        "limit": 100,
        "window": 60,
        "retryAfter": 60
      }
    }
    ```

    **Solutions:**

    * Implement exponential backoff
    * Respect the Retry-After header
    * Use batch operations when possible
    * See the [Rate Limits guide](/developer/rate-limits) for details
  </Accordion>
</AccordionGroup>

## Error Handling Implementation

### JavaScript/Node.js

<CodeGroup>
  ```javascript Comprehensive Error Handler theme={"dark"}
  class DripAPIError extends Error {
    constructor(status, error, message, details, requestId) {
      super(message);
      this.name = 'DripAPIError';
      this.status = status;
      this.error = error;
      this.details = details;
      this.requestId = requestId;
    }
  }

  class DripClient {
    async request(method, endpoint, data = null) {
      try {
        const response = await fetch(`${this.baseUrl}${endpoint}`, {
          method,
          headers: {
            'Authorization': `Bearer ${this.apiKey}`,
            'Content-Type': 'application/json'
          },
          body: data ? JSON.stringify(data) : null
        });

        if (!response.ok) {
          const errorData = await response.json();
          throw new DripAPIError(
            response.status,
            errorData.error,
            errorData.message,
            errorData.details,
            errorData.requestId
          );
        }

        return response.json();
      } catch (error) {
        if (error instanceof DripAPIError) {
          throw error;
        }
        
        // Handle network errors, JSON parsing errors, etc.
        throw new Error(`Network error: ${error.message}`);
      }
    }

    async safeRequest(method, endpoint, data = null, options = {}) {
      const { retries = 3, retryDelay = 1000 } = options;
      
      for (let attempt = 0; attempt <= retries; attempt++) {
        try {
          return await this.request(method, endpoint, data);
        } catch (error) {
          if (error instanceof DripAPIError) {
            // Don't retry client errors (4xx) except rate limits
            if (error.status >= 400 && error.status < 500 && error.status !== 429) {
              throw error;
            }
            
            // Handle rate limits
            if (error.status === 429) {
              const retryAfter = error.details?.retryAfter || 60;
              if (attempt < retries) {
                await this.sleep(retryAfter * 1000);
                continue;
              }
            }
            
            // Retry server errors (5xx)
            if (error.status >= 500 && attempt < retries) {
              await this.sleep(retryDelay * Math.pow(2, attempt));
              continue;
            }
          }
          
          // Final attempt or non-retryable error
          if (attempt === retries) {
            throw error;
          }
        }
      }
    }

    sleep(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
    }
  }

  ```

  ```javascript Usage Example theme={"dark"}
  const client = new DripClient(apiKey, realmId);

  async function updateMemberSafely(memberId, tokens) {
    try {
      const result = await client.safeRequest(
        'PATCH',
        `/realm/${client.realmId}/members/${memberId}/point-balance`,
        { tokens }
      );
      
      console.log('Balance updated successfully:', result);
      return { success: true, data: result };
      
    } catch (error) {
      if (error instanceof DripAPIError) {
        console.error(`API Error [${error.status}]:`, error.message);
        
        switch (error.error) {
          case 'NotFound':
            return { success: false, error: 'Member not found' };
          case 'InsufficientBalance':
            return { success: false, error: 'Not enough points' };
          case 'ValidationError':
            return { success: false, error: 'Invalid input data' };
          default:
            return { success: false, error: 'API error occurred' };
        }
      } else {
        console.error('Network error:', error.message);
        return { success: false, error: 'Network error' };
      }
    }
  }
  ```

</CodeGroup>

### Python

<CodeGroup>
  ```python Error Handling Class theme={"dark"}
  import requests
  import time
  from typing import Optional, Dict, Any

  class DripAPIError(Exception):
      def **init**(self, status: int, error: str, message: str, details: Optional[Dict] = None, request_id: Optional[str] = None):
          super().**init**(message)
          self.status = status
          self.error = error
          self.message = message
          self.details = details or {}
          self.request_id = request_id

  class DripClient:
      def **init**(self, api_key: str, realm_id: str):
          self.api_key = api_key
          self.realm_id = realm_id
          self.base_url = 'https://api.drip.re/api/v1'
          self.session = requests.Session()
          self.session.headers.update({
              'Authorization': f'Bearer {api_key}',
              'Content-Type': 'application/json'
          })

      def request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict[Any, Any]:
          try:
              response = self.session.request(method, f"{self.base_url}{endpoint}", json=data)
              
              if not response.ok:
                  try:
                      error_data = response.json()
                  except ValueError:
                      error_data = {'error': 'UnknownError', 'message': 'Unknown error occurred'}
                  
                  raise DripAPIError(
                      status=response.status_code,
                      error=error_data.get('error', 'UnknownError'),
                      message=error_data.get('message', 'Unknown error'),
                      details=error_data.get('details'),
                      request_id=error_data.get('requestId')
                  )
              
              return response.json()
              
          except requests.exceptions.RequestException as e:
              raise Exception(f"Network error: {str(e)}")

      def safe_request(self, method: str, endpoint: str, data: Optional[Dict] = None, retries: int = 3, retry_delay: int = 1) -> Dict[Any, Any]:
          for attempt in range(retries + 1):
              try:
                  return self.request(method, endpoint, data)
                  
              except DripAPIError as e:
                  # Don't retry client errors except rate limits
                  if 400 <= e.status < 500 and e.status != 429:
                      raise e
                  
                  # Handle rate limits
                  if e.status == 429:
                      retry_after = e.details.get('retryAfter', 60)
                      if attempt < retries:
                          time.sleep(retry_after)
                          continue
                  
                  # Retry server errors
                  if e.status >= 500 and attempt < retries:
                      time.sleep(retry_delay * (2 ** attempt))
                      continue
                  
                  # Final attempt
                  if attempt == retries:
                      raise e
                      
              except Exception as e:
                  if attempt == retries:
                      raise e
                  time.sleep(retry_delay * (2 ** attempt))

  ```

  ```python Usage Example theme={"dark"}
  def update_member_safely(client: DripClient, member_id: str, tokens: int) -> Dict[str, Any]:
      try:
          result = client.safe_request(
              'PATCH',
              f'/realm/{client.realm_id}/members/{member_id}/point-balance',
              {'tokens': tokens}
          )
          
          print('Balance updated successfully:', result)
          return {'success': True, 'data': result}
          
      except DripAPIError as e:
          print(f"API Error [{e.status}]: {e.message}")
          
          error_mapping = {
              'NotFound': 'Member not found',
              'InsufficientBalance': 'Not enough points',
              'ValidationError': 'Invalid input data'
          }
          
          error_message = error_mapping.get(e.error, 'API error occurred')
          return {'success': False, 'error': error_message}
          
      except Exception as e:
          print('Network error:', str(e))
          return {'success': False, 'error': 'Network error'}
  ```

</CodeGroup>

## Debugging and Troubleshooting

### Request ID Tracking

Always log the `requestId` from error responses for support:

```javascript theme={"dark"}
function logError(error) {
  if (error instanceof DripAPIError) {
    console.error(`[${error.requestId}] ${error.error}: ${error.message}`);
    if (error.details) {
      console.error('Details:', JSON.stringify(error.details, null, 2));
    }
  }
}
```

### Common Debugging Steps

<Steps>
  <Step title="Verify API Key">
    Test your API key with a simple request:

    ```bash theme={"dark"}
    curl -X GET "https://api.drip.re/api/v1/realms/YOUR_REALM_ID" \
      -H "Authorization: Bearer YOUR_API_KEY" \
      -w "\nStatus: %{http_code}\n"
    ```
  </Step>

  <Step title="Check Request Format">
    Ensure your request matches the API documentation:

    * Correct HTTP method
    * Proper JSON format
    * Required headers included
    * Valid parameter types
  </Step>

  <Step title="Validate Resource IDs">
    Confirm that all IDs in your request are valid:

    * Realm ID exists and you have access
    * Member ID exists in the realm
    * Point type ID is correct
  </Step>

  <Step title="Test with cURL">
    Replicate the failing request with cURL to isolate the issue:

    ```bash theme={"dark"}
    curl -X PATCH "https://api.drip.re/api/v1/realm/REALM_ID/members/MEMBER_ID/point-balance" \
      -H "Authorization: Bearer YOUR_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{"tokens": 100}' \
      -v
    ```
  </Step>
</Steps>

### Error Monitoring

Set up monitoring to track error patterns:

```javascript theme={"dark"}
class ErrorMonitor {
  constructor() {
    this.errors = [];
  }

  recordError(error, context = {}) {
    this.errors.push({
      timestamp: new Date().toISOString(),
      status: error.status,
      error: error.error,
      message: error.message,
      requestId: error.requestId,
      context
    });

    // Alert on high error rates
    this.checkErrorRate();
  }

  checkErrorRate() {
    const recentErrors = this.errors.filter(
      e => Date.now() - new Date(e.timestamp).getTime() < 300000 // Last 5 minutes
    );

    if (recentErrors.length > 10) {
      console.warn('High error rate detected:', recentErrors.length, 'errors in 5 minutes');
      // Send alert to monitoring system
    }
  }

  getErrorStats() {
    const last24h = this.errors.filter(
      e => Date.now() - new Date(e.timestamp).getTime() < 86400000
    );

    const errorCounts = last24h.reduce((acc, error) => {
      acc[error.error] = (acc[error.error] || 0) + 1;
      return acc;
    }, {});

    return {
      total: last24h.length,
      byType: errorCounts,
      recent: last24h.slice(-10)
    };
  }
}
```

## Best Practices

<CardGroup>
  <Card title="Graceful Degradation" icon="shield-check">
    * Always handle errors gracefully
    * Provide meaningful user feedback
    * Implement fallback behaviors
    * Log errors for debugging
  </Card>

  <Card title="Retry Logic" icon="arrows-rotate">
    * Implement exponential backoff
    * Don't retry client errors (4xx)
    * Respect rate limit headers
    * Set maximum retry limits
  </Card>

  <Card title="Error Logging" icon="file-text">
    * Log all API errors with context
    * Include request IDs for support
    * Monitor error patterns
    * Set up alerting for high error rates
  </Card>

  <Card title="User Experience" icon="heart">
    * Show user-friendly error messages
    * Provide actionable next steps
    * Handle loading and error states
    * Implement proper error boundaries
  </Card>
</CardGroup>

## Getting Help

When contacting support about API errors:

1. **Include the Request ID** from the error response
2. **Provide the full error response** with status code
3. **Share your request details** (without sensitive data)
4. **Describe the expected behavior** vs what happened
5. **Include relevant logs** and timestamps

<CardGroup>
  <Card title="Discord Support" icon="discord" href="https://discord.gg/dripchain">
    Join our community for help and discussions
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference">
    Check the complete API documentation
  </Card>
</CardGroup>

# Code Examples

Source: https://docs.drip.re/developer/examples

Copy-paste code for common DRIP API tasks 📋

Ready-to-use code snippets for the most common DRIP API tasks. Just copy, paste, and customize! 🚀

<Info>
  **New to APIs?** Each example includes error handling and comments explaining what's happening. Perfect for learning!
</Info>

## Setup & Authentication

### Basic API Client Setup

<Tabs>
  <Tab title="JavaScript">
    ```javascript theme={"dark"}
    class DripClient {
      constructor(apiKey, realmId) {
        this.apiKey = apiKey;
        this.realmId = realmId;
        this.baseUrl = 'https://api.drip.re/api/v1';
      }

      async request(method, endpoint, data = null) {
        const url = `${this.baseUrl}${endpoint}`;
        const options = {
          method,
          headers: {
            'Authorization': `Bearer ${this.apiKey}`,
            'Content-Type': 'application/json'
          }
        };

        if (data) {
          options.body = JSON.stringify(data);
        }

        try {
          const response = await fetch(url, options);
          
          if (!response.ok) {
            const error = await response.json();
            throw new Error(`API Error: ${response.status} - ${error.message || 'Unknown error'}`);
          }

          return response.json();
        } catch (error) {
          console.error('DRIP API Error:', error);
          throw error;
        }
      }
    }

    // Usage
    const client = new DripClient('your_api_key', 'your_realm_id');
    ```
  </Tab>

  <Tab title="Python">
    ```python theme={"dark"}
    import requests
    import json

    class DripClient:
        def __init__(self, api_key, realm_id):
            self.api_key = api_key
            self.realm_id = realm_id
            self.base_url = 'https://api.drip.re/api/v1'
            self.session = requests.Session()
            self.session.headers.update({
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            })

        def request(self, method, endpoint, data=None):
            url = f"{self.base_url}{endpoint}"
            
            try:
                response = self.session.request(method, url, json=data)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.HTTPError as e:
                print(f'DRIP API Error: {e}')
                raise
            except Exception as e:
                print(f'Request failed: {e}')
                raise

    # Usage
    client = DripClient('your_api_key', 'your_realm_id')
    ```
  </Tab>

  <Tab title="cURL">
    ```bash theme={"dark"}
    # Set your variables
    DRIP_API_KEY="your_api_key_here"
    REALM_ID="your_realm_id_here"
    BASE_URL="https://api.drip.re/api/v1"

    # Function to make API calls
    drip_api() {
      local method=$1
      local endpoint=$2
      local data=$3
      
      if [ -n "$data" ]; then
        curl -s -X "$method" "$BASE_URL$endpoint" \
          -H "Authorization: Bearer $DRIP_API_KEY" \
          -H "Content-Type: application/json" \
          -d "$data"
      else
        curl -s -X "$method" "$BASE_URL$endpoint" \
          -H "Authorization: Bearer $DRIP_API_KEY"
      fi
    }

    # Usage
    # drip_api GET "/realms/$REALM_ID"
    ```
  </Tab>
</Tabs>

## Member Management

### Search for Members

<Tabs>
  <Tab title="JavaScript">
    ```javascript theme={"dark"}
    // Search by different identifiers
    async function searchMembers(client, searchType, values) {
      const endpoint = `/realm/${client.realmId}/members/search?type=${searchType}&values=${values}`;
      return await client.request('GET', endpoint);
    }

    // Examples
    const client = new DripClient('your_api_key', 'your_realm_id');

    // Search by Discord ID
    const discordMembers = await searchMembers(client, 'discord-id', '123456789012345678');

    // Search by multiple usernames
    const usernameMembers = await searchMembers(client, 'username', 'user1,user2,user3');

    // Search by wallet address
    const walletMembers = await searchMembers(client, 'wallet', '0x742d35Cc6634C0532925a3b8D23');

    // Search by email
    const emailMembers = await searchMembers(client, 'email', 'user@example.com');

    console.log('Found members:', discordMembers.data);
    ```
  </Tab>

  <Tab title="Python">
    ```python theme={"dark"}
    def search_members(client, search_type, values):
        endpoint = f'/realm/{client.realm_id}/members/search?type={search_type}&values={values}'
        return client.request('GET', endpoint)

    # Examples
    client = DripClient('your_api_key', 'your_realm_id')

    # Search by Discord ID
    discord_members = search_members(client, 'discord-id', '123456789012345678')

    # Search by multiple usernames
    username_members = search_members(client, 'username', 'user1,user2,user3')

    # Search by wallet address
    wallet_members = search_members(client, 'wallet', '0x742d35Cc6634C0532925a3b8D23')

    print(f"Found {len(discord_members.get('data', []))} members")
    ```
  </Tab>

  <Tab title="cURL">
    ```bash theme={"dark"}
    # Search by Discord ID
    drip_api GET "/realm/$REALM_ID/members/search?type=discord-id&values=123456789012345678"

    # Search by multiple usernames
    drip_api GET "/realm/$REALM_ID/members/search?type=username&values=user1,user2,user3"

    # Search by wallet
    drip_api GET "/realm/$REALM_ID/members/search?type=wallet&values=0x742d35Cc6634C0532925a3b8D23"
    ```
  </Tab>
</Tabs>

### Get Member Details

<Tabs>
  <Tab title="JavaScript">
    ```javascript theme={"dark"}
    async function getMemberDetails(client, memberId) {
      // First search for the member to get their full details
      const members = await searchMembers(client, 'drip-id', memberId);

      if (members.data && members.data.length > 0) {
        const member = members.data[0];
        
        return {
          id: member.id,
          name: member.displayName || member.username,
          joinedAt: member.joinedAt,
          lastVisit: member.lastVisit,
          points: member.pointBalances || [],
          credentials: member.credentials || []
        };
      }
      
      throw new Error('Member not found');
    }

    // Usage
    try {
      const member = await getMemberDetails(client, 'member_id_here');
      console.log(`${member.name} has ${member.points[0]?.balance || 0} points`);
    } catch (error) {
      console.error('Member not found:', error.message);
    }
    ```
  </Tab>

  <Tab title="Python">
    ```python theme={"dark"}
    def get_member_details(client, member_id):
        members = search_members(client, 'drip-id', member_id)

        if members.get('data') and len(members['data']) > 0:
            member = members['data'][0]
            
            return {
                'id': member['id'],
                'name': member.get('displayName') or member.get('username'),
                'joined_at': member.get('joinedAt'),
                'last_visit': member.get('lastVisit'),
                'points': member.get('pointBalances', []),
                'credentials': member.get('credentials', [])
            }
        
        raise Exception('Member not found')

    # Usage
    try:
        member = get_member_details(client, 'member_id_here')
        points = member['points'][0]['balance'] if member['points'] else 0
        print(f"{member['name']} has {points} points")
    except Exception as e:
        print(f"Member not found: {e}")
    ```
  </Tab>
</Tabs>

## Points Management

### Award Points to a Member

<Tabs>
  <Tab title="JavaScript">
    ```javascript theme={"dark"}
    async function awardPoints(client, memberId, points, realmPointId = null) {
      const endpoint = `/realm/${client.realmId}/members/${memberId}/point-balance`;
      const data = { tokens: points };

      if (realmPointId) {
        data.realmPointId = realmPointId;
      }
      
      return await client.request('PATCH', endpoint, data);
    }

    // Examples
    const client = new DripClient('your_api_key', 'your_realm_id');

    // Award 100 points (default currency)
    const result = await awardPoints(client, 'member_id', 100);
    console.log('Points awarded:', result);

    // Award points to specific currency
    const specificResult = await awardPoints(client, 'member_id', 50, 'specific_point_id');

    // Deduct points (negative number)
    const deductResult = await awardPoints(client, 'member_id', -25);
    ```
  </Tab>

  <Tab title="Python">
    ```python theme={"dark"}
    def award_points(client, member_id, points, realm_point_id=None):
        endpoint = f'/realm/{client.realm_id}/members/{member_id}/point-balance'
        data = {'tokens': points}

        if realm_point_id:
            data['realmPointId'] = realm_point_id
        
        return client.request('PATCH', endpoint, data)

    # Examples
    client = DripClient('your_api_key', 'your_realm_id')

    # Award 100 points
    result = award_points(client, 'member_id', 100)
    print('Points awarded:', result)

    # Deduct 25 points
    deduct_result = award_points(client, 'member_id', -25)
    ```
  </Tab>

  <Tab title="cURL">
    ```bash theme={"dark"}
    # Award 100 points
    drip_api PATCH "/realm/$REALM_ID/members/MEMBER_ID/point-balance" '{"tokens": 100}'

    # Award points to specific currency
    drip_api PATCH "/realm/$REALM_ID/members/MEMBER_ID/point-balance" '{"tokens": 50, "realmPointId": "POINT_ID"}'

    # Deduct points
    drip_api PATCH "/realm/$REALM_ID/members/MEMBER_ID/point-balance" '{"tokens": -25}'
    ```
  </Tab>
</Tabs>

### Batch Update Multiple Members

<Tabs>
  <Tab title="JavaScript">
    ```javascript theme={"dark"}
    async function batchUpdatePoints(client, updates) {
      const endpoint = `/realm/${client.realmId}/members/transaction`;
      return await client.request('PATCH', endpoint, { updates });
    }

    // Example: Award points to multiple members
    const updates = [
      { memberId: 'member_1', tokens: 100 },
      { memberId: 'member_2', tokens: 150 },
      { memberId: 'member_3', tokens: 75, realmPointId: 'specific_point_id' }
    ];

    const batchResult = await batchUpdatePoints(client, updates);
    console.log('Batch update result:', batchResult);

    // Example: Weekly point distribution
    async function weeklyPointDistribution(client, memberIds, basePoints = 50) {
      const updates = memberIds.map(memberId => ({
        memberId,
        tokens: basePoints + Math.floor(Math.random() * 50) // 50-100 points
      }));
      
      return await batchUpdatePoints(client, updates);
    }
    ```
  </Tab>

  <Tab title="Python">
    ```python theme={"dark"}
    def batch_update_points(client, updates):
        endpoint = f'/realm/{client.realm_id}/members/transaction'
        return client.request('PATCH', endpoint, {'updates': updates})

    # Example: Award points to multiple members
    updates = [
        {'memberId': 'member_1', 'tokens': 100},
        {'memberId': 'member_2', 'tokens': 150},
        {'memberId': 'member_3', 'tokens': 75, 'realmPointId': 'specific_point_id'}
    ]

    batch_result = batch_update_points(client, updates)
    print('Batch update result:', batch_result)

    # Weekly distribution function
    def weekly_point_distribution(client, member_ids, base_points=50):
        import random
        updates = [
            {
                'memberId': member_id,
                'tokens': base_points + random.randint(0, 50)
            }
            for member_id in member_ids
        ]
        return batch_update_points(client, updates)
    ```
  </Tab>
</Tabs>

### Transfer Points Between Members

<Tabs>
  <Tab title="JavaScript">
    ```javascript theme={"dark"}
    async function transferPoints(client, senderId, recipientId, amount, realmPointId) {
      const endpoint = `/realm/${client.realmId}/members/${senderId}/transfer`;
      const data = {
        tokens: amount,
        recipientId: recipientId,
        realmPointId: realmPointId
      };

      return await client.request('PATCH', endpoint, data);
    }

    // Example: Transfer 100 points from one member to another
    const transfer = await transferPoints(
      client,
      'sender_member_id',
      'recipient_member_id', 
      100,
      'realm_point_id'
    );

    console.log('Transfer successful:', transfer);
    ```
  </Tab>

  <Tab title="Python">
    ```python theme={"dark"}
    def transfer_points(client, sender_id, recipient_id, amount, realm_point_id):
        endpoint = f'/realm/{client.realm_id}/members/{sender_id}/transfer'
        data = {
            'tokens': amount,
            'recipientId': recipient_id,
            'realmPointId': realm_point_id
        }
        return client.request('PATCH', endpoint, data)

    # Example usage
    transfer = transfer_points(
        client,
        'sender_member_id',
        'recipient_member_id',
        100,
        'realm_point_id'
    )
    print('Transfer successful:', transfer)
    ```
  </Tab>
</Tabs>

## Common Patterns

### Find and Reward Active Members

<Tabs>
  <Tab title="JavaScript">
    ```javascript theme={"dark"}
    async function rewardActiveMembers(client, minPoints = 0, reward = 50) {
      // Get all members
      const allMembers = await searchMembers(client, 'drip-id', 'all');

      // Filter active members (you can customize this logic)
      const activeMembers = allMembers.data.filter(member => {
        const points = member.pointBalances[0]?.balance || 0;
        const lastVisit = new Date(member.lastVisit);
        const weekAgo = new Date(Date.now() - 7 * 24 * 60 * 60 * 1000);
        
        return points >= minPoints && lastVisit > weekAgo;
      });

      // Prepare batch update
      const updates = activeMembers.map(member => ({
        memberId: member.id,
        tokens: reward
      }));

      if (updates.length > 0) {
        const result = await batchUpdatePoints(client, updates);
        console.log(`Rewarded ${updates.length} active members with ${reward} points each`);
        return result;
      } else {
        console.log('No active members found to reward');
        return null;
      }
    }

    // Usage
    await rewardActiveMembers(client, 100, 75); // Reward members with 100+ points who visited in last week
    ```
  </Tab>

  <Tab title="Python">
    ```python theme={"dark"}
    from datetime import datetime, timedelta

    def reward_active_members(client, min_points=0, reward=50):
        # Get all members
        all_members = search_members(client, 'drip-id', 'all')
        
        # Filter active members
        active_members = []
        week_ago = datetime.now() - timedelta(days=7)
        
        for member in all_members.get('data', []):
            points = member.get('pointBalances', [{}])[0].get('balance', 0)
            last_visit = datetime.fromisoformat(member.get('lastVisit', '').replace('Z', '+00:00'))
            
            if points >= min_points and last_visit > week_ago:
                active_members.append(member)

        # Prepare batch update
        updates = [
            {'memberId': member['id'], 'tokens': reward}
            for member in active_members
        ]

        if updates:
            result = batch_update_points(client, updates)
            print(f"Rewarded {len(updates)} active members with {reward} points each")
            return result
        else:
            print("No active members found to reward")
            return None

    # Usage
    reward_active_members(client, 100, 75)
    ```
  </Tab>
</Tabs>

### Create a Leaderboard

<Tabs>
  <Tab title="JavaScript">
    ```javascript theme={"dark"}
    async function getLeaderboard(client, limit = 10) {
      // Get all members
      const allMembers = await searchMembers(client, 'drip-id', 'all');

      // Filter members with points and sort
      const leaderboard = allMembers.data
        .filter(member => member.pointBalances && member.pointBalances.length > 0)
        .map(member => ({
          id: member.id,
          name: member.displayName || member.username || 'Anonymous',
          points: member.pointBalances[0]?.balance || 0,
          joinedAt: member.joinedAt,
          lastVisit: member.lastVisit
        }))
        .sort((a, b) => b.points - a.points)
        .slice(0, limit)
        .map((member, index) => ({
          ...member,
          rank: index + 1
        }));

      return leaderboard;
    }

    // Usage
    const topMembers = await getLeaderboard(client, 10);
    console.log('Top 10 Members:');
    topMembers.forEach(member => {
      console.log(`${member.rank}. ${member.name}: ${member.points} points`);
    });
    ```
  </Tab>

  <Tab title="Python">
    ```python theme={"dark"}
    def get_leaderboard(client, limit=10):
        # Get all members
        all_members = search_members(client, 'drip-id', 'all')

        # Filter and sort members
        leaderboard = []
        for member in all_members.get('data', []):
            if member.get('pointBalances') and len(member['pointBalances']) > 0:
                leaderboard.append({
                    'id': member['id'],
                    'name': member.get('displayName') or member.get('username') or 'Anonymous',
                    'points': member['pointBalances'][0].get('balance', 0),
                    'joined_at': member.get('joinedAt'),
                    'last_visit': member.get('lastVisit')
                })
        
        # Sort by points and add ranks
        leaderboard = sorted(leaderboard, key=lambda x: x['points'], reverse=True)[:limit]
        for i, member in enumerate(leaderboard):
            member['rank'] = i + 1
        
        return leaderboard

    # Usage
    top_members = get_leaderboard(client, 10)
    print("Top 10 Members:")
    for member in top_members:
        print(f"{member['rank']}. {member['name']}: {member['points']} points")
    ```
  </Tab>
</Tabs>

### Discord Bot Integration

<Tabs>
  <Tab title="JavaScript (Discord.js)">
    ```javascript theme={"dark"}
    const { Client, GatewayIntentBits } = require('discord.js');

    const bot = new Client({
      intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent]
    });

    const dripClient = new DripClient('your_drip_api_key', 'your_realm_id');

    // Award points for messages
    bot.on('messageCreate', async (message) => {
      if (message.author.bot) return;

      try {
        // Find member by Discord ID
        const members = await searchMembers(dripClient, 'discord-id', message.author.id);
        
        if (members.data && members.data.length > 0) {
          const memberId = members.data[0].id;
          
          // Award 5 points per message
          await awardPoints(dripClient, memberId, 5);
          
          // Optional: React to show points were awarded
          await message.react('⭐');
        }
      } catch (error) {
        console.error('Error awarding points:', error);
      }
    });

    // Leaderboard command
    bot.on('messageCreate', async (message) => {
      if (message.content === '!leaderboard') {
        try {
          const leaderboard = await getLeaderboard(dripClient, 5);
          
          const leaderboardText = leaderboard
            .map(member => `${member.rank}. ${member.name}: ${member.points} points`)
            .join('\n');
          
          await message.reply(`🏆 **Top 5 Members:**\n\`\`\`\n${leaderboardText}\n\`\`\``);
        } catch (error) {
          await message.reply('Sorry, I couldn\'t fetch the leaderboard right now.');
        }
      }
    });

    bot.login('your_discord_bot_token');
    ```
  </Tab>

  <Tab title="Python (discord.py)">
    ````python theme={"dark"}
    import discord
    from discord.ext import commands

    bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
    drip_client = DripClient('your_drip_api_key', 'your_realm_id')

    @bot.event
    async def on_message(message):
        if message.author.bot:
            return

        try:
            # Find member by Discord ID
            members = search_members(drip_client, 'discord-id', str(message.author.id))
            
            if members.get('data') and len(members['data']) > 0:
                member_id = members['data'][0]['id']
                
                # Award 5 points per message
                award_points(drip_client, member_id, 5)
                
                # React to show points were awarded
                await message.add_reaction('⭐')
        except Exception as e:
            print(f'Error awarding points: {e}')

        await bot.process_commands(message)

    @bot.command()
    async def leaderboard(ctx):
        try:
            top_members = get_leaderboard(drip_client, 5)
            
            leaderboard_text = '\n'.join([
                f"{member['rank']}. {member['name']}: {member['points']} points"
                for member in top_members
            ])
            
            await ctx.send(f"🏆 **Top 5 Members:**\n```\n{leaderboard_text}\n```")
        except Exception as e:
            await ctx.send("Sorry, I couldn't fetch the leaderboard right now.")

    bot.run('your_discord_bot_token')
    ````
  </Tab>
</Tabs>

## Error Handling Patterns

### Robust Error Handling

<Tabs>
  <Tab title="JavaScript">
    ```javascript theme={"dark"}
    async function safeApiCall(apiCall, fallbackValue = null) {
      try {
        return await apiCall();
      } catch (error) {
        console.error('API call failed:', error.message);

        // Handle specific error types
        if (error.message.includes('401')) {
          console.error('Authentication failed - check your API key');
        } else if (error.message.includes('403')) {
          console.error('Permission denied - check your scopes');
        } else if (error.message.includes('404')) {
          console.error('Resource not found');
        } else if (error.message.includes('429')) {
          console.error('Rate limited - slow down your requests');
        }
        
        return fallbackValue;
      }
    }

    // Usage
    const members = await safeApiCall(
      () => searchMembers(client, 'discord-id', 'invalid_id'),
      { data: [] }
    );
    ```
  </Tab>

  <Tab title="Python">
    ```python theme={"dark"}
    def safe_api_call(api_call, fallback_value=None):
        try:
            return api_call()
        except Exception as e:
            print(f'API call failed: {e}')

            # Handle specific error types
            error_str = str(e).lower()
            if '401' in error_str:
                print('Authentication failed - check your API key')
            elif '403' in error_str:
                print('Permission denied - check your scopes')
            elif '404' in error_str:
                print('Resource not found')
            elif '429' in error_str:
                print('Rate limited - slow down your requests')
            
            return fallback_value

    # Usage
    members = safe_api_call(
        lambda: search_members(client, 'discord-id', 'invalid_id'),
        {'data': []}
    )
    ```
  </Tab>
</Tabs>

## Quick Reference

### Most Common API Calls

```javascript theme={"dark"}
// Authentication & Setup
const client = new DripClient('api_key', 'realm_id');

// Get realm info
const realm = await client.request('GET', `/realms/${client.realmId}`);

// Search members
const members = await searchMembers(client, 'discord-id', 'user_id');

// Award points
await awardPoints(client, 'member_id', 100);

// Get leaderboard
const top10 = await getLeaderboard(client, 10);

// Batch update
await batchUpdatePoints(client, [
  { memberId: 'id1', tokens: 50 },
  { memberId: 'id2', tokens: 75 }
]);
```

### Common Search Types

| Type         | Use Case             | Example Value                   |
| ------------ | -------------------- | ------------------------------- |
| `discord-id` | Find Discord users   | `123456789012345678`            |
| `username`   | Find by display name | `cooluser123`                   |
| `email`      | Find by email        | `user@example.com`              |
| `wallet`     | Find crypto users    | `0x742d35Cc6634C0532925a3b8D23` |
| `twitter-id` | Find Twitter users   | `987654321`                     |
| `drip-id`    | Find by DRIP ID      | `507f1f77bcf86cd799439013`      |

<Info>
  **Need more examples?** Check out our [First App tutorial](/developer/first-app) for a complete working project, or browse the [API Reference](/api-reference) for detailed endpoint documentation.
</Info>

# Build Your First DRIP App

Source: https://docs.drip.re/developer/first-app

Create a Discord Balance Manager to search by Discord ID and manage point balances 💰

Let's build a practical tool! We'll create a Discord Balance Manager that lets you search members by Discord ID and manage their point balances. Perfect first project to get familiar with DRIP. 🚀

## Prerequisites (2 minutes)

<Steps>
  <Step title="Get Your API Key">
    Follow the [quickstart guide](/developer/quickstart) to get your API key and realm ID (found in the dashboard header when your project is selected)
  </Step>

  <Step title="Choose Your Weapon">
    Pick your favorite:

    * **HTML + JavaScript** (runs anywhere, no setup)
    * **Node.js** (if you like npm and stuff)
    * **Python** (if you're into that)
  </Step>
</Steps>

## Discord Balance Manager

Let's build another useful app! This time we'll create a balance management tool that lets you search for users by their Discord ID and manage their point balances.

### What We're Building

A balance management app that:

* 🔍 Search users by Discord ID
* 💰 View current point balances
* ➕ Award or deduct points
* 📝 Add reasons for balance changes
* 🎯 Simple, clean interface

<Info>
  **Perfect for community managers** who need to quickly adjust member balances for events, contests, or corrections!
</Info>

<Warning>
  **🔒 SECURITY WARNING: This example is for learning purposes only!**

  The HTML version below exposes your API key in client-side JavaScript, which is **NOT SAFE for production use**. Anyone can view your API key by inspecting the page source.

  **For production applications:**

* Use server-side code (Node.js, Python, etc.) to keep API keys secure
* Store API keys in environment variables, never in source code
* Implement proper authentication and authorization
* Consider using the [App Client flow](/developer/app-development) for multi-realm applications

  **This tutorial is safe for:**

* Local development and testing
* Learning DRIP API concepts
* Prototyping (with test API keys only)
</Warning>

### HTML + JavaScript Version

<CodeGroup>
  ```html balance-manager.html theme={"dark"}
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>DRIP Balance Manager 💰</title>
      <style>
          * {
              margin: 0;
              padding: 0;
              box-sizing: border-box;
          }

          body {
              font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
              background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
              min-height: 100vh;
              padding: 20px;
          }
          
          .container {
              max-width: 800px;
              margin: 0 auto;
              background: white;
              border-radius: 20px;
              box-shadow: 0 20px 40px rgba(0,0,0,0.1);
              overflow: hidden;
          }
          
          .header {
              background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
              color: white;
              padding: 30px;
              text-align: center;
          }
          
          .header h1 {
              font-size: 2.5em;
              margin-bottom: 10px;
          }
          
          .content {
              padding: 30px;
          }
          
          .search-section {
              background: #f8f9ff;
              padding: 25px;
              border-radius: 15px;
              margin-bottom: 30px;
          }
          
          .form-group {
              margin-bottom: 20px;
          }
          
          .form-group label {
              display: block;
              margin-bottom: 8px;
              font-weight: 600;
              color: #333;
          }
          
          .form-group input, .form-group textarea, .form-group select {
              width: 100%;
              padding: 12px 15px;
              border: 2px solid #e1e5e9;
              border-radius: 10px;
              font-size: 16px;
              transition: border-color 0.3s;
          }
          
          .form-group input:focus, .form-group textarea:focus, .form-group select:focus {
              outline: none;
              border-color: #667eea;
          }
          
          .btn {
              background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
              color: white;
              border: none;
              padding: 12px 25px;
              border-radius: 10px;
              font-size: 16px;
              font-weight: 600;
              cursor: pointer;
              transition: transform 0.2s;
              margin-right: 10px;
              margin-bottom: 10px;
          }
          
          .btn:hover {
              transform: translateY(-2px);
          }
          
          .btn.success {
              background: #28a745;
          }
          
          .btn.danger {
              background: #dc3545;
          }
          
          .user-card {
              background: #f8f9ff;
              padding: 25px;
              border-radius: 15px;
              margin-bottom: 20px;
              border-left: 5px solid #667eea;
          }
          
          .user-info {
              display: flex;
              justify-content: space-between;
              align-items: center;
              margin-bottom: 20px;
          }
          
          .user-details h3 {
              color: #333;
              margin-bottom: 5px;
          }
          
          .user-details p {
              color: #666;
              margin: 2px 0;
          }
          
          .balance-list {
              display: grid;
              grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
              gap: 15px;
              margin-bottom: 20px;
          }
          
          .balance-item {
              background: white;
              padding: 15px;
              border-radius: 10px;
              text-align: center;
              border: 2px solid #e1e5e9;
          }
          
          .balance-amount {
              font-size: 1.5em;
              font-weight: bold;
              color: #667eea;
          }
          
          .balance-name {
              font-size: 0.9em;
              color: #666;
              margin-top: 5px;
          }
          
          .balance-actions {
              display: grid;
              grid-template-columns: 1fr 1fr;
              gap: 15px;
              margin-top: 20px;
          }
          
          .loading {
              text-align: center;
              padding: 40px;
              color: #666;
          }
          
          .error {
              background: #f8d7da;
              color: #721c24;
              padding: 15px;
              border-radius: 10px;
              margin-bottom: 20px;
              border-left: 5px solid #dc3545;
          }
          
          .success {
              background: #d4edda;
              color: #155724;
              padding: 15px;
              border-radius: 10px;
              margin-bottom: 20px;
              border-left: 5px solid #28a745;
          }
          
          .hidden {
              display: none;
          }
          
          @media (max-width: 768px) {
              .user-info {
                  flex-direction: column;
                  align-items: flex-start;
              }
              
              .balance-actions {
                  grid-template-columns: 1fr;
              }
          }
      </style>
  </head>
  <body>
      <div class="container">
          <div class="header">
              <h1>💰 Balance Manager</h1>
              <p>Search and manage member point balances</p>
          </div>

          <div class="content">
              <!-- Search Section -->
              <div class="search-section">
                  <h2>🔍 Find Member by Discord ID</h2>
                  <div class="form-group">
                      <label for="discordId">Discord User ID</label>
                      <input type="text" id="discordId" placeholder="e.g., 123456789012345678">
                      <small style="color: #666; font-size: 0.9em;">Right-click a user in Discord → Copy User ID</small>
                  </div>
                  <button class="btn" onclick="searchUser()">Search Member</button>
              </div>
              
              <!-- Loading State -->
              <div id="loading" class="loading hidden">
                  <h3>🔍 Searching for member...</h3>
              </div>
              
              <!-- Error Message -->
              <div id="error" class="error hidden">
                  <h4>❌ Error</h4>
                  <p id="error-message"></p>
              </div>
              
              <!-- Success Message -->
              <div id="success" class="success hidden">
                  <h4>✅ Success</h4>
                  <p id="success-message"></p>
              </div>
              
              <!-- User Details -->
              <div id="user-section" class="hidden">
                  <div class="user-card">
                      <div class="user-info">
                          <div class="user-details">
                              <h3 id="user-name">Loading...</h3>
                              <p><strong>Discord ID:</strong> <span id="user-discord-id"></span></p>
                              <p><strong>Member Since:</strong> <span id="user-joined"></span></p>
                          </div>
                      </div>
                      
                      <h4>💰 Current Balances</h4>
                      <div id="balance-list" class="balance-list">
                          <!-- Balances will be populated here -->
                      </div>
                      
                      <div class="balance-actions">
                          <div>
                              <h4>➕ Award Points</h4>
                              <div class="form-group">
                                  <select id="award-currency">
                                      <!-- Options populated dynamically -->
                                  </select>
                              </div>
                              <div class="form-group">
                                  <input type="number" id="award-amount" placeholder="Amount to award" min="1">
                              </div>
                              <div class="form-group">
                                  <input type="text" id="award-reason" placeholder="Reason (optional)">
                              </div>
                              <button class="btn success" onclick="awardPoints()">Award Points</button>
                          </div>
                          
                          <div>
                              <h4>➖ Deduct Points</h4>
                              <div class="form-group">
                                  <select id="deduct-currency">
                                      <!-- Options populated dynamically -->
                                  </select>
                              </div>
                              <div class="form-group">
                                  <input type="number" id="deduct-amount" placeholder="Amount to deduct" min="1">
                              </div>
                              <div class="form-group">
                                  <input type="text" id="deduct-reason" placeholder="Reason (optional)">
                              </div>
                              <button class="btn danger" onclick="deductPoints()">Deduct Points</button>
                          </div>
                      </div>
                  </div>
              </div>
          </div>
      </div>

           <script>
           // 🔥 CONFIGURE THESE WITH YOUR ACTUAL VALUES
           // ⚠️  WARNING: Never expose API keys in client-side code in production!
           // This is only safe for local development and learning.
           const DRIP_API_KEY = 'your_client_secret_here';
           const REALM_ID = 'your_realm_id_here';
           const API_BASE = 'https://api.drip.re/api/v1';
          
          let currentUser = null;
          let realmCurrencies = [];

          // Search for user by Discord ID
          async function searchUser() {
              const discordId = document.getElementById('discordId').value.trim();
              
              if (!discordId) {
                  showError('Please enter a Discord ID');
                  return;
              }
              
              showLoading(true);
              hideMessages();
              hideUserSection();
              
              try {
                  // Search for member by Discord ID
                  const response = await fetch(`${API_BASE}/realm/${REALM_ID}/members/search?type=discord&value=${discordId}`, {
                      headers: {
                          'Authorization': `Bearer ${DRIP_API_KEY}`,
                          'Content-Type': 'application/json'
                      }
                  });
                  
                  if (!response.ok) {
                      const error = await response.json();
                      throw new Error(error.message || 'Failed to search for member');
                  }
                  
                  const data = await response.json();
                  
                  if (!data.data || data.data.length === 0) {
                      throw new Error('No member found with that Discord ID');
                  }
                  
                  currentUser = data.data[0];
                  await loadRealmCurrencies();
                  displayUser(currentUser);
                  
              } catch (error) {
                  console.error('Search error:', error);
                  showError(error.message);
              } finally {
                  showLoading(false);
              }
          }
          
          // Load realm currencies for dropdowns
          async function loadRealmCurrencies() {
              try {
                  const response = await fetch(`${API_BASE}/realm/${REALM_ID}/points`, {
                      headers: {
                          'Authorization': `Bearer ${DRIP_API_KEY}`,
                          'Content-Type': 'application/json'
                      }
                  });
                  
                  if (!response.ok) {
                      throw new Error('Failed to load currencies');
                  }
                  
                  const data = await response.json();
                  realmCurrencies = data.data || [];
                  
                  populateCurrencyDropdowns();
                  
              } catch (error) {
                  console.error('Failed to load currencies:', error);
                  // Use fallback if available from user balance
                  if (currentUser && currentUser.pointBalances) {
                      realmCurrencies = currentUser.pointBalances.map(balance => balance.realmPoint);
                      populateCurrencyDropdowns();
                  }
              }
          }
          
          // Populate currency dropdown options
          function populateCurrencyDropdowns() {
              const awardSelect = document.getElementById('award-currency');
              const deductSelect = document.getElementById('deduct-currency');
              
              // Clear existing options
              awardSelect.innerHTML = '';
              deductSelect.innerHTML = '';
              
              // Add currency options
              realmCurrencies.forEach(currency => {
                  const option1 = document.createElement('option');
                  option1.value = currency.id;
                  option1.textContent = `${currency.emoji || '💰'} ${currency.name}`;
                  awardSelect.appendChild(option1);
                  
                  const option2 = document.createElement('option');
                  option2.value = currency.id;
                  option2.textContent = `${currency.emoji || '💰'} ${currency.name}`;
                  deductSelect.appendChild(option2);
              });
          }
          
          // Display user information
          function displayUser(user) {
              document.getElementById('user-name').textContent = user.displayName || user.username || 'Unknown User';
              document.getElementById('user-discord-id').textContent = user.credentials?.find(c => c.type === 'discord')?.platformId || 'N/A';
              document.getElementById('user-joined').textContent = user.joinedAt ? new Date(user.joinedAt).toLocaleDateString() : 'Unknown';
              
              // Display balances
              const balanceList = document.getElementById('balance-list');
              balanceList.innerHTML = '';
              
              if (user.pointBalances && user.pointBalances.length > 0) {
                  user.pointBalances.forEach(balance => {
                      const balanceItem = document.createElement('div');
                      balanceItem.className = 'balance-item';
                      balanceItem.innerHTML = `
                          <div class="balance-amount">${balance.balance.toLocaleString()}</div>
                          <div class="balance-name">${balance.realmPoint.emoji || '💰'} ${balance.realmPoint.name}</div>
                      `;
                      balanceList.appendChild(balanceItem);
                  });
              } else {
                  balanceList.innerHTML = '<div class="balance-item"><div class="balance-amount">0</div><div class="balance-name">No balances found</div></div>';
              }
              
              showUserSection();
          }
          
          // Award points to user
          async function awardPoints() {
              if (!currentUser) return;
              
              const currencyId = document.getElementById('award-currency').value;
              const amount = parseInt(document.getElementById('award-amount').value);
              const reason = document.getElementById('award-reason').value.trim();
              
              if (!currencyId || !amount || amount <= 0) {
                  showError('Please select a currency and enter a valid amount');
                  return;
              }
              
              try {
                  const requestBody = {
                      tokens: amount
                  };
                  
                  if (currencyId) {
                      requestBody.realmPointId = currencyId;
                  }
                  
                  const response = await fetch(`${API_BASE}/realm/${REALM_ID}/members/${currentUser.id}/point-balance`, {
                      method: 'PATCH',
                      headers: {
                          'Authorization': `Bearer ${DRIP_API_KEY}`,
                          'Content-Type': 'application/json'
                      },
                      body: JSON.stringify(requestBody)
                  });
                  
                  if (!response.ok) {
                      const error = await response.json();
                      throw new Error(error.message || 'Failed to award points');
                  }
                  
                  const currency = realmCurrencies.find(c => c.id === currencyId);
                  const currencyName = currency ? `${currency.emoji || '💰'} ${currency.name}` : 'points';
                  
                  showSuccess(`Successfully awarded ${amount} ${currencyName}${reason ? ` for: ${reason}` : ''}!`);
                  
                  // Clear form
                  document.getElementById('award-amount').value = '';
                  document.getElementById('award-reason').value = '';
                  
                  // Refresh user data
                  setTimeout(() => {
                      searchUser();
                  }, 1000);
                  
              } catch (error) {
                  console.error('Award error:', error);
                  showError(error.message);
              }
          }
          
          // Deduct points from user
          async function deductPoints() {
              if (!currentUser) return;
              
              const currencyId = document.getElementById('deduct-currency').value;
              const amount = parseInt(document.getElementById('deduct-amount').value);
              const reason = document.getElementById('deduct-reason').value.trim();
              
              if (!currencyId || !amount || amount <= 0) {
                  showError('Please select a currency and enter a valid amount');
                  return;
              }
              
              try {
                  const requestBody = {
                      tokens: -amount // Negative amount for deduction
                  };
                  
                  if (currencyId) {
                      requestBody.realmPointId = currencyId;
                  }
                  
                  const response = await fetch(`${API_BASE}/realm/${REALM_ID}/members/${currentUser.id}/point-balance`, {
                      method: 'PATCH',
                      headers: {
                          'Authorization': `Bearer ${DRIP_API_KEY}`,
                          'Content-Type': 'application/json'
                      },
                      body: JSON.stringify(requestBody)
                  });
                  
                  if (!response.ok) {
                      const error = await response.json();
                      throw new Error(error.message || 'Failed to deduct points');
                  }
                  
                  const currency = realmCurrencies.find(c => c.id === currencyId);
                  const currencyName = currency ? `${currency.emoji || '💰'} ${currency.name}` : 'points';
                  
                  showSuccess(`Successfully deducted ${amount} ${currencyName}${reason ? ` for: ${reason}` : ''}!`);
                  
                  // Clear form
                  document.getElementById('deduct-amount').value = '';
                  document.getElementById('deduct-reason').value = '';
                  
                  // Refresh user data
                  setTimeout(() => {
                      searchUser();
                  }, 1000);
                  
              } catch (error) {
                  console.error('Deduct error:', error);
                  showError(error.message);
              }
          }
          
          // UI Helper Functions
          function showLoading(show) {
              document.getElementById('loading').classList.toggle('hidden', !show);
          }
          
          function showError(message) {
              document.getElementById('error-message').textContent = message;
              document.getElementById('error').classList.remove('hidden');
              setTimeout(() => {
                  document.getElementById('error').classList.add('hidden');
              }, 5000);
          }
          
          function showSuccess(message) {
              document.getElementById('success-message').textContent = message;
              document.getElementById('success').classList.remove('hidden');
              setTimeout(() => {
                  document.getElementById('success').classList.add('hidden');
              }, 5000);
          }
          
          function hideMessages() {
              document.getElementById('error').classList.add('hidden');
              document.getElementById('success').classList.add('hidden');
          }
          
          function showUserSection() {
              document.getElementById('user-section').classList.remove('hidden');
          }
          
          function hideUserSection() {
              document.getElementById('user-section').classList.add('hidden');
          }
          
          // Allow Enter key to trigger search
          document.getElementById('discordId').addEventListener('keypress', function(e) {
              if (e.key === 'Enter') {
                  searchUser();
              }
          });
      </script>
  </body>
  </html>
  ```
</CodeGroup>

### Key Features Explained

<AccordionGroup>
  <Accordion title="Discord ID Search">
    The app searches for members using their Discord user ID:

    * Uses the `/realm/{realmId}/members/search` endpoint
    * Searches by `type=discord` and the provided Discord ID
    * Returns member details including current point balances
  </Accordion>

  <Accordion title="Multi-Currency Support">
    Handles multiple point currencies in your realm:

    * Fetches available currencies from `/realm/{realmId}/points`
    * Populates dropdown menus for currency selection
    * Displays all current balances with currency names and emojis
  </Accordion>

  <Accordion title="Balance Management">
    Award or deduct points with full control:

    * Uses `/realm/{realmId}/members/{memberId}/point-balance` endpoint
    * Positive values for awards, negative for deductions
    * Optional reason tracking for audit purposes
    * Real-time balance updates after each operation
  </Accordion>
</AccordionGroup>

### How to Get Discord IDs

<Steps>
  <Step title="Enable Developer Mode">
    In Discord: Settings → Advanced → Enable "Developer Mode"
  </Step>

  <Step title="Copy User ID">
    Right-click any user → "Copy User ID"
  </Step>

  <Step title="Use in App">
    Paste the ID into the search field and click "Search Member"
  </Step>
</Steps>

## What's Next? 🚀

Congratulations! You just built your first DRIP app! 🎉

Here are some ideas for your next projects:

<CardGroup>
  <Card title="Points Dashboard" icon="chart-bar">
    Show detailed analytics: points over time, top earners, activity trends
  </Card>

  <Card title="Member Directory" icon="users">
    Searchable member list with profiles, badges, and achievements
  </Card>

  <Card title="Quest Tracker" icon="map">
    Show active quests, completion rates, and member progress
  </Card>

  <Card title="Store Integration" icon="coins">
    Let members spend points on rewards directly from your app
  </Card>
</CardGroup>

### Ready for More Advanced Stuff?

<CardGroup>
  <Card title="Multi-Realm Apps" icon="globe" href="/developer/multi-realm-apps">
    Build apps that work across multiple communities
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference">
    Explore all available endpoints and advanced features
  </Card>
</CardGroup>

<Info>
  **Share your creation!** Built something cool? Show it off in our [Discord community](https://discord.gg/dripchain) and get feedback from other developers! 🚀
</Info>

# Member Management

Source: https://docs.drip.re/developer/managing-members

Search, update, and manage community members like a pro 👥

This guide covers everything you need to know about managing members in your DRIP realm, from searching and retrieving member data to updating balances and transferring points.

## Overview

Member management is one of the most common use cases for the DRIP API. You can:

* Search for members using various identifiers
* Retrieve detailed member information and balances
* Update individual or multiple member point balances
* Transfer points between members
* Track member activity and engagement

## Searching Members

### Search by Different Identifiers

The member search endpoint allows you to find members using various identifiers:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function searchMembers(realmId, searchType, values) {
    const response = await fetch(
      `https://api.drip.re/api/v1/realm/${realmId}/members/search?type=${searchType}&values=${values}`,
      {
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`,
          'Content-Type': 'application/json'
        }
      }
    );

    return response.json();
  }

  // Search by Discord ID
  const discordMembers = await searchMembers('YOUR_REALM_ID', 'discord-id', '123456789012345678');

  // Search by multiple wallet addresses
  const walletMembers = await searchMembers(
    'YOUR_REALM_ID',
    'wallet',
    '0x742d35Cc6634C0532925a3b8D23,0x8ba1f109551bD432803012645Hac136c'
  );

  ```

  ```python Python theme={"dark"}
  import requests

  def search_members(realm_id, search_type, values):
      url = f"https://api.drip.re/api/v1/realm/{realm_id}/members/search"
      
      headers = {
          'Authorization': f'Bearer {os.getenv("DRIP_API_KEY")}',
          'Content-Type': 'application/json'
      }
      
      params = {
          'type': search_type,
          'values': values
      }
      
      response = requests.get(url, headers=headers, params=params)
      return response.json()

  # Search by email
  email_members = search_members('YOUR_REALM_ID', 'email', 'user@example.com')

  # Search by multiple usernames
  username_members = search_members('YOUR_REALM_ID', 'username', 'gamer1,gamer2,gamer3')
  ```

  ```bash cURL theme={"dark"}
  # Search by Discord ID
  curl -X GET "https://api.drip.re/api/v1/realm/YOUR_REALM_ID/members/search?type=discord-id&values=123456789012345678" \
    -H "Authorization: Bearer YOUR_API_KEY"

  # Search by multiple DRIP IDs
  curl -X GET "https://api.drip.re/api/v1/realm/YOUR_REALM_ID/members/search?type=drip-id&values=507f1f77bcf86cd799439013,507f1f77bcf86cd799439014" \
    -H "Authorization: Bearer YOUR_API_KEY"
  ```

</CodeGroup>

### Search Types and Examples

| Search Type  | Description             | Value Format                    |
| ------------ | ----------------------- | ------------------------------- |
| `drip-id`    | Internal DRIP member ID | `507f1f77bcf86cd799439013`      |
| `discord-id` | Discord user ID         | `123456789012345678`            |
| `twitter-id` | Twitter/X user ID       | `987654321`                     |
| `wallet`     | Crypto wallet address   | `0x742d35Cc6634C0532925a3b8D23` |
| `email`      | Email address           | `user@example.com`              |
| `username`   | Display username        | `gamerpro123`                   |

<Info>
  You can search for multiple values at once by separating them with commas. For example: `values=user1,user2,user3`
</Info>

## Updating Member Balances

### Single Member Balance Update

Update a specific member's point balance:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function updateMemberBalance(realmId, memberId, tokens, realmPointId = null) {
    const response = await fetch(
      `https://api.drip.re/api/v1/realm/${realmId}/members/${memberId}/point-balance`,
      {
        method: 'PATCH',
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          tokens: tokens,
          ...(realmPointId && { realmPointId })
        })
      }
    );

    return response.json();
  }

  // Award 100 points to a member
  const result = await updateMemberBalance('YOUR_REALM_ID', 'MEMBER_ID', 100);

  // Award 50 points of a specific currency
  const specificResult = await updateMemberBalance(
    'YOUR_REALM_ID',
    'MEMBER_ID',
    50,
    'REALM_POINT_ID'
  );

  ```

  ```python Python theme={"dark"}
  def update_member_balance(realm_id, member_id, tokens, realm_point_id=None):
      url = f"https://api.drip.re/api/v1/realm/{realm_id}/members/{member_id}/point-balance"
      
      headers = {
          'Authorization': f'Bearer {os.getenv("DRIP_API_KEY")}',
          'Content-Type': 'application/json'
      }
      
      data = {'tokens': tokens}
      if realm_point_id:
          data['realmPointId'] = realm_point_id
      
      response = requests.patch(url, headers=headers, json=data)
      return response.json()

  # Deduct 25 points from a member
  result = update_member_balance('YOUR_REALM_ID', 'MEMBER_ID', -25)
  ```

  ```bash cURL theme={"dark"}
  # Award 100 points
  curl -X PATCH "https://api.drip.re/api/v1/realm/YOUR_REALM_ID/members/MEMBER_ID/point-balance" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"tokens": 100}'

  # Deduct 50 points of specific currency
  curl -X PATCH "https://api.drip.re/api/v1/realm/YOUR_REALM_ID/members/MEMBER_ID/point-balance" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"tokens": -50, "realmPointId": "REALM_POINT_ID"}'
  ```

</CodeGroup>

### Batch Balance Updates

Update multiple members' balances in a single API call:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function batchUpdateBalances(realmId, updates) {
    const response = await fetch(
      `https://api.drip.re/api/v1/realm/${realmId}/members/transaction`,
      {
        method: 'PATCH',
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ updates })
      }
    );

    return response.json();
  }

  // Update multiple members at once
  const updates = [
    { memberId: 'MEMBER_ID_1', tokens: 100 },
    { memberId: 'MEMBER_ID_2', tokens: 150, realmPointId: 'SPECIFIC_POINT_ID' },
    { memberId: 'MEMBER_ID_3', tokens: -25 } // Deduct points
  ];

  const batchResult = await batchUpdateBalances('YOUR_REALM_ID', updates);

  ```

  ```python Python theme={"dark"}
  def batch_update_balances(realm_id, updates):
      url = f"https://api.drip.re/api/v1/realm/{realm_id}/members/transaction"
      
      headers = {
          'Authorization': f'Bearer {os.getenv("DRIP_API_KEY")}',
          'Content-Type': 'application/json'
      }
      
      data = {'updates': updates}
      
      response = requests.patch(url, headers=headers, json=data)
      return response.json()

  # Batch update example
  updates = [
      {'memberId': 'MEMBER_ID_1', 'tokens': 200},
      {'memberId': 'MEMBER_ID_2', 'tokens': 100, 'realmPointId': 'SPECIFIC_POINT_ID'},
      {'memberId': 'MEMBER_ID_3', 'tokens': 75}
  ]

  batch_result = batch_update_balances('YOUR_REALM_ID', updates)
  ```

  ```bash cURL theme={"dark"}
  curl -X PATCH "https://api.drip.re/api/v1/realm/YOUR_REALM_ID/members/transaction" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "updates": [
        {"memberId": "MEMBER_ID_1", "tokens": 100},
        {"memberId": "MEMBER_ID_2", "tokens": 150, "realmPointId": "SPECIFIC_POINT_ID"},
        {"memberId": "MEMBER_ID_3", "tokens": -25}
      ]
    }'
  ```

</CodeGroup>

<Warning>
  Batch updates are atomic - if any single update fails, the entire batch is rolled back. This ensures data consistency.
</Warning>

## Transferring Points Between Members

Transfer points directly from one member to another:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function transferPoints(realmId, senderId, recipientId, tokens, realmPointId) {
    const response = await fetch(
      `https://api.drip.re/api/v1/realm/${realmId}/members/${senderId}/transfer`,
      {
        method: 'PATCH',
        headers: {
          'Authorization': `Bearer ${process.env.DRIP_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          tokens,
          recipientId,
          realmPointId
        })
      }
    );

    return response.json();
  }

  // Transfer 50 points from one member to another
  const transfer = await transferPoints(
    'YOUR_REALM_ID',
    'SENDER_MEMBER_ID',
    'RECIPIENT_MEMBER_ID',
    50,
    'REALM_POINT_ID'
  );

  ```

  ```python Python theme={"dark"}
  def transfer_points(realm_id, sender_id, recipient_id, tokens, realm_point_id):
      url = f"https://api.drip.re/api/v1/realm/{realm_id}/members/{sender_id}/transfer"
      
      headers = {
          'Authorization': f'Bearer {os.getenv("DRIP_API_KEY")}',
          'Content-Type': 'application/json'
      }
      
      data = {
          'tokens': tokens,
          'recipientId': recipient_id,
          'realmPointId': realm_point_id
      }
      
      response = requests.patch(url, headers=headers, json=data)
      return response.json()

  # Transfer example
  transfer = transfer_points(
      'YOUR_REALM_ID',
      'SENDER_MEMBER_ID',
      'RECIPIENT_MEMBER_ID',
      100,
      'REALM_POINT_ID'
  )
  ```

  ```bash cURL theme={"dark"}
  curl -X PATCH "https://api.drip.re/api/v1/realm/YOUR_REALM_ID/members/SENDER_MEMBER_ID/transfer" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "tokens": 50,
      "recipientId": "RECIPIENT_MEMBER_ID",
      "realmPointId": "REALM_POINT_ID"
    }'
  ```

</CodeGroup>

## Common Use Cases

### Activity-Based Rewards

Automatically reward members for various activities:

```javascript theme={"dark"}
// Reward system for different activities
const ACTIVITY_REWARDS = {
  'message_sent': 5,
  'reaction_added': 2,
  'voice_join': 10,
  'quest_completed': 100,
  'referral_successful': 250
};

async function rewardActivity(realmId, memberId, activityType) {
  const points = ACTIVITY_REWARDS[activityType];
  if (!points) return null;
  
  return updateMemberBalance(realmId, memberId, points);
}

// Usage in Discord bot or webhook handler
await rewardActivity('YOUR_REALM_ID', 'MEMBER_ID', 'message_sent');
```

### Leaderboard Generation

Create leaderboards by fetching and sorting member data:

```javascript theme={"dark"}
async function generateLeaderboard(realmId, limit = 10) {
  // This would typically involve fetching multiple members
  // and sorting by their point balances
  const members = await searchMembers(realmId, 'drip-id', 'all'); // Pseudo-code
  
  return members
    .sort((a, b) => b.pointBalances[0].balance - a.pointBalances[0].balance)
    .slice(0, limit)
    .map((member, index) => ({
      rank: index + 1,
      username: member.username,
      points: member.pointBalances[0].balance
    }));
}
```

### Member Onboarding

Set up new members with welcome bonuses:

```javascript theme={"dark"}
async function onboardNewMember(realmId, memberId) {
  const welcomeBonus = 100;
  const result = await updateMemberBalance(realmId, memberId, welcomeBonus);
  
  console.log(`Welcomed new member with ${welcomeBonus} points!`);
  return result;
}
```

## Error Handling

Handle common errors when managing members:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function safeUpdateBalance(realmId, memberId, tokens) {
    try {
      const result = await updateMemberBalance(realmId, memberId, tokens);
      return { success: true, data: result };
    } catch (error) {
      if (error.status === 404) {
        return { success: false, error: 'Member not found' };
      } else if (error.status === 400) {
        return { success: false, error: 'Invalid request data' };
      } else if (error.status === 403) {
        return { success: false, error: 'Insufficient permissions' };
      }

      return { success: false, error: 'Unknown error occurred' };
    }
  }

  ```

  ```python Python theme={"dark"}
  def safe_update_balance(realm_id, member_id, tokens):
      try:
          result = update_member_balance(realm_id, member_id, tokens)
          return {'success': True, 'data': result}
      except requests.exceptions.HTTPError as e:
          if e.response.status_code == 404:
              return {'success': False, 'error': 'Member not found'}
          elif e.response.status_code == 400:
              return {'success': False, 'error': 'Invalid request data'}
          elif e.response.status_code == 403:
              return {'success': False, 'error': 'Insufficient permissions'}
          else:
              return {'success': False, 'error': 'Unknown error occurred'}
  ```

</CodeGroup>

## Best Practices

<CardGroup>
  <Card title="Efficient Searching" icon="magnifying-glass">
    * Use specific search types when possible
    * Batch multiple searches together
    * Cache frequently accessed member data
    * Implement pagination for large result sets
  </Card>

  <Card title="Balance Management" icon="scale-balanced">
    * Always validate point amounts before updates
    * Use batch operations for multiple updates
    * Implement transaction logs for audit trails
    * Handle insufficient balance scenarios gracefully
  </Card>

  <Card title="Performance" icon="gauge-high">
    * Use batch endpoints for bulk operations
    * Implement rate limiting in your application
    * Cache member data to reduce API calls
    * Monitor API response times
  </Card>

  <Card title="Security" icon="shield-check">
    * Validate all input parameters
    * Implement proper error handling
    * Log all balance changes for auditing
    * Use least-privilege API keys
  </Card>
</CardGroup>

## Next Steps

<CardGroup>
  <Card title="Point Systems" icon="coins" href="/developer/point-systems">
    Learn advanced point management and currency systems
  </Card>

  <Card title="Ghost Credentials" icon="ghost" href="/developer/credentials">
    Manage points for users before they become members
  </Card>

  <Card title="Quest Management" icon="map" href="/developer/quest-integration">
    Create engaging gamified experiences for members
  </Card>

  <Card title="Webhooks" icon="webhook" href="/developer/webhooks">
    Set up real-time notifications for member activities
  </Card>
</CardGroup>

<Info>
  **Need to manage users who haven't joined yet?** Use [Ghost Credentials](/developer/credentials) to pre-credit points to Twitter followers, wallet holders, or email addresses before they connect to your realm.
</Info>

# Multi-Realm Apps

Source: https://docs.drip.re/developer/multi-realm-apps

Build applications that work across multiple DRIP communities 🌐

Learn how to build applications that can serve multiple DRIP communities simultaneously. This guide covers the technical and business aspects of multi-realm app development.

## Overview

Multi-realm apps are applications that can be authorized and used by multiple DRIP communities. Unlike realm clients that are tied to a single community, multi-realm apps can scale across the entire DRIP ecosystem.

<Info>
  This guide covers app creation, publishing, realm authorization, scopes, and distribution for DRIP Apps.
</Info>

## App Development Lifecycle

```mermaid theme={"dark"}
graph TD;
  A[Create App] --> B[Develop & Test];
  B --> C[Publish];
  C --> D[Realm Authorization];
  D --> E[Active Usage];
  B --> B1[Local Testing];
  B --> B2[Sandbox];
  C --> L[Request App Store Listing];
  L --> V[Manual Verification];
  V --> S[App Store Listing];
```

## Creating Your App

### 1. Access the Developer Portal

<Steps>
  <Step title="Navigate to Developer Portal">
    Go to **Admin** > **Developer** in your DRIP dashboard
  </Step>

  <Step title="Switch to Drip Apps Tab">
    Click on the **Drip Apps** tab to manage your applications
  </Step>

  <Step title="Submit New App">
    Click **Submit New App** to start the creation process
  </Step>
</Steps>

### 2. App Configuration

<Info>
  You can create an API client and start building/testing your app before publishing. While your app is not published, its API client only works on your own realm. To allow other realms to authorize and use your app, you must publish it. Publishing enables other realms to authorize your app. App Store listing happens after manual verification via email to [dev@drip.re](mailto:dev@drip.re).
</Info>

When creating your app, you'll need to provide:

```json theme={"dark"}
{
  "name": "My Awesome App",
  "description": "A comprehensive tool for community engagement",
  "category": "productivity",
  "website": "https://myapp.com",
  "supportUrl": "https://myapp.com/support",
  "privacyPolicy": "https://myapp.com/privacy",
  "termsOfService": "https://myapp.com/terms",
  "logoUrl": "https://myapp.com/logo.png",
  "screenshots": [
    "https://myapp.com/screenshot1.png",
    "https://myapp.com/screenshot2.png"
  ],
  "requestedScopes": [
    "realm:read",
    "members:read",
    "members:write",
    "points:write"
  ]
}
```

## Key Differences from Single-Realm Apps

<CardGroup>
  <Card title="Single-Realm Apps" icon="castle">
    * Fixed realm context
    * Direct API key access
    * Immediate deployment
    * Simple authorization
  </Card>

  <Card title="Multi-Realm Apps" icon="globe">
    * Dynamic realm context
    * App client credentials
    * Publishing required for cross-realm authorization
    * Complex authorization flow
  </Card>
</CardGroup>

## Authorization Architecture

### Realm-Level Authorization

Publishing your app enables cross-realm authorization. Each realm admin authorizes your app and grants scopes for their realm.

```mermaid theme={"dark"}
graph TD;
  A[Publish App] --> B[Realm Admin Reviews Scopes];
  B --> C[Authorize App for Realm];
  C --> D[App Receives Approved Scopes];
  D --> E[App Accesses Realm Endpoints];
```

### Managing Authorized Realms

```javascript theme={"dark"}
class MultiRealmAppClient {
  constructor(appClientSecret) {
    this.appClientSecret = appClientSecret;
    this.authorizedRealms = new Map();
    this.baseUrl = 'https://api.drip.re/api/v1';
  }

  async loadAuthorizedRealms() {
    const response = await fetch(`${this.baseUrl}/apps/:appId/authorized-realms`, {
      headers: {
        'Authorization': `Bearer ${this.appClientSecret}`,
        'Content-Type': 'application/json'
      }
    });

    const data = await response.json();
    
    // Store authorized realms with their permissions
    for (const authorization of data.data) {
      this.authorizedRealms.set(authorization.realmId, {
        realm: authorization.realm,
        approvedScopes: authorization.approvedScopes,
        authorizedAt: authorization.authorizedAt,
        settings: authorization.settings || {}
      });
    }

    return this.authorizedRealms;
  }

  isAuthorizedForRealm(realmId) {
    return this.authorizedRealms.has(realmId);
  }

  hasScope(realmId, scope) {
    const auth = this.authorizedRealms.get(realmId);
    return auth && auth.approvedScopes.includes(scope);
  }

  async makeRealmRequest(realmId, method, endpoint, data = null) {
    if (!this.isAuthorizedForRealm(realmId)) {
      throw new Error(`Not authorized for realm ${realmId}`);
    }

    const url = `${this.baseUrl}${endpoint}`;
    const options = {
      method,
      headers: {
        'Authorization': `Bearer ${this.appClientSecret}`,
        'Content-Type': 'application/json'
      }
    };

    if (data) {
      options.body = JSON.stringify(data);
    }

    const response = await fetch(url, options);
    
    if (!response.ok) {
      const error = await response.json();
      throw new Error(`API Error: ${response.status} - ${error.message}`);
    }

    return response.json();
  }
}
```

## Scopes and Permissions

* Your app selects `requestedScopes`.
* Realms grant those scopes during authorization per realm.
* Changing requested scopes requires realms to reauthorize.
* No platform-level scope approval at this time; all scopes are realm-granted.

## Data Isolation and Management

### Per-Realm Data Storage

Each realm's data should be properly isolated:

```javascript theme={"dark"}
class RealmDataManager {
  constructor(appClient) {
    this.appClient = appClient;
    this.realmData = new Map();
  }

  async initializeRealmData(realmId) {
    if (this.realmData.has(realmId)) {
      return this.realmData.get(realmId);
    }

    // Load realm-specific configuration
    const realmInfo = await this.appClient.makeRealmRequest(
      realmId, 
      'GET', 
      `/realms/${realmId}`
    );

    // Initialize realm data structure
    const realmData = {
      info: realmInfo,
      settings: await this.loadRealmSettings(realmId),
      cache: new Map(),
      lastUpdated: Date.now()
    };

    this.realmData.set(realmId, realmData);
    return realmData;
  }

  async loadRealmSettings(realmId) {
    // Load app-specific settings for this realm
    // This could come from your own database or DRIP's app settings
    return {
      pointsPerAction: 10,
      enableNotifications: true,
      customBranding: {
        primaryColor: '#667eea',
        logo: null
      }
    };
  }

  async updateRealmSettings(realmId, settings) {
    const realmData = await this.initializeRealmData(realmId);
    realmData.settings = { ...realmData.settings, ...settings };
    
    // Persist to your database
    await this.persistRealmSettings(realmId, realmData.settings);
  }

  getRealmData(realmId) {
    return this.realmData.get(realmId);
  }
}
```

### Cross-Realm Analytics

Aggregate data across multiple realms while respecting boundaries:

```javascript theme={"dark"}
class CrossRealmAnalytics {
  constructor(appClient) {
    this.appClient = appClient;
  }

  async getAggregatedStats() {
    const authorizedRealms = this.appClient.authorizedRealms;
    const stats = {
      totalRealms: authorizedRealms.size,
      totalMembers: 0,
      totalPoints: 0,
      realmBreakdown: []
    };

    // Process each realm in parallel
    const realmPromises = Array.from(authorizedRealms.keys()).map(async (realmId) => {
      try {
        if (!this.appClient.hasScope(realmId, 'members:read')) {
          return null; // Skip realms without permission
        }

        const members = await this.appClient.makeRealmRequest(
          realmId,
          'GET',
          `/realm/${realmId}/members/search?type=drip-id&values=all`
        );

        const realmStats = {
          realmId,
          realmName: authorizedRealms.get(realmId).realm.name,
          memberCount: members.data.length,
          totalPoints: members.data.reduce((sum, member) => {
            return sum + (member.pointBalances[0]?.balance || 0);
          }, 0)
        };

        stats.totalMembers += realmStats.memberCount;
        stats.totalPoints += realmStats.totalPoints;

        return realmStats;
      } catch (error) {
        console.error(`Error fetching stats for realm ${realmId}:`, error);
        return null;
      }
    });

    const realmResults = await Promise.all(realmPromises);
    stats.realmBreakdown = realmResults.filter(result => result !== null);

    return stats;
  }

  async getTopMembersAcrossRealms(limit = 10) {
    const authorizedRealms = this.appClient.authorizedRealms;
    const allMembers = [];

    for (const [realmId, auth] of authorizedRealms) {
      if (!this.appClient.hasScope(realmId, 'members:read')) {
        continue;
      }

      try {
        const members = await this.appClient.makeRealmRequest(
          realmId,
          'GET',
          `/realm/${realmId}/members/search?type=drip-id&values=all`
        );

        // Add realm context to each member
        for (const member of members.data) {
          allMembers.push({
            ...member,
            realmId,
            realmName: auth.realm.name
          });
        }
      } catch (error) {
        console.error(`Error fetching members for realm ${realmId}:`, error);
      }
    }

    // Sort by points and return top members
    return allMembers
      .filter(member => member.pointBalances && member.pointBalances.length > 0)
      .sort((a, b) => {
        const aPoints = a.pointBalances[0]?.balance || 0;
        const bPoints = b.pointBalances[0]?.balance || 0;
        return bPoints - aPoints;
      })
      .slice(0, limit)
      .map((member, index) => ({
        rank: index + 1,
        name: member.displayName || member.username,
        points: member.pointBalances[0].balance,
        realmName: member.realmName,
        realmId: member.realmId
      }));
  }
}
```

## User Experience Patterns

### Realm Selection Interface

Create a smooth realm selection experience:

```javascript theme={"dark"}
class RealmSelector {
  constructor(appClient) {
    this.appClient = appClient;
    this.currentRealmId = null;
  }

  async renderRealmSelector() {
    const realms = Array.from(this.appClient.authorizedRealms.values());
    
    return `
      <div class="realm-selector">
        <h3>Select Community</h3>
        <div class="realm-grid">
          ${realms.map(auth => `
            <div class="realm-card" onclick="selectRealm('${auth.realm.id}')">
              <img src="${auth.realm.imageUrl || '/default-realm.png'}" alt="${auth.realm.name}">
              <h4>${auth.realm.name}</h4>
              <p>${auth.realm.memberCount || 0} members</p>
              <div class="scopes">
                ${auth.approvedScopes.slice(0, 3).map(scope => 
                  `<span class="scope-badge">${scope}</span>`
                ).join('')}
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  }

  selectRealm(realmId) {
    if (!this.appClient.isAuthorizedForRealm(realmId)) {
      throw new Error('Not authorized for this realm');
    }

    this.currentRealmId = realmId;
    this.onRealmChanged(realmId);
  }

  onRealmChanged(realmId) {
    // Override this method to handle realm changes
    console.log(`Switched to realm: ${realmId}`);
  }
}
```

### Context-Aware UI

Adapt your UI based on available permissions:

```javascript theme={"dark"}
class ContextAwareUI {
  constructor(appClient, realmId) {
    this.appClient = appClient;
    this.realmId = realmId;
  }

  renderMemberActions() {
    const canRead = this.appClient.hasScope(this.realmId, 'members:read');
    const canWrite = this.appClient.hasScope(this.realmId, 'members:write');
    const canAwardPoints = this.appClient.hasScope(this.realmId, 'points:write');

    if (!canRead) {
      return '<p>No member permissions for this realm</p>';
    }

    return `
      <div class="member-actions">
        ${canRead ? '<button onclick="loadMembers()">View Members</button>' : ''}
        ${canWrite ? '<button onclick="editMember()">Edit Member</button>' : ''}
        ${canAwardPoints ? '<button onclick="awardPoints()">Award Points</button>' : ''}
      </div>
    `;
  }

  renderBasedOnPermissions() {
    const auth = this.appClient.authorizedRealms.get(this.realmId);
    const scopes = auth.approvedScopes;

    const features = {
      analytics: scopes.includes('members:read'),
      pointManagement: scopes.includes('points:write'),
      questManagement: scopes.includes('quests:write'),
      storeManagement: scopes.includes('store:write')
    };

    return `
      <div class="app-features">
        ${features.analytics ? this.renderAnalytics() : ''}
        ${features.pointManagement ? this.renderPointManagement() : ''}
        ${features.questManagement ? this.renderQuestManagement() : ''}
        ${features.storeManagement ? this.renderStoreManagement() : ''}
      </div>
    `;
  }
}
```

## Scaling Considerations

### Database Design

Structure your database to handle multiple realms efficiently:

```sql theme={"dark"}
-- Realm-specific tables
CREATE TABLE realm_settings (
  realm_id VARCHAR(24) PRIMARY KEY,
  app_settings JSONB NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE realm_analytics (
  id SERIAL PRIMARY KEY,
  realm_id VARCHAR(24) NOT NULL,
  metric_name VARCHAR(100) NOT NULL,
  metric_value NUMERIC NOT NULL,
  recorded_at TIMESTAMP DEFAULT NOW(),
  
  INDEX idx_realm_metric (realm_id, metric_name),
  INDEX idx_recorded_at (recorded_at)
);

CREATE TABLE cross_realm_data (
  id SERIAL PRIMARY KEY,
  data_type VARCHAR(50) NOT NULL,
  aggregated_value JSONB NOT NULL,
  realm_count INTEGER NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);
```

### Caching Strategy

Implement realm-aware caching:

```javascript theme={"dark"}
class MultiRealmCache {
  constructor(ttl = 300000) { // 5 minutes
    this.cache = new Map();
    this.ttl = ttl;
  }

  getKey(realmId, type, identifier) {
    return `${realmId}:${type}:${identifier}`;
  }

  set(realmId, type, identifier, data) {
    const key = this.getKey(realmId, type, identifier);
    this.cache.set(key, {
      data,
      timestamp: Date.now()
    });
  }

  get(realmId, type, identifier) {
    const key = this.getKey(realmId, type, identifier);
    const cached = this.cache.get(key);

    if (!cached) {
      return null;
    }

    if (Date.now() - cached.timestamp > this.ttl) {
      this.cache.delete(key);
      return null;
    }

    return cached.data;
  }

  invalidateRealm(realmId) {
    // Remove all cached data for a specific realm
    for (const key of this.cache.keys()) {
      if (key.startsWith(`${realmId}:`)) {
        this.cache.delete(key);
      }
    }
  }

  clear() {
    this.cache.clear();
  }
}
```

## Business Model Considerations

### Pricing Strategies

Different approaches for multi-realm apps:

<AccordionGroup>
  <Accordion title="Per-Realm Pricing">
    Charge based on the number of authorized realms:

    ```javascript theme={"dark"}
    class PerRealmPricing {
      calculatePrice(realmCount) {
        const basePrice = 9.99; // Base price for first realm
        const additionalRealmPrice = 4.99; // Price per additional realm
        
        if (realmCount <= 1) {
          return basePrice;
        }
        
        return basePrice + (realmCount - 1) * additionalRealmPrice;
      }
    }
    ```
  </Accordion>

  <Accordion title="Usage-Based Pricing">
    Charge based on total usage across all realms:

    ```javascript theme={"dark"}
    class UsageBasedPricing {
      calculatePrice(totalApiCalls, totalMembers) {
        const apiCallPrice = 0.001; // $0.001 per API call
        const memberPrice = 0.05; // $0.05 per member per month
        
        return (totalApiCalls * apiCallPrice) + (totalMembers * memberPrice);
      }
    }
    ```
  </Accordion>

  <Accordion title="Feature-Based Pricing">
    Charge based on features used across realms:

    ```javascript theme={"dark"}
    class FeatureBasedPricing {
      calculatePrice(realms, features) {
        let totalPrice = 0;
        
        for (const realm of realms) {
          let realmPrice = 5.99; // Base price per realm
          
          if (features.analytics) realmPrice += 2.99;
          if (features.automation) realmPrice += 4.99;
          if (features.customBranding) realmPrice += 1.99;
          
          totalPrice += realmPrice;
        }
        
        return totalPrice;
      }
    }
    ```
  </Accordion>
</AccordionGroup>

### Revenue Tracking

Track revenue per realm for better insights:

```javascript theme={"dark"}
class RevenueTracker {
  constructor() {
    this.realmRevenue = new Map();
  }

  recordRealmRevenue(realmId, amount, period) {
    if (!this.realmRevenue.has(realmId)) {
      this.realmRevenue.set(realmId, {
        totalRevenue: 0,
        monthlyRevenue: [],
        firstPayment: Date.now()
      });
    }

    const realmData = this.realmRevenue.get(realmId);
    realmData.totalRevenue += amount;
    realmData.monthlyRevenue.push({
      period,
      amount,
      timestamp: Date.now()
    });
  }

  getRealmMetrics(realmId) {
    const data = this.realmRevenue.get(realmId);
    if (!data) return null;

    const monthlyAverage = data.monthlyRevenue.reduce((sum, payment) => 
      sum + payment.amount, 0) / data.monthlyRevenue.length;

    return {
      totalRevenue: data.totalRevenue,
      monthlyAverage,
      paymentCount: data.monthlyRevenue.length,
      customerLifetime: Date.now() - data.firstPayment
    };
  }
}
```

## Testing Multi-Realm Apps

### Testing Strategy

```javascript theme={"dark"}
class MultiRealmTester {
  constructor() {
    this.testRealms = [
      { id: 'test-realm-1', name: 'Test Realm 1', scopes: ['members:read', 'points:write'] },
      { id: 'test-realm-2', name: 'Test Realm 2', scopes: ['members:read'] },
      { id: 'test-realm-3', name: 'Test Realm 3', scopes: ['members:read', 'members:write', 'points:write'] }
    ];
  }

  async testCrossRealmFunctionality() {
    const appClient = new MultiRealmAppClient(process.env.TEST_APP_CLIENT_SECRET);
    
    // Mock authorized realms for testing
    for (const testRealm of this.testRealms) {
      appClient.authorizedRealms.set(testRealm.id, {
        realm: testRealm,
        approvedScopes: testRealm.scopes,
        authorizedAt: new Date().toISOString()
      });
    }

    // Test realm-specific operations
    for (const testRealm of this.testRealms) {
      console.log(`Testing realm: ${testRealm.name}`);
      
      // Test permission checking
      assert(appClient.hasScope(testRealm.id, 'members:read'));
      
      if (appClient.hasScope(testRealm.id, 'points:write')) {
        // Test point operations
        console.log('✅ Can award points in this realm');
      } else {
        console.log('❌ Cannot award points in this realm');
      }
    }

    // Test cross-realm analytics
    const analytics = new CrossRealmAnalytics(appClient);
    const stats = await analytics.getAggregatedStats();
    
    assert(stats.totalRealms === this.testRealms.length);
    console.log('✅ Cross-realm analytics working');
  }
}
```

## Deployment and Monitoring

### Health Checks for Multi-Realm Apps

```javascript theme={"dark"}
async function multiRealmHealthCheck() {
  const appClient = new MultiRealmAppClient(process.env.APP_CLIENT_SECRET);
  
  try {
    await appClient.loadAuthorizedRealms();
    
    const healthStatus = {
      status: 'healthy',
      timestamp: new Date().toISOString(),
      authorizedRealms: appClient.authorizedRealms.size,
      realmStatus: {}
    };

    // Test a sample of realms
    const realmIds = Array.from(appClient.authorizedRealms.keys()).slice(0, 3);
    
    for (const realmId of realmIds) {
      try {
        await appClient.makeRealmRequest(realmId, 'GET', `/realms/${realmId}`);
        healthStatus.realmStatus[realmId] = 'healthy';
      } catch (error) {
        healthStatus.realmStatus[realmId] = 'unhealthy';
        healthStatus.status = 'degraded';
      }
    }

    return healthStatus;
  } catch (error) {
    return {
      status: 'unhealthy',
      timestamp: new Date().toISOString(),
      error: error.message
    };
  }
}
```

<Info>
  **Building something cool?** Share your multi-realm app in our [Discord community](https://discord.gg/dripchain) and get feedback from other developers! 🚀
</Info>

## Creating Secure Installation URLs

For advanced app distribution, you can create encrypted installation URLs that include platform-specific data and expiration times.

### Prerequisites

<CardGroup>
  <Card title="Encryption Key" icon="key">
    You will need the encryption key provided for your app. This key is unique and ensures secure encryption.
  </Card>

  <Card title="Development Environment" icon="code">
    Use a JavaScript environment (Node.js or browser console) to run the encryption logic.
  </Card>
</CardGroup>

### Encryption Implementation

<Tabs>
  <Tab title="Node.js">
    ```javascript theme={"dark"}
    // Import the CryptoJS library
    const CryptoJS = require("crypto-js");

    // Encryption function
    function encryptData(data, passphrase) {
      const json = JSON.stringify(data);
      return CryptoJS.AES.encrypt(json, passphrase).toString();
    }

    // Example Usage:
    const encryptionKey = "your-app-encryption-key"; // Replace with your app's key
    const platformData = {
      platformType: "slack",       // Replace with your platform type
      platformId: "MY_TEAM_ID",    // Replace with your platform ID
      expirationTime: Date.now() + 30 * 60 * 1000 // Optional: expires in 30 minutes
    };

    // Encrypt the data
    const encrypted = encryptData(platformData, encryptionKey);
    console.log("Encrypted Data:", encrypted);

    // Build the URL
    const BASE_URL = "https://app.drip.re/admin/apps/authorize";
    const appId = "your-app-id"; // Replace with your app's ID

    // Final URL
    const installUrl = `${BASE_URL}?appId=${appId}&epfo=${encodeURIComponent(encrypted)}`;
    console.log("Installation URL:", installUrl);
    ```
  </Tab>

  <Tab title="Browser">
    ```html theme={"dark"}
    <!DOCTYPE html>
    <html>
    <head>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"></script>
    </head>
    <body>
      <script>
        // Encryption function
        function encryptData(data, passphrase) {
          const json = JSON.stringify(data);
          return CryptoJS.AES.encrypt(json, passphrase).toString();
        }

        // Configuration
        const encryptionKey = "your-app-encryption-key";
        const platformData = {
          platformType: "discord",
          platformId: "YOUR_GUILD_ID",
          expirationTime: Date.now() + 60 * 60 * 1000 // 1 hour
        };

        // Generate encrypted URL
        const encrypted = encryptData(platformData, encryptionKey);
        const BASE_URL = "https://app.drip.re/admin/apps/authorize";
        const appId = "your-app-id";
        const installUrl = `${BASE_URL}?appId=${appId}&epfo=${encodeURIComponent(encrypted)}`;
        
        console.log("Installation URL:", installUrl);
        document.body.innerHTML = `<a href="${installUrl}" target="_blank">Install App</a>`;
      </script>
    </body>
    </html>
    ```
  </Tab>
</Tabs>

### URL Parameters Explained

<AccordionGroup>
  <Accordion title="platformType">
    The type of platform you're integrating with:

    * `discord` - Discord servers
    * `slack` - Slack workspaces
    * `teams` - Microsoft Teams
    * `custom` - Custom platform integration
  </Accordion>

  <Accordion title="platformId">
    The unique identifier for the specific platform instance:

    * Discord: Guild/Server ID
    * Slack: Team/Workspace ID
    * Teams: Team ID
    * Custom: Your platform's unique identifier
  </Accordion>

  <Accordion title="expirationTime">
    Optional timestamp (in milliseconds) when the installation URL expires:

    * Helps prevent unauthorized installations
    * Recommended for sensitive integrations
    * Set to `Date.now() + (minutes * 60 * 1000)`
  </Accordion>
</AccordionGroup>

### Example Output

When you run the encryption code, you'll get:

```javascript theme={"dark"}
// Encrypted Data Example:
"U2FsdGVkX1+L+8EzH4IbNHRgXLSOh9OUCzPZ8tjVdNA1M5..."

// Generated Installation URL:
"https://app.drip.re/admin/apps/authorize?appId=your-app-id&epfo=U2FsdGVkX1%2BL%2B8EzH4IbNHRgXLSOh9OUCzPZ8tjVdNA1M5..."
```

### Security Best Practices

<CardGroup>
  <Card title="Keep Keys Secure" icon="shield">
    * Never share your encryption key publicly
    * Store keys in environment variables
    * Rotate keys periodically
    * Use different keys for different environments
  </Card>

  <Card title="URL Expiration" icon="clock">
    * Always set expiration times for sensitive URLs
    * Use shorter expiration times for production
    * Monitor for expired URL usage attempts
    * Provide clear error messages for expired URLs
  </Card>

  <Card title="Verify Integration" icon="check">
    * Test encrypted URLs before sharing
    * Verify decryption works correctly
    * Test with different platform types
    * Monitor installation success rates
  </Card>

  <Card title="Error Handling" icon="bug">
    * Handle decryption failures gracefully
    * Provide fallback installation methods
    * Log encryption/decryption errors
    * Validate platform data before encryption
  </Card>
</CardGroup>

## Verifying Authorization Programmatically

Each realm admin must explicitly authorize your app. You can check authorization and approved scopes via the API.

<CodeGroup>
  ```javascript Check Authorization Status theme={"dark"}
  async function checkRealmAuthorization(realmId, appId, appClientSecret) {
    const response = await fetch(`https://api.drip.re/api/v1/apps/${appId}/authorized-realms`, {
      headers: {
        'Authorization': `Bearer ${appClientSecret}`,
        'Content-Type': 'application/json'
      }
    });

    const authorizations = await response.json();
    return authorizations.data.find(auth => auth.realmId === realmId);
  }

  // Usage
  const authorization = await checkRealmAuthorization('REALM_ID', 'YOUR_APP_ID', 'YOUR_APP_CLIENT_SECRET');
  if (authorization) {
    console.log('Authorized scopes:', authorization.approvedScopes);
  } else {
    console.log('App not authorized for this realm');
  }

  ```

  ```python Python Example theme={"dark"}
  import requests

  def check_realm_authorization(realm_id, app_id, app_client_secret):
      url = f"https://api.drip.re/api/v1/apps/{app_id}/authorized-realms"
      
      headers = {
          'Authorization': f'Bearer {app_client_secret}',
          'Content-Type': 'application/json'
      }
      
      response = requests.get(url, headers=headers)
      authorizations = response.json()
      
      for auth in authorizations.get('data', []):
          if auth['realmId'] == realm_id:
              return auth
      
      return None

  # Usage
  authorization = check_realm_authorization('REALM_ID', 'YOUR_APP_ID', 'APP_CLIENT_SECRET')
  if authorization:
      print(f"Authorized scopes: {authorization['approvedScopes']}")
  else:
      print("App not authorized for this realm")
  ```

</CodeGroup>

## Next Steps

<CardGroup>
  <Card title="App Store Submission" icon="store" href="/developer/app-store">
    Learn how to submit your multi-realm app to the DRIP App Store
  </Card>

  <Card title="Best Practices" icon="shield" href="/developer/best-practices">
    Follow production-ready patterns for scalable apps
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference">
    Complete API documentation with all endpoints
  </Card>

  <Card title="Examples" icon="code" href="/developer/examples">
    Copy-paste code snippets for common use cases
  </Card>
</CardGroup>

# Point Systems

Source: https://docs.drip.re/developer/point-systems

Master DRIP's point and currency systems 💰

Learn how to effectively manage points and currencies in your DRIP realm. This guide covers everything from basic point operations to advanced currency management strategies.

## Overview

DRIP's point system is highly flexible, allowing you to create multiple currencies, manage complex reward structures, and build engaging gamification experiences for your community.

<Info>
  Points in DRIP are called "Realm Points" and can be customized with names, emojis, and branding to match your community's theme.
</Info>

## Understanding Realm Points

### Point Types

<CardGroup>
  <Card title="Primary Currency" icon="coins">
    Your main point system (e.g., XP, Coins, Tokens)

    * Usually the most visible to members
    * Used for major rewards and purchases
    * Often tied to overall member ranking
  </Card>

  <Card title="Secondary Currencies" icon="gem">
    Additional point types for specific purposes

    * Event-specific points (e.g., "Summer Points")
    * Category-specific rewards (e.g., "Art Coins")
    * Premium currencies (e.g., "Gems")
  </Card>
</CardGroup>

### Point Properties

Each Realm Point has these key properties:

```javascript theme={"dark"}
const realmPoint = {
  id: "507f1f77bcf86cd799439015",
  name: "Community XP",
  emoji: "⭐",
  description: "Experience points for community participation",
  isDefault: true,
  isTransferable: true,
  minimumBalance: 0,
  maximumBalance: 1000000
};
```

## Basic Point Operations

### Awarding Points

<Tabs>
  <Tab title="JavaScript">
    ```javascript theme={"dark"}
    async function awardPoints(client, memberId, points, reason = '') {
      try {
        const result = await client.request('PATCH',
          `/realm/${client.realmId}/members/${memberId}/point-balance`,
          { tokens: points }
        );

        console.log(`✅ Awarded ${points} points to member ${memberId}`);
        if (reason) console.log(`Reason: ${reason}`);
        
        return result;
      } catch (error) {
        console.error(`❌ Failed to award points: ${error.message}`);
        throw error;
      }
    }

    // Examples
    await awardPoints(client, 'member123', 100, 'Completed daily quest');
    await awardPoints(client, 'member456', 50, 'Helpful community contribution');
    ```
  </Tab>

  <Tab title="Python">
    ```python theme={"dark"}
    def award_points(client, member_id, points, reason=''):
        try:
            result = client.request('PATCH',
                f'/realm/{client.realm_id}/members/{member_id}/point-balance',
                {'tokens': points}
            )

            print(f"✅ Awarded {points} points to member {member_id}")
            if reason:
                print(f"Reason: {reason}")
            
            return result
        except Exception as e:
            print(f"❌ Failed to award points: {e}")
            raise

    # Examples
    award_points(client, 'member123', 100, 'Completed daily quest')
    award_points(client, 'member456', 50, 'Helpful community contribution')
    ```
  </Tab>
</Tabs>

### Deducting Points

```javascript theme={"dark"}
// Deduct points (negative amount)
await awardPoints(client, 'member123', -25, 'Minor rule violation penalty');

// Or use a dedicated deduction function
async function deductPoints(client, memberId, points, reason = '') {
  return await awardPoints(client, memberId, -Math.abs(points), reason);
}
```

### Checking Balances

```javascript theme={"dark"}
async function getPointBalance(client, memberId) {
  const members = await client.searchMembers('drip-id', memberId);
  
  if (members.data && members.data.length > 0) {
    const member = members.data[0];
    return member.pointBalances || [];
  }
  
  throw new Error('Member not found');
}

// Usage
const balances = await getPointBalance(client, 'member123');
balances.forEach(balance => {
  console.log(`${balance.realmPoint.name}: ${balance.balance} ${balance.realmPoint.emoji}`);
});
```

## Advanced Point Management

### Multiple Currency Systems

Manage different types of points for different purposes:

```javascript theme={"dark"}
class MultiCurrencyManager {
  constructor(client) {
    this.client = client;
    this.currencies = new Map();
  }

  async loadCurrencies() {
    // Load available realm points
    const realmPoints = await this.client.getRealmPoints();
    
    for (const point of realmPoints.data) {
      this.currencies.set(point.name.toLowerCase(), {
        id: point.id,
        name: point.name,
        emoji: point.emoji,
        isDefault: point.isDefault
      });
    }
  }

  async awardCurrency(memberId, currencyName, amount, reason = '') {
    const currency = this.currencies.get(currencyName.toLowerCase());
    if (!currency) {
      throw new Error(`Currency '${currencyName}' not found`);
    }

    return await this.client.request('PATCH',
      `/realm/${this.client.realmId}/members/${memberId}/point-balance`,
      { 
        tokens: amount,
        realmPointId: currency.id
      }
    );
  }

  async transferBetweenCurrencies(memberId, fromCurrency, toCurrency, amount) {
    // Convert points between different currencies
    // This would need custom business logic for exchange rates
    
    const exchangeRate = this.getExchangeRate(fromCurrency, toCurrency);
    const convertedAmount = Math.floor(amount * exchangeRate);

    // Deduct from source currency
    await this.awardCurrency(memberId, fromCurrency, -amount, 'Currency conversion');
    
    // Add to target currency
    await this.awardCurrency(memberId, toCurrency, convertedAmount, 'Currency conversion');
    
    return { originalAmount: amount, convertedAmount, exchangeRate };
  }

  getExchangeRate(fromCurrency, toCurrency) {
    // Define your exchange rates
    const rates = {
      'xp_to_coins': 0.1,      // 10 XP = 1 Coin
      'coins_to_gems': 0.01,   // 100 Coins = 1 Gem
      'gems_to_coins': 100,    // 1 Gem = 100 Coins
    };

    const rateKey = `${fromCurrency}_to_${toCurrency}`;
    return rates[rateKey] || 1;
  }
}
```

### Batch Point Operations

Efficiently update multiple members at once:

```javascript theme={"dark"}
async function batchPointAward(client, awards) {
  // awards = [{ memberId, points, reason }, ...]
  
  const updates = awards.map(award => ({
    memberId: award.memberId,
    tokens: award.points
  }));

  try {
    const result = await client.request('PATCH',
      `/realm/${client.realmId}/members/transaction`,
      { updates }
    );

    console.log(`✅ Batch awarded points to ${awards.length} members`);
    return result;
  } catch (error) {
    console.error('❌ Batch point award failed:', error.message);
    throw error;
  }
}

// Usage examples
await batchPointAward(client, [
  { memberId: 'member1', points: 100, reason: 'Event participation' },
  { memberId: 'member2', points: 150, reason: 'Contest winner' },
  { memberId: 'member3', points: 75, reason: 'Helpful member' }
]);
```

### Point Transfer Between Members

Enable peer-to-peer point transfers:

```javascript theme={"dark"}
async function transferPoints(client, senderId, recipientId, amount, currency = null) {
  try {
    const transferData = {
      tokens: amount,
      recipientId: recipientId
    };

    if (currency) {
      transferData.realmPointId = currency;
    }

    const result = await client.request('PATCH',
      `/realm/${client.realmId}/members/${senderId}/transfer`,
      transferData
    );

    console.log(`✅ Transferred ${amount} points from ${senderId} to ${recipientId}`);
    return result;
  } catch (error) {
    console.error(`❌ Transfer failed: ${error.message}`);
    throw error;
  }
}

// Usage
await transferPoints(client, 'sender123', 'recipient456', 50);
```

## Gamification Strategies

### Point Earning Systems

<AccordionGroup>
  <Accordion title="Activity-Based Rewards">
    Reward different types of community engagement:

    ```javascript theme={"dark"}
    const activityRewards = {
      'message_sent': 5,
      'reaction_added': 2,
      'voice_joined': 10,
      'helpful_reaction': 15,
      'first_message_daily': 25,
      'streak_7_days': 100
    };

    async function rewardActivity(client, memberId, activity) {
      const points = activityRewards[activity];
      if (points) {
        await awardPoints(client, memberId, points, `Activity: ${activity}`);
      }
    }
    ```
  </Accordion>

  <Accordion title="Milestone Rewards">
    Reward members for reaching specific milestones:

    ```javascript theme={"dark"}
    const milestones = [
      { threshold: 100, reward: 50, title: 'Newcomer' },
      { threshold: 500, reward: 100, title: 'Regular' },
      { threshold: 1000, reward: 200, title: 'Veteran' },
      { threshold: 5000, reward: 500, title: 'Legend' }
    ];

    async function checkMilestones(client, memberId, currentPoints) {
      for (const milestone of milestones) {
        if (currentPoints >= milestone.threshold) {
          // Check if already awarded (you'd track this in your database)
          const alreadyAwarded = await hasAwardedMilestone(memberId, milestone.threshold);
          
          if (!alreadyAwarded) {
            await awardPoints(client, memberId, milestone.reward, 
              `Milestone achieved: ${milestone.title}`);
            await recordMilestoneAwarded(memberId, milestone.threshold);
          }
        }
      }
    }
    ```
  </Accordion>

  <Accordion title="Time-Based Bonuses">
    Implement daily, weekly, or seasonal bonuses:

    ```javascript theme={"dark"}
    class TimeBonusManager {
      async getDailyBonus(client, memberId) {
        const today = new Date().toDateString();
        const lastClaim = await getLastBonusClaim(memberId);
        
        if (lastClaim !== today) {
          const bonusAmount = 25;
          await awardPoints(client, memberId, bonusAmount, 'Daily bonus');
          await recordBonusClaim(memberId, today);
          return bonusAmount;
        }
        
        return 0;
      }

      async getWeeklyBonus(client, memberId) {
        const streak = await getLoginStreak(memberId);
        if (streak >= 7) {
          const bonusAmount = 100 + (streak * 5); // Escalating bonus
          await awardPoints(client, memberId, bonusAmount, 'Weekly streak bonus');
          return bonusAmount;
        }
        
        return 0;
      }
    }
    ```
  </Accordion>
</AccordionGroup>

### Leaderboards and Rankings

Create competitive elements with point-based rankings:

```javascript theme={"dark"}
class LeaderboardManager {
  constructor(client) {
    this.client = client;
  }

  async getTopMembers(limit = 10, currencyId = null) {
    const members = await this.client.searchMembers('drip-id', 'all');
    
    return members.data
      .filter(member => member.pointBalances && member.pointBalances.length > 0)
      .map(member => {
        const balance = currencyId 
          ? member.pointBalances.find(b => b.realmPoint.id === currencyId)
          : member.pointBalances[0];
          
        return {
          id: member.id,
          name: member.displayName || member.username,
          points: balance?.balance || 0,
          currency: balance?.realmPoint.name || 'Unknown'
        };
      })
      .sort((a, b) => b.points - a.points)
      .slice(0, limit)
      .map((member, index) => ({ ...member, rank: index + 1 }));
  }

  async getMemberRank(memberId, currencyId = null) {
    const leaderboard = await this.getTopMembers(1000, currencyId);
    const memberRank = leaderboard.find(entry => entry.id === memberId);
    
    return memberRank ? memberRank.rank : null;
  }

  async getSeasonalLeaderboard(season, currencyId = null) {
    // This would require tracking seasonal points separately
    // Implementation depends on your seasonal point tracking system
    
    const seasonalPoints = await this.getSeasonalPoints(season, currencyId);
    return seasonalPoints
      .sort((a, b) => b.points - a.points)
      .map((entry, index) => ({ ...entry, rank: index + 1 }));
  }
}
```

## Point Economy Design

### Balancing Your Economy

<CardGroup>
  <Card title="Inflation Control" icon="trending-down">
    Prevent point inflation by:

    * Setting reasonable earning rates
    * Creating point sinks (ways to spend points)
    * Implementing diminishing returns
    * Regular economy reviews
  </Card>

  <Card title="Engagement Optimization" icon="target">
    Optimize for engagement by:

    * Rewarding diverse activities
    * Providing clear progression paths
    * Balancing effort vs. reward
    * Regular feedback and adjustments
  </Card>
</CardGroup>

### Point Sink Strategies

Create ways for members to spend their points:

```javascript theme={"dark"}
const pointSinks = {
  store_items: {
    'premium_role': { cost: 1000, duration: '30 days' },
    'custom_emoji': { cost: 500, permanent: true },
    'channel_access': { cost: 250, duration: '7 days' }
  },
  
  services: {
    'priority_support': { cost: 100, duration: '24 hours' },
    'custom_title': { cost: 300, permanent: true },
    'event_priority': { cost: 150, duration: 'next event' }
  },
  
  gambling: {
    'daily_lottery': { cost: 10, chance_to_win: 0.1, payout: 200 },
    'point_doubler': { cost: 50, chance_to_win: 0.3, payout: 100 }
  }
};
```

## Analytics and Monitoring

### Point Flow Tracking

Monitor how points move through your economy:

```javascript theme={"dark"}
class PointAnalytics {
  constructor(client) {
    this.client = client;
    this.transactions = [];
  }

  recordTransaction(type, memberId, amount, reason) {
    this.transactions.push({
      timestamp: Date.now(),
      type, // 'award', 'deduct', 'transfer'
      memberId,
      amount,
      reason
    });
  }

  getEconomyStats(timeframe = '7d') {
    const cutoff = Date.now() - this.getTimeframeMs(timeframe);
    const recentTransactions = this.transactions.filter(t => t.timestamp > cutoff);

    return {
      totalAwarded: recentTransactions
        .filter(t => t.type === 'award')
        .reduce((sum, t) => sum + t.amount, 0),
      
      totalDeducted: recentTransactions
        .filter(t => t.type === 'deduct')
        .reduce((sum, t) => sum + Math.abs(t.amount), 0),
      
      totalTransfers: recentTransactions
        .filter(t => t.type === 'transfer')
        .reduce((sum, t) => sum + t.amount, 0),
      
      netPointsCreated: recentTransactions
        .reduce((sum, t) => {
          if (t.type === 'award') return sum + t.amount;
          if (t.type === 'deduct') return sum - Math.abs(t.amount);
          return sum; // transfers don't create/destroy points
        }, 0)
    };
  }

  getTimeframeMs(timeframe) {
    const units = {
      'd': 24 * 60 * 60 * 1000,
      'h': 60 * 60 * 1000,
      'm': 60 * 1000
    };
    
    const value = parseInt(timeframe);
    const unit = timeframe.slice(-1);
    
    return value * (units[unit] || units.d);
  }
}
```

## Best Practices

<AccordionGroup>
  <Accordion title="Point Value Consistency">
    Keep point values meaningful and consistent:

    ```javascript theme={"dark"}
    // ✅ Good: Consistent scaling
    const rewards = {
      simple_task: 10,
      medium_task: 25,
      complex_task: 50,
      major_contribution: 100
    };

    // ❌ Bad: Inconsistent scaling
    const badRewards = {
      simple_task: 5,
      medium_task: 100,
      complex_task: 15,
      major_contribution: 1000
    };
    ```
  </Accordion>

  <Accordion title="Error Handling">
    Always handle point operations gracefully:

    ```javascript theme={"dark"}
    async function safePointAward(client, memberId, points, reason) {
      try {
        // Validate inputs
        if (!memberId || typeof points !== 'number' || points === 0) {
          throw new Error('Invalid award parameters');
        }

        // Check if member exists
        const members = await client.searchMembers('drip-id', memberId);
        if (!members.data || members.data.length === 0) {
          throw new Error('Member not found');
        }

        // Award points
        const result = await awardPoints(client, memberId, points, reason);
        
        // Log successful transaction
        console.log(`✅ ${points} points awarded to ${memberId}: ${reason}`);
        
        return result;
      } catch (error) {
        // Log error
        console.error(`❌ Failed to award points: ${error.message}`);
        
        // Don't throw for non-critical errors
        return null;
      }
    }
    ```
  </Accordion>

  <Accordion title="Performance Optimization">
    Optimize point operations for scale:

    ```javascript theme={"dark"}
    // Use batch operations for multiple updates
    const batchUpdates = members.map(member => ({
      memberId: member.id,
      tokens: calculateReward(member.activity)
    }));

    await client.batchUpdatePoints(batchUpdates);

    // Cache frequently accessed data
    const memberBalances = new Map();

    async function getCachedBalance(memberId) {
      if (memberBalances.has(memberId)) {
        return memberBalances.get(memberId);
      }
      
      const balance = await getPointBalance(client, memberId);
      memberBalances.set(memberId, balance);
      
      // Clear cache after 5 minutes
      setTimeout(() => memberBalances.delete(memberId), 5 * 60 * 1000);
      
      return balance;
    }
    ```
  </Accordion>
</AccordionGroup>

## Next Steps

<CardGroup>
  <Card title="Member Management" icon="users" href="/developer/managing-members">
    Learn to search and manage community members effectively
  </Card>

  <Card title="Ghost Credentials" icon="ghost" href="/developer/credentials">
    Pre-credit points to users before they join your realm
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference">
    Explore point-related API endpoints and advanced features
  </Card>

  <Card title="Best Practices" icon="shield" href="/developer/best-practices">
    Follow production-ready patterns for point systems
  </Card>
</CardGroup>

<Info>
  **Building a point economy?** Join our [Discord community](https://discord.gg/dripchain) to discuss strategies and get feedback from other developers! 💰
</Info>

# 5-Minute Quickstart

Source: https://docs.drip.re/developer/quickstart

Get your first DRIP API call working in 5 minutes ⚡

Ready to start building with DRIP? Let's get you up and running in 5 minutes! 🚀

## TL;DR - Just Want to Code?

<CodeGroup>
  ```bash Copy & Run This theme={"dark"}
  # 1. Get your API key from Admin > Developer > Project API
  # 2. Replace YOUR_API_KEY and YOUR_REALM_ID below
  # 3. Run this command

  curl -X GET "https://api.drip.re/api/v1/realms/YOUR_REALM_ID" \
    -H "Authorization: Bearer YOUR_API_KEY"

  ```

  ```javascript Node.js One-Liner theme={"dark"}
  // npm install node-fetch
  const response = await fetch('https://api.drip.re/api/v1/realms/YOUR_REALM_ID', {
    headers: { 'Authorization': 'Bearer YOUR_API_KEY' }
  });
  console.log(await response.json());
  ```

  ```python Python One-Liner   theme={"dark"}
  # pip install requests
  import requests
  r = requests.get('https://api.drip.re/api/v1/realms/YOUR_REALM_ID', 
                   headers={'Authorization': 'Bearer YOUR_API_KEY'})
  print(r.json())
  ```

</CodeGroup>

## Step-by-Step (For Real This Time)

### 1. Get Your API Key (30 seconds)

<Steps>
  <Step title="Open DRIP Dashboard">
    Go to [app.drip.re](https://app.drip.re) and log in
  </Step>

  <Step title="Navigate to Developer Portal">
    Click **Admin** → **Developer** in the sidebar
  </Step>

  <Step title="Create API Client">
    * Click **Project API** tab
    * Click **Create API Client**
    * Give it a name like "My First App"
    * Select some scopes (start with `realm:read` and `members:read`)
    * Click **Create**
  </Step>

  <Step title="Copy Your Keys">
    Copy both the **Client ID** and **Client Secret** (you'll need the secret)
  </Step>
</Steps>

### 2. Find Your Realm (Project) ID (15 seconds)

Your Realm ID is displayed in the dashboard header when you select your project:

<Steps>
  <Step title="Select Your Project">
    In the DRIP dashboard, make sure your project is selected from the project switcher
  </Step>

  <Step title="Copy Realm ID">
    Look at the dashboard header - your Realm ID is displayed there and can be copied directly
  </Step>
</Steps>

### 3. Make Your First Call (1 minute)

<Tabs>
  <Tab title="JavaScript">
    ```javascript theme={"dark"}
    const DRIP_API_KEY = 'your_client_secret_here';
    const REALM_ID = 'your_realm_id_here';

    async function getDripData() {
      try {
        // Get your realm info
        const realm = await fetch(`https://api.drip.re/api/v1/realms/${REALM_ID}`, {
          headers: { 'Authorization': `Bearer ${DRIP_API_KEY}` }
        }).then(r => r.json());
        
        console.log('🎉 Your realm:', realm.name);
        
        // Get some members
        const members = await fetch(`https://api.drip.re/api/v1/realm/${REALM_ID}/members/search?type=drip-id&values=all`, {
          headers: { 'Authorization': `Bearer ${DRIP_API_KEY}` }
        }).then(r => r.json());
        
        console.log('👥 Member count:', members.data?.length || 0);
        
      } catch (error) {
        console.error('❌ Error:', error.message);
      }
    }

    getDripData();
    ```
  </Tab>

  <Tab title="Python">
    ```python theme={"dark"}
    import requests

    DRIP_API_KEY = 'your_client_secret_here'
    REALM_ID = 'your_realm_id_here'

    headers = {'Authorization': f'Bearer {DRIP_API_KEY}'}

    try:
        # Get your realm info
        realm = requests.get(f'https://api.drip.re/api/v1/realms/{REALM_ID}', headers=headers).json()
        print(f'🎉 Your realm: {realm["name"]}')
        
        # Get some members  
        members = requests.get(f'https://api.drip.re/api/v1/realm/{REALM_ID}/members/search?type=drip-id&values=all', headers=headers).json()
        print(f'👥 Member count: {len(members.get("data", []))}')
        
    except Exception as error:
        print(f'❌ Error: {error}')
    ```
  </Tab>

  <Tab title="cURL">
    ```bash theme={"dark"}
    # Set your variables
    DRIP_API_KEY="your_client_secret_here"
    REALM_ID="your_realm_id_here"

    # Get realm info
    echo "🎉 Your realm:"
    curl -s "https://api.drip.re/api/v1/realms/$REALM_ID" \
      -H "Authorization: Bearer $DRIP_API_KEY" | jq '.name'

    # Get member count
    echo "👥 Member count:"
    curl -s "https://api.drip.re/api/v1/realm/$REALM_ID/members/search?type=drip-id&values=all" \
      -H "Authorization: Bearer $DRIP_API_KEY" | jq '.data | length'
    ```
  </Tab>
</Tabs>

## What Just Happened? 🤔

You just:

1. ✅ **Authenticated** with the DRIP API
2. ✅ **Retrieved** your realm information
3. ✅ **Searched** for members in your community

Not bad for 5 minutes! 🎉

## What Can You Do Next?

<CardGroup>
  <Card title="Award Points to Members" icon="coins" href="#award-points-to-a-member">
    Give your community members some points for being awesome
  </Card>

  <Card title="Search for Specific Members" icon="user" href="#search-members-by-discord-id">
    Find members by Discord ID, wallet address, or username
  </Card>

  <Card title="Build a Simple Dashboard" icon="chart-bar" href="/developer/first-app">
    Create your first DRIP-powered app
  </Card>

  <Card title="Member Management" icon="users" href="/developer/managing-members">
    Search, update, and manage community members effectively
  </Card>
</CardGroup>

## Quick Examples for Vibe Coders

### Award Points to a Member

<CodeGroup>
  ```javascript Give 100 Points theme={"dark"}
  // Find a member first
  const members = await fetch(`https://api.drip.re/api/v1/realm/${REALM_ID}/members/search?type=username&values=cool_member`, {
    headers: { 'Authorization': `Bearer ${DRIP_API_KEY}` }
  }).then(r => r.json());

  if (members.data?.length > 0) {
    const memberId = members.data[0].id;

    // Give them 100 points
    const result = await fetch(`https://api.drip.re/api/v1/realm/${REALM_ID}/members/${memberId}/point-balance`, {
      method: 'PATCH',
      headers: { 
        'Authorization': `Bearer ${DRIP_API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ tokens: 100 })
    }).then(r => r.json());
    
    console.log('💰 Points awarded!', result);
  }

  ```

  ```python Award Points theme={"dark"}
  import requests

  # Find a member
  members = requests.get(
      f'https://api.drip.re/api/v1/realm/{REALM_ID}/members/search?type=username&values=cool_member',
      headers={'Authorization': f'Bearer {DRIP_API_KEY}'}
  ).json()

  if members.get('data'):
      member_id = members['data'][0]['id']
      
      # Award 100 points
      result = requests.patch(
          f'https://api.drip.re/api/v1/realm/{REALM_ID}/members/{member_id}/point-balance',
          headers={'Authorization': f'Bearer {DRIP_API_KEY}', 'Content-Type': 'application/json'},
          json={'tokens': 100}
      ).json()
      
      print('💰 Points awarded!', result)
  ```

</CodeGroup>

### Search Members by Discord ID

<CodeGroup>
  ```javascript Find Discord User theme={"dark"}
  const discordId = '123456789012345678'; // Their Discord user ID

  const members = await fetch(`https://api.drip.re/api/v1/realm/${REALM_ID}/members/search?type=discord-id&values=${discordId}`, {
    headers: { 'Authorization': `Bearer ${DRIP_API_KEY}` }
  }).then(r => r.json());

  if (members.data?.length > 0) {
    const member = members.data[0];
    console.log(`Found: ${member.displayName} with ${member.pointBalances[0]?.balance || 0} points`);
  } else {
    console.log('Member not found 😢');
  }

  ```

  ```python Find by Wallet theme={"dark"}
  wallet_address = '0x742d35Cc6634C0532925a3b8D23'

  members = requests.get(
      f'https://api.drip.re/api/v1/realm/{REALM_ID}/members/search?type=wallet&values={wallet_address}',
      headers={'Authorization': f'Bearer {DRIP_API_KEY}'}
  ).json()

  if members.get('data'):
      member = members['data'][0]
      points = member['pointBalances'][0]['balance'] if member['pointBalances'] else 0
      print(f"Found: {member['displayName']} with {points} points")
  else:
      print('Member not found 😢')
  ```

</CodeGroup>

## Common "Oops" Moments 🤦‍♂️

<AccordionGroup>
  <Accordion title="❌ 401 Unauthorized">
    **Problem**: Your API key is wrong or missing

    **Fix**: Double-check you're using the **Client Secret** (not Client ID) from the developer portal

    ```bash theme={"dark"}
    # Wrong ❌
    Authorization: Bearer your_client_id_here

    # Right ✅  
    Authorization: Bearer your_client_secret_here
    ```
  </Accordion>

  <Accordion title="❌ 403 Forbidden">
    **Problem**: Your API client doesn't have the right scopes

    **Fix**: Go back to **Admin > Developer > Project API** and add more scopes to your client

    Common scopes you might need:

    * `realm:read` - Read realm info
    * `members:read` - Read member data
    * `members:write` - Update member points
    * `points:write` - Award/deduct points
  </Accordion>

  <Accordion title="❌ 404 Not Found">
    **Problem**: Wrong Realm ID or member doesn't exist

    **Fix**: Check your realm ID in the dashboard URL. For members, try searching first before updating.
  </Accordion>

  <Accordion title="❌ 429 Too Many Requests">
    **Problem**: You're making requests too fast

    **Fix**: Add a small delay between requests or use batch endpoints

    ```javascript theme={"dark"}
    // Add delay
    await new Promise(resolve => setTimeout(resolve, 100));
    ```
  </Accordion>
</AccordionGroup>

## You're Ready! 🎯

That's it! You now know enough to be dangerous with the DRIP API. Here's what to explore next:

<CardGroup>
  <Card title="Build Your First App" icon="rocket" href="/developer/first-app">
    Create a simple DRIP-powered application
  </Card>

  <Card title="Learn the Fundamentals" icon="book" href="/developer/core-concepts">
    Understand DRIP's data model and concepts
  </Card>

  <Card title="See More Examples" icon="code" href="/developer/examples">
    Copy-paste code for common tasks
  </Card>
</CardGroup>

<Info>
  **Pro tip**: Join our [Discord community](https://discord.gg/dripchain) for help, tips, and to show off what you're building! 🚀
</Info>

# Rate Limits

Source: https://docs.drip.re/developer/rate-limits

Understanding API rate limits, quotas, and best practices for efficient usage

The DRIP API implements rate limiting to ensure fair usage and maintain system performance for all users. This guide explains how rate limits work and how to handle them in your applications.

## Rate Limit Overview

DRIP uses a sliding window rate limiting system that tracks requests over time periods. Different endpoints may have different limits based on their resource intensity.

### Current Limits

#### Free

| Endpoint | Requests per Minute | Requests per Month |
| -------- | ------------------- | ------------------ |
| Points   | 24                  | 100,000            |

#### Pro

| Endpoint    | Requests per Minute | Requests per Month |
| ----------- | ------------------- | ------------------ |
| Points      | 300                 | 1,000,000          |
| Quests      | 120                 | 100,000            |
| Social data | 600                 | 25,000             |

#### Enterprise

| Endpoint    | Requests per Minute | Requests per Month |
| ----------- | ------------------- | ------------------ |
| Points      | 500                 | 5,000,000          |
| Quests      | 200                 | 1,000,000          |
| Social data | 1,200               | 250,000            |

<Info>
  Rate limits are applied per Realm, not per API key.
</Info>

## Rate Limit Headers

Every API response includes headers that show your current rate limit status:

```http theme={"dark"}
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 87
X-RateLimit-Reset: 1642694400
X-RateLimit-Window: 60
```

### Header Descriptions

| Header                  | Description                                    |
| ----------------------- | ---------------------------------------------- |
| `X-RateLimit-Limit`     | Maximum requests allowed in the current window |
| `X-RateLimit-Remaining` | Requests remaining in the current window       |
| `X-RateLimit-Reset`     | Unix timestamp when the window resets          |
| `X-RateLimit-Window`    | Window duration in seconds                     |

## Handling Rate Limits

### 429 Too Many Requests

When you exceed the rate limit, the API returns a `429 Too Many Requests` status with a `Retry-After` header:

```json theme={"dark"}
{
  "error": "Rate limit exceeded",
  "message": "Too many requests. Try again in 30 seconds.",
  "retryAfter": 30
}
```

### Implementation Examples

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  class DripClient {
    constructor(apiKey) {
      this.apiKey = apiKey;
      this.baseUrl = 'https://api.drip.re/api/v1';
    }

    async request(method, endpoint, data = null, retries = 3) {
      const url = `${this.baseUrl}${endpoint}`;
      
      for (let attempt = 0; attempt <= retries; attempt++) {
        try {
          const response = await fetch(url, {
            method,
            headers: {
              'Authorization': `Bearer ${this.apiKey}`,
              'Content-Type': 'application/json'
            },
            body: data ? JSON.stringify(data) : null
          });

          // Log rate limit info
          console.log(`Rate limit: ${response.headers.get('X-RateLimit-Remaining')}/${response.headers.get('X-RateLimit-Limit')}`);

          if (response.status === 429) {
            const retryAfter = parseInt(response.headers.get('Retry-After') || '60');
            
            if (attempt < retries) {
              console.log(`Rate limited. Retrying in ${retryAfter} seconds...`);
              await this.sleep(retryAfter * 1000);
              continue;
            }
            
            throw new Error(`Rate limit exceeded after ${retries} retries`);
          }

          if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
          }

          return response.json();
        } catch (error) {
          if (attempt === retries) throw error;
          
          // Exponential backoff for other errors
          const delay = Math.pow(2, attempt) * 1000;
          await this.sleep(delay);
        }
      }
    }

    sleep(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
    }
  }

  ```

  ```python Python theme={"dark"}
  import requests
  import time
  from typing import Optional, Dict, Any

  class DripClient:
      def __init__(self, api_key: str):
          self.api_key = api_key
          self.base_url = 'https://api.drip.re/api/v1'
          self.session = requests.Session()
          self.session.headers.update({
              'Authorization': f'Bearer {api_key}',
              'Content-Type': 'application/json'
          })

      def request(self, method: str, endpoint: str, data: Optional[Dict] = None, retries: int = 3) -> Dict[Any, Any]:
          url = f"{self.base_url}{endpoint}"
          
          for attempt in range(retries + 1):
              try:
                  response = self.session.request(method, url, json=data)
                  
                  # Log rate limit info
                  remaining = response.headers.get('X-RateLimit-Remaining', 'unknown')
                  limit = response.headers.get('X-RateLimit-Limit', 'unknown')
                  print(f"Rate limit: {remaining}/{limit}")
                  
                  if response.status_code == 429:
                      retry_after = int(response.headers.get('Retry-After', 60))
                      
                      if attempt < retries:
                          print(f"Rate limited. Retrying in {retry_after} seconds...")
                          time.sleep(retry_after)
                          continue
                      
                      raise Exception(f"Rate limit exceeded after {retries} retries")
                  
                  response.raise_for_status()
                  return response.json()
                  
              except requests.exceptions.RequestException as e:
                  if attempt == retries:
                      raise e
                  
                  # Exponential backoff
                  delay = (2 ** attempt)
                  time.sleep(delay)
          
          raise Exception("Max retries exceeded")
  ```

</CodeGroup>

## Best Practices

### 1. Monitor Rate Limit Headers

Always check the rate limit headers in your responses to avoid hitting limits:

```javascript theme={"dark"}
function checkRateLimit(response) {
  const remaining = parseInt(response.headers.get('X-RateLimit-Remaining'));
  const limit = parseInt(response.headers.get('X-RateLimit-Limit'));
  
  if (remaining < limit * 0.1) { // Less than 10% remaining
    console.warn('Approaching rate limit. Consider slowing down requests.');
  }
}
```

### 2. Implement Exponential Backoff

Use exponential backoff for retries to avoid thundering herd problems:

```javascript theme={"dark"}
async function exponentialBackoff(attempt, maxDelay = 60000) {
  const delay = Math.min(Math.pow(2, attempt) * 1000, maxDelay);
  const jitter = Math.random() * 0.1 * delay; // Add 10% jitter
  
  await new Promise(resolve => setTimeout(resolve, delay + jitter));
}
```

### 3. Batch Operations

Use batch endpoints when available to reduce API calls:

```javascript theme={"dark"}
// Instead of multiple individual updates
for (const member of members) {
  await updateMemberBalance(realmId, member.id, 10); // 100 API calls
}

// Use batch update
await batchUpdateBalances(realmId, members.map(m => ({
  memberId: m.id,
  tokens: 10
}))); // 1 API call
```

### 4. Cache Frequently Accessed Data

Implement caching to reduce redundant API calls:

```javascript theme={"dark"}
class CachedDripClient extends DripClient {
  constructor(apiKey, cacheTtl = 300000) { // 5 minutes
    super(apiKey);
    this.cache = new Map();
    this.cacheTtl = cacheTtl;
  }

  async getRealm(realmId) {
    const cacheKey = `realm:${realmId}`;
    const cached = this.cache.get(cacheKey);
    
    if (cached && Date.now() - cached.timestamp < this.cacheTtl) {
      return cached.data;
    }

    const realm = await this.request('GET', `/realms/${realmId}`);
    this.cache.set(cacheKey, {
      data: realm,
      timestamp: Date.now()
    });

    return realm;
  }
}
```

## Endpoint-Specific Limits

Some endpoints have additional restrictions:

### Batch Operations

* **Batch member updates**: Maximum 100 members per request
* **Member search**: Maximum 50 values per search

### File Operations

* **Asset uploads**: 10 MB maximum file size
* **Bulk imports**: Maximum 1,000 records per import

### Webhooks

* **Webhook calls**: Maximum 5 retries per event
* **Webhook timeout**: 30 seconds maximum response time

## Monitoring and Alerts

### Track Your Usage

Implement usage tracking to monitor your API consumption:

```javascript theme={"dark"}
class UsageTracker {
  constructor() {
    this.requests = [];
  }

  recordRequest(endpoint, status, remaining) {
    this.requests.push({
      endpoint,
      status,
      remaining,
      timestamp: Date.now()
    });

    // Keep only last hour of data
    const oneHourAgo = Date.now() - 3600000;
    this.requests = this.requests.filter(r => r.timestamp > oneHourAgo);
  }

  getUsageStats() {
    const totalRequests = this.requests.length;
    const errorRequests = this.requests.filter(r => r.status >= 400).length;
    const rateLimitedRequests = this.requests.filter(r => r.status === 429).length;

    return {
      totalRequests,
      errorRate: errorRequests / totalRequests,
      rateLimitRate: rateLimitedRequests / totalRequests
    };
  }
}
```

### Set Up Alerts

Create alerts for approaching rate limits:

```javascript theme={"dark"}
function checkForAlerts(usageStats, rateLimitRemaining, rateLimitLimit) {
  const usagePercentage = (rateLimitLimit - rateLimitRemaining) / rateLimitLimit;
  
  if (usagePercentage > 0.8) {
    console.warn('WARNING: Using 80% of rate limit');
    // Send alert to monitoring system
  }
  
  if (usageStats.rateLimitRate > 0.05) {
    console.error('ERROR: High rate limit rejection rate');
    // Send alert to monitoring system
  }
}
```

## Upgrading Limits

If you consistently hit rate limits, consider upgrading your plan:

<CardGroup>
  <Card title="Analyze Usage" icon="chart-line">
    Review your API usage patterns and identify peak times
  </Card>

  <Card title="Optimize Code" icon="code">
    Implement caching, batching, and efficient request patterns
  </Card>

  <Card title="Upgrade Plan" icon="arrow-up">
    Contact support to discuss higher rate limits for your use case
  </Card>
</CardGroup>

## Rate Limit Errors

### Common Error Scenarios

<AccordionGroup>
  <Accordion title="Burst Limit Exceeded">
    **Cause**: Too many requests in a very short time period

    **Solution**: Implement request queuing and spacing between calls

    ```javascript theme={"dark"}
    class RequestQueue {
      constructor(maxConcurrent = 5, delayMs = 100) {
        this.queue = [];
        this.running = 0;
        this.maxConcurrent = maxConcurrent;
        this.delayMs = delayMs;
      }

      async add(requestFn) {
        return new Promise((resolve, reject) => {
          this.queue.push({ requestFn, resolve, reject });
          this.process();
        });
      }

      async process() {
        if (this.running >= this.maxConcurrent || this.queue.length === 0) {
          return;
        }

        this.running++;
        const { requestFn, resolve, reject } = this.queue.shift();

        try {
          const result = await requestFn();
          resolve(result);
        } catch (error) {
          reject(error);
        } finally {
          this.running--;
          setTimeout(() => this.process(), this.delayMs);
        }
      }
    }
    ```
  </Accordion>

  <Accordion title="Sustained High Usage">
    **Cause**: Consistently high request volume over time

    **Solution**: Implement better caching and consider plan upgrade
  </Accordion>

  <Accordion title="Inefficient Polling">
    **Cause**: Frequent polling for updates instead of using webhooks

    **Solution**: Switch to webhook-based updates for real-time data
  </Accordion>
</AccordionGroup>

## Testing Rate Limits

### Development Environment

Test your rate limit handling in development:

```javascript theme={"dark"}
async function testRateLimit() {
  const client = new DripClient(process.env.DRIP_API_KEY);
  
  // Make rapid requests to trigger rate limiting
  const promises = [];
  for (let i = 0; i < 150; i++) {
    promises.push(client.getRealm('YOUR_REALM_ID'));
  }
  
  try {
    await Promise.all(promises);
  } catch (error) {
    console.log('Rate limit handling test:', error.message);
  }
}
```

<Warning>
  Only test rate limits in development environments with test API keys to avoid impacting production systems.
</Warning>

## Summary

Effective rate limit handling involves:

1. **Monitor** rate limit headers in all responses
2. **Implement** exponential backoff and retry logic
3. **Use** batch operations and caching to reduce calls
4. **Track** usage patterns and set up alerts
5. **Optimize** your integration for efficiency

Following these practices will ensure your integration remains reliable and performs well within DRIP's rate limits.

# User Authentication & OAuth

Source: https://docs.drip.re/developer/user-authentication

Secure user authentication flow for accessing user data with consent

Enable your app to securely authenticate users and access their DRIP profile data with explicit consent. This OAuth-like flow works for both single-realm and multi-realm applications.

## Overview

The DRIP User Authentication system provides a secure, consent-based flow for apps to access user data. Similar to OAuth 2.0, users must explicitly authorize your app before it can access their information.

### Quick Flow Summary

1. **Your app redirects user** to `https://app.drip.re/oauth/authorize?client_id=YOUR_CLIENT_ID&redirect_uri=YOUR_REDIRECT_URI`
2. **User reviews and approves** your app on the DRIP consent page
3. **User is redirected back** to your `redirect_uri` with an authorization code: `YOUR_REDIRECT_URI?code=AUTH_CODE&response_type=code`
4. **Your app exchanges the code** for the user's DRIP ID by calling the API
5. **Your app can now access** user data using the DRIP ID

<Info>
  **Key Benefits:**

* 🔒 Secure user consent flow
* 🎯 Works for both Realm and Multi-realm apps
* ⚡ Short-lived authorization codes (5-minute TTL)
* 🔑 Minimal data exposure (only returns dripId)
* ✅ Transparent app information for users
</Info>

## Authentication Flow

```mermaid theme={"dark"}
graph TD;
  A[User Clicks Login] --> B[Redirect to DRIP Consent Page];
  B --> C[User Reviews App Info];
  C --> D[User Approves/Denies];
  D --> E[Authorization Code Generated];
  E --> F[Redirect Back with Code];
  F --> G[App Exchanges Code];
  G --> H[Receives User dripId];
  H --> I[App Can Access User Data];
```

## Implementation Guide

### Prerequisites

<CardGroup>
  <Card title="API Client Setup" icon="key">
    Your app must have a valid API client (either Realm or App client) with appropriate scopes
  </Card>

  <Card title="Redirect URI" icon="link">
    Configure a redirect URI where users will be sent after authorization
  </Card>
</CardGroup>

### Step 1: Redirect to Authorization Page

Direct users to the DRIP consent page where they can review and approve your app:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  function initiateUserAuth(clientId, redirectUri) {
    // Redirect user to DRIP consent page
    const authUrl = new URL('https://app.drip.re/oauth/authorize');
    authUrl.searchParams.set('client_id', clientId);
    authUrl.searchParams.set('redirect_uri', redirectUri);

    // Redirect the user to the consent page
    window.location.href = authUrl.toString();
    
    // OR return the URL for the user to visit
    return authUrl.toString();
  }

  // Example usage:
  const authorizationUrl = initiateUserAuth(
    'your-client-id',
    'https://yourapp.com/auth/callback'
  );
  // Result: https://app.drip.re/oauth/authorize?client_id=your-client-id&redirect_uri=https://yourapp.com/auth/callback

  ```

  ```python Python theme={"dark"}
  from urllib.parse import urlencode

  def initiate_user_auth(client_id, redirect_uri):
      # Build the authorization URL
      base_url = "https://app.drip.re/oauth/authorize"
      params = {
          'client_id': client_id,
          'redirect_uri': redirect_uri
      }
      
      auth_url = f"{base_url}?{urlencode(params)}"
      
      # Return the URL for the user to visit
      return auth_url

  # Example usage:
  authorization_url = initiate_user_auth(
      'your-client-id',
      'https://yourapp.com/auth/callback'
  )
  # Result: https://app.drip.re/oauth/authorize?client_id=your-client-id&redirect_uri=https://yourapp.com/auth/callback
  ```

  ```typescript TypeScript theme={"dark"}
  function initiateUserAuth(
    clientId: string,
    redirectUri: string
  ): string {
    // Build the authorization URL
    const authUrl = new URL('https://app.drip.re/oauth/authorize');
    authUrl.searchParams.set('client_id', clientId);
    authUrl.searchParams.set('redirect_uri', redirectUri);
    
    // Redirect the user (browser environment)
    if (typeof window !== 'undefined') {
      window.location.href = authUrl.toString();
    }
    
    // Return the URL
    return authUrl.toString();
  }

  // Example usage:
  const authorizationUrl = initiateUserAuth(
    'your-client-id',
    'https://yourapp.com/auth/callback'
  );
  // Result: https://app.drip.re/oauth/authorize?client_id=your-client-id&redirect_uri=https://yourapp.com/auth/callback
  ```

</CodeGroup>

<Info>
  **What happens on the consent page:**

  1. User must be logged into DRIP
  2. App information is displayed (name, logo, developer, verification status)
  3. User can approve or deny access
  4. If approved, user is redirected to your `redirect_uri` with an authorization code
  5. If denied, user is redirected with an error parameter
</Info>

<Warning>
  **Important:** Do not confuse the consent page URL (`https://app.drip.re/oauth/authorize`) with the API endpoint (`https://api.drip.re/api/v1/auth/oauth/authorize`). Users visit the consent page in their browser - you should never directly call the authorization API endpoint. The consent page handles calling the API internally when the user approves.
</Warning>

### Step 2: Handle the Callback

After user approval, they'll be redirected to your `redirect_uri` with the authorization code:

```
https://yourapp.com/auth/callback?code=AUTHORIZATION_CODE&response_type=code
```

If the user denies access:

```
https://yourapp.com/auth/callback?error=access_denied
```

### Step 3: Exchange Authorization Code

Exchange the authorization code for the user's DRIP ID:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function exchangeAuthCode(appToken, authCode) {
    const response = await fetch('https://api.drip.re/api/v1/auth/oauth/token', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${appToken}`, // Your app's token
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        grant_type: 'authorization_code',
        code: authCode
      })
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(`Exchange failed: ${error.message}`);
    }

    const data = await response.json();
    return data.dripId; // User's DRIP ID
  }

  ```

  ```python Python theme={"dark"}
  def exchange_auth_code(app_token, auth_code):
      url = "https://api.drip.re/api/v1/auth/oauth/token"
      
      headers = {
          'Authorization': f'Bearer {app_token}',
          'Content-Type': 'application/json'
      }
      
      payload = {
          'grant_type': 'authorization_code',
          'code': auth_code
      }
      
      response = requests.post(url, headers=headers, json=payload)
      
      if response.status_code != 200:
          error = response.json()
          raise Exception(f"Exchange failed: {error.get('message', 'Unknown error')}")
      
      data = response.json()
      return data['dripId']  # User's DRIP ID
  ```

  ```typescript TypeScript theme={"dark"}
  interface TokenExchangeResponse {
    dripId: string;
  }

  async function exchangeAuthCode(
    appToken: string,
    authCode: string
  ): Promise<string> {
    const response = await fetch('https://api.drip.re/api/v1/auth/oauth/token', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${appToken}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        grant_type: 'authorization_code',
        code: authCode
      })
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(`Exchange failed: ${error.message}`);
    }

    const data: TokenExchangeResponse = await response.json();
    return data.dripId;
  }
  ```

</CodeGroup>

### Step 4: Get Public Client Information (Optional)

You can fetch your app's public information to display on your own consent/login page:

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  async function getAppInfo(clientId) {
    const response = await fetch(
      `https://api.drip.re/api/v1/auth/oauth/client?client_id=${clientId}`
    );

    if (!response.ok) {
      throw new Error('Failed to fetch app information');
    }

    return await response.json();
    // Returns:
    // {
    //   name: "App Name",
    //   description: "App description",
    //   pfp: "https://...",  // Profile picture URL
    //   verified: true,      // Verification status
    //   developer: "Developer Name"
    // }
  }

  ```

  ```python Python theme={"dark"}
  def get_app_info(client_id):
      url = f"https://api.drip.re/api/v1/auth/oauth/client?client_id={client_id}"
      
      response = requests.get(url)
      
      if response.status_code != 200:
          raise Exception('Failed to fetch app information')
      
      return response.json()
      # Returns app information dict
  ```

</CodeGroup>

## Complete Implementation Example

Here's a full implementation of the user authentication flow:

<CodeGroup>
  ```javascript Express.js Server theme={"dark"}
  const express = require('express');
  const app = express();

  // Configuration
  const CLIENT_ID = process.env.DRIP_CLIENT_ID;
  const APP_TOKEN = process.env.DRIP_APP_TOKEN;
  const REDIRECT_URI = 'https://yourapp.com/auth/callback';
  const REALM_ID = process.env.DRIP_REALM_ID;

  // Step 1: Redirect user to DRIP authorization page
  app.get('/auth/login', (req, res) => {
    const authUrl = new URL('https://app.drip.re/oauth/authorize');
    authUrl.searchParams.set('client_id', CLIENT_ID);
    authUrl.searchParams.set('redirect_uri', REDIRECT_URI);

    // Redirect user to DRIP consent page
    res.redirect(authUrl.toString());
  });

  // Step 2: Handle callback and exchange code
  app.get('/auth/callback', async (req, res) => {
    const { code } = req.query;

    if (!code) {
      return res.status(400).json({ error: 'No authorization code provided' });
    }

    try {
      // Exchange code for user's DRIP ID
      const response = await fetch('https://api.drip.re/api/v1/auth/oauth/token', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${APP_TOKEN}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          grant_type: 'authorization_code',
          code: code
        })
      });

      const data = await response.json();
      
      // Store user's DRIP ID in your database
      const dripId = data.dripId;
      
      // Create session for user
      req.session.dripId = dripId;
      
      res.json({ 
        success: true, 
        message: 'Authentication successful',
        dripId: dripId 
      });
    } catch (error) {
      res.status(500).json({ error: 'Token exchange failed' });
    }
  });

  // Step 4: Use the DRIP ID to fetch user data
  app.get('/user/profile', async (req, res) => {
    const dripId = req.session.dripId;

    if (!dripId) {
      return res.status(401).json({ error: 'Not authenticated' });
    }

    try {
      // Now you can use the dripId to fetch user-specific data
      // from your realm using your app's API token
      const response = await fetch(
        `https://api.drip.re/api/v1/realm/${REALM_ID}/members/search?type=drip-id&values=${dripId}`,
        {
          headers: {
            'Authorization': `Bearer ${APP_TOKEN}`
          }
        }
      );

      const userData = await response.json();
      res.json(userData);
    } catch (error) {
      res.status(500).json({ error: 'Failed to fetch user data' });
    }
  });

  app.listen(3000, () => {
    console.log('Server running on port 3000');
  });

  ```

  ```python Flask Server theme={"dark"}
  from flask import Flask, request, redirect, jsonify, session
  from urllib.parse import urlencode
  import requests
  import os

  app = Flask(__name__)
  app.secret_key = os.urandom(24)

  # Configuration
  CLIENT_ID = os.getenv('DRIP_CLIENT_ID')
  APP_TOKEN = os.getenv('DRIP_APP_TOKEN')
  REDIRECT_URI = 'https://yourapp.com/auth/callback'
  REALM_ID = os.getenv('DRIP_REALM_ID')

  @app.route('/auth/login')
  def auth_login():
      # Build authorization URL
      base_url = "https://app.drip.re/oauth/authorize"
      params = {
          'client_id': CLIENT_ID,
          'redirect_uri': REDIRECT_URI
      }
      auth_url = f"{base_url}?{urlencode(params)}"
      
      # Redirect user to DRIP consent page
      return redirect(auth_url)

  @app.route('/auth/callback')
  def auth_callback():
      code = request.args.get('code')
      
      if not code:
          return jsonify({'error': 'No authorization code provided'}), 400
      
      try:
          # Exchange code for DRIP ID
          response = requests.post(
              'https://api.drip.re/api/v1/auth/oauth/token',
              headers={
                  'Authorization': f'Bearer {APP_TOKEN}',
                  'Content-Type': 'application/json'
              },
              json={
                  'grant_type': 'authorization_code',
                  'code': code
              }
          )
          
          data = response.json()
          drip_id = data['dripId']
          
          # Store in session
          session['drip_id'] = drip_id
          
          return jsonify({
              'success': True,
              'message': 'Authentication successful',
              'dripId': drip_id
          })
      
      except Exception as e:
          return jsonify({'error': 'Token exchange failed'}), 500

  @app.route('/user/profile')
  def user_profile():
      drip_id = session.get('drip_id')
      
      if not drip_id:
          return jsonify({'error': 'Not authenticated'}), 401
      
      try:
          # Fetch user data using DRIP ID
          response = requests.get(
              f'https://api.drip.re/api/v1/realm/{REALM_ID}/members/search',
              params={'type': 'drip-id', 'values': drip_id},
              headers={'Authorization': f'Bearer {APP_TOKEN}'}
          )
          
          user_data = response.json()
          return jsonify(user_data)
      
      except Exception as e:
          return jsonify({'error': 'Failed to fetch user data'}), 500

  if __name__ == '__main__':
      app.run(port=3000)
  ```

</CodeGroup>

## Security Considerations

<CardGroup>
  <Card title="Authorization Code TTL" icon="clock">
    * Codes expire in 5 minutes
    * Single-use only (invalidated after exchange)
    * Cannot be reused once exchanged
    * Implement retry logic for expired codes
  </Card>

  <Card title="Token Security" icon="shield">
    * Store tokens securely (never in frontend code)
    * Use HTTPS for all API calls
    * Validate redirect URIs
    * Implement CSRF protection
  </Card>

  <Card title="User Privacy" icon="user-shield">
    * Minimal data exposure (only dripId)
    * Explicit user consent required
    * Users can revoke access anytime
    * Clear privacy policy recommended
  </Card>

  <Card title="App Verification" icon="certificate">
    * Display app info transparently
    * Show verification status to users
    * Include developer information
    * Provide clear app description
  </Card>
</CardGroup>

## Error Handling

Handle common authentication errors gracefully:

<AccordionGroup>
  <Accordion title="Invalid Client ID">
    **Error**: `invalid_client`

    **Causes**:

    * Client ID doesn't exist
    * Client has been deactivated

    **Solution**:

    ```javascript theme={"dark"}
    if (error.message === 'Invalid clientId') {
      console.error('Check your CLIENT_ID configuration');
      // Redirect to error page
    }
    ```
  </Accordion>

  <Accordion title="Code Already Used">
    **Error**: `code_already_used`

    **Causes**:

    * Authorization code was already exchanged
    * Duplicate exchange attempt

    **Solution**:

    ```javascript theme={"dark"}
    if (error.message === 'code_already_used') {
      // Request new authorization code
      return initiateNewAuthFlow();
    }
    ```
  </Accordion>

  <Accordion title="Code Expired">
    **Error**: `code_expired`

    **Causes**:

    * More than 5 minutes passed since code generation
    * Network delays

    **Solution**:

    ```javascript theme={"dark"}
    if (error.message === 'code_expired') {
      // Automatically restart auth flow
      return restartAuthentication();
    }
    ```
  </Accordion>

  <Accordion title="Invalid Code">
    **Error**: `invalid_code`

    **Causes**:

    * Malformed authorization code
    * Code doesn't exist
    * Wrong client attempting exchange

    **Solution**:

    ```javascript theme={"dark"}
    if (error.message === 'invalid_code' || error.message === 'invalid_code_client') {
      // Log security event and restart
      logSecurityEvent('Invalid auth code attempt');
      return showAuthError();
    }
    ```
  </Accordion>
</AccordionGroup>

## Best Practices

### User Experience

<Steps>
  <Step title="Clear Consent UI">
    Build a clear consent screen showing:

    * App name and logo
    * Requested permissions
    * Developer information
    * What data will be accessed
  </Step>

  <Step title="Smooth Flow">
    * Minimize redirects
    * Show loading states
    * Handle errors gracefully
    * Provide clear success feedback
  </Step>

  <Step title="Session Management">
    * Store DRIP ID securely
    * Implement session expiration
    * Provide logout functionality
    * Clear sessions on errors
  </Step>
</Steps>

### Implementation Tips

```javascript theme={"dark"}
class DripAuthManager {
  constructor(clientId, appToken, realmId) {
    this.clientId = clientId;
    this.appToken = appToken;
    this.realmId = realmId;
    this.redirectUri = 'https://yourapp.com/auth/callback';
    this.sessions = new Map();
  }

  // Generate the authorization URL for user to visit
  getAuthorizationUrl() {
    const authUrl = new URL('https://app.drip.re/oauth/authorize');
    authUrl.searchParams.set('client_id', this.clientId);
    authUrl.searchParams.set('redirect_uri', this.redirectUri);
    return authUrl.toString();
  }

  // Handle the callback after user authorization
  async handleCallback(authorizationCode) {
    try {
      // Exchange code for DRIP ID
      const dripId = await this.exchangeCode(authorizationCode);
      
      // Create session
      const sessionId = this.createSession(dripId);
      
      return { success: true, sessionId, dripId };
    } catch (error) {
      return { success: false, error: error.message };
    }
  }

  async exchangeCode(code) {
    const response = await fetch('https://api.drip.re/api/v1/auth/oauth/token', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${this.appToken}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        grant_type: 'authorization_code',
        code: code
      })
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.message || 'Exchange failed');
    }

    const data = await response.json();
    return data.dripId;
  }

  createSession(dripId) {
    const sessionId = this.generateSessionId();
    this.sessions.set(sessionId, {
      dripId,
      createdAt: Date.now(),
      lastAccessed: Date.now()
    });
    return sessionId;
  }

  generateSessionId() {
    return Math.random().toString(36).substring(2) + Date.now().toString(36);
  }

  async getUserData(sessionId) {
    const session = this.sessions.get(sessionId);
    if (!session) {
      throw new Error('Invalid session');
    }

    // Update last accessed
    session.lastAccessed = Date.now();

    // Fetch user data from DRIP
    const response = await fetch(
      `https://api.drip.re/api/v1/realm/${this.realmId}/members/search?type=drip-id&values=${session.dripId}`,
      {
        headers: {
          'Authorization': `Bearer ${this.appToken}`
        }
      }
    );

    if (!response.ok) {
      throw new Error('Failed to fetch user data');
    }

    return await response.json();
  }

  logout(sessionId) {
    return this.sessions.delete(sessionId);
  }
}

// Usage
const authManager = new DripAuthManager(
  process.env.DRIP_CLIENT_ID,
  process.env.DRIP_APP_TOKEN,
  process.env.DRIP_REALM_ID
);
```

## Testing Your Implementation

### Test Authorization Flow

```javascript theme={"dark"}
async function testAuthFlow() {
  const clientId = 'your_client_id';
  const appToken = 'your_app_token';
  const redirectUri = 'http://localhost:3000/callback';

  try {
    // Step 1: Generate authorization URL
    console.log('🔐 Authorization URL:');
    const authUrl = new URL('https://app.drip.re/oauth/authorize');
    authUrl.searchParams.set('client_id', clientId);
    authUrl.searchParams.set('redirect_uri', redirectUri);
    console.log(authUrl.toString());
    console.log('👆 User must visit this URL and approve the app');
    
    // Step 2: After user approves, they'll be redirected with a code
    // Simulate receiving the authorization code from the callback
    const authorizationCode = 'AUTHORIZATION_CODE_FROM_CALLBACK';
    console.log('✅ Authorization code received:', authorizationCode);

    // Step 3: Exchange code
    console.log('🔄 Exchanging code for DRIP ID...');
    const tokenResponse = await fetch('https://api.drip.re/api/v1/auth/oauth/token', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${appToken}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        grant_type: 'authorization_code',
        code: authorizationCode
      })
    });

    const { dripId } = await tokenResponse.json();
    console.log('✅ DRIP ID received:', dripId);
    console.log('🎉 Authentication flow complete!');

    return dripId;
  } catch (error) {
    console.error('❌ Test failed:', error.message);
    throw error;
  }
}
```

## Troubleshooting

<Warning>
  **Common Issues:**

* Ensure your client has the correct scopes for user data access
* Verify redirect URIs match exactly (including trailing slashes)
* Check that authorization codes are exchanged within 5 minutes
* Confirm your app token has necessary permissions
</Warning>

## Next Steps

<CardGroup>
  <Card title="Multi-Realm Apps" icon="globe" href="/developer/multi-realm-apps">
    Learn how to implement authentication across multiple realms
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference">
    Complete API documentation for all authentication endpoints
  </Card>

  <Card title="Security Best Practices" icon="shield" href="/developer/best-practices">
    Advanced security patterns for production apps
  </Card>

  <Card title="Examples" icon="code" href="/developer/examples">
    More code examples and implementation patterns
  </Card>
</CardGroup>

# DRIP Overview

Source: https://docs.drip.re/overview

A high-level overview of the DRIP platform, core concepts, and how everything fits together

DRIP is a platform for building engaged communities and apps. It provides a unified data layer, permissions model, and APIs so you can extend your community with modular functionality.

## Core concepts

* Realms: Projects/workspaces that contain members, data, and app installations
* Members: Users in your realms, with identities that can span platforms
* Apps: Modular capabilities installed into one or more realms
* Permissions: Scoped per app and per realm for precise control
* APIs: Stable interfaces for reading data and performing actions

<Info>
  DRIP apps follow least‑privilege permissions. Each app only gets the scopes you grant for the realms you select.
</Info>

## How apps fit into DRIP

Apps integrate via DRIP’s APIs and are permissioned per realm. You can install multiple apps to compose end‑to‑end workflows—everything remains auditable and secure.

* Install DRIP or third‑party apps into a realm
* Configure app settings and permissions to match your needs
* Combine apps to power onboarding, engagement, rewards, and more

## Next steps

* Explore the Apps section for installation and official apps
* Visit the Developer Guide to build your own apps
