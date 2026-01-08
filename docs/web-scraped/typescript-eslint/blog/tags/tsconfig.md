# Source: https://typescript-eslint.io/blog/tags/tsconfig

# 2 posts tagged with "tsconfig"[View All Tags](/blog/tags)## [Typed Linting with Project Service
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
**Tags:**- [parser](/blog/tags/parser)- [parser options](/blog/tags/parser-options)- [project](/blog/tags/project)- [project service](/blog/tags/project-service)- [tsconfig](/blog/tags/tsconfig)[**Read more**](/blog/project-service)## [Relative TSConfig Projects with `parserOptions.project = true`
](/blog/parser-options-project-true)September 18, 2023 · 6 min read[](https://github.com/JoshuaKGoldberg)[Josh Goldberg](https://github.com/JoshuaKGoldberg)typescript-eslint Maintainer["Typed linting"](/getting-started/typed-linting), or enabling ESLint rules to tap into the power of the TypeScript type checker, is one of the best parts of typescript-eslint.
But enabling the type checker in repositories with multiple `tsconfig.json` files can be annoying to set up.
Even worse, specifying the wrong include paths could result in incorrect rule reports and/or unexpectedly slow lint times.
Improving the setup experience for typed lint rules has been a long-standing goal for typescript-eslint.
One long-standing feature request for that experience has been to support automatically detecting TSConfigs for developers.
We&#x27;re happy to say that we now support that by setting `parserOptions.project` equal to `true` in ESLint configurations.
This post will explain what life was like before, what&#x27;s changed, and what&#x27;s coming next. 🎉
**Tags:**- [parser](/blog/tags/parser)- [parser options](/blog/tags/parser-options)- [project](/blog/tags/project)- [tsconfig](/blog/tags/tsconfig)[**Read more**](/blog/parser-options-project-true)