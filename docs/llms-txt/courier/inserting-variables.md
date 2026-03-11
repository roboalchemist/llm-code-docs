# Source: https://www.courier.com/docs/platform/content/variables/inserting-variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Inserting Data with Variables

> Personalize notifications by inserting variables from data, profile, tenant, or brand objects into content blocks, Handlebars, email fields, and conditional logic.

Variables let you insert dynamic, personalized values into your notifications. Use curly brackets to reference values from the Send API, user profiles, tenants, and brands.

## Using Variables in Notifications

You can insert variables into:

* [Content Blocks](/platform/content/content-blocks/content-block-basics) (Text, Action, Markdown, Quote, Template, List)
* [Handlebars code](/platform/content/template-designer/handlebars-designer) (Template blocks, Email templates, Brands)
* [Email subject line and addresses](/platform/content/template-settings/email-fields) (From, Reply-To, CC, BCC)
* [Notification Conditions](/platform/content/template-settings/send-conditions) to control notification sending
* [Channel Conditions](/platform/content/template-settings/send-conditions#for-notifications-and-channels) to enable or disable specific channels
* [Filters](/platform/content/template-designer/template-designer-overview#reusable-drag-and-drop-content) to conditionally show or hide content blocks

<Frame caption="Example of Variable Replacement in Rendered Preview">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/data-variables-before-after.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=1a7f744ae4271d5ce9d568f11a552119" alt="Example of Variable Replacement in Rendered Preview" width="1510" height="590" data-path="assets/platform/content/data-variables-before-after.png" />
</Frame>

### Content Blocks

Enclose the variable name in single curly brackets: `{variable_name}`. Properly formatted variables inside Text, Markdown, Quote, and List Blocks are highlighted in green.

<Frame caption="Text Block With Variables">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/data-content-block.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=282be9ab4f795dae1d6aa817f41905c1" alt="Text Block With Variables" width="436" height="372" data-path="assets/platform/content/data-content-block.png" />
</Frame>

### Handlebars

In Handlebars, use double curly brackets `{{ }}` with the [`var`](/platform/content/template-designer/handlebars-helpers#var) or [`path`](/platform/content/template-designer/handlebars-helpers#path) helper:

* Data object: `{{var "variable_name"}}`
* Profile data: `{{var "profile.variable_name"}}`

You can use Handlebars in Template content blocks, Brand templates, and the Handlebars override in Email notifications.

### Email Fields

Variables are also supported in the `Subject` line, `From` address, `Reply-To`, `CC`, and `BCC` fields in the email [channel settings](/platform/content/template-settings/email-fields).

<Frame caption="Email Subject With Variables">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/data-email.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=42f4dc521c3fa6886abff67d0fd77756" alt="Email Subject With Variables" width="1594" height="630" data-path="assets/platform/content/data-email.png" />
</Frame>

<Frame caption="Email Channel Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/content/data-notification-settings.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=6739560505e83c5c932469c24e9ad735" alt="Email Channel Settings" width="2240" height="1316" data-path="assets/platform/content/data-notification-settings.png" />
</Frame>

## Data Sources

Courier resolves variables from the Notification Context, which has four top-level keys. Each data source has its own [JSONPath](https://www.npmjs.com/package/jsonpath) prefix:

| Source                                                    | JSONPath             | Shorthand                     | Example                  |
| --------------------------------------------------------- | -------------------- | ----------------------------- | ------------------------ |
| **[Data](/api-reference/send/send-a-message)**            | `$.data.someProp`    | `data.someProp` or `someProp` | `{order.total}`          |
| **[Profile](/api-reference/user-profiles/get-a-profile)** | `$.profile.someProp` | `profile.someProp`            | `{profile.email}`        |
| **[Tenant](/api-reference/tenants/get-a-tenant)**         | `$.tenant.someProp`  | `tenant.someProp`             | `{tenant.name}`          |
| **[Brand](/api-reference/brands/list-brands)**            | `$.brand.someProp`   | `brand.someProp`              | `{brand.colors.primary}` |

<Tip>
  Courier queries the `data` object by default for any path not prefixed with `profile.`, `tenant.`, or `brand.`. So `{orderId}` is equivalent to `{data.orderId}`.
</Tip>

### The Data Object

The **Data** object is an optional property of the [Send](/api-reference/send/send-a-message) call. Use it to pass key-value pairs into your notification template.

```json  theme={null}
{
  "customer": {
    "name": "Acme Corporation",
    "plan": "Enterprise"
  },
  "order": {
    "id": "order_abc123",
    "total": 99.99,
    "currency": "USD"
  },
  "billing": {
    "nextInvoiceDate": "2024-06-01",
    "paymentMethod": {
      "type": "CreditCard",
      "lastFour": "1234"
    }
  }
}
```

Nested values are accessed with dot notation:

| Path              | Description            |
| ----------------- | ---------------------- |
| `{myField}`       | Top-level key in data  |
| `{customer.name}` | Nested value           |
| `{items[0].name}` | First item in an array |

<Warning>
  Variable names must use camelCase or snake\_case. Dashes and other special characters cause rendering errors: `{firstName}` and `{first_name}` work, `{first-name}` does not.
</Warning>

### The User Profile

**User Profile** data can come from two places:

* The `profile` object in the [Send API](/api-reference/send/send-a-message) request.
* The stored **User Profile** associated with the recipient ID, created via the [Profiles API](/api-reference/user-profiles/get-a-profile).

```json  theme={null}
{
  "email": "jane.doe@example.com",
  "phone": "+1 555 9876543",
  "name": {
    "firstName": "Jane",
    "lastName": "Doe"
  },
  "locale": "en-US",
  "timezone": "America/Los_Angeles",
  "address": {
    "city": "Anytown",
    "state": "CA",
    "country": "USA"
  }
}
```

Core fields:

| Path                     | Description            |
| ------------------------ | ---------------------- |
| `{profile.email}`        | Email address          |
| `{profile.phone_number}` | Phone number           |
| `{profile.locale}`       | Locale (e.g., `en-US`) |

The profile is extensible; any custom fields you store on the profile are accessible via `{profile.yourField}`.

<Note>
  If a key exists in both the Send API `profile` object and the stored User Profile, the Send API value takes precedence.
</Note>

### Built-in Variables

Courier automatically populates these variables during the send process. You can use them in notification content and settings:

| Variable                  | Description                                              |
| ------------------------- | -------------------------------------------------------- |
| `{courier.environment}`   | The environment, e.g., "production" or "test"            |
| `{courier.scope}`         | The notification scope, e.g., "published" or "draft"     |
| `{event}`                 | The event associated with the notification               |
| `{messageId}`             | The unique identifier for the message                    |
| `{openTrackingId}`        | The tracking ID for email open events                    |
| `{recipient}`             | The recipient ID                                         |
| `{subscriptionTopicId}`   | The ID of the subscription topic, if applicable          |
| `{template}`              | The name of the template used for the notification       |
| `{unsubscribeTrackingId}` | The tracking ID for unsubscribe events                   |
| `{urls.opened}`           | The URL for tracking email opens                         |
| `{urls.unsubscribe}`      | The unsubscribe URL                                      |
| `{urls.preferences}`      | The URL for managing the user's notification preferences |
| `{var "datetime.year"}`   | The current year (Handlebars syntax only)                |

### Tenant

The **Tenant** object contains information about the [tenant](/api-reference/tenants/get-a-tenant) associated with the send. Access tenant properties with `{tenant.name}` in content blocks or `{{var "tenant.name"}}` in Handlebars.

| Path                        | Description                                                                   |
| --------------------------- | ----------------------------------------------------------------------------- |
| `{tenant.id}`               | Tenant ID                                                                     |
| `{tenant.name}`             | Tenant name                                                                   |
| `{tenant.brand_id}`         | Default brand ID for the tenant                                               |
| `{tenant.parent_tenant_id}` | Parent tenant ID (if the tenant has a parent)                                 |
| `{tenant.properties.*}`     | Custom properties set on the tenant (e.g., `{tenant.properties.companyLogo}`) |

### Brand

The **Brand** object contains branding values from the [Brand](/api-reference/brands/list-brands) associated with the notification. Commonly used paths:

| Path                                                 | Description            |
| ---------------------------------------------------- | ---------------------- |
| `{brand.id}`                                         | Brand ID               |
| `{brand.name}`                                       | Brand name             |
| `{brand.settings.colors.primary}`                    | Primary brand color    |
| `{brand.settings.colors.secondary}`                  | Secondary brand color  |
| `{brand.settings.colors.tertiary}`                   | Tertiary brand color   |
| `{brand.settings.email.header.barColor}`             | Email header bar color |
| `{brand.settings.email.header.logo.href}`            | Logo link URL          |
| `{brand.settings.email.header.logo.image}`           | Logo image URL         |
| `{brand.settings.email.footer.social.facebook.url}`  | Facebook URL           |
| `{brand.settings.email.footer.social.twitter.url}`   | Twitter URL            |
| `{brand.settings.email.footer.social.linkedin.url}`  | LinkedIn URL           |
| `{brand.settings.email.footer.social.instagram.url}` | Instagram URL          |
| `{brand.settings.email.footer.social.medium.url}`    | Medium URL             |
