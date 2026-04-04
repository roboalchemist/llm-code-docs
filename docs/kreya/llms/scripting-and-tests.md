# Source: https://kreya.app/docs/scripting-and-tests.md

# Scripting and tests [Pro / Enterprise](/pricing.md)

The scripting feature allows you to run custom JavaScript inside Kreya. Among other things, it allows you to create tests and view the results of them.

## Kreya operation scripts[​](#kreya-operation-scripts "Direct link to Kreya operation scripts")

Kreya operation scripts are attached directly to a specific Kreya operation and run automatically when the operation is invoked. These can mainly be used to test operation responses.

Find more information about Kreya operation scripts in the [Operation scripts](/docs/scripting-and-tests/operation-scripts.md) documentation.

## Kreya scripts[​](#kreya-scripts "Direct link to Kreya scripts")

Kreya scripts are scripts within Kreya that provide more advanced control, allowing you to programmatically invoke one or more operations using logic like loops and conditional statements for complex workflows or test scenarios.

Find more information about Kreya scripts in the [Scripts](/docs/scripting-and-tests/invoker-scripts.md) documentation.

## Script APIs[​](#script-apis "Direct link to Script APIs")

Kreya offers a set of useful APIs. Checkout the [operation script API reference](/docs/scripting-and-tests/operation-scripts/operation-script-api-reference.md) and [scripts API reference](/docs/scripting-and-tests/invoker-scripts/api-reference.md) documentation as well as the [general script API reference](/docs/scripting-and-tests/general.md). You can also [share code](/docs/scripting-and-tests/general.md#sharing-code) or [import external NPM modules](/docs/scripting-and-tests/general.md#importing-external-modules).

## User variables[​](#user-variables "Direct link to User variables")

Sometimes, you may need to share data between different operations. For example, if you have a process where you create an entity → update the entity → delete the entity, changing the entity ID manually each time becomes annoying. It would be much easier if you could temporarily store the ID of the created entity and reference it from the other two operations. For such use cases, user variables are the way to go.

The feature is available through the [`kreya.variables`](/docs/scripting-and-tests/general/kreya-base-script-api.md#uservariablesscriptapi) object. User variables can also be referenced via [templating](/docs/templating.md#referencing-user-variables-). A common use case is to set a variable in an operation script and then referencing it from somewhere else:

```
// In some script
kreya.variables.set('my_var', 123);

// In some other script
const myVar = kreya.variables.get('my_var');

// Or via templating in an operation
{{ vars.my_var }}
```

## Faker[​](#faker "Direct link to Faker")

Similar to using faker in [templating](/docs/templating.md#generating-fake-data), it can be used with [`kreya.faker`](/docs/scripting-and-tests/general/kreya-base-script-api.md#fakerscriptapi). It uses [Bogus](https://github.com/bchavez/Bogus) behind the scenes. As an example, you could use

```
const name = kreya.faker.name.fullName();
```

to generate a fake, but realistic full name.

## Tests[​](#tests "Direct link to Tests")

Kreya supports defining tests in scripts using the [`kreya.test`](/docs/scripting-and-tests/general/kreya-base-script-api.md#test) function. Test results are displayed in the Tests tab, showing the number of passed and failed tests.

For detailed examples and instructions, see the [tests](/docs/scripting-and-tests/tests.md) documentation.

## Previewing data[​](#previewing-data "Direct link to Previewing data")

Kreya's preview capabilities allow you to visualize data directly within the app. Using the [`kreya.preview` API](/docs/scripting-and-tests/general/kreya-base-script-api.md#previewscriptapi), you can render PDFs, HTML, or custom visualizations to transform raw response data into meaningful insights.

For more details and examples, see the [Previewing Data](/docs/scripting-and-tests/previews.md) documentation.
