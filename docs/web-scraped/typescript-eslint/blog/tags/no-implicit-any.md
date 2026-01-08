# Source: https://typescript-eslint.io/blog/tags/no-implicit-any

# One post tagged with "noImplicitAny"[View All Tags](/blog/tags)## [Avoiding `any`s with Linting and TypeScript
](/blog/avoiding-anys)January 21, 2025 · 9 min read[](https://github.com/JoshuaKGoldberg)[Josh Goldberg](https://github.com/JoshuaKGoldberg)typescript-eslint MaintainerTypeScript&#x27;s `any` type is, by design, the single most unsafe part of its type system.
The `any` type indicates a type that can be anything and can be used in place of any other type.
Using `any` is unsafe because the type disables many of TypeScript&#x27;s type-checking features and hampers TypeScript&#x27;s ability to provide developer assistance.
typescript-eslint includes several lint rules that help prevent unsafe practices around the `any` type.
These rules flag uses of `any` or code patterns that sneakily introduce it.
In this blog post, we&#x27;ll show you those lint rules and several other handy ways to prevent `any`s from sneaking into your code.
**Tags:**- [any](/blog/tags/any)- [no-explicit-any](/blog/tags/no-explicit-any)- [no-unsafe](/blog/tags/no-unsafe)- [noImplicitAny](/blog/tags/no-implicit-any)- [typed linting](/blog/tags/typed-linting)[**Read more**](/blog/avoiding-anys)