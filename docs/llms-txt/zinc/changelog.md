# Source: https://zinc-staging.vercel.app/docs/changelog.md

> ## Documentation Index
> Fetch the complete documentation index at: https://zinc-staging.vercel.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Changelog

> Product updates and improvements to Zinc API

<Update label="2026-03-06" description="Week of Mar 2">
  <Frame>
    <img src="https://mintcdn.com/zinc/4Fa0HqFFyJ1FBCp6/images/changelog/2026-03-06.png?fit=max&auto=format&n=4Fa0HqFFyJ1FBCp6&q=85&s=b0ba42b0d73ae1d0b2476f7b13a6db7b" alt="Week of Mar 2 updates" width="2048" height="1044" data-path="images/changelog/2026-03-06.png" />
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
    <img src="https://mintcdn.com/zinc/OFkKK_PyX1ZWgJTd/images/changelog/2026-02-27.png?fit=max&auto=format&n=OFkKK_PyX1ZWgJTd&q=85&s=7ddf5933a8b41c80ecdf1ed58f8f2ca8" alt="Week of Feb 23 updates" width="2048" height="1044" data-path="images/changelog/2026-02-27.png" />
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
    <img src="https://mintcdn.com/zinc/GBFEqFDdcC5CovIP/images/changelog/2026-02-20.png?fit=max&auto=format&n=GBFEqFDdcC5CovIP&q=85&s=32787ee9370744c7e9f47603d7bc1945" alt="Week of Feb 16 updates" width="2048" height="1044" data-path="images/changelog/2026-02-20.png" />
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
    <img src="https://mintcdn.com/zinc/zCiMW3lZ8p_0maLd/images/changelog/2026-02-13.png?fit=max&auto=format&n=zCiMW3lZ8p_0maLd&q=85&s=ce9b511506ac68df890ed1f2b696102f" alt="Week of Feb 9 updates" width="2048" height="1044" data-path="images/changelog/2026-02-13.png" />
  </Frame>

  This week's highlight is the launch of our Universal Checkout Skill for AI agents, plus auto wallet top-up and better order visibility.

  ### Universal Checkout Skill

  <CardGroup cols={2}>
    <Frame>
      <video src="https://mintcdn.com/zinc/JcZ_00yHjkmfiMBl/videos/agent-skills/claw-demo-1.mp4?fit=max&auto=format&n=JcZ_00yHjkmfiMBl&q=85&s=fc80277ca75010ace7d79133488b883c" controls muted loop style={{maxHeight: "500px"}} data-path="videos/agent-skills/claw-demo-1.mp4" />
    </Frame>

    <Frame>
      <video src="https://mintcdn.com/zinc/JcZ_00yHjkmfiMBl/videos/agent-skills/claw-demo-2.mp4?fit=max&auto=format&n=JcZ_00yHjkmfiMBl&q=85&s=c887518353c5ac9a75ec1de8a418d184" controls muted loop style={{maxHeight: "500px"}} data-path="videos/agent-skills/claw-demo-2.mp4" />
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
    <img src="https://mintcdn.com/zinc/BUja_LmsxUGysliw/images/changelog/2026-02-06.png?fit=max&auto=format&n=BUja_LmsxUGysliw&q=85&s=53ac4e22f3698df5ce425ab6d3da6c34" alt="Week of Feb 2 updates" width="2048" height="1044" data-path="images/changelog/2026-02-06.png" />
  </Frame>

  This week's highlight is a brand new retailer status page, plus stronger account security and better order visibility.

  ### Retailer Status Page

  <Frame>
    <img src="https://mintcdn.com/zinc/BUja_LmsxUGysliw/images/changelog/2026-02-06-1.png?fit=max&auto=format&n=BUja_LmsxUGysliw&q=85&s=4376af7fe11decaa4e0d8bb3007dce84" alt="Retailer status page" width="2048" height="1044" data-path="images/changelog/2026-02-06-1.png" />
  </Frame>

  Zinc now has a dedicated status page with nightly integration test results for our top retailers. We're committed to full transparency into what's working and what isn't — and we'll be expanding coverage to more retailers over time.

  ### TOTP Support for Retailer Credentials

  Managed retail accounts now support Time-based One-Time Passwords (TOTP). If your retailer account uses two-factor authentication with an authenticator app, you can provide your TOTP secret and Zinc will automatically generate codes during login — no more manual verification steps.

  ### Improved Order Progress

  <Frame>
    <img src="https://mintcdn.com/zinc/w6qgUJZEocjZ12CF/images/changelog/2026-02-06-2.png?fit=max&auto=format&n=w6qgUJZEocjZ12CF&q=85&s=0d5c369e8f2e93709d32fa8100b96d50" alt="Incremental order status updates" width="2354" height="678" data-path="images/changelog/2026-02-06-2.png" />
  </Frame>

  Orders now report more granular progress updates as they move through each step of the purchasing flow, giving you better real-time visibility into order status.
</Update>

<Update label="2026-01-30" description="Week of Jan 26">
  <Frame>
    <img src="https://mintcdn.com/zinc/RqEYpBsupHFLTdrg/images/changelog/2026-01-30.png?fit=max&auto=format&n=RqEYpBsupHFLTdrg&q=85&s=318fd2833c69ee2c4f24338ceaead49f" alt="Week of Jan 26 updates" width="2048" height="1044" data-path="images/changelog/2026-01-30.png" />
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
    <img src="https://mintcdn.com/zinc/pwE47ewGatVotVmw/images/changelog/2026-01-16.png?fit=max&auto=format&n=pwE47ewGatVotVmw&q=85&s=cc80619fbfe6044e268e523463ffdd41" alt="Week of Jan 12 updates" width="2048" height="1044" data-path="images/changelog/2026-01-16.png" />
  </Frame>

  ### Launch Week 1

  **January 20-24** — Zinc's first launch week. Five days. Five releases.

  We're rapidly expanding Zinc 2.0's feature-set, vastly improving devex, and showing off some impressive demos to inspire you on what you can build with Zinc.

  Pay attention to your inboxes and our socials for Launch Week 1!

  ***

  ### Account Selection in Orders

  <Frame>
    <img src="https://mintcdn.com/zinc/pwE47ewGatVotVmw/images/changelog/account-selection.png?fit=max&auto=format&n=pwE47ewGatVotVmw&q=85&s=336809ad69b0177a04b54b328b3aa564" alt="Account selection dropdown" width="1258" height="894" data-path="images/changelog/account-selection.png" />
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
    <img src="https://mintcdn.com/zinc/CdsaQcoVWoxbfAei/images/changelog/2026-01-09.png?fit=max&auto=format&n=CdsaQcoVWoxbfAei&q=85&s=d7cc007fe04c8967c782887f28b7047a" alt="Week of Jan 5 updates" width="2048" height="1044" data-path="images/changelog/2026-01-09.png" />
  </Frame>

  This week we're introducing managed retail accounts and smarter payment handling. These features give you more control over how orders are placed and make credential management significantly easier.

  ### Managed Retail Accounts

  <Frame>
    <img src="https://mintcdn.com/zinc/CdsaQcoVWoxbfAei/images/changelog/managed-accounts.gif?s=54989e6d9de8dc312e311123850a17d0" alt="Managed retail accounts" width="1384" height="1080" data-path="images/changelog/managed-accounts.gif" />
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
    <img src="https://mintcdn.com/zinc/ZdtGFKwvElAycP-R/images/changelog/2026-01-02.png?fit=max&auto=format&n=ZdtGFKwvElAycP-R&q=85&s=23d5f0beea9d967ab563f09f115080bb" alt="Week of Dec 29 updates" width="2048" height="1044" data-path="images/changelog/2026-01-02.png" />
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
    <img src="https://mintcdn.com/zinc/ZdtGFKwvElAycP-R/images/changelog/2025-12-26.png?fit=max&auto=format&n=ZdtGFKwvElAycP-R&q=85&s=29e33c83dea2978eb01eaa2ea8bc3d63" alt="Week of Dec 22 updates" width="2048" height="1044" data-path="images/changelog/2025-12-26.png" />
  </Frame>

  This week brought intelligent product variant interpretation and expanded financial management capabilities. The highlight: we can now automatically understand and parse product variants from plaintext strings.

  ### Product Variant Interpretation

  <Frame>
    <img src="https://mintcdn.com/zinc/ZdtGFKwvElAycP-R/images/changelog/variants.png?fit=max&auto=format&n=ZdtGFKwvElAycP-R&q=85&s=824ed6ff05ae5b74b9be9ce29dd5dd64" alt="Product variant interpretation" width="2048" height="1350" data-path="images/changelog/variants.png" />
  </Frame>

  The biggest update this week is our ability to intelligently interpret product variants from plaintext strings. Instead of requiring structured data, you can now provide variant information as natural text and we'll automatically parse it into the correct format.

  * **Intelligent parsing** — Automatically interpret size, color, and style options from plaintext strings
  * **Flexible input** — No need to pre-structure variant data, just provide the information naturally
  * **Clear label/value pairs** — Properly formatted variants for accurate order placement

  ### Better Test Order Flow

  <Frame>
    <img src="https://mintcdn.com/zinc/ZdtGFKwvElAycP-R/images/changelog/test-order-flow.gif?s=7c52f5fd0b30ece4773723becdd9250f" alt="Better test order flow" width="1620" height="1080" data-path="images/changelog/test-order-flow.gif" />
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
    <img src="https://mintcdn.com/zinc/ZdtGFKwvElAycP-R/images/changelog/2025-12-19.png?fit=max&auto=format&n=ZdtGFKwvElAycP-R&q=85&s=f9a88b40defc659d1a02ab556918dd6f" alt="Week of Dec 15 updates" width="2048" height="1044" data-path="images/changelog/2025-12-19.png" />
  </Frame>

  We finally released the latest version of Zinc. This initial release brings dramatically expanded retailer support, along with key order management features.

  ### V2 Beta Launch

  <Frame>
    <iframe width="100%" style={{aspectRatio: "16/9"}} src="https://www.youtube.com/embed/9K0NO4C6Wro" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
  </Frame>

  Zinc 2.0 beta is now available with a modern API and dashboard. This release dramatically expands our retailer coverage.

  * **More Retailers:** Dramatically expanded retailer support across the world's top online stores
  * **Modern API:** Clean, consistent API design for better developer experience

  <Note>
    Some v1 features (account automation, tracking, returns) are coming soon. See [migrating from v1](/v2/migrating-from-v1) for details.
  </Note>

  ### Order Management

  <Frame>
    <img src="https://mintcdn.com/zinc/ZdtGFKwvElAycP-R/images/changelog/order-management.gif?s=5bf67a8fe27777d4a045249695b79e2c" alt="Order management features" width="800" height="499" data-path="images/changelog/order-management.gif" />
  </Frame>

  You can now cancel orders directly from the dashboard and retry failed orders through the API. This gives you more control over your order lifecycle without needing to contact support.

  * **Cancel orders** — Stop orders before they're fulfilled when plans change (available in dashboard)
  * **Retry failed orders** — Automatically retry orders that failed due to temporary issues (available via API)

  ### Amazon Integration

  <Frame>
    <img src="https://mintcdn.com/zinc/ZdtGFKwvElAycP-R/images/changelog/amazon.png?fit=max&auto=format&n=ZdtGFKwvElAycP-R&q=85&s=3f30423865e9351de5134d1818e3d5c1" alt="Amazon integration" width="2048" height="1350" data-path="images/changelog/amazon.png" />
  </Frame>

  For customers who need Amazon's full feature set during the v2 transition, orders can now be automatically proxied through our v1 API. This ensures continuity while we complete v2 feature parity.

  ### Platform Improvements

  We've also made several improvements to the overall platform experience:

  * **Better order display** — Improved how order details are shown in the dashboard
  * **Payment notifications** — Clearer notifications when payment methods need attention
</Update>

<Update label="2025-12-12" description="Week of Dec 7">
  <Frame>
    <img src="https://mintcdn.com/zinc/ZdtGFKwvElAycP-R/images/changelog/2025-12-12.png?fit=max&auto=format&n=ZdtGFKwvElAycP-R&q=85&s=9330b86cd7cecfba50f3c14204a6609a" alt="Week of Dec 7 updates" width="2048" height="1044" data-path="images/changelog/2025-12-12.png" />
  </Frame>

  This week brought improvements to wallet management and ordering reliability. We're making it easier to manage your account balance and ensuring orders succeed more consistently.

  ### Wallet Management

  <Frame>
    <img src="https://mintcdn.com/zinc/ZdtGFKwvElAycP-R/images/changelog/payment-methods.png?fit=max&auto=format&n=ZdtGFKwvElAycP-R&q=85&s=524ab10854211caecc0aafab898c5cae" alt="Wallet management interface" width="2048" height="1350" data-path="images/changelog/payment-methods.png" />
  </Frame>

  You can now add funds directly to your wallet using your saved payment methods. Previously, you had to contact support to top up your account — now you can do it yourself in seconds.

  We've also added detailed descriptions to all wallet transactions, so you can see exactly what each charge was for (API fees, order costs, etc.).

  ### More Reliable Orders

  Orders now automatically retry when they encounter temporary issues, making the overall process more reliable. We've also made several improvements:

  * **Smarter price checking** — We now validate prices only at the final checkout step, reducing premature order failures
  * **More accurate pricing** — Enhanced price extraction logic handles varied retailer formats more reliably
</Update>


Built with [Mintlify](https://mintlify.com).