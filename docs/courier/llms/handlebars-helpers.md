# Source: https://www.courier.com/docs/platform/content/template-designer/handlebars-helpers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Handlebars Helpers

> Courier Handlebars Helpers extend core templating with logic, math, string formatting, localization, control flow, and data operations for personalized, dynamic notifications.

> Courier's custom Handlebars helpers for use in email template overrides and custom brand templates.

The default Handlebars helpers can be found [here](https://handlebarsjs.com/guide/block-helpers.html).

<Tip>
  Check out our [common use cases documentation](/platform/content/template-designer/handlebars-designer#use-cases) on details on how to use these functions. Don't see a custom handlebars helper you need in the list? [Share your use case](mailto:support@courier.com).
</Tip>

## Whitespace Control

Handlebars expressions can leave unwanted blank lines in rendered output, especially when conditionals hide content. Use the tilde (`~`) character inside expression braces to strip whitespace on that side of the tag.

| Syntax             | Effect                               |
| ------------------ | ------------------------------------ |
| `{{~expression}}`  | Strips whitespace **before** the tag |
| `{{expression~}}`  | Strips whitespace **after** the tag  |
| `{{~expression~}}` | Strips whitespace on **both sides**  |

This works with all Handlebars tags, including block helpers like `#if`, `#each`, `else`, and closing tags.

**Example: Blank lines from hidden conditionals**

Without tilde syntax, a hidden `#if` block leaves blank lines in the output:

```handlebars  theme={null}
Hello {{var "name"}},

{{#if (var "has_coupon")}}
Your coupon code is: {{var "coupon_code"}}
{{/if}}

Thanks for your order!
```

When `has_coupon` is false, this renders as:

```text  theme={null}
Hello Alice,


Thanks for your order!
```

Adding tildes removes the blank lines:

```handlebars  theme={null}
Hello {{var "name"}},

{{~#if (var "has_coupon")}}
Your coupon code is: {{var "coupon_code"}}
{{~/if~}}

Thanks for your order!
```

When `has_coupon` is false, this now renders cleanly:

```text  theme={null}
Hello Alice,
Thanks for your order!
```

<Tip>
  Start by adding `~` to the opening `{{~#if` and closing `{{~/if~}}` tags. Adjust placement if the output has too little or too much spacing. The tilde strips all whitespace (including newlines) on its side, so over-applying it can collapse lines together.
</Tip>

***

## Courier Handlebars Helpers

## Logic

### and

Returns `true` if all arguments are truthy, `false` if one argument is falsy, and `true` if no arguments

**Parameters**

* `input` **{String|Number }**

**Note:** Data and profile can have booleans.

**Example:**

```handlebars  theme={null}
{{#if (and (var "boolean") (var "another_boolean"))}}
  <strong>True</strong>
{{else}}
  <strong>False</strong>
{{/if}}
<!-- Output: dependent on variables, 'true' will render if condition returns true -->

<!-- Reference a "profile" variable -->
{{#if (and (var "profile.boolean") (var "profile.another_boolean"))}}
  <strong>True</strong>
{{else}}
  <strong>False</strong>
{{/if}}
```

### condition

Use the if statement to specify a block of code to be executed if a condition is true. Will throw an error if the operator is unsupported.

* Require two operands separated by an operator.
* Run the appropriate operation on the operands.

**Parameters**

* `input` **{String|Number}**

**Note:** Data and profile can have booleans.

**Example:**

```handlebars  theme={null}
{{#if (condition (var "eligible") "==" "yes")}}
  <strong>Hello!</strong>
{{else}}
  <strong>Bye</strong>
{{/if}}
<!-- Output: dependent on variable -->

<!-- Reference a "profile" variable -->
{{#if (condition (var "profile.name") "==" "rod")}}
  <strong>Hello {{var "profile.name"}}!</strong>
{{else}}
  <strong>Hello there</strong>
{{/if}}

<!-- Reference a boolean -->
{{#if (condition (var "profile.hungry") "==" "true")}}
  <strong>{{var "profile.name"}} is hungry!</strong>
{{else}}
  <strong>{{var "profile.name"}} is not hungry</strong>
{{/if}}
```

**Arithmetic Evaluation Operators:**

The `condition` helper supports various comparison operators for arithmetic evaluations:

* `==` - Equal to
* `!=` - Not equal to
* `>` - Greater than
* `<` - Less than
* `>=` - Greater than or equal to
* `<=` - Less than or equal to

**Examples:**

```handlebars  theme={null}
<!-- Less than -->
{{#if (condition 1 "<" 2)}}
  Display block
{{/if}}

<!-- Greater than -->
{{#if (condition (var "age") ">" 18)}}
  <strong>You are an adult</strong>
{{/if}}

<!-- Greater than or equal to -->
{{#if (condition (var "score") ">=" 100)}}
  <strong>You passed!</strong>
{{/if}}

<!-- Less than or equal to -->
{{#if (condition (var "quantity") "<=" 10)}}
  <strong>Low stock</strong>
{{/if}}

<!-- Not equal to -->
{{#if (condition (var "status") "!=" "inactive")}}
  <strong>Account is active</strong>
{{/if}}

<!-- Equal to -->
{{#if (condition (var "status") "==" "active")}}
  <strong>Welcome back!</strong>
{{/if}}
```

### conditional

* Loops through all arguments and ensures all are truthy if using the "and" logical operator.
* Loops through all arguments and ensures one is truthy if using the "or" logical operator.
* Returns true if the conditions passed, false otherwise (use #unless helper to hide content if condition passes).

**Parameters**

* `input` **{String|Number}**

**Note:** Data and profile can have booleans.

```handlebars  theme={null}
{{conditional
  (filter "data" "customer.name" "EQUALS" "josh")
  (filter "profile" "email" "CONTAINS" "@trycourier.com")
}}
<!-- Output: dependent on variable -->
```

***

### not

Return `false` if the argument is truthy. Returns `true` if argument is `false`, `undefined`, `null`, `""`, `0`, or `[]`

**Parameters**

* `input`

**Example**

```handlebars  theme={null}
{{not true}}
<!-- Output: false -->

{{not "string"}}
<!-- Output: false -->

{{not "" }}
<!-- Output: true -->

{{not undefined }}
<!-- Output: true -->
```

### or

Returns `true` if one argument is truthy, `false` if all argument are falsy, and `false` if no arguments.

**Parameters**

* `input` **{String|Number}**

**Note:** Data and profile can have booleans.

```handlebars  theme={null}
{{#if (or (var "boolean") (var "another_boolean"))}}
  <strong>True</strong>
{{else}}
  <strong>False</strong>
{{/if}}
<!-- Output: dependent on variables, 'true' will render if condition returns true -->

<!-- Reference a "profile" variable -->
{{#if (or (var "profile.boolean") (var "profile.another_boolean"))}}
  <strong>True</strong>
{{else}}
  <strong>False</strong>
{{/if}}
```

## Data

### default

Returns the `value` if it is not nullish.

**Parameters**

* `input` **{String|Number}**

**Note:** Data and profile can have booleans.

**Example:**

```handlebars  theme={null}
{{default undefined (var "customer")}}
<!-- Output: Returns the default value -->
```

### each

Iterates over a list. Inside the block, you can use `this` to reference the element being iterated over.

**Parameters**

* `input` **{String|Number}**

**Example:**

```json  theme={null}
"data": {
    "people": [
      {
        "name": "Rod"
      },
      {
        "name": "TK"
      },
      {
        "name": "Suhas"
      }
    ]
  }
```

```handlebars  theme={null}
<ul>
  {{#each people}}
    <li>{{this.name}}</li>
  {{/each}}
</ul>
<!-- Output: unordered list -->
```

<Note>
  **NOTE**

  This is a modified version of [this Handlebars helper](https://github.com/handlebars-lang/handlebars.js/blob/212f9d930b1a39599da2646ac23da64f6552b9d0/lib/handlebars/helpers/each.js).
</Note>

### path

Use the variable handler to resolve a `JSONPath`, and returns the resolved value, similar to [var](#var). Returns undefined if the value was not found.

**Parameters**

* `input` **{String}**

**Example:**

```handlebars  theme={null}
{{path "profile.doesNotExist"}}
<!-- Output: -->

{{var "profile.doesNotExist"}}
<!-- Output: {profile.doesNotExist} -->

{{#if (path "profile.doesNotExist")}}
abc123
{{/if}}
<!-- Output: -->

{{#if (var "profile.doesNotExist")}}
abc123
{{/if}}
<!-- Output: abc123 -->
```

### set

Set the value of a variable specified by `name`. The top level names cannot start with `brand`, `data`, `event`, `profile`, `recipient`, `urls`

**Parameters**

* `name` **{String}**
* `input` **{String}**

**Example:**

```handlebars  theme={null}
<!-- Set and re-use a default value-->
{{set "name" (default (path "profile.firstName") "valued_customer" )}}
Dear {{name}},

<!-- Make a variable more readable -->
{{set "city" (path "profile.address.primary.city")}}
{{city}}
<!-- Output: Santa Cruz -->

{{set "month" (datetime-format 1554145200000 "%B")}}
{{month}}
<!-- Output: April-->
```

### var

Uses the variable handler to resolve a `JSONPath`, and returns the resolved value, similar to [path](#path). Returns the variable reference as a string `{data.doesNotExist}` if the value was not found.

**Parameters**

* `input` **{String}**

**Example:**

```handlebars  theme={null}
{{path "profile.doesNotExist"}}
<!-- Output: -->

{{var "profile.doesNotExist"}}
<!-- Output: {profile.doesNotExist} -->

{{#if (path "profile.doesNotExist")}}
abc123
{{/if}}
<!-- Output: -->

{{#if (var "profile.doesNotExist")}}
abc123
{{/if}}
<!-- Output: abc123 -->
```

### with

<Note>
  **NOTE**

  This helper is a modified version of the [Handlebars `with` helper](https://github.com/handlebars-lang/handlebars.js/blob/212f9d930b1a39599da2646ac23da64f6552b9d0/lib/handlebars/helpers/with.js).
</Note>

Sets the variable scope when rendering the block content.

**Parameters**

* `input` **{String}**

**Example:**

```handlebars  theme={null}
{{#with person}}
{{firstname}} {{lastname}}
{{/with}}
<!-- Output: Marty Banks -->
```

when run in this context

```json  theme={null}
{
  person: {
    firstname: "Marty",
    lastname: "Banks"
  }
}
```

## String

### capitalize

Returns the capitalized first character of a given string.

**Parameters**

* `input` **{String}**

**Example**

```handlebars  theme={null}
{{capitalize "foo"}}
<!-- Output: Foo -->

<!-- Reference a "data" variable -->
{{capitalize (var "name")}}

<!-- Reference a "profile" variable -->
{{capitalize (var "profile.name")}}
```

### concat

Stringifies all arguments and joins them using the provided separator. Should use `null` string for the separator by default and should return a null string if no arguments.

**Parameters**

* `input` **{String|Number}**

**Example**

```handlebars  theme={null}
{{concat "hello" " " "world"}}
<!-- Output: hello world -->

<!-- Reference a "data" variable -->
{{concat "hello" " " (var "name")}}

<!-- Reference a "profile" variable -->
{{concat "hello" " " (var "profile.name")}}
```

### format

Returns a formatted string given a [format](https://github.com/alexei/sprintf.js) and set of arguments.

**Parameters**

* `input` **{String | Number}**

**Example:**

```handlebars  theme={null}
{{format "%.2f" (var "number")}}
<!-- If number = 1 | Output: 1.00 -->
```

### datetime-format

Returns a formatted date string, can be set to a user IANA Timezone
This helper will throw if an invalid date is provided.

**Parameters**

* `input` **{String|Number}**

**Examples**

```handlebars  theme={null}
{{datetime-format 1554145200000 "%a, %B %d %I:%M %p"}}
<!-- Output: Mon, April 01 7:00 pm-->

{{datetime-format 1554145200000 "%a, %B %d %I:%M %p" "America/Los_Angeles"}}
<!-- Output: Mon, April 01 12:00 pm-->

{{datetime-format "2019-04-01T12:00:00.000Z" "%a, %B %d %I:%M %p"}}
<!-- Output: Mon, April 01 12:00 pm-->

{{datetime-format "2019-04-01T12:00:00.000Z" "%a, %B %d %I:%M %p" "America/Los_Angeles"}}
<!-- Output: Mon, April 01 5:00 am-->
```

<Note>
  **INFO**

  [See full list of format options](https://support.sendwithus.com/jinja/jinja_time/#datetime-format)
  along with an additional option %p to add am, pm
</Note>

### trim-left

Removes whitespace from the beginning of a string, without modifying the original string.

**Parameters**

* `input` **{String}**

**Example:**

```handlebars  theme={null}
{{trim-left "  a string"}}
<!-- Output: a string -->
```

### trim-one-char-right

<Note>
  **INFO**

  This helper is for dealing with the following [escaping issue](https://github.com/handlebars-lang/handlebars.js/issues/1159).
</Note>

Returns the string with the last character removed.

**Parameters**

* `input` **{String}**

**Example:**

```handlebars  theme={null}
{{a-block (params text=(trim-one-char-right "ends with\ "))}}
```

### trim-right

Removes whitespace from the end of a string, without modifying the original string.

**Parameters**

* `input` **{String}**

**Example:**

```handlebars  theme={null}
{{trim-right "a string  "}}
<!-- Output: a string -->
```

### trim

Removes whitespace from the beginning and end of a string, without modifying the original string.

**Parameters**

* `input` **{String}**

**Example:**

```handlebars  theme={null}
{{trim "  a string  "}}
<!-- Output: a string -->
```

### truncate

Truncates the string to the number of characters defined in the helper

**Parameters**

* `input` **{String}**
* `length` **{Number}**
* *(optional)* `suffix` **{String}**

**Example:**

```handlebars  theme={null}
{{ truncate "some very long string" 9 }}
<!-- Output: some very -->

{{ truncate "some very long string" 9 "..." }}
<!-- Output: some very... -->
```

## Math

### abs

Return the magnitude of a number. This helper will throw an error if it encounters a value that is not a number.

**Parameters**

* `input` **{Number}**

**Example**

```handlebars  theme={null}
{{abs -10}}
<!-- Output: 10 -->

<!-- Reference a "data" variable -->
{{abs (var "negative_number")}}

<!-- Reference a "profile" variable -->
{{abs (var "profile.negative_number")}}
```

### add

Returns the the sum of two operands. This helper will throw an error if it encounters an input value that is not a number.

**Parameters**

* `term` **{Number}**
* `term` **{Number}**

**Example**

```handlebars  theme={null}
{{add 5 3}}
<!-- Output: 8 -->

{{add -1 -3}}
<!-- Output: -4 -->

<!-- Reference a "data" variable -->
{{add (var "term_1") (var "term_2")}}

<!-- Reference a "profile" variable -->
{{add (var "profile.term_1") (var "profile.term_2")}}
```

### ceil

Returns the least integer greater than or equal to the decimal number input. This helper will throw an error if it encounters a value that is not a number.

**Parameters**

* `input` **{Number}**

**Example**

```handlebars  theme={null}
{{ceil .95}}
<!-- Output: 1 -->

{{ceil 1.01}}
<!-- Output: 2 -->

{{ceil -1.01}}
<!-- Output: -1 -->

<!-- Reference a "data" variable -->
{{ceil (var "some_number")}}

<!-- Reference a "profile" variable -->
{{ceil (var "profile.some_number")}}
```

### divide

Returns the quotient of its operands where the left operand is the dividend and the right operand is the divisor. This helper will throw an error if it encounters an input value that is not a number or if the divisor is `0`.

**Parameters**

* `dividend` **{Number}**
* `divisor` **{Number}**

**Example**

```handlebars  theme={null}
{{divide 12 2}}
<!-- Output: 6 -->

{{divide 3 2}}
<!-- Output: 1.5 -->

<!-- Reference a "data" variable -->
{{divide (var "dividend") (var "divisor")}}

<!-- Reference a "profile" variable -->
{{divide (var "profile.dividend") (var "profile.divisor")}}
```

### floor

Returns the largest integer less than or equal to a given number. This helper will throw an error if it encounters a value that is not a number.

**Parameters**

* `input` **{Number}**

**Example**

```handlebars  theme={null}
{{floor .95}}
<!-- Output: 0 -->

{{floor 1.01}}
<!-- Output: 1 -->

{{floor -1.01}}
<!-- Output: -2 -->

<!-- Reference a "data" variable -->
{{floor (var "some_number")}}

<!-- Reference a "profile" variable -->
{{floor (var "profile.some_number")}}
```

### inc

Increase value by 1.

**Parameters**

* `input` **{Number}**

**Example:**

```handlebars  theme={null}
{{inc (var "value")}}
<!-- If value = 1 | Output: 2 -->
```

### mod

Returns the remainder left over when one operand is divided by a second operand. It always takes the sign of the dividend.

This helper will throw an error if it encounters an input value that is not a number or if the divisor is `0`.

**Parameters**

* `dividend` **{Number}**
* `divisor` **{Number}**

**Usage:**

**Example**

```handlebars  theme={null}
{{mod 13 5}}
<!-- Output: 3 -->

{{mod -13 5}}
<!-- Output: -3 -->

{{mod 4 2}}
<!-- Output: 0 -->

<!-- Reference a "data" variable -->
{{mod (var "dividend") (var "divisor")}}

<!-- Reference a "profile" variable -->
{{mod (var "profile.dividend") (var "profile.divisor")}}
```

### multiply

Returns the product of two operands. This helper will throw an error if it encounters an input value that is not a number.

**Parameters**

* `multiplier` **{Number}**
* `multiplicand` **{Number}**

**Example**

```handlebars  theme={null}
{{multiply 12 2}}
<!-- Output: 24 -->

{{multiply -12 2}}
<!-- Output: -24 -->

<!-- Reference a "data" variable -->
{{multiply (var "multiplier") (var "multiplicand")}}

<!-- Reference a "profile" variable -->
{{multiply (var "profile.multiplier") (var "profile.multiplicand")}}
```

### round

Returns the value of a number rounded to the nearest integer. This helper will throw an error if it encounters an input value that is not a number.

**Parameters**

* `input` **{Number}**

**Example**

```handlebars  theme={null}
{{round 1.5}}
<!-- Output: 2 -->

{{round 1.4}}
<!-- Output: 1 -->

{{round -1.4}}
<!-- Output: -1 -->

{{round -1.5}}
<!-- Output: -2 -->

<!-- Reference a "data" variable -->
{{round (var "some_variable")}}

<!-- Reference a "profile" variable -->
{{round (var "profile.some_variable")}}
```

### subtract (sub)

Returns the difference of two operands. This helper will throw an error if it encounters an input value that is not a number.

**Parameters**

* `term` **{Number}**
* `term` **{Number}**

**Example**

```handlebars  theme={null}
{{subtract 5 3}}
<!-- Output: 2 -->

{{sub 5 3}}
<!-- Output: 2 -->

{{subtract 3.5 5}}
<!-- Output: -1.5 -->

<!-- Reference a "data" variable -->
{{subtract (var "term_1") (var "term_2")}}

<!-- Reference a "profile" variable -->
{{subtract (var "profile.term_1") (var "profile.term_2")}}
```

## SendWithUs Helpers

SendWithUs helpers are available to help ease migration from your existing Jinja templates to Courier rendered messages.

### swu\_datetimeformat

Returns a formatted date string. This helper will throw if an invalid date is provided.

**Parameters**

* `input` **{String|Number}**

**Examples**

```handlebars  theme={null}
{{swu_datetimeformat 1554145200000 "%a, %B %d"}}
<!-- Output: Mon, April 01 -->

{{swu_datetimeformat "2019-04-01T12:00:00.000Z" "%a, %B %d"}}
<!-- Output: Mon, April 01 -->
```

<Note>
  **INFO**

  [See full list of format options](https://support.sendwithus.com/jinja/jinja_time/#datetime-format)
</Note>

### swu\_iso8601\_to\_time

Returns an ISO-8601 date string as epoch milliseconds. This helper will throw if an invalid date is provided.

**Parameters**

* `input` **{String}**

**Examples**

```handlebars  theme={null}
{{swu_iso8601_to_time "2019-04-01T12:00:00.000Z"}}
<!-- Output: 1554145200000 -->

<!-- Reference a "data" variable -->
{{swu_iso8601_to_time (var "some_date_variable")}}

<!-- Reference a "profile" variable -->
{{swu_iso8601_to_time (var "profile.some_date_variable")}}
```

### swu\_timestamp\_to\_time

Returns an Unix epoch timestamp (seconds) as a millisecond epoch time value. This helper will throw if an invalid unix epoch date is not provided.

**Parameters**

* `input` **{Number}**

**Examples**

```handlebars  theme={null}
{{swu_timestamp_to_time 1554145200}}
<!-- Output: 1554145200000 -->

<!-- Reference a "data" variable -->
{{swu_timestamp_to_time (var "some_timestamp")}}

<!-- Reference a "profile" variable -->
{{swu_timestamp_to_time (var "profile.some_timestamp")}}
```

### translate

Translates a string based on the key, profile locale and .po translations you have uploaded to Courier.

**Parameters**

* `key` **{String}**
* `args` **{String}** (multiple, space separated arguments)
* `domain` **{String}** (only scoped to "default" right now)
* `locale` **{String}** (fetched automatically from profile right now)

**Examples**

```handlebars  theme={null}
{{t "Salutation"}}
<!-- Output: "Welcome" -->

<!-- Pass profile attributes as arguments -->
{{t "Salutation" profile.first_name profile.last_name}}
<!-- Output: "Welcome, John Doe" -->
```
