# Source: https://docs.replit.com/replitai/stripe-payments.md

# Stripe Payments Integration

> Add payments and subscriptions to your app with Stripe using Agent, test safely in a sandbox, then go live with your own Stripe account.

export const AiPrompt = ({children}) => {
  return <CodeBlock className="relative block font-sans whitespace-pre-wrap break-words">
      <div className="pr-7">
        {children}
      </div>
    </CodeBlock>;
};

## What you can build

Use Agent to add Stripe to your app in one click—no setup required. Build a storefront, accept one‑time payments, or create subscriptions. Agent wires up the integration, data models, and test environment.

## How it works

Agent starts with a Stripe sandbox so you can safely test payments without moving real money. You can build and try flows immediately. When you are ready, switch to your live Stripe account to publish and accept real payments.

<Info>
  A Stripe sandbox is an isolated test environment where you can simulate
  payments, subscriptions, and events. Learn more in
  [Stripe's docs on sandboxes](https://docs.stripe.com/sandboxes).
</Info>

## Get started

* **Ask Agent to use Stripe**
  * Use a slash command on the home screen and select Stripe, or ask directly:
    <AiPrompt>Build a storefront and integrate Stripe for payments</AiPrompt>
* **Choose your starting point**
  * Start with a full app, or begin with a design and convert it to a full app
    when you’re ready to generate the Stripe integration.

<Note>
  If you start with a design, Agent creates the Stripe integration when you
  convert the design into a full app.
</Note>

## Test payments in the sandbox

1. Open your app’s **Preview** in a new tab.
2. Make a test purchase from your storefront or payment page.
3. Use Stripe’s standard test card:

```text  theme={null}
Card number: 4242 4242 4242 4242
Expiry: any future date
CVC: any 3 digits
Name, address: any mock values
```

<Tip>
  Sandbox purchases don’t process through real networks or move money. They’re
  safe for testing end to end.
</Tip>

## Manage products and pricing

You have two options:

1. From your app, select **Publish**, then choose to claim your Stripe sandbox.
   * If you don’t have a Stripe account yet, create one to claim the sandbox.
2. In the Stripe Dashboard, open **Products** to add or edit products and prices.
   Changes you make in the Stripe sandbox reflect in your Replit app automatically
   and sync to your app’s database.

### View synced Stripe data

* In your Workspace, open **Database**.
* Select **MyData**.
* Change the schema selector to **Stripe** to see payment objects and related
  records.

## Go live

To accept real payments:

<Warning>
  Before you publish:

  * Install the **Replit Integrated Payments** app in your live Stripe account
    (required for sandbox‑to‑live synchronization)
  * Complete Stripe’s KYB verification and add your live API keys

  Your sandbox integration is not production‑ready. It cannot accept real
  payments until you complete these steps.
</Warning>

1. In Stripe, switch from sandbox to your live account.
2. Complete Stripe’s KYB (Know Your Business) verification if prompted.
3. Copy your live Publishable and Secret keys from Stripe.
4. In Replit, open the **Publish** pane, then add your live keys.
5. Publish your app.

## Manage the integration

* Go to **Integrations > Stripe** to open the Stripe connector.
* From there, you can test the connection, view status, and manage settings.

## Frequently asked questions

### How do I update the prices of my products?

* Ask Agent: Describe the change and Agent updates your app and Stripe objects.
* Use the Stripe Dashboard: Open **Products** to edit prices and product details.
  * In sandbox, changes sync back to your app and database automatically.
  * For production, switch to your live account first, then update prices. Publish again if your app needs to pick up new configuration.

### How do I test transactions on Replit?

Open your app’s **Preview** in a new tab. Run the Stripe Checkout flow with the
standard test card (4242 4242 4242 4242), any future expiry, and any CVC. See
[Test payments in the sandbox](#test-payments-in-the-sandbox) above for details.

### What is a live Stripe account?

A live Stripe account is an activated and verified account that can process real
payments using your business details. See Stripe’s guidance on account creation
and activation: [Create and manage your Stripe account](https://docs.stripe.com/get-started/account).

### How do I find my live keys?

1. In the Stripe Dashboard, switch to your live account using the account picker (top left).
2. From the bottom left, select **Developers** > **API keys**.
3. Reveal your live keys or create new ones. For step‑by‑step instructions on creating new keys, see
   [Create a secret API key](https://docs.stripe.com/keys#create-api-secret-key).

## Notes and limitations

* Sandbox activity does not affect real balances or customers.
* Some Stripe features can’t be tested in sandboxes (for example, IC+ pricing
  and certain Connect flows). See
  [Stripe’s sandbox limitations](https://docs.stripe.com/sandboxes).
