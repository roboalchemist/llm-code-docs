# Source: https://vueform.com/docs/expressions

Title: Expressions | Vueform | Open-Source Form Framework for Vue

URL Source: https://vueform.com/docs/expressions

Markdown Content:
Learn how to use expressions.

Prerequisites:

*   `@vueform/vueform``1.13.0`

What Are Expressions? [​](https://vueform.com/docs/expressions#what-are-expressions)
------------------------------------------------------------------------------------

Expressions let you display dynamic content based on form values. They're often called formulas or computed values.

You can use expressions:

*   as the value of `TextElement` and `HiddenElement` using the `expression` option
*   in the `content` option of `StaticElement`
*   in `conditions`, `readonly`, and `disabled` options of any element

Using Expressions [​](https://vueform.com/docs/expressions#using-expressions)
-----------------------------------------------------------------------------

The [`TextElement`](https://vueform.com/reference/text-element) and [`HiddenElement`](https://vueform.com/reference/hidden-element) has an [`expression`](https://vueform.com/reference/text-element#option-expression) option that can include expressions between curly brackets `{}`:

template

```
<TextElement
  name="first_name"
  label="First name"
  default="John"
/>
<TextElement
  name="greeting"
  label="Greeting"
  expression="Hi, {first_name}!"
  readonly
/>
```

### Expression Resolution Cycle [​](https://vueform.com/docs/expressions#expression-resolution-cycle)

In the example above, the `greeting` field uses an expression that references `first_name`. Behind the scenes, this sets up a watcher on `first_name`, so whenever `first_name` changes, `greeting` automatically updates its value.

This means that if you're listening to the `@change` event on the `Vueform`, you'll get two events:

*   One when `first_name` changes
*   Another when `greeting` updates as a result

Now, if you add a third field that references `greeting` in its expression, you'd get yet another update because that field only updates after `greeting` changes.

> This cascading effect is **important to keep in mind** when chaining expressions. Each dependent field triggers its own update, which can lead to **multiple change events** for a single user action.

### Escaping Expressions [​](https://vueform.com/docs/expressions#escaping-expressions)

If you want to display curly brackets without triggering an expression, you can escape them with `\`:

template

```
<TextElement
  ...
  expression="Hi, \{first_name\}!"
/>
```

### Nested Elements [​](https://vueform.com/docs/expressions#nested-elements)

To reference nested elements, use their [`dataPath`](https://vueform.com/reference/text-element#property-data-path), not [`path`](https://vueform.com/docs/(/reference/text-element#property-path)):

template

```
<GroupElement name="profile"> <!-- GroupElement DOESN'T nest data -->
  <TextElement
    name="first_name"
    label="First name"
    default="John"
  />
</GroupElement>
<ObjectElement name="address"> <!-- ObjectElement DOES nest data -->
  <TextElement
    name="zip"
    label="ZIP Code"
    default="MI 48105"
  />
</GroupElement>
<TextElement
  name="greeting"
  label="Greeting"
  expression="Hi, {first_name}! You ZIP code is: {address.zip}"
  readonly
/>
```

### Array Values [​](https://vueform.com/docs/expressions#array-values)

You can access array values using dot notation with the index:

template

```
<TagsElement
  name="options"
  label="Options"
  :items="['Option 1', 'Option 2', 'Option 3']"
  :default="['Option 2', 'Option 3']"
/>
<TextElement
  name="first"
  label="First option"
  expression="First option: {options.0}"
  readonly
/>
```

### Object Values [​](https://vueform.com/docs/expressions#object-values)

You can access object properties directly as well:

template

```
<ListElement
  name="users"
  label="Users"
  label-prop="name"
  :object="true"
  :native="false" 
  :items="[
    {id: 123, name: 'John', role: 'admin'},
    {id: 456, name: 'Jane', role: 'editor'}
  ]"
  :default="{id: 123, name: 'John', role: 'admin'}"
/>
<TextElement
  name="role"
  label="Role"
  expression="{user.role}"
  readonly
/>
```

### Sibling Values [​](https://vueform.com/docs/expressions#sibling-values)

To reference sibling values in a list, use `*` instead of a specific index:

template

```
<SelectElement
  name="user"
  label="User"
  :element="{
    type: 'object',
    schema: {
      id: { type: 'text', placeholder: 'ID' },
      name: { type: 'text', placeholder: 'Name' },
      role: { type: 'select', placeholder: 'Role', items: ['admin', 'editor'] },
      key: { type: 'text', placeholder: 'Key', expression: '{user.*.role}-{user.*.id}', disabled: true }
    }
  }"
  :default="[
    {
      id: 123,
      name: 'John',
      role: 'admin',
    }
  ]"
/>
```

### Math Expressions [​](https://vueform.com/docs/expressions#math-expressions)

You can do calculations and use [opreators](https://vueform.com/docs/expressions#operators) inside expressions:

template

```
<TextElement
  name="qty"
  label="Quantity"
  input-type="number"
  default="5"
/>
<TextElement
  name="price"
  label="Price"
  input-type="number"
  default="10"
/>
<TextElement
  name="total"
  label="Total"
  expression="{ qty * price }"
  readonly
/>
```

### Using Functions [​](https://vueform.com/docs/expressions#using-functions)

You can also call built-in [functions](https://vueform.com/docs/expressions#functions):

template

```
<DateElement
  name="dob"
  label="Date of birth"
  default="1989-07-07"
/>
<TextElement
  name="age"
  label="Age"
  expression="{AGE(dob)}"
  readonly
/>
```

You can also add your [custom functions](https://vueform.com/docs/expressions#adding-custom-functions-and-constants).

### Using Logical Expressions [​](https://vueform.com/docs/expressions#using-logical-expressions)

Use ternary expressions for conditional values:

template

```
<DateElement
  name="dob"
  label="Date of birth"
  default="1989-07-07"
/>
<TextElement
  name="allowed"
  label="Allowed"
  expression="{AGE(dob) > 18 ? 'allowed' : 'not_allowed'}"
  readonly
/>
```

Using Expressions in StaticElement [​](https://vueform.com/docs/expressions#using-expressions-in-staticelement)
---------------------------------------------------------------------------------------------------------------

Expressions in `StaticElement`'s `content` option require enabling the [`expressions`](https://vueform.com/reference/static-element#option-expressions) first:

template

```
<TextElement
  name="first_name"
  label="First name"
  default="John"
/>
<StaticElement
  name="greeting_1"
  label="Greeting"
  content="Hi, {first_name}!"
/>
<StaticElement
  name="greeting_2"
  label="Greeting"
  content="Hi, {first_name}!"
  :expressions="true"
/>
```

Using Expressions in Conditions-like Options [​](https://vueform.com/docs/expressions#using-expressions-in-conditions-like-options)
-----------------------------------------------------------------------------------------------------------------------------------

When using expressions in [`conditions`](https://vueform.com/reference/text-element#option-conditions), [`disabled`](https://vueform.com/reference/text-element#option-disabled) or [`readonly`](https://vueform.com/docs/(/reference/text-element#option-readonly)), pass them as plain strings—**without**`{}`:

template

```
<CheckboxElement
  name="create_account"
  text="I want to create an account"
/>
<TextElement
  name="password"
  input-type="password"
  label="Password"
  :conditions="[
    'create_account == true'
  ]"
/>
```

When expressions are used in condition-like options, they should not be wrapped in `{}` and they always must end up having a logical value (`true` or `false`).

> Invalid expressions and expressions that don't return a logical value will resolve as an **unmet** condition.

You can combine expressions with `AND`-type conditions, but not `OR`:

template

```
<DateElement
  name="birthday"
  label="Birthday"
  default="1960-06-12"
/>
<CheckboxElement
  name="create_account"
  text="I want to create an account"
/>

<!-- This WILL work -->
<TextElement
  name="password"
  input-type="password"
  label="Password"
  :conditions="[
    // `AND` type conditions
    'AGE(birthday) > 18',
    ['create_account', true],
  ]"
/>

<!-- This WON'T work -->
<ButtonElement
  name="button"
  button-label="Create account"
  :conditions="[
    // `OR` type conditions
    [
      'AGE(birthday) > 18',
    ],
    [
      ['create_account, true],
    ]
  ]"
/>
```

In general it's advisable to use a single condition if you are using expressions.

Operators [​](https://vueform.com/docs/expressions#operators)
-------------------------------------------------------------

| Operator | Description | Example |
| --- | --- | --- |
| `+` | Adds two numbers together. | `{subtotal + tax}` |
| `-` | Subtracts the right number from the left number. | `{total - discount}` |
| `*` | Multiplies two numbers. | `{price * quantity}` |
| `/` | Divides the left number by the right number. | `{total / count}` |
| `%` | Returns the remainder after division of the left number by the right number. | `{count % 2}` |
| `^` | Raises the left number to the power of the right number. | `{base ^ exponent}` |
| `!` | Factorial of the number. Multiplies all whole numbers from the number down to 1. | `{5!}` |
| `==` | Checks if the value on the left is equal to the value on the right. | `{category == 'main'}` |
| `!=` | Checks if the value on the left is not equal to the value on the right. | `{category != 'main'}` |
| `>=` | Checks if the value on the left is greater than or equal to the value on the right. | `{price >= 100}` |
| `>` | Checks if the value on the left is greater than the value on the right. | `{price > 100}` |
| `<=` | Checks if the value on the left is less than or equal to the value on the right. | `{price <= 100}` |
| `<` | Checks if the value on the left is less than the value on the right. | `{price < 100}` |
| `in` | Checks if the value on the left exists in the array or object on the right. | `{'admin' in roles}` |
| `()` | Groups expressions to control order of evaluation. | `{(price > 100) and (stock > 0)}` |
| `and` | Returns `true` if both expressions are `true`. | `{is_active and is_verified}` |
| `or` | Returns `true` if at least one expression is `true`. | `{is_admin or is_moderator}` |

Functions [​](https://vueform.com/docs/expressions#functions)
-------------------------------------------------------------

### NOT(value) [​](https://vueform.com/docs/expressions#function-not)

*   Arguments: 
    *   `{string} value*` - An expression or reference to an element holding an expression that represents some logical value, i.e. `true` or `false`

*   Returns: `boolean`

Returns the opposite of a logical value — `NOT(true)` returns `false`; `NOT(false)` returns `true`.

### EMPTY(value) [​](https://vueform.com/docs/expressions#function-empty)

*   Arguments: 
    *   `{string} value*` - The value or expression to check — can be a string or array.

*   Returns: `boolean`

Returns `true` if the value is considered empty — e.g. an empty string or empty array, `null`, or `undefined`. 0 is not considered empty.

### NOT_EMPTY(value) [​](https://vueform.com/docs/expressions#function-not-empty)

*   Arguments: 
    *   `{string} value*` - The value or expression to check — can be a string or array.

*   Returns: `boolean`

Returns `true` if the value is not empty — i.e. contains some data (including 0) or has length.

### SUM(value1, [value2, ...]) [​](https://vueform.com/docs/expressions#function-sum)

*   Arguments: 
    *   `{string} value1*` - The first number or list of numbers to add together.
    *   `{string} value2` - Additional numbers or lists to add to the total.

*   Returns: `number`

Returns the sum of a series of numbers and/or lists.

### AVG(value1, [value2, ...]) [​](https://vueform.com/docs/expressions#function-avg)

*   Arguments: 
    *   `{string} value1*` - The first number or list of numbers to average.
    *   `{string} value2` - Additional numbers or lists to include in the average.

*   Returns: `number`

Returns the average (mean) value of a list of numbers.

### MIN(value1, [value2, ...]) [​](https://vueform.com/docs/expressions#function-min)

*   Arguments: 
    *   `{string} value1*` - The first number or list of numbers to check.
    *   `{string} value2` - Additional numbers or lists to check.

*   Returns: `number`

Returns the smallest value from the provided values or lists.

### MAX(value1, [value2, ...]) [​](https://vueform.com/docs/expressions#function-max)

*   Arguments: 
    *   `{string} value1*` - The first number or list of numbers to check.
    *   `{string} value2` - Additional numbers or lists to check.

*   Returns: `number`

Returns the largest value from the provided values or lists.

### ROUND(number, [places]) [​](https://vueform.com/docs/expressions#function-round)

*   Arguments: 
    *   `{string} number*` - The number to round.
    *   `{string} places` - Number of decimal places to round to. Defaults to 0.

*   Returns: `number`

Rounds a number to the nearest whole number or to a specific number of decimal places.

### COUNT(value1, [value2, ...]) [​](https://vueform.com/docs/expressions#function-count)

*   Arguments: 
    *   `{string} value1*` - A single value or an array to count.
    *   `{string} value2` - Additional values or arrays to include in the count.

*   Returns: `number`

Counts the number of values or items of an array.

### AGE(birthday) [​](https://vueform.com/docs/expressions#function-age)

*   Arguments: 
    *   `{string} birthday*` - Date of birth as a string or date value.

*   Returns: `number`

Calculates the age in years from a birth date.

### TODAY() [​](https://vueform.com/docs/expressions#function-today)

*   Returns: `string`

Returns the current date.

### NOW() [​](https://vueform.com/docs/expressions#function-now)

*   Returns: `string`

Returns the current time in ISO8601 standard (2013-02-04T22:44:30.652Z).

### DATE_ADD(date, to_add, interval) [​](https://vueform.com/docs/expressions#function-date-add)

*   Arguments: 
    *   `{string} date*` - The starting date.
    *   `{string} to_add*` - The number of intervals to add (can be negative).
    *   `{string} interval*` - The type of interval: `seconds`, `minutes`, `hours`, `days`, `months`, `years`.

*   Returns: `string`

Adds or subtracts a time interval (e.g. days, months, years) from a date.

### FORMAT_DATE(value, format) [​](https://vueform.com/docs/expressions#function-format-date)

*   Arguments: 
    *   `{string} value*` - A string or number representing a date.
    *   `{string} format*` - The format the date should have. [Formatting tokens](https://vueform.com/docs/i18n#date-formatting-tokens)

*   Returns: `string`

Converts a string into a formatted date.

### DISPLAY_VALUE(value, 'full_path') [​](https://vueform.com/docs/expressions#function-display-value)

*   Arguments: 
    *   `{string} value*` - A reference to an element holding the value.
    *   `{string} 'full_path'*` - The **[full path](https://vueform.com/reference/text-element#property-path)** (not [data path](https://vueform.com/reference/text-element#property-data-path)) of the field between single quotes, eg. `DISPLAY_VALUE(container.select, 'container.select')`. Siblings path (eg. `list.*.select`) cannot be used.

*   Returns: `string`

Returns the display label of a value from a select, checkbox, radio, or similar field.

### AVAILABLE('full_path') [​](https://vueform.com/docs/expressions#function-available)

*   Arguments: 
    *   `{string} 'full_path'*` - The **[full path](https://vueform.com/reference/text-element#property-path)** (not [data path](https://vueform.com/reference/text-element#property-data-path)) of the field between single quotes, eg. `AVAILABLE('container.select')`. Siblings path (eg. `list.*.select`) cannot be used.

*   Returns: `boolean`

Returns `true` if the element is available (all of its conditions are met).

Constants [​](https://vueform.com/docs/expressions#constants)
-------------------------------------------------------------

### PI [​](https://vueform.com/docs/expressions#const-pi)

The value of PI.

### E [​](https://vueform.com/docs/expressions#const-e)

The value known as Euler's number.

Adding Custom Functions and Constants [​](https://vueform.com/docs/expressions#adding-custom-functions-and-constants)
---------------------------------------------------------------------------------------------------------------------

We can add custom functions and contants in `vueform.config.js`:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  expression: {
    functions: {
      CUSTOM_FUNC(arg1, arg2, ...) {
        return 'return value'
      },
      DYNAMIC_FUNC: (form$) => (path) => {
        return form$.el$(path)?.label // returns the label of an element by path
      },
    },
    consts: {
      CUSTOM_CONST: 'const value',
    }
  },
})
```

Debugging [​](https://vueform.com/docs/expressions#debugging)
-------------------------------------------------------------

To debug expressions enable `expressionDebug` in `vueform.config.js`:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  expressionDebug: true // `false` by default
})
```

👋**Hire Vueform team** for form customizations and development

[Learn more](https://vueform.dev/)
