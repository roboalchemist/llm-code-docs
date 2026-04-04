# Source: https://typescript-eslint.io/blog

## [Revamping the `ban-types` rule
](/blog/revamping-the-ban-types-rule)January 5, 2026 · 6 min read[](https://github.com/JoshuaKGoldberg)[Josh Goldberg](https://github.com/JoshuaKGoldberg)typescript-eslint MaintainerFor many years, `@typescript-eslint/ban-types` was one of the more prominent rules in typescript-eslint.
It served three purposes:
- It banned usage of the unsafe "empty object" `{}` type
- It banned uses of dangerous or misleading built-in types: `Function`, `Number`, and so on
- It also allowed users to provide additional types to ban
Those are all great areas for linting!
However, `@typescript-eslint/ban-types` suffered from several key design issues:
- By targeting all three areas of banning, it was hard to configure to only what a project needs
- It was overly strict on banning `{}`, to the point of confusing and inconveniencing users
- It was limited in what auto-fixes and edge cases it could handle for its default banned types
This post will explain how `@typescript-eslint/ban-types` came to be, its benefits and drawbacks, and the new rules that better handle its targeted functionality.
**Tags:**- [ban-types](/blog/tags/ban-types)- [interfaces](/blog/tags/interfaces)- [no-empty-object-type](/blog/tags/no-empty-object-type)- [no-restricted-types](/blog/tags/no-restricted-types)- [no-unsafe-function-type](/blog/tags/no-unsafe-function-type)- [no-wrapper-object-types](/blog/tags/no-wrapper-object-types)- [objects](/blog/tags/objects)[**Read more**](/blog/revamping-the-ban-types-rule)## [Typed Linting with Project Service
](/blog/project-service)May 29, 2025 · 8 min read[](https://github.com/JoshuaKGoldberg)[Josh Goldberg](https://github.com/JoshuaKGoldberg)typescript-eslint Maintainer["Typed linting"](/blog/typed-linting), or enabling ESLint rules to understand TypeScript types, is one of the best parts of typescript-eslint.
It enables a slew of [more powerful lint rules](/rules/?=recommended-typeInformation) that check for nuanced bugs, best practice violations, and other code issues that can only be detected using type information.
Typed linting hasn&#x27;t always been straightforward to configure or performant at runtime.
We&#x27;ve seen users have to manage separate `tsconfig.eslint.json` files to enable typed linting — sometimes with different compiler options than the rest of the project.
Not ideal.
In typescript-eslint 8.0, we stabilized a **`parserOptions.projectService`** option that uses more powerful, streamlined TypeScript APIs than before.
The "Project Service" brings several benefits:
- ✍️ **Configuration**: simpler ESLint configs for typed linting with no ESLint-specific TSConfig files
- 🧠 **Predictability**: uses the same type information services as editors, including more reliability
- 🚀 **Scalability**: supporting TypeScript project references for larger repositories (i.e. monorepos)
This blog post will cover how `parserOptions.projectService` simplifies configurations and aligns linting type information to what editors such as VS Code run with.
tipSee [Getting Started](/getting-started) to learn how to lint JavaScript and TypeScript code with typescript-eslint, then [Linting with Type Information](/getting-started/typed-linting) to onboard to typed linting.
**Tags:**- [parser](/blog/tags/parser)- [parser options](/blog/tags/parser-options)- [project](/blog/tags/project)- [project service](/blog/tags/project-service)- [tsconfig](/blog/tags/tsconfig)[**Read more**](/blog/project-service)## [Avoiding `any`s with Linting and TypeScript
](/blog/avoiding-anys)January 21, 2025 · 9 min read[](https://github.com/JoshuaKGoldberg)[Josh Goldberg](https://github.com/JoshuaKGoldberg)typescript-eslint MaintainerTypeScript&#x27;s `any` type is, by design, the single most unsafe part of its type system.
The `any` type indicates a type that can be anything and can be used in place of any other type.
Using `any` is unsafe because the type disables many of TypeScript&#x27;s type-checking features and hampers TypeScript&#x27;s ability to provide developer assistance.
typescript-eslint includes several lint rules that help prevent unsafe practices around the `any` type.
These rules flag uses of `any` or code patterns that sneakily introduce it.
In this blog post, we&#x27;ll show you those lint rules and several other handy ways to prevent `any`s from sneaking into your code.
**Tags:**- [any](/blog/tags/any)- [no-explicit-any](/blog/tags/no-explicit-any)- [no-unsafe](/blog/tags/no-unsafe)- [noImplicitAny](/blog/tags/no-implicit-any)- [typed linting](/blog/tags/typed-linting)[**Read more**](/blog/avoiding-anys)## [Typed Linting: The Most Powerful TypeScript Linting Ever
](/blog/typed-linting)September 30, 2024 · 9 min read[](https://github.com/JoshuaKGoldberg)[Josh Goldberg](https://github.com/JoshuaKGoldberg)typescript-eslint Maintainer[Linting with type information](https://typescript-eslint.io/getting-started/typed-linting), also called "typed linting" or "type-aware linting", is the act of writing lint rules that use type information to understand your code.
Typed linting rules as provided by typescript-eslint are the most powerful JavaScript/TypeScript linting in common use today.
In this blog post, we&#x27;ll give a high-level overview of how linting with type information works, why it&#x27;s so much more powerful than traditional linting, and some of the useful rules you can enable that use it.
**Tags:**- [types](/blog/tags/types)- [type information](/blog/tags/type-information)- [typed linting](/blog/tags/typed-linting)[**Read more**](/blog/typed-linting)## [Announcing typescript-eslint v8
](/blog/announcing-typescript-eslint-v8)July 31, 2024 · 17 min read[](https://github.com/JoshuaKGoldberg)[Josh Goldberg](https://github.com/JoshuaKGoldberg)typescript-eslint Maintainer[typescript-eslint](https://typescript-eslint.io) is the tooling that enables standard JavaScript tools such as [ESLint](https://eslint.org) and [Prettier](https://prettier.io) to support TypeScript code.
We&#x27;ve been working on a set of breaking changes and general features that we&#x27;re excited to get in front of users.
And now, we&#x27;re excited to say that typescript-eslint v8 is released as stable! 🎉
We&#x27;d previously blogged about v8 in [Announcing typescript-eslint v8 Beta](/blog/announcing-typescript-eslint-v8-beta).
This blog post contains much of the same information as that one, and includes the list of steps you&#x27;ll need to take to upgrade.
**Tags:**- [breaking changes](/blog/tags/breaking-changes)- [typescript-eslint](/blog/tags/typescript-eslint)- [v7](/blog/tags/v-7)- [v8](/blog/tags/v-8)[**Read more**](/blog/announcing-typescript-eslint-v8)## [Announcing typescript-eslint v8 Beta
](/blog/announcing-typescript-eslint-v8-beta)May 27, 2024 · 15 min read[](https://github.com/JoshuaKGoldberg)[Josh Goldberg](https://github.com/JoshuaKGoldberg)typescript-eslint MaintainerNewer Information AvailableThis blog post is now out of date, as we&#x27;ve released typescript-eslint v8! 🚀
Please see [Announcing typescript-eslint v8](/blog/announcing-typescript-eslint-v8) for the latest information.
[typescript-eslint](https://typescript-eslint.io) is the tooling that enables standard JavaScript tools such as [ESLint](https://eslint.org) and [Prettier](https://prettier.io) to support TypeScript code.
We&#x27;ve been working on a set of breaking changes and general features that we&#x27;re excited to get in front of users soon.
And now, we&#x27;re excited to say that typescript-eslint v8 is ready for public beta testing! 🎉
Our plan for typescript-eslint v8 is to:
- Have users try out betas starting in May of 2024
- Respond to user feedback for the next ~1-2 months
- Release a stable version within the next ~1-2 months
Nothing mentioned in this blog post is set in stone.
If you feel passionately about any of the choices we&#x27;ve made here — positively or negatively — then do let us know on [the typescript-eslint Discord](https://discord.gg/FSxKq8Tdyg)&#x27;s `#v8` channel!
**Tags:**- [breaking changes](/blog/tags/breaking-changes)- [typescript-eslint](/blog/tags/typescript-eslint)- [v7](/blog/tags/v-7)- [v8](/blog/tags/v-8)[**Read more**](/blog/announcing-typescript-eslint-v8-beta)## [Changes to `consistent-type-imports` with Legacy Decorators and Decorator Metadata
](/blog/changes-to-consistent-type-imports-with-decorators)March 25, 2024 · 7 min read[](https://github.com/bradzacher)[Brad Zacher](https://github.com/bradzacher)typescript-eslint MaintainerWe&#x27;ve made some changes to the [`consistent-type-imports` rule](/rules/consistent-type-imports) to fix some long-standing issues when used alongside `experimentalDecorators: true` and `emitDecoratorMetadata: true`. These changes increase safety and prevent invalid fixes when using decorator metadata.
**Tags:**- [consistent-type-imports](/blog/tags/consistent-type-imports)- [experimentalDecorators](/blog/tags/experimental-decorators)- [emitDecoratorMetadata](/blog/tags/emit-decorator-metadata)- [typescript-eslint](/blog/tags/typescript-eslint)[**Read more**](/blog/changes-to-consistent-type-imports-with-decorators)## [Announcing typescript-eslint v7
](/blog/announcing-typescript-eslint-v7)February 12, 2024 · 3 min read[](https://github.com/bradzacher)[Brad Zacher](https://github.com/bradzacher)typescript-eslint Maintainer[typescript-eslint](https://typescript-eslint.io) is the tooling that enables standard JavaScript tools such as [ESLint](https://eslint.org) and [Prettier](https://prettier.io) to support TypeScript code.
We&#x27;ve been working on infrastructure improvements that will help ensuring long-term interoperability with other tools in the ecosystem. In particular this major release tightens our dependency requirements to help set us up for ESLint v9 and includes a new package `typescript-eslint` providing full support for flat config files!
## Breaking Changes[​](#breaking-changes)
This is a small major release with just three breaking changes:
- Update Node.js engine requirement to `^18.18.0 || >=20.0.0`. This means we are dropping support for Node 16, 19, and Node 18 versions prior to `18.18.0`. Note that this is the same requirement that ESLint v9 will impose.
- Update the TypeScript peer dependency requirement to `>=4.7.4`.
- Update the ESLint peer dependency requirement to `^8.56.0`.
For most users this means that an upgrade from v6 should just look like this:
- npm- Yarn- pnpm```
npm i eslint typescript @typescript-eslint/parser @typescript-eslint/eslint-plugin**
``````
yarn add eslint typescript @typescript-eslint/parser @typescript-eslint/eslint-plugin
``````
pnpm add eslint typescript @typescript-eslint/parser @typescript-eslint/eslint-plugin
```Tags:**- [breaking changes](/blog/tags/breaking-changes)- [typescript-eslint](/blog/tags/typescript-eslint)- [v6](/blog/tags/v-6)- [v7](/blog/tags/v-7)- [flat configs](/blog/tags/flat-configs)[**Read more**](/blog/announcing-typescript-eslint-v7)## [Deprecating Formatting Rules
](/blog/deprecating-formatting-rules)December 25, 2023 · 2 min read[](https://github.com/JoshuaKGoldberg)[Josh Goldberg](https://github.com/JoshuaKGoldberg)typescript-eslint Maintainer[ESLint recently announced their plan to deprecate their core formatting rules](https://eslint.org/blog/2023/10/deprecating-formatting-rules).
The [ESLint Stylistic](https://eslint.style) project has taken over maintenance of formatting rules.
As a result, we in typescript-eslint are now able to deprecate our formatting rules as well.
We&#x27;ll keep these deprecated rules available until our next major version.
**Tags:**- [formatter](/blog/tags/formatter)- [formatting](/blog/tags/formatting)- [prettier](/blog/tags/prettier)- [style](/blog/tags/style)- [stylistic](/blog/tags/stylistic)[**Read more**](/blog/deprecating-formatting-rules)## [Relative TSConfig Projects with `parserOptions.project = true`
](/blog/parser-options-project-true)September 18, 2023 · 6 min read[](https://github.com/JoshuaKGoldberg)[Josh Goldberg](https://github.com/JoshuaKGoldberg)typescript-eslint Maintainer["Typed linting"](/getting-started/typed-linting), or enabling ESLint rules to tap into the power of the TypeScript type checker, is one of the best parts of typescript-eslint.
But enabling the type checker in repositories with multiple `tsconfig.json` files can be annoying to set up.
Even worse, specifying the wrong include paths could result in incorrect rule reports and/or unexpectedly slow lint times.
Improving the setup experience for typed lint rules has been a long-standing goal for typescript-eslint.
One long-standing feature request for that experience has been to support automatically detecting TSConfigs for developers.
We&#x27;re happy to say that we now support that by setting `parserOptions.project` equal to `true` in ESLint configurations.
This post will explain what life was like before, what&#x27;s changed, and what&#x27;s coming next. 🎉
**Tags:**- [parser](/blog/tags/parser)- [parser options](/blog/tags/parser-options)- [project](/blog/tags/project)- [tsconfig](/blog/tags/tsconfig)[**Read more**](/blog/parser-options-project-true)