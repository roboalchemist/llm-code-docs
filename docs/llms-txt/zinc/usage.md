# Source: https://zinc-staging.vercel.app/docs/v2/agent-skills/usage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://zinc-staging.vercel.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Usage Guide

> Place orders, check statuses, and manage purchases through your AI agent.

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


Built with [Mintlify](https://mintlify.com).