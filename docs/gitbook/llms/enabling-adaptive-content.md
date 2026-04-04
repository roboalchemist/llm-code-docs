# Source: https://gitbook.com/docs/documentation/ja-gitbook-documentation/publishing-documentation/adaptive-content/enabling-adaptive-content.md

# Source: https://gitbook.com/docs/documentation/zh/publishing-documentation/adaptive-content/enabling-adaptive-content.md

# Source: https://gitbook.com/docs/documentation/fr/publishing-documentation/adaptive-content/enabling-adaptive-content.md

# Source: https://gitbook.com/docs/publishing-documentation/adaptive-content/enabling-adaptive-content.md

# Enabling adaptive content

To start customizing your documentation experience for your readers, you'll need to enable adaptive content and decide how your visitor data is passed to GitBook. This lets your site's content dynamically adapt based on who's viewing it.

### Enable adaptive content

Before you’re able to pass user data to GitBook, you’ll need to configure your site to use adaptive content.

Head to your [site’s settings](https://gitbook.com/docs/publishing-documentation/site-settings), and enable **Adaptive content** from your site’s audience settings. Once enabled, you’ll get a generated ‘Visitor token signing key’, which you’ll need in order to continue the adaptive content setup.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F5EeWAo5Ij6CKrp69uMl5%2F26_01_06_enable_adaptive_content%402x.png?alt=media&#x26;token=4a1e8558-4b91-4f8b-8581-63d570a2c330" alt="A GitBook screenshot showing the enable adaptive content toggle"><figcaption><p>Enable adaptive content in your site’s Settings</p></figcaption></figure>

### Set your visitor schema

After enabling adaptive content, you’ll need to define a schema for the types of claims you expect GitBook to receive when a user visits your site.

The visitor schema should reflect how these claims are structured when sent to GitBook.

For example, if you expect a visitor to potentially be a beta user in your product, you would set a visitor schema similar to:

```json
{
  "type": "object",
  "properties": {
    "isBetaUser": {
      "type": "boolean",
      "description": "Whether the visitor is a Beta user."
    }
  },
  "additionalProperties": false
}
```

This will also help you use autocomplete when configuring your claims in the [condition editor](https://gitbook.com/docs/publishing-documentation/adapting-your-content#working-with-the-condition-editor). Visitor schemas only support the following types:

{% tabs %}
{% tab title="Strings" %}
Read claims being passed in as strings.

GitBook accepts dynamic strings, meaning you can dynamically pass string data — such as a user’s name, developer tokens, and more.

Strings can also contain an **optional enum** key, which allows you to restrict the data that is received by GitBook to one of it’s set values.

```json
{
  "type": "object",
  "properties": {
    "language": {
          "type": "string",
          "description": "The language of the visitor",
          // Optional enum property
          "enum": [
            "en",
            "fr",
            "it"
          ]
  },
  "additionalProperties": false
}
```

{% hint style="warning" %}
Dynamic strings (strings defined without an enum key) are only accepted for [inline expressions](https://gitbook.com/docs/creating-content/variables-and-expressions#use-variables-in-your-content). Conditional expressions for visibility of elements (pages, sections, blocks) only work with strings defined with enum keys.
{% endhint %}
{% endtab %}

{% tab title="Booleans" %}
Read claims being passed in as booleans.

```json
{
  "type": "object",
  "properties": {
    "isBetaUser": {
      "type": "boolean",
      "description": "Whether the visitor is a Beta user."
    },
  },
  "additionalProperties": false
}
```

{% endtab %}

{% tab title="Objects" %}
Nest claims in an object to group similar values.

```json
{
  // Top level claims
  "type": "object",
  "properties": {
    // Nested claims
    "access": {
      "type": "object",
      "description": "User’s access to product feature",
      "properties": {
        "isAlphaUser": {
          "type": "boolean",
          "description": "Whether the visitor is a Alpha user."
        },
        "isBetaUser": {
          "type": "boolean",
          "description": "Whether the visitor is a Beta user."
        },
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```

{% endtab %}
{% endtabs %}

### Set an unsigned claim

Unsigned claims are a specific type of claim that identifies claims coming through that might not be signed by a client application. It is required to set claims in your visitor schema as `unsigned` if you are passing claims through URL parameters, unsigned cookies, and feature flags.

If you intend to work with unsigned claims, you will need to declare the claims you are expecting in the schema under an “unsigned” prop alongside your signed claims.

```json
{
  "type": "object",
  "properties": {
    "isBetaUser": {
      "type": "boolean",
      "description": "Whether the visitor is a Beta user."
    },
    // Add unsigned claims
    "unsigned": {
      "type": "object",
      "description": "Unsigned claims of the site visitor.",
      "properties": {
        "language": {
          "type": "string",
          "description": "The language of the visitor",
          // Optional enum property
          "enum": [
            "en",
            "fr",
            "it"
          ]
        }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```

### Pass visitor data to GitBook

GitBook provides different ways to pass visitor data to adapt your site's content. After defining your schema, you’ll need to decide how you want to pass your visitor data to GitBook.

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><i class="fa-cookie">:cookie:</i></td><td><strong>Cookies</strong></td><td>Pass visitor data into your docs through a public or signed cookie.</td><td><a href="enabling-adaptive-content/cookies">cookies</a></td></tr><tr><td><i class="fa-link">:link:</i></td><td><strong>URL</strong></td><td>Pass visitor data into your docs through URL query parameters.</td><td><a href="enabling-adaptive-content/url">url</a></td></tr><tr><td><i class="fa-flag">:flag:</i></td><td><strong>Feature flags</strong></td><td>Pass visitor data into your docs through a feature flag provider.</td><td><a href="enabling-adaptive-content/feature-flags">feature-flags</a></td></tr><tr><td><i class="fa-lock">:lock:</i></td><td><strong>Authenticated access</strong></td><td>Pass visitor data into your docs through an authentication provider.</td><td><a href="enabling-adaptive-content/authenticated-access">authenticated-access</a></td></tr></tbody></table>
