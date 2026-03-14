# Source: https://documentation.onesignal.com/docs/en/using-liquid-syntax.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Liquid syntax

> Learn how to personalize message content in OneSignal using Liquid syntax across email, push notifications, SMS, in-app messages, and Live Activities.

Liquid is a templating language supported by OneSignal to personalize messages across channels including email, push, SMS, in-app, and Live Activities. It uses tags, filters, and conditionals to dynamically customize message content.

To learn more about Liquid syntax, see the [official Liquid documentation](https://shopify.github.io/liquid/basics/introduction/).

***

## Supported fields by message type

<Tabs>
  <Tab title="Email">
    * Subject, Reply-to, and Pre-header
    * Message Body
    * Image substitution in HTML blocks. Example: `<img src="{{image_url}}"/>`
    * Button block actions like URLs, Mail to, and other fields.
  </Tab>

  <Tab title="Push">
    * Title (`headings`), Subtitle, Body (`contents`)
    * Image URL
    * Launch URL. Example: `https://example.com/{{last_category_viewed}}`
    * Additional `data` doesn't support Liquid syntax.
  </Tab>

  <Tab title="SMS">
    * Message Body (`contents`)
  </Tab>

  <Tab title="In-App Messages">
    <Warning>
      Only Tag substitution is supported at this time.

      The tag must be set before the user opens the app to start a new session. The tags available are in the [`getTags` method](./mobile-sdk-reference#gettags).
    </Warning>

    **Block editor:**

    * Tag substitution works in Text, Button, Image Blocks.

    **HTML editor:**

    * Tag substitution works in:
      * Header `<h*>` and `<p>` tags. Example: `<h2>Hello {{first_name}}!</h2>`
      * Element attributes: `["src", "href", "action", "data"]`. Example: `<img src="{{image_url}}"/>`

    <Note>
      See [In-app message JavaScript APIs](./in-app-message-api) for more details and examples.
    </Note>
  </Tab>

  <Tab title="Live Activities">
    * Within the `event_updates`, `contents` and `headings` properties.
  </Tab>
</Tabs>

***

## Basic syntax

Liquid uses two main syntax structures:

1. **Output Tags**: `{{ ... }}` - Display data from a variable or object.
2. **Logic Tags**: `{% ... %}` - Execute conditional statements or loops.

***

## Data sources

| Source                                                   | Example                         | Description                                                                                                              |
| -------------------------------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Tag                                                      | `{{ first_name }}`              | OneSignal SDK or API (`tags`)                                                                                            |
| Property                                                 | `{{ subscription.email }}`      | System-managed (email, external\_id, language, etc.)                                                                     |
| Journey Name                                             | `{{ journey.name }}`            | System-managed                                                                                                           |
| Custom Data                                              | `{{ message.custom_data.key }}` | `custom_data` passed in [Create Message API](/reference/create-message)                                                  |
| [Data Feeds](./data-feeds)                               | `{{ data_feed.cart.size }}`     | Data Feeds let you pull real-time data from your APIs directly into messages at send time.                               |
| [Custom Events](./message-personalization#custom-events) | `{{ journey.last_event.name }}` | Set via [Event Triggered Journeys](./journeys-settings#custom-events), [Wait Until nodes](./journeys-actions#wait-until) |

## Conditionals

### Operators

* `==`, `!=`, `>`, `<`, `>=`, `<=`
* `and`, `or`
* `contains` (string or array)

<Info>Operations run right to left. Parentheses are not supported.</Info>

```text liquid theme={null}
{% if true or false and false %}
  This is true.
{% endif %}
```

### `if`, `elsif`, `else`

```text liquid theme={null}
{%- assign userLang = subscription.language -%}
{% if userLang == "es" -%}
Hola {{ first_name }}!
{%- elsif userLang == "fr" -%}
Bonjour {{ first_name }}!
{%- else -%}
Hello {{ first_name }}!
{%- endif %}
```

### `unless`

```text liquid theme={null}
{% unless level == "1" %}
  Great job getting past the first level!
{% endunless %}
```

***

## Filters

Apply filters using `{{ variable | filter }}` to adjust how the data is displayed.

### `default`

Assign a default value if the property is empty or does not exist.

```text liquid theme={null}
Hello {{ first_name | default: "there" }}.
```

### `date`

The date filter converts a timestamp into another date format. The format for this syntax is the same as [strftime](https://strftime.net/). The input uses the same format as Ruby’s [Time.parse](https://ruby-doc.org/stdlib-2.4.1/libdoc/time/rdoc/Time.html).

Set dates as a unix timestamp in seconds with tags. This allows for use of both liquid syntax personalization and segmentation with [Time Operators](./time-operators). For example, a tag might look like: `bill_due : 1687968776`

```text liquid theme={null}
{{ bill_due | date: "%a, %b %d, %y" }}
{{ "now" | date: "%Y-%m-%d %H:%M" }}

```

```text Result theme={null}
Wed, Jun 28, 23
```

```text liquid theme={null}
{{ bill_due | date: "%Y" }}
```

```text Result theme={null}
2023
```

Date formatting works on strings if they contain well-formatted dates.

```text liquid theme={null}
{{ "March 14, 2016" | date: "%b %d, %y" }}
```

```text Result theme={null}
Mar 14, 16
```

To get the current time, pass the special word `now` (or `today`) along with the date filter.

```text liquid theme={null}
This message was sent at {{ "now" | date: "%Y-%m-%d %H:%M" }}.
```

```text Result theme={null}
This message was sent at 2022-11-02 14:39.
```

<Info>
  The current time will be rendered in the message based on when the message is
  sent to the recipient. If you are testing the message, you will see the
  current time as when the test message was sent.
</Info>

### `capitalize`

This filter makes the first character of a string capitalized and converts the remaining characters to lowercase.

```text liquid theme={null}
{{ "my GREAT title" | capitalize }}
```

```text Result theme={null}
My great title
```

### `round`

This filter rounds a number to the nearest integer, or, if a number is passed as an argument, to that number of decimal places.

```text liquid theme={null}
{{ 1.2 | round }}
  {{ 2.7 | round }}
{{ 183.357 | round: 2 }}
```

```text Result theme={null}
1
3
183.36
```

### `pluralize`

This filter returns the singular or plural form of a string based on a given number. The number must be a whole number and can be provided as a string. Both the singular and plural forms of a string must be provided.

```text liquid theme={null}
{{ 1 | pluralize: "singular", "plural" }}
{{ 2 | pluralize: "singular", "plural" }}
1 {{ 1 | pluralize: "person", "people" }}
2 {{ 2 | pluralize: "person", "people" }}
2 {{ "2" | pluralize: "person", "people" }}
```

```text Result theme={null}
singular
plural
1 person
2 people
2 people
```

***

## Iteration

### `for` loops

Repeatedly executes a block of code. For a full list of attributes available within a `for` loop, refer to the `for` loop object.

```text liquid theme={null}
{% for product in message.custom_data.products %}
  - {{ product.name }}
  {% else %}
    Sorry, we're sold out of all products.
  {% endfor %}
```

```ruby Request Body theme={null}
{
  "app_id": "5eb5a37e-b458-11e3-ac11-000c2940e62c",
    "template_id": "be4a8044-bbd6-11e4-a581-000c2940e62c",
    "custom_data": {
      "products": [
        { "name": "Sweater" },
        { "name": "Hat" },
        { "name": "Shirt" }
      ]
    }
  }
```

```text Results theme={null}
  - Sweater
  - Hat
  - Shirt

  // if message.custom_data.products is empty
  Sorry we're sold out of all products
```

<Warning>
  While powerful and flexible, the usage of `for` loops in liquid syntax can
  lead to poor notification delivery performance in certain rare cases. Be
  mindful of your usage of `for` loops. Also note that we prevent the usage of
  `for` loops in a few Push Channel fields: `contents`, `headings`, `subtitle`,
  `apns_alert`, and `url`
</Warning>

### `limit` & `offset`

Limits the loop to the specified number of iterations. For example, if you only want to show 4 products in a message, you could use Limits and Offsets to specify the number of products shown.

```text Data theme={null}
great_numbers = [1,2,3,4,5,5]
```

```text liquid theme={null}
{% for number in great_numbers limit:2 %}
  {{ number }}
{% endfor %}
```

```text Result theme={null}
1 2
```

To begin the loop at the specified index, add an offset value:

```text Data theme={null}
great_numbers = [1,2,3,4,5,5]
```

````text liquid theme={null}
{% for number in great_numbers limit: 3 %}
  {{ number }}
{% endfor %}

{% for number in great_numbers limit: 3 offset: 3 %}
  {{ number }}
{% endfor %}
```text Result
1 2 3
4 5 6
````

### `where`

Creates an array including only the objects with a given property value, or any truthy value by default.

In this example, assume you have a list of products and you want to show your kitchen products separately. Using `where`, you can create an array containing only the products that have a `type` of `kitchen`.

```text Data theme={null}
products = [
  {name:"Vacuum", type:"electronics"},
  {name:"Spatula", type:"kitchen"},
  {name:"Television", type:"electronics"},
  {name:"Garlic press", type:"kitchen"}
]
```

```text liquid theme={null}
All products:
{% for product in products %}
- {{ product.name }}
{% endfor %}

{% assign kitchen_products = products | where: "type", "kitchen" %}

Kitchen products:
{% for product in kitchen_products %}
- {{ product.name }}
{% endfor %}
```

```text Result theme={null}
All products:
  - Vacuum
  - Spatula
  - Television
  - Garlic press

Kitchen products:
- Spatula
- Garlic press
```

***

## String Manipulation

Occasionally you may have data tags that contain strings that is in a format that is not suitable to be shown directly to your users, and you may need to manipulate the string to adjust the format. Below is a table of liquid syntax commands that can be used to adjust strings. You can use string manipulation both on [Tags](./add-user-data-tags) and directly on strings written into the message.

| Command         | Description                                                                | Example                                                  | Example Output |
| --------------- | -------------------------------------------------------------------------- | -------------------------------------------------------- | -------------- |
| `replace`       | Replaces a substring with another string.                                  | `{{ 'hello world' \| replace: 'world', 'there' }}`       | hello there    |
| `capitalize`    | Capitalizes the first letter of a string.                                  | `{{ 'hello' \| capitalize }}`                            | Hello          |
| `upcase`        | Converts a string to uppercase.                                            | `{{ 'hello' \| upcase }}`                                | HELLO          |
| `downcase`      | Converts a string to lowercase.                                            | `{{ 'HELLO' \| downcase }}`                              | hello          |
| `strip`         | Removes leading and trailing whitespace from a string.                     | `{{ ' hello ' \| strip }}`                               | hello          |
| `strip_html`    | Removes all HTML tags from a string.                                       | `{{ '<p>hello</p>' \| strip_html }}`                     | hello          |
| `truncate`      | Shortens a string to a specified length, adding an ellipsis (…) if needed. | `{{ 'This is a long sentence' \| truncate: 10 }}`        | This is a…     |
| `truncatewords` | Truncates a string after a certain number of words.                        | `{{ 'This is a long sentence' \| truncatewords: 2 }}`    | This is…       |
| `replace_first` | Replaces the first occurrence of a substring.                              | `{{ 'hello world' \| replace_first: 'world', 'there' }}` | hello there    |
| `prepend`       | Adds a string to the beginning of another string.                          | `{{ 'world' \| prepend: 'hello ' }}`                     | hello world    |
| `append`        | Adds a string to the end of another string.                                | `{{ 'hello' \| append: ' world' }}`                      | hello world    |
| `lstrip`        | Removes leading whitespace from a string.                                  | `{{ ' hello' \| lstrip }}`                               | hello          |
| `rstrip`        | Removes trailing whitespace from a string.                                 | `{{ 'hello ' \| rstrip }}`                               | hello          |

***

## FAQ

### Why is substitution not working?

* In-App Messages do not support property substitution.
* Tag substitution does not work when using “Send Test Message”.
* Tag keys must be alphanumeric, or use \_ and - (no periods or spaces).
* Substitution does not appear in preview mode — send a real message to test.

### How to control whitespace and newlines?

Use hyphens: `{{- ... -}}`, `{%- ... -%}` to trim surrounding whitespace.
See [Whitespace control](https://shopify.github.io/liquid/basics/whitespace/) for more details.

### How to handle user-generated content?

Wrap user-generated text in `{% raw %}` and `{% endraw %}` to prevent Liquid parsing. See ["raw" syntax](https://shopify.dev/docs/api/liquid/tags/raw).

```json json theme={null}
{
  "contents": {
    "en": "{% raw %} Your user-generated content with invalid characters like {{ {% endraw %}"
  }
}
```

Built with [Mintlify](https://mintlify.com).
