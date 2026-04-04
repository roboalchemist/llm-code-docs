# Source: https://fastify.io/docs/v5.8.x/Guides/Write-Type-Provider.md

# Source: https://fastify.io/docs/v5.7.x/Guides/Write-Type-Provider.md

# Source: https://fastify.io/docs/v5.6.x/Guides/Write-Type-Provider.md

# Source: https://fastify.io/docs/v5.5.x/Guides/Write-Type-Provider.md

# Source: https://fastify.io/docs/v5.4.x/Guides/Write-Type-Provider.md

# Source: https://fastify.io/docs/v5.3.x/Guides/Write-Type-Provider.md

# Source: https://fastify.io/docs/v5.2.x/Guides/Write-Type-Provider.md

# Source: https://fastify.io/docs/v5.1.x/Guides/Write-Type-Provider.md

# Source: https://fastify.io/docs/v5.0.x/Guides/Write-Type-Provider.md

# Source: https://fastify.io/docs/v4.29.x/Guides/Write-Type-Provider.md

# Source: https://fastify.io/docs/latest/Guides/Write-Type-Provider.md

# Write-Type-Provider

## How to write your own type provider[​](#how-to-write-your-own-type-provider "Direct link to How to write your own type provider")

Things to keep in mind when implementing a custom [type provider](/docs/latest/Reference/Type-Providers/.md):

### Type Contravariance[​](#type-contravariance "Direct link to Type Contravariance")

Whereas exhaustive type narrowing checks normally rely on `never` to represent an unreachable state, reduction in type provider interfaces should only be done up to `unknown`.

The reasoning is that certain methods of `FastifyInstance` are contravariant on `TypeProvider`, which can lead to TypeScript surfacing assignability issues unless the custom type provider interface is substitutable with `FastifyTypeProviderDefault`.

For example, `FastifyTypeProviderDefault` will not be assignable to the following:

```
export interface NotSubstitutableTypeProvider extends FastifyTypeProvider {
   // bad, nothing is assignable to `never` (except for itself)
  validator: this['schema'] extends /** custom check here**/ ? /** narrowed type here **/ : never;
  serializer: this['schema'] extends /** custom check here**/ ? /** narrowed type here **/ : never;
}
```

Unless changed to:

```
export interface SubstitutableTypeProvider extends FastifyTypeProvider {
  // good, anything can be assigned to `unknown`
  validator: this['schema'] extends /** custom check here**/ ? /** narrowed type here **/ : unknown;
  serializer: this['schema'] extends /** custom check here**/ ? /** narrowed type here **/ : unknown;
}
```
