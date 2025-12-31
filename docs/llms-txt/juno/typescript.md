# Source: https://juno.build/docs/reference/functions/typescript.md

# Source: https://juno.build/docs/guides/typescript.md

# Source: https://juno.build/docs/examples/functions/typescript.md

# Source: https://juno.build/docs/build/functions/development/typescript.md

# TypeScript

This page covers advanced options for writing serverless functions in TypeScript.

---

## Maintenance

Since your project includes all Satellite features, it's essential to stay in sync with Junoâs updates to maintain compatibility.

Always check the [releases](https://github.com/junobuild/juno/releases) page for the latest changes, and update your local container image (source [repo](https://github.com/junobuild/juno-docker)) accordingly to ensure you're running the latest runtime and features.

**Caution:**

Always upgrade iteratively and avoid skipping version numbers. While we strive to minimize breaking changes, it's crucial to upgrade through each released version sequentially.

For example, if you're on **v0.0.23** and the latest release is **v0.0.26**, first upgrade to **v0.0.24**, then **v0.0.25**, and finally **v0.0.26**. Skipping versions could lead to unexpected issues.

---

## Versioning

When writing serverless functions in TypeScript, Juno uses the version defined in your projectâs `package.json`. This version is embedded into the compiled Wasm module and shown in the Juno Console, making it easier to keep track of deployments.

By default, the version is inherited from the root-level `version` field:

```
{  "name": "demo",  "version": "0.0.10"}
```

However, if you want to version your functions independently from your app or workspace, you can define a custom version field specifically for Juno Functions:

```
{  "name": "demo",  "version": "0.0.10",  "juno": {    "functions": {      "version": "0.0.4"    }  }}
```

This version is embedded into the compiled Wasm binary and displayed in the Juno Console. It helps you:

*   Track which version of your serverless logic is currently deployed.
*   Debug more effectively by matching behavior in the Console with specific code versions.
*   Move independently of Juno updates â you're in full control of your own function versioning.

You can use any versioning scheme that suits your development workflow (e.g. `0.1.0`, `1.0.0-beta`, `2025.04.18`...).