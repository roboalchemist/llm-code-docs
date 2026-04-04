# Source: https://pipedream.com/docs/connect/api-reference/sdk-migration.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SDK Migration Guide

> Safely migrate from Pipedream's TypeScript SDK v1.x to v2.x

<Note>
  **The Pipedream SDK v2.x is now available with significant improvements.** While v1.x continues to be supported, we recommend upgrading to v2.x for new projects to take advantage of improved TypeScript support, new features, and ongoing updates.
</Note>

## Overview

The Pipedream SDK v2.x introduces significant improvements including:

* **Full TypeScript support** with comprehensive type definitions
* **Namespaced methods** for better organization (e.g., `client.actions.run()`)
* **Improved pagination support** for large data sets

## Migration Resources

For detailed migration instructions and examples, refer to the migration guide:

<Card title="Detailed migration guide" icon="github" href="https://github.com/PipedreamHQ/pipedream-sdk-typescript/blob/main/MIGRATE.md" horizontal>
  Step-by-step instructions, code examples, and migration strategies for upgrading from v1.x to v2.x
</Card>

## Key Breaking Changes

The migration guide covers these major breaking changes:

* **Client initialization**: New `PipedreamClient` class
* **Method namespacing**: Actions, accounts, and other methods are now namespaced

## Migration Support

If you encounter issues during migration:

1. Consult the [migration guide](https://github.com/PipedreamHQ/pipedream-sdk-typescript/blob/main/MIGRATE.md) for detailed examples
2. Check the [API / SDK documentation](/connect/api-reference/introduction) for v2.x usage patterns
3. Join our [community](https://pipedream.com/join-slack) for additional support

<Tip>
  The migration guide includes options for incremental migration, allowing you to upgrade your codebase gradually rather than all at once.
</Tip>

Built with [Mintlify](https://mintlify.com).
