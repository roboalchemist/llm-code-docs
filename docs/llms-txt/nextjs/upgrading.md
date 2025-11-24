# Source: https://nextjs.org/docs/pages/guides/upgrading.md

# Source: https://nextjs.org/docs/app/guides/upgrading.md

# Source: https://nextjs.org/docs/app/getting-started/upgrading.md

# Upgrading
@doc-version: 16.0.4


## Latest version

To update to the latest version of Next.js, you can use the `upgrade` command:

```bash filename="Terminal"
next upgrade
```

Next.js 15 and earlier do not support the `upgrade` command and need to use a separate package instead:

```bash filename="Terminal"
npx @next/codemod@canary upgrade latest
```

If you prefer to upgrade manually, install the latest Next.js and React versions:

```bash package="pnpm"
pnpm i next@latest react@latest react-dom@latest eslint-config-next@latest
```

```bash package="npm"
npm i next@latest react@latest react-dom@latest eslint-config-next@latest
```

```bash package="yarn"
yarn add next@latest react@latest react-dom@latest eslint-config-next@latest
```

```bash package="bun"
bun add next@latest react@latest react-dom@latest eslint-config-next@latest
```

## Canary version

To update to the latest canary, make sure you're on the latest version of Next.js and everything is working as expected. Then, run the following command:

```bash filename="Terminal"
npm i next@canary
```

### Features available in canary

The following features are currently available in canary:

**Authentication**:

* [`forbidden`](/docs/app/api-reference/functions/forbidden.md)
* [`unauthorized`](/docs/app/api-reference/functions/unauthorized.md)
* [`forbidden.js`](/docs/app/api-reference/file-conventions/forbidden.md)
* [`unauthorized.js`](/docs/app/api-reference/file-conventions/unauthorized.md)
* [`authInterrupts`](/docs/app/api-reference/config/next-config-js/authInterrupts.md)
## Version guides

See the version guides for in-depth upgrade instructions.

- [Version 16](/docs/app/guides/upgrading/version-16.md)
  - Upgrade your Next.js Application from Version 15 to 16.
- [Version 15](/docs/app/guides/upgrading/version-15.md)
  - Upgrade your Next.js Application from Version 14 to 15.
- [Version 14](/docs/app/guides/upgrading/version-14.md)
  - Upgrade your Next.js Application from Version 13 to 14.
