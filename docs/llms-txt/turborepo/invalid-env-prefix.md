# Source: https://turborepo.dev/messages/invalid-env-prefix.md

---
title: Invalid environment variable prefix
description: Learn more about errors with invalid environment variable prefixes in Turborepo.
product: turborepo
type: troubleshooting
summary: How to fix the deprecated `$` prefix syntax when declaring environment variables in turbo.json.
related:

- /docs/reference/configuration
- /docs/reference/turbo-codemod

---

# Invalid environment variable prefix

Why this error occurred [#why-this-error-occurred]

When declaring environment variables in your `turbo.json`, you cannot prefix them with `$`. This
was an old syntax for declaring a dependency on an environment variable that was deprecated in Turborepo 1.5.

```json title="./turbo.json"
{
  "globalEnv": ["$MY_ENV_VAR"]
}
```

The environment variable declared above has the `$` prefix.

Solution [#solution]

Remove the `$` prefix from your environment variable declaration.

```json title="./turbo.json"
{
  "globalEnv": ["MY_ENV_VAR"]
}
```

You can migrate to the `env` and `globalEnv` keys using `npx @turbo/codemod migrate-env-var-dependencies`.
Check out [the codemod's documentation for more details](/docs/reference/turbo-codemod#turborepo-1x).

---

[View full sitemap](/sitemap.md)
