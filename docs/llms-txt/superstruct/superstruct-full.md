# Superstruct Documentation

Source: https://docs.superstructjs.org/llms-full.txt

---

# Introduction

Superstruct makes it easy to define interfaces and then validate JavaScript data against them. Its type annotation API was inspired by [TypeScript](https://www.typescriptlang.org/docs/handbook/basic-types.html), [Flow](https://flow.org/en/docs/types/), [Go](https://gobyexample.com/structs), and [GraphQL](http://graphql.org/learn/schema/), giving it a familiar and easy to understand API.

But Superstruct is designed for validating data at runtime, so it throws (or returns) detailed runtime errors for you or your end users. This is especially useful in situations like accepting arbitrary input in a REST or GraphQL API. But it can even be used to validate internal data structures at runtime when needed.

<br>

#### Usage

Superstruct allows you to define the shape of data you want to validate:

```js
import { assert, object, number, string, array } from 'superstruct'

const Article = object({
  id: number(),
  title: string(),
  tags: array(string()),
  author: object({
    id: number(),
  }),
})

const data = {
  id: 34,
  title: 'Hello World',
  tags: ['news', 'features'],
  author: {
    id: 1,
  },
}

assert(data, Article)
// This will throw an error when the data is invalid.
// If you'd rather not throw, you can use `is()` or `validate()`.
```

Superstruct ships with validators for all the common JavaScript data types, and you can define custom ones too:

```js
import { is, define, object, string } from 'superstruct'
import isUuid from 'is-uuid'
import isEmail from 'is-email'

const Email = define('Email', isEmail)
const Uuid = define('Uuid', isUuid.v4)

const User = object({
  id: Uuid,
  email: Email,
  name: string(),
})

const data = {
  id: 'c8d63140-a1f7-45e0-bfc6-df72973fea86',
  email: 'jane@example.com',
  name: 'Jane',
}

if (is(data, User)) {
  // Your data is guaranteed to be valid in this block.
}
```

Superstruct can also handle coercion of your data before validating it, for example to mix in default values:

```ts
import { create, object, number, string, defaulted } from 'superstruct'

const User = object({
  id: defaulted(number(), () => 1),
  name: string(),
})

const data = {
  name: 'Jane',
}

// You can apply the defaults to your data while validating.
const user = create(data, User)
// {
//   id: 1,
//   name: 'Jane',
// }
```

And if you use TypeScript, Superstruct automatically ensures that your data has proper typings whenever you validate it:

```ts
import { is, object, number, string } from 'superstruct'

const User = object({
  id: number(),
  name: string()
})

const data: unknown = { ... }

if (is(data, User)) {
  // TypeScript knows the shape of `data` here, so it is safe to access
  // properties like `data.id` and `data.name`.
}
```

Superstruct supports more complex use cases too like defining arrays or nested objects, composing structs inside each other, returning errors instead of throwing them, and more!


# Getting Started

## Installing Superstruct

To install Superstruct run:

```bash
npm install --save superstruct
```

And then you can import it:

```ts
import { object, string, number } from 'superstruct'

const User = object({
  id: number(),
  name: string(),
})
```

If you'd like, you can use a wildcard import:

```ts
import * as s from 'superstruct'

const User = s.object({
  id: s.number(),
  name: s.string(),
})
```

If you'd rather use a `<script>` tag, you can use the UMD build:

```html
<script src="https://unpkg.com/superstruct/lib/index.cjs"></script>
```

This will expose the `Superstruct` global.

## Defining Structs

Once you've got Superstruct installed, the next step is to create a "struct" for some data you want validate. Each struct corresponds to a specific type of data. In our case, lets start with data describing a user:

```ts
const data = {
  id: 42,
  name: 'Jane Smith',
  email: 'jane@example.com',
}
```

We'll import Superstruct and create an object-shaped struct with it:

```ts
import { object, number, string } from 'superstruct'

const User = object({
  id: number(),
  name: string(),
  email: string(),
})
```

This `User` struct will expect an object with an `id` property that is a number, and `name` and `email` properties that are strings.

Now we can use our `User` struct to validate the data. The easiest way to do this is to use the [`assert`](https://docs.superstructjs.org/api-reference/core#assert) helper, like so:

```ts
import { assert } from 'superstruct'

assert(data, User)
```

This will throw an error if the data is invalid. In this case, the data is valid, so no error is thrown.

But if we pass it invalid data, it will throw an error:

```ts
const data = {
  id: 43,
  name: false,
  email: 'jane@example.com',
}

assert(data, User)
// StructError: 'Expected a value of type "string" for `name` but received `false`.' {
//   type: 'string',
//   value: false,
//   branch: [{ ... }, false],
//   path: ['name'],
//   failures: [...],
// }
```

If you'd rather have the error returned instead of thrown, you can use the [`validate`](https://docs.superstructjs.org/api-reference/core#validate) helper. Or, if you'd just like receive a boolean of whether the data is valid or not, use the [`is`](https://docs.superstructjs.org/api-reference/core#is) helper.


# Validating Data

Superstruct is designed to let you validate any data, ensuring that it matches a specific schema. In this guide we'll show you some of the possibilities.

## Primitive Values

The simplest structs are ones that validate "primitive" values, like strings, numbers or booleans. For example:

```ts
import { assert, string } from 'superstruct'

const Struct = string()

assert('a string', Struct) // passes
assert(42, Struct) // throws!
```

In this case, `assert` will throw an error if the input `data` is not a a string. So on any line after the assertion we're guaranteed to be dealing with a string input.

> 🤖 Note: Superstruct works well with TypeScript guards and assertions, so after calling `assert` or `is` you can access your data in a type-safe way!

But Superstruct has simple structs like these for more than the primitive types. It has support out of the box for many of the common types you might need to validate—dates, functions, regexps, etc.

```ts
import { assert, date } from 'superstruct'

const Struct = date()

assert(new Date(), Struct) // passes
assert('a string', Struct) // throws!
```

Here we're ensuring that `data` is a valid `Date` object.

> 🤖 Check out the [Types reference](https://docs.superstructjs.org/api-reference/types) for all of the possible struct types.

## Composed Values

In addition to simple, "flat" values, you can also compose structs into more complex shapes. The most common example of this is `object` structs:

```ts
import { assert, number, object, string } from 'superstruct'

const User = object({
  id: number(),
  email: string(),
  name: string(),
})

// passes
assert(
  {
    id: 1,
    email: 'jane@example.com',
    name: 'Jane',
  },
  User
)

// throws! (id is invalid)
assert(
  {
    id: '1',
    email: 'jane@example.com',
    name: 'Jane',
  },
  User
)

// also throws! (email is missing)
assert(
  {
    id: 1,
    name: 'Jane',
  },
  User
)
```

This `User` struct will ensure that input data is an object with specific shape of properties, and with property values that match structs.

You could also define a struct which represents a list of values that all match a specific type, using the `array` factory. For example:

```ts
import { array, assert, number } from 'superstruct'

const Struct = array(number())

assert([1, 2, 3], Struct) // passes!
assert(false, Struct) // throws!
assert(['a', 'b', 'c'], Struct) // throws! (invalid element)
```

These are only two examples, but Superstruct supports many complex structs—maps, sets, records, tuples, etc.

You can also compose structs together, for cases where you have relationships between pieces of data. For example, a `User` and a `Team`:

```ts
const User = object({
  id: number(),
  email: string(),
  name: string(),
})

const Team = object({
  id: number(),
  name: string(),
  users: array(User),
})
```

> 🤖 For modelling recursive structures you can use the [`lazy`](https://docs.superstructjs.org/api-reference/types#lazy) utility to prevent circular errors.

## Optional Values

You can also model optional properties. For example, maybe an `email` address isn't strictly required for all your users, you could do:

```ts
import { number, object, optional, string } from 'superstruct'

const User = object({
  id: number(),
  name: string(),
  email: optional(string()),
})
```

Wrapping a struct in `optional` means that the value can also be `undefined` and it will still be considered valid.

So now both of these pieces of data would be valid:

```ts
const jane = {
  id: 43,
  name: 'Jane Smith',
  email: 'jane@example.com',
}

const jack = {
  id: 44,
  name: 'Jack Smith',
}
```

Similarly to `optional`, you can use `nullable` for properties that can also be `null` values. For example:

```ts
const Article = object({
  title: string(),
  body: string(),
  published_at: nullable(date()),
})
```

> 🤖 Check out the [Types reference](https://docs.superstructjs.org/api-reference/types) for all of the possible struct types.

## Custom Values

Next up, you might have been wondering about the `email` property. So far we've just defined it as a string, which means that any old string will pass validation.

But we'd really like to validate that the email is a valid email address. You can do this by defining a custom validation struct:

```ts
import { define } from 'superstruct'
import isEmail from 'is-email'

const email = () => define('email', (value) => isEmail(value))
```

Now we can define structs know about the `email` type:

```ts
const User = object({
  id: number(),
  name: string(),
  email: email(),
  is_admin: optional(boolean()),
})
```

Now if you pass in an email string that is invalid, it will throw:

```ts
const data = {
  id: 43,
  name: 'Jane Smith',
  email: 'jane',
}

assert(data, User) // throws! (invalid email)
```

And there you have it!

> 🤖 Check out the [Types reference](https://docs.superstructjs.org/api-reference/types) for all of the possible struct types.


# Coercing Data

Sometimes while validating input data you'll actually want to "coerce" it to change it in someway to help validation pass. The most common example of this is adding default values to properties, but it can also be used to parse multiple input formats, or cleanup inconsistent data.

To allow for these use cases, Superstruct has a concept called "coercion", which allows you to encode specific logic about how to transform a piece of data before validating it.

## Default Values

Since defaults are such a common case, Superstruct comes with a `defaulted` helper that makes defining default values easy:

```ts
import { create, defaulted, number, object, string } from 'superstruct'

let i = 0

const User = object({
  id: defaulted(number(), () => i++),
  email: string(),
  name: string(),
})

const data = {
  name: 'Jane',
  email: 'jane@example.com',
}

const user = create(data, User)
```

Here the `user` object didn't default an `id` property. That's because any `undefined` values will be replaced with their default values instead.

Notice that we used [`create`](https://docs.superstructjs.org/api-reference/core#create) and not [`assert`](https://docs.superstructjs.org/api-reference/core#assert)! This is an important distinction because we want to receive the return value of the newly coerced data.

The `defaults` helper also works with objects:

```ts
const User = defaulted(
  object({
    id: number(),
    name: string(),
    email: string(),
  }),
  {
    id: () => i++,
  }
)
```

## Custom Coercions

We've already covered default values, but sometimes you'll need to create coercions that aren't just defaulted `undefined` values, but instead transforming the input data from one format to another.

For example, maybe you want to ensure that a number is parsed from a string before passing it into the validator. To do that you can define a custom coercion:

```ts
import { coerce, number, string, create } from 'superstruct'

const MyNumber = coerce(number(), string(), (value) => parseFloat(value))
```

Now instead of using `assert()` or `is()` you can use `create()` to apply your custom coercion logic:

```ts
import { create } from 'superstruct'

const data = '3.14'
const output = create(data, MyNumber)
// 3.14
```

If the input data had been invalid or unable to be coerced an error would have been thrown instead.


# Refining Validation

There are some cases where you want to create a validation that is more fine-grained than a "type". For example, you might want not just a `string`, but a specific format of string. Or not just a `User`, but a user that is also an administrator.

For these situations, you can use "refinements". Refinements allow you to create a new struct that is derived from an existing struct with an extra bit of validation layered on top.

## Built-in Refinements

Superstruct has several [built-in refinements](https://docs.superstructjs.org/api-reference/refinements) for common use cases. For example, a common one is ensuring that a string matches a specific regular expression pattern:

```ts
import { assert, pattern, string } from 'superstruct'

const Section = pattern(string(), /\d+(\.\d+/)?/)

assert('2', Section) // passes
assert('2.1', Section) // passes
assert('string', Section) // throws!
```

Or maybe that a string (or array, number, etc.) has a specific size:

```ts
import { assert, size, string } from 'superstruct'

const Name = size(string(), 1, 100)

assert('Alex', Name) // passes
assert('', Name) // throws!
```

Another common use case is validating nonnegative integers (like indexes in an array) using the built-in `min` helper:

```ts
import { assert, min, integer } from 'superstruct'

const Index = min(integer(), 0)

assert(42, Index) // passes
assert(0, Index) // passes
assert(3.14, Index) // throws!
assert(-1, Index) // throws!
```

These refinements don't change the inferred type of the data, but they do ensure that a slightly stricter validation is enforced at runtime.

## Custom Refinements

You can also write your own custom refinements for more domain-specific use cases. For example, for a specific kind of string:

```ts
import { refine, string } from 'superstruct'

const MyString = refine(string(), 'MyString', (value) => {
  return value.startsWith('The') && value.length > 20
})
```

Now the `MyString` will only validate strings that begin with "The" and are longer than 20 characters.

And whenever an error is thrown from the refinements, the `error.refinement` property will tell you which refinement was the cause.


# Handling Errors

By default Superstruct throws errors that are easy to understand for developers. This means that out of the box you'll get nice errors messages that help you track down why a piece of data is invalid.

For example, consider a simple `User` struct:

```ts
const User = object({
  id: number(),
  name: string(),
  email: email(),
})
```

If you pass in an invalid email, an error will be thrown:

```ts
const data = {
  id: 1,
  name: 'Alex',
  email: false,
}

assert(data, User)
// StructError: At path: email -- Expected a string, but received: false
```

You can also specify your own message for more clarity. In this case the original message will be preserved in [Error.cause](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause).

```ts
assert(data, User, "The user is invalid!");
// StructError: The user is invalid!
```

In addition to the error message, the `error` object will have a bunch of useful properties on it:

```ts
StructError {
  value: false,
  key: 'email',
  type: 'string',
  refinement: undefined,
  path: ['email'],
  branch: [{ id: 1, name: 'Alex', email: false }, false],
  failures: [Function]
}
```

You can use those properties to perform whatever logic is necessary to recover from errors in your application.

> To see all of the information embedded in `StructError` objects, check out the [`StructError` reference](https://docs.superstructjs.org/api-reference/errors).

## Customizing Errors

But there are cases where you want more control over the errors, especially when displaying error messages to end users. For example, if you're building a REST or GraphQL API, you probably want to customize your errors to be specific to your application, and to follow a spec.

To make this possible, you can catch the errors, and use their built-in properties to build up your own custom error codes or messages.

For example, consider a REST API for creating users:

```ts
router.post('/users', ({ request, response }) => {
  const data = request.body

  try {
    assert(data, User)
  } catch (e) {
    const { key, value, type } = e

    if (value === undefined) {
      const error = new Error(`user_${key}_required`)
      error.attribute = key
      throw error
    } else if (type === 'never') {
      const error = new Error(`user_attribute_unknown`)
      error.attribute = key
      throw error
    } else {
      const error = new Error(`user_${key}_invalid`)
      error.attribute = key
      error.value = value
      throw error
    }
  }
})
```

When a developer tries to create a user with invalid properties, the error responses given by the API are standardized. You end up with errors with codes like:

```
user_email_invalid
user_email_required
user_email_unknown

user_name_invalid
user_name_required
...
```

Although this example is simplified, the struct errors expose all of the possible information about why the validation failed, so you can use them to construct extremely detailed errors for your end users.

## Multiple Failures

By default Superstruct throws an error for the very first failure encountered during validation. This greatly simplifies logic for most cases, and results in the best performance.

However, there are situations where you need to check for all of the potential errors in a single piece of data. To do that, you can use the `error.failures` generator, like so:

```ts
try {
  assert(data, Struct)
} catch (error) {
  for (const failure of error.failures()) {
    // ...
  }
}
```

Each `failure` object will give you information about a specific failure of the data.

> 🤖 Note: Superstruct actually doesn't know what the failures are beyond the first one *until* you iterate through them. This happens "on-demand", which can signficantly improve performance in failure cases.


# Using TypeScript

Superstruct is built with TypeScript, and is designed to integrate seamlessly with its guards and assertions. Which means that if you're using TypeScript too you'll get compile-time typings for your data.

> 🤖 Warning: You must enable TypeScript's [`strictNullChecks`](https://www.typescriptlang.org/tsconfig#strictNullChecks) option in your `tsconfig.json` for Superstruct to work properly with "optional" types. Note that `strictNullChecks` is disabled by default. If you enable `strict`, `strictNullChecks` will automatically be enabled.

## Narrowing Types

Whenever you use the `is` or `assert` helpers in Superstruct, TypeScript will infer information about your data and give you type safety. For example:

```ts
import { is, number, object, string } from 'superstruct'

const User = object({
  id: number(),
  email: string(),
  name: string(),
})

if (is(data, User)) {
  // In this block TypeScript knows the shape of `data` is guaranteed to match
  // the `User` struct, so you can access properties like `data.name`.
}
```

Inside that `if` block you can safely access the `User` properties `id`, `name` and `email` because TypeScript knows that the data already passed validation.

The same for goes assertions:

```ts
assert(data, User)
// After this point TypeScript knows that data is valid too!
```

This makes it a lot easier to deal with inputs because you don't need to manually guard and refine their types.

## Describing Types

You can ensure that you're properly describing your existing TypeScript types with Superstruct by using the `Describe` utility. For example:

```ts
type User = {
  id: number
  name: string
}

const User: Describe<User> = object({
  id: string(), // This mistake will fail to pass type checking!
  name: string(),
})
```

In this case, the incorrectly defined `id` property will cause TypeScript's compilation checks to throw an error. This way your compile-time and run-time validations are never out of sync.

## Inferring Types

You can also do the reverse and infer a TypeScript type using an existing Superstruct struct with the `Infer` utility. For example:

```ts
import { Infer, number, object, string } from 'superstruct'

const User = object({
  id: number(),
  email: string(),
  name: string(),
})

type User = Infer<typeof User>
```

The `User` type above is the same as if you'd defined it by hand:

```ts
type User = {
  id: number
  email: string
  name: string
}
```

This saves you from having to duplicate definitions.

> 🤖 Notice that in each of the cases above, the `User` type and the `User` struct have the same name! This is handy for importing them elsewhere in the codebase at the same time.


# Core

### `assert`

`assert<T>(value: unknown, struct: Struct<T>, message?: string) => asserts value is T`

```ts
assert(value, User, 'The user is invalid!')
```

Assert that `value` is valid according to a `struct`. If the value is invalid a [`StructError`](https://docs.superstructjs.org/errors#structerror) will be thrown (the optional `message` parameter allows you to override error's message).

> 🤖 When using TypeScript `assert` acts as an [assertion function](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-7.html#assertion-functions), so you can ensure that after calling it the type of the `value` matches the shape of the struct.

### `create`

`create<T>(value: unknown, struct: Struct<T>, message?: string) => T`

```ts
const user = create(value, User, 'Unable to create a user!')
```

Create a `value` using the coercion logic that is built-in to the struct, returning the newly coerced value. If the value is invalid a [`StructError`](https://docs.superstructjs.org/errors#structerror) will be thrown (the optional `message` parameter allows you to override error's message).

> 🤖 If you want coercion logic like defaulted values, you **must** call this helper before running validation.

### `is`

`is<T>(value: unknown, struct: Struct<T>) => value is T`

```ts
if (is(value, User)) {
  // ...
}
```

Test that `value` is valid, returning a boolean representing whether it is valid or not.

> 🤖 When using TypeScript `is` acts as a type guard, so you can use it in an `if` statement to ensure that inside the statement the `value` matches the shape of the struct.

### `mask`

`mask<T>(value: unknown, struct: Struct<T>, message?: string) => T`

```ts
const user = mask(value, User, 'The value is incompatible with type User!')
```

Mask a `value`, returning a new value containing only properties defined by a `struct`. Conceptually this is similar to `create`, except that extra properties are omitted from the newly created value instead of throwing a [`StructError`](https://docs.superstructjs.org/errors#structerror). If an error is thrown anyway, the optional `message` parameter allows you to override its message.

Note that when `mask` is used with `type` — given that `type` signals to the core that an object might have arbitrary additional properties — unknown properties will be retained in the returned value.

> 🤖 Just like `create`, `mask` includes coercion logic and works recursively.

### `validate`

`validate<T>(value: unknown, struct: Struct<T>, options: Object) => [StructError, T]`

```ts
const [err, user] = validate(value, User)
```

Validate `value`, returning a result tuple. If the value is invalid the first element will be a [`StructError`](https://docs.superstructjs.org/errors#structerror). Otherwise, the first element will be `undefined` and the second element will be a value that is guaranteed to match the struct.

You can pass `{ coerce: true }` as the third argument to enable coercion of the input value. As well as pass `{ message: 'Your custom error message' }` to override the message of the [`StructError`](https://docs.superstructjs.org/errors#structerror).


# Types

Superstruct exposes factory functions for a variety of common JavaScript (and TypeScript) types. You can also define your own custom validation functions using the `struct` factory.

### `any`

```ts
any()
```

```ts
'valid'
42
true
undefined
null
{
  also: 'valid'
}
```

`any` structs accept any value as valid.

> 🤖 Note that if you're using TypeScript, the `any` struct will loosen the type to `any`, and you might want to use [`unknown`](#unknown) instead.

### `array`

```ts
array(number())
array(object({ id: number() }))
```

```
[1, 2, 3]
[{ id: 1 }]
```

`array` structs accept a list of values of a specific type.

### `bigint`

```ts
bigint()
```

```ts
0n
3n
4000030n
BigInt(10n^1000n)
```

`bigint` structs validate that a value is a bigint.

### `boolean`

```ts
boolean()
```

```ts
true
false
```

`boolean` structs accept the boolean values `true` and `false`.

### `date`

```ts
date()
```

```ts
new Date()
```

`date` structs accept JavaScript `Date` instances.

> 🤖 To avoid unexpected runtime errors, `date` structs do **not** accept invalid `Date` objects, even though they are technically an instance of a `Date`. This meshes with the 99% use case where invalid dates create inconsistencies.

### `enums`

```ts
enums(['Jane', 'John', 'Jack', 'Jill'])
```

```ts
'Jane'
'John'
```

`enums` structs validate that a value is one of a specific set of literals values.

### `func`

```ts
func()
```

```ts
function () {}
```

`func` structs validate that a value is a function.

### `instance`

```ts
instance(MyClass)
```

```ts
new MyClass()
```

`instance` structs validate that a value is an instance of a particular class, using JavaScript's built-in `instanceof` operator.

### `integer`

```ts
integer()
```

```
-7
0
42
```

`integer` structs validate that a value is an integer.

### `intersection`

```ts
intersection([string(), Email])
```

```ts
'jane@example.com'
```

`intersection` structs validate that a value matches **all** of many structs. It takes existing struct objects as arguments.

### `literal`

```ts
literal(42)
```

```ts
42
```

`literal` structs enforce that a value matches an exact value using the `===` operator.

### `map`

```ts
map(string(), number())
```

```ts
new Map([
  ['a', 1],
  ['b', 2],
])
```

`map` structs validate that a value is a `Map` object with specific types for its keys and values.

> 🤖 When defining a key/value schemas with `map` it will traverse all the properties to ensure they are valid! If you don't care about validating the properties of the map, you can write `map()` instead.

### `never`

```ts
never()
```

```ts
```

`never` structs will fail validation for **every** value.

### `number`

```ts
number()
```

```ts
0
3.14
42
Infinity
```

`number` structs validate that a value is a number.

### `nullable`

```ts
nullable(string())
```

```ts
'a string of text'
null
```

`nullable` structs validate that a value matches a specific struct, or that it is `null`.

### `object`

```ts
object({
  id: number(),
  name: string(),
})
```

```ts
{
  id: 1,
  name: 'Jane Smith',
}
```

`object` structs validate that a value is an object and that each of its properties match a specific type as well.

> 🤖 Note that `object` structs throw errors if they encounter extra properties on an object, unless [`mask`](https://docs.superstructjs.org/core#mask) is used! If you want to be less strict and ignore any extra properties, use [`type`](#type) instead. For other more complex object use cases, check out the [coercions](https://docs.superstructjs.org/api-reference/coercions) and [utilities](https://docs.superstructjs.org/api-reference/utilities) too.

### `optional`

```ts
optional(string())
```

```ts
'a string of text'
undefined
```

`optional` structs validate that a value matches a specific struct, or that it is `undefined`.

> 🤖 Warning: If you are using TypeScript, you must enable TypeScript's [`strictNullChecks`](https://www.typescriptlang.org/tsconfig#strictNullChecks) option in your `tsconfig.json` for Superstruct to work properly with "optional" types. Note that `strictNullChecks` is disabled by default. If you enable `strict`, `strictNullChecks` will automatically be enabled.

### `record`

```ts
record(string(), number())
```

```ts
{
  a: 1,
  b: 2,
}
```

`record` structs validate an object with specific types for its keys and values. But, unlike `object` structs, they do not enforce a specific set of keys.

### `regexp`

```ts
regexp()
```

```ts
;/\d+/
new RegExp()
```

`regexp` structs validate that a value is a `RegExp` object.

> 🤖 This does not test the value against the regular expression! For that you want the [`pattern`](https://docs.superstructjs.org/refinements#pattern) refinement.

### `set`

```ts
set(string())
```

```ts
new Set(['a', 'b', 'c'])
```

`set` structs validate that a value is a `Set` instance with elements of a specific type.

> 🤖 When defining a child schema with `set` it will traverse all the children to ensure they are valid! If you don't care about validating the elements of the set, you can write `set()` instead.

### `string`

```ts
string()
```

```ts
'a string of text'
```

`string` structs validate that a value is a string.

### `tuple`

```ts
tuple([string(), number(), boolean()])
```

```
['a', 1, true]
```

`tuple` structs validate that a value is an array of a specific length with values each of a specific type.

### `type`

```ts
type({
  name: string(),
  walk: func(),
})
```

```ts
{
  name: 'Jill',
  age: 37,
  race: 'human',
  walk: () => {},
}
```

`type` structs validate that a value has a set of properties on it, but it does not assert anything about unspecified properties. This allows you to assert that a particular set of functionality exists without a strict equality check for properties.

When [`mask()`](https://docs.superstructjs.org/core#mask) is used with a value of `type`, its unknown properties are not removed. I.e. consider `type` as a signal to the core that the object may have arbitrary properties in addition to the known ones, in both masked and non-masked validation.

> 🤖 If you want to throw errors when encountering unknown properties, use [`object`](#object) instead.

### `union`

```ts
union([string(), number()])
```

```ts
'a string'
42
```

`union` structs validate that a value matches at least one of many types.

### `unknown`

```ts
unknown()
```

```ts
'valid'
42
true
undefined
null
{
  also: 'valid'
}
```

`unknown` structs accept unknown value as valid without loosening its type to `any`.

### Custom Types

You can also define your own custom structs that are specific to your application's requirements, like so:

```ts
import { define } from 'superstruct'
import isEmail from 'is-email'
import isUuid from 'is-uuid'

const Email = define('Email', isEmail)
const Uuid = define('Uuid', (value) => isUuid.v4(value))

const User = object({
  id: Uuid,
  name: string(),
  email: Email,
  age: number(),
})
```

Custom types take validator functions that return either `true/false` or an array of `StructFailure` objects, in case you want to build more helpful error messages.

> 🤖 If you are using Typescript the value will be of type `unknown` by default. You can pass a more specific type for Typescript:
>
> ```ts
> const Email = define<string>('Email', isEmail)
> ```


# Refinements

Superstruct allows you to constrain existing structs with further validation. This doesn't change the type of the struct, but simply introduces extra validation logic. This can be useful for example when ensuring that a string matches a specific `RegExp`.

### `empty`

```ts
empty(string())
empty(array())
```

```ts
''
[]
```

`empty` enforces that a `string`, `array`, `map`, or `set` is empty.

> 🤖 Technically this is the same as using [`size`](#size) of zero, but "empty" feels slightly nicer and will give a slightly easier to read error.

### `max`

```ts
max(number(), 0)
```

```
-1
```

`max` enforces that a `number` struct is less than a threshold.

> 🤖 If you need an exclusive maxmimum you can pass `{ exclusive: true }` as the third argument, like `max(number(), 0, { exclusive: true })` for negative numbers.

### `min`

```ts
min(number(), 9000)
```

```ts
9001
```

`min` enforces that a `number` struct is greater than a threshold.

> 🤖 If you need an exclusive minimum you can pass `{ exclusive: true }` as the third argument, like `min(number(), 0, { exclusive: true })` for positive numbers.

### `nonempty`

```ts
nonempty(string())
nonempty(array())
```

`nonempty` enforces that a string, array, map, or set is not empty. This does the opposite of `empty`.

### `pattern`

```ts
pattern(string(), /\d+/)
```

```ts
'123'
```

`pattern` enforces that a `string` struct also matches a supplied `RegExp`.

### `size`

```ts
size(string(), 1, 100)
size(array(number()), 0)
size(number(), 93, Infinity)
```

```
'a string of text'
[]
Infinity
```

`size` enforces that a `number`, `string`, `array`, `map`, or `set` struct also is within a certain `min` and `max` size (or length).

> 🤖 The `max` argument is optional and defaults to whatever you pass for `min`, which makes specifying exact sizes easy (just omit the max).

### Custom Refinements

You can also define your own custom refinments that are specific to your application's requirements, like so:

```ts
import { number, refine } from 'superstruct'

const Positive = refine(number(), 'positive', (value) => value >= 0)
```

This allows you to define more fine-grained runtime validation, while still preserving the `number` type at compile time.

> 🤖 The `value` provided to the refiner function is guaranteed to be the provided struct's type. This means you can layer additional validation on top of even complex structs with minimal hassle.

If you'd like to customize the error message that will be returned/thrown by your struct when a value doesn't pass your refinement's validation, you can return a string instead of a boolean inside the refiner.

```ts
const DateRange = refine(
  object({
    startDate: number(),
    endDate: number(),
  }),
  'DateRange',
  (value) => {
    if (value.startDate < value.endDate) {
      return true
    }

    // Returning a string indicates that validation failed and the provided
    // string should be used as a custom error message.
    return (
      `Expected 'startDate' to be less than 'endDate' on type 'DateRange', ` +
      `but received ${JSON.stringify(value)}`
    )
  }
)
```


# Coercions

Superstruct allows structs to be augmented with coercion logic, letting you to transform input data before validating it. This is most commonly used to apply default values to an input, but it can be used for more complex cases like pre-trimming strings, or pre-parsing inputs.

### `defaulted`

```ts
defaulted(string(), 'Untitled')

object({
  id: defaulted(number(), () => i++),
  name: string(),
  role: defaulted(enums(['admin', 'member', 'guest']), 'guest'),
})
```

`defaulted` augments a struct to add coercion logic for default values, which are applied when the input is `undefined`.

> 🤖 If you add `defaulted` to an `object` struct with a dictionary of values, those values will be mixed in one-by-one, so the input doesn't need to be `undefined`, but certain properties can be `undefined`.

### `trimmed`

```ts
trimmed(string())
```

`trimmed` arguments a struct to ensure that any string input values are trimmed.

### Custom Coercions

You can also define your own custom coercions that are specific to your application's requirements, like so:

```ts
import { coerce, number, string, create } from 'superstruct'

const MyNumber = coerce(number(), string(), (value) => parseFloat(value))

const a = create(42, MyNumber) // 42
const b = create('42', MyNumber) // 42
const c = create(false, MyNumber) // error thrown!
```

The second argument to `coerce` is a struct narrowing the types of input values you want to try coercion. In the example above, the coercion function will only ever be called when the input is a string—booleans would ignore coercion and fail normally.

> 🤖 If you want to run coercion for any type of input, use the `unknown()` struct to run it in all cases.


# Utilities

Superstruct also ships with a handful of utility type factories, which allow you to easily manipulate and transforms existing structs.

### `assign`

```ts
assign(object({ id: string() }), object({ name: string() }))
```

```ts
{
  id: 1,
  name: 'Jane',
}
```

`assign` creates a new struct by mixing the properties of existing object structs, similar to JavaScript's native [`Object.assign`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign). It can accept `object` and `type` structs, returning a struct matching whichever is passed in as the first parameter (ie, which struct is being "assigned" into).

### `deprecated`

```ts
object({
  id: number(),
  full_name: string(),
  name: deprecated(string(), (value, ctx) => {
    console.warn(`${ctx.path} is deprecated, but value was '${value}'. Please use 'full_name' instead.`)
  }),
})
```

```ts
{ id: 1, name: 'Jane' }
```

`deprecated` structs validate that a value matches a specific struct, or that it is `undefined`. But in addition, when the value is not `undefined`, it will call the `log` function you pass in so you can warn users that they're using a deprecated API.

### `dynamic`

```ts
const User = object({ ... })
const Bot = object({ ... })

dynamic((value) => {
  return value.kind === 'user' ? User : Bot
})
```

`dynamic` allows you to create a struct with validation logic that can change at runtime. The callback will be called with `(value, context)` and must return the struct to continue validation with.

### `lazy`

```ts
const Node = object({
  id: number(),
  children: lazy(() => array(Node)),
})
```

`lazy` allows you to create a self-referential struct, useful for defining recursive data structures.

> 🤖 Note that TypeScript can't automatically infer the type from this kind of recursive structure, so you'll need to pass in the type manually.

### `omit`

```ts
omit(
  object({
    id: number(),
    name: string(),
  }),
  ['name']
)
```

`omit` allows you to create a new struct based on an existing `object` or `type` struct, but excluding specific properties.

### `partial`

```ts
partial(
  object({
    id: number(),
    name: string(),
  })
)
```

```ts
{ id: 1, name: 'Jane' }
{ id: 1 }
{ name: 'Jane' }
```

`partial` allows you to create a new struct based on an existing `object` or `type` struct, but with all of its properties being optional.

### `pick`

```ts
pick(
  object({
    id: number(),
    name: string(),
  }),
  ['id']
)
```

`pick` allows you to create a new struct based on an existing `object` or `type` struct, but only including specific properties.


# Errors

Superstruct throws detailed errors when data is invalid, so that you can build extremely precise errors of your own to give your end users the best possible experience.

### `StructError`

`Error`

```ts
import { StructError } from 'superstruct'

if (error instanceof StructError) {
  ...
}
```

The error class that Superstruct uses for its validation errors. This is exposed primarily as a convenience for checking whether thrown errors are an `instanceof` the `StructError` class.

### Error Properties

Each error thrown includes the following properties:

| **Property**        | **Type**                        | **Example**                                                                    | **Description**                                                                                                                                                                                                        |
| ------------------- | ------------------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `branch`            | `Array<any>`                    | `[{...}, false]`                                                               | An array of the values being validated at every layer. The first element in the array is the root value, and the last element is the current value that failed. This allows you to inspect the entire validation tree. |
| `failures`          | `() => Array<Failure>`          | `[{...}]`                                                                      | All the validation failures that were encountered. The error object always represents the first failure, but you can write more complex logic involving other failures if you need to.                                 |
| `key`               | `string \| number \| undefined` | The key of the value when validating complex values like objects, arrays, etc. |                                                                                                                                                                                                                        |
| `path`              | `Array<string \| number>`       | `['address', 'street']`                                                        | The path to the invalid value relative to the root value.                                                                                                                                                              |
| `type`              | `string`                        | `'date'` / `'object'` / …                                                      | The expected type of the invalid value. This is a string of the struct that failed validation (eg. `string`, `date`, `object`).                                                                                        |
| `value`             | `any`                           | `false`                                                                        | The invalid value.                                                                                                                                                                                                     |
| `cause`             | `string \| undefined`           | `Expected a string, but received: 42`                                          | If a custom message is specified, the original one will be preserved in this property (complies with [standard](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause)).        |
| ### Multiple Errors |                                 |                                                                                |                                                                                                                                                                                                                        |

The error thrown by Superstruct is always the first validation failure that was encountered, because this makes for convenient and simple logic in the majority of cases. However, the `failures` property is available with a list of all of the validation failures that occurred in case you want to add support for multiple error handling.


# TypeScript

Superstruct is designed with TypeScript in mind, so that you don't need to duplicate type definitions.

## Utilities

### `Describe`

The `Describe` utility returns a type representing a struct for a given valid value type. This allows you to ensure you're writing your struct definitions properly, for example:

```ts
type User = {
  id: number
  name: string
}

const User: Describe<User> = object({
  id: string(), // This mistake will fail to pass type checking!
  name: string(),
})
```

> 🤖 There are limitations to what `Describe` can do, specifically it will always assume object types are as strict as possible. So describing the `type()` struct is not possible, and simple unions of strings will be required to use `enums()`.

### `Infer`

The `Infer` utility type extracts the type of a valid value from a struct definition. This allows you to avoid having to duplicate effort when writing typings, for example:

```ts
const User = object({
  id: number(),
  name: string(),
})

type User = Infer<typeof User>
// type User = {
//   id: number
//   name: string
// }
```

> 🤖 If you are not using TypeScript's [`strictNullChecks`](https://www.typescriptlang.org/tsconfig#strictNullChecks) option, Superstruct will be unable to infer your "optional" types correctly and will mark all types as optional.


# FAQ

Some common questions you might have when first learning Superstruct.

### How can I allow unknown keys with `object` structs?

The [`object`](https://docs.superstructjs.org/api-reference/types#object) struct validates that a value matches a known object shape. Just like it's TypeScript counterpart, it does not allow unknown keys—this is very useful in catching bugs in the majority of cases.

However, there are cases where you'd like to validate a set of properties but ignore any unknown ones. For that you can use the [`type`](https://docs.superstructjs.org/api-reference/types#type) struct which is more generic, and acts similar to TypeScript's structural typing in that it does not care about any extra properties.

### Why not have a built-in `json` struct?

The problem with a built-in `json` struct is that it needs to recursively iterate through deep objects to guarantee they're valid JSON. What's wrong with that? Nothing, except that it would be a footgun.

The cases where you receive a truly unknown object, and you need to validate nothing about its content other than that it is pure JSON are very rare. In those cases, it's not hard to write a `json` utility yourself.

Instead, people would mistakenly use `json` in places where they really meant, "some object I don't care about", without realzing the performance penalty—use [`unknown`](https://docs.superstructjs.org/api-reference/types#unknown) or [`object`](https://docs.superstructjs.org/api-reference/types#object) instead.


# Links

A few resources that are helpful for building with Superstruct.

## Libraries

* [`bumpover`](https://github.com/doodlewind/bumpover) helps you transform data asynchronously with simple rules, whose validation API is built with Superstruct.
* [micro-superstruct](https://github.com/brandon93s/micro-superstruct) allows you to easily validate your [Micro](https://github.com/zeit/micro) API request body and query string parameters using Superstruct.


