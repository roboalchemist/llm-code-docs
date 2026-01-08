# Source: https://typescript-eslint.io/blog/tags/objects

# One post tagged with "objects"[View All Tags](/blog/tags)## [Revamping the `ban-types` rule
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
**Tags:**- [ban-types](/blog/tags/ban-types)- [interfaces](/blog/tags/interfaces)- [no-empty-object-type](/blog/tags/no-empty-object-type)- [no-restricted-types](/blog/tags/no-restricted-types)- [no-unsafe-function-type](/blog/tags/no-unsafe-function-type)- [no-wrapper-object-types](/blog/tags/no-wrapper-object-types)- [objects](/blog/tags/objects)[**Read more**](/blog/revamping-the-ban-types-rule)