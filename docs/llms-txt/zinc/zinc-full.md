# Zinc Documentation

Source: https://www.zinc.com/docs/llms-full.txt

---

# Changelog
Source: https://zinc-staging.vercel.app/docs/changelog

Product updates and improvements to Zinc API

<Update label="2026-03-06" description="Week of Mar 2">
  <Frame>
    <img alt="Week of Mar 2 updates" />
  </Frame>

  This week brings Home Depot support, estimated delivery dates, international currency handling, and a new retailer status page.

  ### Home Depot Support

  Zinc now supports placing orders on **Home Depot**, expanding our retailer coverage to one of the largest home improvement retailers.

  ### Estimated Delivery Dates

  If provided by the retailer, Zinc will now extract estimated delivery dates during the checkout process and include them in your order details.

  ### International Currency Support

  Orders placed on retailers that use non-USD currencies are now automatically converted to USD at charge time. This makes it easier to place orders on international retailers without worrying about currency handling.

  ### Retailer Status Page

  We've added a user-facing [retailer status page](https://app.zinc.com/retailers) so you can monitor which retailers are currently supported and their operational status.

  ### Improvements

  * **Better rural address support** — Fixed validation failures for rural and highway addresses where USPS data is limited
  * **Clearer validation errors** — Enhanced error messages for invalid addresses
  * **Max price display** — The order detail page in the dashboard now shows the max price set for each order
  * **Direct product links** — Order details now include direct links to the product URL
  * **Editable addresses** — Address fields are now editable in the create order flyout after selection
</Update>

<Update label="2026-02-27" description="Week of Feb 23">
  <Frame>
    <img alt="Week of Feb 23 updates" />
  </Frame>

  This week brings Canadian shipping support, saved payment selection for managed accounts, and improved tracking reliability.

  ### Canadian Shipping Addresses

  Zinc now supports shipping to Canada, continuing our expansion of international address coverage. Canadian addresses are fully validated during order creation.

  ### Saved Payment Selection

  When using managed accounts, you can now select which saved payment method to use for an order. If you have multiple cards on file with a retailer, you can specify exactly which one Zinc should use during checkout.

  ### LaserShip Tracking Support

  Orders shipped via LaserShip now include tracking numbers, giving you visibility into deliveries from this regional carrier.

  ### Improvements

  * **Better tracking extraction** — Improved tracking number and verification code extraction with fewer false positives
  * **Smarter email filtering** — Enhanced filtering of emails before extracting tracking and verification data
  * **More accurate merchant order IDs** — Improved extraction of merchant order IDs from retailer confirmations
</Update>

<Update label="2026-02-20" description="Week of Feb 16">
  <Frame>
    <img alt="Week of Feb 16 updates" />
  </Frame>

  This week brings expanded retailer support with account-less checkout, international shipping to new regions, and improved order reliability.

  ### Account-less Checkout for Walmart, Target & Wayfair

  Until now, Zinc-managed checkout accounts were only available for Amazon. This week, we're bringing the same experience to **Walmart**, **Target**, and **Wayfair** — meaning you can place orders on these retailers without creating or managing your own accounts. Just provide a shipping address and payment method, and Zinc handles the rest using our managed credentials.

  This is a major step forward: retailers that previously required you to bring your own account credentials are now accessible out of the box. And this is just the beginning — we'll be rolling out managed checkout to more retailers soon.

  ### International Shipping: New Zealand & Australia

  Zinc now supports shipping to New Zealand and Australia, continuing our expansion of international address coverage. Addresses for both countries are fully validated during order creation.

  ### Payment Verification for Managed Accounts

  Managed accounts now support retailer-specific payment verification. If a retailer requires additional payment confirmation during checkout, Zinc stores and uses the appropriate verification hints automatically.

  ### SMS Verification Code Support

  Our checkout system now supports OTP retrieval from forwarded SMS verification codes, in addition to email-based codes. This improves success rates for retailers that use SMS-based authentication.

  ### Improvements

  * **Smarter cart validation** — Fixed checkout failures caused by cart information no longer being displayed on the page
  * **Better error codes** — Added a specific `payment_verification_required` error code for clearer debugging
</Update>

<Update label="2026-02-13" description="Week of Feb 9">
  <Frame>
    <img alt="Week of Feb 9 updates" />
  </Frame>

  This week's highlight is the launch of our Universal Checkout Skill for AI agents, plus auto wallet top-up and better order visibility.

  ### Universal Checkout Skill

  <CardGroup>
    <Frame>
      <video />
    </Frame>

    <Frame>
      <video />
    </Frame>
  </CardGroup>

  Zinc is now available as an [Agent Skill](https://agentskills.io) — a new way for AI agents to place orders through natural language. Install the [Universal Checkout Skill](/v2/agent-skills/overview) into [OpenClaw](/openclaw), Claude Code, or Gemini CLI, and your agent can search for products, place orders, and check statuses — all from a single conversation.

  * **Natural language ordering** — Ask your agent to buy a product by URL, and it handles the rest
  * **Search-to-purchase** — Pair with Brave Search to find and order products in one workflow
  * **Confirmation built in** — The agent always confirms before spending real money

  [Learn more →](/openclaw)

  ### Auto Wallet Top-up

  Never run out of funds mid-order. You can now configure automatic wallet top-ups that trigger whenever your balance drops below a threshold. Set your minimum balance and top-up amount from the new wallet settings page, and Zinc handles the rest.

  ### Order Progress Timeline

  Order details now include a visual timeline showing each step of the purchasing flow. See exactly where your order is and what's already been completed.

  ### Improvements

  * **Email forwarding indicators** — A new badge shows when forwarded verification emails have been detected for your managed accounts
  * **Better Amazon tracking** — Improved package tracking URL extraction from Amazon order emails
  * **International address fixes** — Fixed address validation for countries that don't require a state or province field
</Update>

<Update label="2026-02-06" description="Week of Feb 2">
  <Frame>
    <img alt="Week of Feb 2 updates" />
  </Frame>

  This week's highlight is a brand new retailer status page, plus stronger account security and better order visibility.

  ### Retailer Status Page

  <Frame>
    <img alt="Retailer status page" />
  </Frame>

  Zinc now has a dedicated status page with nightly integration test results for our top retailers. We're committed to full transparency into what's working and what isn't — and we'll be expanding coverage to more retailers over time.

  ### TOTP Support for Retailer Credentials

  Managed retail accounts now support Time-based One-Time Passwords (TOTP). If your retailer account uses two-factor authentication with an authenticator app, you can provide your TOTP secret and Zinc will automatically generate codes during login — no more manual verification steps.

  ### Improved Order Progress

  <Frame>
    <img alt="Incremental order status updates" />
  </Frame>

  Orders now report more granular progress updates as they move through each step of the purchasing flow, giving you better real-time visibility into order status.
</Update>

<Update label="2026-01-30" description="Week of Jan 26">
  <Frame>
    <img alt="Week of Jan 26 updates" />
  </Frame>

  This week we're focused on reliability and expanding Zinc's reach with international shipping support and B2B features.

  ### International Order Support

  Zinc now supports shipping to Germany, with more countries coming soon. International addresses are validated during order creation, and we've updated our date and currency formatting to handle international locales correctly.

  * **Country configuration** — Each retailer now has configurable supported shipping countries using ISO 3166-1 alpha-2 codes
  * **Address validation** — International addresses are validated before order creation
  * **Flexible formats** — Postal codes work with both `zip_code` and `postal_code` fields, and state/province fields are now optional for countries that don't require them

  ### Purchase Order Support

  For B2B customers, you can now include a purchase order number with your orders. Just pass an optional `po_number` field and we'll automatically detect PO number fields during checkout and fill them in.

  ### Product Variant Fixes

  Fixed an issue where variant verification was failing for products that have pre-selected variants on the page. Variants should now work correctly across all supported retailers.
</Update>

<Update label="2026-01-16" description="Week of Jan 12">
  <Frame>
    <img alt="Week of Jan 12 updates" />
  </Frame>

  ### Launch Week 1

  **January 20-24** — Zinc's first launch week. Five days. Five releases.

  We're rapidly expanding Zinc 2.0's feature-set, vastly improving devex, and showing off some impressive demos to inspire you on what you can build with Zinc.

  Pay attention to your inboxes and our socials for Launch Week 1!

  ***

  ### Account Selection in Orders

  <Frame>
    <img alt="Account selection dropdown" />
  </Frame>

  The order form now includes a dropdown to choose between Zinc-managed accounts and your own retailer credentials. You can see exactly which account will be used before placing an order.

  * **Visual account picker** — Select from your saved retailer accounts directly in the order form
  * **Curl command preview** — See the exact API call that will be made, with one-click copy

  ### Easier Gmail Setup

  Setting up email forwarding for verification codes just got simpler. A new "Add Gmail Filter" button generates the exact filter you need with one click.

  ### Smarter Retry Logic

  We've improved how failed orders are retried to be more intelligent about when retries make sense.

  * **Order-level tracking** — Retry attempts are now tracked at the order level for better visibility
  * **Skip hopeless retries** — Orders that fail due to out-of-stock products, inaccessible items, or unavailable guest checkout no longer waste time retrying
</Update>

<Update label="2026-01-09" description="Week of Jan 5">
  <Frame>
    <img alt="Week of Jan 5 updates" />
  </Frame>

  This week we're introducing managed retail accounts and smarter payment handling. These features give you more control over how orders are placed and make credential management significantly easier.

  ### Managed Retail Accounts

  <Frame>
    <img alt="Managed retail accounts" />
  </Frame>

  You can now use managed retail accounts to place orders with your own retailer credentials. This gives you more control over order placement and unlocks features that require being logged in.

  * **Amazon account support** — Orders placed with Amazon credentials now use our enhanced processing system for better reliability
  * **Forwarding email addresses** — Each managed account automatically gets a dedicated email address for verification codes and tracking notifications
  * **Easy credential reference** — Use short IDs to quickly identify and reference your saved retail credentials
  * **Explicit credential selection** — Specify exactly which credentials to use with the `retailer_credentials_id` parameter

  ### Smarter Payment Handling

  When using managed accounts, Zinc now automatically uses your saved payment method if you don't provide one explicitly. This means less redundant data in your API calls.

  * **Automatic payment detection** — Orders with managed accounts can use saved payment methods without passing payment details each time
  * **Flexible payment modes** — Switch seamlessly between saved and explicit payment methods based on your needs
  * **Clear error messages** — Get helpful `payment_method_required` errors when a saved method is needed but doesn't exist

  ### Streamlined Onboarding

  We've simplified the getting-started experience to help you start testing faster.

  * **Skip optional steps** — Skip non-essential onboarding steps and dive straight into testing
  * **Faster setup** — Streamlined flow gets you to your first test order more quickly

  ### Better Error Tracking

  Enhanced error reporting throughout the platform helps you debug issues faster with more specific error types and clearer messages.
</Update>

<Update label="2026-01-02" description="Week of Dec 29">
  <Frame>
    <img alt="Week of Dec 29 updates" />
  </Frame>

  A lighter week with focused improvements to order search and price clarity, plus continued infrastructure work.

  ### Better Order Search

  You can now search for orders by order ID, making it easier to find specific orders in your dashboard.

  ### Clearer Price Warnings

  When an order exceeds your maximum price threshold, you'll now see a clear "Max Price Exceeded" warning instead of a generic failure message. This makes it easier to understand why an order didn't complete.

  ### Infrastructure Improvements

  We've been working on backend improvements to support future features:

  * **Multi-worker architecture** — Building distributed systems for better scalability
  * **Enhanced authentication** — Improving support for retailer accounts that require login
  * **Better error tracking** — Expanding our monitoring to catch and fix issues faster
</Update>

<Update label="2025-12-26" description="Week of Dec 22">
  <Frame>
    <img alt="Week of Dec 22 updates" />
  </Frame>

  This week brought intelligent product variant interpretation and expanded financial management capabilities. The highlight: we can now automatically understand and parse product variants from plaintext strings.

  ### Product Variant Interpretation

  <Frame>
    <img alt="Product variant interpretation" />
  </Frame>

  The biggest update this week is our ability to intelligently interpret product variants from plaintext strings. Instead of requiring structured data, you can now provide variant information as natural text and we'll automatically parse it into the correct format.

  * **Intelligent parsing** — Automatically interpret size, color, and style options from plaintext strings
  * **Flexible input** — No need to pre-structure variant data, just provide the information naturally
  * **Clear label/value pairs** — Properly formatted variants for accurate order placement

  ### Better Test Order Flow

  <Frame>
    <img alt="Better test order flow" />
  </Frame>

  We've streamlined the in-app test order experience with rich previews and variant management.

  * **URL preview cards** — See product images and details before placing test orders using Open Graph metadata
  * **Variant support** — Test orders now fully support product variants with the new interpretation system
  * **Mobile-optimized** — Fully responsive order interface that works seamlessly on mobile devices

  ### Improvements

  * **Better error messages** — Clearer feedback when payment or order issues occur
  * **Fixed retry logic** — Order retry now works correctly and only triggers for failed orders
</Update>

<Update label="2025-12-19" description="Week of Dec 15">
  <Frame>
    <img alt="Week of Dec 15 updates" />
  </Frame>

  We finally released the latest version of Zinc. This initial release brings dramatically expanded retailer support, along with key order management features.

  ### V2 Beta Launch

  <Frame>
    <iframe />
  </Frame>

  Zinc 2.0 beta is now available with a modern API and dashboard. This release dramatically expands our retailer coverage.

  * **More Retailers:** Dramatically expanded retailer support across the world's top online stores
  * **Modern API:** Clean, consistent API design for better developer experience

  <Note>
    Some v1 features (account automation, tracking, returns) are coming soon. See [migrating from v1](/v2/migrating-from-v1) for details.
  </Note>

  ### Order Management

  <Frame>
    <img alt="Order management features" />
  </Frame>

  You can now cancel orders directly from the dashboard and retry failed orders through the API. This gives you more control over your order lifecycle without needing to contact support.

  * **Cancel orders** — Stop orders before they're fulfilled when plans change (available in dashboard)
  * **Retry failed orders** — Automatically retry orders that failed due to temporary issues (available via API)

  ### Amazon Integration

  <Frame>
    <img alt="Amazon integration" />
  </Frame>

  For customers who need Amazon's full feature set during the v2 transition, orders can now be automatically proxied through our v1 API. This ensures continuity while we complete v2 feature parity.

  ### Platform Improvements

  We've also made several improvements to the overall platform experience:

  * **Better order display** — Improved how order details are shown in the dashboard
  * **Payment notifications** — Clearer notifications when payment methods need attention
</Update>

<Update label="2025-12-12" description="Week of Dec 7">
  <Frame>
    <img alt="Week of Dec 7 updates" />
  </Frame>

  This week brought improvements to wallet management and ordering reliability. We're making it easier to manage your account balance and ensuring orders succeed more consistently.

  ### Wallet Management

  <Frame>
    <img alt="Wallet management interface" />
  </Frame>

  You can now add funds directly to your wallet using your saved payment methods. Previously, you had to contact support to top up your account — now you can do it yourself in seconds.

  We've also added detailed descriptions to all wallet transactions, so you can see exactly what each charge was for (API fees, order costs, etc.).

  ### More Reliable Orders

  Orders now automatically retry when they encounter temporary issues, making the overall process more reliable. We've also made several improvements:

  * **Smarter price checking** — We now validate prices only at the final checkout step, reducing premature order failures
  * **More accurate pricing** — Enhanced price extraction logic handles varied retailer formats more reliably
</Update>


# Introduction
Source: https://zinc-staging.vercel.app/docs/index

Zinc lets you search, buy, and return items from top online retailers with a single API.

<CardGroup>
  <Card title="Quickstart" href="/quickstart" icon="rocket">
    Get up and running with Zinc API in minutes.
  </Card>

  <Card title="What is Zinc?" icon="circle-question" href="/what-is-zinc">
    Learn about Zinc, our mission, and how our API powers e-commerce automation.
  </Card>

  <Card title="API Reference" icon="book" href="/v2/api-reference/introduction/authentication">
    Explore all endpoints, request/response formats, and integration details.
  </Card>

  <Card title="Discord" icon="discord" href="https://discord.gg/cuXgfczYfj">
    Join our Discord community for support, updates, and discussion.
  </Card>
</CardGroup>


# Quickstart
Source: https://zinc-staging.vercel.app/docs/quickstart

Get started with Zinc API in minutes.

<Steps>
  <Step title="Create your Zinc account">
    <a href="https://app.zinc.com">Sign up here</a> to get started. You will need to deposit funds into your Zinc account to use the API.
  </Step>

  <Step title="Get Your API Credentials">
    After signing up, visit your <a href="https://app.zinc.com">Zinc dashboard</a> to find your client token.
  </Step>

  <Step title="Make Your First API Call">
    Here's h ow to place an order using `curl`:

    ```bash theme={null}
    export ZINC_API_KEY=<api_key>;
    curl -X POST https://api.zinc.com/orders \
        -H "Authorization: Bearer $ZINC_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "products": [{
            "url": "https://www.zinc.com/shop/stickers",
            "quantity": 1
          }],
          "max_price": 100,
          "shipping_address": {
            "first_name": "...",
            "last_name": "...",
            "address_line1": "...",
            "address_line2": null,
            "city": "...",
            "state": "...",
            "postal_code": "...",
            "phone_number": "..."
          }
        }';
    ```

    <Info>
      Replace <code>\<api\_key></code> with your actual token. Never share your client token publicly.
    </Info>

    If successful, you'll get a successful JSON response with the request data. The order will now show
    up in your dashboard.
  </Step>
</Steps>

***

Need help? <a href="mailto:support@zinc.com">Contact support</a> or check out the [What is Zinc?](/what-is-zinc) page for more info.


# Universal Checkout Skill
Source: https://zinc-staging.vercel.app/docs/v2/agent-skills/overview

Let AI agents buy anything with a URL using the Zinc API.

The **Universal Checkout Skill** is an [Agent Skill](https://agentskills.io) that enables AI agents to place and manage e-commerce orders through the [Zinc API](https://zinc.com). Once installed, you can ask your AI agent to buy products from online retailers, check order statuses, and list recent orders — all through natural language.

<CardGroup>
  <Frame>
    <video />
  </Frame>

  <Frame>
    <video />
  </Frame>

  <Frame>
    <video />
  </Frame>
</CardGroup>

## What is an Agent Skill?

An Agent Skill is a declarative specification (a `SKILL.md` file) that teaches AI agents how to interact with an API. There's no executable code — the skill simply provides instructions, endpoint definitions, and safety guidelines that the agent follows.

Agent Skills use **progressive disclosure**: at startup only the skill name and description are loaded. The full instructions are read into context only when the agent detects a matching task, keeping your agent fast and focused.

## What Can It Do?

The Universal Checkout Skill gives your agent three capabilities:

| Capability             | Description                                               |
| ---------------------- | --------------------------------------------------------- |
| **Place orders**       | Buy products from supported retailers using a product URL |
| **Check order status** | Look up the current status and tracking info for an order |
| **List orders**        | View recent orders placed through Zinc                    |

<Warning>
  Placing an order spends real money from your Zinc account. The agent will
  always confirm with you before submitting an order.
</Warning>

## Supported Platforms

The Universal Checkout Skill works with any agent platform that supports the [Agent Skills](https://agentskills.io) standard, including:

* [OpenClaw](https://openclaw.ai)
* [Claude Code](https://claude.ai/code)
* [Gemini CLI](https://github.com/google-gemini/gemini-cli)

## Prerequisites

Before you begin, you'll need:

1. A **Zinc API key**. [Sign up at app.zinc.com](https://app.zinc.com) to get one.
2. Funds deposited in your Zinc account to place orders.
3. A supported AI agent platform (see above).

## Next Steps

<CardGroup>
  <Card title="Setup" icon="wrench" href="/v2/agent-skills/setup">
    Install and configure the skill for your platform.
  </Card>

  <Card title="Usage Guide" icon="cart-shopping" href="/v2/agent-skills/usage">
    Learn how to place orders and track them with your agent.
  </Card>
</CardGroup>


# Setup
Source: https://zinc-staging.vercel.app/docs/v2/agent-skills/setup

Install and configure the Universal Checkout Skill for your AI agent.

## Installation

The Universal Checkout Skill is installed by cloning the repository into a location
your agent can discover. The exact steps depend on your platform.

<Tabs>
  <Tab title="Git Clone">
    Clone the skill into your project's `skills/` directory:

    ```bash theme={null}
    git clone https://github.com/zincio/universal-checkout-skill.git ./skills/universal-checkout-skill
    ```

    Compatible agents automatically discover skills in the workspace `skills/` folder. No additional configuration is needed beyond setting the API key.
  </Tab>

  <Tab title="OpenClaw via Clawhub">
    **Option 1: Install via ClawHub**

    ```bash theme={null}
    clawhub install a5huynh/universal-checkout
    ```

    **Option 2: Clone manually**

    Install at the user level (available across all projects):

    ```bash theme={null}
    git clone https://github.com/zincio/universal-checkout-skill.git ~/.openclaw/skills/universal-checkout-skill
    ```

    Or at the workspace level (available only in the current project):

    ```bash theme={null}
    git clone https://github.com/zincio/universal-checkout-skill.git ./skills/universal-checkout-skill
    ```

    <Info>
      OpenClaw loads skills from three locations, in priority order: workspace (`./skills/`), user (`~/.openclaw/skills/`), and bundled (shipped with installation). Additional directories can be configured via `skills.load.extraDirs`.
    </Info>

    OpenClaw hot-reloads skills when `SKILL.md` changes, so no restart is needed after updates.
  </Tab>
</Tabs>

<Tip>
  We recommend installing the skill via GitHub to ensure you're using the latest
  version.
</Tip>

## Configuration

### API Key

The skill requires a `ZINC_API_KEY` environment variable. Set it in your shell before starting your agent:

```bash theme={null}
export ZINC_API_KEY=your-api-key
```

<Info>
  Get your API key from the

  <a href="https://app.zinc.com">
    Zinc dashboard
  </a>

  . You'll need to create an account and deposit funds to place orders.
</Info>

### OpenClaw Configuration File

If you're using OpenClaw, you can set the API key through the configuration file instead of an environment variable:

```json ~/.openclaw/openclaw.json theme={null}
{
  "skills": {
    "entries": {
      "zinc-orders": {
        "enabled": true,
        "env": {
          "ZINC_API_KEY": "your-api-key"
        }
      }
    }
  }
}
```

## Verifying the Installation

After installing, start your agent and ask it something like:

> "List my recent Zinc orders."

If the skill is loaded correctly, the agent will make a `GET /orders` request to the Zinc API and return your order history. If you see an authentication error, double-check that your `ZINC_API_KEY` is set correctly.

## Updating

To update the skill to the latest version, pull the latest changes:

```bash theme={null}
cd ./skills/universal-checkout-skill && git pull
```


# Usage Guide
Source: https://zinc-staging.vercel.app/docs/v2/agent-skills/usage

Place orders, check statuses, and manage purchases through your AI agent.

Once the Universal Checkout Skill is [installed and configured](/v2/agent-skills/setup), you can interact with the Zinc API through natural language. This guide covers the key workflows.

## Finding Products

Don't have a product URL yet? If your agent has access to [Brave Search](https://brave.com/search/api/), you can ask it to find products for you:

> "Search for a highly-rated French press coffee maker under \$40."

> "Find me a USB-C hub with at least 3 ports."

The agent will search the web, return product options with links, and you can
pick the one you'd like to order — all without leaving the conversation. This pairs
naturally with the checkout skill: search for a product, choose one, and place
the order in a single workflow.

<Tip>
  We recommeded using Brave Search as your agent search engine. It is available
  as an [MCP server](https://modelcontextprotocol.io/integrations/brave-search)
  or skill that works with Claude Code, OpenClaw, and other agent platforms.
  Install it alongside the Universal Checkout Skill for a complete
  search-to-purchase workflow.
</Tip>

## Placing an Order

To place an order, provide your agent with:

* A **product URL** from a supported retailer
* A **shipping address**
* A **maximum price** you're willing to pay (in dollars — the agent converts to cents)

**Example prompts:**

> "Search for a French press coffee maker under \$40, then order the best option. Ship it to Jane Doe, 123 Main St, San Francisco, CA 94105."

> "Buy this product: [https://www.amazon.com/dp/B0EXAMPLE](https://www.amazon.com/dp/B0EXAMPLE) — ship it to Jane Doe, 123 Main St, San Francisco, CA 94105. Don't spend more than \$50."

The agent will construct the API request and **ask for your confirmation before submitting**, since placing an order spends real money. If you start from a search query, the agent will use Brave Search to find products first, then proceed to checkout once you pick one.

### Product Variants

If the product has variants (size, color, etc.), specify them in your prompt:

> "Find a Nike Dri-FIT t-shirt in size Large and color Blue, then order it for me."

The agent will search for the product, and include the variant selections in the order request.

### Multiple Products

You can order multiple products in a single request:

> "I need 2 packs of AA batteries and 1 USB-C charging cable. Search for the best deals and order them together. Ship to..."

## Checking Order Status

Orders are processed asynchronously and typically take 5–10 minutes to complete. Ask your agent to check the status:

> "What's the status of my last order?"

> "Check the status of order `ord_abc123`."

### Order Statuses

| Status         | Meaning                                 |
| -------------- | --------------------------------------- |
| `pending`      | Order received, not yet processing      |
| `in_progress`  | Order is being placed with the retailer |
| `order_placed` | Order completed successfully            |
| `order_failed` | Order could not be completed            |
| `cancelled`    | Order was cancelled                     |

<Info>
  `order_placed`, `order_failed`, and `cancelled` are terminal statuses — the
  order will not change further. If the status is `pending` or `in_progress`,
  check again in a few minutes.
</Info>

## Listing Orders

View your recent orders:

> "List my recent Zinc orders."

> "Show me all orders from this week."

The agent will return a summary of your orders including IDs, statuses, and timestamps.

## Error Handling

If an order fails, the agent will report the error. Common issues include:

| Error                      | What to Do                                                                                  |
| -------------------------- | ------------------------------------------------------------------------------------------- |
| `max_price_exceeded`       | The product price exceeds your max price. Increase the limit or choose a different product. |
| `product_out_of_stock`     | The product is unavailable. Try again later or choose an alternative.                       |
| `invalid_shipping_address` | Double-check the address fields (state must be 2-letter code, country must be ISO alpha-2). |
| `insufficient_funds`       | Deposit more funds in your [Zinc account](https://app.zinc.com).                            |
| `product_variant_required` | The product has variants (size, color, etc.) that must be specified.                        |
| `retailer_unavailable`     | The retailer is temporarily unavailable. Try again later.                                   |

For a complete list of error codes, see the [Error Handling](/v2/api-reference/introduction/error-handling) reference.

## Tips

* **Set a reasonable max price.** This protects you from unexpected price increases. The agent will validate this before submitting.
* **Use direct product URLs.** Provide the URL of the specific product page, not a search results or category page.
* **Check status after a few minutes.** Orders are asynchronous — don't expect instant results.
* **Reading is always safe.** Listing and checking orders never costs money or changes state. Only placing a new order requires confirmation.


# Managed Accounts
Source: https://zinc-staging.vercel.app/docs/v2/api-reference/configuration/managed-accounts

Configure retailer account credentials for order processing

Managed accounts (aka retailer credentials) allow you to use your own retailer
accounts (e.g., Amazon) for order processing. This gives you control over the accounts
used to place orders and can help with order limits and account management.

## Overview

When you create retailer credentials, Zinc uses those accounts to log in and place orders on your behalf. Credentials are encrypted and stored securely.

<Info>
  If you don't configure retailer credentials, Zinc will use default internal accounts
  to process your orders.
</Info>

## Order Locking

To prevent conflicts and ensure order integrity, managed accounts are locked during order processing. Only one order can be processed at a time per managed account.

If you submit multiple orders simultaneously using the same managed account, they will be queued and processed sequentially. This prevents issues like duplicate cart items or checkout conflicts that could occur if multiple orders were placed concurrently on the same retailer account.

## Two-Factor Authentication (TOTP)

If your retailer account has two-factor authentication enabled, you must provide the TOTP secret key when creating or updating credentials.

<Info>
  Using 2FA is the most secure and reliable method for avoiding account verification issues during order processing.
</Info>

### Finding Your Amazon TOTP Key

To find your Amazon TOTP secret key:

1. Go to Amazon's Login & Security settings
2. Enable Two-Factor Authentication
3. When shown the QR code, click **"Can't scan the barcode?"**
4. Copy the displayed secret key (64 characters)

<Warning>
  The TOTP key is the 64-character secret key, NOT the 6-digit time-based code that changes every 30 seconds.
</Warning>

<Frame>
  <img alt="Amazon 2FA setup showing where to find the secret key" />
</Frame>

## Email Forwarding

Retailers like Amazon may send verification codes via email during login. To handle these
automatically, you can forward emails from your retailer account to a special Zinc email
address. Zinc will parse incoming emails and automatically extract verification codes,
so orders can proceed without manual intervention.

Each managed account is assigned a dedicated forwarding address. You can find this address
in the [Zinc dashboard](https://dash.zinc.com) under your managed account settings.

<Info>
  Once email forwarding is configured and verified, the `has_forwarding` field on your
  managed account will be set to `true`.
</Info>

### Setting Up Email Forwarding in Gmail

Rather than forwarding all incoming mail to Zinc, we recommend creating a Gmail filter
that only forwards emails from the retailer. This keeps your forwarding targeted and
avoids sending unrelated emails to Zinc.

<Steps>
  <Step title="Register the Zinc forwarding address">
    Before Gmail can forward to any address, it must be registered. Go to **Settings >
    Forwarding and POP/IMAP** and click **Add a forwarding address**. Enter the Zinc
    forwarding email address shown in your managed account settings on the
    [Zinc dashboard](https://dash.zinc.com).

    Google will send a confirmation email to the Zinc address. Zinc automatically verifies
    the forwarding request — this may take a few minutes. Once confirmed, the address will
    appear as verified in Gmail.

    <Warning>
      Do **not** enable the "Forward a copy of incoming mail to" option on this page. That
      would forward all of your email. Instead, leave it set to **Disable forwarding** and
      use a filter in the next steps to forward only retailer emails.
    </Warning>
  </Step>

  <Step title="Create a new filter">
    Go to **Settings > Filters and Blocked Addresses** and click **Create a new filter**.
  </Step>

  <Step title="Set the filter criteria">
    In the **From** field, enter the retailer's email domain. For example, for Amazon
    enter `amazon.com`. This will match all emails sent from any `@amazon.com` address.
    Leave the other fields blank and click **Create filter**.
  </Step>

  <Step title="Set the filter action">
    Check **Forward it to** and select the Zinc forwarding address from the dropdown.
    You can also check **Never send it to Spam** to make sure retailer emails aren't
    missed. Click **Create filter** to save.
  </Step>
</Steps>

<Tip>
  If you also want to forward emails that are already in your inbox (e.g., a pending
  verification code), check **Also apply filter to matching conversations** when creating
  the filter.
</Tip>

## Endpoints

| Method   | Endpoint                                                                                    | Description                        |
| -------- | ------------------------------------------------------------------------------------------- | ---------------------------------- |
| `GET`    | [`/managed-accounts`](/v2/api-reference/managed-accounts/list-managed-accounts)             | List all your retailer credentials |
| `POST`   | [`/managed-accounts`](/v2/api-reference/managed-accounts/create-managed-account)            | Create new retailer credentials    |
| `PUT`    | [`/managed-accounts/{short_id}`](/v2/api-reference/managed-accounts/update-managed-account) | Update existing credentials        |
| `DELETE` | [`/managed-accounts/{short_id}`](/v2/api-reference/managed-accounts/delete-managed-account) | Delete credentials                 |

## Create Credentials

```bash theme={null}
curl -X POST https://api.zinc.com/managed-accounts \
  -H "Authorization: Bearer <your_api_key>" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "your-amazon-email@example.com",
    "password": "your-amazon-password",
    "retailer": "amazon",
    "totp_secret": "YOUR_64_CHARACTER_SECRET_KEY"
  }'
```

### Request Fields

| Field         | Type   | Required | Description                                                                                      |
| ------------- | ------ | -------- | ------------------------------------------------------------------------------------------------ |
| `email`       | string | Yes      | The email address for the retailer account                                                       |
| `password`    | string | No       | The password for the retailer account (encrypted on storage)                                     |
| `retailer`    | string | No       | Retailer name (e.g., `amazon`). If omitted, applies as default credentials                       |
| `totp_secret` | string | No       | The secret key for two-factor authentication. Required if 2FA is enabled on the retailer account |

### Response

```json theme={null}
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "short_id": "zn_acct_a1b2c3d4",
  "email": "your-amazon-email@example.com",
  "retailer": "amazon",
  "has_totp": true,
  "created_at": "2026-01-15T10:30:00Z",
  "updated_at": "2026-01-15T10:30:00Z"
}
```

<Warning>
  Passwords and TOTP secrets are never returned in API responses. They are encrypted and stored securely. The `has_totp` field indicates whether 2FA is configured.
</Warning>

## List Credentials

```bash theme={null}
curl https://api.zinc.com/managed-accounts \
  -H "Authorization: Bearer <your_api_key>"
```

### Response

```json theme={null}
{
  "credentials": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "short_id": "zn_acct_a1b2c3d4",
      "email": "your-amazon-email@example.com",
      "retailer": "amazon",
      "has_totp": true,
      "created_at": "2026-01-15T10:30:00Z",
      "updated_at": "2026-01-15T10:30:00Z"
    }
  ],
  "total": 1
}
```

## Update Credentials

Use the `short_id` from the credentials response to update:

```bash theme={null}
curl -X PUT https://api.zinc.com/managed-accounts/zn_acct_a1b2c3d4 \
  -H "Authorization: Bearer <your_api_key>" \
  -H "Content-Type: application/json" \
  -d '{
    "password": "new-password"
  }'
```

### Request Fields

All fields are optional. Only provided fields are updated.

| Field         | Type   | Description               |
| ------------- | ------ | ------------------------- |
| `email`       | string | New email address         |
| `password`    | string | New password              |
| `retailer`    | string | New retailer association  |
| `totp_secret` | string | Update the 2FA secret key |

## Delete Credentials

```bash theme={null}
curl -X DELETE https://api.zinc.com/managed-accounts/zn_acct_a1b2c3d4 \
  -H "Authorization: Bearer <your_api_key>"
```

Returns `204 No Content` on success.

## Response Fields

| Field            | Type              | Description                                                 |
| ---------------- | ----------------- | ----------------------------------------------------------- |
| `id`             | string (UUID)     | Unique identifier                                           |
| `short_id`       | string            | Short identifier used in URLs (e.g., `zn_acct_a1b2c3d4`)    |
| `email`          | string            | Retailer account email                                      |
| `retailer`       | string or null    | Retailer name, or null if default credentials               |
| `has_totp`       | boolean           | Whether TOTP 2FA is configured for this account             |
| `has_forwarding` | boolean           | Whether email forwarding has been verified for this account |
| `created_at`     | string (ISO 8601) | When the credentials were created                           |
| `updated_at`     | string (ISO 8601) | When the credentials were last updated                      |

## Best Practices

1. **Use dedicated accounts** - Create retailer accounts specifically for Zinc orders to avoid conflicts with personal orders

2. **Monitor account health** - Retailer accounts can be locked if flagged for unusual activity. Check for `login_failed` or `account_locked` errors

3. **Keep credentials updated** - If you change your retailer account password, update it here to avoid order failures

4. **Enable 2FA** - Two-factor authentication prevents account lockouts from verification challenges and is the most reliable method for automated ordering


# Authentication
Source: https://zinc-staging.vercel.app/docs/v2/api-reference/introduction/authentication

How to authenticate with the Zinc API

To use the Zinc API, you must authenticate every request with your API key.

<Info>
  You can find your API key in your <a href="https://app.zinc.com">Zinc dashboard</a> after creating an account.
</Info>

## Example Authentication Request

```bash theme={null}
curl https://api.zinc.com/orders \
  -H "Authorization: Bearer <your_api_key>"
```

Authentication is performed using **Bearer token authentication**.

* Include your API key in the `Authorization` header
* Format: `Authorization: Bearer <your_api_key>`

<Warning>
  Never share your API key or expose it in public repositories, client-side code, or other insecure locations. Your API key is tied to your account, and you are responsible for all requests made with it.
</Warning>

If you believe your API key has been compromised, please contact [support@zinc.com](mailto:support@zinc.com) immediately.


# Error Handling
Source: https://zinc-staging.vercel.app/docs/v2/api-reference/introduction/error-handling

Understanding error responses from the Zinc API

The Zinc API uses conventional HTTP response codes to indicate the success or failure of an API request.

## HTTP Status Codes

| Status Code | Description                                                   |
| ----------- | ------------------------------------------------------------- |
| `200`       | Success - The request was successful                          |
| `201`       | Created - A new resource was created successfully             |
| `400`       | Bad Request - The request was malformed or invalid            |
| `401`       | Unauthorized - Invalid or missing authentication              |
| `402`       | Payment Required - Payment or wallet issue                    |
| `403`       | Forbidden - You don't have permission to access this resource |
| `404`       | Not Found - The requested resource does not exist             |
| `409`       | Conflict - Resource already exists                            |
| `422`       | Unprocessable Entity - Validation error                       |
| `500`       | Internal Server Error - Something went wrong on our end       |
| `502`       | Bad Gateway - External service error                          |

## Error Response Format

All error responses follow a consistent structure:

```json theme={null}
{
  "code": "error_code",
  "message": "Human-readable error message",
  "details": {
    "field": "Additional context about the error"
  }
}
```

## API Error Codes

### General Errors

| Error Code         | Description                                                              |
| ------------------ | ------------------------------------------------------------------------ |
| `not_found`        | Resource was not found                                                   |
| `validation_error` | A parameter was incorrect or missing. Check details for more information |
| `bad_request`      | The request was malformed or invalid                                     |
| `already_exists`   | Resource already exists (e.g., duplicate idempotency key)                |
| `internal_error`   | Something went wrong with our internal systems                           |

#### Example

```json theme={null}
{
  "code": "validation_error",
  "message": "Invalid request parameters",
  "details": {
    "products": "At least one product is required"
  }
}
```

### Authentication Errors

| Error Code      | Description                                |
| --------------- | ------------------------------------------ |
| `unauthorized`  | Authentication is required for this action |
| `forbidden`     | You do not have permission for this action |
| `invalid_token` | Your API token is invalid                  |
| `token_expired` | Your API token has expired                 |

#### Example

```json theme={null}
{
  "code": "invalid_token",
  "message": "The provided API token is not valid"
}
```

### Wallet & Payment Errors

| Error Code                | Description                                |
| ------------------------- | ------------------------------------------ |
| `insufficient_funds`      | Insufficient funds in wallet for the order |
| `payment_failed`          | Payment operation failed                   |
| `payment_method_required` | No default payment method configured       |
| `invalid_payment_method`  | The provided payment method is invalid     |

#### Example

```json theme={null}
{
  "code": "insufficient_funds",
  "message": "Your wallet balance is insufficient for this order",
  "details": {
    "required": 4999,
    "available": 1000
  }
}
```

### Order Request Errors

| Error Code                 | Description                                               |
| -------------------------- | --------------------------------------------------------- |
| `invalid_shipping_address` | The shipping address failed validation                    |
| `url_unreachable`          | The product URL provided is inaccessible                  |
| `invalid_variant`          | Product variant not provided or not found on product page |
| `out_of_stock`             | Product is not currently available for purchase           |
| `shipping_unavailable`     | Shipping to this address is not available                 |
| `non_us_retailer`          | Only US retailer sites are supported                      |
| `order_not_cancellable`    | Order cannot be cancelled due to its current status       |

#### Example

```json theme={null}
{
  "code": "invalid_shipping_address",
  "message": "The shipping address could not be validated",
  "details": {
    "field": "postal_code",
    "reason": "Postal code does not match city/state"
  }
}
```

### External Service Errors

| Error Code               | Description                     |
| ------------------------ | ------------------------------- |
| `external_service_error` | An external service call failed |

#### Example

```json theme={null}
{
  "code": "external_service_error",
  "message": "Unable to connect to external service. Please try again."
}
```

## Order Processing Errors

When an order fails during processing, the `error_type` field in the order response or webhook payload contains one of these codes:

### Product Errors

| Error Type                     | Description                                  |
| ------------------------------ | -------------------------------------------- |
| `product_not_found`            | Product page doesn't exist or was removed    |
| `product_out_of_stock`         | Product is out of stock                      |
| `product_unavailable`          | Product exists but cannot be purchased       |
| `invalid_product_url`          | URL is malformed or not a valid product page |
| `product_variant_required`     | Product requires a variant selection         |
| `product_variant_unavailable`  | Selected variant is not available            |
| `product_quantity_unavailable` | Requested quantity is not available          |

#### Example

```json theme={null}
{
  "event": "order.failed",
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "failed",
  "timestamp": "2026-01-15T14:30:00Z",
  "data": {
    "error_type": "product_out_of_stock",
    "error": "The requested product is currently out of stock"
  }
}
```

### Price Errors

| Error Type           | Description                               |
| -------------------- | ----------------------------------------- |
| `max_price_exceeded` | Total price exceeds the `max_price` limit |

#### Example

```json theme={null}
{
  "event": "order.failed",
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "failed",
  "timestamp": "2026-01-15T14:30:00Z",
  "data": {
    "error_type": "max_price_exceeded",
    "error": "Order total of $52.99 exceeds max_price of $50.00"
  }
}
```

### Cart & Checkout Errors

| Error Type           | Description                                    |
| -------------------- | ---------------------------------------------- |
| `add_to_cart_failed` | Could not add product to cart                  |
| `cart_empty`         | Cart became empty during checkout              |
| `checkout_blocked`   | Checkout blocked (captcha, verification, etc.) |
| `checkout_failed`    | Generic checkout failure                       |

#### Example

```json theme={null}
{
  "event": "order.failed",
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "failed",
  "timestamp": "2026-01-15T14:30:00Z",
  "data": {
    "error_type": "checkout_blocked",
    "error": "Checkout requires additional verification"
  }
}
```

### Shipping Errors

| Error Type                    | Description                                |
| ----------------------------- | ------------------------------------------ |
| `shipping_address_invalid`    | Address validation failed on retailer site |
| `shipping_unavailable`        | Cannot ship to the given address           |
| `shipping_method_unavailable` | No shipping methods available              |

#### Example

```json theme={null}
{
  "event": "order.failed",
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "failed",
  "timestamp": "2026-01-15T14:30:00Z",
  "data": {
    "error_type": "shipping_unavailable",
    "error": "This item cannot be shipped to the selected address"
  }
}
```

### Payment Errors

| Error Type               | Description                      |
| ------------------------ | -------------------------------- |
| `payment_declined`       | Payment was declined by retailer |
| `payment_method_invalid` | Payment method not accepted      |
| `payment_failed`         | Generic payment failure          |

#### Example

```json theme={null}
{
  "event": "order.failed",
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "failed",
  "timestamp": "2026-01-15T14:30:00Z",
  "data": {
    "error_type": "payment_declined",
    "error": "The payment method was declined by the retailer"
  }
}
```

### Account Errors

| Error Type                      | Description                             |
| ------------------------------- | --------------------------------------- |
| `login_failed`                  | Could not log into retailer account     |
| `session_expired`               | Session expired during checkout         |
| `account_locked`                | Retailer account is locked or suspended |
| `account_verification_required` | Account needs verification              |

#### Example

```json theme={null}
{
  "event": "order.failed",
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "failed",
  "timestamp": "2026-01-15T14:30:00Z",
  "data": {
    "error_type": "login_failed",
    "error": "Unable to authenticate with retailer account"
  }
}
```

### Retailer Errors

| Error Type               | Description                              |
| ------------------------ | ---------------------------------------- |
| `retailer_unavailable`   | Retailer website is down or inaccessible |
| `retailer_not_supported` | Retailer is not supported                |
| `retailer_rate_limited`  | Rate limited by retailer                 |

#### Example

```json theme={null}
{
  "event": "order.failed",
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "failed",
  "timestamp": "2026-01-15T14:30:00Z",
  "data": {
    "error_type": "retailer_unavailable",
    "error": "The retailer website is currently unavailable"
  }
}
```

### Quantity Limit Errors

| Error Type                | Description                           |
| ------------------------- | ------------------------------------- |
| `quantity_limit_exceeded` | Retailer has purchase quantity limits |
| `order_limit_exceeded`    | Account has reached order limits      |

#### Example

```json theme={null}
{
  "event": "order.failed",
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "failed",
  "timestamp": "2026-01-15T14:30:00Z",
  "data": {
    "error_type": "quantity_limit_exceeded",
    "error": "Maximum purchase quantity for this item is 3"
  }
}
```


# Sandbox & Testing
Source: https://zinc-staging.vercel.app/docs/v2/api-reference/introduction/sandbox

Test your integration without placing real orders

The Zinc API provides a sandbox environment for testing your integration without placing real orders or incurring charges. Test mode uses isolated data and simulates various order scenarios.

## Enabling Test Mode

Use an API key with the `zn_test_` prefix:

```bash theme={null}
curl https://api.zinc.com/orders \
  -H "Authorization: Bearer zn_test_abc123..."
```

<Info>
  Test mode uses a separate sandbox database. Orders created in test mode are
  completely isolated from production data.
</Info>

## Test Products

Use these special product URLs to simulate different order scenarios:

| Product URL                                                | Scenario             | Description                       |
| ---------------------------------------------------------- | -------------------- | --------------------------------- |
| `https://zinc.com/shop/products/test-success`              | Success              | Order completes successfully      |
| `https://zinc.com/shop/products/test-out-of-stock`         | Out of Stock         | Product is unavailable            |
| `https://zinc.com/shop/products/test-price-exceeded`       | Price Exceeded       | Total exceeds `max_price`         |
| `https://zinc.com/shop/products/test-invalid-address`      | Invalid Address      | Shipping address validation fails |
| `https://zinc.com/shop/products/test-url-unreachable`      | URL Unreachable      | Product URL is inaccessible       |
| `https://zinc.com/shop/products/test-invalid-variant`      | Invalid Variant      | Variant selection required        |
| `https://zinc.com/shop/products/test-shipping-unavailable` | Shipping Unavailable | Cannot ship to address            |
| `https://zinc.com/shop/products/test-insufficient-funds`   | Insufficient Funds   | Wallet balance too low            |

### Get Test Products Programmatically

```bash theme={null}
curl https://api.zinc.com/orders/test-products \
  -H "Authorization: Bearer <your_api_key>"
```

#### Response

```json theme={null}
{
  "products": [
    {
      "url": "https://zinc.com/shop/products/test-success",
      "scenario": "success",
      "name": "Success",
      "is_synchronous_error": false
    },
    {
      "url": "https://zinc.com/shop/products/test-invalid-address",
      "scenario": "invalid_address",
      "name": "Invalid Address",
      "is_synchronous_error": true
    }
  ]
}
```

## Error Timing

Test scenarios produce errors at different stages:

### Synchronous Errors

These errors occur immediately when creating the order:

* `test-invalid-address` - Returns `invalid_shipping_address` error
* `test-url-unreachable` - Returns `url_unreachable` error
* `test-insufficient-funds` - Returns `insufficient_funds` error

#### Example

```bash theme={null}
curl -X POST https://api.zinc.com/orders \
  -H "Authorization: Bearer zn_test_abc123..." \
  -H "Content-Type: application/json" \
  -d '{
    "products": [{"url": "https://zinc.com/shop/products/test-invalid-address"}],
    "shipping_address": {...},
    "max_price": 5000
  }'
```

```json theme={null}
{
  "code": "invalid_shipping_address",
  "message": "The shipping address failed validation (test scenario)"
}
```

### Asynchronous Errors

These errors occur during order processing and are delivered via webhooks:

* `test-out-of-stock` - Order fails with `product_out_of_stock`
* `test-price-exceeded` - Order fails with `max_price_exceeded`
* `test-invalid-variant` - Order fails with `invalid_variant`
* `test-shipping-unavailable` - Order fails with `shipping_unavailable`

The order is created successfully, but transitions to `failed` status during processing.

## Test Success Scenario

The `test-success` product simulates a complete successful order:

```bash theme={null}
curl -X POST https://api.zinc.com/orders \
  -H "Authorization: Bearer zn_test_abc123..." \
  -H "Content-Type: application/json" \
  -d '{
    "products": [{"url": "https://zinc.com/shop/products/test-success"}],
    "shipping_address": {
      "name": "John Smith",
      "address_line_1": "123 Main Street",
      "city": "Seattle",
      "state": "WA",
      "postal_code": "98101",
      "country": "US",
      "phone": "206-555-0100"
    },
    "max_price": 5000
  }'
```

### Successful Test Order Response

When retrieved after processing:

```json theme={null}
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "order_placed",
  "merchant_order_id": "TEST-550e8400",
  "tracking_numbers": [
    {
      "carrier": "usps",
      "tracking_number": "ZINC_TEST_123456789"
    }
  ],
  "price_components": {
    "subtotal": 4500,
    "tax": 250,
    "shipping": 150,
    "total": 4900
  }
}
```

## Skipped Validations

In test mode, the following validations are bypassed to simplify testing:

* Wallet balance checks
* US retailer URL validation
* URL reachability validation
* Shipping address country validation
* Address verification via external APIs

<Warning>
  Test mode behavior differs from production. Always perform final testing with
  real orders before going live.
</Warning>

## Data Isolation

Test mode data is completely isolated:

* Orders created in test mode are stored in a sandbox database
* Test orders do not appear in production order lists
* Production orders do not appear in test mode
* Wallet balances are separate between test and production

## Best Practices

1. **Start with test mode** - Build and test your entire integration using test products before switching to production

2. **Test all scenarios** - Use each test product to verify your error handling works correctly

3. **Test webhooks** - Configure webhooks and verify you receive events for both successful and failed test orders

4. **Verify error handling** - Ensure your application gracefully handles both synchronous and asynchronous errors

5. **Use consistent mode** - Don't mix test and production API keys in the same environment


# Create Managed Account
Source: https://zinc-staging.vercel.app/docs/v2/api-reference/managed-accounts/create-managed-account

versions/latest.json post /managed-accounts
Create new retailer credentials

Create new retailer credentials for order processing. Credentials are encrypted and stored securely.

## Request Fields

* **email** (required) - The email address for the retailer account
* **password** - The password for the retailer account (encrypted at rest)
* **retailer** - Retailer name (e.g., `amazon`). If omitted, applies as default credentials
* **totp\_secret** - TOTP secret key for two-factor authentication (encrypted at rest)

<Info>
  If your retailer account has 2FA enabled, you must provide the `totp_secret` to avoid verification issues during order processing. See the [Managed Accounts guide](/v2/api-reference/configuration/managed-accounts#two-factor-authentication-totp) for details on finding your TOTP key.
</Info>

## Response

Returns the created credential object with:

* **id** - Unique identifier (UUID)
* **short\_id** - Short identifier used in URLs (e.g., `zn_acct_a1b2c3d4`)
* **email** - Retailer account email
* **retailer** - Retailer name, or null if default credentials
* **has\_totp** - Whether TOTP 2FA is configured
* **has\_forwarding** - Whether email forwarding has been verified
* **created\_at** - Creation timestamp
* **updated\_at** - Last update timestamp

<Warning>
  Passwords and TOTP secrets are never returned in API responses. The `has_totp` field indicates whether 2FA is configured.
</Warning>


# Delete Managed Account
Source: https://zinc-staging.vercel.app/docs/v2/api-reference/managed-accounts/delete-managed-account

versions/latest.json delete /managed-accounts/{short_id}
Delete retailer credentials

Permanently delete retailer credentials. This action cannot be undone.

## Path Parameters

* **short\_id** (required) - The short identifier of the credentials to delete (e.g., `zn_acct_a1b2c3d4`)

<Warning>
  Deleting credentials that are actively in use by a processing order may cause the order to fail. Ensure no orders are currently processing with these credentials before deleting.
</Warning>


# List Managed Accounts
Source: https://zinc-staging.vercel.app/docs/v2/api-reference/managed-accounts/list-managed-accounts

versions/latest.json get /managed-accounts
List all retailer credentials for your account

Retrieve a list of all retailer credentials associated with your account.

## Response

Returns an object containing:

* **credentials** - Array of retailer credential objects
* **total** - Total number of credentials

Each credential includes:

* **id** - Unique identifier (UUID)
* **short\_id** - Short identifier used in URLs (e.g., `zn_acct_a1b2c3d4`)
* **email** - Retailer account email
* **retailer** - Retailer name, or null if default credentials
* **has\_totp** - Whether TOTP 2FA is configured
* **has\_forwarding** - Whether email forwarding has been verified
* **created\_at** - When the credentials were created
* **updated\_at** - When the credentials were last updated


# Update Managed Account
Source: https://zinc-staging.vercel.app/docs/v2/api-reference/managed-accounts/update-managed-account

versions/latest.json put /managed-accounts/{short_id}
Update existing retailer credentials

Update an existing managed account's retailer credentials. Only provided fields are updated.

## Path Parameters

* **short\_id** (required) - The short identifier of the credentials to update (e.g., `zn_acct_a1b2c3d4`)

## Request Fields

All fields are optional. Only provided fields are updated.

* **email** - New email address
* **password** - New password (encrypted at rest)
* **retailer** - New retailer association
* **totp\_secret** - Update the 2FA secret key (encrypted at rest)

## Response

Returns the updated credential object.


# Order Tracking
Source: https://zinc-staging.vercel.app/docs/v2/api-reference/order-updates/tracking

How to retrieve tracking information for your orders

Once an order has been placed with a retailer, tracking information becomes available as shipments are dispatched. Tracking numbers are automatically extracted from retailer shipping notifications and associated with your order.

## How Tracking Works

1. Your order is successfully placed with the retailer
2. The retailer ships the item and sends a shipping notification
3. We automatically extract tracking numbers from the notification
4. Tracking information appears in the order response

<Info>
  Tracking numbers are added to orders automatically. There is no separate endpoint to create or manage tracking numbers.
</Info>

## Tracking in Order Response

Tracking information is returned as part of the order response when you retrieve an order:

```json theme={null}
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "order_placed",
  "tracking_numbers": [
    {
      "id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
      "carrier": "ups",
      "tracking_number": "1Z999AA10123456784",
      "created_at": "2026-01-15T14:30:00Z"
    }
  ],
  ...
}
```

### Tracking Number Fields

| Field             | Type              | Description                                     |
| ----------------- | ----------------- | ----------------------------------------------- |
| `id`              | string (UUID)     | Unique identifier for the tracking record       |
| `carrier`         | string            | Shipping carrier (see supported carriers below) |
| `tracking_number` | string            | The carrier's tracking number                   |
| `created_at`      | string (ISO 8601) | When the tracking number was extracted          |

## Supported Carriers

The following carriers are automatically detected:

| Carrier          | `carrier` value | Example Format           |
| ---------------- | --------------- | ------------------------ |
| UPS              | `ups`           | `1Z999AA10123456784`     |
| FedEx            | `fedex`         | `123456789012`           |
| USPS             | `usps`          | `9400111899223033005001` |
| Amazon Logistics | `amazon`        | `TBA123456789000`        |
| DHL              | `dhl`           | `1234567890`             |

## Multiple Tracking Numbers

An order may have multiple tracking numbers if:

* Items ship separately from the retailer
* Multiple products in the order ship from different fulfillment centers

```json theme={null}
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "order_placed",
  "tracking_numbers": [
    {
      "id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
      "carrier": "ups",
      "tracking_number": "1Z999AA10123456784",
      "created_at": "2026-01-15T14:30:00Z"
    },
    {
      "id": "8d0f7780-8536-51ef-055c-f18fd2g01bf8",
      "carrier": "amazon",
      "tracking_number": "TBA123456789000",
      "created_at": "2026-01-16T09:15:00Z"
    }
  ]
}
```

## Tracking Links

You can construct tracking URLs for each carrier:

| Carrier | Tracking URL                                                                    |
| ------- | ------------------------------------------------------------------------------- |
| UPS     | `https://www.ups.com/track?tracknum={tracking_number}`                          |
| FedEx   | `https://www.fedex.com/fedextrack/?trknbr={tracking_number}`                    |
| USPS    | `https://tools.usps.com/go/TrackConfirmAction?tLabels={tracking_number}`        |
| Amazon  | `https://www.amazon.com/progress-tracker/package/?trackingId={tracking_number}` |
| DHL     | `https://www.dhl.com/us-en/home/tracking.html?tracking-id={tracking_number}`    |

## When Tracking Is Available

Tracking numbers appear after the order status changes to `order_placed` and the retailer has shipped the item. The timing depends on:

* Retailer processing time
* Shipping method selected
* Product availability

<Warning>
  Tracking numbers may not be available immediately after an order is placed. Check the order periodically to retrieve tracking information once items have shipped.
  Webhook events for tracking and shipping notifications are coming soon.
</Warning>


# Webhooks
Source: https://zinc-staging.vercel.app/docs/v2/api-reference/order-updates/webhooks

Receive real-time notifications about order events

Webhooks allow you to receive real-time HTTP notifications when events occur on your orders. Instead of polling the API for updates, configure a webhook URL to receive automatic notifications.

## Configuration

Configure your webhook URL in the [Zinc dashboard](https://app.zinc.com) under Settings. You can also generate a webhook secret for signature verification.

### Webhook Secret

Your webhook secret is used to verify that incoming webhook requests are from Zinc. The secret format is:

```
zn_whsec_XXXXXXXXXXXXXXXXXXXXXXXX
```

<Warning>
  Keep your webhook secret secure. If compromised, rotate it immediately in the dashboard. Rotating the secret invalidates the previous one.
</Warning>

## Events

Zinc sends webhooks for the following order events:

| Event           | Description                                          |
| --------------- | ---------------------------------------------------- |
| `order.started` | Order has been created and queued for processing     |
| `order.placed`  | Order was successfully placed with the retailer      |
| `order.failed`  | Order failed after all retry attempts were exhausted |

## Payload Structure

All webhook payloads follow this structure:

```json theme={null}
{
  "event": "order.placed",
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "order_placed",
  "timestamp": "2026-01-15T14:30:00Z",
  "data": {}
}
```

### Payload Fields

| Field       | Type              | Description                                                            |
| ----------- | ----------------- | ---------------------------------------------------------------------- |
| `event`     | string            | The event type (e.g., `order.started`, `order.placed`, `order.failed`) |
| `order_id`  | string            | The UUID of the order                                                  |
| `status`    | string            | Current order status                                                   |
| `timestamp` | string (ISO 8601) | When the event occurred                                                |
| `data`      | object            | Additional event-specific data                                         |

### Event-Specific Data

**`order.placed`** includes price components:

```json theme={null}
{
  "event": "order.placed",
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "order_placed",
  "timestamp": "2026-01-15T14:30:00Z",
  "data": {
    "price_components": {
      "subtotal": 1999,
      "shipping": 499,
      "tax": 150,
      "total": 2648
    }
  }
}
```

**`order.failed`** includes error information:

```json theme={null}
{
  "event": "order.failed",
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "failed",
  "timestamp": "2026-01-15T14:30:00Z",
  "data": {
    "error_type": "product_not_found",
    "error": "The product is no longer available"
  }
}
```

## Security

Webhook requests include headers for verification:

| Header                | Description                          |
| --------------------- | ------------------------------------ |
| `Content-Type`        | Always `application/json`            |
| `X-Webhook-Signature` | HMAC-SHA256 signature of the payload |
| `X-Webhook-Event`     | The event type                       |

### Verifying Signatures

To verify a webhook is from Zinc, compute the HMAC-SHA256 signature of the raw request body using your webhook secret and compare it to the `X-Webhook-Signature` header.

**Python Example:**

```python theme={null}
import hmac
import hashlib

def verify_webhook(payload: bytes, signature: str, secret: str) -> bool:
    expected = hmac.new(
        secret.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, signature)

# In your webhook handler
@app.post("/webhook")
async def handle_webhook(request: Request):
    payload = await request.body()
    signature = request.headers.get("X-Webhook-Signature")

    if not verify_webhook(payload, signature, WEBHOOK_SECRET):
        raise HTTPException(status_code=401, detail="Invalid signature")

    data = json.loads(payload)
    # Process the webhook event
```

**Node.js Example:**

```javascript theme={null}
const crypto = require('crypto');

function verifyWebhook(payload, signature, secret) {
  const expected = crypto
    .createHmac('sha256', secret)
    .update(payload)
    .digest('hex');
  return crypto.timingSafeEqual(
    Buffer.from(expected),
    Buffer.from(signature)
  );
}

// In your webhook handler
app.post('/webhook', (req, res) => {
  const signature = req.headers['x-webhook-signature'];

  if (!verifyWebhook(req.rawBody, signature, WEBHOOK_SECRET)) {
    return res.status(401).send('Invalid signature');
  }

  const event = req.body;
  // Process the webhook event
});
```

<Info>
  Always verify webhook signatures before processing the payload to ensure the request originated from Zinc.
</Info>

## Best Practices

1. **Respond quickly** - Return a 2xx status code as soon as possible. Process the webhook asynchronously if needed.

2. **Handle duplicates** - Webhooks may occasionally be delivered more than once. Use the `order_id` to deduplicate.

3. **Verify signatures** - Always validate the `X-Webhook-Signature` header before trusting the payload.

4. **Use HTTPS** - Configure an HTTPS endpoint to ensure webhook data is encrypted in transit.

5. **Log events** - Keep records of received webhooks for debugging and auditing.


# Create Order
Source: https://zinc-staging.vercel.app/docs/v2/api-reference/orders/create-order

versions/latest.json post /orders
Create a new order

Create a new order for processing. Orders are queued and processed asynchronously.

## Request Flow

1. **Submit Order** - Send order details including products and shipping address
2. **Validation** - We validate product URLs and shipping address
3. **Queued** - Order is queued for processing
4. **Processing** - Our system places the order with the retailer
5. **Completed** - You receive confirmation with tracking details

<Frame>
  <img alt="Order flow diagram" />
</Frame>

## Product URLs

Provide direct product URLs from supported retailers. Each product must include:

* **url** - Direct link to the product page

<Info>
  Make sure product URLs are accessible and lead directly to the product page, not search results or category pages.
</Info>

Optionally, the product can include:

* **quantity** - Number of items to order (integer, default 1)
* **variant** - A list of label, value pairs indicating a variant of a product.
  For example, if you're ordering a shirt. The shirt may come in different colors and different sizes.
  To indicate a red medium shirt, you would do:
  ```
  [
    {
      "label": "Color",
      "value": "Red"
    },
    {
      "label": "Size",
      "value": "Medium"
    }
  ]
  ```
  <Info>
    Make sure the strings used for both the label and value match up to what is
    present on the retailer website. For example, if a `medium` is indicated by the value `M`, use `M`
    for the value.
  </Info>

## Shipping Address

All orders require a valid US shipping address. Addresses are validated using Google's Address Validation API.

Required fields:

* Name
* Street address
* City
* State (2-letter code)
* Postal code
* Phone number
* Country (must be "US")

<Warning>
  We currently only support shipping to addresses in the United States.
</Warning>

## Optional Order Data

You can include additional data with your order for tracking and reference purposes.
This data *will* be used by our system as as input to any fields during checkout that match.

* **po\_number** - Your internal purchase order number for tracking and reconciliation

<Tip>
  If you only need data for internal reference, use the `metadata` field instead.
</Tip>

## Response

A successful order creation returns:

* **id** - Unique order identifier (UUID)
* **status** - Current order status (initially "pending")
* **items** - Array of order items with their details
* **shipping\_address** - Confirmed shipping address
* **created\_at** - Timestamp of order creation

Use the order `id` to retrieve order status and updates.


# Get Order
Source: https://zinc-staging.vercel.app/docs/v2/api-reference/orders/get-order

versions/latest.json get /orders/{order_id}
Retrieve a specific order by ID

Retrieve detailed information about a specific order using its unique identifier.

## Path Parameters

* **order\_id** (required) - The UUID of the order to retrieve

## Response

Returns a complete order object with:

* **id** - Order UUID
* **status** - Current order status
* **items** - Array of order items with individual statuses
* **shipping\_address** - Delivery address
* **job\_result** - Detailed processing results (when available)
* **created\_at** - Order creation timestamp
* **updated\_at** - Last update timestamp

## Item-Level Status

Each item in the order has its own status tracking:

```json theme={null}
{
  "id": "item-uuid",
  "url": "https://www.amazon.com/...",
  "quantity": 2,
  "status": "shipped",
  "created_at": "2025-11-24T10:00:00Z",
  "updated_at": "2025-11-24T12:30:00Z"
}
```

## Job Results

For completed or failed orders, the `job_result` field contains detailed information about the order processing, including:

* Success/failure status
* Retailer confirmation numbers
* Tracking information
* Error details (if failed)

<Tip>
  Poll this endpoint to track order progress. We recommend checking every 30-60 seconds while the order is processing.
</Tip>

## Error Responses

* **404 Not Found** - Order ID does not exist or you don't have access to it
* **401 Unauthorized** - Invalid or missing authentication


# List Orders
Source: https://zinc-staging.vercel.app/docs/v2/api-reference/orders/list-orders

versions/latest.json get /orders
Retrieve all orders for your account

Retrieve a list of all orders associated with your account. Orders are returned in reverse chronological order (most recent first).

## Response

Returns an array of order objects, each containing:

* **id** - Order UUID
* **status** - Current order status
* **items** - Products in the order
* **shipping\_address** - Delivery address
* **job\_result** - Processing results (for completed/failed orders)
* **created\_at** - Order creation timestamp
* **updated\_at** - Last update timestamp

## Order Statuses

| Status        | Description                        |
| ------------- | ---------------------------------- |
| `pending`     | Order queued, not yet processing   |
| `in_progress` | Order is being placed              |
| `ordered`     | Successfully placed with retailer  |
| `shipped`     | Order shipped (tracking available) |
| `delivered`   | Order delivered to address         |
| `cancelled`   | Order was cancelled                |
| `failed`      | Order processing failed            |

## Pagination

<Info>
  Currently, all orders are returned in a single response. Pagination will be added in a future update.
</Info>


# Multiple Products & Quantities
Source: https://zinc-staging.vercel.app/docs/v2/api-reference/orders/multiple-products-quantities

How to order multiple products and specify quantities in a single API request

The Zinc API allows you to order multiple products in a single request and specify quantities for each item.

## Products Array

The `products` array in your order request accepts multiple `OrderProduct` objects. Each product is processed as part of the same order.

<Warning>
  All products in an order must be from the same retailer. You cannot mix products from different retailers in a single order request.
</Warning>

```json theme={null}
{
  "products": [
    {
      "url": "https://www.amazon.com/dp/B07JGBW826"
    },
    {
      "url": "https://www.amazon.com/dp/B09V3KXJPB"
    }
  ],
  "shipping_address": { ... },
  "max_price": 5000
}
```

## Setting Quantities

Each product can include a `quantity` field to specify how many units to order. What
will be accepted by the retailer depends on the product and availability. We will return
an error code, `product_quantity_not_available` if we are unable to purchase the amount
specified.

* **Range**: 1 to 100
* **Default**: 1 (if omitted)

```json theme={null}
{
  "products": [
    {
      "url": "https://www.amazon.com/dp/B07JGBW826",
      "quantity": 3
    }
  ],
  "shipping_address": { ... },
  "max_price": 3000
}
```

## Combining with Variants

When ordering products with variants (size, color, etc.), you can combine the `variant` array with `quantity`:

```json theme={null}
{
  "products": [
    {
      "url": "https://www.amazon.com/dp/B07JGBW826",
      "quantity": 2,
      "variant": [
        {
          "label": "Color",
          "value": "Black"
        },
        {
          "label": "Size",
          "value": "Large"
        }
      ]
    }
  ],
  "shipping_address": { ... },
  "max_price": 4000
}
```

## Complete Example

Here's an example ordering multiple products with different quantities and variants:

```json theme={null}
{
  "products": [
    {
      "url": "https://www.amazon.com/dp/B07JGBW826",
      "quantity": 2,
      "variant": [
        {
          "label": "Color",
          "value": "Navy"
        }
      ]
    },
    {
      "url": "https://www.amazon.com/dp/B09V3KXJPB",
      "quantity": 1
    },
    {
      "url": "https://www.amazon.com/dp/B08N5WRWNW",
      "quantity": 3,
      "variant": [
        {
          "label": "Size",
          "value": "Medium"
        }
      ]
    }
  ],
  "shipping_address": {
    "name": "John Smith",
    "address_line_1": "123 Main Street",
    "city": "Seattle",
    "state": "WA",
    "postal_code": "98101",
    "country": "US",
    "phone": "206-555-0100"
  },
  "max_price": 15000
}
```

## Max Price Considerations

The `max_price` field applies to the **total order amount** across all products and quantities combined.

<Warning>
  If the total order cost (including all products, quantities, taxes, and shipping) exceeds `max_price`, the order will fail with an error. Set your `max_price` high enough to account for the full order total.
</Warning>

When calculating `max_price`, consider:

* Unit price × quantity for each product
* Applicable taxes
* Shipping costs
* Any additional fees


# Migrating from V1
Source: https://zinc-staging.vercel.app/docs/v2/migrating-from-v1

Frequently asked questions about V2

**Is Zinc 1.0 going away?**

No. Zinc 1.0 (dash.zinc.io) is staying live and unchanged. If it's working for you, nothing changes.

**What's different about 2.0?**

Zinc 2.0 is a completely new system: A new dashboard (app.zinc.com), new API, & new account. We rebuilt everything leveraging AI, which lets us support way more retailers than before.

**Can I use my existing account/API keys?**

No. 2.0 requires a new account and new API keys. Your 1.0 credentials won't carry over. It’s super-easy to get started.

**How is pricing different?**

2.0 combines Zinc Managed Accounts funding and API fees into one system. You add funds to your wallet and everything is handled from there. You’ll be able to track every transaction and fee just like before.

**What features does 2.0 have that 1.0 doesn't?**

More retailers, and soon, more flexibility in what you can do on those retailers (eg. picking different delivery options, etc.)

**What features does 1.0 have that 2.0 doesn't have yet?**

Returns and cancellations. We're shipping these in the coming weeks.

**Should I switch to 2.0?**

If you need returns or cancellations today for mission-critical purchasing — stick with 1.0 for now. If you're starting something new and want access to more retailers via guest checkout, 2.0 is ready. The sooner you move to 2.0, the more we’ll prioritize your specific needs faster!

**I have more questions.**

[Email Ian](mailto:ian@zinc.com) or [book time with Ian directly](https://cal.com/zinc-ian/15min)


# What is Zinc?
Source: https://zinc-staging.vercel.app/docs/what-is-zinc

Zinc is building the universal API for ecommerce automation. With a single integration, you can buy products, retrieve pricing and product data, and automate order management across the world's top online retailers.

<Info>
  **Zinc 2.0 is in active development.** We're rebuilding from the ground up with AI to support dramatically more retailers and flexibility. Some features from v1 (account automation, tracking, returns, cancellations) are coming soon. For production use cases requiring these features today, see [v1 documentation](/v1/quickstart).
</Info>

## Why Zinc?

* **Universal API:** We're building one consistent, modern API to access millions of products across retailers worldwide.
* **Simplified Ordering:** Place orders across a growing list of retailers with a unified interface.
* **Developer-First:** Clear documentation, fast onboarding, and responsive support.

## Who Uses Zinc?

* **Cross Border:** Enable global e-commerce by purchasing and shipping products internationally.
* **AI:** Power intelligent agents and automation platforms that buy, compare, and manage products programmatically.
* **Gifts + Rewards:** Automate the delivery of gifts, incentives, and rewards to customers or employees at scale.
* **Price Tracking:** Monitor product prices and availability across retailers for dynamic pricing, alerts, or analytics.
* **Social Shopping:** Build platforms where users can discover, share, and purchase products collaboratively.


