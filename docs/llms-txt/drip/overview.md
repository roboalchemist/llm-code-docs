# Source: https://docs.drip.re/overview.md

# Source: https://docs.drip.re/apps/overview.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Understand the DRIP apps ecosystem and how apps fit into your workspace

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

<CardGroup cols={3}>
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

<CardGroup cols={3}>
  <Card title="Discord Bot" icon="discord" href="/bot-documentation/home">
    Moderation, quests, points, and community engagement features.
  </Card>

  <Card title="Burn Ghosts Activity" icon="ghost" href="/burn-ghosts-activity/home">
    Competitive tournaments with 9 mini-games and token rewards.
  </Card>
</CardGroup>

Built with [Mintlify](https://mintlify.com).
