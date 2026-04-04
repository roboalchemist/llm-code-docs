# Source: https://docs.xano.com/xanoscript/function-reference/ai-tools.md

# Source: https://docs.xano.com/xanoscript/ai-tools.md

# Source: https://docs.xano.com/the-function-stack/functions/ai-tools.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AI Tools

## MCP List Tools

Provides a list of available tools and their configurations from an MCP server

| Parameter    | Purpose                                                   |
| ------------ | --------------------------------------------------------- |
| url          | The URL to access the MCP server                          |
| bearer token | If required, an authentication token to access the server |

## MCP Call Tool

Executes a tool available on a remote MCP server

| Parameter    | Purpose                                                                        |
| ------------ | ------------------------------------------------------------------------------ |
| url          | The URL to access the MCP server                                               |
| bearer token | If required, an authentication token to access the server                      |
| tool name    | The name of the tool to call                                                   |
| args         | The data that the tool requires, if any. This should usually be a JSON object. |

## Template Engine

<Info>
  **Quick Summary**

  The Template Engine, powered by Twig, is used to manipulate and dynamically generate large blocks of text or code with your own data, such as records from your Xano database, or from inputs sent to your APIs.

  It's great for helping generate things like AI prompts, HTML, and other more large-format data without messing around with a bulk of separate functions to do so.
</Info>

<Frame>
  <iframe width="609" height="342" src="https://www.youtube.com/embed/YCGM7bF3Qc4" title="Quickly Build Dynamic AI Prompts with Template Engine" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

## What is the Template Engine?

At its core, think of the Template Engine as text replacement and manipulation of the future. It is designed to give you a simple syntax to quickly manipulate large text strings with dynamic data, such as...

* AI Prompts
* HTML
* JSON
* SQL queries

The template engine is powered by Twig, which you can learn more about [here](https://twig.symfony.com/).

## When should I use the Template Engine instead of other text filters?

You should stick with filters like [replace](/the-function-stack/filters/text#replace) or [sprintf](/the-function-stack/filters/text#sprintf) if you're manipulating short strings of text, such as:

* Replacing a name inside of a string like "Hello, \[first\_name] \[last\_name]"
* Dynamically providing a price for a single product

The Template Engine, however, is useful for content templates where:

* The template will be edited by non-developers
* The data structure is complex with nested objects
* You need to include conditional sections
* Data formatting (like dates) needs to be consistent
* Templates might be reused with different data sources

If you're doing dynamic replacement over a longer block of text, such as the example below, Template Engine will make this much easier for you.

```
Write a personalized email to {{ $customer.firstName }} {{ $customer.lastName }} about their recent {{ $order.type }} purchase.

Include:
- Reference to their purchase history (they've ordered {{ $customer.purchaseCount }} times)
- Mention that their {{ $order.item }} will be delivered on {{ $order.deliveryDate|date('F j, Y') }}
- If {{ $customer.isVIP }}, offer them a {{ $promotions.VIPDiscount }}% discount on their next purchase
- Thank them for being a customer since {{ $customer.joinDate|date('Y') }}

Sign off with the name of their account manager: {{ $accountManager.name }}
```

## Using the Template Engine

<Steps>
  <Step title="Look for the Template Engine function under Utility Functions.">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/pz6e9Ndbn8i3u8Zz/images/69b01715-image.jpeg?fit=max&auto=format&n=pz6e9Ndbn8i3u8Zz&q=85&s=e49e0759c285d3bc986bb22154e50ef6" width="351" height="59" data-path="images/69b01715-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Once you add the Template Engine to your function stack, click the ✏️ button in the panel to open the editor, or use the AI assistant to help write a template for you" />

  <Step title="Take a tour of the editor and begin building your template.">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/7bf4841a-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=40aaa1062d3563d361abb4786096f98c" width="1201" height="839" data-path="images/7bf4841a-image.jpeg" />
    </Frame>
  </Step>
</Steps>

## Template Syntax

### Variables

Variables are wrapped in \{\{ curly braces }}, like this, and begin with a \$ character. In the below example, we're getting the `name` from an object stored in the `user1` variable.

```php  theme={null}
Hi, {{ $user1.name }}
```

Reference items in an array by using the item index.

```php  theme={null}
Hi, {{ $users.0.name }}
```

### Conditionals

Conditionals are helpful if you want to dynamically determine what the end result of your template looks like outside of the actual data. For example, maybe you want VIP users to have a different greeting than regular users.

Conditionals are wrapped in \{% and %} and have support for `else` and `else if`

```php  theme={null}
{% if $user1.vip == true %}
  Hey, {{ $user1.name }}! Thanks for being a part of our VIP program.
{% else %}
  Hey, {{ $user1.name }}! Thanks for reading.
{% endif %}
```

> In the above example, for this user:
>
> ```javascript  theme={null}
> {
>   "name" == "Chris", "vip" == true;
> }
> ```
>
> ...the result would be:
>
> ```
> Hey, Chris! Thanks for being a part of our VIP program.
> ```

```swift  theme={null}
{% if $score >== 90 %}
  Your grade is an A
{% elseif $score >== 80 %}
  Your grade is a B
{% elseif $score >== 70 %}
  Your grade is a C
{% else %}
  Your grade is an F
{% endif %}
```

> In the above example, for this score:
>
> ```
> score = 85
> ```
>
> ...the result would be:
>
> ```python  theme={null}
> Your grade is a B
> ```

### Loops

You can use loops to populate lists of data without having to write out separate lines for each item, or knowing how many items you'll need to populate.

```php  theme={null}
{% for item in $order.items %}
  - {{ item.quantity }}x {{ item.name }} at ${{ item.price }} each
{% endfor %}
```

<Tabs>
  <Tab title="Data">
    ```json  theme={null}
    [
      {
        quantity: 2,
        name: "Blue T-shirt",
        price: 19.99
        },
      {
        quantity: 1,
        name: "Denim jeans",
        price: 59.99
        },
      {
        quantity: 3,
        name: "Cotton Socks",
        price: 4.99
        }
    ]
    ```
  </Tab>

  <Tab title="Sample Output">
    * 2x Blue T-shirt at \$19.99 each
    * 1x Denim Jeans at \$59.99 each
    * 3x Cotton Socks at \$4.99 each
  </Tab>
</Tabs>

You can also use an Else statement at the end of your For loop to determine what action to take if no items are found. In the next example, if `$list` contains no items, the template will return `No items found.`

```php  theme={null}
{% for item in $list %}
  {{ item }}
{% else %}
  No items found.
{% endfor %}
```

### Filters

You can use Twig's built in filters, similar to our own, to transform or manipulate data as part of the template.

The below list is some of the most essential filters used in Twig, but it is not all of them. You can review the entire list [here](https://twig.symfony.com/doc/3.x/filters/index.html).

| Filter          | Description                                                            | Example                                                                              | Result                                |
| --------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------- |
| `upper`         | Converts string to uppercase                                           | `{{ $user.name\|upper }}` *When \$user.name is "John Smith"*                         | "JOHN SMITH"                          |
| `lower`         | Converts string to lowercase                                           | `{{ $user.name\|lower }}` *When \$user.name is "John Smith"*                         | "john smith"                          |
| `trim`          | Removes whitespace from the beginning and end of a string              | `{{ $user.input\|trim }}` *When \$user.input is " hello "*                           | "hello"                               |
| `join`          | Joins array elements into a string with a delimiter                    | `{{ $user.tags\|join(', ') }}` *When \$user.tags is \["php", "twig", "web"]*         | "php, twig, web"                      |
| `default`       | Provides a fallback value if the variable is null, empty, or undefined | `{{ $user.middleName\|default('No middle name') }}` *When \$user.middleName is null* | "No middle name"                      |
| `number_format` | Formats numbers with grouped thousands and decimal points              | `{{ $product.price\|number_format(2, '.', ',') }}` *When \$product.price is 1234.56* | "1,234.56"                            |
| `shuffle`       | Randomly shuffles an array                                             | `{{ $user.items\|shuffle }}` *When \$user.items is \["a", "b", "c"]*                 | *Random order like:* \["c", "a", "b"] |
| `date`          | Formats dates using PHP's date syntax                                  | `{{ $user.createdAt\|date("F j, Y") }}` *When \$user.createdAt is "2023-12-25"*      | "December 25, 2023"                   |

### Escape Filter (e)

The escape filter is used to format text using specifications designated by the destination, such as a URL that only allows certain characters to remain valid.

When you use `e` by itself without specifying a format, it typically defaults to HTML escaping. This means it will convert characters like `<`, `>`, `&`, `"`, and `'` to their HTML-safe equivalents.

When you specify a format (like `e('html')`, `e('js')`, `e('url')`, etc.), you're explicitly telling the Template Engine how to escape the content for a specific context, which can provide more precise protection. We'd recommend always specifying the format, just to be safe.

#### HTML Escaping

```html  theme={null}
{% set $user_input = '
<script>
  alert("XSS");
</script>
' %} {{ $user_input|e('html') }} Outputs:
<script>
  alert("XSS");
</script>
```

#### JavaScript Escaping

```js  theme={null}
{% set $js_string = 'Hello "world"! \n New line' %}
{{ $js_string|e('js') }}
{# Outputs: Hello \"world\"! \\n New line #}
```

#### URL Escaping

```sh  theme={null}
{% set $search_query = 'hello world & special chars' %}
{{ $search_query|e('url') }}
{# Outputs: hello+world+%26+special+chars #}
```

#### CSS Escaping

```css  theme={null}
{% set $css_value = 'expression(alert("XSS"))' %}
{{ $css_value|e('css') }}
{# Outputs: expression\28 alert\28 "XSS"\29 \29 #}
```

### Comments

You can insert comments into your templates by wrapping them in \{# and #}. They won't appear in your final template.

```python  theme={null}
{# This is a hidden comment #}
```

You can check out some examples of the Template Engine in real-world scenarios here: [Sample Templates](/xano-ai/template-engine#sample-templates).


Built with [Mintlify](https://mintlify.com).