# Source: https://trigger.dev/docs/cli-switch.md

# CLI switch command

> The `trigger.dev switch` command can be used to switch between profiles.

Run the command like this:

<CodeGroup>
  ```bash npm theme={null}
  npx trigger.dev@latest switch [profile]
  ```

  ```bash pnpm theme={null}
  pnpm dlx trigger.dev@latest switch [profile]
  ```

  ```bash yarn theme={null}
  yarn dlx trigger.dev@latest switch [profile]
  ```
</CodeGroup>

It will switch to the specified profile. If no profile is specified, it will list all available profiles and run interactively.

## Arguments

```
npx trigger.dev@latest switch [profile]
```

<ParamField body="Profile" type="[profile]">
  The profile to switch to. If not specified, it will list all available profiles and run interactively.
</ParamField>
