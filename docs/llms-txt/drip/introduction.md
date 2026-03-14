# Source: https://docs.drip.re/api-reference/introduction.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# API Introduction

> Welcome to the DRIP API documentation. Learn about our current and legacy APIs.

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

```diff  theme={"dark"}
- https://legacy-api.drip.re/v1
+ https://api.drip.re/api/v1
```

### Step 3: Update Authentication

```diff  theme={"dark"}
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

Built with [Mintlify](https://mintlify.com).
