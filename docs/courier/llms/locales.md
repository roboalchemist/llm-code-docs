# Source: https://www.courier.com/docs/platform/content/elemental/locales.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Locales

> Localize your Elemental templates for multiple languages and regions. Define translations once and Courier automatically serves the right content based on each recipient's locale.

## Why Use Locales?

Elemental's locale system lets you create a single template that automatically adapts to your users' preferred languages. Instead of maintaining separate templates for each language, define translations once and Courier handles the rest.

* **Single template, multiple languages**: One template structure with translations for all supported locales
* **Automatic selection**: Courier uses the recipient's locale from their profile or the `message.to.locale` field
* **Fallback support**: If a translation is missing, Courier uses the default content
* **Consistent structure**: Keep the same layout and logic across all languages

## Supported Elements and Properties

Locales can be applied to any Elemental element that has localizable properties. The following properties support localization:

* **`content`**: Text content in `text`, `action`, `quote`, and `html` elements
* **`title`**: Title in `meta` elements (email subject lines, push notification titles)
* **`href`**: URLs in `action` and `image` elements
* **`src`**: Image source URLs in `image` elements
* **`elements`**: Inline text content elements (string, link, img) in `text` elements, or nested elements in `channel` and `group` elements
* **`template`**: Template strings in `jsonnet` elements

## How Locales Work

When you specify a `locale` in the `message.to` field, Courier automatically replaces the default property values with locale-specific translations for each element that has a matching locale definition.

The locale interface follows this structure:

```ts  theme={null}
interface Locales {
  [locale: string]: {
    content?: string;    // For text, action, quote, html elements
    title?: string;      // For meta elements
    href?: string;       // For action, image elements
    src?: string;        // For image elements
    elements?: Element[]; // For text elements (inline content) or channel/group elements (nested)
    template?: string;   // For jsonnet elements
  };
}
```

### Text Node Locale Resolution

Text elements support two content formats: `content` (a plain or markdown string) and `elements` (a structured array of inline nodes like string, link, and img). The locale system handles all combinations:

| Root node has          | Locale provides        | Behavior                                                                        |
| ---------------------- | ---------------------- | ------------------------------------------------------------------------------- |
| `content`              | `content`              | Replaces the content string                                                     |
| `elements`             | `elements`             | Replaces the elements array                                                     |
| `elements`             | `content`              | Wraps the content string into a single-element array for backward compatibility |
| `content` + `elements` | `content` + `elements` | Uses `elements` (structured format takes precedence)                            |
| `content` + `elements` | `content` only         | Wraps the content string into a single-element array                            |
| `content` + `elements` | `elements` only        | Uses the locale's elements array                                                |

<Note>
  If a locale translation is missing for a specific element, Courier falls back to the default property value. This ensures your notifications always render, even if some translations are incomplete.
</Note>

<Warning>
  When a text node uses the `elements` format and a locale provides only a `content` string, Courier wraps the string into a single-element array (`[{ type: "string", content: "..." }]`). This preserves rendering but loses any inline formatting (bold, italic, links) that the original elements may have had. For full formatting fidelity, provide `elements` in your locale translations.
</Warning>

## Basic Example

Here's a simple example showing how to localize a text element:

<CodeGroup>
  ```bash cURL icon="terminal" wrap theme={null}
  curl -X POST https://api.courier.com/send \
    -H "Authorization: Bearer $COURIER_AUTH_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "message": {
        "to": {
          "email": "user@example.com",
          "locale": "fr"
        },
        "content": {
          "version": "2022-01-01",
          "elements": [
            {
              "type": "text",
              "content": "Hello",
              "locales": {
                "fr": {
                  "content": "Bonjour"
                },
                "es": {
                  "content": "Hola"
                }
              }
            }
          ]
        }
      }
    }'
  ```

  ```javascript Node.js icon="node-js" lines theme={null}
  const { CourierClient } = require("@trycourier/courier");

  const courier = new CourierClient({
    authorizationToken: process.env.COURIER_AUTH_TOKEN,
  });

  const { requestId } = await courier.send({
    message: {
      to: {
        email: "user@example.com",
        locale: "fr",
      },
      content: {
        version: "2022-01-01",
        elements: [
          {
            type: "text",
            content: "Hello",
            locales: {
              fr: {
                content: "Bonjour",
              },
              es: {
                content: "Hola",
              },
            },
          },
        ],
      },
    },
  });

  console.log(`Sent with request ID: ${requestId}`);
  ```

  ```python Python icon="python" lines theme={null}
  import os
  from trycourier import Courier

  client = Courier(auth_token=os.environ["COURIER_AUTH_TOKEN"])

  response = client.send_message(
      message={
          "to": {
              "email": "user@example.com",
              "locale": "fr",
          },
          "content": {
              "version": "2022-01-01",
              "elements": [
                  {
                      "type": "text",
                      "content": "Hello",
                      "locales": {
                          "fr": {"content": "Bonjour"},
                          "es": {"content": "Hola"},
                      },
                  }
              ],
          },
      }
  )

  print(f"Sent with request ID: {response['requestId']}")
  ```
</CodeGroup>

In this example, when the recipient's locale is `"fr"`, the text `"Hello"` is replaced with `"Bonjour"`. If the locale is `"es"`, it becomes `"Hola"`. For any other locale (or if no locale is specified), the default `"Hello"` is used.

## Localizing Multiple Elements

You can localize multiple elements in a single template. Here's a comprehensive example showing localization for different element types:

<CodeGroup>
  ```bash cURL icon="terminal" wrap theme={null}
  curl -X POST https://api.courier.com/send \
    -H "Authorization: Bearer $COURIER_AUTH_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "message": {
        "to": {
          "email": "user@example.com",
          "locale": "es"
        },
        "content": {
          "version": "2022-01-01",
          "elements": [
            {
              "type": "meta",
              "title": "Welcome to our platform",
              "locales": {
                "es": {
                  "title": "Bienvenido a nuestra plataforma"
                },
                "fr": {
                  "title": "Bienvenue sur notre plateforme"
                }
              }
            },
            {
              "type": "text",
              "content": "Thanks for signing up, {{user_name}}!",
              "locales": {
                "es": {
                  "content": "¡Gracias por registrarte, {{user_name}}!"
                },
                "fr": {
                  "content": "Merci de vous être inscrit, {{user_name}} !"
                }
              }
            },
            {
              "type": "action",
              "content": "Get Started",
              "href": "https://app.example.com/dashboard",
              "locales": {
                "es": {
                  "content": "Comenzar",
                  "href": "https://app.example.com/es/dashboard"
                },
                "fr": {
                  "content": "Commencer",
                  "href": "https://app.example.com/fr/dashboard"
                }
              }
            }
          ]
        }
      }
    }'
  ```

  ```javascript Node.js icon="node-js" lines theme={null}
  const { CourierClient } = require("@trycourier/courier");

  const courier = new CourierClient({
    authorizationToken: process.env.COURIER_AUTH_TOKEN,
  });

  const { requestId } = await courier.send({
    message: {
      to: {
        email: "user@example.com",
        locale: "es",
      },
      data: {
        user_name: "María",
      },
      content: {
        version: "2022-01-01",
        elements: [
          {
            type: "meta",
            title: "Welcome to our platform",
            locales: {
              es: {
                title: "Bienvenido a nuestra plataforma",
              },
              fr: {
                title: "Bienvenue sur notre plateforme",
              },
            },
          },
          {
            type: "text",
            content: "Thanks for signing up, {{user_name}}!",
            locales: {
              es: {
                content: "¡Gracias por registrarte, {{user_name}}!",
              },
              fr: {
                content: "Merci de vous être inscrit, {{user_name}} !",
              },
            },
          },
          {
            type: "action",
            content: "Get Started",
            href: "https://app.example.com/dashboard",
            locales: {
              es: {
                content: "Comenzar",
                href: "https://app.example.com/es/dashboard",
              },
              fr: {
                content: "Commencer",
                href: "https://app.example.com/fr/dashboard",
              },
            },
          },
        ],
      },
    },
  });

  console.log(`Sent with request ID: ${requestId}`);
  ```

  ```python Python icon="python" lines theme={null}
  import os
  from trycourier import Courier

  client = Courier(auth_token=os.environ["COURIER_AUTH_TOKEN"])

  response = client.send_message(
      message={
          "to": {
              "email": "user@example.com",
              "locale": "es",
          },
          "data": {
              "user_name": "María",
          },
          "content": {
              "version": "2022-01-01",
              "elements": [
                  {
                      "type": "meta",
                      "title": "Welcome to our platform",
                      "locales": {
                          "es": {"title": "Bienvenido a nuestra plataforma"},
                          "fr": {"title": "Bienvenue sur notre plateforme"},
                      },
                  },
                  {
                      "type": "text",
                      "content": "Thanks for signing up, {{user_name}}!",
                      "locales": {
                          "es": {"content": "¡Gracias por registrarte, {{user_name}}!"},
                          "fr": {"content": "Merci de vous être inscrit, {{user_name}} !"},
                      },
                  },
                  {
                      "type": "action",
                      "content": "Get Started",
                      "href": "https://app.example.com/dashboard",
                      "locales": {
                          "es": {
                              "content": "Comenzar",
                              "href": "https://app.example.com/es/dashboard",
                          },
                          "fr": {
                              "content": "Commencer",
                              "href": "https://app.example.com/fr/dashboard",
                          },
                      },
                  },
              ],
          },
      }
  )

  print(f"Sent with request ID: {response['requestId']}")
  ```
</CodeGroup>

This example demonstrates:

* **Meta element**: Localizing the email subject line (`title` property)
* **Text element**: Localizing body content with Handlebars variables
* **Action element**: Localizing both button text (`content`) and URL (`href`)

## Localizing Text Elements with Structured Elements

When your text node uses the `elements` array (with inline string, link, and img nodes), you can provide locale translations as `elements` arrays too. This preserves rich formatting like bold, italic, and inline links across languages.

```json  theme={null}
{
  "type": "text",
  "elements": [
    { "type": "string", "content": "Your order " },
    { "type": "string", "content": "#{{order.id}}", "bold": true },
    { "type": "string", "content": " has been " },
    { "type": "string", "content": "confirmed", "bold": true },
    { "type": "string", "content": "." }
  ],
  "locales": {
    "fr": {
      "elements": [
        { "type": "string", "content": "Votre commande " },
        { "type": "string", "content": "#{{order.id}}", "bold": true },
        { "type": "string", "content": " a été " },
        { "type": "string", "content": "confirmée", "bold": true },
        { "type": "string", "content": "." }
      ]
    },
    "ja": {
      "elements": [
        { "type": "string", "content": "ご注文 " },
        { "type": "string", "content": "#{{order.id}}", "bold": true },
        { "type": "string", "content": " が" },
        { "type": "string", "content": "確認", "bold": true },
        { "type": "string", "content": "されました。" }
      ]
    }
  }
}
```

### Mixed Locale Formats

You can mix `content` and `elements` across different locales within the same text node. This is useful when some translations need rich formatting while others can use simple strings:

```json  theme={null}
{
  "type": "text",
  "elements": [
    { "type": "string", "content": "Need help? " },
    { "type": "link", "content": "Contact support", "href": "https://support.example.com" },
    { "type": "string", "content": "." }
  ],
  "locales": {
    "fr": {
      "content": "Besoin d'aide ? [Contacter le support](https://support.example.com/fr)."
    },
    "es": {
      "elements": [
        { "type": "string", "content": "¿Necesita ayuda? " },
        { "type": "link", "content": "Contactar soporte", "href": "https://support.example.com/es" },
        { "type": "string", "content": "." }
      ]
    }
  }
}
```

In this example, the French locale uses a `content` string (which Courier wraps into a single text element at render time), while the Spanish locale preserves the structured elements with an inline link.

### When Both `content` and `elements` Are Present

If a locale entry includes both `content` and `elements`, only `elements` is used — `content` is ignored. We recommend choosing one format per locale entry to keep your templates clear. See the [resolution table](#text-node-locale-resolution) for all combinations.

## Locale Sources

Courier determines the recipient's locale from the following sources, in order of precedence:

1. **`message.to.locale`**: Explicitly set in the `to` object of the send request (highest priority)
2. **`profile.locale`**: Set in the top-level `profile` object of the send request
3. **User profile locale**: Stored in the user's profile via the [Profiles API](/platform/users/users-overview)
4. **Default fallback**: If no locale is found, the default content is used

<Note>
  When `message.to.locale` is provided, it takes precedence over all other locale sources. The locale from `message.to` is merged into the profile object during processing, so it will override any locale stored in the user's profile or passed in the top-level `profile` object.
</Note>

You can specify the locale in multiple ways:

<CodeGroup>
  ```bash cURL icon="terminal" wrap theme={null}
  # Option 1: In message.to.locale (highest priority)
  curl -X POST https://api.courier.com/send \
    -H "Authorization: Bearer $COURIER_AUTH_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "message": {
        "to": {
          "email": "user@example.com",
          "locale": "fr"
        },
        "content": { ... }
      }
    }'
  ```

  ```bash cURL icon="terminal" wrap theme={null}
  # Option 2: In profile.locale
  curl -X POST https://api.courier.com/send \
    -H "Authorization: Bearer $COURIER_AUTH_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "message": {
        "to": {
          "email": "user@example.com"
        },
        "content": { ... }
      },
      "profile": {
        "locale": "fr"
      }
    }'
  ```

  ```javascript Node.js icon="node-js" lines theme={null}
  // Option 1: In message.to.locale (highest priority)
  await courier.send({
    message: {
      to: {
        email: "user@example.com",
        locale: "fr",
      },
      content: { ... },
    },
  });

  // Option 2: In profile.locale
  await courier.send({
    message: {
      to: {
        email: "user@example.com",
      },
      content: { ... },
    },
    profile: {
      locale: "fr",
    },
  });
  ```

  ```python Python icon="python" lines theme={null}
  # Option 1: In message.to.locale (highest priority)
  client.send_message(
      message={
          "to": {
              "email": "user@example.com",
              "locale": "fr",
          },
          "content": { ... },
      }
  )

  # Option 2: In profile.locale
  client.send_message(
      message={
          "to": {
              "email": "user@example.com",
          },
          "content": { ... },
      },
      profile={
          "locale": "fr",
      }
  )
  ```
</CodeGroup>

<Tip>
  **Pro Tip**: Set the locale in user profiles (via the Profiles API) to automatically localize all notifications for that user. This way, you don't need to specify the locale in every send request. The locale from the user profile will be used unless overridden by `message.to.locale` or `profile.locale` in the send request.
</Tip>

## Best Practices

### Use Consistent Locale Codes

Use standard locale codes (e.g., `en-US`, `es-ES`, `fr-FR`) or simple language codes (e.g., `en`, `es`, `fr`) consistently across your templates. Courier supports any locale string format, but consistency makes maintenance easier.

### Provide Default Content

Always provide default content for each element. This ensures your notifications render correctly even if:

* A user's locale isn't supported
* A translation is missing
* The locale field is omitted

### Localize URLs When Needed

For action buttons and images, consider localizing the `href` and `src` properties to point to localized versions of your website or app:

```json  theme={null}
{
  "type": "action",
  "content": "View Dashboard",
  "href": "https://app.example.com/dashboard",
  "locales": {
    "es": {
      "content": "Ver Panel",
      "href": "https://app.example.com/es/dashboard"
    }
  }
}
```

### Combine with Channel-Specific Customization

You can combine locales with [channel-specific customization](/platform/content/elemental/control-flow#channel-specific-content) to create fully localized, channel-optimized notifications:

```json  theme={null}
{
  "type": "channel",
  "channels": ["email"],
  "elements": [
    {
      "type": "text",
      "content": "Check your email for details",
      "locales": {
        "es": {
          "content": "Revisa tu correo para más detalles"
        }
      }
    }
  ]
}
```

### Test All Locales

Before deploying, test your templates with all supported locales to ensure:

* All translations are present
* Handlebars variables work correctly in all languages
* URLs and links are properly localized
* Text fits within UI constraints (button sizes, email widths, etc.)

## Related Approaches

Elemental locales are defined directly in your template JSON, making them ideal for templates where translations are known at template creation time. However, Courier offers other internationalization approaches that may better suit your needs:

## Related Documentation

<CardGroup cols={2}>
  <Card title="Elements Reference" icon="file-code" href="/platform/content/elemental/elements/index">
    Complete reference for all Elemental element types and their properties, including locale support.
  </Card>

  <Card title="Localization" icon="globe" href="/platform/content/localization">
    For Business customers: API-based translation workflow with webhooks, programmatic locale management, and translation service integration.
  </Card>

  <Card title="Control Flow" icon="code" href="/platform/content/elemental/control-flow">
    Combine locales with channel-specific customization and conditional logic.
  </Card>

  <Card title="Profiles API" icon="user" href="/platform/users/users-overview">
    Manage user profiles and set default locales for automatic localization.
  </Card>
</CardGroup>
