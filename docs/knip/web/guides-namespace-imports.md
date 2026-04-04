# Namespace Imports

Source: https://knip.dev/guides/namespace-imports

The intention of exports used through namespace imports may not always be clear
to Knip. Here’s a guide to better understand how Knip handles such exports.

## Example

We start off by having two exports:

```typescript
exportconstversion='v5';exportconstgetRocket=()=>'🚀';
```

The next snippet shows how to import all the exports above on a namespace. All
exports of themy-namespace.jsmodule will be members on theNSobject:

```typescript
import*asNSfrom'./my-namespace.js';importsendfrom'stats';send(NS);
```

The intention of export usage is not always clear. In the example above isversionorgetRocketused? We’re not sure, but weprobablydon’t want them
to be reported as unused. The same goes for the next example:

```typescript
import*asNSfrom'./my-namespace.js';export{ NS };
```

If this all usage of theNSnamespace object, we also don’t know whether
individual exports likeversionorgetRocketwill be used. However, if at
least one reference to a property such asNS.versionis found, then the
individual exports are considered separately again andgetRocketwill be
marked as unused:

```typescript
import{ NS }from'./my-module.js';constversion=NS.version;
```

## The default heuristic

Knip uses the following heuristic to determine which of the individual exports
are used:

- If there’s one or more references to the import namespace object, but without
any property access, all exports on that namespace are considered used.
- Otherwise, exports are considered separately.

Below are a few more examples, and a way to disable this default behavior.

## Examples

Let’s take a look at more examples:

```typescript
exportconststart=1;exportconstend=1;
```

In the following cases all exports ofmy-namespace.tsare considered used:

```typescript
import*asNSfrom'./my-namespace.js';importsendfrom'stats';send(NS);constspread={...NS};constshorthand={ NS };constassignment=NS;constitem=[NS];typeTypeOf=typeofNS;Object.values(NS);for(constfruitinFruits) {//}export{ NS };export{ NSasAliasedNS };export=NS;
```

However, this is no longer the case when one of the properties is accessed:

```typescript
import*asNSfrom'./namespace.js';constbegin=NS.start;send(NS);
```

In this case, theendexport will be reported as unused, even though theNSobject itself is referenced on its own as well.

## IncludensExportsandnsTypes

To disable the heuristic as explained above, and enforce Knip to consider each
export on a namespace individually, include thensExportsissue type:

```typescript
{"include":["nsExports"]}
```

Or use the--include nsExportsargument from the CLI. ThensTypescan be
added as well to do the same for exported types.

ISC License© 2024Lars Kappert

