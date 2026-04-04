# Source: https://kreya.app/docs/templating.md

# Templating

With the templating feature, you can insert [environment](/docs/environments.md) values almost everywhere inside Kreya.

List of features that support templating:

* [Authentication](/docs/authentication.md)
* [Default settings](/docs/default-settings.md)
* Certificates
* gRPC metadata
* gRPC requests
* gRPC endpoint
* gRPC server reflection endpoint
* REST headers
* REST query parameters
* REST requests
* REST endpoint
* REST importers
* GraphQL headers
* GraphQL query parameters
* GraphQL requests
* GraphQL variables
* GraphQL endpoint
* GraphQL schema importers
* WebSocket headers
* WebSocket requests
* WebSocket endpoint

## Templating language[​](#templating-language "Direct link to Templating language")

Kreya uses [Scriban](https://github.com/scriban/scriban) as its templating language. Usually, only variables are used, such as `{{ env.endpoint }}`. However, Scriban supports more complex features.

Take a look at the [Scriban language guide](https://github.com/scriban/scriban/blob/master/doc/language.md) and [built in functions](https://github.com/scriban/scriban/blob/master/doc/builtins.md).

## Kreya environment data[​](#kreya-environment-data "Direct link to Kreya environment data")

The active kreya environment can be accessed by the `env` Scriban object: `{{ env.myProperty }}`.

info

Starting with Kreya 1.7, directly referencing environment variables (ex. `{{ endpoint }}`) has been deprecated. Please use the `env` object to reference environment variables, for example `{{ env.endpoint }}`.

## Generating fake data[​](#generating-fake-data "Direct link to Generating fake data")

In addition to the default Scriban features, Kreya also implements [Bogus](https://github.com/bchavez/Bogus) to allow fake data generation. For example, using

```
I am {{ faker.name.full_name }}
```

will result in a random name:

```
I am Jazlyn Gorczany
```

## Referencing user variables [Pro / Enterprise](/pricing.md)[​](#referencing-user-variables- "Direct link to referencing-user-variables-")

[User variables](/docs/scripting-and-tests.md#user-variables) can be set via scripting. If you set a user variable via scripting

```
kreya.variables.set('my_variable', 12345);
```

it can be referenced via templating:

```
My variable contains {{ vars.my_variable }}
```

## Referencing authentication configurations[​](#referencing-authentication-configurations "Direct link to Referencing authentication configurations")

Should you need to send authentication tokens via custom headers, in the request body or elsewhere, simply reference your existing authentication configurations. For example, if you have a basic authentication configuration called "My Auth":

```
The value of {{ auth.configs.my_auth.name }} is {{ auth.configs.my_auth.value }}
```

If you also need the "authentication prefix" (Basic, Bearer, ...), use `prefixed_value` instead of `value`.
