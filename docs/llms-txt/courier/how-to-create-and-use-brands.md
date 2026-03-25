# Source: https://www.courier.com/docs/tutorials/content/how-to-create-and-use-brands.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Brand Your Notifications

> Create and customize Courier Brands to apply consistent logos, colors, headers, footers, and social links across your email notifications.

Courier Brands let you apply a consistent look and feel to your email and inbox notifications. You can maintain a single brand or create multiple brands for white-labeling, multi-tenant apps, or different product lines. Brands are fully API-enabled via the [Brands API](/api-reference/brands/list-brands).

By the end of this tutorial you'll have a brand configured with a logo, colors, footer, and social links, and you'll know how to apply it to notifications.

## Prerequisites

* A [Courier account](https://app.courier.com/)
* Your brand assets ready: logo image, hex color codes, social media URLs

## Understanding Email Brand Templates

Courier offers three template types for brands:

| Template Type              | Best For                      | Customization Level                    |
| -------------------------- | ----------------------------- | -------------------------------------- |
| **Standard**               | Most use cases; visual editor | Logo, colors, footer, social links     |
| **Handlebars**             | Custom header/footer layouts  | Handlebars templating in header/footer |
| **Custom MJML/Handlebars** | Fully custom email layout     | Complete control over HTML structure   |

This tutorial uses the Standard template. For custom MJML/Handlebars templates, see the [Brands reference](/platform/content/brands/brands-overview).

## Step 1: Create a Brand

<Steps>
  <Step title="Open the Brand Designer">
    Navigate to **Templates > Brands** in the Courier dashboard and click **New Brand**.

    <Frame caption="Creating a new brand">
      <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/create-brand.gif?s=f4a1955ae158476b74e0ca2819e7e24f" width="1429" height="371" data-path="assets/platform/content/create-brand.gif" />
    </Frame>
  </Step>

  <Step title="Name your brand">
    Give your brand a descriptive name (e.g. "Acme Corp"). Optionally set a `brand_id` if you plan to manage the brand via the API.
  </Step>
</Steps>

## Step 2: Customize Your Brand

<Steps>
  <Step title="Upload a logo">
    In the Brand Designer, locate the Logo section and upload your logo. Requirements:

    * JPEG, PNG, or GIF format
    * Maximum 5MB
    * Ideally 140px wide (height is flexible)
  </Step>

  <Step title="Set brand colors">
    Configure your color palette:

    * **Primary** - Buttons, links, and key accent elements
    * **Secondary / Tertiary** - Supporting accent colors
    * **Header** - Background color of the email header bar
  </Step>

  <Step title="Configure the footer">
    Add your company name and optional legal text. You can use built-in variables:

    * `{datetime.year}` - Current year (e.g. for `© {datetime.year} Acme Corp`)
    * `{urls.unsubscribe}` - One-click unsubscribe link
    * `{urls.preferences}` - Link to the user's preference page

    Add social media links (Facebook, Instagram, LinkedIn, Twitter/X, Medium) to display icon links in the footer.
  </Step>

  <Step title="Preview and publish">
    Click **Preview** to see how your brand looks in a sample email. When you're satisfied, click **Publish**.
  </Step>
</Steps>

## Step 3: Apply the Brand

### Set as Default

Setting a brand as default means it automatically applies to all notifications that don't specify a different brand. Open the brand settings and click **Set as Default**.

<Frame caption="Setting a brand as the default">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/content/set-brand-as-default.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=6ab4e4df891a03b722b423cb3d798467" width="414" height="139" data-path="assets/platform/content/set-brand-as-default.png" />
</Frame>

<Note>
  Every email notification uses the default brand unless you explicitly disable brands in the template settings or specify a different brand in the send request.
</Note>

### Apply to Specific Notifications

If you don't want the brand as default, you can assign it per notification:

1. Open the notification template
2. Go to **Template Settings**
3. Select your brand from the dropdown

### Specify at Send Time

Pass a `brand_id` in the [Send API](/api-reference/send/send-a-message) request to override the default brand:

<CodeGroup>
  ```bash curl theme={null}
  curl -X POST https://api.courier.com/send \
    -H "Authorization: Bearer $COURIER_AUTH_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "message": {
        "brand_id": "your-brand-id",
        "to": { "email": "recipient@example.com" },
        "content": {
          "title": "Welcome!",
          "body": "This uses your custom brand."
        }
      }
    }'
  ```

  ```typescript Node theme={null}
  import Courier from "@trycourier/courier";

  const client = new Courier({ apiKey: "your_api_key" });

  await client.send.message({
    message: {
      brand_id: "your-brand-id",
      to: { email: "recipient@example.com" },
      content: {
        title: "Welcome!",
        body: "This uses your custom brand.",
      },
    },
  });
  ```

  ```python Python theme={null}
  from courier import Courier

  client = Courier(api_key="your_api_key")

  client.send.message(
      message={
          "brand_id": "your-brand-id",
          "to": {"email": "recipient@example.com"},
          "content": {
              "title": "Welcome!",
              "body": "This uses your custom brand.",
          },
      },
  )
  ```
</CodeGroup>

## Advanced Customization

### Custom Templates

For more control over the email layout, select **Use Custom Template** in the Brand Designer. This lets you write Handlebars and HTML or [MJML](https://mjml.io/) for the header and footer while still using drag-and-drop content blocks for the email body.

<Frame caption="Custom template editor in the Brand Designer">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/brand-custom-template.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=94b5755591a656ec752c6f62d75d4533" width="1520" height="1190" data-path="assets/platform/content/brand-custom-template.png" />
</Frame>

### Custom CSS

You can customize the `<style>` element in the `<head>` section of your emails. This works with both Standard and Custom template brands. See [CSS Classnames](/platform/content/brands/css-classnames) for available selectors.

### Snippets

Snippets are reusable pieces of Handlebars code that you can call from any template block:

1. Create a snippet in the Brand Designer (e.g. `my_snippet`)
2. In a notification, add a **Template Block** and call it: `{{>my_snippet}}`

<Frame caption="Using a snippet in a template block">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/brand-snippet-block.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=0f1c0a04f0b19f7f6f9766bca6391eca" width="1540" height="558" data-path="assets/platform/content/brand-snippet-block.png" />
</Frame>

Snippets support variables, so you can pass dynamic content into them via the send request. A snippet defined in the default brand is available in all custom brands unless the custom brand defines its own snippet with the same name.

### Brand Variables

Any brand attribute you can configure in the UI is also available as a Handlebars variable. For example, `{{var "brand.social.facebook"}}` renders the Facebook URL. Available variables include:

* `brand.colors.primary`, `brand.colors.secondary`, `brand.colors.tertiary`
* `brand.email.header.barColor`, `brand.email.header.logo.image`, `brand.email.header.logo.href`
* `brand.social.facebook`, `brand.social.instagram`, `brand.social.linkedin`, `brand.social.twitter`, `brand.social.medium`

## What's Next

<CardGroup cols={2}>
  <Card title="Brands Reference" href="/platform/content/brands/brands-overview" icon="copyright">
    Full reference for brand configuration, MJML templates, and API management
  </Card>

  <Card title="Brands API" href="/api-reference/brands/list-brands" icon="code">
    Create, update, and delete brands programmatically
  </Card>

  <Card title="CSS Classnames" href="/platform/content/brands/css-classnames" icon="paintbrush">
    Customize email styles with CSS selectors
  </Card>

  <Card title="Design Your First Notification" href="/tutorials/content/how-to-design-your-first-notification" icon="palette">
    Build a notification template that uses your brand
  </Card>
</CardGroup>
