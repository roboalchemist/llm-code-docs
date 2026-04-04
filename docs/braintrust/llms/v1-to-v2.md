# Source: https://braintrust.dev/docs/reference/sdks/typescript/migrations/v1-to-v2.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrate from v1.x to v2.x

> Guide for migrating from TypeScript SDK v1.x to v2.x

## What's changed

Starting in v2.0.0, [Zod](https://zod.dev) is now a **peer dependency** instead of a bundled dependency. This gives you control over the Zod version in your project and reduces bundle size if you're already using Zod.

The SDK requires **Zod v3.25.34 or later**.

## Migration steps

<Steps>
  <Step title="Install Zod">
    Add Zod v3.25.34+ to your project alongside the Braintrust SDK:

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      npm install zod@^3.25.34
      ```

      ```bash pnpm theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      pnpm add zod@^3.25.34
      ```

      ```bash yarn theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      yarn add zod@^3.25.34
      ```
    </CodeGroup>
  </Step>

  <Step title="Upgrade the SDK">
    <CodeGroup>
      ```bash npm theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      npm install braintrust@latest
      ```

      ```bash pnpm theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      pnpm add braintrust@latest
      ```

      ```bash yarn theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      yarn add braintrust@latest
      ```
    </CodeGroup>
  </Step>

  <Step title="Verify your setup">
    Run your build to ensure everything works:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    npm run build
    ```

    If you see any Zod-related type errors, ensure your Zod version is v3.25.34 or later.
  </Step>
</Steps>

## Troubleshooting

**"Cannot find module 'zod'"** — You need to install Zod as shown in Step 1.

**Type mismatches with Zod schemas** — If you're passing Zod schemas between your code and the Braintrust SDK, ensure you're using the same Zod version. Check for duplicate Zod installations:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
npm ls zod
```

<Note>
  If you encounter issues during migration, please [open an issue](https://github.com/braintrustdata/braintrust-sdk/issues) with details about your setup.
</Note>
