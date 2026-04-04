# Source: https://www.courier.com/docs/platform/content/elemental/elements/jsonnet.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Jsonnet

> Embed Jsonnet templates in your Elemental notifications to programmatically generate structured content. Jsonnet is a data templating language that generates JSON output.

## Overview

The Jsonnet element allows you to embed Jsonnet templates directly within your Elemental notification structure. Jsonnet is a data templating language designed to generate JSON output, making it ideal for programmatically creating structured content, avoiding repetition, and building complex data structures.

**When to use:**

* Generate dynamic JSON structures based on data
* Create reusable template logic with functions and variables
* Build complex nested objects programmatically
* Avoid repetitive JSON structures
* Generate locale-specific content programmatically

<Warning>
  Jsonnet is an advanced templating feature. It requires knowledge of the Jsonnet language syntax. For simple content, consider using [Text elements](/platform/content/elemental/elements/text) with Handlebars variables instead.
</Warning>

## Basic Example

<CodeGroup>
  ```json icon="code" theme={null}
  {
    "type": "jsonnet",
    "template": "local person(name, age) = { name: name, age: age, greeting: \"Hello \" + name + \"!\" }; { user: person(\"Alice\", 30) }"
  }
  ```

  ```javascript Node.js icon="node-js" lines theme={null}
  const { CourierClient } = require("@trycourier/courier");

  const courier = new CourierClient({
    authorizationToken: process.env.COURIER_AUTH_TOKEN,
  });

  await courier.send({
    message: {
      to: { email: "user@example.com" },
      content: {
        version: "2022-01-01",
        elements: [
          {
            type: "jsonnet",
            template: `local person(name, age) = {
              name: name,
              age: age,
              greeting: "Hello " + name + "!"
            };
            {
              user: person("Alice", 30)
            }`,
          },
        ],
      },
    },
  });
  ```

  ```python Python icon="python" lines theme={null}
  import os
  from trycourier import Courier

  client = Courier(auth_token=os.environ["COURIER_AUTH_TOKEN"])

  client.send_message(
      message={
          "to": {"email": "user@example.com"},
          "content": {
              "version": "2022-01-01",
              "elements": [
                  {
                      "type": "jsonnet",
                      "template": """local person(name, age) = {
                          name: name,
                          age: age,
                          greeting: "Hello " + name + "!"
                      };
                      {
                          user: person("Alice", 30)
                      }""",
                  }
              ],
          },
      }
  )
  ```
</CodeGroup>

## Fields

<ParamField path="type" type="string" required>
  The type of element. For Jsonnet elements, this value must be `"jsonnet"`.
</ParamField>

<ParamField path="template" type="string" required>
  The Jsonnet template code. This is a string containing valid Jsonnet syntax that will be evaluated to generate JSON output. The template has access to the message data via Jsonnet's standard variable access.
</ParamField>

<ParamField path="locales" type="object">
  Region-specific Jsonnet templates. The object keys are locale codes (e.g., `"es"`, `"fr"`), and values are Jsonnet template strings that will be used for that locale. See [Locales documentation](/platform/content/elemental/locales) for more details.
</ParamField>

<ParamField path="channels" type="string[]">
  An array of channel names. The Jsonnet element will only be rendered for the specified channels. See [Control Flow documentation](/platform/content/elemental/control-flow#channel-specific-content) for details.
</ParamField>

## Jsonnet Language Basics

Jsonnet is a data templating language that extends JSON with features like:

* **Variables**: `local name = "Alice";`
* **Functions**: `local greet(name) = "Hello " + name;`
* **Object composition**: Merge objects with `+`
* **Conditionals**: `if condition then value1 else value2`
* **Loops**: `[x * 2 for x in [1, 2, 3]]`
* **Imports**: `local lib = import "lib.jsonnet";`

<Info>
  For complete Jsonnet language documentation, see the [official Jsonnet documentation](https://jsonnet.org/).
</Info>

## Examples & Variants

### Simple Object Generation

Generate a simple JSON object:

```json  theme={null}
{
  "type": "jsonnet",
  "template": "{ message: \"Welcome!\", timestamp: \"2024-01-15\" }"
}
```

**Output:**

```json  theme={null}
{
  "message": "Welcome!",
  "timestamp": "2024-01-15"
}
```

### Using Functions

Create reusable functions:

```json  theme={null}
{
  "type": "jsonnet",
  "template": "local formatPrice(amount) = \"$\" + std.toString(amount); { price: formatPrice(99.99), discount: formatPrice(49.99) }"
}
```

**Output:**

```json  theme={null}
{
  "price": "$99.99",
  "discount": "$49.99"
}
```

### Conditional Content

Generate different content based on conditions:

```json  theme={null}
{
  "type": "jsonnet",
  "template": "local isPremium = true; { tier: if isPremium then \"premium\" else \"basic\", features: if isPremium then [\"feature1\", \"feature2\", \"feature3\"] else [\"feature1\"] }"
}
```

**Output:**

```json  theme={null}
{
  "tier": "premium",
  "features": ["feature1", "feature2", "feature3"]
}
```

### Array Generation

Generate arrays programmatically:

```json  theme={null}
{
  "type": "jsonnet",
  "template": "{ items: [\"item\" + std.toString(i) for i in [1, 2, 3, 4, 5]] }"
}
```

**Output:**

```json  theme={null}
{
  "items": ["item1", "item2", "item3", "item4", "item5"]
}
```

### Localized Templates

Provide different Jsonnet templates for different locales:

```json  theme={null}
{
  "type": "jsonnet",
  "template": "{ greeting: \"Hello\", name: \"World\" }",
  "locales": {
    "es": "{ greeting: \"Hola\", name: \"Mundo\" }",
    "fr": "{ greeting: \"Bonjour\", name: \"Monde\" }"
  }
}
```

### Complex Nested Structures

Build complex nested objects:

```json  theme={null}
{
  "type": "jsonnet",
  "template": "local user(name, email) = { profile: { name: name, email: email }, settings: { notifications: true } }; { users: [user(\"Alice\", \"alice@example.com\"), user(\"Bob\", \"bob@example.com\")] }"
}
```

**Output:**

```json  theme={null}
{
  "users": [
    {
      "profile": {
        "name": "Alice",
        "email": "alice@example.com"
      },
      "settings": {
        "notifications": true
      }
    },
    {
      "profile": {
        "name": "Bob",
        "email": "bob@example.com"
      },
      "settings": {
        "notifications": true
      }
    }
  ]
}
```

### Channel-Specific Jsonnet

Render Jsonnet only for specific channels:

```json  theme={null}
{
  "type": "jsonnet",
  "channels": ["email"],
  "template": "{ format: \"html\", content: \"<p>Email-specific content</p>\" }"
}
```

## Best Practices

* **Keep templates readable**: Use multi-line strings in your code for complex templates
* **Use functions for reusability**: Extract common logic into functions
* **Validate output**: Ensure your Jsonnet templates produce valid JSON
* **Test templates**: Test Jsonnet templates independently before embedding in Elemental
* **Consider alternatives**: For simple content, Handlebars in Text elements may be simpler
* **Error handling**: Jsonnet syntax errors will cause rendering to fail, so test thoroughly

<Warning>
  Jsonnet templates are evaluated at render time. Syntax errors or runtime errors in Jsonnet will cause the entire notification to fail to render. Always test your Jsonnet templates before deploying.
</Warning>

## Channel Support

* **Email**: ✅ Full support
* **Push**: ✅ Supported (JSON output can be used in push payloads)
* **SMS**: ⚠️ Limited support (JSON output may need to be stringified)
* **Inbox**: ✅ Full support

## Related Elements

* [Text Element](/platform/content/elemental/elements/text) - For simple text content with Handlebars
* [HTML Element](/platform/content/elemental/elements/html) - For raw HTML content
* [Group Element](/platform/content/elemental/elements/group) - For grouping Jsonnet with other elements
* [Control Flow](/platform/content/elemental/control-flow) - For conditional rendering
* [Locales](/platform/content/elemental/locales) - For locale-specific content

## Additional Resources

* [Jsonnet Language Documentation](https://jsonnet.org/)
* [Jsonnet Tutorial](https://jsonnet.org/learning/tutorial.html)
* [Jsonnet Standard Library](https://jsonnet.org/ref/stdlib.html)
